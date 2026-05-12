---
title: "Segunda Ley (Sistema Cerrado)"
tags:
  - termodinamica
  - conservacion
  - entropia
  - segunda_ley
  - sistema_cerrado
draft: false
aliases:
  - segunda ley SC
  - balance entropico SC
  - desigualdad de Clausius
---

# Segunda Ley (Sistema Cerrado)

> [!definicion]
> Para un [[Sistemas Cerrados]] (masa fija), la variación de entropía entre dos estados de equilibrio es:
> $$
> \Delta S = S_2 - S_1 = \int_1^2 \frac{\delta Q}{T} + S_{gen}
> $$
>
> Forma diferencial:
> $$
> dS = \frac{\delta Q}{T} + \delta S_{gen}, \quad \delta S_{gen} \geq 0
> $$
>
> - $S$: [[Entropia]] total [kJ/K]
> - $T$: temperatura en la frontera donde ocurre $\delta Q$ [K]
> - $S_{gen} \geq 0$: entropía generada por irreversibilidades internas [kJ/K]

## Formas particulares

> [!proposicion]
> **Proceso adiabático** ($\delta Q = 0$):
> $$
> \Delta S = S_{gen} \geq 0
> $$
> La entropía nunca disminuye en un sistema cerrado adiabático.

> [!proposicion]
> **Proceso reversible** ($S_{gen} = 0$):
> $$
> \Delta S = \int_1^2 \frac{\delta Q_{rev}}{T}
> $$
> o en forma diferencial: $dS = \frac{\delta Q_{rev}}{T}$

> [!proposicion]
> **Proceso internamente reversible** (sin irreversibilidades internas, pero puede haber transferencia de calor irreversible a través de la frontera):
> - Internamente: $dS = \delta Q/T$
> - Si además $T_{frontera} = T_{sistema}$, entonces $\delta Q = T dS$

## Desigualdad de Clausius

> [!teorema]
> Para cualquier **ciclo** termodinámico:
> $$
> \oint \frac{\delta Q}{T} \leq 0
> $$
>
> - La igualdad se cumple para ciclos **reversibles**
> - La desigualdad para ciclos **irreversibles**
>
> Esta desigualdad es equivalente al enunciado de la segunda ley.

> [!demostracion]
> **De la desigualdad de Clausius a la definición de entropía**
>
> 1. **Ciclo reversible**:
>    - Para un ciclo reversible: $\oint (\delta Q_{rev}/T) = 0$
>    - Esto implica que $\int_1^2 (\delta Q_{rev}/T)$ es **independiente del camino**
>    - Se define una función de estado $S$ tal que:
>      $$
>      S_2 - S_1 = \int_1^2 \frac{\delta Q_{rev}}{T}
>      $$
>
> 2. **Ciclo irreversible** (camino 1→2 irreversible, 2→1 reversible):
>    - Aplicando desigualdad de Clausius:
>      $$
>      \oint \frac{\delta Q}{T} = \int_1^2 \frac{\delta Q_{irr}}{T} + \int_2^1 \frac{\delta Q_{rev}}{T} \leq 0
>      $$
>    - Sustituyendo $\int_2^1 \delta Q_{rev}/T = S_1 - S_2$:
>      $$
>      \int_1^2 \frac{\delta Q_{irr}}{T} + S_1 - S_2 \leq 0
>      $$
>    - Reordenando:
>      $$
>      S_2 - S_1 \geq \int_1^2 \frac{\delta Q_{irr}}{T}
>      $$
>
> 3. **Definición de $S_{gen}$**:
>    - Se define $S_{gen} = \Delta S - \int_1^2 \delta Q/T \geq 0$
>    - $S_{gen} = 0$ para procesos reversibles
>    - $S_{gen} > 0$ para procesos irreversibles
>
> 4. **Forma diferencial**:
>    $$
>    dS = \frac{\delta Q}{T} + \delta S_{gen}, \quad \delta S_{gen} \geq 0
>    $$
>
> **Interpretación**: La entropía de un sistema cerrado puede aumentar por:
> - Transferencia de calor **hacia** el sistema ($\delta Q > 0$)
> - Irreversibilidades internas ($\delta S_{gen} > 0$)

## Relación con la primera ley

> [!info]
> Para procesos **reversibles**, combinando primera y segunda ley:
> $$
> dU = \delta Q_{rev} - \delta W_{rev} = TdS - PdV
> $$
>
> Para procesos **irreversibles**:
> - $\delta W_{irr} \leq PdV$ (expansión: trabajo menor; compresión: trabajo mayor)
> - $\delta Q_{irr} \leq TdS$ (calor recibido menor que $TdS$ si hay irreversibilidades)
> - La igualdad $dU = \delta Q - \delta W$ siempre se cumple, pero $\delta Q \leq TdS$ y $\delta W \leq PdV$ (con signos adecuados)

## Casos particulares

> [!proposicion]
> **Proceso isotérmico reversible**:
> $$
> \Delta S = \frac{Q_{rev}}{T}
> $$

> [!proposicion]
> **Proceso adiabático reversible** (isentrópico):
> $$
> \Delta S = 0, \quad S_2 = S_1
> $$

> [!proposicion]
> **Proceso isocórico reversible** ($dV=0$):
> $$
> \Delta S = \int_1^2 \frac{m c_v(T)}{T} dT
> $$

> [!proposicion]
> **Proceso isobárico reversible** ($dP=0$):
> $$
> \Delta S = \int_1^2 \frac{m c_p(T)}{T} dT
> $$

> [!proposicion]
> **Gas ideal** (reversible, cualquier proceso):
> - En términos de $T$ y $v$: $\Delta s = \int c_v(T) \frac{dT}{T} + R \ln\frac{v_2}{v_1}$
> - En términos de $T$ y $P$: $\Delta s = \int c_p(T) \frac{dT}{T} - R \ln\frac{P_2}{P_1}$
> - Para $c_p$, $c_v$ constantes:
>   $\Delta s = c_v \ln\frac{T_2}{T_1} + R \ln\frac{v_2}{v_1} = c_p \ln\frac{T_2}{T_1} - R \ln\frac{P_2}{P_1}$

> [!proposicion]
> **Sustancia incompresible** ($v$ constante, $c_p = c_v = c$):
> $$
> \Delta s = \int c(T) \frac{dT}{T}
> $$
> Para $c$ constante: $\Delta s = c \ln\frac{T_2}{T_1}$

> [!proposicion]
> **Mezcla líquido-vapor** (región de saturación):
> $$
> s = s_f + x s_{fg}, \quad \Delta s = s_2 - s_1
> $$

> [!ejemplo]
> **Generación de entropía en una expansión libre (Joule)**
>
> Sistema cerrado: gas ideal en un recipiente con dos cámaras separadas por membrana. Inicialmente gas en cámara 1 (volumen $V_1$), cámara 2 vacío. Se rompe la membrana y el gas ocupa $V_2 = 2V_1$ (expansión al vacío, adiabática, sin trabajo).
>
> 1. Primera ley: $\Delta U = 0 - 0 = 0$ → $T_2 = T_1$ (gas ideal)
> 2. El proceso es **irreversible**
> 3. Para calcular $\Delta S$, se diseña un proceso reversible entre los mismos estados: expansión isotérmica reversible de $V_1$ a $V_2$ a temperatura $T$
> 4. $\Delta S = \int \frac{\delta Q_{rev}}{T} = \frac{Q_{rev}}{T} = \frac{mRT \ln(V_2/V_1)}{T} = mR \ln 2$
> 5. Como $\int \delta Q/T = 0$ (adiabático irreversible), entonces:
>    $S_{gen} = \Delta S - 0 = mR \ln 2 > 0$

> [!ejemplo]
> **Transferencia de calor con diferencia finita**
>
> Sistema cerrado: dos cuerpos idénticos con capacidad calorífica $C = mc$, inicialmente a $T_1 = 400K$ y $T_2 = 200K$. Se ponen en contacto térmico hasta alcanzar equilibrio $T_f = 300K$ (aislados del entorno).
>
> 6. Calor cedido por cuerpo caliente = calor ganado por cuerpo frío
> 7. $\Delta S_{total} = \Delta S_1 + \Delta S_2 = C \ln\frac{T_f}{T_1} + C \ln\frac{T_f}{T_2}$
> 8. $\Delta S = C \left( \ln\frac{300}{400} + \ln\frac{300}{200} \right) = C \left( \ln 0.75 + \ln 1.5 \right)$
> 9. $\Delta S = C (\ln 1.125) = C \times 0.1178$
> 10. Como el sistema total es adiabático, $\int \delta Q/T = 0$, por lo tanto $S_{gen} = \Delta S_{total} > 0$

> [!ejemplo]
> **Compresión adiabática irreversible** (gas ideal)
>
> Datos: $m=1kg$, $c_v=0.718 kJ/kg·K$, $R=0.287 kJ/kg·K$, $T_1=300K$, $P_1=100kPa$, $P_2=600kPa$, trabajo real $W_{in} = 250 kJ$.
>
> 11. **Proceso real**: Primera ley: $Q=0$, $\Delta U = -W$ con $W = -250 kJ$ (trabajo entra) → $\Delta U = 250 kJ$
> 12. $\Delta U = m c_v (T_2 - T_1)$ → $T_2 = T_1 + \Delta U/(m c_v) = 300 + 250/0.718 = 300 + 348.2 = 648.2K$
> 13. $\Delta S = m \left( c_p \ln\frac{T_2}{T_1} - R \ln\frac{P_2}{P_1} \right)$, con $c_p = c_v + R = 1.005 kJ/kg·K$
> 14. $\Delta S = 1 \times \left( 1.005 \ln(648.2/300) - 0.287 \ln 6 \right)$
> 15. $\Delta S = 1.005 \times 0.770 - 0.287 \times 1.792 = 0.774 - 0.514 = 0.260 kJ/K$
> 16. Proceso adiabático: $S_{gen} = \Delta S = 0.260 kJ/K$

## Relaciones con otras notas

> [!info]
> - [[Primera Ley SC]] (complementa para determinar estados)
> - [[Balance de Entropia VC]] (extensión a volumen de control)
> - [[Exergia]] ($B_{dest} = T_0 S_{gen}$)
> - [[Irreversibilidad]]
> - [[Relaciones TdS]]

> [!warning]
> - $S_{gen} \geq 0$ es la única dirección impuesta por la segunda ley; $\Delta S$ puede ser negativo si el sistema cede calor
> - Para calcular $\Delta S$ entre dos estados, **siempre** se puede usar un proceso reversible aunque el real sea irreversible (entropía es función de estado)
> - **No confundir**: $dS = \delta Q/T$ solo para procesos reversibles. En irreversibles, $dS > \delta Q/T$ (o $\delta S_{gen} > 0$)
> - La temperatura $T$ en $\delta Q/T$ es **la temperatura en la frontera** donde ocurre la transferencia, no necesariamente la temperatura del sistema

> [!info]
> **Convención de signos**:
> - $Q$: + hacia el sistema
> - $S_{gen}$: siempre $\geq 0$
> - $\Delta S$ puede ser positivo, negativo o cero
> - En procesos adiabáticos: $\Delta S = S_{gen} \geq 0$