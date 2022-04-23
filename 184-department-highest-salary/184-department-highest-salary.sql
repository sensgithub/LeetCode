# Write your MySQL query statement below

SELECT d.name as 'Department', e.name as 'Employee', e.salary as 'Salary'
FROM Employee e 
	INNER JOIN (SELECT departmentId, max(salary) as highest_salary
                FROM Employee 
                GROUP BY departmentId) m ON m.departmentId = e.departmentId and m.highest_salary = e.salary
    JOIN Department d ON e.departmentId = d.id