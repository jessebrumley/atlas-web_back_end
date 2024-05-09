export default function getStudentsByLocation(students, city) {
  const matches = students.filter((student) => student.location === city);
  return matches;
}
