import sys
import unittest

from os.path import dirname, abspath, join

root_dir = dirname(dirname(abspath(__file__)))
sys.path.append(root_dir)

from gangagsoc.ganga_database.config import DBConfig
from gangagsoc.ganga_database.database import connect_to_db
from gangagsoc.ganga_database.config import DBConfig


class TestDatabaseConnection(unittest.TestCase):
    def test_config(self):
        getattr(DBConfig, "HOST")
        getattr(DBConfig, "PORT")
        getattr(DBConfig, "USER")
        getattr(DBConfig, "PASSWORD")
        getattr(DBConfig, "DBNAME")

    def test_connect_to_db(self):
        from sqlalchemy.engine import Engine

        engine = connect_to_db(DBConfig)

        assert isinstance(engine, Engine)
