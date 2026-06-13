---
title: "Problema 06 — Compresión politrópica de una mezcla"
tags:
  - termodinamica
  - problemas
  - mezclas
  - primera_ley
draft: false
aliases:
  - compresión de mezcla
  - mezcla CO2 N2 politrópica
---

# Problema 06 — Compresión politrópica de una mezcla

> [!definicion] Enunciado
> Una mezcla de $0{,}15\ \text{kg}$ de $\text{CO}_2$ y $0{,}1\ \text{kg}$ de $\text{N}_2$ se comprime desde $p_1 = 1\ \text{atm}$, $T_1 = 300\ \text{K}$ hasta $p_2 = 3\ \text{atm}$ en un proceso **politrópico** con $n = 1{,}25$. Se desprecian energía cinética y potencial.
>
> Se pide:
> 1. La temperatura final.
> 2. El trabajo de compresión.
> 3. El calor intercambiado.
> 4. La variación de entropía de la mezcla.

## Estrategia

> [!teoria]
> Sistema **cerrado** de composición constante. La mezcla se trata como un [[Gas Ideal]] de masa molar aparente $M$ (ver [[Mezclas de Gases]]). Aplican el trabajo politrópico, la [[Primera Ley SC]] $Q = \Delta U + W$, y el cambio de entropía de mezcla. Es la versión "de mezcla" del [[Problema 02]].

## Composición de la mezcla

> [!solucion]
> Moles de cada componente y masa molecular aparente:
> $$
> n_{\text{CO}_2} = \frac{0{,}15}{44} = 0{,}00341, \quad n_{\text{N}_2} = \frac{0{,}1}{28} = 0{,}00357\ \text{kmol}, \quad n = 0{,}00698\ \text{kmol}
> $$
> $$
> m = 0{,}25\ \text{kg}, \qquad M = \frac{m}{n} = \frac{0{,}25}{0{,}00698} = 35{,}81\ \text{kg/kmol}, \qquad \frac{R_u}{M} = \frac{8{,}314}{35{,}81} = 0{,}2322\ \text{kJ/kg·K}
> $$
> Fracciones másicas: $fm_{\text{CO}_2} = 0{,}6$, $fm_{\text{N}_2} = 0{,}4$.

## Inciso 1 — Temperatura final

> [!solucion]
> Para gas ideal en proceso politrópico:
> $$
> T_2 = T_1\left(\frac{p_2}{p_1}\right)^{\frac{n-1}{n}} = 300\,(3)^{0{,}2} = 300 \times 1{,}2457 = 374\ \text{K}
> $$

## Inciso 2 — Trabajo

> [!solucion]
> Trabajo politrópico de gas ideal, con $R/M$ de la mezcla:
> $$
> W = \frac{m\,(R_u/M)\,(T_2 - T_1)}{1 - n} = \frac{0{,}25 \times 0{,}2322 \times (374 - 300)}{1 - 1{,}25} = \frac{4{,}295}{-0{,}25} = -17{,}18\ \text{kJ}
> $$
> El signo negativo indica trabajo **hecho sobre** la mezcla (compresión), según la convención de [[Primera Ley SC]].

## Inciso 3 — Calor

> [!solucion]
> **Con tablas de gas ideal** (base molar, $\bar u_i$ de tabla A-23):
> $$
> \Delta U = n_{\text{CO}_2}\big[\bar u_{\text{CO}_2}(374) - \bar u_{\text{CO}_2}(300)\big] + n_{\text{N}_2}\big[\bar u_{\text{N}_2}(374) - \bar u_{\text{N}_2}(300)\big]
> $$
> $$
> \Delta U = 0{,}00341\,(9197 - 6939) + 0{,}00357\,(7769 - 6229) = 13{,}22\ \text{kJ}
> $$
> Por la [[Primera Ley SC]]:
> $$
> Q = \Delta U + W = 13{,}22 + (-17{,}18) = -3{,}96\ \text{kJ}
> $$
> $Q < 0$: la mezcla **cede** calor (el índice $n = 1{,}25$ está entre el isotérmico y el adiabático).

> [!info] Atajo con $c_v$ constante
> Como $\Delta T$ es pequeño, vale usar $c_v$ de mezcla. Con $c_{v,\text{CO}_2} = 0{,}657$, $c_{v,\text{N}_2} = 0{,}743\ \text{kJ/kg·K}$:
> $$
> c_v = \sum_i fm_i\,c_{v,i} = 0{,}6\,(0{,}657) + 0{,}4\,(0{,}743) = 0{,}691\ \text{kJ/kg·K}
> $$
> $$
> \Delta U = m c_v \Delta T = 0{,}25 \times 0{,}691 \times 74 = 12{,}8\ \text{kJ}
> $$
> coherente con el valor de tablas.

## Inciso 4 — Variación de entropía

> [!solucion]
> A composición constante el cociente de presiones parciales iguala al de la mezcla, así que (con $c_p = \sum fm_i c_{p,i} = 0{,}6(0{,}846)+0{,}4(1{,}040) = 0{,}924\ \text{kJ/kg·K}$):
> $$
> \Delta S = m\left[c_p \ln\frac{T_2}{T_1} - \frac{R_u}{M}\ln\frac{p_2}{p_1}\right] = 0{,}25\left[0{,}924\,\ln(1{,}2457) - 0{,}2322\,\ln 3\right]
> $$
> $$
> \Delta S = 0{,}25\,[0{,}2030 - 0{,}2551] = -0{,}0130\ \text{kJ/K}
> $$
> El valor con tablas de entropía ($\bar s^{\circ}$ de A-23) da $\Delta S = -0{,}0117\ \text{kJ/K}$, del mismo orden.

> [!info] Verificación física
> $\Delta S < 0$ porque la entropía sale del sistema con el calor cedido. No contradice la segunda ley: el balance completo exige sumar la entropía recibida por el entorno (ver el razonamiento de [[Problema 02]], aquí con propiedades de mezcla).

## Notas usadas

> [!referencia]
> [[Mezclas de Gases]] · [[Primera Ley SC]] · [[Gas Ideal]] · [[Energia Interna]] · [[Entropia]] · [[Problema 02]] · Moran & Shapiro, Ej. 12.3.

> [!info]
> **Convención de notación**:
> - $W > 0$: trabajo realizado por el sistema; $Q > 0$: calor hacia el sistema.
> - $M$: masa molecular aparente; $R_u/M$: constante particular de la mezcla.
> - $n$: índice politrópico (no confundir con número de moles $n$ del gas).
