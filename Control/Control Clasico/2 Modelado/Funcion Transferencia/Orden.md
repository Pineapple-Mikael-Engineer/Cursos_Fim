---
title: Orden del Sistema
tags:
  - control-clasico
  - teoria
  - modelado
draft: false
aliases:
  - orden
  - grado del sistema
---

# Orden del Sistema

# Definición

> [!definicion] Orden
> Es el grado del polinomio denominador de $G(s)$ **después de cancelar** todos los factores comunes con el numerador.
> 
> $$G(s) = \frac{N(s)}{D(s)} \implies \text{orden} = \deg(D(s)) \text{ tras cancelación}$$

> [!ejemplo] Cancelación reduce orden
> $$G(s) = \frac{(s+1)}{(s+1)(s+2)(s+3)} = \frac{1}{(s+2)(s+3)}$$
> - Denominador original: grado 3
> - Tras cancelar $(s+1)$: grado 2
> - **Orden = 2**

> [!ejemplo] Sistema de primer orden
> $$G(s) = \frac{K}{\tau s + 1}$$
> Orden = 1

> [!ejemplo] Sistema de segundo orden
> $$G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$$
> Orden = 2

# Por qué importa el orden

> [!info] Dinámica
> El orden determina el **número de condiciones iniciales** necesarias y el **número de polos** del sistema.
> 
> - Orden 1: un polo, un modo ($e^{-t/\tau}$)
> - Orden 2: dos polos (pueden ser reales o complejos)
> - Orden $n$: $n$ polos, $n$ modos naturales

> [!info] Respuesta temporal
> | Orden | Característica |
> |-------|----------------|
> | 1 | Monótona, sin sobrepico |
> | 2 | Puede tener sobrepico (si $\zeta < 1$) |
> | $\ge 3$ | Puede tener comportamientos complejos, pero suele dominarse por [[Polos Ceros|polos dominantes]] |

# Polos dominantes y reducción de orden

> [!regla] Aproximación por polos dominantes
> Si hay polos con parte real mucho más negativa que otros ($|\Re(p_{\text{rápido}})| \ge 5 \times |\Re(p_{\text{lento}})|$), los rápidos decaen rápido y pueden despreciarse.
> 
> El sistema de orden $n$ se aproxima por uno de orden menor (1 o 2).

> [!ejemplo] Tercer orden a primer orden
> $$G(s) = \frac{10}{(s+1)(s+10)(s+20)}$$
> Polos: $-1$ (lento), $-10$, $-20$ (rápidos)
> 
> Aproximación:
> $$G(s) \approx \frac{10}{(1)(s+1)(10)(20)} = \frac{0.05}{s+1}$$
> 
> Ver [[Polos Ceros]].

> [!ejemplo] Tercer orden a segundo orden
> $$G(s) = \frac{100}{(s^2 + 2s + 100)(s+20)}$$
> Polos complejos: $-1 \pm j9.95$ ($\zeta=0.1$, $\omega_n=10$)
> Polo real: $-20$ (rápido, $|\Re| = 20$)
> 
> Aproximación:
> $$G(s) \approx \frac{100/20}{(s^2 + 2s + 100)} = \frac{5}{s^2 + 2s + 100}$$

# Sistemas de orden superior

> [!info] Comportamiento típico
> - Si hay un par complejo dominante → comportamiento similar a segundo orden
> - Si hay un polo real dominante → comportamiento similar a primer orden
> - Si hay polos múltiples dominantes → respuesta más lenta (factor $t^{r-1}$)

> [!warning] Cuidado con cancelaciones
> Reducir orden por cancelación polo-cero es válido **solo en la función transferencia**. El sistema interno puede tener modos no observables o no controlables.
> 
> Ver [[Polos Ceros]] y [[Espacio Estados]].

# Ejemplo completo

> [!ejemplo] Sistema masa-resorte-amortiguador con dinámica del actuador
> $$G(s) = \frac{1}{(ms^2 + bs + k)(\tau s + 1)}$$
> - Orden original: 3
> - Si $\tau$ es pequeño (actuador rápido), polo en $s = -1/\tau$ es rápido
> - Se aproxima como sistema de segundo orden:
> $$G(s) \approx \frac{1}{ms^2 + bs + k} \cdot \frac{1}{1} \quad \text{(ganancia DC del actuador = 1)}$$

# Relación con espacio de estados

> [!info] Orden = dimensión del estado
> En [[Espacio Estados]], el orden del sistema es la **dimensión del vector de estado** $x \in \mathbb{R}^n$.
> 
> La función transferencia $G(s) = C(sI-A)^{-1}B + D$ tendrá denominador de grado $\le n$, pero cancelaciones pueden reducir el orden aparente.