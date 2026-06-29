---
title: "P3 — Combustión de etano con exceso de aire"
order: 4
tags: [termodinamica, problemas, combustion]
draft: false
aliases: [combustión etano C2H6, exceso aire]
---

# P3 — Combustión de etano con exceso de aire

> [!definicion] Enunciado
> Se queman $15$ kg/hr de etano $\mathrm{C_2H_6}$ con $100\%$ de **exceso de aire**, de tal manera que los gases de combustión salen a $500$ K. El aire y el combustible ingresan a $300$ K. Determinar **(a)** el balance estequiométrico de la combustión; **(b)** el caudal de aire ingresado [m³/hr]; **(c)** el calor generado [kW].

![[combustion_esquema_reactivos_productos.svg|400]]

> [!solucion] (a) Balance
> Estequiométrico: $\mathrm{C_2H_6}+a(\mathrm{O_2}+3{,}76\mathrm{N_2})\to2\,\mathrm{CO_2}+3\,\mathrm{H_2O}+3{,}76a\,\mathrm{N_2}$; O: $2a=7\Rightarrow a=3{,}5$.
> $100\%$ de exceso ($a=7$): $\mathrm{O_2}=7$, $\mathrm{N_2}=26{,}32$, exceso $\mathrm{O_2}=3{,}5$:
> $$\boxed{\mathrm{C_2H_6}+7\,\mathrm{O_2}+26{,}32\,\mathrm{N_2}\to2\,\mathrm{CO_2}+3\,\mathrm{H_2O}+3{,}5\,\mathrm{O_2}+26{,}32\,\mathrm{N_2}}$$

> [!solucion] (b) Caudal de aire
> Flujo molar de combustible: $\dot n_f=\dfrac{15}{30{,}07}=0{,}499$ kmol/hr. Aire por kmol de combustible $=7+26{,}32=33{,}32$ kmol. A $300$ K, $101{,}325$ kPa:
> $$\dot V_{aire}=\dot n_f(33{,}32)\frac{R_u T}{P}=0{,}499(33{,}32)\frac{8{,}314(300)}{101{,}325}=\boxed{409\ \text{m}^3/\text{hr}}.$$

> [!solucion] (c) Calor generado
> $Q=H_P(500\text{K})-H_R(300\text{K})$. Con $\bar h_f^\circ$ [kJ/kmol] ($\mathrm{C_2H_6}=-84\,680$, $\mathrm{CO_2}=-393\,520$, $\mathrm{H_2O(g)}=-241\,820$) y $\Delta\bar h_{500}$ ($\mathrm{CO_2}\,8314$, $\mathrm{H_2O}\,6920$, $\mathrm{O_2}\,6086$, $\mathrm{N_2}\,5912$):
> $$H_P=2(-385\,206)+3(-234\,900)+3{,}5(6086)+26{,}32(5912)=-1\,298\,200\ \text{kJ/kmol}.$$
> $$Q=H_P-H_R=-1\,298\,200-(-84\,680)=-1\,213\,500\ \text{kJ/kmol}.$$
> $$\dot Q=\dot n_f\,Q=0{,}499(-1\,213\,500)=-605\,500\ \text{kJ/hr}=\boxed{-168\ \text{kW}}.$$
> El signo negativo indica calor cedido (generado): $\approx168$ kW.

> [!info] Nota
> Valores de $\bar h_f^\circ$ y $\Delta\bar h$ de tablas termoquímicas; reactantes a $300$ K $\approx298$ K (sensible despreciable).

> [!referencia]
> [[Combustion/index | Combustión]] · [[Mezclas de Gases]] · [[Gas Ideal]]
