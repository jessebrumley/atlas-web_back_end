export default function getListStudents() {
  const student1 = { firstName: 'Guillaume', id: 1, location: 'San Francisco' };
  const student2 = { firstName: 'James', id: 2, location: 'Columbia' };
  const student3 = { firstName: 'Serena', id: 5, location: 'San Francisco' };

  const studentArray = [student1, student2, student3];

  return studentArray;
}
