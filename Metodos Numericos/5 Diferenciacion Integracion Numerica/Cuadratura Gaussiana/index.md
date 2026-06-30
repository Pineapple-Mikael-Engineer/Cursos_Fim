---
title: Cuadratura Gaussiana
order: 3
tags:
  - metodos-numericos
  - teoria
  - diferenciacion-integracion
  - cuadratura-gaussiana
  - index
draft: false
aliases:
  - Cuadratura gaussiana
  - Gaussian quadrature
  - Gauss-Legendre
---

# Cuadratura Gaussiana

> [!definicion]
> La **cuadratura gaussiana** aproxima $\int_a^b f(x)\,dx \approx \sum_{i=1}^n w_i f(x_i)$ eligiendo **simultáneamente** los $n$ nodos $x_i$ y los $n$ pesos $w_i$ para maximizar el grado de exactitud. Con $n$ nodos, integra exactamente todo polinomio de grado $\leq 2n-1$.

> [!info]
> La diferencia con [[Integracion Numerica Newton Cotes/index|Newton-Cotes]]: allí los nodos son fijos (equiespaciados) y solo se optimizan los pesos, dando grado $\sim n$; aquí los nodos también son libres, duplicando el grado a $2n-1$. Los nodos óptimos resultan ser los ceros de los **polinomios ortogonales** (de Legendre, en $[-1,1]$).

---

## Las cuatro piezas

> [!info]
> - **[[Fundamentos Gauss Legendre Polinomios Ortogonales|Fundamentos]]:** por qué los nodos óptimos son los ceros de los polinomios de Legendre (ortogonalidad).
> - **[[Determinacion Nodos y Pesos Optimos|Nodos y pesos]]:** cómo se calculan; pesos siempre positivos.
> - **[[Grado Exactitud Polinomica 2n 1|Grado de exactitud $2n-1$]]:** la demostración del resultado central.
> - **[[Comparacion Eficiencia vs Newton Cotes|Eficiencia]]** y **[[Cambio Variable Intervalo General|cambio de variable]]** a un intervalo general $[a,b]$.

---

## Ejemplo

> [!ejemplo]
> **$\int_{-1}^1 e^x\,dx = e - e^{-1} \approx 2.350402$** con Gauss-Legendre de 2 nodos ($x = \pm1/\sqrt3$, $w = 1, 1$):
> $$\int_{-1}^1 e^x\,dx \approx 1\cdot e^{-1/\sqrt3} + 1\cdot e^{1/\sqrt3} = e^{-0.5774} + e^{0.5774} = 2.342696.$$
> Error $7.7\times10^{-3}$ con **2 evaluaciones**, comparable a Simpson con muchos más puntos. Con 3 nodos el error baja a $\sim10^{-4}$.

---

## Gauss vs Newton-Cotes

> [!info]
> | | [[Integracion Numerica Newton Cotes/index\|Newton-Cotes]] | Gauss-Legendre |
> |:---|:---|:---|
> | Nodos | fijos, equiespaciados | óptimos (ceros de Legendre) |
> | Grados de libertad | $n$ pesos | $n$ nodos + $n$ pesos |
> | Grado de exactitud | $\sim n$ | $2n-1$ |
> | Pesos | pueden ser negativos | **siempre positivos** |
> | Nodos en extremos | sí (cerradas) | no (interiores) |

---

## Resumen

| Tema | Nota |
|:---|:---|
| Polinomios ortogonales y nodos | [[Fundamentos Gauss Legendre Polinomios Ortogonales]] |
| Cálculo de nodos y pesos | [[Determinacion Nodos y Pesos Optimos]] |
| Grado de exactitud $2n-1$ | [[Grado Exactitud Polinomica 2n 1]] |
| Eficiencia vs Newton-Cotes | [[Comparacion Eficiencia vs Newton Cotes]] |
| Cambio de variable a $[a,b]$ | [[Cambio Variable Intervalo General]] |

> [!corolario]
> La cuadratura gaussiana elige nodos y pesos óptimos para alcanzar grado de exactitud $2n-1$ con solo $n$ evaluaciones, el doble de lo que logra [[Integracion Numerica Newton Cotes/index|Newton-Cotes]] con nodos fijos. Los nodos óptimos son los ceros de los [[Fundamentos Gauss Legendre Polinomios Ortogonales|polinomios de Legendre]], y los pesos resultan siempre positivos, garantizando estabilidad. Es la cuadratura más eficiente para integrandos suaves, a costa de no reutilizar evaluaciones al cambiar $n$ y requerir un [[Cambio Variable Intervalo General|cambio de variable]] al intervalo de referencia.
