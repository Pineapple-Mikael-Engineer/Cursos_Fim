---
title: Determinantes de Fredholm
order: 4
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - fredholm
  - resolvente
draft: false
aliases:
  - determinantes de Fredholm
  - determinante de Fredholm
  - menor de Fredholm
  - Fredholm determinants
---

# Determinantes de Fredholm

> [!definicion]
> Para un núcleo **general** (no necesariamente degenerado), Fredholm construyó la [[Nucleos Iterados y Resolvente| resolvente]] como un **cociente de dos series enteras** en $\lambda$:
> $$\Gamma(x,t;\lambda)=\frac{D(x,t;\lambda)}{D(\lambda)},$$
> donde $D(\lambda)$ es el **determinante de Fredholm** y $D(x,t;\lambda)$ su **menor** (primer menor). La solución de [[Fredholm Segunda Especie| Fredholm de 2ª especie]] es entonces
> $$\varphi(x)=f(x)+\lambda\int_a^b \Gamma(x,t;\lambda)\,f(t)\,dt.$$
> La gran virtud: estas series convergen para **todo** $\lambda$, no solo para $\lambda$ pequeño.

> [!info]
> El método "global" de [[Fredholm/index| Fredholm]] dentro del [[3 Ecuaciones Integrales/index| capítulo de ecuaciones integrales]]. Generaliza la fórmula de Cramer (cociente de determinantes) a dimensión infinita: $D(\lambda)$ hace de $\det(\mathsf{I}-\lambda \mathsf{A})$ y sus **ceros** son las [[Raices Caracteristicas y Funciones Propias| raíces características]] del núcleo. A diferencia de la serie de Neumann de los [[Nucleos Iterados y Resolvente| núcleos iterados]], vale en todo el plano $\lambda$.

---

## Ejemplo

> [!ejemplo] $D(\lambda)$ a primer orden y el caso degenerado
> Tomemos el núcleo degenerado $K(x,t)=x\,t$ en $[0,1]$ (el de [[Fredholm Segunda Especie| Fredholm de 2ª especie]]). Calculemos $D(\lambda)$ con la serie y veamos que reproduce $\det(\mathsf{I}-\lambda\mathsf{A})$.
>
> **Término $n=0$.** Por convenio $D(\lambda)=1-\lambda\,c_1+\cdots$; el primero vale $1$.
>
> **Término $n=1$.** El coeficiente es la **traza** del núcleo:
> $$c_1=\int_0^1 K(s,s)\,ds=\int_0^1 s^2\,ds=\frac{1}{3}.$$
>
> **Término $n=2$.** Requiere el determinante $2\times2$ del núcleo evaluado en dos puntos:
> $$\det\begin{pmatrix}K(s_1,s_1)&K(s_1,s_2)\\ K(s_2,s_1)&K(s_2,s_2)\end{pmatrix}
> =\det\begin{pmatrix}s_1^2&s_1s_2\\ s_2s_1&s_2^2\end{pmatrix}=s_1^2 s_2^2-s_1^2 s_2^2=0.$$
> Se anula porque el núcleo tiene **rango 1**: cualquier menor $2\times2$ es cero. Lo mismo ocurre con todos los términos $n\ge2$.
>
> **Resultado.** La serie se **trunca**:
> $$\boxed{D(\lambda)=1-\frac{\lambda}{3}.}$$
> Su único cero es $\lambda=3$, exactamente la raíz característica hallada en [[Fredholm Segunda Especie| la nota de 2ª especie]] (donde el denominador era $1-\lambda/3$). Para un núcleo degenerado, $D(\lambda)$ es el **polinomio** $\det(\mathsf{I}-\lambda\mathsf{A})$.

---

## En qué consiste

> [!teoria] Las series de Fredholm
> El determinante de Fredholm y su menor son las series enteras
> $$D(\lambda)=\sum_{n=0}^{\infty}\frac{(-\lambda)^n}{n!}\int_a^b\!\!\cdots\!\!\int_a^b
> \det\big[K(s_i,s_j)\big]_{i,j=1}^{n}\;ds_1\cdots ds_n,$$
> $$D(x,t;\lambda)=\sum_{n=0}^{\infty}\frac{(-\lambda)^n}{n!}\int_a^b\!\!\cdots\!\!\int_a^b
> \det\begin{pmatrix}K(x,t)&K(x,s_1)&\cdots&K(x,s_n)\\ K(s_1,t)&K(s_1,s_1)&\cdots&K(s_1,s_n)\\ \vdots&&\ddots&\vdots\\ K(s_n,t)&K(s_n,s_1)&\cdots&K(s_n,s_n)\end{pmatrix}ds_1\cdots ds_n.$$
> El término $n=0$ de $D(\lambda)$ es $1$; el $n=1$ es $-\lambda\int_a^b K(s,s)\,ds$ (la **traza**). Para un núcleo continuo y acotado en $[a,b]$, **ambas series son funciones enteras de $\lambda$** (los determinantes de Hadamard hacen que los coeficientes decaigan más rápido que cualquier geométrica), de modo que convergen para **todo** $\lambda$.

> [!teorema] Las raíces características son los ceros de $D(\lambda)$
> Los valores de $\lambda$ para los que la ecuación deja de tener solución única —las **raíces características** del núcleo— son exactamente los **ceros** de la función entera $D(\lambda)$. En ellos, $\Gamma=D(x,t;\lambda)/D(\lambda)$ tiene un polo y aplica la [[Alternativa de Fredholm| alternativa de Fredholm]]. Por ser $D$ entera, esos ceros son **aislados** y, salvo $D\equiv0$, forman un conjunto **discreto** sin punto de acumulación finito.

> [!proposicion] Ventaja sobre la serie de Neumann
> La serie de Neumann (núcleos iterados) $\Gamma=\sum_{k\ge0}\lambda^k K_{k+1}$ solo converge para $\lvert\lambda\rvert<1/\lVert K\rVert$: ve únicamente la primera raíz característica como radio de convergencia. El cociente de Fredholm, en cambio, es la **continuación analítica** de esa serie a todo el plano: $D(\lambda)$ y $D(x,t;\lambda)$ no tienen singularidades, y los polos de $\Gamma$ aparecen solo donde $D(\lambda)=0$. Por eso los determinantes capturan **todo** el espectro.

> [!warning]
> Las series son **laboriosas**: cada término pide integrar un determinante $n\times n$ sobre un cubo $n$-dimensional. En la práctica casi nunca se suman a mano; se prefiere reducir a un [[Nucleo Degenerado| núcleo degenerado]] (donde $D$ es un polinomio) o usar la [[Nucleos Iterados y Resolvente| resolvente]] vía Neumann cuando $\lambda$ es pequeño. El valor de los determinantes es sobre todo **teórico**: prueban que el espectro es discreto y que la resolvente es meromorfa en $\lambda$.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Resolvente | $\Gamma(x,t;\lambda)=D(x,t;\lambda)/D(\lambda)$ |
> | Solución | $\varphi=f+\lambda\int_a^b \Gamma\,f\,dt$ |
> | $D(\lambda)$ | serie entera; $n{=}0\!:1$, $n{=}1\!:-\lambda\int K(s,s)ds$ (traza) |
> | Validez | **todo** $\lambda$ (a diferencia de Neumann) |
> | Raíces características | **ceros** de $D(\lambda)$ |
> | Núcleo degenerado | $D(\lambda)=\det(\mathsf{I}-\lambda\mathsf{A})$, un **polinomio** |

> [!corolario]
> Los determinantes de Fredholm son la fórmula de Cramer en dimensión infinita: la resolvente es un cociente de dos funciones enteras, $D(x,t;\lambda)/D(\lambda)$, válido en todo el plano $\lambda$. Su mensaje estructural —el espectro del núcleo es el conjunto **discreto** de ceros de una función entera— es lo que sostiene la [[Alternativa de Fredholm| alternativa de Fredholm]] y toda la teoría espectral de [[Fredholm/index| Fredholm]].

> [!referencia]
> - La serie de Neumann y la resolvente: [[Nucleos Iterados y Resolvente]].
> - El caso polinómico: [[Nucleo Degenerado]].
> - La ecuación de partida: [[Fredholm Segunda Especie]].
> - Panorama general: [[Fredholm/index]].
