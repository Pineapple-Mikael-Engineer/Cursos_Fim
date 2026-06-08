---
title: Iteración de Picard
tags:
  - ecuaciones
  - edo
  - teoria
  - fundamentos
  - existencia-unicidad
draft: false
aliases:
  - iteración de Picard
  - aproximaciones sucesivas
  - iteradas de Picard
  - Picard iteration
  - successive approximations
---

# Iteración de Picard

> [!definicion]
> Las **iteradas de Picard** del problema de valor inicial
> $$y'=f(x,y),\qquad y(x_0)=y_0$$
> son la sucesión de funciones $\{y_n(x)\}$ definida por **recurrencia** a partir de la constante
> $y_0(x)\equiv y_0$ mediante
> $$y_{n+1}(x)\ =\ y_0+\int_{x_0}^{x} f\bigl(t,\,y_n(t)\bigr)\,dt.$$
> Cuando $f$ es continua y **Lipschitz en $y$**, esta sucesión converge **uniformemente** a la
> solución del PVI. Es, por tanto, la versión **constructiva** del teorema de
> [[Existencia y Unicidad Picard| Picard]]: no solo afirma que la solución existe, sino que la
> **fabrica** como límite de aproximaciones sucesivas.

> [!info]
> Vive en los [[Fundamentos y Teoria Cualitativa/index| fundamentos cualitativos]] del libro, como contraparte algorítmica del
> [[Existencia y Unicidad Picard| teorema de Picard-Lindelöf]]. La idea de fondo es la misma que
> allí: escribir el PVI como la **ecuación integral** $y=y_0+\int_{x_0}^{x} f(t,y)\,dt$ y aplicar el
> operador de Picard $T[y]=y_0+\int_{x_0}^{x} f(t,y)\,dt$ una y otra vez, $y_{n+1}=T[y_n]$, partiendo
> de la función constante. La convergencia se cuantifica con la [[Desigualdad de Gronwall| desigualdad de Gronwall]]; la versión que pide solo continuidad (y construye la solución de otro modo) es el
> [[Teorema de Peano| teorema de Peano]].

---

## Ejemplo

> [!ejemplo] Iteradas de Picard convergiendo a $e^x$
> ![[iteracion_picard.svg|460]]
>
> Para $y'=y,\,y(0)=1$ las iteradas $y_0=1,\ y_1=1+x,\ y_2=1+x+\tfrac{x^2}{2},\dots$ son las sumas
> parciales de $e^x$ y se acercan a la solución exacta.

> [!ejemplo]
> **El PVI $y'=y$, $y(0)=1$.** Aquí $f(x,y)=y$, $x_0=0$ e $y_0=1$. La recurrencia es
> $y_{n+1}(x)=1+\int_0^x y_n(t)\,dt$. Arrancamos con la constante y vamos integrando:
> $$y_0=1,$$
> $$y_1=1+\int_0^x 1\,dt=1+x,$$
> $$y_2=1+\int_0^x (1+t)\,dt=1+x+\frac{x^2}{2},$$
> $$y_3=1+\int_0^x\Bigl(1+t+\frac{t^2}{2}\Bigr)dt=1+x+\frac{x^2}{2}+\frac{x^3}{6}.$$
> El patrón es transparente: cada integración **añade un término** y reproduce el siguiente. Por
> inducción,
> $$y_n(x)=\sum_{k=0}^{n}\frac{x^k}{k!}.$$
> Pero esa es exactamente la **suma parcial $n$-ésima** de la serie de Taylor de la exponencial. Por
> tanto
> $$y_n(x)\ \xrightarrow[\;n\to\infty\;]{}\ \sum_{k=0}^{\infty}\frac{x^k}{k!}=e^{x},$$
> que es justo la solución del PVI ($y'=y$, $y(0)=1\Rightarrow y=e^x$). Las iteradas de Picard no son
> aproximaciones cualesquiera: son las truncaciones de la serie de potencias de la solución.

> [!ejemplo]
> **Un segundo caso: $y'=x+y$, $y(0)=1$.** Ahora $f(x,y)=x+y$ y $y_{n+1}=1+\int_0^x\!\bigl(t+y_n(t)\bigr)dt$.
> Calculemos dos iteradas:
> $$y_0=1,$$
> $$y_1=1+\int_0^x (t+1)\,dt=1+x+\frac{x^2}{2},$$
> $$y_2=1+\int_0^x\Bigl(t+1+t+\frac{t^2}{2}\Bigr)dt=1+x+x^2+\frac{x^3}{6}.$$
> De nuevo cada paso afina el siguiente coeficiente del desarrollo. La solución exacta es
> $y=2e^x-x-1=1+x+x^2+\frac{x^3}{3}+\cdots$; compárense los primeros términos con $y_2$: ya coinciden
> hasta $x^2$, y el de $x^3$ se irá corrigiendo en la siguiente iterada. Cada vuelta de la recurrencia
> recupera **un orden más** del desarrollo de la solución.

---

## En qué consiste

> [!teoria] Por qué iterar el operador integral
> La idea nace de la reformulación integral del PVI (la misma de [[Existencia y Unicidad Picard| Picard]]):
> una función continua $y$ resuelve $y'=f(x,y),\ y(x_0)=y_0$ **si y solo si** es **punto fijo** del
> operador
> $$T[y](x)=y_0+\int_{x_0}^{x} f\bigl(t,y(t)\bigr)\,dt,\qquad\text{es decir }y=T[y].$$
> Para encontrar un punto fijo, la receta más natural es la **iteración**: se parte de una semilla
> $y_0(x)\equiv y_0$ y se aplica $T$ repetidamente,
> $$y_1=T[y_0],\quad y_2=T[y_1],\quad\dots,\quad y_{n+1}=T[y_n].$$
> Si cada aplicación de $T$ **acerca** las funciones entre sí (es una contracción), la sucesión se
> "estabiliza" en el único punto fijo. Esa es la maquinaria del teorema del punto fijo de Banach; aquí
> la vemos funcionar paso a paso y, además, **acotamos** la velocidad a la que las iteradas se juntan.

> [!algoritmo] Cómo iterar a mano
> 1. Toma la semilla $y_0(x)\equiv y_0$ (la propia condición inicial, vista como función constante).
> 2. Sustituye $y_n(t)$ dentro de $f(t,\,\cdot\,)$ y **calcula la integral** $\int_{x_0}^{x} f(t,y_n(t))\,dt$.
> 3. Suma $y_0$: obtienes $y_{n+1}(x)=y_0+\int_{x_0}^{x} f(t,y_n(t))\,dt$.
> 4. Repite con $y_{n+1}$ en lugar de $y_n$. Tras $n$ pasos tienes la aproximación $y_n(x)$.
> 5. Si reconoces el patrón de los coeficientes (como en $e^x$), **identifica la serie** y pasa al
>    límite: ese límite es la solución.

> [!teorema] Convergencia de las iteradas de Picard
> Sea $f$ continua y **Lipschitz en $y$** con constante $L$ en un rectángulo $R$ alrededor de
> $(x_0,y_0)$, con $|f|\le M$ en $R$. Entonces la sucesión de iteradas $y_n$ está bien definida y
> **converge uniformemente** en un intervalo $|x-x_0|\le h$ a una función $y(x)$ que satisface la
> ecuación integral $y=y_0+\int_{x_0}^{x} f(t,y)\,dt$, es decir, a la **solución** del PVI. Además, el
> error de la $n$-ésima iterada está dominado por la cola de una exponencial:
> $$|y(x)-y_n(x)|\ \le\ \frac{M}{L}\sum_{k=n+1}^{\infty}\frac{\bigl(L|x-x_0|\bigr)^{k}}{k!}.$$

> [!demostracion]
> La estrategia es **telescópica**: escribimos el límite como la serie
> $y(x)=y_0+\sum_{n\ge 0}\bigl(y_{n+1}(x)-y_n(x)\bigr)$ y acotamos cada incremento.
>
> **Paso 1 — primer incremento.** Como $|f|\le M$,
> $$|y_1(x)-y_0|=\Bigl|\int_{x_0}^{x} f(t,y_0)\,dt\Bigr|\ \le\ M\,|x-x_0|.$$
> Este es el "tamaño" del primer salto: crece a lo sumo linealmente al alejarnos de $x_0$.
>
> **Paso 2 — incrementos sucesivos por inducción y Lipschitz.** Afirmamos que
> $$|y_{n+1}(x)-y_n(x)|\ \le\ \frac{M\,L^{n}}{(n+1)!}\,|x-x_0|^{\,n+1}.$$
> Para $n=0$ es el Paso 1. Supuesto cierto para $n-1$, usamos que la diferencia de dos iteradas pasa
> por el operador y aplicamos Lipschitz dentro de la integral:
> $$|y_{n+1}(x)-y_n(x)|=\Bigl|\int_{x_0}^{x}\!\bigl[f(t,y_n)-f(t,y_{n-1})\bigr]dt\Bigr|
> \le\int_{x_0}^{x} L\,|y_n(t)-y_{n-1}(t)|\,dt.$$
> Metiendo la hipótesis de inducción $|y_n-y_{n-1}|\le \frac{M L^{n-1}}{n!}|t-x_0|^{n}$ e integrando
> el monomio,
> $$|y_{n+1}(x)-y_n(x)|\ \le\ L\cdot\frac{M L^{n-1}}{n!}\int_{x_0}^{x}|t-x_0|^{n}\,dt
> =\frac{M L^{n}}{n!}\cdot\frac{|x-x_0|^{\,n+1}}{n+1}=\frac{M L^{n}}{(n+1)!}\,|x-x_0|^{\,n+1},$$
> que es la cota buscada. La clave es que el factorial del denominador **crece más rápido** que
> cualquier potencia, lo que controlará la suma.
>
> **Paso 3 — serie dominada y sucesión de Cauchy.** La serie de los incrementos está mayorada,
> término a término, por una serie numérica que reconocemos como una exponencial:
> $$\sum_{n=0}^{\infty}|y_{n+1}-y_n|\ \le\ \frac{M}{L}\sum_{n=0}^{\infty}\frac{\bigl(L|x-x_0|\bigr)^{n+1}}{(n+1)!}
> =\frac{M}{L}\bigl(e^{\,L|x-x_0|}-1\bigr)<\infty.$$
> Como está dominada por una serie convergente (y la cota es **uniforme** en $|x-x_0|\le h$, sin más
> que poner $h$ en lugar de $|x-x_0|$), la serie telescópica converge **absoluta y uniformemente**:
> las colas $\sum_{k\ge n}|y_{k+1}-y_k|$ se hacen arbitrariamente pequeñas y $\{y_n\}$ es una
> **sucesión de Cauchy** en la norma del supremo. Por completitud del espacio de continuas, tiene un
> **límite uniforme** $y(x)$, que es continuo. Pasando al límite en $y_{n+1}=y_0+\int_{x_0}^{x} f(t,y_n)\,dt$
> —lícito porque la convergencia uniforme y la continuidad de $f$ permiten intercambiar límite e
> integral— se obtiene $y=y_0+\int_{x_0}^{x} f(t,y)\,dt$: el límite **satisface la ecuación integral**
> y es la solución del PVI. La cota del error es la cola de esa misma serie.
> $\blacksquare$

> [!warning]
> En la teoría el método es impecable, pero en la **práctica** las integrales se vuelven enseguida
> impracticables: salvo casos felices como $y'=y$ (donde aparece una serie reconocible), evaluar
> $\int f(t,y_n)\,dt$ requiere primitivas que crecen en complejidad a cada paso y rara vez tienen forma
> cerrada. Por eso el valor de la iteración de Picard es sobre todo **teórico y conceptual** —prueba la
> existencia de la solución y muestra que es un límite controlado— más que un algoritmo de cálculo. Para
> aproximar numéricamente se usan métodos como Euler o Runge-Kutta, no Picard.

> [!proposicion] Relación con la serie de Taylor de la solución
> Cuando $f$ es analítica, la $n$-ésima iterada coincide con la solución **hasta el orden $x^{n}$**:
> cada iteración recupera un coeficiente más del desarrollo de Taylor de $y$ alrededor de $x_0$. Por eso
> en el ejemplo de $e^x$ las iteradas son literalmente las sumas parciales de la serie, y en
> $y'=x+y$ los primeros términos van fijándose uno a uno.

## Resumen

> [!resumen]
> | Elemento | Expresión | Papel |
> |---|---|---|
> | Semilla | $y_0(x)\equiv y_0$ | condición inicial como función constante |
> | Recurrencia | $y_{n+1}=y_0+\int_{x_0}^{x} f(t,y_n)\,dt$ | aplicar el operador $T$ una vez más |
> | Cota del incremento | $\|y_{n+1}-y_n\|\le \frac{M L^{n}}{(n+1)!}\|x-x_0\|^{n+1}$ | controla la convergencia |
> | Serie dominante | $\frac{M}{L}\bigl(e^{L\|x-x_0\|}-1\bigr)$ | mayorante convergente |
> | Límite | $y_n\to y$ **uniformemente** | la solución del PVI |
> | Ejemplo guía | $y'=y$: $y_n=\sum_{k\le n}\frac{x^k}{k!}\to e^x$ | iteradas = sumas parciales |

> [!corolario]
> La iteración de Picard convierte la existencia abstracta en un **proceso explícito**: la solución no
> es un objeto que "está ahí", sino el límite de una sucesión que se puede arrancar a mano. Su cota de
> error, dominada por una exponencial dividida entre factoriales, garantiza convergencia rápida; su
> límite es único porque el operador es una contracción. Es la cara algorítmica del determinismo que
> consagra [[Existencia y Unicidad Picard| Picard]].

> [!referencia]
> - El teorema que esta iteración demuestra de forma constructiva: [[Existencia y Unicidad Picard]].
> - La herramienta que cuantifica la convergencia y la unicidad: [[Desigualdad de Gronwall]].
> - La versión que pide solo continuidad: [[Teorema de Peano]].
> - Marco general: [[Fundamentos y Teoria Cualitativa/index]].
