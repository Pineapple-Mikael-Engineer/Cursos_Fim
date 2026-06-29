---
title: Procesos Psicrométricos
order: 2
tags:
  - termodinamica
  - psicrometria
  - procesos
  - aire-humedo
  - HVAC
draft: false
aliases:
  - Procesos Psicrométricos
  - Procesos Psicrometricos
  - HVAC
---

# Procesos Psicrométricos

> [!definicion]
> Un **proceso psicrométrico** es cualquier transformación del estado del aire húmedo. En la carta psicrométrica, cada proceso es una **trayectoria** entre dos puntos. La clave para analizar cualquier proceso es plantear simultáneamente:
> - **Balance de masa de aire seco** (siempre constante: $\dot{m}_a = \text{cte}$).
> - **Balance de masa de vapor de agua** ($\dot{m}_a\,\omega_2 = \dot{m}_a\,\omega_1 \pm \dot{m}_{agua}$).
> - **Balance de energía** (primera ley para VC estacionario, sin trabajo de eje).
>
> Todos los balances se plantean **por kg de aire seco**, ya que $\dot{m}_a$ es la cantidad conservada en procesos de climatización.

---

## Proceso 1: Calentamiento sensible

> [!teoria]
> El aire pasa por una batería de calefacción sin aporte de humedad. Resultado: $T$ sube, $\omega$ no cambia (trayectoria horizontal en la carta), $\phi$ **disminuye** (porque $P_{\rm sat}$ sube pero $P_v$ no).
>
> **Balance de energía** (VC estacionario, $\dot{W}=0$, $\dot{m}_a$ constante):
> $$\dot{Q}_{\rm cal} = \dot{m}_a(h_2-h_1) = \dot{m}_a\,(1.005+1.86\,\omega)\,(T_2-T_1).$$

---

## Proceso 2: Enfriamiento sin condensación

> [!teoria]
> Análogo al calentamiento con $\dot{Q}<0$. $\omega$ no cambia; $\phi$ **aumenta** al bajar $T$. El proceso es horizontal en la carta, desplazándose hacia la izquierda. El límite es cuando $T$ alcanza $T_d$: en ese punto $\phi=100\%$ y comienza la condensación.

---

## Proceso 3: Enfriamiento con deshumidificación ($T_2 < T_d$)

> [!teoria]
> Al enfriar por debajo del punto de rocío, el vapor condensa y $\omega$ disminuye. En la carta: la trayectoria va horizontalmente hasta la curva de saturación (donde empieza la condensación) y luego **desciende sobre ella** hasta $T_2$.
>
> El estado de salida está en la curva $\phi=100\%$ a temperatura $T_2$:
> $$\omega_2 = 0.622\,\frac{P_{\rm sat}(T_2)}{P - P_{\rm sat}(T_2)}.$$

> [!proposicion]
> Balance de masa de agua condensada y balance de energía del proceso de enfriamiento-deshumidificación:
>
> **Masa de condensado** (sale como líquido a $T_2$):
> $$\dot{m}_{\rm cond} = \dot{m}_a(\omega_1 - \omega_2).$$
>
> **Balance de energía** (el condensado sale con entalpía $h_f(T_2)$):
> $$\dot{Q}_{\rm enfr} = \dot{m}_a\left[(h_2 - h_1) - (\omega_1-\omega_2)\,h_f(T_2)\right].$$

> [!demostracion]
> **Hipótesis:** VC estacionario, $\dot{W}=0$, el condensado sale como líquido saturado a $T_2$, $\dot{m}_a$ constante.
>
> **Paso 1 — Balance de masa de vapor.** Entrada: $\dot{m}_a\,\omega_1$. Salida: $\dot{m}_a\,\omega_2$ (con el aire) $+\, \dot{m}_{\rm cond}$ (como líquido). Entonces $\dot{m}_{\rm cond} = \dot{m}_a(\omega_1-\omega_2)$.
>
> **Paso 2 — Primera ley del VC.** Sin trabajo, en régimen estacionario:
> $$\dot{Q} = \dot{H}_{\rm sal} - \dot{H}_{\rm ent}.$$
>
> **Paso 3 — Entalpías de entrada y salida.** Entrada: $\dot{m}_a\,(h_1)$ (aire húmedo a estado 1). Salida: $\dot{m}_a\,h_2$ (aire húmedo a estado 2) $+\, \dot{m}_{\rm cond}\,h_f(T_2)$ (condensado).
>
> **Paso 4 — Sustituir:** dividiendo entre $\dot{m}_a$:
> $$q = h_2 + (\omega_1-\omega_2)\,h_f(T_2) - h_1.$$
>
> **Paso 5 — Reorganizar** ($q$ es negativo, el sistema pierde calor):
> $$\dot{Q} = \dot{m}_a\left[(h_2-h_1) - (\omega_1-\omega_2)\,h_f(T_2)\right]. \qquad \blacksquare$$
>
> *Nota:* el término $-(\omega_1-\omega_2)\,h_f(T_2)$ representa el calor que "se lleva" el condensado al salir. Normalmente es pequeño (< 2% del calor total) porque $h_f \approx 4.18\times T_2$ kJ/kg y $T_2$ es baja.

![[proceso_enfriamiento_deshumidificacion.svg|440]]
*Trayectoria del proceso de enfriamiento con deshumidificación. Estado 1: aire caliente húmedo. Se enfría horizontalmente hasta la curva de saturación ($T_d$); luego desciende sobre $\phi=100\%$ hasta $T_2$.*

---

## Proceso 4: Humidificación

> [!teoria]
> Se añade vapor o agua líquida al flujo de aire, aumentando $\omega$.
>
> **Inyección de vapor saturado a $T_v$:**
> $$h_2 = h_1 + (\omega_2-\omega_1)\,h_g(T_v).$$
> Si $T_v \approx T_1$, la temperatura no cambia significativamente (el vapor entra con entalpía similar al del vapor ya en el aire).
>
> **Humidificador evaporativo** (agua líquida): el agua se evapora tomando calor sensible del aire, bajando $T$ mientras sube $\omega$. El proceso es aproximadamente a $h \approx \text{cte}$ (entalpía constante) si es adiabático, siguiendo una línea de $T_{bh} \approx \text{cte}$ en la carta.

---

## Proceso 5: Mezcla adiabática de dos corrientes

> [!proposicion]
> Dos corrientes de aire húmedo (1 y 2) se mezclan adiabáticamente para producir la corriente 3. Los balances:
>
> **Masa de aire seco:** $\dot{m}_{a3} = \dot{m}_{a1} + \dot{m}_{a2}$.
>
> **Masa de vapor:** $\dot{m}_{a3}\,\omega_3 = \dot{m}_{a1}\,\omega_1 + \dot{m}_{a2}\,\omega_2$.
>
> **Energía:** $\dot{m}_{a3}\,h_3 = \dot{m}_{a1}\,h_1 + \dot{m}_{a2}\,h_2$.
>
> Resultados:
> $$\omega_3 = \frac{\dot{m}_{a1}\,\omega_1 + \dot{m}_{a2}\,\omega_2}{\dot{m}_{a1}+\dot{m}_{a2}}, \qquad h_3 = \frac{\dot{m}_{a1}\,h_1 + \dot{m}_{a2}\,h_2}{\dot{m}_{a1}+\dot{m}_{a2}}.$$

> [!demostracion]
> **Hipótesis:** VC adiabático, sin trabajo, régimen estacionario.
>
> **Paso 1 — Balance de masa total.** $\dot{m}_{a3} = \dot{m}_{a1}+\dot{m}_{a2}$.
>
> **Paso 2 — Balance de masa de vapor.** $\dot{m}_{a3}\,\omega_3 = \dot{m}_{a1}\,\omega_1+\dot{m}_{a2}\,\omega_2$. Despejando: $\omega_3 = (\dot{m}_{a1}\,\omega_1+\dot{m}_{a2}\,\omega_2)/\dot{m}_{a3}$.
>
> **Paso 3 — Balance de energía.** $\dot{m}_{a3}\,h_3 = \dot{m}_{a1}\,h_1+\dot{m}_{a2}\,h_2$. Despejando: $h_3 = (\dot{m}_{a1}\,h_1+\dot{m}_{a2}\,h_2)/\dot{m}_{a3}$.
>
> **Paso 4 — Posición geométrica en la carta.** Tanto $\omega_3$ como $h_3$ son promedios ponderados de (1) y (2). Esto equivale geométricamente a que el estado 3 divide el segmento $\overline{1\text{-}2}$ en razón inversa a los caudales:
> $$\frac{d(1\text{-}3)}{d(2\text{-}3)} = \frac{\dot{m}_{a2}}{\dot{m}_{a1}}.$$
>
> **Paso 5 — Verificación (caso igual mezcla).** Si $\dot{m}_{a1}=\dot{m}_{a2}$: $\omega_3=({\omega_1+\omega_2})/2$, $h_3=(h_1+h_2)/2$ → el estado 3 es el punto medio del segmento. ✓ $\blacksquare$

![[mezcla_corrientes_psicrometrico.svg|420]]
*Regla de la palanca psicrométrica: el estado de mezcla (3) se ubica sobre el segmento $\overline{1\text{-}2}$ en proporción inversa a los caudales. Si el segmento cruza la curva de saturación, el estado real tendrá niebla.*

---

## Ejemplo complejo: sistema de climatización completo

> [!ejemplo]
> Un sistema de climatización procesa $\dot{m}_a = 2\,\mathrm{kg\,a.s./s}$. Condiciones: aire exterior a $T_1=35\,°\mathrm{C}$, $\phi_1=80\%$. Se requiere entregar al local a $T_4=22\,°\mathrm{C}$, $\phi_4=50\%$. Proceso:
> - **Etapa A:** enfriamiento con deshumidificación hasta $\phi_2=100\%$ a la temperatura necesaria.
> - **Etapa B:** calentamiento sensible hasta $T_4=22\,°\mathrm{C}$.
>
> $P=101.325\,\mathrm{kPa}$. Determinar: (a) estados en los puntos clave; (b) $\dot{Q}_{\rm enfr}$; (c) $\dot{m}_{\rm cond}$; (d) $\dot{Q}_{\rm calef}$.

> [!solucion]
> **Tablas de saturación:**
> $P_{\rm sat}(35) = 5.629\,\mathrm{kPa}$; $P_{\rm sat}(22) = 2.645\,\mathrm{kPa}$; $P_{\rm sat}(11.1) = 1.321\,\mathrm{kPa}$.
>
> **Estado 4 (condición de entrega):** $T_4=22\,°\mathrm{C}$, $\phi_4=50\%$.
> $P_{v,4} = 0.50\times2.645 = 1.3225\,\mathrm{kPa}$.
> $\omega_4 = 0.622\times1.3225/(101.325-1.3225) = 0.008222\,\mathrm{kg/kg}$.
> $h_4 = (1.005+1.86\times0.008222)\times22+2501\times0.008222 = 1.0203\times22+20.56 = 43.0\,\mathrm{kJ/kg}$.
>
> **Estado 2 (fin de etapa A = inicio de etapa B).** La etapa B es calentamiento sensible: $\omega_2 = \omega_4 = 0.008222\,\mathrm{kg/kg}$. El estado 2 está en $\phi_2=100\%$ con ese $\omega$:
> $P_{v,2} = 0.008222\times101.325/(0.622+0.008222) = 1.321\,\mathrm{kPa}$.
> $T_2 = T_{\rm sat}(1.321\,\mathrm{kPa}) \approx 11.1\,°\mathrm{C}$.
> $h_2 = (1.005+1.86\times0.008222)\times11.1+2501\times0.008222 = 1.0203\times11.1+20.56 = 11.33+20.56 = 31.9\,\mathrm{kJ/kg}$.
> $h_f(11.1\,°\mathrm{C}) \approx 46.6\,\mathrm{kJ/kg}$.
>
> **Estado 1 (entrada):** $T_1=35\,°\mathrm{C}$, $\phi_1=80\%$.
> $P_{v,1} = 0.80\times5.629 = 4.503\,\mathrm{kPa}$.
> $\omega_1 = 0.622\times4.503/(101.325-4.503) = 0.02893\,\mathrm{kg/kg}$.
> $h_1 = (1.005+1.86\times0.02893)\times35+2501\times0.02893 = 1.0588\times35+72.36 = 37.06+72.36 = 109.4\,\mathrm{kJ/kg}$.
>
> **(b) Calor de enfriamiento (etapa A):**
> $\dot{m}_{\rm cond} = \dot{m}_a(\omega_1-\omega_2) = 2\times(0.02893-0.008222) = 2\times0.02071 = 0.04142\,\mathrm{kg/s}$.
>
> $\dot{Q}_{\rm enfr} = \dot{m}_a[(h_2-h_1)-(\omega_1-\omega_2)\,h_f(T_2)]$.
> $= 2\times[(31.9-109.4)-0.02071\times46.6] = 2\times[-77.5-0.965] = 2\times(-78.5) = -156.9\,\mathrm{kW}$.
>
> **(c) Condensado:**
> $\dot{m}_{\rm cond} = 0.04142\,\mathrm{kg/s} = 149.1\,\mathrm{kg/h}$.
>
> **(d) Calor de calefacción (etapa B):**
> $\dot{Q}_{\rm calef} = \dot{m}_a(h_4-h_2) = 2\times(43.0-31.9) = 2\times11.1 = 22.2\,\mathrm{kW}$.
>
> $\boxed{\dot{Q}_{\rm enfr} = -156.5\,\mathrm{kW},\quad \dot{Q}_{\rm calef} = 22.2\,\mathrm{kW},\quad \dot{m}_{\rm cond} = 149\,\mathrm{kg/h}.}$ $\blacksquare$

> [!referencia]
> Çengel & Boles, §14-4 a 14-7; Moran & Shapiro, §12.6; ASHRAE Fundamentals, cap. 1.
