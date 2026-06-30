---
title: Fenómeno de Runge y Nodos de Chebyshev
order: 5
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - interpolacion
  - chebyshev
draft: false
aliases:
  - Fenómeno de Runge
  - Runge phenomenon
  - Nodos de Chebyshev
  - Chebyshev nodes
---

# Fenómeno de Runge y Nodos de Chebyshev

> [!definicion]
> El **fenómeno de Runge** es la aparición de oscilaciones de amplitud creciente cerca de los extremos del intervalo cuando se interpola con polinomios de **grado alto** sobre nodos **equiespaciados**. Aumentar el número de nodos **empeora** la aproximación en lugar de mejorarla.

> [!info]
> El fenómeno demuestra que la interpolación polinómica de grado alto es intrínsecamente inestable con nodos equiespaciados: el factor $\max|\prod(x-x_i)|$ del [[Error Interpolacion Formula Cauchy|error de Cauchy]] crece sin control. La solución es redistribuir los nodos (Chebyshev) o cambiar a [[Interpolacion Tramos Splines/index|splines]].

---

## El ejemplo de Runge

> [!ejemplo]
> **Función de Runge $f(x) = \dfrac{1}{1 + 25x^2}$ en $[-1, 1]$**, interpolada con $n+1$ nodos equiespaciados:
>
> | $n$ | Error máximo $\max_{[-1,1]}|f - p_n|$ |
> |:---:|:---:|
> | 5 | 0.43 |
> | 10 | 1.92 |
> | 15 | 7.19 |
> | 20 | 58.6 |
>
> El error **diverge** al aumentar el grado, con oscilaciones que explotan cerca de $x = \pm 1$. La función es suave (analítica), pero sus derivadas $f^{(n+1)}$ crecen más rápido que $(n+1)!$, violando la condición de convergencia de la cota de error.

---

## Origen: el polinomio nodal

> [!teoria]
> Según la [[Error Interpolacion Formula Cauchy|fórmula de Cauchy]], $e_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}\prod(x-x_i)$. Con nodos equiespaciados, el **polinomio nodal** $\omega(x) = \prod(x-x_i)$ es muy desigual: pequeño en el centro pero con picos enormes cerca de los extremos (crece como $\sim 2^n$ veces su valor central). Allí el error se amplifica. La **constante de Lebesgue** asociada crece exponencialmente, $\Lambda_n \sim 2^n/(n\log n)$.

> [!warning]
> El fenómeno **no** se debe a falta de suavidad de $f$ ni a redondeo: ocurre en aritmética exacta con funciones analíticas. Es una propiedad de la *distribución equiespaciada de nodos*.

---

## Solución: nodos de Chebyshev

> [!definicion]
> Los **nodos de Chebyshev** en $[-1, 1]$ son los ceros (o extremos) del polinomio de Chebyshev $T_{n+1}$:
> $$x_i = \cos\!\left(\frac{2i+1}{2(n+1)}\pi\right) \ \text{(ceros)}, \qquad x_i = \cos\!\left(\frac{i\pi}{n}\right) \ \text{(extremos, Chebyshev–Lobatto)}.$$
> Se concentran cerca de los extremos del intervalo, compensando el crecimiento del polinomio nodal.

> [!teorema]
> Entre todos los polinomios mónicos de grado $n+1$, el polinomio nodal de Chebyshev **minimiza** la norma del máximo:
> $$\max_{[-1,1]}\Big|\prod_{i=0}^n (x - x_i)\Big| = \frac{1}{2^n} \quad\text{(nodos de Chebyshev)},$$
> el menor valor posible. Esto minimiza el factor geométrico del [[Error Interpolacion Formula Cauchy|error de interpolación]].

---

## Comparación equiespaciados vs Chebyshev

> [!ejemplo]
> **Función de Runge con nodos de Chebyshev:**
>
> | $n$ | Error (equiespaciados) | Error (Chebyshev) |
> |:---:|:---:|:---:|
> | 5 | 0.43 | 0.56 |
> | 10 | 1.92 | 0.11 |
> | 15 | 7.19 | 0.022 |
> | 20 | 58.6 | 0.0040 |
>
> Con nodos de Chebyshev el error **converge** a cero geométricamente, mientras que con equiespaciados diverge. La constante de Lebesgue de Chebyshev crece solo como $\Lambda_n \sim \frac{2}{\pi}\log n$.

---

## Estrategias prácticas

> [!info]
> | Estrategia | Cuándo |
> |:---|:---|
> | Nodos de Chebyshev | si se eligen los puntos de muestreo libremente |
> | [[Interpolacion Tramos Splines/index\|Splines]] | si los nodos vienen dados (equiespaciados) y son muchos |
> | [[Costo Computacional Evaluacion Directa\|Interpolación baricéntrica]] | evaluación estable de alto grado en nodos de Chebyshev |
> | Limitar el grado | usar interpolación a tramos de grado bajo |
>
> Regla práctica: **nunca** interpolar con un único polinomio de grado alto sobre nodos equiespaciados.

---

## Relación con otras notas

> [!info]
> - El error que el fenómeno hace explotar: [[Error Interpolacion Formula Cauchy]].
> - La alternativa robusta de grado bajo a tramos: [[Interpolacion Tramos Splines/index]] y [[Convergencia y Estabilidad vs Polinomios Grado Alto]].
> - La evaluación estable en nodos de Chebyshev: [[Costo Computacional Evaluacion Directa]].
> - La constante de Lebesgue: [[Formulacion Polinomios Cardinales L i x]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Fenómeno | oscilación divergente, grado alto + equiespaciados |
| Causa | polinomio nodal con picos en los extremos |
| Constante de Lebesgue (equi.) | $\sim 2^n$ |
| Nodos de Chebyshev | $x_i = \cos(\frac{2i+1}{2(n+1)}\pi)$ |
| Polinomio nodal mínimo | $\max|\omega| = 2^{-n}$ |
| Lebesgue (Chebyshev) | $\sim \log n$ |

> [!corolario]
> El fenómeno de Runge muestra que interpolar con un polinomio de grado alto sobre nodos equiespaciados diverge, porque el polinomio nodal del [[Error Interpolacion Formula Cauchy|error de Cauchy]] desarrolla picos exponenciales cerca de los extremos. Los nodos de Chebyshev, concentrados en los bordes, minimizan ese polinomio nodal ($\max|\omega| = 2^{-n}$) y restauran la convergencia con constante de Lebesgue logarítmica. Cuando los nodos vienen impuestos, la alternativa es la interpolación a tramos de grado bajo: los [[Interpolacion Tramos Splines/index|splines]], inmunes a Runge por construcción.
