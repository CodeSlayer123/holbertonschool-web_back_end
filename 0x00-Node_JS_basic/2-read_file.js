var fs=require("fs")

function countStudents(path){
    students = []
    cs = []
    swe = []
    if (!fs.existsSync(path)) {
        throw new Error("Cannot load the database");
    }

    const data = fs.readFileSync(path, 'utf8').split("\n");

    for (let i = 1; i < data.length; i++){

        if (data[i].length > 0){
            students.push(data[i].split(","))
        }
    }

    for (i in students){
        if (students[i][3] === 'CS'){
            cs.push(students[i][0])
        }
        else if (students[i][3] === 'SWE') {
            swe.push(students[i][0])
        }
    }

  console.log(`Number of students: ${students.length}`)
  console.log(`Number of students in CS: ${cs.length}. List: ${cs.join(", ")}`)
  console.log(`Number of students in SWE: ${swe.length}. List: ${swe.join(", ")}`)

}

module.exports = countStudents