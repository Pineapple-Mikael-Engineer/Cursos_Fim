---
title: Procesos Psicrométricos
tags:
  - termodinamica
  - teoria
  - psicrometria
  - procesos
  - aire-humedo
draft: false
aliases:
  - Procesos Psicrometricos
  - Procesos Psicrométricos
  - HVAC
---

# Procesos Psicrométricos

> [!definicion]
> Un **proceso psicrométrico** es cualquier transformación del estado del aire húmedo. Los procesos fundamentales se clasifican según si cambia la composición ($\omega$) o solo la temperatura ($T$). En un diagrama psicrométrico, cada proceso es una trayectoria entre dos puntos de estado.

> [!info]
> **Base de cálculo.** Todos los balances se plantean por **kg de aire seco** (a.s.), porque la masa de aire seco es invariante en la mayoría de los procesos (solo cambia en la inyección/extracción de vapor). El flujo de aire seco $\dot{m}_a$ es la referencia.

---

## Proceso 1: Calentamiento sensible (sin cambio de $\omega$)

El aire pasa por una batería de calefacción sin aporte de humedad. $\omega=\text{cte}$, $P=\text{cte}$, $T$ aumenta. En el diagrama psicrométrico: **trayectoria horizontal** hacia la derecha.

**Balance de energía** (VC adiabático al exterior excepto la fuente de calor, flujo estacionario):
$$\dot{Q} = \dot{m}_a(h_2-h_1) = \dot{m}_a\,c_{pa,h}(T_2-T_1)$$
donde $c_{pa,h}=(1.005+1.86\,\omega)$ es el calor específico del aire húmedo a $\omega$ constante.

La humedad relativa **disminuye** al aumentar $T$ (con $P_v$ fija, $P_{\rm sat}(T)$ crece):
$$\phi_2 = \frac{P_v}{P_{\rm sat}(T_2)} < \phi_1.$$

---

## Proceso 2: Enfriamiento sensible por encima de $T_d$

Si $T_2 > T_d$: mismo análisis que calentamiento con $\dot{Q}<0$. $\omega$ no cambia.

---

## Proceso 3: Enfriamiento con condensación ($T_2 < T_d$)

Al enfriar por debajo del punto de rocío, el vapor comienza a condensar. La trayectoria en el diagrama psicrométrico sigue la curva de saturación ($\phi=1$) hasta $T_2$.

**Balance de masa de vapor:**
$$\dot{m}_{w,\rm cond} = \dot{m}_a(\omega_1 - \omega_2)$$
donde $\omega_2 = \omega_{\rm sat}(T_2) = 0.622\,P_{\rm sat}(T_2)/(P-P_{\rm sat}(T_2))$.

**Balance de energía:**
$$\dot{Q} = \dot{m}_a[(h_2-h_1) - (\omega_1-\omega_2)\,h_f(T_2)]$$
donde el término $(\omega_1-\omega_2)h_f(T_2)$ es la entalpía del condensado que sale como líquido a $T_2$.

![[proceso_enfriamiento_deshumidificacion.svg|440]]
*Diagrama psicrométrico: proceso de enfriamiento con deshumidificación. El estado 1 entra a la izquierda de $T_d$; al llegar a la curva de saturación ($\phi=1$) empieza la condensación; el estado 2 está sobre la curva a $T_2<T_d$. El estado del aire de salida queda siempre sobre la curva de saturación si el proceso termina en la bobina fría.*

---

## Proceso 4: Humidificación (inyección de vapor)

Se inyecta vapor de agua saturado (o sobrecalentado) al flujo de aire. $T$ cambia poco si el vapor entra cerca de la temperatura del aire.

**Balance de masa:** $\dot{m}_v = \dot{m}_a(\omega_2-\omega_1)$.

**Balance de energía:**
$$\dot{Q}+\dot{m}_v\,h_v = \dot{m}_a(h_2-h_1)$$
Si el proceso es adiabático y se inyecta vapor saturado a $T_v$:
$$h_2 = h_1 + (\omega_2-\omega_1)\,h_v(T_v).$$

Si se inyecta agua líquida en lugar de vapor (humidificador evaporativo): el agua se evapora tomando calor del aire, por lo que $T$ disminuye (proceso aproximadamente a $T_{bh}=\text{cte}$ si es adiabático).

---

## Proceso 5: Mezcla adiabática de dos corrientes

Dos flujos de aire húmedo con estados $(T_1,\omega_1,\dot{m}_{a,1})$ y $(T_2,\omega_2,\dot{m}_{a,2})$ se mezclan adiabáticamente.

**Balance de masa de aire seco:** $\dot{m}_{a,3}=\dot{m}_{a,1}+\dot{m}_{a,2}$.
**Balance de masa de vapor:** $\dot{m}_{a,3}\,\omega_3 = \dot{m}_{a,1}\,\omega_1 + \dot{m}_{a,2}\,\omega_2$.
**Balance de energía:** $\dot{m}_{a,3}\,h_3 = \dot{m}_{a,1}\,h_1 + \dot{m}_{a,2}\,h_2$.

De los tres balances:
$$\omega_3 = \frac{\dot{m}_{a,1}\,\omega_1+\dot{m}_{a,2}\,\omega_2}{\dot{m}_{a,1}+\dot{m}_{a,2}}, \qquad h_3 = \frac{\dot{m}_{a,1}\,h_1+\dot{m}_{a,2}\,h_2}{\dot{m}_{a,1}+\dot{m}_{a,2}}.$$

**Regla de la palanca psicrométrica.** El estado 3 divide el segmento $\overline{1\text{-}2}$ en el diagrama psicrométrico en razón inversa a los caudales:
$$\frac{d(1\text{-}3)}{d(2\text{-}3)} = \frac{\dot{m}_{a,2}}{\dot{m}_{a,1}}.$$

> [!demostracion]
> De $\omega_3 = \frac{\dot{m}_{a,1}\omega_1+\dot{m}_{a,2}\omega_2}{\dot{m}_{a,1}+\dot{m}_{a,2}}$:
> $$\omega_3-\omega_1 = \frac{\dot{m}_{a,2}}{\dot{m}_{a,1}+\dot{m}_{a,2}}(\omega_2-\omega_1).$$
> Análogamente para $h_3$, con $T_3\approx h_3/c_{pa,h}$:
> $$h_3-h_1 = \frac{\dot{m}_{a,2}}{\dot{m}_{a,1}+\dot{m}_{a,2}}(h_2-h_1).$$
> Ambas ecuaciones dicen que el punto $3$ divide al segmento $1$-$2$ en la misma razón en el plano $(\omega,h)$, es decir, en el diagrama psicrométrico. $\blacksquare$

![[mezcla_corrientes_psicrometrico.svg|420]]
*Diagrama psicrométrico: la mezcla adiabática de las corrientes 1 y 2 produce el estado 3 sobre el segmento $\overline{1\text{-}2}$. Si el segmento cruza la curva de saturación, el estado 3 estará en la zona de niebla y se producirá condensación.*

---

## Ejemplo complejo: sistema de climatización completo

> [!ejemplo]
> Un sistema de climatización procesa $\dot{m}_a=2\,\mathrm{kg/s}$ de aire seco. El aire exterior entra a $T_1=35\,°\mathrm{C}$, $\phi_1=80\%$, y debe entregarse al local a $T_4=22\,°\mathrm{C}$, $\phi_4=50\%$. El proceso consiste en:
> - **Etapa A**: enfriamiento con deshumidificación hasta $T_2=12\,°\mathrm{C}$, $\phi_2=100\%$ (bobina fría).
> - **Etapa B**: calentamiento sensible hasta $T_4=22\,°\mathrm{C}$ (batería de calefacción).
>
> $P=101.325\,\mathrm{kPa}$. Determinar: (a) todos los estados, (b) $\dot{Q}_{\rm enfr}$, (c) caudal de condensado $\dot{m}_w$, (d) $\dot{Q}_{\rm calef}$.

> [!solucion]
> **Tablas de saturación del agua:**
> $P_{\rm sat}(35\,°\mathrm{C})=5.629\,\mathrm{kPa}$; $P_{\rm sat}(12\,°\mathrm{C})=1.403\,\mathrm{kPa}$; $P_{\rm sat}(22\,°\mathrm{C})=2.645\,\mathrm{kPa}$.
>
> **Estado 1** ($T_1=35\,°\mathrm{C}$, $\phi_1=80\%$):
> $P_{v,1}=0.80\times5.629=4.503\,\mathrm{kPa}$.
> $\omega_1=0.622\times4.503/(101.325-4.503)=0.622\times4.503/96.822=0.02893\,\mathrm{kg/kg}$.
> $h_1=(1.005+1.86\times0.02893)\times35+2501\times0.02893=(1.005+0.05381)\times35+72.36=1.05881\times35+72.36=37.06+72.36=109.42\,\mathrm{kJ/kg}$.
>
> **Estado 2** ($T_2=12\,°\mathrm{C}$, $\phi_2=100\%$, saturado):
> $P_{v,2}=P_{\rm sat}(12)=1.403\,\mathrm{kPa}$.
> $\omega_2=0.622\times1.403/(101.325-1.403)=0.622\times1.403/99.922=0.008738\,\mathrm{kg/kg}$.
> $h_2=(1.005+1.86\times0.008738)\times12+2501\times0.008738=(1.005+0.01625)\times12+21.847=1.02125\times12+21.847=12.255+21.847=34.10\,\mathrm{kJ/kg}$.
>
> **Estado 4 (= estado de entrega)** ($T_4=22\,°\mathrm{C}$, $\phi_4=50\%$):
> $P_{v,4}=0.50\times2.645=1.3225\,\mathrm{kPa}$.
> $\omega_4=0.622\times1.3225/(101.325-1.3225)=0.622\times1.3225/100.003=0.008222\,\mathrm{kg/kg}$.
> $h_4=(1.005+1.86\times0.008222)\times22+2501\times0.008222=(1.005+0.01529)\times22+20.559=1.02029\times22+20.559=22.446+20.559=43.01\,\mathrm{kJ/kg}$.
>
> **Verificación del proceso B (calentamiento sensible):** el calentamiento de 2 a 4 es a $\omega=\text{cte}$. $\omega_2=0.008738$ vs. $\omega_4=0.008222$. No son iguales, lo que significa que la etapa B no puede reproducir exactamente $\omega_4$ solo con calentamiento. El proceso real requeriría una ligera deshumidificación adicional. Para este ejemplo simplificado, asumiremos que la etapa A lleva hasta $\omega_2=\omega_4=0.008222$, y la etapa B solo calienta:
>
> **Estado 2 corregido** ($\phi_2=100\%$, $\omega_2=0.008222$):
> $P_{v,2}=0.008222\times101.325/(0.622+0.008222)=0.008222\times101.325/0.630222=1.321\,\mathrm{kPa}$.
> $T_2=T_{\rm sat}(1.321\,\mathrm{kPa})\approx T_{\rm sat}(1.3225\,\mathrm{kPa})\approx11.1\,°\mathrm{C}$.
> $h_2=(1.005+1.86\times0.008222)\times11.1+2501\times0.008222=1.02029\times11.1+20.559=11.325+20.559=31.88\,\mathrm{kJ/kg}$.
> $h_f(11.1\,°\mathrm{C})\approx46.6\,\mathrm{kJ/kg}$ (entalpía del condensado).
>
> **(b) Calor de enfriamiento (Etapa A):**
> $\dot{m}_w=\dot{m}_a(\omega_1-\omega_2)=2\times(0.02893-0.008222)=2\times0.02071=0.04142\,\mathrm{kg/s}$.
> $$\dot{Q}_{\rm enfr}=\dot{m}_a[(h_2-h_1)-(\omega_1-\omega_2)h_f(T_2)]$$
> $$=2[(31.88-109.42)-0.02071\times46.6]=2[-77.54-0.965]=2\times(-78.50)=-157.0\,\mathrm{kW}.$$
> El sistema extrae $157.0\,\mathrm{kW}$.
>
> **(c) Caudal de condensado:**
> $\dot{m}_w=0.04142\,\mathrm{kg/s}=149.1\,\mathrm{kg/h}$.
>
> **(d) Calor de calefacción (Etapa B, de $T_2=11.1\,°\mathrm{C}$ a $T_4=22\,°\mathrm{C}$, $\omega=\text{cte}$):**
> $$\dot{Q}_{\rm calef}=\dot{m}_a(h_4-h_2)=2\times(43.01-31.88)=2\times11.13=22.26\,\mathrm{kW}. \qquad \blacksquare$$

> [!referencia]
> Çengel & Boles, *Termodinámica*, §14-4 a 14-7; Moran & Shapiro §12.6; ASHRAE Fundamentals Handbook, cap. 1.
