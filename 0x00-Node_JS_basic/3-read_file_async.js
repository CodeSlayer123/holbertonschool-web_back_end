const fs = require('fs').promises;
const { parse } = require("csv-parse");

const countStudents = async (path) => {
    students = []
    cs = []
    swe = []

    fs.access(path, (error) => {
        if (error) {
            throw new Error("Cannot load the database");
        }


    const data = await fs.readFile(path,
            {encoding:'utf8', flag:'r'}).toString().split("\n");

    for (i in data){
        students.push(data[i].split(","))
    }

    for (i in students){
        if (students[i][3] === 'CS'){
            cs.push(students[i][0])
        }
        else if (students[i][3] === 'SWE') {
            swe.push(students[i][0])
        }
    }

  console.log(`Number of students: ${students.length - 1}`)

  console.log(`Number of students in CS: ${cs.length}. List: ${cs.join(", ")}`)
  console.log(`Number of students in SWE: ${swe.length}. List: ${swe.join(", ")}`)

}

module.exports = countStudents