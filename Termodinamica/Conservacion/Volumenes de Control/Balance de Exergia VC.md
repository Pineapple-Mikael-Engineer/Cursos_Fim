---
title: "Balance de Exergía (Volumen de Control)"
order: 4
tags:
  - termodinamica
  - conservacion
  - exergia
  - segunda_ley
  - volumen_de_control
draft: false
aliases:
  - balance exergético VC
  - disponibilidad VC
  - exergy balance VC
---

# Balance de Exergía — Volumen de Control

> [!definicion]
> El **balance de exergía** para un [[Volumenes de Control/index | volumen de control]] en régimen estacionario con un fluido entrante (1) y uno saliente (2):
> $$\boxed{\dot{B}_{\rm dest} = \dot{m}(\psi_1 - \psi_2) + \sum_k\!\left(1 - \frac{T_0}{T_k}\right)\dot{Q}_k - \dot{W}_{\rm útil},}$$
> donde la **exergía de flujo** específica es:
> $$\psi = (h - h_0) - T_0(s - s_0) + \frac{V^2}{2} + gz \quad [\text{kJ/kg}],$$
> y $\dot{B}_{\rm dest} = T_0\,\dot{S}_{\rm gen} \ge 0$ es la tasa de destrucción de exergía (ecuación de Gouy-Stodola).
>
> **Lectura:** la exergía que "entra" con el fluido ($\dot{m}\psi_1$) menos la que "sale" ($\dot{m}\psi_2$) más la exergía de calor más/menos la que sale como trabajo útil equals la exergía destruida. Todo proceso real tiene $\dot{B}_{\rm dest} > 0$; el proceso ideal tiene $\dot{B}_{\rm dest} = 0$.

---

## Qué es la exergía de flujo $\psi$

> [!teoria]
> La exergía de flujo $\psi = (h - h_0) - T_0(s - s_0)$ es el trabajo máximo útil que podría extraerse del kilogramo de fluido en estado $(h, s)$ si se llevara reversiblemente al estado muerto $(h_0, s_0)$, con el entorno a $T_0$.
>
> **¿Por qué $h$ y no $u$?** En un VC, el fluido que fluye ya "pagó" su trabajo de flujo $Pv$ al entrar. La energía que el kg de fluido puede convertir en trabajo cuando sale es la entalpía $h$ (no $u$), menos la parte que no puede convertirse porque la segunda ley lo impide: $T_0(s - s_0)$ (la "energía de baja calidad" atrapada en la entropía).
>
> **Estado muerto** $(h_0, s_0)$: las propiedades del fluido cuando está en equilibrio termodinámico con el entorno a $T_0$ y $P_0$. Para el agua líquida: $h_0 \approx 104.9\,\text{kJ/kg}$, $s_0 \approx 0.3674\,\text{kJ/(kg·K)}$ a $T_0 = 25\,°\text{C}$.

---

## Derivación: combinar balance de energía y entropía en el VC

> [!demostracion]
> **Meta:** deducir el balance de exergía del VC a partir del balance de energía y el de entropía.
>
> **Hipótesis:** VC en régimen estacionario, una entrada (1), una salida (2), calor $\dot{Q}_k$ a través de fronteras a $T_k$, trabajo de eje $\dot{W}$. Entorno a $T_0$.
>
> **Paso 1 — Balance de energía (régimen estacionario, $V^2$ y $gz$ despreciables):**
> $$\dot{Q} - \dot{W} = \dot{m}(h_2 - h_1).$$
>
> **Paso 2 — Balance de entropía (régimen estacionario):**
> $$\dot{S}_{\rm gen} = \dot{m}(s_2 - s_1) - \sum_k \frac{\dot{Q}_k}{T_k} \ge 0$$
> $$\implies \sum_k \frac{\dot{Q}_k}{T_k} = \dot{m}(s_2 - s_1) - \dot{S}_{\rm gen}.$$
>
> **Paso 3 — Multiplicar la ecuación de entropía por $T_0$ y sumar a la de energía.** El objetivo es eliminar $\dot{Q}$ y encontrar el balance en términos de exergía. Multiplico el balance de entropía por $(-T_0)$:
> $$-T_0\sum_k\frac{\dot{Q}_k}{T_k} = -\dot{m}\,T_0(s_2 - s_1) + T_0\dot{S}_{\rm gen}.$$
> Sumo al balance de energía:
> $$\dot{Q} - T_0\sum_k\frac{\dot{Q}_k}{T_k} - \dot{W} = \dot{m}[(h_2 - h_1) - T_0(s_2 - s_1)] + T_0\dot{S}_{\rm gen}.$$
>
> **Paso 4 — Identificar los factores de Carnot y la exergía de calor.** El lado izquierdo: $\dot{Q} - T_0\sum_k \dot{Q}_k/T_k = \sum_k(1 - T_0/T_k)\dot{Q}_k$ (exergía del calor). El lado derecho contiene $\dot{m}[(h_1 - h_0) - T_0(s_1 - s_0)] - \dot{m}[(h_2 - h_0) - T_0(s_2 - s_0)] = \dot{m}(\psi_1 - \psi_2)$.
>
> **Paso 5 — Reescribir como balance de exergía.** Despejando $\dot{W}$:
> $$\dot{W} = \dot{m}(\psi_1 - \psi_2) + \sum_k\!\left(1 - \frac{T_0}{T_k}\right)\dot{Q}_k - T_0\dot{S}_{\rm gen}.$$
> Identificando $\dot{B}_{\rm dest} = T_0\dot{S}_{\rm gen} \ge 0$ (Gouy-Stodola):
> $$\dot{W}_{\rm útil} = \dot{m}(\psi_1 - \psi_2) + \sum_k\!\left(1 - \frac{T_0}{T_k}\right)\dot{Q}_k - \dot{B}_{\rm dest}. \qquad \blacksquare$$

---

## Eficiencia exergética de dispositivos de flujo

> [!proposicion]
> Para una **turbina adiabática** (produce trabajo):
> $$\epsilon_T = \frac{\dot{W}}{\dot{m}(\psi_1 - \psi_2)} = 1 - \frac{\dot{B}_{\rm dest}}{\dot{m}(\psi_1 - \psi_2)}.$$
>
> Para un **compresor adiabático** (consume trabajo):
> $$\epsilon_C = \frac{\dot{m}(\psi_2 - \psi_1)}{\dot{W}} = 1 - \frac{\dot{B}_{\rm dest}}{\dot{W}}.$$
>
> Para un **intercambiador de calor** (VC sin trabajo):
> $$\epsilon_{HX} = \frac{\dot{m}_C(\psi_{C,2} - \psi_{C,1})}{\dot{m}_H(\psi_{H,1} - \psi_{H,2})}.$$

---

## Ejemplo: análisis exergético de compresor

> [!ejemplo]
> **Compresor adiabático** comprime aire de $T_1 = 300\,\text{K}$, $P_1 = 100\,\text{kPa}$ a $P_2 = 600\,\text{kPa}$. Eficiencia isentrópica $\eta_C = 0.82$. Flujo $\dot{m} = 1\,\text{kg/s}$. Entorno: $T_0 = 298\,\text{K}$.
>
> **Paso 1 — Estado isentrópico de salida:**
> $$T_{2s} = 300 \times 6^{0.2857} = 300 \times 1.669 = 500.7\,\text{K}.$$
>
> **Paso 2 — Trabajo isentrópico y real ($c_p = 1.005\,\text{kJ/(kg·K)}$):**
> $$w_s = c_p(T_{2s} - T_1) = 1.005 \times 200.7 = 201.7\,\text{kJ/kg}.$$
> $$w_{\rm real} = w_s/\eta_C = 201.7/0.82 = 245.9\,\text{kJ/kg}.$$
>
> **Paso 3 — Temperatura de salida real:**
> $$T_2 = T_1 + w_{\rm real}/c_p = 300 + 245.9/1.005 = 300 + 244.7 = 544.7\,\text{K}.$$
>
> **Paso 4 — Exergías de flujo** (despreciando cinética y potencial, $h_0$ y $s_0$ al estado muerto con $T_0$, $P_0$):
> $$\psi = c_p(T - T_0) - T_0\!\left[c_p\ln\frac{T}{T_0} - R\ln\frac{P}{P_0}\right].$$
> $$\psi_1 = 1.005(300 - 298) - 298[1.005\ln(300/298) - 0.287\ln(100/100)] = 2.01 - 298(0.00671) = 2.01 - 2.0 = 0.01\,\text{kJ/kg} \approx 0.$$
> $$\psi_2 = 1.005(544.7 - 298) - 298[1.005\ln(544.7/298) - 0.287\ln(600/100)]$$
> $$= 1.005 \times 246.7 - 298[1.005 \times 0.607 - 0.287 \times 1.792] = 247.9 - 298[0.610 - 0.514] = 247.9 - 28.6 = 219.3\,\text{kJ/kg}.$$
>
> **Paso 5 — Exergía destruida y eficiencia exergética:**
> $$\dot{B}_{\rm dest} = \dot{m}(\psi_1 - \psi_2) + \dot{W}_{\rm útil}\text{ (entra)} = w_{\rm real} - (\psi_2 - \psi_1) = 245.9 - 219.3 = 26.6\,\text{kJ/kg}.$$
> $$\epsilon_C = 1 - \frac{\dot{B}_{\rm dest}}{\dot{W}} = 1 - \frac{26.6}{245.9} = 89.2\%.$$
> Comparar con $\eta_C = 82\%$ (energética) — la eficiencia exergética es mayor porque toma en cuenta que el fluido comprimido a alta presión todavía tiene mucha exergía disponible. $\blacksquare$

---

## Relación con otras notas

> [!info]
> - [[Balance de Energia VC]] — proporciona el trabajo y los estados que aparecen en $\psi_1 - \psi_2$.
> - [[Balance de Entropia VC]] — proporciona $\dot{S}_{\rm gen}$ para calcular $\dot{B}_{\rm dest} = T_0\dot{S}_{\rm gen}$.
> - [[Exergia]] — definición general de $\psi$, teorema de Gouy-Stodola, eficiencias.
> - [[Balance de Exergia SC]] — la versión para sistemas cerrados.

> [!info]
> **Notación:** $\psi$ [kJ/kg]: exergía específica de flujo; $\dot{B}_{\rm dest}$ [kW]: tasa de destrucción de exergía; $T_0$ [K]: temperatura del entorno (estado muerto).

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, cap. 10; Çengel & Boles, *Termodinámica*, cap. 8; Moran & Shapiro, caps. 7–8; Bejan, *Advanced Engineering Thermodynamics*, §3.4.
