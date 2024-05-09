export default function updateStudentGradeByCity(array, city, newGrades) {
  const filteredStudents = array.filter((student) => student.location === city);

  const gradedStudents = filteredStudents.map((student) => {
    const studentGrade = newGrades.find((grade) => grade.studentId === student.id);

    return { ...student, grade: studentGrade ? studentGrade.grade : 'N/A' };
  });

  return gradedStudents;
}
