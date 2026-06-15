---
title: "Primera Ley (Sistema Cerrado)"
tags:
  - termodinamica
  - conservacion
  - energia
  - primera_ley
  - sistema_cerrado
draft: false
aliases:
  - primera ley SC
  - balance energetico SC
  - conservacion energia SC
---

# Primera Ley (Sistema Cerrado)

> [!definicion]
> Para un [[Sistemas Cerrados]] (masa fija, sin transferencia de masa a través de la frontera):
> $$
> \Delta U = Q - W
> $$
> 
> Forma diferencial:
> $$
> dU = \delta Q - \delta W
> $$
> 
> - $U$: [[Energia Interna]] total [kJ]
> - $Q$: calor neto transferido **hacia** el sistema [kJ]
> - $W$: trabajo neto **realizado por** el sistema [kJ]

## Formas particulares

> [!proposicion]
> **Proceso cíclico** ($\Delta U = 0$):
> $$
> \oint \delta Q = \oint \delta W
> $$

> [!proposicion]
> **Proceso infinitesimal reversible**:
> $$
> dU = TdS - PdV
> $$
> donde $\delta Q_{rev} = TdS$, $\delta W_{rev} = PdV$

## Trabajo en sistema cerrado

> [!info]
> El trabajo total $W$ puede incluir:
> - **Trabajo de expansión/compresión** (frontera móvil): $W_{borde} = \int P_{ext} dV$
> - **Trabajo de eje** (agitadores, hélices): $W_{eje}$
> - **Trabajo eléctrico**: $W_{elec}$
> - **Trabajo de tensión superficial**, magnético, etc.
> 
> Para proceso **cuasiestático** (reversible): $P_{ext} = P_{sistema}$, entonces $W_{borde} = \int P dV$

> [!demostracion]
> **De la equivalencia calor-trabajo (experimentos de Joule)**
>
> 1. **Experimento de Joule** (1843-1849):
>    - Sistema cerrado: agua en recipiente adiabático con rueda de paletas
>    - El trabajo realizado por la caída de un peso se disipa completamente en el agua
>    - Se mide el aumento de temperatura del agua
>    - Conclusión: $W \propto \Delta T$
>
> 2. **Calibración**:
>    - Misma masa de agua, mismo $\Delta T$, mediante transferencia de calor directa (agitación vs. calentamiento)
>    - Se establece la equivalencia: $1 cal = 4.184 J$
>
> 3. **Formulación matemática**:
>    - Para cualquier proceso entre dos estados de equilibrio:
>      $$
>      \oint \delta Q = \oint \delta W \quad \text{(para ciclos)}
>      $$
>    - Esto implica que $Q - W$ es independiente del camino
>    - Se define $U$ tal que $\Delta U = Q - W$
>
> 4. **Forma general**:
>    - La primera ley **no** afirma que $Q$ y $W$ sean funciones de estado
>    - Afirma que su diferencia sí lo es ($\Delta U$)
>    - Para procesos infinitesimales: $dU = \delta Q - \delta W$, donde $dU$ es exacta, $\delta Q$ y $\delta W$ son inexactas

> [!proposicion]
> **Consecuencias de la primera ley**:
> 1. $U$ es función de estado (su diferencial es exacta)
> 2. Para sistemas aislados ($Q=0$, $W=0$): $\Delta U = 0$ (conservación de la energía)
> 3. La energía no se crea ni se destruye, solo se transforma

## Casos particulares

> [!proposicion]
> **Proceso isocórico** ($dV = 0$, $W_{borde} = 0$):
> $$
> \Delta U = Q_v
> $$
> Si además no hay otros modos de trabajo: el calor medido en bomba calorimétrica es $\Delta U$

> [!proposicion]
> **Proceso isobárico** ($P = \text{constante}$, solo trabajo de borde):
> $$
> Q_P = \Delta U + P\Delta V = \Delta H
> $$
> donde $H = U + PV$ es la [[Entalpia]]

> [!proposicion]
> **Proceso adiabático** ($Q = 0$):
> $$
> \Delta U = -W
> $$

> [!proposicion]
> **Proceso reversible** (sin irreversibilidades internas):
> - $\delta W_{rev} = P dV$
> - $\delta Q_{rev} = T dS$
> - $dU = TdS - PdV$

> [!proposicion]
> **Gas ideal**:
> - $U = U(T)$ (ley de Joule)
> - $\Delta U = \int m c_v(T) dT$
> - Para $c_v$ constante: $\Delta U = m c_v \Delta T$

> [!ejemplo]
> **Expansión isotérmica de gas ideal** (sistema cerrado)
>
> Datos: $m=1kg$, $R=0.287 kJ/kg·K$, $T=300K$, $P_1=500kPa$, $P_2=100kPa$
>
> 1. Gas ideal isotérmico: $\Delta U = 0$
> 2. Primera ley: $Q = W$
> 3. Trabajo reversible: $W = \int P dV = mRT \ln(V_2/V_1) = mRT \ln(P_1/P_2)$
> 4. $W = 1 \times 0.287 \times 300 \times \ln(500/100) = 86.1 \times \ln 5 = 86.1 \times 1.609 = 138.5 kJ$
> 5. Por lo tanto: $Q = 138.5 kJ$

> [!ejemplo]
> **Compresión adiabática reversible de aire** (gas ideal)
>
> Datos: $m=2kg$, $c_v=0.718 kJ/kg·K$, $\gamma=1.4$, $T_1=300K$, $P_1=100kPa$, $P_2=600kPa$
>
> 6. Relación isentrópica: $T_2 = T_1 (P_2/P_1)^{(\gamma-1)/\gamma} = 300 \times 6^{0.2857} = 300 \times 1.669 = 500.7K$
> 7. $\Delta U = m c_v (T_2 - T_1) = 2 \times 0.718 \times 200.7 = 288.2 kJ$
> 8. Proceso adiabático: $Q = 0$ → $W = -\Delta U = -288.2 kJ$ (trabajo **entra** al sistema)

> [!ejemplo]
> **Calentamiento isocórico de agua** (sustancia incompresible)
>
> Datos: $m=3kg$, $c = 4.18 kJ/kg·K$, $T_1=20°C$, $T_2=80°C$
>
> 9. Volumen constante: $W_{borde} = 0$ (sin deformación)
> 10. Suponiendo otros trabajos nulos: $\Delta U = Q$
> 11. Para incompresible: $\Delta u \approx c \Delta T$
> 12. $Q = m c (T_2 - T_1) = 3 \times 4.18 \times 60 = 752.4 kJ$

## Relaciones con otras notas

> [!info]
> - [[Balance de Masa VC]] (para volumen de control, la forma cambia e introduce entalpía)
> - [[Segunda Ley SC]] (complementa con la dirección de los procesos)
> - [[Energia Interna]] (propiedad clave para sistemas cerrados)
> - [[Procesos/index | Procesos Termodinámicos]] (aplicaciones isotérmicas, isobáricas, etc.)

> [!warning]
> - **Signos**: $Q$ positivo **hacia** el sistema, $W$ positivo **realizado por** el sistema. Muchos textos de ingeniería usan convención opuesta para $W$
> - **No confundir** $W$ con trabajo de eje solamente: en sistema cerrado, $W$ incluye todo trabajo que cruza la frontera
> - **Proceso reversible**: solo es una idealización; los procesos reales tienen irreversibilidades ($W_{real} < W_{rev}$ para expansión, $W_{real} > W_{rev}$ para compresión)
> - **Sistema cerrado no implica volumen constante**: la frontera puede moverse (pistón)

> [!info]
> **Convención de signos adoptada**:
> - $Q$: + hacia el sistema
> - $W$: + realizado por el sistema
> - $\Delta U = Q - W$
> 
> Para trabajo **recibido** por el sistema: $W$ negativo
> 
> Alternativa común en ingeniería: $W$ como trabajo neto **entrante** → $\Delta U = Q + W$. **Verificar convención** según contexto.