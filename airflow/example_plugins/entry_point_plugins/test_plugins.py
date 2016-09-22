from flask import Blueprint

from airflow.plugins_manager import AirflowPlugin


bp = Blueprint("test_plugin", __name__, static_url_path='/')


class EntryPointTestPlugin(AirflowPlugin):
    name = "EntryPointTestPlugin"
    operators = []
    hooks = []
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = [bp]
    menu_links = []


class AnotherEntryPointTestPlugin(AirflowPlugin):
    name = "AnotherEntryPointTestPlugin"
    operators = []
    hooks = []
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = [bp]
    menu_links = []
