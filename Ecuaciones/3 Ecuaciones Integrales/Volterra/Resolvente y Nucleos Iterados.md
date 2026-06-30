---
title: Resolvente y Núcleos Iterados
order: 2
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - volterra
  - resolvente
draft: false
aliases:
  - resolvente
  - núcleos iterados
  - serie de Neumann
  - resolvent kernel
  - iterated kernels
---

# Resolvente y Núcleos Iterados

> [!definicion]
> Los **núcleos iterados** de $K(x,t)$ se definen por recurrencia: $K_1(x,t)=K(x,t)$ y
> $$K_{n}(x,t)=\int_{t}^{x}K(x,s)\,K_{n-1}(s,t)\,ds\qquad(n\ge 2).$$
> La **resolvente** (o núcleo resolvente) es la serie de Neumann
> $$\Gamma(x,t;\lambda)=\sum_{n=1}^{\infty}\lambda^{\,n-1}\,K_{n}(x,t),$$
> y con ella la solución de la Volterra de 2ª especie $\varphi=f+\lambda\int_0^x K\varphi\,dt$ se escribe **explícitamente**:
> $$\varphi(x)=f(x)+\lambda\int_{0}^{x}\Gamma(x,t;\lambda)\,f(t)\,dt.$$

> [!info]
> Es el **método estrella** de [[Volterra Segunda Especie| Volterra de 2ª especie]], dentro del [[Volterra/index| bloque de Volterra]]. La resolvente es la **suma cerrada** de las [[Aproximaciones Sucesivas| aproximaciones sucesivas]]: empaqueta toda la iteración en una sola función. Si además el núcleo es de convolución $K(x-t)$, la serie se suma cómodamente con [[Ecuaciones de Convolucion| transformada de Laplace]].

---

## Ejemplo

> [!ejemplo] El núcleo constante $K(x,t)=1$ y su resolvente exponencial
> Tomemos el núcleo más simple posible, $K(x,t)=1$, y calculemos sus iterados.
>
> **Núcleos iterados.** Con $K_1=1$,
> $$K_2(x,t)=\int_t^x 1\cdot 1\,ds=x-t,\qquad
> K_3(x,t)=\int_t^x 1\cdot(s-t)\,ds=\frac{(x-t)^2}{2}.$$
> El patrón, demostrable por inducción, es
> $$K_n(x,t)=\frac{(x-t)^{\,n-1}}{(n-1)!}.$$
>
> **Resolvente.** Sumamos la serie de Neumann reconociendo la exponencial:
> $$\Gamma(x,t;\lambda)=\sum_{n=1}^{\infty}\lambda^{\,n-1}\frac{(x-t)^{\,n-1}}{(n-1)!}
> =\sum_{m=0}^{\infty}\frac{\big(\lambda(x-t)\big)^{m}}{m!}=e^{\lambda(x-t)}.$$
>
> **Solución.** Para la ecuación $\varphi(x)=f(x)+\lambda\int_0^x\varphi(t)\,dt$ la fórmula da
> $$\varphi(x)=f(x)+\lambda\int_0^x e^{\lambda(x-t)}f(t)\,dt.$$
> Por ejemplo, con $f(x)=1$ y $\lambda=1$ se recupera $\varphi(x)=e^x$ (coherente con el Ejemplo 1 de [[Volterra Segunda Especie]]): $1+\int_0^x e^{x-t}\,dt=1+(e^x-1)=e^x$.

---

## En qué consiste

> [!teoria]
> La idea es **sustituir la ecuación en sí misma** una y otra vez. Cada sustitución cambia un $\varphi$ del integrando por toda la ecuación de nuevo, generando potencias del operador integral $K$. Los "coeficientes" de esas potencias son precisamente los núcleos iterados $K_n$, y la suma de la serie es la resolvente. Lo notable de Volterra es que la serie **converge siempre**, porque cada iterado decae factorialmente.

> [!teorema] La solución por resolvente
> Para $K$ continuo en $0\le t\le x\le a$, la serie $\Gamma(x,t;\lambda)=\sum_{n\ge1}\lambda^{n-1}K_n(x,t)$ converge absoluta y uniformemente para **todo** $\lambda$, y
> $$\varphi(x)=f(x)+\lambda\int_0^x\Gamma(x,t;\lambda)\,f(t)\,dt$$
> es la única solución de la Volterra de 2ª especie.

> [!demostracion] Iteración del operador y convergencia de la serie de Neumann
> **Paso 1 — iterar la ecuación.** Escribimos abreviadamente $(K\varphi)(x)=\int_0^x K(x,t)\varphi(t)\,dt$, de modo que la ecuación es $\varphi=f+\lambda K\varphi$. Sustituyendo $\varphi$ del lado derecho por su propia expresión,
> $$\varphi=f+\lambda K(f+\lambda K\varphi)=f+\lambda Kf+\lambda^2K^2\varphi.$$
> Repitiendo $n$ veces,
> $$\varphi=f+\lambda Kf+\lambda^2 K^2 f+\dots+\lambda^{n}K^{n}f+\lambda^{n+1}K^{n+1}\varphi.$$
>
> **Paso 2 — identificar los núcleos iterados.** El operador $K^n$ tiene por núcleo exactamente $K_n$: $(K^n f)(x)=\int_0^x K_n(x,t)f(t)\,dt$, lo que se comprueba con la definición recursiva (un $K^n$ es un $K$ compuesto con $K^{n-1}$, y componer núcleos es la integral $\int_t^x K(x,s)K_{n-1}(s,t)\,ds$). Por tanto la serie formal es $\varphi=f+\lambda\int_0^x\big(\sum_{n\ge1}\lambda^{n-1}K_n\big)f\,dt$.
>
> **Paso 3 — acotar los iterados.** Sea $M=\max\lvert K\rvert$ en el triángulo. Por inducción,
> $$\lvert K_n(x,t)\rvert\le M^{\,n}\,\frac{(x-t)^{\,n-1}}{(n-1)!}.$$
> En efecto, vale para $n=1$ ($\lvert K_1\rvert\le M$), y si vale para $n-1$, $\lvert K_n\rvert\le\int_t^x M\cdot M^{n-1}\frac{(s-t)^{n-2}}{(n-2)!}\,ds=M^n\frac{(x-t)^{n-1}}{(n-1)!}$.
>
> **Paso 4 — convergencia.** Cada término de $\Gamma$ está mayorado por $\lvert\lambda\rvert^{n-1}M^n\frac{(x-t)^{n-1}}{(n-1)!}$, cuya suma es la **serie de una exponencial** $M\,e^{\lvert\lambda\rvert M(x-t)}$, finita para **cualquier** $\lambda$. La serie converge absoluta y uniformemente, y el resto $\lambda^{n+1}K^{n+1}\varphi\to0$. Así $\Gamma$ está bien definida y la fórmula resuelve la ecuación. $\blacksquare$

> [!algoritmo] Resolver con la resolvente
> 1. **Calcula los iterados** $K_2,K_3,\dots$ con $K_n(x,t)=\int_t^x K(x,s)K_{n-1}(s,t)\,ds$ hasta ver el patrón.
> 2. **Suma la serie** $\Gamma(x,t;\lambda)=\sum_{n\ge1}\lambda^{n-1}K_n(x,t)$ en forma cerrada (a menudo una exponencial o una función conocida).
> 3. **Aplica la fórmula** $\varphi(x)=f(x)+\lambda\int_0^x\Gamma(x,t;\lambda)f(t)\,dt$.
> 4. **Verifica** sustituyendo en la ecuación original.

> [!proposicion]
> Si el núcleo es de **convolución**, $K(x,t)=k(x-t)$, también lo son todos sus iterados, y la resolvente depende solo de $x-t$: $\Gamma=\Gamma(x-t;\lambda)$. Entonces la suma de la serie de Neumann coincide con resolver por [[Ecuaciones de Convolucion| transformada de Laplace]], donde la convolución se vuelve un producto y $\widehat{\Gamma}=\lambda\widehat{k}/(1-\lambda\widehat{k})$.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Iterados | $K_1=K$,  $K_n(x,t)=\int_t^x K(x,s)K_{n-1}(s,t)\,ds$ |
> | Resolvente | $\Gamma(x,t;\lambda)=\sum_{n\ge1}\lambda^{n-1}K_n(x,t)$ |
> | Solución | $\varphi=f+\lambda\int_0^x\Gamma(x,t;\lambda)f(t)\,dt$ |
> | Cota clave | $\lvert K_n\rvert\le M^n(x-t)^{n-1}/(n-1)!$ |
> | Convergencia | **siempre** (mayorada por exponencial), todo $\lambda$ |
> | Ejemplo | $K=1\Rightarrow K_n=\tfrac{(x-t)^{n-1}}{(n-1)!}\Rightarrow\Gamma=e^{\lambda(x-t)}$ |

> [!corolario]
> La resolvente es la **suma cerrada** de la serie de Neumann: convierte la iteración infinita de las aproximaciones sucesivas en una sola fórmula. Como cada iterado decae como $1/(n-1)!$, la serie converge para todo $\lambda$ —el sello de Volterra—.

> [!referencia]
> - La ecuación que resuelve: [[Volterra Segunda Especie]].
> - La iteración que esta serie suma: [[Aproximaciones Sucesivas]].
> - El caso de convolución vía Laplace: [[Ecuaciones de Convolucion]].
> - Vista de conjunto: [[Volterra/index]].
