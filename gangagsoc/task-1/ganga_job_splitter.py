import os
import time

import ganga.ganga
from ganga import Job, Executable, ArgSplitter, GangaDataset, LocalFile, CustomMerger, runMonitoring, jobs

# List all PDF files in the cern-pages directory.
pdf_files = os.listdir('./cern-pages/')

# Create a new job
j = Job(name='Count Word Occurences ')

# Set the job application as python3.
j.application = Executable()
j.application.exe = 'python3'

# Give the python script and the PDF files as input to the job.
j.inputfiles = [LocalFile('count_occurences.py'), LocalFile('cern-pages/*.pdf')]

# Split the jobs into subjobs, one for each PDF file.
j.splitter = ArgSplitter()
j.splitter.args = [['count_occurences.py', filename] for i, filename in enumerate(pdf_files, start=1)]

# Submit the job.
j.submit()

# Start monitoring loop with 2 steps to wait for the job to completed.
runMonitoring(steps=2, jobs=jobs[-1:])

# To count the total number of occurences, we define a custom merger (defined in file sum_merger.py) which takes the sum of the count in the output file of each subjob. 
merger = CustomMerger(files=['stdout'], module='./sum_merger.py', overwrite=True)

# If the job has submitted, merge the outputs.
if j.status == 'completed':
    merger.merge(j, outputdir='./')

