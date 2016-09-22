import unittest

from airflow.example_plugins.plugins.test_plugins import (
    AirflowTestPlugin, AirflowAnotherTestPlugin
)
from airflow.example_plugins.entry_point_plugins.test_plugins import (
    EntryPointTestPlugin,
)


class TestEntryPointPlugins(unittest.TestCase):

    def test_load_entry_point_plugins(self):
        import airflow.configuration
        airflow.configuration.load_test_config()

        import airflow.plugins_manager

        expected = [AirflowAnotherTestPlugin.__name__, AirflowTestPlugin.__name__,
                    EntryPointTestPlugin.__name__]
        self.assertListEqual([p.name for p in airflow.plugins_manager.plugins],
                             expected)
