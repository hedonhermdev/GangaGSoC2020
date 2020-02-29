import ganga.ganga
from ganga import Job, Local, runMonitoring

# Create a new job. 
j = Job(name='Simple Hello World')
j.backend = Local()

# Submit the job.
j.submit()

runMonitoring()
print("Job Status:", j.status)

# Print the stdout output of the job. 
output = j.peek('stdout', 'more')
print(output)
