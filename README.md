# CS361-Microservice
Gradebook API for getting csv files (and potentially making)

## Gradebook API Contract
Currently API will have to run locally for the server and have a gradebook folder with csv
files. The csv file will contain a header "date,gpa" and the next lines will contain the date.
```
data,gpa
yyyy-mm-dd,float
```
### Setup
Before you run the API, run "source .env" to fill:
```
PORT = ...
API_KEY = ...
```
Also do:
```
pip install -r requirements.txt
```
**NOTE**: api keys are not used, if added it's a "dummy" one

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

- **POST** /files/:file/new
```
json = {"header": "data,gpa\n", "grades": "yyyy-mm-dd,gpa\n"}
```
    - Create new csv file with specified grades

- **POST** /files/:file/add
```
json = {"grades": "yyyy-mm-dd,gpa\n"}
```
    - Append new grades to an existing gradebook
