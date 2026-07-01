---
title: Convergencia de Métodos Iterativos
order: 4
tags:
  - metodos-numericos
  - teoria
  - sistemas-lineales
  - index
draft: false
aliases:
  - convergencia de métodos iterativos
  - convergencia iterativa
  - convergence of iterative methods
---

# Convergencia de Métodos Iterativos

> [!definicion]
> Un método iterativo ($\mathbf{x}^{(k+1)}=T\mathbf{x}^{(k)}+\mathbf{c}$) solo sirve si la sucesión **converge** a la solución. Esta sección reúne los **criterios** que lo garantizan y las **cotas** para estimar el error sin conocer la solución exacta. La condición clave es sobre la **matriz de iteración** $T$: converge para cualquier $\mathbf{x}^{(0)}$ **si y solo si** su **radio espectral** cumple $\rho(T)<1$.

> [!info]
> El fundamento teórico de los [[2 Sistemas Ecuaciones Lineales/Metodos Iterativos/index| métodos iterativos]] (Jacobi, Gauss–Seidel). Dice **cuándo** convergen y **cómo de rápido**, ligando la práctica con el álgebra de $T$. Burden–Faires, cap. 7.

## Cuándo y cuán rápido converge

> [!teoria] Del radio espectral a las cotas de error
> - **Criterio general**: $\rho(T)<1\iff$ converge; cuanto menor $\rho(T)$, más rápido. → [[Criterio Radio Espectral Convergencia]].
> - **Condiciones suficientes prácticas**: si $A$ es de **diagonal estrictamente dominante**, Jacobi y Gauss–Seidel convergen sin calcular $\rho(T)$. → [[Teorema Diagonal Dominante Estricta]].
> - **Comparar métodos**: el **teorema de Stein–Rosenberg** relaciona la convergencia (y velocidad) de Jacobi y Gauss–Seidel. → [[Teorema Stein-Rosenberg]].
> - **Estimar el error**: cotas **a priori** que acotan $\|\mathbf{x}^{(k)}-\mathbf{x}\|$ a partir de $\rho(T)$ o de una norma de $T$, para decidir cuántas iteraciones bastan. → [[Estimacion Error y Cotas A Priori]].

## Mapa de la sección

> [!info] Las notas
> | Nota | Contenido |
> |:---|:---|
> | [[Criterio Radio Espectral Convergencia]] | $\rho(T)<1$: criterio necesario y suficiente |
> | [[Teorema Diagonal Dominante Estricta]] | condición suficiente cómoda de verificar |
> | [[Teorema Stein-Rosenberg]] | Jacobi vs Gauss–Seidel |
> | [[Estimacion Error y Cotas A Priori]] | cotas del error e iteraciones necesarias |

> [!corolario]
> Toda la convergencia iterativa se decide en la **matriz de iteración** $T$: $\rho(T)<1$ es el veredicto exacto, la diagonal dominante es el atajo práctico, y las cotas a priori traducen $\rho(T)$ en un número concreto de iteraciones.

> [!referencia]
> Burden–Faires, *Análisis Numérico*, cap. 7. Varga, *Matrix Iterative Analysis*.
