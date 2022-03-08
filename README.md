# API Automation Task 
API automation that:
- verifies country codes of European capitals, listed in test_data.py are valid,
using soft asserts
- validates temperature of all listed capitals is within the valid for the continent range
- html reports are generated in project root and can be opened 


# Getting started
Run the command to get required packages in terminal
   
     $ pip install -r requirements.txt

# How to execute
To execute tests run in terminal and generate reports run
    
    $ pytest --html=report.html --self-contained-html


 
