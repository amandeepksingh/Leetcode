# Write your MySQL query statement below
SELECT PLAYER_ID, MIN(EVENT_DATE) AS first_login
FROM ACTIVITY
GROUP BY PLAYER_ID;