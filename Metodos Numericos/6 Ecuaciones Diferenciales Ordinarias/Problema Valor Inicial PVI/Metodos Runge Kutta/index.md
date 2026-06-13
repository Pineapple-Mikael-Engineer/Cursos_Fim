---
title: Métodos de Runge-Kutta
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-inicial
  - runge-kutta
  - index
draft: false
aliases:
  - Runge-Kutta
  - Métodos de Runge-Kutta
  - RK methods
---

# Métodos de Runge-Kutta

> [!definicion]
> Los **métodos de Runge-Kutta** (RK) alcanzan alto orden evaluando $f$ en varios puntos intermedios (**etapas**) dentro de cada paso y combinando los resultados con pesos cuidadosamente elegidos:
> $$y_{n+1} = y_n + h\sum_{i=1}^s b_i k_i, \qquad k_i = f\Big(t_n + c_i h,\ y_n + h\sum_{j} a_{ij}k_j\Big).$$

> [!info]
> Son los métodos de un paso **más usados**: reproducen la serie de [[Metodos Serie Taylor Orden Superior|Taylor]] hasta orden $p$ **sin calcular derivadas** de $f$, solo evaluándola. [[RK4 Clasico Tabla Butcher y Orden Cuatro|RK4]] es el caballo de batalla de la simulación física; las versiones [[Control Paso Adaptativo RK45 Dormand Prince|adaptativas]] ajustan el paso automáticamente.

---

## La idea: Taylor sin derivadas

> [!teoria]
> En lugar de calcular $f_t, f_y, \dots$ (como [[Metodos Serie Taylor Orden Superior|Taylor]]), RK evalúa $f$ en puntos $(t_n+c_i h,\ \cdot)$ y ajusta los pesos $b_i$, nodos $c_i$ y coeficientes $a_{ij}$ para que la expansión del método coincida con la de Taylor hasta orden $p$. Toda la información del método cabe en su **tabla de Butcher**.

## Componentes de la teoría

> [!info]
> - **[[Construccion General Etapas s y Orden p|Construcción general]]:** etapas $s$, condiciones de orden, tabla de Butcher, relación entre $s$ y el orden $p$ alcanzable.
> - **[[RK2 Heun Euler Modificado Punto Medio|RK2]]:** los métodos de 2 etapas (Heun, punto medio, Euler modificado), orden 2.
> - **[[RK4 Clasico Tabla Butcher y Orden Cuatro|RK4 clásico]]:** el método de 4 etapas y orden 4, el más usado.
> - **[[Control Paso Adaptativo RK45 Dormand Prince|Paso adaptativo]]:** RK45, pares encajados, control automático del error.
> - **[[Regiones Estabilidad Absoluta A Estabilidad|Estabilidad]]:** las regiones de estabilidad absoluta de cada RK.

---

## Ejemplo

> [!ejemplo]
> **$y'=y$, $y(0)=1$ hasta $t=1$ (exacta $e\approx2.71828$), $h=0.25$:**
>
> | Método | Etapas | $y(1)$ | Error |
> |:---|:---:|:---:|:---:|
> | [[Euler Explicito Orden 1 Interpretacion Geometrica\|Euler]] | 1 | 2.44141 | $2.8\times10^{-1}$ |
> | [[RK2 Heun Euler Modificado Punto Medio\|RK2 (Heun)]] | 2 | 2.69409 | $2.4\times10^{-2}$ |
> | [[RK4 Clasico Tabla Butcher y Orden Cuatro\|RK4]] | 4 | 2.71821 | $7\times10^{-5}$ |
>
> Cada salto de orden mejora drásticamente la precisión; RK4, con 4 evaluaciones por paso, da $\sim5$ cifras correctas donde Euler da 0.

---

## Tabla de Butcher

> [!teoria]
> Todo RK se codifica en una tabla:
> $$\begin{array}{c|c} \mathbf{c} & A \\ \hline & \mathbf{b}^T \end{array} = \begin{array}{c|cccc} c_1 & a_{11} & \cdots & a_{1s} \\ \vdots & \vdots & & \vdots \\ c_s & a_{s1} & \cdots & a_{ss} \\ \hline & b_1 & \cdots & b_s \end{array}$$
> Si $A$ es **estrictamente triangular inferior**, el método es **explícito** (cada $k_i$ usa solo etapas previas); si no, es **implícito** (sistema acoplado, útil para [[Rigidez Stiffness Problemas Ingenieria|rigidez]]).

---

## Resumen

| Tema | Nota |
|:---|:---|
| Construcción, etapas y orden | [[Construccion General Etapas s y Orden p]] |
| RK2 (Heun, punto medio) | [[RK2 Heun Euler Modificado Punto Medio]] |
| RK4 clásico | [[RK4 Clasico Tabla Butcher y Orden Cuatro]] |
| Paso adaptativo (RK45) | [[Control Paso Adaptativo RK45 Dormand Prince]] |
| Estabilidad absoluta | [[Regiones Estabilidad Absoluta A Estabilidad]] |

> [!corolario]
> Los métodos de Runge-Kutta logran alto orden evaluando $f$ en etapas intermedias y combinándolas con pesos que reproducen la serie de [[Metodos Serie Taylor Orden Superior|Taylor]] sin derivar $f$, codificados en la tabla de Butcher. [[RK4 Clasico Tabla Butcher y Orden Cuatro|RK4]] —orden 4 con 4 etapas— es el estándar de la simulación; los pares [[Control Paso Adaptativo RK45 Dormand Prince|encajados RK45]] controlan el error automáticamente, y las variantes implícitas atacan la [[Rigidez Stiffness Problemas Ingenieria|rigidez]]. Su [[Regiones Estabilidad Absoluta A Estabilidad|región de estabilidad]] determina el paso máximo seguro.
