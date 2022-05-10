export default function getListStudentIds(students) {
  if (!Array.isArray(students)) {
    return [];
  }
  const result = students.map((student) => student.id);

  return result;
}
