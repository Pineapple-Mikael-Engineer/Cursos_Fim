---
title: Construcción General — Etapas s y Orden p
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-inicial
  - runge-kutta
draft: false
aliases:
  - Construcción de Runge-Kutta
  - Condiciones de orden
  - Tabla de Butcher
  - Etapas y orden
---

# Construcción General: Etapas $s$ y Orden $p$

> [!definicion]
> Un **método de Runge-Kutta de $s$ etapas** se define por
> $$k_i = f\Big(t_n + c_i h,\ y_n + h\textstyle\sum_{j=1}^s a_{ij}k_j\Big), \qquad y_{n+1} = y_n + h\sum_{i=1}^s b_i k_i,$$
> con coeficientes $\{a_{ij}\}$, pesos $\{b_i\}$ y nodos $\{c_i\}$ recogidos en su **tabla de Butcher**.

> [!info]
> Los coeficientes se eligen imponiendo las **condiciones de orden**: ecuaciones que fuerzan a que la expansión de Taylor del método coincida con la de la solución exacta hasta orden $p$. El número de etapas $s$ acota el orden $p$ alcanzable.

---

## Condiciones de orden

> [!teorema]
> Imponiendo que el método reproduzca la serie de [[Metodos Serie Taylor Orden Superior|Taylor]] hasta orden $p$, los coeficientes deben satisfacer las **condiciones de orden**. Las primeras:
> $$\text{orden 1:}\ \sum_i b_i = 1, \qquad \text{orden 2:}\ \sum_i b_i c_i = \tfrac12,$$
> $$\text{orden 3:}\ \sum_i b_i c_i^2 = \tfrac13,\quad \sum_{i,j} b_i a_{ij} c_j = \tfrac16,$$
> junto con la consistencia $c_i = \sum_j a_{ij}$ (los nodos son sumas de filas de $A$).

> [!demostracion]
> Se desarrolla $y_{n+1}$ del método en potencias de $h$ y se compara término a término con la serie de Taylor de $y(t_{n+1})$. Igualar los coeficientes de $h^1, h^2, \dots, h^p$ produce el sistema de condiciones de orden. El número de condiciones crece **rápidamente** (relacionado con árboles con raíz de Butcher): 1 para orden 1, 2 para orden 2, 4 para orden 3, 8 para orden 4, 17 para orden 5...

---

## La barrera de Butcher: $s$ vs $p$

> [!teorema]
> Para métodos RK **explícitos**, el orden máximo $p$ alcanzable con $s$ etapas es:
>
> | Etapas $s$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
> |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
> | Orden máx. $p$ | 1 | 2 | 3 | 4 | 4 | 5 | 6 | 6 |
>
> Hasta orden 4, $p = s$ (una etapa por orden). A partir de orden 5, hace falta **más** etapas que el orden (**barreras de Butcher**): por eso RK4 es el punto óptimo de eficiencia.

> [!info]
> Esta tabla explica la popularidad de [[RK4 Clasico Tabla Butcher y Orden Cuatro|RK4]]: es el orden más alto que se obtiene con $s=p$ (sin etapas "desperdiciadas"). Subir a orden 5 cuesta una etapa extra; los métodos adaptativos modernos ([[Control Paso Adaptativo RK45 Dormand Prince|Dormand-Prince]]) usan 6-7 etapas para orden 5 con par encajado.

---

## Ejemplo: derivar RK2

> [!ejemplo]
> **Familia RK de 2 etapas.** Con tabla
> $$\begin{array}{c|cc} 0 & 0 & 0 \\ c_2 & c_2 & 0 \\ \hline & b_1 & b_2 \end{array}$$
> las condiciones de orden 2 son $b_1 + b_2 = 1$ y $b_2 c_2 = \tfrac12$. Es un sistema con **un parámetro libre**: eligiendo $c_2$ se obtienen distintos métodos de [[RK2 Heun Euler Modificado Punto Medio|orden 2]]:
> - $c_2 = 1$: $b_1=b_2=\tfrac12$ → **Heun** (trapecio).
> - $c_2 = \tfrac12$: $b_1=0, b_2=1$ → **punto medio**.
>
> Todos son orden 2; difieren en la constante de error.

---

## Explícito vs implícito

> [!info]
> | | Explícito | Implícito |
> |:---|:---|:---|
> | Matriz $A$ | estrictamente triangular inferior | llena o triangular con diagonal |
> | Cálculo de $k_i$ | secuencial, directo | sistema acoplado (Newton) |
> | Orden con $s$ etapas | $\leq s$ (barrera de Butcher) | hasta $2s$ (Gauss-RK) |
> | Estabilidad | condicional | puede ser A-estable |
> | Uso | no rígidos | [[Rigidez Stiffness Problemas Ingenieria\|rígidos]] |
>
> Los RK **implícitos de Gauss** alcanzan orden $2s$ (relacionados con la [[Cuadratura Gaussiana/index|cuadratura gaussiana]]) y son A-estables, ideales para rigidez, a costa de resolver sistemas.

---

## Relación con otras notas

> [!info]
> - La idea de imitar Taylor: [[Metodos Serie Taylor Orden Superior]].
> - Los casos concretos: [[RK2 Heun Euler Modificado Punto Medio]] y [[RK4 Clasico Tabla Butcher y Orden Cuatro]].
> - El uso del par encajado: [[Control Paso Adaptativo RK45 Dormand Prince]].
> - La conexión Gauss-RK: [[Cuadratura Gaussiana/index]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Etapas | $k_i = f(t_n+c_ih, y_n+h\sum a_{ij}k_j)$ |
| Actualización | $y_{n+1} = y_n + h\sum b_i k_i$ |
| Tabla de Butcher | $(c, A, b)$ |
| Condiciones de orden | $\sum b_i=1$, $\sum b_ic_i=\tfrac12$, ... |
| Barrera | $p=s$ hasta orden 4; $p<s$ después |
| Explícito | $A$ estrictamente triangular inferior |

> [!corolario]
> Un método de Runge-Kutta de $s$ etapas se define por su tabla de Butcher $(c, A, b)$, cuyos coeficientes se fijan imponiendo las condiciones de orden que igualan su expansión a la de [[Metodos Serie Taylor Orden Superior|Taylor]] hasta orden $p$. El número de condiciones crece como los árboles de Butcher, y las barreras de Butcher limitan el orden: $p=s$ solo hasta orden 4, lo que hace de [[RK4 Clasico Tabla Butcher y Orden Cuatro|RK4]] el óptimo de eficiencia explícita. Los RK implícitos de Gauss alcanzan orden $2s$ y A-estabilidad —ligados a la [[Cuadratura Gaussiana/index|cuadratura gaussiana]]— para problemas [[Rigidez Stiffness Problemas Ingenieria|rígidos]].
