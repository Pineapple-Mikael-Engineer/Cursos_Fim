---
title: Sistemas Mecánicos Traslacionales
tags:
  - control-clasico
  - dominios-fisicos
  - modelado
draft: false
aliases:
  - mecanico traslacional
  - masa-resorte-amortiguador
  - traslacional
---

# Sistemas Mecánicos Traslacionales

# Elementos fundamentales

> [!definicion] Masa ($m$)
> Unidad: kg
> 
> Relación fuerza-velocidad: $F = m \frac{dv}{dt} = m \ddot{x}$
> 
> Relación fuerza-posición: $F = m \ddot{x}$

> [!definicion] Resorte ($k$)
> Unidad: N/m
> 
> Relación fuerza-posición: $F = k x$ (lineal)
> 
> Relación fuerza-velocidad: $F = k \int v \, dt$

> [!definicion] Amortiguador ($b$)
> Unidad: N·s/m
> 
> Relación fuerza-velocidad: $F = b v = b \dot{x}$
> 
> (También se denota como $c$ o $B$)

# Leyes fundamentales

> [!info] Segunda ley de Newton
> $$\sum F = m \ddot{x}$$
> 
> La suma de todas las fuerzas actuantes sobre una masa es igual a masa × aceleración.

> [!info] Convención de signos
> ![[mecanico_traslacional_convencion.svg|400]]
> 
> Se define una coordenada $x$ para cada masa, con dirección positiva arbitraria. Las fuerzas se escriben consistentes con esa dirección.

# Modelado paso a paso

> [!ejemplo] Masa-resorte-amortiguador (simple)
> 
> ![[mra_simple.svg|500]]
> 
> **Sistema:** Masa $m$ conectada a pared fija por resorte $k$ y amortiguador $b$.
> 
> **Entrada:** fuerza externa $F(t)$ aplicada a la masa.
> 
> **Salida:** posición $x(t)$ de la masa.
> 
> **Paso 1:** Diagrama de cuerpo libre.
> 
> **Paso 2:** Suma de fuerzas:
> $$\sum F = F(t) - F_k - F_b = m\ddot{x}$$
> 
> **Paso 3:** Relaciones constitutivas:
> $$F_k = k x, \quad F_b = b \dot{x}$$
> 
> **Paso 4:** Ecuación diferencial:
> $$m\ddot{x} + b\dot{x} + kx = F(t)$$
> 
> **Paso 5:** Función transferencia (CI nulas):
> $$G(s) = \frac{X(s)}{F(s)} = \frac{1}{ms^2 + bs + k}$$

> [!ejemplo] Dos masas acopladas
> 
> ![[mra_doble.svg|600]]
> 
> **Sistema:** Masas $m_1$ y $m_2$ conectadas por resorte $k_1$ y amortiguador $b$. $m_1$ conectada a pared por $k_2$.
> 
> **Entrada:** $F_1(t)$ sobre $m_1$, $F_2(t)$ sobre $m_2$.
> 
> **Salidas:** $x_1(t)$, $x_2(t)$.
> 
> **Paso 1:** DCL para $m_1$:
> 
> Fuerzas: $F_1(t)$ (entrada), $-k_2 x_1$ (resorte izquierdo), $-k_1(x_1 - x_2)$ (resorte central), $-b(\dot{x}_1 - \dot{x}_2)$ (amortiguador).
> 
> $$\sum F_{m_1} = F_1 - k_2 x_1 - k_1(x_1 - x_2) - b(\dot{x}_1 - \dot{x}_2) = m_1 \ddot{x}_1$$
> 
> **Paso 2:** DCL para $m_2$:
> 
> Fuerzas: $F_2(t)$ (entrada), $-k_1(x_2 - x_1)$ (resorte central), $-b(\dot{x}_2 - \dot{x}_1)$ (amortiguador).
> 
> $$\sum F_{m_2} = F_2 - k_1(x_2 - x_1) - b(\dot{x}_2 - \dot{x}_1) = m_2 \ddot{x}_2$$
> 
> **Paso 3:** Ecuaciones diferenciales:
> $$m_1 \ddot{x}_1 + b\dot{x}_1 - b\dot{x}_2 + (k_1 + k_2)x_1 - k_1 x_2 = F_1$$
> $$m_2 \ddot{x}_2 - b\dot{x}_1 + b\dot{x}_2 - k_1 x_1 + k_1 x_2 = F_2$$

# Analogía con circuitos eléctricos

> [!info] Tabla de analogías (fuerza-voltaje)
> | Mecánico | Eléctrico |
> |----------|-----------|
> | Fuerza $F$ | Voltaje $V$ |
> | Velocidad $v$ | Corriente $i$ |
> | Masa $m$ | Inductancia $L$ |
> | Resorte $1/k$ (cumplianza) | Capacitancia $C$ |
> | Amortiguador $b$ | Resistencia $R$ |
> 
> Ver [[Electrico]] para profundizar.

# Función transferencia y parámetros

> [!info] Parámetros característicos
> Para el sistema masa-resorte-amortiguador:
> $$G(s) = \frac{1/m}{s^2 + \frac{b}{m}s + \frac{k}{m}}$$
> 
> - $\omega_n = \sqrt{\frac{k}{m}}$ (frecuencia natural)
> - $\zeta = \frac{b}{2\sqrt{km}}$ (razón de amortiguamiento)
> 
> Ver [[Respuesta Temporal/Segundo Orden]].

# Limitaciones del modelo lineal

> [!warning]
> 1. **Resorte lineal:** $F = kx$ solo válido para pequeñas deformaciones
> 2. **Amortiguador lineal:** $F = bv$ solo válido para velocidades bajas (flujo laminar)
> 3. **Rozamiento seco (Coulomb):** no lineal, no incluido en este modelo
> 4. **Masas rígidas:** se asume que la masa es un cuerpo rígido (sin deformación interna)