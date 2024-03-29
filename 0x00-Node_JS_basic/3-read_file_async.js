const fs = require('fs');

const countStudents = async (path) => {
  const students = [];
  const cs = [];
  const swe = [];

  fs.access(path, (error) => {
    if (error) {
      throw new Error('Cannot load the database');
    }
  });
  const newPromise = await fs.promises.readFile(path, 'utf8');
  const data = newPromise.split('\n');
  for (let i = 1; i < data.length; i += 1) {
    if (data[i].length > 0) {
      students.push(data[i].split(','));
    }
  }

  for (const i in students) {
    if (students[i][3] === 'CS') {
      cs.push(students[i][0]);
    } else if (students[i][3] === 'SWE') {
      swe.push(students[i][0]);
    }
  }
  const numOfStudents = `Number of students: ${students.length}`;
  const numOfStudentsCS = `Number of students in CS: ${cs.length}. List: ${cs.join(', ')}`;
  const numOfStudentsSWE = `Number of students in SWE: ${swe.length}. List: ${swe.join(', ')}`;

  const result = `${numOfStudents}\n${numOfStudentsCS}\n${numOfStudentsSWE}`;
  console.log(result);
  return result;
};
module.exports = countStudents;
