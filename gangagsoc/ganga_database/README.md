# Database Task
  The project demonstrates the following:
    
    1. Setting up a MySQL server and creating a database. 
    2. Connecting to the MySQL server from Python using SQLAlchemy. 
    3. Creating a database model to store a Ganga Job object in the database. 
    4. Exporting the Job data to a bytes object which can be stored as a blob in the database. 
    5. Querying the database to retreive a previously stored job in the database and creating a new job from the blob data of retreived job. 


## Setting Up the Database

  * Install Docker on your machine. Instructions can be found [here](https://docs.docker.com/install/) depending on your system. 

  * Go to the `db-docker` directory in the root folder. And start the docker container for the MySQL server. 
      ```bash
      $ cd ../../db-docker
      $ docker-compose up -d # The -d flag detaches the container so that the MySQL server runs in the background. 

      ```

## Demonstration
  Run the [demonstration.py](./demonstration.py) file to see a demo. 
  The script creates a Job which does the task described in the initial task and saves it to the database. It then queries the database for a job with the id of the previous job. Using the data stored in that job, it creates another Job which can reproduce the task. 
  ```bash
    $ python demonstration.py
  ```


## Tests
Running the Tests
All tests reside in the test folder. To run the tests with pytest:

```
  $ pytest test/
```

## Performance
  For measuring performance, use the [performance.py](./performance.py) script. It uses the Python time module to separately measure the execution time for Querying the Database and Recreating the Job from the data. Sample output of the script is shown below: 

    Querying the database:
    - Number of calls: 1000
    - Total time taken: 0.8227760791778564 miliseconds
    - Time per call: 0.0008227760791778564 miliseconds
    Creating a job from the data:
    - Number of calls: 1000
    - Total time taken: 26235.963821411133 miliseconds
    - Time per call: 26.235963821411133 miliseconds

## Documentation
The code is well documented with the use of comments and docstrings. An overview of the code can be found in [documentation.md](./documentation.md)
