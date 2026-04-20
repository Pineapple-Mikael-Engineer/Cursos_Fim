---
title: Circuitos Pasivos
tags:
  - control-clasico
  - modelado
  - circuitos-electricos
  - input-output
draft: true
aliases:
  - Redes Pasivas
  - Circuitos RLC
---


# Circuitos Pasivos

> [!definicion] Circuito Pasivo como Sistema
> Un **circuito pasivo** es una red compuesta exclusivamente por resistencias ($R$), capacitores ($C$) e inductores ($L$). Desde la perspectiva de [[Control Clasico/index|control clásico]], se modela como un sistema donde una **entrada** $V_{in}(s)$ es procesada para producir una **salida** $V_{out}(s)$.

El objetivo es obtener la [[Control Clasico/Función de Transferencia/index|función de transferencia]]:
$$G(s) = \frac{V_{out}(s)}{V_{in}(s)}$$

---

## Impedancias en el Dominio $s$

> [!teoria] Transformación al Dominio de Laplace
> Aplicando la [[Transformada de Laplace]] con condiciones iniciales cero, cada componente se representa por su **impedancia compleja** $Z(s)$:

| Componente | Relación $v$-$i$ (tiempo) | Impedancia $Z(s) = V(s)/I(s)$ |
| :---: | :---: | :---: |
| $R$ | $v = R \cdot i$ | $Z_R = R$ |
| $C$ | $i = C \frac{dv}{dt}$ | $Z_C = \frac{1}{Cs}$ |
| $L$ | $v = L \frac{di}{dt}$ | $Z_L = Ls$ |

---

## Circuito RC (Pasa-Bajos)

> [!ejemplo] Topología RC con Salida en el Capacitor
> **Estructura:** Fuente $V_{in}$ en serie con $R$ y $C$. La salida $V_{out}$ se mide en los terminales del capacitor.

![[circuito_rc_pasabajos.png|Esquema del circuito RC serie con salida en el capacitor]]
*Esquema TikZ: Fuente $V_{in}(s)$ conectada en serie a resistencia $R$, luego a capacitor $C$ conectado a tierra. La salida $V_{out}(s)$ se toma en paralelo con el capacitor.*

> [!teoria] Función de Transferencia
> Por divisor de voltaje en el dominio $s$:
> 
> $$V_{out}(s) = V_{in}(s) \cdot \frac{Z_C}{Z_R + Z_C} = V_{in}(s) \cdot \frac{\frac{1}{Cs}}{R + \frac{1}{Cs}}$$
> 
> Multiplicando numerador y denominador por $Cs$:
> 
> $$G(s) = \frac{V_{out}(s)}{V_{in}(s)} = \frac{1}{RCs + 1}$$

> [!info] Interpretación
> - **Orden:** 1 (un solo elemento almacenador de energía, $C$).
> - **Ganancia DC:** $G(0) = 1$ (el capacitor se comporta como circuito abierto en estado estable).
> - **Polo:** $s = -\frac{1}{RC}$.

---

## Circuito CR (Pasa-Altos)

> [!ejemplo] Topología RC con Salida en la Resistencia
> **Estructura:** Fuente $V_{in}$ en serie con $C$ y $R$. La salida $V_{out}$ se mide en los terminales de la resistencia.

![[circuito_cr_pasaaltos.png|Esquema del circuito CR serie con salida en la resistencia]]
*Esquema TikZ: Fuente $V_{in}(s)$ conectada en serie a capacitor $C$, luego a resistencia $R$ conectada a tierra. La salida $V_{out}(s)$ se toma en paralelo con la resistencia.*

> [!teoria] Función de Transferencia
> Por divisor de voltaje en el dominio $s$:
> 
> $$V_{out}(s) = V_{in}(s) \cdot \frac{Z_R}{Z_C + Z_R} = V_{in}(s) \cdot \frac{R}{\frac{1}{Cs} + R}$$
> 
> Multiplicando numerador y denominador por $Cs$:
> 
> $$G(s) = \frac{V_{out}(s)}{V_{in}(s)} = \frac{RCs}{RCs + 1}$$

> [!info] Interpretación
> - **Orden:** 1.
> - **Ganancia DC:** $G(0) = 0$ (bloquea señales constantes).
> - **Cero en el origen:** $s = 0$.
> - **Polo:** $s = -\frac{1}{RC}$.

---

## Circuito RLC Serie

> [!ejemplo] Topología RLC con Salida en el Capacitor
> **Estructura:** Fuente $V_{in}$ en serie con $R$, $L$ y $C$. La salida $V_{out}$ se mide en el capacitor.

![[circuito_rlc_serie.png|Esquema del circuito RLC serie con salida en el capacitor]]
*Esquema TikZ: Fuente $V_{in}(s)$ conectada en serie a resistencia $R$, inductor $L$ y capacitor $C$ conectado a tierra. La salida $V_{out}(s)$ se toma en paralelo con el capacitor.*

> [!teoria] Función de Transferencia
> Aplicando divisor de voltaje:
> 
> $$G(s) = \frac{Z_C}{Z_R + Z_L + Z_C} = \frac{\frac{1}{Cs}}{R + Ls + \frac{1}{Cs}}$$
> 
> Multiplicando numerador y denominador por $Cs$:
> 
> $$G(s) = \frac{1}{LCs^2 + RCs + 1}$$

> [!info] Interpretación
> - **Orden:** 2 (dos elementos almacenadores, $L$ y $C$).
> - Forma estándar: $G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$
>   - $\omega_n = \frac{1}{\sqrt{LC}}$ (frecuencia natural)
>   - $\zeta = \frac{R}{2}\sqrt{\frac{C}{L}}$ (factor de amortiguamiento)

---

## Circuito RLC con Salida en la Resistencia

> [!ejemplo] Topología RLC con Salida en $R$
> **Estructura:** Fuente $V_{in}$ en serie con $L$, $C$ y $R$. La salida $V_{out}$ se mide en la resistencia.

![[circuito_rlc_salida_r.png|Esquema del circuito RLC serie con salida en la resistencia]]
*Esquema TikZ: Fuente $V_{in}(s)$ conectada en serie a inductor $L$, capacitor $C$ y resistencia $R$ conectada a tierra. La salida $V_{out}(s)$ se toma en paralelo con la resistencia.*

> [!teoria] Función de Transferencia
> Por divisor de voltaje:
> 
> $$G(s) = \frac{Z_R}{Z_L + Z_C + Z_R} = \frac{R}{Ls + \frac{1}{Cs} + R}$$
> 
> Multiplicando numerador y denominador por $Cs$:
> 
> $$G(s) = \frac{RCs}{LCs^2 + RCs + 1}$$

> [!info] Interpretación
> - **Orden:** 2.
> - **Cero en el origen:** $s = 0$ (comportamiento pasa-altos).
> - Misma ecuación característica que el caso anterior.

---

> [!teoria] Estructura General para Circuitos Pasivos
> Para cualquier red pasiva sin fuentes controladas, el procedimiento es sistemático:
> 1. Sustituir cada componente por su impedancia $Z(s)$.
> 2. Identificar la variable de entrada $V_{in}(s)$ y la de salida $V_{out}(s)$.
> 3. Aplicar **divisor de voltaje** (para configuraciones serie) o **divisor de corriente** (para configuraciones paralelo).
> 4. Simplificar algebraicamente para obtener $G(s) = V_{out}(s)/V_{in}(s)$.

