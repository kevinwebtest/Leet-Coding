# Write your MySQL query statement below
SELECT s.score, COUNT(s2.score) "rank"
FROM Scores s, (SELECT DISTINCT score FROM Scores) s2
WHERE s2.score >= s.score
GROUP BY s.id
ORDER By s.score DESC
