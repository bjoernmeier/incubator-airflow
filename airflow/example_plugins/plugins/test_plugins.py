from flask import Blueprint

from airflow.plugins_manager import AirflowPlugin


bp = Blueprint("test_plugin", __name__, static_url_path='/')


class AirflowTestPlugin(AirflowPlugin):
    name = "AirflowTestPlugin"
    operators = []
    hooks = []
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = [bp]
    menu_links = []


class AirflowAnotherTestPlugin(AirflowPlugin):
    name = "AirflowAnotherTestPlugin"
    operators = []
    hooks = []
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = [bp]
    menu_links = []
