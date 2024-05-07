export default function createEmployeesObject(departmentName, employees) {
  employeesObject = {
    [`${departmentName}`]: [...employees],
  };
  return employeesObject;
}
