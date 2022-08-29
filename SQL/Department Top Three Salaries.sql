select tD.Name as 'Department', tE1.Name as 'Employee', tE1.Salary from Employee as tE1
Inner join Department as tD on tE1.DepartmentId = tD.Id
Left join Employee as tE2 on tE1.DepartmentId = tE2.DepartmentId and tE1.Salary <= tE2.Salary
group by tE1.Id
having count(distinct tE2.Salary) <= 3
order by tE1.DepartmentId, tE1.Salary desc
