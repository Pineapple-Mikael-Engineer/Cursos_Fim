---
title: Formulario — Mezclas, Psicrometría y Combustión
order: 99
tags:
  - termodinamica
  - formulario
  - mezclas
  - combustion
draft: false
aliases:
  - formulario mezclas y psicrometria
  - formulario combustion
---

# Formulario — Mezclas, Psicrometría y Combustión

## Mezclas de gases ideales

$$y_i = \frac{n_i}{n}, \qquad \sum_i y_i = 1, \qquad fm_i = \frac{m_i}{m}, \qquad \sum_i fm_i = 1$$
Fracción molar y másica. $n=\sum_i n_i$; $m=\sum_i m_i$.

$$M = \frac{m}{n} = \sum_i y_i M_i = \frac{1}{\displaystyle\sum_k fm_k/M_k}$$
Masa molecular aparente. $M_i$: masa molar del componente $i$.

$$y_i = \frac{fm_i/M_i}{\displaystyle\sum_k fm_k/M_k}, \qquad fm_i = \frac{y_i M_i}{M}$$
Conversión entre fracción másica y molar.

$$P_i = \frac{n_i R_u T}{V} = y_i\,P, \qquad P = \sum_i P_i$$
Ley de Dalton (presiones parciales). $P_i$: presión parcial; $R_u$: constante universal.

$$V_i = \frac{n_i R_u T}{P} = y_i\,V, \qquad \sum_i V_i = V, \qquad \frac{V_i}{V} = y_i$$
Ley de Amagat (volúmenes parciales); la fracción volumétrica iguala a la molar.

$$\bar{u} = \sum_i y_i\,\bar{u}_i(T), \qquad \bar{h} = \sum_i y_i\,\bar{h}_i(T)$$
Energía interna y entalpía molares de la mezcla (solo función de $T$).

$$\bar{c}_v = \sum_i y_i\,\bar{c}_{v,i}, \qquad \bar{c}_p = \sum_i y_i\,\bar{c}_{p,i}, \qquad \gamma = \frac{\bar{c}_p}{\bar{c}_v}$$
Calores específicos molares de la mezcla.

$$\bar{s} = \sum_i y_i\,\bar{s}_i(T, P_i) = \sum_i y_i\left[\bar{s}_i^\circ(T) - R_u\ln\frac{P_i}{P^\circ}\right]$$
Entropía molar (evaluada a presiones parciales). $\bar{s}_i^\circ$: entropía estándar; $P^\circ$: presión de referencia.

$$\Delta \bar{s}_{\rm mezcla} = -R_u\sum_i y_i\ln y_i \geq 0$$
Aumento de entropía al mezclar gases distintos (solo gases distinguibles).

$$\Delta\bar{h} = \bar{c}_p(T_2-T_1), \qquad \Delta\bar{s} = \bar{c}_p\ln\frac{T_2}{T_1} - R_u\ln\frac{P_2}{P_1}$$
Cambios de propiedad a composición constante entre $(T_1,P_1)$ y $(T_2,P_2)$.

$$T_{2s} = T_1\left(\frac{P_2}{P_1}\right)^{R_u/\bar{c}_p}$$
Temperatura de salida en proceso isentrópico ($\Delta\bar{s}=0$).

## Aire húmedo — fundamentos (psicrometría)

$$\omega \equiv \frac{m_v}{m_a} = \frac{n_v M_v}{n_a M_a} = 0.622\,\frac{P_v}{P - P_v}$$
Razón de humedad [kg vapor/kg a.s.]. $M_a=28.97$, $M_v=18.015$; $P_v$: presión parcial del vapor.

$$P_v = \frac{\omega\,P}{0.622 + \omega}$$
Presión parcial del vapor en función de $\omega$.

$$\phi \equiv \frac{P_v}{P_{\rm sat}(T)} \in [0,\,1]$$
Humedad relativa. $P_{\rm sat}(T)$: presión de saturación a $T$.

$$\omega = 0.622\,\frac{\phi\,P_{\rm sat}(T)}{P - \phi\,P_{\rm sat}(T)}$$
Razón de humedad en función de $\phi$ y $T$.

$$P_{\rm sat}(T_d) = P_v = \frac{\omega\,P}{0.622+\omega}$$
Temperatura de rocío $T_d$ (saturación a $\omega$ y $P$ constantes).

$$\omega = \omega_{bh} - \frac{c_{pa}(T - T_{bh})}{h_{fg}(T_{bh})}, \qquad \omega_{bh} = 0.622\,\frac{P_{\rm sat}(T_{bh})}{P - P_{\rm sat}(T_{bh})}$$
Saturador adiabático (bulbo húmedo $T_{bh}$). $c_{pa}=1.005$; $h_{fg}$: calor latente.

$$h = c_{pa}\,T + \omega\,(h_{fg,0} + c_{pv}\,T) = (1.005 + 1.86\,\omega)\,T + 2501\,\omega$$
Entalpía por kg de aire seco [kJ/kg a.s.], $T$ en °C. $c_{pv}=1.86$; $h_{fg,0}=2501$.

## Carta psicrométrica

$$\left.\frac{d\omega}{dT}\right|_{T_{bh}} \approx -\frac{c_{pa}}{h_{fg}(T_{bh})} \approx -\frac{1.005}{2450} \approx -4.1\times10^{-4}$$
Pendiente de las líneas de bulbo húmedo constante [(kg/kg)/K].

$$\left.\frac{d\omega}{dT}\right|_h = -\frac{1.005 + 1.86\,\omega}{2501 + 1.86\,T}$$
Pendiente de las líneas de entalpía constante.

$$v = \frac{R_a\,T}{P - P_v} = \frac{0.2870\,(T+273.15)}{P - \omega P/(0.622+\omega)}$$
Volumen específico por kg de aire seco [m³/kg a.s.]. $R_a=0.2870$; $T$ en °C.

## Procesos psicrométricos

$$\dot{Q}_{\rm cal} = \dot{m}_a(h_2-h_1) = \dot{m}_a\,(1.005+1.86\,\omega)\,(T_2-T_1)$$
Calentamiento/enfriamiento sensible ($\omega$ constante). $\dot{m}_a$: flujo de aire seco.

$$\omega_2 = 0.622\,\frac{P_{\rm sat}(T_2)}{P - P_{\rm sat}(T_2)}$$
Salida saturada ($\phi=100\%$) en enfriamiento con deshumidificación.

$$\dot{m}_{\rm cond} = \dot{m}_a(\omega_1 - \omega_2)$$
Masa de condensado retirado.

$$\dot{Q}_{\rm enfr} = \dot{m}_a\left[(h_2 - h_1) - (\omega_1-\omega_2)\,h_f(T_2)\right]$$
Calor de enfriamiento-deshumidificación. $h_f(T_2)$: entalpía del líquido a $T_2$.

$$h_2 = h_1 + (\omega_2-\omega_1)\,h_g(T_v)$$
Humidificación por inyección de vapor saturado a $T_v$. $h_g$: entalpía del vapor saturado.

$$\dot{m}_{a3} = \dot{m}_{a1} + \dot{m}_{a2}, \qquad \omega_3 = \frac{\dot{m}_{a1}\,\omega_1 + \dot{m}_{a2}\,\omega_2}{\dot{m}_{a1}+\dot{m}_{a2}}, \qquad h_3 = \frac{\dot{m}_{a1}\,h_1 + \dot{m}_{a2}\,h_2}{\dot{m}_{a1}+\dot{m}_{a2}}$$
Mezcla adiabática de dos corrientes.

$$\frac{d(1\text{-}3)}{d(2\text{-}3)} = \frac{\dot{m}_{a2}}{\dot{m}_{a1}}$$
Regla de la palanca psicrométrica (posición del estado de mezcla en la carta).

## Torres de enfriamiento

$$\text{Rango} = T_3 - T_4, \qquad \text{Aproximación} = T_4 - T_{bh,1}$$
Parámetros de rendimiento. $T_3,T_4$: agua caliente/fría; $T_{bh,1}$: bulbo húmedo del aire entrante.

$$\dot{m}_4 = \dot{m}_3 - \dot{m}_a(\omega_2 - \omega_1)$$
Balance de masa de agua (agua fría de salida).

$$\dot{m}_{\rm maq} = \dot{m}_a(\omega_2 - \omega_1)$$
Agua de maquillaje (repone lo evaporado).

$$\frac{\dot{m}_3}{\dot{m}_a} = \frac{(h_{a2}-h_{a1}) - (\omega_2-\omega_1)\,h_f(T_4)}{h_f(T_3) - h_f(T_4)}$$
Razón de flujos agua/aire (del balance de energía).

$$\dot{m}_3 = \frac{\dot{Q}_{\rm cond}}{h_f(T_3)-h_f(T_4)}$$
Flujo de agua caliente a partir del calor rechazado en el condensador.

## Combustión — Estequiometría

$$\mathrm{C_xH_y} + a_{\rm est}(\mathrm{O_2}+3.76\,\mathrm{N_2}) \to x\,\mathrm{CO_2} + \frac{y}{2}\mathrm{H_2O} + 3.76\,a_{\rm est}\,\mathrm{N_2}$$
Combustión completa estequiométrica de $\mathrm{C_xH_y}$; aire seco $\approx 21\%\,\mathrm{O_2}+79\%\,\mathrm{N_2}$ ($3.76\,\mathrm{N_2}$ por $\mathrm{O_2}$).

$$a_{\rm est} = x + \frac{y}{4}$$
Moles estequiométricos de $\mathrm{O_2}$ (del balance $2a_{\rm est}=2x+y/2$).

## Combustión — Relación aire-combustible y exceso

$$\mathrm{AF} = \frac{m_{\rm aire}}{m_{\rm comb}} = \frac{a_{\rm est}/\Phi\times(M_{\mathrm{O_2}}+3.76\,M_{\mathrm{N_2}})}{M_{\rm comb}} = \frac{a_{\rm est}/\Phi\times137.28}{M_{\rm comb}}$$
Relación aire-combustible másica. $\Phi$: relación de equivalencia; $137.28=32+3.76\times28$.

$$\Phi = \frac{\mathrm{AF}_{\rm est}}{\mathrm{AF}}$$
Relación de equivalencia ($\Phi<1$ pobre; $\Phi=1$ estequiométrica; $\Phi>1$ rica).

$$e = \left(\frac{1}{\Phi} - 1\right)\times100\%$$
Porcentaje de exceso de aire (positivo para mezcla pobre).

$$\mathrm{C_xH_y} + \frac{a_{\rm est}}{\Phi}(\mathrm{O_2}+3.76\,\mathrm{N_2}) \to x\,\mathrm{CO_2} + \frac{y}{2}\mathrm{H_2O} + a_{\rm est}\!\left(\frac{1}{\Phi}-1\right)\mathrm{O_2} + 3.76\,\frac{a_{\rm est}}{\Phi}\,\mathrm{N_2}$$
Combustión completa con exceso de aire (mezcla pobre, $\Phi<1$).

$$n_{\mathrm{O_2,exceso}} = a_{\rm est}\!\left(\frac{1}{\Phi}-1\right), \qquad n_{\mathrm{N_2}} = 3.76\,\frac{a_{\rm est}}{\Phi}$$
$\mathrm{O_2}$ sobrante y $\mathrm{N_2}$ en productos.

## Combustión — Combustión incompleta (mezcla rica)

$$\mathrm{C_xH_y}+a(\mathrm{O_2}+3.76\,\mathrm{N_2})\to b\,\mathrm{CO_2}+(x-b)\mathrm{CO}+\frac{y}{2}\mathrm{H_2O}+3.76a\,\mathrm{N_2}$$
Balanceo con CO en productos para $a<a_{\rm est}$ (equilibrio parcial).

$$b = 2a - x - \frac{y}{2}$$
Moles de $\mathrm{CO_2}$; existe CO si $(x+y/2)/2 \le a \le a_{\rm est}=x+y/4$.

## Combustión — Análisis de Orsat

$$n_{\mathrm{O_2,aire}} = \frac{n_{\mathrm{N_2}}}{3.76}, \qquad n_C = n_{\mathrm{CO_2}}+n_{\mathrm{CO}}, \qquad n_{\rm comb} = \frac{n_C}{x}$$
Balances de N₂ y C (base 100 mol de gases secos). $y_{\mathrm{CO_2}}+y_{\mathrm{O_2}}+y_{\mathrm{CO}}+y_{\mathrm{N_2}}=1$.

$$n_{\mathrm{H_2O}} = 2n_{\mathrm{O_2,aire}} - 2n_{\mathrm{CO_2}} - n_{\mathrm{CO}} - 2n_{\mathrm{O_2,gases}}$$
Agua condensada (no medida por Orsat) del balance de O.

$$\mathrm{AF} = \frac{n_{\mathrm{O_2,aire}}\times137.28}{n_C\times M_C + n_H\times M_H}$$
Relación AF real reconstruida del análisis de Orsat.

$$\eta_{\rm comb} = 1 - \frac{n_{\mathrm{CO}}\times|{\bar{h}_{R,\mathrm{CO}}}|}{n_{\rm comb}\times\mathrm{PCI}}, \qquad |\bar{h}_{R,\mathrm{CO}}| = 282\,990\,\mathrm{kJ/kmol}$$
Eficiencia de combustión (pérdida por CO en gases).

## Combustión — Entalpía de reacción y poder calorífico

$$\bar{h}_R^\circ = \sum_{\rm prod} n_i\,\bar{h}_{f,i}^\circ - \sum_{\rm react} n_j\,\bar{h}_{f,j}^\circ$$
Entalpía de reacción a $T^\circ=25\,°\mathrm{C}$; $\bar{h}_f^\circ=0$ para elementos estables. Combustión: $\bar{h}_R^\circ<0$.

$$\mathrm{PCS} = -\bar{h}_R^\circ\big|_{\mathrm{H_2O(l)}}, \qquad \mathrm{PCI} = -\bar{h}_R^\circ\big|_{\mathrm{H_2O(g)}}$$
Poder calorífico superior (agua líquida) e inferior (agua vapor).

$$\mathrm{PCS} = \mathrm{PCI} + \frac{n_{\mathrm{H_2O}}\times M_{\mathrm{H_2O}}}{M_{\rm comb}}\times h_{fg}(25\,°\mathrm{C})$$
Diferencia PCS–PCI (calor de condensación); $h_{fg}(25\,°\mathrm{C})=2441.7\,\mathrm{kJ/kg}$.

## Combustión — Temperatura adiabática de llama

$$H_{\rm react}(T_R) = H_{\rm prod}(T_{\rm AFT})$$
Balance de entalpía en cámara adiabática ($\dot{Q}=0$, $\dot{W}=0$).

$$H = \sum_i n_i\,\bar{h}_i(T) = \sum_i n_i\!\left[\bar{h}_{f,i}^\circ + \Delta\bar{h}_i(T)\right], \qquad \Delta\bar{h}_i(T) = \bar{h}_i(T) - \bar{h}_i(T^\circ)$$
Entalpía total de una corriente; $\Delta\bar{h}_i$: entalpía sensible desde $T^\circ=298.15\,\mathrm{K}$.

$$-\bar{h}_R^\circ = \sum_i n_i\,\Delta\bar{h}_i(T_{\rm AFT})$$
Balance para reactivos a $T_R=T^\circ$ (calor de reacción $\to$ calor sensible de productos).

$$T_{\rm AFT}^{(0)} \approx T_R + \frac{-\bar{h}_R^\circ}{\displaystyle\sum_i n_i\,\bar{c}_{p,i}^{\rm medio}}$$
Estimación inicial con calores específicos medios.

$$T_{\rm AFT} = T_a + \frac{-\bar{h}_R^\circ - \sum_i n_i\,\Delta\bar{h}_i(T_a)}{\sum_i n_i\,\Delta\bar{h}_i(T_b) - \sum_i n_i\,\Delta\bar{h}_i(T_a)}\times(T_b-T_a)$$
Interpolación lineal entre $T_a$ y $T_b$ con tablas de entalpía (JANAF).
