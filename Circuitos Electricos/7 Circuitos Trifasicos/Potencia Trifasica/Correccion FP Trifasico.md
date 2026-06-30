---
title: Corrección del FP Trifásico
tags:
  - circuitos-electricos
  - teoria
  - trifasico
draft: false
aliases:
  - corrección factor de potencia trifásico
  - corrección del FP trifásico
  - three-phase power factor correction
---

# Corrección del FP Trifásico

> [!definicion]
> Igual que en el caso monofásico, un **factor de potencia bajo** en una carga trifásica (típicamente inductiva) obliga a circular **más corriente de línea** $I_L$ para entregar la misma potencia activa $P$. Se **corrige** conectando un **banco de condensadores** —normalmente en **triángulo**— que aporta potencia reactiva capacitiva, reduciendo así la reactiva $Q$ que el sistema toma de la red. La reactiva capacitiva necesaria para pasar de $\cos\varphi_1$ a $\cos\varphi_2$ es
> $$Q_C = P\,(\tan\varphi_1 - \tan\varphi_2).$$

> [!info]
> Esta nota extiende la [[Correccion del Factor de Potencia| corrección monofásica]] (capítulo 5) al sistema trifásico, dentro de la [[Potencia Trifasica/index| potencia trifásica]] del [[7 Circuitos Trifasicos/index| capítulo 7]]. Apóyate en [[Potencia en Sistemas Balanceados]] para el triángulo de potencias y en [[Factor de Potencia]] para el significado de $\cos\varphi$. Referencia: Fraile Mora, cap. 3 §3.9.

---

## Ejemplo

> [!ejemplo] Banco de condensadores en triángulo
> Una carga trifásica equilibrada consume $P = 12{,}2\ \text{kW}$ con $\cos\varphi_1 = 0{,}766$ (es decir $\varphi_1 = 40^\circ$, $\tan\varphi_1 = 0{,}839$), alimentada a una tensión de línea $V_L = 400\ \text{V}$ y frecuencia $f = 50\ \text{Hz}$. Se desea corregir el factor de potencia a $\cos\varphi_2 = 0{,}95$ ($\varphi_2 = 18{,}2^\circ$, $\tan\varphi_2 = 0{,}329$) mediante un banco de condensadores conectados en **triángulo**. Hallar la capacidad necesaria por fase.
>
> > [!solucion]
> > **Paso 1 — Reactiva capacitiva total a compensar.**
> > $$Q_C = P\,(\tan\varphi_1 - \tan\varphi_2) = 12200\,(0{,}839 - 0{,}329) = 12200 \cdot 0{,}510 \approx 6{,}22\ \text{kVAr}.$$
> >
> > **Paso 2 — Reparto entre los tres condensadores.** En conexión $\Delta$ el banco tiene 3 condensadores, uno por rama:
> > $$Q_{C,\text{fase}} = \frac{Q_C}{3} = \frac{6220}{3} \approx 2073\ \text{VAr}.$$
> >
> > **Paso 3 — Capacidad por fase.** En $\Delta$ cada condensador queda sometido a la **tensión de línea** $V_L = 400\ \text{V}$. Con $\omega = 2\pi f = 314\ \text{rad/s}$:
> > $$C = \frac{Q_{C,\text{fase}}}{\omega\,V_L^2} = \frac{2073}{314 \cdot 400^2} = \frac{2073}{314 \cdot 160000} \approx 41\ \mu\text{F}.$$
> >
> > **Resultado:** $Q_C \approx 6{,}22\ \text{kVAr}$ totales; $C \approx 41\ \mu\text{F}$ por fase, en triángulo.

---

## En qué consiste

> [!teoria] Por qué baja la corriente sin tocar la potencia útil
> El condensador aporta reactiva capacitiva ($Q_C < 0$) que **cancela** parte de la reactiva inductiva de la carga. La potencia activa $P$ —la que realiza trabajo útil— **no cambia**, pero la reactiva neta $Q$ disminuye. Como
> $$S = \sqrt{P^2 + Q^2}, \qquad I_L = \frac{S}{\sqrt{3}\,V_L},$$
> al reducir $Q$ baja la potencia aparente $S$ y, con ella, la corriente de línea $I_L$ y las pérdidas $\propto I_L^2$ en la red.
>
> **Conexión del banco.** Los condensadores en **triángulo** soportan la tensión de línea $V_L$, mayor que en estrella, pero por ello necesitan **menos capacidad** (un tercio) para entregar la misma $Q_C$. Por eso suele preferirse la conexión $\Delta$.

> [!algoritmo] Procedimiento de cálculo
> **Paso 1.** Determinar la potencia activa $P$ y el ángulo $\varphi_1$ de la carga (a partir de $\cos\varphi_1$). **Paso 2.** Fijar el factor de potencia objetivo $\cos\varphi_2$ y obtener $\tan\varphi_2$. **Paso 3.** Calcular la reactiva a compensar: $Q_C = P\,(\tan\varphi_1 - \tan\varphi_2)$. **Paso 4.** Repartir entre los 3 condensadores ($Q_{C,\text{fase}} = Q_C/3$) y hallar $C$ según la conexión:
> - en **triángulo**: $C = \dfrac{Q_{C,\text{fase}}}{\omega\,V_L^2}$ (cada condensador ve $V_L$);
> - en **estrella**: $C = \dfrac{Q_{C,\text{fase}}}{\omega\,V_F^2}$ (cada condensador ve la tensión de fase $V_F = V_L/\sqrt{3}$).

> [!proposicion] Triángulo frente a estrella: factor 1/3
> Para entregar la misma reactiva $Q_C$, los condensadores en **triángulo** requieren **un tercio** de la capacidad que en estrella. La razón: en $\Delta$ cada condensador soporta $\sqrt{3}$ veces más tensión que en $Y$, y como $Q = \omega C\,V^2$ depende del **cuadrado** de la tensión,
> $$\frac{C_\Delta}{C_Y} = \frac{V_F^2}{V_L^2} = \frac{1}{3}.$$
> Esta es la ventaja económica de la conexión $\Delta$ del banco de compensación.

---

> [!warning]
> - **No sobrecompensar.** Pasarse de la cuenta lleva a un factor de potencia **capacitivo**, lo cual suele ser indeseable (salvo que se busque expresamente). Conviene quedarse en el objetivo $\cos\varphi_2$.
> - La corrección **no reduce** la potencia activa $P$ ni la potencia útil de la carga: solo disminuye la corriente de línea y las pérdidas.
> - Cuidado con la **conexión** ($\Delta$ frente a $Y$) al despejar $C$: el factor $3$ entre ambas cambia el resultado por completo.

---

## Resumen

> [!resumen]
> | Magnitud | Expresión | Comentario |
> |---|---|---|
> | Reactiva a compensar | $Q_C = P\,(\tan\varphi_1 - \tan\varphi_2)$ | igual que en monofásico |
> | Reactiva por fase | $Q_{C,\text{fase}} = Q_C/3$ | 3 condensadores |
> | $C$ en triángulo | $C = \dfrac{Q_{C,\text{fase}}}{\omega\,V_L^2}$ | cada uno ve $V_L$ |
> | $C$ en estrella | $C = \dfrac{Q_{C,\text{fase}}}{\omega\,V_F^2}$ | cada uno ve $V_F = V_L/\sqrt{3}$ |
> | Relación $\Delta$ / $Y$ | $C_\Delta = \tfrac{1}{3}\,C_Y$ | ventaja del triángulo |
> | Efecto | $S \downarrow,\ I_L \downarrow$ con $P$ constante | $I_L = S/(\sqrt{3}\,V_L)$ |

> [!corolario]
> Corregir el factor de potencia de una carga trifásica equivale a calcular una sola $Q_C = P\,(\tan\varphi_1 - \tan\varphi_2)$ y repartirla entre tres condensadores. La conexión en **triángulo** es preferible porque, a igual $Q_C$, exige solo un tercio de la capacidad que en estrella. La potencia activa permanece intacta; lo que se reduce es la corriente de línea y, con ella, las pérdidas del sistema.

> [!referencia]
> - Fraile Mora, J. *Circuitos Eléctricos*, cap. 3 §3.9 (corrección del factor de potencia, sistemas trifásicos).
> - Relacionadas: [[Correccion del Factor de Potencia]], [[Factor de Potencia]], [[Potencia en Sistemas Balanceados]], [[Conexion Triangulo]].
