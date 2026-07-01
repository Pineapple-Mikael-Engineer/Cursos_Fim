---
title: "Examen Final Termodinámica I — MN121 2024-II"
order: 1
tags:
  - termodinamica
  - problemas
  - examen
  - index
draft: false
aliases:
  - Final Termo 2024-II
  - examen final MN121
---

# Examen Final de Termodinámica I — MN121 (2024-II)

> [!definicion]
> Resolución completa del examen final ($10/12/24$). Cubre todo el curso: ciclos de potencia (Rankine, Brayton), motores de combustión interna (Otto, Diesel), combustión con aire húmedo y psicrometría. Cada problema delega su teoría a las notas del vault.

## Problemas

> [!info]
> - [[P1 Rankine Recalentamiento | P1 — Rankine con recalentamiento]] (planta de 20 MW)
> - [[P2 Brayton Regeneracion Recalentamiento | P2 — Brayton con regeneración y recalentamiento]] (12 MW)
> - [[P3 Ciclo Otto | P3 — Motor de explosión (Otto)]]
> - [[P4 Ciclo Diesel | P4 — Motor Diesel (8 cilindros)]]
> - [[P5 Combustion Butano | P5 — Combustión de butano con aire húmedo]]
> - [[P6 Psicrometria Deshumidificacion | P6 — Psicrometría: enfriamiento y deshumidificación]]

> [!warning] Erratas detectadas en la clave manuscrita
> - **P2 (10):** la clave da $\eta=32{,}68\%$ porque ignora el regenerador en el calor aportado (incoherente con su propia $r_{a/c}$); lo correcto es $\eta\approx45\%$.
> - **P4 (18):** la clave da $1550$ kW; el cálculo $31\cdot\tfrac{1000}{120}\cdot8\cdot0{,}85$ da $\approx1757$ kW.

---

## Preguntas teóricas ($0{,}5$ pts c/u)

> [!proposicion] Pregunta 1 — La humedad a la salida de una turbina de vapor está limitada por:
> 1. La temperatura máxima del ciclo · 2. Las condiciones ambientales · 3. La erosión de los álabes de la turbina. **Respuesta: c) Sólo 3.** La humedad excesiva forma gotas que erosionan los álabes de baja presión; por eso se impone $x_{salida}\gtrsim0{,}88$ (y se usa [[Conversión de Energía/Ciclos de Potencia/Rankine/Rankine con Recalentamiento | recalentamiento]]).

> [!proposicion] Pregunta 2 — Sobre el ciclo Brayton teórico (V/F):
> 1. No se considera el efecto de los gases de combustión. · 2. Siempre es posible usar los gases de escape para calentar el aire que sale del compresor. · 3. El trabajo del compresor se considera despreciable. **Respuesta: d) VFV → en la clave, "VFF".** (1) **V**: en aire-estándar se modela todo con aire. (2) **F**: la regeneración solo es posible si $T_{escape}>T_{salida\ compresor}$. (3) **F**: en el Brayton el trabajo del compresor es una fracción grande (bwr alto), nunca despreciable.

> [!proposicion] Pregunta 3 — Sobre los motores Otto y Diesel (V/F):
> 1. A igual relación de compresión, el Diesel es más eficiente que el Otto. · 2. En general el Diesel tiene mayor relación de compresión que el Otto. · 3. La eficiencia de un Diesel solo depende de su relación de compresión. **Respuesta: a) FVF.** (1) **F**: a *igual* $r$, el Otto es más eficiente (el factor de corte $>1$ penaliza al Diesel). (2) **V**: el Diesel opera a $r$ mucho mayor (no hay autoignición prematura). (3) **F**: $\eta_{Diesel}$ depende de $r$ **y** de la relación de corte $r_c$.

> [!proposicion] Pregunta 4 — Sobre los motores Diesel (V/F):
> 1. La relación de corte es igual a la relación de compresión. · 2. El combustible diesel tiene un alto octanaje. · 3. La eficiencia del ciclo es variable. **Respuesta: d) FFV.** (1) **F**: $r_c=V_3/V_2\neq r_k=V_1/V_2$. (2) **F**: el diesel se caracteriza por su **cetanaje**, no octanaje. (3) **V**: $\eta$ varía con la carga (cambia $r_c$).
