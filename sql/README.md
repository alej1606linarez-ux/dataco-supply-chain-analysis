# Análisis SQL — Cadena de suministro DataCo

## Descripción general

Esta carpeta contiene la versión SQL del análisis de la cadena de suministro de DataCo, desarrollado inicialmente con Python y Pandas. El objetivo es reproducir y ampliar el análisis original mediante consultas SQL para obtener información útil para la toma de decisiones empresariales.

El proyecto utiliza PostgreSQL para consultar y analizar el archivo `DataCoSupplyChainDataset.csv`, que contiene aproximadamente 180.000 registros relacionados con pedidos, clientes, productos, envíos, ventas y rentabilidad.

## Preguntas de negocio

El análisis se centra en tres preguntas principales:

1. **Rentabilidad por región:** ¿Qué regiones generan mayores ganancias totales y cuáles presentan una mayor proporción de registros con pérdidas?
2. **Desempeño de los envíos:** ¿Qué modalidades de envío presentan mayor riesgo de entrega tardía y cómo se compara la rentabilidad entre los registros con y sin ese riesgo?
3. **Rentabilidad por segmento de cliente:** ¿Qué segmentos de clientes generan mayores ganancias totales y promedio, y cómo varía la rentabilidad entre ellos?

## Herramientas y tecnologías

- **SQL:** consultas, filtrado, agregación, lógica condicional y análisis de datos.
- **PostgreSQL:** sistema de gestión de bases de datos relacionales utilizado para ejecutar las consultas.
- **pgAdmin:** administración de la base de datos y ejecución de consultas SQL.
- **Git y GitHub:** control de versiones y documentación del proyecto.

## Conceptos SQL aplicados

El análisis utiliza las siguientes funcionalidades de SQL:

- `SELECT` y `WHERE` para seleccionar y filtrar registros.
- Funciones de agregación como `SUM()`, `AVG()`, `COUNT()`, `MIN()` y `MAX()`.
- `GROUP BY` y `HAVING` para analizar datos agrupados.
- `CASE WHEN` para realizar cálculos condicionales.
- `ORDER BY` y `ROUND()` para ordenar y presentar resultados.
- Expresiones comunes de tabla (`WITH` o CTE) para organizar consultas de varios pasos.
- `CROSS JOIN` para combinar resultados por segmento con métricas generales.
- Validación de valores `NULL` y análisis de valores distintos cuando corresponde.

## Estructura del proyecto

- `analysis.sql`: contiene las consultas SQL desarrolladas para responder las preguntas de negocio.
- `README.md`: documenta los objetivos, el alcance y las técnicas utilizadas en esta versión SQL.

## Cómo ejecutar el análisis

1. Instalar PostgreSQL y pgAdmin.
2. Crear o seleccionar una base de datos PostgreSQL.
3. Importar `DataCoSupplyChainDataset.csv` en una tabla llamada `dataco`.
4. Abrir `analysis.sql` en el Query Tool de pgAdmin.
5. Ejecutar las consultas individualmente y revisar los resultados.

Es necesario verificar que el nombre de la tabla y los nombres de sus columnas coincidan con los utilizados en el archivo SQL.

## Objetivo y aprendizajes

Este proyecto demuestra la aplicación de SQL al análisis de datos orientado a problemas de negocio. Complementa la versión original desarrollada con Pandas y permite practicar la traducción de la lógica analítica entre herramientas, la agregación de datos, la comparación de segmentos comerciales y la organización de cálculos de varios pasos.

**Consideración sobre los resultados:** antes de interpretar las métricas como pedidos únicos o ganancias totales definitivas, es importante validar el nivel de detalle de los registros. Si existen varias filas por pedido y determinadas métricas se repiten entre ellas, contar o sumar directamente todas las filas podría distorsionar los resultados.
