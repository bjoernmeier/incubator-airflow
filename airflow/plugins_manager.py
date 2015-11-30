from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from builtins import object
import imp
import inspect
import logging
import os
import sys
from pkg_resources import iter_entry_points
from itertools import chain
merge = chain.from_iterable

from airflow import configuration

class AirflowPluginException(Exception):
    pass

class AirflowPlugin(object):
    name = None
    operators = []
    hooks = []
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = []
    menu_links = []

    @classmethod
    def validate(cls):
        if not cls.name:
            raise AirflowPluginException("Your plugin needs a name.")


entrypoint_group = configuration.get('core', 'entrypoint_group')
plugins_folder = configuration.get('core', 'plugins_folder')
if not plugins_folder:
    plugins_folder = configuration.get('core', 'airflow_home') + '/plugins'
plugins_folder = os.path.expanduser(plugins_folder)

if plugins_folder not in sys.path:
    sys.path.append(plugins_folder)

plugins = []
if not plugins:
    # Crawl through the plugins folder to find AirflowPlugin derivatives
    for root, dirs, files in os.walk(plugins_folder, followlinks=True):
        for f in files:
            try:
                filepath = os.path.join(root, f)
                if not os.path.isfile(filepath):
                    continue
                mod_name, file_ext = os.path.splitext(
                    os.path.split(filepath)[-1])
                if file_ext != '.py':
                    continue
                namespace = root.replace('/', '__') + '_' + mod_name
                m = imp.load_source(namespace, filepath)
                for obj in list(m.__dict__.values()):
                    if (
                            inspect.isclass(obj) and
                            issubclass(obj, AirflowPlugin) and
                            obj is not AirflowPlugin):
                        obj.validate()
                        if obj not in plugins:
                            plugins.append(obj)

            except Exception as e:
                logging.exception(e)
                logging.error('Failed to import plugin ' + filepath)

    # Allow for plugin classes also to be registered as entry points in packages
    for entry_point in iter_entry_points(group=entrypoint_group + '.plugins', name=None):
        dist = entry_point.dist
        try:
            obj = entry_point.load()
            if issubclass(obj, AirflowPlugin) and obj is not AirflowPlugin:
                obj.validate()
                if obj not in plugins:
                    plugins.append(obj)
        except Exception as e:
            logging.exception(e)
            logging.error('Failed to import plugin ' + entry_point.module_name)

operators = merge([p.operators for p in plugins])
hooks = merge([p.hooks for p in plugins])
executors = merge([p.executors for p in plugins])
macros = merge([p.macros for p in plugins])
admin_views = merge([p.admin_views for p in plugins])
flask_blueprints = merge([p.flask_blueprints for p in plugins])
menu_links = merge([p.menu_links for p in plugins])
