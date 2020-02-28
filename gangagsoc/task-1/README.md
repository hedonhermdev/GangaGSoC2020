# Ganga Initial Task

### Hello World
  Run the [hello_world.py](./hello_world.py) file to see a demonstration of a simple job. 

   `python hello_world.py`


### Demonstrating the Arg Splitter

  * Splitting the PDF ([pdf_split.py](./pdf_split.py)): 

    `$ python pdf_split.py`

  * The [count_occurences.py](./count_occurences.py) file counts the number of occurences of the word 'the' in PDF file. This file is used by the job. This file can be used as:

    `$ python count_occurences.py <filename>.pdf`

  * Making a job and splitting it into subjobs ([ganga_job_splitter.py](./ganga_job_splitter.py)): 

    `$ python ganga_job_splitter.py`

  * The total count of all occurrences of the word 'the' is stored in a file named 'stdout'. Print the file to get the result:
    `$ cat stdout` 

### Testing the Code
  The tests are written in the `test` folder. To run the tests:
  
    `$ pytest test/`

Note: The ganga namespace is imported in both files. So it is perfectly fine to run the file withe python interpreter. 
