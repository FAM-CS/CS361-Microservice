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
NOTE: not using api keys atm, if used it's a "dummy" one

### Run
```
node gradebookService.js
```
To stop, hit `ctrl+C` or `cmd+C` (keyboard interrupt)

### Requests

GET /files