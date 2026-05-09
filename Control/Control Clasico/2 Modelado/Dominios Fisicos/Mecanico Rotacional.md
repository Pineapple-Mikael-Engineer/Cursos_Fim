---
title: Sistemas Mecánicos Rotacionales
tags:
  - control-clasico
  - dominios-fisicos
  - modelado
draft: false
aliases:
  - rotacional
  - inercia
  - torsional
  - ejes
  - engranajes
---

# Sistemas Mecánicos Rotacionales

# Elementos fundamentales

> [!definicion] Inercia / Momento de inercia ($J$)
> Unidad: kg·m²
> 
> Relación torque-velocidad angular: $\tau = J \frac{d\omega}{dt} = J \ddot{\theta}$
> 
> **Operador en Laplace:** $\frac{\Theta}{\tau} = \frac{1}{Js^2}$ (doble integrador)
> 
> **Interpretación:** Torque causa aceleración. Dos integradores: aceleración → velocidad → posición.

> [!definicion] Resorte torsional ($k$)
> Unidad: N·m/rad
> 
> Relación torque-posición angular: $\tau = k (\theta_1 - \theta_2)$
> 
> **Operador en Laplace:** $\frac{\theta_1 - \theta_2}{\tau} = \frac{1}{k}$ (algebraico)
> 
> **Interpretación:** El torque depende de la **diferencia de ángulos** entre dos extremos.

> [!definicion] Amortiguador rotacional ($b$)
> Unidad: N·m·s/rad
> 
> Relación torque-velocidad angular: $\tau = b (\omega_1 - \omega_2) = b(\dot{\theta}_1 - \dot{\theta}_2)$
> 
> **Operador en Laplace:** $\frac{\theta_1 - \theta_2}{\tau} = \frac{1}{bs}$ (integrador)
> 
> **Interpretación:** Disipa energía proporcional a diferencia de velocidades.

> [!definicion] Eje rígido (conexión directa)
> Relación cinemática: $\theta_1 = \theta_2$, $\omega_1 = \omega_2$
> 
> **Operador:** $\frac{\Theta_2}{\Theta_1} = 1$ (ganancia unitaria)
> 
> **Torque:** $\tau_1 = -\tau_2$ (acción y reacción)

# Leyes fundamentales

> [!info] Segunda ley de Newton rotacional (para cada inercia)
> $$\sum \tau = J \ddot{\theta}$$
> 
> Los torques que actúan sobre una inercia incluyen:
> - Torques aplicados externamente
> - Torques de resortes torsionales ($k(\theta_j - \theta_i)$)
> - Torques de amortiguadores ($b(\omega_j - \omega_i)$)
> - Torques de reacción de ejes conectados

# Configuraciones fundamentales

## Caso 1: Inercia con entrada y salida de torque

> [!ejemplo] Eje con torque aplicado y torque de carga
> 
> ![[eje_torques.svg]]
> 
> **Sistema:** Inercia $J$ con torque de entrada $\tau_{\text{in}}$ aplicado por un motor, y torque de carga $\tau_{\text{carga}}$ aplicado por una carga (ej. herramienta, ventilador).
> 
> **Ecuación:**
> $$\tau_{\text{in}} - \tau_{\text{carga}} = J \ddot{\theta}$$
> 
> **Transferencia (si $\tau_{\text{carga}} = 0$):**
> $$G(s) = \frac{\Theta(s)}{\tau_{\text{in}}(s)} = \frac{1}{Js^2}$$
> 
> **Caso con carga resistiva ($\tau_{\text{carga}} = b\omega$):**
> $$\tau_{\text{in}} - b\dot{\theta} = J\ddot{\theta}$$
> $$G(s) = \frac{\Theta(s)}{\tau_{\text{in}}(s)} = \frac{1}{s(Js + b)}$$

## Caso 2: Dos inercias conectadas por eje rígido (comparten torque)

> [!ejemplo] Eje común, múltiples inercias
> 
> ![[ejes_compartidos.svg]]
> 
> **Configuración:** Dos inercias $J_1$ y $J_2$ montadas sobre el **mismo eje rígido**.
> 
> **Cinemática:** $\theta_1 = \theta_2 = \theta$ (giran juntas)
> 
> **Torques:** $\tau_1$ sobre $J_1$, $\tau_2$ sobre $J_2$
> 
> **Ecuación de Newton para el sistema combinado:**
> $$\tau_1 + \tau_2 = (J_1 + J_2) \ddot{\theta}$$
> 
> **Inercia equivalente:** $J_{\text{eq}} = J_1 + J_2$
> 
> **Función transferencia (posición):**
> $$G(s) = \frac{\Theta(s)}{\tau_1(s) + \tau_2(s)} = \frac{1}{(J_1+J_2)s^2}$$
> 
> **Caso especial:** Si $\tau_2 = 0$ y solo $\tau_1$ actúa:
> $$G(s) = \frac{1}{(J_1+J_2)s^2}$$
> 
> **Observación:** Las inercias se **suman** cuando comparten el mismo eje y velocidad.

## Caso 3: Dos inercias conectadas por resorte torsional (eje flexible)

> [!ejemplo] Eje elástico (transmisión flexible)
> 
> ![[eje_flexible.svg]]
> 
> **Sistema:** Inercia $J_1$ (motor) conectada a inercia $J_2$ (carga) mediante resorte torsional $k$ (eje con rigidez finita).
> 
> **Variables:** $\theta_1$ (ángulo del motor), $\theta_2$ (ángulo de la carga)
> 
> **Torque en el eje:** $\tau_{\text{eje}} = k(\theta_1 - \theta_2)$ (se opone a la diferencia angular)
> 
> **Ecuaciones:**
> 
> Para $J_1$: $\tau_{\text{motor}} - k(\theta_1 - \theta_2) = J_1 \ddot{\theta}_1$
> 
> Para $J_2$: $k(\theta_1 - \theta_2) - \tau_{\text{carga}} = J_2 \ddot{\theta}_2$
> 
> **Función transferencia (sin carga, $\tau_{\text{carga}}=0$, de $\tau_{\text{motor}}$ a $\theta_2$):**
> 
> En Laplace (CI nulas):
> $$(J_1 s^2 + k) \Theta_1(s) - k \Theta_2(s) = \tau_{\text{motor}}(s)$$
> $$-k \Theta_1(s) + (J_2 s^2 + k) \Theta_2(s) = 0$$
> 
> Resolviendo:
> $$G(s) = \frac{\Theta_2(s)}{\tau_{\text{motor}}(s)} = \frac{k}{J_1 J_2 s^4 + (J_1 + J_2)k s^2}$$
> 
> O equivalentemente:
> $$G(s) = \frac{k/J_1}{s^2 \left(s^2 + \frac{J_1+J_2}{J_1 J_2}k \right)}$$
> 
> **Observación:** Dos polos en $s=0$ (modo rígido) + un par de polos complejos (modo elástico).

## Caso 4: Transmisión con engranajes (relación de ángulos fija)

> [!ejemplo] Engranajes ideales (sin elasticidad)
> 
> ![[engranajes.svg]]
> 
> **Relación cinemática:** $\frac{\theta_2}{\theta_1} = \frac{N_1}{N_2} = n$, donde $N_1, N_2$ son números de dientes.
> 
> **Relación de torques (conservación de potencia, engranajes ideales):**
> $$\tau_2 \cdot \theta_2 = \tau_1 \cdot \theta_1 \implies \tau_2 = \frac{\theta_1}{\theta_2} \tau_1 = \frac{1}{n} \tau_1$$
> 
> **Reflexión de inercias:**
> 
> La inercia $J_2$ vista desde el eje 1 es: $J_{2,\text{ref}} = n^2 J_2$
> 
> **Inercia total equivalente vista desde el eje 1:**
> $$J_{\text{eq}} = J_1 + n^2 J_2$$
> 
> **Sistema equivalente:**
> $$J_{\text{eq}} \ddot{\theta}_1 = \tau_1$$
> 
> **Si hay resorte o amortiguador en el eje 2, también se reflejan:**
> $$k_{\text{eq}} = n^2 k_2, \quad b_{\text{eq}} = n^2 b_2$$
> 
> **Caso de engranajes con inercias a ambos lados:**
> $$G(s) = \frac{\Theta_2(s)}{\tau_1(s)} = \frac{n}{J_{\text{eq}} s^2}$$


## Caso 5: Tren de engranajes con múltiples etapas

> [!ejemplo] Reductor de velocidad de varias etapas
> 
> ![[tren_engranajes.svg]]
> 
> **Relación total:** $n_{\text{total}} = n_1 \cdot n_2 \cdot n_3 \dots$
> 
> **Inercia total reflejada al eje de entrada:**
> $$J_{\text{eq}} = J_1 + n_1^2 J_2 + (n_1 n_2)^2 J_3 + \dots$$
> 
> **Torque de carga reflejado:**
> $$\tau_{\text{carga,ref}} = n_{\text{total}} \cdot \tau_{\text{carga}}$$
> 
> **Sistema equivalente:**
> $$J_{\text{eq}} \ddot{\theta}_{\text{in}} + b_{\text{eq}} \dot{\theta}_{\text{in}} + k_{\text{eq}} \theta_{\text{in}} = \tau_{\text{in}} - \tau_{\text{carga,ref}}$$

# Elementos derivativos e integradores (resumen)

> [!info] Análisis de operadores por configuración
> 
> | Configuración | Función transferencia $\Theta_{\text{sal}} / \tau_{\text{ent}}$ | Polos en $s=0$ | Tipo |
> |---------------|---------------------------------------------------------------|----------------|------|
> | Inercia sola | $\frac{1}{Js^2}$ | 2 | Doble integrador |
> | Inercia + amortiguador (velocidad) | $\frac{1}{Js+b}$ | 0 | Polo real |
> | Inercia + amortiguador (posición) | $\frac{1}{s(Js+b)}$ | 1 | Integrador |
> | Dos inercias mismo eje | $\frac{1}{(J_1+J_2)s^2}$ | 2 | Doble integrador |
> | Eje flexible (posición carga) | $\frac{k/J_1}{s^2(s^2 + \frac{J_1+J_2}{J_1J_2}k)}$ | 2 | Doble integrador + modo elástico |
> | Engranajes ideales | $\frac{n}{J_{\text{eq}}s^2}$ | 2 | Doble integrador con ganancia |
> | Diferencial (ángulo out / in) | $\frac{1}{2}$ | 0 | Algebraico |


# Limitaciones

> [!warning]
> 1. **Ejes rígidos:** Asumen deformación nula (para alta rigidez se puede despreciar)
> 2. **Engranajes ideales:** Sin juego, sin fricción, sin elasticidad
> 3. **Resorte lineal:** $k$ constante solo para pequeñas deformaciones
> 4. **Amortiguador lineal:** $b$ constante solo para bajas velocidades
> 5. **Diferencial ideal:** Sin inercias internas ni pérdidas