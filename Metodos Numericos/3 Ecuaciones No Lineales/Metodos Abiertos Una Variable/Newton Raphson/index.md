---
title: Newton Raphson
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-no-lineales
  - metodos-abiertos
  - newton-raphson
  - index
draft: false
aliases:
  - Método de Newton
  - Newton-Raphson method
  - Método de las tangentes
---

# Método de Newton-Raphson

> [!definicion]
> El **método de Newton-Raphson** (o simplemente método de Newton) es un método abierto iterativo para encontrar raíces de $f(x)=0$ que utiliza la derivada $f'(x)$. Partiendo de una aproximación inicial $x^{(0)}$, la iteración es:
> $$x^{(k+1)} = x^{(k)} - \frac{f(x^{(k)})}{f'(x^{(k)})}$$

> [!info]
> Es uno de los métodos más potentes y ampliamente utilizados para resolver ecuaciones no lineales. Su principal ventaja es la **convergencia cuadrática** (muy rápida) cuando se cumplen ciertas condiciones. Sin embargo, requiere calcular $f'(x)$ y puede diverger si la aproximación inicial no es suficientemente cercana a la raíz.

---

## Ejemplo

> [!ejemplo]
> **Encontrar la raíz de $f(x) = x^2 - 2$ usando Newton (solución $x = \sqrt{2} \approx 1.414213562$).**
>
> La derivada es $f'(x) = 2x$. La iteración:
> $$x^{(k+1)} = x^{(k)} - \frac{(x^{(k)})^2 - 2}{2x^{(k)}} = \frac{x^{(k)} + \frac{2}{x^{(k)}}}{2}$$
>
> Partiendo de $x^{(0)} = 2$:
>
> | $k$ | $x^{(k)}$ | Error $\|x^{(k)} - \sqrt{2}\|$ |
> |:---|:---|:---|
> | 0 | 2.000000000 | 5.86e-01 |
> | 1 | 1.500000000 | 8.58e-02 |
> | 2 | 1.416666667 | 2.45e-03 |
> | 3 | 1.414215686 | 2.12e-06 |
> | 4 | 1.414213562 | 1.59e-12 |
> | 5 | 1.414213562 | 0.00e+00 |
>
> **Observación:** El error se reduce aproximadamente al cuadrado en cada iteración (convergencia cuadrática). En 5 iteraciones se alcanza precisión de máquina.

---

## En qué consiste el método

> [!teoria]
> **Algoritmo de Newton-Raphson.**
>
> Dada una función $f$ diferenciable y una aproximación inicial $x^{(0)}$:
>
> 1. Calcular $f(x^{(k)})$ y $f'(x^{(k)})$
> 2. Actualizar: $x^{(k+1)} = x^{(k)} - \frac{f(x^{(k)})}{f'(x^{(k)})}$
> 3. Si $|x^{(k+1)} - x^{(k)}| < \text{tol}$ o $|f(x^{(k+1)})| < \text{tol}$, parar
> 4. Repetir desde el paso 1
>
> **Interpretación geométrica:**
>
> En cada iteración, se traza la recta tangente a $f$ en el punto $(x^{(k)}, f(x^{(k)}))$. La ecuación de la tangente es:
> $$y = f(x^{(k)}) + f'(x^{(k)})(x - x^{(k)})$$
>
> La intersección de esta recta con el eje $x$ ($y=0$) da la siguiente aproximación:
> $$0 = f(x^{(k)}) + f'(x^{(k)})(x^{(k+1)} - x^{(k)}) \Rightarrow x^{(k+1)} = x^{(k)} - \frac{f(x^{(k)})}{f'(x^{(k)})}$$

---

## Derivación geométrica y serie de Taylor

> [!info]
> La deducción formal del método de Newton, tanto desde la interpretación geométrica (tangente) como desde la expansión en serie de Taylor, se desarrolla en [[Derivacion Geometrica y Serie Taylor]].

---

## Orden de convergencia cuadrática (raíces simples)

> [!info]
> Para raíces simples ($f(r)=0$, $f'(r) \neq 0$), el método de Newton tiene convergencia cuadrática ($p=2$). El análisis detallado y la demostración se encuentran en [[Orden Convergencia Cuadratica Simple]].

---

## Convergencia lineal en raíces múltiples

> [!info]
> Cuando la raíz es múltiple ($f(r)=0$, $f'(r)=0$), la convergencia de Newton se reduce a lineal. Las modificaciones necesarias para recuperar convergencia cuadrática se estudian en [[Convergencia Lineal Raices Multiples]].

---

## Criterios de fallo, divergencia y oscilación

> [!info]
> El método de Newton no siempre converge. Las situaciones problemáticas (puntos críticos, ciclos, divergencia) y los criterios para detectarlas se analizan en [[Criterios Fallo Divergencia Oscilacion]].

---

## Método de la secante

> [!info]
> Una variante del método de Newton que evita el cálculo de la derivada aproximándola por diferencias finitas. Su orden de convergencia es superlineal ($p \approx 1.618$). Se desarrolla en [[Metodo Secante Orden Convergencia Fi]].

---

## Relación con el método de punto fijo

> [!info]
> El método de Newton puede verse como un caso particular del [[Punto Fijo Aproximaciones Sucesivas]] con función de iteración:
> $$g(x) = x - \frac{f(x)}{f'(x)}$$
>
> Para raíces simples, $g'(r) = 0$, lo que explica la convergencia cuadrática. Esta conexión es fundamental para entender por qué Newton es tan rápido: es un método de punto fijo con constante asintótica $c = 0$.

---

## Algoritmo

> [!algoritmo]
> **Pseudocódigo de Newton-Raphson.**
>
> ```
> función newton(f, df, x0, tol, max_iter)
>     x = x0
>     para k = 1 hasta max_iter
>         fx = f(x)
>         dfx = df(x)
>         si |dfx| < eps
>             error("Derivada cercana a cero")
>         x_nuevo = x - fx / dfx
>         si |x_nuevo - x| < tol o |fx| < tol
>             retornar x_nuevo, k
>         x = x_nuevo
>     retornar x, max_iter
> ```

> [!algoritmo]
> **Implementación en Python.**
>
> ```python
> def newton(f, df, x0, tol=1e-10, max_iter=100):
>     """
>     Método de Newton-Raphson para encontrar una raíz de f(x)=0.
>     
>     Parámetros:
>     - f: función
>     - df: derivada de f
>     - x0: aproximación inicial
>     - tol: tolerancia
>     - max_iter: iteraciones máximas
>     
>     Retorna:
>     - x: aproximación a la raíz
>     - iter: número de iteraciones
>     """
>     x = x0
>     
>     for k in range(max_iter):
>         fx = f(x)
>         dfx = df(x)
>         
>         if abs(dfx) < 1e-12:
>             raise ValueError("Derivada cercana a cero")
>         
>         x_new = x - fx / dfx
>         
>         if abs(x_new - x) < tol or abs(fx) < tol:
>             return x_new, k + 1
>         
>         x = x_new
>     
>     return x, max_iter
> 
> # Ejemplo
> f = lambda x: x**2 - 2
> df = lambda x: 2*x
> raiz, iters = newton(f, df, 2.0)
> print(f"Raíz: {raiz}")
> print(f"Iteraciones: {iters}")
> ```

---

## Limitaciones

> [!warning]
> **Limitaciones del método de Newton-Raphson.**
>
> 1. **Requiere derivada:** La función debe ser diferenciable y la derivada debe ser accesible (analítica o numérica).
> 2. **Derivada cercana a cero:** Si $f'(x^{(k)}) \approx 0$, la iteración puede divergir o producir valores extremadamente grandes.
> 3. **Convergencia local:** La convergencia cuadrática solo está garantizada si $x^{(0)}$ está suficientemente cerca de la raíz.
> 4. **Raíces múltiples:** La convergencia se reduce a lineal a menos que se modifique el método.
> 5. **Ciclos y oscilaciones:** Puede entrar en ciclos periódicos o divergir oscilatoriamente.

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| **Tipo** | Método abierto (requiere derivada) |
| **Iteración** | $x^{(k+1)} = x^{(k)} - f(x^{(k)})/f'(x^{(k)})$ |
| **Orden de convergencia** | Cuadrático ($p=2$) para raíces simples |
| **Constante asintótica** | $c = \frac{\|f''(r)\|}{2\|f'(r)\|}$ |
| **Ventaja** | Muy rápido (cuadrático) |
| **Desventaja** | Requiere derivada, convergencia local, puede fallar |

> [!corolario]
> El método de Newton-Raphson es el estándar de oro para resolver ecuaciones no lineales cuando se dispone de la derivada y se tiene una buena aproximación inicial. Su convergencia cuadrática lo hace extremadamente eficiente: los dígitos correctos se duplican en cada iteración. Sin embargo, su carácter local y la necesidad de calcular $f'(x)$ limitan su aplicabilidad en algunos contextos. Para raíces simples, es el método de elección. Para raíces múltiples o cuando la derivada no está disponible, se utilizan variantes como el [[Metodo Secante Orden Convergencia Fi]] o modificaciones del método de Newton.