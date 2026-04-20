---
title: "Invarianza Temporal"
tags:
  - control-clasico
  - sistemas-lineales
  - propiedades
draft: false
aliases:
  - Time-Invariance
  - Sistemas Invariantes en el Tiempo
  - LTI
---

# Invarianza Temporal

> [!definicion] Definición Formal
> Sea un sistema con operador $\mathcal{H}$ que mapea entrada $u(t)$ a salida $y(t) = \mathcal{H}[u(t)]$. El sistema es **invariante en el tiempo** si para todo $\tau \in \mathbb{R}$:
> $$
> \mathcal{H}[u(t - \tau)] = y(t - \tau) \quad \forall u(t)
> $$
> Es decir, el operador $\mathcal{H}$ conmuta con el operador desplazamiento temporal $T_\tau$:
> $$
> \mathcal{H} \circ T_\tau = T_\tau \circ \mathcal{H}
> $$

---

## Caracterización Matemática

> [!teorema] Condición de Coeficientes Constantes
> Un sistema descripto por una ecuación diferencial ordinaria lineal es invariante en el tiempo **si y solo si** todos los coeficientes son constantes:
> $$
> \sum_{k=0}^{n} a_k \frac{d^k y}{dt^k} = \sum_{k=0}^{m} b_k \frac{d^k u}{dt^k}, \quad a_k, b_k \in \mathbb{R}
> $$
> Si algún coeficiente depende explícitamente de $t$, el sistema es **variante**.

> [!demostracion]
> Sea la ecuación $\sum a_k(t) y^{(k)} = \sum b_k(t) u^{(k)}$. Definimos $u_\tau(t) = u(t-\tau)$ y $y_\tau(t)$ como la respuesta correspondiente. Por definición de invarianza, se requiere $y_\tau(t) = y(t-\tau)$. Derivando: $y_\tau^{(k)}(t) = y^{(k)}(t-\tau)$. Sustituyendo en la ecuación original con coeficientes $a_k(t)$:
> $$
> \sum a_k(t) y_\tau^{(k)}(t) = \sum b_k(t) u_\tau^{(k)}(t)
> $$
> Para que $y_\tau(t) = y(t-\tau)$ sea solución, los coeficientes deben satisfacer $a_k(t) = a_k(t-\tau)$ para todo $\tau$, lo cual implica $a_k$ constante. Análogamente para $b_k$. $\square$

---

## Sistemas Invariantes (Ejemplos Matemáticos)

> [!ejemplo] Sistemas con coeficientes constantes
> | Sistema | Ecuación | ¿Invariante? |
> |---------|----------|---------------|
> | Resistor | $v(t) = R \cdot i(t)$ | Sí, $R$ constante |
> | Resorte amortiguado | $m\ddot{x} + c\dot{x} + kx = F(t)$ | Sí, $m,c,k$ constantes |
> | Filtro RC | $\dot{v}_o + \frac{1}{RC}v_o = \frac{1}{RC}v_i$ | Sí, $RC$ constante |

> [!ejemplo] Verificación directa de invarianza
> Dado $y(t) = \int_{-\infty}^{t} e^{-(t-\sigma)} u(\sigma) d\sigma$:
> - Para $u_\tau(t) = u(t-\tau)$:
> $$
> y_\tau(t) = \int_{-\infty}^{t} e^{-(t-\sigma)} u(\sigma - \tau) d\sigma
> $$
> - Cambio de variable $\lambda = \sigma - \tau$:
> $$
> y_\tau(t) = \int_{-\infty}^{t-\tau} e^{-(t - (\lambda + \tau))} u(\lambda) d\lambda = \int_{-\infty}^{t-\tau} e^{-((t-\tau) - \lambda)} u(\lambda) d\lambda = y(t-\tau)
> $$
> - Se cumple la condición $\Rightarrow$ sistema invariante.

---

## Sistemas Variantes (Ejemplos Matemáticos)

> [!ejemplo] Sistemas con coeficientes dependientes del tiempo
> | Sistema | Ecuación | Razón |
> |---------|----------|-------|
> | Resistor con temperatura | $v(t) = R_0(1 + \alpha T(t)) \cdot i(t)$ | $R(t)$ depende de $t$ |
> | Amortiguador desgastado | $m\ddot{x} + c(t)\dot{x} + kx = F(t)$ | $c(t)$ varía con el tiempo |
> | Ganancia modulada | $y(t) = \sin(\omega_0 t) \cdot u(t)$ | Coeficiente $a_0(t) = \sin(\omega_0 t)$ |

> [!ejemplo] Verificación de violación de invarianza
> Dado $y(t) = t \cdot u(t)$:
> - Para $u_\tau(t) = u(t-\tau)$: $y_\tau(t) = t \cdot u(t-\tau)$
> - Respuesta esperada si fuera invariante: $y(t-\tau) = (t-\tau) \cdot u(t-\tau)$
> - Diferencia: $y_\tau(t) - y(t-\tau) = \tau \cdot u(t-\tau) \neq 0$ (excepto $\tau=0$)
> - Por lo tanto, el sistema es **variante** en el tiempo.

---

## Consecuencia en el Dominio de Laplace

> [!teoria] Imposibilidad de Función de Transferencia
> Para sistemas variantes en el tiempo, no existe una [[Función de Transferencia]] $G(s)$ tal que $Y(s) = G(s)U(s)$. En su lugar, se requiere una representación más compleja:
> $$
> Y(s) = \int_{c-j\infty}^{c+j\infty} H(s, \sigma) U(\sigma) d\sigma
> $$
> donde $H(s, \sigma)$ es el **núcleo de transferencia** (transformada bidimensional de la respuesta al impulso variante $h(t,\tau)$).

---

## La Clase LTI

> [!definicion] Sistemas LTI
> Un sistema pertenece a la clase **LTI** (Linear Time-Invariant) si y solo si satisface simultáneamente:
> 1. [[Linealidad]] (superposición + homogeneidad)
> 2. Invarianza temporal (desplazamiento de entrada $\Rightarrow$ desplazamiento de salida)

Esta combinación permite:
- Caracterización completa mediante respuesta al impulso $h(t)$
- Convolución: $y(t) = (u * h)(t) = \int_{-\infty}^{\infty} u(\tau) h(t-\tau) d\tau$
- Multiplicación en Laplace: $Y(s) = H(s) U(s)$

---

## La Importancia para el Control

**Diseño de controladores:** La invarianza temporal garantiza que un controlador diseñado en un instante funcionará idénticamente en cualquier otro. Los controladores PID, el lugar de las raíces y la respuesta en frecuencia presuponen sistemas LTI.

**Sistemas reales:** Todo sistema físico presenta cierto grado de variación temporal (envejecimiento, deriva térmica, desgaste mecánico). La validez del modelo invariante depende de que la escala temporal de las variaciones sea mucho mayor que la dinámica del sistema (aproximación cuasi-estacionaria).

**Limitación fundamental:** Para sistemas con variaciones rápidas (ej. canal de comunicaciones variante, control de cohetes con consumo de combustible), se requieren técnicas avanzadas: sistemas lineales variantes en el tiempo (LTV), control adaptativo o control gain-scheduling.