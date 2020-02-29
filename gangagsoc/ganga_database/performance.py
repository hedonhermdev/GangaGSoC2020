import time
from sqlalchemy.orm import Session

from gangagsoc.ganga_database.database import (
    connect_to_db,
    create_job_data,
    create_job_from_data,
)
from gangagsoc.ganga_database.config import DBConfig
from gangagsoc.ganga_database.models import JobModel
from ganga import Job, Local, Executable, jobs


engine = connect_to_db(DBConfig)

session = Session(engine)

job = Job()

blob = create_job_data(job)

JobInstance = JobModel(id=job.id, name=job.name, data=blob)

outfile = open('performance.log', 'w')


session.add(JobInstance)
session.commit()


n_calls = 1000

t0 = time.time()
for _ in range(1000):
    queried_job = session.query(JobModel).filter(JobModel.id == job.id).one()

time_taken = time.time() - t0

outfile.write("Querying the database:\n")
outfile.write(f"- Number of calls: {n_calls}\n")
outfile.write(f"- Total time taken: {time_taken} miliseconds\n")
outfile.write(f"- Time per call: {time_taken/n_calls} miliseconds\n")


t0 = time.time()
for _ in range(1000):
    new_job = create_job_from_data(queried_job.data)
time_taken = (time.time() - t0) * 1000


outfile.write("Creating a job from the data:\n")
outfile.write(f"- Number of calls: {n_calls}\n")
outfile.write(f"- Total time taken: {time_taken} miliseconds\n")
outfile.write(f"- Time per call: {time_taken/n_calls} miliseconds\n")


# Cleanup
job.remove()
first_job_id = queried_job.id + 1
for i in range(first_job_id, first_job_id+1000):
    jobs(i).remove()


