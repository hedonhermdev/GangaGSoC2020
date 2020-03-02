# The total sum of the count in each page turns out to be 350. 
# In this test we verify that number. 

import os

def test_occurences():
    os.system("python3 pdf_split.py")
    assert os.path.exists('./cern-pages')

    num_pages = len(os.listdir('./cern-pages'))
    assert num_pages == 12

    os.system("python3 ganga_job_splitter.py")

    assert os.path.exists('stdout')

    output = open('stdout')
    assert output.read().strip() == '350'




