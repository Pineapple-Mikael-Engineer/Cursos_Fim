---
title: "Brayton Simple"
order: 1
tags:
  - termodinamica
  - ciclos
  - brayton
  - turbina_gas
draft: false
aliases:
  - Brayton Simple
  - ciclo Brayton ideal
  - air-standard Brayton
---

# Brayton Simple $\eta_{\rm th} = 1 - r_P^{-(\gamma-1)/\gamma}$

> [!definicion]
> El **ciclo Brayton simple** modela la turbina de gas con **cuatro estados** y la hipótesis aire-estándar (aire ideal de $c_p$ constante). Los cuatro procesos:
>
> - **1→2:** Compresión isentrópica en el compresor (del ambiente a alta presión).
> - **2→3:** Adición de calor isobárica en la cámara de combustión (hasta $T_3$, temperatura máxima).
> - **3→4:** Expansión isentrópica en la turbina (de $P_H$ al ambiente).
> - **4→1:** Rechazo de calor isobárico al ambiente (o equivalente en ciclo abierto: purga de gases).
>
> *Diferencia con el ciclo real:* las turbinas de gas industriales operan en ciclo **abierto**: aspiran aire fresco y descargan gases quemados. El análisis aire-estándar trata el ciclo como cerrado con $c_p = 1.005\,\mathrm{kJ/(kg\cdot K)}$, $\gamma = 1.4$ para aire a $\approx 300\,\mathrm{K}$.

---

## Identificación de estados

| Estado | Descripción | Condición |
|:---:|:---|:---|
| 1 | Entrada del compresor | $T_1$, $P_L$ (ambiente) |
| 2 | Salida del compresor = entrada cámara | $T_2$, $P_H$ |
| 3 | Salida cámara = entrada turbina | $T_3$ (máxima), $P_H$ |
| 4 | Salida turbina = descarga | $T_4$, $P_L$ |

La **relación de presiones** $r_P = P_H / P_L$ es el parámetro de diseño fundamental.

---

## Balances de energía (base 1 kg)

> [!proposicion]
> **Trabajo del compresor** (por unidad de masa aspirada):
> $$
> w_C = c_p(T_2 - T_1) \quad [\mathrm{kJ/kg}].
> $$
>
> **Calor de entrada** (cámara de combustión):
> $$
> q_H = c_p(T_3 - T_2) \quad [\mathrm{kJ/kg}].
> $$
>
> **Trabajo de turbina:**
> $$
> w_T = c_p(T_3 - T_4) \quad [\mathrm{kJ/kg}].
> $$
>
> **Trabajo neto:**
> $$
> w_{\rm neto} = w_T - w_C = c_p[(T_3 - T_4) - (T_2 - T_1)].
> $$

---

## Eficiencia y relaciones isentrópicas

> [!teorema]
> Para el ciclo Brayton ideal aire-estándar con $r_P = P_H/P_L$:
> $$
> \boxed{\eta_{\rm th} = 1 - \frac{1}{r_P^{(\gamma-1)/\gamma}}}.
> $$

> [!demostracion]
> **Hipótesis:** gas ideal, $c_p$ constante ($\gamma = 1.4$ para aire), procesos 1→2 y 3→4 isentrópicos, 2→3 y 4→1 isobáricos.
>
> **Paso 1 — Eficiencia en función de temperaturas:**
> $$
> \eta_{\rm th} = \frac{w_{\rm neto}}{q_H} = \frac{c_p[(T_3-T_4)-(T_2-T_1)]}{c_p(T_3-T_2)} = 1 - \frac{T_4-T_1}{T_3-T_2}.
> $$
>
> **Paso 2 — Relaciones isentrópicas.** Para gas ideal, proceso isentrópico: $T P^{-(\gamma-1)/\gamma} = \text{cte}$. Compresor (1→2):
> $$
> \frac{T_2}{T_1} = \left(\frac{P_H}{P_L}\right)^{(\gamma-1)/\gamma} = r_P^{(\gamma-1)/\gamma} \equiv t.
> \tag{A}
> $$
> Turbina (3→4): misma relación de presiones, mismo exponente:
> $$
> \frac{T_3}{T_4} = r_P^{(\gamma-1)/\gamma} = t \implies T_4 = \frac{T_3}{t}.
> \tag{B}
> $$
>
> **Paso 3 — Expresar $T_2$ y $T_4$:** $T_2 = t\,T_1$ y $T_4 = T_3/t$.
>
> **Paso 4 — Sustituir en $\eta_{\rm th}$:**
> $$
> \eta_{\rm th} = 1 - \frac{T_3/t - T_1}{T_3 - t\,T_1} = 1 - \frac{(T_3 - t\,T_1)/t}{T_3 - t\,T_1} = 1 - \frac{1}{t}.
> $$
>
> **Paso 5 — Resultado en términos de $r_P$:**
> $$
> \eta_{\rm th} = 1 - \frac{1}{r_P^{(\gamma-1)/\gamma}}. \qquad \blacksquare
> $$
>
> **Verificación (caso límite):** si $r_P = 1$, $t=1$, $\eta_{\rm th}=0$ (sin compresión no hay ciclo). Si $r_P \to \infty$, $\eta_{\rm th} \to 1$ (no físico: límite de materiales). Para $r_P = 10$: $\eta_{\rm th} = 1 - 1/10^{0.2857} = 1 - 1/1.931 = 48.2\%$.

---

## Ciclo Brayton real con eficiencias isentrópicas

> [!proposicion]
> Los dispositivos reales son irreversibles. Las eficiencias isentrópicas corrigen los estados 2 y 4:
>
> **Compresor real** (necesita más trabajo que el ideal):
> $$
> \eta_C = \frac{w_{C,{\rm ideal}}}{w_{C,{\rm real}}} = \frac{T_{2s}-T_1}{T_{2r}-T_1} \implies T_{2r} = T_1 + \frac{T_{2s}-T_1}{\eta_C}.
> $$
>
> **Turbina real** (produce menos trabajo):
> $$
> \eta_T = \frac{w_{T,{\rm real}}}{w_{T,{\rm ideal}}} = \frac{T_3-T_{4r}}{T_3-T_{4s}} \implies T_{4r} = T_3 - \eta_T(T_3-T_{4s}).
> $$
>
> Con estas correcciones:
> $$
> w_{\rm neto,r} = c_p[(T_3-T_{4r}) - (T_{2r}-T_1)], \qquad \eta_{\rm th,r} = \frac{w_{\rm neto,r}}{q_{H,r}}.
> $$
>
> *Efecto del bwr alto:* como el compresor consume ~40–60% del trabajo de la turbina, pequeñas ineficiencias en el compresor ($\eta_C < 1$) o la turbina ($\eta_T < 1$) reducen drásticamente la eficiencia neta. Comparar con Rankine donde bwr $\approx 1\%$ y las irreversibilidades en la bomba son insignificantes.

---

## Temperatura de salida de la turbina

> [!teoria]
> En el ciclo Brayton ideal, la temperatura de salida de la turbina $T_4$ es:
> $$
> T_4 = \frac{T_3}{r_P^{(\gamma-1)/\gamma}} = \frac{T_3}{t}.
> $$
>
> Si $T_3 = 1400\,\mathrm{K}$ y $r_P = 10$: $T_4 = 1400/1.931 = 725\,\mathrm{K}$ (452°C). Este calor residual es recuperable mediante un **regenerador**, lo que motiva el ciclo con regeneración. Condición necesaria para que el regenerador sea útil: $T_4 > T_2$.
>
> $$
> T_4 > T_2 \iff \frac{T_3}{t} > t\,T_1 \iff T_3 T_1 > t^2 T_1^2 \iff \frac{T_3}{T_1} > r_P^{2(\gamma-1)/\gamma}.
> $$
>
> Para $T_3/T_1 = 1400/300 = 4.67$ y $\gamma=1.4$: el regenerador es útil si $r_P < (4.67)^{1/0.5714} = (4.67)^{1.75} \approx 17$. A $r_P$ muy altos, el ciclo regenerativo deja de tener ventaja.

---

## Ejemplo: turbina de gas con $r_P = 10$

> [!ejemplo]
> Ciclo Brayton ideal con aire como fluido de trabajo:
> - Condiciones de entrada al compresor: $T_1 = 300\,\mathrm{K}$, $P_1 = 100\,\mathrm{kPa}$.
> - Relación de presiones: $r_P = 10$.
> - Temperatura máxima del ciclo: $T_3 = 1400\,\mathrm{K}$.
> - Propiedades del aire: $c_p = 1.005\,\mathrm{kJ/(kg\cdot K)}$, $\gamma = 1.4$.
>
> Determinar: (a) temperaturas en todos los estados; (b) $w_C$, $w_T$, bwr; (c) $q_H$, $\eta_{\rm th}$; (d) comparar con ciclo real si $\eta_C = 0.82$, $\eta_T = 0.86$.

> [!solucion]
> **(a) Temperaturas:**
>
> $t = r_P^{(\gamma-1)/\gamma} = 10^{(1.4-1)/1.4} = 10^{0.2857} = 1.9307$.
>
> Estado 2 (salida compresor ideal):
> $T_{2s} = T_1 \cdot t = 300 \times 1.9307 = 579.2\,\mathrm{K}$.
>
> Estado 4 (salida turbina ideal):
> $T_{4s} = T_3 / t = 1400 / 1.9307 = 725.1\,\mathrm{K}$.
>
> **(b) Trabajos y bwr (ciclo ideal):**
>
> $w_C = c_p(T_{2s}-T_1) = 1.005 \times (579.2-300) = 1.005 \times 279.2 = 280.6\,\mathrm{kJ/kg}$.
>
> $w_T = c_p(T_3-T_{4s}) = 1.005 \times (1400-725.1) = 1.005 \times 674.9 = 678.3\,\mathrm{kJ/kg}$.
>
> $w_{\rm neto} = 678.3 - 280.6 = 397.7\,\mathrm{kJ/kg}$.
>
> $\text{bwr} = w_C/w_T = 280.6/678.3 = 0.414$ (el compresor consume el **41.4%** del trabajo de turbina).
>
> **(c) Calor y eficiencia (ciclo ideal):**
>
> $q_H = c_p(T_3-T_{2s}) = 1.005 \times (1400-579.2) = 1.005 \times 820.8 = 824.9\,\mathrm{kJ/kg}$.
>
> $$\eta_{\rm th} = \frac{w_{\rm neto}}{q_H} = \frac{397.7}{824.9} = 0.482 = 48.2\%.$$
>
> Verificación: $\eta = 1 - 1/1.9307 = 1 - 0.518 = 0.482$ ✓.
>
> **(d) Ciclo real** ($\eta_C = 0.82$, $\eta_T = 0.86$):
>
> $T_{2r} = T_1 + (T_{2s}-T_1)/\eta_C = 300 + 279.2/0.82 = 300 + 340.5 = 640.5\,\mathrm{K}$.
>
> $T_{4r} = T_3 - \eta_T(T_3-T_{4s}) = 1400 - 0.86 \times 674.9 = 1400 - 580.4 = 819.6\,\mathrm{K}$.
>
> $w_{C,r} = 1.005 \times (640.5-300) = 342.1\,\mathrm{kJ/kg}$.
>
> $w_{T,r} = 1.005 \times (1400-819.6) = 583.3\,\mathrm{kJ/kg}$.
>
> $w_{\rm neto,r} = 583.3 - 342.1 = 241.2\,\mathrm{kJ/kg}$.
>
> $q_{H,r} = 1.005 \times (1400-640.5) = 763.2\,\mathrm{kJ/kg}$.
>
> $$\eta_{\rm th,r} = \frac{241.2}{763.2} = 0.316 = 31.6\%.$$
>
> | Parámetro | Ideal | Real |
> |:---:|:---:|:---:|
> | $T_2$ [K] | 579.2 | 640.5 |
> | $T_4$ [K] | 725.1 | 819.6 |
> | $w_C$ [kJ/kg] | 280.6 | 342.1 |
> | $w_T$ [kJ/kg] | 678.3 | 583.3 |
> | $w_{\rm neto}$ [kJ/kg] | 397.7 | 241.2 |
> | bwr | 41.4% | 58.6% |
> | $\eta_{\rm th}$ | **48.2%** | **31.6%** |
>
> La eficiencia cae de 48.2% a 31.6% por las irreversibilidades — una reducción del 34%. El bwr alto amplifica el efecto: el compresor consume más (+22% de trabajo) y la turbina produce menos (-14%).
>
> La temperatura de salida de la turbina real es $T_{4r} = 819.6\,\mathrm{K}$ (vs $725.1\,\mathrm{K}$ ideal). Este calor puede recuperarse con un regenerador → ver [[Brayton con Regeneración]].
>
> $\boxed{\eta_{\rm th,ideal} = 48.2\%,\quad \eta_{\rm th,real} = 31.6\%.}$ $\blacksquare$

> [!referencia]
> Borgnakke & Sonntag, §12.1–12.2; Çengel & Boles, §9-6 a 9-8; Moran & Shapiro, §9.5–9.6.
