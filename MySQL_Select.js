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
/*
  //CREATE DATABASE
  con.query("CREATE DATABASE mynodedb", function (err, result) {
    if (err) throw err;
    console.log("Database created");
  });
  
  //CREATE TABLE
  var sql = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))";
  con.query(sql, function (err, result) {
	if (err) throw err;
	console.log("Table created");
  });
  
  //INSERT RECORD
  var sql = "INSERT INTO customers (name, address) VALUES ('Company Inc', 'Highway 37')";
  con.query(sql, function (err, result) {
	if (err) throw err;
	console.log("1 record inserted, ID:" + result.insertId);
  });
  
  //Insert Multiple Records
  var sql = "INSERT INTO customers (name, address) VALUES ?";
  var values = [
    ['John', 'Highway 71'],
    ['Peter', 'Lowstreet 4'],
    ['Amy', 'Apple st 652'],
    ['Hannah', 'Mountain 21'],
    ['Michael', 'Valley 345'],
    ['Sandy', 'Ocean blvd 2'],
    ['Betty', 'Green Grass 1'],
    ['Richard', 'Sky st 331'],
    ['Susan', 'One way 98'],
    ['Vicky', 'Yellow Garden 2'],
    ['Ben', 'Park Lane 38'],
    ['William', 'Central st 954'],
    ['Chuck', 'Main Road 989'],
    ['Viola', 'Sideway 1633']
  ];
  con.query(sql, [values], function (err, result) {
    if (err) throw err;
    console.log("Number of records inserted: " + result.affectedRows);
  });
*/	
	//Select all 
	con.query("SELECT * FROM customers", function (err, result) {
		if (err) throw err;
		for(var i=0; i<result.length; i++) {
			result_name.push((result[i].name).toString());
			result_address.push((result[i].address).toString());
		}
		console.log(result);
	});
	//Select column
	con.query("SELECT name,address FROM customers", function (err, result) {
		if (err) throw err;
		console.log(result);
		console.log("Loc 1 record: "+result[2].address);
	});
	//Select fields
	con.query("SELECT name, address FROM customers", function (err, result, fields) {
		if (err) throw err;
		console.log(fields);
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