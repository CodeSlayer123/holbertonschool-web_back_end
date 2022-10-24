const readDatabase = require('../utils');


class StudentsController{
    static getAllStudents(request, response){
        response.status(200)
        readDatabase(process.argv[2]).then(values => {
            response.write("This is the list of our students\n")
            let studentsCS = values[1].sort()
            let studentsSWE = values[2].sort()
            response.write(`Number of students in CS: ${studentsCS.length}. List: ${studentsCS.join(", ")}\n`)
            response.write(`Number of students in SWE: ${studentsSWE.length}. List: ${studentsSWE.join(", ")}`)
        })
        .catch((err) => res.end(output + err.message));
        response.end();


    }

    static getAllStudentsByMajor(request, response){
        response.status(200)
        let acceptable = ["CS", "SWE"]
        const major = request.params.major
        if (!acceptable.includes(major)){
            response.status(500)
            response.write(`Major parameter must be ${acceptable[0]} or ${acceptable[1]}`)
            response.end()

        }
        readDatabase(process.argv[2]).then(values => {
            let studentsCS = values[1]
            let studentsSWE = values[2]
            if (major === acceptable[0]){
                response.write(`List: ${studentsCS.join(", ")}\n`)
            }
            else if (major === acceptable[1]){
                response.write(`List: ${studentsSWE.join(", ")}`)

            }

        })
        .catch((err) => res.end(output + err.message));
        response.end();

    }
}

module.exports = StudentsController