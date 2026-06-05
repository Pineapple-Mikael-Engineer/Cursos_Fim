---
title: Integración Numérica de Newton-Cotes
tags:
  - metodos-numericos
  - teoria
  - diferenciacion-integracion
  - integracion-numerica
  - newton-cotes
  - index
draft: false
aliases:
  - Newton-Cotes
  - Integración de Newton-Cotes
  - Cuadratura de Newton-Cotes
---

# Integración Numérica de Newton-Cotes

> [!definicion]
> Las fórmulas de **Newton-Cotes** aproximan $\int_a^b f(x)\,dx$ integrando el [[Interpolacion Polinomica/index|polinomio interpolante]] de $f$ en nodos **equiespaciados**. Tienen la forma
> $$\int_a^b f(x)\,dx \approx \sum_{i=0}^n w_i\, f(x_i), \qquad x_i = a + ih, \quad h = \frac{b-a}{n}.$$

> [!info]
> Los **pesos** $w_i = \int_a^b L_i(x)\,dx$ son las integrales de los [[Formulacion Polinomios Cardinales L i x|polinomios cardinales de Lagrange]]. Cada grado da una regla: $n=1$ trapecio, $n=2$ Simpson 1/3, $n=3$ Simpson 3/8. Su [[Formulacion General Pesos Newton Cotes|deducción general]] es común; la práctica usa versiones **compuestas**.

---

## Reglas cerradas y compuestas

> [!info]
> - **[[Reglas Cerradas/index|Reglas cerradas]]:** usan los extremos del intervalo. Trapecio, Simpson 1/3, Simpson 3/8 y por qué el grado alto se vuelve [[Inestabilidad Pesos Negativos Grado Alto|inestable]].
> - **[[Metodos Compuestos/index|Métodos compuestos]]:** subdividen $[a,b]$ y aplican una regla simple en cada subintervalo. Son la forma de uso real: [[Trapecio Compuesto Convergencia O h2|trapecio]] $O(h^2)$ y [[Simpson Compuesto Convergencia O h4|Simpson]] $O(h^4)$.

---

## Ejemplo

> [!ejemplo]
> **$\int_0^2 \frac{1}{1+x^2}\,dx = \arctan 2 \approx 1.10715$.**
>
> | Regla | Nodos | Aproximación | Error |
> |:---|:---:|:---:|:---:|
> | Trapecio | 2 | 0.80000 | $3.1\times10^{-1}$ |
> | Simpson 1/3 | 3 | 1.06667 | $4.0\times10^{-2}$ |
> | Simpson 3/8 | 4 | 1.08000 | $2.7\times10^{-2}$ |
>
> El grado más alto mejora, pero la ganancia se estanca; la subdivisión (métodos compuestos) es más efectiva que subir el grado.

---

## El grado de exactitud

> [!teoria]
> Una regla tiene **grado de exactitud** $m$ si integra exactamente todo polinomio de grado $\leq m$. Newton-Cotes con $n+1$ nodos tiene grado $n$ (o $n+1$ si $n$ es par, por simetría). La [[Cuadratura Gaussiana/index|cuadratura gaussiana]] alcanza grado $2n-1$ eligiendo los nodos, frente al $\sim n$ de Newton-Cotes con nodos fijos.

---

## Resumen

| Tema | Nota |
|:---|:---|
| Deducción general de los pesos | [[Formulacion General Pesos Newton Cotes]] |
| Reglas cerradas (trapecio, Simpson) | [[Reglas Cerradas/index]] |
| Métodos compuestos | [[Metodos Compuestos/index]] |
| Alternativa de nodos óptimos | [[Cuadratura Gaussiana/index]] |

> [!corolario]
> Las fórmulas de Newton-Cotes integran el polinomio interpolante en nodos equiespaciados, con pesos $w_i = \int L_i$ que dan el trapecio ($n=1$), Simpson 1/3 ($n=2$) y Simpson 3/8 ($n=3$). Como la interpolación de grado alto, sufren [[Inestabilidad Pesos Negativos Grado Alto|inestabilidad]] al aumentar $n$, por lo que en la práctica se usan las versiones [[Metodos Compuestos/index|compuestas]] de grado bajo: trapecio $O(h^2)$ y Simpson $O(h^4)$. Cuando se pueden elegir los nodos, la [[Cuadratura Gaussiana/index|cuadratura gaussiana]] duplica el grado de exactitud.
