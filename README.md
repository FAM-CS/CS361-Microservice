# CS361-Gradebook Microservice
Gradebook API for getting and making csv files. Also contains a demo on how to use it
with python (3.10)[^1] requests library.

## Gradebook API Contract
Currently API will have to run locally for the _server_ and have a _gradebook folder_ with csv files.
The csv file will contain a header "date,gpa" and the next lines will contain the date and gpa data.
There is no enforcement on the types/format of the date and gpa values.
```
date,gpa
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
npm run start
```
To stop, hit `ctrl+C` or `cmd+C` (keyboard interrupt)

### Requests & Responses
**NOTE**: Anything in {} is meant to be replaced with the corresponding value, :name are parameters


**baseURL** = "http://localhost:{PORT}"

- **GET** /files
    - Returns string of csv gradebook files separated by a comma
    - Python example:
        - response = requests.get(baseURL + /files)
        - files = response.text

- **GET** /files/:file
    - Returns contents of specified csv file as a string
    - Python example:
        - response = requests.get(baseURL + "/files/{file}")
        - csv_string = response.text

- **POST** /files/:file/new
    - Create new csv file with specified grades
    - Python example:
        - data = {"header": "data,gpa\n", "grades": "yyyy-mm-dd,gpa\n"}
        - response = requests.post(baseURL + "/files/{file}/new", json = data)
        - response is a status code and simple message (OK=200, ERR=500)

- **POST** /files/:file/add
    - Append new grades to an existing gradebook
    - Python example:
        - data = {"grades": "yyyy-mm-dd,gpa\n"}
        - response = requests.post(baseURL + "/files/{file}/add", json = data)
        - response is a status code and simple message (OK=200, ERR=500)

[^1]: I believe it is compatible with most python3 versions
