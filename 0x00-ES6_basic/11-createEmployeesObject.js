export default function createEmployeesObject(departmentName, employees) {
    const billy = {
        [departmentName]: employees,
   }
    return billy
}