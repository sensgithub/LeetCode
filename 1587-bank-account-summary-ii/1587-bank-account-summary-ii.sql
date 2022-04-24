# Write your MySQL query statement below
SELECT name, SUM(amount) as balance
FROM Users
INNER JOIN Transactions ON
Transactions.account = Users.account
GROUP BY name
HAVING SUM(amount) > 10000