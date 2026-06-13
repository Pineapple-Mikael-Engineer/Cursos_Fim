---
title: Funciones Armónicas
tags:
  - ecuaciones
  - edp
  - teoria
  - laplace
  - armonicas
draft: false
aliases:
  - función armónica
  - funciones armónicas
  - armónica conjugada
  - harmonic functions
  - Liouville
---

# Funciones Armónicas

> [!definicion]
> Una función $u$ (de clase $C^2$) es **armónica** en un dominio $\Omega$ si satisface la
> **ecuación de Laplace**
> $$\nabla^2u=0,$$
> es decir $u_{xx}+u_{yy}=0$ en 2D, o $u_{xx}+u_{yy}+u_{zz}=0$ en 3D. Las funciones armónicas son
> los estados de **equilibrio** del operador de Laplace y poseen cuatro propiedades estructurales:
> - **Propiedad del valor medio**: $u$ en un punto es el **promedio** de sus valores sobre cualquier
>   esfera centrada en él.
> - **Principio del máximo**: los extremos de $u$ están siempre en la **frontera**, nunca en el
>   interior.
> - **Suavidad analítica**: toda función armónica es $C^\infty$ —de hecho **analítica**— en el
>   interior, por irregular que sea el dato de frontera.
> - **Teorema de Liouville**: una función armónica y **acotada** en todo $\mathbb{R}^n$ es
>   necesariamente **constante**.

> [!info]
> Objeto central del [[Ecuacion de Laplace y Poisson/index| bloque de Laplace y Poisson]], dentro
> del [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]]. Las dos primeras propiedades
> se desarrollan en [[Teorema del Valor Medio]] y [[Principio del Maximo Eliptico]]; los ejemplos
> concretos de funciones armónicas en regiones acotadas aparecen en [[Laplace en Disco]].

---

## Ejemplo

> [!ejemplo] Verificar que $x^2-y^2$, $xy$ y $\ln r$ son armónicas
> Comprobamos directamente $\nabla^2u=u_{xx}+u_{yy}$ en cada caso.
>
> **(a) Polinomio $u=x^2-y^2$.**
> $$u_x=2x,\quad u_{xx}=2,\qquad u_y=-2y,\quad u_{yy}=-2.$$
> Sumando, $u_{xx}+u_{yy}=2-2=0$. **Es armónica.** Físicamente representa un potencial de "punto de
> silla": crece en $x$ y decrece en $y$ con curvaturas que se cancelan.
>
> **(b) Producto $u=xy$.**
> $$u_x=y,\quad u_{xx}=0,\qquad u_y=x,\quad u_{yy}=0.$$
> Trivialmente $u_{xx}+u_{yy}=0$. **Es armónica.** Junto con $x^2-y^2$ son las dos armónicas
> cuadráticas básicas (parte real e imaginaria de $z^2=(x+iy)^2=x^2-y^2+2ixy$).
>
> **(c) Logaritmo $u=\ln r$ en 2D**, con $r=\sqrt{x^2+y^2}$.
> Usamos el laplaciano en polares $\nabla^2u=u_{rr}+\tfrac1r u_r+\tfrac1{r^2}u_{\theta\theta}$.
> Como $u=\ln r$ no depende de $\theta$,
> $$u_r=\frac1r,\qquad u_{rr}=-\frac{1}{r^2},\qquad u_\theta=0.$$
> Entonces $\nabla^2u=-\dfrac{1}{r^2}+\dfrac1r\cdot\dfrac1r=0$ para $r\neq0$. **Es armónica** salvo
> en el origen, donde tiene la singularidad del potencial de una carga puntual. El análogo en 3D es
> $u=1/r$, el **potencial de Coulomb**, que cumple $\nabla^2(1/r)=0$ para $r\neq0$.

---

## En qué consiste

> [!teoria] Catálogo de funciones armónicas
> Conviene tener en la cabeza una **biblioteca** de armónicas, porque por superposición generan
> todas las demás:
> - **Lineales** $ax+by$ (y $ax+by+cz$): laplaciano nulo por ser de segundo orden cero. Cualquier
>   plano es armónico.
> - **Cuadráticas** $x^2-y^2$ y $xy$ en 2D: las dos curvaturas opuestas se cancelan.
> - **Partes real e imaginaria de una función analítica**: si $f(z)=u(x,y)+iv(x,y)$ es analítica,
>   tanto $u$ como $v$ son armónicas (teorema de abajo). Esto convierte **toda** la teoría de
>   variable compleja en una fábrica de armónicas: $e^x\cos y$, $e^x\operatorname{sen} y$,
>   $\cos x\cosh y$, etc.
> - **Potenciales fundamentales**: $\ln r$ en 2D y $1/r$ en 3D, armónicos fuera de su singularidad.
>   Son las soluciones "fuente" del potencial gravitatorio y electrostático.

> [!teorema] Las partes de una función analítica son armónicas conjugadas
> Si $f=u+iv$ es **analítica** en un dominio (holomorfa), entonces $u$ y $v$ son **armónicas** allí,
> y se dicen **armónicas conjugadas**.

> [!demostracion]
> **Paso 1 — Cauchy-Riemann.** Que $f$ sea analítica equivale a las ecuaciones de Cauchy-Riemann
> $$u_x=v_y,\qquad u_y=-v_x.$$
> Como $f$ es analítica, $u$ y $v$ tienen derivadas parciales continuas de todo orden, así que las
> derivadas cruzadas conmutan ($v_{xy}=v_{yx}$).
>
> **Paso 2 — Derivar para $u$.** Derivamos la primera ecuación respecto de $x$ y la segunda respecto
> de $y$:
> $$u_{xx}=v_{yx},\qquad u_{yy}=-v_{xy}.$$
> Sumando y usando $v_{xy}=v_{yx}$:
> $$u_{xx}+u_{yy}=v_{yx}-v_{xy}=0.$$
> Por tanto $u$ es armónica.
>
> **Paso 3 — Lo mismo para $v$.** Derivamos ahora la primera respecto de $y$ y la segunda respecto
> de $x$:
> $$u_{xy}=v_{yy},\qquad u_{yx}=-v_{xx},$$
> de donde $v_{xx}+v_{yy}=u_{yx}-u_{xy}=0$. Así $v$ también es armónica. $\blacksquare$

> [!info] El valor medio y el máximo
> Las dos propiedades más usadas se enuncian aparte por su importancia:
> - la **propiedad del valor medio** —$u(P)$ es el promedio de $u$ sobre círculos/esferas centrados
>   en $P$— se trata en [[Teorema del Valor Medio]];
> - el **principio del máximo** —los extremos viven en la frontera, de donde sale la unicidad del
>   problema de Dirichlet— se trata en [[Principio del Maximo Eliptico]].

> [!proposicion] Teorema de Liouville (armónico)
> Si $u$ es armónica en **todo** $\mathbb{R}^n$ y está **acotada** ($|u|\le M$), entonces $u$ es
> **constante**. Idea: por el valor medio, $u$ en cualquier punto es un promedio sobre esferas
> arbitrariamente grandes; comparando dos puntos, los promedios coinciden en el límite, así que $u$
> no puede variar. Es el análogo armónico del Liouville complejo (una entera y acotada es constante),
> coherente con que las partes de $f$ analítica son armónicas.

> [!warning]
> "Armónica" es una propiedad **local en la EDP pero global en sus consecuencias**: no se puede
> construir una función armónica con un "bulto" interior aislado. Si intentas imponer un máximo
> interior, violas el principio del máximo y la función deja de ser armónica. Toda la rigidez de
> $\nabla^2u=0$ viene de ahí.

## Resumen

> [!resumen]
> | Propiedad | Enunciado | Consecuencia |
> |---|---|---|
> | Valor medio | $u(P)=$ promedio sobre esferas centradas en $P$ | no hay "grumos" |
> | Máximo | extremos en la **frontera** | unicidad de Dirichlet |
> | Suavidad | $u$ es **analítica** en el interior | regulariza el dato |
> | Liouville | armónica + acotada en $\mathbb{R}^n$ $\Rightarrow$ constante | rigidez global |
> | Conjugada | $f=u+iv$ analítica $\Rightarrow$ $u,v$ armónicas | fábrica de ejemplos |

> [!corolario]
> Ser armónica es ser el **equilibrio perfecto**: cada punto es la media de su entorno. Esa única
> condición, $\nabla^2u=0$, fuerza simultáneamente la suavidad analítica, la ausencia de extremos
> interiores y la rigidez de Liouville. En 2D el puente con la variable compleja regala
> infinitas armónicas listas para usar.

> [!referencia]
> - El promedio sobre esferas: [[Teorema del Valor Medio]].
> - Extremos en la frontera y unicidad: [[Principio del Maximo Eliptico]].
> - Armónicas en regiones acotadas y la fórmula de Poisson: [[Laplace en Disco]].
> - Marco general: [[Ecuacion de Laplace y Poisson/index]].
