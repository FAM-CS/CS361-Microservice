//~To start this server, run "npm run start"
//~Run "npm install" before to get all node mod dependencies

/* Sources:
 * https://blog.logrocket.com/understanding-api-key-authentication-node-js/
 * https://blog.hubspot.com/website/what-is-rest-api
 */

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
    console.log("path: ", req.path)
    console.log("query: ", req.query)
    console.log("params: ", req.params)
    console.log("body: ", req.body)

    next()		// Go to next middleware function
})


/*********************************************************************
 ** Function: HTTP GET HANDLE
 ** Description: Handle get request for sendMsg page
 ** Parameters: req, res, next
 *********************************************************************/
app.get("/files",function (req, res, next) {
    // !req.param@deprecated
    // since 4.11 Use either req.params, req.body or req.query, as applicable.
    //
    // Return the value of param name when present or defaultValue.
    //
    // Checks route placeholders, ex: /user/:id
    // Checks body params, ex: id=12, {"id":12}
    // Checks query string params, ex: ?id=12
    // To utilize request bodies, req.body should be an object. This can be done by using the connect.bodyParser() middleware.
    console.log("req.query: ", req.query['api_key'])
    res.status(200).send("A message from CS361")
})

/*********************************************************************
 ** Function: HTTP GET HANDLE
 ** Description: Handle get request for sendMsg page
 ** Parameters: req, res, next
 *********************************************************************/
 app.get("/sendMsg/:misc",function (req, res, next) {
    // console.log("req.params: ", req.params)             // for route placeholders: /user/:id
    // console.log("req.query: ", req.query)               // for body params, ex: id=12, {"id":12}
    res.status(200).send("A SECRET message from CS361")
})


/*********************************************************************
 ** Function: HTTP GET HANDLE
 ** Description: Handle get request for unknown cases (404 error)
 ** Parameters: req, res, next
 *********************************************************************/
app.get("*", function (req, res, next) {
    res.status(404).send("404: Error :(")
})