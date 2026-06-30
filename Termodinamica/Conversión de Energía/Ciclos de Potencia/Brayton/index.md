---
title: "Ciclo Brayton"
order: 2
tags:
  - termodinamica
  - ciclos
  - brayton
  - turbina_gas
  - index
draft: false
aliases:
  - Ciclo Brayton
  - Brayton cycle
  - turbina de gas
  - gas turbine cycle
---

# Ciclo Brayton

> [!definicion]
> El **ciclo Brayton** es el ciclo termodinámico de las **turbinas de gas**: motores a reacción de aviación, turbinas industriales de generación y cogeneración, y ciclos combinados. A diferencia del Rankine, el fluido de trabajo es un **gas** (normalmente aire) que permanece en fase gaseosa durante todo el ciclo. El análisis estándar usa la **hipótesis aire-estándar**: el ciclo se modela con aire (gas ideal, $\gamma = 1.4$) en lugar de mezcla combustible/productos reales.
>
> El ciclo de 4 procesos: compresión isentrópica (1→2), adición de calor isobárica (2→3, cámara de combustión), expansión isentrópica (3→4, turbina), y rechazo de calor isobárico (4→1, al ambiente).
>
> *Diferencia clave con Rankine:* en el Brayton no hay cambio de fase. La **relación de retrabajo** (bwr) es mucho mayor (~40–80%) porque comprimir un gas consume mucha más energía que comprimir un líquido. La turbina produce trabajo, pero el compresor consume una parte significativa de él.

![[brayton_esquema_dispositivos.svg|500]]
*Ciclo Brayton ideal de turbina de gas. El compresor aspira aire a las condiciones ambientales (estado 1) y lo comprime a $P_H$ (estado 2). La cámara de combustión añade calor a presión constante hasta $T_3$ (temperatura máxima del ciclo). La turbina expande los gases de $P_H$ a $P_L$ (estado 4), produciendo trabajo neto.*

---

## Diagramas $T$-$s$ y $P$-$v$

![[brayton_diagrama_Ts.svg|440]]
*Diagrama $T$-$s$ del ciclo Brayton ideal. El compresor (1→2) y la turbina (3→4) son líneas verticales (isentrópicas). La adición de calor (2→3) y el rechazo (4→1) son líneas a $P$ constante. La eficiencia es la razón entre el área encerrada y el área bajo la curva 2→3.*

---

## Eficiencia del ciclo Brayton ideal

> [!teorema]
> Para el ciclo Brayton ideal (aire-estándar, $c_p$ constante, procesos isentrópicos), la eficiencia térmica depende únicamente de la **relación de presiones** $r_P = P_H/P_L$:
> $$
> \eta_{\rm th,Brayton} = 1 - \frac{1}{r_P^{(\gamma-1)/\gamma}}.
> $$

> [!teoria]
> El rasgo notable es que $\eta$ **solo depende de $r_P$**, no de la temperatura máxima $T_3$. La razón aparece al escribir los calores $q_H=c_p(T_3-T_2)$ y $q_L=c_p(T_4-T_1)$ y usar las relaciones isentrópicas $\dfrac{T_2}{T_1}=\dfrac{T_3}{T_4}=r_P^{(\gamma-1)/\gamma}\equiv t$: las dos temperaturas extremas se factorizan en $\eta=1-\dfrac{T_4-T_1}{T_3-T_2}$ y queda $\eta=1-1/t$. La **derivación paso a paso** y el ejemplo numérico completo están en [[Brayton Simple]].
>
> *Consecuencia de diseño:* subir $r_P$ siempre mejora $\eta$, pero el límite lo fija la temperatura máxima admisible por los materiales de la turbina (que acota $T_3$ y, con ella, el trabajo neto por unidad de masa). El compromiso entre $\eta$ (favorece $r_P$ alto) y trabajo neto (tiene un óptimo intermedio) es el criterio central de diseño del Brayton.

---

## Relación de retrabajo (bwr)

> [!proposicion]
> $$
> \text{bwr} = \frac{w_C}{w_T} = \frac{c_p(T_2-T_1)}{c_p(T_3-T_4)} = \frac{T_2-T_1}{T_3-T_4} = \frac{T_1}{T_3}\cdot r_P^{(\gamma-1)/\gamma}.
> $$
> Para $r_P = 10$, $T_1 = 300\,\mathrm{K}$, $T_3 = 1400\,\mathrm{K}$: bwr $\approx 0.3\times1.931 = 0.579$, es decir, el compresor consume el 58% del trabajo de la turbina. Comparar con el Rankine donde bwr $\approx 1\%$.

---

## Mapa de notas

> [!info]
> - [[Brayton Simple]] — ciclo ideal y real; eficiencia $\eta = 1 - r_P^{-(γ-1)/γ}$; ejemplo completo.
> - [[Brayton con Regeneración]] — recuperador de calor del escape; $\eta_{\rm regen}$ y efectividad.

> [!referencia]
> Borgnakke & Sonntag, §12.1–12.2; Çengel & Boles, §9-6 a 9-8; Moran & Shapiro, §9.5–9.6.
