---
title: Temperatura Adiabática de Llama
order: 2
tags:
  - termodinamica
  - mezclas
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
> La **temperatura adiabática de llama** ($T_{\rm AFT}$) es la temperatura que alcanzan los productos de combustión cuando la reacción ocurre sin pérdida de calor al entorno ($\dot{Q}=0$) y sin trabajo de eje. Es el **límite termodinámico superior** de temperatura: cualquier proceso de combustión real tiene $T_{\rm real} < T_{\rm AFT}$, porque siempre existe alguna pérdida de calor o disociación.
>
> *Importancia práctica:* $T_{\rm AFT}$ determina el nivel máximo de temperatura que deben soportar los materiales en turbinas de gas (álabes, cámara de combustión) y motores de explosión (pistones, culata). Diseñar con exceso de aire ($\Phi < 1$) reduce $T_{\rm AFT}$ y permite usar materiales más baratos; pero reduce también la eficiencia del ciclo. Este compromiso define la relación de equivalencia óptima en el diseño de turbinas.

---

## Balance de entalpía para la TAF

> [!teorema]
> En una cámara de combustión estacionaria adiabática ($\dot{Q}=0$, $\dot{W}=0$):
> $$H_{\rm react}(T_R) = H_{\rm prod}(T_{\rm AFT}),$$
> donde la entalpía total de cada corriente es:
> $$H = \sum_i n_i\,\bar{h}_i(T) = \sum_i n_i\!\left[\bar{h}_{f,i}^\circ + \Delta\bar{h}_i(T)\right],$$
> con $\Delta\bar{h}_i(T) = \bar{h}_i(T) - \bar{h}_i(T^\circ)$ el incremento de entalpía sensible desde $T^\circ = 298.15\,\mathrm{K}$.

> [!demostracion]
> **Hipótesis:** VC estacionario, $\dot{Q}=0$, $\dot{W}=0$, sin EC ni EP, combustión completa.
>
> **Paso 1 — Primera ley del VC.** En régimen estacionario:
> $$\dot{Q} - \dot{W} = \dot{H}_{\rm sal} - \dot{H}_{\rm ent} \implies \dot{H}_{\rm react} = \dot{H}_{\rm prod}.$$
>
> **Paso 2 — Descomponer la entalpía.** Para cada especie, en la escala de referencia de las entalpías de formación:
> $$\bar{h}_i(T) = \underbrace{\bar{h}_{f,i}^\circ}_{\text{química}} + \underbrace{\Delta\bar{h}_i(T)}_{\text{sensible}}.$$
>
> **Paso 3 — Escribir el balance explícitamente:**
> $$\sum_j n_j\!\left[\bar{h}_{f,j}^\circ + \Delta\bar{h}_j(T_R)\right] = \sum_i n_i\!\left[\bar{h}_{f,i}^\circ + \Delta\bar{h}_i(T_{\rm AFT})\right].$$
>
> **Paso 4 — Caso especial $T_R=T^\circ=298.15\,\mathrm{K}$.** Entonces $\Delta\bar{h}_j(T_R)=0$ y el balance se simplifica a:
> $$\sum_j n_j\,\bar{h}_{f,j}^\circ = \sum_i n_i\!\left[\bar{h}_{f,i}^\circ + \Delta\bar{h}_i(T_{\rm AFT})\right].$$
>
> **Paso 5 — Reformular en términos del calor de reacción.** Restando $\sum_i n_i\,\bar{h}_{f,i}^\circ$ de ambos lados:
> $$\underbrace{\sum_j n_j\,\bar{h}_{f,j}^\circ - \sum_i n_i\,\bar{h}_{f,i}^\circ}_{= -(-\bar{h}_R^\circ) = \text{calor de reacción}} = \sum_i n_i\,\Delta\bar{h}_i(T_{\rm AFT}).$$
> $$\boxed{-\bar{h}_R^\circ = \sum_i n_i\,\Delta\bar{h}_i(T_{\rm AFT}).}$$
>
> Todo el calor de reacción $-\bar{h}_R^\circ$ va íntegramente a elevar la temperatura (entalpía sensible) de los productos. $\blacksquare$

---

## Efecto del exceso de aire

> [!teoria]
> El exceso de aire diluye los productos con $\mathrm{N_2}$ y $\mathrm{O_2}$ adicionales. El calor de reacción $-\bar{h}_R^\circ$ es **constante** (no depende del exceso), pero debe elevar la temperatura de una **mayor masa** de productos:
>
> $$T_{\rm AFT}\downarrow \quad\text{cuando}\quad\%\,\text{exceso de aire}\uparrow.$$
>
> La temperatura máxima se alcanza con la **mezcla estequiométrica** ($\Phi=1$) y reactivos a $25\,°\mathrm{C}$. El precalentamiento de los reactivos ($T_R > 25\,°\mathrm{C}$) eleva $T_{\rm AFT}$, pero el efecto es secundario comparado con el exceso de aire.

![[taf_vs_exceso_aire.svg|420]]
*$T_{\rm AFT}$ del metano en función del porcentaje de exceso de aire. A exceso 0% (estequiométrico): $T_{\rm AFT}\approx2230\,\mathrm{K}$. El descenso es casi lineal para excesos moderados (<100%) porque el calor sensible del N₂ es casi lineal en ese rango.*

---

## Método de cálculo iterativo

> [!proposicion]
> Algoritmo para calcular $T_{\rm AFT}$ con tablas de entalpía (JANAF o apéndices de Moran & Shapiro):
>
> **Paso 1 — Balancear la reacción** y determinar los $n_i$ de cada producto.
>
> **Paso 2 — Calcular el calor de reacción:**
> $$-\bar{h}_R^\circ = \sum_{\rm react} n_j\,\bar{h}_{f,j}^\circ - \sum_{\rm prod} n_i\,\bar{h}_{f,i}^\circ.$$
>
> **Paso 3 — Estimación inicial** con calores específicos medios promedio:
> $$T_{\rm AFT}^{(0)} \approx T_R + \frac{-\bar{h}_R^\circ}{\displaystyle\sum_i n_i\,\bar{c}_{p,i}^{\rm medio}}.$$
>
> **Paso 4 — Evaluar desde tablas.** Calcular $\sum_i n_i\,\Delta\bar{h}_i(T)$ a dos temperaturas $T_a$ y $T_b$ que encuadren $T_{\rm AFT}^{(0)}$.
>
> **Paso 5 — Interpolar linealmente** para encontrar $T_{\rm AFT}$ exacto:
> $$T_{\rm AFT} = T_a + \frac{-\bar{h}_R^\circ - \sum_i n_i\,\Delta\bar{h}_i(T_a)}{\sum_i n_i\,\Delta\bar{h}_i(T_b) - \sum_i n_i\,\Delta\bar{h}_i(T_a)}\times(T_b-T_a).$$

---

## Ejemplo: combustión de metano con 150% de aire

> [!ejemplo]
> Metano ($\mathrm{CH_4}$, $\bar{h}_f^\circ=-74850\,\mathrm{kJ/kmol}$) quema con 150% de aire teórico. Reactivos a $T_R=25\,°\mathrm{C}=298.15\,\mathrm{K}$. Calcular $T_{\rm AFT}$.

> [!solucion]
> **Datos de entalpía de formación:** $\bar{h}_f^\circ[\mathrm{CO_2}]=-393520$; $\bar{h}_f^\circ[\mathrm{H_2O(g)}]=-241826$; $\bar{h}_f^\circ[\mathrm{O_2}]=\bar{h}_f^\circ[\mathrm{N_2}]=0$ (todos en kJ/kmol).
>
> **Paso 1 — Reacción con 150% de aire.** $a_{\rm est}=1+4/4=2$ para $\mathrm{CH_4}$; con $\Phi=1/1.5$: $a=1.5\times2=3$ mol $\mathrm{O_2}$:
> $$\mathrm{CH_4}+3\,\mathrm{O_2}+3\times3.76\,\mathrm{N_2}\to\mathrm{CO_2}+2\,\mathrm{H_2O}+1\,\mathrm{O_2}+11.28\,\mathrm{N_2}.$$
> Verificación: O: $6=2+2+2$ ✓; H: $4=4$ ✓; N: $22.56=22.56$ ✓.
>
> **Paso 2 — Calor de reacción:**
> $$-\bar{h}_R^\circ = \sum_{\rm react}n_j\bar{h}_{f,j}^\circ - \sum_{\rm prod}n_i\bar{h}_{f,i}^\circ$$
> $$= [(-74850)+0+0] - [(-393520)+2(-241826)+0+0]$$
> $$= -74850 - (-877172) = +802\,322\,\mathrm{kJ/kmol\,CH_4}.$$
>
> **Paso 3 — Estimación inicial.** $\bar{c}_p$ medios (1000–2000 K, kJ/(kmol·K)): $\bar{c}_p[\mathrm{CO_2}]\approx50$, $\bar{c}_p[\mathrm{H_2O}]\approx38$, $\bar{c}_p[\mathrm{O_2}]\approx33$, $\bar{c}_p[\mathrm{N_2}]\approx32$:
> $$\sum n_i\bar{c}_{p,i}=50+2\times38+33+11.28\times32=50+76+33+360.96=520.0\,\mathrm{kJ/K}.$$
> $$T_{\rm AFT}^{(0)}=298+802322/520.0=298+1543\approx1841\,\mathrm{K}.$$
>
> **Paso 4 — Evaluación con tablas JANAF** ($\Delta\bar{h}(T)=\bar{h}(T)-\bar{h}(298\,\mathrm{K})$ en kJ/kmol):
>
> | Componente | $n_i$ | $\Delta\bar{h}(1800\,\mathrm{K})$ | $n_i\Delta\bar{h}$ | $\Delta\bar{h}(1900\,\mathrm{K})$ | $n_i\Delta\bar{h}$ |
> |:---:|:---:|:---:|:---:|:---:|:---:|
> | $\mathrm{CO_2}$ | 1 | 79 432 | 79 432 | 87 600 | 87 600 |
> | $\mathrm{H_2O}$ | 2 | 57 999 | 115 998 | 63 288 | 126 576 |
> | $\mathrm{O_2}$ | 1 | 45 648 | 45 648 | 48 807 | 48 807 |
> | $\mathrm{N_2}$ | 11.28 | 43 491 | 490 575 | 46 612 | 525 803 |
> | **Total** | | | **731 653** | | **788 786** |
>
> **Paso 5 — Interpolación:**
> $$T_{\rm AFT}=1800+\frac{802322-731653}{788786-731653}\times(1900-1800)=1800+\frac{70669}{57133}\times100.$$
> $$=1800+123.7\approx\boxed{1924\,\mathrm{K}=1651\,°\mathrm{C}.}$$
>
> **Verificación de razonabilidad.** Para $\mathrm{CH_4}$ estequiométrico $T_{\rm AFT}\approx2230\,\mathrm{K}$. Con 50% de exceso de aire la temperatura baja 306 K (14%): consistente con la literatura. $\blacksquare$

---

## Temperatura real vs. TAF

> [!teoria]
> En aplicaciones reales $T_{\rm real} < T_{\rm AFT}$ por varios efectos:
>
> | Causa | Efecto sobre $T$ |
> |:---|:---|
> | Pérdidas de calor a las paredes | $T\downarrow$ |
> | Disociación de $\mathrm{CO_2}$ y $\mathrm{H_2O}$ ($T>1500\,\mathrm{K}$) | $T\downarrow$ (reacciones endotérmicas) |
> | Combustión incompleta (CO, H₂ en escape) | $T\downarrow$ (calor latente sin liberar) |
> | Precalentamiento de reactivos ($T_R > 25\,°\mathrm{C}$) | $T\uparrow$ |
>
> La **disociación** es el efecto limitante más importante: por encima de $\sim\!1800\,\mathrm{K}$, $\mathrm{CO_2}\rightleftharpoons\mathrm{CO}+\tfrac{1}{2}\mathrm{O_2}$ y $\mathrm{H_2O}\rightleftharpoons\mathrm{H_2}+\tfrac{1}{2}\mathrm{O_2}$ absorben parte del calor. La temperatura real en cámaras de combustión de turbinas de gas ($T_{\rm AFT}\approx1800$–$2100\,\mathrm{K}$) se lleva a $T_{\rm entrada\,álabe}\approx1400$–$1700\,\mathrm{K}$ con refrigeración activa de los álabes.

> [!referencia]
> Çengel & Boles, §15-5; Moran & Shapiro, §13.3–13.4; Borgnakke & Sonntag, §13.5. Tablas NIST-JANAF para $\bar{h}_f^\circ$ y $\Delta\bar{h}(T)$.
