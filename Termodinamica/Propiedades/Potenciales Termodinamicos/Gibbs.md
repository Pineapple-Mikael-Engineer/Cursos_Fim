---
title: "Energía de Gibbs $G$"
order: 5
tags:
  - termodinamica
  - potenciales_termodinamicos
  - gibbs
draft: false
aliases:
  - Gibbs free energy
  - energía libre de Gibbs
  - G
  - potencial químico
  - equilibrio de fases
---

# Energía de Gibbs $G$

> [!definicion]
> La **energía libre de Gibbs** se define como:
> $$G \equiv H - TS = U + PV - TS,$$
> y es el potencial termodinámico con variables naturales $(T, P)$. Su significado físico central es: **$-\Delta G$ es el trabajo no-$PV$ máximo extraíble en un proceso a temperatura y presión constantes**. Esto incluye trabajo eléctrico, trabajo de tensión superficial, trabajo elástico — cualquier forma de trabajo excepto la expansión $P\,dV$ contra el entorno. En procesos a $(T, P)$ constantes (la condición más común en ingeniería y química), el equilibrio corresponde al mínimo de $G$.
>
> La energía libre de Gibbs es también el potencial que rige el equilibrio de fases y las reacciones químicas: dos fases coexisten en equilibrio cuando tienen el mismo valor de $g$ (energía de Gibbs por mol), y una reacción es espontánea a $(T, P)$ constantes cuando $\Delta G < 0$.

---

## Diferencial y variables naturales

> [!proposicion]
> De $G = H - TS$ y $dH = T\,dS + V\,dP$:
> $$dG = dH - T\,dS - S\,dT = (T\,dS + V\,dP) - T\,dS - S\,dT$$
> $$\boxed{dG = -S\,dT + V\,dP.}$$
> Variables naturales: $(T, P)$. Derivadas primeras:
> $$S = -\left(\frac{\partial G}{\partial T}\right)_P, \qquad V = \left(\frac{\partial G}{\partial P}\right)_T.$$
> La segunda derivada da el volumen directamente desde $G(T,P)$ — de aquí se puede recuperar la ecuación de estado sin información adicional.

---

## Cuarta relación de Maxwell (desde $G$)

> [!proposicion]
> Por igualdad de derivadas cruzadas de $dG = -S\,dT + V\,dP$:
> $$\left(\frac{\partial S}{\partial P}\right)_T = -\left(\frac{\partial V}{\partial T}\right)_P.$$
> Esta es la cuarta relación de Maxwell. El lado derecho es $-v\alpha$ ($\alpha$ = coeficiente de expansión térmica), directamente medible. La aplicación directa más importante: calcular $(\partial h/\partial P)_T = v(1 - T\alpha)$ para cualquier sustancia real sin datos calorimétricos a alta presión. Ver [[Maxwell]].

---

## Criterio de equilibrio a $(T, P)$ constantes

> [!demostracion]
> **Meta:** probar que en un proceso a $(T, P)$ constantes, el equilibrio corresponde al mínimo de $G$.
>
> **Hipótesis:** sistema cerrado en contacto con un reservorio de calor a temperatura $T$ y con el entorno a presión $P$; el sistema puede realizar trabajo de frontera $P\,dV$ pero no otro tipo de trabajo.
>
> **Paso 1 — Primera ley a presión constante:**
> $$dU = \delta Q - P\,dV \implies \delta Q = dU + P\,dV = dH \quad (P = \text{cte}).$$
>
> **Paso 2 — Aplicar la segunda ley.**
> Para el sistema: $dS \ge \delta Q/T = dH/T$:
> $$T\,dS \ge dH \implies dH - T\,dS \le 0 \quad (T, P = \text{cte}).$$
>
> **Paso 3 — Identificar la variación de $G$.**
> A $(T, P)$ constantes: $dG = dH - T\,dS - S\,dT = dH - T\,dS$ (ya que $dT = 0$). Por tanto:
> $$dG \le 0 \quad (T, P = \text{cte}).$$
>
> **Paso 4 — Interpretación.**
> $G$ solo puede disminuir o mantenerse constante. Los procesos espontáneos ($dG < 0$) ocurren hasta alcanzar el estado donde $dG = 0$ — el mínimo de $G$. Ese mínimo es el equilibrio.
>
> **Paso 5 — Verificación del criterio de estabilidad.**
> Para que el mínimo sea estable (no solo un punto estacionario): $\delta^2 G > 0$, que implica $c_P > 0$ y $\kappa_T > 0$ (estabilidad mecánica y térmica). Si alguna de estas condiciones falla, el sistema se vuelve inestable y se produce separación de fases. $\blacksquare$

---

## Potencial químico: $G$ para sistemas multicomponentes

> [!proposicion]
> Para una mezcla de $k$ componentes, la energía de Gibbs extensiva es función de $(T, P, n_1, \ldots, n_k)$:
> $$dG = -S\,dT + V\,dP + \sum_{i=1}^{k}\mu_i\,dn_i,$$
> donde el **potencial químico** del componente $i$ es:
> $$\mu_i \equiv \left(\frac{\partial G}{\partial n_i}\right)_{T,P,n_{j\neq i}}.$$
> $\mu_i$ [kJ/mol] es la energía de Gibbs que se añade al sistema cuando se introduce un mol del componente $i$ a $(T, P)$ y composición constantes. Para una sustancia pura, $\mu = g$ (energía de Gibbs molar).

---

## Equilibrio de fases: ecuación de Clapeyron

> [!demostracion]
> **Meta:** deducir la pendiente $dP_{sat}/dT$ de la curva de saturación a partir de la condición de equilibrio de fases.
>
> **Hipótesis:** coexistencia de dos fases (f = líquido, g = vapor) en equilibrio; el equilibrio requiere $T_f = T_g$, $P_f = P_g$ y, crucialmente, $\mu_f = \mu_g$, es decir, $g_f = g_g$ (potenciales químicos iguales para sustancia pura).
>
> **Paso 1 — Condición de coexistencia.**
> A lo largo de la curva de saturación, $g_f(T, P_{sat}) = g_g(T, P_{sat})$ en todos los puntos. Diferenciando este requisito cuando $(T, P)$ cambian a lo largo de la curva:
> $$dg_f = dg_g.$$
>
> **Paso 2 — Expandir usando $dg = -s\,dT + v\,dP$.**
> $$-s_f\,dT + v_f\,dP = -s_g\,dT + v_g\,dP.$$
>
> **Paso 3 — Reordenar.**
> $$(s_g - s_f)\,dT = (v_g - v_f)\,dP \implies \frac{dP_{sat}}{dT} = \frac{s_g - s_f}{v_g - v_f} = \frac{s_{fg}}{v_{fg}}.$$
>
> **Paso 4 — Usar $s_{fg} = h_{fg}/T_{sat}$.**
> El cambio de entropía en el cambio de fase isobárico-isotérmico es $\Delta s = h_{fg}/T_{sat}$ (el calor $h_{fg}$ se transfiere a temperatura constante $T_{sat}$). Por tanto:
> $$\boxed{\frac{dP_{sat}}{dT} = \frac{h_{fg}}{T_{sat}\,v_{fg}}.}$$
>
> **Paso 5 — Verificación de signos y límites.**
> Para vaporización ($h_{fg} > 0$, $v_{fg} > 0$): $dP_{sat}/dT > 0$ — la presión de saturación crece con la temperatura. Para fusión del agua ($h_{fg} > 0$, $v_{fg} < 0$ porque el hielo es menos denso que el agua): $dP_{sat}/dT < 0$ — el hielo se funde a mayor presión, lo que explica el patinaje sobre hielo. $\checkmark\,\blacksquare$

![[gibbs_curva_saturacion_Clapeyron.svg|440]]
*Diagrama $P$-$T$ con las curvas de saturación (sólido-líquido, líquido-vapor, sólido-vapor) y el punto triple. La pendiente de cada curva es $dP/dT = h_{fg}/(T v_{fg})$. Para el agua, la curva sólido-líquido tiene pendiente negativa (anotada en la figura).*

---

## Gibbs-Duhem: no toda la variación de potenciales es independiente

> [!proposicion]
> Para un sistema a composición constante con $G = nG/n = n\bar{g} = n\mu$ (sustancia pura):
> $$G = \sum_i n_i\,\mu_i \implies dG = \sum_i n_i\,d\mu_i + \sum_i \mu_i\,dn_i.$$
> Comparando con $dG = -S\,dT + V\,dP + \sum_i \mu_i\,dn_i$:
> $$\boxed{S\,dT - V\,dP + \sum_i n_i\,d\mu_i = 0.}$$
> Esta es la **ecuación de Gibbs-Duhem**: las variaciones de los potenciales químicos de los componentes de una mezcla no son independientes — están ligadas por $(T, P)$ y la composición. Para una sustancia pura: $n\,d\mu = S\,dT - V\,dP \implies d\mu = -s\,dT + v\,dP$, que confirma que $\mu = g$ (energía de Gibbs molar).

---

## Variación de $G$ con la presión: gases y líquidos

> [!proposicion]
> De $(\partial g/\partial P)_T = v$:
>
> **Gas ideal** ($v = RT/P$):
> $$g(T, P) = g^\circ(T) + RT\ln\frac{P}{P^\circ},$$
> donde $g^\circ$ es la energía de Gibbs estándar a presión de referencia $P^\circ = 100\,\text{kPa}$ (o 1 atm). La fugacidad de una mezcla generaliza este resultado: $g_i = g_i^\circ + RT\ln(f_i/f_i^\circ)$.
>
> **Líquido incompresible** ($v \approx v_f = \text{cte}$):
> $$g(T, P) \approx g_f(T, P_{sat}) + v_f\,[P - P_{sat}(T)].$$
> Esta corrección es pequeña para presiones moderadas (< 10 MPa), lo que explica por qué en procesos a presión baja-moderada los líquidos se comportan con $g \approx g_f(T)$.

---

## Ejemplo: ebullición del agua y efecto de la altitud

> [!ejemplo]
> **El agua hierve donde $g_f(T,P) = g_g(T,P)$, es decir, donde $P = P_{sat}(T)$.** A nivel del mar, $P = 101.3\,\text{kPa}$, la curva de Clausius-Clapeyron da $T_{sat} = 100\,°\text{C}$.
>
> **Paso 1 — En Ciudad de México a $P = 78\,\text{kPa}$**, ¿a qué temperatura hierve el agua?
>
> **Paso 2 — Usar la ecuación de Clausius-Clapeyron simplificada** (válida con $v_{fg} \approx RT/P$):
> $$\ln\frac{P_2}{P_1} \approx \frac{h_{fg}}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right) = -\frac{h_{fg}}{R}\,\frac{T_2 - T_1}{T_1 T_2}.$$
>
> **Paso 3 — Despejar $T_2$:** con $h_{fg} = 2257\,\text{kJ/kg}$, $R = 0.4615\,\text{kJ/(kg·K)}$ (agua), $T_1 = 373.15\,\text{K}$:
> $$T_2 \approx T_1 - \frac{T_1^2 R}{h_{fg}}\ln\frac{P_2}{P_1} = 373.15 - \frac{373.15^2 \times 0.4615}{2257}\ln\frac{78}{101.3}$$
> $$= 373.15 - 28.46 \times (-0.261) = 373.15 + 7.43 \approx 365.7\,\text{K} = 92.6\,°\text{C}.$$
>
> **Paso 4 — Interpretación:** el agua hierve a $\sim 92{-}93\,°\text{C}$ en Ciudad de México, no a 100 °C. Para cocinar pastas o legumbres (que requieren 100 °C para cocerse correctamente), se necesita una olla de presión que restaure la presión de saturación a 100 °C. El criterio de equilibrio $g_f = g_g$ (o equivalentemente la ecuación de Clapeyron) explica directamente este efecto. $\blacksquare$

---

## Relación con otras notas

> [!info]
> - Las reacciones de combustión y el entalpía de formación usan $\Delta G^\circ$; ver [[Combustion/index | Combustión]].
> - La ecuación de Clapeyron y las curvas de saturación de agua se tabulan en [[Sustancias Puras/index | Sustancias Puras]].
> - El equilibrio de mezclas y fugacidades es el tema central de [[Mezclas/index | Mezclas]].
> - $G$ mínimo a $(T,P)$ constantes equivale a $S$ máxima total; ver [[Entropia]].
> - El potencial químico en mezclas ideales: $\mu_i = g_i^\circ + RT\ln y_i$; ver [[Mezcla Gas Ideal]].

> [!info]
> **Convención:** $G$: extensiva [kJ]; $g = G/m$ [kJ/kg]; $\bar{g} = G/n$ [kJ/mol]; $\mu = \bar{g}$ para sustancia pura.
> Estándar: $g^\circ$ a $T$ dada y $P^\circ = 100\,\text{kPa}$.

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, §12.2–12.4; Callen, *Thermodynamics*, §6-1 a 6-4 y §7-1 a 7-3; Çengel & Boles, *Termodinámica*, §12-1, §14-1; Moran & Shapiro, §12.3–12.4; Clausius-Clapeyron en todo texto de termodinámica clásica.
