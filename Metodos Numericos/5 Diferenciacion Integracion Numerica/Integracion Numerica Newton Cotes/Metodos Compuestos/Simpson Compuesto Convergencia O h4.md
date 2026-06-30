---
title: Simpson Compuesto y Convergencia O(h⁴)
order: 2
tags:
  - metodos-numericos
  - teoria
  - diferenciacion-integracion
  - integracion-numerica
  - newton-cotes
  - convergencia
draft: false
aliases:
  - Simpson compuesto
  - Composite Simpson
  - Regla de Simpson compuesta
---

# Simpson Compuesto y Convergencia $O(h^4)$

> [!definicion]
> El **Simpson compuesto** divide $[a,b]$ en un número **par** $n$ de subintervalos de paso $h = \frac{b-a}{n}$ y aplica [[Simpson 1 3 Orden Precision y Error Cuarta Derivada|Simpson 1/3]] a cada par de paneles:
> $$\int_a^b f\,dx \approx \frac{h}{3}\Big(f_0 + 4\!\!\sum_{i\ \text{impar}}\!\!f_i + 2\!\!\sum_{i\ \text{par}}\!\!f_i + f_n\Big).$$

> [!info]
> Los nodos impares (centros de cada parábola) pesan $4$; los pares internos (fronteras compartidas) pesan $2$; los extremos, $1$. Su error global es $O(h^4)$, lo que lo hace mucho más preciso que el [[Trapecio Compuesto Convergencia O h2|trapecio compuesto]] al mismo número de evaluaciones.

---

## Error global

> [!teorema]
> Si $f \in C^4[a,b]$, el error del Simpson compuesto es
> $$\int_a^b f\,dx - S_n = -\frac{(b-a)h^4}{180}f^{(4)}(\xi), \qquad \xi\in(a,b),$$
> es decir $O(h^4)$: dos órdenes mejor que el trapecio compuesto.

> [!demostracion]
> El error de Simpson sobre cada par de paneles $[x_{2k}, x_{2k+2}]$ es $-\frac{h^5}{90}f^{(4)}(\xi_k)$. Hay $n/2$ pares; sumando:
> $$E = -\frac{h^5}{90}\sum_{k=0}^{n/2-1}f^{(4)}(\xi_k) = -\frac{h^5}{90}\cdot\frac{n}{2}\,\overline{f^{(4)}} = -\frac{h^5}{90}\cdot\frac{b-a}{2h}\,\overline{f^{(4)}} = -\frac{(b-a)h^4}{180}f^{(4)}(\xi).$$
> Al sumar $(b-a)/(2h)$ pares se pierde una potencia de $h$: de $O(h^5)$ por par a $O(h^4)$ global.

---

## Ejemplo

> [!ejemplo]
> **$\int_0^1 e^x\,dx = e-1 \approx 1.7182818$**, Simpson compuesto:
>
> | $n$ | $h$ | $S_n$ | error | factor |
> |:---:|:---:|:---:|:---:|:---:|
> | 2 | 0.5 | 1.7188612 | $5.8\times10^{-4}$ | — |
> | 4 | 0.25 | 1.7183188 | $3.7\times10^{-5}$ | 15.7 |
> | 8 | 0.125 | 1.7182841 | $2.3\times10^{-6}$ | 16.0 |
>
> Halvar $h$ divide el error por $\approx 16 = 2^4$, confirmando $O(h^4)$. Con $n=8$ ya hay $\sim6$ dígitos correctos, frente a $\sim3$ del trapecio compuesto.

---

## Comparación con el trapecio compuesto

> [!info]
> | | [[Trapecio Compuesto Convergencia O h2\|Trapecio comp.]] | Simpson comp. |
> |:---|:---|:---|
> | Error global | $-\frac{(b-a)h^2}{12}f''$ | $-\frac{(b-a)h^4}{180}f^{(4)}$ |
> | Orden | $O(h^2)$ | $O(h^4)$ |
> | Factor al halvar $h$ | 4 | 16 |
> | Subintervalos | cualquiera | par |
> | Evaluaciones | $n+1$ | $n+1$ |
>
> Mismo número de evaluaciones, dos órdenes más de precisión: Simpson compuesto es la elección por defecto para integrandos suaves.

---

## Algoritmo

> [!algoritmo]
> **Simpson compuesto en Python** ($n$ par).
>
> ```python
> def simpson_compuesto(f, a, b, n):
>     if n % 2 != 0:
>         raise ValueError("n debe ser par")
>     h = (b - a) / n
>     x = [a + i*h for i in range(n + 1)]
>     impares = sum(f(x[i]) for i in range(1, n, 2))   # peso 4
>     pares   = sum(f(x[i]) for i in range(2, n, 2))   # peso 2
>     return h/3 * (f(x[0]) + 4*impares + 2*pares + f(x[-1]))
> ```

> [!warning]
> Requiere $n$ **par**. Para $n$ impar, se aplica Simpson 1/3 a $n-3$ paneles y [[Simpson 3 8 y Reglas Grado Superior|Simpson 3/8]] a los $3$ últimos, manteniendo $O(h^4)$.

---

## Relación con otras notas

> [!info]
> - La regla simple que se repite: [[Simpson 1 3 Orden Precision y Error Cuarta Derivada]].
> - La regla compuesta de menor orden: [[Trapecio Compuesto Convergencia O h2]].
> - El mismo $O(h^4)$ obtenido por extrapolación: [[Extrapolacion Richardson Aceleracion Convergencia]] (segunda columna de Romberg = Simpson).
> - La alternativa de mayor eficiencia: [[Comparacion Eficiencia vs Newton Cotes]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Fórmula | $\frac{h}{3}(f_0 + 4\sum_{\text{impar}} + 2\sum_{\text{par}} + f_n)$ |
| Error global | $-\frac{(b-a)h^4}{180}f^{(4)}(\xi)$ |
| Orden | $O(h^4)$ |
| Factor al halvar $h$ | 16 |
| Subintervalos | par |

> [!corolario]
> El Simpson compuesto aplica Simpson 1/3 a cada par de paneles, con pesos $1,4,2,4,\dots,4,1$ y error global $-\frac{(b-a)h^4}{180}f^{(4)}(\xi) = O(h^4)$, dos órdenes mejor que el [[Trapecio Compuesto Convergencia O h2|trapecio compuesto]] con el mismo número de evaluaciones. Es la regla de Newton-Cotes de uso por defecto para integrandos suaves, equivalente a la segunda columna de [[Extrapolacion Richardson Aceleracion Convergencia|Romberg]]. Requiere número par de paneles, completable con [[Simpson 3 8 y Reglas Grado Superior|Simpson 3/8]]. Para máxima eficiencia con pocos nodos, la [[Cuadratura Gaussiana/index|cuadratura gaussiana]] aún la supera.
