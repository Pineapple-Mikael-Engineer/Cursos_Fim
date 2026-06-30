---
title: Método de la Secante y Orden de Convergencia φ
order: 5
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-no-lineales
  - metodos-abiertos
  - secante
  - convergencia
draft: false
aliases:
  - Método de la secante
  - Secant method
  - Orden de convergencia áureo
  - Convergencia superlineal
---

# Método de la Secante y Orden de Convergencia $\varphi$

> [!definicion]
> El **método de la secante** aproxima la raíz de $f(x) = 0$ sustituyendo la derivada de [[Derivacion Geometrica y Serie Taylor|Newton]] por una diferencia finita entre las dos últimas iteradas:
> $$x^{(k+1)} = x^{(k)} - f(x^{(k)})\,\frac{x^{(k)} - x^{(k-1)}}{f(x^{(k)}) - f(x^{(k-1)})}.$$
> Requiere dos puntos iniciales $x^{(0)}, x^{(1)}$ y **una sola** evaluación de $f$ por iteración.

> [!info]
> Es un método abierto: no garantiza convergencia, pero cuando converge lo hace con orden **superlineal** $p = \varphi = \tfrac{1+\sqrt5}{2} \approx 1.618$ (la razón áurea), intermedio entre la [[Biseccion|bisección]] lineal y [[Orden Convergencia Cuadratica Simple|Newton]] cuadrático, sin necesitar la derivada de $f$.

---

## Interpretación geométrica

> [!teoria]
> Newton usa la **tangente** a $f$ en $x^{(k)}$; la secante usa la **recta secante** por los puntos $(x^{(k-1)}, f(x^{(k-1)}))$ y $(x^{(k)}, f(x^{(k)}))$. La nueva iterada es la abscisa donde esa secante corta el eje $x$. La pendiente de la secante,
> $$\frac{f(x^{(k)}) - f(x^{(k-1)})}{x^{(k)} - x^{(k-1)}} \approx f'(x^{(k)}),$$
> aproxima la derivada por una diferencia finita: la secante es "Newton sin derivada".

---

## Ejemplo

> [!ejemplo]
> **Raíz de $f(x) = x^2 - 2$, $r = \sqrt2 \approx 1.414213562373095$, con $x^{(0)} = 2$, $x^{(1)} = 1.5$.**
>
> | $k$ | $x^{(k)}$ | $f(x^{(k)})$ | error $e^{(k)}$ |
> |:---|:---|:---|:---|
> | 0 | 2.000000000 | 2.000000 | 5.86e-1 |
> | 1 | 1.500000000 | 0.250000 | 8.58e-2 |
> | 2 | 1.411764706 | $-7.61\text{e-}3$ | 2.45e-3 |
> | 3 | 1.414211438 | $-6.01\text{e-}6$ | 2.12e-6 |
> | 4 | 1.414213562 | $1.46\text{e-}11$ | 5.16e-12 |
> | 5 | 1.414213562 | $\approx 0$ | $<10^{-15}$ |
>
> Los dígitos correctos crecen $\approx 1.6\times$ por iteración (0 → 1 → 3 → 6 → 12), no se duplican como en Newton ni avanzan a paso fijo como en bisección.

---

## Orden de convergencia $\varphi$

> [!teorema]
> Si $f \in C^2$ en una vecindad de una raíz simple $r$ ($f'(r) \neq 0$), el método de la secante converge localmente con orden $p = \varphi = \tfrac{1+\sqrt5}{2}$:
> $$\lim_{k\to\infty}\frac{|e^{(k+1)}|}{|e^{(k)}|^{\varphi}} = C^{1/\varphi}, \qquad C = \left|\frac{f''(r)}{2f'(r)}\right|.$$

> [!demostracion]
> **Paso 1: relación de error.** Por análisis de la fórmula de la secante con desarrollo de Taylor alrededor de $r$ se obtiene, con $C = |f''(r)/2f'(r)|$:
> $$e^{(k+1)} \approx C\, e^{(k)} e^{(k-1)}.$$
> El error nuevo es proporcional al **producto** de los dos errores previos (no al cuadrado de uno, como Newton).
>
> **Paso 2: ansatz de orden.** Supóngase $|e^{(k+1)}| \approx K\,|e^{(k)}|^{p}$. Entonces $|e^{(k)}| \approx K|e^{(k-1)}|^p$, de donde $|e^{(k-1)}| \approx (|e^{(k)}|/K)^{1/p}$. Sustituyendo en la relación del Paso 1:
> $$K|e^{(k)}|^p \approx C\,|e^{(k)}|\,(|e^{(k)}|/K)^{1/p} = C K^{-1/p}\,|e^{(k)}|^{1 + 1/p}.$$
>
> **Paso 3: ecuación del exponente.** Igualando exponentes de $|e^{(k)}|$:
> $$p = 1 + \frac1p \;\Longrightarrow\; p^2 - p - 1 = 0 \;\Longrightarrow\; p = \frac{1+\sqrt5}{2} = \varphi \approx 1.618.$$
> La constante sale de igualar coeficientes: $K = C^{1/\varphi}$.

---

## Eficiencia: por qué a veces supera a Newton

> [!info]
> El **índice de eficiencia** de un método es $E = p^{1/m}$, donde $m$ es el número de evaluaciones de función por iteración. Comparando coste por evaluación:
>
> | Método | Orden $p$ | Evaluaciones/iter $m$ | Eficiencia $p^{1/m}$ |
> |:---|:---:|:---:|:---:|
> | [[Biseccion]] | 1 | 1 ($f$) | 1.000 |
> | **Secante** | 1.618 | 1 ($f$) | **1.618** |
> | [[Orden Convergencia Cuadratica Simple\|Newton]] | 2 | 2 ($f$ y $f'$) | $\sqrt2 \approx 1.414$ |
>
> Si evaluar $f'$ cuesta tanto como evaluar $f$, la secante es **más eficiente** que Newton por evaluación, además de no requerir la derivada analítica.

---

## Ventajas y limitaciones

> [!info]
> **Ventajas.**
> - No requiere la derivada $f'$ (útil si es cara o no se conoce en forma cerrada).
> - Una sola evaluación de $f$ por paso.
> - Convergencia superlineal, mayor eficiencia por evaluación que Newton.

> [!warning]
> **Limitaciones.**
> - **No garantiza convergencia:** como método abierto, puede diverger u oscilar si los puntos iniciales están lejos de $r$ (véase [[Criterios Fallo Divergencia Oscilacion]]).
> - **División por diferencias pequeñas:** si $f(x^{(k)}) \approx f(x^{(k-1)})$, la pendiente se vuelve numéricamente inestable ([[Perdida Significancia y Cancelacion Catastrofica|cancelación]]).
> - **Raíces múltiples:** el orden cae a lineal, como en [[Convergencia Lineal Raices Multiples|Newton]].
> - No encierra la raíz: a diferencia de [[Regula Falsi]], no mantiene un intervalo con cambio de signo.

---

## Secante frente a Regula Falsi

> [!info]
> Ambos usan una recta secante, pero difieren en qué puntos retienen:
>
> | | Secante | [[Regula Falsi]] |
> |:---|:---|:---|
> | Puntos usados | las dos **últimas** iteradas | un par con $f$ de **signos opuestos** |
> | Encierra la raíz | no | sí |
> | Convergencia | superlineal ($\varphi$), no garantizada | lineal, garantizada |
> | Riesgo | divergencia | estancamiento de un extremo |

---

## Algoritmo

> [!algoritmo]
> **Implementación en Python.**
>
> ```python
> def secante(f, x0, x1, tol=1e-12, max_iter=100):
>     """Método de la secante para f(x)=0 con dos puntos iniciales."""
>     f0, f1 = f(x0), f(x1)
>     for k in range(max_iter):
>         if f1 == f0:
>             raise ZeroDivisionError("Diferencia de f nula: pendiente indefinida")
>         x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
>         if abs(x2 - x1) < tol:
>             return x2, k + 1
>         x0, f0 = x1, f1
>         x1, f1 = x2, f(x2)
>     return x1, max_iter
>
> # Ejemplo
> f = lambda x: x**2 - 2
> raiz, iters = secante(f, 2.0, 1.5)
> print(f"Raíz: {raiz}, iteraciones: {iters}")
> ```

---

## Relación con otras notas

> [!info]
> - Es la versión sin derivada de [[Derivacion Geometrica y Serie Taylor|Newton-Raphson]]; comparte estructura con [[Orden Convergencia Cuadratica Simple]].
> - El intervalo que la secante no mantiene sí lo conserva [[Regula Falsi]].
> - Comparación cuantitativa de todos los órdenes: [[Comparacion Analitica Orden Convergencia]].
> - Modos de fallo de los métodos abiertos: [[Criterios Fallo Divergencia Oscilacion]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Iteración | $x^{(k+1)} = x^{(k)} - f(x^{(k)})\frac{x^{(k)}-x^{(k-1)}}{f(x^{(k)})-f(x^{(k-1)})}$ |
| Puntos iniciales | dos ($x^{(0)}, x^{(1)}$) |
| Evaluaciones/iter | 1 (solo $f$) |
| Orden | $\varphi = \frac{1+\sqrt5}{2} \approx 1.618$ (superlineal) |
| Relación de error | $e^{(k+1)} \approx C\,e^{(k)}e^{(k-1)}$ |
| Eficiencia | $1.618 >$ Newton ($1.414$) por evaluación |

> [!corolario]
> El método de la secante reemplaza la derivada de Newton por una diferencia finita entre las dos últimas iteradas, logrando convergencia superlineal de orden áureo $\varphi = \tfrac{1+\sqrt5}{2} \approx 1.618$ con una sola evaluación de $f$ por paso. La relación de error $e^{(k+1)} \approx C\,e^{(k)}e^{(k-1)}$ conduce a la ecuación $p^2 - p - 1 = 0$ cuya raíz positiva es $\varphi$. Aunque su orden es menor que el de Newton, su mayor índice de eficiencia por evaluación y la ausencia de derivada lo hacen preferible cuando $f'$ es costosa o desconocida. Su lugar exacto en la jerarquía de métodos se establece en [[Comparacion Analitica Orden Convergencia]].
