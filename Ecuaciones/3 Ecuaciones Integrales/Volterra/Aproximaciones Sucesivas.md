---
title: Aproximaciones Sucesivas
order: 3
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - volterra
  - aproximaciones-sucesivas
draft: false
aliases:
  - aproximaciones sucesivas
  - iteración de punto fijo
  - successive approximations
  - method of successive approximations
---

# Aproximaciones Sucesivas

> [!definicion]
> El **método de aproximaciones sucesivas** resuelve la Volterra de 2ª especie por **iteración de punto fijo**: se parte de $\varphi_0=f$ y se mejora la estimación una y otra vez,
> $$\varphi_{n+1}(x)=f(x)+\lambda\int_{0}^{x}K(x,t)\,\varphi_{n}(t)\,dt.$$
> La sucesión $\{\varphi_n\}$ **converge uniformemente** a la única solución $\varphi$ de la ecuación, y lo hace **para todo $\lambda$**. Es la [[Iteracion de Picard| iteración de Picard]] aplicada a ecuaciones integrales.

> [!info]
> Es el **motor teórico** de [[Volterra Segunda Especie| Volterra de 2ª especie]]: con él se demuestra la existencia y unicidad. Su **suma cerrada** es la [[Resolvente y Nucleos Iterados| resolvente]] $\Gamma(x,t;\lambda)$. Pertenece al [[Volterra/index| bloque de Volterra]] y es el mismo mecanismo de punto fijo que prueba el teorema de existencia para EDOs.

---

## Ejemplo

> [!ejemplo] Las iteraciones reconstruyen $e^x$ término a término
> Resolvamos por iteración $\varphi(x)=1+\int_0^x\varphi(t)\,dt$ (aquí $f=1$, $K=1$, $\lambda=1$).
>
> **Arranque.** $\varphi_0(x)=f(x)=1$.
>
> **Primera iteración.**
> $$\varphi_1(x)=1+\int_0^x 1\,dt=1+x.$$
>
> **Segunda iteración.**
> $$\varphi_2(x)=1+\int_0^x(1+t)\,dt=1+x+\frac{x^2}{2}.$$
>
> **Tercera iteración.**
> $$\varphi_3(x)=1+\int_0^x\Big(1+t+\frac{t^2}{2}\Big)dt=1+x+\frac{x^2}{2}+\frac{x^3}{6}.$$
>
> **Patrón.** Cada paso añade el siguiente término de la serie de Taylor:
> $$\varphi_n(x)=\sum_{k=0}^{n}\frac{x^{k}}{k!}\ \xrightarrow{\,n\to\infty\,}\ e^{x}.$$
> Las aproximaciones sucesivas son exactamente las **sumas parciales de $e^x$**, que es la solución hallada por diferenciación en [[Volterra Segunda Especie]]. La iteración "descubre" la exponencial sin resolver ninguna EDO.

---

## En qué consiste

> [!teoria]
> La ecuación $\varphi=f+\lambda K\varphi$ pide un **punto fijo** del operador $T\varphi=f+\lambda K\varphi$. La estrategia natural es iterar $T$ partiendo de cualquier semilla (tomamos $\varphi_0=f$) y confiar en que $T^n\varphi_0$ se acerque al punto fijo. Funciona porque, en Volterra, aplicar $K$ "encoge" las diferencias por el factor $(x-t)$ del intervalo de integración: cada iteración gana un orden en $(x-t)^n/n!$, que decae más rápido que cualquier potencia de $\lambda$.

> [!algoritmo] Iterar a mano
> 1. **Semilla:** $\varphi_0(x)=f(x)$.
> 2. **Itera:** $\varphi_{n+1}(x)=f(x)+\lambda\int_0^x K(x,t)\varphi_n(t)\,dt$.
> 3. **Observa el patrón** de las $\varphi_n$ (suelen ser sumas parciales de una serie conocida).
> 4. **Pasa al límite** $n\to\infty$ para identificar $\varphi$, o reconoce la [[Resolvente y Nucleos Iterados| resolvente]] como suma cerrada.

> [!teorema] Convergencia de las aproximaciones sucesivas
> Si $K$ es continuo en $0\le t\le x\le a$ (con $\lvert K\rvert\le M$) y $f$ es continua en $[0,a]$, la sucesión $\varphi_{n+1}=f+\lambda K\varphi_n$ con $\varphi_0=f$ converge **uniformemente** en $[0,a]$, para **todo** $\lambda$, a la única solución continua de la Volterra de 2ª especie.

> [!demostracion] Cotas factoriales y sucesión de Cauchy
> **Paso 1 — diferencias consecutivas.** Sea $d_n=\varphi_{n+1}-\varphi_n$. Restando dos iteraciones,
> $$d_n(x)=\lambda\int_0^x K(x,t)\,d_{n-1}(t)\,dt,$$
> y $d_0=\varphi_1-\varphi_0=\lambda\int_0^x K(x,t)f(t)\,dt$. Es decir, $d_n=\lambda^{n+1}K^{n+1}f$ en la notación de operadores: cada diferencia es una potencia más del operador integral aplicada a $f$.
>
> **Paso 2 — acotar por inducción.** Con $F=\max\lvert f\rvert$, se prueba que
> $$\lvert d_n(x)\rvert\le F\,\frac{\big(\lvert\lambda\rvert M\big)^{\,n+1}(x-t)^{\,n+1}}{(n+1)!}
> \le F\,\frac{\big(\lvert\lambda\rvert M a\big)^{\,n+1}}{(n+1)!}.$$
> El caso base sale de $\lvert d_0\rvert\le\lvert\lambda\rvert M F x$; el paso inductivo, integrando la cota anterior, multiplica por $\lvert\lambda\rvert M$ y sube el exponente y el factorial.
>
> **Paso 3 — serie telescópica dominada.** Como $\varphi_n=\varphi_0+\sum_{k=0}^{n-1}d_k$, la convergencia de $\{\varphi_n\}$ equivale a la de $\sum_k d_k$. Pero $\sum_k\lvert d_k\rvert$ está mayorada término a término por la serie de la exponencial $F\,e^{\lvert\lambda\rvert M a}$, **finita para todo $\lambda$**. Por el criterio de Weierstrass la serie converge **uniformemente**.
>
> **Paso 4 — el límite es la solución.** La sucesión es uniformemente de Cauchy, luego converge a una función continua $\varphi$. Pasando al límite en $\varphi_{n+1}=f+\lambda K\varphi_n$ (la convergencia uniforme permite intercambiar límite e integral) se obtiene $\varphi=f+\lambda K\varphi$. La unicidad sale de la misma cota: dos soluciones tendrían diferencia acotada por $C(\lvert\lambda\rvert Ma)^n/n!\to0$. La convergencia vale para **todo** $\lambda$: ese es el rasgo propio de Volterra. $\blacksquare$

> [!info]
> La [[Resolvente y Nucleos Iterados| resolvente]] es la **suma cerrada** de esta iteración: sumando $\varphi=f+\sum_n d_n=f+\lambda\int_0^x\big(\sum_n\lambda^{n-1}K_n\big)f\,dt$ aparecen los núcleos iterados $K_n$ y, con ellos, $\Gamma(x,t;\lambda)$. Iterar y "sumar la serie de Neumann" son la misma cosa vista de dos maneras.

> [!warning]
> Aunque la teoría garantiza convergencia para todo $\lambda$, **a mano** solo es práctica cuando las $\varphi_n$ revelan un patrón cerrado; si no, conviene la resolvente o, en casos de convolución, [[Ecuaciones de Convolucion| Laplace]]. Recuerda iniciar con $\varphi_0=f$ (no con $0$) para que las sumas parciales salgan limpias.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Iteración | $\varphi_0=f$,  $\varphi_{n+1}=f+\lambda\int_0^x K\varphi_n\,dt$ |
> | Diferencia | $d_n=\varphi_{n+1}-\varphi_n=\lambda^{n+1}K^{n+1}f$ |
> | Cota | $\lvert d_n\rvert\le F(\lvert\lambda\rvert Ma)^{n+1}/(n+1)!$ |
> | Convergencia | **uniforme**, para todo $\lambda$ (Cauchy, Weierstrass) |
> | Suma cerrada | la [[Resolvente y Nucleos Iterados\|resolvente]] $\Gamma(x,t;\lambda)$ |
> | Ejemplo | $\varphi=1+\int_0^x\varphi\Rightarrow\varphi_n=\sum_{k\le n}x^k/k!\to e^x$ |

> [!corolario]
> Las aproximaciones sucesivas son la **construcción** de la solución de Volterra: la sucesión de Cauchy que converge a ella demuestra de paso la existencia y la unicidad. Cuando la serie se suma en forma cerrada, ese límite **es** la resolvente.

> [!referencia]
> - La forma cerrada de esta serie: [[Resolvente y Nucleos Iterados]].
> - La ecuación que se resuelve: [[Volterra Segunda Especie]].
> - El mismo método para EDOs: [[Iteracion de Picard]].
> - Vista de conjunto: [[Volterra/index]].
