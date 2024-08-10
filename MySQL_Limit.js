//INSTALL: C:\Users\Your Name>npm install mysql 
//run: C:\NodeJS\Exam2>node MySQL_Select.js
var mysql = require('mysql');
var http = require('http');
var result_name = [];
var result_address = [];

var con = mysql.createConnection({
  host: "localhost",
  user: "admin",
  password: "123456",
  database: "mynodedb"
});

con.connect(function(err) {
	if (err) throw err;
	console.log("Connected!");
	//Select all 
	con.query("SELECT * FROM customers ORDER BY name DESC LIMIT 5", function (err, result) {
		if (err) throw err;
		for(var i=0; i<result.length; i++) {
			result_name.push((result[i].name).toString());
			result_address.push((result[i].address).toString());
		}
		console.log(result);
	});
	
	//Limit 5, tinh tu record thu 2 -> 7
	con.query("SELECT * FROM customers ORDER BY name DESC LIMIT 5 OFFSET 2", function (err, result) {
		if (err) throw err;
		console.log(result);
	});
	
	var sql = "SELECT * FROM customers ORDER BY name DESC LIMIT 2, 5";
	con.query(sql, function (err, result) {
		if (err) throw err;
		console.log(result);
	});
});

http.createServer(function (req, res) {
	//Add an HTTP Header
	res.writeHead(200, {'Content-Type': 'text/html'});
	res.write("<html><body>");
	res.write("<table border='1'>");
	var i = 0;
	result_name.forEach(function(item, index, array){
		res.write("<tr>");
		res.write("<td>"+ (i+1) +"</td>");
		res.write("<td>"+item +"</td><td>"+result_address[i]+"</td>");
		res.write("</tr>");
		i++;
	});
	res.write("</table>");
	res.write("</body></html>");
	res.end();	//end the response
}).listen(8080);	//the server object listens on port 8080