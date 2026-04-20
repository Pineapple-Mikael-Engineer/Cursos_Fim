---
title: Rotación
tags:
  - control-clasico
  - modelado
  - sistemas-mecanicos
  - rotacion
draft: true
aliases:
  - Inercia-Resorte-Amortiguador Angular
  - Sistema Mecánico Rotacional
---

# Rotación

> [!definicion] Sistema Mecánico de Rotación como Sistema Dinámico
> Un **sistema mecánico de rotación** es un conjunto de inercias, resortes torsionales y amortiguadores rotacionales que giran alrededor de un eje. Desde la perspectiva de [[Control Clasico/index|control clásico]], se modela como un sistema donde una **entrada** (típicamente un torque $T(s)$) es procesada para producir una **salida** (típicamente una posición angular $\theta(s)$ o velocidad angular $\Omega(s)$).

El objetivo es obtener la [[Control Clasico/Función de Transferencia/index|función de transferencia]]:
$$G(s) = \frac{\theta(s)}{T(s)} \quad \text{o} \quad G(s) = \frac{\Omega(s)}{T(s)}$$

---

## Elementos Rotacionales en el Dominio $s$

> [!teoria] Leyes Constitutivas Transformadas
> Aplicando la [[Transformada de Laplace]] con condiciones iniciales cero, cada elemento rotacional se representa por su **impedancia mecánica rotacional** $Z_r(s) = T(s)/\Omega(s)$:

| Elemento | Relación Torque-Velocidad Angular (tiempo) | Dominio $s$ | Impedancia $Z_r(s)$ |
| :---: | :---: | :---: | :---: |
| Inercia ($J$) | $\tau = J \frac{d\omega}{dt} = J \frac{d^2\theta}{dt^2}$ | $T(s) = Js\Omega(s) = Js^2\theta(s)$ | $Js$ |
| Resorte torsional ($K$) | $\tau = K \int \omega dt = K\theta$ | $T(s) = \frac{K}{s}\Omega(s) = K\theta(s)$ | $\frac{K}{s}$ |
| Amortiguador rotacional ($B$) | $\tau = B\omega = B\frac{d\theta}{dt}$ | $T(s) = B\Omega(s) = Bs\theta(s)$ | $B$ |

> [!info] Variables de Interés
> - $\theta(s)$: Desplazamiento angular (posición).
> - $\Omega(s) = s\theta(s)$: Velocidad angular.
> - $\alpha(s) = s\Omega(s) = s^2\theta(s)$: Aceleración angular.

---

## Sistema Inercia-Resorte-Amortiguador (Entrada Torque)

> [!ejemplo] Topología con Torque Aplicado a la Inercia
> **Estructura:** Una inercia $J$ gira sobre un eje sin fricción. Está conectada a un punto fijo mediante un resorte torsional $K$ y un amortiguador rotacional $B$ en paralelo. Un torque externo $\tau(t)$ se aplica directamente sobre la inercia. La salida de interés es el desplazamiento angular $\theta(t)$.

![[inercia_resorte_amortiguador_torque.png|Esquema del sistema inercia-resorte-amortiguador rotacional con torque aplicado]]
*Esquema TikZ: Disco representando inercia $J$. Torque $\tau(t)$ aplicado al eje. Resorte torsional $K$ y amortiguador rotacional $B$ conectados en paralelo entre la inercia y una referencia fija. Desplazamiento angular $\theta(t)$ indicado como salida.*

> [!teoria] Ecuación de Movimiento
> Aplicando la **Segunda Ley de Newton para Rotación** en el dominio del tiempo:
> 
> $$\sum \tau = J \frac{d^2\theta}{dt^2}$$
> 
> Torques que actúan sobre la inercia:
> - Torque aplicado: $+\tau(t)$
> - Torque del resorte: $-K\theta(t)$ (se opone al desplazamiento angular)
> - Torque del amortiguador: $-B\frac{d\theta}{dt}$ (se opone a la velocidad angular)
> 
> $$\tau(t) - B\frac{d\theta}{dt} - K\theta = J\frac{d^2\theta}{dt^2}$$
> 
> Reordenando:
> 
> $$J\frac{d^2\theta}{dt^2} + B\frac{d\theta}{dt} + K\theta = \tau(t)$$

> [!teoria] Función de Transferencia
> Aplicando la [[Transformada de Laplace]] con condiciones iniciales cero:
> 
> $$Js^2\theta(s) + Bs\theta(s) + K\theta(s) = T(s)$$
> 
> $$\theta(s)(Js^2 + Bs + K) = T(s)$$
> 
> $$G(s) = \frac{\theta(s)}{T(s)} = \frac{1}{Js^2 + Bs + K}$$

> [!info] Interpretación
> - **Orden:** 2 (inercia y resorte almacenan energía).
> - Forma estándar: $G(s) = \frac{1/J}{s^2 + \frac{B}{J}s + \frac{K}{J}} = \frac{1/K \cdot \omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$
>   - $\omega_n = \sqrt{\frac{K}{J}}$ (frecuencia natural)
>   - $\zeta = \frac{B}{2\sqrt{JK}}$ (factor de amortiguamiento)
>   - Ganancia estática: $G(0) = \frac{1}{K}$ (desplazamiento angular DC por unidad de torque)

---

## Sistema con Entrada Desplazamiento Angular

> [!ejemplo] Topología con Movimiento Angular en la Base
> **Estructura:** Una inercia $J$ está conectada a una base giratoria mediante un resorte torsional $K$ y un amortiguador rotacional $B$ en paralelo. La entrada es el desplazamiento angular de la base $\theta_{in}(t)$. La salida es el desplazamiento angular de la inercia $\theta_{out}(t)$.

![[inercia_resorte_amortiguador_base_rotacional.png|Esquema del sistema rotacional con excitación por la base]]
*Esquema TikZ: Base giratoria a la izquierda con desplazamiento angular $\theta_{in}(t)$. Resorte torsional $K$ y amortiguador rotacional $B$ en paralelo conectan la base con la inercia $J$. Desplazamiento angular de la inercia $\theta_{out}(t)$ como salida.*

> [!teoria] Ecuación de Movimiento
> El torque neto sobre la inercia proviene de la deformación relativa del resorte y la velocidad relativa del amortiguador:
> 
> $$J\frac{d^2\theta_{out}}{dt^2} = K(\theta_{in} - \theta_{out}) + B\left(\frac{d\theta_{in}}{dt} - \frac{d\theta_{out}}{dt}\right)$$
> 
> Reordenando:
> 
> $$J\frac{d^2\theta_{out}}{dt^2} + B\frac{d\theta_{out}}{dt} + K\theta_{out} = B\frac{d\theta_{in}}{dt} + K\theta_{in}$$

> [!teoria] Función de Transferencia
> Aplicando la [[Transformada de Laplace]] con condiciones iniciales cero:
> 
> $$Js^2\theta_{out}(s) + Bs\theta_{out}(s) + K\theta_{out}(s) = Bs\theta_{in}(s) + K\theta_{in}(s)$$
> 
> $$\theta_{out}(s)(Js^2 + Bs + K) = \theta_{in}(s)(Bs + K)$$
> 
> $$G(s) = \frac{\theta_{out}(s)}{\theta_{in}(s)} = \frac{Bs + K}{Js^2 + Bs + K}$$

> [!info] Interpretación
> - **Orden:** 2.
> - **Ganancia DC:** $G(0) = \frac{K}{K} = 1$ (la inercia sigue a la base en estado estable).
> - **Cero:** $s = -\frac{K}{B}$.
> - Aplicación típica: Transmisión flexible entre motor y carga.

---

## Tren de Engranajes

> [!ejemplo] Sistema con Dos Inercias Acopladas por Engranajes
> **Estructura:** Dos ejes con inercias $J_1$ y $J_2$ conectados mediante un tren de engranajes con relación de transmisión $N = \frac{n_2}{n_1}$ (número de dientes). Un torque $\tau_1(t)$ se aplica al eje 1. Las salidas de interés son $\theta_1(t)$ y $\theta_2(t)$.

![[tren_engranajes.png|Esquema de tren de engranajes con dos inercias]]
*Esquema TikZ: Torque $\tau_1$ aplicado a inercia $J_1$. Engranaje 1 ($n_1$ dientes) acoplado a engranaje 2 ($n_2$ dientes) conectado a inercia $J_2$. Resorte $K$ y amortiguador $B$ en el eje 2 representando flexibilidad.*

> [!teoria] Relaciones del Tren de Engranajes Ideal
> Para engranajes ideales (sin juego ni pérdidas):
> 
> $$\frac{\theta_1}{\theta_2} = \frac{n_2}{n_1} = N$$
> $$\frac{\tau_1}{\tau_2} = \frac{n_1}{n_2} = \frac{1}{N}$$

> [!teoria] Reflexión de Impedancias
> Para analizar el sistema, se reflejan todos los elementos al eje 1 (o eje 2). Reflejando al eje 1:
> 
> $$J_{eq} = J_1 + N^2 J_2$$
> $$B_{eq} = B_1 + N^2 B_2$$
> $$K_{eq} = K_1 + N^2 K_2$$
> 
> La función de transferencia vista desde $\tau_1$ es:
> 
> $$G(s) = \frac{\theta_1(s)}{T_1(s)} = \frac{1}{J_{eq}s^2 + B_{eq}s + K_{eq}}$$
> 
> Y para obtener $\theta_2(s)$:
> 
> $$\theta_2(s) = \frac{1}{N} \theta_1(s)$$

> [!info] Interpretación
> - La inercia de la carga se refleja multiplicada por $N^2$.
> - Un tren reductor ($N > 1$) reduce la inercia reflejada de la carga.
> - Un tren multiplicador ($N < 1$) aumenta la inercia reflejada.

---

## Péndulo Simple

> [!ejemplo] Péndulo Linealizado
> **Estructura:** Una masa puntual $m$ suspendida de una cuerda de longitud $L$. El ángulo $\theta(t)$ se mide desde la vertical. La entrada es un torque $\tau(t)$ aplicado en el pivote.

![[pendulo_simple.png|Esquema del péndulo simple con torque aplicado]]
*Esquema TikZ: Masa $m$ suspendida de cuerda de longitud $L$. Ángulo $\theta$ medido desde la vertical. Torque $\tau$ aplicado en el pivote. Fuerza de gravedad $mg$ actuando hacia abajo.*

> [!teoria] Ecuación de Movimiento (No Lineal)
> Por conservación de momento angular:
> 
> $$mL^2 \frac{d^2\theta}{dt^2} + mgL \sin\theta = \tau(t)$$

> [!teoria] Linealización para Ángulos Pequeños
> Para $\theta \approx 0$, se aproxima $\sin\theta \approx \theta$:
> 
> $$mL^2 \frac{d^2\theta}{dt^2} + mgL \theta = \tau(t)$$

> [!teoria] Función de Transferencia Linealizada
> Aplicando Laplace:
> 
> $$mL^2 s^2 \theta(s) + mgL \theta(s) = T(s)$$
> 
> $$G(s) = \frac{\theta(s)}{T(s)} = \frac{1}{mL^2 s^2 + mgL} = \frac{1/(mgL)}{\frac{L}{g}s^2 + 1}$$

> [!info] Interpretación
> - **Orden:** 2 (sin amortiguamiento, $B = 0$).
> - **Frecuencia natural:** $\omega_n = \sqrt{\frac{g}{L}}$.
> - Polos en $s = \pm j\sqrt{\frac{g}{L}}$ (marginalmente estable).
> - La linealización es válida solo para pequeñas oscilaciones.

---

## Analogía con Sistemas de Traslación

> [!teoria] Correspondencia Traslación-Rotación
> Las ecuaciones son matemáticamente idénticas, solo cambian las variables:

| Traslación | Rotación |
| :---: | :---: |
| Fuerza $f(t)$ | Torque $\tau(t)$ |
| Masa $m$ | Inercia $J$ |
| Desplazamiento $x(t)$ | Ángulo $\theta(t)$ |
| Velocidad $v(t)$ | Velocidad angular $\omega(t)$ |
| Resorte $k$ | Resorte torsional $K$ |
| Amortiguador $b$ | Amortiguador rotacional $B$ |

> [!ejemplo] Equivalencia Directa
> La función de transferencia $\frac{X(s)}{F(s)} = \frac{1}{ms^2 + bs + k}$ de [[Traslación]] es idéntica en forma a $\frac{\theta(s)}{T(s)} = \frac{1}{Js^2 + Bs + K}$ de rotación.

---

## Analogía con Circuitos Eléctricos

> [!teoria] Correspondencia Rotación-Eléctrico
> Extendiendo la analogía de [[Traslación]]:

| Rotación | Eléctrico (Analogía T-V) |
| :---: | :---: |
| Torque $\tau(t)$ | Voltaje $v(t)$ |
| Velocidad angular $\omega(t)$ | Corriente $i(t)$ |
| Ángulo $\theta(t)$ | Carga $q(t)$ |
| Inercia $J$ | Inductor $L$ |
| Resorte torsional $K$ | Capacitor $1/C$ |
| Amortiguador rotacional $B$ | Resistencia $R$ |

> [!ejemplo] Circuito Equivalente
> La ecuación $J\frac{d\omega}{dt} + B\omega + K\int \omega dt = \tau(t)$ es análoga a un circuito **RLC serie**:
> 
> $$L\frac{di}{dt} + Ri + \frac{1}{C}\int i dt = v(t)$$
> 
> Donde $L \leftrightarrow J$, $R \leftrightarrow B$, $C \leftrightarrow 1/K$.

