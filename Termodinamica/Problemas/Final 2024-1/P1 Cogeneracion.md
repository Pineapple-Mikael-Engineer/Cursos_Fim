---
title: "P1 — Ciclo de cogeneración (vapor con proceso industrial)"
order: 2
tags: [termodinamica, problemas, ciclos, rankine, cogeneracion]
draft: false
aliases: [cogeneración vapor, factor de utilización, extracción proceso industrial]
---

# P1 — Ciclo de cogeneración (vapor con proceso industrial)

> [!definicion] Enunciado
> Un ciclo de **cogeneración**: el vapor ingresa a la turbina de alta presión (punto 5) a $10$ MPa y $550\,^\circ$C; luego se extrae el $25\%$ del vapor (punto 6) a $1{,}5$ MPa para uso industrial, donde se requieren $5000$ kW de flujo de calor ($\dot Q_{load}$). El resto se descarga de la turbina de baja presión al condensador a $15$ kPa. El vapor del proceso retorna como **líquido saturado a $1$ MPa** (punto 8) y se mezcla con el agua del condensador impulsada por la bomba P1; la mezcla se impulsa a la caldera por P2. Todos los procesos son reversibles, las turbinas adiabáticas. Determinar **(a)** datos faltantes; **(b)** flujo de vapor de la caldera [kg/s]; **(c)** potencia de las turbinas; **(d)** potencia neta [kW]; **(e)** factor de utilización [%].

## Estrategia

> [!teoria]
> Cogeneración = producir potencia **y** calor útil de proceso con el mismo vapor. La extracción a $1{,}5$ MPa alimenta el proceso; el resto sigue expandiéndose. El [[Sistemas/Dispositivos Flujo/Flash | mezclador]] junta el retorno del proceso (8) con el condensado (2). El **factor de utilización** mide cuánta de la energía del combustible se aprovecha (potencia + calor de proceso).

![[rankine_esquema_planta.svg|360]]

> [!info] Estados (vapor)
> | Pto | $P$ [MPa] | $T$ [°C] | $h$ [kJ/kg] | $s$ [kJ/kg·K] |
> |:---:|:---:|:---:|:---:|:---:|
> | 5 | 10 | 550 | 3501 | 6{,}756 |
> | 6 | 1{,}5 | — | 2948 | 6{,}756 |
> | 7 | 0{,}015 | — | 2189 | 6{,}756 |
> | 1 | 0{,}015 | 53{,}97 | 225{,}9 | $v_f=0{,}001014$ |
> | 2 | 1 | — | 226{,}9 | — |
> | 8 | 1 | 179{,}9 | 762{,}8 | $x=0$ |
> | 3 (mezcla) | 1 | — | 360{,}9 | — |
> | 4 | 10 | — | 371{,}0 | — |

> [!solucion] (b) Flujo de vapor de la caldera
> El proceso recibe $\dot Q_{load}=0{,}25\dot m_5(h_6-h_8)=5000$ kW:
> $$\dot m_5=\frac{5000}{0{,}25\,(2948-762{,}8)}=\boxed{9{,}15\ \text{kg/s}}.$$

> [!solucion] (c) Potencia de las turbinas
> $$\dot W_T=\dot m_5(h_5-h_6)+0{,}75\dot m_5(h_6-h_7)=9{,}15(553)+6{,}86(759)=\boxed{10\,271\ \text{kW}}.$$

> [!solucion] (d) Potencia neta
> Bombas: P1 ($0{,}75\dot m_5$, $15\,\text{kPa}\to1\,\text{MPa}$): $\dot W_{P1}=6{,}86$ kW; P2 ($\dot m_5$, $1\to10$ MPa): $\dot W_{P2}=\dot m_5 v_{f3}(9000)\approx92{,}8$ kW.
> $$\dot W_n=\dot W_T-\dot W_{P1}-\dot W_{P2}=10\,271-6{,}9-92{,}8=\boxed{10\,171\ \text{kW}}.$$

> [!solucion] (e) Factor de utilización
> Calor aportado en caldera: $\dot Q_A=\dot m_5(h_5-h_4)=9{,}15(3501-371)=28\,640$ kW.
> $$F_u=\frac{\dot W_n+\dot Q_{load}}{\dot Q_A}=\frac{10\,171+5000}{28\,640}=\boxed{53{,}0\%}.$$

> [!info]
> El factor de utilización ($53\%$) es muy superior a la eficiencia eléctrica sola, porque la cogeneración aprovecha además los $5000$ kW de calor de proceso que de otro modo se perderían en el condensador. Coincide con la clave ($\dot m_5=9{,}152$ kg/s).

> [!referencia]
> [[Conversión de Energía/Ciclos de Potencia/Rankine/Rankine Regenerativo | Rankine Regenerativo]] · [[Sistemas/Dispositivos Flujo/Turbinas | Turbinas]] · [[Balance de Energia VC]]
