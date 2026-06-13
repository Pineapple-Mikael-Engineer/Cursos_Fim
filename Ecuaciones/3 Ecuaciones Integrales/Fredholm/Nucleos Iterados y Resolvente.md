---
title: Núcleos Iterados y Resolvente
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - fredholm
  - resolvente
draft: false
aliases:
  - núcleos iterados
  - resolvente de Fredholm
  - serie de Neumann
  - iterated kernels
  - resolvent kernel
  - Neumann series
---

# Núcleos Iterados y Resolvente

> [!definicion]
> Los **núcleos iterados** de $K(x,t)$ se construyen por recurrencia: $K_1(x,t)=K(x,t)$ y
> $$K_{n}(x,t)=\int_{a}^{b}K(x,s)\,K_{n-1}(s,t)\,ds\qquad(n\ge 2),$$
> donde —a diferencia de [[Volterra/index| Volterra]]— se integra sobre **todo** $[a,b]$. La
> **resolvente** (o núcleo resolvente) es la **serie de Neumann**
> $$\Gamma(x,t;\lambda)=\sum_{n=1}^{\infty}\lambda^{\,n-1}\,K_{n}(x,t),$$
> y con ella la solución de la Fredholm de 2ª especie $\varphi=f+\lambda\int_a^b K\varphi\,dt$ se escribe
> en forma cerrada:
> $$\varphi(x)=f(x)+\lambda\int_{a}^{b}\Gamma(x,t;\lambda)\,f(t)\,dt.$$

> [!info]
> Es el método iterativo de [[Fredholm Segunda Especie| Fredholm de 2ª especie]], dentro del
> [[Fredholm/index| bloque de Fredholm]]. La resolvente empaqueta toda la iteración del operador
> integral en una sola función, igual que en [[Volterra/index| Volterra]]; la diferencia crucial es
> que aquí la serie **solo converge para $\lambda$ pequeño**. Cuando $\lambda$ es grande hay que recurrir
> a los [[Determinantes de Fredholm| determinantes de Fredholm]].

---

## Ejemplo

> [!ejemplo] El núcleo $K(x,t)=xt$ en $[0,1]$ y su resolvente geométrica
> Tomemos el núcleo separable $K(x,t)=xt$ sobre $[0,1]$ y calculemos sus iterados.
>
> **Núcleos iterados.** Con $K_1=xt$,
> $$K_2(x,t)=\int_0^1 (xs)(st)\,ds=xt\int_0^1 s^2\,ds=\frac{xt}{3}.$$
> El siguiente repite el patrón, porque el factor $\int_0^1 s^2\,ds=\tfrac13$ reaparece en cada paso:
> $$K_3(x,t)=\int_0^1 (xs)\,\frac{st}{3}\,ds=\frac{xt}{3}\cdot\frac{1}{3}=\frac{xt}{3^2},
> \qquad K_n(x,t)=\frac{xt}{3^{\,n-1}}.$$
>
> **Resolvente.** Sumamos la serie de Neumann, que es **geométrica** de razón $\lambda/3$:
> $$\Gamma(x,t;\lambda)=\sum_{n=1}^{\infty}\lambda^{\,n-1}\frac{xt}{3^{\,n-1}}
> =xt\sum_{m=0}^{\infty}\Big(\frac{\lambda}{3}\Big)^{m}=\frac{xt}{1-\lambda/3},$$
> válida cuando $\lvert\lambda/3\rvert<1$, es decir $\lvert\lambda\rvert<3$.
>
> **Coherencia con el núcleo degenerado.** Como $K=xt$ es de rango $1$, la solución por
> [[Nucleo Degenerado| núcleo degenerado]] da exactamente el mismo factor $\tfrac{1}{1-\lambda/3}$: la
> raíz característica es $\lambda=3$, justo el borde del disco de convergencia.

---

## En qué consiste

> [!teoria]
> La idea es **sustituir la ecuación en sí misma** repetidamente. Cada vez que reemplazamos el $\varphi$
> del integrando por toda la ecuación, aparece una potencia más del operador integral $K$, y el "núcleo"
> de la potencia $K^n$ es precisamente el iterado $K_n$. Sumar esas potencias es la serie geométrica de
> operadores $(\mathbb{I}-\lambda K)^{-1}=\sum_n\lambda^n K^n$. La diferencia con Volterra es **decisiva**:
> allí los iterados decaen como $1/(n-1)!$ y la serie converge siempre; aquí, al integrar sobre todo
> $[a,b]$, los iterados crecen como $\lVert K\rVert^{\,n}$ y la serie es solo geométrica, así que
> **converge únicamente si $\lambda$ es suficientemente pequeño**.

> [!teorema] Convergencia de la serie de Neumann
> Sea $K$ continuo en $[a,b]\times[a,b]$ y definamos
> $$\lVert K\rVert=\Big(\int_a^b\!\!\int_a^b \lvert K(x,t)\rvert^2\,dx\,dt\Big)^{1/2}.$$
> Entonces la serie de Neumann $\Gamma(x,t;\lambda)=\sum_{n\ge1}\lambda^{n-1}K_n(x,t)$ converge absoluta y
> uniformemente, y la fórmula $\varphi=f+\lambda\int_a^b\Gamma f\,dt$ es la única solución, siempre que
> $$\lvert\lambda\rvert<\frac{1}{\lVert K\rVert}.$$

> [!demostracion] Cota de los iterados y radio de convergencia
> **Paso 1 — iterar la ecuación.** Con $(K\varphi)(x)=\int_a^b K(x,t)\varphi(t)\,dt$, la ecuación es
> $\varphi=f+\lambda K\varphi$. Sustituyendo $\varphi$ del lado derecho por su propia expresión $n$ veces,
> $$\varphi=f+\lambda Kf+\lambda^2 K^2 f+\dots+\lambda^{n}K^{n}f+\lambda^{n+1}K^{n+1}\varphi.$$
>
> **Paso 2 — identificar los iterados.** El operador $K^n$ tiene por núcleo $K_n$: componer núcleos es
> la integral $K_n(x,t)=\int_a^b K(x,s)K_{n-1}(s,t)\,ds$. Luego la serie formal es
> $\varphi=f+\lambda\int_a^b\big(\sum_{n\ge1}\lambda^{n-1}K_n\big)f\,dt$.
>
> **Paso 3 — acotar los iterados (clave Fredholm).** Por la desigualdad de Cauchy-Schwarz, componer dos
> núcleos no aumenta la norma más que el producto de normas:
> $$\lVert K_n\rVert\le\lVert K\rVert\,\lVert K_{n-1}\rVert\quad\Longrightarrow\quad
> \lVert K_n\rVert\le\lVert K\rVert^{\,n}.$$
> Nótese el contraste con Volterra: aquí **no** aparece el $1/(n-1)!$ que allí garantizaba convergencia
> universal; solo queda la potencia $\lVert K\rVert^n$.
>
> **Paso 4 — convergencia geométrica.** Cada término de $\Gamma$ está mayorado por
> $\lvert\lambda\rvert^{n-1}\lVert K\rVert^{n}$, cuya suma es la **serie geométrica**
> $\lVert K\rVert\sum_{n\ge0}(\lvert\lambda\rvert\lVert K\rVert)^{n}$. Esta converge si y solo si
> $\lvert\lambda\rvert\lVert K\rVert<1$, esto es $\lvert\lambda\rvert<1/\lVert K\rVert$. En ese disco el
> resto $\lambda^{n+1}K^{n+1}\varphi\to0$ y la fórmula resuelve la ecuación. $\blacksquare$

> [!algoritmo] Resolver con la resolvente
> 1. **Calcula los iterados** $K_2,K_3,\dots$ con $K_n(x,t)=\int_a^b K(x,s)K_{n-1}(s,t)\,ds$ hasta ver el
>    patrón.
> 2. **Suma la serie** $\Gamma(x,t;\lambda)=\sum_{n\ge1}\lambda^{n-1}K_n(x,t)$ en forma cerrada (a menudo
>    geométrica).
> 3. **Verifica el rango** $\lvert\lambda\rvert<1/\lVert K\rVert$; fuera de él la serie diverge.
> 4. **Aplica la fórmula** $\varphi(x)=f(x)+\lambda\int_a^b\Gamma(x,t;\lambda)f(t)\,dt$.

> [!info]
> Para $\lambda$ **fuera del disco de convergencia** la serie de Neumann ya no sirve, pero la solución
> puede seguir existiendo. En ese caso se usan los [[Determinantes de Fredholm| determinantes de Fredholm]], que expresan la resolvente como un **cociente de dos series enteras** convergentes para
> **todo** $\lambda$: $\Gamma(x,t;\lambda)=D(x,t;\lambda)/D(\lambda)$. Los polos de ese cociente son
> justamente las [[Raices Caracteristicas y Funciones Propias| raíces características]].

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Iterados | $K_1=K$,  $K_n(x,t)=\int_a^b K(x,s)K_{n-1}(s,t)\,ds$ |
> | Resolvente | $\Gamma(x,t;\lambda)=\sum_{n\ge1}\lambda^{n-1}K_n(x,t)$ |
> | Solución | $\varphi=f+\lambda\int_a^b\Gamma(x,t;\lambda)f(t)\,dt$ |
> | Cota clave | $\lVert K_n\rVert\le\lVert K\rVert^{\,n}$ (sin factorial) |
> | Convergencia | **solo** si $\lvert\lambda\rvert<1/\lVert K\rVert$ (Volterra: siempre) |
> | Ejemplo | $K=xt\Rightarrow K_n=xt/3^{n-1}\Rightarrow\Gamma=xt/(1-\lambda/3)$ |

> [!corolario]
> La resolvente es la suma cerrada de la serie de Neumann, pero en Fredholm esa suma es **geométrica**:
> converge solo en el disco $\lvert\lambda\rvert<1/\lVert K\rVert$. Esa es la huella del carácter
> **global** de Fredholm frente a Volterra. Para todo $\lambda$ hace falta la maquinaria de los
> [[Determinantes de Fredholm| determinantes de Fredholm]].

> [!referencia]
> - La ecuación que resuelve: [[Fredholm Segunda Especie]].
> - La versión válida para todo $\lambda$: [[Determinantes de Fredholm]].
> - El mismo método donde sí converge siempre: [[Volterra/index]].
> - Vista de conjunto: [[Fredholm/index]].
