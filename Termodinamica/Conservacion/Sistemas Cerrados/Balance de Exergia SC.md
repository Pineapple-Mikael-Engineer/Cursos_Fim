---
title: "Balance de Exergía (Sistema Cerrado)"
order: 3
tags:
  - termodinamica
  - conservacion
  - exergia
  - segunda_ley
  - sistema_cerrado
draft: false
aliases:
  - balance exergético SC
  - disponibilidad SC
  - exergy balance SC
---

# Balance de Exergía — Sistema Cerrado

> [!definicion]
> Para un [[Sistemas Cerrados/index | sistema cerrado]] que interactúa con un entorno a $(T_0, P_0)$ (el **estado muerto**), el balance de exergía es:
> $$\boxed{\Delta B = \int_1^2\!\left(1 - \frac{T_0}{T}\right)\delta Q - \left[W - P_0(V_2 - V_1)\right] - B_{\rm dest},}$$
> donde $B_{\rm dest} = T_0 S_{\rm gen} \ge 0$ es la exergía destruida por irreversibilidades internas, y la exergía del sistema cerrado es:
> $$B = (U - U_0) + P_0(V - V_0) - T_0(S - S_0).$$
>
> **Lectura del balance:** la exergía del sistema cambia porque (1) entra o sale exergía asociada al calor (el factor $1 - T_0/T$ es la eficiencia de Carnot — solo esa fracción del calor es "trabajo potencial"), (2) sale trabajo útil ($W - P_0\Delta V$, descontando el trabajo desperdiciado en empujar la atmósfera), y (3) se destruye exergía irreversiblemente en $B_{\rm dest}$. A diferencia de la energía (que se conserva), **la exergía siempre disminuye o se conserva**: $B_{\rm dest} \ge 0$ en todos los procesos reales.

---

## Derivación: combinar primera ley + segunda ley

> [!demostracion]
> **Meta:** derivar el balance de exergía para un sistema cerrado a partir de las dos leyes.
>
> **Hipótesis:** sistema cerrado en contacto con entorno a $T_0$, $P_0$; el sistema puede intercambiar calor a temperatura de frontera $T$ y realizar trabajo $W$.
>
> **Paso 1 — Primera ley:**
> $$\Delta U = Q - W.$$
>
> **Paso 2 — Segunda ley (balance de entropía con generación):**
> $$\Delta S = \int_1^2\frac{\delta Q}{T} + S_{\rm gen} \implies Q = \int_1^2 T\,\frac{\delta Q}{T} = T_0\Delta S - T_0 S_{\rm gen} + \int_1^2\!\left(1 - \frac{T_0}{T}\right)T\,\frac{\delta Q}{T}.$$
> Más directamente: de la segunda ley, $T_0 S_{\rm gen} = T_0\Delta S - \int (T_0/T)\delta Q$, luego $Q = \int \delta Q = \int\left(1 - T_0/T\right)\delta Q + T_0\Delta S - T_0 S_{\rm gen}$.
>
> **Paso 3 — Sustituir $Q$ en la primera ley.**
> $$\Delta U = \int\!\left(1 - \frac{T_0}{T}\right)\delta Q + T_0\Delta S - T_0 S_{\rm gen} - W.$$
>
> **Paso 4 — Reorganizar sumando y restando $T_0\Delta S$ y $P_0\Delta V$ a ambos lados.**
> $$\Delta U - T_0\Delta S + P_0\Delta V = \int\!\left(1 - \frac{T_0}{T}\right)\delta Q - (W - P_0\Delta V) - T_0 S_{\rm gen}.$$
>
> **Paso 5 — Identificar $\Delta B$ y $B_{\rm dest}$.** El lado izquierdo es exactamente $\Delta B = \Delta U + P_0\Delta V - T_0\Delta S$; el último término del lado derecho es $B_{\rm dest} = T_0 S_{\rm gen} \ge 0$. Por tanto:
> $$\Delta B = \int_1^2\!\left(1 - \frac{T_0}{T}\right)\delta Q - (W - P_0\Delta V) - B_{\rm dest}. \qquad \blacksquare$$

---

## Trabajo útil vs. trabajo total

> [!teoria]
> Cuando un sistema cerrado se expande ($\Delta V > 0$), parte del trabajo realizado va a "empujar" la atmósfera: $W_{atm} = P_0\Delta V$. Ese trabajo no está disponible para ningún uso útil — simplemente desplaza aire. El **trabajo útil** (el que puede mover un generador, levantar un peso, etc.) es:
> $$W_{\rm útil} = W - P_0\Delta V.$$
> El balance de exergía se escribe en términos de $W_{\rm útil}$, no de $W$ total, porque la exergía mide trabajo **aprovechable**.
>
> **Consecuencia:** el trabajo máximo útil extraíble en un proceso entre 1 y 2 (con calor al entorno a $T_0$) es:
> $$W_{\rm útil,\,máx} = -\Delta B \quad \text{(proceso reversible, } B_{\rm dest} = 0\text{)}.$$

---

## La ecuación de Gouy-Stodola

> [!teorema]
> La exergía destruida es proporcional a la entropía generada:
> $$B_{\rm dest} = T_0\,S_{\rm gen} \ge 0.$$
> Todo lo que genera entropía destruye exergía a razón de $T_0$ por unidad de entropía generada. Para reducir las pérdidas de exergía, hay que minimizar las irreversibilidades (diferencias de temperatura en transferencia de calor, fricción, mezcla, etc.).

---

## Casos particulares

> [!proposicion]
> **Proceso adiabático** ($\delta Q = 0$):
> $$\Delta B = -(W - P_0\Delta V) - B_{\rm dest} \implies W_{\rm útil,\,máx} = -\Delta B \quad (B_{\rm dest} = 0).$$
>
> **Proceso isotérmico** ($T = \text{cte}$):
> $$\Delta B = \left(1 - \frac{T_0}{T}\right)Q - (W - P_0\Delta V) - B_{\rm dest}.$$
> Si además $T = T_0$: el factor $(1 - T_0/T) = 0$ — el calor del entorno tiene **cero exergía** (no se puede extraer trabajo de él).
>
> **Sistema aislado** ($Q = 0$, $W = 0$):
> $$\Delta B = -B_{\rm dest} \le 0.$$
> La exergía de un sistema aislado nunca aumenta.

---

## Eficiencia exergética del sistema cerrado

> [!proposicion]
> Para un proceso de expansión (el sistema produce trabajo):
> $$\epsilon = \frac{W_{\rm útil}}{W_{\rm útil,\,máx}} = \frac{W_{\rm útil}}{-\Delta B + \int(1 - T_0/T)\delta Q} = 1 - \frac{B_{\rm dest}}{-\Delta B + \int(1 - T_0/T)\delta Q}.$$
> Para un proceso de compresión (se suministra trabajo):
> $$\epsilon = \frac{W_{\rm útil,\,min}}{W_{\rm útil}} = 1 - \frac{B_{\rm dest}}{W_{\rm útil}}.$$

---

## Ejemplo: expansión adiabática irreversible

> [!ejemplo]
> **Gas ideal (aire)** ($m = 1\,\text{kg}$, $c_v = 0.718\,\text{kJ/(kg·K)}$, $R = 0.287\,\text{kJ/(kg·K)}$) **se expande adiabáticamente desde $T_1 = 600\,\text{K}$, $P_1 = 500\,\text{kPa}$ hasta $P_2 = 100\,\text{kPa}$. Eficiencia isentrópica de la turbina: $\eta_T = 0.85$.** Entorno a $T_0 = 298\,\text{K}$.
>
> **Paso 1 — Estado isentrópico de salida:**
> $$T_{2s} = T_1\left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma} = 600 \times 5^{-0.2857} = 600 \times 0.6310 = 378.6\,\text{K}.$$
>
> **Paso 2 — Trabajo isentrópico y real:**
> $$w_s = c_v(T_1 - T_{2s}) = 0.718 \times 221.4 = 158.9\,\text{kJ/kg}.$$
> $$w_{\rm real} = \eta_T \times w_s = 0.85 \times 158.9 = 135.1\,\text{kJ/kg}.$$
>
> **Paso 3 — Temperatura de salida real:**
> $$T_2 = T_1 - w_{\rm real}/c_v = 600 - 135.1/0.718 = 600 - 188.2 = 411.8\,\text{K}.$$
>
> **Paso 4 — Variación de exergía del gas.** Con proceso adiabático:
> $$\Delta B = (u_2 - u_1) - T_0(s_2 - s_1) = c_v(T_2 - T_1) - T_0\left[c_p\ln\frac{T_2}{T_1} - R\ln\frac{P_2}{P_1}\right].$$
> $$\Delta s = 1.005\ln\frac{411.8}{600} - 0.287\ln\frac{100}{500} = 1.005(-0.376) - 0.287(-1.609) = -0.378 + 0.462 = +0.084\,\text{kJ/(kg·K)}.$$
> $$\Delta B = -135.1 - 298 \times 0.084 = -135.1 - 25.0 = -160.1\,\text{kJ/kg}.$$
>
> **Paso 5 — Verificación con Gouy-Stodola:**
> $$B_{\rm dest} = T_0 S_{\rm gen} = T_0\Delta s_{\rm gen} = 298 \times 0.084 = 25.0\,\text{kJ/kg}.$$
> $$w_{\rm útil} = -\Delta B - B_{\rm dest} = 160.1 - 25.0 = 135.1\,\text{kJ/kg}. \checkmark$$
> La eficiencia exergética es $\epsilon = 135.1/160.1 = 84.4\%$, ligeramente diferente de $\eta_T = 85\%$ por el efecto de la temperatura de salida sobre la exergía del fluido que sale. $\blacksquare$

---

## Relación con otras notas

> [!info]
> - [[Primera Ley SC]] — proporciona $\Delta U = Q - W$.
> - [[Segunda Ley SC]] — proporciona $S_{\rm gen}$ y el vínculo $B_{\rm dest} = T_0 S_{\rm gen}$.
> - [[Exergia]] — definición general de $B$, teorema de Gouy-Stodola completo, eficiencias.
> - [[Balance de Exergia VC]] — extensión a sistemas abiertos con flujo de exergía $\psi$.

> [!warning]
> - **Trabajo útil** $\ne$ trabajo total: $W_{\rm útil} = W - P_0\Delta V$. Solo el trabajo útil aparece en el balance de exergía.
> - **Estado muerto:** $T_0$, $P_0$ son del entorno; $U_0$, $S_0$, $V_0$ son los valores que el sistema tomaría si estuviera en equilibrio con el entorno.
> - **Exergía negativa** es posible si el sistema está por debajo del ambiente (fluido frío, temperatura sub-ambiente). Significa que se puede extraer trabajo dejando que el sistema suba hasta $T_0$.

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, cap. 10; Çengel & Boles, *Termodinámica*, cap. 8; Moran & Shapiro, caps. 7–8; Bejan, Tsatsaronis & Moran, *Thermal Design and Optimization* (1996), cap. 3.
