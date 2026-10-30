SELECT id FROM ( 
    SELECT id, 
    temperature as currTemp, 
    recordDate AS currDate, 
    LAG(recordDate) OVER (ORDER BY recordDate) AS prevDate,
    LAG(temperature) OVER (ORDER BY recordDate) as prevTemp
FROM Weather) w 
WHERE currTemp > prevTemp
AND DATEDIFF(currDate, prevDate) = 1