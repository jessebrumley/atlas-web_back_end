export default function createEmployeesObject(departmentName, employees) {
  const employeeObject = {
    [`${departmentName}`]: employees,
  };

  return employeeObject;
}
