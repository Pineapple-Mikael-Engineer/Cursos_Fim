---
title: Metodos Cerrados Una Variable
order: 2
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-no-lineales
  - metodos-cerrados
  - index
draft: false
aliases:
  - Bracketing methods
  - Métodos de intervalo
  - Métodos cerrados
---

# Métodos Cerrados para Ecuaciones No Lineales

> [!definicion]
> Los **métodos cerrados** (o de intervalo) son métodos iterativos que mantienen un intervalo $[a, b]$ que contiene una raíz de $f(x)=0$, garantizando convergencia bajo condiciones generales.

> [!info]
> A diferencia de los [[Metodos Abiertos Una Variable/index|métodos abiertos]], los métodos cerrados no requieren derivadas y siempre convergen (aunque lentamente), siempre que $f$ sea continua y $f(a)f(b) < 0$.

---

## Bisección

> [!info]
> El método más simple y robusto: divide el intervalo en cada iteración. Su convergencia es lineal pero garantizada.
>
> Se estudia en [[Biseccion|Biseccion]].

---

## Regula Falsi

> [!info]
> Mejora la bisección usando interpolación lineal para acelerar la convergencia, pero puede sufrir estancamiento unilateral.
>
> Se estudia en [[Regula Falsi/index|Regula Falsi]].

---

## Ejemplo

> [!ejemplo]
> **Encontrar la raíz de $f(x) = x^2 - 2$ en $[1, 2]$ (solución $x = \sqrt{2} \approx 1.414213562$).**
>
> **Bisección:**
>
> | $k$ | $a_k$ | $b_k$ | $c_k$ | $f(c_k)$ |
> |:---|:---|:---|:---|:---|
> | 0 | 1.0000 | 2.0000 | 1.5000 | 0.2500 |
> | 1 | 1.0000 | 1.5000 | 1.2500 | -0.4375 |
> | 2 | 1.2500 | 1.5000 | 1.3750 | -0.1094 |
> | 3 | 1.3750 | 1.5000 | 1.4375 | 0.0664 |
> | 4 | 1.3750 | 1.4375 | 1.4063 | -0.0225 |
> | 5 | 1.4063 | 1.4375 | 1.4219 | 0.0217 |
>
> **Regula Falsi:**
>
> | $k$ | $a_k$ | $b_k$ | $c_k$ | $f(c_k)$ |
> |:---|:---|:---|:---|:---|
> | 0 | 1.0000 | 2.0000 | 1.3333 | -0.2222 |
> | 1 | 1.3333 | 2.0000 | 1.4000 | -0.0400 |
> | 2 | 1.4000 | 2.0000 | 1.4118 | -0.0069 |
> | 3 | 1.4118 | 2.0000 | 1.4138 | -0.0012 |
> | 4 | 1.4138 | 2.0000 | 1.4142 | -0.0002 |
>
> **Observaciones:**
> - Bisección reduce el intervalo a la mitad en cada iteración (convergencia lenta pero predecible).
> - Regula Falsi converge más rápido en este ejemplo, pero el extremo $b=2$ nunca se mueve (estancamiento unilateral).

---

## Motivación

> [!teoria]
> **¿Por qué usar métodos cerrados?**
>
> **Ventajas:**
> - Convergencia **garantizada** bajo condiciones débiles ($f$ continua, $f(a)f(b) < 0$)
> - No requieren derivadas ni información adicional
> - Fáciles de implementar y entender
> - El error está acotado por la longitud del intervalo
>
> **Desventajas:**
> - Convergencia lenta (lineal)
> - Requieren un intervalo inicial que contenga una raíz (obtenido mediante [[Teorema de Bolzano y Metodo Grafico]])
> - No se extienden naturalmente a varias variables
>
> **Regula Falsi vs Bisección:**
> - Regula Falsi suele converger más rápido en funciones convexas/cóncavas
> - Pero puede sufrir estancamiento (un extremo no se actualiza)
> - Las modificaciones (Illinois, Pegasus) corrigen este problema

---

## Resumen

| Método | Principio | Convergencia | Ventaja | Desventaja |
|:---|:---|:---|:---|:---|
| **Bisección** | División del intervalo | Lineal ($p=1$, factor $1/2$) | Robusto, simple, error acotado | Lento |
| **Regula Falsi** | Interpolación lineal | Lineal (más rápido que bisección) | Más rápido que bisección | Estancamiento unilateral |

> [!corolario]
> Los métodos cerrados son la base del análisis de convergencia para ecuaciones no lineales. La bisección garantiza convergencia con una tasa predecible, mientras que Regula Falsi intenta acelerar mediante interpolación. Ambos requieren un intervalo inicial que contenga una raíz, obtenido mediante [[Teorema de Bolzano y Metodo Grafico]].
>
> Para convergencia más rápida (cuadrática o superlineal), consúltense los [[Metodos Abiertos Una Variable/index|métodos abiertos]] como Newton o Secante. Para problemas multivariable, véase [[Sistemas Ecuaciones No Lineales/index|Sistemas Ecuaciones No Lineales]].