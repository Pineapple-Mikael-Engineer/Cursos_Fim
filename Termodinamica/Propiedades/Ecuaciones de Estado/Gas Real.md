---
title: "Gas real"
order: 2
tags:
  - termodinamica
  - propiedades
  - ecuaciones_de_estado
  - gas_real
draft: false
aliases:
  - real gas
  - van der Waals
  - factor de compresibilidad
  - Z
---

# Gas real $Z = Pv/RT \neq 1$

> [!definicion]
> Un **gas real** es una sustancia gaseosa donde las moléculas tienen **volumen propio finito** y **fuerzas atractivas** entre sí. Estos dos efectos hacen que el comportamiento se desvíe del gas ideal, especialmente a alta presión y baja temperatura. El desvío se cuantifica mediante el **factor de compresibilidad**:
> $$
> Z \equiv \frac{Pv}{RT},
> $$
> que vale exactamente $1$ para el gas ideal. Cuando $Z < 1$ dominan las atracciones (el gas ocupa menos volumen del esperado); cuando $Z > 1$ domina el covolumen (las moléculas se repelen a distancia muy corta y el gas ocupa más).

![[gas_real_factor_Z_Nelson_Obert.svg|460]]
*Carta de Nelson-Obert generalizada: $Z$ como función de $P_r = P/P_c$ para distintos $T_r = T/T_c$. A $T_r > 2$ el gas se comporta casi idealmente a cualquier presión. La región $Z < 1$ (debajo de la isoterma de $T_r=1$) corresponde a atracción dominante; la región $Z > 1$ (a $P_r$ muy alta) corresponde a repulsión/covolumen dominante.*

---

## Ecuación de van der Waals

> [!teorema]
> La EOS cúbica prototipo para gas real (forma molar):
> $$
> \left(P + \frac{a}{\bar{v}^{\,2}}\right)(\bar{v} - b) = R_u T.
> $$
> - $a/\bar{v}^{\,2}$: **presión interna** — corrección que añade presión efectiva por atracción molecular. Las moléculas atraídas hacia el interior reducen la presión sobre las paredes; el término $a/\bar{v}^2$ la compensa.
> - $b$: **covolumen** — volumen molar excluido por el tamaño finito de las moléculas. El volumen disponible para moverse es $\bar{v} - b$, no $\bar{v}$.

> [!demostracion]
> **Objetivo:** deducir $a$ y $b$ en función de las propiedades críticas $T_c$, $P_c$, $\bar{v}_c$.
>
> **Hipótesis:** el punto crítico es un **punto de inflexión horizontal** de la isoterma $P(\bar{v})$ en el diagrama $P$-$\bar{v}$.
>
> **Paso 1 — Condiciones matemáticas en el punto crítico.** Para que sea un punto de inflexión y simultáneamente el máximo de la campana de saturación:
> $$
> \left(\frac{\partial P}{\partial \bar{v}}\right)_{T_c} = 0, \qquad \left(\frac{\partial^2 P}{\partial \bar{v}^{\,2}}\right)_{T_c} = 0.
> $$
>
> **Paso 2 — Expresar $P$ despejando de la EOS de van der Waals:**
> $$
> P = \frac{R_u T}{\bar{v}-b} - \frac{a}{\bar{v}^{\,2}}.
> $$
>
> **Paso 3 — Derivar e igualar a cero (a $T = T_c$, $\bar{v} = \bar{v}_c$):**
> $$
> \frac{\partial P}{\partial \bar{v}} = -\frac{R_u T_c}{(\bar{v}_c-b)^2} + \frac{2a}{\bar{v}_c^3} = 0 \tag{1}
> $$
> $$
> \frac{\partial^2 P}{\partial \bar{v}^2} = \frac{2R_u T_c}{(\bar{v}_c-b)^3} - \frac{6a}{\bar{v}_c^4} = 0 \tag{2}
> $$
>
> **Paso 4 — Resolver el sistema.** Dividiendo (2)/(1) × $(-1)$:
> $$
> \frac{2}{\bar{v}_c - b} = \frac{3}{\bar{v}_c} \implies \bar{v}_c = 3b.
> $$
> Sustituyendo en (1): $R_u T_c/(2b)^2 = 2a/(3b)^3 \implies T_c = 8a/(27 R_u b)$. Con $P_c = R_u T_c/(\bar{v}_c-b) - a/\bar{v}_c^2 = R_u T_c/(2b) - a/(9b^2)$, finalmente:
>
> $$
> \boxed{a = \frac{27 R_u^2 T_c^2}{64 P_c}, \qquad b = \frac{R_u T_c}{8 P_c}.} \qquad \blacksquare
> $$
>
> *Nota:* la predicción $\bar{v}_c = 3b = 3R_uT_c/(8P_c)$ implica $Z_c = P_c\bar{v}_c/(R_uT_c) = 3/8 = 0.375$ para cualquier gas van der Waals — el valor experimental está entre $0.23$–$0.29$, lo que indica que van der Waals sobreestima $\bar{v}_c$ cerca del punto crítico.

---

## Energía interna y $c_p - c_v$ del gas real

> [!proposicion]
> A diferencia del gas ideal, en un gas real la energía interna depende del volumen. De la ecuación térmica de la energía (derivada de las relaciones $TdS$ y Maxwell):
> $$
> \left(\frac{\partial \bar{u}}{\partial \bar{v}}\right)_T = T\left(\frac{\partial P}{\partial T}\right)_{\bar{v}} - P.
> $$
> Para van der Waals, $(\partial P/\partial T)_{\bar{v}} = R_u/(\bar{v}-b)$, entonces:
> $$
> \left(\frac{\partial \bar{u}}{\partial \bar{v}}\right)_T = \frac{R_u T}{\bar{v}-b} - P = \frac{a}{\bar{v}^{\,2}} > 0.
> $$
> Al expandir, las moléculas se separan contra la atracción: la energía interna **aumenta** durante una expansión isotérmica. Por eso un gas real se enfría al expandirse libremente (experimento de Joule).

> [!proposicion]
> La diferencia $c_p - c_v$ para cualquier fluido (derivada de las relaciones termodinámicas exactas):
> $$
> c_p - c_v = -T\frac{\left[(\partial P/\partial T)_v\right]^2}{(\partial P/\partial v)_T} = \frac{Tv\alpha_P^2}{\kappa_T},
> $$
> donde $\alpha_P = (1/v)(\partial v/\partial T)_P$ es el coeficiente de expansión térmica y $\kappa_T = -(1/v)(\partial v/\partial P)_T$ la compresibilidad isotérmica. Para el gas ideal ($Pv=RT$): $\alpha_P = 1/T$, $\kappa_T = 1/P$, y la fórmula da $c_p - c_v = R$ (consistente). Para van der Waals, la corrección aumenta con la presión.

---

## Principio de estados correspondientes

> [!teoria]
> En términos de las **propiedades reducidas** $P_r = P/P_c$, $T_r = T/T_c$, $\bar{v}_r = \bar{v}/\bar{v}_c$, el factor de compresibilidad es **casi universal** para gases no polares:
> $$
> Z \approx Z(P_r, T_r) \quad \text{(principio de estados correspondientes)}.
> $$
> Esto justifica las **cartas de compresibilidad generalizadas** (Nelson-Obert, Pitzer): conociendo $T_c$ y $P_c$ de la sustancia, se puede estimar $Z$ y con él $v = ZRT/P$.
>
> Tendencias clave en la carta:
> - $P_r \to 0$ (cualquier $T_r$): $Z \to 1$ (límite ideal).
> - $T_r > 2$ (cualquier $P_r$ razonable): $Z \approx 1$ (gas casi ideal).
> - $P_r$ moderada y $T_r$ baja (cerca del punto de ebullición): $Z < 1$ (dominan atracciones).
> - $P_r$ muy alta: $Z > 1$ (domina el covolumen).

---

## Ecuaciones de estado mejoradas

> [!info]
> Van der Waals captura la física correcta pero tiene error de hasta 30% en densidades cerca del punto crítico. Las EOS modernas refinan los términos atractivo y repulsivo:
>
> **Redlich-Kwong (RK, 1949):**
> $$
> P = \frac{R_u T}{\bar{v}-b} - \frac{a}{T^{1/2}\,\bar{v}(\bar{v}+b)}.
> $$
> Mucho mejor en fase gaseosa; el término $T^{-1/2}$ corrige la temperatura del atractivo.
>
> **Soave-Redlich-Kwong (SRK, 1972):** Introduce la función $\alpha(T_r, \omega)$ que depende también del **factor acéntrico** $\omega$ de cada sustancia, mejorando el ajuste en la zona de condensación y en líquidos.
>
> **Peng-Robinson (PR, 1976):**
> $$
> P = \frac{R_u T}{\bar{v}-b} - \frac{a\,\alpha(T_r,\omega)}{\bar{v}(\bar{v}+b)+b(\bar{v}-b)},
> $$
> estándar en simuladores de procesos (Aspen, HYSYS). Mejor predicción de densidades líquidas y presiones de vapor que SRK.
>
> Todas comparten la estructura **covolumen repulsivo + término atractivo** y se reducen al gas ideal cuando $P \to 0$.

---

## Ejemplo: nitrógeno comprimido con van der Waals

> [!ejemplo]
> Se comprimen $n = 1\,\mathrm{kmol}$ de $\mathrm{N_2}$ desde $T = 300\,\mathrm{K}$, $P_1 = 1\,\mathrm{MPa}$ hasta $P_2 = 20\,\mathrm{MPa}$. Calcular el volumen molar real $\bar{v}_2$ usando la ecuación de van der Waals y comparar con el gas ideal.
>
> **Propiedades críticas de $\mathrm{N_2}$:** $T_c = 126.2\,\mathrm{K}$, $P_c = 3.39\,\mathrm{MPa}$, $M = 28.014\,\mathrm{kg/kmol}$.

> [!solucion]
> **Paso 1 — Constantes de van der Waals.**
> $$
> a = \frac{27\times(8.314)^2\times(126.2)^2}{64\times3390} = \frac{27\times69.12\times15926.4}{217\,\!000} = \frac{2.974\times10^7}{2.17\times10^5} = 137.1\,\mathrm{kPa\cdot m^6/kmol^2}.
> $$
> $$
> b = \frac{8.314\times126.2}{8\times3390} = \frac{1049.2}{27120} = 0.03868\,\mathrm{m^3/kmol}.
> $$
>
> **Paso 2 — Gas ideal para comparación.**
> $$
> \bar{v}_{\rm ideal} = \frac{R_u T}{P_2} = \frac{8.314\times300}{20000} = \frac{2494.2}{20000} = 0.1247\,\mathrm{m^3/kmol}.
> $$
>
> **Paso 3 — Ecuación cúbica de van der Waals a $T=300\,\mathrm{K}$, $P_2=20\,\mathrm{MPa}=20000\,\mathrm{kPa}$.**
> $$
> \left(20000 + \frac{137.1}{\bar{v}^2}\right)(\bar{v} - 0.03868) = 8.314\times300 = 2494.2.
> $$
> Expandiendo: $\bar{v}^3 - (b + R_u T/P)\bar{v}^2 + (a/P)\bar{v} - ab/P = 0$:
> $$
> \bar{v}^3 - (0.03868 + 0.12471)\bar{v}^2 + (137.1/20000)\bar{v} - (137.1\times0.03868/20000) = 0.
> $$
> $$
> \bar{v}^3 - 0.16339\,\bar{v}^2 + 0.006855\,\bar{v} - 0.0002651 = 0.
> $$
>
> **Paso 4 — Solución numérica.** Probando $\bar{v} = 0.11\,\mathrm{m^3/kmol}$: $0.001331 - 0.16339\times0.0121 + 0.006855\times0.11 - 0.0002651 = 0.001331 - 0.001977 + 0.000754 - 0.000265 = -0.000157 \approx 0$. Probando $\bar{v} = 0.108$: $\approx 0.001259 - 0.001906 + 0.000740 - 0.000265 = -0.000172$. Probando $\bar{v}=0.112$: $0.001405 - 0.002049 + 0.000768 - 0.000265 = -0.000141$. Por interpolación: $\bar{v} \approx 0.110\,\mathrm{m^3/kmol}$.
>
> **Paso 5 — Comparación y factor Z.**
> $$
> Z = \frac{P_2\bar{v}}{R_uT} = \frac{20000\times0.110}{8.314\times300} = \frac{2200}{2494.2} = 0.882.
> $$
> El gas real ocupa un **11.8% menos** que el ideal. Las atracciones dominan a esta temperatura ($T_r = 300/126.2 = 2.38$, relativamente moderada) y presión ($P_r = 20/3.39 = 5.9$, alta). $\blacksquare$

> [!info]
> **Convención de notación:** $Z = Pv/RT$; $P_r = P/P_c$, $T_r = T/T_c$ propiedades reducidas; barra: magnitudes molares [kmol]; $\omega$: factor acéntrico de Pitzer.

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, §12.1–12.4; Çengel & Boles, *Termodinámica*, §3.7; Callen, *Thermodynamics*, §9.4 (van der Waals desde postulados); Smith, Van Ness & Abbott, *Introduction to Chemical Engineering Thermodynamics*, cap. 3 (SRK, PR).
