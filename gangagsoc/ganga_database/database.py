import io

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import ganga.ganga
from ganga import *

from gangagsoc.ganga_database.config import DBConfig
from gangagsoc.ganga_database.models import Base, JobModel


def connect_to_db(db_config):
    """
    Connect to a MySQL database given a Config object.
    """
    HOST = getattr(db_config, "HOST")
    PORT = getattr(db_config, "PORT")
    USER = getattr(db_config, "USER")
    PASSWORD = getattr(db_config, "PASSWORD")
    DBNAME = getattr(db_config, "DBNAME")

    connection_string = f"mysql+mysqldb://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"
    engine = create_engine(connection_string)

    return engine


def create_job_data(job):
    """
    Return a bytes object of the string representation of a Job object.
    """
    s = io.StringIO()
    job._impl.printTree(s, "copyable")
    return s.getvalue().encode()


def create_job_from_data(job_data):
    """
    Create a job given the data in bytes format. To be used in complement with create_job_data(job).
    """
    job_string = job_data.decode()
    j = eval(job_string)
    return j
