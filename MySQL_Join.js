//INSTALL: C:\Users\Your Name>npm install mysql 
//run: C:\NodeJS\Exam2>node MySQL_Select.js
var mysql = require('mysql');

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
	//CREATE USERS Table
	var sql = "CREATE TABLE users (id int(10), name VARCHAR(255), favorite_product int(10))";
	con.query(sql, function (err, result) {
		if (err) throw err;
		console.log("Table users created");
	});
	//CREATE PRODUCTS Table
	var sql = "CREATE TABLE products (id int(10), name VARCHAR(255))";
	con.query(sql, function (err, result) {
		if (err) throw err;
		console.log("Table products created");
	});
	
	//Insert Multiple Records of Users
	var sql = "INSERT INTO users (id, name, favorite_product) VALUES ?";
	var values = [
		[1,'John', 154],
		[2,'Peter', 154],
		[3,'Amy', 155],
		[4,'Hannah', 0],
		[5,'Michael', 0],
	];
	con.query(sql, [values], function (err, result) {
		if (err) throw err;
		console.log("Number of records inserted: " + result.affectedRows);
	});
	//Insert Multiple Records of Products
	var sql = "INSERT INTO products (id, name) VALUES ?";
	var values = [
		[154,'Chocolate Heaven'],
		[155,'Tasty Lemons'],
		[156,'Vanilla Dreams'],
	];
	con.query(sql, [values], function (err, result) {
		if (err) throw err;
		console.log("Number of records inserted: " + result.affectedRows);
	});
*/	
	//Inner join
	var sql = "SELECT users.name AS user, products.name AS favorite FROM users JOIN products ON users.favorite_product = products.id";
	con.query(sql, function (err, result) {
		if (err) throw err;
		console.log(result);
	});
	
	//Left join
	var sql = "SELECT users.name AS user, products.name AS favorite FROM users LEFT JOIN products ON users.favorite_product = products.id";
	con.query(sql, function (err, result) {
		if (err) throw err;
		console.log(result);
	});
	
	//Right join
	var sql = "SELECT users.name AS user, products.name AS favorite FROM users RIGHT JOIN products ON users.favorite_product = products.id";
	con.query(sql, function (err, result) {
		if (err) throw err;
		console.log(result);
	});
	console.log("\n");
});
