//RUN IN COMMAND PROMPT: node C:\NodeJS\Exam1\2_FileServer.js
var http = require('http');	//The built-in HTTP Module
//Node.js as a File Server
var fs = require('fs');

http.createServer(function (req, res) {
	fs.readFile('demofile1.html', function(err, data) {
		//Add an HTTP Header
		res.writeHead(200, {'Content-Type': 'text/html'});
		res.write(data);
		res.end();	//end the response
	});
}).listen(8080);	//the server object listens on port 8080