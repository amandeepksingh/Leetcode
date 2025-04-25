-- # Write your MySQL query statement below
-- SELECT DEPARTMENT.NAME AS DEPARTMENT, 
-- EMPLOYEE.NAME AS EMPLOYEE, 
-- SALARY
-- FROM EMPLOYEE 
-- JOIN DEPARTMENT 
-- ON EMPLOYEE.DEPARTMENTID = DEPARTMENT.ID 
-- WHERE SALARY = 
-- (SELECT MAX(SALARY) 
-- FROM EMPLOYEE
-- WHERE DEPARTMENTID = EMPLOYEE.DEPARTMENTID)
SELECT d.name AS Department, 
       e.name AS Employee, 
       e.salary AS Salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE e.salary = (
    SELECT MAX(salary)
    FROM Employee
    WHERE departmentId = e.departmentId
);