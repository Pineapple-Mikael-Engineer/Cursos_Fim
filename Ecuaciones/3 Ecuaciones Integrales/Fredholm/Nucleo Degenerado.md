---
title: Núcleo Degenerado
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - fredholm
  - nucleo-degenerado
draft: false
aliases:
  - núcleo degenerado
  - núcleo separable
  - degenerate kernel
  - separable kernel
---

# Núcleo Degenerado

> [!definicion]
> Un núcleo es **degenerado** (o **separable**) si se escribe como una **suma finita** de productos
> que separan las variables:
> $$K(x,t)=\sum_{i=1}^{m} a_i(x)\,b_i(t),$$
> con $\{a_i\}$ y $\{b_i\}$ funciones dadas (puede suponerse cada familia linealmente independiente; $m$
> es el **rango**). Para este núcleo, la ecuación de [[Fredholm Segunda Especie| Fredholm de 2ª especie]] se reduce a un **sistema lineal finito** $m\times m$: el problema continuo se vuelve, exacta
> y exactamente, álgebra lineal en dimensión finita.

> [!info]
> El método más directo de [[Fredholm/index| Fredholm]] y la puerta de entrada al
> [[3 Ecuaciones Integrales/index| capítulo de ecuaciones integrales]]. La idea —sacar de la integral
> todo lo que depende de $x$— hace explícita la analogía con un sistema lineal y deja ver de inmediato
> el espectro: las [[Raices Caracteristicas y Funciones Propias| raíces características]] son las
> raíces de un determinante $m\times m$.

---

## Ejemplo

> [!ejemplo] Núcleo $K=x+t$ resuelto completo (rango 2)
> Resolvamos, con $f(x)=1$,
> $$\varphi(x)=1+\lambda\int_{0}^{1}(x+t)\,\varphi(t)\,dt.$$
>
> **Paso 1 — separa el núcleo.** $K(x,t)=x+t=\underbrace{x}_{a_1}\cdot\underbrace{1}_{b_1}+\underbrace{1}_{a_2}\cdot\underbrace{t}_{b_2}$: degenerado de rango $2$, con
> $a_1=x,\;b_1=1,\;a_2=1,\;b_2=t$.
>
> **Paso 2 — define las constantes.** Al integrar aparecen dos números,
> $$c_1=\int_0^1 b_1(t)\,\varphi(t)\,dt=\int_0^1\varphi(t)\,dt,\qquad c_2=\int_0^1 b_2(t)\,\varphi(t)\,dt=\int_0^1 t\,\varphi(t)\,dt.$$
> Entonces $\int_0^1(x+t)\varphi\,dt=x\,c_1+c_2$, y la solución tiene la forma
> $$\varphi(x)=1+\lambda\,(c_1\,x+c_2).$$
>
> **Paso 3 — arma el sistema.** Sustituye esa $\varphi$ en las definiciones de $c_1,c_2$. Necesitamos
> $\int_0^1 1\,dt=1$, $\int_0^1 t\,dt=\tfrac12$, $\int_0^1 t^2\,dt=\tfrac13$:
> $$c_1=\int_0^1\big(1+\lambda(c_1t+c_2)\big)dt=1+\lambda\big(\tfrac12 c_1+c_2\big),$$
> $$c_2=\int_0^1 t\big(1+\lambda(c_1t+c_2)\big)dt=\tfrac12+\lambda\big(\tfrac13 c_1+\tfrac12 c_2\big).$$
> Reordenando, $(\mathsf{I}-\lambda\mathsf{A})\mathbf{c}=\mathbf{f}$ con
> $$\mathsf{A}=\begin{pmatrix}\tfrac12&1\\[2pt]\tfrac13&\tfrac12\end{pmatrix},\qquad
> \begin{cases}\big(1-\tfrac{\lambda}{2}\big)c_1-\lambda c_2=1,\\[4pt]-\tfrac{\lambda}{3}c_1+\big(1-\tfrac{\lambda}{2}\big)c_2=\tfrac12.\end{cases}$$
>
> **Paso 4 — raíces características.** Son los $\lambda$ con $\det(\mathsf{I}-\lambda\mathsf{A})=0$:
> $$\Big(1-\tfrac{\lambda}{2}\Big)^2-\tfrac{\lambda}{3}\,\lambda=0\;\Longrightarrow\;1-\lambda+\tfrac{\lambda^2}{4}-\tfrac{\lambda^2}{3}=0\;\Longrightarrow\;1-\lambda-\tfrac{\lambda^2}{12}=0.$$
> Multiplicando por $-12$: $\lambda^2+12\lambda-12=0$, de donde
> $$\boxed{\lambda_{1,2}=-6\pm 4\sqrt{3}}\quad(\approx 0.928\ \text{y}\ -12.93).$$
> Para esos dos valores el sistema es singular y la ecuación cae en la
> [[Alternativa de Fredholm| alternativa de Fredholm]].
>
> **Paso 5 — resuelve para $f=1$ (con $\lambda$ genérico).** Sea $\Delta=1-\lambda-\tfrac{\lambda^2}{12}$
> el determinante. Por Cramer,
> $$c_1=\frac{1}{\Delta}\begin{vmatrix}1&-\lambda\\ \tfrac12&1-\tfrac{\lambda}{2}\end{vmatrix}=\frac{1-\tfrac{\lambda}{2}+\tfrac{\lambda}{2}}{\Delta}=\frac{1}{\Delta},\qquad
> c_2=\frac{1}{\Delta}\begin{vmatrix}1-\tfrac{\lambda}{2}&1\\ -\tfrac{\lambda}{3}&\tfrac12\end{vmatrix}=\frac{\tfrac12-\tfrac{\lambda}{4}+\tfrac{\lambda}{3}}{\Delta}=\frac{\tfrac12+\tfrac{\lambda}{12}}{\Delta}.$$
> La solución es entonces, para $\lambda\neq\lambda_{1,2}$,
> $$\boxed{\varphi(x)=1+\frac{\lambda}{\Delta}\Big(x+\tfrac12+\tfrac{\lambda}{12}\Big),\qquad \Delta=1-\lambda-\tfrac{\lambda^2}{12}.}$$
> Por ejemplo, en $\lambda=1$ se tiene $\Delta=-\tfrac{1}{12}$, $c_1=-12$, $c_2=-7$, luego
> $\varphi(x)=1-12x-7$, es decir $\varphi(x)=-6-12x$. (Comprobación rápida: $\int_0^1\varphi=-12=c_1$ y
> $\int_0^1 t\varphi=-7=c_2$.)

---

## En qué consiste

> [!teorema] Un núcleo degenerado convierte Fredholm en un sistema lineal $m\times m$
> Para $K(x,t)=\sum_{i=1}^m a_i(x)b_i(t)$, la ecuación
> $\varphi=f+\lambda\int_a^b K\varphi$ equivale al sistema lineal $(\mathsf{I}-\lambda\mathsf{A})\mathbf{c}=\mathbf{f}$,
> con $\alpha_{ji}=\int_a^b b_j(t)a_i(t)\,dt$, $f_j=\int_a^b b_j(t)f(t)\,dt$, y la solución
> $\varphi=f+\lambda\sum_i c_i\,a_i$. Las **raíces características** son los $\lambda$ con
> $\det(\mathsf{I}-\lambda\mathsf{A})=0$ (a lo sumo $m$).

> [!demostracion]
> **Paso 1 — sustituye el núcleo en la integral.** Como $K=\sum_i a_i(x)b_i(t)$,
> $$\int_a^b K(x,t)\varphi(t)\,dt=\sum_{i=1}^m a_i(x)\underbrace{\int_a^b b_i(t)\varphi(t)\,dt}_{\displaystyle c_i},$$
> donde cada $c_i$ es una **constante** (no depende de $x$).
>
> **Paso 2 — forma de la solución.** Llevando esto a la ecuación,
> $$\varphi(x)=f(x)+\lambda\sum_{i=1}^m c_i\,a_i(x).$$
> Resolver $\varphi$ equivale a hallar los $m$ números $c_1,\dots,c_m$.
>
> **Paso 3 — ecuaciones para los $c_j$.** Multiplica la expresión anterior por $b_j(t)$ e integra,
> usando que $c_j=\int_a^b b_j\varphi$:
> $$c_j=\int_a^b b_j(t)\Big(f(t)+\lambda\sum_i c_i a_i(t)\Big)dt=f_j+\lambda\sum_{i=1}^m \alpha_{ji}\,c_i,$$
> con $f_j=\int_a^b b_j f$ y $\alpha_{ji}=\int_a^b b_j a_i$. En forma matricial,
> $$(\mathsf{I}-\lambda\mathsf{A})\,\mathbf{c}=\mathbf{f},\qquad \mathsf{A}=(\alpha_{ji}).$$
>
> **Paso 4 — espectro.** Este sistema tiene solución única salvo si su determinante se anula. Las
> **raíces características** del núcleo son, por tanto, las raíces del polinomio
> $\det(\mathsf{I}-\lambda\mathsf{A})=0$ —a lo sumo $m$, el rango del núcleo. $\blacksquare$

> [!proposicion]
> El polinomio $\det(\mathsf{I}-\lambda\mathsf{A})$ de grado $\le m$ coincide con el **determinante de
> Fredholm** $D(\lambda)$ del núcleo degenerado: para estos núcleos, la serie entera de los
> [[Determinantes de Fredholm| determinantes de Fredholm]] se trunca y se reduce a este polinomio.

> [!info] Cualquier núcleo continuo se aproxima por uno degenerado
> Si $K(x,t)$ es continuo, por Weierstrass (o truncando un desarrollo de Fourier/Taylor) se aproxima
> uniformemente por sumas finitas $\sum a_i(x)b_i(t)$. Resolver la ecuación con el núcleo aproximado da
> un sistema finito cuya solución converge a la verdadera: es la base de muchos
> [[Sustitucion Nucleo Degenerado| métodos numéricos]] para ecuaciones integrales.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Degenerado | $K(x,t)=\sum_{i=1}^m a_i(x)b_i(t)$ (suma **finita**, rango $m$) |
> | Reduce a | sistema lineal $(\mathsf{I}-\lambda\mathsf{A})\mathbf{c}=\mathbf{f}$, $m\times m$ |
> | Coeficientes | $\alpha_{ji}=\int_a^b b_j a_i$, $\;f_j=\int_a^b b_j f$ |
> | Solución | $\varphi=f+\lambda\sum_i c_i a_i$ |
> | Raíces características | ceros de $\det(\mathsf{I}-\lambda\mathsf{A})$ (a lo sumo $m$) |
> | Si $\det=0$ | [[Alternativa de Fredholm\|alternativa de Fredholm]] |

> [!corolario]
> El núcleo degenerado es el caso donde Fredholm se vuelve **exactamente** finito: $m$ funciones
> $b_i(t)$ "miden" $\varphi$ y producen $m$ números $c_i$ que satisfacen un sistema lineal ordinario.
> Por eso es el primer método a intentar, el modelo mental para todo lo demás, y el motor de las
> aproximaciones numéricas de núcleos generales.

> [!referencia]
> - La ecuación general: [[Fredholm Segunda Especie]].
> - El polinomio como caso de la serie: [[Determinantes de Fredholm]].
> - El espectro que se obtiene: [[Raices Caracteristicas y Funciones Propias]].
> - Panorama general: [[Fredholm/index]].
