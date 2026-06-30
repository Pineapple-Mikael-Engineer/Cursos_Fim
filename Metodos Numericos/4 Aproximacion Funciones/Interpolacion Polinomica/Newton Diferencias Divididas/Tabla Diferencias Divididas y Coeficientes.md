---
title: Tabla de Diferencias Divididas y Coeficientes
order: 1
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - interpolacion
  - newton-interpolacion
draft: false
aliases:
  - Tabla de diferencias divididas
  - Diferencias divididas
  - Divided difference table
---

# Tabla de Diferencias Divididas y Coeficientes

> [!definicion]
> La **diferencia dividida** de orden $k$ sobre nodos $x_i, \dots, x_{i+k}$ se define recursivamente por
> $$f[x_i] = f(x_i), \qquad f[x_i,\dots,x_{i+k}] = \frac{f[x_{i+1},\dots,x_{i+k}] - f[x_i,\dots,x_{i+k-1}]}{x_{i+k} - x_i}.$$
> Son los coeficientes de la [[Newton Diferencias Divididas/index|forma de Newton]] del polinomio interpolador.

> [!info]
> La recurrencia genera una tabla triangular en $O(n^2)$ operaciones; la **diagonal superior** $f[x_0], f[x_0,x_1], \dots, f[x_0,\dots,x_n]$ son los coeficientes $c_0, \dots, c_n$ de $p_n(x) = \sum_k c_k \prod_{j<k}(x-x_j)$.

---

## Construcción de la tabla

> [!algoritmo]
> **Recurrencia por columnas.** Partiendo de la columna $0$ con los valores $f(x_i)$, cada columna se obtiene de la anterior:
>
> ```
> para i = 0 .. n:  d[i][0] = f(x_i)
> para k = 1 .. n:
>     para i = 0 .. n-k:
>         d[i][k] = (d[i+1][k-1] - d[i][k-1]) / (x[i+k] - x[i])
> coeficientes c_k = d[0][k]            // diagonal superior
> ```
>
> Costo $O(n^2)$ en operaciones y $O(n)$ en memoria si se sobrescribe en un vector.

---

## Ejemplo

> [!ejemplo]
> **Tabla para $(1, 0), (2, \ln 2), (4, \ln 4), (8, \ln 8)$** (interpolando $\ln x$):
>
> | $x_i$ | $f[\,]$ | orden 1 | orden 2 | orden 3 |
> |:---:|:---:|:---:|:---:|:---:|
> | 1 | 0 | | | |
> | 2 | 0.6931 | 0.6931 | | |
> | 4 | 1.3863 | 0.3466 | $-0.1155$ | |
> | 8 | 2.0794 | 0.1733 | $-0.0289$ | $0.0124$ |
>
> Coeficientes (diagonal): $c_0=0$, $c_1=0.6931$, $c_2=-0.1155$, $c_3=0.0124$. El interpolador es
> $$p_3(x) = 0 + 0.6931(x-1) - 0.1155(x-1)(x-2) + 0.0124(x-1)(x-2)(x-4).$$

---

## Propiedades clave

> [!proposicion]
> 1. **Simetría:** $f[x_{i_0},\dots,x_{i_k}]$ es invariante ante permutaciones de los nodos.
> 2. **Incrementalidad:** añadir un nodo $x_{n+1}$ solo requiere calcular una nueva diferencia dividida $f[x_0,\dots,x_{n+1}]$ y agregar un término; los coeficientes previos no cambian.
> 3. **Coeficiente director:** $f[x_0,\dots,x_n]$ es el coeficiente de $x^n$ en $p_n$.

> [!demostracion]
> **Incrementalidad.** Por la unicidad del [[Existencia Unicidad Polinomio Interpolador|interpolador]], $p_{n+1} = p_n + (\text{término de grado } n+1)$ donde el término extra debe anularse en $x_0,\dots,x_n$: tiene la forma $c_{n+1}\prod_{j=0}^n(x-x_j)$. Igualando coeficientes de $x^{n+1}$, $c_{n+1} = f[x_0,\dots,x_{n+1}]$. Por eso Newton es incremental y Lagrange no.

---

## Diferencias divididas con nodos repetidos

> [!info]
> Cuando nodos coinciden, la recurrencia diverge ($x_{i+k} - x_i = 0$), pero el límite existe y vale una **derivada**:
> $$f[x_0, x_0] = f'(x_0), \qquad f[\underbrace{x_0,\dots,x_0}_{k+1}] = \frac{f^{(k)}(x_0)}{k!}.$$
> Esto extiende Newton a la **interpolación de Hermite** (prescribir valores y derivadas), desarrollada en [[Relacion Diferencias Divididas Derivadas]].

---

## Relación con otras notas

> [!info]
> - El polinomio que estos coeficientes forman: [[Newton Diferencias Divididas/index]].
> - Su evaluación eficiente: [[Forma Anidada y Eficiencia Algoritmo Horner]].
> - El significado de las diferencias divididas como derivadas: [[Relacion Diferencias Divididas Derivadas]].
> - Su aparición en el término de error: [[Error Interpolacion Formula Cauchy]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Recurrencia | $f[x_i,..,x_{i+k}] = \frac{f[x_{i+1},..]-f[x_i,..]}{x_{i+k}-x_i}$ |
| Costo | $O(n^2)$ |
| Coeficientes | diagonal superior $f[x_0,\dots,x_k]$ |
| Incremental | sí (nodo nuevo = un término) |
| Simetría | invariante ante permutación |
| Nodo repetido | $f[x_0,\dots,x_0] = f^{(k)}(x_0)/k!$ |

> [!corolario]
> Las diferencias divididas se calculan por una recurrencia triangular en $O(n^2)$, y su diagonal superior son directamente los coeficientes de la forma de Newton. Su propiedad esencial es la incrementalidad —añadir un nodo agrega un solo término sin alterar los previos—, consecuencia de la unicidad del interpolador, lo que distingue a [[Newton Diferencias Divididas/index|Newton]] de [[Lagrange/index|Lagrange]]. Son simétricas en los nodos, dan el coeficiente director $f[x_0,\dots,x_n]$, y en el límite de nodos confluentes se vuelven [[Relacion Diferencias Divididas Derivadas|derivadas]], puente hacia Hermite y el [[Error Interpolacion Formula Cauchy|término de error]].
