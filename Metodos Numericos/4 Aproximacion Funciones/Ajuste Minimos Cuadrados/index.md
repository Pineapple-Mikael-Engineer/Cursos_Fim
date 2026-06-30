---
title: Ajuste por Mínimos Cuadrados
order: 3
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - minimos-cuadrados
  - index
draft: false
aliases:
  - Mínimos cuadrados
  - Ajuste por mínimos cuadrados
  - Least squares
  - Regresión
---

# Ajuste por Mínimos Cuadrados

> [!definicion]
> El **ajuste por mínimos cuadrados** busca, dentro de una familia de modelos $\phi(x; c)$ con parámetros $c$, el que minimiza la suma de cuadrados de los residuos sobre los datos $\{(x_i, y_i)\}_{i=1}^m$:
> $$\min_{c}\ \sum_{i=1}^m \big(\phi(x_i; c) - y_i\big)^2.$$

> [!info]
> A diferencia de la [[Interpolacion Polinomica/index|interpolación]], el modelo **no** pasa por los datos: capta su tendencia. Es la herramienta para datos con **ruido** o **sobredeterminados** (más datos que parámetros, $m > n$), situación típica en experimentos y regresión.

---

## Estructura del problema lineal

> [!info]
> Cuando el modelo es lineal en los parámetros, $\phi(x; c) = \sum_j c_j \varphi_j(x)$, el ajuste se reduce a un problema de álgebra lineal:
> - **[[Formulacion Residuos y Norma Euclidea|Formulación de residuos]]:** minimizar $\|Ac - y\|_2^2$, con $A$ la matriz de diseño.
> - **[[Ecuaciones Normales y Matriz Gram|Ecuaciones normales]]:** la condición de óptimo $A^TAc = A^Ty$.
> - **[[Condicionamiento Ecuaciones Normales|Condicionamiento]]:** por qué las ecuaciones normales son peligrosas ($\kappa(A^TA) = \kappa(A)^2$) y la alternativa QR.
> - **[[Regresion Lineal Multiple y Polinomial|Regresión]]:** los casos prácticos (recta, polinomio, múltiples variables).

---

## Ejemplo

> [!ejemplo]
> **Ajustar una recta $y = c_0 + c_1 x$ a $(1,1), (2,2), (3,2), (4,3)$** (4 datos, 2 parámetros).
>
> La solución de mínimos cuadrados minimiza $\sum (c_0 + c_1 x_i - y_i)^2$:
> $$c_1 = \frac{\sum(x_i-\bar x)(y_i-\bar y)}{\sum(x_i-\bar x)^2} = \frac{5}{5} = 1.0\cdot? \quad c_0 = \bar y - c_1\bar x.$$
> Con $\bar x = 2.5$, $\bar y = 2$: $c_1 = 0.6$, $c_0 = 0.5$. La recta $y = 0.5 + 0.6x$ no pasa por ningún punto pero minimiza el error cuadrático total. El residuo $r = Ac - y$ es ortogonal a las columnas de $A$.

---

## Interpolar vs ajustar

> [!info]
> | | [[Interpolacion Polinomica/index\|Interpolación]] | Mínimos cuadrados |
> |:---|:---|:---|
> | Parámetros | $= m$ datos | $< m$ datos |
> | Pasa por los datos | sí | no |
> | Datos | exactos | con ruido |
> | Sistema | cuadrado, exacto | sobredeterminado, óptimo |
> | Geometría | resolver $Ac = y$ | proyección de $y$ sobre $\operatorname{col}(A)$ |

---

## Resumen

| Tema | Nota |
|:---|:---|
| Residuos y norma euclídea | [[Formulacion Residuos y Norma Euclidea]] |
| Ecuaciones normales y matriz de Gram | [[Ecuaciones Normales y Matriz Gram]] |
| Condicionamiento y alternativa QR | [[Condicionamiento Ecuaciones Normales]] |
| Regresión lineal múltiple y polinomial | [[Regresion Lineal Multiple y Polinomial]] |

> [!corolario]
> El ajuste por mínimos cuadrados aproxima datos con ruido o sobredeterminados minimizando $\|Ac - y\|_2^2$, sin pasar por los puntos sino captando su tendencia. Para modelos lineales en los parámetros, la condición de óptimo son las [[Ecuaciones Normales y Matriz Gram|ecuaciones normales]] $A^TAc = A^Ty$, geométricamente la proyección ortogonal de $y$ sobre el espacio de columnas de $A$. Su [[Condicionamiento Ecuaciones Normales|condicionamiento]] desaconseja resolverlas directamente cuando $\kappa(A)$ es grande, favoreciendo la factorización QR. Es la contraparte de la [[Interpolacion Polinomica/index|interpolación]] cuando los datos no deben reproducirse exactamente.
