---
title: Sistema Cerrado
order: 1
tags:
  - termodinamica
  - sistemas
  - sistema-cerrado
draft: false
aliases:
  - closed system
  - masa de control
  - sistemas cerrados
  - SC
---

# Sistema Cerrado

> [!definicion]
> Un **sistema cerrado** (SC) — también llamado *masa de control* — es una región del espacio cuya **masa es fija**: no cruza materia a través de su frontera, aunque sí puede cruzar calor y trabajo. La frontera puede ser rígida o móvil (pistón).
>
> *¿Por qué este modelo?* En muchos procesos de interés la masa de fluido es siempre la misma: gas atrapado en un cilindro, una bomba de calor en proceso por lotes, un globo que se infla. Fijar la masa elimina el término de flujo másico y simplifica radicalmente los balances.
>
> *Diferencia esencial con el volumen de control:* en el SC no hay entalpía transportada por corrientes de masa — la propiedad natural es la [[Energia Interna | energía interna]] $U$, no la [[Entalpia | entalpía]] $h$. El trabajo de eje (émbolo) sí aparece directamente como $\int P\,dV$.
>
> *Aplicaciones:* pistón-cilindro (ciclos Otto, Diesel), reactores batch, globos y cámaras de gas, recipientes a presión sin flujo.

---

## Primera Ley: $\Delta U = Q - W$

> [!teorema]
> Para un sistema cerrado entre dos estados 1 y 2:
> $$\boxed{\Delta U = U_2 - U_1 = Q_{12} - W_{12}.}$$
>
> Con convención: $Q>0$ calor que **entra** al sistema; $W>0$ trabajo realizado **por** el sistema.
>
> En forma diferencial (proceso infinitesimal):
> $$dU = \delta Q - \delta W.$$

> [!demostracion]
> **Hipótesis:** sistema de masa $m$ constante, sin EC ni EP (el sistema no traslada ni rota globalmente).
>
> **Paso 1 — Balance de energía general.** La energía total del sistema es $E = U + EC + EP$. El primer principio para cualquier sistema (SC o VC) establece que la variación de $E$ iguala la transferencia neta de energía a través de la frontera:
> $$\frac{dE}{dt} = \dot{Q} - \dot{W}.$$
>
> **Paso 2 — Aplicar $\Delta EC = \Delta EP = 0$.** Para un SC en reposo macroscópico: $\frac{d}{dt}(U+EC+EP) = \frac{dU}{dt}$. Luego:
> $$\frac{dU}{dt} = \dot{Q} - \dot{W}.$$
>
> **Paso 3 — Integrar entre estados.** Integrando desde $t_1$ hasta $t_2$:
> $$U_2 - U_1 = Q_{12} - W_{12}.$$
>
> **Paso 4 — Descomponer el trabajo.** El trabajo total incluye trabajo de frontera móvil (pdV) y trabajo de eje o eléctrico:
> $$W_{12} = \underbrace{\int_1^2 P\,dV}_{W_{\rm frontera}} + W_{\rm eje} + W_{\rm elec} + \cdots$$
> Para proceso **cuasiestático** (reversible lento): $W_{\rm frontera} = \int P\,dV$. Para proceso irreversible (expansión libre, estrangulamiento dentro del SC): no se puede usar $\int P\,dV$.
>
> **Paso 5 — Caso simple: SC rígido.** Si la frontera no se mueve ($dV=0$), $W_{\rm frontera}=0$ y $\Delta U = Q_{12}$: todo el calor va directamente a energía interna. En un SC con pistón adiabático ($Q=0$): $\Delta U = -W$ — el sistema se enfría al expandir. $\blacksquare$

---

## Segunda ley y generación de entropía

> [!teorema]
> Para un SC que intercambia calor con una fuente a temperatura de frontera $T_b$:
> $$dS = \frac{\delta Q}{T_b} + \delta S_{\rm gen}, \qquad \delta S_{\rm gen} \geq 0.$$
> Integrado: $S_2 - S_1 = \int_1^2 \frac{\delta Q}{T_b} + S_{\rm gen}$. Para un proceso **adiabático**: $\Delta S \geq 0$ (la entropía no puede disminuir en un SC aislado).

---

## Trabajo de frontera móvil

> [!proposicion]
> Para un SC con pistón en proceso **cuasiestático** (equilibrio en todo instante):
> $$W_{12} = \int_1^2 P\,dV.$$
>
> | Proceso | $W_{12}$ |
> |:---|:---|
> | Isocórico ($V=\text{cte}$) | $0$ |
> | Isobárico ($P=\text{cte}$) | $P(V_2-V_1)$ |
> | Isotérmico (gas ideal) | $mRT\ln(V_2/V_1)$ |
> | Politrópico ($PV^n=\text{cte}$) | $\dfrac{P_2V_2-P_1V_1}{1-n}$ ($n\neq1$) |
>
> Para un proceso **irreversible** (expansión contra presión constante externa $P_{\rm ext}$): $W = P_{\rm ext}(V_2-V_1)$, que es menor que el trabajo reversible máximo.

---

## Ejemplo: gas en pistón-cilindro con calefacción isobárica

> [!ejemplo]
> 0.2 kg de nitrógeno ($M=28\,\mathrm{kg/kmol}$, $c_v=0.743\,\mathrm{kJ/(kg\cdot K)}$, $c_p=1.040\,\mathrm{kJ/(kg\cdot K)}$) se calientan isobáricamente desde $T_1=300\,\mathrm{K}$ hasta $T_2=600\,\mathrm{K}$ a $P=200\,\mathrm{kPa}$. Calcular: (a) $W_{12}$; (b) $Q_{12}$; (c) $\Delta U$; (d) $\Delta S$.

> [!solucion]
> **Paso 1 — Trabajo de frontera.** $W_{12}=P(V_2-V_1)=P m R_{\rm esp}(T_2-T_1)/P = m R_{\rm esp}(T_2-T_1)$.
> $R_{\rm esp}=R/M=8.314/28=0.297\,\mathrm{kJ/(kg\cdot K)}$.
> $$W_{12}=0.2\times0.297\times300=17.8\,\mathrm{kJ}.$$
>
> **Paso 2 — Calor absorbido.** En proceso isobárico, $Q_{12}=mc_p(T_2-T_1)=0.2\times1.040\times300=62.4\,\mathrm{kJ}$.
>
> **Paso 3 — Variación de energía interna.** Primera ley: $\Delta U=Q-W=62.4-17.8=44.6\,\mathrm{kJ}$. Verificación: $\Delta U=mc_v(T_2-T_1)=0.2\times0.743\times300=44.6\,\mathrm{kJ}$ ✓.
>
> **Paso 4 — Variación de entropía.** Para gas ideal en proceso isobárico:
> $$\Delta S = mc_p\ln\frac{T_2}{T_1} = 0.2\times1.040\times\ln2 = 0.2\times1.040\times0.693 = 0.144\,\mathrm{kJ/K}.$$
>
> **Paso 5 — Verificación de la segunda ley.** $Q_{12}/T_{\rm media} \approx 62.4/[(300+600)/2]=62.4/450=0.139\,\mathrm{kJ/K}$. Como $\Delta S=0.144>0.139$, la generación de entropía es positiva (irreversibilidad por transferencia de calor a través de gradiente finito). ✓
>
> $\boxed{W=17.8\,\mathrm{kJ},\quad Q=62.4\,\mathrm{kJ},\quad \Delta U=44.6\,\mathrm{kJ},\quad \Delta S=0.144\,\mathrm{kJ/K}.}$ $\blacksquare$

> [!info]
> **Convención:** $Q>0$ calor que entra al SC; $W>0$ trabajo realizado por el SC. Propiedades extensivas en mayúscula ($U$, $S$, $V$); específicas en minúscula ($u$, $s$, $v$). Los balances detallados están en [[Primera Ley SC]] y [[Segunda Ley SC]].

> [!referencia]
> Borgnakke & Sonntag, Cap. 4–5; Çengel & Boles, Cap. 4; Moran & Shapiro, Cap. 2.
