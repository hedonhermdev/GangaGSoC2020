import io

import ganga.ganga
from ganga import *

import ring

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from gangagsoc.ganga_database import models
from gangagsoc.ganga_database.config import DBConfig


def connect_to_db(db_config):
    """
    Connect to a MySQL database given a Config object.
    """
    HOST = getattr(db_config, "HOST")
    PORT = getattr(db_config, "PORT")
    USER = getattr(db_config, "USER")
    PASSWORD = getattr(db_config, "PASSWORD")
    DBNAME = getattr(db_config, "DBNAME")

    connection_string = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"
    engine = create_engine(connection_string)

    return engine


class GangaDBSession(Session):
    @ring.lru()
    def get_job_from_db(self, job_id):
        queried_job = self.query(models.JobModel).get(job_id)
        data = queried_job.data
        job = create_job_from_data(data)
        return job

    def save_job(self, id, name, data):
        j = models.JobModel(id=id, name=name, data=data)
        self.add(j)
        self.commit()

    @ring.lru()
    def query_job_by_id(self, job_id):
        j = self.query(models.JobModel).get(job_id)
        return j

    @ring.lru()
    def query_job_by_name(self, job_name):
        j = self.query(models.JobModel).get(name=job_name)
        return j

    def __ring_key__(self):
        return ""



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
