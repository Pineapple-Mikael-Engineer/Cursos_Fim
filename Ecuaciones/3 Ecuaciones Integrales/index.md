---
title: Ecuaciones Integrales
order: 3
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - index
draft: false
aliases:
  - ecuaciones integrales
  - integral equations
---

# Ecuaciones Integrales

> [!definicion]
> Una **ecuación integral** tiene la función incógnita $\varphi$ **dentro de una integral**. La forma general (lineal) es
> $$\alpha(x)\,\varphi(x)=f(x)+\lambda\int K(x,t)\,\varphi(t)\,dt,$$
> donde $K(x,t)$ es el **núcleo**, $f$ el término libre y $\lambda$ un parámetro. Según los **límites** de integración y dónde aparezca $\varphi$, se clasifican en **Volterra** / **Fredholm** y en **primera** / **segunda especie**.

> [!info]
> Tercera familia del curso, "espejo" de las [[1 Ecuaciones Diferenciales Ordinarias/index| ecuaciones diferenciales]]: donde la EDO **deriva** la incógnita, la integral la **promedia**. Ambas se conectan (un PVI **es** una ecuación integral, base de [[Iteracion de Picard| Picard]]), y la [[Funcion de Green para EDO| función de Green]] convierte problemas de frontera en ecuaciones integrales. La fuente de referencia es **Krasnov, Kiseliov, Makarenko**.

---

## El mapa: dos ejes de clasificación

> [!teoria]
> Toda la teoría se ordena por **dos preguntas**:
> 1. **¿Los límites son fijos o variables?** — define la **familia**:
>    - **Volterra**: límite superior **variable**, $\displaystyle\int_0^x K(x,t)\varphi(t)\,dt$. Como un PVI, "acumula" desde un inicio; siempre tiene solución única (se parece a integrar).
>    - **Fredholm**: límites **fijos**, $\displaystyle\int_a^b K(x,t)\varphi(t)\,dt$. Como un PVF, es un problema **global**; puede tener una, ninguna o infinitas soluciones (autovalores).
> 2. **¿La incógnita aparece fuera de la integral?** — define la **especie**:
>    - **Segunda especie**: $\varphi$ aparece **también fuera**, $\varphi=f+\lambda\int K\varphi$. Bien planteada; se resuelve por **resolvente** / aproximaciones sucesivas.
>    - **Primera especie**: $\varphi$ aparece **solo dentro**, $f=\int K\varphi$. A menudo **mal planteada** (un problema inverso); requiere regularización.
> | | **2ª especie** ($\varphi$ fuera y dentro) | **1ª especie** ($\varphi$ solo dentro) |
> |---|---|---|
> | **Volterra** (límite variable) | $\varphi(x)=f+\lambda\int_0^x K\varphi$ | $f(x)=\int_0^x K\varphi$ (Abel) |
> | **Fredholm** (límites fijos) | $\varphi(x)=f+\lambda\int_a^b K\varphi$ | $f(x)=\int_a^b K\varphi$ (mal planteada) |

> [!teoria] Las herramientas que se repiten
> Aunque hay muchos tipos, los métodos son pocos y reaparecen: la **resolvente** (núcleos iterados, serie de Neumann), las **aproximaciones sucesivas** (punto fijo, como Picard), la **transformada de Laplace** para núcleos de convolución $K(x-t)$, y —para Fredholm— el **espectro del núcleo** (autovalores y funciones propias) con la **alternativa de Fredholm**.

---

## Mapa del capítulo

> [!info]
> | Sección | Contenido |
> |---|---|
> | [[Conceptos Fundamentales\|Conceptos Fundamentales]] | núcleo, especie, familia, homogénea |
> | [[Nexo EDO e Integrales\|Nexo EDO e Integrales]] | un PVI/PVF reescrito como ecuación integral |
> | [[Volterra/index\|Volterra]] | límite variable: resolvente, convolución, Abel |
> | [[Fredholm/index\|Fredholm]] | límites fijos: núcleo degenerado, espectro, alternativa |
> | [[No Lineales/index\|No Lineales]] | Hammerstein, Urysohn |
> | [[Singulares/index\|Singulares]] | Abel generalizada, Cauchy, Wiener-Hopf |
> | [[Metodos Aproximados/index\|Métodos Aproximados]] | degenerar el núcleo, Galerkin, colocación, Nyström |
> | [[Multivariable/index\|Multivariable y Física]] | Fredholm $n$-dim, teoría de potencial (BEM), dispersión, transporte |

## Resumen

> [!resumen]
> | Eje | Opciones | Consecuencia |
> |---|---|---|
> | Familia | Volterra / Fredholm | límite variable (local) / fijo (global, espectral) |
> | Especie | 2ª / 1ª | bien planteada / a menudo inversa mal planteada |
> | Núcleo | general / convolución / degenerado / simétrico | método: resolvente / Laplace / álgebra / espectral |

> [!corolario]
> Una ecuación integral es una EDO "puesta del revés": la incógnita está bajo el signo integral. Esa integral **regulariza** (suaviza), lo que hace que las de **segunda especie** estén bien planteadas y las de **primera especie** sean problemas inversos delicados. Clasificar bien —familia y especie— es, como en las EDP, el primer paso para elegir el método.

> [!referencia]
> - Empezar por: [[Conceptos Fundamentales]] y [[Nexo EDO e Integrales]].
> - La familia más "amable": [[Volterra/index]].
> - El puente con lo diferencial: [[Funcion de Green para EDO]].
