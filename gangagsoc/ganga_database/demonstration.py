import os

os.chdir("../initial")

from sqlalchemy.orm import Session
import ganga

from gangagsoc.ganga_database import database as db
from gangagsoc.ganga_database import models
from gangagsoc.ganga_database.config import DBConfig
from gangagsoc.initial.ganga_job_splitter import split_job

# Create a db connection.
engine = db.connect_to_db(DBConfig)
session = db.GangaDBSession(engine)

# Drop all tables and create new tables for the db.
models.Base.metadata.drop_all(engine)
models.Base.metadata.create_all(engine)

# Create an instance of the JobModel to save the Job.
id = split_job.id
name = split_job.name
job_data = db.create_job_data(split_job)
job_db = models.JobModel(id=id, name=name, data=job_data)
print(f"Job Saved to database - {job_db.id} - {job_db.name}")

# Add the job to the session and commit the session.
session.add(job_db)
session.commit()

new_job = session.get_job_from_db(job_id=id)

print(f"Job queried from db - {new_job.id} - {new_job.name}")

