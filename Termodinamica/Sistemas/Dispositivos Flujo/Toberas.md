---
title: Toberas
order: 3
tags:
  - termodinamica
  - dispositivos-flujo
  - toberas
draft: false
aliases:
  - nozzle
  - boquilla
---

# Toberas

> [!definicion]
> Una **tobera** es un conducto de sección variable sin trabajo de eje ($\dot{W}=0$) que convierte **entalpía en energía cinética**: el fluido entra lento, se acelera expandiéndose, y sale con alta velocidad. El proceso inverso (fluido entrando rápido y saliéndose lento) es un [[Difusores | difusor]].
>
> *¿Por qué una sección convergente acelera un fluido compresible?* Para gas subsónico ($Ma < 1$), reducir el área $A$ obliga a aumentar la velocidad (por conservación de masa: $\dot{m}=\rho C A = \text{cte}$, y aunque $\rho$ baja, $A$ baja más). Para gas supersónico ($Ma > 1$), sucede lo contrario: la densidad cae más rápido que el área, por lo que se necesita aumentar $A$ para seguir acelerando. De ahí la tobera **convergente-divergente** (de Laval) para alcanzar regímenes supersónicos.
>
> *Aplicaciones:* inyectores de vapor (ciclo Rankine), toberas de cohetes y aviones, válvulas de expansión acústica, antorchas de soldadura oxiacetileno.

![[tobera_esquema_area_velocidad.svg|460]]
*Tobera convergente-divergente (de Laval). En la sección convergente el fluido es subsónico y se acelera al reducir $A$. En la garganta $Ma=1$. En la divergente el fluido es supersónico y sigue acelerándose al aumentar $A$. Si la presión de salida es insuficiente para mantener el supersónico, aparece un choque normal.*

---

## Balance de energía: conversión h → EC

> [!teorema]
> Para una tobera adiabática, estacionaria, sin trabajo de eje, con una entrada y una salida:
> $$h_1 + \frac{C_1^2}{2} = h_2 + \frac{C_2^2}{2}.$$
>
> Despejando la velocidad de salida:
> $$\boxed{C_2 = \sqrt{C_1^2 + 2(h_1 - h_2)}.}$$
>
> **Eficiencia de la tobera** (relación entre EC real obtenida y EC isentrópica máxima):
> $$\eta_{\rm tob} = \frac{C_2^2/2}{C_{2s}^2/2} = \frac{h_1 - h_2}{h_1 - h_{2s}},$$
> donde $h_{2s}$ corresponde al proceso isentrópico desde 1 hasta $P_2$.

> [!demostracion]
> **Hipótesis:** VC estacionario, $\dot{Q}=0$, $\dot{W}=0$, $\Delta EP = 0$, una sola corriente.
>
> **Paso 1 — Primera ley del VC.** La SFEE con $\dot{Q}=\dot{W}=0$:
> $$\dot{m}\!\left[h_2 + \frac{C_2^2}{2} - h_1 - \frac{C_1^2}{2}\right] = 0 \implies h_1 + \frac{C_1^2}{2} = h_2 + \frac{C_2^2}{2}.$$
>
> **Paso 2 — Significado físico.** La entalpía de estancamiento $h_0 = h + C^2/2$ es constante a lo largo de la tobera. La entalpía "cae" exactamente en la cantidad que aumenta la energía cinética.
>
> **Paso 3 — Despejar $C_2$.** Reorganizando:
> $$\frac{C_2^2}{2} - \frac{C_1^2}{2} = h_1 - h_2 \implies C_2 = \sqrt{C_1^2 + 2(h_1-h_2)}.$$
> Si $C_1 \ll C_2$ (tobera de cohete), aproximar $C_2 \approx \sqrt{2(h_1-h_2)}$.
>
> **Paso 4 — Proceso isentrópico de referencia.** El proceso real tiene $s_2 > s_{2s}$ (la fricción genera entropía). Esto implica $h_2 > h_{2s}$ para la misma $P_2$: menos entalpía disponible para EC → $C_2 < C_{2s}$.
>
> **Paso 5 — Eficiencia.** Dividiendo EC real entre EC isentrópica:
> $$\eta_{\rm tob} = \frac{C_2^2/2}{C_{2s}^2/2} = \frac{h_1-h_2}{h_1-h_{2s}} \leq 1.$$
> Valores típicos: $0.92$–$0.99$ para toberas de vapor bien diseñadas. $\blacksquare$

---

## Caso especial: gas ideal con $c_p$ constante

> [!proposicion]
> Para gas ideal con $c_p$ constante y $C_1 \approx 0$:
> $$C_2 = \sqrt{2c_p(T_1-T_2)}, \qquad T_{2s} = T_1\!\left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma}.$$
>
> La velocidad de salida isentrópica:
> $$C_{2s} = \sqrt{2c_pT_1\!\left[1-\left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma}\right]}.$$
>
> Para comparar con la velocidad del sonido: $a = \sqrt{\gamma R T}$. Número de Mach de salida: $Ma_2 = C_{2s}/a_2$.

---

## Ejemplo: tobera de vapor en turbina de impulso

> [!ejemplo]
> Vapor a $P_1=1\,\mathrm{MPa}$, $T_1=300\,°\mathrm{C}$ entra en una tobera con velocidad $C_1=20\,\mathrm{m/s}$ y se expande hasta $P_2=200\,\mathrm{kPa}$. La eficiencia de la tobera es $\eta_{\rm tob}=0.95$. Determinar: (a) velocidad de salida real; (b) temperatura de salida real.

> [!solucion]
> **Paso 1 — Estado de entrada (tablas de vapor sobrecalentado).** A $P_1=1\,\mathrm{MPa}$, $T_1=300\,°\mathrm{C}$:
> $$h_1 = 3051.2\,\mathrm{kJ/kg}, \quad s_1 = 7.1229\,\mathrm{kJ/(kg\cdot K)}.$$
>
> **Paso 2 — Estado isentrópico de salida.** A $P_2=200\,\mathrm{kPa}$, $s_{2s}=s_1=7.1229\,\mathrm{kJ/(kg\cdot K)}$.
> De tablas de vapor sobrecalentado a $200\,\mathrm{kPa}$, $s=7.1229$ está entre $150\,°\mathrm{C}$ ($s=7.0792$) y $200\,°\mathrm{C}$ ($s=7.5074$). Interpolando:
> $$T_{2s} = 150 + \frac{7.1229-7.0792}{7.5074-7.0792}\times50 = 150+5.1=155.1\,°\mathrm{C}.$$
> $$h_{2s} = 2769.1 + \frac{7.1229-7.0792}{7.5074-7.0792}\times(2870.5-2769.1)=2769.1+10.3=2779.4\,\mathrm{kJ/kg}.$$
>
> **Paso 3 — Velocidad isentrópica de salida.**
> $$C_{2s}=\sqrt{C_1^2+2(h_1-h_{2s})\times10^3}=\sqrt{20^2+2\times(3051.2-2779.4)\times10^3}.$$
> $$=\sqrt{400+543\,600}=\sqrt{544\,000}=737.6\,\mathrm{m/s}.$$
>
> **Paso 4 — Velocidad real de salida.**
> $$C_2 = C_{2s}\sqrt{\eta_{\rm tob}} = 737.6\times\sqrt{0.95} = 737.6\times0.9747 = 718.9\,\mathrm{m/s}.$$
>
> **Paso 5 — Entalpía y temperatura real de salida.**
> EC real $= C_2^2/2 = 718.9^2/2\times10^{-3} = 258.4\,\mathrm{kJ/kg}$.
> $h_2 = h_1 + C_1^2/2\times10^{-3} - C_2^2/2\times10^{-3} = 3051.2+0.2-258.4 = 2793.0\,\mathrm{kJ/kg}$.
> A $P_2=200\,\mathrm{kPa}$, interpolando: $T_2 \approx 162\,°\mathrm{C}$.
>
> $\boxed{C_2 = 718.9\,\mathrm{m/s},\quad T_2 \approx 162\,°\mathrm{C}.}$ $\blacksquare$

> [!warning]
> La velocidad $C_2=719\,\mathrm{m/s}$ corresponde al número de Mach subsónico a esa condición ($a_2 \approx 575\,\mathrm{m/s}$ para vapor a $162\,°\mathrm{C}$). Una tobera convergente simple alcanzaría el máximo en la garganta ($Ma=1$). Para velocidades supersónicas se requiere la geometría convergente-divergente de Laval.

> [!referencia]
> Borgnakke & Sonntag, §6.5; Çengel & Boles, §9-3; Moran & Shapiro, §6.4.
