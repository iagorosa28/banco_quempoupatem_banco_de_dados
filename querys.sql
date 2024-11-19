-- 1. Clientes com saldo maior que 5.000
SELECT * 
FROM cliente AS c
JOIN conta AS ct ON c.id = ct.id_cliente
WHERE ct.saldo > 5000;

-- 2. Todas as contas criadas por um gerente específico
SELECT *
FROM conta
WHERE id_gerente = "ID DO GERENTE";

-- 3. Clientes com saldo menor que 5.000
SELECT * 
FROM cliente AS c
JOIN conta AS ct ON c.id = ct.id_cliente
WHERE ct.saldo < 5000;

-- 4. Clientes com mais de 10 cotas compradas.
SELECT c.id, c.nome, SUM(i.quantidade) AS total_cotas_compradas
FROM cliente AS c
JOIN investimento AS i ON c.id = i.id_cliente
GROUP BY c.id, c.nome
HAVING SUM(i.quantidade) > 10;

-- 5. Clientes que realizaram mais operações de débito do que de depósito
SELECT c.id, c.nome
FROM cliente AS c
JOIN debito AS d ON c.id = d.id_cliente
JOIN deposito AS dp ON c.id = dp.id_cliente
GROUP BY c.id, c.nome
HAVING COUNT(d.id) > COUNT(dp.id);

-- 6. Clientes com saldo menor que 0
SELECT * 
FROM cliente AS c
JOIN conta AS ct ON c.id = ct.id_cliente
WHERE ct.saldo < 0;

-- 7. Gerentes com mais de 5 contas criadas
SELECT g.id, g.nome, COUNT(ct.id_cliente) AS contas_criadas
FROM gerente AS g
JOIN conta AS ct ON g.id = ct.id_gerente
GROUP BY g.id, g.nome
HAVING COUNT(ct.id_cliente) > 5;

-- 8. Empresas com mais de 50 cotas vendidas
SELECT e.id, e.nome, SUM(i.quantidade) AS total_cotas_vendidas
FROM empresa AS e
JOIN investimento AS i ON e.id = i.id_empresa
GROUP BY e.id, e.nome
HAVING SUM(i.quantidade) > 50;

-- 9. Empresas com menos de 50 cotas vendidas
SELECT e.id, e.nome, SUM(i.quantidade) AS total_cotas_vendidas
FROM empresa AS e
JOIN investimento AS i ON e.id = i.id_empresa
GROUP BY e.id, e.nome
HAVING SUM(i.quantidade) < 50;

-- 10. Clientes com idade menor que 18 anos
SELECT * 
FROM cliente
WHERE idade < 18;