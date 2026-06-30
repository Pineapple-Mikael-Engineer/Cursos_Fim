---
title: "P4 — Brayton real (eficiencias internas y caída de presión)"
order: 5
tags: [termodinamica, problemas, ciclos, brayton]
draft: false
aliases: [Brayton real 88% caída presión]
---

# P4 — Brayton real (eficiencias internas y caída de presión)

> [!definicion] Enunciado
> Una planta generadora funciona bajo un ciclo Joule-Brayton estándar; el aire entra al compresor a $35\,^\circ$C y $106$ kPa. La relación de presiones es $11$ y la temperatura máxima es $1400$ K. Las eficiencias internas del compresor y de la turbina son ambas $88\%$, y existe una caída de $30$ kPa entre la descarga del compresor y la admisión a la turbina. Determinar **(a)** $P$ y $T$ en cada estado; **(b)** trabajo específico del compresor, de la turbina y eficiencia térmica.

> [!solucion] (a) Estados (con $\eta_c=\eta_t=0{,}88$ y $\Delta P=30$ kPa)
> **Compresor:** $T_{2s}=308\,(11)^{0{,}2857}=611{,}4$ K, $P_2=1166$ kPa; real $T_2=308+\dfrac{611{,}4-308}{0{,}88}=652{,}8$ K.
> **Admisión turbina:** $P_3=1166-30=1136$ kPa, $T_3=1400$ K.
> **Turbina:** $T_{4s}=1400\,(106/1136)^{0{,}2857}=711$ K; real $T_4=1400-0{,}88(1400-711)=793{,}7$ K, $P_4=106$ kPa.

> [!solucion] (b) Trabajos y eficiencia
> $$w_C=c_p(T_2-T_1)=1{,}005(652{,}8-308)=\boxed{346{,}5\ \text{kJ/kg}},$$
> $$w_T=c_p(T_3-T_4)=1{,}005(1400-793{,}7)=\boxed{609{,}3\ \text{kJ/kg}},$$
> $$\eta=\frac{w_T-w_C}{c_p(T_3-T_2)}=\frac{262{,}8}{750{,}9}=\boxed{35{,}0\%}.$$

> [!info]
> Las irreversibilidades (compresor/turbina al $88\%$) y la caída de presión bajan la eficiencia del $49{,}6\%$ ideal a $35{,}0\%$; el bwr $=w_C/w_T=0{,}57$ es alto, típico del Brayton.

> [!referencia]
> [[Conversión de Energía/Ciclos de Potencia/Brayton/Brayton Simple | Brayton Simple]] · [[Sistemas/Dispositivos Flujo/Compresores | Compresores]]
