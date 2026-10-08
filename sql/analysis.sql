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

-- Pregunta 2: ¿Qué modo de envío tiene más retrasos, y cómo afecta eso a la ganancia?

2.1 Modo de envio con mas retrasos

SELECT shipping_mode,
	COUNT(*) as all_methods,
	SUM(CASE WHEN late_delivery_risk > 0 THEN 1 ELSE 0 END) AS delays,
	ROUND(100.0 * SUM(CASE WHEN late_delivery_risk > 0 THEN 1 ELSE 0 END) / COUNT(*), 2) AS delay_pct
FROM dataco
GROUP BY shipping_mode
ORDER BY delay_pct DESC;

2.2 Afectacion retraso a a ganancia 

SELECT
    ROUND(AVG(CASE
        WHEN late_delivery_risk > 0
        THEN order_profit_per_order
    END), 2) AS avg_profit_with_delay,

    ROUND(AVG(CASE
        WHEN late_delivery_risk = 0
        THEN order_profit_per_order
    END), 2) AS avg_profit_without_delay
FROM dataco;

2.3 Impacto por modo de envío

SELECT
    shipping_mode,

    ROUND(AVG(CASE
        WHEN late_delivery_risk > 0
        THEN order_profit_per_order
    END), 2) AS avg_profit_with_delay,

    ROUND(AVG(CASE
        WHEN late_delivery_risk = 0
        THEN order_profit_per_order
    END), 2) AS avg_profit_without_delay

FROM dataco
GROUP BY shipping_mode
ORDER BY avg_profit_with_delay DESC;

-- Pregunta 3
