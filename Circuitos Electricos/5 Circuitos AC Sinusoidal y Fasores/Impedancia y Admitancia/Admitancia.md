---
title: Admitancia
tags:
  - circuitos-electricos
  - teoria
  - impedancia
  - admitancia
draft: false
aliases:
  - admitancia
  - conductancia
  - susceptancia
  - admittance
---

# Admitancia $\;Y=G+jB$

> [!definicion]
> La **admitancia** es la inversa de la impedancia, el cociente de los fasores de corriente y tensión,
> $$Y=\frac{1}{Z}=\frac{\overline{I}}{\overline{V}}=G+jB\quad[\text{S}],$$
> medida en **siemens** ($\text{S}$). Su parte real es la **conductancia** $G$ y la imaginaria la
> **susceptancia** $B$. Mide la **facilidad** con que circula la corriente: es a la impedancia lo que la
> conductancia a la resistencia. Su utilidad es que **simplifica los circuitos en paralelo**, donde las
> admitancias simplemente se suman.

> [!info]
> La cara **dual** de la [[Impedancia Compleja]] dentro de [[Impedancia y Admitancia/index| Impedancia y admitancia]] ([[5 Circuitos AC Sinusoidal y Fasores/index| capítulo 5]]). Es imprescindible para la
> [[Asociacion de Impedancias| asociación en paralelo]] y para el [[Analisis de Nodos| análisis de nodos]] en corriente alterna, donde trabajar con $1/Z$ sería engorroso. Fraile Mora, cap. 2, §2.7.

---

## Ejemplo

> [!ejemplo]
> **Admitancia de una rama RL serie.**
>
> Hallar la admitancia de la impedancia $Z=3+j4\ \Omega$ (la misma rama RL del ejemplo de
> [[Impedancia Compleja]]).
>
> **Paso 1 — Invertir el complejo.** Se multiplica numerador y denominador por el conjugado:
> $$Y=\frac{1}{3+j4}=\frac{3-j4}{(3+j4)(3-j4)}=\frac{3-j4}{3^2+4^2}=\frac{3-j4}{25}.$$
>
> **Paso 2 — Separar parte real e imaginaria.**
> $$Y=0{,}12-j0{,}16\ \text{S},\qquad G=0{,}12\ \text{S},\quad B=-0{,}16\ \text{S}.$$
>
> **Paso 3 — Módulo y ángulo.** Como $\lvert Z\rvert=5\ \Omega$ y $\angle Z=+53^\circ$:
> $$\lvert Y\rvert=\frac{1}{\lvert Z\rvert}=\frac{1}{5}=0{,}2\ \text{S},\qquad \angle Y=-53^\circ.$$
>
> > [!solucion]
> > $Y=0{,}12-j0{,}16=0{,}2\angle(-53^\circ)\ \text{S}$. La susceptancia es **negativa**, coherente con
> > una carga inductiva. Nótese que $G=0{,}12\neq1/R=1/3$: la conductancia **no** es el inverso de la
> > resistencia porque hay reactancia presente. El módulo y el ángulo son, respectivamente, el inverso y
> > el opuesto de los de $Z$.

---

## En qué consiste

> [!teoria] De impedancia a admitancia
> Pasar de $Z=R+jX$ a $Y=1/Z$ es **invertir un número complejo**. En forma polar es inmediato:
> $$\lvert Y\rvert=\frac{1}{\lvert Z\rvert},\qquad \angle Y=-\angle Z.$$
> En forma rectangular, racionalizando con el conjugado, las componentes quedan **acopladas**:
> $$G=\frac{R}{R^2+X^2},\qquad B=\frac{-X}{R^2+X^2}.$$
> La conductancia $G$ depende de $R$ **y** de $X$; sólo cuando $X=0$ se recupera $G=1/R$. El signo de la
> susceptancia $B$ es **opuesto** al de la reactancia $X$.

> [!teoria] Admitancias de los elementos pasivos
> Invirtiendo cada impedancia elemental:
> - **Resistencia:** $Y_R=\dfrac{1}{R}=G$ (conductancia pura, sin parte imaginaria).
> - **Inductor:** $Y_L=\dfrac{1}{j\omega L}=-\dfrac{j}{\omega L}$, susceptancia **inductiva**
>   $B_L=-\dfrac{1}{\omega L}<0$ (decrece con la frecuencia).
> - **Condensador:** $Y_C=j\omega C$, susceptancia **capacitiva** $B_C=+\omega C>0$ (crece con la
>   frecuencia).
>
> Los signos de las susceptancias son **opuestos** a los de las reactancias correspondientes: el
> inductor, que tenía $X_L>0$, aporta $B_L<0$, y viceversa para el condensador.

> [!proposicion] Las admitancias en paralelo se suman
> Para ramas conectadas en **paralelo**, todas comparten la misma tensión $\overline{V}$, y las
> corrientes se suman ($\overline{I}=\sum\overline{I}_k$); por tanto
> $$Y_{eq}=\sum_{k}Y_k=\sum_k(G_k+jB_k),$$
> exactamente igual que las conductancias en continua. Esto evita la incómoda fórmula
> $1/Z_{eq}=\sum 1/Z_k$ y es la razón por la que el [[Analisis de Nodos| método de nodos]] se formula
> de manera natural en términos de admitancias.

> [!warning]
> Dos errores frecuentes:
> - $G\neq1/R$ cuando hay reactancia. Lo correcto es $G=\dfrac{R}{R^2+X^2}$; igualmente
>   $B\neq -1/X$ en general.
> - La susceptancia **inductiva es negativa** y la **capacitiva positiva**, signos contrarios a las
>   reactancias. Confundir el signo invierte el carácter (inductivo/capacitivo) de la rama.

---

## Resumen

> [!resumen]
> | Magnitud | Símbolo | Expresión | Unidad |
> |:---|:---|:---|:---|
> | Admitancia | $Y$ | $\dfrac{1}{Z}=\dfrac{\overline{I}}{\overline{V}}=G+jB$ | $\text{S}$ |
> | Conductancia | $G$ | $\dfrac{R}{R^2+X^2}$ | $\text{S}$ |
> | Susceptancia | $B$ | $\dfrac{-X}{R^2+X^2}$ | $\text{S}$ |
> | Módulo | $\lvert Y\rvert$ | $1/\lvert Z\rvert$ | $\text{S}$ |
> | Ángulo | $\angle Y$ | $-\angle Z$ | — |
>
> | Elemento | $Y$ | $G$ | $B$ |
> |:---|:---|:---|:---|
> | Resistencia | $1/R$ | $1/R$ | $0$ |
> | Inductor | $-\dfrac{j}{\omega L}$ | $0$ | $-\dfrac{1}{\omega L}$ |
> | Condensador | $j\omega C$ | $0$ | $+\omega C$ |

> [!corolario]
> Conviene la **impedancia** para asociar elementos en **serie** (se suman las $Z$) y la **admitancia**
> para asociarlos en **paralelo** (se suman las $Y$). Elegir la magnitud según la topología ahorra
> inversiones de complejos.

> [!referencia]
> Fraile Mora, J. *Circuitos eléctricos*, cap. 2, §2.7. Véase también [[Impedancia Compleja]],
> [[Asociacion de Impedancias]] y [[Analisis de Nodos]].
