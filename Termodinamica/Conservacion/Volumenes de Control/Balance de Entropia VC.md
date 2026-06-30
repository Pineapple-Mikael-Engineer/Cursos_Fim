---
title: "Balance de Entropía (Volumen de Control)"
order: 3
tags:
  - termodinamica
  - conservacion
  - entropia
  - segunda_ley
  - volumen_de_control
draft: false
aliases:
  - segunda ley VC
  - balance entropico VC
  - entropy balance VC
---

# Balance de Entropía — Volumen de Control

> [!definicion]
> La **segunda ley de la termodinámica** para un [[Volumenes de Control/index | volumen de control]] fijo en el espacio:
> $$\boxed{\frac{dS_{VC}}{dt} = \sum_k \frac{\dot{Q}_k}{T_k} + \sum_i \dot{m}_i\,s_i - \sum_e \dot{m}_e\,s_e + \dot{S}_{\rm gen},}$$
> con $\dot{S}_{\rm gen} \ge 0$ siempre. El balance de entropía describe **cómo evoluciona la entropía del VC**: aumenta cuando entra calor ($\dot{Q}_k/T_k$), cuando entra flujo de entropía con el fluido ($\dot{m}_i s_i$), y cuando se generan irreversibilidades internas ($\dot{S}_{\rm gen}$); disminuye cuando sale calor o flujo de entropía.
>
> La diferencia fundamental con el balance de energía: la energía **se conserva** ($\dot{E}_{\rm gen} = 0$ siempre), pero la entropía **se genera** ($\dot{S}_{\rm gen} \ge 0$ — nunca negativa). Medir $\dot{S}_{\rm gen}$ en un dispositivo real dice cuán lejos está de la operación ideal reversible.

---

## Por qué la entropía se genera pero no se destruye

> [!teoria]
> Las irreversibilidades internas al VC (fricción, mezcla, transferencia de calor con gradiente de temperatura dentro del VC, reacciones espontáneas) crean entropía que no puede "deshacerse". A diferencia del calor ($\dot{Q}$ puede ser positivo o negativo) o del trabajo ($\dot{W}$ puede cambiar de signo), $\dot{S}_{\rm gen}$ **solo puede ser $\ge 0$**.
>
> Esto impone una asimetría temporal: el estado con más entropía es estadísticamente abrumadoramente más probable, y los procesos espontáneos van de estados menos probables (menos entropía) a estados más probables (más entropía). Aplicado al VC: si calculamos $\dot{S}_{\rm gen} < 0$ para un proceso propuesto, ese proceso viola la segunda ley y es físicamente imposible.

---

## Régimen estacionario: generación de entropía directamente observable

> [!proposicion]
> En régimen estacionario ($dS_{VC}/dt = 0$), con una entrada y una salida, $\dot{m}_1 = \dot{m}_2 = \dot{m}$:
> $$\dot{S}_{\rm gen} = \dot{m}(s_e - s_i) - \sum_k \frac{\dot{Q}_k}{T_k} \ge 0.$$
> En forma específica ($s_{\rm gen} = \dot{S}_{\rm gen}/\dot{m}$):
> $$s_{\rm gen} = (s_e - s_i) - \sum_k \frac{q_k}{T_k} \ge 0.$$
>
> **Caso adiabático** ($\dot{Q}_k = 0$):
> $$\dot{S}_{\rm gen} = \dot{m}(s_e - s_i) \ge 0 \implies s_e \ge s_i.$$
> En un dispositivo adiabático, la entropía específica del fluido **nunca puede decrecer**. Si un ingeniero presenta un diseño donde $s_2 < s_1$ en una turbina adiabática, el diseño es termodinámicamente imposible.

---

## Cómo usar el balance de entropía en la práctica

> [!teoria]
> El balance de entropía tiene dos aplicaciones principales:
>
> 1. **Verificar la viabilidad de un proceso:** dado un proceso propuesto con estados 1, 2 y calor $\dot{Q}$, calcular $\dot{S}_{\rm gen}$. Si $\dot{S}_{\rm gen} < 0$: el proceso viola la segunda ley, es imposible.
>
> 2. **Cuantificar las pérdidas por irreversibilidad:** $\dot{S}_{\rm gen}$ mide la "calidad de energía" disipada. Junto con el balance de exergía: $\dot{B}_{\rm dest} = T_0\,\dot{S}_{\rm gen}$. Minimizar $\dot{S}_{\rm gen}$ equivale a maximizar el trabajo útil del dispositivo.
>
> 3. **Encontrar el estado de salida de un proceso ideal vs. real:** para turbina adiabática ideal ($\dot{S}_{\rm gen} = 0$): $s_2 = s_1$ → proceso isentrópico. Para turbina real: $s_2 > s_1$ → estado de salida real.

---

## Proceso isentrópico como límite ideal

> [!proposicion]
> En un dispositivo adiabático ($\dot{Q} = 0$) y en régimen estacionario, la segunda ley impone:
> $$s_e \ge s_i.$$
> El caso $s_e = s_i$ ($s_{\rm gen} = 0$) corresponde al **proceso isentrópico ideal** — el límite reversible para ese dispositivo. Este límite es la referencia contra la que se define la **eficiencia isentrópica**:
>
> | Dispositivo | Eficiencia isentrópica | Definición |
> |:---|:---:|:---|
> | Turbina | $\eta_T$ | $w_{\rm real}/w_s = (h_1 - h_2)/(h_1 - h_{2s})$ |
> | Compresor | $\eta_C$ | $w_s/w_{\rm real} = (h_{2s} - h_1)/(h_2 - h_1)$ |
> | Tobera | $\eta_N$ | $V_e^2/V_{es}^2 = (h_1 - h_e)/(h_1 - h_{es})$ |

---

## Ejemplo: generación de entropía en un intercambiador de calor

> [!ejemplo]
> **Intercambiador de calor adiabático** (sin pérdidas al exterior). Corriente de aire caliente ($\dot{m}_H = 2\,\text{kg/s}$, $T_{H,1} = 500\,\text{K}$) cede calor a corriente de agua ($\dot{m}_C = 1\,\text{kg/s}$, $T_{C,1} = 300\,\text{K}$). Salidas: aire a $T_{H,2} = 350\,\text{K}$, agua a $T_{C,2} = ?$. Datos: $c_{p,\rm aire} = 1.005\,\text{kJ/(kg·K)}$, $c_{p,\rm agua} = 4.18\,\text{kJ/(kg·K)}$.
>
> **Paso 1 — Balance de masa:** dos fluidos separados, cada uno conserva su masa en régimen estacionario.
>
> **Paso 2 — Balance de energía del intercambiador completo** (VC que incluye ambas corrientes, adiabático con el exterior):
> $$\dot{m}_H c_{p,H}(T_{H,1} - T_{H,2}) = \dot{m}_C c_{p,C}(T_{C,2} - T_{C,1}).$$
> $$2 \times 1.005 \times (500 - 350) = 1 \times 4.18 \times (T_{C,2} - 300).$$
> $$301.5 = 4.18(T_{C,2} - 300) \implies T_{C,2} = 300 + 72.1 = 372.1\,\text{K}.$$
>
> **Paso 3 — Balance de entropía del intercambiador.** VC adiabático con dos entradas y dos salidas:
> $$\dot{S}_{\rm gen} = \dot{m}_H(s_{H,2} - s_{H,1}) + \dot{m}_C(s_{C,2} - s_{C,1}).$$
> Para gases ideales y líquidos incompresibles (variación isobárica): $\Delta s = c_p\ln(T_2/T_1)$.
> $$\dot{S}_{\rm gen} = 2 \times 1.005\ln\frac{350}{500} + 1 \times 4.18\ln\frac{372.1}{300}$$
> $$= 2.010 \times (-0.357) + 4.18 \times 0.2155 = -0.718 + 0.901 = +0.183\,\text{kW/K}.$$
>
> **Paso 4 — Verificar e interpretar.** $\dot{S}_{\rm gen} = 0.183\,\text{kW/K} > 0$ ✓. El proceso es irreversible (siempre lo es con diferencia finita de temperatura). La exergía destruida es $\dot{B}_{\rm dest} = T_0\dot{S}_{\rm gen} = 298 \times 0.183 = 54.5\,\text{kW}$ — esa potencia podría haberse convertido en trabajo útil en una instalación reversible (e.g., máquina de Carnot entre 500 K y 300 K). $\blacksquare$

---

## Relación con otras notas

> [!info]
> - [[Balance de Energia VC]] — da los estados de entrada/salida que aparecen en $\dot{m}(s_e - s_i)$.
> - [[Entropia]] — definición de $s$, su cálculo para gas ideal e incompresible.
> - [[Balance de Exergia VC]] — usa $\dot{S}_{\rm gen}$ de este balance: $\dot{B}_{\rm dest} = T_0\dot{S}_{\rm gen}$.
> - [[Sistemas/Dispositivos Flujo/index | Dispositivos de Flujo]] — eficiencia isentrópica de turbinas, compresores y toberas.

> [!warning]
> - $\dot{S}_{\rm gen}$ calculado $< 0$ significa que el proceso propuesto viola la segunda ley — revisar los datos o el modelo.
> - La temperatura $T_k$ en $\dot{Q}_k/T_k$ es la temperatura **en la frontera** del VC donde entra o sale el calor, no la temperatura interior del VC.
> - En el intercambiador de calor del ejemplo, los dos fluidos tienen fronteras separadas dentro del intercambiador; el VC único que los envuelve tiene una sola frontera exterior (adiabática).

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, §9.1–9.2; Çengel & Boles, *Termodinámica*, §7-1 a 7-4; Moran & Shapiro, §6.4.
