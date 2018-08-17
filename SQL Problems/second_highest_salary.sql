SELECT 
    CASE
        WHEN COUNT(*) >= 2 THEN MIN(Salary) 
        ELSE NULL 
    END AS SecondHighestSalary
FROM (
    SELECT DISTINCT Salary 
    FROM Employee
    ORDER BY Salary DESC
    LIMIT 2
) AS TOP2;