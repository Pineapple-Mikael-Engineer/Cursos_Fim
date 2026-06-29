---
title: Mezclas de Gases Ideales
order: 1
tags:
  - termodinamica
  - mezclas
  - gas-ideal
  - dalton
  - amagat
draft: false
aliases:
  - Mezclas de Gases
  - Mezclas de Gases Ideales
  - ideal gas mixtures
  - mezcla no reactiva
---

# Mezclas de Gases Ideales

> [!definicion]
> Una **mezcla de gases ideales** es un sistema de $N$ componentes gaseosos no reactivos, cada uno modelado como gas ideal. La mezcla en conjunto también se comporta como gas ideal con masa molecular aparente $M = \sum_i y_i M_i$. El estado queda fijado por $(T, P, y_1, \ldots, y_N)$.
>
> *Idea física clave:* en una mezcla de gases ideales, las moléculas de distintos componentes no interactúan entre sí (la hipótesis de gas ideal supone ausencia de fuerzas intermoleculares). Por tanto, cada componente actúa como si los demás no existieran: ocupa el volumen total, tiene la misma temperatura que la mezcla, y ejerce su propia **presión parcial** $P_i = y_i P$ (ley de Dalton). La energía interna y la entalpía dependen solo de $T$; la entropía depende además de las presiones parciales.

![[mezcla_gases_dalton_esquema.svg|440]]
*Modelo de Dalton para una mezcla de tres gases. Cada componente ocupa el volumen total $V$ a $T$ constante y ejerce su presión parcial $P_i$. La presión total es la suma: $P = P_1 + P_2 + P_3$.*

---

## Composición

> [!proposicion]
> Sean $n_i$ los kmoles y $m_i$ la masa del componente $i$; $n = \sum_i n_i$, $m = \sum_i m_i$.
>
> **Fracción molar:** $y_i = n_i/n$, $\sum_i y_i = 1$.
>
> **Fracción másica:** $fm_i = m_i/m$, $\sum_i fm_i = 1$.
>
> **Masa molecular aparente:** $M = m/n = \sum_i y_i M_i$.
>
> **Conversión $fm_i \to y_i$:**
> $$y_i = \frac{fm_i/M_i}{\displaystyle\sum_k fm_k/M_k}, \qquad fm_i = \frac{y_i M_i}{M}.$$

> [!demostracion]
> **Hipótesis:** mezcla de $N$ gases a temperatura y presión uniformes.
>
> **Paso 1 — Base másica.** Tomar $1\,\mathrm{kg}$ de mezcla. El componente $i$ aporta $fm_i\,\mathrm{kg}$, equivalente a $n_i' = fm_i/M_i$ kmol.
>
> **Paso 2 — Total de moles.** El número total de kmol en la base de $1\,\mathrm{kg}$ es:
> $$n' = \sum_k \frac{fm_k}{M_k}.$$
>
> **Paso 3 — Fracción molar.** Por definición:
> $$y_i = \frac{n_i'}{n'} = \frac{fm_i/M_i}{\displaystyle\sum_k fm_k/M_k}. \qquad \blacksquare$$
>
> *Verificación:* $\sum_i y_i = \sum_i (fm_i/M_i) / \sum_k (fm_k/M_k) = n'/n' = 1$ ✓.
>
> **Paso 4 — Masa molecular.** $M = 1\,\mathrm{kg}/n' = 1/\sum_k(fm_k/M_k)$. También: $M = m/n = \sum_i n_i M_i/\sum_i n_i = \sum_i y_i M_i$.
>
> **Paso 5 — Conversión inversa.** $fm_i = m_i/m = n_i M_i/(nM) = y_i M_i/M$. $\blacksquare$

---

## Ley de Dalton (presiones parciales)

> [!teorema]
> En la mezcla a $(T, V)$: cada componente ocupa el volumen total $V$ a la misma $T$ y ejerce la **presión parcial** $P_i = n_i R_u T/V$. La presión total:
> $$P = \sum_i P_i, \qquad P_i = y_i\,P.$$

> [!demostracion]
> **Hipótesis:** mezcla de gases ideales a temperatura y volumen dados.
>
> **Paso 1 — Gas ideal para el componente $i$:** $P_i V = n_i R_u T$ → $P_i = n_i R_u T/V$.
>
> **Paso 2 — Gas ideal para la mezcla:** $P V = n R_u T$ → $P = n R_u T/V$.
>
> **Paso 3 — Fracción de presiones:** dividiendo ambas expresiones:
> $$\frac{P_i}{P} = \frac{n_i}{n} = y_i \implies P_i = y_i\,P.$$
>
> **Paso 4 — Presión total:** $\sum_i P_i = P\sum_i y_i = P\times1 = P$. ✓
>
> **Paso 5 — Interpretación:** $P_i < P$ siempre que $y_i < 1$. La presión parcial es la presión que ejercería el componente $i$ si estuviera solo ocupando el volumen total. El $\mathrm{N_2}$ en el aire (a $P=101.3\,\mathrm{kPa}$, $y_{\mathrm{N_2}}=0.78$) ejerce $P_{\mathrm{N_2}}=0.78\times101.3=79\,\mathrm{kPa}$. $\blacksquare$

---

## Ley de Amagat (volúmenes parciales)

> [!teorema]
> A $(T, P)$ fijos, el volumen parcial es el volumen que ocuparía el componente $i$ solo a $T$ y $P$:
> $$V_i = n_i R_u T/P = y_i V, \qquad \sum_i V_i = V.$$
>
> **Consecuencia importante:** la fracción volumétrica coincide con la fracción molar ($V_i/V = y_i$). Por eso el **análisis volumétrico** (medición de fracciones de volumen en un gas) entrega directamente las fracciones molares.

---

## Propiedades de la mezcla

> [!proposicion]
> **Energía interna y entalpía** (dependen solo de $T$ para gas ideal):
> $$\bar{u} = \sum_i y_i\,\bar{u}_i(T), \qquad \bar{h} = \sum_i y_i\,\bar{h}_i(T).$$
>
> **Calores específicos:**
> $$\bar{c}_v = \sum_i y_i\,\bar{c}_{v,i}, \qquad \bar{c}_p = \sum_i y_i\,\bar{c}_{p,i}, \qquad \gamma = \bar{c}_p/\bar{c}_v.$$
>
> **Entropía.** El componente $i$ en la mezcla se encuentra a $T$ y $P_i < P$: su entropía es mayor que si estuviera a $P$ total. Por eso la entropía de la mezcla debe evaluarse a presiones parciales:
> $$\bar{s} = \sum_i y_i\,\bar{s}_i(T, P_i) = \sum_i y_i\left[\bar{s}_i^\circ(T) - R_u\ln\frac{P_i}{P^\circ}\right].$$

---

## Entropía de mezcla de gases distintos

> [!proposicion]
> Al mezclar adiabáticamente $N$ gases ideales distintos, cada uno inicialmente a $(T, P)$, la entropía total aumenta:
> $$\Delta \bar{s}_{\rm mezcla} = -R_u\sum_i y_i\ln y_i \geq 0.$$
> (El signo $\geq 0$ se debe a que $\ln y_i \leq 0$ para $y_i \in (0,1)$.)

> [!demostracion]
> **Hipótesis:** $N$ gases ideales distintos, cada uno a $(T, P)$, se mezclan adiabáticamente. El sistema es cerrado.
>
> **Paso 1 — Entropía inicial.** Cada gas $i$ está a $(T, P)$ en su propio compartimento de volumen $V_i = y_i V$:
> $$S_{\rm ini} = \sum_i n_i\,\bar{s}_i(T, P).$$
>
> **Paso 2 — Entropía final.** Tras la mezcla, cada componente ocupa el volumen total $V$ a $T$ y $P$. Pero su presión parcial es $P_i = y_i P < P$:
> $$S_{\rm fin} = \sum_i n_i\,\bar{s}_i(T, P_i) = \sum_i n_i\left[\bar{s}_i(T,P) - R_u\ln\frac{P_i}{P}\right].$$
>
> **Paso 3 — Variación:** restando y usando $P_i/P = y_i$:
> $$\Delta S = S_{\rm fin} - S_{\rm ini} = -R_u\sum_i n_i\ln y_i.$$
>
> **Paso 4 — Base molar:** dividiendo por $n$:
> $$\Delta\bar{s} = -R_u\sum_i y_i\ln y_i.$$
>
> **Paso 5 — Signo:** como $y_i \in (0,1)$, $\ln y_i < 0$ para todo $i$ con $y_i \neq 0, 1$. Luego $-\ln y_i > 0$ y $\Delta\bar{s} > 0$. El proceso de mezcla es **irreversible**: no se puede separar espontáneamente la mezcla. $\blacksquare$
>
> *Nota (paradoja de Gibbs):* si todos los gases son idénticos, no existe diferencia entre "antes" y "después" de la mezcla. La fórmula no aplica en ese caso y $\Delta\bar{s}=0$ (mezcla reversible). La ecuación $-R_u\sum y_i\ln y_i$ solo es válida para **gases distinguibles**.

---

## Cambios de propiedad entre estados

> [!proposicion]
> Entre estados $(T_1, P_1)$ y $(T_2, P_2)$ a composición constante, por kmol de mezcla:
> $$\Delta\bar{h} = \bar{c}_p(T_2-T_1), \qquad \Delta\bar{s} = \bar{c}_p\ln\frac{T_2}{T_1} - R_u\ln\frac{P_2}{P_1}.$$
> Los términos $\ln y_i$ en la entropía se cancelan entre estado inicial y final cuando la composición es constante.

---

## Ejemplo: gas de síntesis — análisis completo

> [!ejemplo]
> Una corriente de **gas de síntesis** tiene la siguiente composición volumétrica: $30\%\,\mathrm{CO}$, $25\%\,\mathrm{H_2}$, $15\%\,\mathrm{CO_2}$, $30\%\,\mathrm{N_2}$. El gas se comprime desde $T_1=300\,\mathrm{K}$, $P_1=200\,\mathrm{kPa}$ hasta $T_2=500\,\mathrm{K}$, $P_2=800\,\mathrm{kPa}$.
>
> Determinar: (a) $M$ y fracciones másicas; (b) $\Delta\bar{h}$ y $\Delta h$; (c) $\Delta\bar{s}$; (d) potencia mínima isentrópica para $\dot{m}=5\,\mathrm{kg/s}$.

> [!solucion]
> **(a) Composición.** Fracciones volumétricas = molares: $y_{\mathrm{CO}}=0.30$, $y_{\mathrm{H_2}}=0.25$, $y_{\mathrm{CO_2}}=0.15$, $y_{\mathrm{N_2}}=0.30$.
>
> Masas molares ($\mathrm{kg/kmol}$): $M_{\mathrm{CO}}=28.01$, $M_{\mathrm{H_2}}=2.016$, $M_{\mathrm{CO_2}}=44.01$, $M_{\mathrm{N_2}}=28.014$.
>
> $$M = 0.30\times28.01 + 0.25\times2.016 + 0.15\times44.01 + 0.30\times28.014 = 8.403+0.504+6.602+8.404 = 23.91\,\mathrm{kg/kmol}.$$
>
> Fracciones másicas: $fm_i = y_i M_i/M$:
> $fm_{\mathrm{CO}} = 8.403/23.91 = 0.3514$; $fm_{\mathrm{H_2}} = 0.504/23.91 = 0.0211$; $fm_{\mathrm{CO_2}} = 6.602/23.91 = 0.2761$; $fm_{\mathrm{N_2}} = 8.404/23.91 = 0.3515$. Suma $= 1.000$. ✓
>
> **(b) $\Delta\bar{h}$ y $\Delta h$.** $\bar{c}_p$ promedio en kJ/(kmol·K): $\bar{c}_{p,\mathrm{CO}}=29.1$, $\bar{c}_{p,\mathrm{H_2}}=29.0$, $\bar{c}_{p,\mathrm{CO_2}}=43.1$, $\bar{c}_{p,\mathrm{N_2}}=29.1$.
>
> $$\bar{c}_p = 0.30\times29.1 + 0.25\times29.0 + 0.15\times43.1 + 0.30\times29.1 = 8.73+7.25+6.47+8.73 = 31.18\,\mathrm{kJ/(kmol\cdot K)}.$$
>
> $$\Delta\bar{h} = 31.18\times(500-300) = 6236\,\mathrm{kJ/kmol}.$$
>
> $$\Delta h = 6236/23.91 = 260.8\,\mathrm{kJ/kg}.$$
>
> **(c) $\Delta\bar{s}$.**
> $$\Delta\bar{s} = \bar{c}_p\ln\frac{T_2}{T_1} - R_u\ln\frac{P_2}{P_1} = 31.18\times\ln\frac{500}{300} - 8.314\times\ln\frac{800}{200}.$$
> $$= 31.18\times0.5108 - 8.314\times1.3863 = 15.93 - 11.52 = +4.41\,\mathrm{kJ/(kmol\cdot K)}.$$
>
> $\Delta\bar{s} > 0$: el proceso real no es isentrópico; el estado $(T_2, P_2)$ dado no corresponde a una compresión isentrópica desde el estado 1.
>
> **(d) Potencia isentrópica.** Temperatura de salida isentrópica ($s_2 = s_1$, $\Delta\bar{s} = 0$):
>
> $R_u/\bar{c}_p = 8.314/31.18 = 0.2667$. Para proceso isentrópico:
> $$T_{2s} = T_1\left(\frac{P_2}{P_1}\right)^{R_u/\bar{c}_p} = 300\times4^{0.2667} = 300\times e^{0.2667\ln4} = 300\times1.447 = 434.2\,\mathrm{K}.$$
>
> Trabajo específico isentrópico:
> $$w_s = \frac{\bar{c}_p}{M}(T_{2s}-T_1) = \frac{31.18}{23.91}\times134.2 = 1.304\times134.2 = 175.0\,\mathrm{kJ/kg}.$$
>
> Potencia mínima:
> $$\dot{W}_{\rm min} = \dot{m}\,w_s = 5\times175.0 = 875\,\mathrm{kW}.$$
>
> $\boxed{M = 23.91\,\mathrm{kg/kmol},\quad \dot{W}_{\rm min} = 875\,\mathrm{kW}.}$ $\blacksquare$

> [!referencia]
> Borgnakke & Sonntag, cap. 12; Çengel & Boles, cap. 13; Moran & Shapiro, cap. 12.
