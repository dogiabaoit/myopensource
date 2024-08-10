//RUN IN COMMAND PROMPT: node C:\NodeJS\Exam1\1_start.js
var http = require('http');	//The built-in HTTP Module
var dt = require('./mymodule');
var url = require('url');	//Split the Query String

//Node.js as a File Server
var fs = require('fs');

http.createServer(function (req, res) {
	//Add an HTTP Header
	res.writeHead(200, {'Content-Type': 'text/html'});
	res.write("The date and time are currently: "+ dt.myDateTime());	//write a response to the client
	//res.write(req.url);
	var q = url.parse(req.url, true).query;
	var txt = q.year + " " + q.month;	//http://localhost:8080/?year=2017&month=July
	res.write("<br>"); 
	res.end(txt);	//end the response
}).listen(8080);	//the server object listens on port 8080