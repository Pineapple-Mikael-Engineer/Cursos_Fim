---
title: "Compresión de Vapor"
order: 1
tags:
  - termodinamica
  - ciclos
  - refrigeracion
  - compresion_vapor
  - R134a
draft: false
aliases:
  - Compresión de Vapor
  - vapor-compression refrigeration
  - ciclo de refrigeración estándar
  - VCR cycle
---

# Ciclo de Compresión de Vapor

> [!definicion]
> El **ciclo de compresión de vapor** (VCR, *vapor-compression refrigeration*) es el ciclo estándar de los refrigeradores domésticos, acondicionadores de aire y chillers industriales. Es esencialmente el **ciclo Rankine invertido**: en lugar de producir trabajo a partir de calor, consume trabajo para transferir calor de frío a caliente.
>
> El fluido de trabajo es un **refrigerante** (R-134a, R-410A, R-32, CO₂, amoniaco, etc.) seleccionado por su temperatura de ebullición a baja presión (dentro del evaporador), su estabilidad química y bajo impacto ambiental. El R-134a (tetrafluoroetano) es el refrigerante de referencia para los cálculos de este curso.
>
> *Cuatro procesos y dispositivos:*
> - **1→2:** Compresión isentrópica (vapor saturado o sobrecalentado comprimido a $P_H$).
> - **2→3:** Rechazo de calor isobárico en el condensador (a $P_H$, hasta líquido saturado).
> - **3→4:** Expansión irreversible en la válvula de expansión (proceso isoenthálpico, $h_4 = h_3$).
> - **4→1:** Absorción de calor isobárica en el evaporador (a $P_L$, hasta vapor saturado o sobrecalentado).

![[VCR_esquema_dispositivos.svg|480]]
*Ciclo de compresión de vapor estándar. El compresor eleva la presión del vapor (1→2). El condensador cede calor al ambiente (2→3). La válvula expande irreversiblemente el líquido (3→4, isoenthálpica). El evaporador absorbe calor del espacio frío (4→1).*

![[VCR_diagrama_Ph.svg|440]]
*Diagrama $P$-$h$ del ciclo VCR. El eje horizontal es la entalpía $h$ y el vertical la presión $P$ (escala logarítmica). El ciclo forma un bucle: la válvula es una línea vertical descendente (isoenthálpica) y el evaporador una línea horizontal a $P_L$.*

---

## Nomenclatura de estados

| Estado | Descripción | Región |
|:---:|:---|:---|
| 1 | Salida del evaporador = entrada compresor | Vapor saturado ($x=1$) o sobrecalentado |
| 2 | Salida del compresor = entrada condensador | Vapor sobrecalentado ($P_H$) |
| 3 | Salida del condensador = entrada válvula | Líquido saturado ($x=0$, $P_H$) |
| 4 | Salida de la válvula = entrada evaporador | Mezcla líquido-vapor ($P_L$) |

---

## Válvula de expansión: proceso isoenthálpico

> [!proposicion]
> La válvula de expansión (o tubo capilar) es un dispositivo de estrangulación: no hay trabajo de eje, se considera adiabática y sin cambios de EC ni EP. Primera ley:
> $$
> h_3 = h_4 \quad (\text{proceso isoenthálpico}).
> $$
>
> *¿Por qué produce mezcla?* El líquido a $P_H$ y $T_3 = T_{\rm sat}(P_H)$ entra a la válvula con entalpía $h_3 = h_f(P_H)$. Al salir a $P_L$ con la misma entalpía, se encuentra a $h_4 > h_f(P_L)$: parte del líquido se ha vaporizado para enfriarse hasta $T_{\rm sat}(P_L)$. Esta vaporización repentina (flash) es el efecto de enfriamiento. La calidad a la salida:
> $$
> x_4 = \frac{h_4 - h_f(P_L)}{h_{fg}(P_L)} = \frac{h_3 - h_f(P_L)}{h_{fg}(P_L)}.
> $$

---

## Balances de energía (base 1 kg)

> [!proposicion]
> **Trabajo del compresor** (proceso 1→2, isentrópico ideal):
> $$
> w_C = h_2 - h_1 \quad [\mathrm{kJ/kg}].
> $$
>
> **Calor cedido en el condensador** (proceso 2→3, isobárico):
> $$
> q_H = h_2 - h_3 \quad [\mathrm{kJ/kg}].
> $$
>
> **Efecto refrigerante** (calor absorbido en el evaporador, proceso 4→1):
> $$
> q_L = h_1 - h_4 = h_1 - h_3 \quad [\mathrm{kJ/kg}].
> $$
>
> **Verificación (primera ley del ciclo):**
> $$
> q_H = q_L + w_C \iff (h_2-h_3) = (h_1-h_3) + (h_2-h_1). \checkmark
> $$
>
> **Coeficientes de desempeño:**
> $$
> \text{COP}_R = \frac{q_L}{w_C} = \frac{h_1 - h_3}{h_2 - h_1}, \qquad \text{COP}_{HP} = \frac{q_H}{w_C} = \frac{h_2 - h_3}{h_2 - h_1}.
> $$

---

## Ejemplo: refrigerador con R-134a

> [!ejemplo]
> Ciclo VCR con refrigerante R-134a:
> - Temperatura del evaporador: $T_L = -20°\mathrm{C}$ → $P_L = P_{\rm sat}(-20°\mathrm{C})$.
> - Temperatura del condensador: $T_H = 40°\mathrm{C}$ → $P_H = P_{\rm sat}(40°\mathrm{C})$.
> - Estado 1: vapor saturado a $T_L$ ($x_1 = 1$).
> - Compresor ideal ($\eta_C = 1$): $s_2 = s_1$.
> - Estado 3: líquido saturado a $T_H$ ($x_3 = 0$).
> - Capacidad frigorífica: $\dot{Q}_L = 10\,\mathrm{kW}$.
>
> Determinar: (a) entalpías en los 4 estados; (b) $\text{COP}_R$ y $\text{COP}_{HP}$; (c) caudal másico $\dot{m}$; (d) potencia del compresor $\dot{W}_C$.

> [!solucion]
> **Propiedades del R-134a** (tablas de saturación, **referencia IIR**: $h_f=200\,\mathrm{kJ/kg}$, $s_f=1.00\,\mathrm{kJ/(kg\cdot K)}$ para líquido saturado a $0°\mathrm{C}$). Se usa una sola convención en los cuatro estados.
>
> A $T_L=-20°\mathrm{C}$ ($P_L=132.68\,\mathrm{kPa}$): $h_f=173.74$, $h_g=386.55$, $h_{fg}=212.81\,\mathrm{kJ/kg}$; $s_g=1.7414\,\mathrm{kJ/(kg\cdot K)}$. A $T_H=40°\mathrm{C}$ ($P_H=1016.6\,\mathrm{kPa}$): $h_f=256.44\,\mathrm{kJ/kg}$.
>
> **Estado 1** — vapor saturado a $T_L=-20°\mathrm{C}$: $h_1 = 386.55\,\mathrm{kJ/kg}$, $s_1 = 1.7414\,\mathrm{kJ/(kg\cdot K)}$.
>
> **Estado 3** — líquido saturado a $T_H=40°\mathrm{C}$: $h_3 = 256.44\,\mathrm{kJ/kg}$.
>
> **Estado 2** — compresión isentrópica a $P_H=1016.6\,\mathrm{kPa}$ con $s_2=s_1=1.7414\,\mathrm{kJ/(kg\cdot K)}$. Interpolando en la tabla de vapor sobrecalentado de R-134a (misma referencia IIR) a esa presión y entropía:
> $$T_2\approx56.6°\mathrm{C}, \qquad h_2 = 428.35\,\mathrm{kJ/kg}.$$
>
> **Estado 4** — válvula isoentálpica, $h_4=h_3=256.44\,\mathrm{kJ/kg}$. Como $h_f(P_L)=173.74 < h_4 < h_g(P_L)=386.55$, la salida es bifásica con calidad
> $$x_4=\frac{h_4-h_f(-20°\mathrm{C})}{h_{fg}(-20°\mathrm{C})}=\frac{256.44-173.74}{212.81}=0.389.$$
>
> Resumen de estados:
>
> | Estado | $T$ [°C] | $P$ [kPa] | $h$ [kJ/kg] | $s$ [kJ/(kg·K)] |
> |:---:|:---:|:---:|:---:|:---:|
> | 1 | $-20$ | 132.68 | 386.55 | 1.7414 |
> | 2 | ≈56.6 | 1016.6 | 428.35 | 1.7414 |
> | 3 | 40 | 1016.6 | 256.44 | — |
> | 4 | $-20$ | 132.68 | 256.44 | — |
>
> **(a) Entalpías:** $h_1 = 386.55\,\mathrm{kJ/kg}$, $h_2 = 428.35\,\mathrm{kJ/kg}$, $h_3 = h_4 = 256.44\,\mathrm{kJ/kg}$.
>
> **(b) Coeficientes de desempeño:**
>
> $w_C = h_2 - h_1 = 428.35 - 386.55 = 41.80\,\mathrm{kJ/kg}$.
>
> $q_L = h_1 - h_4 = 386.55 - 256.44 = 130.11\,\mathrm{kJ/kg}$.
>
> $q_H = h_2 - h_3 = 428.35 - 256.44 = 171.91\,\mathrm{kJ/kg}$.
>
> $$\text{COP}_R = \frac{q_L}{w_C} = \frac{130.11}{41.80} = 3.11.$$
>
> $$\text{COP}_{HP} = \frac{q_H}{w_C} = \frac{171.91}{41.80} = 4.11 = \text{COP}_R + 1. \checkmark$$
>
> **Límite de Carnot:** $\text{COP}_{R,\rm Carnot} = T_L/(T_H-T_L) = 253.15/(313.15-253.15) = 253.15/60 = 4.22$ (usando temperaturas absolutas).
>
> La eficiencia relativa del ciclo real: $\text{COP}_R/\text{COP}_{R,\rm Carnot} = 3.11/4.22 = 73.7\%$.
>
> **(c) Caudal másico:**
> $$\dot{m} = \frac{\dot{Q}_L}{q_L} = \frac{10\,\mathrm{kW}}{130.11\,\mathrm{kJ/kg}} = 0.0769\,\mathrm{kg/s} = 4.61\,\mathrm{kg/min}.$$
>
> **(d) Potencia del compresor:**
> $$\dot{W}_C = \dot{m}\,w_C = 0.0769 \times 41.80 = 3.21\,\mathrm{kW}.$$
>
> Verificación: $\dot{Q}_H = \dot{m}\,q_H = 0.0769 \times 171.91 = 13.22\,\mathrm{kW} = \dot{Q}_L + \dot{W}_C = 10 + 3.22 = 13.22\,\mathrm{kW}$. ✓
>
> $$\boxed{\text{COP}_R = 3.11,\quad \dot{W}_C = 3.21\,\mathrm{kW}.}$$ $\blacksquare$

> [!info]
> El ciclo de compresión de vapor real se diferencia del ideal en: (1) el compresor es irreversible ($\eta_C < 1$), aumentando $h_2$ y reduciendo el COP; (2) el estado de entrada al compresor puede ser vapor sobrecalentado (*superheat*) para evitar líquido en el compresor; (3) puede haber subenfriamiento (*subcooling*) en la salida del condensador, reduciendo $h_3$ y aumentando el efecto refrigerante.

> [!referencia]
> Borgnakke & Sonntag, §11.6; Çengel & Boles, §11-2; Moran & Shapiro, §10.2.
