---
title: Estabilidad BIBO
tags:
  - control-clasico
  - estabilidad
  - criterios
draft: true
aliases:
  - BIBO Stability
  - Estabilidad Entrada Acotada Salida Acotada
  - Estabilidad Externa
---

# Estabilidad BIBO

> [!definicion] Definición Formal
> Un sistema [[Sistemas LTI]] es **BIBO estable** (Bounded Input Bounded Output) si **para toda** entrada $u(t)$ que satisface:
> $$
> |u(t)| \le M_u < \infty, \quad \forall t
> $$
> existe una constante $M_y < \infty$ (que puede depender de $M_u$ pero no de $t$) tal que la salida correspondiente satisface:
> $$
> |y(t)| \le M_y < \infty, \quad \forall t
> $$
> 
> La palabra clave es **para toda** entrada acotada. Si existe **alguna** entrada acotada que produzca salida no acotada, el sistema **no es BIBO estable**.

> [!warning] Sistemas Marginalmente Estables NO son BIBO estables
> Un sistema con polos simples en el eje imaginario (ej. $G(s) = 1/(s^2+1)$) tiene salida acotada para muchas entradas, pero **no para todas**:
> - Entrada $u(t) = \sin(\omega_0 t)$ (frecuencia de resonancia) produce salida $y(t) = \frac{t}{2\omega_0} \sin(\omega_0 t)$, que **crece linealmente**
> - Por lo tanto, el sistema **no es BIBO estable**

> [!definicion] BIBO Estable vs Marginalmente Estable
> | Tipo | Condición de polos | ¿BIBO estable? | Observación |
> |------|-------------------|----------------|--------------|
> | Estable | $\Re(p_i) < 0$ | **Sí** | Toda entrada acotada produce salida acotada |
> | Marginalmente estable | $\Re(p_i) \le 0$, polos eje imaginario simples | **No** | Existen entradas acotadas que producen salida no acotada (resonancia) |
> | Inestable | Algún $\Re(p_i) > 0$ o polos múltiples en eje imaginario | **No** | Salida crece exponencial o polinomialmente |

---

## Caracterización en el Dominio Temporal

> [!teorema] Condición de Estabilidad vía Respuesta al Impulso
> Un sistema [[Sistemas LTI]] causal es BIBO estable **si y solo si** su [[Respuesta al Impulso]] $h(t)$ es **absolutamente integrable**:
> $$
> \int_{0}^{\infty} |h(\tau)| \, d\tau < \infty
> $$

> [!demostracion]
> **($\Rightarrow$) Suficiencia:** Supóngase que $\int_0^\infty |h(\tau)| d\tau = C < \infty$ y que $|u(t)| \le M_u$. Entonces:
> $$
> |y(t)| = \left| \int_0^\infty h(\tau) u(t-\tau) d\tau \right| \le \int_0^\infty |h(\tau)| |u(t-\tau)| d\tau \le M_u \int_0^\infty |h(\tau)| d\tau = M_u C
> $$
> Por lo tanto $|y(t)| \le M_u C$, y el sistema es BIBO estable.
> 
> **($\Leftarrow$) Necesidad:** Si $\int_0^\infty |h(\tau)| d\tau$ diverge, puede construirse una entrada acotada (ej. $u(t) = \text{sign}(h(-t))$) que produce salida no acotada. $\square$

> [!ejemplo] Sistema BIBO estable
> $h(t) = e^{-at} \mathbf{1}(t)$ con $a > 0$:
> $$
> \int_0^\infty |e^{-at}| dt = \int_0^\infty e^{-at} dt = \frac{1}{a} < \infty
> $$
> → Sistema BIBO estable.

> [!ejemplo] Sistema marginalmente estable (NO BIBO estable)
> $h(t) = \sin(\omega_0 t) \mathbf{1}(t)$:
> $$
> \int_0^\infty |\sin(\omega_0 t)| dt = \infty
> $$
> → Sistema **NO** BIBO estable, aunque para entradas como escalón la salida sea acotada.

> [!ejemplo] Sistema inestable
> $h(t) = e^{at} \mathbf{1}(t)$ con $a > 0$:
> $$
> \int_0^\infty e^{at} dt = \infty
> $$
> → Sistema **NO** BIBO estable.


---

## Caracterización en el Dominio de Laplace

> [!teorema] Condición de Estabilidad vía Polos
> Un sistema [[Sistemas LTI]] causal con [[Función de Transferencia]] racional $G(s) = N(s)/D(s)$ es BIBO estable si y solo si **todos los polos** tienen parte real estrictamente negativa:
> $$
> \Re(p_i) < 0, \quad \forall i
> $$

> [!demostracion]
> La [[Respuesta al Impulso]] es $h(t) = \sum_{i} A_i e^{p_i t} \mathbf{1}(t)$ (para polos distintos). Entonces:
> $$
> \int_0^\infty |h(t)| dt \le \sum_i |A_i| \int_0^\infty |e^{p_i t}| dt = \sum_i |A_i| \int_0^\infty e^{\Re(p_i) t} dt
> $$
> 
> La integral $\int_0^\infty e^{\sigma t} dt$ converge si y solo si $\sigma < 0$. Si algún polo tiene $\Re(p_i) \ge 0$, la integral diverge. $\square$

> [!proposicion] Resumen de condiciones
> | Ubicación de polos | $\int_0^\infty \|h(t)\| dt$ | Estabilidad BIBO |
> |--------------------|------------------------------|------------------|
> | Todos $\Re(p_i) < 0$ | Converge | **Estable** |
> | Alguno $\Re(p_i) > 0$ | Diverge | **Inestable** |
> | Polos en eje imaginario (simples) | Diverge (oscilación) | **Marginalmente estable** |
> | Polos en eje imaginario (múltiples) | Diverge (crecimiento polinomial) | **Inestable** |

---

## Estabilidad Interna vs Estabilidad Externa

> [!definicion] Distinción Fundamental
> - **Estabilidad BIBO (externa):** Solo considera la relación entrada-salida. Un sistema puede ser BIBO estable incluso si tiene modos internos no observables o no controlables inestables.
> - **Estabilidad Interna (asintótica):** Requiere que todos los modos del sistema (incluyendo los no observables) tiendan a cero.

> [!ejemplo] Sistema con cancelación polo-cero
> Sea $G(s) = \dfrac{s-1}{(s-1)(s+2)} = \dfrac{1}{s+2}$:
> - La función de transferencia tiene un polo en $p = -2$ (estable)
> - Pero el sistema original tiene un polo en $p = +1$ cancelado por un cero
> - **BIBO estable:** Sí (entrada-salida)
> - **Internamente estable:** No (el modo inestable puede excitarse con condiciones iniciales o perturbaciones)

> [!warning]
> En control, **nunca se deben cancelar polos inestables**. Aunque la función de transferencia resultante sea estable, el sistema real tendrá modos internos inestables que pueden ser excitados.

---

## Sistemas Marginalmente Estables

> [!definicion] Marginalmente Estable
> Un sistema se denomina **marginalmente estable** (o críticamente estable) cuando:
> - Todos los polos tienen $\Re(p_i) \le 0$
> - Al menos un polo tiene $\Re(p_i) = 0$ (eje imaginario)
> - Los polos en el eje imaginario son **simples** (no múltiples)

> [!ejemplo] Polos simples en eje imaginario
> $G(s) = \dfrac{1}{s^2 + \omega_0^2}$:
> - Polos: $p = \pm j\omega_0$ (simples)
> - Respuesta al impulso: $h(t) = \frac{1}{\omega_0} \sin(\omega_0 t) \mathbf{1}(t)$ (oscila, no crece)
> - **Marginalmente estable**

> [!ejemplo] Polos múltiples en eje imaginario
> $G(s) = \dfrac{1}{(s^2 + \omega_0^2)^2}$:
> - Polos: $p = \pm j\omega_0$ (multiplicidad 2)
> - Respuesta al impulso: $h(t) = \frac{1}{2\omega_0^3} [\sin(\omega_0 t) - \omega_0 t \cos(\omega_0 t)] \mathbf{1}(t)$ (crece linealmente)
> - **Inestable**

---

## Criterios de Estabilidad sin Calcular Polos

> [!teoria] Métodos Alternativos
> Para sistemas de orden alto, calcular explícitamente los polos puede ser costoso. Existen criterios que determinan estabilidad sin calcular raíces:

| Criterio | Aplicación | Ventaja |
|----------|------------|---------|
| [[Criterio de Routh-Hurwitz]] | Sistemas continuos | Determina si hay polos en SPD sin factorizar |
| [[Criterio de Jury]] | Sistemas discretos | Versión discreta de Routh-Hurwitz |
| [[Criterio de Nyquist]] | Sistemas continuos | Usa respuesta en frecuencia |
| [[Lugar de las Raíces]] | Sistemas con parámetro variable | Muestra cómo se mueven los polos |

---

## Estabilidad en Sistemas Discretos

> [!definicion] Caso Discreto
> Para sistemas discretos LTI, la condición de estabilidad BIBO es:
> $$
> \sum_{n=0}^{\infty} |h[n]| < \infty
> $$
> 
> En términos de polos de $H(z) = \mathcal{Z}\{h[n]\}$:
> - **Estable:** Todos los polos dentro del círculo unitario ($|p_i| < 1$)
> - **Marginalmente estable:** Polos en $|p_i| = 1$ (simples)
> - **Inestable:** Algún polo con $|p_i| > 1$ o polos múltiples en $|p_i| = 1$

```
Plano z:
    Im{z}
     ↑
   1 +   × (polo inestable)
     |
----+----+----→ Re{z}
   -1   0   1
     |
    -1
```

---

## Resumen de Condiciones

> [!teorema] Tabla Resumen
> | Sistema | Condición de estabilidad | Región de estabilidad |
> |---------|-------------------------|----------------------|
> | Continuo (Laplace) | $\Re(p_i) < 0$ | Semi-plano izquierdo |
> | Discreto (Z) | $\|p_i\| < 1$ | Círculo unitario |

> [!info]
> La estabilidad BIBO es un requisito mínimo para cualquier sistema de control real. Un sistema inestable no puede ser usado en lazo cerrado sin antes ser estabilizado.
