---
title: "Balance de Masa (Volumen de Control)"
order: 1
tags:
  - termodinamica
  - conservacion
  - masa
  - volumen_de_control
draft: false
aliases:
  - continuidad
  - conservation of mass
  - balance de masa VC
  - ecuacion de continuidad
---

# Balance de Masa — Volumen de Control

> [!definicion]
> El **balance de masa** para un [[Volumenes de Control/index | volumen de control]] establece que la tasa de cambio de masa en el VC es igual a la diferencia entre flujos másicos de entrada y salida:
> $$\boxed{\frac{dm_{VC}}{dt} = \sum_i \dot{m}_i - \sum_e \dot{m}_e,}$$
> donde el flujo másico a través de una sección de área $A$ con velocidad normal $V$ y densidad $\rho$ es:
> $$\dot{m} = \rho V A \quad [\text{kg/s}].$$
>
> A diferencia de los sistemas cerrados (donde la masa es constante por definición), en un VC la masa puede acumularse o reducirse: un tanque que se llena tiene $dm_{VC}/dt > 0$; uno que se vacía tiene $dm_{VC}/dt < 0$.

---

## Flujo másico: de la densidad a la masa por segundo

> [!teoria]
> El flujo másico $\dot{m}$ surge de contar cuántas moléculas cruzan la sección de control por unidad de tiempo. Si la densidad es $\rho$ [kg/m³] y la velocidad normal a la sección es $V$ [m/s], entonces en 1 segundo cruzan todas las moléculas dentro del cilindro de base $A$ y longitud $V\cdot 1$:
> $$\dot{m} = \rho \cdot (V \cdot A) = \rho V A.$$
> Si el perfil de velocidad no es uniforme, se integra: $\dot{m} = \int_A \rho\,V_n\,dA$ (donde $V_n$ es la componente normal al área). En la mayoría de los análisis termodinámicos se usa el **valor promedio**: $\dot{m} = \rho\,V_{\rm prom}\,A$, lo que es exacto para flujo uniforme.
>
> Forma equivalente con volumen específico $v = 1/\rho$:
> $$\dot{m} = \frac{V\,A}{v} \qquad [\text{kg/s}].$$

![[balance_masa_VC.svg|420]]
*Volumen de control con una entrada (sección 1, área $A_1$, velocidad $V_1$, densidad $\rho_1$) y una salida (sección 2). Si el VC es en régimen no estacionario, la diferencia de flujos másicos acumula o reduce masa dentro del VC.*

---

## Régimen estacionario: la ecuación de continuidad

> [!proposicion]
> En **régimen estacionario** ($dm_{VC}/dt = 0$, las propiedades en cada punto del VC no varían con el tiempo), el balance de masa se convierte en la **ecuación de continuidad**:
> $$\sum_i \dot{m}_i = \sum_e \dot{m}_e.$$
> Para una sola entrada y una sola salida:
> $$\dot{m}_1 = \dot{m}_2 \implies \rho_1\,V_1\,A_1 = \rho_2\,V_2\,A_2.$$
>
> **Interpretación física:** si el fluido se comprime ($\rho_2 > \rho_1$) al pasar de 1 a 2, la velocidad y/o el área deben disminuir para que la misma masa por segundo cruce ambas secciones.

---

## Para fluido incompresible: relación de velocidades y áreas

> [!proposicion]
> Para un fluido incompresible ($\rho = \text{cte}$, como el agua a baja presión):
> $$V_1\,A_1 = V_2\,A_2 \implies \frac{V_2}{V_1} = \frac{A_1}{A_2}.$$
> Al reducir el área (sección más estrecha), la velocidad aumenta proporcionalmente. Este es el principio de una boquilla o tobera: controlar la velocidad del chorro ajustando el área de salida.

---

## Régimen no estacionario: llenado y vaciado de tanques

> [!teoria]
> Para procesos transitorios (llenado de un recipiente presurizado, vaciado de un tanque de vapor), la forma integral es:
> $$m_2 - m_1 = \sum_i m_i - \sum_e m_e,$$
> donde $m_i$ y $m_e$ son las masas totales que cruzaron la frontera durante el proceso. Esta forma discreta se obtiene integrando el balance diferencial en el tiempo del proceso.

---

## Ejemplo: tobera convergente con vapor de agua

> [!ejemplo]
> **Tobera adiabática en régimen estacionario.** Vapor entra ($\dot{m} = 5\,\text{kg/s}$, $v_1 = 0.1\,\text{m}^3/\text{kg}$, $V_1 = 50\,\text{m/s}$) y sale ($v_2 = 0.5\,\text{m}^3/\text{kg}$, $V_2 = 300\,\text{m/s}$). Calcular las áreas de entrada y salida.
>
> **Paso 1 — Aplicar la ecuación de continuidad en régimen estacionario:** $\dot{m}_1 = \dot{m}_2 = \dot{m} = 5\,\text{kg/s}$.
>
> **Paso 2 — Despejar el área de entrada** (de $\dot{m} = VA/v$):
> $$A_1 = \frac{\dot{m}\,v_1}{V_1} = \frac{5 \times 0.1}{50} = \frac{0.5}{50} = 0.01\,\text{m}^2 = 100\,\text{cm}^2.$$
>
> **Paso 3 — Despejar el área de salida:**
> $$A_2 = \frac{\dot{m}\,v_2}{V_2} = \frac{5 \times 0.5}{300} = \frac{2.5}{300} = 8.33 \times 10^{-3}\,\text{m}^2 = 83.3\,\text{cm}^2.$$
>
> **Paso 4 — Verificar e interpretar.** La sección se estrecha de 100 a 83.3 cm² ($A_2 < A_1$) aunque el volumen específico creció 5 veces. El estrechamiento aceleró el fluido pero no tanto como si el fluido fuera incompresible (donde sería $A_2/A_1 = V_1/V_2 = 1/6$). La compresibilidad del vapor atenúa el efecto. $\blacksquare$

---

## Relación con otras notas

> [!info]
> - [[Balance de Energia VC]] — usa el mismo $\dot{m}$ para ponderar la entalpía de flujo.
> - [[Balance de Entropia VC]] — mismo $\dot{m}$ para ponderar la entropía transportada.
> - [[Sistemas/Dispositivos Flujo/index | Dispositivos de Flujo]] — toberas, turbinas, compresores: todos aplican este balance como primer paso.

> [!info]
> **Unidades y notación:**
> - $\dot{m}$ [kg/s]: flujo másico; $m$ [kg]: masa total; $V$ [m/s]: velocidad; $A$ [m²]: área.
> - El volumen de control puede tener múltiples entradas ($i$) y salidas ($e$).

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, §6.1; Çengel & Boles, *Termodinámica*, §5-1; Moran & Shapiro, *Fundamentals of Engineering Thermodynamics*, §4.1.
