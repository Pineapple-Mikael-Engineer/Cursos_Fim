---
title: Integradores Simplécticos y Conservación
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-inicial
  - sistemas-edo
  - simplecticos
draft: false
aliases:
  - Integradores simplécticos
  - Verlet
  - Leapfrog
  - Integración geométrica
  - Conservación de energía
  - Symplectic integrators
---

# Integradores Simplécticos y Conservación

> [!definicion]
> Un **integrador simpléctico** es un método para sistemas **hamiltonianos** (mecánica conservativa) que preserva la estructura geométrica del flujo: conserva el área en el espacio de fases y, con ella, mantiene la energía **acotada** a largo plazo. Son los métodos correctos para simular sistemas físicos sin disipación durante muchos periodos.

> [!info]
> Los métodos estándar fallan a largo plazo en mecánica: [[Euler Explicito Orden 1 Interpretacion Geometrica|Euler explícito]] **gana** energía (la órbita se abre en espiral), [[Euler Implicito Estabilidad Incondicional|Euler implícito]] la **pierde** (el péndulo se frena), e incluso [[RK4 Clasico Tabla Butcher y Orden Cuatro|RK4]] acumula una **deriva** lenta de energía. Los simplécticos no: su energía oscila en torno al valor exacto sin deriva secular. Por eso dominan en mecánica celeste y dinámica molecular.

---

## Sistemas hamiltonianos

> [!definicion]
> Un sistema **hamiltoniano** con coordenadas $\mathbf q$ y momentos $\mathbf p$ evoluciona según
> $$\dot{\mathbf q} = \frac{\partial H}{\partial \mathbf p}, \qquad \dot{\mathbf p} = -\frac{\partial H}{\partial \mathbf q},$$
> donde $H(\mathbf q, \mathbf p)$ es la **energía** (hamiltoniano), conservada por el flujo exacto. Para una partícula, $H = \frac{|\mathbf p|^2}{2m} + V(\mathbf q)$ (cinética + potencial).

> [!info]
> El flujo exacto preserva el **volumen** en el espacio de fases (teorema de Liouville) y la forma simpléctica $d\mathbf q\wedge d\mathbf p$. Un integrador simpléctico imita esta propiedad geométrica **exactamente** (no solo aproximadamente), lo que le da su comportamiento energético superior.

---

## El método de Verlet / leapfrog

> [!teorema]
> Para $\ddot{\mathbf q} = -\nabla V(\mathbf q)/m = \mathbf a(\mathbf q)$, el **Verlet de velocidades** avanza posición y velocidad de forma intercalada:
> $$\mathbf v_{n+1/2} = \mathbf v_n + \tfrac{h}{2}\mathbf a(\mathbf q_n), \qquad \mathbf q_{n+1} = \mathbf q_n + h\,\mathbf v_{n+1/2}, \qquad \mathbf v_{n+1} = \mathbf v_{n+1/2} + \tfrac{h}{2}\mathbf a(\mathbf q_{n+1}).$$
> Es de **orden 2**, simpléctico, **reversible en el tiempo** y requiere **una sola** evaluación de fuerza por paso.

> [!info]
> El nombre *leapfrog* ("rana saltando") viene de que posiciones y velocidades se evalúan en instantes intercalados ($\mathbf q$ en pasos enteros, $\mathbf v$ en medios pasos). Es el integrador más usado en simulación molecular y de N cuerpos por su eficiencia y fidelidad.

---

## Euler simpléctico

> [!teorema]
> El **Euler simpléctico** (semi-implícito) es el simpléctico más simple: actualiza la velocidad **antes** que la posición usando la velocidad **ya actualizada**:
> $$\mathbf v_{n+1} = \mathbf v_n + h\,\mathbf a(\mathbf q_n), \qquad \mathbf q_{n+1} = \mathbf q_n + h\,\mathbf v_{n+1}.$$
> Orden 1, pero —a diferencia del Euler explícito— **conserva la energía acotada**. El cambio es mínimo (usar $\mathbf v_{n+1}$ en lugar de $\mathbf v_n$ para $\mathbf q$), pero el efecto a largo plazo es radical.

> [!ejemplo]
> **Oscilador armónico $\ddot x = -x$**, energía $E = \frac12(x^2+v^2)$, integrado $10\,000$ periodos:
>
> | Método | Energía tras $10^4$ periodos | Órbita en el plano de fases |
> |:---|:---|:---|
> | [[Euler Explicito Orden 1 Interpretacion Geometrica\|Euler explícito]] | crece $\to\infty$ | espiral hacia afuera |
> | [[Euler Implicito Estabilidad Incondicional\|Euler implícito]] | decae $\to0$ | espiral hacia adentro |
> | Euler simpléctico | **oscila en torno a $E_0$** | elipse cerrada (ligeramente deformada) |
> | [[RK4 Clasico Tabla Butcher y Orden Cuatro\|RK4]] | deriva lenta | elipse que encoge muy despacio |
>
> Solo el simpléctico mantiene la órbita cerrada indefinidamente: la energía oscila pero **no deriva**.

---

## Por qué conservan la energía

> [!teoria]
> Un integrador simpléctico no conserva $H$ exactamente, pero conserva **exactamente** un hamiltoniano modificado $\tilde H = H + O(h^p)$ cercano al real (teoría del **análisis hacia atrás** / backward error analysis). Como $\tilde H$ es una constante del movimiento numérico, la energía real $H$ permanece **acotada** (oscila en torno a $\tilde H$) durante tiempos exponencialmente largos, sin deriva secular. Esta es la diferencia esencial con RK4, que no conserva ningún hamiltoniano cercano y por eso deriva.

> [!info]
> Es el mismo espíritu del [[Estabilidad Algoritmos Forward Backward|análisis hacia atrás]] de la estabilidad numérica: el método resuelve **exactamente** un problema ligeramente modificado. Aquí ese problema modificado es también un sistema hamiltoniano, lo que garantiza buen comportamiento energético.

---

## Algoritmo

> [!algoritmo]
> **Verlet de velocidades para un sistema orbital.**
>
> ```python
> import numpy as np
>
> def verlet(aceleracion, q0, v0, h, N):
>     q, v = np.array(q0, float), np.array(v0, float)
>     a = aceleracion(q)
>     traj = [q.copy()]
>     for _ in range(N):
>         v_half = v + 0.5*h*a
>         q = q + h*v_half
>         a = aceleracion(q)            # una sola evaluación de fuerza
>         v = v_half + 0.5*h*a
>         traj.append(q.copy())
>     return np.array(traj)
>
> # Órbita kepleriana: a(q) = -q / |q|^3
> acc = lambda q: -q / np.linalg.norm(q)**3
> orbita = verlet(acc, [1.0, 0.0], [0.0, 0.9], 0.01, 100000)  # 100k pasos estables
> ```

---

## Cuándo usar simplécticos

> [!info]
> | Situación | Método |
> |:---|:---|
> | Mecánica conservativa, largo plazo (órbitas, moléculas) | **Verlet / simpléctico** |
> | Integración corta y precisa | [[RK4 Clasico Tabla Butcher y Orden Cuatro\|RK4]] / [[Control Paso Adaptativo RK45 Dormand Prince\|RK45]] |
> | Sistema disipativo (con rozamiento) | RK estándar o implícito |
> | Sistema [[Rigidez Stiffness Problemas Ingenieria\|rígido]] | implícito A-estable |

> [!warning]
> Los simplécticos requieren **paso fijo**: el control adaptativo destruye la propiedad simpléctica (cambiar $h$ rompe la conservación del hamiltoniano modificado). Tampoco sirven para sistemas con disipación, donde la energía *debe* decaer. Su nicho es la dinámica conservativa de largo plazo.

---

## Relación con otras notas

> [!info]
> - Los métodos que fallan en conservación: [[Euler Explicito Orden 1 Interpretacion Geometrica]], [[Euler Implicito Estabilidad Incondicional]], [[RK4 Clasico Tabla Butcher y Orden Cuatro]].
> - La reducción a sistema de primer orden de la mecánica: [[Reduccion EDO Orden n a Sistema Primer Orden]].
> - El análisis hacia atrás que explica la conservación: [[Estabilidad Algoritmos Forward Backward]].
> - El panorama de sistemas físicos: [[Sistemas EDO y Orden Superior/index]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Aplicación | sistemas hamiltonianos (conservativos) |
| Verlet | orden 2, 1 evaluación de fuerza, reversible |
| Euler simpléctico | orden 1, usa $v_{n+1}$ para $q$ |
| Propiedad clave | conserva un $\tilde H = H + O(h^p)$ exacto |
| Energía | acotada, sin deriva secular |
| Requisito | paso fijo, sistema sin disipación |

> [!corolario]
> Los integradores simplécticos preservan la estructura geométrica de los sistemas hamiltonianos, conservando exactamente un hamiltoniano modificado $\tilde H = H + O(h^p)$ que mantiene la energía real **acotada sin deriva** durante tiempos enormes. El Verlet/leapfrog (orden 2, una evaluación de fuerza, reversible) y el Euler simpléctico son los más usados, y superan a [[RK4 Clasico Tabla Butcher y Orden Cuatro|RK4]] —que deriva— en mecánica celeste y dinámica molecular de largo plazo. Su precio es exigir paso fijo y no aplicar a sistemas disipativos. Junto con los métodos para [[Rigidez Stiffness Problemas Ingenieria|rigidez]], completan el arsenal para simular fielmente cualquier sistema físico, cerrando el estudio del [[Problema Valor Inicial PVI/index|problema de valor inicial]].
