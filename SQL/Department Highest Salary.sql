SELECT d.name Department, e.name Employee, salary Salary
FROM Employee e
INNER JOIN Department d
ON departmentId = d.id
WHERE e.name NOT IN (
    SELECT e2.name FROM Employee e1
    INNER JOIN Employee e2
    WHERE e1.salary>e2.salary
    AND e1.departmentId = e2.departmentId
)