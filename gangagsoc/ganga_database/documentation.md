# Documentation
The code is split up into the following files:

  * [models.py]()
  * [database.py]()
  * [config.py]()
  * [demonstration.py]()

The following sections will explain the contents of each of the above files. 

## [models.py]()
  The JobModel object describes the database schema for storing a Job in the database using the SQLAlchemy ORM. 

  | Field | Type    | Key     |
  |-------|---------|---------|
  | id    | Integer | Primary |
  | name  | String  |         |
  | data  | BLOB    |         |

## [database.py]()
  This file contains all the functions related to the database.

#### connect_to_db(db_config)

  Given a `DBConfig` object, connects to the database and returns a SQLAlchemy `engine`. 

#### create_job_data(job)

  Takes a job object and returns a string encoded into bytes containing the representation of the job. This function makes use of the `printTree` method of the Job.

  Note: I tried using both `full_print(job, interactive=False)` and `full_print(job, interactive=True)` for this purpose but the returned output could not be passed to `eval()` to reconstruct the job. So I did some digging and found this method.

#### create_job_from_data(job_data)

  Takes a bytes object, decodes it and passes into the eval() function to return a Job.


