---
title: "Ciclo Otto"
order: 1
tags:
  - termodinamica
  - ciclos
  - otto
  - combustion_interna
  - gasolina
draft: false
aliases:
  - Ciclo Otto
  - Otto cycle
  - motor de gasolina
  - ciclo de cuatro tiempos gasolina
---

# Ciclo Otto $\eta_{\rm th} = 1 - r^{-(\gamma-1)}$

> [!definicion]
> El **ciclo Otto** es el ciclo aire-estándar del **motor de gasolina de encendido por chispa**. La característica que lo distingue es que la **combustión ocurre a volumen aproximadamente constante** (mientras el pistón está en el punto muerto superior): la bujía produce una detonación rápida antes de que el pistón se mueva significativamente.
>
> *Cuatro procesos del ciclo ideal:*
> - **1→2:** Compresión isentrópica (pistón sube, $V_1 \to V_2$, $s = \text{cte}$).
> - **2→3:** Adición de calor isocórica ($V = V_2 = \text{cte}$, modelando la combustión).
> - **3→4:** Expansión isentrópica (pistón baja, $V_2 \to V_1$, $s = \text{cte}$, produce trabajo).
> - **4→1:** Rechazo de calor isocórico ($V = V_1 = \text{cte}$, modelando la purga de gases).
>
> *Relación de compresión:* $r = V_1/V_2$ es el cociente entre el volumen desplazado más el volumen muerto y el volumen muerto. Típicamente $r = 8{-}11$ en motores de gasolina; valores mayores causan **detonación** (autoignición de la mezcla antes de la chispa).

![[otto_diagrama_Pv.svg|440]]
*Diagrama $P$-$v$ del ciclo Otto ideal. Los dos procesos verticales (isocóricos 2→3 y 4→1) corresponden a la combustión y la purga. Los dos procesos curvos (isentrópicos) corresponden a la compresión y expansión del pistón.*

---

## Balances de energía (base 1 kg)

> [!proposicion]
> **Calor de entrada** (proceso isocórico 2→3):
> $$
> q_H = c_v(T_3 - T_2) \quad [\mathrm{kJ/kg}].
> $$
>
> **Calor rechazado** (proceso isocórico 4→1):
> $$
> q_L = c_v(T_4 - T_1) \quad [\mathrm{kJ/kg}].
> $$
>
> **Trabajo neto** (por primera ley del ciclo):
> $$
> w_{\rm neto} = q_H - q_L = c_v[(T_3-T_2) - (T_4-T_1)].
> $$
>
> *¿Por qué $c_v$ y no $c_p$?* En un proceso isocórico ($dv=0$), la primera ley para sistema cerrado da $\delta q = du = c_v\,dT$. El trabajo de frontera $P\,dv = 0$ porque el volumen no cambia.

---

## Derivación de la eficiencia

> [!teorema]
> Para el ciclo Otto ideal aire-estándar:
> $$
> \boxed{\eta_{\rm th} = 1 - \frac{1}{r^{\gamma-1}}}.
> $$

> [!demostracion]
> **Hipótesis:** aire ideal, $c_v$ y $\gamma$ constantes, procesos 1→2 y 3→4 isentrópicos, 2→3 y 4→1 isocóricos.
>
> **Paso 1 — Eficiencia en función de temperaturas:**
> $$
> \eta_{\rm th} = 1 - \frac{q_L}{q_H} = 1 - \frac{c_v(T_4-T_1)}{c_v(T_3-T_2)} = 1 - \frac{T_4-T_1}{T_3-T_2}.
> $$
>
> **Paso 2 — Relación isentrópica en la compresión (1→2).** Para gas ideal, proceso isentrópico: $Tv^{\gamma-1} = \text{cte}$:
> $$
> T_1 V_1^{\gamma-1} = T_2 V_2^{\gamma-1} \implies \frac{T_2}{T_1} = \left(\frac{V_1}{V_2}\right)^{\gamma-1} = r^{\gamma-1}.
> \tag{A}
> $$
>
> **Paso 3 — Relación isentrópica en la expansión (3→4).** Misma relación de volúmenes ($V_4 = V_1$, $V_3 = V_2$):
> $$
> T_3 V_2^{\gamma-1} = T_4 V_1^{\gamma-1} \implies \frac{T_3}{T_4} = \left(\frac{V_1}{V_2}\right)^{\gamma-1} = r^{\gamma-1}.
> \tag{B}
> $$
>
> **Paso 4 — Razón de temperaturas.** De (A) y (B):
> $$
> \frac{T_2}{T_1} = \frac{T_3}{T_4} \implies \frac{T_4}{T_1} = \frac{T_3}{T_2} \implies T_4-T_1 = T_1\left(\frac{T_3}{T_2}-1\right) \implies \frac{T_4-T_1}{T_3-T_2} = \frac{T_1}{T_2}.
> $$
>
> **Paso 5 — Sustituir:**
> $$
> \eta_{\rm th} = 1 - \frac{T_1}{T_2} = 1 - \frac{1}{r^{\gamma-1}}. \qquad \blacksquare
> $$
>
> **Verificación (casos límite):**
> - $r = 1$: $\eta = 0$ (sin compresión no hay ciclo). ✓
> - $r \to \infty$: $\eta \to 1$ (imposible; limitado por detonación y materiales). ✓
> - $r = 8$, $\gamma = 1.4$: $\eta = 1 - 8^{-0.4} = 1 - 1/2.297 = 1 - 0.435 = 56.5\%$ (ideal; eficiencia real ~25–35% por irreversibilidades y calores específicos variables).

---

## Temperatura máxima y presión en el ciclo

> [!teoria]
> La temperatura máxima $T_3$ depende de la cantidad de combustible quemado por kg de aire. La relación combustible-aire estequiométrica para gasolina ($C_8H_{18}$) es $FA_{\rm estequio} \approx 1/15.1$. La energía liberada por kg de mezcla a FA estequiométrico: $q_H \approx 2800\,\mathrm{kJ/kg}_{\rm aire}$.
>
> Con $q_H = c_v(T_3-T_2)$ y $c_v = 0.718\,\mathrm{kJ/(kg\cdot K)}$:
> $$
> T_3 = T_2 + \frac{q_H}{c_v}.
> $$
>
> Para $T_2 = 689\,\mathrm{K}$ (compresión desde 300 K con $r=8$) y $q_H = 800\,\mathrm{kJ/kg}$: $T_3 = 689 + 800/0.718 = 689 + 1114 = 1803\,\mathrm{K}$.
>
> La presión máxima en el estado 3: $P_3 = P_2(T_3/T_2)$ (isocórico → ley de Gay-Lussac). Con $P_2 = P_1 r^\gamma = 100\times 8^{1.4} = 1837\,\mathrm{kPa}$: $P_3 = 1837 \times (1803/689) = 4807\,\mathrm{kPa} \approx 48\,\mathrm{bar}$.

---

## Ejemplo: motor de gasolina a $r = 8$

> [!ejemplo]
> Motor de gasolina idealizado (ciclo Otto):
> - Condiciones de admisión: $T_1 = 300\,\mathrm{K}$, $P_1 = 100\,\mathrm{kPa}$.
> - Relación de compresión: $r = 8$.
> - Calor añadido por combustión: $q_H = 800\,\mathrm{kJ/kg}$.
> - Propiedades del aire: $c_v = 0.718\,\mathrm{kJ/(kg\cdot K)}$, $c_p = 1.005\,\mathrm{kJ/(kg\cdot K)}$, $\gamma = 1.4$.
>
> Determinar: (a) temperaturas y presiones en los 4 estados; (b) $\eta_{\rm th}$; (c) trabajo neto por kg de aire; (d) temperatura y calidad del proceso de rechazo.

> [!solucion]
> **(a) Estado 2** (compresión isentrópica):
>
> $T_2 = T_1 \cdot r^{\gamma-1} = 300 \times 8^{0.4}$.
>
> $8^{0.4} = e^{0.4\ln8} = e^{0.4\times2.0794} = e^{0.8318} = 2.297$.
>
> $T_2 = 300 \times 2.297 = 689.2\,\mathrm{K}$.
>
> $P_2 = P_1 \cdot r^\gamma = 100 \times 8^{1.4} = 100 \times 18.38 = 1837.9\,\mathrm{kPa}$.
>
> **Estado 3** (adición isocórica):
>
> $T_3 = T_2 + q_H/c_v = 689.2 + 800/0.718 = 689.2 + 1114.2 = 1803.4\,\mathrm{K}$.
>
> $P_3 = P_2 \cdot (T_3/T_2) = 1837.9 \times (1803.4/689.2) = 1837.9 \times 2.617 = 4808.4\,\mathrm{kPa}$.
>
> **Estado 4** (expansión isentrópica):
>
> $T_4 = T_3 / r^{\gamma-1} = 1803.4 / 2.297 = 784.9\,\mathrm{K}$.
>
> $P_4 = P_3 / r^\gamma = 4808.4 / 18.38 = 261.6\,\mathrm{kPa}$.
>
> **(b) Eficiencia:**
>
> $$\eta_{\rm th} = 1 - \frac{1}{r^{\gamma-1}} = 1 - \frac{1}{2.297} = 1 - 0.4354 = 0.5646 = 56.5\%.$$
>
> **(c) Trabajo neto:**
>
> $q_L = c_v(T_4-T_1) = 0.718 \times (784.9-300) = 0.718 \times 484.9 = 348.2\,\mathrm{kJ/kg}$.
>
> $w_{\rm neto} = q_H - q_L = 800 - 348.2 = 451.8\,\mathrm{kJ/kg}$.
>
> Verificación: $w_{\rm neto} = \eta_{\rm th} \times q_H = 0.5646 \times 800 = 451.7\,\mathrm{kJ/kg}$ ✓.
>
> **(d) Temperatura de rechazo:**
>
> El rechazo ocurre en el estado 4→1 a $V = V_1$. La temperatura cae de $T_4 = 784.9\,\mathrm{K}$ a $T_1 = 300\,\mathrm{K}$.
>
> | Estado | $T$ [K] | $P$ [kPa] |
> |:---:|:---:|:---:|
> | 1 (admisión) | 300.0 | 100.0 |
> | 2 (post-compresión) | 689.2 | 1837.9 |
> | 3 (post-combustión) | 1803.4 | 4808.4 |
> | 4 (post-expansión) | 784.9 | 261.6 |
>
> $$\boxed{\eta_{\rm th} = 56.5\%,\quad w_{\rm neto} = 451.8\,\mathrm{kJ/kg}.}$$ $\blacksquare$

> [!warning]
> La eficiencia ideal del 56.5% es mucho mayor que la real (~25–35%). Las causas principales: (1) los calores específicos del aire/gases quemados aumentan con la temperatura ($\gamma < 1.4$ efectivo), (2) la combustión no es instantánea ni a volumen exactamente constante, (3) hay transferencia de calor a las paredes y fricción mecánica. El ciclo Otto aire-estándar sobreestima la eficiencia en ~50%.

> [!referencia]
> Borgnakke & Sonntag, §13.1; Çengel & Boles, §9-3; Moran & Shapiro, §9.3.
