---
title: Sistemas de EDO y Orden Superior
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-inicial
  - sistemas-edo
  - index
draft: false
aliases:
  - Sistemas de EDO
  - EDO de orden superior
  - Systems of ODEs
---

# Sistemas de EDO y Orden Superior

> [!definicion]
> Un **sistema de EDOs** de primer orden es $\mathbf{y}' = \mathbf{f}(t, \mathbf{y})$ con $\mathbf{y}\in\mathbb{R}^m$. Toda EDO de **orden $n$** (como la segunda ley de Newton $m\ddot x = F$) se reescribe como un sistema de primer orden, al que se aplican directamente los métodos vectoriales.

> [!info]
> Esta es la forma en que se simulan los sistemas físicos reales: rara vez aparecen como una sola EDO escalar de primer orden. La mecánica es de segundo orden, los circuitos acoplados son sistemas, y todos se reducen a la forma estándar $\mathbf y' = \mathbf f(t,\mathbf y)$.

---

## Componentes

> [!info]
> - **[[Reduccion EDO Orden n a Sistema Primer Orden|Reducción de orden]]:** cómo convertir $y^{(n)} = g(t, y, y', \dots)$ en un sistema de $n$ ecuaciones de primer orden. El truco universal de la simulación física.
> - **[[Acoplamiento Metodos Sistemas Runge Kutta|Métodos vectoriales]]:** cómo Euler, RK y demás se aplican componente a componente (vectorialmente) sin cambios.
> - **[[Rigidez Stiffness Problemas Ingenieria|Rigidez]]:** sistemas con escalas de tiempo muy dispares (autovalores de la jacobiana muy distintos), que exigen métodos implícitos.
> - **[[Integradores Simplecticos Conservacion|Integradores simplécticos]]:** para sistemas conservativos (hamiltonianos), métodos que preservan energía y estructura geométrica a largo plazo.

---

## Ejemplo: el péndulo como sistema

> [!ejemplo]
> **Péndulo $\ddot\theta = -\frac{g}{L}\sin\theta$** (orden 2). Con $\omega = \dot\theta$ se vuelve un sistema de primer orden en $\mathbf y = (\theta, \omega)$:
> $$\mathbf y' = \begin{pmatrix} \dot\theta \\ \dot\omega \end{pmatrix} = \begin{pmatrix} \omega \\ -\frac{g}{L}\sin\theta \end{pmatrix} = \mathbf f(\mathbf y).$$
> Cualquier método ([[RK4 Clasico Tabla Butcher y Orden Cuatro|RK4]], etc.) avanza el **vector** $(\theta_n, \omega_n)$ con la **misma** fórmula que en el caso escalar. El plano $(\theta, \omega)$ es el espacio de fases del sistema.

---

## Estructura general de la simulación física

> [!teoria]
> El flujo de trabajo para simular cualquier sistema físico:
> 1. Escribir las leyes (Newton, Kirchhoff, balances) como EDOs de orden alto.
> 2. [[Reduccion EDO Orden n a Sistema Primer Orden|Reducir]] a $\mathbf y' = \mathbf f(t, \mathbf y)$ de primer orden.
> 3. Elegir el método según las propiedades: no rígido → [[RK4 Clasico Tabla Butcher y Orden Cuatro|RK4]]/[[Control Paso Adaptativo RK45 Dormand Prince|RK45]]; rígido → implícito; conservativo de largo plazo → [[Integradores Simplecticos Conservacion|simpléctico]].
> 4. Integrar y analizar (trayectorias, espacio de fases, invariantes).

---

## Resumen

| Tema | Nota |
|:---|:---|
| Reducción de orden $n$ a primer orden | [[Reduccion EDO Orden n a Sistema Primer Orden]] |
| Métodos vectoriales (RK para sistemas) | [[Acoplamiento Metodos Sistemas Runge Kutta]] |
| Rigidez | [[Rigidez Stiffness Problemas Ingenieria]] |
| Integradores simplécticos y conservación | [[Integradores Simplecticos Conservacion]] |

> [!corolario]
> Todo sistema físico —mecánico, circuital, reactivo— se modela con EDOs de orden alto o acopladas que se [[Reduccion EDO Orden n a Sistema Primer Orden|reducen]] a la forma estándar de primer orden $\mathbf y'=\mathbf f(t,\mathbf y)$, sobre la que los métodos de un paso actúan [[Acoplamiento Metodos Sistemas Runge Kutta|vectorialmente]] sin cambios. La elección del método depende de las propiedades del sistema: [[Rigidez Stiffness Problemas Ingenieria|rigidez]] (implícitos) o carácter [[Integradores Simplecticos Conservacion|conservativo]] (simplécticos). Este es el núcleo práctico de la programación de simulaciones físicas.
