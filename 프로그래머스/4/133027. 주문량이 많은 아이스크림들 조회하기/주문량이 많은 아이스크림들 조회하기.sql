-- 코드를 입력하세요
SELECT a.flavor
FROM first_half a, july b
WHERE a.flavor = b.flavor
GROUP BY a.flavor
ORDER BY sum(a.total_order + b.total_order) desc 
LIMIT 3