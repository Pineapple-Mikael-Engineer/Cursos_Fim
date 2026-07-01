---
title: "Brayton con Regeneración"
order: 2
tags:
  - termodinamica
  - ciclos
  - brayton
  - regeneracion
  - recuperador
draft: false
aliases:
  - Brayton con Regeneración
  - Brayton regenerativo
  - ciclo Brayton recuperado
---

# Brayton con Regeneración $\eta_{\rm regen} = 1 - \frac{T_1}{T_3}\,r_P^{(\gamma-1)/\gamma}$

> [!definicion]
> En el ciclo Brayton simple los gases de escape salen de la turbina a alta temperatura ($T_4 \approx 700{-}900\,\mathrm{K}$) y ese calor se pierde al ambiente. En el **ciclo Brayton con regeneración**, un **recuperador de calor** (intercambiador regenerativo) usa esos gases calientes para **precalentar el aire comprimido** antes de entrar a la cámara de combustión.
>
> *Beneficio:* el aire entra a la cámara a mayor temperatura ($T_5 > T_2$), por lo que se necesita quemar menos combustible para alcanzar $T_3$. El calor que antes era residuo ahora hace trabajo interno al ciclo.
>
> *Condición necesaria:* para que el recuperador sea beneficioso, la temperatura de salida de la turbina debe ser mayor que la de salida del compresor: $T_4 > T_2$. Esto requiere $T_3/T_1 > r_P^{2(\gamma-1)/\gamma}$, es decir, es útil a **bajos $r_P$** y alta $T_3/T_1$.

---

## Diagrama y estados

![[brayton_regeneracion_esquema.svg|500]]
*Ciclo Brayton con regenerador. El compresor comprime el aire (1→2). El recuperador transfiere calor de los gases de escape (4→6) al aire comprimido (2→5). La cámara de combustión eleva la temperatura de 5 a 3. La turbina expande (3→4). El recuperador enfría el escape antes de descargarlo al ambiente.*

| Estado | Descripción | Condición |
|:---:|:---|:---|
| 1 | Entrada compresor | $T_1$, $P_L$ |
| 2 | Salida compresor | $T_2 = T_1 r_P^{(\gamma-1)/\gamma}$, $P_H$ |
| 5 | Salida recuperador (lado frío) | $T_5$, $P_H$ |
| 3 | Salida cámara de combustión | $T_3$ (máxima), $P_H$ |
| 4 | Salida turbina | $T_4 = T_3/r_P^{(\gamma-1)/\gamma}$, $P_L$ |
| 6 | Salida recuperador (lado caliente) | $T_6$, $P_L$ |

---

## Efectividad del recuperador

> [!definicion]
> La **efectividad** $\varepsilon$ mide qué fracción del máximo posible de transferencia de calor ocurre realmente en el recuperador:
> $$
> \varepsilon = \frac{q_{\rm real}}{q_{\rm max}} = \frac{T_5 - T_2}{T_4 - T_2}.
> $$
>
> El máximo ocurre cuando el lado frío sale a la temperatura del lado caliente: $T_{5,\rm max} = T_4$ (recuperador infinitamente largo). En la práctica, $\varepsilon = 0.65{-}0.85$ para recuperadores bien diseñados.
>
> Entonces: $T_5 = T_2 + \varepsilon(T_4 - T_2)$.
>
> Y por balance de energía (fluidos con $c_p$ igual, mismo $\dot{m}$): $T_6 = T_4 - (T_5 - T_2) = T_4 - \varepsilon(T_4 - T_2)$.

---

## Eficiencia del ciclo Brayton con regeneración ideal ($\varepsilon = 1$)

> [!teorema]
> Para el ciclo Brayton con regeneración **perfecta** ($\varepsilon = 1$, es decir $T_5 = T_4$ y $T_6 = T_2$):
> $$
> \boxed{\eta_{\rm th,regen} = 1 - \frac{T_1}{T_3}\,r_P^{(\gamma-1)/\gamma}}.
> $$

> [!demostracion]
> **Hipótesis:** gas ideal, $c_p$ constante, recuperador perfecto ($T_5 = T_4$, $T_6 = T_2$), procesos 1→2 y 3→4 isentrópicos, 2→5 y 4→6 isobáricos (sin pérdida de presión en el recuperador).
>
> **Paso 1 — Calor de entrada con regeneración.** El aire que entra a la cámara ya está a $T_5 = T_4$, por lo que solo se necesita calentarlo de $T_4$ a $T_3$:
> $$
> q_H = c_p(T_3 - T_5) = c_p(T_3 - T_4).
> $$
>
> **Paso 2 — Trabajo neto.** No cambia respecto al ciclo simple (el recuperador no produce ni consume trabajo de eje):
> $$
> w_{\rm neto} = c_p[(T_3-T_4)-(T_2-T_1)].
> $$
>
> **Paso 3 — Eficiencia:**
> $$
> \eta_{\rm th} = \frac{w_{\rm neto}}{q_H} = \frac{(T_3-T_4)-(T_2-T_1)}{T_3-T_4} = 1 - \frac{T_2-T_1}{T_3-T_4}.
> $$
>
> **Paso 4 — Relaciones isentrópicas.** Sea $t = r_P^{(\gamma-1)/\gamma}$: $T_2 = t\,T_1$ y $T_4 = T_3/t$.
> $$
> T_2 - T_1 = T_1(t-1), \qquad T_3 - T_4 = T_3\left(1-\frac{1}{t}\right) = T_3\frac{t-1}{t}.
> $$
>
> **Paso 5 — Sustituir:**
> $$
> \eta_{\rm th} = 1 - \frac{T_1(t-1)}{T_3(t-1)/t} = 1 - \frac{T_1\,t}{T_3} = 1 - \frac{T_1}{T_3}\,r_P^{(\gamma-1)/\gamma}. \qquad \blacksquare
> $$
>
> **Verificación:**
> - Si $r_P = 1$: $\eta = 1 - T_1/T_3$. Sin compresión, el ciclo Brayton regenerado se comporta como Carnot inverso entre $T_1$ y $T_3$.
> - Conforme $r_P$ aumenta: $\eta_{\rm regen}$ **disminuye** (¡a diferencia del Brayton simple donde aumenta con $r_P$!). Esto ocurre porque con más compresión, $T_2$ sube, y si $T_2 \geq T_4$ el regenerador ya no puede transferir calor.

---

## Comparación con el ciclo Brayton simple

| Parámetro | Brayton Simple | Brayton con Regeneración (ε=1) |
|:---:|:---:|:---:|
| $\eta_{\rm th}$ | $1 - r_P^{-(\gamma-1)/\gamma}$ | $1 - (T_1/T_3)\,r_P^{(\gamma-1)/\gamma}$ |
| Efecto de $r_P$ | $\eta\uparrow$ con $r_P$ | $\eta\downarrow$ con $r_P$ |
| $q_H$ | $c_p(T_3-T_2)$ | $c_p(T_3-T_4)$ |
| Condición de mejora | — | $T_4 > T_2$, i.e. $r_P$ bajo |

> [!info]
> Para $T_3/T_1 = 5$ y $\gamma = 1.4$, los dos ciclos tienen la misma eficiencia a $r_P^* = (T_3/T_1)^{\gamma/(2(\gamma-1))} = 5^{1.75} \approx 18.3$. Para $r_P < 18.3$, el regenerativo es más eficiente; para $r_P > 18.3$, el regenerador en realidad enfría el aire y deja de ser útil.

---

## Ejemplo: ciclo regenerativo con $r_P = 6$

> [!ejemplo]
> Ciclo Brayton con regeneración:
> - Entrada compresor: $T_1 = 300\,\mathrm{K}$, $P_L = 100\,\mathrm{kPa}$.
> - $r_P = 6$, $T_3 = 1200\,\mathrm{K}$.
> - Propiedades del aire: $c_p = 1.005\,\mathrm{kJ/(kg\cdot K)}$, $\gamma = 1.4$.
> - Efectividad del recuperador: $\varepsilon = 0.75$.
> - Eficiencias isentrópicas: $\eta_C = \eta_T = 1$ (ciclo ideal).
>
> Determinar: (a) temperaturas en todos los estados; (b) $q_H$, $\eta_{\rm th}$; (c) comparar con Brayton simple a las mismas condiciones.

> [!solucion]
> **Paso 1 — Parámetro isentrópico:** $t = r_P^{(\gamma-1)/\gamma} = 6^{0.2857} = 6^{4/14} = e^{(4/14)\ln6} = e^{0.2857 \times 1.7918} = e^{0.5119} = 1.668$.
>
> **Estado 2** (compresor ideal): $T_2 = T_1 \cdot t = 300 \times 1.668 = 500.4\,\mathrm{K}$.
>
> $w_C = c_p(T_2-T_1) = 1.005 \times 200.4 = 201.4\,\mathrm{kJ/kg}$.
>
> **Estado 4** (turbina ideal): $T_4 = T_3/t = 1200/1.668 = 719.4\,\mathrm{K}$.
>
> $w_T = c_p(T_3-T_4) = 1.005 \times 480.6 = 483.0\,\mathrm{kJ/kg}$.
>
> $w_{\rm neto} = 483.0 - 201.4 = 281.6\,\mathrm{kJ/kg}$.
>
> **Verificación de condición de recuperación:** $T_4 = 719.4\,\mathrm{K} > T_2 = 500.4\,\mathrm{K}$ ✓.
>
> **Estado 5** (salida recuperador, lado frío, $\varepsilon = 0.75$): $T_5 = T_2 + \varepsilon(T_4-T_2) = 500.4 + 0.75 \times (719.4-500.4) = 500.4 + 0.75 \times 219.0 = 500.4 + 164.3 = 664.7\,\mathrm{K}$.
>
> **Estado 6** (salida recuperador, lado caliente): $T_6 = T_4 - (T_5-T_2) = 719.4 - 164.3 = 555.1\,\mathrm{K}$.
>
> **(a) Temperaturas:** $T_1 = 300$, $T_2 = 500.4$, $T_5 = 664.7$, $T_3 = 1200$, $T_4 = 719.4$, $T_6 = 555.1$ (todas en K).
>
> **(b) Calor y eficiencia con regeneración:**
>
> $q_H = c_p(T_3-T_5) = 1.005 \times (1200-664.7) = 1.005 \times 535.3 = 538.0\,\mathrm{kJ/kg}$.
>
> $$\eta_{\rm th,regen} = \frac{w_{\rm neto}}{q_H} = \frac{281.6}{538.0} = 0.523 = 52.3\%.$$
>
> **(c) Brayton simple a $r_P = 6$, $T_3 = 1200\,\mathrm{K}$:**
>
> $q_{H,\rm simple} = c_p(T_3-T_2) = 1.005 \times (1200-500.4) = 1.005 \times 699.6 = 703.0\,\mathrm{kJ/kg}$.
>
> $\eta_{\rm th,simple} = w_{\rm neto}/q_{H,\rm simple} = 281.6/703.0 = 0.401 = 40.1\%$.
>
> Verificación fórmula: $\eta = 1 - 1/t = 1 - 1/1.668 = 0.401$ ✓.
>
> Si $\varepsilon = 1$: $\eta_{\rm regen,max} = 1 - (T_1/T_3)\,t = 1 - (300/1200)\times1.668 = 1 - 0.417 = 58.3\%$.
>
> | Parámetro | Simple | Regen ($\varepsilon=0.75$) | Regen ($\varepsilon=1$) |
> |:---:|:---:|:---:|:---:|
> | $q_H$ [kJ/kg] | 703.0 | 538.0 | 480.6 |
> | $\eta_{\rm th}$ | 40.1% | **52.3%** | 58.3% |
>
> El recuperador reduce el calor de entrada en 23.5% y eleva la eficiencia en 12.2 puntos porcentuales.
>
> $\boxed{\eta_{\rm th,regen} = 52.3\%,\quad T_5 = 664.7\,\mathrm{K}.}$ $\blacksquare$

> [!warning]
> El recuperador solo mejora la eficiencia cuando $T_4 > T_2$. Para $r_P$ altos, $T_2$ sube más rápido que $T_4$ disminuye, y la condición se invierte. En turbinas aeronáuticas ($r_P \approx 30{-}40$) el recuperador no se usa; en microturbinas y turbinas industriales de baja compresión ($r_P \approx 4{-}10$) el regenerador es estándar.

> [!referencia]
> Borgnakke & Sonntag, §12.3; Çengel & Boles, §9-7; Moran & Shapiro, §9.7.
