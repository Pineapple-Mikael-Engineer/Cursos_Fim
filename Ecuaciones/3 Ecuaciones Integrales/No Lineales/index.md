---
title: Ecuaciones Integrales No Lineales
order: 5
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - no-lineales
  - index
draft: false
aliases:
  - ecuaciones integrales no lineales
  - nonlinear integral equations
---

# Ecuaciones Integrales No Lineales

> [!definicion]
> En una ecuación integral **no lineal** la incógnita $\varphi$ entra de forma no lineal. Las dos formas canónicas son:
> $$\text{Hammerstein:}\quad \varphi(x)=f(x)+\lambda\int_a^b K(x,t)\,g\big(t,\varphi(t)\big)\,dt,\qquad \text{Urysohn:}\quad \varphi(x)=f(x)+\lambda\int_a^b K\big(x,t,\varphi(t)\big)\,dt.$$
> En Hammerstein la no linealidad $g$ está **separada** del núcleo; en Urysohn el **núcleo entero** es no lineal. Sin superposición, pueden tener **una, ninguna o varias** soluciones.

> [!info]
> Familia que rompe la linealidad del [[3 Ecuaciones Integrales/index| capítulo]]. A diferencia de [[Fredholm/index| Fredholm]] lineal (espectro y alternativa), aquí no hay teoría cerrada: la existencia se prueba con **teoremas de punto fijo** y aparecen fenómenos no lineales como las **bifurcaciones** (múltiples soluciones al variar $\lambda$).

---

## Por qué cambian las reglas

> [!teoria]
> Sin superposición se pierden la resolvente y el principio de descomposición; en su lugar, la herramienta es el **punto fijo** del operador no lineal $T\varphi=f+\lambda\int K\,g(t,\varphi)$:
> - **Contracción (Banach).** Si $g$ es Lipschitz y $\lvert\lambda\rvert$ es pequeño, $T$ es una contracción y hay solución **única**, hallada por [[Aproximaciones Sucesivas| iteración]] $\varphi_{n+1}=T\varphi_n$.
> - **Compacidad (Schauder).** Si el operador es **compacto** y mapea un convexo en sí mismo, el teorema de Schauder garantiza **existencia** (aunque no unicidad): puede haber **varias** soluciones.
> - **Bifurcación.** Cuando $\lambda$ cruza un autovalor del núcleo linealizado, pueden **nacer soluciones nuevas** —ramas que se separan de la trivial—, igual que en los sistemas dinámicos no lineales.

> [!info] Recorrido de la sección
> | Nota | Aporte |
> |---|---|
> | [[Ecuacion de Hammerstein\|Ecuación de Hammerstein]] | no linealidad separada $g(t,\varphi)$; bifurcaciones |
> | [[Ecuacion de Urysohn\|Ecuación de Urysohn]] | núcleo no lineal general; Schauder |

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Hammerstein | $\varphi=f+\lambda\int K\,g(t,\varphi)$ |
> | Urysohn | $\varphi=f+\lambda\int K(x,t,\varphi)$ |
> | Existencia | punto fijo: Banach (única) / Schauder (existencia) |
> | Fenómeno nuevo | **bifurcaciones**, múltiples soluciones |

> [!corolario]
> Quitar la linealidad cambia la pregunta: ya no es "¿cuál es la solución?" sino "¿cuántas hay y cómo aparecen?". La teoría se vuelve **cualitativa** (punto fijo, bifurcaciones), emparentada con la dinámica no lineal de las [[Ciclos Limite y Poincare-Bendixson| EDO no lineales]].

> [!referencia]
> - La forma más estudiada: [[Ecuacion de Hammerstein]].
> - El caso general: [[Ecuacion de Urysohn]].
> - La iteración que las resuelve: [[Aproximaciones Sucesivas]].
