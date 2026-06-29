---
title: "Ciclo Diesel"
order: 2
tags:
  - termodinamica
  - ciclos
  - diesel
  - combustion_interna
draft: false
aliases:
  - Ciclo Diesel
  - Diesel cycle
  - motor diésel
  - ciclo de encendido por compresión
---

# Ciclo Diesel $\eta_{\rm th} = 1 - \dfrac{r_c^\gamma - 1}{r^{\gamma-1}\,\gamma(r_c-1)}$

> [!definicion]
> El **ciclo Diesel** es el ciclo aire-estándar del **motor diésel de encendido por compresión**. La diferencia fundamental con el Otto: en el motor diésel no hay bujía. El aire se comprime tan fuertemente que su temperatura supera el punto de autoignición del combustible (diésel, $T_{\rm autoig} \approx 650\,\mathrm{K}$); el combustible se inyecta entonces y arde espontáneamente.
>
> Como la inyección ocurre mientras el pistón comienza a descender, la combustión ocurre a **presión aproximadamente constante** (isobárica), en contraste con el Otto (isocórica). Esto permite al motor diésel usar **relaciones de compresión mucho mayores** ($r \approx 14{-}22$) sin detonación, lo que eleva su eficiencia.
>
> *Cuatro procesos del ciclo ideal:*
> - **1→2:** Compresión isentrópica ($V_1 \to V_2$).
> - **2→3:** Adición de calor isobárica ($P = P_2 = \text{cte}$, hasta $V_3$).
> - **3→4:** Expansión isentrópica ($V_3 \to V_4 = V_1$).
> - **4→1:** Rechazo de calor isocórico ($V = V_1 = \text{cte}$).

![[diesel_diagrama_Pv.svg|440]]
*Diagrama $P$-$v$ del ciclo Diesel ideal. La adición de calor (2→3) ocurre a presión constante mientras el volumen aumenta de $V_2$ a $V_3$. La relación de corte $r_c = V_3/V_2$ mide cuánto se expande el gas durante la combustión.*

---

## Parámetros geométricos

> [!definicion]
> Dos parámetros geométricos definen el ciclo:
>
> **Relación de compresión total:**
> $$
> r = \frac{V_1}{V_2}.
> $$
>
> **Relación de corte** (cutoff ratio): fracción del volumen que se expande durante la combustión isobárica:
> $$
> r_c = \frac{V_3}{V_2} \geq 1.
> $$
>
> Nótese que $V_4 = V_1$ (el pistón vuelve a su posición inicial). La relación de expansión efectiva de la etapa 3→4 es $V_4/V_3 = V_1/V_3 = r/r_c$.

---

## Balances de energía (base 1 kg)

> [!proposicion]
> **Calor de entrada** (proceso isobárico 2→3, $P = \text{cte}$):
> $$
> q_H = c_p(T_3 - T_2) \quad [\mathrm{kJ/kg}].
> $$
> *¿Por qué $c_p$?* En un proceso isobárico de sistema cerrado: $\delta q = du + P\,dv = dh = c_p\,dT$ (para gas ideal).
>
> **Calor rechazado** (proceso isocórico 4→1):
> $$
> q_L = c_v(T_4 - T_1) \quad [\mathrm{kJ/kg}].
> $$
>
> **Trabajo neto:**
> $$
> w_{\rm neto} = q_H - q_L = c_p(T_3-T_2) - c_v(T_4-T_1).
> $$

---

## Eficiencia del ciclo Diesel

> [!teorema]
> Para el ciclo Diesel ideal aire-estándar con relación de compresión $r$ y relación de corte $r_c$:
> $$
> \boxed{\eta_{\rm th} = 1 - \frac{1}{r^{\gamma-1}}\cdot\frac{r_c^\gamma - 1}{\gamma(r_c - 1)}}.
> $$

> [!demostracion]
> **Hipótesis:** gas ideal, $c_v$, $c_p$, $\gamma$ constantes. Proceso 1→2: isentrópico; 2→3: isobárico; 3→4: isentrópico; 4→1: isocórico.
>
> **Paso 1 — Eficiencia general:**
> $$
> \eta_{\rm th} = 1 - \frac{q_L}{q_H} = 1 - \frac{c_v(T_4-T_1)}{c_p(T_3-T_2)} = 1 - \frac{T_4-T_1}{\gamma(T_3-T_2)}.
> $$
> donde se usó $c_p/c_v = \gamma$.
>
> **Paso 2 — Relaciones de temperatura.**
>
> *Proceso 1→2 (isentrópico):*
> $$
> T_2 = T_1 r^{\gamma-1}. \tag{A}
> $$
>
> *Proceso 2→3 (isobárico, gas ideal $Pv = RT$):* como $P = \text{cte}$, $T/v = \text{cte}$:
> $$
> \frac{T_3}{T_2} = \frac{V_3}{V_2} = r_c \implies T_3 = T_2 r_c = T_1 r^{\gamma-1} r_c. \tag{B}
> $$
>
> *Proceso 3→4 (isentrópico):* relación de volúmenes $V_4/V_3 = V_1/(r_c V_2) = r/r_c$:
> $$
> T_4 = T_3 \left(\frac{V_3}{V_4}\right)^{\gamma-1} = T_3 \left(\frac{r_c}{r}\right)^{\gamma-1} = T_1 r^{\gamma-1} r_c \cdot \frac{r_c^{\gamma-1}}{r^{\gamma-1}} = T_1 r_c^\gamma. \tag{C}
> $$
>
> **Paso 3 — Sustituir en $\eta_{\rm th}$:**
> $$
> T_4 - T_1 = T_1(r_c^\gamma - 1).
> $$
> $$
> T_3 - T_2 = T_1 r^{\gamma-1}(r_c - 1).
> $$
> $$
> \eta_{\rm th} = 1 - \frac{T_1(r_c^\gamma-1)}{\gamma \cdot T_1 r^{\gamma-1}(r_c-1)} = 1 - \frac{1}{r^{\gamma-1}}\cdot\frac{r_c^\gamma - 1}{\gamma(r_c-1)}. \qquad \blacksquare
> $$
>
> **Verificación (caso $r_c \to 1$):** usando L'Hôpital: $\lim_{r_c\to1}(r_c^\gamma-1)/[\gamma(r_c-1)] = \lim_{r_c\to1}\gamma r_c^{\gamma-1}/\gamma = 1$. Luego $\eta \to 1-r^{-(\gamma-1)}$, que es la fórmula del ciclo **Otto** — el Diesel converge al Otto cuando la combustión isobárica ocurre en un volumen infinitesimal (corte instantáneo). ✓
>
> **Efecto de $r_c$:** el factor $f(r_c) = (r_c^\gamma-1)/[\gamma(r_c-1)] > 1$ para $r_c > 1$. Por tanto $\eta_{\rm Diesel}(r) < \eta_{\rm Otto}(r)$ a la **misma $r$**. Sin embargo, el motor diésel opera a $r$ mucho mayor, lo que compensa con creces.

---

## Comparación de eficiencias a distintas $r$

| $r$ | $r_c$ | $\eta_{\rm Diesel}$ | Equivalente Otto $r$ |
|:---:|:---:|:---:|:---:|
| 14 | 2.0 | 59.3% | — |
| 18 | 2.0 | 63.1% | $r=11$: 61.7% |
| 18 | 2.5 | 60.9% | — |
| 20 | 2.0 | 64.7% | — |

---

## Ejemplo: motor diésel con $r=18$, $r_c=2$

> [!ejemplo]
> Motor diésel idealizado (ciclo Diesel):
> - Condiciones de admisión: $T_1 = 300\,\mathrm{K}$, $P_1 = 95\,\mathrm{kPa}$.
> - Relación de compresión: $r = 18$.
> - Relación de corte: $r_c = 2$.
> - Propiedades del aire: $c_v = 0.718\,\mathrm{kJ/(kg\cdot K)}$, $c_p = 1.005\,\mathrm{kJ/(kg\cdot K)}$, $\gamma = 1.4$.
>
> Determinar: (a) temperaturas y presiones en los 4 estados; (b) calor añadido $q_H$; (c) $\eta_{\rm th}$; (d) trabajo neto.

> [!solucion]
> **(a) Estado 2** (compresión isentrópica):
>
> $r^{\gamma-1} = 18^{0.4} = e^{0.4\ln18} = e^{0.4\times2.890} = e^{1.156} = 3.177$.
>
> $T_2 = T_1 \cdot r^{\gamma-1} = 300 \times 3.177 = 953.1\,\mathrm{K}$.
>
> $P_2 = P_1 \cdot r^\gamma = 95 \times 18^{1.4} = 95 \times 57.20 = 5433.9\,\mathrm{kPa}$.
>
> **Estado 3** (adición isobárica):
>
> $T_3 = T_2 \cdot r_c = 953.1 \times 2 = 1906.2\,\mathrm{K}$.
>
> $P_3 = P_2 = 5433.9\,\mathrm{kPa}$ (isobárico).
>
> **Estado 4** (expansión isentrópica):
>
> $T_4 = T_1 \cdot r_c^\gamma = 300 \times 2^{1.4} = 300 \times 2.639 = 791.7\,\mathrm{K}$.
>
> $P_4 = P_3 \cdot (V_3/V_4)^\gamma = P_3 \cdot (r_c/r)^\gamma = 5433.9 \times (2/18)^{1.4} = 5433.9 \times (0.1111)^{1.4}$.
> $(0.1111)^{1.4} = e^{1.4 \times \ln(0.1111)} = e^{1.4\times(-2.198)} = e^{-3.077} = 0.04612$.
> $P_4 = 5433.9 \times 0.04612 = 250.6\,\mathrm{kPa}$.
>
> **(b) Calor añadido:**
>
> $q_H = c_p(T_3-T_2) = 1.005 \times (1906.2-953.1) = 1.005 \times 953.1 = 957.9\,\mathrm{kJ/kg}$.
>
> **(c) Eficiencia:**
>
> Factor de corte: $f(r_c) = (r_c^\gamma-1)/[\gamma(r_c-1)] = (2^{1.4}-1)/[1.4\times(2-1)] = (2.639-1)/(1.4) = 1.639/1.4 = 1.171$.
>
> $$\eta_{\rm th} = 1 - \frac{f(r_c)}{r^{\gamma-1}} = 1 - \frac{1.171}{3.177} = 1 - 0.3686 = 0.6314 = 63.1\%.$$
>
> Verificación alternativa:
> $q_L = c_v(T_4-T_1) = 0.718 \times (791.7-300) = 0.718 \times 491.7 = 353.1\,\mathrm{kJ/kg}$.
> $\eta = 1 - q_L/q_H = 1 - 353.1/957.9 = 1 - 0.3686 = 0.6314$ ✓.
>
> **(d) Trabajo neto:**
>
> $w_{\rm neto} = q_H - q_L = 957.9 - 353.1 = 604.8\,\mathrm{kJ/kg}$.
>
> | Estado | $T$ [K] | $P$ [kPa] |
> |:---:|:---:|:---:|
> | 1 (admisión) | 300.0 | 95.0 |
> | 2 (post-compresión) | 953.1 | 5433.9 |
> | 3 (post-combustión) | 1906.2 | 5433.9 |
> | 4 (post-expansión) | 791.7 | 250.6 |
>
> $$\boxed{\eta_{\rm th} = 63.1\%,\quad w_{\rm neto} = 604.8\,\mathrm{kJ/kg}.}$$ $\blacksquare$

> [!info]
> La temperatura al final de la compresión, $T_2 = 953\,\mathrm{K}$ (680°C), es suficiente para la autoignición del diésel ($T_{\rm autoig} \approx 500{-}650°\mathrm{C}$). El motor diésel **no necesita bujía** precisamente porque comprime el aire hasta esta temperatura.

> [!referencia]
> Borgnakke & Sonntag, §13.2; Çengel & Boles, §9-4 a 9-5; Moran & Shapiro, §9.4.
