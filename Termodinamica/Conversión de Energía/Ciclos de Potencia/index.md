---
title: "Ciclos de Potencia"
order: 1
tags:
  - termodinamica
  - ciclos
  - ciclos_potencia
  - index
draft: false
aliases:
  - Ciclos de Potencia
  - Power Cycles
---

# Ciclos de Potencia

> [!definicion]
> Un **ciclo de potencia** convierte de forma neta calor en trabajo mecánico. Opera recibiendo calor $q_H$ de una fuente de alta temperatura $T_H$, produciendo trabajo neto $w_{\rm neto} = q_H - q_L$, y rechazando el resto $q_L$ a un sumidero de baja temperatura $T_L$. La **eficiencia térmica** mide qué fracción del calor recibido se convierte en trabajo:
> $$
> \eta_{\rm th} = \frac{w_{\rm neto}}{q_H} = 1 - \frac{q_L}{q_H} \leq 1 - \frac{T_L}{T_H}.
> $$
> El límite superior es la eficiencia de **Carnot**: un ciclo que opera con solo 2 procesos isotérmicos y 2 isentrópicos es el más eficiente posible entre $T_H$ y $T_L$.

---

## Representación en el diagrama $T$-$s$

> [!teoria]
> En el diagrama $T$-$s$, el área encerrada por el ciclo es el **trabajo neto** producido:
> $$
> w_{\rm neto} = \oint T\,ds.
> $$
> El área bajo la curva de proceso de calor de entrada es $q_H$; el área bajo la de rechazo es $q_L$. El **ciclo de Carnot** es un rectángulo en el diagrama $T$-$s$: dos líneas horizontales ($T_H$ y $T_L$) y dos verticales ($s = \text{cte}$).
>
> Todo ciclo real que se acerque a la forma rectangular en el $T$-$s$ tiene mayor eficiencia. El ciclo Rankine mejora con recalentamiento y regeneración precisamente porque eleva la temperatura promedio de adición de calor.

![[Ts_comparacion_ciclos_potencia.svg|460]]
*Diagrama $T$-$s$ comparando el ciclo de Carnot (rectángulo ideal) con el Rankine simple y el Rankine con recalentamiento. La zona sombreada es el trabajo neto. El Rankine simple tiene una cola triangular por debajo de $T_H$ que reduce la eficiencia respecto al Carnot.*

---

## Temperatura media de adición de calor $T_m$

> [!proposicion]
> Para comparar ciclos, es útil definir la **temperatura media de adición de calor**:
> $$
> T_{m,\rm entrada} = \frac{q_H}{\Delta s_{\rm entrada}} = \frac{\int T\,ds}{\Delta s},
> $$
> tal que un ciclo de Carnot operando entre $T_{m,\rm entrada}$ y $T_L$ tiene la misma eficiencia. Mejorar un ciclo real = aumentar $T_{m,\rm entrada}$ o reducir $T_L$.

---

## Eficiencias reales vs. Carnot

| Ciclo | $\eta_{\rm Carnot}$ aprox. | $\eta_{\rm th}$ típica real |
|:---:|:---:|:---:|
| Rankine simple | $\approx 55\%$ ($T_H=500°\mathrm{C}$, $T_L=30°\mathrm{C}$) | $30$–$40\%$ |
| Rankine recalentado | $\approx 60\%$ | $35$–$45\%$ |
| Brayton simple | $\approx 65\%$ ($T_H=1400°\mathrm{C}$, $T_L=25°\mathrm{C}$) | $25$–$40\%$ |
| Brayton combinado | — | $50$–$65\%$ |

---

## Mapa de notas

> [!info]
> - [[Rankine/index | Rankine]] — ciclo de vapor de agua para plantas eléctricas.
>   - [[Rankine/Rankine Simple | Rankine Simple]] — ciclo de 4 estados; eficiencia base; ejemplo.
>   - [[Rankine/Rankine con Recalentamiento | Rankine con Recalentamiento]] — evita vapor húmedo; mejora $\eta$.
>   - [[Rankine/Rankine Regenerativo | Rankine Regenerativo]] — extracción de vapor; calentador abierto.
> - [[Brayton/index | Brayton]] — ciclo de turbina de gas (aire-estándar).
>   - [[Brayton/Brayton Simple | Brayton Simple]] — ciclo ideal; $\eta = 1 - r_p^{-(γ-1)/γ}$.
>   - [[Brayton/Brayton con Regeneración | Brayton con Regeneración]] — recuperador de calor de escape.

> [!referencia]
> Çengel & Boles, *Termodinámica*, caps. 9–10; Borgnakke & Sonntag, caps. 11–12; Moran & Shapiro, §9.1–9.2.
