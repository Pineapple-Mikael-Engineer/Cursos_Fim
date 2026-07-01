---
title: "Exergía (Disponibilidad) $B$"
order: 6
tags:
  - termodinamica
  - exergia
  - segunda_ley
  - conversion_energia
draft: false
aliases:
  - disponibilidad
  - exergy
  - availability
  - B
  - trabajo útil máximo
  - destrucción de exergía
---

# Exergía (Disponibilidad) $B$

> [!definicion]
> La **exergía** $B$ (o disponibilidad) de un sistema es el **trabajo útil máximo** que puede extraerse del sistema mientras este alcanza el equilibrio termodinámico con su entorno a temperatura $T_0$, presión $P_0$ (el estado muerto). A diferencia de la energía (que se conserva), la exergía **se destruye** en todo proceso real: la destrucción de exergía es la "calidad de energía" perdida irrecuperablemente en las irreversibilidades.
>
> Formalmente, para un sistema cerrado:
> $$B = (U - U_0) + P_0(V - V_0) - T_0(S - S_0),$$
> donde el subíndice 0 denota el estado muerto (equilibrio con el entorno).
>
> **¿Qué hace útil la exergía vs. la energía?** La energía total de un sistema se conserva siempre, pero no toda puede convertirse en trabajo. La exergía cuantifica exactamente cuánto puede convertirse. Un litro de agua a 40 °C y un litro a 100 °C tienen casi la misma energía interna relativa al estado muerto, pero la segunda tiene mucho más exergía porque puede impulsar un ciclo de potencia con mayor temperatura de fuente.

---

## Conexión con Helmholtz y Gibbs

> [!teoria]
> La exergía generaliza las energías libres de Helmholtz y Gibbs al caso en que el sistema puede intercambiar trabajo con un entorno a presión $P_0$:
>
> **Sistema cerrado a volumen variable:** cuando el sistema se expande, parte del trabajo que realiza es trabajo de frontera $P_0\,\Delta V$ contra el entorno — ese trabajo no es útil (ya lo "gasta" empujar la atmósfera). El **trabajo útil** es:
> $$W_{\rm útil} = W_{\rm total} - P_0\,\Delta V.$$
> El máximo trabajo útil extraíble a temperatura $T_0$ es:
> $$W_{\rm útil,\,máx} = -\Delta B = -(B_2 - B_1).$$
>
> **Relación con $F$ (Helmholtz):** si $V$ es constante, $\Delta B = \Delta F\big|_{T=T_0}$: la exergía en proceso isocórico-isotérmico al estado muerto es exactamente la variación de energía de Helmholtz.
>
> **Relación con $G$ (Gibbs):** en flujo estacionario (sistema abierto), la exergía específica de flujo es $\psi = (h - h_0) - T_0(s - s_0)$, que es la diferencia de energía de Gibbs respecto al estado muerto (a la temperatura del estado, no $T_0$). Cuando la temperatura es precisamente $T_0$: $\psi = g - g_0 = \Delta G\big|_{T=T_0}$.

---

## Exergía de flujo (sistema abierto)

> [!proposicion]
> Para un fluido en flujo estacionario, la exergía específica transferida por unidad de masa es:
> $$\psi = (h - h_0) - T_0(s - s_0) + \frac{V^2}{2} + g_z,$$
> donde $V$ es la velocidad y $z$ la altura. Negligiendo cinética y potencial en la mayoría de los análisis termodinámicos:
> $$\psi \approx (h - h_0) - T_0(s - s_0).$$
> Esta forma aparece en el análisis de turbinas, compresores, intercambiadores de calor y toberas.

---

## Trabajo máximo útil y el teorema de Gouy-Stodola

> [!demostracion]
> **Meta:** probar que la exergía destruida es proporcional a la entropía generada (teorema de Gouy-Stodola).
>
> **Hipótesis:** proceso entre estados 1 y 2 con un entorno a $(T_0, P_0)$; el proceso puede intercambiar calor con el entorno y realizar trabajo útil.
>
> **Paso 1 — Balance de energía del sistema cerrado:**
> $$\Delta U = Q - W_{\rm total} = Q - W_{\rm útil} - P_0\,\Delta V,$$
> donde $W_{\rm útil}$ es el trabajo neto útil (excluyendo el trabajo $P_0\,dV$ contra el entorno).
>
> **Paso 2 — Balance de entropía incluyendo generación de entropía $S_{\rm gen}$:**
> $$\Delta S = \frac{Q}{T_0} + S_{\rm gen}, \quad S_{\rm gen} \ge 0 \implies Q = T_0(\Delta S - S_{\rm gen}).$$
> (El único reservorio es el entorno a $T_0$; si el sistema pierde calor, $Q < 0$ en esta convención.)
>
> **Paso 3 — Sustituir $Q$ en el balance de energía:**
> $$\Delta U = T_0(\Delta S - S_{\rm gen}) - W_{\rm útil} - P_0\,\Delta V.$$
> Despejando $W_{\rm útil}$:
> $$W_{\rm útil} = T_0\,\Delta S - P_0\,\Delta V - \Delta U - T_0\,S_{\rm gen}.$$
>
> **Paso 4 — Identificar $-\Delta B$:**
> $$-\Delta B = -(B_2 - B_1) = -\Delta U - P_0\,\Delta V + T_0\,\Delta S.$$
> Entonces:
> $$W_{\rm útil} = -\Delta B - T_0\,S_{\rm gen}.$$
>
> **Paso 5 — Definir destrucción de exergía y enunciar el teorema.** Exergía destruida: $\Phi \equiv T_0\,S_{\rm gen} \ge 0$. En proceso reversible ($S_{\rm gen} = 0$): $W_{\rm útil,\,máx} = -\Delta B$. En proceso real:
> $$W_{\rm útil} = -\Delta B - \Phi = -\Delta B - T_0\,S_{\rm gen}.$$
> $$\boxed{\Phi = T_0\,S_{\rm gen}.}$$
> Esta es la ecuación de **Gouy-Stodola**: la exergía destruida es la temperatura del entorno multiplicada por la entropía generada. Para minimizar pérdidas, hay que minimizar $S_{\rm gen}$. $\blacksquare$

![[exergia_destruccion_Gouy_Stodola.svg|440]]
*Balance de exergía en un proceso real: la exergía de entrada $B_1$ se divide en exergía de salida $B_2$ (trabajo útil recuperado), trabajo perdido en el empuje contra el entorno $P_0\Delta V$, y exergía destruida $\Phi = T_0 S_{\rm gen}$. Solo la primera fracción es recuperable en la operación del equipo.*

---

## Eficiencia exergética

> [!proposicion]
> La **eficiencia energética** $\eta$ compara lo que se obtiene con lo que entra en términos de energía. La **eficiencia exergética** $\epsilon$ es más rigurosa: compara la exergía útil obtenida con la exergía suministrada:
> $$\epsilon = \frac{W_{\rm útil}}{-\Delta B_{\rm entrada}} = 1 - \frac{\Phi}{-\Delta B_{\rm entrada}} = 1 - \frac{T_0\,S_{\rm gen}}{-\Delta B_{\rm entrada}}.$$
>
> **Comparación con eficiencia energética:**
> | Dispositivo | $\eta$ energética | $\epsilon$ exergética | ¿Por qué difieren? |
> |:---|:---:|:---:|:---|
> | Calefactor eléctrico | 100% | $<10\%$ | Se degrada trabajo (alta calidad) en calor a baja temperatura |
> | Turbina de vapor moderna | 88% | 80% | Irreversibilidades en el proceso |
> | Intercambiador de calor bien diseñado | 95% | 60% | Gran diferencia de temperatura → destrucción de exergía |
>
> La eficiencia exergética revela dónde se pierde potencial de trabajo de verdad, no solo cuánta energía se transfiere.

---

## Fuentes de irreversibilidad y destrucción de exergía

> [!teoria]
> Las irreversibilidades que destruyen exergía ($S_{\rm gen} > 0$) en ingeniería son:
>
> 1. **Transferencia de calor a través de gradiente de temperatura finito.** Si $\delta Q$ se transfiere desde $T_H$ a $T_L$ ($T_H > T_L > T_0$):
> $$S_{\rm gen} = \delta Q\left(\frac{1}{T_L} - \frac{1}{T_H}\right) > 0.$$
> La exergía destruida aumenta cuanto mayor es la diferencia de temperaturas.
>
> 2. **Mezcla de sustancias a distinta composición o temperatura.** La mezcla aumenta la entropía del universo sin trabajo útil extraíble.
>
> 3. **Fricción mecánica.** Trabajo mecánico se convierte directamente en calor a temperatura baja.
>
> 4. **Expansión libre (válvulas de estrangulamiento).** El fluido cae de presión alta a baja sin hacer trabajo; la entalpía se conserva pero la exergía disminuye.
>
> 5. **Reacciones químicas espontáneas.** Se destruye exergía química.
>
> La ingeniería de segunda ley (*exergy analysis*) ubica cuál de estas fuentes domina en cada equipo y guía las mejoras de diseño.

---

## Ejemplo: análisis exergético de turbina de vapor

> [!ejemplo]
> **Turbina de vapor:** entrada a $P_1 = 6\,\text{MPa}$, $T_1 = 500\,°\text{C}$ ($h_1 = 3422.2\,\text{kJ/kg}$, $s_1 = 6.882\,\text{kJ/(kg·K)}$); salida real a $h_2 = 2330.2\,\text{kJ/kg}$, $s_2 = 7.47\,\text{kJ/(kg·K)}$. Entorno: $T_0 = 25\,°\text{C} = 298.15\,\text{K}$, $P_0 = 100\,\text{kPa}$. Estado muerto del agua: $h_0 \approx 104.9\,\text{kJ/kg}$, $s_0 \approx 0.3674\,\text{kJ/(kg·K)}$.
>
> **Paso 1 — Exergías de flujo:**
> $$\psi_1 = (h_1 - h_0) - T_0(s_1 - s_0) = (3422.2 - 104.9) - 298.15(6.882 - 0.3674) = 3317.3 - 1942.1 = 1375.2\,\text{kJ/kg}.$$
> $$\psi_2 = (h_2 - h_0) - T_0(s_2 - s_0) = (2330.2 - 104.9) - 298.15(7.47 - 0.3674) = 2225.3 - 2117.6 = 107.7\,\text{kJ/kg}.$$
>
> **Paso 2 — Trabajo real de la turbina:**
> $$w_{\rm real} = h_1 - h_2 = 3422.2 - 2330.2 = 1092.0\,\text{kJ/kg}.$$
>
> **Paso 3 — Exergía destruida:**
> $$\Phi = \psi_1 - \psi_2 - w_{\rm real} = 1375.2 - 107.7 - 1092.0 = 175.5\,\text{kJ/kg}.$$
>
> **Paso 4 — Verificación con Gouy-Stodola:**
> $$\Delta s_{\rm gen} = s_2 - s_1 = 7.47 - 6.882 = 0.588\,\text{kJ/(kg·K)}.$$
> $$T_0\,\Delta s_{\rm gen} = 298.15 \times 0.588 = 175.3\,\text{kJ/kg}.$$
> Coincide con $\Phi = 175.5\,\text{kJ/kg}$ (diferencia por redondeo): para una turbina adiabática toda la exergía destruida es $\Phi = T_0\,\dot S_{\rm gen}/\dot m$ exactamente, sin término de transferencia con el ambiente.
>
> **Paso 5 — Eficiencia exergética:**
> $$\epsilon = \frac{w_{\rm real}}{\psi_1 - \psi_2} = \frac{1092.0}{1375.2 - 107.7} = \frac{1092.0}{1267.5} = 86.2\%.$$
> Comparar: eficiencia isentrópica $\eta_T = 88\%$ vs. eficiencia exergética $\epsilon = 86.2\%$ — valores cercanos para turbinas porque la única irreversibilidad significativa es la generación de entropía interna. $\blacksquare$

---

## Relación con otras notas

> [!info]
> - El teorema de Gouy-Stodola conecta exergía con entropía: $\Phi = T_0 S_{\rm gen}$; ver [[Entropia]].
> - La exergía de flujo $\psi = h - h_0 - T_0(s-s_0)$ usa entalpía y entropía de [[Entalpia]] y [[Entropia]].
> - $F$ (Helmholtz) es la exergía a volumen constante; $G$ (Gibbs) es la exergía de flujo a $T_0$: ver [[Helmholtz]] y [[Gibbs]].
> - El análisis exergético de ciclos de potencia se desarrolla en [[Ciclos/index | Ciclos Termodinámicos]].
> - La eficiencia de segunda ley de turbinas y compresores: ver [[Eficiencias de Dispositivos]].

> [!info]
> **Notación:** $B$ o $\Phi$: exergía cerrada [kJ]; $\psi$: exergía de flujo [kJ/kg]; $\Phi$: exergía destruida [kJ]; $\dot{\Phi}$: tasa de destrucción [kW]. Algunos textos usan $E_x$, $\Xi$, o $\Phi$ para la exergía.

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, cap. 10; Çengel & Boles, *Termodinámica*, caps. 8–9; Moran & Shapiro, caps. 7–8; Bejan, Tsatsaronis & Moran, *Thermal Design and Optimization* (1996); Gouy (1889) y Stodola (1910) — trabajo original.
