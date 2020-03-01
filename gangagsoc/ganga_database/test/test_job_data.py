# Test to demonstrate that the create_job_data and create_job_from_data functions can work as complements of each other.
import sys
import unittest

from os.path import dirname, abspath, join

root_dir = dirname(dirname(abspath(__file__)))
sys.path.append(root_dir)

from gangagsoc.ganga_database.database import create_job_data, create_job_from_data
from ganga import Job


class TestJobData(unittest.TestCase):
    def test_create_job_data(self):
        j = Job()
        data = create_job_data(j)
        print(data)
        assert isinstance(data, bytes)

    def test_create_job_from_data(self):
        job_data = "Job()".encode()  # Simple job data.
        job = create_job_from_data(job_data)
        assert isinstance(job, Job)
