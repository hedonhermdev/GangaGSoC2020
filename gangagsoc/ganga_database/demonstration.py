import os

os.chdir("../initial")

from gangagsoc.ganga_database.database import *
from gangagsoc.initial.ganga_job_splitter import split_job

# Create a database connection.
engine = connect_to_db(DBConfig)
session = Session(engine)

# Drop all tables and create new tables for the database.
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Create a monitoring loop to wait for the job to complete.
runMonitoring()

# Create an instance of the JobModel to save the Job.
id = split_job.id
name = split_job.name
job_data = create_job_data(split_job)
job_db = JobModel(id=id, name=name, data=job_data)

# Add the job to the session and commit the session.
session.add(job_db)
session.commit()

# Query the database for our job.
queried_job = session.query(JobModel).filter(JobModel.id == id).one()

# Get data from the query.
data = queried_job.data

# Create a new job from the queried data.
new_job = create_job_from_data(data)
new_job.name = name + " copy"
new_job.submit()

# Create a monitoring loop to wait for the job to complete.
runMonitoring()
