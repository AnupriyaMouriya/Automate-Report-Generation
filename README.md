##IPS AMGEN REPORT AUTOMATION


###STEPS FOR SCRIPT EXECUTION

1. Install python and set the python path to system environment variable.
2. Check if python is installed successfully. Open cmd line and type:
```
some\path\> python --version
```
3. Clone the repository.
4. Go to the script path.
```
some\path\> cd pythonProject
```
5. Open main.py file.
6. Provide the required inputs
```
    a. result file name
    b. result file path
    c. path of aggregate report name
    d. values (unique script tag)
```
7. Save it and run the script
8. The result csv file will be saved in the provided result file path.


###PREREQUISITE

1. Jmeter aggregate report should be in csv format(no fomrmatting needed at all)
2. Each script should have a unique tag prefixed with the transaction name to differentiate from others.
3. Make sure the column extracted in the script is same as required.

###WEBSITE FOR REFERENCE
1. Steps to setup python on windows - https://phoenixnap.com/kb/how-to-install-python-3-windows 
2.python install - https://www.python.org/downloads/windows/


#####---------Thank you----------- 
#####Author - Anupriya Mouriya
