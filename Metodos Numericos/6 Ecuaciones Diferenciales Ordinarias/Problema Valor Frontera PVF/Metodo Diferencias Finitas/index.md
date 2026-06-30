---
title: Método de Diferencias Finitas (PVF)
order: 1
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-frontera
  - diferencias-finitas
  - index
draft: false
aliases:
  - Diferencias finitas para PVF
  - Finite differences BVP
  - Método de diferencias finitas
---

# Método de Diferencias Finitas (PVF)

> [!definicion]
> El **método de diferencias finitas** resuelve un [[Problema Valor Frontera PVF/index|PVF]] discretizando el dominio en una malla y reemplazando las derivadas por [[Aproximacion Diferencias Finitas Serie Taylor|fórmulas de diferencias finitas]]. El resultado es un **sistema de ecuaciones algebraicas** —tridiagonal en 1D— cuya solución son los valores de $y$ en los nodos.

> [!info]
> Convierte un problema continuo (resolver una EDO) en uno discreto (resolver un sistema lineal), trasladando toda la maquinaria del [[2 Sistemas Ecuaciones Lineales/index|álgebra lineal numérica]]. Es el método base de las simulaciones de equilibrio y la puerta de entrada a las diferencias finitas para EDPs.

---

## Las cuatro piezas

> [!info]
> - **[[Discretizacion Dominio y Aproximacion Centrada|Discretización]]:** malla, nodos y aproximación de $y'$, $y''$ por [[Orden Error Progresiva Regresiva Centrada|diferencias centradas]] ($O(h^2)$).
> - **[[Construccion Sistema Tridiagonal Lineal|Sistema tridiagonal]]:** cómo las ecuaciones nodales se ensamblan en una matriz tridiagonal, resoluble en $O(N)$.
> - **[[Consistencia Estabilidad Convergencia Lax|Consistencia, estabilidad, convergencia]]:** el teorema de equivalencia de Lax, que garantiza que el esquema converge.
> - **[[Tratamiento Condiciones Frontera Dirichlet Neumann|Condiciones de frontera]]:** cómo incorporar Dirichlet (valor) y Neumann (derivada) en el sistema.

---

## Ejemplo

> [!ejemplo]
> **Deflexión de una viga: $y'' = q/(EI)$, $y(0)=y(L)=0$** (apoyos simples), $q/(EI)$ constante, $L=1$, $N=4$ ($h=0.25$). La diferencia centrada $y''_i \approx (y_{i-1}-2y_i+y_{i+1})/h^2$ en cada nodo interno da:
> $$\frac{y_{i-1} - 2y_i + y_{i+1}}{h^2} = \frac{q}{EI}, \qquad i=1,2,3,$$
> con $y_0 = y_4 = 0$. Es un sistema tridiagonal $3\times3$ cuya solución aproxima la curva de deflexión (parábola), con error $O(h^2)$.

---

## Estructura del método

> [!teoria]
> El flujo de trabajo:
> 1. **Discretizar:** $x_i = a + ih$, $i=0,\dots,N$, con $h=(b-a)/N$.
> 2. **Sustituir** derivadas por diferencias finitas en cada nodo interno.
> 3. **Ensamblar** el sistema lineal $A\mathbf{y} = \mathbf{b}$ (tridiagonal).
> 4. **Imponer** las condiciones de frontera (modifican primera/última ecuación).
> 5. **Resolver** por [[Construccion Sistema Tridiagonal Lineal|algoritmo de Thomas]] ($O(N)$).

---

## Resumen

| Tema | Nota |
|:---|:---|
| Malla y aproximación centrada | [[Discretizacion Dominio y Aproximacion Centrada]] |
| Ensamblaje del sistema tridiagonal | [[Construccion Sistema Tridiagonal Lineal]] |
| Convergencia (teorema de Lax) | [[Consistencia Estabilidad Convergencia Lax]] |
| Condiciones Dirichlet y Neumann | [[Tratamiento Condiciones Frontera Dirichlet Neumann]] |

> [!corolario]
> El método de diferencias finitas discretiza el dominio y reemplaza las derivadas por [[Discretizacion Dominio y Aproximacion Centrada|aproximaciones centradas]], transformando el PVF en un [[Construccion Sistema Tridiagonal Lineal|sistema lineal tridiagonal]] resoluble en $O(N)$ por el algoritmo de Thomas. Su convergencia la garantiza el [[Consistencia Estabilidad Convergencia Lax|teorema de Lax]] (consistencia + estabilidad), y las [[Tratamiento Condiciones Frontera Dirichlet Neumann|condiciones de frontera]] Dirichlet/Neumann se incorporan modificando las ecuaciones de los bordes. Resuelve todos los nodos simultáneamente, en contraste con el [[Metodo Disparo Shooting/index|disparo]], y es la base de las diferencias finitas para EDPs.
