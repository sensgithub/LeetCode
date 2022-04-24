# Write your MySQL query statement below
SELECT U.name AS name,
       sum(CASE WHEN distance IS NULL
           THEN 0 ELSE distance END) AS travelled_distance
FROM Users U
LEFT JOIN Rides
ON Rides.user_id = U.id
GROUP BY U.name
ORDER BY travelled_distance DESC, name;