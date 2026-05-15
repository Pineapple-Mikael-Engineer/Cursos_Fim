---
title: Derivacion Geometrica y Serie Taylor
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-no-lineales
  - newton-raphson
draft: false
aliases:
  - Deducción del método de Newton
  - Demostración de convergencia de Newton
  - Interpretación geométrica de Newton
---

# Derivación Geométrica, Serie de Taylor y Demostración del Método de Newton

> [!definicion]
> El **método de Newton-Raphson** define la sucesión:
> $$x^{(k+1)} = x^{(k)} - \frac{f(x^{(k)})}{f'(x^{(k)})}$$
> partiendo de una aproximación inicial $x^{(0)}$. Esta nota presenta la motivación geométrica, la derivación mediante serie de Taylor y la demostración formal de convergencia.

---

## Ejemplo

> [!ejemplo]
> **Aproximar $\sqrt{2}$ usando $f(x)=x^2-2$, $x^{(0)}=2$.**
>
> | $k$ | $x^{(k)}$ | Error $\|x^{(k)} - \sqrt{2}\|$ |
> |:---|:---|:---|
> | 0 | 2.000000000 | 5.86e-01 |
> | 1 | 1.500000000 | 8.58e-02 |
> | 2 | 1.416666667 | 2.45e-03 |
> | 3 | 1.414215686 | 2.12e-06 |
> | 4 | 1.414213562 | 1.59e-12 |
>
> La convergencia es extremadamente rápida (cuadrática).

---

## Derivación geométrica (motivación)

> [!teoria]
> **Interpretación geométrica del método de Newton.**
>
> Sea $f: \mathbb{R} \to \mathbb{R}$ una función diferenciable. Dada una aproximación $x^{(k)}$ a una raíz $r$ de $f$, se construye la recta tangente a la curva $y = f(x)$ en el punto $(x^{(k)}, f(x^{(k)}))$.
>
> La ecuación de la recta tangente es:
> $$y = f(x^{(k)}) + f'(x^{(k)})(x - x^{(k)})$$
>
> Esta recta aproxima a la función $f$ en una vecindad de $x^{(k)}$. La siguiente aproximación $x^{(k+1)}$ se define como la raíz de esta recta tangente, es decir, el punto donde la recta corta al eje $x$ ($y=0$):
> $$0 = f(x^{(k)}) + f'(x^{(k)})(x^{(k+1)} - x^{(k)})$$
>
> Despejando $x^{(k+1)}$:
> $$-f(x^{(k)}) = f'(x^{(k)})(x^{(k+1)} - x^{(k)})$$
> $$x^{(k+1)} - x^{(k)} = -\frac{f(x^{(k)})}{f'(x^{(k)})}$$
> $$x^{(k+1)} = x^{(k)} - \frac{f(x^{(k)})}{f'(x^{(k)})}$$
>
> **Justificación de la idea:** Si la función es suficientemente suave y $x^{(k)}$ está cerca de la raíz, la tangente es una buena aproximación de $f$, por lo que la raíz de la tangente está cerca de la raíz de $f$. Este proceso iterativo refina sucesivamente la aproximación.

> [!ejemplo]
> **Aproximar $\sqrt{2}$ usando la tangente a $f(x)=x^2-2$ en $x_0=2$.**
>
> La tangente en $x_0=2$ tiene ecuación:
> $$y = f(2) + f'(2)(x-2) = 2 + 4(x-2) = 4x - 6$$
>
> La raíz de la tangente ($y=0$):
> $$0 = 4x - 6 \quad \Rightarrow \quad x = 1.5$$
>
> Este es exactamente $x_1$. Luego se repite el proceso en $x_1=1.5$:
> $$y = f(1.5) + f'(1.5)(x-1.5) = 0.25 + 3(x-1.5) = 3x - 4.25$$
> $$0 = 3x - 4.25 \quad \Rightarrow \quad x = 1.416666...$$

---

## Derivación mediante serie de Taylor (motivación)

> [!teoria]
> **Aproximación lineal por serie de Taylor.**
>
> Sea $f$ una función suficientemente diferenciable. La expansión en serie de Taylor de $f$ alrededor de $x^{(k)}$ es:
> $$f(x) = f(x^{(k)}) + f'(x^{(k)})(x - x^{(k)}) + \frac{f''(\xi)}{2}(x - x^{(k)})^2$$
>
> Si $x$ está cerca de $x^{(k)}$, el término cuadrático es pequeño. Truncando la serie al término lineal:
> $$f(x) \approx f(x^{(k)}) + f'(x^{(k)})(x - x^{(k)})$$
>
> Se busca $x = x^{(k+1)}$ tal que $f(x^{(k+1)}) = 0$. Sustituyendo en la aproximación lineal:
> $$0 \approx f(x^{(k)}) + f'(x^{(k)})(x^{(k+1)} - x^{(k)})$$
>
> Despejando:
> $$x^{(k+1)} = x^{(k)} - \frac{f(x^{(k)})}{f'(x^{(k)})}$$
>
> **Interpretación:** El método de Newton reemplaza la función $f$ por su aproximación lineal de Taylor en $x^{(k)}$ y calcula la raíz de esta aproximación lineal.

---

## Comparación entre ambas motivaciones

> [!info]
> | Aspecto | Derivación geométrica | Derivación por serie de Taylor |
> |:---|:---|:---|
> | Idea principal | Recta tangente | Aproximación lineal |
> | Requisito | $f$ diferenciable | $f$ diferenciable |
> | Formalismo | Visual, intuitivo | Analítico, más riguroso |
> | Utilidad | Comprensión geométrica | Análisis de error (teorema de convergencia) |

---

## Demostración formal de convergencia

> [!teorema]
> Sea $f \in C^2([a, b])$ (dos veces continuamente diferenciable) y sea $r \in (a, b)$ una raíz simple de $f$ ($f(r)=0$, $f'(r) \neq 0$). Entonces existe $\delta > 0$ tal que para todo $x^{(0)} \in (r-\delta, r+\delta)$, la sucesión definida por:
> $$x^{(k+1)} = x^{(k)} - \frac{f(x^{(k)})}{f'(x^{(k)})}$$
> converge a $r$. Además, la convergencia es cuadrática, es decir:
> $$\lim_{k \to \infty} \frac{|x^{(k+1)} - r|}{|x^{(k)} - r|^2} = \frac{|f''(r)|}{2|f'(r)|}$$

> [!demostracion]
> **Paso 1: Definición del error.**
>
> Sea $e^{(k)} = x^{(k)} - r$. Se quiere demostrar que si $|e^{(0)}|$ es suficientemente pequeño, entonces $e^{(k)} \to 0$.
>
> **Paso 2: Expresión de $f(x^{(k)})$ mediante serie de Taylor alrededor de $r$.**
>
> Expandemos $f$ hasta segundo orden:
> $$f(x^{(k)}) = f(r) + f'(r)(x^{(k)} - r) + \frac{f''(\xi_k)}{2}(x^{(k)} - r)^2$$
>
> Como $f(r)=0$:
> $$f(x^{(k)}) = f'(r) e^{(k)} + \frac{f''(\xi_k)}{2} (e^{(k)})^2$$
> donde $\xi_k$ está entre $x^{(k)}$ y $r$.
>
> **Paso 3: Expresión de $f'(x^{(k)})$ mediante serie de Taylor alrededor de $r$.**
>
> $$f'(x^{(k)}) = f'(r) + f''(\eta_k) e^{(k)}$$
> donde $\eta_k$ está entre $x^{(k)}$ y $r$.
>
> **Paso 4: Sustitución en la iteración de Newton.**
>
> La iteración es:
> $$x^{(k+1)} = x^{(k)} - \frac{f(x^{(k)})}{f'(x^{(k)})}$$
>
> Restando $r$:
> $$e^{(k+1)} = e^{(k)} - \frac{f'(r) e^{(k)} + \frac{f''(\xi_k)}{2} (e^{(k)})^2}{f'(r) + f''(\eta_k) e^{(k)}}$$
>
> **Paso 5: Simplificación algebraica.**
>
> Sea $A = f'(r) \neq 0$. Entonces:
> $$e^{(k+1)} = \frac{e^{(k)}(A + f''(\eta_k) e^{(k)}) - A e^{(k)} - \frac{f''(\xi_k)}{2} (e^{(k)})^2}{A + f''(\eta_k) e^{(k)}}$$
>
> Simplificando el numerador:
> $$e^{(k+1)} = \frac{\left(f''(\eta_k) - \frac{f''(\xi_k)}{2}\right) (e^{(k)})^2}{A + f''(\eta_k) e^{(k)}}$$
>
> **Paso 6: Acotación del error.**
>
> Existe una vecindad de $r$ donde $|f''(x)| \leq M$ y $|f'(x)| \geq m > 0$ (por continuidad de $f''$ y porque $f'(r) \neq 0$). Entonces, si $|e^{(k)}|$ es suficientemente pequeño (digamos $|e^{(k)}| \leq \delta$, con $\delta < \frac{m}{M}$ para que el denominador no se anule), se tiene:
> $$|e^{(k+1)}| \leq \frac{\left(M + \frac{M}{2}\right) |e^{(k)}|^2}{m - M\delta} = \frac{\frac{3M}{2}}{m - M\delta} |e^{(k)}|^2$$
>
> Definiendo $C = \frac{\frac{3M}{2}}{m - M\delta}$, se obtiene:
> $$|e^{(k+1)}| \leq C |e^{(k)}|^2$$
>
> **Paso 7: Condición para convergencia cuadrática.**
>
> Si además se elige $|e^{(0)}|$ tal que $C |e^{(0)}| < 1$, entonces:
> $$|e^{(1)}| \leq C |e^{(0)}|^2 = |e^{(0)}| \cdot (C |e^{(0)}|) < |e^{(0)}|$$
>
> **Paso 8: Inducción y convergencia.**
>
> Por inducción, si $|e^{(k)}| < \delta$ y $C |e^{(k)}| < 1$, entonces:
> $$|e^{(k+1)}| \leq C |e^{(k)}|^2 = |e^{(k)}| \cdot (C |e^{(k)}|) < |e^{(k)}|$$
>
> Además, la cota cuadrática implica:
> $$|e^{(k)}| \leq \frac{1}{C} (C |e^{(0)}|)^{2^k} \to 0$$
>
> Por lo tanto, $x^{(k)} \to r$ y la convergencia es cuadrática.


---

## Relación con el método de punto fijo

> [!info]
> Sea $g(x) = x - f(x)/f'(x)$. Entonces:
> $$g'(x) = \frac{f(x) f''(x)}{(f'(x))^2}$$
>
> En la raíz $r$, $f(r)=0$, por lo tanto $g'(r) = 0$. Esto explica la convergencia cuadrática:
> - Para raíces simples, $g'(r)=0$ → la constante asintótica es $c=0$
> - Para raíces múltiples, $g'(r) \neq 0$ → la convergencia se reduce a lineal

---

## Resumen

| Aspecto                       | Descripción                                                  |
| :---------------------------- | :----------------------------------------------------------- |
| **Motivación geométrica**     | Raíz de la recta tangente                                    |
| **Motivación analítica**      | Serie de Taylor truncada al término lineal                   |
| **Definición de la sucesión** | $x^{(k+1)} = x^{(k)} - f(x^{(k)})/f'(x^{(k)})$               |
| **Error**                     | $e^{(k)} = x^{(k)} - r$                                      |
| **Relación del error**        | $e^{(k+1)} = \frac{f''(\xi_k)}{2f'(x^{(k)})} (e^{(k)})^2$    |
| **Demostración**              | Serie de Taylor alrededor de $r$ y simplificación algebraica |
| **Convergencia**              | Local (existe vecindad de $r$ donde converge)                |
| **Orden**                     | Cuadrático ($p=2$) para raíces simples                       |

> [!corolario]
> El método de Newton se obtiene de dos maneras equivalentes: geométricamente como la raíz de la recta tangente, y analíticamente como la raíz de la aproximación lineal de Taylor. La demostración formal de convergencia se basa en definir el error $e^{(k)} = x^{(k)} - r$ y usar expansiones de Taylor de $f$ y $f'$ alrededor de $r$, obteniendo que $e^{(k+1)} = O((e^{(k)})^2)$. Esto demuestra que, si la aproximación inicial está suficientemente cerca de $r$, el error se reduce cuadráticamente, garantizando convergencia a la raíz. El análisis detallado del orden de convergencia cuadrática se profundiza en [[Newton Raphson/Orden Convergencia Cuadratica Simple]].