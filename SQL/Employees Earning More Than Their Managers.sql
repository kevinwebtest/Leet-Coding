SELECT e.name AS "Employee" FROM Employee e, Employee e2
WHERE e2.id = e.managerId
AND e.salary > e2.salary
