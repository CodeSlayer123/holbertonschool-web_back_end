-- this is task 2
-- ranks country origins of bands
SELECT origin, sum(fans) AS nb_fans
FROM metal_bands GROUP BY origin
ORDER BY nb_fans DESC;