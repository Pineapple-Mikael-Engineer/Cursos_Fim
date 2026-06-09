---
title: Raíces Características Aproximadas
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - metodos-aproximados
  - autovalores
draft: false
aliases:
  - raíces características aproximadas
  - estimación de autovalores
  - método de Ritz
  - método de las trazas
  - método de Kellog
  - approximate characteristic values
---

# Raíces Características Aproximadas

> [!definicion]
> Reúne los métodos para **estimar las raíces características** —los autovalores asociados al núcleo, ver
> [[Raices Caracteristicas y Funciones Propias| raíces características y funciones propias]]— **sin
> resolver** la ecuación de autovalores exactamente. Tres clásicos, según qué se quiera y qué estructura
> tenga el núcleo:
> - **Ritz** (variacional, núcleo simétrico): obtiene la **primera** raíz como extremo de un cociente.
> - **Trazas** (método de las trazas): de las **trazas de los núcleos iterados** estima las **menores**
>   raíces en conjunto.
> - **Kellog** (iteración de potencias): itera el operador para capturar la raíz **dominante** y su
>   función propia.

> [!info]
> Son los **análogos continuos** de las técnicas del [[Sistemas Lineales Autovalores| álgebra lineal]]:
> Ritz es el cociente de Rayleigh y el método de Rayleigh–Ritz; trazas es "$\sum$ de autovalores $=$
> traza"; Kellog es la iteración de potencias (*power iteration*). Cierran la sección de
> [[Metodos Aproximados/index| métodos aproximados]] del [[3 Ecuaciones Integrales/index| capítulo]]:
> en vez de aproximar la **solución** $\varphi$ de una ecuación con segundo miembro, aproximan el
> **espectro** del operador, que rige la [[Alternativa de Fredholm| alternativa de Fredholm]] y la
> [[Teoria de Hilbert-Schmidt| teoría de Hilbert–Schmidt]].

---

## Ejemplo

> [!ejemplo] Método de las trazas en un núcleo degenerado simétrico
> Tomemos el núcleo simétrico, separable y de rango $2$,
> $$K(x,t)=\cos x\cos t+2\sin x\sin t,\qquad x,t\in[0,2\pi],$$
> y estimemos sus raíces características con las **trazas**. Para un núcleo simétrico, las raíces
> características $\lambda_n$ y sus inversos $\mu_n=1/\lambda_n$ (los **autovalores del operador**)
> satisfacen
> $$\operatorname{tr}K_p=\int_a^b K_p(x,x)\,dx=\sum_n \mu_n^{\,p}=\sum_n\frac{1}{\lambda_n^{\,p}}.$$
>
> **Paso 1 — primera traza.** $K_1=K$, así que $\operatorname{tr}K_1=\int_0^{2\pi}K(x,x)\,dx$ con
> $K(x,x)=\cos^2x+2\sin^2x=1+\sin^2x$. Como $\int_0^{2\pi}1\,dx=2\pi$ y
> $\int_0^{2\pi}\sin^2x\,dx=\pi$,
> $$\operatorname{tr}K_1=2\pi+\pi=3\pi=\mu_1+\mu_2.$$
>
> **Paso 2 — segunda traza.** Aquí conviene reconocer la estructura: con base ortogonal
> $\{\cos x,\sin x\}$ (cada una de norma$^2$ $\int_0^{2\pi}\cos^2=\pi$), el operador actúa como
> $\mu=\pi\cdot(\text{coeficiente})$. Sobre $\cos x$: $K$ devuelve $\cos x\cdot\pi$, autovalor
> $\mu_1=\pi$. Sobre $\sin x$: devuelve $2\sin x\cdot\pi$, autovalor $\mu_2=2\pi$. Comprobamos con la
> traza: $\mu_1+\mu_2=\pi+2\pi=3\pi$ ✓, coincide con el Paso 1.
>
> **Paso 3 — segunda traza como control.**
> $\operatorname{tr}K_2=\mu_1^2+\mu_2^2=\pi^2+4\pi^2=5\pi^2$. Si solo conociéramos $\operatorname{tr}K_1=3\pi$
> y $\operatorname{tr}K_2=5\pi^2$, despejaríamos los dos autovalores resolviendo
> $\mu_1+\mu_2=3\pi$, $\mu_1^2+\mu_2^2=5\pi^2$, de donde $\mu_1\mu_2=\tfrac{(3\pi)^2-5\pi^2}{2}=2\pi^2$ y
> $\mu$ son raíces de $z^2-3\pi z+2\pi^2=0$, es decir $z=\pi,2\pi$.
>
> **Paso 4 — raíces características.** Invirtiendo, $\lambda_n=1/\mu_n$:
> $$\boxed{\lambda_1=\frac{1}{2\pi}\approx0.159\ \text{(la menor en módulo)},\qquad \lambda_2=\frac{1}{\pi}\approx0.318.}$$
> Con las **dos primeras trazas** hemos recuperado **exactamente** las dos raíces (porque el rango es
> $2$). Para un núcleo de rango infinito, las primeras trazas dan las **menores** $\lambda_n$ con buena
> precisión, pues las trazas $\sum\mu_n^p$ están dominadas por los $\mu_n$ mayores —los $\lambda_n$
> menores—.

---

## En qué consiste

> [!teoria] Ritz — el cociente de Rayleigh
> Para un núcleo **simétrico** (operador autoadjunto), la mayor escala del operador se lee en el
> **cociente de Rayleigh**
> $$R[\varphi]=\frac{\langle K\varphi,\varphi\rangle}{\langle\varphi,\varphi\rangle}=\frac{\displaystyle\int\!\!\int K(x,t)\varphi(x)\varphi(t)\,dx\,dt}{\displaystyle\int\varphi(x)^2\,dx}.$$
> Su **máximo** sobre todas las $\varphi$ es el mayor autovalor $\mu_1=\max_\varphi R[\varphi]$, esto es
> $$\lambda_1^{-1}=\max_{\varphi}\frac{\langle K\varphi,\varphi\rangle}{\langle\varphi,\varphi\rangle},$$
> la **raíz característica de menor módulo** $\lambda_1$. El **método de Ritz** consiste en no maximizar
> sobre todo el espacio, sino sobre un **subespacio** $\varphi=\sum_i c_i\phi_i$: el máximo del cociente
> ahí da una **cota** del autovalor extremo (y, refinando el subespacio, converge). En la práctica se
> reduce a un problema de autovalores **generalizado** $\mathsf{K}\mathbf{c}=\mu\,\mathsf{M}\mathbf{c}$
> con $\mathsf{K}_{ij}=\langle K\phi_i,\phi_j\rangle$ y $\mathsf{M}_{ij}=\langle\phi_i,\phi_j\rangle$.

> [!teoria] Trazas — sumas de potencias del espectro
> Los [[Nucleos Iterados y Resolvente| núcleos iterados]] $K_p$ tienen por traza la **suma de las
> potencias** de los autovalores:
> $$\operatorname{tr}K_p=\int_a^b K_p(x,x)\,dx=\sum_n\frac{1}{\lambda_n^{\,p}},\qquad K_p(x,t)=\int K(x,s)K_{p-1}(s,t)\,ds.$$
> Calculando $\operatorname{tr}K_1,\operatorname{tr}K_2,\dots$ se tienen las **sumas de potencias**
> $S_p=\sum_n\mu_n^p$; por las identidades de Newton se reconstruyen los primeros $\mu_n$ (los mayores, o
> sea los $\lambda_n$ menores). Es el método más directo para una **estimación global** de las primeras
> raíces.

> [!teorema] Kellog — iteración de potencias
> Sea $K$ simétrico con autovalor dominante $\mu_1=1/\lambda_1$ **simple** y $|\mu_1|>|\mu_2|\ge\cdots$.
> Partiendo de cualquier $\psi_0$ no ortogonal a la función propia dominante, la iteración
> $$\psi_{k+1}=K\psi_k=\int_a^b K(x,t)\,\psi_k(t)\,dt$$
> converge (tras normalizar) a la **función propia dominante** $\varphi_1$, y el cociente de normas
> $$\frac{\lVert\psi_{k+1}\rVert}{\lVert\psi_k\rVert}\;\xrightarrow[k\to\infty]{}\;\mu_1=\frac{1}{\lambda_1},$$
> con lo que $\lambda_1$ —la raíz característica de **menor módulo**— se obtiene como límite del inverso.

> [!demostracion]
> **Paso 1 — desarrolla en la base propia.** Como $K$ es simétrico, sus funciones propias
> $\{\varphi_n\}$ forman base ortonormal y $K\varphi_n=\mu_n\varphi_n$. Escribe
> $\psi_0=\sum_n a_n\varphi_n$ con $a_1\neq0$ (la hipótesis de no ortogonalidad).
>
> **Paso 2 — aplica el operador $k$ veces.** Por linealidad y $K\varphi_n=\mu_n\varphi_n$,
> $$\psi_k=K^k\psi_0=\sum_n a_n\,\mu_n^{\,k}\,\varphi_n=\mu_1^{\,k}\Big(a_1\varphi_1+\sum_{n\ge2}a_n\Big(\tfrac{\mu_n}{\mu_1}\Big)^{\!k}\varphi_n\Big).$$
>
> **Paso 3 — domina el primer término.** Como $|\mu_n/\mu_1|<1$ para $n\ge2$, las potencias
> $(\mu_n/\mu_1)^k\to0$: el corchete tiende a $a_1\varphi_1$. Por tanto $\psi_k/\mu_1^k\to a_1\varphi_1$,
> y normalizando, $\psi_k/\lVert\psi_k\rVert\to\pm\varphi_1$.
>
> **Paso 4 — el cociente de normas da $\mu_1$.** Usando la ortonormalidad,
> $\lVert\psi_k\rVert^2=\sum_n a_n^2\mu_n^{2k}=\mu_1^{2k}\big(a_1^2+o(1)\big)$, de modo que
> $$\frac{\lVert\psi_{k+1}\rVert}{\lVert\psi_k\rVert}=\frac{|\mu_1|^{k+1}\sqrt{a_1^2+o(1)}}{|\mu_1|^{k}\sqrt{a_1^2+o(1)}}\;\longrightarrow\;|\mu_1|=\frac{1}{|\lambda_1|}.$$
> La convergencia es **geométrica** de razón $|\mu_2/\mu_1|$: cuanto más separado esté el autovalor
> dominante, más rápido. $\blacksquare$

> [!info] Análogos del álgebra lineal
> Las tres técnicas son los métodos matriciales clásicos trasladados al operador integral: **Ritz** es
> Rayleigh–Ritz (cota variacional del espectro), **trazas** es "$\operatorname{tr}A^p=\sum\mu_n^p$" con
> identidades de Newton, y **Kellog** es la **iteración de potencias** del
> [[Sistemas Lineales Autovalores| álgebra lineal]]. La diferencia es que aquí $K$ es un operador de
> dimensión infinita y las "matrices" son integrales —pero la mecánica espectral es idéntica—.

> [!warning]
> Ritz y Kellog en su forma básica solo dan la raíz **extrema** (la dominante / menor en módulo). Para
> las **siguientes** raíces hay que **deflactar** (restar la componente ya hallada: $\psi\to\psi-\langle\psi,\varphi_1\rangle\varphi_1$)
> o ampliar el subespacio de Ritz. El método de trazas, en cambio, captura **varias** a la vez, pero
> pierde precisión en las raíces grandes (las $\mu_n$ pequeñas) porque apenas contribuyen a las trazas.

## Resumen

> [!resumen]
> | Método | Qué estima | Idea | Requiere |
> |---|---|---|---|
> | Ritz | raíz extrema (cota) | max del cociente de Rayleigh en subespacio | núcleo simétrico |
> | Trazas | las menores $\lambda_n$ | $\operatorname{tr}K_p=\sum 1/\lambda_n^{\,p}$ + Newton | núcleos iterados |
> | Kellog | raíz dominante + función propia | iterar $\psi_{k+1}=K\psi_k$, $\lVert\psi_{k+1}\rVert/\lVert\psi_k\rVert\to1/\lambda_1$ | gap espectral |

> [!corolario]
> Estimar el espectro de un núcleo es hacer **álgebra lineal de operadores**: Rayleigh–Ritz acota,
> las trazas suman potencias y Newton las separa, y la iteración de potencias de Kellog persigue el
> modo dominante. Son la vía rápida a los autovalores cuando resolver la ecuación característica completa
> es inviable, y la base de los algoritmos numéricos para [[Nucleos Simetricos/index| núcleos simétricos]].

> [!referencia]
> - El objeto que se estima: [[Raices Caracteristicas y Funciones Propias]].
> - La proyección emparentada (Ritz ↔ Galerkin): [[Metodo de Bubnov-Galiorkin]].
> - Panorama de los métodos: [[Metodos Aproximados/index]].
