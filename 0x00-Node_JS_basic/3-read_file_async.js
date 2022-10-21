const fs = require('fs');

const countStudents = async (path) => {

    students = []
    cs = []
    swe = []
    fs.access(path, (error) => {
        if (error) {
            throw new Error("Cannot load the database");
        }})

    const newPromise = await fs.promises.readFile(path,"utf8");

    let data = newPromise.split('\n');

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
    numOfStudents = `Number of students: ${students.length - 1}`
    numOfStudentsCS = `Number of students in CS: ${cs.length}. List: ${cs.join(", ")}`
    numOfStudentsSWE = `Number of students in SWE: ${swe.length}. List: ${swe.join(", ")}`

    result = `${numOfStudents}\n${numOfStudentsCS}\n${numOfStudentsSWE}`
    console.log(result)
    return result
}

module.exports = countStudents