---
title: Líquido Comprimido
tags:
  - termodinamica
  - teoria
  - sustancias-puras
  - liquido-comprimido
  - subenfriado
draft: false
aliases:
  - Liquido Comprimido
  - Liquido Subenfriado
  - Región Subenfriada
---

# Líquido Comprimido $h(T,P)\approx h_f(T)+v_f(T)\,[P-P_{\rm sat}(T)]$

> [!definicion]
> El **líquido comprimido** (o subenfriado) es la región donde la temperatura del fluido es menor que la temperatura de saturación a la presión dada: $T < T_{\rm sat}(P)$. Equivalentemente, la presión es mayor que la presión de saturación a la temperatura dada: $P > P_{\rm sat}(T)$. En esta región el estado está fijado por dos propiedades independientes $(T,P)$.

> [!info]
> **Contexto.** En los ciclos de potencia de vapor (Rankine), la bomba opera sobre líquido comprimido. La comprensión de las propiedades en esta región permite calcular el trabajo de la bomba y el calor en los intercambiadores de la sección a presión alta del ciclo.

---

## Insensibilidad al efecto de la presión

Las propiedades del líquido comprimido son **poco sensibles a la presión**. Cuantitativamente, para el volumen específico:
$$\left(\frac{\partial v}{\partial P}\right)_T = -v\kappa_T,$$
donde $\kappa_T$ es la compresibilidad isotérmica. Para el agua líquida a $20\,°\mathrm{C}$: $\kappa_T\approx 4.6\times10^{-10}\,\mathrm{Pa^{-1}}$; un aumento de presión de $10\,\mathrm{MPa}$ cambia $v$ en solo $0.46\%$. Por eso la primera aproximación es:

$$\boxed{v(T,P) \approx v_f(T).}$$

Para la energía interna, la ecuación de estado termodinámica da:
$$\left(\frac{\partial u}{\partial P}\right)_T = -P\left(\frac{\partial v}{\partial P}\right)_T - T\left(\frac{\partial P}{\partial T}\right)_v \cdot \left(\frac{\partial v}{\partial P}\right)_T + P\left(\frac{\partial v}{\partial P}\right)_T = -T\left(\frac{\partial v}{\partial T}\right)_P$$
(identidad de la primera ley para el potencial termodinámica). Para líquidos, $(\partial v/\partial T)_P = v\beta_P$ con $\beta_P$ pequeño, así que $u$ también es poco sensible a $P$:
$$u(T,P) \approx u_f(T).$$

---

## Corrección de presión para la entalpía

La aproximación de primer orden más útil se obtiene para $h$:

> [!proposicion] Aproximación de líquido comprimido
> $$h(T,P) \approx h_f(T) + v_f(T)\,[P - P_{\rm sat}(T)].$$

> [!demostracion]
> **Paso 1.** Escribir $h=u+Pv$. De la relación de Maxwell aplicada a la entalpía:
> $$\left(\frac{\partial h}{\partial P}\right)_T = v - T\left(\frac{\partial v}{\partial T}\right)_P.$$
> Para un líquido incompresible ideal ($v=v_f=\text{cte}$, $(\partial v/\partial T)_P=0$):
> $$\left(\frac{\partial h}{\partial P}\right)_T \approx v_f(T).$$
>
> **Paso 2.** Integrar desde el estado de referencia $(T,\,P_{\rm sat}(T))$ —donde el líquido está saturado y $h=h_f(T)$— hasta $(T,P)$ a temperatura constante:
> $$h(T,P) - h_f(T) = \int_{P_{\rm sat}}^{P} v_f(T)\,dP' = v_f(T)\,[P - P_{\rm sat}(T)].$$
> Luego:
> $$h(T,P) \approx h_f(T) + v_f(T)\,[P-P_{\rm sat}(T)]. \qquad \blacksquare$$
>
> **Paso 3 — Magnitud de la corrección.** Para agua a $20\,°\mathrm{C}$ bajo $P=10\,\mathrm{MPa}$: $P_{\rm sat}(20\,°\mathrm{C})\approx2.34\,\mathrm{kPa}\ll P$, por lo que $P-P_{\rm sat}\approx P=10000\,\mathrm{kPa}$.
> $$\Delta h = v_f\,\Delta P = 0.001002\times10000=10.02\,\mathrm{kJ/kg}.$$
> Comparado con $h_f(20\,°\mathrm{C})=83.9\,\mathrm{kJ/kg}$: corrección del 12%. No despreciable en ciclos de alta presión.

---

## Cuándo usar tablas de líquido comprimido

Las tablas de **líquido comprimido** (Tabla A-7 CATT3 para el agua) tabulan propiedades a presiones fijas elevadas ($P=5,\,10,\,15,\,20,\,25,\,30\,\mathrm{MPa}$) y múltiples temperaturas. Deben usarse cuando:
1. La presión es alta (típicamente $P>5\,\mathrm{MPa}$ para el agua).
2. La temperatura se acerca a $T_{\rm sat}(P)$ (la corrección crece al acercarse a la cúpula).
3. La precisión requerida es mayor al 1–2%.

Para presiones moderadas ($P < 5\,\mathrm{MPa}$) la aproximación $y(T,P)\approx y_f(T)$ es suficiente en la mayoría de aplicaciones de ingeniería.

![[liquido_comprimido_region.svg|420]]
*Diagrama $T$–$v$: la región de líquido comprimido es el área a la izquierda de la línea de líquido saturado ($x=0$). Las isolíneas de presión son casi verticales (el volumen varía poco con la presión a temperatura fija). La separación entre las isotermas a alta presión indica la pequeña variación de $v$ con $P$.*

---

## Ejemplo: trabajo de la bomba en ciclo Rankine

> [!ejemplo]
> En un ciclo Rankine simple, la bomba comprime agua líquida desde $P_1=10\,\mathrm{kPa}$ (condensador) hasta $P_2=8\,\mathrm{MPa}$ (caldera). La entrada a la bomba es líquido saturado a $P_1$. La eficiencia isentrópica de la bomba es $\eta_B=0.85$. Determinar:
> (a) El trabajo de bomba isentrópico $w_{B,s}$ usando la aproximación de líquido comprimido.
> (b) El trabajo real $w_{B,\rm real}$ y la temperatura de salida $T_2$.
> (c) La entalpía de salida $h_2$ real.
> (d) Comparar $w_{B,s}$ con el calculado mediante tablas de líquido comprimido.

> [!solucion]
> **Datos de tablas a $P_1=10\,\mathrm{kPa}$ (Tabla A-5):**
> $T_{\rm sat}(10\,\mathrm{kPa})=45.81\,°\mathrm{C}$, estado 1 = líquido saturado: $h_1=h_f=191.8\,\mathrm{kJ/kg}$, $v_1=v_f=0.001010\,\mathrm{m^3/kg}$, $s_1=s_f=0.6493\,\mathrm{kJ/(kg\cdot K)}$.
>
> **Parte (a) — Trabajo isentrópico de bomba.**
> Para la bomba (volumen de control abierto, flujo estacionario, $q=0$):
> $$w_{B,s} = -\int_{P_1}^{P_2} v\,dP \approx -v_f(P_2-P_1) = -0.001010\times(8000-10) = -0.001010\times7990 = -8.07\,\mathrm{kJ/kg}.$$
> El trabajo es negativo (entra a la bomba). En módulo: $\lvert w_{B,s}\rvert=8.07\,\mathrm{kJ/kg}$.
>
> **Parte (b) — Trabajo real.**
> $$\eta_B = \frac{w_{B,s}}{w_{B,\rm real}} \implies w_{B,\rm real} = \frac{w_{B,s}}{\eta_B} = \frac{-8.07}{0.85} = -9.49\,\mathrm{kJ/kg}.$$
>
> **Parte (c) — Entalpía de salida real.**
> Aplicando el balance de energía a la bomba real (adiabática):
> $$h_2 = h_1 - w_{B,\rm real} = h_1 + \lvert w_{B,\rm real}\rvert = 191.8 + 9.49 = 201.3\,\mathrm{kJ/kg}.$$
>
> Temperatura de salida: usando la aproximación de líquido comprimido,
> $$h_2 \approx h_f(T_2) + v_f(T_2)\,(P_2 - P_{\rm sat}(T_2)).$$
> Para $P_2=8\,\mathrm{MPa}$ y $h_2=201.3\,\mathrm{kJ/kg}$: iterando en tablas de líquido comprimido (A-7), a $T_2\approx46\,°\mathrm{C}$ y $P=8\,\mathrm{MPa}$: $h\approx201.9\,\mathrm{kJ/kg}$. Así $T_2\approx46\,°\mathrm{C}$ (aumento ínfimo de temperatura, característico de las bombas de líquido).
>
> **Parte (d) — Comparación con tablas de líquido comprimido (A-7).**
> En Tabla A-7 a $T=45\,°\mathrm{C}$, $P=8\,\mathrm{MPa}$: $h=193.9\,\mathrm{kJ/kg}$, $v=0.001009\,\mathrm{m^3/kg}$.
> $w_{B,s} = v_1(P_2-P_1)$ vs. $w_{B,s}^{\rm tablas} = h_{2s}^{\rm tablas}-h_1 = (191.8 + v_f\Delta P) = 191.8+8.07=199.87\,\mathrm{kJ/kg}$ como estado final isentrópico.
> Diferencia: $< 0.5\%$. La aproximación de líquido incompresible es excelente para la bomba. $\blacksquare$

> [!warning]
> La fórmula $w_{B,s}=-v\,\Delta P$ (trabajo de flujo reversible) es **diferente** del trabajo de frontera $w=-\int P\,dv\approx 0$ para líquido incompresible. La bomba realiza trabajo de flujo, no de frontera. El trabajo de frontera es nulo porque $\Delta v\approx 0$; el trabajo de flujo $-\int v\,dP$ es no nulo porque $\Delta P\neq 0$.

> [!referencia]
> Çengel & Boles, *Termodinámica*, §3-6 y §10-1; Moran & Shapiro §6.6; Borgnakke & Sonntag §9.2.
