---
title: "Problema 08 — Mezcla adiabática de dos gases"
tags:
  - termodinamica
  - problemas
  - mezclas
  - segunda_ley
draft: false
aliases:
  - mezcla irreversible
  - entropía generada por mezcla
  - mezcla adiabática volumen constante
---

# Problema 08 — Mezcla adiabática de dos gases

> [!definicion] Enunciado
> Dos depósitos rígidos y aislados se conectan por una válvula. Inicialmente uno contiene $n_{\text{N}_2} = 0{,}79\ \text{kmol}$ de nitrógeno a $2\ \text{atm}$ y $250\ \text{K}$; el otro, $n_{\text{O}_2} = 0{,}21\ \text{kmol}$ de oxígeno a $1\ \text{atm}$ y $300\ \text{K}$. Se abre la válvula y los gases se mezclan hasta el equilibrio, sin intercambio de calor ni trabajo con el entorno.
>
> Se pide:
> 1. La temperatura final de la mezcla.
> 2. La presión final.
> 3. La entropía generada.

## Estrategia

> [!teoria]
> Sistema **cerrado y aislado** (rígido, adiabático): $\Delta U = 0$ y $W = 0$. Es el caso de **formación de mezcla**: gases distintos, a distinta $T$ y distinta $p$ — las **tres** causas de irreversibilidad (ver [[Mezclas de Gases]]). La [[Segunda Ley SC]] da $S_{gen} = \Delta S > 0$, pues no hay transferencia de entropía ($Q = 0$). Se usan $c_v$, $c_p$ constantes a la temperatura media.

## Inciso 1 — Temperatura final

> [!solucion]
> Balance de energía $\Delta U = 0$: $n_{\text{N}_2}c_{v,\text{N}_2}(T_2 - T_{\text{N}_2}) + n_{\text{O}_2}c_{v,\text{O}_2}(T_2 - T_{\text{O}_2}) = 0$. Despejando $T_2$:
> $$
> T_2 = \frac{n_{\text{N}_2}\bar c_{v,\text{N}_2}T_{\text{N}_2} + n_{\text{O}_2}\bar c_{v,\text{O}_2}T_{\text{O}_2}}{n_{\text{N}_2}\bar c_{v,\text{N}_2} + n_{\text{O}_2}\bar c_{v,\text{O}_2}}
> $$
> Con $\bar c_v$ molares a $\sim 275\ \text{K}$: $\bar c_{v,\text{N}_2} = 28{,}02(0{,}742) = 20{,}79$, $\bar c_{v,\text{O}_2} = 32{,}0(0{,}655) = 20{,}96\ \text{kJ/kmol·K}$:
> $$
> T_2 = \frac{0{,}79(20{,}79)(250) + 0{,}21(20{,}96)(300)}{0{,}79(20{,}79) + 0{,}21(20{,}96)} = \frac{4106 + 1320{,}5}{16{,}42 + 4{,}40} = 260\ \text{K}
> $$
> La temperatura final es una media ponderada por las capacidades caloríficas; queda cerca de $T_{\text{N}_2}$ por su mayor cantidad.

## Inciso 2 — Presión final

> [!solucion]
> El volumen total es la suma de los volúmenes iniciales (ecuación de estado de cada gas):
> $$
> V = \frac{n_{\text{N}_2}R_u T_{\text{N}_2}}{p_{\text{N}_2}} + \frac{n_{\text{O}_2}R_u T_{\text{O}_2}}{p_{\text{O}_2}}
> $$
> La mezcla final ocupa $V$ a $T_2$ con $n = 1{,}0\ \text{kmol}$, así que $p_2 = nR_u T_2 / V$:
> $$
> p_2 = \frac{(n_{\text{N}_2}+n_{\text{O}_2})\,T_2}{\dfrac{n_{\text{N}_2}T_{\text{N}_2}}{p_{\text{N}_2}} + \dfrac{n_{\text{O}_2}T_{\text{O}_2}}{p_{\text{O}_2}}} = \frac{(1{,}0)(260)}{\dfrac{0{,}79(250)}{2} + \dfrac{0{,}21(300)}{1}} = \frac{260}{98{,}75 + 63} = 1{,}61\ \text{atm}
> $$

## Inciso 3 — Entropía generada

> [!solucion]
> Con $Q = 0$, la [[Segunda Ley SC]] da $S_{gen} = \Delta S$. Cada gas pasa de su estado inicial a $T_2$ y a su **presión parcial** $y_i p_2$ en la mezcla. Con $c_p$ constante ($\bar c_{p,i} = \bar c_{v,i} + R_u$: $\bar c_{p,\text{N}_2} = 29{,}10$, $\bar c_{p,\text{O}_2} = 29{,}27$) y $y_{\text{N}_2} = 0{,}79$, $y_{\text{O}_2} = 0{,}21$:
> $$
> S_{gen} = n_{\text{N}_2}\!\left[\bar c_{p,\text{N}_2}\ln\frac{T_2}{T_{\text{N}_2}} - R_u\ln\frac{y_{\text{N}_2}p_2}{p_{\text{N}_2}}\right] + n_{\text{O}_2}\!\left[\bar c_{p,\text{O}_2}\ln\frac{T_2}{T_{\text{O}_2}} - R_u\ln\frac{y_{\text{O}_2}p_2}{p_{\text{O}_2}}\right]
> $$

> [!solucion]
> Evaluando cada término ($p_2 = 1{,}61\ \text{atm}$):
> $$
> \text{N}_2:\; 0{,}79\left[29{,}10\,\ln\frac{260}{250} - 8{,}314\,\ln\frac{0{,}79(1{,}61)}{2}\right] = 0{,}79\,[1{,}14 + 3{,}80] = 3{,}90\ \text{kJ/K}
> $$
> $$
> \text{O}_2:\; 0{,}21\left[29{,}27\,\ln\frac{260}{300} - 8{,}314\,\ln\frac{0{,}21(1{,}61)}{1}\right] = 0{,}21\,[-4{,}19 + 8{,}90] = 0{,}99\ \text{kJ/K}
> $$
> $$
> S_{gen} = 3{,}90 + 0{,}99 = 4{,}89\ \text{kJ/K} \;>\; 0
> $$

> [!info] Verificación física
> $S_{gen} > 0$ confirma que la mezcla espontánea es **irreversible**: para volver a separar los gases haría falta trabajo del entorno. Aunque el $\text{O}_2$ se enfría (su término de temperatura es negativo), el término de presión —la **mezcla difusiva** hacia su presión parcial, menor que la inicial— domina y produce entropía. Aquí actúan las tres causas: distinta $T$, distinta $p$ y gases distintos.

## Notas usadas

> [!referencia]
> [[Mezclas de Gases]] · [[Segunda Ley SC]] · [[Sistemas Cerrados]] · [[Gas Ideal]] · [[Entropia]] · [[Energia Interna]] · Moran & Shapiro, Ej. 12.5.

> [!info]
> **Convención de notación**:
> - $S_{gen} \ge 0$: entropía generada [kJ/K]; $y_i p_2$: presión parcial del componente en la mezcla final.
> - $\bar c_v$, $\bar c_p$: calores específicos molares [kJ/kmol·K]; barra: magnitud molar.
