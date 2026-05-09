---
title: Sistemas de Segundo Orden
tags:
  - control-clasico
  - analisis
  - respuesta-temporal
draft: false
aliases:
  - segundo orden
  - 2do orden
  - respuesta segundo orden
---

# Sistemas de Segundo Orden

# Definición

> [!definicion] Función transferencia estándar (tiempo continuo)
> $$G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$$
> 
> donde:
> - $\omega_n$: **frecuencia natural no amortiguada** [rad/s]
> - $\zeta$: **razón de amortiguamiento** (adimensional)

> [!definicion] Forma general con ganancia
> $$G(s) = \frac{K\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$$
> 
> Normalmente se trabaja con $K=1$ para análisis de respuesta temporal, y se agrega la ganancia al final por linealidad.

# Polos del sistema

> [!teorema] Polos de lazo cerrado
> $$s_{1,2} = -\zeta\omega_n \pm \omega_n\sqrt{\zeta^2 - 1}$$

> [!info] Clasificación según $\zeta$
> | $\zeta$ | Tipo de polos | Respuesta |
> |---------|---------------|-----------|
> | $\zeta = 0$ | Imaginarios puros ($\pm j\omega_n$) | No amortiguada (oscila) |
> | $0 < \zeta < 1$ | Complejos conjugados | Subamortiguada |
> | $\zeta = 1$ | Reales iguales ($s = -\omega_n$) | Críticamente amortiguada |
> | $\zeta > 1$ | Reales distintos y negativos | Sobreamortiguada |

# Parámetros de respuesta (subamortiguada, $0 < \zeta < 1$)

> [!definicion] Frecuencia amortiguada
> $$\omega_d = \omega_n \sqrt{1 - \zeta^2}$$

> [!definicion] Sobrepico máximo ($M_p$)
> $$M_p = e^{-\pi\zeta/\sqrt{1-\zeta^2}} \quad \text{(en por unidad)}$$
> 
> En porcentaje: $M_p(\%) = 100 \cdot e^{-\pi\zeta/\sqrt{1-\zeta^2}}$
> 
> Ver [[Sobrepico Mp]] para:
> - Cálculo detallado
> - Relación inversa $\zeta$ a partir de $M_p$
> - Curva $M_p$ vs $\zeta$

> [!definicion] Tiempo de pico ($T_p$)
> $$T_p = \frac{\pi}{\omega_d} = \frac{\pi}{\omega_n\sqrt{1-\zeta^2}}$$
> 
> Ver [[Tiempo Pico Tp]] para:
> - Demostración por derivación de $y(t)$
> - Relación con $\omega_d$

> [!definicion] Tiempo de establecimiento ($T_s$)
> $$T_s(2\%) \approx \frac{4}{\zeta\omega_n}$$
> $$T_s(5\%) \approx \frac{3}{\zeta\omega_n}$$
> 
> Ver [[Tiempo Establecimiento Ts]] para:
> - Demostración de la envolvente $1 \pm e^{-\zeta\omega_n t}/\sqrt{1-\zeta^2}$
> - Criterios porcentuales

> [!definicion] Tiempo de subida ($T_r$)
> Aproximaciones:
> $$T_r \approx \frac{1.8}{\omega_n} \quad \text{(para } \zeta \approx 0.5\text{)}$$
> $$T_r \approx \frac{1 + 0.7\zeta}{\omega_n} \quad \text{(fórmula empírica)}$$
> 
> Ver [[Tiempo Subida Tr]] para:
> - Definición exacta (10% → 90%)
> - Cálculo numérico
> - Validación de aproximaciones

# Respuesta a escalón

> [!teorema] Salida para escalón unitario ($0 < \zeta < 1$)
> $$y(t) = 1 - \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}} \sin(\omega_d t + \theta)$$
> 
> donde $\theta = \arccos(\zeta) = \arctan\left(\frac{\sqrt{1-\zeta^2}}{\zeta}\right)$

> [!ejemplo] Curva característica
> 
> ![[segundo_orden_escalon.svg]]

# Relación con polos dominantes

> [!info] Orden superior
> Los sistemas de orden superior pueden aproximarse como segundo orden si tienen un [[Polos Ceros | par de polos complejos dominantes]].
> 
> Condición: Otros polos tienen parte real al menos 5 veces más negativa que la parte real del par dominante.

# Uso en diseño

> [!info] Especificaciones de diseño
> Dadas las especificaciones de respuesta temporal:
> - $M_p \to \zeta$
> - $T_s \to \zeta\omega_n$
> - $T_p \to \omega_n$
> 
> Se puede determinar $\zeta$ y $\omega_n$ y ubicar los polos deseados:
> $$s_{1,2} = -\zeta\omega_n \pm j\omega_n\sqrt{1-\zeta^2}$$
> 
> Luego, diseñar controladores para ubicar los polos en esas posiciones (ver [[Lugar Raices/index | lugar de las raíces]]).

# Limitaciones

> [!warning]
> 1. Las fórmulas asumen un sistema **subamortiguado** ($0 < \zeta < 1$)
> 2. Para $\zeta \ge 1$, la respuesta no tiene sobrepico y las fórmulas de $M_p$, $T_p$ no aplican
> 3. Las aproximaciones de $T_r$ tienen error para $\zeta$ muy bajo o muy alto
> 4. En presencia de ceros, la respuesta puede diferir significativamente (ver [[Polos Ceros| efecto de ceros]])