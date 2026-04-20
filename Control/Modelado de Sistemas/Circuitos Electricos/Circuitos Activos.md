---
title: Circuitos Activos
tags:
  - control-clasico
  - modelado
  - circuitos-electricos
  - amplificadores
draft: true
aliases:
  - Amplificador Operacional
  - Op-Amp
---


# Circuitos Activos

> [!definicion] Circuito Activo como Sistema
> Un **circuito activo** es una red que incluye elementos capaces de entregar energía al sistema, típicamente **Amplificadores Operacionales (Op-Amp)** . Desde la perspectiva de [[Control Clasico/index|control clásico]], se modelan como sistemas con realimentación donde una **entrada** $V_{in}(s)$ es procesada para producir una **salida** $V_{out}(s)$.

A diferencia de los [[Circuitos Pasivos]], los circuitos activos permiten:
- Ganancia mayor que la unidad.
- Impedancia de entrada muy alta e impedancia de salida muy baja.
- Implementación de funciones de transferencia complejas (PID, filtros activos).

---

## Modelo Ideal del Amplificador Operacional

> [!teoria] Propiedades del Op-Amp Ideal
> El amplificador operacional ideal se caracteriza por tres propiedades fundamentales:
> 
> 1. **Ganancia infinita en lazo abierto:** $A \to \infty$
> 2. **Impedancia de entrada infinita:** $Z_{in} \to \infty$ (corrientes de entrada nulas: $i_+ = i_- = 0$)
> 3. **Impedancia de salida cero:** $Z_{out} = 0$

> [!proposicion] Consecuencia: Cortocircuito Virtual
> En configuraciones con realimentación negativa, la ganancia infinita fuerza que la diferencia de voltaje entre las entradas sea cero:
> 
> $$V_+ = V_-$$
> 
> Este principio es la base para analizar todas las configuraciones lineales con Op-Amp.

---

## Amplificador Inversor

> [!ejemplo] Configuración Inversora
> **Estructura:** La entrada $V_{in}$ se conecta a la entrada inversora ($V_-$) a través de una impedancia $Z_1$. Una impedancia de realimentación $Z_2$ conecta la salida con $V_-$. La entrada no inversora ($V_+$) se conecta a tierra.

![[amplificador_inversor.png|Esquema del amplificador inversor con impedancias Z1 y Z2]]
*Esquema TikZ: Op-Amp con entrada $V_+$ a tierra. Entrada $V_{in}$ conectada a $V_-$ mediante $Z_1$. Realimentación $Z_2$ entre $V_{out}$ y $V_-$.*

> [!teoria] Función de Transferencia
> Aplicando **Ley de Corrientes de Kirchhoff (LCK)** en el nodo $V_-$:
> 
> $$I_1 + I_2 = I_-$$
> 
> Por impedancia infinita: $I_- = 0$, luego $I_1 = -I_2$.
> 
> $$\frac{V_{in} - V_-}{Z_1} = -\frac{V_{out} - V_-}{Z_2}$$
> 
> Por cortocircuito virtual: $V_+ = V_- = 0$ (tierra virtual).
> 
> $$\frac{V_{in}}{Z_1} = -\frac{V_{out}}{Z_2}$$
> 
> $$G(s) = \frac{V_{out}(s)}{V_{in}(s)} = -\frac{Z_2(s)}{Z_1(s)}$$

> [!info] Interpretación
> - **Signo negativo:** Inversión de fase ($180^\circ$).
> - **Ganancia:** Determinada exclusivamente por la relación de impedancias externas.
> - **Impedancia de entrada:** Vista desde $V_{in}$, es $Z_{in} = Z_1$.

---

## Amplificador No Inversor

> [!ejemplo] Configuración No Inversora
> **Estructura:** La entrada $V_{in}$ se conecta directamente a la entrada no inversora ($V_+$). Un divisor de voltaje formado por $Z_1$ y $Z_2$ realimenta una fracción de la salida a la entrada inversora ($V_-$).

![[amplificador_no_inversor.png|Esquema del amplificador no inversor con divisor Z1-Z2]]
*Esquema TikZ: Op-Amp con entrada $V_{in}$ conectada a $V_+$. $Z_1$ conectada entre $V_-$ y tierra. $Z_2$ conectada entre $V_{out}$ y $V_-$.*

> [!teoria] Función de Transferencia
> Por cortocircuito virtual: $V_- = V_+ = V_{in}$.
> 
> El voltaje en $V_-$ se obtiene por divisor de voltaje desde $V_{out}$:
> 
> $$V_- = V_{out} \cdot \frac{Z_1}{Z_1 + Z_2}$$
> 
> Igualando:
> 
> $$V_{in} = V_{out} \cdot \frac{Z_1}{Z_1 + Z_2}$$
> 
> $$G(s) = \frac{V_{out}(s)}{V_{in}(s)} = \frac{Z_1 + Z_2}{Z_1} = 1 + \frac{Z_2}{Z_1}$$

> [!info] Interpretación
> - **Sin inversión de fase.**
> - **Ganancia mínima:** $G = 1$ (cuando $Z_2 = 0$ o $Z_1 \to \infty$).
> - **Impedancia de entrada:** Teóricamente infinita (ideal para sensores de alta impedancia).

---

## Seguidor de Voltaje (Buffer)

> [!ejemplo] Configuración de Seguidor Unitario
> **Estructura:** Caso especial del no inversor con $Z_1 \to \infty$ (circuito abierto) y $Z_2 = 0$ (cortocircuito).

![[seguidor_voltaje.png|Esquema del seguidor de voltaje con realimentación directa]]
*Esquema TikZ: Op-Amp con entrada $V_{in}$ a $V_+$. Salida $V_{out}$ cortocircuitada directamente a $V_-$.*

> [!teoria] Función de Transferencia
> Aplicando la fórmula del no inversor con $Z_1 \to \infty$ y $Z_2 = 0$:
> 
> $$G(s) = 1 + \frac{0}{\infty} = 1$$
> 
> $$V_{out}(s) = V_{in}(s)$$

> [!info] Interpretación
> - **Ganancia unitaria.**
> - **Aislamiento de impedancias:** Entrada de alta impedancia, salida de baja impedancia.
> - Uso típico: Adaptación entre etapas sin cargar el circuito previo.

---

## Integrador Analógico

> [!ejemplo] Configuración Integradora
> **Estructura:** Amplificador inversor con $Z_1 = R$ y $Z_2 = \frac{1}{Cs}$.

![[integrador_opamp.png|Esquema del integrador con resistencia R y capacitor C]]
*Esquema TikZ: Op-Amp inversor con $R$ en la entrada y $C$ en la realimentación.*

> [!teoria] Función de Transferencia
> Sustituyendo en la fórmula del inversor:
> 
> $$G(s) = -\frac{Z_2}{Z_1} = -\frac{\frac{1}{Cs}}{R} = -\frac{1}{RCs}$$

> [!info] Interpretación
> - En el dominio del tiempo: $v_{out}(t) = -\frac{1}{RC} \int v_{in}(t) dt$.
> - **Polo en el origen:** $s = 0$ (ganancia infinita en DC).
> - Aplicación: Controladores [[Control Clasico/index|PID]], generación de rampas.

---

## Derivador Analógico

> [!ejemplo] Configuración Derivadora
> **Estructura:** Amplificador inversor con $Z_1 = \frac{1}{Cs}$ y $Z_2 = R$.

![[derivador_opamp.png|Esquema del derivador con capacitor C y resistencia R]]
*Esquema TikZ: Op-Amp inversor con $C$ en la entrada y $R$ en la realimentación.*

> [!teoria] Función de Transferencia
> Sustituyendo en la fórmula del inversor:
> 
> $$G(s) = -\frac{Z_2}{Z_1} = -\frac{R}{\frac{1}{Cs}} = -RCs$$

> [!info] Interpretación
> - En el dominio del tiempo: $v_{out}(t) = -RC \frac{d}{dt} v_{in}(t)$.
> - **Cero en el origen:** $s = 0$.
> - Amplifica ruido de alta frecuencia (implementación práctica requiere filtro limitador).

---

## Filtro Activo Pasa-Bajos de Primer Orden

> [!ejemplo] Integrador con Realimentación Resistiva
> **Estructura:** Amplificador inversor con $Z_1 = R_1$ y $Z_2 = R_2 \parallel C$ (paralelo).

![[filtro_activo_pasabajos.png|Esquema del filtro pasa-bajos activo de primer orden]]
*Esquema TikZ: Op-Amp inversor con $R_1$ en entrada. Realimentación con $R_2$ en paralelo con $C$.*

> [!teoria] Función de Transferencia
> Impedancia de realimentación: $Z_2 = R_2 \parallel \frac{1}{Cs} = \frac{R_2 \cdot \frac{1}{Cs}}{R_2 + \frac{1}{Cs}} = \frac{R_2}{R_2Cs + 1}$.
> 
> $$G(s) = -\frac{Z_2}{Z_1} = -\frac{R_2}{R_1} \cdot \frac{1}{R_2Cs + 1}$$

> [!info] Interpretación
> - **Ganancia DC:** $-\frac{R_2}{R_1}$.
> - **Frecuencia de corte:** $\omega_c = \frac{1}{R_2C}$.
> - Ventaja sobre el RC pasivo: Ganancia ajustable independientemente de la frecuencia de corte.

---

> [!teoria] Comparación con Circuitos Pasivos
> | Característica | [[Circuitos Pasivos]] | **Circuitos Activos** |
> | :---: | :---: | :---: |
> | Ganancia | $\leq 1$ | Cualquier valor (típ. $>1$) |
> | Impedancia de entrada | Depende de la red | Muy alta (idealmente $\infty$) |
> | Impedancia de salida | Depende de la red | Muy baja (idealmente $0$) |
> | Implementación de polos | Pasivos (limitados) | Arbitrarios (con realimentación) |
> | Alimentación | No requiere | Requiere fuente DC ($\pm V_{cc}$) |

---
