---
title: Sistemas Eléctricos (Circuitos Pasivos)
tags:
  - control-clasico
  - dominios-fisicos
  - modelado
draft: false
aliases:
  - electrico
  - circuitos pasivos
  - RLC
---

# Sistemas Eléctricos (Circuitos Pasivos)

# Elementos fundamentales

> [!definicion] Resistencia ($R$)
> Unidad: Ohm ($\Omega$)
> 
> **Ley de Ohm:** $V_R = R \cdot I$
> 
> **Operador en Laplace:** $\frac{V_R(s)}{I(s)} = R$ (algebraico)
> 
> **Interpretación:** Disipa energía. Relación instantánea entre voltaje y corriente.

> [!definicion] Inductancia ($L$)
> Unidad: Henry (H)
> 
> **Relación voltaje-corriente:** $V_L = L \frac{dI}{dt}$
> 
> **Operador en Laplace:** $\frac{V_L(s)}{I(s)} = L s$
> 
> **Interpretación:** **Derivador** (voltaje es derivada de corriente). También: $I(s) = \frac{1}{Ls} V_L(s)$ (integrador).

> [!definicion] Capacitancia ($C$)
> Unidad: Farad (F)
> 
> **Relación corriente-voltaje:** $I_C = C \frac{dV_C}{dt}$
> 
> **Operador en Laplace:** $\frac{V_C(s)}{I(s)} = \frac{1}{C s}$
> 
> **Interpretación:** **Integrador** (voltaje es integral de corriente). O $I(s) = C s V_C(s)$ (derivador según variable elegida).

# Elementos derivativos e integradores

> [!info] Análisis de operadores
> 
> | Elemento | Relación $V$ vs $I$ | Operador $Z(s) = V/I$ | Tipo |
> |----------|---------------------|----------------------|------|
> | Resistencia $R$ | $V = R I$ | $R$ | **Algebraico** |
> | Inductancia $L$ | $V = L s I$ | $L s$ | **Derivador** |
> | Capacitancia $C$ | $V = \frac{1}{C s} I$ | $\frac{1}{C s}$ | **Integrador** |
> 
> **Observación clave:**
> - **Inductor:** voltaje es derivada de corriente (polo en corriente, cero en voltaje)
> - **Capacitor:** voltaje es integral de corriente (polo en voltaje, cero en corriente)
> - **Resistencia:** relación algebraica (sin dinámica)

# Leyes fundamentales

> [!info] Leyes de Kirchhoff
> 
> **Ley de voltajes de Kirchhoff (LVK):** La suma de voltajes en una malla es cero.
> $$\sum V_k = 0$$
> 
> **Ley de corrientes de Kirchhoff (LCK):** La suma de corrientes en un nodo es cero.
> $$\sum I_k = 0$$

# Configuraciones básicas

## Caso 1: Circuito RC serie

> [!ejemplo] RC serie - voltaje en capacitor
> 
> ![[rc_serie.svg]]
> 
> **Entrada:** $V_i(s)$, **Salida:** $V_o(s)$ (en $C$)
> 
> **Malla:** $V_i(s) = V_R(s) + V_o(s) = R I(s) + V_o(s)$
> 
> **Relación $I$-$V_o$:** $I(s) = C s V_o(s)$ (capacitor)
> 
> **Sustituyendo:** $V_i(s) = R C s V_o(s) + V_o(s) = V_o(s) (R C s + 1)$
> 
> **Función transferencia:**
> $$G(s) = \frac{V_o(s)}{V_i(s)} = \frac{1}{RC s + 1}$$
> 
> **Observación:** Un polo en $s = -1/RC$ (primer orden, pasa bajos).

## Caso 2: Circuito RC serie - voltaje en resistencia

> [!ejemplo] RC serie - voltaje en resistencia
> 
> **Entrada:** $V_i(s)$, **Salida:** $V_R(s)$
> 
> $V_R(s) = R I(s) = R \cdot C s V_C(s)$
> 
> Pero $V_C(s) = V_i(s) - V_R(s)$, entonces:
> $$V_R(s) = RC s (V_i(s) - V_R(s))$$
> 
> $$V_R(s) (1 + RC s) = RC s V_i(s)$$
> 
> **Función transferencia:**
> $$G(s) = \frac{V_R(s)}{V_i(s)} = \frac{RC s}{RC s + 1}$$
> 
> **Observación:** Un cero en $s=0$ (derivador filtrado, pasa altos).

## Caso 3: Circuito RL serie

> [!ejemplo] RL serie - voltaje en inductor
> 
> ![[rl_serie.svg]]
> 
> **Entrada:** $V_i(s)$, **Salida:** $V_L(s)$ (en $L$)
> 
> **Malla:** $V_i(s) = V_R(s) + V_L(s) = R I(s) + V_L(s)$
> 
> **Relación $I$-$V_L$:** $V_L(s) = L s I(s) \implies I(s) = \frac{V_L(s)}{L s}$
> 
> **Sustituyendo:** $V_i(s) = R \cdot \frac{V_L(s)}{L s} + V_L(s) = V_L(s) \left( \frac{R}{L s} + 1 \right)$
> 
> **Función transferencia:**
> $$G(s) = \frac{V_L(s)}{V_i(s)} = \frac{L s}{R + L s} = \frac{s}{s + R/L}$$
> 
> **Observación:** Un polo en $s = -R/L$, un cero en $s=0$ (pasa altos).

## Caso 4: Circuito RL serie - voltaje en resistencia

> [!ejemplo] RL serie - voltaje en resistencia
> 
> **Entrada:** $V_i(s)$, **Salida:** $V_R(s)$
> 
> $V_R(s) = R I(s) = R \cdot \frac{V_L(s)}{L s}$
> 
> Pero $V_L(s) = V_i(s) - V_R(s)$, entonces:
> $$V_R(s) = \frac{R}{L s} (V_i(s) - V_R(s))$$
> 
> $$V_R(s) \left(1 + \frac{R}{L s}\right) = \frac{R}{L s} V_i(s)$$
> 
> $$V_R(s) \left(\frac{L s + R}{L s}\right) = \frac{R}{L s} V_i(s)$$
> 
> **Función transferencia:**
> $$G(s) = \frac{V_R(s)}{V_i(s)} = \frac{R}{R + L s} = \frac{R/L}{s + R/L}$$
> 
> **Observación:** Un polo en $s = -R/L$ (pasa bajos).

## Caso 5: Circuito RLC serie

> [!ejemplo] RLC serie - voltaje en capacitor
> 
> ![[rlc_serie.svg]]
> 
> **Entrada:** $V_i(s)$, **Salida:** $V_o(s)$ (en $C$)
> 
> **Malla:** $V_i(s) = V_R(s) + V_L(s) + V_o(s)$
> 
> $V_R(s) = R I(s)$, $V_L(s) = L s I(s)$, $I(s) = C s V_o(s)$
> 
> **Sustituyendo:**
> $$V_i(s) = R C s V_o(s) + L C s^2 V_o(s) + V_o(s) = V_o(s) (L C s^2 + R C s + 1)$$
> 
> **Función transferencia:**
> $$G(s) = \frac{V_o(s)}{V_i(s)} = \frac{1}{LC s^2 + RC s + 1} = \frac{1/LC}{s^2 + \frac{R}{L}s + \frac{1}{LC}}$$
> 
> **Parámetros característicos:**
> - $\omega_n = \frac{1}{\sqrt{LC}}$ (frecuencia natural)
> - $\zeta = \frac{R}{2}\sqrt{\frac{C}{L}}$ (razón de amortiguamiento)
> 
> **Observación:** Segundo orden. Según $\zeta$: subamortiguado ($\zeta < 1$), crítico ($\zeta = 1$), sobreamortiguado ($\zeta > 1$).

## Caso 6: Circuito RLC serie - voltaje en inductor

> [!ejemplo] RLC serie - voltaje en inductor
> 
> **Entrada:** $V_i(s)$, **Salida:** $V_L(s)$
> 
> $V_L(s) = L s I(s) = L s \cdot C s V_C(s) = LC s^2 V_C(s)$
> 
> Pero $V_C(s) = \frac{1}{LC s^2 + RC s + 1} V_i(s)$, entonces:
> $$G(s) = \frac{V_L(s)}{V_i(s)} = \frac{LC s^2}{LC s^2 + RC s + 1} = \frac{s^2}{s^2 + \frac{R}{L}s + \frac{1}{LC}}$$
> 
> **Observación:** Dos ceros en $s=0$ (doble derivador). Filtro pasa altos de segundo orden.

# Relaciones entrada-salida comunes

> [!info] Tabla de funciones transferencia para circuitos pasivos
> 
> | Circuito | Entrada | Salida | $G(s)$ | Tipo |
> |----------|---------|--------|--------|------|
> | RC serie | $V_i$ | $V_C$ | $\frac{1}{RC s + 1}$ | Pasa bajos 1er orden |
> | RC serie | $V_i$ | $V_R$ | $\frac{RC s}{RC s + 1}$ | Pasa altos 1er orden |
> | RL serie | $V_i$ | $V_R$ | $\frac{R/L}{s + R/L}$ | Pasa bajos 1er orden |
> | RL serie | $V_i$ | $V_L$ | $\frac{s}{s + R/L}$ | Pasa altos 1er orden |
> | RLC serie | $V_i$ | $V_C$ | $\frac{1/LC}{s^2 + \frac{R}{L}s + \frac{1}{LC}}$ | Pasa bajos 2do orden |
> | RLC serie | $V_i$ | $V_L$ | $\frac{s^2}{s^2 + \frac{R}{L}s + \frac{1}{LC}}$ | Pasa altos 2do orden |

# División de voltaje y corriente

> [!info] Reglas prácticas
> 
> **Divisor de voltaje (circuito serie):**
> $$V_k(s) = \frac{Z_k(s)}{Z_{\text{total}}(s)} V_{\text{total}}(s)$$
> 
> **Divisor de corriente (circuito paralelo):**
> $$I_k(s) = \frac{Z_{\text{total}}(s)}{Z_k(s)} I_{\text{total}}(s) \quad \text{(en admitancias)}$$

# Ejemplo: Divisor de voltaje RC

> [!ejemplo] Aplicación de regla de divisor
> 
> Circuito RC serie: $Z_R = R$, $Z_C = \frac{1}{Cs}$
> 
> $Z_{\text{total}} = R + \frac{1}{Cs} = \frac{RCs + 1}{Cs}$
> 
> **Salida en $C$:**
> $$V_C(s) = \frac{1/Cs}{(RCs+1)/Cs} V_i(s) = \frac{1}{RCs + 1} V_i(s)$$
> 
> **Salida en $R$:**
> $$V_R(s) = \frac{R}{(RCs+1)/Cs} V_i(s) = \frac{RCs}{RCs + 1} V_i(s)$$

# Analogía con sistemas mecánicos

> [!info] Analogía fuerza-voltaje
> 
> | Eléctrico | Mecánico (traslacional) |
> |-----------|-------------------------|
> | Voltaje $V$ | Fuerza $F$ |
> | Corriente $I$ | Velocidad $v$ |
> | Resistencia $R$ | Amortiguador $b$ |
> | Inductancia $L$ | Masa $m$ |
> | Capacitancia $C$ | Cumplianza $1/k$ (inverso del resorte) |
> 
> Ver [[Mecanico Traslacional]].

# Limitaciones

> [!warning]
> 1. **Circuitos pasivos lineales:** Solo combina $R$, $L$, $C$. No incluye fuentes controladas, amplificadores operacionales, transistores, etc.
> 2. **Componentes ideales:** $R$, $L$, $C$ son constantes, sin tolerancias ni efectos parásitos.
> 3. **Rango de frecuencias:** A altas frecuencias, inductores y capacitores tienen comportamientos no ideales.
> 4. **Condiciones iniciales:** Las funciones transferencia asumen CI nulas.