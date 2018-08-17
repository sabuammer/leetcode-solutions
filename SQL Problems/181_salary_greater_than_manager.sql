SELECT e2.name AS Employee
FROM Employee e1
Inner JOIN Employee e2
ON e1.Id = e2.ManagerID and e1.salary < e2.salary;