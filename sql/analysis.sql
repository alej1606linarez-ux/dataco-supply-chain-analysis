-- DataCo Supply Chain Analysis
-- SQL adaptation of the Pandas analysis

-- Pregunta 1: ¿qué región genera más ganancia neta, y cuáles tienen pérdidas constantes?

1. Ganancias netas por región

SELECT order_region, ROUND(SUM(order_profit_per_order), 0) AS total_profit
FROM dataco
GROUP BY order_region
ORDER BY total_profit DESC;

1.2 Regiones con pérdidas constantes y su proporción de pérdida por total de órdenes.

SELECT 
    order_region,
    COUNT(*) AS total_ordenes,
    SUM(CASE WHEN order_profit_per_order < 0 THEN 1 ELSE 0 END) AS ordenes_con_perdida,
	100.0 * SUM(CASE WHEN order_profit_per_order < 0 THEN 1 ELSE 0 END) / COUNT(*) AS proporcion_perdida
FROM dataco
GROUP BY order_region
ORDER BY proporcion_perdida DESC;

-- Pregunta 2


-- Pregunta 3
