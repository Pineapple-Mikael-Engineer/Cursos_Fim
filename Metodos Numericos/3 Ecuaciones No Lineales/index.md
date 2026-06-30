---
title: Ecuaciones No Lineales
order: 3
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-no-lineales
  - index
draft: false
aliases:
  - Nonlinear equations
  - Raíces de ecuaciones
  - Ceros de funciones
---

# Ecuaciones No Lineales

> [!definicion]
> Una **ecuación no lineal** en una variable es una expresión de la forma $f(x) = 0$, donde $f: \mathbb{R} \to \mathbb{R}$ es una función no lineal. En varias variables, es un sistema de la forma $F(x) = 0$ con $F: \mathbb{R}^n \to \mathbb{R}^n$.

> [!info]
> A diferencia de las ecuaciones lineales ($Ax = b$), las ecuaciones no lineales no tienen una solución cerrada general. Su resolución requiere **métodos iterativos** que generan una sucesión $\{x^{(k)}\}$ convergente a una raíz.

---

## Localización de raíces

> [!info]
> Antes de aplicar un método iterativo, es necesario identificar intervalos que contengan raíces. El análisis de existencia y unicidad se desarrolla en [[Localizacion Raices/index]].

---

## Métodos cerrados (una variable)

> [!info]
> Los métodos cerrados trabajan con un intervalo $[a, b]$ que contiene una raíz y garantizan convergencia bajo condiciones generales. Bisección y Regula Falsi se estudian en [[Metodos Cerrados Una Variable/index]].

---

## Métodos abiertos (una variable)

> [!info]
> Los métodos abiertos parten de una o dos aproximaciones iniciales sin requerir un intervalo que contenga la raíz. Pueden converger más rápido, pero no siempre convergen. Punto fijo, Newton-Raphson y Secante se estudian en [[Metodos Abiertos Una Variable/index]].

---

## Ejemplo

> [!ejemplo]
> **Encontrar la raíz de $f(x) = x^2 - 2$ en $[1, 2]$ (solución $x = \sqrt{2} \approx 1.414213562$).**
>
> | Método | Iteración 1 | Iteración 2 | Iteración 3 | Iteración 4 | Iteración 5 |
> |:---|:---:|:---:|:---:|:---:|:---:|
> | Bisección | 1.5000 | 1.2500 | 1.3750 | 1.4375 | 1.40625 |
> | Regula Falsi | 1.3333 | 1.4000 | 1.4118 | 1.4138 | 1.4142 |
> | Newton ($x_0=2$) | 1.5000 | 1.41667 | 1.41422 | 1.41421 | — |
> | Secante ($x_0=2, x_1=1.5$) | 1.4000 | 1.41463 | 1.41421 | — | — |

---

## Sistemas de ecuaciones no lineales

> [!info]
> La extensión a varias variables es fundamental en aplicaciones prácticas. El método de Newton multivariable y las aproximaciones sucesivas se estudian en [[Sistemas Ecuaciones No Lineales/index]].

---

## Motivación

> [!teoria]
> **¿Por qué métodos iterativos para ecuaciones no lineales?**
>
> No existen fórmulas cerradas para raíces de ecuaciones polinómicas de grado $\geq 5$ (teorema de Abel-Ruffini) ni para ecuaciones trascendentes. Los métodos iterativos son la única opción.
>
> **Orden de convergencia:**
> - Bisección: lineal ($p = 1$), factor $1/2$
> - Regula Falsi: lineal, puede ser muy lento
> - Punto fijo: lineal ($p = 1$), factor $|g'(\xi)|$
> - Secante: superlineal ($p = \phi \approx 1.618$)
> - Newton: cuadrático ($p = 2$) para raíces simples

---

## Resumen

| Categoría | Subdirectorio |
|:---|:---|
| Localización de raíces | [[Localizacion Raices/index]] |
| Métodos cerrados (Bisección, Regula Falsi) | [[Metodos Cerrados Una Variable/index]] |
| Métodos abiertos (Punto fijo, Newton, Secante) | [[Metodos Abiertos Una Variable/index]] |
| Sistemas no lineales | [[Sistemas Ecuaciones No Lineales/index]] |

> [!corolario]
> El estudio de ecuaciones no lineales comienza con la localización de raíces. Luego, los métodos cerrados garantizan convergencia a costa de velocidad. Los métodos abiertos ofrecen convergencia rápida pero requieren condiciones adicionales. Finalmente, la extensión a sistemas multivariable completa el panorama.