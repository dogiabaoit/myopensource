var fs = require('fs');
//appendFile con dong vai tro update, noi dung moi duoc them vao CUOI DONG
fs.appendFile('mynewfile1.txt', 'Hello content!', function (err) {
  if (err) throw err;
  console.log('Saved!');
}); 