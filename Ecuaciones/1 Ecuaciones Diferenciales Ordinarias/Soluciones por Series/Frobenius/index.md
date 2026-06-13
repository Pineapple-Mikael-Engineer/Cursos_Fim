---
title: Frobenius
tags:
  - ecuaciones
  - edo
  - teoria
  - series
  - frobenius
  - index
draft: false
aliases:
  - método de Frobenius
  - serie de Frobenius
  - Frobenius method
  - generalized power series
---

# Frobenius

> [!definicion]
> En un **punto singular regular** la serie de potencias ordinaria $\sum a_n x^n$ **falla** (no logra
> reproducir el comportamiento de la solución cerca de la singularidad). El **método de Frobenius**
> remedia esto proponiendo una **serie generalizada**
> $$y(x)=x^{r}\sum_{n=0}^{\infty}a_n x^{n}=\sum_{n=0}^{\infty}a_n\,x^{n+r},\qquad a_0\neq0,$$
> con un **exponente $r$ a determinar** (que puede **no** ser entero, ni siquiera real). Ese exponente
> sale de la **ecuación indicial**, una ecuación de segundo grado para $r$ obtenida de la potencia más
> baja al sustituir la serie en la EDO.

> [!info]
> Subcarpeta del bloque [[Soluciones por Series/index| soluciones por series]], dentro del
> [[1 Ecuaciones Diferenciales Ordinarias/index| capítulo de EDO]]. Es la versión del método de series
> para el caso **singular regular**, complementaria a los [[Puntos Ordinarios]]. De aquí salen las
> grandes funciones especiales de la física.

---

## En qué consiste

> [!teoria] Por qué hace falta el factor $x^{r}$
> Cerca de un punto singular, las soluciones **no** son analíticas: típicamente se comportan como una
> **potencia $x^{r}$** (con $r$ fraccionario o negativo) o incluso con un $\ln x$. Una serie de Taylor
> $\sum a_n x^n$ solo puede representar funciones analíticas en $0$, así que **no puede** capturar un
> $x^{1/2}$ o un $x^{-1}$. El prototipo es la **ecuación de Euler**
> $$x^2y''+a\,x\,y'+b\,y=0,$$
> cuyas soluciones son exactamente potencias $y=x^{m}$ (al sustituir, $x^m[m(m-1)+am+b]=0$). El factor
> $x^{r}$ de Frobenius es precisamente esa potencia "de cabecera": separa el comportamiento singular
> $x^{r}$ y deja que la **serie** $\sum a_n x^n$ corrija lo analítico restante.

> [!teoria] De dónde sale la ecuación indicial
> Al sustituir $y=\sum a_n x^{n+r}$ en la EDO normalizada $x^2y''+x(xp)y'+(x^2q)y=0$ y mirar la
> **potencia más baja** ($x^{r}$, la del término $a_0$), aparece la condición
> $$a_0\big[r(r-1)+p_0\,r+q_0\big]=0,\qquad p_0=\lim_{x\to0}x\,p(x),\quad q_0=\lim_{x\to0}x^2q(x).$$
> Como $a_0\neq0$, el corchete debe anularse: esa es la **ecuación indicial** $r(r-1)+p_0r+q_0=0$.
> Es cuadrática, así que da **dos raíces** $r_1\ge r_2$ (los *exponentes* de la singularidad). El
> desarrollo formal en [[Ecuacion Indicial]].

> [!teoria] La diferencia $r_1-r_2$ decide la forma de la segunda solución
> Una raíz siempre entrega una solución $y_1=x^{r_1}\sum a_n x^n$ limpia. La **segunda** solución
> depende de cómo se relacionen $r_1$ y $r_2$, y todo se reduce al valor de la **diferencia
> $r_1-r_2$**:
> - **No entera** → las dos raíces dan **dos series de Frobenius independientes** y limpias, sin
>   sorpresas. Caso [[Raices Diferencia No Entera]].
> - **Entera positiva** → la recurrencia de la raíz menor puede **romperse** (división por cero); la
>   segunda solución a veces necesita un **término logarítmico** $C\,y_1\ln x$. Caso
>   [[Raices Diferencia Entera]].
> - **Repetida** ($r_1=r_2$) → solo hay **una** serie posible; la segunda solución **siempre** lleva un
>   $\ln x$. Caso [[Raices Repetidas]].
>
> Estos tres escenarios son el corazón del método y se desarrollan en las notas hijas.

> [!info] Mapa de las hijas
> 1. Antes de aplicar el método, hay que **clasificar el punto**: [[Puntos Singulares Regulares]].
> 2. El exponente $r$ y su ecuación: [[Ecuacion Indicial]].
> 3. Los tres casos según $r_1-r_2$:
>    - [[Raices Diferencia No Entera]] — dos series limpias.
>    - [[Raices Diferencia Entera]] — posible logaritmo.
>    - [[Raices Repetidas]] — logaritmo seguro.

> [!info] Qué produce el método
> Aplicado a las grandes EDO de la física, Frobenius **genera** las funciones de **Bessel**
> $J_\nu,Y_\nu$ (de $x^2y''+xy'+(x^2-\nu^2)y=0$) y las funciones/polinomios de **Legendre** (de
> $(1-x^2)y''-2xy'+\ell(\ell+1)y=0$, tras llevar la singularidad al origen). Todas se catalogan en
> [[Funciones Especiales/index| funciones especiales]].

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Cuándo | punto **singular regular** ([[Puntos Singulares Regulares\|clasificar antes]]) |
> | Propuesta | $y=x^{r}\sum a_n x^{n}$, $a_0\neq0$ |
> | Exponente $r$ | raíces de la **ecuación indicial** $r(r-1)+p_0r+q_0=0$ |
> | $p_0,q_0$ | $p_0=\lim x p$, $q_0=\lim x^2q$ |
> | Caso $r_1-r_2\notin\mathbb{Z}$ | dos series limpias |
> | Caso $r_1-r_2\in\mathbb{Z}^{+}$ | posible $\ln x$ |
> | Caso $r_1=r_2$ | $\ln x$ seguro |
> | Frutos | Bessel, Legendre ([[Funciones Especiales/index\|funciones especiales]]) |

> [!corolario]
> Frobenius **extiende** el método de series al caso singular regular: añadiendo un factor $x^{r}$ que
> absorbe el comportamiento no analítico, recupera una recurrencia algebraica para los $a_n$. El precio
> es vigilar la **diferencia de raíces** $r_1-r_2$, que decide si la segunda solución es otra serie
> limpia o necesita un logaritmo. Es la puerta de entrada a las funciones especiales.

> [!referencia]
> - El paso previo (clasificar el punto): [[Puntos Singulares Regulares]].
> - El exponente $r$: [[Ecuacion Indicial]].
> - Los tres casos: [[Raices Diferencia No Entera]], [[Raices Diferencia Entera]], [[Raices Repetidas]].
> - El caso ordinario (sin $x^r$): [[Puntos Ordinarios]].
> - Las funciones que produce: [[Funciones Especiales/index]].
> - Marco del bloque: [[Soluciones por Series/index]].
