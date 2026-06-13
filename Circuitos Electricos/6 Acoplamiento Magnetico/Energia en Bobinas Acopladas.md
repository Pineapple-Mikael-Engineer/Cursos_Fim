---
title: Energía en Bobinas Acopladas
tags:
  - circuitos-electricos
  - teoria
  - acoplamiento-magnetico
draft: false
aliases:
  - energía en bobinas acopladas
  - energía magnética almacenada
  - energy in coupled coils
---

# Energía en Bobinas Acopladas

> [!definicion]
> La **energía magnética almacenada** en dos bobinas acopladas con corrientes $i_1$ e $i_2$ es
> $$W=\tfrac12 L_1 i_1^2+\tfrac12 L_2 i_2^2\pm M\,i_1 i_2,$$
> es decir la **autoinducción** de cada bobina ($\tfrac12 L i^2$) más un **término mutuo** $\pm M\,i_1 i_2$
> debido al acoplamiento. El signo lo fija la [[Regla de los Puntos]]: **positivo** ($+M$) si los flujos
> se **refuerzan**, **negativo** ($-M$) si se **oponen**.

> [!info]
> Extiende la energía del [[Inductor| inductor]] ($\tfrac12 L i^2$) al **par acoplado**, en el
> [[6 Acoplamiento Magnetico/index| capítulo 6]]; el acoplamiento se mide con la
> [[Inductancia Mutua| inductancia mutua]] $M$. De exigir $W\ge0$ para todo par de corrientes sale la
> cota del [[Coeficiente de Acoplamiento| coeficiente de acoplamiento]] ($k\le1$). Fraile Mora, cap. 1,
> §1.19.

---

## Ejemplo

> [!ejemplo]
> **Energía con flujos que se refuerzan.**
>
> Dos bobinas acopladas tienen $L_1=2\ \text{H}$, $L_2=8\ \text{H}$ y $M=3\ \text{H}$. Por ellas circulan
> $i_1=2\ \text{A}$ e $i_2=1\ \text{A}$, y sus flujos se **refuerzan** (término mutuo $+M$). Hallar la
> energía almacenada.
>
> **Paso 1 — Términos de autoinducción.**
> $$\tfrac12 L_1 i_1^2=\tfrac12(2)(2^2)=4\ \text{J},\qquad \tfrac12 L_2 i_2^2=\tfrac12(8)(1^2)=4\ \text{J}.$$
>
> **Paso 2 — Término mutuo.** Como los flujos se refuerzan, va con signo $+$:
> $$+M\,i_1 i_2=+3\cdot2\cdot1=6\ \text{J}.$$
>
> **Paso 3 — Sumar.** $W=4+4+6=14\ \text{J}$.
>
> > [!solucion]
> > $W=14\ \text{J}$: la **autoinducción** aporta $4+4=8\ \text{J}$ y la **mutua** $6\ \text{J}$. Si los
> > flujos se opusieran ($-M$), el término mutuo restaría y la energía bajaría a $8-6=2\ \text{J}$.

---

## En qué consiste

> [!teoria] El término mutuo es la energía del acoplamiento
> Los dos primeros términos, $\tfrac12 L_1 i_1^2$ y $\tfrac12 L_2 i_2^2$, son la energía propia de cada
> bobina: la misma que tendría aislada, **siempre $\ge0$**. El tercero, $\pm M\,i_1 i_2$, es la energía
> **del acoplamiento**:
> - **Positiva** ($+M$) cuando los campos se **suman**: para las mismas corrientes hay más flujo enlazado
>   y, por tanto, más energía almacenada.
> - **Negativa** ($-M$) cuando los campos se **oponen**: el flujo total disminuye y la energía baja.
>
> A diferencia de la autoinducción, el término mutuo **puede restar**. Lo que nunca puede es hacer que
> $W$ se vuelva negativa, y esa imposibilidad es justo lo que acota a $M$.

> [!teorema] Cota de la inductancia mutua
> La energía almacenada es no negativa para **cualquier** par de corrientes $i_1,i_2$. De ello se sigue
> que la inductancia mutua está acotada por la media geométrica de las autoinducciones:
> $$M\le\sqrt{L_1 L_2},\qquad\text{es decir}\qquad k=\frac{M}{\sqrt{L_1 L_2}}\le1.$$

> [!demostracion]
> **Paso 1 — Caso desfavorable.** Tomamos el signo que puede hacer $W$ menor (flujos opuestos):
> $$W=\tfrac12 L_1 i_1^2+\tfrac12 L_2 i_2^2- M\,i_1 i_2.$$
>
> **Paso 2 — Forma cuadrática.** $W$ es una forma cuadrática en $i_1,i_2$. Es $\ge0$ para **todo**
> $i_1,i_2$ si y solo si la matriz asociada $\begin{pmatrix} L_1 & -M \\ -M & L_2\end{pmatrix}$ es
> semidefinida positiva, lo que (con $L_1,L_2>0$) equivale a que su determinante sea no negativo:
> $$L_1 L_2-M^2\ge0.$$
>
> **Paso 3 — Despejar.** De $M^2\le L_1 L_2$ resulta $M\le\sqrt{L_1 L_2}$, esto es $k\le1$.
> $\blacksquare$

> [!warning]
> El signo del término mutuo lo dicta la [[Regla de los Puntos]]: **no es siempre $+$**. Con corrientes
> tales que el término reste, la energía **disminuye**, pero nunca cae por debajo de $0$ (de ahí la cota
> $M\le\sqrt{L_1 L_2}$). Además, $W$ es una **función de estado**: depende solo de las corrientes
> $(i_1,i_2)$, no del camino seguido para alcanzarlas.

## Resumen

> [!resumen]
> | Concepto | Expresión |
> |:---|:---|
> | Energía almacenada | $W=\tfrac12 L_1 i_1^2+\tfrac12 L_2 i_2^2\pm M\,i_1 i_2$ |
> | Término de autoinducción | $\tfrac12 L_1 i_1^2+\tfrac12 L_2 i_2^2\ \ (\ge0)$ |
> | Término mutuo | $\pm M\,i_1 i_2$ ($+$ refuerzan, $-$ se oponen) |
> | Cota de $M$ | $M\le\sqrt{L_1 L_2}$, equivale a $k\le1$ |

> [!corolario]
> La energía de un par de bobinas acopladas suma la energía propia de cada una más un término mutuo con
> signo. Exigir que esa energía sea siempre no negativa fuerza $M\le\sqrt{L_1 L_2}$: el acoplamiento no
> puede ser arbitrariamente grande, y el [[Coeficiente de Acoplamiento| coeficiente de acoplamiento]]
> nunca supera la unidad.

> [!referencia]
> Fraile Mora, cap. 1, §1.19. Parámetro del acoplo: [[Inductancia Mutua]]. Cota deducida:
> [[Coeficiente de Acoplamiento]]. Caso de una sola bobina: [[Inductor]]. Signo del término:
> [[Regla de los Puntos]]. Índice: [[6 Acoplamiento Magnetico/index]].
