---
title: Formulario — Conversión de Energía (Ciclos)
order: 99
tags:
  - termodinamica
  - formulario
  - ciclos
draft: false
aliases:
  - formulario ciclos termodinamicos
---

# Formulario — Conversión de Energía (Ciclos)

## Rankine Simple

Estados: 1 líquido sat. ($P_L$), 2 líquido comp. ($P_H$), 3 vapor sobrecal. ($P_H,T_3$), 4 salida turbina ($P_L$).

Bomba isentrópica:
$$
h_2 = h_1 + v_1(P_H - P_L)
$$

Calidad estado 4 (mezcla húmeda):
$$
x_4 = \frac{s_3 - s_f}{s_{fg}}, \qquad h_4 = h_f + x_4\,h_{fg}
$$

Eficiencia térmica:
$$
\eta_{\rm th} = \frac{(h_3 - h_4) - (h_2 - h_1)}{h_3 - h_2}
$$

Verificación por calores: $q_L = h_4 - h_1$, $q_H = h_3 - h_2$.
$$
\eta_{\rm th} = 1 - \frac{q_L}{q_H}
$$

Turbina real (eficiencia isentrópica):
$$
\eta_T = \frac{h_3 - h_{4,\rm real}}{h_3 - h_{4s}} \implies h_{4,\rm real} = h_3 - \eta_T(h_3 - h_{4s})
$$

Bomba real:
$$
\eta_P = \frac{h_{2s} - h_1}{h_{2,\rm real} - h_1} \implies h_{2,\rm real} = h_1 + \frac{v_1(P_H - P_L)}{\eta_P}
$$

Flujo másico:
$$
\dot{m} = \frac{\dot{W}_{\rm neto}}{w_{\rm neto}}
$$

$\eta_T$: efic. isentrópica turbina; $\eta_P$: efic. bomba; $x_4$: calidad; $s_{fg}=s_g-s_f$; $h_{fg}=h_g-h_f$.

---

## Rankine con Recalentamiento

Estados: 3 entrada TAP ($P_H,T_3$), 4 salida TAP ($P_r$), 5 entrada TBP ($P_r,T_5$), 6 salida TBP ($P_L$).

Trabajo de turbina (dos etapas):
$$
w_T = (h_3 - h_4) + (h_5 - h_6)
$$

Calor de entrada (caldera + recalentador):
$$
q_H = (h_3 - h_2) + (h_5 - h_4)
$$

Calor rechazado:
$$
q_L = h_6 - h_1
$$

Eficiencia térmica:
$$
\eta_{\rm th} = \frac{(h_3-h_4)+(h_5-h_6)-(h_2-h_1)}{(h_3-h_2)+(h_5-h_4)}
$$

Presión de recalentamiento óptima: $P_r \approx P_H/4$ a $P_H/5$.

$P_r$: presión de recalentamiento; TAP/TBP: turbina alta/baja presión; $x_6\ge 0.88$.

---

## Rankine Regenerativo

Estados: 1 líq. sat. ($P_L$), 2 salida bomba 1 ($P_e$), 3 líq. sat. salida CAA ($P_e$), 4 salida bomba 2 ($P_H$), 5 entrada turbina ($P_H,T_5$), $e$ extracción ($P_e$), 6 salida turbina ($P_L$).

Fracción extraída (balance del calentador abierto CAA):
$$
y = \frac{h_3 - h_2}{h_e - h_2}
$$

Trabajo de turbina (dos etapas):
$$
w_T = (h_5 - h_e) + (1-y)(h_e - h_6)
$$

Trabajos de bombas:
$$
w_{P1} = (1-y)(h_2 - h_1) = (1-y)v_1(P_e - P_L)
$$
$$
w_{P2} = h_4 - h_3 = v_3(P_H - P_e)
$$

Calor de entrada (solo caldera):
$$
q_H = h_5 - h_4
$$

Calor rechazado (fracción $1-y$):
$$
q_L = (1-y)(h_6 - h_1)
$$

Eficiencia térmica:
$$
\eta_{\rm th} = \frac{w_T - w_{P1} - w_{P2}}{q_H}
$$

$y$: fracción de vapor extraído; $P_e$: presión de extracción; CAA: calentador abierto de alimentación.

---

## Brayton Simple

Estados: 1 entrada compresor ($T_1,P_L$), 2 salida compresor ($P_H$), 3 salida cámara ($T_3,P_H$), 4 salida turbina ($P_L$). Aire-estándar $c_p$ cte.

Relación de presiones y parámetro isentrópico:
$$
r_P = \frac{P_H}{P_L}, \qquad t = r_P^{(\gamma-1)/\gamma}
$$

Relaciones isentrópicas:
$$
T_2 = t\,T_1, \qquad T_4 = \frac{T_3}{t}
$$

Balances de energía (base 1 kg):
$$
w_C = c_p(T_2 - T_1), \qquad q_H = c_p(T_3 - T_2)
$$
$$
w_T = c_p(T_3 - T_4), \qquad w_{\rm neto} = c_p[(T_3 - T_4) - (T_2 - T_1)]
$$

Eficiencia térmica:
$$
\eta_{\rm th} = 1 - \frac{T_4 - T_1}{T_3 - T_2} = 1 - \frac{1}{r_P^{(\gamma-1)/\gamma}}
$$

Relación de trabajos (back work ratio):
$$
\text{bwr} = \frac{w_C}{w_T}
$$

Compresor real:
$$
\eta_C = \frac{T_{2s} - T_1}{T_{2r} - T_1} \implies T_{2r} = T_1 + \frac{T_{2s} - T_1}{\eta_C}
$$

Turbina real:
$$
\eta_T = \frac{T_3 - T_{4r}}{T_3 - T_{4s}} \implies T_{4r} = T_3 - \eta_T(T_3 - T_{4s})
$$

Condición de utilidad del regenerador:
$$
T_4 > T_2 \iff \frac{T_3}{T_1} > r_P^{2(\gamma-1)/\gamma}
$$

$r_P$: relación de presiones; $\gamma$: razón de calores específicos; bwr: fracción de trabajo consumida por el compresor.

---

## Brayton con Regeneración

Estados: 2 salida compresor, 5 salida recuperador (lado frío), 3 salida cámara, 4 salida turbina, 6 salida recuperador (lado caliente).

Efectividad del recuperador:
$$
\varepsilon = \frac{T_5 - T_2}{T_4 - T_2}
$$

Temperaturas del recuperador:
$$
T_5 = T_2 + \varepsilon(T_4 - T_2), \qquad T_6 = T_4 - \varepsilon(T_4 - T_2)
$$

Calor de entrada (con regeneración):
$$
q_H = c_p(T_3 - T_5)
$$

Trabajo neto (igual al simple):
$$
w_{\rm neto} = c_p[(T_3 - T_4) - (T_2 - T_1)]
$$

Eficiencia con regeneración perfecta ($\varepsilon = 1$, $T_5=T_4$):
$$
\eta_{\rm th,regen} = 1 - \frac{T_2 - T_1}{T_3 - T_4} = 1 - \frac{T_1}{T_3}\,r_P^{(\gamma-1)/\gamma}
$$

Relación de presiones de igual eficiencia (simple vs regenerativo):
$$
r_P^{*} = \left(\frac{T_3}{T_1}\right)^{\gamma/[2(\gamma-1)]}
$$

$\varepsilon$: efectividad del recuperador; $\eta_{\rm regen}$ disminuye con $r_P$ (opuesto al simple).

---

## Ciclo Otto

Estados: 1 admisión, 2 post-compresión, 3 post-combustión, 4 post-expansión. Combustión isocórica.

Relación de compresión:
$$
r = \frac{V_1}{V_2}
$$

Balances de energía (base 1 kg):
$$
q_H = c_v(T_3 - T_2), \qquad q_L = c_v(T_4 - T_1)
$$
$$
w_{\rm neto} = q_H - q_L = c_v[(T_3 - T_2) - (T_4 - T_1)]
$$

Relaciones isentrópicas:
$$
\frac{T_2}{T_1} = r^{\gamma-1}, \qquad \frac{T_3}{T_4} = r^{\gamma-1}, \qquad P_2 = P_1\,r^{\gamma}
$$

Estado tras combustión:
$$
T_3 = T_2 + \frac{q_H}{c_v}, \qquad P_3 = P_2\,\frac{T_3}{T_2}
$$

Eficiencia térmica:
$$
\eta_{\rm th} = 1 - \frac{T_1}{T_2} = 1 - \frac{1}{r^{\gamma-1}}
$$

$r$: relación de compresión; $c_v$: calor específico a volumen cte; $\gamma$: razón de calores específicos.

---

## Ciclo Diesel

Estados: 1 admisión, 2 post-compresión, 3 post-combustión (isobárica), 4 post-expansión. Rechazo isocórico.

Parámetros geométricos:
$$
r = \frac{V_1}{V_2}, \qquad r_c = \frac{V_3}{V_2} \ge 1
$$

Balances de energía (base 1 kg):
$$
q_H = c_p(T_3 - T_2), \qquad q_L = c_v(T_4 - T_1)
$$
$$
w_{\rm neto} = c_p(T_3 - T_2) - c_v(T_4 - T_1)
$$

Relaciones de temperatura:
$$
T_2 = T_1\,r^{\gamma-1}, \qquad T_3 = T_2\,r_c = T_1\,r^{\gamma-1}r_c, \qquad T_4 = T_1\,r_c^{\gamma}
$$

Presión estado 4:
$$
P_4 = P_3\left(\frac{r_c}{r}\right)^{\gamma}
$$

Factor de corte:
$$
f(r_c) = \frac{r_c^{\gamma} - 1}{\gamma(r_c - 1)} > 1 \quad (r_c > 1)
$$

Eficiencia térmica:
$$
\eta_{\rm th} = 1 - \frac{1}{r^{\gamma-1}}\cdot\frac{r_c^{\gamma} - 1}{\gamma(r_c - 1)}
$$

Límite $r_c \to 1$: converge al Otto, $\eta_{\rm th} \to 1 - r^{-(\gamma-1)}$.

$r$: relación de compresión; $r_c$: relación de corte (cutoff); $c_p,c_v$: calores específicos.

---

## Refrigeración — Compresión de Vapor (VCR)

Estados: 1 salida evaporador (vapor sat. $P_L$), 2 salida compresor ($P_H$), 3 salida condensador (líq. sat. $P_H$), 4 salida válvula ($P_L$).

Válvula isoenthálpica:
$$
h_4 = h_3
$$

Calidad a la salida de la válvula:
$$
x_4 = \frac{h_3 - h_f(P_L)}{h_{fg}(P_L)}
$$

Balances de energía (base 1 kg):
$$
w_C = h_2 - h_1, \qquad q_H = h_2 - h_3
$$
$$
q_L = h_1 - h_4 = h_1 - h_3
$$

Primera ley del ciclo:
$$
q_H = q_L + w_C
$$

Coeficientes de desempeño:
$$
\text{COP}_R = \frac{q_L}{w_C} = \frac{h_1 - h_3}{h_2 - h_1}, \qquad \text{COP}_{HP} = \frac{q_H}{w_C} = \frac{h_2 - h_3}{h_2 - h_1}
$$

Límite de Carnot (refrigerador):
$$
\text{COP}_{R,\rm Carnot} = \frac{T_L}{T_H - T_L}
$$

Flujo másico y potencia:
$$
\dot{m} = \frac{\dot{Q}_L}{q_L}, \qquad \dot{W}_C = \dot{m}\,w_C
$$

$\text{COP}_R$: coef. desempeño refrigerador; $x_4$: calidad; $T_L,T_H$: temperaturas absolutas de foco frío/caliente.

---

## Refrigeración — Bomba de Calor

Efecto útil $q_H$ (calor cedido al espacio caliente):
$$
\text{COP}_{HP} = \frac{q_H}{w_C} = \frac{h_2 - h_3}{h_2 - h_1}
$$

Relación con el refrigerador:
$$
\text{COP}_{HP} = \text{COP}_R + 1
$$

Condición de ventaja sobre resistencia eléctrica:
$$
\text{COP}_{HP} > 1 \iff q_H > w_C \iff q_L > 0
$$

Límite de Carnot (bomba de calor):
$$
\text{COP}_{HP,\rm Carnot} = \frac{T_H}{T_H - T_L}
$$

Calor cedido y calor tomado:
$$
\dot{Q}_H = \dot{W}_C\,\text{COP}_{HP}, \qquad \dot{Q}_L = \dot{Q}_H - \dot{W}_C
$$

$\text{COP}_{HP}$: coef. desempeño bomba de calor; resistencia eléctrica: $\text{COP}=1$.
