---
title: "Volumen específico $v$"
tags:
  - termodinamica
  - propiedades
  - variables_de_estado
  - volumen_especifico
draft: false
aliases:
  - specific volume
  - v
  - volumen especifico
---

# Volumen específico $v$

> [!definicion]
> Propiedad **intensiva**: volumen por unidad de masa,
> $$
> v = \frac{V}{m} \quad [\text{m}^3/\text{kg}]
> $$
>
> Es el inverso de la densidad: $v = 1/\rho$. Su versión molar es $\bar{v} = V/n = M v$, con $M$ la masa molar.

## Específico, total y molar

> [!proposicion]
> | Magnitud | Símbolo | Unidad |
> |:---|:---|:---|
> | Volumen total (extensivo) | $V$ | m³ |
> | Volumen específico (por masa) | $v = V/m$ | m³/kg |
> | Volumen molar (por mol) | $\bar{v} = V/n$ | m³/mol |
>
> La distinción mayúscula/minúscula es general en el vault: la mayúscula denota la propiedad **extensiva** total; la minúscula, la **específica**; la barra, la **molar**.

## Región bifásica

> [!proposicion]
> En la mezcla líquido–vapor, el volumen específico se obtiene por la regla de la palanca a partir de la [[Calidad]] $x$:
> $$
> v = v_f + x\,v_{fg}, \qquad v_{fg} = v_g - v_f
> $$
> - $v_f$: volumen específico del líquido saturado.
> - $v_g$: volumen específico del vapor saturado.
>
> La misma forma vale para cualquier propiedad específica ($u$, $h$, $s$): $y = y_f + x\,y_{fg}$.

> [!ejemplo]
> **Mezcla agua líquido–vapor a $100\ ^\circ\text{C}$.** De tablas: $v_f = 0.001044\ \text{m}^3/\text{kg}$, $v_g = 1.6720\ \text{m}^3/\text{kg}$. Para calidad $x = 0.6$:
> $$
> v = 0.001044 + 0.6\,(1.6720 - 0.001044) = 0.001044 + 0.6\,(1.6710) = 1.0037\ \text{m}^3/\text{kg}
> $$
> El resultado está dominado por la fase vapor, consistente con $v_g \gg v_f$.

## Casos límite

> [!proposicion]
> **Gas ideal:** de $Pv = RT$,
> $$
> v = \frac{RT}{P}
> $$
>
> **Líquido o sólido (incompresible):** $v \approx v_f(T)$, prácticamente independiente de la presión. En cálculos de [[Entalpia]] de líquidos comprimidos se aproxima $h(T,P) \approx h_f(T) + v_f\,[P - P_{sat}(T)]$.

## Papel en el estado termodinámico

> [!teoria]
> Con [[Presion]] y [[Temperatura]], el volumen específico completa el trío de variables de estado de la sustancia simple compresible. En las regiones de una sola fase, $(P,T)$ determinan $v$ a través de la [[Ecuaciones de Estado/index | ecuación de estado]]; en la región bifásica, $(P,T)$ son dependientes y $v$ depende de la [[Calidad]].

## Relación con otras propiedades

> [!info]
> - Trabajo de frontera específico en proceso cuasiestático: $w = \int P\,dv$.
> - Variable natural de la [[Energia Interna]] (a través de $S$ y $V$) y presente en $H = U + PV$ (ver [[Entalpia]]).
> - Derivada de Maxwell asociada (desde $dG$): $\left(\dfrac{\partial S}{\partial P}\right)_T = -\left(\dfrac{\partial v}{\partial T}\right)_P$ (forma específica), ver [[Maxwell]].

> [!info]
> **Convención de notación**:
> - $v$: volumen específico [m³/kg]; $\bar{v}$: molar [m³/mol]; $V$: total [m³]
> - $v_f$, $v_g$: líquido y vapor saturados; $v_{fg} = v_g - v_f$
> - $\rho = 1/v$: densidad [kg/m³]
