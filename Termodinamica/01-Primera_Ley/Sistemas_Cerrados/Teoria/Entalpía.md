---
title: Entalpía
tags:
  - termodinámica
  - primera-ley
  - entalpia
  - funcion-estado
  - volumen-control
  - flujo-energia
draft: true
---

# Entalpía

> [!abstract] Resumen
> La entalpía $H$ es una función de estado que combina la energía interna $U$ con el trabajo de flujo $PV$. Su utilidad fundamental radica en que simplifica el análisis de volúmenes de control y procesos a presión constante, donde el cambio de entalpía equivale directamente al calor transferido. Es la propiedad termodinámica más utilizada en aplicaciones de flujo de fluidos, intercambiadores de calor y sistemas de potencia.

---

## Definición Formal

> [!definicion] Entalpía
> La entalpía $H$ de un sistema termodinámico se define como:
> 
> $$
> H = U + PV
> $$
> 
> donde:
> - $U$ = energía interna del sistema
> - $P$ = presión absoluta
> - $V$ = volumen del sistema

### Formas Específicas

| Forma | Notación | Definición | Unidades (SI) |
|-------|----------|------------|---------------|
| Total | $H$ | $H = U + PV$ | J |
| Específica | $h$ | $h = u + Pv$ | J/kg |
| Molar | $\bar{h}$ | $\bar{h} = \bar{u} + P\bar{v}$ | J/mol |

> [!info] Observación
> El término $PV$ representa el **trabajo de flujo** o **energía de flujo**, que es la energía necesaria para introducir o extraer masa de un [[Volumenes_de_Control|volumen de control]].

---

## Interpretación Física

> [!teoria] Significado Energético
> La entalpía puede interpretarse como:
> 
> 1. **Energía total transportada por un fluido en movimiento**: En flujo estacionario, la entalpía representa la suma de la energía interna más el trabajo necesario para desplazar el fluido.
> 
> 2. **Calor transferido en procesos isobáricos**: Para un sistema cerrado que experimenta un proceso a presión constante, el cambio de entalpía es igual al calor transferido:
>    $$
>    Q_P = \Delta H
>    $$
> 
> 3. **Propiedad de conveniencia**: Aunque $U$ es la energía "real" del sistema, $H$ surge naturalmente cuando se analizan sistemas que intercambian masa con su entorno.

> [!example] Ejemplo Físico
> Considere una caldera que produce vapor. El agua entra a cierta presión y temperatura, absorbe calor, y sale como vapor. La entalpía del vapor de salida es significativamente mayor que la del agua de entrada, y esa diferencia (multiplicada por el flujo másico) es precisamente el calor absorbido por el agua en la caldera.

### Rol en Sistemas Abiertos

> [!proposicion] Energía de Flujo
> Cuando una masa $m$ entra a un [[Volumenes_de_Control|volumen de control]], realiza un **trabajo de flujo** $Pv$ por unidad de masa para desplazar el fluido que ya estaba presente. La energía total transportada por la masa que fluye es:
> 
> $$
> E_{\text{transporte}} = u + Pv + \frac{v^2}{2} + gz = h + \frac{v^2}{2} + gz
> $$
> 
> donde:
> - $\frac{v^2}{2}$ = energía cinética específica
> - $gz$ = energía potencial específica

---

## Forma Diferencial

> [!teoria] Diferencial de Entalpía
> Partiendo de la definición $H = U + PV$ y diferenciando:
> 
> $$
> dH = dU + P\,dV + V\,dP
> $$

### Relación con $dU$

Sustituyendo la [[Primera Ley de la Termodinámica]] para un sistema cerrado en forma diferencial ($dU = \delta Q - \delta W$), y considerando trabajo de expansión $\delta W = P\,dV$ (para procesos cuasiestáticos):

$$
dH = \delta Q - P\,dV + P\,dV + V\,dP = \delta Q + V\,dP
$$

> [!warning] Limitación
> Esta expresión $dH = \delta Q + V\,dP$ es válida para procesos cuasiestáticos (reversibles) con trabajo solo de expansión.

---

## Relación Fundamental

> [!lema] Ecuación Fundamental de la Entalpía
> Combinando la Primera Ley ($dU = T\,dS - P\,dV$) con la definición de $H$:
> 
> $$
> dH = dU + P\,dV + V\,dP = (T\,dS - P\,dV) + P\,dV + V\,dP
> $$
> 
> Simplificando:
> 
> $$
> dH = T\,dS + V\,dP
> $$
> 
> Esta es la **relación fundamental de Gibbs para la entalpía**, válida para sistemas cerrados en equilibrio.

> [!info] Variables Naturales
> De la ecuación $dH = T\,dS + V\,dP$, se deduce que las **variables naturales** de la entalpía son la entropía $S$ y la presión $P$:
> 
> $$
> H = H(S, P)
> $$

---

## Relación con Energía Interna

> [!teoria] Transformación $H = U + PV$
> La relación entre entalpía y [[Energía Interna|energía interna]] se puede visualizar como:

| Aspecto | $U$ | Entalpía $H$ |
|---------|-----|--------------|
| **Qué mide** | Energía microscópica total | $U$ + trabajo de flujo |
| **Útil para** | Sistemas cerrados | Volúmenes de control |
| **Proceso característico** | Volumen constante | Presión constante |
| **Calor asociado** | $Q_V = \Delta U$ | $Q_P = \Delta H$ |

### Interpretación del Término $PV$

> [!demostracion] Trabajo de Flujo
> El término $PV$ (o $Pv$ en forma específica) tiene un significado físico claro en flujo estacionario:
> 
> Considere un pistón que empuja un fluido hacia un volumen de control. Para introducir un volumen $V$ de fluido a presión $P$, el pistón debe realizar un trabajo:
> 
> $$
> W_{\text{flujo}} = \int P \, dV = P \Delta V \quad \text{(presión constante)}
> $$
> 
> Por unidad de masa:
> 
> $$
> w_{\text{flujo}} = Pv
> $$
> 
> Este trabajo no modifica la energía interna del fluido, pero es necesario para el transporte. La suma $u + Pv$ representa la energía total que el fluido "entrega" al volumen de control al entrar.
> 
> $\square$

---

## Dependencia de Variables

### Caso General: $H = H(T, P)$

> [!teoria] Variables Prácticas
> Para la mayoría de las aplicaciones en ingeniería, la entalpía se expresa en función de la temperatura y la presión:
> 
> $$
> H = H(T, P)
> $$
> 
> Su diferencial total es:
> 
> $$
> dH = \left(\frac{\partial H}{\partial T}\right)_P dT + \left(\frac{\partial H}{\partial P}\right)_T dP
> $$

### Dependencia Alternativa: $H = H(T, v)$

> [!info] Formulación con Volumen
> También es posible expresar la entalpía en función de $T$ y $v$, aunque es menos común en la práctica:
> 
> $$
> dH = \left(\frac{\partial H}{\partial T}\right)_v dT + \left(\frac{\partial H}{\partial v}\right)_T dv
> $$

---

## Relación con la Temperatura

> [!teoria] Calor Específico a Presión Constante
> Por definición, el calor específico a presión constante es:
> 
> $$
> c_p = \left(\frac{\partial h}{\partial T}\right)_P
> $$

### Expresión Diferencial

Para una sustancia pura:

$$
dh = c_p(T, P) \, dT + \left(\frac{\partial h}{\partial P}\right)_T dP
$$

Para un gas ideal ($h$ independiente de $P$):

$$
dh = c_p(T) \, dT
$$

### Forma Integrada

> [!proposicion] Caso General
> $$
> \Delta h = \int_{T_1}^{T_2} c_p(T, P) \, dT + \int_{P_1}^{P_2} \left(\frac{\partial h}{\partial P}\right)_T dP
> $$

> [!example] Gas Ideal con $c_p$ Constante
> $$
> \Delta H = m \, c_p \, (T_2 - T_1)
> $$
> 
> o en forma molar:
> $$
> \Delta H = n \, \bar{c}_p \, (T_2 - T_1)
> $$

---

## Calores Específicos

### Definición de $c_p$

> [!definicion] Calor Específico a Presión Constante
> $$
> c_p = \left(\frac{\partial h}{\partial T}\right)_P
> $$
> 
> Representa la cantidad de calor necesaria para aumentar la temperatura de una unidad de masa en un grado, manteniendo la presión constante.

### Relación con $c_v$

> [!demostracion] Relación $c_p - c_v$
> 
> Partimos de la relación entre $h$ y $u$:
> 
> $$
> h = u + Pv
> $$
> 
> Diferenciando:
> 
> $$
> dh = du + P\,dv + v\,dP
> $$
> 
> Pero $du = c_v\,dT + \left(\frac{\partial u}{\partial v}\right)_T dv$, por lo tanto:
> 
> $$
> dh = c_v\,dT + \left[\left(\frac{\partial u}{\partial v}\right)_T + P\right] dv + v\,dP
> $$
> 
> Ahora, considerando $h = h(T, P)$ y usando relaciones de Maxwell, se obtiene la expresión general:
> 
> $$
> c_p - c_v = T v \frac{\beta^2}{\kappa_T}
> $$
> 
> donde:
> - $\beta = \frac{1}{v} \left(\frac{\partial v}{\partial T}\right)_P$ = coeficiente de expansión térmica
> - $\kappa_T = -\frac{1}{v} \left(\frac{\partial v}{\partial P}\right)_T$ = compresibilidad isoterma
> 
> Para un **gas ideal**:
> 
> $$
> \beta = \frac{1}{T}, \quad \kappa_T = \frac{1}{P}
> $$
> 
> Sustituyendo:
> 
> $$
> c_p - c_v = T v \frac{(1/T)^2}{1/P} = \frac{Pv}{T} = R
> $$
> 
> Es decir:
> 
> $$
> \bar{c}_p - \bar{c}_v = R \quad \text{(base molar)}
> $$
> 
> $\square$

### Interpretación Física

| Aspecto | $c_v$ | $c_p$ |
|---------|-------|-------|
| **Condición** | Volumen constante | Presión constante |
| **Trabajo** | $W = 0$ | $W > 0$ (expansión) |
| **Calor requerido** | Menor (solo aumenta $U$) | Mayor (aumenta $U$ + realiza trabajo) |
| **Relación** | $c_p > c_v$ (siempre) | $c_p - c_v = R$ (gas ideal) |

---

## Aplicación en Volúmenes de Control

### Flujo Estacionario

> [!teorema] Balance de Energía para Volumen de Control (Flujo Estacionario)
> 
> Para un [[Volumenes_de_Control|volumen de control]] en estado estacionario con una entrada y una salida:
> 
> $$
> \dot{Q} - \dot{W} = \dot{m} \left[ (h_2 - h_1) + \frac{V_2^2 - V_1^2}{2} + g(z_2 - z_1) \right]
> $$
> 
> donde:
> - $\dot{Q}$ = tasa de transferencia de calor
> - $\dot{W}$ = potencia (trabajo por unidad de tiempo)
> - $\dot{m}$ = flujo másico
> - $V$ = velocidad
> - $z$ = altura

> [!info] Energía de Flujo
> La entalpía $h$ aparece naturalmente en este balance porque incorpora el trabajo de flujo $Pv$. Sin este término, el balance sería incorrecto para sistemas con flujo de masa.

### Casos Particulares en Dispositivos

| Dispositivo | Condiciones | Balance Simplificado |
|-------------|-------------|---------------------|
| **Tobera / Difusor** | $\dot{Q}=0$, $\dot{W}=0$, $\Delta z \approx 0$ | $h_1 + \frac{V_1^2}{2} = h_2 + \frac{V_2^2}{2}$ |
| **Intercambiador de Calor** | $\dot{W}=0$, $\Delta z \approx 0$, $\Delta V \approx 0$ | $\dot{Q} = \dot{m} (h_2 - h_1)$ |
| **Turbina** | $\dot{Q} \approx 0$, $\Delta z \approx 0$, $\Delta V \approx 0$ | $\dot{W} = \dot{m} (h_1 - h_2)$ |
| **Bomba / Compresor** | $\dot{Q} \approx 0$, $\Delta z \approx 0$, $\Delta V \approx 0$ | $\dot{W} = \dot{m} (h_2 - h_1)$ |
| **Válvula de Estrangulamiento** | $\dot{Q}=0$, $\dot{W}=0$, $\Delta z \approx 0$, $\Delta V \approx 0$ | $h_2 = h_1$ (proceso isoentálpico) |

---

## Casos Importantes

### Proceso Isobárico (Presión Constante)

> [!teoria] Calor en Proceso Isobárico
> Para un sistema cerrado que experimenta un proceso a presión constante:
> 
> $$
> Q_P = \Delta U + P \Delta V = \Delta (U + PV) = \Delta H
> $$
> 
> Esto es válido tanto para procesos reversibles como irreversibles, siempre que la presión sea constante en los estados inicial y final.

### Proceso Adiabático Reversible en Volumen de Control

> [!teoria] Trabajo en Dispositivos Adiabáticos
> Para una turbina o compresor adiabático reversible (isoentrópico):
> 
> $$
> \dot{W} = \dot{m} (h_1 - h_2) \quad \text{(turbina)}
> $$
> 
> $$
> \dot{W} = \dot{m} (h_2 - h_1) \quad \text{(compresor)}
> $$

### Proceso de Estrangulamiento

> [!teoria] Proceso Isoentálpico
> En una válvula de estrangulamiento o un tapón poroso, el proceso es:
> - Adiabático ($Q = 0$)
> - Sin trabajo ($W = 0$)
> - Sin cambios significativos en energía cinética y potencial
> 
> Por lo tanto:
> 
> $$
> h_2 = h_1
> $$
> 
> Este es el principio detrás de la refrigeración por expansión y el efecto Joule-Thomson.

### Flujo en Dispositivos

> [!example] Tobera
> En una tobera, el fluido se acelera convirtiendo entalpía en energía cinética:
> 
> $$
> h_1 + \frac{V_1^2}{2} = h_2 + \frac{V_2^2}{2}
> $$
> 
> Si $V_1 \ll V_2$:
> 
> $$
> V_2 = \sqrt{2(h_1 - h_2)}
> $$

> [!example] Intercambiador de Calor
> En un intercambiador de calor, el calor transferido se calcula como:
> 
> $$
> \dot{Q} = \dot{m}_f (h_{f,2} - h_{f,1}) = \dot{m}_c (h_{c,1} - h_{c,2})
> $$
> 
> donde los subíndices $f$ y $c$ indican fluido caliente y frío respectivamente.

---

## Modelos Útiles

### Gas Ideal

> [!teoria] Propiedades de la Entalpía en Gas Ideal
> Para un gas ideal:
> 
> 1. **Dependencia solo de temperatura**:
>    $$
>    h = h(T) \quad \text{independiente de } P
>    $$
> 
> 2. **Relación con energía interna**:
>    $$
>    h = u + RT \quad \text{(base molar)}
>    $$
> 
> 3. **Calor específico**:
>    $$
>    c_p(T) = \frac{dh}{dT}
>    $$
> 
> 4. **Modelo de calor específico constante** (aproximación):
>    $$
>    \Delta h = c_p (T_2 - T_1)
>    $$

### Sustancias Reales

> [!teoria] Uso de Tablas
> Para sustancias reales como agua, refrigerantes y combustibles, se utilizan:
> 
> 1. **Tablas de propiedades**:
>    - Tablas de vapor sobrecalentado
>    - Tablas de líquido comprimido
>    - Tablas de saturación ($T$ o $P$)
> 
> 2. **Diagramas termodinámicos**:
>    - Diagrama $T$-$s$
>    - Diagrama $h$-$s$ (Diagrama de Mollier)
>    - Diagrama $P$-$h$ (para ciclos de refrigeración)

> [!example] Uso de Tablas para Agua
> Para determinar $h$ del agua a $T = 200^\circ\text{C}$, $P = 1.5\ \text{MPa}$:
> 1. Verificar si es vapor sobrecalentado, líquido comprimido o mezcla saturada
> 2. Usar la tabla correspondiente
> 3. Interpolar si es necesario

---

## Demostraciones Clave

### 1. Relación $dH = T\,dS + V\,dP$

> [!demostracion] Demostración
> 
> Partimos de la definición:
> $$
> H = U + PV
> $$
> 
> Diferenciando:
> $$
> dH = dU + P\,dV + V\,dP
> $$
> 
> De la Primera Ley en forma diferencial para un proceso reversible:
> $$
> dU = T\,dS - P\,dV
> $$
> 
> Sustituyendo:
> $$
> dH = (T\,dS - P\,dV) + P\,dV + V\,dP
> $$
> 
> Simplificando:
> $$
> dH = T\,dS + V\,dP
> $$
> 
> $\square$

### 2. Relación entre $c_p$ y $c_v$ (demostración alternativa con entalpía)

> [!demostracion] Demostración usando $h(T,P)$
> 
> Para una sustancia pura:
> 
> Por definición:
> $$
> c_p = \left(\frac{\partial h}{\partial T}\right)_P
> $$
> 
> Como $h = u + Pv$:
> $$
> c_p = \left(\frac{\partial u}{\partial T}\right)_P + P \left(\frac{\partial v}{\partial T}\right)_P
> $$
> 
> Pero $\left(\frac{\partial u}{\partial T}\right)_P = c_v + \left(\frac{\partial u}{\partial v}\right)_T \left(\frac{\partial v}{\partial T}\right)_P$
> 
> Usando relaciones termodinámicas ($\left(\frac{\partial u}{\partial v}\right)_T = T \left(\frac{\partial P}{\partial T}\right)_v - P$):
> 
> $$
> c_p = c_v + \left[T \left(\frac{\partial P}{\partial T}\right)_v - P\right] \left(\frac{\partial v}{\partial T}\right)_P + P \left(\frac{\partial v}{\partial T}\right)_P
> $$
> 
> Simplificando:
> 
> $$
> c_p - c_v = T \left(\frac{\partial P}{\partial T}\right)_v \left(\frac{\partial v}{\partial T}\right)_P
> $$
> 
> Usando la identidad cíclica $\left(\frac{\partial P}{\partial T}\right)_v \left(\frac{\partial T}{\partial v}\right)_P \left(\frac{\partial v}{\partial P}\right)_T = -1$:
> 
> $$
> c_p - c_v = -T \left(\frac{\partial v}{\partial T}\right)_P^2 \left(\frac{\partial P}{\partial v}\right)_T
> $$
> 
> Reconociendo $\beta = \frac{1}{v} \left(\frac{\partial v}{\partial T}\right)_P$ y $\kappa_T = -\frac{1}{v} \left(\frac{\partial v}{\partial P}\right)_T$:
> 
> $$
> c_p - c_v = T v \frac{\beta^2}{\kappa_T}
> $$
> 
> $\square$

### 3. Demostración de $Q_P = \Delta H$ para Proceso Isobárico

> [!demostracion] Demostración
> 
> Para un sistema cerrado:
> 
> De la Primera Ley:
> $$
> Q - W = \Delta U
> $$
> 
> Si el proceso es a presión constante y solo hay trabajo de expansión ($W = P \Delta V$):
> 
> $$
> Q_P - P \Delta V = \Delta U
> $$
> 
> Reordenando:
> $$
> Q_P = \Delta U + P \Delta V
> $$
> 
> Como $P$ es constante, $P \Delta V = \Delta (PV)$, entonces:
> $$
> Q_P = \Delta (U + PV) = \Delta H
> $$
> 
> $\square$

---

## Tabla de Correspondencias

| Concepto | Notación | Unidades (SI) |
|----------|----------|---------------|
| Entalpía (total) | $H$ | J |
| Entalpía específica | $h = H/m$ | J/kg |
| Entalpía molar | $\bar{h} = H/n$ | J/mol |
| Calor específico a presión constante | $c_p$ | J/(kg·K) |
| Calor específico molar a presión constante | $\bar{c}_p$ | J/(mol·K) |
| Proceso isobárico | $Q_P = \Delta H$ | J |
| Proceso isoentálpico | $\Delta h = 0$ | J/kg |

---

## Ejercicios Propuestos

> [!question] Ejercicio 1
> Un sistema cerrado contiene 3 kg de agua líquida a $20^\circ\text{C}$ y se calienta a presión constante de 1 atm hasta $80^\circ\text{C}$. Si $c_p = 4.18\ \text{kJ/kg·K}$, determine:
> a) El cambio de entalpía
> b) El calor transferido

<details>
<summary>Solución</summary>

a) $\Delta H = m c_p (T_2 - T_1) = 3 \cdot 4.18 \cdot (80 - 20) = 752.4\ \text{kJ}$
b) Proceso isobárico: $Q_P = \Delta H = 752.4\ \text{kJ}$
</details>

> [!question] Ejercicio 2
> Una turbina de vapor opera en flujo estacionario. El vapor entra a $h_1 = 3200\ \text{kJ/kg}$ y sale a $h_2 = 2500\ \text{kJ/kg}$. Si el flujo másico es $\dot{m} = 5\ \text{kg/s}$ y las pérdidas de calor son despreciables, calcule la potencia desarrollada.

<details>
<summary>Solución</summary>

Para una turbina adiabática con despreciables cambios de energía cinética y potencial:
$\dot{W} = \dot{m} (h_1 - h_2) = 5 \cdot (3200 - 2500) = 3500\ \text{kW} = 3.5\ \text{MW}$
</details>

> [!question] Ejercicio 3
> Un gas ideal ($c_p = 1.005\ \text{kJ/kg·K}$, $R = 0.287\ \text{kJ/kg·K}$) se calienta desde $300\ \text{K}$ hasta $600\ \text{K}$ a presión constante.
> a) Calcular $\Delta h$
> b) Calcular $\Delta u$
> c) Verificar que $\Delta h - \Delta u = R \Delta T$

<details>
<summary>Solución</summary>

a) $\Delta h = c_p (T_2 - T_1) = 1.005 \cdot 300 = 301.5\ \text{kJ/kg}$
b) $\Delta u = c_v (T_2 - T_1)$, con $c_v = c_p - R = 1.005 - 0.287 = 0.718\ \text{kJ/kg·K}$
$\Delta u = 0.718 \cdot 300 = 215.4\ \text{kJ/kg}$
c) $\Delta h - \Delta u = 301.5 - 215.4 = 86.1\ \text{kJ/kg}$
$R \Delta T = 0.287 \cdot 300 = 86.1\ \text{kJ/kg}$ ✓
</details>

> [!question] Ejercicio 4
> Un proceso de estrangulamiento reduce la presión de un refrigerante de 1.2 MPa a 0.3 MPa. Si el refrigerante entra como líquido saturado, determine la calidad a la salida. (Use las tablas de propiedades del refrigerante, donde $h_f(1.2\ \text{MPa}) = 100\ \text{kJ/kg}$, $h_f(0.3\ \text{MPa}) = 50\ \text{kJ/kg}$, $h_{fg}(0.3\ \text{MPa}) = 200\ \text{kJ/kg}$)

<details>
<summary>Solución</summary>

Proceso isoentálpico: $h_2 = h_1 = 100\ \text{kJ/kg}$
A la salida (0.3 MPa): $h_f = 50$, $h_g = h_f + h_{fg} = 250$
$x = \frac{h_2 - h_f}{h_{fg}} = \frac{100 - 50}{200} = 0.25\ (25\%)$
</details>

> [!question] Ejercicio 5
> Derive la expresión $c_p - c_v = R$ para un gas ideal a partir de la definición de entalpía.

<details>
<summary>Solución</summary>

Para gas ideal: $h = u + RT$ (base molar)
Derivando respecto a $T$:
$\frac{dh}{dT} = \frac{du}{dT} + R$
Pero $\bar{c}_p = \frac{dh}{dT}$ y $\bar{c}_v = \frac{du}{dT}$, por lo tanto:
$\bar{c}_p = \bar{c}_v + R$ ⇒ $\bar{c}_p - \bar{c}_v = R$
</details>

---

## Notas Relacionadas

- [[Energía Interna]]
- [[Primera Ley de la Termodinámica]]
- [[Calores_Especificos_Gases_Ideales]]
- [[Volumenes_de_Control]]
- [[Flujo_Estacionario_SSP]]
- [[Proceso Isobarico]]
- [[Proceso_Estrangulacion]]
- [[Gases Ideales]]
- [[Tablas Termodinámicas]]
- [[Entropía]]
- [[Sistemas Cerrados]]
- [[Diagramas T-s h-s P-h]]