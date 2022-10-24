const countStudents = require('./3-read_file_async');
const http = require("http");
const host = 'localhost';
const port = 1245;
const app = http.createServer(async (req, res) => {
    path = process.argv[2]

    if (req.url === "/"){
        res.end('Hello Holberton School!');
    }

    if (req.url === "/students"){
        res.write('This is the list of our students\n');
        await countStudents(path).then(values => {
            res.write(values)
        })
        .catch((err) => res.end(output + err.message));
    }
    res.end();

  }).listen(port);
module.exports = app
