# Write your MySQL query statement below
SELECT u.name as name, IFNULL(SUM(distance),0) AS travelled_distance
FROM USERS U LEFT JOIN RIDES R
ON R.USER_ID = U.ID
GROUP BY R.USER_ID
ORDER BY travelled_distance DESC, name ASC;