---
title: Maxima Transferencia de Potencia en CA
tags:
  - circuitos-electricos
  - teoria
  - potencia
draft: false
aliases:
  - máxima transferencia de potencia en CA
  - adaptación de impedancias
  - carga conjugada
  - maximum power transfer AC
  - conjugate impedance matching
---

# Máxima Transferencia de Potencia en CA $\;Z_L=Z_{Th}^{*}$

> [!definicion]
> En corriente alterna, una fuente —o su equivalente [[Teorema de Thevenin| Thévenin]] de tensión $\overline{V}_{Th}$ e impedancia $Z_{Th}=R_{Th}+jX_{Th}$— entrega la **máxima potencia activa** a una carga $Z_L$ cuando esta es el **conjugado** de la impedancia de Thévenin:
> $$Z_L=Z_{Th}^{*}\quad\Longleftrightarrow\quad R_L=R_{Th},\ \ X_L=-X_{Th}.$$
> Es decir, las **reactancias se cancelan** (condición de resonancia) y las **resistencias se igualan**. En esa adaptación la potencia transferida vale
> $$P_{max}=\frac{V_{Th}^2}{4R_{Th}},$$
> con $V_{Th}$ expresada en valor **eficaz**.

> [!info]
> Es la generalización a CA de la [[Maxima Transferencia de Potencia| máxima transferencia en CC]], dentro de [[Potencia en AC/index| Potencia en AC]] ([[5 Circuitos AC Sinusoidal y Fasores/index| capítulo 5]]). Se apoya en el equivalente [[Teorema de Thevenin| Thévenin]] y en el manejo de [[Impedancia Compleja| impedancias complejas]]. Fraile Mora, cap. 2, §2.14.

---

## Ejemplo

> [!ejemplo]
> **Carga óptima de un equivalente Thévenin.**
>
> El circuito visto por la carga tiene equivalente Thévenin $\overline{V}_{Th}=10\ \text{V}$ (eficaz) y $Z_{Th}=4+j3\ \Omega$. Hallar la carga $Z_L$ que recibe la máxima potencia y el valor de esa potencia.
>
> **Paso 1 — Carga conjugada.** La óptima es el conjugado de la impedancia de Thévenin:
> $$Z_L=Z_{Th}^{*}=4-j3\ \Omega,$$
> esto es, una resistencia de $4\ \Omega$ en serie con un **condensador** cuya reactancia $-3\ \Omega$ cancela la reactancia inductiva $+3\ \Omega$ de la fuente.
>
> **Paso 2 — Corriente en adaptación.** Al conectar $Z_L=Z_{Th}^{*}$, la reactancia total del lazo es nula y solo quedan en serie las resistencias $R_{Th}+R_L=4+4=8\ \Omega$:
> $$I=\frac{V_{Th}}{R_{Th}+R_L}=\frac{10}{8}=1{,}25\ \text{A}.$$
>
> **Paso 3 — Potencia máxima.** La potencia activa absorbida por $R_L$ es
> $$P_{max}=I^2 R_L=(1{,}25)^2\cdot 4=6{,}25\ \text{W},$$
> que coincide con la fórmula directa $P_{max}=\dfrac{V_{Th}^2}{4R_{Th}}=\dfrac{100}{16}=6{,}25\ \text{W}$.
>
> > [!solucion]
> > $Z_L=4-j3\ \Omega$ (resistencia $4\ \Omega$ y condensador de reactancia $-3\ \Omega$); $P_{max}=6{,}25\ \text{W}$.

---

## En qué consiste

> [!teorema] Condición de adaptación conjugada
> Con $Z_L=R_L+jX_L$ y $Z_{Th}=R_{Th}+jX_{Th}$, la corriente del lazo y la potencia en la carga son
> $$I=\frac{V_{Th}}{(R_{Th}+R_L)+j(X_{Th}+X_L)},\qquad
> P_L=I^2R_L=\frac{V_{Th}^2\,R_L}{(R_{Th}+R_L)^2+(X_{Th}+X_L)^2}.$$
> La maximización se hace en **dos etapas**:
> 1. **Reactancia.** $X_L$ solo aparece en el denominador; elegir $X_L=-X_{Th}$ anula la parte imaginaria $(X_{Th}+X_L)=0$ y hace **máxima** la corriente (denominador mínimo).
> 2. **Resistencia.** Cancelada la reactancia, queda el caso puramente resistivo de CC: derivando $P_L=\dfrac{V_{Th}^2R_L}{(R_{Th}+R_L)^2}$ respecto de $R_L$ e igualando a cero se obtiene $R_L=R_{Th}$.
>
> Ambas condiciones equivalen a $Z_L=Z_{Th}^{*}$, y sustituyendo resulta $P_{max}=\dfrac{V_{Th}^2}{4R_{Th}}$.

> [!teoria] Por qué el conjugado y no la igualdad
> La intuición de CC ("carga igual a la interna") se rompe en CA porque la reactancia **no disipa** potencia: solo limita la corriente. Igualar $Z_L=Z_{Th}$ dejaría una reactancia total $X_{Th}+X_L=2X_{Th}\neq0$ que **estrangula** la corriente sin aportar potencia activa. El conjugado $Z_L=Z_{Th}^{*}$ hace que las reactancias opuestas (una inductiva, otra capacitiva) **resuenen** y se cancelen, dejando un circuito resistivo puro donde toda la corriente es útil. Por eso la adaptación de impedancias en CA es siempre **conjugada**.

> [!algoritmo] Cómo aplicarla
> 1. **Equivalente Thévenin.** Apagar las fuentes independientes y hallar $\overline{V}_{Th}$ y $Z_{Th}=R_{Th}+jX_{Th}$ vistos desde los terminales de la carga.
> 2. **Carga óptima.** Tomar $Z_L=Z_{Th}^{*}$, es decir $R_L=R_{Th}$ y $X_L=-X_{Th}$ (reactancia de signo opuesto).
> 3. **Potencia máxima.** Calcular $P_{max}=\dfrac{V_{Th}^2}{4R_{Th}}$ con $V_{Th}$ eficaz.

> [!warning]
> - Si la carga **solo puede ser resistiva** ($X_L=0$ forzado, no hay reactancia disponible), la óptima **no** es $R_L=R_{Th}$ sino $R_L=\lvert Z_{Th}\rvert=\sqrt{R_{Th}^2+X_{Th}^2}$; se maximiza $P_L$ sin poder anular la reactancia de Thévenin.
> - Como en CC, **máxima transferencia $\neq$ máxima eficiencia**: en adaptación se disipa tanta potencia en $R_{Th}$ como en $R_L$, de modo que el **rendimiento es del 50 %**. Se busca en electrónica/señal, no en transporte de energía.
> - Usar siempre **valores eficaces** en $\overline{V}_{Th}$ y $V_{Th}$; con amplitudes de pico aparecería un factor adicional.

## Resumen

> [!resumen]
> | Situación | Carga óptima | Potencia máxima |
> |:---|:---|:---|
> | Caso general ($Z_L$ libre) | $Z_L=Z_{Th}^{*}$, o sea $R_L=R_{Th},\ X_L=-X_{Th}$ | $P_{max}=\dfrac{V_{Th}^2}{4R_{Th}}$ |
> | Carga solo resistiva ($X_L=0$) | $R_L=\lvert Z_{Th}\rvert=\sqrt{R_{Th}^2+X_{Th}^2}$ | $P_{max}=\dfrac{V_{Th}^2}{2\,(R_{Th}+\lvert Z_{Th}\rvert)}$ |
> | Rendimiento en adaptación | $\eta=50\ \%$ | $P_{R_{Th}}=P_{R_L}$ |

> [!corolario]
> La adaptación de impedancias en CA es **conjugada**: la reactancia de la carga cancela la de la fuente (resonancia) y su resistencia iguala a la interna. Esto reduce el problema al de CC sobre la parte resistiva, con el mismo techo $P_{max}=V_{Th}^2/4R_{Th}$ y el mismo rendimiento del 50 %.

> [!referencia]
> Fraile Mora, cap. 2, §2.14. Versión en CC: [[Maxima Transferencia de Potencia]]. Herramientas: [[Teorema de Thevenin]], [[Impedancia Compleja]]. Marco: [[Potencia en AC/index]].
