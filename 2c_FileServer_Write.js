var fs = require('fs');
//WriteFile con dong vai tro update ngoai viec tao moi, noi dung moi duoc THAY THE 
fs.writeFile('mynewfile2.txt', 'Hello content!', function (err) {
  if (err) throw err;
  console.log('Saved!');
}); 