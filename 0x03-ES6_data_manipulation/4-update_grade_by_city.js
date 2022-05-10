export default function updateStudentGradeByCity(students, city, newGrades) {
  if (!Array.isArray(students)) {
    return [];
  }
  const locationstu = students.filter((student) => student.location === city);
  return locationstu.map((student) => {
    const gr = newGrades.filter((element) => element.studentId === student.id);
    if (gr.length === 0) {
      return ({ ...student, grade: 'N/A' });
    }
    return ({ ...student, grade: gr[0].grade });
  });
}
