---
title: Compresores
order: 2
tags:
  - termodinamica
  - dispositivos-flujo
  - compresores
draft: false
aliases:
  - compressor
  - compresor
---

# Compresores

> [!definicion]
> Un **compresor** es un volumen de control de flujo estacionario que consume trabajo para elevar la presión de un gas. El fluido entra a baja presión, recibe trabajo del rotor o émbolo, y sale a alta presión. Es el proceso inverso de una [[Turbinas | turbina]].
>
> *¿Por qué consume tanto trabajo?* La presión de un gas cae drásticamente con el volumen. Para comprimir desde $P_1$ hasta $P_2$ hay que vencer continuamente la presión creciente del gas. El trabajo mínimo (proceso reversible) es $w_{\rm rev} = \int_1^2 v\,dP$ — el área a la izquierda de la curva en el diagrama $P$-$v$. Las irreversibilidades (fricción, turbulencia) elevan el trabajo real por encima de este mínimo.
>
> *Importancia en ciclos:* el compresor del ciclo Brayton consume entre el 40–80% del trabajo bruto de la turbina — el "trabajo de retorno" (back work ratio). Reducir las irreversibilidades del compresor es tan crítico como mejorar la turbina.

![[compresor_esquema_vc.svg|440]]
*Volumen de control de un compresor. El fluido entra en el estado 1 (baja $P$) y sale en el estado 2 (alta $P$). El motor aplica trabajo de eje $\dot{W}_c > 0$ que entra al VC. Las irreversibilidades elevan $T_2$ sobre $T_{2s}$, desperdiciando trabajo.*

---

## Balance de energía y eficiencia isentrópica

> [!teorema]
> Para un compresor en flujo estacionario, adiabático, con una entrada y una salida, despreciando $\Delta EC$ y $\Delta EP$:
>
> **Trabajo del compresor** (positivo = entra al sistema):
> $$\dot{W}_c = \dot{m}(h_2 - h_1).$$
>
> **Eficiencia isentrópica** (relación entre trabajo reversible mínimo y trabajo real):
> $$\boxed{\eta_c = \frac{\dot{W}_{\rm rev}}{\dot{W}_{\rm real}} = \frac{h_{2s} - h_1}{h_2 - h_1},}$$
> donde $2s$ es la salida para el proceso isentrópico ($s_{2s}=s_1$, $P_{2s}=P_2$).

> [!demostracion]
> **Hipótesis:** VC estacionario, $\dot{Q}=0$, $\dot{W}_c>0$ (entra al VC), $\Delta EC \approx 0$, $\Delta EP \approx 0$.
>
> **Paso 1 — Primera ley del VC.** Con convención de trabajo de entrada positivo:
> $$\dot{W}_c - \dot{Q} = \dot{m}(h_2 - h_1) \implies \dot{W}_c = \dot{m}(h_2 - h_1).$$
> Como $h_2 > h_1$ (la presión aumenta), $\dot{W}_c > 0$ ✓.
>
> **Paso 2 — Proceso isentrópico de referencia.** El proceso adiabático reversible cumple $s_{2s}=s_1$ y fija $h_{2s}$ en función de $P_2$. Para gas ideal: $T_{2s}=T_1(P_2/P_1)^{(\gamma-1)/\gamma}$, luego $h_{2s}-h_1=c_p(T_{2s}-T_1)$.
>
> **Paso 3 — Efecto de las irreversibilidades.** La fricción y la turbulencia generan entropía, elevando la temperatura de salida: $s_2 > s_{2s}$, lo que implica $h_2 > h_{2s}$ para la misma $P_2$. El trabajo real es mayor que el mínimo:
> $$\dot{W}_{\rm real} = \dot{m}(h_2-h_1) > \dot{m}(h_{2s}-h_1) = \dot{W}_{\rm rev}.$$
>
> **Paso 4 — Definir $\eta_c$.** El cociente es menor que 1 para un proceso real:
> $$\eta_c = \frac{h_{2s}-h_1}{h_2-h_1} \leq 1.$$
>
> **Paso 5 — Despejar el estado real de salida.** A partir de la definición:
> $$h_2 = h_1 + \frac{h_{2s}-h_1}{\eta_c}.$$
> Para gas ideal: $T_2 = T_1 + (T_{2s}-T_1)/\eta_c$. Nótese que cuanto menor sea $\eta_c$, mayor es $T_2$ — el gas sale más caliente y el trabajo consumido es mayor. $\blacksquare$

> [!proposicion]
> Para gas ideal con $c_p$ constante:
> $$\eta_c = \frac{T_{2s}-T_1}{T_2-T_1}, \qquad T_{2s} = T_1\!\left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma}.$$

---

## Compresión en etapas con interenfriamiento

> [!proposicion]
> Para relaciones de presión elevadas ($P_2/P_1 > 5$–6), comprimir en $N$ etapas con **interenfriamiento** hasta $T_1$ entre etapas minimiza el trabajo total. La relación de presión óptima por etapa (la que minimiza el trabajo) es igual para todas las etapas:
> $$r_{\rm opt} = \left(\frac{P_2}{P_1}\right)^{1/N}.$$
>
> El trabajo total para $N$ etapas con enfriamiento perfecto a $T_1$:
> $$\dot{W}_{\rm total} = N\,\dot{m}\,c_p\,T_1\left[r_{\rm opt}^{(\gamma-1)/\gamma}-1\right].$$
>
> *Intuición:* el interenfriamiento reduce el volumen específico del gas antes de cada etapa, disminuyendo $\int v\,dP$ (área en el diagrama $P$-$v$). El trabajo se acerca al mínimo isotérmico $\dot{m}RT_1\ln(P_2/P_1)$ cuando $N\to\infty$.

---

## Ejemplo: compresor de aire para turbina de gas

> [!ejemplo]
> Aire a $P_1=100\,\mathrm{kPa}$, $T_1=300\,\mathrm{K}$ se comprime en un compresor de eficiencia $\eta_c=0.85$ hasta $P_2=800\,\mathrm{kPa}$, con caudal $\dot{m}=2\,\mathrm{kg/s}$. Datos: $c_p=1.005\,\mathrm{kJ/(kg\cdot K)}$, $\gamma=1.4$, $R=0.287\,\mathrm{kJ/(kg\cdot K)}$, $T_0=298\,\mathrm{K}$. Determinar: (a) temperatura de salida real; (b) potencia consumida; (c) destrucción de exergía.

> [!solucion]
> **Paso 1 — Estado isentrópico de salida.**
> $$T_{2s} = T_1\!\left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma} = 300\times8^{0.2857} = 300\times1.811 = 543.3\,\mathrm{K}.$$
>
> **Paso 2 — Temperatura real de salida.**
> $$T_2 = T_1 + \frac{T_{2s}-T_1}{\eta_c} = 300 + \frac{543.3-300}{0.85} = 300 + \frac{243.3}{0.85} = 300 + 286.2 = 586.2\,\mathrm{K}.$$
>
> **Paso 3 — Potencia consumida.**
> $$\dot{W}_c = \dot{m}\,c_p(T_2-T_1) = 2\times1.005\times(586.2-300) = 2\times1.005\times286.2 = 575.3\,\mathrm{kW}.$$
> Verificación de eficiencia: $\dot{W}_{\rm rev}=\dot{m}\,c_p(T_{2s}-T_1)=2\times1.005\times243.3=489.0\,\mathrm{kW}$. $\eta_c=489.0/575.3=0.850$ ✓.
>
> **Paso 4 — Generación de entropía.**
> $$\Delta s = c_p\ln\frac{T_2}{T_1} - R\ln\frac{P_2}{P_1} = 1.005\times\ln\frac{586.2}{300} - 0.287\times\ln8.$$
> $$= 1.005\times0.6699 - 0.287\times2.079 = 0.6732 - 0.5967 = 0.0765\,\mathrm{kJ/(kg\cdot K)}.$$
> $$\dot{S}_{\rm gen} = \dot{m}\,\Delta s = 2\times0.0765 = 0.153\,\mathrm{kW/K}.$$
>
> **Paso 5 — Destrucción de exergía.**
> $$\dot{X}_{\rm dest} = T_0\,\dot{S}_{\rm gen} = 298\times0.153 = 45.6\,\mathrm{kW}.$$
> Es el 7.9% de la potencia consumida. La eficiencia exergética: $\varepsilon_c = 1 - 45.6/575.3 = 0.921$ (mayor que $\eta_c=0.85$ porque parte del calor de irreversibilidad queda en el fluido como entalpía aprovechable aguas abajo).
>
> $\boxed{T_2=586.2\,\mathrm{K},\quad \dot{W}_c=575.3\,\mathrm{kW},\quad \dot{X}_{\rm dest}=45.6\,\mathrm{kW}.}$ $\blacksquare$

> [!warning]
> La temperatura de salida $T_2=586\,\mathrm{K}=313\,°\mathrm{C}$ es significativa: requiere materiales de alta temperatura en las etapas de compresión. En ciclos regenerativos esta temperatura alta es ventajosa (calienta el precalentador); en otros casos, el interenfriamiento es necesario.

> [!referencia]
> Borgnakke & Sonntag, §6.4; Çengel & Boles, §9-2; Moran & Shapiro, §6.7.
