---
title: "Balance de Exergía (Sistema Cerrado)"
tags:
  - termodinamica
  - conservacion
  - exergia
  - segunda_ley
  - sistema_cerrado
draft: false
aliases:
  - balance exergético SC
  - disponibilidad SC
  - exergy balance SC
---

# Balance de Exergía (Sistema Cerrado)

> [!definicion]
> Para un [[Sistemas Cerrados]] (masa fija) que interactúa con un ambiente a $T_0$, $P_0$:
> $$
> \Delta \Phi = \int_1^2 \left(1 - \frac{T_0}{T}\right) \delta Q - \left[W - P_0(V_2 - V_1)\right] - B_{dest}
> $$
>
> Forma diferencial:
> $$
> d\Phi = \left(1 - \frac{T_0}{T}\right) \delta Q - \left(\delta W - P_0 dV\right) - \delta B_{dest}
> $$
>
> - $\Phi = U - U_0 - T_0(S - S_0) + P_0(V - V_0)$: exergía del sistema cerrado (disponibilidad) [kJ]
> - $T_0$, $P_0$: temperatura y presión del ambiente muerto
> - $B_{dest} = T_0 S_{gen} \geq 0$: exergía destruida por irreversibilidades [kJ]

## Formas particulares

> [!proposicion]
> **Proceso reversible** ($B_{dest} = 0$):
> $$
> \Delta \Phi = \int_1^2 \left(1 - \frac{T_0}{T}\right) \delta Q - \left[W_{rev} - P_0(V_2 - V_1)\right]
> $$
>
> El trabajo reversible (máximo) es:
> $$
> W_{rev} = \int_1^2 \left(1 - \frac{T_0}{T}\right) \delta Q - \Delta \Phi + P_0(V_2 - V_1)
> $$

> [!proposicion]
> **Proceso adiabático** ($\delta Q = 0$):
> $$
> \Delta \Phi = -\left[W - P_0(V_2 - V_1)\right] - B_{dest}
> $$
>
> O equivalentemente: $W = P_0(V_2 - V_1) - \Delta \Phi - B_{dest}$

> [!proposicion]
> **Proceso isocórico** ($dV = 0$):
> $$
> \Delta \Phi = \int_1^2 \left(1 - \frac{T_0}{T}\right) \delta Q - W - B_{dest}
> $$

> [!proposicion]
> **Proceso isotérmico** ($T = \text{constante}$):
> $$
> \Delta \Phi = \left(1 - \frac{T_0}{T}\right) Q - \left[W - P_0(V_2 - V_1)\right] - B_{dest}
> $$

> [!proposicion]
> **Sistema aislado** ($\delta Q = 0$, $W = 0$, $dV = 0$):
> $$
> \Delta \Phi = -B_{dest} \leq 0
> $$
> La exergía de un sistema aislado nunca aumenta (se destruye o se mantiene constante si reversible).

> [!proposicion]
> **Sistema en equilibrio con el ambiente** ($U = U_0$, $S = S_0$, $V = V_0$):
> $$
> \Phi = 0
> $$
> No hay capacidad de producir trabajo.

> [!demostracion]
> **De la combinación de primera y segunda ley**
>
> 1. **Primera ley** para sistema cerrado:
>    $$
>    \Delta U = Q - W
>    $$
>
> 2. **Segunda ley** para sistema cerrado:
>    $$
>    \Delta S = \int \frac{\delta Q}{T} + S_{gen}, \quad S_{gen} \geq 0
>    $$
>
> 3. **Definición de exergía** para sistema cerrado:
>    $$
>    \Phi = U - U_0 - T_0(S - S_0) + P_0(V - V_0)
>    $$
>
> 4. **Diferencia de exergía** entre dos estados:
>    $$
>    \Delta \Phi = \Delta U - T_0 \Delta S + P_0 \Delta V
>    $$
>
> 5. **Sustituir** $\Delta U$ de la primera ley y $\Delta S$ de la segunda ley:
>    $$
>    \Delta \Phi = (Q - W) - T_0 \left( \int \frac{\delta Q}{T} + S_{gen} \right) + P_0 \Delta V
>    $$
>
> 6. **Reordenar** términos de calor:
>    $$
>    \Delta \Phi = \int \left(1 - \frac{T_0}{T}\right) \delta Q - \left(W - P_0 \Delta V\right) - T_0 S_{gen}
>    $$
>
> 7. **Identificar** $B_{dest} = T_0 S_{gen} \geq 0$:
>    $$
>    \Delta \Phi = \int \left(1 - \frac{T_0}{T}\right) \delta Q - \left(W - P_0 \Delta V\right) - B_{dest}
>    $$
>
> **Interpretación de términos**:
> - $\int (1 - T_0/T) \delta Q$: exergía asociada al calor transferido (trabajo máximo obtenible de ese calor)
> - $W - P_0 \Delta V$: trabajo útil (trabajo total menos el trabajo contra la atmósfera)
> - $B_{dest}$: exergía destruida por irreversibilidades (pérdida de potencial de trabajo)

## Trabajo máximo (reversible)

> [!teorema]
> Para un sistema cerrado que evoluciona entre dos estados, el **trabajo máximo** obtenible (o mínimo requerido) ocurre cuando el proceso es reversible:
>
> **Expansión** (el sistema produce trabajo):
> $$
> W_{max} = W_{rev} = -\Delta \Phi + \int \left(1 - \frac{T_0}{T}\right) \delta Q_{rev} + P_0 \Delta V
> $$
>
> **Compresión** (se requiere trabajo sobre el sistema):
> $$
> W_{min,entra} = -W_{max,sale} = \Delta \Phi - \int \left(1 - \frac{T_0}{T}\right) \delta Q_{rev} - P_0 \Delta V
> $$
>
> Para **sistema adiabático** ($\delta Q = 0$):
> - Expansión: $W_{max} = -\Delta \Phi + P_0 \Delta V$
> - Compresión: $W_{min,entra} = \Delta \Phi - P_0 \Delta V$

## Exergía destruida en procesos comunes

> [!info]
> **Transferencia de calor con diferencia finita**:
> - Dos cuerpos con $T_1 > T_2$, se transfiere calor $Q$ (aislados del ambiente)
> - $B_{dest} = T_0 S_{gen} = T_0 Q \left( \frac{1}{T_2} - \frac{1}{T_1} \right) = Q \frac{T_0 (T_1 - T_2)}{T_1 T_2}$
>
> **Expansión libre de Joule** (gas ideal, $T$ constante):
> - $B_{dest} = T_0 S_{gen} = T_0 mR \ln(V_2/V_1)$
>
> **Fricción mecánica** (trabajo disipado como calor):
> - Si el calor se disipa al ambiente a $T_0$: $B_{dest} = W_{fricción}$

> [!ejemplo]
> **Expansión libre de Joule** (determinar destrucción de exergía)
>
> Sistema: gas ideal, $m=1kg$, $R=0.287 kJ/kg·K$, $T_0=298K$, expansión de $V_1=0.1m^3$ a $V_2=0.2m^3$, $T$ constante.
>
> 1. Proceso: adiabático, sin trabajo, irreversible
> 2. $\Delta U = 0$, $T_2 = T_1 = T_0$ (suponiendo $T_1 = T_0$)
> 3. $\Delta S = mR \ln(V_2/V_1) = 0.287 \times \ln 2 = 0.287 \times 0.693 = 0.199 kJ/K$
> 4. $S_{gen} = \Delta S$ (adiabático) = $0.199 kJ/K$
> 5. $B_{dest} = T_0 S_{gen} = 298 \times 0.199 = 59.3 kJ$
>
> Interpretación: Se destruyeron $59.3 kJ$ de exergía (potencial de trabajo) a pesar de que la energía se conservó.

> [!ejemplo]
> **Transferencia de calor entre dos cuerpos**
>
> Dos cuerpos idénticos con $C = 10 kJ/K$, $T_1=500K$, $T_2=300K$, $T_0=298K$. Se ponen en contacto hasta $T_f=400K$.
>
> 6. $Q = C(T_1 - T_f) = 10 \times 100 = 1000 kJ$ (calor cedido por el caliente)
> 7. $S_{gen} = C \ln\frac{T_f}{T_1} + C \ln\frac{T_f}{T_2} = 10 (\ln\frac{400}{500} + \ln\frac{400}{300}) = 10 (\ln 0.8 + \ln 1.333) = 10 \times (-0.223 + 0.287) = 0.64 kJ/K$
> 8. $B_{dest} = T_0 S_{gen} = 298 \times 0.64 = 190.7 kJ$
> 9. Calor transferido a $T_0$? El proceso ocurre sin intercambio con el ambiente, por lo que $\int (1 - T_0/T)\delta Q$ se calcula por separado. La destrucción refleja la irreversibilidad de la transferencia con diferencia finita.

> [!ejemplo]
> **Compresión adiabática reversible vs. irreversible**
>
> Aire comprimido desde $T_1=300K$, $P_1=100kPa$ hasta $P_2=800kPa$. Comparar trabajo real con trabajo reversible mínimo.
>
> **Caso reversible** (isentrópico):
> - $T_{2s} = 300 \times 8^{0.2857} = 543.3K$
> - $W_{rev} = m c_v (T_{2s} - T_1) = 1 \times 0.718 \times 243.3 = 174.7 kJ$ (trabajo recibido, por eso es positivo pero en convención de primera ley sería negativo)
>
> **Caso real** ($\eta = 0.85$):
> - $T_2 = T_1 + (T_{2s} - T_1)/\eta = 300 + 243.3/0.85 = 586.2K$
> - $W_{real} = m c_v (T_2 - T_1) = 0.718 \times 286.2 = 205.5 kJ$
>
> **Exergía destruida** (proceso adiabático):
> - $\Delta \Phi = (U_2 - U_0) - T_0(S_2 - S_0) + P_0(V_2 - V_0)$
> - Alternativamente: $B_{dest} = W_{real} - W_{rev} = 205.5 - 174.7 = 30.8 kJ$
> - Verificar: $T_0 S_{gen} = 298 \times \Delta S$. $\Delta S = c_p \ln(T_2/T_1) - R \ln(P_2/P_1) = 1.005 \ln(586.2/300) - 0.287 \ln 8 = 0.678 - 0.597 = 0.081 kJ/K$
> - $T_0 \Delta S = 298 \times 0.081 = 24.1 kJ$ (diferencia por aproximaciones en $c_p$, $c_v$ constantes)

## Relaciones con otras notas

> [!info]
> - [[Primera Ley SC]] (proporciona $\Delta U$)
> - [[Segunda Ley SC]] (proporciona $S_{gen}$)
> - [[Balance de Exergia VC]] (extensión a volumen de control)
> - [[Exergia]] (definiciones y propiedades de $\Phi$)
> - [[Eficiencia Exergética]]

> [!warning]
> - **Trabajo útil**: $W_{util} = W - P_0 \Delta V$. No confundir con trabajo total.
> - **Ambiente muerto**: $T_0$, $P_0$ deben especificarse. $U_0$, $S_0$, $V_0$ son los valores que el sistema tendría si estuviera en equilibrio con ese ambiente.
> - **Exergía negativa**: posibles si el sistema está por debajo del ambiente (ej. fluido frío). Significa que se requiere trabajo para llevarlo al estado muerto.
> - **La exergía no se conserva**: $B_{dest} \geq 0$ para procesos irreversibles, $=0$ para reversibles.
> - En sistemas aislados, $\Delta \Phi = -B_{dest} \leq 0$ (la exergía disminuye o es constante).

> [!info]
> **Convención de signos**:
> - $W$: positivo cuando el sistema **realiza** trabajo (sale del sistema)
> - $W - P_0 \Delta V$: trabajo útil (lo que realmente se puede aprovechar)
> - $B_{dest}$: siempre $\geq 0$
> - $\int (1 - T_0/T)\delta Q$: puede ser positivo ($T > T_0$) o negativo ($T < T_0$)