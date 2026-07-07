---
title: Formulario — Sistemas Termodinámicos
order: 99
tags:
  - termodinamica
  - formulario
  - sistemas
draft: false
aliases:
  - formulario sistemas termodinamicos
---

# Formulario — Sistemas Termodinámicos

## Sistema Cerrado

$C$: velocidad; $z$: altura; $\theta$: energía específica de corriente.

**Energía transportada por corriente**
$$\theta = \underbrace{u + Pv}_{=\,h} + \frac{C^2}{2} + gz$$

**Primera ley (SC)**
$$\Delta U = U_2 - U_1 = Q_{12} - W_{12}$$

**Segunda ley (SC)**
$$S_2 - S_1 = \int_1^2 \frac{\delta Q}{T_b} + S_{\rm gen}, \qquad S_{\rm gen}\ge 0$$

**Destrucción de exergía**
$$B_{\rm dest}=T_0 S_{\rm gen}$$

**Trabajo de frontera (cuasiestático)**
$$W_{\rm frontera}=\int_1^2 P\,dV$$

**Trabajo de frontera (irreversible, $P_{\rm ext}$ constante)**
$$W=P_{\rm ext}(V_2-V_1)$$

---

## Volumen de Control

$\dot{m}$: flujo másico [kg/s]; $C$: velocidad [m/s]; $z$: altura [m]; subíndices $i$: entrada, $e$: salida.

**Balance de masa (tasa)**
$$\frac{dm_{\rm vc}}{dt} = \sum_i\dot m_i - \sum_e\dot m_e$$

**Balance de energía (tasa)**
$$\frac{dE_{\rm vc}}{dt} = \dot Q - \dot W + \sum_i\dot m_i\theta_i - \sum_e\dot m_e\theta_e, \qquad \theta = h+\tfrac{C^2}{2}+gz$$

**Balance de entropía (tasa)**
$$\frac{dS_{\rm vc}}{dt} = \sum_k\frac{\dot Q_k}{T_k} + \sum_i\dot m_i s_i - \sum_e\dot m_e s_e + \dot S_{\rm gen}, \qquad \dot S_{\rm gen}\ge0$$

**Entalpía (propiedad natural del VC)**
$$h=u+Pv$$

---

## Flujo Estacionario (SFEE)

$q=\dot{Q}/\dot{m}$; $w=\dot{W}/\dot{m}$; $T_b$: temperatura de frontera de entrada de calor.

**Condición estacionaria**
$$\frac{dm_{\rm vc}}{dt} = 0, \qquad \frac{dE_{\rm vc}}{dt} = 0$$

**Balance de masa (1 entrada, 1 salida)**
$$\dot{m}_1 = \dot{m}_2 = \dot{m}$$

**Ecuación de energía SFEE**
$$\dot{Q} - \dot{W} = \dot{m}\!\left[(h_2-h_1) + \frac{C_2^2-C_1^2}{2} + g(z_2-z_1)\right]$$

**SFEE por unidad de masa**
$$q - w = (h_2-h_1) + \frac{C_2^2-C_1^2}{2} + g(z_2-z_1)$$

**SFEE, múltiples corrientes**
$$\dot{Q} - \dot{W} = \sum_e \dot{m}_e\theta_e - \sum_i \dot{m}_i\theta_i, \qquad \sum_i\dot{m}_i=\sum_e\dot{m}_e$$

**Balances simplificados por dispositivo**
$$\text{Turbinas / Compresores:}\quad \dot{W} = \dot{m}(h_1-h_2)$$
$$\text{Toberas / Difusores:}\quad h_1+C_1^2/2 = h_2+C_2^2/2$$
$$\text{Válvulas:}\quad h_2 = h_1$$
$$\text{Intercambiadores:}\quad \sum \dot{m}_i h_i = \sum \dot{m}_e h_e$$

**Balance de entropía (1 entrada, 1 salida)**
$$\dot{S}_{\rm gen} = \dot{m}(s_2-s_1) - \frac{\dot{Q}}{T_b} \geq 0$$

**Balance de entropía (adiabático)**
$$\dot{S}_{\rm gen} = \dot{m}(s_2-s_1) \geq 0, \qquad s_2 \geq s_1$$

---

## Turbinas

$2s$: estado isentrópico ($s_{2s}=s_1$, $P_{2s}=P_2$); $\psi$: exergía de flujo; $T_0$: temperatura de referencia.

**Trabajo de la turbina**
$$\dot{W}_t = \dot{m}(h_1 - h_2)$$

**Eficiencia isentrópica**
$$\eta_t = \frac{\dot{W}_{\rm real}}{\dot{W}_{\rm rev}} = \frac{h_1 - h_2}{h_1 - h_{2s}}$$

**Estado real de salida**
$$h_2 = h_1 - \eta_t(h_1-h_{2s})$$

**Gas ideal, $c_p$ constante**
$$\eta_t = \frac{T_1 - T_2}{T_1 - T_{2s}}, \qquad T_{2s} = T_1\!\left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma}$$

**Destrucción de exergía**
$$\dot{X}_{\rm dest} = T_0\,\dot{S}_{\rm gen} = T_0\,\dot{m}(s_2 - s_1) \geq 0$$

**Eficiencia exergética**
$$\varepsilon_t = \frac{\dot{W}_t}{\dot{m}(\psi_1-\psi_2)} = 1 - \frac{\dot{X}_{\rm dest}}{\dot{m}(\psi_1-\psi_2)}$$

**Exergía de flujo**
$$\psi = h - T_0 s - (h_0 - T_0 s_0)$$

---

## Compresores

$2s$: estado isentrópico ($s_{2s}=s_1$, $P_{2s}=P_2$); trabajo positivo = entra al sistema.

**Trabajo del compresor**
$$\dot{W}_c = \dot{m}(h_2 - h_1)$$

**Eficiencia isentrópica**
$$\eta_c = \frac{\dot{W}_{\rm rev}}{\dot{W}_{\rm real}} = \frac{h_{2s} - h_1}{h_2 - h_1}$$

**Estado real de salida**
$$h_2 = h_1 + \frac{h_{2s}-h_1}{\eta_c}$$

**Gas ideal, $c_p$ constante**
$$\eta_c = \frac{T_{2s}-T_1}{T_2-T_1}, \qquad T_{2s} = T_1\!\left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma}, \qquad T_2 = T_1 + \frac{T_{2s}-T_1}{\eta_c}$$

**Trabajo reversible (mínimo)**
$$w_{\rm rev} = \int_1^2 v\,dP$$

**Relación de presión óptima por etapa ($N$ etapas)**
$$r_{\rm opt} = \left(\frac{P_2}{P_1}\right)^{1/N}$$

**Trabajo total, $N$ etapas con interenfriamiento a $T_1$**
$$\dot{W}_{\rm total} = N\,\dot{m}\,c_p\,T_1\left[r_{\rm opt}^{(\gamma-1)/\gamma}-1\right]$$

**Trabajo mínimo isotérmico ($N\to\infty$)**
$$\dot{W}_{\rm iso} = \dot{m}RT_1\ln(P_2/P_1)$$

---

## Toberas

$h_0$: entalpía de estancamiento; $a$: velocidad del sonido; $Ma$: número de Mach.

**Balance de energía**
$$h_1 + \frac{C_1^2}{2} = h_2 + \frac{C_2^2}{2}$$

**Velocidad de salida**
$$C_2 = \sqrt{C_1^2 + 2(h_1 - h_2)}$$

**Aproximación $C_1 \ll C_2$**
$$C_2 \approx \sqrt{2(h_1-h_2)}$$

**Eficiencia de la tobera**
$$\eta_{\rm tob} = \frac{C_2^2/2}{C_{2s}^2/2} = \frac{h_1 - h_2}{h_1 - h_{2s}}$$

**Entalpía de estancamiento**
$$h_0 = h + C^2/2$$

**Gas ideal, $c_p$ constante, $C_1 \approx 0$**
$$C_2 = \sqrt{2c_p(T_1-T_2)}, \qquad T_{2s} = T_1\!\left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma}$$

**Velocidad de salida isentrópica**
$$C_{2s} = \sqrt{2c_pT_1\!\left[1-\left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma}\right]}$$

**Velocidad del sonido y Mach de salida**
$$a = \sqrt{\gamma R T}, \qquad Ma_2 = C_{2s}/a_2$$

**Relación área-velocidad**
$$\frac{dA}{A} = (Ma^2-1)\,\frac{dC}{C}$$

---

## Difusores

$2s$: estado isentrópico a la misma $P_2$ ($s_{2s}=s_1$).

**Balance de energía**
$$h_1 + \frac{C_1^2}{2} = h_2 + \frac{C_2^2}{2}$$

**Eficiencia del difusor**
$$\eta_d = \frac{h_{2s} - h_1}{h_2 - h_1} = \frac{h_{2s} - h_1}{C_1^2/2 - C_2^2/2}$$

**Gas ideal, $C_2 \approx 0$**
$$h_{2s} - h_1 = c_p(T_{2s}-T_1), \qquad \frac{P_{2s}}{P_1} = \left(\frac{T_{2s}}{T_1}\right)^{\gamma/(\gamma-1)}, \qquad T_{2s} = T_1+\frac{\eta_d C_1^2}{2c_p}$$

**Bernoulli (flujo incompresible)**
$$P + \tfrac{1}{2}\rho C^2 = \text{cte}$$

**Temperatura de estancamiento isentrópica**
$$T_{0s} = T_\infty + \frac{C_1^2}{2c_p}$$

**Presión de estancamiento isentrópica**
$$P_{0s} = P_\infty\!\left(\frac{T_{0s}}{T_\infty}\right)^{\gamma/(\gamma-1)}$$

---

## Válvulas de Estrangulamiento

$\mu_{\rm JT}$: coeficiente Joule–Thomson; $T_{\rm inv}$: temperatura de inversión.

**Balance de energía (isoentálpico)**
$$h_1 = h_2$$

**Balance de entropía (irreversible)**
$$\dot{S}_{\rm gen} = \dot{m}(s_2-s_1) \geq 0, \qquad s_2 > s_1$$

**Coeficiente de Joule–Thomson**
$$\mu_{\rm JT} = \left(\frac{\partial T}{\partial P}\right)_h$$

**Título de vapor a la salida (ciclo de refrigeración)**
$$x_4 = \frac{h_3 - h_{f}(P_4)}{h_{fg}(P_4)}$$

**COP de refrigeración**
$$\mathrm{COP_R} = \frac{q_L}{w_c} = \frac{h_1-h_4}{h_2-h_1}$$

**Trabajo potencial perdido**
$$w_{\rm perdido}=T_0(s_4-s_3)$$

---

## Intercambiadores de Calor

Subíndices $h$: corriente caliente; $c$: corriente fría; $1$: entrada, $2$: salida.

**Conservación de masa**
$$\dot{m}_h = \text{cte}, \qquad \dot{m}_c = \text{cte}$$

**Primera ley**
$$\dot{Q} = \dot{m}_h(h_{h,1}-h_{h,2}) = \dot{m}_c(h_{c,2}-h_{c,1})$$

**Primera ley, $c_p$ constante**
$$\dot{Q} = \dot{m}_h c_{p,h}(T_{h,1}-T_{h,2}) = \dot{m}_c c_{p,c}(T_{c,2}-T_{c,1})$$

**Segunda ley**
$$\dot{S}_{\rm gen} = \dot{m}_h(s_{h,2}-s_{h,1}) + \dot{m}_c(s_{c,2}-s_{c,1}) \geq 0$$

**Capacidades térmicas y razón**
$$C_h = \dot{m}_h c_{p,h}, \quad C_c = \dot{m}_c c_{p,c}, \quad C_r = \frac{C_{\rm min}}{C_{\rm max}} \leq 1$$

**Número de unidades de transferencia**
$$NTU = UA/C_{\rm min}$$

**Calor máximo y eficiencia**
$$\dot{Q}_{\rm max} = C_{\rm min}(T_{h,1}-T_{c,1}), \qquad \varepsilon = \dot{Q}/\dot{Q}_{\rm max}$$

**Contraflujo, $C_r < 1$**
$$\varepsilon = \frac{1 - e^{-NTU(1-C_r)}}{1 - C_r\,e^{-NTU(1-C_r)}}$$

**Contraflujo, $C_r = 1$**
$$\varepsilon = \frac{NTU}{1+NTU}$$

**Flujo paralelo**
$$\varepsilon = \frac{1-e^{-NTU(1+C_r)}}{1+C_r}$$

**Cambio de fase ($C_r=0$)**
$$\varepsilon = 1 - e^{-NTU}$$

**Cambio de fase (condensación total)**
$$\dot{Q} = \dot{m}_h\,h_{fg}$$

**Temperatura de aproximación**
$$\Delta T_{\rm approach} = T_{\rm sat} - T_{c,2}$$

**Factor de obstrucción (fouling)**
$$\frac{1}{U_{\rm real}} = \frac{1}{U_{\rm limpio}} + R_f$$

---

## Flash (Vaporización Instantánea)

$F,V,L$: caudales de alimentación, vapor, líquido; $z_i,y_i,x_i$: fracciones molares; $K_i$: constante de equilibrio; $\Psi=V/F$.

**Balance de masa global**
$$F = V + L$$

**Balance de masa por componente**
$$F z_i = V y_i + L x_i \quad \forall\,i$$

**Balance de energía**
$$F h_F = V H_V + L h_L$$

**Equilibrio de fases (Raoult modificada)**
$$y_i = K_i(T_{\rm tambor}, P_{\rm tambor})\,x_i, \qquad K_i \approx \frac{P_i^{\rm sat}(T_{\rm tambor})}{P_{\rm tambor}}$$

**Composiciones**
$$x_i = \frac{z_i}{1 + \Psi(K_i-1)}, \qquad y_i = \frac{K_i z_i}{1 + \Psi(K_i-1)}$$

**Ecuación de Rachford-Rice**
$$\sum_i \frac{z_i(K_i-1)}{1+\Psi(K_i-1)} = 0$$

**Balance de entropía**
$$\dot{S}_{\rm gen} = V s_V + L s_L - F s_F \geq 0$$

**Condición de existencia del flash**
$$\sum_i z_i/K_i < 1 < \sum_i z_i K_i$$
