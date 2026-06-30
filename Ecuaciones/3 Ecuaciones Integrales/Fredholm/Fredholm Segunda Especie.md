---
title: Fredholm de Segunda Especie
order: 1
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - fredholm
  - segunda-especie
draft: false
aliases:
  - Fredholm de segunda especie
  - ecuación de Fredholm de 2ª especie
  - Fredholm equation of the second kind
---

# Fredholm de Segunda Especie

> [!definicion]
> Una **ecuación integral de Fredholm de segunda especie** es
> $$\varphi(x)=f(x)+\lambda\int_{a}^{b}K(x,t)\,\varphi(t)\,dt,$$
> donde $\varphi(x)$ es la **incógnita**, $K(x,t)$ el **núcleo** (dado), $f(x)$ el **término libre** y $\lambda$ un **parámetro**. En forma de operador se escribe $(\mathbb{I}-\lambda K)\varphi=f$, con $K\varphi=\int_a^b K(x,t)\varphi(t)\,dt$. Tiene **solución única** mientras $\lambda$ **no** sea una raíz característica del núcleo; si $\lambda$ **sí** lo es, hay que recurrir a la [[Alternativa de Fredholm| alternativa de Fredholm]].

> [!info]
> La ecuación estándar de [[Fredholm/index| Fredholm]], dentro del [[3 Ecuaciones Integrales/index| capítulo de ecuaciones integrales]]. Es el análogo continuo del sistema lineal $(\mathsf{I}-\lambda\mathsf{A})\mathbf{x}=\mathbf{f}$: el núcleo $K$ hace de matriz y $\lambda$ de (inverso de) autovalor. Su tratamiento depende de la forma de $K$ —ver el panorama de métodos más abajo— y su teoría de existencia descansa en las [[Raices Caracteristicas y Funciones Propias| raíces características]].

---

## Ejemplo

> [!ejemplo] Una Fredholm de 2ª especie resuelta de principio a fin
> Resolvamos
> $$\varphi(x)=f(x)+\lambda\int_{0}^{1} x\,t\,\varphi(t)\,dt.$$
> El núcleo $K(x,t)=x\,t$ es **degenerado** (un solo término): toda la dependencia en $x$ sale fuera de la integral.
>
> **Paso 1 — saca $x$ de la integral.** Como $K=x\cdot t$,
> $$\int_0^1 x\,t\,\varphi(t)\,dt = x\underbrace{\int_0^1 t\,\varphi(t)\,dt}_{\displaystyle C},$$
> donde $C$ es una **constante** (un número, no depende de $x$). Entonces la solución tiene la forma
> $$\boxed{\varphi(x)=f(x)+\lambda\,C\,x.}$$
> Hallar $\varphi$ se reduce a hallar el número $C$.
>
> **Paso 2 — ecuación para $C$.** Multiplica la expresión de $\varphi$ por $t$ e integra en $[0,1]$, usando que por definición $C=\int_0^1 t\,\varphi(t)\,dt$:
> $$C=\int_0^1 t\big(f(t)+\lambda\,C\,t\big)\,dt=\int_0^1 t\,f(t)\,dt+\lambda\,C\int_0^1 t^2\,dt
> =\underbrace{\int_0^1 t\,f(t)\,dt}_{\displaystyle f_1}+\frac{\lambda}{3}\,C.$$
>
> **Paso 3 — despeja $C$.** Pasando el término en $C$ al lado izquierdo,
> $$\Big(1-\frac{\lambda}{3}\Big)\,C=f_1\quad\Longrightarrow\quad C=\frac{f_1}{\,1-\lambda/3\,}=\frac{\displaystyle\int_0^1 t\,f(t)\,dt}{\,1-\lambda/3\,}.$$
>
> **Paso 4 — solución.** Sustituyendo de vuelta,
> $$\boxed{\varphi(x)=f(x)+\frac{\lambda\,x}{\,1-\lambda/3\,}\int_0^1 t\,f(t)\,dt.}$$
> Es **única** y válida para **todo** $\lambda\neq 3$.
>
> **El caso $\lambda=3$.** El denominador $1-\lambda/3$ se anula: $\lambda=3$ es la **raíz característica** del núcleo. Ahí la fórmula deja de valer y la ecuación entra en la [[Alternativa de Fredholm| alternativa de Fredholm]]: si $f_1=\int_0^1 t\,f(t)\,dt\neq0$ **no hay solución**; si $f_1=0$ hay **infinitas** (la constante $C$ queda libre, y $\varphi=f+3Cx$ resuelve para cualquier $C$). La función propia asociada es $\varphi_1(x)=x$.

---

## En qué consiste

> [!teoria] Fredholm como sistema lineal de dimensión infinita
> Escrita $(\mathbb{I}-\lambda K)\varphi=f$, la ecuación es **idéntica** en estructura a un sistema lineal: $K$ es el "operador-matriz", $\varphi$ y $f$ son "vectores" (funciones). Por eso valen los mismos reflejos que en álgebra lineal:
> - Si $\mathbb{I}-\lambda K$ es **invertible** (lo es cuando $\lambda$ no es raíz característica), la solución es única: $\varphi=(\mathbb{I}-\lambda K)^{-1}f$. Ese inverso se materializa en la **resolvente** $\Gamma(x,t;\lambda)$, con $\varphi=f+\lambda\int_a^b\Gamma(x,t;\lambda)f(t)\,dt$.
> - Si $\lambda$ **es** raíz característica ($\mathbb{I}-\lambda K$ singular), o no hay solución o hay infinitas: la [[Alternativa de Fredholm| alternativa]].

> [!algoritmo] Cómo abordar una Fredholm de 2ª especie según el núcleo
> 1. **¿El núcleo es degenerado** $K=\sum_i a_i(x)b_i(t)$**?** Reduce la ecuación a un [[Nucleo Degenerado| sistema lineal finito]] $m\times m$ y resuélvelo (como en el ejemplo). Es la vía más directa.
> 2. **¿Núcleo general?** Usa los [[Determinantes de Fredholm| determinantes de Fredholm]] (válidos para todo $\lambda$) o la serie de Neumann de los [[Nucleos Iterados y Resolvente| núcleos iterados]] (válida si $\lvert\lambda\rvert$ es pequeño).
> 3. **¿Núcleo simétrico** $K(x,t)=K(t,x)$**?** Aplica la teoría de [[Nucleos Simetricos/index| Hilbert-Schmidt]]: desarrolla $f$ y $\varphi$ en la base ortonormal de funciones propias —una verdadera **diagonalización**.
> 4. **Comprueba $\lambda$ frente al espectro.** Si $\lambda$ coincide con una [[Raices Caracteristicas y Funciones Propias| raíz característica]], pasa a la [[Alternativa de Fredholm| alternativa de Fredholm]].

> [!info] La analogía matricial, en concreto
> Discretiza la integral con una cuadratura de $n$ nodos: $\int_a^b K(x,t)\varphi(t)\,dt\approx\sum_j w_j K(x_i,t_j)\varphi(t_j)$. La ecuación se vuelve **exactamente** el sistema lineal
> $$(\mathsf{I}-\lambda\mathsf{A})\,\mathbf{x}=\mathbf{f},\qquad \mathsf{A}_{ij}=w_j\,K(x_i,t_j),\quad x_i=\varphi(x_i),\quad f_i=f(x_i).$$
> Resoluble de forma única salvo cuando $\det(\mathsf{I}-\lambda\mathsf{A})=0$, es decir, cuando $1/\lambda$ es autovalor de $\mathsf{A}$. Esos $\lambda$ son la versión discreta de las raíces características. Toda la teoría de Fredholm es esta analogía llevada al límite continuo.

> [!warning]
> No confundas con la **primera especie** $f(x)=\lambda\int_a^b K(x,t)\varphi(t)\,dt$, donde la incógnita aparece **solo** dentro de la integral: es un problema **mal planteado** (sin el término $\varphi(x)$ libre que estabiliza). Aquí, en segunda especie, ese término exterior es justamente lo que da buen comportamiento.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Forma | $\varphi(x)=f(x)+\lambda\int_a^b K(x,t)\varphi(t)\,dt$, es decir $(\mathbb{I}-\lambda K)\varphi=f$ |
> | Incógnita / datos | $\varphi$ incógnita; $K,f,\lambda$ dados |
> | Solución única | si $\lambda$ **no** es raíz característica del núcleo |
> | Si $\lambda$ es raíz | [[Alternativa de Fredholm\|alternativa]]: sin solución o con infinitas |
> | Núcleo degenerado | [[Nucleo Degenerado\|sistema lineal finito]] |
> | Núcleo general | [[Determinantes de Fredholm\|determinantes]] / [[Nucleos Iterados y Resolvente\|resolvente]] |
> | Núcleo simétrico | [[Nucleos Simetricos/index\|Hilbert-Schmidt]] |

> [!corolario]
> Una Fredholm de 2ª especie es álgebra lineal en dimensión infinita: $(\mathbb{I}-\lambda K)\varphi=f$. Resolverla es invertir $\mathbb{I}-\lambda K$, y eso solo falla cuando $\lambda$ cae en el espectro del núcleo. La elección del método (degenerado, resolvente, simétrico) la dicta la **forma** del núcleo, no la dificultad aparente del problema.

> [!referencia]
> - El método más operativo: [[Nucleo Degenerado]].
> - Cuándo falla la unicidad: [[Alternativa de Fredholm]].
> - La resolvente como serie: [[Nucleos Iterados y Resolvente]].
> - Panorama general: [[Fredholm/index]].
