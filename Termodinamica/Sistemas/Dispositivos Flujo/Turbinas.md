---
title: Turbinas
order: 1
tags:
  - termodinamica
  - dispositivos-flujo
  - turbinas
draft: false
aliases:
  - turbine
  - expansor
---

# Turbinas

> [!definicion]
> Una **turbina** es un volumen de control de flujo estacionario que extrae trabajo de un fluido en expansión: el fluido entra a alta presión y temperatura, entrega energía al rotor mediante su expansión, y sale a baja presión y temperatura. Es el dispositivo que convierte energía interna (o química) en trabajo mecánico en ciclos de potencia.
>
> *¿Por qué la entalpía?* En un sistema cerrado (pistón), el trabajo sería $\int P\,dv$. En el volumen de control, cada kg que cruza la frontera también arrastra la energía de "empuje" $Pv$ para abrirse paso. Por eso la energía transportada por cada corriente es $h = u + Pv$ (entalpía), y el balance de energía del flujo estacionario adiabático da directamente $\dot{W} = \dot{m}(h_1 - h_2)$.
>
> *Tipos:* turbinas de vapor (ciclo Rankine), turbinas de gas (ciclo Brayton), turbinas hidráulicas. Todas comparten la misma ecuación de energía; difieren en el modelo del fluido (tablas de vapor, gas ideal, líquido incompresible).

![[turbina_esquema_vc.svg|440]]
*Volumen de control de una turbina. El fluido entra por el estado 1 (alta $P$, alta $T$) y sale por el estado 2 (baja $P$, baja $T$). El rotor extrae trabajo de eje $\dot{W}_t$. La flecha de $\dot{S}_{\rm gen}$ indica que el proceso real es irreversible.*

---

## Balance de energía y eficiencia isentrópica

> [!teorema]
> Para una turbina en flujo estacionario con una entrada y una salida, despreciando $\Delta EC$ y $\Delta EP$:
>
> **Trabajo de la turbina:**
> $$\dot{W}_t = \dot{m}(h_1 - h_2).$$
>
> **Eficiencia isentrópica** (relación entre trabajo real y trabajo reversible máximo):
> $$\boxed{\eta_t = \frac{\dot{W}_{\rm real}}{\dot{W}_{\rm rev}} = \frac{h_1 - h_2}{h_1 - h_{2s}},}$$
> donde el estado $2s$ es la salida hipotética de un proceso **isentrópico** ($s_{2s} = s_1$, $P_{2s} = P_2$).

> [!demostracion]
> **Hipótesis:** VC estacionario, $\dot{Q}=0$ (adiabático), $\dot{W}_{\rm eje}\neq0$ (turbina), $\Delta EC \approx 0$, $\Delta EP \approx 0$.
>
> **Paso 1 — Primera ley del VC estacionario.** Para una entrada (1) y una salida (2), la SFEE es:
> $$\dot{Q} - \dot{W}_t = \dot{m}[(h_2 - h_1) + \underbrace{\tfrac{1}{2}(C_2^2-C_1^2)}_{\approx0} + \underbrace{g(z_2-z_1)}_{\approx0}].$$
>
> **Paso 2 — Aplicar $\dot{Q}=0$.** Despejando $\dot{W}_t$:
> $$\dot{W}_t = \dot{m}(h_1 - h_2).$$
> Como $h_1 > h_2$ (el fluido se expande, cede entalpía), $\dot{W}_t > 0$ ✓ (sale del sistema).
>
> **Paso 3 — Proceso isentrópico de referencia.** El proceso reversible y adiabático no genera entropía: $s_{2s} = s_1$. Combinado con $P_2$ conocida, $h_{2s}$ queda determinado unívocamente por la ecuación de estado (tablas o $Pv^{\gamma}=\text{cte}$ para gas ideal).
>
> **Paso 4 — Definir eficiencia isentrópica.** Las irreversibilidades internas (fricción en los álabes, remolinos) elevan la entropía de salida: $s_2 > s_{2s}$, lo que implica $h_2 > h_{2s}$ (mayor temperatura de salida para la misma $P_2$). El trabajo real es menor que el reversible:
> $$\dot{W}_{\rm real} = \dot{m}(h_1-h_2) < \dot{m}(h_1-h_{2s}) = \dot{W}_{\rm rev}.$$
>
> **Paso 5 — Expresión de $\eta_t$.** Dividiendo:
> $$\eta_t = \frac{h_1-h_2}{h_1-h_{2s}} < 1.$$
> Despejando el estado real de salida: $h_2 = h_1 - \eta_t(h_1-h_{2s})$. $\blacksquare$

> [!proposicion]
> Para gas ideal con $c_p$ constante, la eficiencia isentrópica toma la forma:
> $$\eta_t = \frac{T_1 - T_2}{T_1 - T_{2s}}, \qquad T_{2s} = T_1\!\left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma}.$$

---

## Destrucción de exergía

> [!proposicion]
> La destrucción de exergía en una turbina real (adiabática) es directamente proporcional a la entropía generada:
> $$\dot{X}_{\rm dest} = T_0\,\dot{S}_{\rm gen} = T_0\,\dot{m}(s_2 - s_1) \geq 0.$$
>
> La eficiencia exergética (de segunda ley):
> $$\varepsilon_t = \frac{\dot{W}_t}{\dot{m}(\psi_1-\psi_2)} = 1 - \frac{\dot{X}_{\rm dest}}{\dot{m}(\psi_1-\psi_2)}.$$
>
> Para turbinas de vapor con gas ideal y $c_p$ constante, $\varepsilon_t \approx \eta_t$; en general difieren porque $\psi = h - T_0 s - (h_0 - T_0 s_0)$ incluye el calor latente.

---

## Ejemplo: turbina de vapor de planta de potencia

> [!ejemplo]
> Vapor a $P_1=6\,\mathrm{MPa}$, $T_1=600\,°\mathrm{C}$ se expande en una turbina hasta $P_2=10\,\mathrm{kPa}$ con eficiencia isentrópica $\eta_t=0.90$ y caudal $\dot{m}=10\,\mathrm{kg/s}$. Temperatura de referencia $T_0=298\,\mathrm{K}$, $P_0=100\,\mathrm{kPa}$. Determinar: (a) potencia real; (b) estado de salida real; (c) destrucción de exergía.

> [!solucion]
> **Paso 1 — Estado de entrada (tablas de vapor sobrecalentado).** A $P_1=6\,\mathrm{MPa}$, $T_1=600\,°\mathrm{C}$:
> $$h_1 = 3658.4\,\mathrm{kJ/kg}, \quad s_1 = 7.1677\,\mathrm{kJ/(kg\cdot K)}.$$
>
> **Paso 2 — Estado isentrópico de salida.** A $P_2=10\,\mathrm{kPa}$, $s_{2s}=s_1=7.1677\,\mathrm{kJ/(kg\cdot K)}$.
> De tablas de saturación a $10\,\mathrm{kPa}$: $s_f=0.6493$, $s_g=8.1502$, $h_f=191.8$, $h_{fg}=2392.8$.
> $$x_{2s}=\frac{7.1677-0.6493}{8.1502-0.6493}=\frac{6.5184}{7.5009}=0.869.$$
> $$h_{2s}=191.8+0.869\times2392.8=191.8+2079.3=2271.1\,\mathrm{kJ/kg}.$$
>
> **Paso 3 — Trabajo isentrópico y potencia real.** Trabajo isentrópico: $w_s=h_1-h_{2s}=3658.4-2271.1=1387.3\,\mathrm{kJ/kg}$. Potencia real:
> $$\dot{W}_t = \eta_t\,\dot{m}\,w_s = 0.90\times10\times1387.3 = 12\,486\,\mathrm{kW} \approx 12.5\,\mathrm{MW}.$$
>
> **Paso 4 — Estado real de salida.** $h_2 = h_1 - \dot{W}_t/\dot{m} = 3658.4 - 1248.6 = 2409.8\,\mathrm{kJ/kg}$.
> A $P_2=10\,\mathrm{kPa}$: $x_2=(2409.8-191.8)/2392.8=2218.0/2392.8=0.927$.
> $s_2=0.6493+0.927\times7.5009=0.6493+6.953=7.602\,\mathrm{kJ/(kg\cdot K)}$.
>
> **Paso 5 — Destrucción de exergía.** $\dot{S}_{\rm gen}=\dot{m}(s_2-s_1)=10\times(7.602-7.168)=10\times0.434=4.34\,\mathrm{kW/K}$.
> $$\dot{X}_{\rm dest}=T_0\,\dot{S}_{\rm gen}=298\times4.34=1293\,\mathrm{kW}.$$
> Representa el 9.4% de la potencia real, principalmente por fricción en álabes.
>
> $\boxed{\dot{W}_t = 12.5\,\mathrm{MW},\quad x_2=0.927,\quad \dot{X}_{\rm dest}=1293\,\mathrm{kW}.}$ $\blacksquare$

> [!warning]
> La calidad de salida $x_2$ debe mantenerse por encima de $0.88$–$0.90$. Con $x_2=0.927$ este diseño es aceptable. Si $x_2 < 0.88$, las gotas de líquido erosionan los álabes de las últimas etapas.

> [!referencia]
> Borgnakke & Sonntag, §6.3; Çengel & Boles, §9-1; Moran & Shapiro, §6.6.
