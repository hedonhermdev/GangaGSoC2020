# Ganga GSoC 2020 Challenge

## Project Structure
    gangagsoc
    ├── __init__.py
    ├── ganga_database (# Persistent Storage Task #)
    │   ├── README.md
    │   ├── __init__.py
    │   ├── config.py
    │   ├── database.py
    │   ├── demonstration.py
    │   ├── documentation.md
    │   ├── models.py
    │   ├── performance.py
    │   └── test
    │       ├── __init__.py
    │       └── test_database.py
    └── initial (# Initial Task #)
        ├── README.md
        ├── count_occurences.py
        ├── ganga_job_splitter.py
        ├── hello_world.py
        ├── pdf_split.py
        ├── stdout
        ├── sum_merger.py
        └── test
            └── test_count_occurences.py

  The 3 parts of the challenge are implemented in directories (python packages) inside the `gangagsoc` directory. Each task has its own `README.md` and/or `DOCUMENTATION.md`


## Initial Task

  * [README.md](./gangagsoc/initial/README.md)

  For this task, I wrote a script to use Python's PyPDF2 library to split the given CERN.pdf into 12 pages and store them inside a directory called `cern-pages`. Then I wrote another script that used the `textract` library to extract text from a PDF file and count occurences of a word in the text. I tried using `PyPDF2` for the text extraction job but it failed to work with a few pages so I switched to `textract`. 


## Persistent Storage Task 

  * [README.md](./gangagsoc/ganga_database/README.md)
  * [DOCUMENTATION.md](./gangagsoc/ganga_database/documentation.md)

  For this task, I chose `MysSQL` as my database engine and used the `SQLAlchemy ORM` to create a database structure that can be used to save all data about a job in a reproducible format. To demonstrate this, I used the job created in the initial task and saved it in the database. Next, I queried the database for this task and reproduced the task as a new task.

