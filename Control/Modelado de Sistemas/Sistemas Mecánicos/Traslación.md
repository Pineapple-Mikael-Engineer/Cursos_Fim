---
title: Traslación
tags:
  - control-clasico
  - modelado
  - sistemas-mecanicos
  - traslacion
draft: true
aliases:
  - Masa-Resorte-Amortiguador
  - Sistema Mecánico Lineal
---

# Traslación

> [!definicion] Sistema Mecánico de Traslación como Sistema Dinámico
> Un **sistema mecánico de traslación** es un conjunto de masas, resortes y amortiguadores que se desplazan a lo largo de una línea recta. Desde la perspectiva de [[Control Clasico/index|control clásico]], se modela como un sistema donde una **entrada** (típicamente una fuerza $F(s)$) es procesada para producir una **salida** (típicamente una posición $X(s)$ o velocidad $V(s)$).

El objetivo es obtener la [[Control Clasico/Función de Transferencia/index|función de transferencia]]:
$$G(s) = \frac{X(s)}{F(s)} \quad \text{o} \quad G(s) = \frac{V(s)}{F(s)}$$

---

## Elementos Mecánicos en el Dominio $s$

> [!teoria] Leyes Constitutivas Transformadas
> Aplicando la [[Transformada de Laplace]] con condiciones iniciales cero, cada elemento mecánico se representa por su **impedancia mecánica** $Z_m(s) = F(s)/V(s)$:

| Elemento | Relación Fuerza-Velocidad (tiempo) | Dominio $s$ | Impedancia $Z_m(s)$ |
| :---: | :---: | :---: | :---: |
| Masa ($m$) | $f = m \frac{dv}{dt} = m \frac{d^2x}{dt^2}$ | $F(s) = msV(s) = ms^2X(s)$ | $ms$ |
| Resorte ($k$) | $f = k \int v dt = kx$ | $F(s) = \frac{k}{s}V(s) = kX(s)$ | $\frac{k}{s}$ |
| Amortiguador ($b$) | $f = bv = b\frac{dx}{dt}$ | $F(s) = bV(s) = bsX(s)$ | $b$ |

> [!info] Variables de Interés
> - $X(s)$: Desplazamiento (posición).
> - $V(s) = sX(s)$: Velocidad.
> - $A(s) = sV(s) = s^2X(s)$: Aceleración.

---

## Sistema Masa-Resorte-Amortiguador (Entrada Fuerza)

> [!ejemplo] Topología con Fuerza Aplicada a la Masa
> **Estructura:** Una masa $m$ se desplaza horizontalmente sobre una superficie sin fricción. Está conectada a un punto fijo mediante un resorte $k$ y un amortiguador $b$ en paralelo. Una fuerza externa $f(t)$ se aplica directamente sobre la masa. La salida de interés es el desplazamiento $x(t)$.

![[masa_resorte_amortiguador_fuerza.png|Esquema del sistema masa-resorte-amortiguador con fuerza aplicada]]
*Esquema TikZ: Bloque representando masa $m$. Fuerza $f(t)$ entrando por la izquierda. Resorte $k$ y amortiguador $b$ conectados en paralelo entre la masa y una pared fija. Desplazamiento $x(t)$ indicado como salida.*

> [!teoria] Ecuación de Movimiento
> Aplicando la **Segunda Ley de Newton** en el dominio del tiempo:
> 
> $$\sum F = m \frac{d^2x}{dt^2}$$
> 
> Fuerzas que actúan sobre la masa:
> - Fuerza aplicada: $+f(t)$
> - Fuerza del resorte: $-kx(t)$ (se opone al desplazamiento)
> - Fuerza del amortiguador: $-b\frac{dx}{dt}$ (se opone a la velocidad)
> 
> $$f(t) - b\frac{dx}{dt} - kx = m\frac{d^2x}{dt^2}$$
> 
> Reordenando:
> 
> $$m\frac{d^2x}{dt^2} + b\frac{dx}{dt} + kx = f(t)$$

> [!teoria] Función de Transferencia
> Aplicando la [[Transformada de Laplace]] con condiciones iniciales cero:
> 
> $$ms^2X(s) + bsX(s) + kX(s) = F(s)$$
> 
> $$X(s)(ms^2 + bs + k) = F(s)$$
> 
> $$G(s) = \frac{X(s)}{F(s)} = \frac{1}{ms^2 + bs + k}$$

> [!info] Interpretación
> - **Orden:** 2 (masa y resorte almacenan energía).
> - Forma estándar: $G(s) = \frac{1/m}{s^2 + \frac{b}{m}s + \frac{k}{m}} = \frac{1/k \cdot \omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$
>   - $\omega_n = \sqrt{\frac{k}{m}}$ (frecuencia natural)
>   - $\zeta = \frac{b}{2\sqrt{mk}}$ (factor de amortiguamiento)
>   - Ganancia estática: $G(0) = \frac{1}{k}$ (desplazamiento DC por unidad de fuerza)

---

## Sistema Masa-Resorte-Amortiguador (Entrada Desplazamiento)

> [!ejemplo] Topología con Movimiento en la Base
> **Estructura:** Una masa $m$ está conectada a una base móvil mediante un resorte $k$ y un amortiguador $b$ en paralelo. La entrada es el desplazamiento de la base $x_{in}(t)$. La salida es el desplazamiento de la masa $x_{out}(t)$. No hay fuerza externa aplicada directamente sobre la masa.

![[masa_resorte_amortiguador_base.png|Esquema del sistema con excitación por la base]]
*Esquema TikZ: Pared móvil a la izquierda con desplazamiento $x_{in}(t)$. Resorte $k$ y amortiguador $b$ en paralelo conectan la pared móvil con la masa $m$. Desplazamiento de la masa $x_{out}(t)$ como salida.*

> [!teoria] Ecuación de Movimiento
> La fuerza neta sobre la masa proviene de la deformación relativa del resorte y la velocidad relativa del amortiguador:
> 
> $$m\frac{d^2x_{out}}{dt^2} = k(x_{in} - x_{out}) + b\left(\frac{dx_{in}}{dt} - \frac{dx_{out}}{dt}\right)$$
> 
> Reordenando:
> 
> $$m\frac{d^2x_{out}}{dt^2} + b\frac{dx_{out}}{dt} + kx_{out} = b\frac{dx_{in}}{dt} + kx_{in}$$

> [!teoria] Función de Transferencia
> Aplicando la [[Transformada de Laplace]] con condiciones iniciales cero:
> 
> $$ms^2X_{out}(s) + bsX_{out}(s) + kX_{out}(s) = bsX_{in}(s) + kX_{in}(s)$$
> 
> $$X_{out}(s)(ms^2 + bs + k) = X_{in}(s)(bs + k)$$
> 
> $$G(s) = \frac{X_{out}(s)}{X_{in}(s)} = \frac{bs + k}{ms^2 + bs + k}$$

> [!info] Interpretación
> - **Orden:** 2.
> - **Ganancia DC:** $G(0) = \frac{k}{k} = 1$ (la masa sigue a la base en estado estable).
> - **Cero:** $s = -\frac{k}{b}$ (introduce sobreimpulso en la respuesta transitoria).
> - Aplicación típica: Suspensión de vehículos (la rueda sigue el perfil del camino).

---

## Sistema Masa-Resorte (Sin Amortiguamiento)

> [!ejemplo] Sistema Oscilatorio Puro
> **Estructura:** Caso particular con $b = 0$ (sin amortiguador). Masa $m$ conectada a un punto fijo mediante resorte $k$.

![[masa_resorte_puro.png|Esquema del sistema masa-resorte sin amortiguamiento]]
*Esquema TikZ: Masa $m$ conectada a pared fija mediante resorte $k$. Fuerza $f(t)$ aplicada a la masa. Desplazamiento $x(t)$ como salida.*

> [!teoria] Función de Transferencia
> Con $b = 0$ en la ecuación general:
> 
> $$G(s) = \frac{X(s)}{F(s)} = \frac{1}{ms^2 + k} = \frac{1/m}{s^2 + \omega_n^2}$$
> 
> donde $\omega_n = \sqrt{\frac{k}{m}}$.

> [!info] Interpretación
> - Polos en $s = \pm j\omega_n$ (marginalmente estable).
> - Respuesta oscilatoria no amortiguada ante cualquier perturbación.
> - No existe en la práctica real (siempre hay algún amortiguamiento).

---

## Sistema con Dos Masas Acopladas

> [!ejemplo] Topología Masa-Resorte-Masa
> **Estructura:** Dos masas $m_1$ y $m_2$ conectadas por un resorte $k$ y un amortiguador $b$ en paralelo. La fuerza $f(t)$ se aplica sobre $m_1$. Las salidas de interés son los desplazamientos $x_1(t)$ y $x_2(t)$.

![[dos_masas_acopladas.png|Esquema de sistema con dos masas acopladas por resorte y amortiguador]]
*Esquema TikZ: Fuerza $f(t)$ aplicada sobre $m_1$. Resorte $k$ y amortiguador $b$ en paralelo conectan $m_1$ con $m_2$. Desplazamientos $x_1(t)$ y $x_2(t)$ indicados.*

> [!teoria] Ecuaciones de Movimiento
> Para $m_1$:
> 
> $$m_1\frac{d^2x_1}{dt^2} = f(t) - k(x_1 - x_2) - b\left(\frac{dx_1}{dt} - \frac{dx_2}{dt}\right)$$
> 
> Para $m_2$:
> 
> $$m_2\frac{d^2x_2}{dt^2} = k(x_1 - x_2) + b\left(\frac{dx_1}{dt} - \frac{dx_2}{dt}\right)$$

> [!teoria] Función de Transferencia $X_2(s)/F(s)$
> Aplicando Laplace y resolviendo el sistema:
> 
> $$m_1s^2X_1 = F - k(X_1 - X_2) - bs(X_1 - X_2)$$
> $$m_2s^2X_2 = k(X_1 - X_2) + bs(X_1 - X_2)$$
> 
> De la segunda ecuación: $X_1 = \frac{m_2s^2 + bs + k}{bs + k}X_2$.
> 
> Sustituyendo en la primera y simplificando:
> 
> $$G(s) = \frac{X_2(s)}{F(s)} = \frac{bs + k}{m_1m_2s^4 + (m_1+m_2)bs^3 + (m_1+m_2)ks^2}$$

> [!info] Interpretación
> - **Orden:** 4 (dos masas, cada una contribuye con orden 2).
> - **Cero:** $s = -\frac{k}{b}$ (igual que en el caso de excitación por base).
> - El sistema exhibe dos modos naturales de vibración.

---

## Analogía Fuerza-Voltaje

> [!teoria] Correspondencia entre Dominios
> Existe una analogía matemática directa entre sistemas mecánicos de traslación y [[Circuitos Pasivos|circuitos eléctricos pasivos]]:

| Mecánico Traslacional | Eléctrico (Analogía F-V) |
| :---: | :---: |
| Fuerza $f(t)$ | Voltaje $v(t)$ |
| Velocidad $v(t) = \frac{dx}{dt}$ | Corriente $i(t)$ |
| Desplazamiento $x(t)$ | Carga $q(t)$ |
| Masa $m$ | Inductor $L$ |
| Resorte $k$ | Capacitor $1/C$ |
| Amortiguador $b$ | Resistencia $R$ |

> [!ejemplo] Circuito Equivalente del Masa-Resorte-Amortiguador
> La ecuación $m\frac{dv}{dt} + bv + k\int v dt = f(t)$ es análoga a un circuito **RLC serie**:
> 
> $$L\frac{di}{dt} + Ri + \frac{1}{C}\int i dt = v(t)$$
> 
> Donde $L \leftrightarrow m$, $R \leftrightarrow b$, $C \leftrightarrow 1/k$.