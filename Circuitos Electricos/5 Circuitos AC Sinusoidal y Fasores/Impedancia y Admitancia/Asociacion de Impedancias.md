---
title: Asociación de Impedancias
tags:
  - circuitos-electricos
  - teoria
  - impedancia
draft: false
aliases:
  - asociación de impedancias
  - impedancias en serie y paralelo
  - impedance association
  - series and parallel impedances
---

# Asociación de Impedancias $\;Z_{eq}$

> [!definicion]
> En régimen sinusoidal las impedancias se asocian **igual que las resistencias**, pero con álgebra
> compleja. En **serie** (misma corriente) se **suman** directamente,
> $$Z_{eq}=\sum_k Z_k\quad[\Omega];$$
> en **paralelo** (misma tensión) se suman sus **admitancias**,
> $$\frac{1}{Z_{eq}}=\sum_k\frac{1}{Z_k}\qquad\Longleftrightarrow\qquad Y_{eq}=\sum_k Y_k\quad[\text{S}].$$
> Para **dos** ramas en paralelo es cómodo el producto sobre la suma,
> $$Z_{eq}=\frac{Z_1 Z_2}{Z_1+Z_2}.$$

> [!info]
> Extiende a la corriente alterna la [[Resistencias en Serie y Paralelo| asociación resistiva]],
> dentro de [[Impedancia y Admitancia/index| Impedancia y admitancia]]
> ([[5 Circuitos AC Sinusoidal y Fasores/index| capítulo 5]]). Opera sobre la
> [[Impedancia Compleja]] y su inversa, la [[Admitancia]]. Fraile Mora, cap. 2, §2.8.2.

---

## Ejemplo

> [!ejemplo]
> Una rama serie $Z_1=3+j4\ \Omega$ (carácter RL, $R=3\ \Omega$, $X_L=4\ \Omega$) se conecta en
> **paralelo** con un condensador $Z_2=-j10\ \Omega$ (reactancia capacitiva $X_C=-10\ \Omega$).
> Hallar la impedancia equivalente $Z_{eq}$.

> [!solucion]
> Al ser **dos** ramas en paralelo se aplica el producto sobre la suma,
> $Z_{eq}=\dfrac{Z_1 Z_2}{Z_1+Z_2}$.
>
> **Paso 1 — producto** (numerador):
> $$Z_1 Z_2=(3+j4)(-j10)=-j30-j^2 40=40-j30.$$
>
> **Paso 2 — suma** (denominador), en forma rectangular:
> $$Z_1+Z_2=3+j4-j10=3-j6.$$
>
> **Paso 3 — cociente**, racionalizando con el conjugado $\dfrac{3+j6}{3+j6}$:
> $$
> Z_{eq}=\frac{40-j30}{3-j6}\cdot\frac{3+j6}{3+j6}
> =\frac{(40-j30)(3+j6)}{3^2+6^2}.
> $$
> Numerador: $(40-j30)(3+j6)=120+j240-j90-j^2180=300+j150$. Denominador: $9+36=45$. Luego
> $$
> Z_{eq}=\frac{300+j150}{45}\approx 6{,}67+j3{,}33\ \Omega
> =7{,}45\,\angle\,26{,}6^\circ\ \Omega.
> $$
> El resultado tiene reactancia **positiva**: el conjunto es **inductivo** pese a contener un
> condensador, porque la rama RL domina sobre $Z_2$.

---

## En qué consiste

> [!teoria]
> Las reglas heredan la topología de las resistencias; el fasor sustituye al número real.
>
> **Serie — se suman las impedancias.** Por una asociación serie circula **la misma corriente**
> fasorial $\overline{I}$. La tensión total es la suma de las tensiones de cada elemento (LKT en
> fasores):
> $$\overline{V}=\sum_k \overline{V}_k=\sum_k Z_k\,\overline{I}
> \;\Longrightarrow\; Z_{eq}=\frac{\overline{V}}{\overline{I}}=\sum_k Z_k.$$
>
> **Paralelo — se suman las admitancias.** En paralelo todos los elementos comparten **la misma
> tensión** $\overline{V}$. La corriente total es la suma de las corrientes de rama (LKC en fasores):
> $$\overline{I}=\sum_k \overline{I}_k=\sum_k Y_k\,\overline{V}
> \;\Longrightarrow\; Y_{eq}=\frac{\overline{I}}{\overline{V}}=\sum_k Y_k.$$
>
> Es la **misma deducción** que para las resistencias, sin más cambio que trabajar con fasores y
> números complejos. Por la misma razón siguen valiendo los **divisores** con impedancias:
> $$\overline{V}_k=\overline{V}\,\frac{Z_k}{\sum_i Z_i}\quad(\text{tensión, serie}),\qquad
> \overline{I}_k=\overline{I}\,\frac{Y_k}{\sum_i Y_i}=\overline{I}\,\frac{Z_{eq}}{Z_k}\quad(\text{corriente, paralelo}).$$

> [!algoritmo]
> Reducción de una red de impedancias a $Z_{eq}$:
> 1. **Identificar** asociaciones serie y paralelo elementales en la red.
> 2. **Serie:** sumar las impedancias, $Z_{eq}=\sum_k Z_k$.
> 3. **Paralelo:** sumar las admitancias, $Y_{eq}=\sum_k Y_k$; para dos ramas, $Z_{eq}=\dfrac{Z_1 Z_2}{Z_1+Z_2}$.
> 4. **Sustituir** cada grupo por su equivalente y repetir desde (1) hasta quedar una sola impedancia.
> 5. Trabajar en la forma compleja **cómoda**: **rectangular** para sumar/restar, **polar** para
>    multiplicar/dividir.

> [!warning]
> - Las **sumas y restas** se hacen en forma **rectangular** ($a+jb$); los **productos y cocientes**,
>   en forma **polar** ($\rho\,\angle\,\theta$). No mezclar formas en una misma operación.
> - Una reactancia **inductiva** ($+jX$) y una **capacitiva** ($-jX$) pueden **cancelarse** al
>   sumarse en serie; si lo hacen por completo, la reactancia neta es nula (**resonancia**) y queda
>   sólo la parte resistiva.
> - El producto sobre la suma $\dfrac{Z_1 Z_2}{Z_1+Z_2}$ vale **sólo para dos** ramas en paralelo;
>   con tres o más, sumar admitancias.

---

## Resumen

> [!resumen]
> | Asociación | Magnitud que se conserva | Regla |
> |:---|:---|:---|
> | Serie | corriente $\overline{I}$ | $Z_{eq}=\sum_k Z_k$ |
> | Paralelo (general) | tensión $\overline{V}$ | $Y_{eq}=\sum_k Y_k$, es decir $\dfrac{1}{Z_{eq}}=\sum_k\dfrac{1}{Z_k}$ |
> | Paralelo (dos ramas) | tensión $\overline{V}$ | $Z_{eq}=\dfrac{Z_1 Z_2}{Z_1+Z_2}$ |
> | Divisor de tensión (serie) | — | $\overline{V}_k=\overline{V}\,\dfrac{Z_k}{\sum_i Z_i}$ |
> | Divisor de corriente (paralelo) | — | $\overline{I}_k=\overline{I}\,\dfrac{Z_{eq}}{Z_k}$ |

> [!corolario]
> La asociación resistiva es el caso particular con $X=0$ en todas las ramas: con impedancias reales,
> $Z_{eq}=\sum R_k$ (serie) y $1/Z_{eq}=\sum 1/R_k$ (paralelo) reproducen exactamente la
> [[Resistencias en Serie y Paralelo| asociación de resistencias]]. La generalización compleja no
> introduce reglas nuevas: sólo cambia el cuerpo de los números, de $\mathbb{R}$ a $\mathbb{C}$.

> [!referencia]
> Fraile Mora, *Circuitos Eléctricos*, cap. 2, §2.8.2. Véase la [[Impedancia Compleja]], la
> [[Admitancia]] y la [[Resistencias en Serie y Paralelo]] dentro de
> [[Impedancia y Admitancia/index| Impedancia y admitancia]].
