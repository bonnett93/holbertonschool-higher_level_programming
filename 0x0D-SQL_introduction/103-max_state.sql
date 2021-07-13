-- Displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- SQL keywords in uppercase.
SELECT state, MAX(value) AS max_temp FROM temperatures
    GROUP BY state
    ORDER BY state ASC;
