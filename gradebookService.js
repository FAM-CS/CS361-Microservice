/*********************************************************************
 ** Global variables
 *********************************************************************/
// var path = require('path');
var express = require("express")
//
var app = express()
var port = process.env.PORT || 3000;

// Set express app server to listen to a port, default is 3000
app.listen(port, function () {
    console.log("== Server is listening on port: ", port)
})


/*********************************************************************
 ** Function: (Logger)
 ** Description:
 **     Logging request information
 ** Parameters: req, res, next
 *********************************************************************/
 app.use(function (req, res, next) {
    console.log("=== Request recieved ===")
    console.log("method: ", req.method)
    console.log("url: ", req.url)
    console.log("headers: ", req.headers)

    next()		// Go to next middleware function
})


/*********************************************************************
 ** Function: HTTP GET HANDLE
 ** Description: Handle get request for sendMsg page
 ** Parameters: req, res, next
 *********************************************************************/
app.get("/sendMsg",function (req, res, next) {
    res.status(200).send("A message from CS361")
})


/*********************************************************************
 ** Function: HTTP GET HANDLE
 ** Description: Handle get request for unknown cases (404 error)
 ** Parameters: req, res, next
 *********************************************************************/
app.get("*", function (req, res, next) {
    res.status(404).send("404: Error :(")
})