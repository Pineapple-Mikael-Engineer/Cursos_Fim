---
title: Temperatura Adiabática de Llama
tags:
  - termodinamica
  - teoria
  - combustion
  - temperatura-llama
  - entalpia-formacion
draft: false
aliases:
  - Temperatura Adiabatica de Llama
  - TAF
  - Adiabatic Flame Temperature
  - AFT
---

# Temperatura Adiabática de Llama

> [!definicion]
> La **temperatura adiabática de llama** ($T_{\rm AFT}$) es la temperatura máxima que alcanzan los productos de combustión cuando la reacción ocurre sin pérdidas de calor al entorno ($\dot{Q}=0$) y sin trabajo de eje. Es el límite superior de temperatura de cualquier proceso de combustión real. Todo el calor de reacción va íntegramente a elevar la temperatura de los productos.

---

## Balance de entalpía

Para una cámara de combustión en régimen estacionario ($\dot{Q}=0$, $\dot{W}=0$, $\Delta\mathrm{Ec}=0$):

$$H_{\rm reactivos}(T_R) = H_{\rm productos}(T_{\rm AFT})$$

donde $H$ es la entalpía total (en base molar):
$$H = \sum_i n_i\,\bar{h}_i(T) = \sum_i n_i\left[\bar{h}_{f,i}^\circ + \Delta\bar{h}_i(T)\right]$$
con $\Delta\bar{h}_i(T) = \bar{h}_i(T) - \bar{h}_i(T^\circ)$ el incremento de entalpía sensible desde $T^\circ=298.15\,\mathrm{K}$.

La ecuación de $T_{\rm AFT}$ queda:
$$\sum_{\rm react} n_j\left[\bar{h}_{f,j}^\circ + \Delta\bar{h}_j(T_R)\right] = \sum_{\rm prod} n_i\left[\bar{h}_{f,i}^\circ + \Delta\bar{h}_i(T_{\rm AFT})\right].$$

Si los reactivos entran a $T_R=25\,°\mathrm{C}=T^\circ$ ($\Delta\bar{h}_j=0$):
$$\sum_{\rm react} n_j\,\bar{h}_{f,j}^\circ = \sum_{\rm prod} n_i\left[\bar{h}_{f,i}^\circ + \Delta\bar{h}_i(T_{\rm AFT})\right]$$
$$\underbrace{-\bar{h}_R^\circ}_{\mathrm{calor\ de\ reacci\acute{o}n}} = \sum_{\rm prod} n_i\,\Delta\bar{h}_i(T_{\rm AFT}).$$

El calor de reacción se reparte como entalpía sensible entre todos los productos: la solución de esta ecuación para $T_{\rm AFT}$ requiere **iteración** con las tablas de entalpía de los productos.

---

## Efecto del exceso de aire sobre $T_{\rm AFT}$

El exceso de aire diluye los productos con $\mathrm{N_2}$ y $\mathrm{O_2}$ adicionales sin contribuir al calor de reacción. El calor $-\bar{h}_R^\circ$ es constante (fijado por la estequiometría), pero debe elevar la temperatura de una mayor masa de productos:

$$T_{\rm AFT}\downarrow \quad\text{cuando}\quad\%\,\text{exceso de aire}\uparrow.$$

$T_{\rm AFT}$ también disminuye si los reactivos entran a temperatura mayor (mayor $\Delta\bar{h}_j(T_R)$) — este efecto es opuesto y pequeño comparado con el del exceso de aire. La temperatura máxima se alcanza con la **mezcla estequiométrica** y reactivos a $25\,°\mathrm{C}$.

![[taf_vs_exceso_aire.svg|420]]
*$T_{\rm AFT}$ del metano como función del porcentaje de exceso de aire. A exceso 0% (estequiométrico): $T_{\rm AFT}\approx2230\,\mathrm{K}$. El descenso es casi lineal para excesos moderados (<100%) porque el calor sensible de $\mathrm{N_2}$ es casi lineal en ese rango de temperatura.*

---

## Método de cálculo iterativo

> [!proposicion] Algoritmo para $T_{\rm AFT}$
> **Paso 1.** Balancear la reacción y calcular $n_i$ para cada producto.
>
> **Paso 2.** Calcular el calor de reacción:
> $$-\bar{h}_R^\circ = \sum_{\rm react} n_j\,\bar{h}_{f,j}^\circ - \sum_{\rm prod} n_i\,\bar{h}_{f,i}^\circ.$$
>
> **Paso 3.** Estimar $T_{\rm AFT}^{(0)}$ con capacidades caloríficas constantes:
> $$T_{\rm AFT}^{(0)} \approx T_R + \frac{-\bar{h}_R^\circ}{\sum_i n_i\,\bar{c}_{p,i}}.$$
>
> **Paso 4.** Evaluar $\sum_{\rm prod} n_i\,\Delta\bar{h}_i(T)$ desde tablas a $T=T_{\rm AFT}^{(0)}$.
> Si difiere de $-\bar{h}_R^\circ$: interpolar linealmente entre dos temperaturas de tabla para obtener $T_{\rm AFT}$.
>
> **Paso 5.** Verificar con las tablas y refinar si es necesario.

---

## Ejemplo: combustión de metano con 150% de aire

> [!ejemplo]
> Metano ($\mathrm{CH_4}$) quema con $150\%$ de aire teórico. Reactivos a $T_R=25\,°\mathrm{C}=298.15\,\mathrm{K}$. Calcular $T_{\rm AFT}$.

> [!solucion]
> **Datos:**
> $\bar{h}_f^\circ[\mathrm{CH_4}]=-74850\,\mathrm{kJ/kmol}$; $\bar{h}_f^\circ[\mathrm{CO_2}]=-393520$; $\bar{h}_f^\circ[\mathrm{H_2O(g)}]=-241826$; $\bar{h}_f^\circ[\mathrm{O_2}]=\bar{h}_f^\circ[\mathrm{N_2}]=0$.
>
> **Paso 1 — Reacción con 150% de aire ($\Phi=1/1.5$).** $a_{\rm est}=1+4/4=2$ para $\mathrm{CH_4}$:
> $$\mathrm{CH_4}+\frac{2}{1/1.5}(\mathrm{O_2}+3.76\,\mathrm{N_2})\to\mathrm{CH_4}+3\,\mathrm{O_2}+11.28\,\mathrm{N_2}$$
> $$\to\mathrm{CO_2}+2\,\mathrm{H_2O}+1\,\mathrm{O_2}+11.28\,\mathrm{N_2}.$$
> Verificación O: $6=2+2+2=6$ ✓; H: $4=4$ ✓; N: $22.56=22.56$ ✓.
>
> **Paso 2 — Calor de reacción** (reactivos a 25°C, productos de referencia):
> $$-\bar{h}_R^\circ = \sum_{\rm react}n_j\bar{h}_{f,j}^\circ - \sum_{\rm prod}n_i\bar{h}_{f,i}^\circ$$
> $$= [1\cdot(-74850)+0+0] - [1\cdot(-393520)+2\cdot(-241826)+1\cdot0+11.28\cdot0]$$
> $$= -74850 - [-393520-483652]= -74850-(-877172)=+802322\,\mathrm{kJ/kmol\,CH_4}.$$
>
> **Paso 3 — Estimación inicial** con $\bar{c}_p$ promedio (en kJ/(kmol·K)):
> $\bar{c}_p[\mathrm{CO_2}]\approx50$, $\bar{c}_p[\mathrm{H_2O}]\approx38$, $\bar{c}_p[\mathrm{O_2}]\approx33$, $\bar{c}_p[\mathrm{N_2}]\approx32$ (valores promedio 1000–2000 K).
> $$\sum n_i\bar{c}_{p,i}=1\times50+2\times38+1\times33+11.28\times32=50+76+33+360.96=519.96\,\mathrm{kJ/K}.$$
> $$T_{\rm AFT}^{(0)}=298.15+\frac{802322}{519.96}\approx298+1543=1841\,\mathrm{K}.$$
>
> **Paso 4 — Evaluación con tablas de entalpía sensible** $\Delta\bar{h}(T)=\bar{h}(T)-\bar{h}(298\,\mathrm{K})$:
>
> De tablas JANAF/Apéndice Moran & Shapiro (valores en kJ/kmol):
>
> | Componente | $\Delta\bar{h}(1800\,\mathrm{K})$ | $\Delta\bar{h}(1900\,\mathrm{K})$ |
> |:---:|:---:|:---:|
> | $\mathrm{CO_2}$ | 79432 | 87600 |
> | $\mathrm{H_2O}$ | 57999 | 63288 |
> | $\mathrm{O_2}$ | 45648 | 48807 |
> | $\mathrm{N_2}$ | 43491 | 46612 |
>
> A $T=1800\,\mathrm{K}$:
> $$\sum n_i\Delta\bar{h}_i = 1\times79432+2\times57999+1\times45648+11.28\times43491$$
> $$=79432+115998+45648+490375=731453\,\mathrm{kJ/kmol}.$$
>
> A $T=1900\,\mathrm{K}$:
> $$\sum n_i\Delta\bar{h}_i = 1\times87600+2\times63288+1\times48807+11.28\times46612$$
> $$=87600+126576+48807+525898=788881\,\mathrm{kJ/kmol}.$$
>
> **Paso 5 — Interpolación.** Necesitamos $\sum n_i\Delta\bar{h}_i = -\bar{h}_R^\circ = 802322\,\mathrm{kJ/kmol}$:
> $$T_{\rm AFT}=1800+\frac{802322-731453}{788881-731453}\times(1900-1800)=1800+\frac{70869}{57428}\times100.$$
> $$=1800+\frac{70869}{57428}\times100=1800+123.4\approx1923\,\mathrm{K}.$$
> $$\boxed{T_{\rm AFT}\approx1923\,\mathrm{K}=1650\,°\mathrm{C}.}$$
>
> **Verificación de razonabilidad.** Para $\mathrm{CH_4}$ estequiométrico: $T_{\rm AFT}\approx2230\,\mathrm{K}$. Con 50% de exceso de aire los productos absorben más masa, por lo que la temperatura baja. De $2230$ a $1923\,\mathrm{K}$: reducción de $307\,\mathrm{K}$ con 50% de exceso. Es consistente con los datos de la literatura. $\blacksquare$

---

## Temperatura de llama en aplicaciones reales

En aplicaciones reales $T_{\rm real} < T_{\rm AFT}$ por:

| Causa | Efecto |
|:---|:---|
| Pérdidas de calor a las paredes | $\dot{Q}<0$ → productos más fríos |
| Disociación de $\mathrm{CO_2}$ y $\mathrm{H_2O}$ a $T>1500\,\mathrm{K}$ | Reacciones endotérmicas consumen parte del calor |
| Combustión incompleta | $\mathrm{CO}$, $\mathrm{H_2}$ en productos; $-\bar{h}_R^\circ$ efectivo menor |
| Reactivos a $T_R>25\,°\mathrm{C}$ (precalentamiento) | Eleva $T_{\rm AFT}$ (efecto positivo) |

La disociación es el factor limitante más importante: por encima de $\sim1800\,\mathrm{K}$ la reacción $\mathrm{CO_2}\rightleftharpoons\mathrm{CO}+\frac{1}{2}\mathrm{O_2}$ (y $\mathrm{H_2O}\rightleftharpoons\mathrm{H_2}+\frac{1}{2}\mathrm{O_2}$) se vuelve significativa, reduciendo el calor disponible.

> [!referencia]
> Çengel & Boles, *Termodinámica*, §15-5; Moran & Shapiro §13.3–13.4; Borgnakke & Sonntag §13.5. Tablas NIST-JANAF para $\bar{h}^\circ_f$ y $\Delta\bar{h}(T)$.
