---
title: Regla de Simpson 1/3 y Error de Cuarta Derivada
order: 2
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
## Construcción de la regla

> [!teoria]
> La regla de Simpson se obtiene reemplazando $f$ por su [[Lagrange/index|polinomio interpolador de Lagrange]] de grado $2$ construido sobre los nodos
> $$
> x_0=a,\qquad
> x_1=\frac{a+b}{2},\qquad
> x_2=b,
> $$
> e integrando exactamente dicho polinomio.
>
> Si $h=\frac{b-a}{2}$, el resultado es
> $$
> \boxed{
> \int_a^b f(x)\,dx
> \approx
> \frac{h}{3}
> \left(
> f_0+4f_1+f_2
> \right).
> }
> $$
>
> Los pesos $1:4:1$ provienen de integrar los polinomios fundamentales de Lagrange sobre el intervalo.

---

## Error de truncamiento



> [!teorema]
> Si $f\in C^4[a,b]$, existe un punto $\xi\in(a,b)$ tal que
> $$
> \boxed{
> \int_a^b f(x)\,dx
> =
> \frac{h}{3}\left(f_0+4f_1+f_2\right)
> -
> \frac{h^5}{90}\,f^{(4)}(\xi),
> }
> \qquad
> h=\frac{b-a}{2}.
> $$
>
> En consecuencia, el error local es de orden $O(h^5)$ y la regla es exacta para todo polinomio de grado menor o igual que $3$.

> [!demostracion]
> La regla de Simpson se obtiene integrando el [[Lagrange/index|polinomio interpolador de Lagrange]] de grado $2$, por lo que es exacta para todos los polinomios de grado menor o igual que $2$. Además, gracias a la simetría de los nodos respecto al punto medio, también integra exactamente cualquier polinomio de grado $3$.
>
> Por ello, el primer polinomio para el cual puede existir error es
> $$
> f(x)=x^4.
> $$
>
> Consideremos el intervalo simétrico $[-1,1]$, donde $h=1$. La integral exacta vale
> $$
> \int_{-1}^{1}x^4\,dx
> =
> \frac{2}{5},
> $$
> mientras que la regla de Simpson produce
> $$
> \frac{1}{3}\big(f(-1)+4f(0)+f(1)\big)
> =
> \frac{1}{3}(1+0+1)
> =
> \frac{2}{3}.
> $$
>
> El error es, por tanto,
> $$
> E
> =
> \frac{2}{5}
> -
> \frac{2}{3}
> =
> -\frac{4}{15}.
> $$
>
> Como
> $$
> f^{(4)}(x)=24,
> $$
> si el error tiene la forma
> $$
> E=-C\,h^5\,f^{(4)}(\xi),
> $$
> resulta
> $$
> -\frac{4}{15}
> =
> -24C,
> $$
> de donde
> $$
> C=\frac{1}{90}.
> $$
>
> Así se obtiene la expresión general
> $$
> E
> =
> -\frac{h^5}{90}\,f^{(4)}(\xi),
> $$
> válida para funciones de clase $C^4[a,b]$.

---

## Cancelación por simetría

> [!teoria]
> Aunque Simpson interpola mediante una parábola (grado $2$), integra exactamente cualquier polinomio de grado hasta $3$.
>
> La razón es la simetría del intervalo. Si se desarrolla una cúbica respecto al punto medio, el término de grado $3$ es impar. Tanto la integral exacta como la regla de Simpson anulan automáticamente todas las contribuciones impares sobre un intervalo simétrico.
>
> Por ello, Simpson posee **grado de exactitud $3$**, uno superior al grado del polinomio interpolante.

---

## Ejemplos

> [!ejemplo]
> **$\int_0^1 e^x\,dx = e-1 \approx 1.7182818$** con Simpson 1/3 ($h=0.5$):
> $$\frac{0.5}{3}\big(e^0 + 4e^{0.5} + e^1\big) = \frac{0.5}{3}(1 + 6.59489 + 2.71828) = 1.718862.$$
> Error $= 5.8\times10^{-4}$, frente al $1.4\times10^{-1}$ del [[Trapecio Error Truncamiento Segunda Derivada|trapecio]]: **240 veces** menor con solo un punto más. La cota $\frac{h^5}{90}\max|f^{(4)}| = \frac{(0.5)^5 e}{90} \approx 9.4\times10^{-4}$ es consistente.

> [!ejemplo]
> Sea
> $$
> f(x)=x^3.
> $$
>
> En el intervalo $[-1,1]$,
> $$
> \int_{-1}^{1}x^3\,dx=0.
> $$
>
> La regla de Simpson produce
> $$
> \frac{1}{3}
> \left(
> -1
> +4\cdot0
> +1
> \right)
> =0,
> $$
> reproduciendo exactamente la integral, a pesar de que el interpolante utilizado es únicamente cuadrático.
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
