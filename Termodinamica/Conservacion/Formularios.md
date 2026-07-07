---
title: Formulario — Conservación de Masa y Energía
order: 99
tags:
  - termodinamica
  - formulario
  - conservacion
draft: false
aliases:
  - formulario conservacion
---

# Formulario — Conservación de Masa y Energía

## Primera Ley (Sistema Cerrado)

Primera ley (integral y diferencial):
$$\Delta U = Q - W, \qquad dU = \delta Q - \delta W.$$
$U$: energía interna [kJ]; $Q>0$: calor que entra; $W>0$: trabajo que sale.

Definición de $U$ como función de estado:
$$U_2 - U_1 = \Delta U \equiv Q - W.$$

Trabajo de frontera:
$$\delta W_b = P_{\rm ext}\,dV, \qquad W_b = \int_1^2 P\,dV \quad (\text{cuasiestático}).$$

Proceso irreversible:
$$W_{\rm irr} < \int_1^2 P\,dV.$$

Isocórico ($V=\text{cte}$):
$$\Delta U = Q_v.$$

Isobárico ($P=\text{cte}$):
$$Q_P = \Delta U + P\Delta V = \Delta(U+PV) = \Delta H.$$

Adiabático ($Q=0$):
$$\Delta U = -W.$$

Ciclo ($\Delta U = 0$):
$$Q_{\rm neto} = W_{\rm neto}.$$

Gas ideal ($u=u(T)$):
$$du = c_v(T)\,dT, \qquad \Delta u = \int_{T_1}^{T_2} c_v(T)\,dT, \qquad \Delta u = c_v\,\Delta T \;(c_v\ \text{cte}).$$

Trabajo isotérmico reversible (gas ideal):
$$W = mRT\ln\frac{V_2}{V_1} = mRT\ln\frac{P_1}{P_2}.$$

Relación isentrópica (adiabático reversible, gas ideal):
$$T_2 = T_1\left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma}.$$

Relación de Gibbs (procesos reversibles):
$$dU = T\,dS - P\,dV.$$

## Segunda Ley (Sistema Cerrado)

Balance de entropía (integral y diferencial):
$$S_2 - S_1 = \int_1^2 \frac{\delta Q}{T_b} + S_{\rm gen}, \qquad dS = \frac{\delta Q}{T_b} + \delta S_{\rm gen}, \qquad S_{\rm gen}\ge 0.$$
$T_b$: temperatura de frontera; $S_{\rm gen}$: entropía generada.

Cálculo de $S_{\rm gen}$ (proceso real):
$$S_{\rm gen} = \Delta S - \int_1^2 \frac{\delta Q_{\rm real}}{T_b} \ge 0.$$

Desigualdad de Clausius:
$$\oint \frac{\delta Q}{T_b} \le 0 \quad (= 0 \text{ reversible}).$$

Eficiencia de Carnot auxiliar (deducción de Clausius):
$$\frac{\delta Q_{0k}}{\delta Q_k} = \frac{T_0}{T_k}, \qquad Q_{0,\rm ciclo} = T_0\oint\frac{\delta Q}{T_b}.$$

Adiabático ($\delta Q = 0$):
$$\Delta S = S_{\rm gen} \ge 0 \quad (\text{isentrópico si reversible: } \Delta S = 0).$$

Reversible:
$$\Delta S = \int_1^2 \frac{\delta Q_{\rm rev}}{T}.$$

Isotérmico reversible:
$$\Delta S = \frac{Q_{\rm rev}}{T}.$$

Gas ideal (proceso reversible):
$$\Delta s = c_p\ln\frac{T_2}{T_1} - R\ln\frac{P_2}{P_1} = c_v\ln\frac{T_2}{T_1} + R\ln\frac{v_2}{v_1}.$$

Sustancia incompresible ($c_p = c_v = c$):
$$\Delta s = c\ln\frac{T_2}{T_1}.$$

Expansión libre (gas ideal, $V_2=2V_1$):
$$S_{\rm gen} = mR\ln\frac{V_2}{V_1} = mR\ln 2.$$

Mezcla térmica (dos cuerpos, aislado):
$$T_f = \frac{T_A+T_B}{2}, \qquad S_{\rm gen} = C\ln\frac{T_f}{T_A} + C\ln\frac{T_f}{T_B} \ge 0.$$

## Balance de Exergía (Sistema Cerrado)

Balance de exergía:
$$\Delta B = \int_1^2\!\left(1-\frac{T_0}{T}\right)\delta Q - \left[W - P_0(V_2-V_1)\right] - B_{\rm dest}.$$
$T_0,P_0$: estado muerto; $B_{\rm dest}$: exergía destruida.

Exergía del sistema cerrado:
$$B = (U - U_0) + P_0(V - V_0) - T_0(S - S_0).$$

Gouy-Stodola:
$$B_{\rm dest} = T_0\,S_{\rm gen} \ge 0.$$

Trabajo útil:
$$W_{\rm útil} = W - P_0\Delta V, \qquad W_{\rm útil,\,máx} = -\Delta B \quad (B_{\rm dest}=0).$$

Adiabático ($\delta Q = 0$):
$$\Delta B = -(W - P_0\Delta V) - B_{\rm dest}.$$

Isotérmico ($T=\text{cte}$):
$$\Delta B = \left(1-\frac{T_0}{T}\right)Q - (W - P_0\Delta V) - B_{\rm dest}.$$

Sistema aislado ($Q=0$, $W=0$):
$$\Delta B = -B_{\rm dest} \le 0.$$

Eficiencia exergética (expansión):
$$\epsilon = \frac{W_{\rm útil}}{-\Delta B + \int(1-T_0/T)\delta Q} = 1 - \frac{B_{\rm dest}}{-\Delta B + \int(1-T_0/T)\delta Q}.$$

Eficiencia exergética (compresión):
$$\epsilon = \frac{W_{\rm útil,\,min}}{W_{\rm útil}} = 1 - \frac{B_{\rm dest}}{W_{\rm útil}}.$$

## Balance de Masa (Volumen de Control)

Balance de masa:
$$\frac{dm_{VC}}{dt} = \sum_i \dot{m}_i - \sum_e \dot{m}_e.$$
$\dot m$: flujo másico [kg/s]; $m$: masa [kg].

Flujo másico:
$$\dot{m} = \rho V A = \frac{V A}{v} = \int_A \rho\,V_n\,dA \quad [\text{kg/s}].$$

Régimen estacionario (continuidad):
$$\sum_i \dot{m}_i = \sum_e \dot{m}_e, \qquad \rho_1 V_1 A_1 = \rho_2 V_2 A_2.$$

Fluido incompresible ($\rho=\text{cte}$):
$$V_1 A_1 = V_2 A_2, \qquad \frac{V_2}{V_1} = \frac{A_1}{A_2}.$$

No estacionario (forma integral):
$$m_2 - m_1 = \sum_i m_i - \sum_e m_e.$$

## Balance de Energía (Volumen de Control)

Balance de energía:
$$\frac{dE_{VC}}{dt} = \dot{Q} - \dot{W} + \sum_i \dot{m}_i\!\left(h_i + \frac{V_i^2}{2} + gz_i\right) - \sum_e \dot{m}_e\!\left(h_e + \frac{V_e^2}{2} + gz_e\right).$$
$h = u + Pv$: entalpía específica; $\dot Q$: calor que entra; $\dot W$: trabajo de eje que sale.

Trabajo de flujo:
$$W_{\rm flujo} = P v \quad [\text{kJ/kg}].$$

Energía transportada por el flujo:
$$e_{\rm total} = u + Pv + \frac{V^2}{2} + gz = h + \frac{V^2}{2} + gz.$$

Régimen estacionario (SFSS, 1 entrada/1 salida):
$$\dot{Q} - \dot{W} = \dot{m}\!\left[(h_e - h_i) + \frac{V_e^2 - V_i^2}{2} + g(z_e - z_i)\right].$$

Forma específica:
$$q - w = (h_e - h_i) + \frac{V_e^2 - V_i^2}{2} + g(z_e - z_i), \qquad q=\frac{\dot Q}{\dot m},\; w=\frac{\dot W}{\dot m}.$$

Tobera/difusor ($\dot W = 0$):
$$h_1 + \frac{V_1^2}{2} = h_2 + \frac{V_2^2}{2}.$$

Turbina adiabática:
$$w_{\rm turbina} = h_1 - h_2 > 0.$$

Compresor/bomba adiabático:
$$w_{\rm compresor} = h_2 - h_1 > 0.$$

Caldera/condensador ($\dot W = 0$):
$$q = h_e - h_i.$$

Válvula de estrangulamiento (isentálpico):
$$h_1 = h_2.$$

## Balance de Entropía (Volumen de Control)

Balance de entropía:
$$\frac{dS_{VC}}{dt} = \sum_k \frac{\dot{Q}_k}{T_k} + \sum_i \dot{m}_i s_i - \sum_e \dot{m}_e s_e + \dot{S}_{\rm gen}, \qquad \dot{S}_{\rm gen}\ge 0.$$
$T_k$: temperatura de frontera; $s$: entropía específica.

Régimen estacionario (1 entrada/1 salida):
$$\dot{S}_{\rm gen} = \dot{m}(s_e - s_i) - \sum_k \frac{\dot{Q}_k}{T_k} \ge 0.$$

Forma específica:
$$s_{\rm gen} = (s_e - s_i) - \sum_k \frac{q_k}{T_k} \ge 0.$$

Adiabático ($\dot Q_k = 0$):
$$\dot{S}_{\rm gen} = \dot{m}(s_e - s_i) \ge 0 \implies s_e \ge s_i.$$

Vínculo con exergía:
$$\dot{B}_{\rm dest} = T_0\,\dot{S}_{\rm gen}.$$

Isentrópico ideal:
$$s_e = s_i \quad (s_{\rm gen} = 0).$$

Eficiencia isentrópica — turbina:
$$\eta_T = \frac{w_{\rm real}}{w_s} = \frac{h_1 - h_2}{h_1 - h_{2s}}.$$

Eficiencia isentrópica — compresor:
$$\eta_C = \frac{w_s}{w_{\rm real}} = \frac{h_{2s} - h_1}{h_2 - h_1}.$$

Eficiencia isentrópica — tobera:
$$\eta_N = \frac{V_e^2}{V_{es}^2} = \frac{h_1 - h_e}{h_1 - h_{es}}.$$

Entropía en intercambiador (gas ideal/incompresible, isobárico):
$$\Delta s = c_p\ln\frac{T_2}{T_1}.$$

## Balance de Exergía (Volumen de Control)

Balance de exergía (estacionario, 1 entrada/1 salida):
$$\dot{W}_{\rm útil} = \dot{m}(\psi_1 - \psi_2) + \sum_k\!\left(1 - \frac{T_0}{T_k}\right)\dot{Q}_k - \dot{B}_{\rm dest}.$$
$\psi$: exergía de flujo [kJ/kg]; $\dot B_{\rm dest}$: destrucción de exergía [kW].

Exergía de flujo:
$$\psi = (h - h_0) - T_0(s - s_0) + \frac{V^2}{2} + gz \quad [\text{kJ/kg}].$$

Gouy-Stodola:
$$\dot{B}_{\rm dest} = T_0\,\dot{S}_{\rm gen} \ge 0.$$

Exergía de flujo con gas ideal:
$$\psi = c_p(T - T_0) - T_0\!\left[c_p\ln\frac{T}{T_0} - R\ln\frac{P}{P_0}\right].$$

Eficiencia exergética — turbina:
$$\epsilon_T = \frac{\dot{W}}{\dot{m}(\psi_1 - \psi_2)} = 1 - \frac{\dot{B}_{\rm dest}}{\dot{m}(\psi_1 - \psi_2)}.$$

Eficiencia exergética — compresor:
$$\epsilon_C = \frac{\dot{m}(\psi_2 - \psi_1)}{\dot{W}} = 1 - \frac{\dot{B}_{\rm dest}}{\dot{W}}.$$

Eficiencia exergética — intercambiador:
$$\epsilon_{HX} = \frac{\dot{m}_C(\psi_{C,2} - \psi_{C,1})}{\dot{m}_H(\psi_{H,1} - \psi_{H,2})}.$$
