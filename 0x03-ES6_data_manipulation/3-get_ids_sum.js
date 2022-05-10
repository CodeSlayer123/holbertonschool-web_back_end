export default function getStudentIdsSum(students) {
  return students.reduce((accum, student) => accum + student.id, 0);
}
