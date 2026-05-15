---
title: Criterios Fallo Divergencia Oscilacion
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-no-lineales
  - newton-raphson
  - divergencia
  - oscilacion
draft: false
aliases:
  - Fallo de Newton
  - Divergencia de Newton
  - Ciclos de Newton
---

# Criterios de Fallo, Divergencia y Oscilación en Newton

> [!definicion]
> El método de Newton no siempre converge. Existen varias situaciones en las que el método puede fallar: divergencia, oscilación, ciclos periódicos o estancamiento. Esta nota clasifica y analiza estos comportamientos.

> [!info]
> En condiciones ideales (raíz simple, $f \in C^2$, $x^{(0)}$ suficientemente cerca de $r$), Newton converge cuadráticamente. Sin embargo, cuando estas condiciones no se cumplen, el método puede fallar de maneras espectaculares.

---

## Ejemplos de fallo

> [!ejemplo]
> **Cuatro comportamientos patológicos de Newton.**
>
> | Tipo | Ejemplo $f(x)$ | $x^{(0)}$ | Comportamiento |
> |:---|:---|:---|:---|
> | Ciclo de 2 | $x^3 - 2x + 2$ | $0$ | Alterna entre $0$ y $1$ |
> | Divergencia oscilatoria | $\arctan(x)$ | $1.5$ | Oscila creciendo en magnitud |
> | Ciclo de 3 | $x^3 - 2x + 2$ | $\approx -0.169$ | Alterna entre tres valores |
> | Derivada nula | $x^2 + 1$ (real) | $0$ | $f'(0)=0$, división por cero |
>
> Algunos de estos ejemplos se analizan en detalle a continuación.

---

## Puntos críticos y derivada nula

> [!teoria]
> **¿Qué ocurre cuando $f'(x^{(k)}) = 0$?**
>
> La iteración de Newton es:
> $$x^{(k+1)} = x^{(k)} - \frac{f(x^{(k)})}{f'(x^{(k)})}$$
>
> Si $f'(x^{(k)}) = 0$ pero $f(x^{(k)}) \neq 0$, la fórmula produce una división por cero. En la práctica, si $f'(x^{(k)})$ es muy pequeño, $x^{(k+1)}$ puede ser extremadamente grande (divergencia).
>
> **Si $f(x^{(k)}) = 0$ y $f'(x^{(k)}) = 0$:** La raíz es múltiple. En este caso, el método aún converge, pero solo linealmente (véase [[Convergencia Lineal Raices Multiples]]).

> [!ejemplo]
> **$f(x) = x^2 + 1$ con $x^{(0)} = 1$.**
>
> $f'(x) = 2x$.
>
> | $k$ | $x^{(k)}$ | $f(x^{(k)})$ | $f'(x^{(k)})$ | $x^{(k+1)}$ |
> |:---|:---|:---|:---|:---|
> | 0 | 1.0000 | 2.0000 | 2.0000 | 0.0000 |
> | 1 | 0.0000 | 1.0000 | 0.0000 | indefinido |
>
> El método alcanza un punto donde la derivada es nula antes de encontrar una raíz. La iteración deja de estar definida.

---

## Ciclos periódicos

> [!teoria]
> **Ciclos de periodo 2.**
>
> Un **ciclo de periodo 2** ocurre cuando $x^{(1)} \neq x^{(0)}$ pero $x^{(2)} = x^{(0)}$. Es decir:
> $$g(g(x^{(0)})) = x^{(0)} \quad \text{pero} \quad g(x^{(0)}) \neq x^{(0)}$$
>
> Esto significa que la iteración alterna entre dos valores sin converger.
>
> **Ciclos de periodo superior.** Existen funciones para las cuales Newton genera ciclos de periodo 3, 4, o cualquier otro. Estos comportamientos están relacionados con la teoría del caos en sistemas dinámicos.

> [!ejemplo]
> **$f(x) = x^3 - 2x + 2$ con $x^{(0)} = 0$.**
>
> $f'(x) = 3x^2 - 2$.
>
> | $k$ | $x^{(k)}$ | $f(x^{(k)})$ | $f'(x^{(k)})$ | $x^{(k+1)}$ |
> |:---|:---|:---|:---|:---|
> | 0 | 0.0000 | 2.0000 | -2.0000 | 1.0000 |
> | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 |
> | 2 | 0.0000 | 2.0000 | -2.0000 | 1.0000 |
>
> La iteración alterna entre $0$ y $1$ para siempre. No converge.

> [!ejemplo]
> **$f(x) = x^3 - 2x + 2$ con $x^{(0)} \approx -0.169$.**
>
> Para esta condición inicial, la iteración de Newton entra en un ciclo de periodo 3:
>
> $$x^{(0)} \to x^{(1)} \to x^{(2)} \to x^{(0)}$$
>
> Este es un ejemplo clásico de comportamiento caótico inducido por Newton. Pequeñas perturbaciones en $x^{(0)}$ pueden destruir el ciclo o producir divergencia.

---

## Divergencia

> [!teoria]
> **Tipos de divergencia.**
>
> 1. **Divergencia monótona:** $|x^{(k)}| \to \infty$ creciendo en cada iteración.
> 2. **Divergencia oscilatoria:** $x^{(k)}$ alterna signos y crece en magnitud.
> 3. **Divergencia caótica:** $x^{(k)}$ se comporta de manera impredecible.
>
> **Causas comunes:**
> - $x^{(0)}$ lejos de la raíz
> - $f'$ pequeña cerca de $x^{(k)}$
> - $f$ tiene asíntotas o comportamiento no lineal extremo

> [!ejemplo]
> **$f(x) = \arctan(x)$ con $x^{(0)} = 1.5$.**
>
> $f'(x) = 1/(1+x^2)$.
>
> | $k$ | $x^{(k)}$ | $x^{(k+1)}$ |
> |:---|:---|:---|
> | 0 | 1.5000 | -1.6949 |
> | 1 | -1.6949 | 2.3207 |
> | 2 | 2.3207 | -5.1279 |
>
> La sucesión alterna de signo mientras aumenta rápidamente en magnitud. Newton no converge hacia la raíz $r=0$.

---

## Sensibilidad a la condición inicial

> [!info]
> **El método de Newton es muy sensible a $x^{(0)}$.**
>
> Pequeños cambios en la condición inicial pueden llevar a:
> - Convergencia a diferentes raíces
> - Divergencia
> - Ciclos periódicos
>
> **Cuencas de atracción.**
>
> Para funciones con múltiples raíces, el conjunto de puntos que convergen a una raíz específica forma una **cuenca de atracción**. Estas cuencas pueden tener fronteras fractales, especialmente para polinomios complejos (conjunto de Julia).

> [!ejemplo]
> **$f(x) = x^3 - x$ (raíces en $-1, 0, 1$).**
>
> | Intervalo de $x^{(0)}$ | Raíz de convergencia |
> |:---|:---|
> | $\|x^{(0)}\| < 1/\sqrt{5}$ | $0$ |
> | $1/\sqrt{5} < x^{(0)} < 1$ | $-1$ |
> | $-1 < x^{(0)} < -1/\sqrt{5}$ | $1$ |
> | $x^{(0)} = \pm 1/\sqrt{5}$ | Ciclo periódico |
>
> Pequeñas variaciones en $x^{(0)}$ pueden cambiar completamente el comportamiento de la iteración.

---

## Estrategias para mitigar fallos

> [!info]
> **¿Qué hacer cuando Newton falla?**
>
> 1. **Usar un método de respaldo:** Combinar Newton con [[Biseccion]] o [[Regula Falsi]] cuando se detecta un problema.
>
> 2. **Atenuar el paso:** Usar Newton con relajación:
>    $$x^{(k+1)} = x^{(k)} - \omega \frac{f(x^{(k)})}{f'(x^{(k)})}, \quad \omega \in (0, 1)$$
>
> 3. **Método de Newton globalizado:** Incorporar búsqueda lineal (line search) para asegurar que $|f(x^{(k+1)})| < |f(x^{(k)})|$.
>
> 4. **Cambiar la condición inicial:** Si la primera aproximación conduce a divergencia, probar otro valor.
>
> 5. **Método de Newton con continuación:** Variar un parámetro para acercarse gradualmente a la raíz.
>
> 6. **Usar otros métodos:** Si Newton falla consistentemente, probar [[Metodo Secante Orden Convergencia Fi]] (no requiere derivada) o métodos de punto fijo.

---

## Relación con otras notas

> [!info]
> - La convergencia cuadrática en condiciones ideales se estudia en [[Orden Convergencia Cuadratica Simple]].
> - El caso de raíces múltiples (donde Newton converge pero es lineal) se desarrolla en [[Convergencia Lineal Raices Multiples]].
> - El [[Metodo Secante Orden Convergencia Fi]] puede ser más robusto en algunos casos patológicos porque no usa derivada.
> - Las condiciones globales de convergencia pueden analizarse con el teorema de [[Punto Fijo Aproximaciones Sucesivas/Teorema Punto Fijo Banach Contraccion]].

---

## Resumen

| Tipo de fallo | Causa | Ejemplo | Solución |
|:---|:---|:---|:---|
| **Derivada nula** | $f'(x^{(k)}) \approx 0$ | $x^2+1$ | Evitar puntos críticos |
| **Ciclo periódico** | $g(g(x^{(0)})) = x^{(0)}$ | $x^3-2x+2$, $x_0=0$ | Cambiar $x^{(0)}$ |
| **Divergencia** | $x^{(k)}$ se aleja | $\arctan(x)$ | Usar respaldo (bisección) |
| **Sensibilidad** | Fronteras complejas | $x^3-x$, $x_0=\pm1/\sqrt{5}$ | Métodos globales |

> [!corolario]
> El método de Newton es poderoso pero frágil. Su convergencia está garantizada solo bajo condiciones restrictivas (raíz simple, $x^{(0)}$ cerca de $r$). Fuera de estas condiciones, puede diverger, oscilar o caer en ciclos periódicos. En la práctica, se recomienda:
> - Combinar Newton con un método de respaldo (bisección, regula falsi) cuando se detecta fallo.
> - Usar técnicas de globalización (búsqueda lineal, continuación) para ampliar la región de convergencia.
> - Cuando la derivada es problemática, considerar el [[Metodo Secante Orden Convergencia Fi]].
>
> Para raíces múltiples (donde Newton converge pero lentamente), véase [[Convergencia Lineal Raices Multiples]].