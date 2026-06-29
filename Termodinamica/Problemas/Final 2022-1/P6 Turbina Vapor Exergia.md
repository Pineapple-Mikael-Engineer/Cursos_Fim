---
title: "P6 — Turbina de vapor: análisis de exergía"
order: 7
tags: [termodinamica, problemas, exergia, turbina]
draft: false
aliases: [turbina exergía destruida segunda ley]
---

# P6 — Turbina de vapor: análisis de exergía

> [!definicion] Enunciado
> El vapor entra a una turbina en forma estacionaria a $3{,}5$ MPa y $450\,^\circ$C a $10$ kg/s, y sale a $0{,}22$ MPa y $170\,^\circ$C. El vapor pierde calor hacia el aire a una tasa de $300$ kW, que se halla a $100$ kPa y $25\,^\circ$C; $\Delta$EC y $\Delta$EP despreciables. Determinar **(a)** potencia real; **(b)** potencia máxima posible; **(c)** eficiencia según la 2ª ley; **(d)** exergía destruida; **(e)** exergía del vapor a la entrada.

> [!teoria]
> Con [[Balance de Exergia VC]]: $\dot W_{rev}=\dot m(\psi_1-\psi_2)$ (la pérdida de calor a $T_0$ no destruye exergía adicional pues sale al ambiente); $\dot W_{real}=\dot m(h_1-h_2)-\dot Q_{perd}$; $\eta_{II}=\dot W_{real}/\dot W_{rev}$; $\dot X_{dest}=\dot W_{rev}-\dot W_{real}$.

> [!solucion]
> Estados: $h_1=3337$, $s_1=7{,}005$; $h_2=2810$ ($0{,}22$ MPa, $170\,^\circ$C), $s_2=7{,}370$. Estado muerto ($25\,^\circ$C): $h_0=104{,}8$, $s_0=0{,}367$.
> **(a)** $\dot W_{real}=\dot m(h_1-h_2)-\dot Q_{perd}=10(3337-2810)-300=\boxed{4977\ \text{kW}}.$
> **(b)** $\dot W_{max}=\dot m[(h_1-h_2)-T_0(s_1-s_2)]=10[527-298{,}15(7{,}005-7{,}370)]=\boxed{6366\ \text{kW}}.$
> **(c)** $\eta_{II}=\dfrac{4977}{6366}=\boxed{78{,}2\%}.$
> **(d)** $\dot X_{dest}=6366-4977=\boxed{1389\ \text{kW}}.$
> **(e)** $\psi_1\dot m=\dot m[(h_1-h_0)-T_0(s_1-s_0)]=10[(3337-104{,}8)-298{,}15(7{,}005-0{,}367)]=\boxed{12\,535\ \text{kW}}.$

> [!info]
> Valores de vapor interpolados (cotejar con CATT3). $\dot X_{dest}=T_0\dot S_{gen}$ mide la pérdida de calidad por la expansión irreversible y la transferencia de calor con gradiente.

> [!referencia]
> [[Balance de Exergia VC]] · [[Exergia]] · [[Sistemas/Dispositivos Flujo/Turbinas | Turbinas]]
