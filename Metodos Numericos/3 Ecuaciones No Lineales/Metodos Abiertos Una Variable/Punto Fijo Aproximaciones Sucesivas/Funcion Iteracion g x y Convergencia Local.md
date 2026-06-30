---
title: Funcion Iteracion g x y Convergencia Local
order: 2
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-no-lineales
  - punto-fijo
draft: false
aliases:
  - Función de iteración
  - Convergencia local punto fijo
  - Condición |g'(r)| < 1
---

# Función de Iteración y Convergencia Local

> [!definicion]
> Dada una ecuación $f(x)=0$, el **método de punto fijo** consiste en reescribirla como $x = g(x)$ e iterar:
> $$x^{(k+1)} = g(x^{(k)})$$
>
> La función $g$ se llama **función de iteración**. La convergencia local del método depende del valor de $g'(r)$ en la raíz $r$.

> [!info]
> El [[Teorema Punto Fijo Banach Contraccion]] proporciona condiciones suficientes para convergencia global. En la práctica, se utiliza la condición más débil de **convergencia local**: $|g'(r)| < 1$ es suficiente para garantizar convergencia en una vecindad de $r$.

---

## Ejemplo

> [!ejemplo]
> **Diferentes funciones de iteración para $f(x) = x^2 - x - 1 = 0$ (raíz $r \approx 1.618$).**
>
> | Forma | $g(x)$ | $g'(r)$ | $\|g'(r)\|$ | ¿Converge? |
> |:---|:---|:---|:---|:---|
> | 1 | $x^2 - 1$ | $2r \approx 3.236$ | $3.236 > 1$ | No |
> | 2 | $\sqrt{x+1}$ | $\frac{1}{2\sqrt{r+1}} \approx 0.309$ | $0.309 < 1$ | Sí (rápida) |
> | 3 | $1 + 1/x$ | $-\frac{1}{r^2} \approx -0.382$ | $0.382 < 1$ | Sí (lenta) |
> | 4 | $\frac{x^2+1}{2x-1}$ | derivada en $r$ es $0$ | $0$ | Sí (cuadrática) |
>
> **Observación:** Cuanto menor es $|g'(r)|$, más rápida es la convergencia. Cuando $g'(r)=0$, la convergencia es al menos cuadrática.

---

## Construcción de la función de iteración

> [!teoria]
> **Estrategias para construir $g$ a partir de $f$.**
>
> 1. **Método directo:** Despejar $x$ de $f(x)=0$ cuando sea posible.
>    $$f(x) = x^2 - x - 1 = 0 \quad \Rightarrow \quad x = \sqrt{x+1}$$
>
> 2. **Método de suma:** $g(x) = x + c f(x)$ con $c \neq 0$.
>    $$g(x) = x + c(x^2 - x - 1)$$
>    La derivada en la raíz es $g'(r) = 1 + c f'(r)$. Para convergencia local, se necesita $|1 + c f'(r)| < 1$.
>
> 3. **Método de Newton (caso particular):** $g(x) = x - \frac{f(x)}{f'(x)}$, que logra $g'(r) = 0$ para raíces simples.
>
> 4. **Método de Aitken ($\Delta^2$):** Técnica de aceleración de convergencia que transforma una sucesión linealmente convergente en una superlinealmente convergente. Dada una sucesión $\{x^{(k)}\}$ generada por punto fijo, se define:
>    $$\hat{x}^{(k)} = x^{(k)} - \frac{(x^{(k+1)} - x^{(k)})^2}{x^{(k+2)} - 2x^{(k+1)} + x^{(k)}}$$
>
> 5. **Método de Steffensen:** Combina el método de punto fijo con la aceleración de Aitken, pero aplicando la aceleración en cada iteración sin necesidad de esperar a tres términos. La iteración es:
>    $$x^{(k+1)} = x^{(k)} - \frac{(g(x^{(k)}) - x^{(k)})^2}{g(g(x^{(k)})) - 2g(x^{(k)}) + x^{(k)}}$$
>    Este método logra convergencia cuadrática sin usar derivadas, similar a Newton.

> [!info]
> El método de Steffensen es especialmente útil cuando $f$ es diferenciable pero su derivada es costosa o difícil de calcular, o cuando se trabaja con funciones definidas por procedimientos complejos.

---
---

## Condición de convergencia local

> [!teorema] [Convergencia local del método de punto fijo]
> Sea $r$ un punto fijo de $g$ ($r = g(r)$) y supóngase que $g$ es continuamente diferenciable en una vecindad de $r$. Si $|g'(r)| < 1$, entonces existe $\delta > 0$ tal que para todo $x^{(0)} \in (r-\delta, r+\delta)$, la sucesión $x^{(k+1)} = g(x^{(k)})$ converge a $r$.
>
> Si $|g'(r)| > 1$, el método diverge (es decir, no existe vecindad de convergencia).

> [!demostracion]
> **Paso 1: Estimación del error.**
>
> Por el teorema del valor medio, para $x$ cercano a $r$:
> $$g(x) - r = g(x) - g(r) = g'(\xi)(x - r)$$
> donde $\xi$ está entre $x$ y $r$.
>
> Como $g'$ es continua y $|g'(r)| < 1$, existe $\delta > 0$ tal que para todo $x \in I = [r-\delta, r+\delta]$ se tiene $|g'(x)| \leq L < 1$ (tomar $L = (|g'(r)| + 1)/2$, por ejemplo).
>
> **Paso 2: Contracción local.**
>
> Si $x \in I$, entonces:
> $$|g(x) - r| = |g'(\xi)| |x - r| \leq L |x - r| \leq L \delta < \delta$$
>
> Por lo tanto, $g(I) \subset I$ y $g$ es contracción en $I$ con constante $L < 1$.
>
> **Paso 3: Aplicación del teorema de Banach.**
>
> Por el [[Teorema Punto Fijo Banach Contraccion]], la iteración converge a $r$ desde cualquier $x^{(0)} \in I$.
>
> **Paso 4: Divergencia si $|g'(r)| > 1$.**
>
> Si $|g'(r)| > 1$, por continuidad existe $\delta > 0$ tal que $|g'(x)| \geq \mu > 1$ para $x \in I$. Entonces para $x^{(0)} \neq r$:
> $$|x^{(1)} - r| = |g(x^{(0)}) - g(r)| = |g'(\xi)| |x^{(0)} - r| \geq \mu |x^{(0)} - r|$$
>
> El error crece en cada iteración, por lo que no hay convergencia.

> [!corolario]
> **Caso borde $|g'(r)| = 1$:** No se puede concluir. Puede converger o diverger dependiendo de términos de orden superior.

---

## Relación con el teorema de Banach

> [!info]
> **Diferencias entre convergencia global y local.**
>
> | Aspecto | Teorema de Banach (global) | Convergencia local |
> |:---|:---|:---|
> | Condición | $\max_{x \in I} \|g'(x)\| < 1$ | $\|g'(r)\| < 1$ |
> | Invarianza | $g(I) \subset I$ requerida | Automática en vecindad suficientemente pequeña |
> | Dominio | Todo $I$ | Solo una vecindad de $r$ |
> | Utilidad | Teórica, difícil de verificar | Práctica, fácil de verificar |
>
> En la práctica, se verifica $|g'(r)| < 1$ evaluando $g'$ en la raíz aproximada. Si se cumple, se sabe que existe una vecindad de convergencia, aunque no se conozca su tamaño.

---

## Elección óptima de $g$

> [!info]
> **¿Cuál es la mejor función de iteración?**
>
> La convergencia del método de punto fijo es lineal con constante asintótica $|g'(r)|$. Por lo tanto:
>
> - Cuanto menor sea $|g'(r)|$, más rápida es la convergencia.
> - Si $g'(r) = 0$, la convergencia es al menos cuadrática.
>
> **Método de Newton:** $g(x) = x - \frac{f(x)}{f'(x)}$ tiene $g'(r) = 0$ para raíces simples. Por eso Newton converge cuadráticamente.
>
> **Método de la secante:** Puede verse como una aproximación a Newton sin derivadas, con convergencia superlineal ($p \approx 1.618$).
>
> **Estrategia:** Si se conoce una aproximación de $f'(r)$, se puede elegir $g(x) = x - \frac{f(x)}{f'(r)}$, que es lineal pero con $g'(r) = 0$.

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| **Construcción de $g$** | Reescribir $f(x)=0$ como $x=g(x)$ |
| **Condición suficiente** | $\|g'(r)\| < 1$ |
| **Tipo de convergencia** | Local (existe vecindad de convergencia) |
| **Orden de convergencia** | Lineal ($p=1$), a menos que $g'(r)=0$ |
| **Constante asintótica** | $\|g'(r)\|$ |
| **Caso óptimo** | $g'(r)=0$ → convergencia al menos cuadrática (ej: Newton) |

> [!corolario]
> La convergencia local del método de punto fijo está determinada por $|g'(r)|$. Si $|g'(r)| < 1$, el método converge para condiciones iniciales suficientemente cercanas a la raíz. Cuanto menor sea $|g'(r)|$, más rápida es la convergencia. El [[Teorema Punto Fijo Banach Contraccion]] proporciona condiciones más fuertes (globales) que no siempre son necesarias. El [[Newton Raphson/index]] es un caso particular con $g'(r)=0$, lo que explica su convergencia cuadrática. El análisis de la constante asintótica y el orden de convergencia se profundiza en [[Orden Convergencia Lineal Constante Asintotica]].

