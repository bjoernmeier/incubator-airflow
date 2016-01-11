from airflow.plugins_manager import AirflowPlugin

class AirflowTestPlugin(AirflowPlugin):
    name = "AirflowTestPlugin"
    operators = []
    hooks = []
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = []
    menu_links = []


class AirflowAnotherTestPlugin(AirflowPlugin):
    name = "AirflowAnotherTestPlugin"
    operators = []
    hooks = []
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = []
    menu_links = []