---
title: Reducción de Orden
tags:
  - ecuaciones
  - edo
  - teoria
  - lineales
  - segunda-solucion
draft: false
aliases:
  - reducción de orden
  - segunda solución
  - método de d'Alembert
  - reduction of order
---

# Reducción de Orden

> [!definicion]
> Dada **una** solución $y_1(x)$ de la EDO lineal homogénea de segundo orden
> $$y''+p(x)\,y'+q(x)\,y=0,$$
> la **reducción de orden** halla una segunda solución independiente con la sustitución
> $$y_2=v(x)\,y_1(x).$$
> Al sustituir, **los términos en $v$ se cancelan** (precisamente porque $y_1$ ya es solución), y lo que
> queda es una ecuación de **primer orden** en la incógnita $w=v'$. Resolverla y luego integrar da
> $v$, y con él $y_2$. Es la herramienta para coeficientes **variables** cuando se conoce una solución, y
> es lo que **justifica el factor $x$** de las raíces repetidas en [[Coeficientes Constantes Homogenea]].

> [!info]
> Pieza del bloque [[Lineales de Orden Superior/index| lineales de orden superior]]. Resuelve el
> problema "tengo $y_1$, ¿de dónde saco $y_2$?". El resultado coincide con el que entrega la
> [[Formula de Abel| fórmula de Abel]] para el wronskiano, y es la base teórica del segundo término en
> el caso repetido de [[Coeficientes Constantes Homogenea| coeficientes constantes]] y de
> [[Cauchy-Euler| Cauchy-Euler]].

---

## Ejemplo

> [!ejemplo] Recuperar el factor $x$ de una raíz repetida
> **La EDO $y''-4y'+4y=0$ tiene la raíz doble $r=2$**, así que $y_1=e^{2x}$. Hallemos $y_2$ por
> reducción de orden y veamos aparecer el factor $x$.
>
> **Paso 1 — identificar $p$.** Aquí $p(x)=-4$, de modo que $e^{-\int p\,dx}=e^{\int 4\,dx}=e^{4x}$.
>
> **Paso 2 — usar la fórmula** $\displaystyle y_2=y_1\int\frac{e^{-\int p\,dx}}{y_1^2}\,dx$. Con
> $y_1^2=(e^{2x})^2=e^{4x}$:
> $$y_2=e^{2x}\int\frac{e^{4x}}{e^{4x}}\,dx=e^{2x}\int 1\,dx=e^{2x}\cdot x=x\,e^{2x}.$$
>
> **Conclusión.** $y_2=xe^{2x}$. **Esto justifica el factor $x$**: cuando la raíz se repite, $y_1$ y
> $y_1^2$ se cancelan exactamente con $e^{-\int p}$, la integral da $\int dx=x$, y por eso la segunda
> solución es $x$ veces la primera. La solución general es $y=(c_1+c_2x)e^{2x}$.

> [!ejemplo] Coeficientes variables: aparece un $\ln x$
> **La EDO $x^2y''-3xy'+4y=0$ tiene la solución $y_1=x^2$** (una [[Cauchy-Euler| Cauchy-Euler]] con
> raíz doble $m=2$). Para usar la fórmula la escribimos en forma estándar dividiendo entre $x^2$:
> $$y''-\frac{3}{x}y'+\frac{4}{x^2}y=0\;\Rightarrow\; p(x)=-\frac{3}{x}.$$
> Entonces $\displaystyle \int p\,dx=-3\ln x$, luego $e^{-\int p\,dx}=e^{3\ln x}=x^3$, y $y_1^2=x^4$:
> $$y_2=x^2\int\frac{x^3}{x^4}\,dx=x^2\int\frac{dx}{x}=x^2\ln x.$$
> La segunda solución es $y_2=x^2\ln x$: el análogo del factor $x$, pero con $\ln x$, típico de las
> ecuaciones equidimensionales con raíz repetida.

---

## En qué consiste

> [!teoria] La idea: "ya tengo una dirección, busco la otra"
> El espacio de soluciones de la homogénea de segundo orden tiene **dimensión $2$**. Conocer $y_1$ es
> tener **una** dirección de ese plano; falta una segunda independiente. En vez de buscarla a ciegas, se
> propone $y_2=v(x)y_1$ —"$y_1$ deformada por un factor variable $v$"—. Si $v$ fuera constante, $y_2$
> sería proporcional a $y_1$ (dependiente); la novedad la trae $v(x)$ no constante. Al meter este ansatz
> en la EDO, el hecho de que $y_1$ **ya** sea solución elimina el término sin derivar de $v$, **bajando
> el orden** de la ecuación para $v$: queda primer orden en $w=v'$, que siempre se resuelve por factor
> integrante o por separación de variables.

> [!teorema] Fórmula de la segunda solución
> Si $y_1$ resuelve $y''+p(x)y'+q(x)y=0$ y $y_1\neq0$ en el intervalo, entonces
> $$y_2=y_1(x)\int\frac{e^{-\int p(x)\,dx}}{y_1(x)^2}\,dx$$
> es una segunda solución **linealmente independiente** de $y_1$.

> [!demostracion] De la sustitución $y=vy_1$ a la fórmula
> **Paso 1 — derivar el producto.** Con $y=v\,y_1$:
> $$y'=v'y_1+vy_1',\qquad y''=v''y_1+2v'y_1'+vy_1''.$$
>
> **Paso 2 — sustituir y agrupar por $v$.** Metemos en $y''+py'+qy=0$ y agrupamos según deriven a $v$:
> $$v''\,y_1+v'\big(2y_1'+py_1\big)+v\big(\underbrace{y_1''+py_1'+qy_1}_{=\,0}\big)=0.$$
> El paréntesis que multiplica a $v$ es **exactamente la EDO evaluada en $y_1$**, y vale $0$ porque
> $y_1$ es solución. Esa cancelación es el corazón del método. Queda
> $$y_1v''+\big(2y_1'+py_1\big)v'=0.$$
>
> **Paso 3 — bajar a primer orden con $w=v'$.** La ecuación es de primer orden en $w$:
> $$y_1w'+\big(2y_1'+py_1\big)w=0\;\Rightarrow\;\frac{w'}{w}=-\left(\frac{2y_1'}{y_1}+p\right).$$
> Integrando, $\ln w=-2\ln y_1-\int p\,dx+\text{const}$, es decir
> $$w=\frac{C\,e^{-\int p\,dx}}{y_1^2}.$$
>
> **Paso 4 — integrar para recuperar $v$ y $y_2$.** Como $w=v'$, integramos una vez más y tomamos
> $C=1$ (cualquier constante sirve, las generales las dan $c_1,c_2$):
> $$v=\int\frac{e^{-\int p\,dx}}{y_1^2}\,dx,\qquad y_2=v\,y_1=y_1\int\frac{e^{-\int p\,dx}}{y_1^2}\,dx.$$
> Esto **coincide** con lo que predice la [[Formula de Abel| fórmula de Abel]] $W=W_0e^{-\int p}$ para
> el wronskiano del par $\{y_1,y_2\}$. $\blacksquare$

> [!proposicion] Por qué $y_2$ es independiente de $y_1$
> El cociente $y_2/y_1=v=\int w\,dx$ con $w=e^{-\int p}/y_1^2\neq0$, así que $v$ es **no constante**.
> Dos soluciones cuyo cociente no es constante son linealmente independientes; por tanto $\{y_1,y_2\}$
> es un conjunto fundamental y la solución general es $y=c_1y_1+c_2y_2$.

> [!algoritmo] Reducción de orden, paso a paso
> 1. Ten **una** solución $y_1$ y escribe la EDO en **forma estándar** $y''+py'+qy=0$ (coeficiente de $y''$ igual a $1$) para leer $p$.
> 2. Propón $y_2=v\,y_1$.
> 3. Resuelve la ecuación de **primer orden** en $w=v'$: $\ \displaystyle w=\dfrac{e^{-\int p\,dx}}{y_1^2}$.
> 4. **Integra** $v=\int w\,dx$.
> 5. Escribe $y_2=v\,y_1$ y la general $y=c_1y_1+c_2y_2$.

## Resumen

> [!resumen]
> | Elemento | Expresión |
> |---|---|
> | Punto de partida | una solución $y_1$ de $y''+py'+qy=0$ |
> | Sustitución | $y_2=v(x)\,y_1(x)$ |
> | Lo que se cancela | el término en $v$: $y_1''+py_1'+qy_1=0$ |
> | Ecuación reducida | $y_1v''+(2y_1'+py_1)v'=0$, primer orden en $w=v'$ |
> | Resultado | $\displaystyle y_2=y_1\int\frac{e^{-\int p\,dx}}{y_1^2}\,dx$ |

> [!corolario]
> Reducción de orden convierte "buscar una segunda solución de una EDO de segundo orden" en "resolver
> una de primer orden", aprovechando la solución que ya se tiene. Es a la vez una **herramienta
> práctica** (coeficientes variables con una solución conocida) y la **justificación teórica** del factor
> $x$ en raíces repetidas de [[Coeficientes Constantes Homogenea]] y del $\ln x$ en
> [[Cauchy-Euler| Cauchy-Euler]].

> [!referencia]
> - El wronskiano que esta fórmula reproduce: [[Formula de Abel]].
> - El factor $x$ que justifica: [[Coeficientes Constantes Homogenea]].
> - Aplicación a ecuaciones equidimensionales: [[Cauchy-Euler]].
> - El bloque completo: [[Lineales de Orden Superior/index]].
