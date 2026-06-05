---
title: "Mezclas de gases ideales"
tags:
  - termodinamica
  - mezclas
  - gas_ideal
  - formulario
draft: false
aliases:
  - Mezclas de Gases
  - ideal gas mixtures
  - mezcla no reactiva
  - Dalton
  - Amagat
---

# Mezclas de gases ideales

> [!definicion]
> Conjunto de $j$ gases no reactivos que coexisten a la misma temperatura $T$ y ocupan el mismo volumen $V$. Cada componente se modela como [[Gas Ideal]] y la mezcla global también. El estado de cada componente queda fijado por $T$ y su **presión parcial** $p_i$ (modelo de Dalton).

## Composición

> [!proposicion]
> Con $m_i = n_i M_i$ (masa = moles × masa molar del componente):
> $$
> \text{fracción másica: } fm_i = \frac{m_i}{m}, \qquad \text{fracción molar: } y_i = \frac{n_i}{n}
> $$
> $$
> \sum_i fm_i = 1, \qquad \sum_i y_i = 1
> $$
> **Masa molecular aparente** de la mezcla (promedio ponderado por fracción molar):
> $$
> M = \frac{m}{n} = \sum_i y_i M_i
> $$

> [!regla] Conversión entre análisis
> Cuando se desconoce la cantidad de mezcla, basar el cálculo en una **base cómoda**: $1\ \text{kmol}$ para pasar de molar a másico, o $100\ \text{kg}$ para pasar de másico a molar.
> $$
> fm_i = \frac{y_i M_i}{M} = \frac{y_i M_i}{\sum_k y_k M_k}, \qquad y_i = \frac{fm_i / M_i}{\sum_k fm_k / M_k}
> $$

## Relaciones $p\text{-}V\text{-}T$: Dalton y Amagat

> [!teorema]
> La mezcla satisface $pV = nR_u T$. Dos modelos equivalentes la descomponen:
>
> **Modelo de Dalton** — cada componente ocupa todo $V$ a $T$; su **presión parcial** es
> $$
> p_i = \frac{n_i R_u T}{V} = y_i\,p, \qquad \sum_i p_i = p
> $$
>
> **Modelo de Amagat** — cada componente está a $p$ y $T$; su **volumen parcial** es
> $$
> V_i = \frac{n_i R_u T}{p} = y_i\,V, \qquad \sum_i V_i = V
> $$
> Por eso el análisis volumétrico coincide con el molar: $V_i/V = y_i$.

## Propiedades de la mezcla

> [!proposicion]
> Las extensivas suman la contribución de cada componente. [[Energia Interna]] y [[Entalpia]] dependen solo de $T$; la [[Entropia]] de cada componente se evalúa a $T$ y a su presión parcial $p_i$. En base molar:
> $$
> \bar u = \sum_i y_i \bar u_i(T), \qquad \bar h = \sum_i y_i \bar h_i(T), \qquad \bar s = \sum_i y_i \bar s_i(T, p_i)
> $$
> $$
> \bar c_v = \sum_i y_i \bar c_{v,i}, \qquad \bar c_p = \sum_i y_i \bar c_{p,i}, \qquad k = \frac{\bar c_p}{\bar c_v}
> $$
> Conversión base molar ↔ másica con $M$: $\bar u = M u$, $\bar h = M h$, $\bar s = M s$, $\bar c_p = M c_p$.

## Cambios de propiedad (composición constante)

> [!teorema]
> Entre dos estados de la mezcla, por unidad de masa y con $c_p$, $c_v$ constantes:
> $$
> \Delta u = c_v\,(T_2 - T_1), \qquad \Delta h = c_p\,(T_2 - T_1)
> $$
> $$
> \Delta s = c_p \ln\frac{T_2}{T_1} - \frac{R_u}{M}\ln\frac{p_2}{p_1}
> $$
> A composición constante, el cociente de presiones parciales iguala al de la mezcla ($p_{i2}/p_{i1} = p_2/p_1$), por lo que basta la presión total. Con tablas de gas ideal (variable con $T$) se usan $\bar u_i(T)$, $\bar h_i(T)$ y $\bar s_i^{\circ}(T)$, con $\Delta \bar s_i = \bar s_i^{\circ}(T_2) - \bar s_i^{\circ}(T_1) - R_u \ln(p_2/p_1)$.

## Mezcla irreversible (formación de la mezcla)

> [!warning]
> Cuando gases inicialmente **separados** se mezclan, el proceso es **irreversible** y genera entropía. Tres causas independientes contribuyen: distinta temperatura inicial, distinta presión inicial, y ser **gases distintos** (mezcla difusiva). En la mezcla, cada componente pasa a su presión parcial $p_i = y_i p_2$:
> $$
> S_{gen} = \sum_i n_i\left[\bar c_{p,i}\ln\frac{T_2}{T_{i,1}} - R_u \ln\frac{y_i\,p_2}{p_{i,1}}\right] \;\ge\; 0
> $$

## Relación con otras notas

> [!info]
> - Cada componente y la mezcla son [[Gas Ideal | gases ideales]]; la versión real usa la regla de Kay sobre una [[Ecuaciones de Estado/index | ecuación de estado]].
> - Los balances no cambian: [[Primera Ley SC]], [[Segunda Ley SC]] y los de [[Volumenes de Control]] se aplican con las propiedades de la mezcla.
> - Problemas resueltos: [[Problema 05]], [[Problema 06]], [[Problema 07]], [[Problema 08]].
> - Caso particular aire–vapor de agua: psicrometría.

> [!referencia]
> Moran & Shapiro, *Fundamentos de Termodinámica Técnica*, Cap. 12 (mezclas no reactivas de gases ideales). Tablas A-1 (masas molares), A-20 (calores específicos), A-22/A-23 ($\bar u$, $\bar h$, $\bar s^{\circ}$ de gas ideal).

> [!info]
> **Convención de notación**:
> - $y_i$: fracción molar; $fm_i$: fracción másica; $M = \sum y_i M_i$: masa molecular aparente [kg/kmol].
> - $p_i = y_i p$: presión parcial; $V_i = y_i V$: volumen parcial; $R_u = 8.314\ \text{kJ/kmol·K}$.
> - barra: propiedad molar; $\bar s_i^{\circ}(T)$: entropía de referencia de tabla a $p = 1\ \text{atm}$.
