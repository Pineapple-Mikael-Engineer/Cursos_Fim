---
title: Análisis de Error en Métodos Directos
order: 3
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - sistemas-lineales
  - error-numerico
  - index
draft: false
aliases:
  - Análisis de error directos
  - Fiabilidad de la solución
  - Error en métodos directos
---

# Análisis de Error en Métodos Directos

> [!definicion]
> El **análisis de error en métodos directos** evalúa la fiabilidad de la solución calculada $\tilde x$ de un sistema $Ax = b$ resuelto por [[Eliminacion Gaussiana]] o [[Factorizacion LU/index|factorización LU]]. Distingue lo que se *puede medir* (el residuo) de lo que se *quiere conocer* (el error), y relaciona ambos mediante el [[Condicionamiento Numerico Numero Condicion|número de condición]].

> [!info]
> Tras resolver un sistema en aritmética finita, $\tilde x \neq x$. Surgen dos preguntas que esta sección responde por separado:
> - ¿Cuánto se desvía $\tilde x$ de la solución exacta? → **error**, no observable directamente.
> - ¿Cuánto incumple $\tilde x$ la ecuación? → **residuo** $r = b - A\tilde x$, siempre calculable.

---

## Residuo frente a error

> [!info]
> Un residuo pequeño **no** garantiza un error pequeño: la conexión entre ambos pasa por $\kappa(A)$. Para sistemas mal condicionados, $\tilde x$ puede satisfacer casi exactamente la ecuación y aun así estar lejos de $x$. El desarrollo cuantitativo está en [[Residuo vs Error Relativo Solucion]].

## Sensibilidad y número de condición

> [!info]
> La amplificación de las perturbaciones —tanto las de los datos como las de redondeo— está gobernada por el número de condición. La cota $\|\Delta x\|/\|x\| \leq \kappa(A)\,\|\Delta b\|/\|b\|$ y sus consecuencias prácticas se desarrollan en [[Sensibilidad Solucion Numero Condicion]].

---

## Ejemplo

> [!ejemplo]
> **Sistema mal condicionado de orden 2.** Sea
> $$A = \begin{pmatrix} 1 & 1 \\ 1 & 1.0001 \end{pmatrix}, \quad b = \begin{pmatrix} 2 \\ 2.0001 \end{pmatrix}, \quad x = \begin{pmatrix} 1 \\ 1 \end{pmatrix}.$$
> La solución aproximada $\tilde x = (2,\,0)^T$ produce residuo
> $$r = b - A\tilde x = \begin{pmatrix} 0 \\ -0.0001 \end{pmatrix}, \quad \|r\|_\infty = 10^{-4},$$
> **muy pequeño**, pese a que el error $\|\tilde x - x\|_\infty = 1$ es enorme. La causa es $\kappa_\infty(A) \approx 4\times10^4$: residuo y error difieren en cuatro órdenes de magnitud.

---

## Estrategias de control del error

> [!info]
> Herramientas prácticas para acotar y reducir el error de una solución directa:
>
> | Estrategia | Función |
> |:---|:---|
> | Cálculo del residuo $r = b - A\tilde x$ | Diagnóstico barato ($O(n^2)$) del error hacia atrás |
> | [[Pivoteo Parcial Total Estabilidad\|Pivoteo]] | Controla el factor de crecimiento $\rho$, garantiza estabilidad hacia atrás |
> | Estimación de $\kappa(A)$ | Predice los dígitos correctos perdidos |
> | Refinamiento iterativo | Resuelve $A\,\delta = r$ y corrige $\tilde x \leftarrow \tilde x + \delta$ para recuperar precisión |

---

## Resumen

| Concepto | Nota |
|:---|:---|
| Residuo vs error, error hacia atrás | [[Residuo vs Error Relativo Solucion]] |
| Cotas de sensibilidad, $\kappa(A)$ | [[Sensibilidad Solucion Numero Condicion]] |
| Sensibilidad intrínseca del problema | [[Condicionamiento Numerico Numero Condicion]] |
| Estabilidad del algoritmo | [[Estabilidad Algoritmos Forward Backward]] |

> [!corolario]
> El análisis de error de los métodos directos separa lo medible (residuo) de lo deseado (error) y los une por el número de condición. Un residuo pequeño solo certifica estabilidad hacia atrás; la precisión real de $\tilde x$ depende además de $\kappa(A)$. Las dos notas hijas desarrollan, respectivamente, la relación [[Residuo vs Error Relativo Solucion|residuo–error]] y el [[Sensibilidad Solucion Numero Condicion|análisis de sensibilidad]] que cierra el estudio de fiabilidad de la solución.
