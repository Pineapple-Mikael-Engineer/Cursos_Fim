---
title: Electrónica (Amplificadores Operacionales)
tags:
  - control-clasico
  - dominios-fisicos
  - modelado
draft: false
aliases:
  - electronica
  - amplificadores
  - op-amp
  - operacional
---

# Electrónica-Amplificadores Operacionales

# Fundamentos de electricidad en amplificadores

> [!definicion] Corriente y voltaje en un amplificador
> Un amplificador operacional (op-amp) es un dispositivo activo que **toma energía de una fuente externa** (alimentación) y la usa para amplificar la diferencia de voltaje entre sus dos entradas.
> 
> **Principio físico:**
> - Los electrones fluyen desde la fuente de alimentación hacia el circuito de salida
> - El transistor internamente **controla** esta corriente según el voltaje de entrada
> - No se "crea" energía: la salida tiene más potencia que la entrada, pero proviene de la alimentación

> [!info] Ley de conservación de energía
> $$P_{\text{entrada}} + P_{\text{alimentación}} = P_{\text{salida}} + P_{\text{disipada}}$$
> 
> - La potencia de entrada es muy pequeña (alta impedancia)
> - La potencia de salida proviene principalmente de la fuente de alimentación
> - La diferencia se disipa como calor

# El amplificador operacional ideal

> [!definicion] Op-amp ideal
> 
> ![[opamp_ideal.svg]]
> 
> **Símbolo y terminales:**
> - `+` : Entrada no inversora
> - `-` : Entrada inversora
> - `V+` : Alimentación positiva (ej. +15V)
> - `V-` : Alimentación negativa (ej. -15V)
> - `V_out` : Salida
> 
> **Características ideales:**
> 1. **Ganancia diferencial infinita:** $A_{ol} \to \infty$
> 2. **Impedancia de entrada infinita:** $Z_{in} \to \infty$ (no entra corriente)
> 3. **Impedancia de salida cero:** $Z_{out} = 0$
> 4. **Ancho de banda infinito:** funciona a cualquier frecuencia
> 5. **Offset nulo:** $V_{out} = 0$ cuando $V_+ = V_-$

# Reglas del amplificador operacional-ideal

> [!info] Reglas para análisis (con realimentación negativa)
> 
> **Regla 1:** La corriente en las entradas es cero.
> $$I_+ = I_- = 0$$
> 
> **Regla 2:** El voltaje en las entradas es igual (por realimentación, el op-amp fuerza esta condición).
> $$V_+ = V_-$$
> 
> **Regla 3:** La salida intenta hacer lo necesario para mantener $V_+ = V_-$ (mientras no se sature).

# Configuraciones básicas

## Configuración 1: Amplificador inversor

> [!ejemplo] Amplificador inversor
> 
> ![[inversor.svg]]
> 
> **Componentes:** $R_1$ (entrada), $R_f$ (realimentación)
> 
> **Análisis:**
> 
> Entrada no inversora: $V_+ = 0$ (masa virtual)
> 
> Por regla 2: $V- = V_+ = 0$ (masa virtual)
> 
> Por regla 1: $I_1 = \frac{V_{in} - V_-}{R_1} = \frac{V_{in}}{R_1}$
> 
> La corriente no entra al op-amp, entonces $I_f = I_1$
> 
> $I_f = \frac{V_- - V_{out}}{R_f} = \frac{-V_{out}}{R_f}$
> 
> **Igualando:** $\frac{V_{in}}{R_1} = -\frac{V_{out}}{R_f}$
> 
> **Función transferencia:**
> $$G(s) = \frac{V_{out}(s)}{V_{in}(s)} = -\frac{R_f}{R_1}$$
> 
> **Observaciones:**
> - Ganancia constante (independiente de frecuencia, op-amp ideal)
> - Inversión de fase: signo negativo
> - Impedancia de entrada: $Z_{in} = R_1$
> - La masa virtual hace que $V_- \approx 0$ sin conexión directa a tierra

## Configuración 2: Amplificador no inversor

> [!ejemplo] Amplificador no inversor
> 
> ![[no_inversor.svg]]
> 
> **Componentes:** $R_1$, $R_f$ (realimentación)
> 
> **Análisis:**
> 
> $V_+ = V_{in}$
> 
> Por regla 2: $V_- = V_+ = V_{in}$
> 
> Por regla 1: corriente en $R_1$: $I_1 = \frac{V_- - 0}{R_1} = \frac{V_{in}}{R_1}$
> 
> No entra corriente, entonces $I_f = I_1 = \frac{V_{out} - V_-}{R_f} = \frac{V_{out} - V_{in}}{R_f}$
> 
> **Igualando:** $\frac{V_{in}}{R_1} = \frac{V_{out} - V_{in}}{R_f}$
> 
> **Función transferencia:**
> $$G(s) = \frac{V_{out}(s)}{V_{in}(s)} = 1 + \frac{R_f}{R_1}$$
> 
> **Observaciones:**
> - Ganancia constante mayor o igual a 1
> - No inversor (signo positivo)
> - Impedancia de entrada muy alta (idealmente infinita: $V_{in}$ ve al op-amp directamente)

## Configuración 3: Seguidor de voltaje (buffer)

> [!ejemplo] Seguidor de voltaje
> 
> ![[seguidor.svg]]
> 
> **Conexión:** $V_{out}$ conectado directamente a $V_-$ ($R_f=0$, $R_1=\infty$)
> 
> **Análisis:** $V_{out} = V_- = V_+ = V_{in}$
> 
> **Función transferencia:**
> $$G(s) = 1$$
> 
> **Observaciones:**
> - Ganancia unitaria
> - Impedancia de entrada muy alta, impedancia de salida muy baja
> - Útil para aislar etapas (buffer, separador de impedancias)

# Circuitos dinámicos con op-amps

## Integrador (compensación en frecuencia)

> [!ejemplo] Integrador (Miller)
> 
> ![[integrador.svg]]
> 
> **Componentes:** $R_1$, $C_f$ (en lugar de $R_f$)
> 
> **Análisis:**
> 
> Mismo principio que inversor, pero ahora $Z_f = \frac{1}{C_f s}$
> 
> Por reglas: $V_- = 0$, $I_1 = \frac{V_{in}}{R_1}$
> 
> Corriente por $C_f$: $I_f = \frac{V_- - V_{out}}{1/(C_f s)} = -C_f s V_{out}$
> 
> $I_1 = I_f$: $\frac{V_{in}}{R_1} = -C_f s V_{out}$
> 
> **Función transferencia:**
> $$G(s) = \frac{V_{out}(s)}{V_{in}(s)} = -\frac{1}{R_1 C_f s}$$
> 
> **Observaciones:**
> - Un polo en $s=0$ (integrador puro)
> - Ganancia infinita en DC (teóricamente)
> - En la práctica, se añade una resistencia en paralelo con $C_f$ para limitar ganancia DC

## Derivador (compensación en frecuencia)

> [!ejemplo] Derivador
> 
> ![[derivador.svg]]
> 
> **Componentes:** $C_1$, $R_f$
> 
> **Análisis:**
> 
> $V_- = 0$, $I_1 = \frac{V_{in} - 0}{1/(C_1 s)} = C_1 s V_{in}$
> 
> $I_f = \frac{0 - V_{out}}{R_f} = -\frac{V_{out}}{R_f}$
> 
> $I_1 = I_f$: $C_1 s V_{in} = -\frac{V_{out}}{R_f}$
> 
> **Función transferencia:**
> $$G(s) = \frac{V_{out}(s)}{V_{in}(s)} = -R_f C_1 s$$
> 
> **Observaciones:**
> - Un cero en $s=0$ (derivador puro)
> - Muy ruidoso en la práctica (amplifica ruido de alta frecuencia)
> - Se suele añadir una resistencia en serie con $C_1$ para limitar ganancia en altas frecuencias

## Integrador y derivador prácticos

> [!info] Versiones prácticas (limitadas)
> 
> **Integrador práctico:** $R_f$ en paralelo con $C_f$ (para evitar saturación DC)
> $$G(s) = -\frac{R_f/R_1}{R_f C_f s + 1}$$
> 
> **Derivador práctico:** $R_1$ en serie con $C_1$ (para limitar ganancia en alta frecuencia)
> $$G(s) = -\frac{R_f C_1 s}{R_1 C_1 s + 1} = -\frac{R_f/R_1}{s + 1/(R_1 C_1)} \cdot s$$

## Filtro activo pasa bajos (primer orden)

> [!ejemplo] Filtro activo pasa bajos
> 
> ![[filtro_pasa_bajos.svg]]
> 
> **Componentes:** $R_1$, $R_f$, $C_f$ en paralelo con $R_f$
> 
> **Impedancia de realimentación:** $Z_f(s) = \frac{R_f}{R_f C_f s + 1}$
> 
> **Función transferencia (configuración inversora):**
> $$G(s) = -\frac{Z_f(s)}{R_1} = -\frac{R_f/R_1}{R_f C_f s + 1}$$
> 
> **Observaciones:**
> - Un polo en $s = -1/(R_f C_f)$
> - Pasa bajos de primer orden
> - Ganancia DC: $G(0) = -R_f/R_1$

## Filtro activo pasa altos (primer orden)

> [!ejemplo] Filtro activo pasa altos
> 
> ![[filtro_pasa_altos.svg]]
> 
> **Componentes:** $C_1$, $R_f$
> 
> **Impedancia de entrada:** $Z_1(s) = \frac{1}{C_1 s}$
> 
> **Función transferencia (configuración inversora):**
> $$G(s) = -\frac{R_f}{Z_1(s)} = -R_f C_1 s$$
> 
> Con resistencia en serie para limitar:
> $$G(s) = -\frac{R_f C_1 s}{R_1 C_1 s + 1}$$
> 
> **Observaciones:**
> - Un cero en $s=0$ y un polo en $s = -1/(R_1 C_1)$
> - Pasa altos de primer orden

## Filtro activo pasa bajos (segundo orden, Sallen-Key)

> [!ejemplo] Filtro Sallen-Key (bajos)
> 
> ![[sallen_key.svg]]
> 
> **Configuración:** No inversor, seguidor de voltaje ($G=1$)
> 
> **Componentes:** $R_1$, $R_2$, $C_1$, $C_2$
> 
> **Función transferencia:**
> $$G(s) = \frac{1}{R_1 R_2 C_1 C_2 s^2 + (R_1 C_2 + R_2 C_2)s + 1}$$
> 
> **Parámetros:**
> - $\omega_n = \frac{1}{\sqrt{R_1 R_2 C_1 C_2}}$
> - $\zeta = \frac{R_1 C_2 + R_2 C_2}{2\sqrt{R_1 R_2 C_1 C_2}}$
> 
> **Observaciones:**
> - Segundo orden sin usar inductores
> - Se puede ajustar $\zeta$ (amortiguamiento) para obtener Butterworth, Chebyshev, etc.

# Limitaciones del modelo ideal

> [!warning] Limitaciones reales
> 1. **Ganancia finita:** $A_{ol} \sim 10^5$ a $10^6$, no infinita. Para ganancias altas, afecta la precisión.
> 2. **Corriente de polarización:** Pequeñas corrientes entran a las entradas (del orden de nA), causan offset.
> 3. **Voltaje de offset:** Pequeña diferencia de voltaje entre entradas necesaria para que la salida sea cero ($\sim$mV).
> 4. **Ancho de banda limitado:** Producto ganancia-ancho de banda constante (ej. 1 MHz). A mayor ganancia, menor ancho de banda.
> 5. **Saturación:** La salida no puede superar los voltajes de alimentación $V+$ y $V-$.
> 6. **Slew rate:** Velocidad máxima de cambio de la salida (V/µs). Para señales rápidas, la salida se distorsiona.

# Electricidad en el amplificador (física básica)

> [!info] Funcionamiento interno simplificado
> 
> **Etapa de entrada (diferencial):**
> - Dos transistores (bipolares o FET) que comparan $V_+$ y $V_-$
> - La diferencia de voltaje genera una **diferencia de corriente**
> - Alta impedancia de entrada para no cargar la fuente
> 
> **Etapa de ganancia (intermedia):**
> - Amplifica la diferencia de corriente
> - Genera un voltaje que controla la etapa de salida
> 
> **Etapa de salida (push-pull):**
> - Transistores complementarios (NPN y PNP)
> - Entregan corriente a la carga
> - Baja impedancia de salida
> 
> **Fuente de alimentación (ej. $\pm 15V$):**
> - Proporciona la energía para amplificar
> - La salida nunca puede exceder estos voltajes (saturación)

# Resumen de configuraciones

> [!info] Tabla de funciones transferencia (op-amp ideal)
> 
> | Configuración | $G(s)$ | Tipo |
> |---------------|--------|------|
> | Inversor | $-\frac{R_f}{R_1}$ | Ganancia constante |
> | No inversor | $1 + \frac{R_f}{R_1}$ | Ganancia constante |
> | Seguidor | $1$ | Buffer |
> | Integrador | $-\frac{1}{R_1 C_f s}$ | Un polo en 0 |
> | Derivador | $-R_f C_1 s$ | Un cero en 0 |
> | Pasa bajos (inversor) | $-\frac{R_f/R_1}{R_f C_f s + 1}$ | Polo real |
> | Pasa altos (inversor) | $-\frac{R_f C_1 s}{R_1 C_1 s + 1}$ | Cero + polo |
> | Sallen-Key (bajos) | $\frac{1}{R_1 R_2 C_1 C_2 s^2 + (R_1 C_2 + R_2 C_2)s + 1}$ | Segundo orden |

# Analogía con sistemas de control

> [!info] Op-amp como controlador
> - **Inversor con ganancia $K$** → Controlador proporcional ($P$)
> - **Integrador** → Controlador integral ($I$)
> - **Derivador** → Controlador derivativo ($D$) (ruidoso)
> - **Combinaciones** → Controladores PID
> 
> Ver [[Controladores/PID]].