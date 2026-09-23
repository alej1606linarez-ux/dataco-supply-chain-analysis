"""
Análisis de rentabilidad y logística — DataCo Supply Chain
Dataset real de ~180,000 pedidos de una empresa global de e-commerce/retail (2015-2017).

Preguntas de negocio:
 1. ¿Qué región/mercado genera más ganancia neta, y cuáles tienen pérdidas constantes?
 2. ¿Qué modo de envío tiene más retrasos, y cómo afecta eso a la ganancia?
 3. ¿Qué segmento de cliente es más rentable vs. cuál genera más volumen pero menos margen?

Fuente del dataset:
https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis
"""

import pandas as pd

pd.set_option("display.float_format", "{:.2f}".format)


# ============================================
# CARGA Y LIMPIEZA
# ============================================

df = pd.read_csv("DataCoSupplyChainDataset.csv", encoding="latin1")

df_limpio = df.copy()
df_limpio = df_limpio.drop(columns=[
    "Customer Email", "Customer Password", "Customer Fname", "Customer Lname",
    "Customer Street", "Product Description"
])
df_limpio["order date (DateOrders)"] = pd.to_datetime(df_limpio["order date (DateOrders)"])
df_limpio["shipping date (DateOrders)"] = pd.to_datetime(df_limpio["shipping date (DateOrders)"])

print(f"Dataset cargado: {df_limpio.shape[0]:,} filas, {df_limpio.shape[1]} columnas")
print(f"Filas duplicadas: {df_limpio.duplicated().sum()}")


# ============================================
# PREGUNTA 1 — Ganancia y pérdida por región
# ============================================

ganancia_neta = df_limpio.groupby(["Order Region"])["Order Profit Per Order"].sum().sort_values(ascending=False)

perdida = (df_limpio[df_limpio["Order Profit Per Order"] < 0]).groupby("Order Region").size()
total_ordenes_region = df_limpio.groupby("Order Region")["Order Region"].count()
proporcionalidad = (perdida / total_ordenes_region * 100).sort_values(ascending=False)

print("\n--- P1: Ganancia neta total por región ---")
print(ganancia_neta)
print("\n--- P1: % de órdenes en pérdida por región ---")
print(proporcionalidad.round(2))

# CONCLUSIÓN P1:
# Hallazgo: Western Europe genera la mayor ganancia neta ($625,446.08), seguida
# de Central America ($616,341.57).
# Matiz: La proporción de órdenes en pérdida es prácticamente uniforme entre
# regiones (16.16%-19.92%, ~3.76 puntos de diferencia) — no hay una región con
# un problema estructural distinto a las demás.
# Recomendación: No se justifica una intervención específica por región; la
# tasa de pérdida es un fenómeno consistente en todo el negocio.


# ============================================
# PREGUNTA 2 — Retrasos por modo de envío
# ============================================

delays = df_limpio[df_limpio["Late_delivery_risk"] > 0]
delays_agrupado = delays.groupby(["Shipping Mode"]).size().sort_values(ascending=False)
total_ordenes = df_limpio.groupby("Shipping Mode")["Late_delivery_risk"].count()
porcentajes_retrasos = (delays_agrupado / total_ordenes * 100).round(2).sort_values(ascending=False)

sin_delays = df_limpio[df_limpio["Late_delivery_risk"] <= 0]
promedio_con_retraso = delays["Order Profit Per Order"].mean()
promedio_sin_retraso = sin_delays["Order Profit Per Order"].mean()

print("\n--- P2: % de retraso por modo de envío ---")
print(porcentajes_retrasos)
print(f"\nGanancia promedio CON retraso: {promedio_con_retraso:.2f}")
print(f"Ganancia promedio SIN retraso: {promedio_sin_retraso:.2f}")

# CONCLUSIÓN P2:
# Hallazgo: First Class incumple el 95.32% de sus envíos, muy por encima de
# Standard Class (38.07%), aunque este último tiene el mayor conteo absoluto
# de retrasos por ser el modo más usado.
# Matiz: First Class entrega en promedio en 2 días (más rápido que Standard
# Class), pero promete solo 1 — un plazo casi imposible de cumplir. Es un
# problema de expectativa mal calibrada en vez de mala ejecución logística. El
# retraso apenas afecta la ganancia promedio ($21.62 con retraso vs $22.40 sin).
# Recomendación: Ajustar el SLA de First Class a un plazo realista (ej. 2 días)
# en vez de invertir en acelerar la logística.


# ============================================
# PREGUNTA 3 — Segmento de cliente: volumen vs. margen
# ============================================

volumen = df_limpio.groupby("Customer Segment")["Order Profit Per Order"].agg(["sum", "mean", "count"])
diferencia_pct = (volumen["mean"].max() - volumen["mean"].min()) / volumen["mean"].min() * 100

print("\n--- P3: Ganancia por segmento de cliente ---")
print(volumen)
print(f"\nDiferencia de margen promedio entre el mejor y el peor segmento: {diferencia_pct:.2f}%")

# CONCLUSIÓN P3:
# Hallazgo: Consumer domina en volumen (93,504 órdenes, 53% del total) y en
# ganancia total acumulada ($2,073,487.67), muy por encima de Corporate y
# Home Office.
# Matiz: El margen promedio por orden es prácticamente idéntico entre los tres
# segmentos (diferencia de apenas 3.44%). La ganancia de Consumer viene de
# volumen, no de mejor rentabilidad relativa.
# Recomendación: No hay un segmento "ineficiente" que requiera mejorar su
# margen. La oportunidad de crecimiento está en aumentar el volumen de
# Corporate y Home Office.
