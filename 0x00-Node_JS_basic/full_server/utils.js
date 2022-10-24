const fs = require('fs');

const readDatabase = async (path) =>{

    let students = []
    let cs = []
    let swe = []
    fs.access(path, (error) => {
        if (error) {
            const err = new Error("Cannot load the database")
            err.code = 500
            throw err
        }})

    const newPromise = await fs.promises.readFile(path,"utf8");

    let data = newPromise.split('\n');

    for (let i = 1; i < data.length; i++){

        if (data[i].length > 0){
            students.push(data[i].split(","))
        }
    }

    for (let student in students){
        if (students[student][3] === 'CS'){
            cs.push(students[student][0])
        }
        else if (students[student][3] === 'SWE') {
            swe.push(students[student][0])
        }
    }

    let result = [students, cs, swe]
    return result
}

module.exports = readDatabase
