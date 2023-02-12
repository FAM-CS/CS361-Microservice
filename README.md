# CS361-Gradebook Microservice
Gradebook API for getting and making csv files

## Gradebook API Contract
Currently API will have to run locally for the server and have a gradebook folder with csv
files. The csv file will contain a header "date,gpa" and the next lines will contain the date and gpa data.
```
data,gpa
yyyy-mm-dd,float
```
### Setup
Before you run the API, run `source .env` to fill env variables:
```
PORT = ...
API_KEY = ...
GRADE_FOLDER = ...
```
*NOTE: api keys are not used, if added it's a "dummy" one*


Install needed python libraries:
```
pip install -r requirements.txt
```

### Run
```
node gradebookService.js
```
To stop, hit `ctrl+C` or `cmd+C` (keyboard interrupt)

### Requests
- **GET** /files
    - Returns string of csv gradebook files separated by a comma

- **GET** /files/:file
    - Returns contents of specified csv file as a string

- **POST** /files/:file/new   json = {"header": "data,gpa\n", "grades": "yyyy-mm-dd,gpa\n"}
    - Create new csv file with specified grades

- **POST** /files/:file/add   json = {"grades": "yyyy-mm-dd,gpa\n"}
    - Append new grades to an existing gradebook
