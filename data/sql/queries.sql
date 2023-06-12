

-- GET THE MAX AND A VALUE IT MATCHES THE MAX OF ANOTHER COLUMN JOININ TO THE SAME TABLE.
SELECT t1.barri, t1.valor AS max_valor, t1.sound
FROM soroll t1 
INNER JOIN (
    SELECT barri, MAX(valor) AS max_valor
    FROM soroll t2
    GROUP BY barri
) t2
ON t1.barri = t2.barri AND t1.valor = t2.max_valor;