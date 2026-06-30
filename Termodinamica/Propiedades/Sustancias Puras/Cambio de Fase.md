---
title: Cambio de Fase
order: 2
tags:
  - termodinamica
  - teoria
  - sustancias-puras
  - cambio-de-fase
  - entalpía-vaporización
draft: false
aliases:
  - Cambio de Fase
  - Vaporización
  - Condensación
  - Entalpía de Vaporización
---

# Cambio de Fase $h_{fg}=h_g - h_f,\quad s_{fg}=h_{fg}/T_{\rm sat}$

> [!definicion]
> Un **cambio de fase** es la transición de una sustancia pura de una fase a otra a temperatura y presión constantes. Los cambios de fase relevantes en ingeniería son: **vaporización** (líquido → vapor), **condensación** (vapor → líquido), **fusión** (sólido → líquido), **solidificación** y **sublimación** (sólido → vapor). La energía intercambiada es el **calor latente** $h_{\beta\alpha}=h_\beta-h_\alpha$; el proceso es isotérmico e isobárico (a presión fija, $T=T_{\rm sat}(P)$).

> [!info]
> **Conexión.** El calor latente es la fuente de toda la no-linealidad de la [[Propiedades en la Region Bifasica | región bifásica]] y el parámetro central del balance de energía en intercambiadores y ciclos de vapor. Su variación con $T$ sigue la [[Diagramas de Fase | ecuación de Clausius-Clapeyron]].

---

## Entalpía de vaporización $h_{fg}$

La **entalpía de vaporización** (calor latente de vaporización) se define:
$$h_{fg}(T) \equiv h_g(T)-h_f(T)$$
donde $g$ denota vapor saturado ($x=1$) y $f$ denota líquido saturado ($x=0$).

Del primer principio para un cambio de fase isobárico de un sistema cerrado:
$$q_{\rm vap} = \Delta h = h_g - h_f = h_{fg}. $$
Todo el calor suministrado a $T_{\rm sat}$ constante va a romper la cohesión molecular: $\Delta u=u_g-u_f$ es la energía interna de vaporización, y el término $P\,v_{fg}$ es el trabajo de frontera:
$$h_{fg} = u_{fg} + P\,v_{fg}, \qquad u_{fg}=u_g-u_f,\quad v_{fg}=v_g-v_f.$$

La **entropía de vaporización** es:
$$s_{fg} = \frac{h_{fg}}{T_{\rm sat}},$$
consecuencia directa del proceso reversible a $T$ constante ($\Delta s = q_{\rm rev}/T$).

![[hfg_vs_temperatura.svg|420]]
*Entalpía de vaporización del agua $h_{fg}(T)$ en función de la temperatura de saturación. $h_{fg}$ decrece monótonamente desde $\approx 2501\,\mathrm{kJ/kg}$ a $0\,°\mathrm{C}$ hasta cero en el punto crítico ($374.14\,°\mathrm{C}$). En el punto crítico las dos fases se vuelven indistinguibles.*

**Valores de referencia para el agua (de tablas):**

| $T_{\rm sat}$ (°C) | $P_{\rm sat}$ (kPa) | $h_f$ (kJ/kg) | $h_g$ (kJ/kg) | $h_{fg}$ (kJ/kg) |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0.6113 | 0.00 | 2501.4 | 2501.4 |
| 50 | 12.35 | 209.3 | 2592.1 | 2382.8 |
| 100 | 101.3 | 419.1 | 2675.6 | 2256.5 |
| 150 | 476.2 | 632.3 | 2747.0 | 2114.7 |
| 200 | 1555 | 852.4 | 2793.2 | 1940.8 |
| 300 | 8587 | 1345 | 2749.0 | 1404.0 |
| 374.14 | 22090 | 2099 | 2099 | 0 |

---

## Correlación de Watson para $h_{fg}(T)$

Para estimar $h_{fg}$ a temperaturas distintas de las tabuladas, la correlación de Watson predice la variación con $T$ a partir de un valor de referencia $h_{fg,r}$ a $T_r$:

$$\boxed{h_{fg}(T) = h_{fg,r}\left(\frac{1-T/T_c}{1-T_r/T_c}\right)^{0.38}}$$

donde $T$, $T_r$, $T_c$ están en Kelvin y el exponente $0.38$ proviene del comportamiento crítico universal (exponente crítico $\beta\approx 0.326$, combinado con la relación de escala).

> [!demostracion]
> **Motivación termodinámica.** De Clausius-Clapeyron exacto:
> $$\frac{dP_{\rm sat}}{dT}=\frac{h_{fg}}{T\,v_{fg}}.$$
> Cerca del punto crítico, la teoría de escala predice $v_{fg}\sim(T_c-T)^\beta$ con $\beta\approx0.326$ y $P_{\rm sat}-P_c\sim(T_c-T)^{1+\beta}$, de donde se puede mostrar que $h_{fg}\sim(T_c-T)^{\beta+\Delta}$ con $\Delta\approx0.054$. La correlación de Watson usa el exponente empírico $0.38\approx\beta+\Delta$ como aproximación de campo medio.
>
> **Paso de verificación dimensional.** A $T\to T_c$: $(1-T/T_c)\to 0$, luego $h_{fg}\to 0$. A $T=T_r$: la razón es $1$ y $h_{fg}=h_{fg,r}$. Ambas condiciones son satisfechas. $\blacksquare$

**Ejemplo de uso.** Para el refrigerante R-134a: $T_c=374.2\,\mathrm{K}$, $h_{fg}=204.6\,\mathrm{kJ/kg}$ a $T_r=30\,°\mathrm{C}=303.15\,\mathrm{K}$. Estimar $h_{fg}$ a $-20\,°\mathrm{C}=253.15\,\mathrm{K}$:
$$h_{fg}(-20\,°\mathrm{C})=204.6\left(\frac{1-253.15/374.2}{1-303.15/374.2}\right)^{0.38}=204.6\left(\frac{0.3232}{0.1901}\right)^{0.38}=204.6\times(1.700)^{0.38}.$$
$(1.700)^{0.38}=e^{0.38\ln 1.700}=e^{0.38\times0.5306}=e^{0.2016}=1.223.$ $h_{fg}\approx204.6\times1.223=250.2\,\mathrm{kJ/kg}$. Valor tabular: $212.9\,\mathrm{kJ/kg}$ (error $\approx17\%$; la correlación es más precisa cuando $T$ y $T_r$ están más cercanos). Como $-20\,°\mathrm{C}<T_r$, el resultado $h_{fg}>h_{fg,r}$ tiene el signo correcto: $h_{fg}$ crece al alejarse del punto crítico.

---

## Los cambios de fase y sus calores latentes

**Vaporización / condensación.** El más relevante en ingeniería de potencia y refrigeración. $h_{fg}>0$ siempre (absorbe calor al vaporizar).

**Fusión / solidificación.** $h_{sl}=h_l-h_s$. Para el agua: $h_{sl}=334\,\mathrm{kJ/kg}$ a $0\,°\mathrm{C}$. $v_{sl}<0$ para el agua (el hielo es menos denso), lo que invierte la pendiente de la curva de fusión en el diagrama $P$–$T$.

**Sublimación.** $h_{sg}=h_{sl}+h_{lg}>h_{fg}$; para el agua a $0\,°\mathrm{C}$: $h_{sg}\approx2835\,\mathrm{kJ/kg}$.

La identidad $h_{sg}=h_{sl}+h_{lg}$ se deduce de la linealidad de $h$ como función de estado (independiente del camino):
$$h_s\to h_l\to h_g:\quad h_{sl}+h_{lg}=h_g-h_s=h_{sg}. \qquad \blacksquare$$

---

## Regla de fases de Gibbs

> [!proposicion] Regla de Gibbs
> Para un sistema con $C$ componentes y $\phi$ fases en equilibrio, los grados de libertad intensivos son:
> $$F = C - \phi + 2.$$
> Para una sustancia pura ($C=1$):
> - Fase única ($\phi=1$): $F=2$ → estado fijado por $(T,P)$.
> - Coexistencia de 2 fases ($\phi=2$): $F=1$ → sobre la curva de saturación, $P=P_{\rm sat}(T)$.
> - Punto triple ($\phi=3$): $F=0$ → $(T_t,P_t)$ es único.

---

## Ejemplo complejo: calor de condensación en un intercambiador de vapor

> [!ejemplo]
> Vapor de agua saturado a $P=1\,\mathrm{MPa}$ entra a un condensador de carcasa y tubos a $\dot{m}_v=5\,\mathrm{kg/s}$. Sale como líquido saturado. El agua de enfriamiento (a $P_{\rm agua}=200\,\mathrm{kPa}$) entra a $T_{\rm e}=15\,°\mathrm{C}$ y sale a $T_{\rm s}=45\,°\mathrm{C}$.
>
> Determinar: (a) la tasa de transferencia de calor $\dot{Q}$, (b) el flujo másico de agua de enfriamiento $\dot{m}_{\rm agua}$, (c) la tasa de generación de entropía $\dot{S}_{\rm gen}$, (d) si el diseño cumple la segunda ley.

> [!solucion]
> **Datos de tablas (CATT3):**
>
> Vapor de agua a $P=1\,\mathrm{MPa}$: $T_{\rm sat}=179.91\,°\mathrm{C}$, $h_g=2778.1\,\mathrm{kJ/kg}$, $h_f=762.8\,\mathrm{kJ/kg}$, $s_g=6.5865\,\mathrm{kJ/(kg\cdot K)}$, $s_f=2.1387\,\mathrm{kJ/(kg\cdot K)}$.
>
> Agua de enfriamiento a $200\,\mathrm{kPa}$ (líquido comprimido ≈ líquido saturado a misma $T$): $h_{\rm agua,e}\approx h_f(15\,°\mathrm{C})=63.0\,\mathrm{kJ/kg}$, $s_{\rm agua,e}\approx s_f(15\,°\mathrm{C})=0.2245\,\mathrm{kJ/(kg\cdot K)}$. $h_{\rm agua,s}\approx h_f(45\,°\mathrm{C})=188.5\,\mathrm{kJ/kg}$, $s_{\rm agua,s}\approx s_f(45\,°\mathrm{C})=0.6384\,\mathrm{kJ/(kg\cdot K)}$.
>
> **Parte (a) — Balance de energía sobre el vapor.** Sistema: el vapor condensando (volumen de control, régimen estacionario, $\dot{W}=0$, $\Delta\mathrm{Ec}=0$):
> $$\dot{Q}_{\rm cedido}=\dot{m}_v(h_g-h_f)=5\times(2778.1-762.8)=5\times2015.3=10076.5\,\mathrm{kW}.$$
> El vapor cede $10076.5\,\mathrm{kW}$ al agua de enfriamiento.
>
> **Parte (b) — Balance de energía sobre el agua de enfriamiento.** El agua de enfriamiento recibe toda esa energía (condensador adiabático al exterior):
> $$\dot{Q}=\dot{m}_{\rm agua}(h_{\rm agua,s}-h_{\rm agua,e})$$
> $$\dot{m}_{\rm agua}=\frac{\dot{Q}}{h_{\rm agua,s}-h_{\rm agua,e}}=\frac{10076.5}{188.5-63.0}=\frac{10076.5}{125.5}=80.3\,\mathrm{kg/s}.$$
>
> **Parte (c) — Balance de entropía sobre el sistema combinado (adiabático al exterior).**
> $$\dot{S}_{\rm gen}=\dot{m}_v(s_f-s_g)+\dot{m}_{\rm agua}(s_{\rm agua,s}-s_{\rm agua,e})$$
> $$=5\times(2.1387-6.5865)+80.3\times(0.6384-0.2245)$$
> $$=5\times(-4.4478)+80.3\times0.4139$$
> $$=-22.239+33.236=+10.997\,\mathrm{kW/K}.$$
>
> **Parte (d) — Verificación de la segunda ley.** $\dot{S}_{\rm gen}=+10.997\,\mathrm{kW/K}>0$: proceso irreversible pero físicamente válido. La irreversibilidad se origina en la diferencia finita de temperatura entre el vapor ($179.9\,°\mathrm{C}$) y el agua de enfriamiento (promedio $\approx30\,°\mathrm{C}$). El calor fluye de mayor a menor temperatura, lo que siempre genera entropía. $\blacksquare$

> [!referencia]
> Çengel & Boles, *Termodinámica*, §3-4 a 3-6; Moran & Shapiro §11.2; Borgnakke & Sonntag §2.7.
