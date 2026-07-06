---
title: Formulario — Propiedades Termodinámicas
order: 99
tags:
  - termodinamica
  - formulario
  - propiedades
draft: false
aliases:
  - formulario propiedades termodinamicas
---

# Formulario — Propiedades Termodinámicas

## Presión

**Definición**
$$P = \lim_{\delta A \to 0} \frac{\delta F_n}{\delta A} \quad [\text{Pa} = \text{N/m}^2]$$

**Escalas de referencia**
$$P_{abs} = P_{atm} + P_{man} \qquad P_{vac} = P_{atm} - P_{abs}$$

**Variación hidrostática**
$$\frac{dP}{dz} = -\rho g \qquad \Delta P = \rho g h$$

**Gas ideal**
$$Pv = RT \qquad Z = \frac{Pv}{RT}$$

**Relaciones**
$$\delta W = P\,dV \qquad dH = T\,dS + V\,dP \qquad dG = -S\,dT + V\,dP$$
$$\left(\frac{\partial S}{\partial P}\right)_T = -\left(\frac{\partial V}{\partial T}\right)_P$$

$P$: presión absoluta; $P_{sat}$: presión de saturación; $\rho$: densidad.

## Temperatura

**Escala termodinámica (Carnot)**
$$\frac{Q_C}{Q_H} = \frac{T_C}{T_H} \qquad T_{\text{triple, agua}} = 273.16\,\text{K}$$

**Termómetro de gas ideal**
$$T = \lim_{P \to 0} \frac{P v}{R}$$

**Definición desde la relación fundamental**
$$T \equiv \left(\frac{\partial U}{\partial S}\right)_V$$

**Interpretación estadística (gas monoatómico)**
$$\frac{3}{2}k_B T = \frac{1}{2}m\langle v^2 \rangle \qquad T = \frac{m\langle v^2\rangle}{3k_B} \qquad v_{\rm rms} = \sqrt{\frac{3RT}{M}}$$

**Conversión Celsius–Kelvin**
$$T\,[\text{K}] = T\,[°\text{C}] + 273.15 \qquad \Delta T\,[\text{K}] = \Delta T\,[°\text{C}]$$

**Variables naturales**
$$dF = -S\,dT - P\,dV \qquad dG = -S\,dT + V\,dP$$
$$c_v = \left(\frac{\partial u}{\partial T}\right)_v \qquad c_p = \left(\frac{\partial h}{\partial T}\right)_P \qquad \delta Q_{\rm rev} = T\,dS$$

$k_B = 1.381\times10^{-23}\,\text{J/K}$; $R_u = 8.314\,\text{J/(mol·K)}$.

## Volumen específico

**Definición**
$$v \equiv \frac{V}{m} \quad [\text{m}^3/\text{kg}] \qquad \rho = \frac{1}{v}$$

**Extensivo, específico, molar**
$$\bar{v} = \frac{V}{n} \qquad V = mv = n\bar{v} \qquad m = nM \qquad \bar{v} = Mv$$

**Región bifásica (regla de la palanca)**
$$v = v_f + x\,v_{fg} \qquad v_{fg} = v_g - v_f$$

**Gas ideal / líquido incompresible**
$$v = \frac{RT}{P} \qquad v \approx v_f(T)$$
$$h(T,P) \approx h_f(T) + v_f\,[P - P_{sat}(T)]$$

**Trabajo de frontera y coeficientes**
$$w = \int_1^2 P\,dv \qquad \alpha \equiv \frac{1}{v}\left(\frac{\partial v}{\partial T}\right)_P \qquad \kappa_T \equiv -\frac{1}{v}\left(\frac{\partial v}{\partial P}\right)_T$$

$v_f, v_g$: líquido y vapor saturados; $\bar v$: molar.

## Calidad

**Definición**
$$x = \frac{m_g}{m_g + m_f} = \frac{m_{vapor}}{m_{total}}, \qquad 0 \le x \le 1$$

**Regla de la palanca (propiedad genérica $y\in\{v,u,h,s\}$)**
$$y = y_f + x\,y_{fg}, \qquad y_{fg} = y_g - y_f \qquad x = \frac{y - y_f}{y_{fg}}$$

**Fracción volumétrica de vapor**
$$\frac{V_g}{V} = \frac{x\,v_g}{v_f + x\,v_{fg}}$$

$x$: fracción másica de vapor; subíndices $f$: líquido sat.; $g$: vapor sat.; $fg = g-f$.

## Diagramas de Fase (Clausius-Clapeyron)

**Ecuación de Clausius-Clapeyron**
$$\frac{dP}{dT}\bigg|_{\rm coex} = \frac{h_{\beta\alpha}}{T\,v_{\beta\alpha}} \qquad \frac{dP}{dT} = \frac{s_{\beta\alpha}}{v_{\beta\alpha}} \qquad s_{\beta\alpha} = \frac{h_{\beta\alpha}}{T}$$

**Condición de coexistencia**
$$g_\alpha(T,P) = g_\beta(T,P) \qquad dg = -s\,dT + v\,dP$$

**Curvas de coexistencia**
$$\frac{dP_{\rm sat}}{dT} = \frac{h_{fg}}{T\,v_{fg}}>0 \qquad \frac{dP_{\rm fus}}{dT} = \frac{h_{sl}}{T\,v_{sl}} \qquad \frac{dP_{\rm sub}}{dT} = \frac{h_{sg}}{T\,v_{sg}}>0$$
$$h_{sg}=h_{sl}+h_{lg}$$

**Clausius-Clapeyron integrada** (con $v_{fg}\approx v_g=RT/P$, $h_{fg}$ cte)
$$\frac{d\ln P_{\rm sat}}{d(1/T)}=-\frac{h_{fg}}{R} \qquad \ln\frac{P_2}{P_1}=-\frac{h_{fg}}{R}\left(\frac{1}{T_2}-\frac{1}{T_1}\right)$$

**Isobara de coexistencia**
$$P=P_{\rm sat}(T)=\text{cte},\quad v\in[v_f(T),\,v_g(T)]$$

**Ecuación de estado (superficie)**
$$f(P,v,T)=0$$

## Cambio de Fase

**Entalpía de vaporización (calor latente)**
$$h_{fg}(T) \equiv h_g(T)-h_f(T) \qquad q_{\rm vap} = \Delta h = h_g - h_f = h_{fg}$$
$$h_{fg} = u_{fg} + P\,v_{fg}, \qquad u_{fg}=u_g-u_f,\quad v_{fg}=v_g-v_f$$

**Entropía de vaporización**
$$s_{fg} = \frac{h_{fg}}{T_{\rm sat}}$$

**Correlación de Watson**
$$h_{fg}(T) = h_{fg,r}\left(\frac{1-T/T_c}{1-T_r/T_c}\right)^{0.38}$$

**Otros calores latentes**
$$h_{sl}=h_l-h_s \qquad h_{sg}=h_{sl}+h_{lg} = h_g-h_s$$

**Regla de fases de Gibbs**
$$F = C - \phi + 2$$

## Propiedades en la Región Bifásica

**Regla de mezcla**
$$y = y_f + x\,y_{fg}, \qquad y_{fg} = y_g - y_f \qquad y = (1-x)\,y_f + x\,y_g$$

**Balance de masa**
$$m = m_f + m_g \qquad m_g = xm, \quad m_f = (1-x)m$$
$$Y = m_f\,y_f + m_g\,y_g$$

**Relaciones explícitas**
$$v = v_f + x\,v_{fg} \qquad u = u_f + x\,u_{fg} \qquad h = h_f + x\,h_{fg} \qquad s = s_f + x\,s_{fg}$$

**Calidad desde propiedades medibles**
$$x = \frac{v-v_f}{v_{fg}} = \frac{h-h_f}{h_{fg}} = \frac{s-s_f}{s_{fg}} = \frac{u-u_f}{u_{fg}}$$

**Regla de la palanca (geométrica)**
$$\frac{v-v_f}{v_{fg}} = x, \qquad \frac{v_g - v}{v_{fg}} = 1-x \qquad m_f\,(v-v_f) = m_g\,(v_g-v)$$

**Proceso isobárico (sistema cerrado)**
$$w = P\,\Delta v \qquad q = \Delta h \qquad \Delta S = \frac{Q_{\rm rev}}{T_{\rm sat}}$$

## Líquido Comprimido

**Región**: $T < T_{\rm sat}(P)$ equiv. $P > P_{\rm sat}(T)$.

**Insensibilidad a la presión**
$$\left(\frac{\partial v}{\partial P}\right)_T = -v\kappa_T \qquad v(T,P) \approx v_f(T) \qquad u(T,P) \approx u_f(T)$$
$$\left(\frac{\partial u}{\partial P}\right)_T = v(P\kappa_T - T\alpha)$$

**Corrección de presión para la entalpía**
$$h(T,P) \approx h_f(T) + v_f(T)\,[P - P_{\rm sat}(T)]$$
$$\left(\frac{\partial h}{\partial P}\right)_T = v - T\left(\frac{\partial v}{\partial T}\right)_P \approx v_f(T)$$

**Trabajo de bomba (flujo reversible)**
$$w_{B,s} = -\int_{P_1}^{P_2} v\,dP \approx -v_f(P_2-P_1) \qquad \eta_B = \frac{w_{B,s}}{w_{B,\rm real}}$$

## Vapor Sobrecalentado

**Región**: $T > T_{\rm sat}(P)$; grado de sobrecalentamiento $\Delta T_{\rm sh}=T-T_{\rm sat}(P)$.

**Factor de compresibilidad**
$$Z \equiv \frac{Pv}{RT}, \qquad R = \frac{R_u}{M}$$

**Presión y temperatura reducidas**
$$P_r = \frac{P}{P_c} \qquad T_r = \frac{T}{T_c}$$

**Interpolación bilineal**
$$y(T,P) \approx y(T_1,P_1)\,\frac{(T_2-T)(P_2-P)}{(T_2-T_1)(P_2-P_1)} + y(T_2,P_1)\,\frac{(T-T_1)(P_2-P)}{(T_2-T_1)(P_2-P_1)}$$
$$+ y(T_1,P_2)\,\frac{(T_2-T)(P-P_1)}{(T_2-T_1)(P_2-P_1)} + y(T_2,P_2)\,\frac{(T-T_1)(P-P_1)}{(T_2-T_1)(P_2-P_1)}$$

**Principio de estados correspondientes**
$$Z \approx Z(P_r, T_r)$$

**Propiedades calóricas del gas ideal**
$$h_{\rm ig}(T) = h_{\rm ig}(T_{\rm ref}) + \int_{T_{\rm ref}}^T c_p(T')\,dT'$$
$$s_{\rm ig}(T,P)=s_{\rm ig}(T_{\rm ref},P_{\rm ref})+\int_{T_{\rm ref}}^T \frac{c_p}{T'}\,dT'-R\ln\frac{P}{P_{\rm ref}}$$

## Gas Ideal

**Ecuación de estado**
$$Pv = RT \qquad PV = mRT \qquad P\bar{v} = R_u T, \qquad R = \frac{R_u}{M}$$

**Ley de Joule**
$$u = u(T), \qquad h = u + Pv = u(T) + RT = h(T)$$
$$du = c_v(T)\,dT, \qquad dh = c_p(T)\,dT$$
$$\left(\frac{\partial u}{\partial v}\right)_T = T\left(\frac{\partial P}{\partial T}\right)_v - P = 0$$

**Relación de Mayer**
$$c_p - c_v = R \qquad dh = du + R\,dT$$

**Cambios de propiedades (calóricamente perfecto)**
$$\Delta u = c_v (T_2 - T_1), \qquad \Delta h = c_p (T_2 - T_1)$$
$$\Delta s = c_v \ln\frac{T_2}{T_1} + R \ln\frac{v_2}{v_1} = c_p \ln\frac{T_2}{T_1} - R \ln\frac{P_2}{P_1}$$
$$\Delta s = s^\circ(T_2) - s^\circ(T_1) - R\ln\frac{P_2}{P_1}$$

**Procesos isentrópicos** ($\gamma = c_p/c_v$)
$$Tv^{\gamma-1} = \text{cte}, \qquad T P^{(1-\gamma)/\gamma} = \text{cte}, \qquad Pv^{\gamma} = \text{cte}$$

$R_u = 8.314\,\mathrm{kJ/(kmol\cdot K)}$; $\gamma = c_p/c_v$.

## Gas Real

**Factor de compresibilidad**
$$Z \equiv \frac{Pv}{RT} \neq 1$$

**Ecuación de van der Waals**
$$\left(P + \frac{a}{\bar{v}^{\,2}}\right)(\bar{v} - b) = R_u T \qquad P = \frac{R_u T}{\bar{v}-b} - \frac{a}{\bar{v}^{\,2}}$$

**Condiciones del punto crítico**
$$\left(\frac{\partial P}{\partial \bar{v}}\right)_{T_c} = 0, \qquad \left(\frac{\partial^2 P}{\partial \bar{v}^{\,2}}\right)_{T_c} = 0$$

**Constantes de van der Waals**
$$a = \frac{27 R_u^2 T_c^2}{64 P_c}, \qquad b = \frac{R_u T_c}{8 P_c} \qquad \bar{v}_c = 3b \qquad Z_c = \frac{P_c\bar{v}_c}{R_uT_c} = \frac{3}{8}$$

**Energía interna del gas real**
$$\left(\frac{\partial \bar{u}}{\partial \bar{v}}\right)_T = T\left(\frac{\partial P}{\partial T}\right)_{\bar{v}} - P = \frac{a}{\bar{v}^{\,2}} > 0$$

**Diferencia de calores específicos (general)**
$$c_p - c_v = -T\frac{\left[(\partial P/\partial T)_v\right]^2}{(\partial P/\partial v)_T} = \frac{Tv\alpha_P^2}{\kappa_T}$$
$$\alpha_P = \frac{1}{v}\left(\frac{\partial v}{\partial T}\right)_P, \qquad \kappa_T = -\frac{1}{v}\left(\frac{\partial v}{\partial P}\right)_T$$

**Propiedades reducidas / estados correspondientes**
$$P_r = \frac{P}{P_c}, \quad T_r = \frac{T}{T_c}, \quad \bar{v}_r = \frac{\bar{v}}{\bar{v}_c} \qquad Z \approx Z(P_r, T_r)$$

**Redlich-Kwong**
$$P = \frac{R_u T}{\bar{v}-b} - \frac{a}{T^{1/2}\,\bar{v}(\bar{v}+b)}$$

**Peng-Robinson**
$$P = \frac{R_u T}{\bar{v}-b} - \frac{a\,\alpha(T_r,\omega)}{\bar{v}(\bar{v}+b)+b(\bar{v}-b)}$$

**Forma cúbica (vdW)**
$$\bar{v}^3 - \left(b + \frac{R_u T}{P}\right)\bar{v}^2 + \frac{a}{P}\,\bar{v} - \frac{ab}{P} = 0 \qquad v = \frac{ZRT}{P}$$

$\omega$: factor acéntrico; barra: magnitudes molares.

## Energía Interna

**Relación fundamental**
$$dU = T\,dS - P\,dV \qquad dU = \delta Q - \delta W$$
$$\delta W_{\rm rev} = P\,dV \qquad \delta Q_{\rm rev} = T\,dS$$

**Derivadas primeras (variables naturales $S,V$)**
$$T = \left(\frac{\partial U}{\partial S}\right)_V, \qquad P = -\left(\frac{\partial U}{\partial V}\right)_S$$

**Primera relación de Maxwell**
$$\left(\frac{\partial T}{\partial V}\right)_S = -\left(\frac{\partial P}{\partial S}\right)_V$$

**Gas ideal (experimento de Joule)**
$$\left(\frac{\partial U}{\partial V}\right)_T = 0 \qquad dU = c_v(T)\,dT \qquad U = U(T)$$

**Calor específico a volumen constante**
$$c_v \equiv \left(\frac{\partial u}{\partial T}\right)_v \qquad \Delta u = \int c_v\,dT$$

**Presión interna (gas real)**
$$\pi_T = \left(\frac{\partial u}{\partial v}\right)_T = \frac{T\alpha}{\kappa_T} - P$$

**Potenciales derivados**
$$H = U+PV, \qquad F = U-TS, \qquad G = U-TS+PV \qquad \Delta U = Q - W$$

## Entalpía

**Definición**
$$H \equiv U + PV \qquad h = u + Pv$$

**Energía de flujo estacionario**
$$e = h + \frac{V^2}{2} + gz \qquad \delta W_{\rm flujo} = P\,v$$

**Diferencial y variables naturales**
$$dH = T\,dS + V\,dP \qquad T = \left(\frac{\partial H}{\partial S}\right)_P, \qquad V = \left(\frac{\partial H}{\partial P}\right)_S$$

**Segunda relación de Maxwell**
$$\left(\frac{\partial T}{\partial P}\right)_S = \left(\frac{\partial V}{\partial S}\right)_P \qquad \left(\frac{\partial T}{\partial P}\right)_s = \frac{Tv\alpha}{c_p}$$

**Proceso isobárico**
$$q_P = \Delta h \qquad c_p = \left(\frac{\partial h}{\partial T}\right)_P$$

**Gas ideal**
$$h = u + RT = h(T) \qquad dh = c_p\,dT \qquad \Delta h = c_p\,\Delta T$$
$$\left(\frac{\partial h}{\partial P}\right)_T = v(1 - T\alpha)$$

**Sustancia incompresible**
$$dh = du + v\,dP = c\,dT + v\,dP \qquad \Delta h \approx v\,\Delta P$$

**Eficiencia isentrópica de turbina**
$$w_s = h_1 - h_{2s} \qquad w_{\rm real} = \eta_T\,w_s \qquad h_2 = h_1 - w_{\rm real}$$

## Entropía

**Definición (proceso reversible)**
$$dS = \frac{\delta Q_{\rm rev}}{T} \qquad S_2 - S_1 = \int_{1}^{2}\left(\frac{\delta Q}{T}\right)_{\rm rev}$$

**Desigualdad de Clausius**
$$\oint \frac{\delta Q}{T_b} \le 0$$

**Producción de entropía**
$$S_2 - S_1 \ge \int_1^2 \frac{\delta Q}{T_b} \qquad dS = \frac{\delta Q}{T_b} + \delta S_{\rm gen}, \qquad \delta S_{\rm gen} \ge 0$$

**Ecuaciones $T\,ds$**
$$T\,ds = du + P\,dv \qquad T\,ds = dh - v\,dP$$

**Entropía del gas ideal**
$$ds = c_p\,\frac{dT}{T} - R\,\frac{dP}{P}$$
$$\Delta s = \int_{T_1}^{T_2}c_p(T)\,\frac{dT}{T} - R\ln\frac{P_2}{P_1} = c_p\ln\frac{T_2}{T_1} - R\ln\frac{P_2}{P_1}$$
$$\Delta s = c_v\ln\frac{T_2}{T_1} + R\ln\frac{v_2}{v_1}$$

**Interpretación estadística**
$$S = k_B \ln\Omega \qquad R = N_A k_B \qquad \Delta S = k_B \ln\frac{\Omega_2}{\Omega_1}$$

**Región bifásica**
$$s = s_f + x\,s_{fg}, \qquad s_{fg} = s_g - s_f = \frac{h_{fg}}{T_{sat}}$$

**Conexión con exergía**
$$\dot{E}x_{\rm destruida} = T_0\,\dot{S}_{\rm gen}$$

$k_B = 1.380649\times10^{-23}\,\text{J/K}$.

## Energía de Helmholtz

**Definición**
$$F \equiv U - TS$$

**Diferencial y variables naturales**
$$dF = -S\,dT - P\,dV \qquad S = -\left(\frac{\partial F}{\partial T}\right)_V, \qquad P = -\left(\frac{\partial F}{\partial V}\right)_T$$

**Tercera relación de Maxwell**
$$\left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial P}{\partial T}\right)_V = \frac{\alpha}{\kappa_T}$$

**Trabajo máximo isotérmico**
$$W \le T\,\Delta S - \Delta U = -\Delta F \qquad W_{\rm máx} = -\Delta F$$

**Criterio de equilibrio ($T,V$ cte)**
$$\left.\Delta F\right|_{T,V} \le 0, \qquad F = \text{mínimo}$$

**Mecánica estadística**
$$Z = \sum_i e^{-E_i/(k_B T)} \qquad F = -k_B T\ln Z$$

**Relación de Gibbs-Helmholtz**
$$U = F - T\left(\frac{\partial F}{\partial T}\right)_V = -T^2 \left(\frac{\partial(F/T)}{\partial T}\right)_V \qquad \frac{\partial}{\partial T}\!\left(\frac{F}{T}\right)_V = -\frac{U}{T^2}$$

$G = F + PV$.

## Energía de Gibbs

**Definición**
$$G \equiv H - TS = U + PV - TS$$

**Diferencial y variables naturales**
$$dG = -S\,dT + V\,dP \qquad S = -\left(\frac{\partial G}{\partial T}\right)_P, \qquad V = \left(\frac{\partial G}{\partial P}\right)_T$$

**Cuarta relación de Maxwell**
$$\left(\frac{\partial S}{\partial P}\right)_T = -\left(\frac{\partial V}{\partial T}\right)_P = -v\alpha$$

**Criterio de equilibrio ($T,P$ cte)**
$$dG \le 0 \qquad \delta^2 G > 0 \;\Rightarrow\; c_P > 0,\; \kappa_T > 0$$

**Potencial químico (multicomponente)**
$$dG = -S\,dT + V\,dP + \sum_{i}\mu_i\,dn_i \qquad \mu_i \equiv \left(\frac{\partial G}{\partial n_i}\right)_{T,P,n_{j\neq i}}$$

**Equilibrio de fases (Clapeyron)**
$$g_f = g_g \qquad \frac{dP_{sat}}{dT} = \frac{s_{fg}}{v_{fg}} = \frac{h_{fg}}{T_{sat}\,v_{fg}}$$

**Ecuación de Gibbs-Duhem**
$$S\,dT - V\,dP + \sum_i n_i\,d\mu_i = 0 \qquad d\mu = -s\,dT + v\,dP$$

**Variación de $G$ con la presión**
$$\left(\frac{\partial g}{\partial P}\right)_T = v$$
$$g(T,P) = g^\circ(T) + RT\ln\frac{P}{P^\circ} \qquad g_i = g_i^\circ + RT\ln\frac{f_i}{f_i^\circ}$$
$$g(T,P) \approx g_f(T,P_{sat}) + v_f\,[P - P_{sat}(T)]$$

**Clausius-Clapeyron (ebullición)**
$$\ln\frac{P_2}{P_1} \approx \frac{h_{fg}}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$$

$\mu = \bar g$ (sustancia pura); $P^\circ = 100\,\text{kPa}$.

## Exergía (Disponibilidad)

**Definición (sistema cerrado)**
$$B = (U - U_0) + P_0(V - V_0) - T_0(S - S_0)$$

**Trabajo útil**
$$W_{\rm útil} = W_{\rm total} - P_0\,\Delta V \qquad W_{\rm útil,\,máx} = -\Delta B$$

**Exergía de flujo**
$$\psi = (h - h_0) - T_0(s - s_0) + \frac{V^2}{2} + gz \qquad \psi \approx (h - h_0) - T_0(s - s_0)$$

**Balances y trabajo útil**
$$\Delta U = Q - W_{\rm útil} - P_0\,\Delta V \qquad \Delta S = \frac{Q}{T_0} + S_{\rm gen}$$
$$W_{\rm útil} = -\Delta B - T_0\,S_{\rm gen}$$

**Gouy-Stodola (exergía destruida)**
$$\Phi \equiv T_0\,S_{\rm gen} \ge 0$$

**Eficiencia exergética**
$$\epsilon = \frac{W_{\rm útil}}{-\Delta B_{\rm entrada}} = 1 - \frac{T_0\,S_{\rm gen}}{-\Delta B_{\rm entrada}}$$

**Generación de entropía (transferencia de calor)**
$$S_{\rm gen} = \delta Q\left(\frac{1}{T_L} - \frac{1}{T_H}\right) > 0$$

$B,\Phi$: exergía cerrada; $\psi$: exergía de flujo; subíndice $0$: estado muerto.
