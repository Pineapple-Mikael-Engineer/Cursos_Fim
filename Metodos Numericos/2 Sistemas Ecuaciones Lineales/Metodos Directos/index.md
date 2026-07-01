---
title: Métodos Directos
order: 1
tags:
  - metodos-numericos
  - teoria
  - sistemas-lineales
  - index
draft: false
aliases:
  - métodos directos
  - eliminación gaussiana
  - factorización LU
  - direct methods
---

# Métodos Directos

> [!definicion]
> Los **métodos directos** resuelven $A\mathbf{x}=\mathbf{b}$ en un **número finito de operaciones**, dando la solución exacta salvo el error de redondeo. La idea común es **triangularizar** el sistema (llevarlo a una forma escalonada) y resolver por sustitución. La **eliminación de Gauss** lo hace en un pase; las **factorizaciones** ($A=LU$, $A=LL^{T}$) guardan ese trabajo para reutilizarlo con varios lados derechos.

> [!info]
> Una de las dos vías para [[2 Sistemas Ecuaciones Lineales/index| resolver sistemas lineales]]. Convienen para matrices **densas** de tamaño moderado. Su coste es $\mathcal{O}(n^3)$ y su precisión depende del [[Condicionamiento Numerico Numero Condicion| condicionamiento]] y del **pivoteo**. Burden–Faires, cap. 6.

## De Gauss a las factorizaciones

> [!teoria] Triangularizar una vez, resolver muchas
> - **Eliminación gaussiana**: convierte $A$ en triangular superior con operaciones de fila; el **pivoteo** (parcial/total) evita dividir por números pequeños y mantiene la estabilidad. Cuesta $\sim\tfrac{2}{3}n^3$. → [[2 Sistemas Ecuaciones Lineales/Metodos Directos/Eliminacion Gaussiana/index| Eliminación gaussiana]].
> - **Factorización $LU$** (y **Cholesky** para matrices simétricas definidas positivas): separa el trabajo caro (factorizar $A$) del barato (resolver $L\mathbf{y}=\mathbf{b}$ y $U\mathbf{x}=\mathbf{y}$), de modo que **varios $\mathbf{b}$** salen casi gratis. → [[2 Sistemas Ecuaciones Lineales/Metodos Directos/Factorizacion LU/index| Factorización LU]].
> - **Análisis de error**: el residuo pequeño **no** garantiza solución exacta si $A$ está mal condicionada; la sensibilidad se mide con $\kappa(A)$. → [[2 Sistemas Ecuaciones Lineales/Metodos Directos/Analisis Error Directos/index| Análisis de error]].

## Mapa de la sección

> [!info] Las subsecciones
> | Subsección | Contenido |
> |:---|:---|
> | [[2 Sistemas Ecuaciones Lineales/Metodos Directos/Eliminacion Gaussiana/index\| Eliminación gaussiana]] | pivoteo, coste $\mathcal{O}(n^3)$, redondeo |
> | [[2 Sistemas Ecuaciones Lineales/Metodos Directos/Factorizacion LU/index\| Factorización LU]] | $LU$, Cholesky, Doolittle/Crout |
> | [[2 Sistemas Ecuaciones Lineales/Metodos Directos/Analisis Error Directos/index\| Análisis de error]] | residuo vs error, sensibilidad |

> [!corolario]
> Todo método directo es, en el fondo, **triangularizar y sustituir**. Factorizar en vez de eliminar amortiza el coste cuando hay varios lados derechos, y el pivoteo es lo que separa un algoritmo estable de uno que se rompe con un pivote pequeño.

> [!referencia]
> Burden–Faires, *Análisis Numérico*, cap. 6. Golub–Van Loan, *Matrix Computations*, cap. 3.
