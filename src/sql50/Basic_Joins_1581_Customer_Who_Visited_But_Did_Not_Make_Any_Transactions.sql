SELECT
    v.customer_id,
    COUNT(COALESCE(transaction_id, 1)) AS count_no_trans
FROM Visits v 
LEFT JOIN Transactions t ON v.visit_id = t.visit_id 
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id