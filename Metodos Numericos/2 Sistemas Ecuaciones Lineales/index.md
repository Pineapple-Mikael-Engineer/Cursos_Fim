---
title: Sistemas de Ecuaciones Lineales
order: 2
tags:
  - metodos-numericos
  - teoria
  - sistemas-lineales
  - index
draft: false
aliases:
  - sistemas de ecuaciones lineales
  - sistemas lineales
  - linear systems
  - Ax=b
---

# Sistemas de Ecuaciones Lineales

> [!definicion]
> Resolver un **sistema lineal** $A\mathbf{x}=\mathbf{b}$ (con $A\in\mathbb{R}^{n\times n}$) es el problema más frecuente del cálculo numérico: aparece al discretizar EDPs, ajustar datos, o como paso interno de métodos no lineales. Hay dos familias de métodos —**directos** (dan la solución exacta salvo redondeo, en un número fijo de pasos) e **iterativos** (aproximan la solución con una sucesión que converge)— y un problema hermano, el de **valores y vectores propios**.

> [!info]
> Segundo bloque del curso. Se apoya en la [[1 Teoria Errores Analisis Estabilidad/index| teoría de errores]] (el [[Condicionamiento Numerico Numero Condicion| número de condición]] de $A$ decide cuánta precisión se pierde) y alimenta casi todo lo demás. Burden–Faires, cap. 6–7; Chapra, cap. 9–11.

## Cómo se resuelve $A\mathbf{x}=\mathbf{b}$

> [!teoria] Directos, iterativos y espectrales
> - **Métodos directos**: eliminación de Gauss y factorizaciones ($LU$, Cholesky). Cuestan $\mathcal{O}(n^3)$ y dan la solución en un número finito de pasos; ideales para $n$ moderado y varios lados derechos. → [[2 Sistemas Ecuaciones Lineales/Metodos Directos/index| Métodos directos]].
> - **Métodos iterativos**: Jacobi, Gauss–Seidel, SOR. Parten de una estimación y la refinan; convienen para sistemas **grandes y dispersos**. Convergen si se cumplen condiciones sobre $A$ (radio espectral, diagonal dominante). → [[2 Sistemas Ecuaciones Lineales/Metodos Iterativos/index| Métodos iterativos]].
> - **Valores y vectores propios**: el problema $A\mathbf{v}=\lambda\mathbf{v}$, resuelto con el método de la potencia y sus variantes o con $QR$. → [[2 Sistemas Ecuaciones Lineales/Valores Vectores Propios/index| Valores y vectores propios]].

## Mapa de la sección

> [!info] Las subsecciones
> | Subsección | Contenido |
> |:---|:---|
> | [[2 Sistemas Ecuaciones Lineales/Metodos Directos/index\| Métodos directos]] | Gauss, $LU$, Cholesky; análisis de error |
> | [[2 Sistemas Ecuaciones Lineales/Metodos Iterativos/index\| Métodos iterativos]] | Jacobi, Gauss–Seidel; convergencia |
> | [[2 Sistemas Ecuaciones Lineales/Valores Vectores Propios/index\| Valores y vectores propios]] | método de la potencia, $QR$ |

> [!corolario]
> Directos para sistemas densos de tamaño moderado; iterativos para los grandes y dispersos. En ambos casos, el **condicionamiento** de $A$ marca el techo de precisión alcanzable, y el problema espectral abre la puerta a estabilidad, vibraciones y convergencia de los propios iterativos.

> [!referencia]
> Burden–Faires, *Análisis Numérico*, cap. 6–7. Chapra–Canale, cap. 9–11.
