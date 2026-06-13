---
title: Regresión Lineal Múltiple y Polinomial
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - minimos-cuadrados
draft: false
aliases:
  - Regresión lineal múltiple
  - Regresión polinomial
  - Regresión lineal
  - Linear regression
---

# Regresión Lineal Múltiple y Polinomial

> [!definicion]
> La **regresión** aplica el [[Ajuste Minimos Cuadrados/index|ajuste por mínimos cuadrados]] a modelos lineales en los parámetros:
> - **Lineal simple:** $y = c_0 + c_1 x$.
> - **Polinomial:** $y = c_0 + c_1 x + \cdots + c_p x^p$.
> - **Lineal múltiple:** $y = c_0 + c_1 x_1 + \cdots + c_k x_k$ (varias variables predictoras).
>
> Todos son **lineales en los coeficientes** $c_j$ y se resuelven con la misma maquinaria: [[Ecuaciones Normales y Matriz Gram|ecuaciones normales]] o [[Condicionamiento Ecuaciones Normales|QR]].

> [!info]
> "Lineal" se refiere a los **parámetros**, no a la variable: la regresión polinomial ajusta una curva, pero es un problema lineal porque $\phi(x;c) = \sum_j c_j x^j$ depende linealmente de $c$. Esto unifica los tres casos bajo $\min_c\|Ac-y\|_2^2$.

---

## La matriz de diseño según el modelo

> [!info]
> | Modelo | Funciones base $\varphi_j(x)$ | Fila $i$ de $A$ |
> |:---|:---|:---|
> | Recta | $1,\ x$ | $[1,\ x_i]$ |
> | Polinomio grado $p$ | $1, x, \dots, x^p$ | $[1, x_i, \dots, x_i^p]$ |
> | Lineal múltiple | $1, x_1, \dots, x_k$ | $[1, x_{i1}, \dots, x_{ik}]$ |
>
> En todos los casos $A_{ij} = \varphi_j(x_i)$ y se minimiza $\|Ac-y\|_2$. Solo cambia la construcción de $A$.

---

## Regresión lineal simple: fórmulas cerradas

> [!teorema]
> Para $y = c_0 + c_1 x$ con datos $\{(x_i,y_i)\}_{i=1}^m$, las ecuaciones normales dan
> $$c_1 = \frac{\sum_i (x_i-\bar x)(y_i-\bar y)}{\sum_i (x_i-\bar x)^2}, \qquad c_0 = \bar y - c_1\bar x,$$
> donde $\bar x, \bar y$ son las medias. La recta pasa por el **centroide** $(\bar x, \bar y)$.

> [!demostracion]
> Las ecuaciones normales $2\times2$ son $\sum(c_0+c_1x_i-y_i)=0$ y $\sum x_i(c_0+c_1x_i-y_i)=0$. La primera da $c_0 = \bar y - c_1\bar x$. Sustituyendo en la segunda y simplificando con las definiciones de media se obtiene $c_1$ como cociente de covarianza muestral entre varianza muestral de $x$.

---

## Ejemplo: regresión polinomial

> [!ejemplo]
> **Ajustar parábola $y = c_0 + c_1 x + c_2 x^2$ a $(-1, 2), (0, 0), (1, 1), (2, 5)$.** Matriz de diseño:
> $$A = \begin{pmatrix} 1 & -1 & 1 \\ 1 & 0 & 0 \\ 1 & 1 & 1 \\ 1 & 2 & 4 \end{pmatrix}, \quad y = \begin{pmatrix} 2 \\ 0 \\ 1 \\ 5 \end{pmatrix}.$$
> Resolviendo $A^TAc = A^Ty$ (o por [[Condicionamiento Ecuaciones Normales|QR]]) se obtiene $c \approx (0.05,\ 0.15,\ 1.05)^T$, es decir $y \approx 0.05 + 0.15x + 1.05x^2$. La parábola **no** pasa por los 4 puntos (4 datos, 3 parámetros) pero minimiza el error cuadrático.

---

## Bondad del ajuste

> [!info]
> El **coeficiente de determinación** $R^2$ mide qué fracción de la varianza de $y$ explica el modelo:
> $$R^2 = 1 - \frac{\sum_i (y_i - \hat y_i)^2}{\sum_i (y_i - \bar y)^2} = 1 - \frac{\|r\|_2^2}{\|y - \bar y\|_2^2},$$
> donde $\hat y_i$ son los valores ajustados y $r$ el residuo. $R^2 = 1$ indica ajuste perfecto; $R^2 = 0$, que el modelo no mejora a la media.

> [!warning]
> **Sobreajuste.** Aumentar el grado del polinomio siempre **reduce** el residuo en los datos ($R^2 \to 1$ cuando grado $= m-1$, recuperando la [[Interpolacion Polinomica/index|interpolación]]), pero degrada la predicción fuera de ellos y dispara el [[Condicionamiento Ecuaciones Normales|condicionamiento]]. Hay que equilibrar ajuste y complejidad (validación, regularización).

---

## Modelos linealizables

> [!info]
> Algunos modelos no lineales se transforman en lineales por cambio de variable:
>
> | Modelo | Transformación | Forma lineal |
> |:---|:---|:---|
> | $y = a e^{bx}$ | $\ln y$ | $\ln y = \ln a + b x$ |
> | $y = a x^b$ | $\ln y,\ \ln x$ | $\ln y = \ln a + b\ln x$ |
> | $y = \frac{1}{a + bx}$ | $1/y$ | $1/y = a + bx$ |
>
> Cuidado: la transformación cambia la métrica del error (minimiza residuos en la variable transformada, no en $y$), lo que puede sesgar el ajuste frente a un ajuste no lineal directo.

---

## Relación con otras notas

> [!info]
> - El planteamiento general: [[Formulacion Residuos y Norma Euclidea]].
> - El sistema que se resuelve: [[Ecuaciones Normales y Matriz Gram]].
> - Por qué grado alto es peligroso: [[Condicionamiento Ecuaciones Normales]] y [[Matriz Vandermonde Mal Condicionamiento]].
> - El límite cuando parámetros = datos: [[Interpolacion Polinomica/index]].

---

## Resumen

| Modelo | Base | Solución |
|:---|:---|:---|
| Recta | $1, x$ | fórmula cerrada (centroide) |
| Polinomio | $1,\dots,x^p$ | ecuaciones normales / QR |
| Múltiple | $1, x_1,\dots,x_k$ | ecuaciones normales / QR |
| Bondad | — | $R^2 = 1 - \|r\|^2/\|y-\bar y\|^2$ |
| Riesgo | grado alto | sobreajuste + mal condicionamiento |

> [!corolario]
> La regresión lineal simple, polinomial y múltiple son el mismo problema de mínimos cuadrados $\min\|Ac-y\|_2$, lineal en los coeficientes, que solo difiere en la construcción de la matriz de diseño. La recta tiene fórmula cerrada (pasa por el centroide); los demás se resuelven por [[Ecuaciones Normales y Matriz Gram|ecuaciones normales]] o, ante mal condicionamiento, por [[Condicionamiento Ecuaciones Normales|QR]]. El $R^2$ mide la bondad del ajuste, pero subir el grado hasta interpolar produce sobreajuste y dispara el condicionamiento: la regresión busca la tendencia, no reproducir los datos, marcando la frontera con la [[Interpolacion Polinomica/index|interpolación]] y cerrando el capítulo de [[Aproximacion Funciones/index|aproximación de funciones]].
