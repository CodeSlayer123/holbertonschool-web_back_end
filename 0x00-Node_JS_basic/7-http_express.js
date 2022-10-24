const express = require("express");
const port = 1245;
const countStudents = require('./3-read_file_async');
const app = express();


app.get("/", (req, res) => {
    res.send("Hello Holberton School!");
 });
 app.get("/students", async (req, res) => {
    path = process.argv[2]

    res.write("This is the list of our students\n");
    await countStudents(path).then(values => {
        res.write(values)
    })
    .catch((err) => res.end(output + err.message));
    res.end();

 });

 app.listen(port);

module.exports = app