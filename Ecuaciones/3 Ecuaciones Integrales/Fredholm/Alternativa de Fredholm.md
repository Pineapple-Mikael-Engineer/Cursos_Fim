---
title: Alternativa de Fredholm
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - fredholm
  - existencia
draft: false
aliases:
  - alternativa de Fredholm
  - teoremas de Fredholm
  - dicotomía de Fredholm
  - Fredholm alternative
  - solvability condition
---

# Alternativa de Fredholm

> [!definicion]
> La **alternativa de Fredholm** es la dicotomía que gobierna la ecuación $(\mathbb{I}-\lambda K)\varphi=f$,
> es decir $\varphi(x)=f(x)+\lambda\int_a^b K(x,t)\varphi(t)\,dt$. **O bien** $\lambda$ **no** es una raíz
> característica del núcleo y entonces la ecuación tiene **solución única** para todo $f$; **o bien**
> $\lambda$ **es** una raíz característica, y entonces la ecuación tiene solución **solo si** $f$ es
> **ortogonal** a todas las funciones propias $\psi$ del núcleo **adjunto** $K^{*}(x,t)=K(t,x)$,
> $$\int_a^b f(x)\,\psi(x)\,dx=0,$$
> en cuyo caso hay **infinitas** soluciones (una solución particular más cualquier combinación de las
> funciones propias).

> [!info]
> Es el **teorema de existencia** de [[Fredholm Segunda Especie| Fredholm de 2ª especie]], el desenlace
> de toda la teoría espectral del [[Fredholm/index| bloque de Fredholm]]. Decide, según dónde caiga
> $\lambda$ respecto a las [[Raices Caracteristicas y Funciones Propias| raíces características]], si hay
> una, ninguna o infinitas soluciones. Es la traducción **literal** a dimensión infinita del teorema de
> Rouché-Frobenius para sistemas lineales.

---

## Ejemplo

> [!ejemplo] Un núcleo degenerado en una raíz característica
> Tomemos $K(x,t)=\cos x\,\cos t$ en $[0,2\pi]$ y $\lambda=1/\pi$. La ecuación es
> $$\varphi(x)=f(x)+\frac{1}{\pi}\cos x\int_0^{2\pi}\cos t\,\varphi(t)\,dt.$$
> El núcleo es de rango $1$ y simétrico. La homogénea ($f=0$) tiene la función propia
> $\varphi_1(x)=\cos x$ con raíz característica $\lambda_1=1/\pi$, porque
> $\tfrac1\pi\cos x\int_0^{2\pi}\cos^2 t\,dt=\tfrac1\pi\cos x\cdot\pi=\cos x$. Estamos **exactamente** en
> $\lambda=\lambda_1$: la primera rama de la alternativa falla.
>
> **Un $f$ que NO da solución.** Sea $f(x)=\cos x$. Como el núcleo es simétrico, la condición es
> $f\perp\varphi_1$, pero
> $$\int_0^{2\pi}\cos x\,\cos x\,dx=\pi\neq 0.$$
> No se cumple la ortogonalidad, así que la ecuación **no tiene solución**: al proyectar sobre $\cos x$
> el lado izquierdo se anula y el derecho no.
>
> **Un $f$ que da infinitas.** Sea $f(x)=\operatorname{sen} x$. Ahora
> $$\int_0^{2\pi}\operatorname{sen} x\,\cos x\,dx=0,$$
> de modo que $f\perp\varphi_1$ y la ecuación **es compatible**. Una solución particular es
> $\varphi_p=\operatorname{sen} x$ (el término integral se anula porque $\int_0^{2\pi}\cos t\operatorname{sen} t\,dt=0$),
> y como $\varphi_1=\cos x$ resuelve la homogénea, **toda** $\varphi=\operatorname{sen} x+C\cos x$ con $C\in\mathbb{R}$
> sirve: hay **infinitas** soluciones.

---

## En qué consiste

> [!teoria]
> La alternativa de Fredholm es álgebra lineal mirada en un espacio de funciones. Para el sistema finito
> $(\mathsf{I}-\lambda\mathsf{A})\mathbf{x}=\mathbf{b}$ ocurre exactamente lo mismo: si la matriz
> $\mathsf{I}-\lambda\mathsf{A}$ es invertible (es decir $\lambda$ no es autovalor de $\mathsf{A}$) hay
> solución única; si es singular, el sistema es compatible **únicamente** cuando $\mathbf{b}$ es ortogonal
> al núcleo de la **traspuesta** $(\mathsf{I}-\lambda\mathsf{A})^{\!\top}$. El operador integral $K$ hace
> de matriz, su adjunto $K^{*}(x,t)=K(t,x)$ hace de traspuesta, y el producto escalar es la integral
> $\int_a^b f\psi\,dx$.

> [!teorema] Los teoremas de Fredholm
> Para la ecuación $\varphi=f+\lambda\int_a^b K\varphi\,dt$ y su homogénea adjunta
> $\psi=\lambda\int_a^b K^{*}\psi\,dt$ se cumple:
> 1. **(Primer teorema)** Si $\lambda$ no es raíz característica, la ecuación tiene **solución única**
>    para todo $f$.
> 2. **(Segundo teorema)** Las ecuaciones homogéneas $\varphi=\lambda K\varphi$ y $\psi=\lambda K^{*}\psi$
>    tienen el **mismo número finito** de soluciones independientes.
> 3. **(Tercer teorema)** Si $\lambda$ es raíz característica, la no homogénea tiene solución **si y solo
>    si** $\int_a^b f\,\psi_k\,dx=0$ para toda función propia $\psi_k$ del adjunto; entonces hay
>    **infinitas** soluciones.

> [!demostracion] Esquema vía la analogía del sistema lineal
> **Paso 1 — discretizar el operador.** Aproximamos $K$ por un [[Nucleo Degenerado| núcleo degenerado]]
> $K_m=\sum_{i=1}^{m}a_i(x)b_i(t)$. La ecuación se vuelve un sistema lineal **finito**
> $(\mathsf{I}-\lambda\mathsf{A})\mathbf{c}=\mathbf{d}$ para los coeficientes $\mathbf c$, con
> $\mathsf{A}_{ij}=\int_a^b b_i(t)a_j(t)\,dt$.
>
> **Paso 2 — aplicar Rouché-Frobenius.** Para el sistema finito ya es álgebra lineal: si
> $\det(\mathsf I-\lambda\mathsf A)\neq0$ hay solución única (rama 1). Si $\det=0$, el sistema es
> compatible **si y solo si** $\mathbf d\perp\ker(\mathsf I-\lambda\mathsf A)^{\!\top}$, y entonces hay
> infinitas soluciones (rama 2).
>
> **Paso 3 — traducir la condición.** El núcleo de la traspuesta $\ker(\mathsf I-\lambda\mathsf A)^{\!\top}$
> corresponde exactamente a las funciones propias del **núcleo adjunto** $K^{*}(x,t)=K(t,x)$. La condición
> $\mathbf d\perp\ker(\cdot)^{\!\top}$ se traduce en $\int_a^b f\,\psi\,dx=0$.
>
> **Paso 4 — pasar al límite.** Como el operador integral es **compacto**, la aproximación degenerada
> $K_m\to K$ preserva la dicotomía (teoría de Riesz-Schauder), y la alternativa vale para el núcleo
> general. $\blacksquare$

> [!proposicion]
> El segundo teorema garantiza que la "deficiencia" y el "exceso" se compensan: el número de condiciones
> de ortogonalidad sobre $f$ (dimensión del núcleo del adjunto) coincide con el número de funciones
> propias libres que se suman a la solución. Por eso, cuando hay solución, hay tantas como dimensión tenga
> el espacio propio.

> [!warning]
> No basta con que $\lambda$ sea raíz característica para que "no haya solución": **puede** haberla si $f$
> cumple las condiciones de ortogonalidad. Lo que se pierde en una raíz característica es la **unicidad**,
> no necesariamente la existencia.

## Resumen

> [!resumen]
> | Caso | Existencia | Unicidad |
> |---|---|---|
> | $\lambda$ **no** raíz característica | siempre, para todo $f$ | **única** |
> | $\lambda$ raíz característica, $f\perp\psi_k$ | sí | **infinitas** soluciones |
> | $\lambda$ raíz característica, $f\not\perp\psi_k$ | **no** hay solución | — |
> | Condición de compatibilidad | $\int_a^b f\,\psi_k\,dx=0$ ($\psi_k$ propias del adjunto) | |

> [!corolario]
> Para **núcleos simétricos** ($K(x,t)=K(t,x)$) el adjunto coincide con el propio núcleo, así que las
> funciones propias del adjunto son las mismas $\varphi_n$ del núcleo. La condición de compatibilidad se
> simplifica a $f\perp\varphi_n$: $f$ debe ser ortogonal a las funciones propias de la raíz característica
> $\lambda_n$. Es el caso natural de la teoría de [[Nucleos Simetricos/index| Hilbert-Schmidt]].

> [!referencia]
> - El espectro que dispara la alternativa: [[Raices Caracteristicas y Funciones Propias]].
> - El caso simétrico (adjunto = núcleo): [[Nucleos Simetricos/index]].
> - La ecuación a la que se aplica: [[Fredholm Segunda Especie]].
> - Vista de conjunto: [[Fredholm/index]].
