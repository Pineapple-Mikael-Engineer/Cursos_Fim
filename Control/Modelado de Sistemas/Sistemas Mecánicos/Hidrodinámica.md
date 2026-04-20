---
title: Hidrodinámica
tags:
  - control-clasico
  - modelado
  - sistemas-de-fluidos
  - hidrodinamica
draft: true
aliases:
  - Tanques Acoplados
  - Sistemas de Nivel
---

# Hidrodinámica

> [!definicion] Sistema Hidrodinámico como Sistema Dinámico
> Un **sistema hidrodinámico** consiste en recipientes (tanques) que se llenan o vacían mediante caudales de fluido. Desde la perspectiva de [[Control Clasico/index|control clásico]], se modela como un sistema donde una **entrada** (caudal $Q_{in}(s)$ o presión $P_{in}(s)$) es procesada para producir una **salida** (nivel $H(s)$ o caudal de salida $Q_{out}(s)$).

El análisis se realiza bajo la suposición de **comportamiento lineal**, lo que implica resistencias hidráulicas constantes y tanques de sección uniforme.

---

## Elementos Hidrodinámicos en el Dominio $s$

> [!teoria] Componentes Fundamentales
> Aplicando la [[Transformada de Laplace]] con condiciones iniciales cero, cada elemento se caracteriza por su relación entre presión (o nivel) y caudal.

| Elemento | Relación en el tiempo | Dominio $s$ |
| :---: | :---: | :---: |
| **Válvula / Restricción** ($R$) | $Q = \frac{\Delta P}{R}$ o $Q = \frac{h}{R_h}$ | $Q(s) = \frac{\Delta P(s)}{R}$ |
| **Tanque / Recipiente** ($A$) | $A \frac{dh}{dt} = Q_{in} - Q_{out}$ | $A s H(s) = Q_{in}(s) - Q_{out}(s)$ |
| **Tubería larga** ($I_f$) | $\Delta P = I_f \frac{dQ}{dt}$ | $\Delta P(s) = I_f s Q(s)$ |

> [!info] Parámetros
> - $R$: Resistencia hidráulica de la válvula [Pa·s/m³].
> - $R_h$: Resistencia referida al nivel $R_h = R/(\rho g)$ [s/m²].
> - $A$: Área transversal del tanque [m²].
> - $I_f$: Inertancia del fluido en tubería [Pa·s²/m³].

---

## 1. Tubería con Válvula entre Dos Presiones

> [!ejemplo] Topología Básica
> **Estructura:** Una tubería con una válvula conecta dos puntos con presiones conocidas $P_1$ y $P_2$. No se especifica el origen de las presiones. El interés es el caudal $Q$ que circula.

![[tuberia_valvula_presiones.png|Esquema de tubería con válvula entre dos presiones]]
*Esquema TikZ: Bloque con presión $P_1$ a la izquierda, símbolo de válvula, presión $P_2$ a la derecha. Flecha indicando caudal $Q$.*

> [!teoria] Ecuación del Caudal
> Para flujo laminar (lineal), el caudal es proporcional a la diferencia de presión:
> 
> $$Q(t) = \frac{P_1(t) - P_2(t)}{R}$$
> 
> En el dominio $s$:
> 
> $$Q(s) = \frac{1}{R} \left( P_1(s) - P_2(s) \right)$$

> [!teoria] Función de Transferencia
> Considerando $P_1(s)$ como entrada y $P_2 = 0$ como referencia:
> 
> $$G(s) = \frac{Q(s)}{P_1(s)} = \frac{1}{R}$$

> [!info] Interpretación
> - **Orden 0:** Respuesta instantánea, sin almacenamiento de fluido.
> - **Ganancia:** $1/R$ (conductancia hidráulica).

---

## 2. Tanque Simple con Válvula de Descarga

> [!ejemplo] Topología de un Tanque
> **Estructura:** Un caudal $Q_{in}$ entra a un tanque de sección transversal $A$. El fluido sale por una válvula en el fondo con resistencia $R$. La salida de interés es el nivel $h(t)$.

![[tanque_simple_hidro.png|Esquema de tanque con válvula de descarga]]
*Esquema TikZ: Caudal $Q_{in}$ entrando por arriba a un tanque de área $A$. Válvula en el fondo con caudal $Q_{out}$. Nivel $h(t)$ indicado.*

> [!teoria] Ecuación de Balance de Masa
> La variación de volumen es igual al caudal neto:
> 
> $$A \frac{dh}{dt} = Q_{in}(t) - Q_{out}(t)$$

> [!teoria] Relación Caudal de Salida - Nivel
> Para flujo laminar a través de la válvula:
> 
> $$Q_{out}(t) = \frac{h(t)}{R_h}$$
> 
> donde $R_h = R/(\rho g)$ es la resistencia referida al nivel.

> [!teoria] Función de Transferencia
> Sustituyendo y aplicando Laplace con condiciones iniciales cero:
> 
> $$A s H(s) = Q_{in}(s) - \frac{H(s)}{R_h}$$
> 
> $$H(s) \left( A s + \frac{1}{R_h} \right) = Q_{in}(s)$$
> 
> $$G(s) = \frac{H(s)}{Q_{in}(s)} = \frac{R_h}{A R_h s + 1}$$

> [!info] Interpretación
> - **Orden 1:** Un solo elemento almacenador (el tanque).
> - **Ganancia estática:** $G(0) = R_h$ (nivel por unidad de caudal).
> - **Constante de tiempo:** $\tau = A R_h$ (producto área-resistencia).

> [!teoria] Función de Transferencia Caudal-Caudal
> Dado que $Q_{out}(s) = H(s)/R_h$:
> 
> $$G(s) = \frac{Q_{out}(s)}{Q_{in}(s)} = \frac{1}{A R_h s + 1}$$

---

## 3. Dos Tanques en Cascada (No Interactuantes)

> [!ejemplo] Topología con Válvulas Independientes
> **Estructura:** El caudal $Q_{in}$ entra al Tanque 1 (área $A_1$). La salida del Tanque 1 pasa por una válvula $R_1$ y cae a un segundo tanque (área $A_2$). El Tanque 2 descarga a través de otra válvula $R_2$. La descarga del Tanque 1 **no depende** del nivel del Tanque 2.

![[dos_tanques_no_interactuantes.png|Esquema de dos tanques en cascada no interactuantes]]
*Esquema TikZ: $Q_{in}$ a Tanque 1 ($A_1$, $h_1$). Válvula $R_1$ descarga $Q_1$ a Tanque 2 ($A_2$, $h_2$). Válvula $R_2$ descarga $Q_{out}$. Caída libre entre tanques.*

> [!teoria] Ecuaciones del Sistema
> Para el Tanque 1:
> 
> $$A_1 \frac{dh_1}{dt} = Q_{in} - \frac{h_1}{R_1}$$
> 
> Para el Tanque 2:
> 
> $$A_2 \frac{dh_2}{dt} = \frac{h_1}{R_1} - \frac{h_2}{R_2}$$

> [!teoria] Función de Transferencia $H_2(s)/Q_{in}(s)$
> Aplicando Laplace:
> 
> $$H_1(s) = \frac{R_1}{A_1 R_1 s + 1} Q_{in}(s)$$
> 
> $$H_2(s) = \frac{R_2}{A_2 R_2 s + 1} \cdot \frac{H_1(s)}{R_1}$$
> 
> Sustituyendo:
> 
> $$G(s) = \frac{H_2(s)}{Q_{in}(s)} = \frac{R_2}{(A_1 R_1 s + 1)(A_2 R_2 s + 1)}$$

> [!info] Interpretación
> - **Orden 2:** Dos tanques independientes.
> - Producto de dos sistemas de primer orden.
> - Respuesta sobreamortiguada (dos polos reales).

---

## 4. Dos Tanques Acoplados con Válvula Intermedia

> [!ejemplo] Topología Interactuante
> **Estructura:** Dos tanques de áreas $A_1$ y $A_2$ conectados por una **válvula** $R_1$. El caudal entre tanques depende de la diferencia de niveles $h_1 - h_2$. El Tanque 2 descarga por una válvula $R_2$.

![[dos_tanques_acoplados_valvula.png|Esquema de dos tanques acoplados con válvula intermedia]]
*Esquema TikZ: $Q_{in}$ a Tanque 1 ($A_1$, $h_1$). Válvula $R_1$ conecta Tanque 1 con Tanque 2 ($A_2$, $h_2$). Válvula $R_2$ en salida del Tanque 2.*

> [!teoria] Ecuaciones del Sistema
> Para el Tanque 1:
> 
> $$A_1 \frac{dh_1}{dt} = Q_{in} - \frac{h_1 - h_2}{R_1}$$
> 
> Para el Tanque 2:
> 
> $$A_2 \frac{dh_2}{dt} = \frac{h_1 - h_2}{R_1} - \frac{h_2}{R_2}$$

> [!teoria] Función de Transferencia $H_2(s)/Q_{in}(s)$
> Aplicando Laplace y resolviendo el sistema:
> 
> $$A_1 s H_1 = Q_{in} - \frac{H_1 - H_2}{R_1} \implies H_1(A_1 R_1 s + 1) = R_1 Q_{in} + H_2$$
> 
> $$A_2 s H_2 = \frac{H_1 - H_2}{R_1} - \frac{H_2}{R_2}$$
> 
> Sustituyendo y simplificando:
> 
> $$G(s) = \frac{H_2(s)}{Q_{in}(s)} = \frac{R_2}{A_1 A_2 R_1 R_2 s^2 + (A_1 R_1 + A_2 R_2 + A_1 R_2)s + 1}$$

> [!info] Interpretación
> - **Orden 2** con acoplamiento.
> - El término $A_1 R_2$ en el coeficiente de $s$ refleja la interacción entre tanques.
> - Si $A_1 R_2 = 0$ (no interactuante), se recupera el producto de dos sistemas de primer orden.

---

## 5. Dos Tanques con Tubería Larga (Efecto de Inertancia)

> [!ejemplo] Topología con Inercia del Fluido
> **Estructura:** Dos tanques conectados por una **tubería larga** que introduce inercia al movimiento del fluido. El Tanque 2 descarga por una válvula $R_2$.

![[tanques_inertancia.png|Esquema de tanques con tubería larga]]
*Esquema TikZ: $Q_{in}$ a Tanque 1 ($A_1$, $h_1$). Tubería larga (longitud $L$, diámetro $D$) conecta al Tanque 2 ($A_2$, $h_2$). Válvula $R_2$ en salida.*

> [!teoria] Ecuación de la Tubería con Inertancia
> Para una tubería de longitud $L$ y sección $A_t$, la inercia del fluido introduce una caída de presión proporcional a la aceleración del caudal:
> 
> $$P_1 - P_2 = I_f \frac{dQ_1}{dt} + R_1 Q_1$$
> 
> En términos de niveles ($P = \rho g h$):
> 
> $$h_1 - h_2 = \frac{I_f}{\rho g} \frac{dQ_1}{dt} + R_1 Q_1$$
> 
> donde $I_f = \frac{\rho L}{A_t}$ es la inertancia del fluido.

> [!teoria] Ecuaciones del Sistema Completo
> Tanque 1:
> $$A_1 \frac{dh_1}{dt} = Q_{in} - Q_1$$
> 
> Tubería:
> $$h_1 - h_2 = L_h \frac{dQ_1}{dt} + R_1 Q_1 \quad \text{con } L_h = \frac{I_f}{\rho g}$$
> 
> Tanque 2:
> $$A_2 \frac{dh_2}{dt} = Q_1 - \frac{h_2}{R_2}$$

> [!teoria] Función de Transferencia
> Aplicando Laplace y eliminando variables:
> 
> $$H_1 = \frac{Q_{in} - Q_1}{A_1 s}$$
> $$H_2 = \frac{Q_1 - Q_{out}}{A_2 s} = \frac{Q_1}{A_2 s} - \frac{H_2}{A_2 R_2 s} \implies H_2 = \frac{R_2}{A_2 R_2 s + 1} Q_1$$
> 
> De la ecuación de la tubería:
> $$H_1 - H_2 = (L_h s + R_1) Q_1$$
> 
> Sustituyendo $H_1$ y $H_2$:
> 
> $$\frac{Q_{in} - Q_1}{A_1 s} - \frac{R_2}{A_2 R_2 s + 1} Q_1 = (L_h s + R_1) Q_1$$
> 
> Despejando $Q_1/Q_{in}$ y luego $H_2/Q_{in}$:
> 
> $$G(s) = \frac{H_2(s)}{Q_{in}(s)} = \frac{R_2}{a_3 s^3 + a_2 s^2 + a_1 s + 1}$$
> 
> donde los coeficientes dependen de $A_1$, $A_2$, $R_1$, $R_2$ y $L_h$.

> [!info] Interpretación
> - **Orden 3:** Dos tanques + inercia del fluido en la tubería.
> - Puede presentar respuesta oscilatoria subamortiguada.
> - El término $L_h$ introduce dinámica de segundo orden en el acoplamiento.

---

## Linealización para Válvulas Reales

> [!warning] Validez del Modelo Lineal
> En la práctica, las válvulas presentan una relación **no lineal** entre caudal y presión:
> 
> $$Q = k \sqrt{\Delta P} = k \sqrt{h}$$
> 
> Para aplicar el análisis lineal, se linealiza alrededor de un punto de operación $(h_0, Q_0)$.

> [!teoria] Procedimiento de Linealización
> 1. Expansión en serie de Taylor de primer orden:
> 
>    $$Q \approx Q_0 + \left. \frac{dQ}{dh} \right|_{h_0} (h - h_0)$$
> 
> 2. Derivada en el punto de operación:
> 
>    $$\frac{dQ}{dh} = \frac{k}{2\sqrt{h_0}} = \frac{1}{R_{eq}}$$
> 
> 3. Resistencia equivalente linealizada:
> 
>    $$R_{eq} = \frac{2\sqrt{h_0}}{k} = \frac{2 h_0}{Q_0}$$

> [!teoria] Variables de Desviación
> Se definen:
> - $\tilde{q} = Q - Q_0$ (desviación del caudal)
> - $\tilde{h} = h - h_0$ (desviación del nivel)
> 
> La relación linealizada es:
> 
> $$\tilde{q} = \frac{1}{R_{eq}} \tilde{h}$$
> 
> Esta expresión es válida **solo para pequeñas perturbaciones** alrededor del punto de equilibrio.

---

## Analogía con Circuitos Eléctricos

> [!teoria] Correspondencia de Variables
> Existe una analogía matemática exacta entre sistemas hidrodinámicos lineales y circuitos eléctricos:

| Hidrodinámico | Eléctrico |
| :---: | :---: |
| Presión $P$ (o Nivel $h$) | Voltaje $v$ |
| Caudal $Q$ | Corriente $i$ |
| Volumen $V$ | Carga $q$ |
| Resistencia hidráulica $R$ | Resistencia $R$ |
| Capacitancia hidráulica $C_h = A/(\rho g)$ | Capacitor $C$ |
| Inertancia $I_f$ | Inductor $L$ |

> [!ejemplo] Circuito Equivalente del Tanque Simple
> La ecuación $A \frac{dh}{dt} = Q_{in} - \frac{h}{R_h}$ es análoga a:
> 
> $$C \frac{dv}{dt} = i_{in} - \frac{v}{R}$$
> 
> con $C \leftrightarrow A$, $v \leftrightarrow h$, $i_{in} \leftrightarrow Q_{in}$.