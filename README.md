# Example Whetstone API pull - Python
## 2018-06-14
With the files in this folder and a Python installation, you can pull all data from the 'kipp-hs' Whetstone instance.

### Files
1) whetstone.py contains the Whetstone class object that autenticates your credentials and handles GET requests.
2) pull_all_endpoints.py loops through all /api/v2 endpoints (as of 2018-06-14) and outputs results for each endpoint as a JSON file.
3) run.bat is a Windows powershell script that initializes the "pull_all_endpoints.py" script and writes a log of the results.
3) run.sh is a script for Mac users that initializes the "pull..." python script
4) observation-report.twb is a Tableau report that can be directly connected to the "data/observations.json" file.
5) requirements.txt is a log of all Python dependencies (irrelevant if Python is installed by directions below)

    NOTE: The scripts will only run if they are not moved from this directory (folder). Don't move or make a shortcut to this file.

### Installing Python
1) Download Python 3.6 from Anaconda (https://www.anaconda.com/download/)
2) Install Anaconda
    - Select "Just Me"
    - Copy path to destination folder (will use later)

### Run on Windows
1) Open .bat file in Notepad. Replace path with destination folder (C:\users\\[your account]\AppData\Local\Continuum\anaconda3) and save.
4) Replace the instance and api key in the "private\credentials.json" file with your own.
    - Instance is what comes before ".whetstone.com" in your address bar
    - API key can be found by accessing "My Settings"
2) Double click .bat file to run
3) Open the log.txt file to ensure that data was successfully pulled.


### Run on Mac OS
1) Open Terminal
2) Change directory to the location of the python folder (something like, "cd ~/Desktop/whetstone-api/python")
3) Run shell script by typing "sh run.sh"
4) Open the log.txt file to ensure that data was successfully pulled.
