---
title: Aproximaciones Sucesivas Numéricas
order: 2
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - metodos-aproximados
  - aproximaciones-sucesivas
draft: false
aliases:
  - aproximaciones sucesivas numéricas
  - iteración numérica de Neumann
  - numerical successive approximations
  - iterated numerical resolvent
---

# Aproximaciones Sucesivas Numéricas

> [!definicion]
> El método **itera numéricamente** la ecuación de Fredholm de 2ª especie,
> $$\varphi_{n+1}(x)=f(x)+\lambda\int_a^b K(x,t)\,\varphi_n(t)\,dt,\qquad \varphi_0=f,$$
> evaluando en cada paso la integral con una **cuadratura** (regla de trapecios, Simpson, etc.). La sucesión converge a la solución exacta si
> $$\lvert\lambda\rvert\,\lVert K\rVert<1,$$
> y entonces el límite coincide con la suma de la **serie de Neumann** truncada paso a paso. Es la versión computable de la resolvente: en vez de sumar la serie analíticamente, se la **acumula numéricamente**.

> [!info]
> Es la cara numérica de la [[Aproximaciones Sucesivas| iteración de punto fijo de Volterra]] aplicada a [[Fredholm Segunda Especie| Fredholm]], dentro de [[Metodos Aproximados/index| Métodos Aproximados]] del [[3 Ecuaciones Integrales/index| capítulo de ecuaciones integrales]]. A diferencia de la [[Sustitucion Nucleo Degenerado| sustitución por núcleo degenerado]] (que resuelve un sistema de una vez), aquí no se resuelve ningún sistema: solo se **evalúan integrales repetidamente**, lo que la hace trivial de programar pero limitada a $\lvert\lambda\rvert$ pequeño.

---

## Ejemplo

> [!ejemplo] Iteración de una Fredholm sencilla
> Resolvamos por iteración
> $$\varphi(x)=x+\tfrac12\int_0^1 x\,t\,\varphi(t)\,dt,$$
> es decir $f(x)=x$, $K(x,t)=xt$, $\lambda=\tfrac12$. (Tiene solución cerrada, lo que nos deja comprobar la convergencia.)
>
> **Paso 1 — primera iteración.** Con $\varphi_0=x$,
> $$\varphi_1(x)=x+\tfrac12\int_0^1 x t\cdot t\,dt=x+\tfrac12 x\int_0^1 t^2 dt=x+\tfrac12 x\cdot\tfrac13=x\big(1+\tfrac16\big)=\tfrac76 x.$$
>
> **Paso 2 — segunda iteración.** Con $\varphi_1=\tfrac76 x$,
> $$\varphi_2(x)=x+\tfrac12\int_0^1 x t\cdot\tfrac76 t\,dt=x+\tfrac12\cdot\tfrac76 x\cdot\tfrac13=x\big(1+\tfrac{7}{36}\big)=\tfrac{43}{36}x\approx 1.194\,x.$$
>
> **Paso 3 — tercera iteración.** Con $\varphi_2=\tfrac{43}{36}x$,
> $$\varphi_3(x)=x+\tfrac12\cdot\tfrac{43}{36}x\cdot\tfrac13=x\big(1+\tfrac{43}{216}\big)=\tfrac{259}{216}x\approx 1.199\,x.$$
>
> **Paso 4 — el límite.** Los coeficientes $1,\ \tfrac76,\ \tfrac{43}{36},\ \tfrac{259}{216},\dots$ son sumas parciales de la **serie geométrica** $\sum_{n\ge 0}\big(\tfrac{1}{6}\big)^n=\dfrac{1}{1-1/6}=\dfrac65=1.2$. En efecto, $\varphi=cx$ exige $cx=x+\tfrac12 x\cdot c\cdot\tfrac13$, o sea $c=1+\tfrac{c}{6}$, luego $c=\tfrac65$. La sucesión converge a $\boxed{\varphi(x)=\tfrac65 x}$, y ya en $\varphi_3$ el error es $\lvert 1.199-1.2\rvert<10^{-3}$.
>
> **Cuadratura.** Aquí las integrales salieron exactas; con un $K$ general se reemplaza cada $\int_0^1(\cdots)dt$ por $\sum_j w_j(\cdots)\big|_{t=t_j}$ (trapecios/Simpson) y se itera igual, ahora sobre los valores nodales $\varphi_n(t_j)$.

---

## En qué consiste

> [!teoria]
> La recurrencia $\varphi_{n+1}=f+\lambda\,\mathcal{K}\varphi_n$ es una **iteración de punto fijo** del operador $T\varphi=f+\lambda\mathcal{K}\varphi$. Desplegándola desde $\varphi_0=f$,
> $$\varphi_n=f+\lambda\mathcal{K}f+\lambda^2\mathcal{K}^2 f+\dots+\lambda^n\mathcal{K}^n f,$$
> que es exactamente la **suma parcial $n$-ésima de la serie de Neumann**. Iterar numéricamente equivale, pues, a **acumular término a término** la resolvente, sin tener que calcular los [[Nucleos Iterados y Resolvente| núcleos iterados]] en forma cerrada: cada paso aplica una sola integral.

> [!algoritmo] Aproximaciones sucesivas numéricas
> 1. **Inicializa** $\varphi_0=f$ y fija una cuadratura $\int_a^b g\approx\sum_j w_j\,g(t_j)$.
> 2. **Itera** $\varphi_{n+1}(x_i)=f(x_i)+\lambda\sum_j w_j\,K(x_i,t_j)\,\varphi_n(t_j)$ en los nodos.
> 3. **Detente** cuando $\lVert\varphi_{n+1}-\varphi_n\rVert<\text{tol}$.
> 4. **Verifica** $\lvert\lambda\rvert\,\lVert K\rVert<1$ antes de empezar: si no se cumple, no converge.

> [!teorema] Cota de error geométrica
> Si $q:=\lvert\lambda\rvert\,\lVert K\rVert<1$, la iteración converge y el error tras $n$ pasos está acotado por la cola geométrica
> $$\lVert\varphi-\varphi_n\rVert\le\frac{q^{\,n+1}}{1-q}\,\lVert f\rVert.$$
> En particular, el número de iteraciones para una tolerancia $\varepsilon$ crece como $\log\varepsilon/\log q$.

> [!demostracion]
> **Paso 1 — contracción.** Para dos funciones $u,v$, $\lVert T u-T v\rVert=\lvert\lambda\rvert\,\lVert\mathcal{K}(u-v)\rVert\le\lvert\lambda\rvert\,\lVert K\rVert\,\lVert u-v\rVert=q\,\lVert u-v\rVert$, con $q<1$: $T$ es una **contracción**.
>
> **Paso 2 — pasos sucesivos.** Aplicándolo a $u=\varphi_n,\ v=\varphi_{n-1}$, $\lVert\varphi_{n+1}-\varphi_n\rVert\le q\,\lVert\varphi_n-\varphi_{n-1}\rVert\le\dots\le q^{n}\lVert\varphi_1-\varphi_0\rVert$. Y como $\varphi_1-\varphi_0=\lambda\mathcal{K}f$, se tiene $\lVert\varphi_1-\varphi_0\rVert\le q\,\lVert f\rVert$, luego $\lVert\varphi_{n+1}-\varphi_n\rVert\le q^{\,n+1}\lVert f\rVert$.
>
> **Paso 3 — suma de la cola.** Por la desigualdad triangular sobre los pasos restantes,
> $$\lVert\varphi-\varphi_n\rVert\le\sum_{k\ge n}\lVert\varphi_{k+1}-\varphi_k\rVert\le\sum_{k\ge n}q^{\,k+1}\lVert f\rVert=\frac{q^{\,n+1}}{1-q}\,\lVert f\rVert.$$
> Como $q<1$, el límite existe y es el único punto fijo $\varphi=T\varphi$, la solución de la ecuación. $\blacksquare$

> [!warning]
> El método **solo converge para $\lvert\lambda\rvert$ pequeño** (concretamente $\lvert\lambda\rvert<1/\lVert K\rVert$): pasada esa frontera la serie de Neumann diverge y la iteración se dispara. Esto contrasta con la [[Aproximaciones Sucesivas| iteración de Volterra]], que **converge siempre** (para todo $\lambda$), porque el núcleo iterado de Volterra lleva un factor $\frac{(x-t)^{n}}{n!}$ que mata el crecimiento. En Fredholm no hay tal factorial salvador. Para $\lambda$ grande hay que recurrir a la [[Sustitucion Nucleo Degenerado| sustitución por núcleo degenerado]] o a la [[Cuadratura y Nystrom| cuadratura de Nyström]], que resuelven un sistema y no dependen de la convergencia de una serie.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Iteración | $\varphi_{n+1}=f+\lambda\int K\varphi_n$, $\varphi_0=f$ |
> | Integral | evaluada por cuadratura en cada paso |
> | Equivale a | sumar la serie de Neumann término a término |
> | Converge si | $q=\lvert\lambda\rvert\,\lVert K\rVert<1$ |
> | Error | $\lVert\varphi-\varphi_n\rVert\le\dfrac{q^{\,n+1}}{1-q}\lVert f\rVert$ (geométrico) |
> | Limitación | solo $\lvert\lambda\rvert$ pequeño (Volterra no la tiene) |

> [!corolario]
> Es el método **más simple de programar** —un bucle de integraciones— y el más transparente: cada iteración es un término más de la resolvente. Su precio es la restricción $\lvert\lambda\rvert<1/\lVert K\rVert$; dentro de ella la convergencia es geométrica y rapidísima.

> [!referencia]
> - La versión que converge siempre (Volterra): [[Aproximaciones Sucesivas]].
> - Cuando $\lambda$ es grande, resolver un sistema: [[Sustitucion Nucleo Degenerado]].
> - Panorama de la sección: [[Metodos Aproximados/index]].
