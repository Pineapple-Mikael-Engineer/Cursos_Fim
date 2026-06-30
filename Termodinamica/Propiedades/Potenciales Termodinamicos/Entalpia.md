---
title: "Entalpía $H$"
order: 2
tags:
  - termodinamica
  - potenciales_termodinamicos
  - entalpia
draft: false
aliases:
  - enthalpy
  - H
  - calor a presión constante
---

# Entalpía $H$

> [!definicion]
> La **entalpía** $H \equiv U + PV$ es el potencial termodinámico con variables naturales $(S, P)$. Su significado físico es doble:
>
> 1. **En sistemas de flujo estacionario:** $h = u + Pv$ es la energía que "lleva" cada kilogramo de fluido al cruzar una frontera de control. Al entrar al volumen de control, el fluido no solo trae su energía interna $u$, sino que además la corriente precedente "empuja" contra la presión, aportando un trabajo de flujo $Pv$ por kg. La suma $h = u + Pv$ es la energía total transportada por unidad de masa en flujo.
>
> 2. **En procesos isobáricos:** el calor intercambiado a presión constante es exactamente $\delta q_P = dh$, lo que hace a $h$ la propiedad central en calderas, condensadores y procesos de combustión.

---

## Por qué aparece $h$ en el balance de flujo estacionario

> [!demostracion]
> **Meta:** demostrar que la energía transportada por un fluido en flujo es $h = u + Pv$, no solo $u$.
>
> **Hipótesis:** flujo estacionario; un fluido que cruza una sección de entrada a presión $P_{\rm ent}$, volumen específico $v_{\rm ent}$, energía interna específica $u_{\rm ent}$.
>
> **Paso 1 — Balance de energía para el volumen de control en régimen estacionario.**
> La primera ley establece que la tasa de cambio de energía en el VC es cero (régimen permanente), así que todo el trabajo y calor que cruzan la frontera deben igualar el flujo neto de energía transportada por las corrientes másicas.
>
> **Paso 2 — Identificar los tipos de energía que cruzan la frontera.**
> Cuando 1 kg de fluido entra al VC a través de una sección de área $A$:
> - Trae su energía interna $u_{\rm ent}$ [kJ/kg].
> - Trae su energía cinética $V_{\rm ent}^2/2$ [kJ/kg].
> - Trae su energía potencial $g z_{\rm ent}$ [kJ/kg].
> - Además, el fluido que viene detrás lo empuja: eso es el **trabajo de flujo**.
>
> **Paso 3 — Calcular el trabajo de flujo.**
> El fluido detrás de la sección de entrada ejerce una fuerza $P_{\rm ent} A$ sobre el kg que acaba de entrar. Para desplazarlo una distancia $dL$ (de forma que ese kg ocupe su volumen $v_{\rm ent}$ dentro del VC), el trabajo realizado es:
> $$\delta W_{\rm flujo} = (P_{\rm ent}\,A)\,dL = P_{\rm ent}\,(A\,dL) = P_{\rm ent}\,dV = P_{\rm ent}\,v_{\rm ent} \quad [{\rm kJ/kg}].$$
>
> **Paso 4 — Energía total transportada por el fluido entrante.**
> La energía total que "entra" al VC por kg de fluido es:
> $$e_{\rm ent} = u_{\rm ent} + P_{\rm ent}\,v_{\rm ent} + \frac{V_{\rm ent}^2}{2} + g z_{\rm ent} = h_{\rm ent} + \frac{V_{\rm ent}^2}{2} + g z_{\rm ent}.$$
>
> **Paso 5 — Análisis equivalente en la salida y conclusión.**
> Al salir, el fluido empuja contra $P_{\rm sal}$ para abrirse paso: aportó un trabajo de flujo $P_{\rm sal}v_{\rm sal}$ que sale del sistema. La energía neta transportada por la corriente saliente es $h_{\rm sal} + V_{\rm sal}^2/2 + g z_{\rm sal}$. El balance de energía del VC mide diferencias en $h$, no en $u$, porque los fluidos en movimiento siempre llevan el trabajo de flujo $Pv$ consigo. $\blacksquare$

![[entalpia_flujo_trabajo_Pv.svg|440]]
*Volumen de control: el fluido a la izquierda empuja el kg entrante contra la presión $P_{\rm ent}$, realizando trabajo de flujo $P_{\rm ent}v_{\rm ent}$. A la derecha, el fluido saliente empuja hacia afuera con $P_{\rm sal}v_{\rm sal}$. La energía total del fluido en flujo es $h = u + Pv$.*

---

## Diferencial y variables naturales

> [!proposicion]
> De $H = U + PV$ y $dU = T\,dS - P\,dV$:
> $$dH = dU + P\,dV + V\,dP = (T\,dS - P\,dV) + P\,dV + V\,dP$$
> $$\boxed{dH = T\,dS + V\,dP.}$$
> Variables naturales: $(S, P)$. Derivadas primeras:
> $$T = \left(\frac{\partial H}{\partial S}\right)_P, \qquad V = \left(\frac{\partial H}{\partial P}\right)_S.$$

---

## Segunda relación de Maxwell (desde $H$)

> [!proposicion]
> Por la igualdad de derivadas cruzadas de $dH = T\,dS + V\,dP$:
> $$\left(\frac{\partial T}{\partial P}\right)_S = \left(\frac{\partial V}{\partial S}\right)_P.$$
> Es la segunda relación de Maxwell; entra en el cálculo de derivadas isentrópicas como $(\partial T/\partial P)_s = Tv\alpha/c_p$. Ver [[Maxwell]].

---

## Proceso isobárico: $q_P = \Delta h$

> [!proposicion]
> Para un sistema **cerrado** con $P = \text{cte}$ y sin trabajo de eje:
> $$dU = \delta Q - P\,dV \implies \delta Q = dU + P\,dV = dH \implies q_P = \Delta h.$$
> El calor intercambiado a presión constante es exactamente el cambio de entalpía. De aquí se define:
> $$c_p = \left(\frac{\partial h}{\partial T}\right)_P.$$

---

## Para gas ideal: $h = h(T)$ solamente

> [!demostracion]
> **Meta:** probar que la entalpía del gas ideal depende solo de $T$.
>
> **Hipótesis:** gas ideal — $Pv = RT$ (ecuación de estado) y $u = u(T)$ (resultado del experimento de Joule).
>
> **Paso 1 — Expresar $h$ como suma de $u$ y $Pv$:**
> $$h = u + Pv.$$
>
> **Paso 2 — Sustituir la ecuación de estado $Pv = RT$:**
> $$h = u + RT.$$
>
> **Paso 3 — Verificar que ambos términos dependen solo de $T$:**
> $u = u(T)$ por el experimento de Joule; $RT$ depende solo de $T$. Por tanto:
> $$h = h(T) \quad \text{únicamente.} \qquad \blacksquare$$
>
> **Paso 4 — Calcular $dh$:**
> $$dh = du + R\,dT = c_v\,dT + R\,dT = (c_v + R)\,dT = c_p\,dT,$$
> donde se usó la **relación de Mayer** $c_p - c_v = R$ (deducida para el gas ideal en [[Gas Ideal]]). Así $dh = c_p\,dT$ con $c_p$ constante.
>
> **Paso 5 — Verificar el límite para gases reales:**
> Para cualquier sustancia, $(\partial h/\partial P)_T = v(1 - T\alpha)$. Para gas ideal: $\alpha = 1/T$, luego $v(1 - T/T) = 0$, lo que confirma que $h$ no depende de $P$ para el gas ideal. Para gas real, $T\alpha \neq 1$ y la dependencia de $h$ en $P$ es el **efecto Joule-Thomson**. $\checkmark$

---

## Casos particulares

> [!proposicion]
> **Gas ideal** ($c_p$ constante en rango):
> $$\Delta h = c_p\,\Delta T.$$
>
> **Sustancia incompresible** ($dv \approx 0$):
> $$dh = du + v\,dP = c\,dT + v\,dP.$$
> Para proceso isobárico: $\Delta h = c\,\Delta T$. Para corrección de presión: $\Delta h \approx v\,\Delta P$ (líquido comprimido; ver [[Liquido Comprimido]]).

---

## Ejemplo: turbina de vapor con entalpías de tabla

> [!ejemplo]
> **Turbina adiabática de vapor con $\eta_T = 0.88$.** Entrada: $P_1 = 6\,\text{MPa}$, $T_1 = 500\,°\text{C}$; salida: $P_2 = 10\,\text{kPa}$.
>
> **Paso 1 — Leer $h_1$ y $s_1$ de tablas de vapor sobrecalentado:**
> $$h_1 = 3422.2\,\text{kJ/kg}, \quad s_1 = 6.8820\,\text{kJ/(kg·K)}.$$
>
> **Paso 2 — Estado isentrópico ($s_{2s} = s_1$) a $P_2 = 10\,\text{kPa}$:**
> A 10 kPa: $s_f = 0.649$, $s_g = 8.151\,\text{kJ/(kg·K)}$; $x_{2s} = (6.882 - 0.649)/(8.151 - 0.649) = 0.831$.
> $$h_{2s} = 191.8 + 0.831 \times 2392.8 = 2181.3\,\text{kJ/kg}.$$
>
> **Paso 3 — Trabajo isentrópico:**
> $$w_s = h_1 - h_{2s} = 3422.2 - 2181.3 = 1240.9\,\text{kJ/kg}.$$
>
> **Paso 4 — Trabajo real (con eficiencia):**
> $$w_{\rm real} = \eta_T\,w_s = 0.88 \times 1240.9 = 1092.0\,\text{kJ/kg}.$$
>
> **Paso 5 — Entalpía de salida real:**
> $$h_2 = h_1 - w_{\rm real} = 3422.2 - 1092.0 = 2330.2\,\text{kJ/kg}.$$
> (La salida real tiene calidad $x_2 = (2330.2 - 191.8)/2392.8 = 0.895$: mezcla húmeda. $\blacksquare$)

---

## Relación con otras notas

> [!info]
> - $H$ aparece en todos los balances de volumen de control: [[Balance de Energia VC]].
> - La relación $c_p - c_v = Tv\alpha^2/\kappa_T$ se deduce en [[Cp Cv/index | $c_p - c_v$]].
> - El efecto Joule-Thomson ($\mu_{JT}$) conecta $H$ con el coeficiente de expansión; ver [[Cp Cv/index | Efecto Joule-Thomson]].
> - $dH = T\,dS + V\,dP$ produce la segunda ecuación $T\,ds$; ver [[TdS]].

> [!info]
> **Convención:** $H$: extensiva [kJ]; $h = H/m$ [kJ/kg]; $\bar{h}$ [kJ/mol].

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, §5.4, §12.1; Çengel & Boles, *Termodinámica*, §5-1 a 5-3; Moran & Shapiro, §4.1–4.3; Callen, *Thermodynamics*, §5-2.
