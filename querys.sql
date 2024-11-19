-- 1. Clientes com saldo maior que 5.000
SELECT * 
FROM cliente AS c
JOIN conta AS ct ON c.id = ct.id_cliente
WHERE ct.saldo > 5000;

-- 2. Todas as contas criadas por um gerente específico
SELECT *
FROM conta
WHERE id_gerente = "ID DO GERENTE";

-- 3. Quantidade de contas que cada gerente criou

-- 4. Quantidade de clientes que compraram cotas de uma empresa específica


-- 5. Clientes que realizaram mais operações de débito do que de depósito
SELECT c.id, c.nome
FROM cliente AS c
JOIN debito AS d ON c.id = d.id_cliente
JOIN deposito AS dp ON c.id = dp.id_cliente
GROUP BY c.id, c.nome
HAVING COUNT(d.id) > COUNT(dp.id);

-- 6. Quantidade total de movimentações (débito e depósito) de um cliente

-- 7. Quantidade total de cotas que um cliente possui

-- 8. Quantidade de compradores de cota para cada empresa

-- 9. Quantidade de cotas vendidas por cada empresa

-- 10. Idade média dos clientes

-- 11. Quantidade de clientes com idade menor que 18 anos
