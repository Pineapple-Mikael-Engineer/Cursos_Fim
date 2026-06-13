---
title: Regla del Trapecio y Error de Truncamiento
tags:
  - metodos-numericos
  - teoria
  - diferenciacion-integracion
  - integracion-numerica
  - newton-cotes
draft: false
aliases:
  - Regla del trapecio
  - Trapezoidal rule
  - Error del trapecio
---

# Regla del Trapecio y Error de Truncamiento

> [!definicion]
> La **regla del trapecio** aproxima $\int_a^b f(x)\,dx$ por el área del trapecio bajo la recta que une $(a, f(a))$ y $(b, f(b))$. Con $h = b - a$:
> $$\int_a^b f(x)\,dx \approx \frac{h}{2}\big(f(a) + f(b)\big).$$

> [!info]
> Es la regla de [[Reglas Cerradas/index|Newton-Cotes]] de grado $1$: integra el [[Splines Lineales Continuidad C0|interpolante lineal]] de $f$. Simple y robusta, su error depende de $f''$, lo que la hace exacta para funciones lineales y base de la integración compuesta y de [[Extrapolacion Richardson Aceleracion Convergencia|Romberg]].

---

## Error de truncamiento

> [!teorema]
> Si $f \in C^2[a,b]$, existe $\xi \in (a,b)$ tal que
> $$\int_a^b f(x)\,dx = \frac{h}{2}\big(f(a)+f(b)\big) - \frac{h^3}{12}f''(\xi), \qquad h = b-a.$$
> El error es $O(h^3)$ por panel y proporcional a $f''$: nulo para funciones lineales.

> [!demostracion]
> El error es la integral del [[Error Interpolacion Formula Cauchy|error de interpolación]] lineal $e(x) = \frac{f''(\xi_x)}{2}(x-a)(x-b)$:
> $$\int_a^b f - \frac{h}{2}(f_0+f_1) = \int_a^b \frac{f''(\xi_x)}{2}(x-a)(x-b)\,dx.$$
> Como $(x-a)(x-b) \leq 0$ en $[a,b]$ (no cambia de signo), por el teorema del valor medio para integrales se extrae $f''(\xi)$:
> $$= \frac{f''(\xi)}{2}\int_a^b (x-a)(x-b)\,dx = \frac{f''(\xi)}{2}\cdot\left(-\frac{h^3}{6}\right) = -\frac{h^3}{12}f''(\xi).$$

---

## Ejemplo

> [!ejemplo]
> **$\int_0^1 e^x\,dx = e - 1 \approx 1.71828$** con trapecio simple ($h=1$):
> $$\frac{1}{2}(e^0 + e^1) = \frac{1}{2}(1 + 2.71828) = 1.85914, \qquad \text{error} = 0.14086.$$
> La cota predice $|E| \leq \frac{1}{12}\max|f''| = \frac{e}{12} \approx 0.226$, consistente. El error positivo del método (sobrestima) corresponde a $f'' > 0$ (función convexa): el trapecio queda por encima de la curva.

---

## Interpretación geométrica

> [!teoria]
> Para $f$ **convexa** ($f'' > 0$), la cuerda está por encima de la curva, así que el trapecio **sobrestima** la integral ($E < 0$ en la convención $\int = \text{trap} + E$, es decir el método da de más). Para $f$ cóncava, subestima. El signo del error lo fija el de $f''$, coherente con $-\frac{h^3}{12}f''$.

---

## Ventajas y limitaciones

> [!info]
> **Ventajas.** Trivial, robusta, exacta para lineales, base de [[Trapecio Compuesto Convergencia O h2|trapecio compuesto]] y [[Extrapolacion Richardson Aceleracion Convergencia|Romberg]]. Para funciones **periódicas** integradas sobre un período, es sorprendentemente precisa (convergencia espectral).

> [!warning]
> **Limitaciones.** Solo $O(h^3)$ por panel (grado de exactitud $1$); para integrandos curvados es poco precisa frente a [[Simpson 1 3 Orden Precision y Error Cuarta Derivada|Simpson]]. Requiere subdivisión para precisión razonable.

---

## Algoritmo

> [!algoritmo]
> **Trapecio simple y compuesto.**
>
> ```python
> def trapecio(f, a, b):
>     return 0.5 * (b - a) * (f(a) + f(b))
>
> def trapecio_compuesto(f, a, b, n):
>     h = (b - a) / n
>     x = [a + i*h for i in range(n + 1)]
>     return h * (0.5*f(x[0]) + sum(f(xi) for xi in x[1:-1]) + 0.5*f(x[-1]))
> ```

---

## Relación con otras notas

> [!info]
> - El error como integral del error de interpolación: [[Error Interpolacion Formula Cauchy]].
> - La versión práctica subdividida: [[Trapecio Compuesto Convergencia O h2]].
> - La regla de mayor orden: [[Simpson 1 3 Orden Precision y Error Cuarta Derivada]].
> - Su aceleración: [[Extrapolacion Richardson Aceleracion Convergencia]] (Romberg).

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Fórmula | $\frac{h}{2}(f_0 + f_1)$ |
| Error | $-\frac{h^3}{12}f''(\xi)$ |
| Grado de exactitud | 1 (lineales) |
| Signo del error | $-\operatorname{sgn}(f'')$ |
| Exacta para | funciones lineales (y periódicas en su período) |

> [!corolario]
> La regla del trapecio integra el interpolante lineal de $f$, dando $\frac{h}{2}(f_0+f_1)$ con error $-\frac{h^3}{12}f''(\xi)$: exacta para funciones lineales, sobrestima las convexas y subestima las cóncavas. Su grado de exactitud $1$ la hace poco precisa para integrandos curvados frente a [[Simpson 1 3 Orden Precision y Error Cuarta Derivada|Simpson]], pero su simplicidad y robustez la convierten en la base del [[Trapecio Compuesto Convergencia O h2|trapecio compuesto]] y de la extrapolación de [[Extrapolacion Richardson Aceleracion Convergencia|Romberg]], además de ser óptima para integrandos periódicos.
