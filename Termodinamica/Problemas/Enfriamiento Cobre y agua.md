---
title: Enfriamiento de un Cubo de Cobre en Agua
tags:
  - termodinámica
  - transferencia-de-calor
  - ecuaciones-diferenciales
  - ley-enfriamiento-newton
  - balance-energético
  - ejercicio-resuelto
draft: true
---

# Enfriamiento de un Cubo de Cobre en Agua

> [!abstract] Resumen
> Este ejercicio resuelto modela la transferencia de calor entre un cubo de cobre caliente y un volumen de agua fría. Se presentan dos enfoques: el primero usando la [[Ley de Enfriamiento de Newton]] de manera rigurosa, y el segundo siguiendo un método basado en diferencias de temperaturas y constantes fenomenológicas, que permite mayor flexibilidad para variar condiciones iniciales.

## Planteamiento

Un cubo de cobre de **10 cm** de lado a **200°C** se introduce en **3 litros** de agua a **20°C**. El sistema se demora **2 minutos** en calentar el agua hasta **25°C**.

**Datos:**
- Lado del cubo: $L = 0.1\ \text{m}$
- Temperatura inicial del cobre: $T_{Cu,0} = 200\ \text{°C}$
- Volumen de agua: $V_{H_2O} = 0.003\ \text{m}^3$
- Temperatura inicial del agua: $T_{H_2O,0} = 20\ \text{°C}$
- Temperatura del agua en $t_1 = 2\ \text{min}$: $T_{H_2O}(t_1) = 25\ \text{°C}$
- Calor específico del cobre: $c_{Cu} = 0.39\ \text{kJ/(kg·K)} = 390\ \text{J/(kg·K)}$
- Calor específico del agua: $c_{H_2O} = 4.18\ \text{kJ/(kg·K)} = 4180\ \text{J/(kg·K)}$
- Densidad del cobre: $\rho_{Cu} = 8960\ \text{kg/m}^3$
- Densidad del agua: $\rho_{H_2O} = 1000\ \text{kg/m}^3$

**Objetivos:**
- **a)** Proponer una expresión para $T_{H_2O}(t)$
- **b)** Determinar el tiempo para que el agua alcance $30\ \text{°C}$

> [!warning] Suposiciones Fundamentales
> 1. La transferencia de calor es proporcional a la diferencia de temperaturas.
> 2. El sistema está perfectamente aislado (no hay pérdidas al exterior).
> 3. Las propiedades termofísicas son constantes.
> 4. La temperatura es uniforme en cada cuerpo en cada instante.

## Esquema del Sistema

> [!figure] Diagrama de transferencia de calor
> 
> ![[imagen.png]]
> 
> *Representación esquemática del intercambio térmico entre el cubo de cobre y el agua.*

---

## Método 1: Ley de Enfriamiento de Newton (Enfoque Riguroso)

> [!teoria] Ley de Enfriamiento de Newton
> La potencia térmica transferida desde el cobre al agua es:
> $$
> \frac{dQ}{dt} = hA\left(T_{Cu}(t) - T_{H_2O}(t)\right)
> $$

### Paso 1: Masas y capacidades térmicas

**Masa del cobre:**
$$
m_{Cu} = \rho_{Cu} L^3 = 8960 \cdot (0.1)^3 = 8.96\ \text{kg}
$$

**Masa del agua:**
$$
m_{H_2O} = \rho_{H_2O} V_{H_2O} = 1000 \cdot 0.003 = 3\ \text{kg}
$$

**Capacidades térmicas:**
$$
C_{Cu} = m_{Cu}c_{Cu} = 8.96 \cdot 390 = 3494.4\ \text{J/K}
$$
$$
C_{H_2O} = m_{H_2O}c_{H_2O} = 3 \cdot 4180 = 12540\ \text{J/K}
$$
$$
\alpha = \frac{C_{H_2O}}{C_{Cu}} \approx 3.588
$$

### Paso 2: Relación entre temperaturas por balance energético

Calor perdido por Cu = Calor ganado por agua:

$$
-C_{Cu}(T_{Cu} - T_{Cu,0}) = C_{H_2O}(T_{H_2O} - T_{H_2O,0})
$$

Despejando:

$$
T_{Cu}(t) = T_{Cu,0} - \alpha \left(T_{H_2O}(t) - T_{H_2O,0}\right)
$$

### Paso 3: Temperatura de equilibrio

Cuando $t \to \infty$, $T_{Cu} = T_{H_2O} = T_f$:

$$
T_f = \frac{C_{Cu}T_{Cu,0} + C_{H_2O}T_{H_2O,0}}{C_{Cu} + C_{H_2O}} = \frac{3494.4 \cdot 200 + 12540 \cdot 20}{3494.4 + 12540} \approx 59.23\ \text{°C}
$$

### Paso 4: Ecuación diferencial para el agua

$$
C_{H_2O} \frac{dT_{H_2O}}{dt} = hA (T_{Cu} - T_{H_2O})
$$

Sustituyendo $T_{Cu}$:

$$
T_{Cu} - T_{H_2O} = (1 + \alpha)(T_f - T_{H_2O}) = \beta (T_f - T_{H_2O})
$$

con $\beta = 1 + \alpha \approx 4.588$.

Entonces:

$$
\frac{dT_{H_2O}}{dt} = \frac{hA\beta}{C_{H_2O}} (T_f - T_{H_2O}) = \frac{1}{\tau} (T_f - T_{H_2O})
$$

### Paso 5: Solución

Integrando:

$$
\int_{T_{H_2O,0}}^{T_{H_2O}} \frac{dT}{T_f - T} = \int_0^t \frac{dt}{\tau}
$$

$$
-\ln\left(\frac{T_f - T_{H_2O}}{T_f - T_{H_2O,0}}\right) = \frac{t}{\tau}
$$

$$
\boxed{T_{H_2O}(t) = T_f - (T_f - T_{H_2O,0}) e^{-t/\tau}}
$$

### Paso 6: Determinar $\tau$ con el dato experimental

Para $t_1 = 120\ \text{s}$, $T_{H_2O} = 25\ \text{°C}$:

$$
25 = 59.23 - 39.23 e^{-120/\tau} \quad \Rightarrow \quad e^{-120/\tau} = \frac{34.23}{39.23} \approx 0.8725
$$

$$
\tau = \frac{120}{-\ln(0.8725)} \approx \frac{120}{0.1364} \approx 879.8\ \text{s}
$$

### Paso 7: Tiempo para $30\ \text{°C}$

$$
30 = 59.23 - 39.23 e^{-t/879.8} \quad \Rightarrow \quad e^{-t/879.8} = \frac{29.23}{39.23} \approx 0.7451
$$

$$
t = -879.8 \cdot \ln(0.7451) \approx 879.8 \cdot 0.2943 \approx 259\ \text{s} \approx 4.32\ \text{min}
$$

> [!success] Resultados Método 1
> - **Expresión:** $T_{H_2O}(t) = 59.23 - 39.23 e^{-t/879.8}$ (con $t$ en segundos)
> - **Tiempo para 30°C:** $t \approx 4.32\ \text{min}$

---

## Método 2: Enfoque Fenomenológico de Constantes 

Este método sigue tu idea original de usar solo constantes $k$, $k_1$, $k_2$ sin introducir explícitamente $h$, $A$, ni áreas. Todo se maneja en términos de **capacidades térmicas** y una **constante de acoplamiento fenomenológica** $K$.

### Paso 1: Ecuaciones de balance para cada masa

$$
\begin{aligned}
\left( T_{H_2O}(t) - T_{H_2O,0} \right) C_{H_2O} &= Q_{H_2O} \quad &(1)\\
\left( T_{Cu}(t) - T_{Cu,0} \right) C_{Cu} &= Q_{Cu} \quad &(2)
\end{aligned}
$$

### Paso 2: Relación fenomenológica

Proponemos que la **tasa de transferencia de calor** es proporcional a la diferencia de temperaturas:

$$
\boxed{\frac{dQ_{H_2O}}{dt} = K \left( T_{Cu}(t) - T_{H_2O}(t) \right)}
$$

donde $K$ es una **constante fenomenológica global** (en W/K o J/(s·K)) que encapsula todo: conductividad, área, geometría, etc.

Por conservación de energía:

$$
\frac{dQ_{Cu}}{dt} = -\frac{dQ_{H_2O}}{dt} = -K \left( T_{Cu}(t) - T_{H_2O}(t) \right)
$$

### Paso 3: Derivar las ecuaciones (1) y (2) respecto al tiempo

Derivando (1):

$$
C_{H_2O} \frac{dT_{H_2O}}{dt} = \frac{dQ_{H_2O}}{dt} = K \left( T_{Cu} - T_{H_2O} \right) \quad (3)
$$

Derivando (2):

$$
C_{Cu} \frac{dT_{Cu}}{dt} = \frac{dQ_{Cu}}{dt} = -K \left( T_{Cu} - T_{H_2O} \right) \quad (4)
$$

### Paso 4: Definir variables reducidas

Definimos:

$$
k_1 = \frac{K}{C_{H_2O}}, \qquad k_2 = \frac{K}{C_{Cu}}
$$

Las ecuaciones (3) y (4) se reescriben como:

$$
\begin{aligned}
\frac{dT_{H_2O}}{dt} &= k_1 \left( T_{Cu} - T_{H_2O} \right) \quad &(5)\\
\frac{dT_{Cu}}{dt} &= -k_2 \left( T_{Cu} - T_{H_2O} \right) \quad &(6)
\end{aligned}
$$

> [!note] Observación
> Las constantes $k_1$ y $k_2$ tienen unidades de $s^{-1}$. Son **tasas características** de cada cuerpo.

### Paso 5: Ecuación para la diferencia de temperaturas

Definimos $\Delta(t) = T_{Cu}(t) - T_{H_2O}(t)$.

Restamos (5) y (6):

$$
\frac{dT_{H_2O}}{dt} - \frac{dT_{Cu}}{dt} = k_1 \Delta - (-k_2 \Delta) = (k_1 + k_2) \Delta
$$

Pero $\frac{dT_{H_2O}}{dt} - \frac{dT_{Cu}}{dt} = -\frac{d\Delta}{dt}$, entonces:

$$
-\frac{d\Delta}{dt} = (k_1 + k_2) \Delta
$$

$$
\boxed{\frac{d\Delta}{dt} = -(k_1 + k_2) \Delta}
$$

### Paso 6: Solución para $\Delta(t)$

Esta es una EDO exponencial simple:

$$
\Delta(t) = \Delta(0) e^{-(k_1 + k_2) t}
$$

donde $\Delta(0) = T_{Cu,0} - T_{H_2O,0} = 200 - 20 = 180\ \text{°C}$.

Definimos la **constante de tiempo fenomenológica**:

$$
\boxed{\tau = \frac{1}{k_1 + k_2} = \frac{1}{\frac{K}{C_{H_2O}} + \frac{K}{C_{Cu}}} = \frac{C_{H_2O} C_{Cu}}{K (C_{H_2O} + C_{Cu})}}
$$

Entonces:

$$
\Delta(t) = \Delta(0) e^{-t/\tau}
$$

### Paso 7: Relación entre $T_{H_2O}$ y $T_{Cu}$ por balance energético

De la conservación de la energía total (sumando (1) y (2) en forma diferencial o integrada):

$$
C_{H_2O} \left( T_{H_2O}(t) - T_{H_2O,0} \right) + C_{Cu} \left( T_{Cu}(t) - T_{Cu,0} \right) = 0
$$

Despejamos $T_{Cu}(t)$:

$$
\boxed{T_{Cu}(t) = T_{Cu,0} - \frac{C_{H_2O}}{C_{Cu}} \left( T_{H_2O}(t) - T_{H_2O,0} \right)}
$$

### Paso 8: Expresar $T_{H_2O}(t)$ en términos de $\Delta(t)$

Sabemos que $T_{Cu}(t) = T_{H_2O}(t) + \Delta(t)$. Sustituimos en la relación anterior:

$$
T_{H_2O}(t) + \Delta(t) = T_{Cu,0} - \frac{C_{H_2O}}{C_{Cu}} \left( T_{H_2O}(t) - T_{H_2O,0} \right)
$$

Agrupamos términos con $T_{H_2O}$:

$$
T_{H_2O}(t) + \frac{C_{H_2O}}{C_{Cu}} T_{H_2O}(t) = T_{Cu,0} + \frac{C_{H_2O}}{C_{Cu}} T_{H_2O,0} - \Delta(t)
$$

$$
T_{H_2O}(t) \left( 1 + \frac{C_{H_2O}}{C_{Cu}} \right) = T_{Cu,0} + \frac{C_{H_2O}}{C_{Cu}} T_{H_2O,0} - \Delta(t)
$$

Pero $1 + \frac{C_{H_2O}}{C_{Cu}} = \frac{C_{Cu} + C_{H_2O}}{C_{Cu}}$, entonces:

$$
T_{H_2O}(t) = \frac{C_{Cu}}{C_{Cu} + C_{H_2O}} \left( T_{Cu,0} + \frac{C_{H_2O}}{C_{Cu}} T_{H_2O,0} - \Delta(t) \right)
$$

$$
T_{H_2O}(t) = \frac{C_{Cu} T_{Cu,0} + C_{H_2O} T_{H_2O,0}}{C_{Cu} + C_{H_2O}} - \frac{C_{Cu}}{C_{Cu} + C_{H_2O}} \Delta(t)
$$

### Paso 9: Identificar la temperatura de equilibrio $T_f$

Cuando $t \to \infty$, $\Delta(\infty) = 0$, entonces:

$$
T_f = \frac{C_{Cu} T_{Cu,0} + C_{H_2O} T_{H_2O,0}}{C_{Cu} + C_{H_2O}}
$$

Además, notamos que:

$$
\frac{C_{Cu}}{C_{Cu} + C_{H_2O}} \Delta(0) = \frac{C_{Cu}}{C_{Cu} + C_{H_2O}} (T_{Cu,0} - T_{H_2O,0}) = T_f - T_{H_2O,0}
$$

Por lo tanto:

$$
\frac{C_{Cu}}{C_{Cu} + C_{H_2O}} \Delta(t) = (T_f - T_{H_2O,0}) e^{-t/\tau}
$$

### Paso 10: Expresión final para $T_{H_2O}(t)$

Sustituyendo en la expresión del Paso 8:

$$
\boxed{T_{H_2O}(t) = T_f - (T_f - T_{H_2O,0}) e^{-t/\tau}}
$$

### Paso 11: Determinar $K$ y $\tau$ a partir del dato experimental

Primero calculamos las capacidades térmicas (como antes):

$$
C_{Cu} = 3494.4\ \text{J/K}, \qquad C_{H_2O} = 12540\ \text{J/K}
$$

$$
T_f = \frac{3494.4 \cdot 200 + 12540 \cdot 20}{3494.4 + 12540} = \frac{698880 + 250800}{16034.4} = \frac{949680}{16034.4} \approx 59.23\ \text{°C}
$$

Con el dato $t_1 = 120\ \text{s}$, $T_{H_2O}(t_1) = 25\ \text{°C}$:

$$
25 = 59.23 - (59.23 - 20) e^{-120/\tau}
$$

$$
25 = 59.23 - 39.23 e^{-120/\tau}
$$

$$
39.23 e^{-120/\tau} = 34.23
$$

$$
e^{-120/\tau} = \frac{34.23}{39.23} \approx 0.8725
$$

$$
-\frac{120}{\tau} = \ln(0.8725) \approx -0.1364
$$

$$
\boxed{\tau = \frac{120}{0.1364} \approx 879.8\ \text{s}}
$$

Ahora despejamos $K$ de la expresión de $\tau$:

$$
\tau = \frac{C_{H_2O} C_{Cu}}{K (C_{H_2O} + C_{Cu})} \quad \Rightarrow \quad K = \frac{C_{H_2O} C_{Cu}}{\tau (C_{H_2O} + C_{Cu})}
$$

$$
K = \frac{12540 \cdot 3494.4}{879.8 \cdot 16034.4} = \frac{43\,819\,776}{14\,107\,000} \approx \boxed{3.11\ \text{W/K}}
$$

### Paso 12: Tiempo para alcanzar $30\ \text{°C}$

$$
30 = 59.23 - 39.23 e^{-t/879.8}
$$

$$
39.23 e^{-t/879.8} = 29.23
$$

$$
e^{-t/879.8} = \frac{29.23}{39.23} \approx 0.7451
$$

$$
-\frac{t}{879.8} = \ln(0.7451) \approx -0.2943
$$

$$
\boxed{t = 879.8 \cdot 0.2943 \approx 259\ \text{s} \approx 4.32\ \text{min}}
$$

---

## Resumen del Método Fenomenológico 

> [!success] Constantes fenomenológicas clave
> - **$K$** : constante de acoplamiento global (W/K)
> - **$k_1 = K/C_{H_2O}$** : tasa de calentamiento del agua (s⁻¹)
> - **$k_2 = K/C_{Cu}$** : tasa de enfriamiento del cobre (s⁻¹)
> - **$\tau = 1/(k_1 + k_2)$** : constante de tiempo del sistema (s)

> [!success] Expresiones finales en variables simbólicas
> $$
> \boxed{T_{H_2O}(t) = T_f - (T_f - T_{H_2O,0}) e^{-t/\tau}}
> $$
> $$
> \boxed{T_f = \frac{C_{Cu}T_{Cu,0} + C_{H_2O}T_{H_2O,0}}{C_{Cu} + C_{H_2O}}}
> $$
> $$
> \boxed{\tau = \frac{C_{H_2O}C_{Cu}}{K(C_{H_2O} + C_{Cu})}}
> $$

---

## Ventajas de Tu Método Fenomenológico

> [!tip] ¿Por qué es mejor este enfoque para ti?
> 
> 1. **No necesitas $h$, $A$, ni geometría** — todo está en $K$.
> 2. **Puras variables simbólicas** — puedes cambiar masas, calores específicos, o $K$ y ver cómo afecta $\tau$.
> 3. **Ideal para análisis de sensibilidad** — ¿qué pasa si duplicas $C_{H_2O}$? $\tau$ cambia de inmediato.
> 4. **Físicamente consistente** — a diferencia de tu primer intento, ahora $dQ/dt \propto \Delta$, no $Q \propto d\Delta/dt$.

---

## Ejemplo de Análisis de Sensibilidad con Tu Método

> [!question] ¿Qué pasa si duplicamos la masa de agua?
> 
> $C_{H_2O}' = 2 C_{H_2O} = 25080\ \text{J/K}$
> 
> Nuevo $\tau$:
> $$
> \tau' = \frac{C_{H_2O}' C_{Cu}}{K(C_{H_2O}' + C_{Cu})} = \frac{25080 \cdot 3494.4}{3.11 \cdot (25080 + 3494.4)} = \frac{87\,639\,552}{3.11 \cdot 28574.4} = \frac{87\,639\,552}{88\,866} \approx 986\ \text{s}
> $$
> 
> Nueva $T_f$:
> $$
> T_f' = \frac{3494.4 \cdot 200 + 25080 \cdot 20}{3494.4 + 25080} = \frac{698880 + 501600}{28574.4} = \frac{1\,200\,480}{28574.4} \approx 42.0\ \text{°C}
> $$
> 
> El agua tarda más en calentarse ($\tau$ mayor) pero alcanza una temperatura final más baja.

---

## Ejercicios Propuestos con Tu Método

> [!question] Ejercicio 1
> Usando tus expresiones simbólicas, encuentra cómo varía $\tau$ si $C_{Cu} \to \infty$ (cobre como reservorio infinito). ¿Tiene sentido físico?

> [!question] Ejercicio 2
> Si en lugar de agua fuera aceite con $c_{aceite} = 2000\ \text{J/(kg·K)}$ y misma masa, ¿cómo cambian $K$ (suponiendo que la física de contacto es la misma) y $\tau$?

> [!question] Ejercicio 3
> Deriva la expresión para $T_{Cu}(t)$ usando tu método fenomenológico. Verifica que satisface $T_{Cu}(0) = T_{Cu,0}$ y $T_{Cu}(\infty) = T_f$.

