---
title: Difusores
order: 4
tags:
  - termodinamica
  - dispositivos-flujo
  - difusores
draft: false
aliases:
  - diffuser
  - difusor
---

# Difusores

> [!definicion]
> Un **difusor** es un conducto de sección creciente, sin trabajo de eje ($\dot{W}=0$), que convierte **energía cinética en entalpía (presión)**: el fluido entra con alta velocidad, desacelera, y sale a mayor presión. Es el proceso inverso de una [[Toberas | tobera]].
>
> *¿Por qué aumenta la presión?* La ecuación de Bernoulli para flujo incompresible ($P + \frac{1}{2}\rho C^2 = \text{cte}$) lo ilustra: al caer $C^2$, sube $P$. En el caso compresible, el balance de entalpía de estancamiento reemplaza a Bernoulli, pero el mecanismo es el mismo: intercambio entre energía cinética y presión estática.
>
> *Aplicaciones:* entrada de aire en turbinas de gas (el difusor aerodinámico del fuselaje), difusores en compresores centrífugos (convierten la velocidad saliente del rotor en presión), intercambiadores de calor de carcasa (reducen velocidad para maximizar tiempo de residencia).

![[difusor_esquema_vc.svg|440]]
*Difusor simple. El fluido entra rápido en el estado 1 y sale lento en el estado 2. La sección crece en dirección del flujo. El gradiente adverso de presión ($dP/dx>0$) es la causa principal de irreversibilidades: la capa límite puede despegarse si el ángulo de apertura es demasiado grande (separación del flujo).*

---

## Balance de energía

> [!teorema]
> Para un difusor adiabático, estacionario, sin trabajo de eje, con una entrada y una salida:
> $$h_1 + \frac{C_1^2}{2} = h_2 + \frac{C_2^2}{2}.$$
>
> Como $C_2 < C_1$, se tiene $h_2 > h_1$: la entalpía (y con ella la temperatura y la presión) aumenta.
>
> **Eficiencia del difusor** (relación entre la recuperación de presión isentrópica y la recuperación real):
> $$\boxed{\eta_d = \frac{h_{2s} - h_1}{h_2 - h_1} = \frac{h_{2s} - h_1}{C_1^2/2 - C_2^2/2},}$$
> donde $2s$ es el estado isentrópico que tendría la misma presión $P_2$ que el estado real.

> [!demostracion]
> **Hipótesis:** VC estacionario, $\dot{Q}=0$, $\dot{W}=0$, $\Delta EP=0$, una corriente.
>
> **Paso 1 — Primera ley del VC.** Idéntica a la tobera:
> $$h_1 + \frac{C_1^2}{2} = h_2 + \frac{C_2^2}{2}.$$
>
> **Paso 2 — Signo del cambio de entalpía.** En el difusor $C_2 < C_1$, luego $C_2^2/2 < C_1^2/2$, por lo que $h_2 > h_1$. La conversión EC → $h$ es el proceso opuesto a la tobera.
>
> **Paso 3 — Estado isentrópico de referencia.** El estado $2s$ tiene la misma $P_2$ que el estado real pero fue alcanzado sin irreversibilidades: $s_{2s}=s_1$. En el diagrama $h$-$s$: el punto $2s$ está a la izquierda de $2$ (misma $P_2$, menor $s$), y $h_{2s} < h_2$ (la entalpía real de salida es mayor que la isentrópica porque las irreversibilidades depositan calor).
>
> **Paso 4 — ¿Por qué $h_{2s} < h_2$?** Las irreversibilidades (fricción, separación de capa límite) disipan EC en calor interno, elevando más la temperatura que en el caso reversible. Para la misma $P_2$, el estado real 2 tiene mayor $T$ (y $h$) que el isentrópico $2s$.
>
> **Paso 5 — Definición de $\eta_d$.** El difusor ideal comprime isentrópicamente desde $P_1$ hasta $P_2$ usando solo la energía cinética disponible. La eficiencia compara cuánta entalpía isentrópica se "ganó" sobre cuánta energía cinética se "gastó":
> $$\eta_d = \frac{h_{2s}-h_1}{h_1+C_1^2/2-h_1-C_2^2/2} = \frac{h_{2s}-h_1}{(C_1^2-C_2^2)/2} \leq 1.$$ $\blacksquare$

> [!proposicion]
> Para gas ideal y $C_2 \approx 0$ (difusor completo que detiene el fluido):
> $$h_{2s} - h_1 = c_p(T_{2s}-T_1), \qquad \frac{P_{2s}}{P_1} = \left(\frac{T_{2s}}{T_1}\right)^{\gamma/(\gamma-1)}, \qquad T_{2s} = T_1+\frac{\eta_d C_1^2}{2c_p}.$$

---

## Ejemplo: difusor de entrada de turborreactor

> [!ejemplo]
> Un avión vuela a $Ma_\infty=0.80$ a $H=10\,\mathrm{km}$ de altitud. En esas condiciones: $T_\infty=223\,\mathrm{K}$, $P_\infty=26.5\,\mathrm{kPa}$, $a_\infty=\sqrt{\gamma RT_\infty}=299\,\mathrm{m/s}$. El difusor de entrada desacelera el aire hasta $C_2\approx0$ (cámara de combustión) con eficiencia $\eta_d=0.88$. Calcular: (a) temperatura y presión de estancamiento isentrópica ($T_{0s}$, $P_{0s}$); (b) temperatura de salida real $T_2$; (c) presión real de salida $P_2$. Datos: $c_p=1.005\,\mathrm{kJ/(kg\cdot K)}$, $\gamma=1.4$.

> [!solucion]
> **Paso 1 — Velocidad de vuelo.**
> $$C_1 = Ma_\infty\times a_\infty = 0.80\times299 = 239.2\,\mathrm{m/s}.$$
>
> **Paso 2 — Temperatura de estancamiento isentrópica.**
> $$T_{0s} = T_\infty + \frac{C_1^2}{2c_p} = 223 + \frac{239.2^2}{2\times1005} = 223 + 28.5 = 251.5\,\mathrm{K}.$$
>
> **Paso 3 — Presión de estancamiento isentrópica.**
> $$P_{0s} = P_\infty\!\left(\frac{T_{0s}}{T_\infty}\right)^{\gamma/(\gamma-1)} = 26.5\times\!\left(\frac{251.5}{223}\right)^{3.5} = 26.5\times1.524 = 40.4\,\mathrm{kPa}.$$
>
> **Paso 4 — Temperatura real de salida.** La temperatura de parada real $T_2=T_{0s}=251.5\,\mathrm{K}$ (la energía se conserva; la temperatura de salida no depende de $\eta_d$ cuando $C_2=0$). La presión real sí depende de $\eta_d$.
>
> **Paso 5 — Presión real de salida.** $h_{2s}-h_1 = \eta_d\,c_p(T_2-T_1) = 0.88\times1.005\times28.5=25.2\,\mathrm{kJ/kg}$. $T_{2s} = T_1 + (h_{2s}-h_1)/c_p = 223+25.1=248.1\,\mathrm{K}$.
> $$P_2 = P_\infty\!\left(\frac{T_{2s}}{T_\infty}\right)^{3.5} = 26.5\times\!\left(\frac{248.1}{223}\right)^{3.5} = 26.5\times1.478 = 39.2\,\mathrm{kPa}.$$
> Relación de recuperación de presión: $P_2/P_{0s}=39.2/40.4=0.970$. Se pierden 1.2 kPa respecto al difusor ideal.
>
> $\boxed{T_{0s}=251.5\,\mathrm{K},\quad P_{0s}=40.4\,\mathrm{kPa},\quad P_2=39.2\,\mathrm{kPa}.}$ $\blacksquare$

> [!warning]
> El ángulo de divergencia del difusor es crítico: si supera $\sim8°$–$12°$, la capa límite se desprende y la eficiencia cae abruptamente. Los difusores de alta eficiencia son largos y estrechos, o usan diseños con múltiples canales paralelos.

> [!referencia]
> Borgnakke & Sonntag, §6.5; Çengel & Boles, §9-3; Moran & Shapiro, §9.6.
