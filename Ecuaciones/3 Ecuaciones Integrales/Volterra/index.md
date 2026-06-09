---
title: Ecuaciones de Volterra
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - volterra
  - index
draft: false
aliases:
  - ecuaciones de Volterra
  - Volterra equations
---

# Ecuaciones de Volterra

> [!definicion]
> Una **ecuación integral de Volterra** tiene el **límite superior variable**: la incógnita se integra
> desde un inicio fijo hasta el punto actual $x$,
> $$\varphi(x)=f(x)+\lambda\int_{0}^{x}K(x,t)\,\varphi(t)\,dt\quad(\text{2ª especie}),\qquad f(x)=\int_{0}^{x}K(x,t)\,\varphi(t)\,dt\quad(\text{1ª especie}).$$
> Por "acumular desde un inicio", se comporta como un **problema de valor inicial**: su solución
> (2ª especie) **existe y es única**, y se construye por iteración.

> [!info]
> La familia **amable** del [[3 Ecuaciones Integrales/index| capítulo de ecuaciones integrales]]: a
> diferencia de [[Fredholm/index| Fredholm]] (límites fijos, problema global con espectro), Volterra
> es **local** y siempre resoluble. Nace al integrar EDOs ([[Nexo EDO e Integrales| nexo EDO]]) y su
> caso de **convolución** se resuelve con [[Ecuaciones de Convolucion| Laplace]].

---

## Por qué Volterra siempre se resuelve

> [!teoria]
> La diferencia con Fredholm es geométrica: el límite superior **variable** hace que el operador
> $K\varphi=\int_0^x K(x,t)\varphi(t)\,dt$ sea "pequeño" para $x$ cerca de $0$ (el intervalo de
> integración tiende a cero). Eso lo vuelve una **contracción** en intervalos cortos, así que las
> [[Aproximaciones Sucesivas| aproximaciones sucesivas]] **siempre convergen** —sin restricción sobre
> $\lambda$— a la única solución. La [[Resolvente y Nucleos Iterados| resolvente]] $\Gamma(x,t;\lambda)$
> empaqueta esa serie:
> $$\varphi(x)=f(x)+\lambda\int_0^x\Gamma(x,t;\lambda)\,f(t)\,dt.$$
> Es el mismo mecanismo que la [[Iteracion de Picard| iteración de Picard]] para EDOs: no por casualidad, porque un PVI **es** una ecuación de Volterra.

> [!info] Recorrido de la sección
> | Nota | Aporte |
> |---|---|
> | [[Volterra Segunda Especie\|Volterra de 2ª Especie]] | la ecuación estándar; existencia y unicidad |
> | [[Resolvente y Nucleos Iterados\|Resolvente y Núcleos Iterados]] | serie de Neumann; $\Gamma(x,t;\lambda)$ |
> | [[Aproximaciones Sucesivas\|Aproximaciones Sucesivas]] | iteración de punto fijo; convergencia |
> | [[Ecuaciones de Convolucion\|Ecuaciones de Convolución]] | núcleo $K(x-t)$ → resolver con Laplace |
> | [[Volterra Primera Especie\|Volterra de 1ª Especie]] | reducir a 2ª especie derivando |
> | [[Problema de Abel\|Problema de Abel]] | núcleo singular $1/\sqrt{x-t}$; la tautócrona |

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Forma (2ª especie) | $\varphi=f+\lambda\int_0^x K\varphi$ |
> | Existencia/unicidad | **siempre** (para todo $\lambda$) |
> | Método general | resolvente / aproximaciones sucesivas |
> | Convolución $K(x-t)$ | transformada de [[Ecuaciones de Convolucion\|Laplace]] |
> | 1ª especie | derivar para pasar a 2ª especie; Abel si es singular |

> [!corolario]
> Volterra es "integrar hacia adelante": como cada valor depende solo del **pasado** ($t\le x$), no hay
> conflicto global y la solución existe siempre. Es el reflejo integral del determinismo de un PVI.

> [!referencia]
> - El método estrella: [[Resolvente y Nucleos Iterados]].
> - El caso con Laplace: [[Ecuaciones de Convolucion]].
> - El ejemplo histórico: [[Problema de Abel]].
