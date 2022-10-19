const http = require("http");
const host = 'localhost';
const port = 1245;
 app = http.createServer(function (req, res) {
    res.write('Hello Holberton School!');
    res.end();
  }).listen(port);
module.exports = app