---
title: "Problema 02 — Compresión politrópica en pistón-cilindro"
tags:
  - termodinamica
  - problemas
  - sistema_cerrado
  - primera_ley
draft: false
aliases:
  - compresión politrópica
  - pistón-cilindro aire
---

# Problema 02 — Compresión politrópica en pistón-cilindro

> [!definicion] Enunciado
> Un dispositivo pistón-cilindro contiene $m = 0.5\ \text{kg}$ de aire (gas ideal) a $P_1 = 100\ \text{kPa}$ y $T_1 = 300\ \text{K}$. El aire se comprime en un proceso cuasiestático **politrópico** $P\,V^{\,n} = \text{cte}$ con $n = 1.3$ hasta $P_2 = 600\ \text{kPa}$.
>
> Datos del aire: $R = 0.287$, $c_v = 0.718$, $c_p = 1.005\ \text{kJ/kg·K}$.
>
> Se pide:
> 1. La temperatura final.
> 2. El trabajo de frontera y el calor intercambiado.
> 3. La entropía generada, tomando el entorno a $T_0 = 300\ \text{K}$.

## Estrategia

> [!teoria]
> Sistema **cerrado** (masa fija, frontera móvil). Aplican:
> - [[Primera Ley SC]]: $\Delta U = Q - W$, con trabajo de frontera $W = \int P\,dV$.
> - Modelo de [[Gas Ideal]]: $Pv = RT$, $\Delta U = m c_v \Delta T$.
> - [[Segunda Ley SC]]: $S_{gen} = \Delta S - \displaystyle\int \frac{\delta Q}{T_b} \ge 0$.
>
> El cambio de entropía del gas ideal se obtiene de las ecuaciones [[TdS]].

## Inciso 1 — Temperatura final

> [!proposicion]
> Para un proceso politrópico de gas ideal, combinando $P\,V^{\,n}=\text{cte}$ con $Pv=RT$:
> $$
> \frac{T_2}{T_1} = \left(\frac{P_2}{P_1}\right)^{\frac{n-1}{n}}
> $$

> [!solucion]
> $$
> T_2 = 300\,(6)^{0.3/1.3} = 300 \times 1.512 = 453.6\ \text{K}
> $$
> La [[Temperatura]] sube al comprimir, como exige $Pv = RT$ con [[Volumen Especifico | volumen específico]] decreciente.

## Inciso 2 — Trabajo de frontera y calor

> [!proposicion]
> El trabajo de frontera de un proceso politrópico ($n \ne 1$) es
> $$
> W = \int_1^2 P\,dV = \frac{P_1 V_1 - P_2 V_2}{n-1} = \frac{m R\,(T_1 - T_2)}{n-1}
> $$

> [!solucion]
> $$
> W = \frac{0.5 \times 0.287\,(300 - 453.6)}{1.3 - 1} = \frac{0.1435 \times (-153.6)}{0.3} = -73.5\ \text{kJ}
> $$
> El signo negativo indica trabajo **hecho sobre** el gas (compresión), coherente con la convención de [[Primera Ley SC]] ($W$ positivo si lo realiza el sistema).
>
> Variación de [[Energia Interna]] y calor por la primera ley:
> $$
> \Delta U = m c_v \Delta T = 0.5 \times 0.718 \times 153.6 = 55.1\ \text{kJ}
> $$
> $$
> Q = \Delta U + W = 55.1 + (-73.5) = -18.4\ \text{kJ}
> $$
> $Q < 0$: el gas **cede** calor durante la compresión (el proceso $n=1.3$ está entre el isotérmico $n=1$ y el adiabático $n=\gamma=1.4$).

## Inciso 3 — Entropía generada

> [!solucion]
> Cambio de entropía del gas ideal (segunda ecuación [[TdS]], $c_p$ constante):
> $$
> \Delta s = c_p \ln\frac{T_2}{T_1} - R \ln\frac{P_2}{P_1} = 1.005\,\ln(1.512) - 0.287\,\ln(6) = 0.4156 - 0.5142 = -0.0987\ \text{kJ/kg·K}
> $$
> $$
> \Delta S = m\,\Delta s = -0.0493\ \text{kJ/K}
> $$
> Con el calor cedido a través de una frontera a $T_b \approx T_0 = 300\ \text{K}$:
> $$
> S_{gen} = \Delta S - \frac{Q}{T_b} = -0.0493 - \frac{-18.4}{300} = -0.0493 + 0.0613 = 0.0120\ \text{kJ/K}
> $$

> [!info] Verificación física
> Aunque la entropía del gas **disminuye** ($\Delta S < 0$, porque se enfría hacia el entorno), la entropía generada es positiva ($S_{gen} > 0$): la irreversibilidad asociada a la transferencia de calor con diferencia finita de temperatura domina el balance. Coherente con [[Segunda Ley SC]].

## Notas usadas

> [!referencia]
> [[Primera Ley SC]] · [[Segunda Ley SC]] · [[Energia Interna]] · [[Entropia]] · [[TdS]] · [[Gas Ideal]] · [[Presion]] · [[Temperatura]] · [[Volumen Especifico]]

> [!info]
> **Convención de notación**:
> - $W > 0$: trabajo realizado por el sistema; $Q > 0$: calor hacia el sistema.
> - $n$: índice politrópico; $\gamma = c_p/c_v = 1.4$ para el aire.
> - $T_b$: temperatura de la frontera por la que cruza el calor.
