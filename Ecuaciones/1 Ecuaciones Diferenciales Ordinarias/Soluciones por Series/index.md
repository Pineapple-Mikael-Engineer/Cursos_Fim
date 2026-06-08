---
title: Soluciones por Series
tags:
  - ecuaciones
  - edo
  - teoria
  - series
  - index
draft: false
aliases:
  - soluciones en serie
  - método de series de potencias
  - series solutions
---

# Soluciones por Series

> [!definicion]
> Cuando una EDO lineal tiene **coeficientes variables** y no encaja en ningún método elemental, se
> busca la solución como una **serie de potencias**
> $$y(x)=\sum_{n=0}^{\infty}a_n\,(x-x_0)^{n},$$
> se sustituye en la ecuación y se obtiene una **relación de recurrencia** para los $a_n$. Según el
> punto $x_0$ sea **ordinario** o **singular regular**, el desarrollo es una serie de Taylor directa o
> una serie **de Frobenius** (multiplicada por $x^{r}$).

> [!info]
> Quinto y último bloque del [[1 Ecuaciones Diferenciales Ordinarias/index| capítulo de EDO]]. Es el
> método más general para coeficientes variables y la **cuna de las funciones especiales** (Bessel,
> Legendre, Hermite), que reaparecen al separar variables en las
> [[2 Ecuaciones en Derivadas Parciales/index| EDP]] y se catalogan en
> [[Funciones Especiales/index| funciones especiales]].

---

## La idea: convertir la EDO en una recurrencia

> [!teoria]
> Una serie de potencias se puede **derivar término a término** dentro de su radio de convergencia.
> Al meter $y=\sum a_n(x-x_0)^n$ en una EDO lineal, cada derivada baja el exponente y desplaza los
> índices; igualando a cero el coeficiente de **cada** potencia $(x-x_0)^k$ se obtiene una **relación
> de recurrencia** que expresa los $a_n$ en función de los primeros. Las constantes libres (dos, para
> una EDO de segundo orden) son los **datos iniciales** $a_0=y(x_0)$ y $a_1=y'(x_0)$: el método
> entrega directamente las dos soluciones independientes.
>
> Lo que decide la **forma** del desarrollo es la naturaleza del punto $x_0$:

> [!info] Punto ordinario vs. punto singular
> | | Punto **ordinario** | Punto **singular regular** |
> |---|---|---|
> | Condición | $p,q$ **analíticas** en $x_0$ | singularidad "suave": $(x-x_0)p$ y $(x-x_0)^2q$ analíticas |
> | Desarrollo | Taylor $\sum a_n(x-x_0)^n$ | Frobenius $(x-x_0)^{r}\sum a_n(x-x_0)^n$ |
> | Soluciones | **dos** en serie de potencias | dependen de la [[Ecuacion Indicial\|ecuación indicial]] |
> | Nota | [[Puntos Ordinarios\|Puntos Ordinarios]] | [[Frobenius/index\|método de Frobenius]] |

---

## Por qué importa (y qué garantiza)

> [!teoria]
> La fuerza del método es doble: (1) **siempre funciona** en un punto ordinario, dando soluciones
> válidas al menos hasta la singularidad más cercana (incluso en el plano complejo); (2) cuando la
> serie **no** suma a una función elemental, *ella misma define* una función nueva. Así nacieron las
> funciones de **Bessel** (de $x^2y''+xy'+(x^2-\nu^2)y=0$), los polinomios de **Legendre** (de
> $(1-x^2)y''-2xy'+\ell(\ell+1)y=0$) y muchas otras: no son "trucos", son las soluciones en serie de
> EDO que aparecen una y otra vez en física.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Idea | $y=\sum a_n(x-x_0)^n$ → recurrencia para $a_n$ |
> | Punto ordinario | dos soluciones de Taylor ([[Puntos Ordinarios\|Puntos Ordinarios]]) |
> | Punto singular regular | serie de Frobenius $x^r\sum a_n x^n$ ([[Frobenius/index\|Frobenius]]) |
> | Constantes | $a_0=y(x_0)$, $a_1=y'(x_0)$ |
> | Frutos | funciones especiales (Bessel, Legendre, …) |

> [!corolario]
> El método de series es el más **universal** para lineales de coeficientes variables: transforma la
> EDO en un problema **algebraico** (una recurrencia) y, de paso, **genera** las funciones especiales
> de la física matemática. Donde fallan los métodos cerrados, la serie siempre avanza.

> [!referencia]
> - El caso fácil y garantizado: [[Puntos Ordinarios]].
> - El caso singular: [[Frobenius/index]].
> - Las funciones que produce: [[Funciones Especiales/index]].
