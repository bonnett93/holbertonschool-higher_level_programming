-- Displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- SQL keywords in uppercase.
SELECT city, AVG(value) AS avg_temp FROM temperatures
    WHERE month = 7 OR month = 8
    GROUP BY city
    ORDER BY avg_temp DESC LIMIT 3;
