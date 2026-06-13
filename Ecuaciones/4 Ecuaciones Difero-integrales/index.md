---
title: Ecuaciones Difero-integrales
tags:
  - ecuaciones
  - difero-integrales
  - teoria
  - index
draft: false
aliases:
  - ecuaciones difero-integrales
  - ecuaciones integro-diferenciales
  - cálculo fraccionario
  - differintegral
---

# Ecuaciones Difero-integrales

> [!definicion]
> Las **ecuaciones difero-integrales** mezclan, sobre la misma incógnita, **derivación** e
> **integración**. Hay dos grandes formas de esa mezcla:
> 1. **Integro-diferenciales**: aparecen a la vez la derivada $\varphi'$ **y** una integral
>    $\int K\varphi$ de la incógnita.
> 2. **Cálculo fraccionario**: un **único operador** $D^{q}$ de **orden arbitrario** $q$ (no entero)
>    que interpola con continuidad entre derivar ($q>0$) e integrar ($q<0$) — el *differintegral*.

> [!info]
> Cuarta familia del curso: la **fusión** de las [[1 Ecuaciones Diferenciales Ordinarias/index| EDO]]
> y las [[3 Ecuaciones Integrales/index| ecuaciones integrales]]. La hemos venido anticipando: el
> [[Problema de Abel| problema de Abel]] ya era una *media integración*, y las
> [[Ecuaciones de Convolucion| ecuaciones de convolución]] se resuelven con la misma herramienta —la
> [[Transformada de Laplace/index| transformada de Laplace]]— que domina aquí.

---

## Dos caras de "derivar e integrar a la vez"

> [!teoria]
> El nombre **difero-integral** capta una idea profunda: derivar e integrar no son operaciones
> opuestas y aisladas, sino los **extremos de un continuo**. Las dos ramas del capítulo lo exploran
> desde ángulos distintos:
> - Las **[[Integro-Diferenciales/index| integro-diferenciales]]** surgen de modelar sistemas con
>   **memoria**: la tasa de cambio $\varphi'(t)$ depende no solo del estado actual, sino de toda la
>   **historia** $\int_0^t K(t-s)\varphi(s)\,ds$ (viscoelasticidad, poblaciones con retardo, control).
>   Se resuelven con **Laplace** (convierten la mezcla en una ecuación algebraica).
> - El **[[Calculo Fraccionario/index| cálculo fraccionario]]** generaliza el propio operador: define
>   $D^{q}$ para $q$ real (o complejo). $D^{1}$ es la derivada, $D^{-1}$ la integral, y $D^{1/2}$ una
>   "media derivada" —aplicarla dos veces da una derivada entera—. Es la herramienta natural para la
>   **difusión anómala** y los materiales con memoria de **ley de potencias**.
>
> Ambas se encuentran: una ecuación integro-diferencial de convolución con núcleo $1/(t-s)^{\alpha}$
> **es** una ecuación diferencial **fraccionaria**.

> [!info] Mapa del capítulo
> | Sección | Contenido |
> |---|---|
> | [[Integro-Diferenciales/index\|Integro-Diferenciales]] | derivada + integral; memoria; resolver con Laplace |
> | [[Calculo Fraccionario/index\|Cálculo Fraccionario]] | el operador $D^{q}$; Riemann-Liouville, Caputo, Mittag-Leffler, EDF |

## Resumen

> [!resumen]
> | Rama | Forma | Herramienta |
> |---|---|---|
> | Integro-diferencial | $\varphi'(t)=f+\int K(t-s)\varphi\,ds$ | [[Transformada de Laplace/index\|Laplace]] |
> | Fraccionaria | $D^{q}\varphi=f$, $q\notin\mathbb{Z}$ | Riemann-Liouville / Caputo; Mittag-Leffler |
> | Puente | núcleo $1/(t-s)^{\alpha}$ | una integro-dif. de convolución ES fraccionaria |

> [!corolario]
> El cálculo clásico separa tajantemente derivar de integrar; las ecuaciones difero-integrales
> revelan que entre ambos hay un **continuo**. Modelar la **memoria** —que el presente dependa de
> todo el pasado— lleva de forma natural a operadores que son parte derivada y parte integral.

> [!referencia]
> - El caso con memoria explícita: [[Integro-Diferenciales/index]].
> - El operador unificado: [[Calculo Fraccionario/index]].
> - El precursor histórico: [[Problema de Abel]].
