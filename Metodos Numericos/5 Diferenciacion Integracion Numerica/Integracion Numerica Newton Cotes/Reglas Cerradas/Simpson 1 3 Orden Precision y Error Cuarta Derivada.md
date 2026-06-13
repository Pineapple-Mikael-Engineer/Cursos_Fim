---
title: Regla de Simpson 1/3 y Error de Cuarta Derivada
tags:
  - metodos-numericos
  - teoria
  - diferenciacion-integracion
  - integracion-numerica
  - newton-cotes
draft: false
aliases:
  - Regla de Simpson
  - Simpson 1/3
  - Simpson's rule
  - Error de Simpson
---

# Regla de Simpson 1/3 y Error de Cuarta Derivada

> [!definicion]
> La **regla de Simpson 1/3** aproxima $\int_a^b f(x)\,dx$ integrando la **parábola** que pasa por los extremos y el punto medio. Con $h = \frac{b-a}{2}$ y nodos $x_0=a$, $x_1=\frac{a+b}{2}$, $x_2=b$:
> $$\int_a^b f(x)\,dx \approx \frac{h}{3}\big(f_0 + 4f_1 + f_2\big).$$

> [!info]
> Es la regla de [[Reglas Cerradas/index|Newton-Cotes]] de grado $2$, pero con **grado de exactitud 3**: integra cúbicas exactamente pese a usar una parábola. Su error depende de $f^{(4)}$, lo que la hace mucho más precisa que el [[Trapecio Error Truncamiento Segunda Derivada|trapecio]] al mismo costo de subdivisión.

---

## Error de truncamiento

> [!teorema]
> Si $f \in C^4[a,b]$, existe $\xi \in (a,b)$ tal que
> $$\int_a^b f(x)\,dx = \frac{h}{3}\big(f_0 + 4f_1 + f_2\big) - \frac{h^5}{90}f^{(4)}(\xi), \qquad h = \frac{b-a}{2}.$$
> El error es $O(h^5)$ por panel y proporcional a $f^{(4)}$: nulo para polinomios de grado $\leq 3$.

> [!demostracion]
> La parábola tiene grado de exactitud $\geq 2$ por construcción. Que sea $3$ se ve porque el término de error de orden $h^4$ se anula por **simetría** de los nodos respecto al centro: el polinomio nodal $\prod(x-x_i)$ es impar respecto al punto medio, y su integral contra una constante (el siguiente término de Taylor) se cancela. El primer término no nulo involucra $f^{(4)}$, dando $-\frac{h^5}{90}f^{(4)}(\xi)$. (Se prueba con el método del núcleo de Peano o por integración del error de interpolación de Hermite.)

---

## El "bonus de paridad"

> [!teoria]
> Simpson usa $3$ puntos (parábola, grado $2$) pero integra **cúbicas** exactamente. La razón: una cúbica se descompone en una parábola más un término cúbico **antisimétrico** respecto al punto medio; al integrar sobre el intervalo simétrico, la parte antisimétrica se cancela. Este ascenso de grado "gratis" es lo que hace a Simpson tan eficiente: orden $h^5$ por el precio de $3$ evaluaciones.

---

## Ejemplo

> [!ejemplo]
> **$\int_0^1 e^x\,dx = e-1 \approx 1.7182818$** con Simpson 1/3 ($h=0.5$):
> $$\frac{0.5}{3}\big(e^0 + 4e^{0.5} + e^1\big) = \frac{0.5}{3}(1 + 6.59489 + 2.71828) = 1.718862.$$
> Error $= 5.8\times10^{-4}$, frente al $1.4\times10^{-1}$ del [[Trapecio Error Truncamiento Segunda Derivada|trapecio]]: **240 veces** menor con solo un punto más. La cota $\frac{h^5}{90}\max|f^{(4)}| = \frac{(0.5)^5 e}{90} \approx 9.4\times10^{-4}$ es consistente.

---

## Comparación con el trapecio

> [!info]
> | | [[Trapecio Error Truncamiento Segunda Derivada\|Trapecio]] | Simpson 1/3 |
> |:---|:---|:---|
> | Interpolante | recta | parábola |
> | Nodos | 2 | 3 |
> | Error | $-\frac{h^3}{12}f''$ | $-\frac{h^5}{90}f^{(4)}$ |
> | Grado de exactitud | 1 | **3** |
> | Exacta para | lineales | cúbicas |

> [!warning]
> Simpson 1/3 requiere un número **par** de subintervalos (nodos impares). Para un número impar de paneles se combina con un panel de [[Simpson 3 8 y Reglas Grado Superior|Simpson 3/8]] al final.

---

## Algoritmo

> [!algoritmo]
> **Simpson 1/3 simple y compuesto.**
>
> ```python
> def simpson(f, a, b):
>     m = 0.5 * (a + b)
>     return (b - a) / 6 * (f(a) + 4*f(m) + f(b))    # = (h/3)(f0+4f1+f2), h=(b-a)/2
>
> def simpson_compuesto(f, a, b, n):                 # n par
>     h = (b - a) / n
>     x = [a + i*h for i in range(n + 1)]
>     impares = sum(f(x[i]) for i in range(1, n, 2))
>     pares   = sum(f(x[i]) for i in range(2, n, 2))
>     return h/3 * (f(x[0]) + 4*impares + 2*pares + f(x[-1]))
> ```

---

## Relación con otras notas

> [!info]
> - La regla más simple que supera: [[Trapecio Error Truncamiento Segunda Derivada]].
> - La versión práctica subdividida: [[Simpson Compuesto Convergencia O h4]].
> - La regla hermana para paneles impares: [[Simpson 3 8 y Reglas Grado Superior]].
> - Su deducción dentro de la familia: [[Formulacion General Pesos Newton Cotes]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Fórmula | $\frac{h}{3}(f_0 + 4f_1 + f_2)$ |
| Error | $-\frac{h^5}{90}f^{(4)}(\xi)$ |
| Grado de exactitud | 3 (cúbicas) |
| Subintervalos | número par |
| Ventaja | orden $h^5$ con 3 puntos |

> [!corolario]
> La regla de Simpson 1/3 integra una parábola por $3$ puntos, $\frac{h}{3}(f_0+4f_1+f_2)$, con error $-\frac{h^5}{90}f^{(4)}(\xi)$ y grado de exactitud $3$: integra cúbicas exactamente gracias al "bonus de paridad" que cancela el término de error de orden $h^4$ por simetría. Es órdenes de magnitud más precisa que el [[Trapecio Error Truncamiento Segunda Derivada|trapecio]] al mismo costo de subdivisión, lo que la convierte en la regla de Newton-Cotes más usada. Requiere un número par de paneles, completado si es necesario con [[Simpson 3 8 y Reglas Grado Superior|Simpson 3/8]], y su forma compuesta da [[Simpson Compuesto Convergencia O h4|convergencia $O(h^4)$]].
