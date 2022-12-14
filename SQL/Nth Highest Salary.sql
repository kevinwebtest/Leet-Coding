CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N=N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT(salary) FROM Employee
      ORDER BY salary DESC
      LIMIT 1 OFFSET N
  );
END

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT e1.Salary
      FROM (SELECT DISTINCT Salary FROM Employee) e1
      WHERE (SELECT COUNT(*) FROM (SELECT DISTINCT Salary FROM Employee) e2 WHERE e2.Salary > e1.Salary) = N - 1      
      LIMIT 1	
  );
END
