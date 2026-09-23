# Análisis de Rentabilidad y Logística — DataCo Supply Chain

Proyecto de análisis de datos aplicando Pandas sobre un dataset real de ~180,000 pedidos de una empresa global de e-commerce/retail (2015-2017), con foco en preguntas de negocio de rentabilidad y logística — el tipo de análisis que conecta con mi experiencia previa de ~5 años en customer service y logística.

## Contexto

Este proyecto es el segundo de mi portafolio en mi transición hacia un rol de Data Analyst, después de un primer proyecto de fundamentos de Python (simulador de ATM) y de una práctica dedicada a los verbos fundamentales de Pandas (ver repositorio `pandas-fundamentos-practica`). Aquí aplico esos mismos verbos —filtrar, agrupar, agregar, combinar, transformar— sobre datos reales y de gran volumen, con el objetivo de responder preguntas de negocio concretas, no solo demostrar sintaxis.

## Preguntas de negocio

1. **¿Qué región/mercado genera más ganancia neta, y cuáles tienen pérdidas constantes?**
2. **¿Qué modo de envío tiene más retrasos, y cómo afecta eso a la ganancia?**
3. **¿Qué segmento de cliente es más rentable vs. cuál genera más volumen pero menos margen?**

## Hallazgos principales

**1. Rentabilidad por región:** Western Europe lidera en ganancia neta total ($625,446.08), pero la proporción de órdenes en pérdida es prácticamente uniforme en todas las regiones (16.16%-19.92%). No hay evidencia de que alguna región tenga un problema estructural distinto — la variación observada es simple ruido, no una señal real.

**2. Retrasos por modo de envío:** First Class incumple el 95.32% de sus envíos —la tasa más alta de los cuatro modos— a pesar de que Standard Class concentra más retrasos en números absolutos por ser el modo más usado. La causa no es mala ejecución logística: First Class entrega en promedio en 2 días (más rápido que Standard Class), pero promete solo 1 día, un plazo estadísticamente casi imposible de cumplir. El retraso, además, apenas afecta la ganancia promedio por orden.

**3. Segmento de cliente:** Consumer domina en volumen (53% de las órdenes) y en ganancia total, pero el margen promedio por orden es casi idéntico entre los tres segmentos (diferencia de apenas 3.44%). La ganancia de Consumer viene de volumen, no de mejor rentabilidad relativa.

## Dataset

[DataCo Smart Supply Chain for Big Data Analysis](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis) — 180,519 filas, 53 columnas originales. Se eliminaron columnas con datos personales identificables (nombre, email, contraseña, dirección) antes del análisis.

## Cómo correrlo

```bash
pip install pandas
python analisis_supply_chain_dataco.py
```

El dataset (`DataCoSupplyChainDataset.csv`) debe estar en la misma carpeta que el script. Puede descargarse desde el link de Kaggle de arriba (requiere cuenta gratuita).

## Herramientas y verbos aplicados

Pandas: `groupby`, `.agg()`, filtrado booleano, `.merge()` de conceptos previos, `.sort_values()`, manejo de tipos de fecha, formateo de salida numérica.

## Próximo paso

Replicar estas mismas 3 preguntas en SQL sobre el mismo dataset, para demostrar la misma lógica de análisis en ambas herramientas.
