---
title: "Entropía $S$"
tags:
  - termodinamica
  - potenciales_termodinamicos
  - segunda_ley
draft: false
aliases:
  - entropy
  - S
---

# Entropía $S$

> [!definicion]
> Función de estado extensiva. Mide la dispersión de energía o el número de microestados compatibles con un macroestado.
> 
> Segunda ley: $dS \geq \delta Q/T$ para sistemas cerrados.
> 
> Variables naturales: $S(U, V)$ para sistema simple compresible.

## Entropía específica y molar

> [!proposicion]
> **Entropía específica** (por unidad de masa):
> $$
> s = \frac{S}{m} \quad [\text{kJ/kg·K}]
> $$
> 
> **Entropía molar** (por unidad de mol):
> $$
> \bar{s} = \frac{S}{n} \quad [\text{kJ/mol·K}]
> $$

## Ecuación fundamental

> [!teorema]
> De $dU = TdS - PdV$, despejando:
> $$
> dS = \frac{dU}{T} + \frac{P}{T}dV
> $$
> 
> Variables naturales: $S(U, V)$
> 
> Derivadas:
> $$
> \frac{1}{T} = \left(\frac{\partial S}{\partial U}\right)_V, \quad \frac{P}{T} = \left(\frac{\partial S}{\partial V}\right)_U
> $$

## Desigualdad de Clausius

> [!teorema]
> Para cualquier ciclo termodinámico:
> $$
> \oint \frac{\delta Q}{T} \leq 0
> $$
> 
> La igualdad se cumple para ciclos **reversibles**.
> 
> Para un proceso irreversible entre dos estados:
> $$
> \Delta S = S_2 - S_1 \geq \int_1^2 \frac{\delta Q}{T}
> $$

## Generación de entropía

> [!definicion]
> Para un [[Sistemas Cerrados]]:
> $$
> \Delta S = \int_1^2 \frac{\delta Q}{T} + S_{gen}
> $$
> donde $S_{gen} \geq 0$ (cero para proceso reversible, positivo para irreversible)
> 
> Para [[Volumenes de Control]] en [[Flujo Estacionario]]:
> $$
> \dot{S}_{gen} = \sum_{out} \dot{m}_e s_e - \sum_{in} \dot{m}_i s_i - \sum \frac{\dot{Q}_k}{T_k} \geq 0
> $$

## Relaciones con otras propiedades

> [!info]
> **Primera ecuación $TdS$** (desde $dU$):
> $$
> TdS = dU + PdV
> $$
> 
> **Segunda ecuación $TdS$** (desde $dH$):
> $$
> TdS = dH - VdP
> $$
> 
> **Con [[Energia Interna]]**:
> $$
> \left(\frac{\partial S}{\partial U}\right)_V = \frac{1}{T}
> $$
> 
> **Con [[Entalpia]]**:
> $$
> \left(\frac{\partial S}{\partial P}\right)_H = -\frac{V}{T} \quad \text{(coeficiente de Joule-Thomson relacionado)}
> $$
> 
> **Con [[Presion]] y [[Temperatura]]**:
> $$
> \left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial P}{\partial T}\right)_V \quad \text{(relación de Maxwell desde $dF$)}
> $$

## Derivadas útiles

> [!proposicion]
> **Variación con $T$ y $v$**:
> $$
> ds = \frac{c_v}{T}dT + \left(\frac{\partial P}{\partial T}\right)_v dv
> $$
> 
> **Variación con $T$ y $P$**:
> $$
> ds = \frac{c_p}{T}dT - \left(\frac{\partial v}{\partial T}\right)_P dP
> $$
> 
> **Relación de [[Maxwell]]** (desde $dS$ expresada con $T$,$v$):
> $$
> \left(\frac{\partial c_v}{\partial v}\right)_T = T\left(\frac{\partial^2 P}{\partial T^2}\right)_v
> $$

## Casos particulares

> [!proposicion]
> **[[Gas Ideal]]**:
> 
> Usando $Pv = RT$:
> - De $ds = c_v dT/T + R dv/v$:
> $$
> s_2 - s_1 = \int_{T_1}^{T_2} c_v(T)\frac{dT}{T} + R \ln\frac{v_2}{v_1}
> $$
> - De $ds = c_p dT/T - R dP/P$:
> $$
> s_2 - s_1 = \int_{T_1}^{T_2} c_p(T)\frac{dT}{T} - R \ln\frac{P_2}{P_1}
> $$
> 
> Para $c_p$, $c_v$ constantes:
> $$
> s_2 - s_1 = c_v \ln\frac{T_2}{T_1} + R \ln\frac{v_2}{v_1} = c_p \ln\frac{T_2}{T_1} - R \ln\frac{P_2}{P_1}
> $$

> [!proposicion]
> **Sustancia incompresible** ($dv = 0$, $c = c_v = c_p$):
> $$
> ds = c(T)\frac{dT}{T}
> $$
> 
> Para $c$ constante:
> $$
> s_2 - s_1 = c \ln\frac{T_2}{T_1}
> $$

> [!proposicion]
> **Mezcla líquido-vapor** (región de saturación):
> $$
> s = s_f + x\,s_{fg}
> $$
> - $x$: [[Calidad]]
> - $s_{fg} = s_g - s_f$

## Procesos isentrópicos

> [!definicion]
> Proceso **isentrópico**: $S_2 = S_1$ (reversible y adiabático)
> 
> Para [[Gas Ideal]] con $c_p$, $c_v$ constantes:
> - $T v^{\gamma-1} = \text{constante}$, con $\gamma = c_p/c_v$
> - $T P^{(1-\gamma)/\gamma} = \text{constante}$
> - $P v^{\gamma} = \text{constante}$

> [!ejemplo]
> **Compresor adiabático reversible de aire** (gas ideal)
> 
> Datos: $T_1=300K$, $P_1=100kPa$, $P_2=800kPa$, $\gamma=1.4$, $c_p=1.005 kJ/kg·K$
> 
> Proceso isentrópico:
> $$
> T_2 = T_1 \left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma} = 300 \times 8^{0.4/1.4} = 300 \times 8^{0.2857} = 300 \times 1.811 = 543.3K
> $$
> 
> Trabajo de compresión (despreciando $C$ y $z$):
> $$
> W_{entra} = \dot{m}(h_2 - h_1) = \dot{m} c_p (T_2 - T_1)
> $$
> Para $\dot{m}=1 kg/s$:
> $$
> W_{entra} = 1 \times 1.005 \times (543.3 - 300) = 244.5 kW
> $$

> [!ejemplo]
> **Expansión libre de Joule** (irreversible)
> 
> Gas ideal expande al vacío, $T$ constante ($U$ constante), $V_2 = 2V_1$
> 
> Como $T$ constante y gas ideal: $\Delta s = R \ln(V_2/V_1) = R \ln 2$
> 
> No hay transferencia de calor: $\int \delta Q/T = 0$
> 
> Generación: $S_{gen} = \Delta S = mR\ln 2 > 0$

## Tercera ley

> [!teorema]
> **Postulado de Nernst**:
> $$
> \lim_{T \to 0} S(T) = 0
> $$
> 
> Para un cristal perfecto a $T=0K$, la entropía es cero (solo un microestado).
> 
> Consecuencia: Los calores específicos tienden a cero cuando $T \to 0$.

> [!warning]
> **Precauciones**:
> - La entropía **absoluta** existe (tercera ley), a diferencia de $U$ y $H$.
> - Proceso isentrópico $\neq$ reversible adiabático si hay irreversibilidades internas (ej. disipación viscosa)
> - Para [[Volumenes de Control]] en [[Flujo Estacionario]]: $S_{gen} \geq 0$ se aplica al **volumen de control**, no a la masa que fluye

> [!info]
> **Convención de notación**:
> - $s$: entropía específica [kJ/kg·K]
> - $S_{gen}$: entropía generada [kJ/K]
> - $\dot{S}_{gen}$: tasa de generación de entropía [kW/K]