---
title: "Problema 05 — Composición de una mezcla de gases"
tags:
  - termodinamica
  - problemas
  - mezclas
  - gas_ideal
draft: false
aliases:
  - composición de mezcla
  - fracciones molares y másicas
  - presiones parciales
---

# Problema 05 — Composición de una mezcla de gases

> [!definicion] Enunciado
> El análisis molar de los productos gaseosos de la combustión de un hidrocarburo es: $\text{CO}_2$, $0{,}08$; $\text{H}_2\text{O}$, $0{,}11$; $\text{O}_2$, $0{,}07$; $\text{N}_2$, $0{,}74$. La mezcla está a $p = 2\ \text{atm}$ y $T = 500\ \text{K}$ en un recipiente de $V = 0{,}5\ \text{m}^3$.
>
> Se pide:
> 1. La masa molecular aparente $M$ y la composición en fracciones másicas.
> 2. Las presiones parciales (Dalton) y los volúmenes parciales (Amagat).
> 3. La masa total de mezcla y el número de moles.

## Estrategia

> [!teoria]
> Todas las relaciones son las del formulario de [[Mezclas de Gases]]: $M = \sum_i y_i M_i$, $fm_i = y_i M_i / M$, $p_i = y_i p$, $V_i = y_i V$. Las masas molares se toman de tablas: $M_{\text{CO}_2}=44$, $M_{\text{H}_2\text{O}}=18$, $M_{\text{O}_2}=32$, $M_{\text{N}_2}=28\ \text{kg/kmol}$.

## Inciso 1 — Masa molecular aparente y fracciones másicas

> [!solucion]
> Tomando como base $1\ \text{kmol}$ de mezcla, cada $n_i$ es numéricamente igual a $y_i$. La masa de cada componente es $m_i = y_i M_i$:
>
> | Componente | $y_i$ | $M_i$ | $m_i = y_i M_i$ | $fm_i = m_i/M$ |
> |:---|:---:|:---:|:---:|:---:|
> | $\text{CO}_2$ | 0,08 | 44 | 3,52 | 0,1237 |
> | $\text{H}_2\text{O}$ | 0,11 | 18 | 1,98 | 0,0696 |
> | $\text{O}_2$ | 0,07 | 32 | 2,24 | 0,0787 |
> | $\text{N}_2$ | 0,74 | 28 | 20,72 | 0,7280 |
> | **Total** | 1,00 | — | **28,46** | 1,0000 |
>
> La suma de la columna $m_i$ es la masa molecular aparente:
> $$
> M = \sum_i y_i M_i = 28{,}46\ \text{kg/kmol}
> $$
> Las fracciones másicas se obtienen dividiendo cada $m_i$ entre $M$. Nótese que el $\text{N}_2$, mayoritario en moles, lo es aún más en masa.

## Inciso 2 — Presiones y volúmenes parciales

> [!solucion]
> **Dalton** (presión parcial $p_i = y_i\,p$, con $p = 2\ \text{atm}$):
> $$
> p_{\text{CO}_2} = 0{,}16, \quad p_{\text{H}_2\text{O}} = 0{,}22, \quad p_{\text{O}_2} = 0{,}14, \quad p_{\text{N}_2} = 1{,}48\ \text{atm}
> $$
> Su suma es $2\ \text{atm} = p$, como exige $\sum_i p_i = p$.
>
> **Amagat** (volumen parcial $V_i = y_i\,V$, con $V = 0{,}5\ \text{m}^3$):
> $$
> V_{\text{CO}_2} = 0{,}040, \quad V_{\text{H}_2\text{O}} = 0{,}055, \quad V_{\text{O}_2} = 0{,}035, \quad V_{\text{N}_2} = 0{,}370\ \text{m}^3
> $$
> Su suma es $0{,}5\ \text{m}^3 = V$. El análisis volumétrico coincide con el molar.

## Inciso 3 — Cantidad de mezcla

> [!solucion]
> Número de moles por la ecuación de estado de la mezcla ($1\ \text{atm} = 101{,}325\ \text{kPa}$, $R_u = 8{,}314\ \text{kJ/kmol·K}$):
> $$
> n = \frac{pV}{R_u T} = \frac{(2 \times 101{,}325)(0{,}5)}{8{,}314 \times 500} = 0{,}02437\ \text{kmol}
> $$
> Masa total:
> $$
> m = nM = 0{,}02437 \times 28{,}46 = 0{,}6936\ \text{kg}
> $$

> [!info] Verificación física
> $\sum p_i = p$ y $\sum V_i = V$ confirman la consistencia de Dalton y Amagat. La mezcla se trata como un [[Gas Ideal]] de masa molar $M = 28{,}46$, casi la del aire ($28{,}97$), lo que es razonable para productos de combustión dominados por $\text{N}_2$.

## Notas usadas

> [!referencia]
> [[Mezclas de Gases]] · [[Gas Ideal]] · [[Presion]] · [[Volumen Especifico]] · [[Temperatura]] · Moran & Shapiro, Ej. 12.1.

> [!info]
> **Convención de notación**:
> - $y_i$: fracción molar; $fm_i$: fracción másica; $M = \sum y_i M_i$ [kg/kmol].
> - $p_i = y_i p$: presión parcial (Dalton); $V_i = y_i V$: volumen parcial (Amagat).
