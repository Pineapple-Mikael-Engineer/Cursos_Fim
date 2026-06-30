---
title: Intercambiadores de Calor
order: 6
tags:
  - termodinamica
  - dispositivos-flujo
  - intercambiadores
  - transferencia-calor
draft: false
aliases:
  - heat exchanger
  - intercambiador
  - Intercambiadores de Calor
  - HX
---

# Intercambiadores de Calor

> [!definicion]
> Un **intercambiador de calor** (HX) es un volumen de control de flujo estacionario que transfiere calor entre dos o más corrientes de fluido **sin que se mezclen físicamente**. Las corrientes están separadas por paredes sólidas (tubos, placas, espirales). No hay trabajo de eje ($\dot{W}=0$) y el VC completo es externamente adiabático.
>
> *¿Por qué son tan importantes?* Recuperar calor de una corriente caliente para precalentar otra evita quemar combustible extra. En una planta de ciclo combinado, los recuperadores de calor de gases de escape (HRSGs) elevan la eficiencia global del 35% al 58%. La regla de Carnot garantiza que la transferencia de calor entre fluidos de diferente temperatura es siempre irreversible — el objetivo del diseño es minimizar esa diferencia.
>
> *Tipos principales:* tubos y carcasa (shell & tube), placas, doble tubo, compactos (aletas-tubos). Las configuraciones de flujo son: **paralelo**, **contraflujo** y **flujo cruzado**.

![[intercambiador_contraflujo_esquema.svg|460]]
*Intercambiador de doble tubo en contraflujo. La corriente caliente ($T_h$) entra por la derecha y la fría ($T_c$) por la izquierda. En contraflujo la diferencia de temperatura es más uniforme a lo largo del intercambiador, lo que maximiza la transferencia.*

---

## Balance de energía

> [!teorema]
> Para un intercambiador de calor en flujo estacionario, externamente adiabático ($\dot{Q}_{\rm ext}=0$), sin trabajo de eje, despreciando $\Delta EC$ y $\Delta EP$:
>
> **Conservación de masa** (por separado en cada corriente): $\dot{m}_h = \text{cte}$, $\dot{m}_c = \text{cte}$.
>
> **Primera ley:** el calor cedido por la corriente caliente igual al absorbido por la fría:
> $$\boxed{\dot{Q} = \dot{m}_h(h_{h,1}-h_{h,2}) = \dot{m}_c(h_{c,2}-h_{c,1}).}$$
>
> Para fluidos con $c_p$ constante (sin cambio de fase): $\dot{Q} = \dot{m}_h c_{p,h}(T_{h,1}-T_{h,2}) = \dot{m}_c c_{p,c}(T_{c,2}-T_{c,1})$.
>
> **Segunda ley:**
> $$\dot{S}_{\rm gen} = \dot{m}_h(s_{h,2}-s_{h,1}) + \dot{m}_c(s_{c,2}-s_{c,1}) \geq 0.$$

> [!demostracion]
> **Hipótesis:** VC estacionario, $\dot{Q}_{\rm ext}=0$ (el VC encierra ambas corrientes), $\dot{W}=0$, $\Delta EC=\Delta EP=0$, dos corrientes sin mezcla.
>
> **Paso 1 — Dibujar el VC.** El volumen de control abarca ambos lados del intercambiador. Hay cuatro corrientes cruzando la frontera: dos entradas ($\dot{m}_h$ en la entrada caliente, $\dot{m}_c$ en la entrada fría) y dos salidas.
>
> **Paso 2 — Primera ley del VC.** Con $\dot{Q}_{\rm ext}=0$ y $\dot{W}=0$:
> $$0 = \dot{m}_h h_{h,2} + \dot{m}_c h_{c,2} - \dot{m}_h h_{h,1} - \dot{m}_c h_{c,1}.$$
>
> **Paso 3 — Reorganizar.** Agrupando por corriente:
> $$\dot{m}_h(h_{h,1}-h_{h,2}) = \dot{m}_c(h_{c,2}-h_{c,1}).$$
> El lado izquierdo es el calor cedido por la corriente caliente; el derecho es el calor absorbido por la fría. Son iguales porque no hay pérdidas al exterior.
>
> **Paso 4 — Caso con cambio de fase.** Si la corriente caliente condensa a $T_{\rm sat}$: $h_{h,1}-h_{h,2} = h_{fg}$ (para condensación total) o bien $h_{h,1}-h_{h,2} = h_{fg}+c_{p,l}(T_{\rm sat}-T_{h,2})$ si hay subenfriamiento.
>
> **Paso 5 — Segunda ley.** Para el VC aislado, toda la entropía generada internamente debe aparecer en las corrientes de salida:
> $$\dot{S}_{\rm gen} = (\dot{m}_h s_{h,2} + \dot{m}_c s_{c,2}) - (\dot{m}_h s_{h,1} + \dot{m}_c s_{c,1}) = \dot{m}_h(s_{h,2}-s_{h,1}) + \dot{m}_c(s_{c,2}-s_{c,1}) \geq 0.$$
> La irreversibilidad proviene de la transferencia de calor a través de una diferencia finita de temperatura. $\blacksquare$

---

## Método $\varepsilon$-NTU

> [!teoria]
> El método $\varepsilon$-NTU relaciona la eficiencia del intercambiador con el área de transferencia y los caudales másicos, útil cuando no se conocen las temperaturas de salida a priori.
>
> **Definiciones:**
> - Capacidades térmicas: $C_h = \dot{m}_h c_{p,h}$, $C_c = \dot{m}_c c_{p,c}$ [kW/K].
> - $C_{\rm min} = \min(C_h, C_c)$, $C_{\rm max} = \max(C_h, C_c)$, $C_r = C_{\rm min}/C_{\rm max} \leq 1$.
> - Número de unidades de transferencia: $NTU = UA/C_{\rm min}$, donde $U$ es el coeficiente global [kW/(m²·K)] y $A$ el área [m²].
> - Calor máximo posible: $\dot{Q}_{\rm max} = C_{\rm min}(T_{h,1}-T_{c,1})$ (ocurriría si la corriente de $C_{\rm min}$ alcanzara la temperatura de entrada de la otra).
> - **Eficiencia**: $\varepsilon = \dot{Q}/\dot{Q}_{\rm max}$.
>
> **Correlaciones $\varepsilon$-NTU:**
>
> | Configuración | Relación |
> |:---|:---|
> | Contraflujo, $C_r < 1$ | $\varepsilon = \dfrac{1 - e^{-NTU(1-C_r)}}{1 - C_r\,e^{-NTU(1-C_r)}}$ |
> | Contraflujo, $C_r = 1$ | $\varepsilon = \dfrac{NTU}{1+NTU}$ |
> | Flujo paralelo | $\varepsilon = \dfrac{1-e^{-NTU(1+C_r)}}{1+C_r}$ |
> | Cambio de fase ($C_r=0$) | $\varepsilon = 1 - e^{-NTU}$ |

---

## Ejemplo: intercambiador agua-agua en contraflujo

> [!ejemplo]
> Agua caliente ($\dot{m}_h=2\,\mathrm{kg/s}$, $c_{p,h}=4.18\,\mathrm{kJ/(kg\cdot K)}$, $T_{h,1}=80\,°\mathrm{C}$) calienta agua fría ($\dot{m}_c=3\,\mathrm{kg/s}$, $c_{p,c}=4.18\,\mathrm{kJ/(kg\cdot K)}$, $T_{c,1}=20\,°\mathrm{C}$) en un intercambiador de contraflujo con $UA=50\,\mathrm{kW/K}$ y $T_0=298\,\mathrm{K}$. Determinar: (a) $\dot{Q}$; (b) temperaturas de salida; (c) $\dot{S}_{\rm gen}$ y $\dot{X}_{\rm dest}$.

> [!solucion]
> **Paso 1 — Capacidades térmicas.**
> $$C_h = 2\times4.18 = 8.36\,\mathrm{kW/K}, \quad C_c = 3\times4.18 = 12.54\,\mathrm{kW/K}.$$
> $C_{\rm min}=8.36\,\mathrm{kW/K}$ (corriente caliente), $C_r=8.36/12.54=0.667$.
>
> **Paso 2 — NTU y eficiencia.**
> $$NTU = UA/C_{\rm min} = 50/8.36 = 5.98.$$
> $$NTU(1-C_r) = 5.98\times0.333 = 1.991, \quad e^{-1.991}=0.137.$$
> $$\varepsilon = \frac{1-0.137}{1-0.667\times0.137} = \frac{0.863}{0.9086} = 0.950.$$
>
> **Paso 3 — Calor transferido.**
> $$\dot{Q}_{\rm max} = C_{\rm min}(T_{h,1}-T_{c,1}) = 8.36\times60 = 501.6\,\mathrm{kW}.$$
> $$\dot{Q} = \varepsilon\,\dot{Q}_{\rm max} = 0.950\times501.6 = 476.5\,\mathrm{kW}.$$
>
> **Paso 4 — Temperaturas de salida.**
> $$T_{h,2} = T_{h,1} - \dot{Q}/C_h = 80 - 476.5/8.36 = 80-57.0 = 23.0\,°\mathrm{C}.$$
> $$T_{c,2} = T_{c,1} + \dot{Q}/C_c = 20 + 476.5/12.54 = 20+38.0 = 58.0\,°\mathrm{C}.$$
> Verificación: $T_{c,2}(58)<T_{h,1}(80)$ ✓ y $T_{h,2}(23)>T_{c,1}(20)$ ✓.
>
> **Paso 5 — Generación de entropía y destrucción de exergía.** En Kelvin: $T_{h,1}=353.15$, $T_{h,2}=296.15$, $T_{c,1}=293.15$, $T_{c,2}=331.15$.
> $$\Delta s_h = c_{p,h}\ln\frac{T_{h,2}}{T_{h,1}} = 4.18\ln\frac{296.15}{353.15} = 4.18\times(-0.176) = -0.736\,\mathrm{kJ/(kg\cdot K)}.$$
> $$\Delta s_c = 4.18\ln\frac{331.15}{293.15} = 4.18\times0.122 = 0.510\,\mathrm{kJ/(kg\cdot K)}.$$
> $$\dot{S}_{\rm gen} = \dot{m}_h\Delta s_h + \dot{m}_c\Delta s_c = 2\times(-0.736)+3\times0.510 = -1.472+1.530 = 0.058\,\mathrm{kW/K}.$$
> $$\dot{X}_{\rm dest} = T_0\dot{S}_{\rm gen} = 298\times0.058 = 17.3\,\mathrm{kW}.$$
>
> $\boxed{\dot{Q}=476.5\,\mathrm{kW},\quad T_{h,2}=23\,°\mathrm{C},\quad T_{c,2}=58\,°\mathrm{C},\quad \dot{X}_{\rm dest}=17.3\,\mathrm{kW}.}$ $\blacksquare$

---

## Ejemplo: condensador de vapor (cambio de fase)

> [!ejemplo]
> En un condensador de planta de potencia, vapor saturado a $T_{\rm sat}=40\,°\mathrm{C}$ ($P_{\rm sat}=7.38\,\mathrm{kPa}$, $h_{fg}=2406.7\,\mathrm{kJ/kg}$) condensa completamente a razón de $\dot{m}_h=50\,\mathrm{kg/s}$. El agua de enfriamiento entra a $T_{c,1}=20\,°\mathrm{C}$ y debe salir a no más de $30\,°\mathrm{C}$. Determinar: (a) $\dot{Q}$; (b) caudal mínimo de agua de enfriamiento; (c) temperatura efectiva de aproximación.

> [!solucion]
> **Paso 1 — Calor cedido por el vapor.** El vapor condensa totalmente; no hay cambio de temperatura en la corriente caliente:
> $$\dot{Q} = \dot{m}_h\,h_{fg} = 50\times2406.7 = 120\,335\,\mathrm{kW} \approx 120.3\,\mathrm{MW}.$$
>
> **Paso 2 — Caudal mínimo de agua de enfriamiento.** La limitación es $T_{c,2}\leq30\,°\mathrm{C}$, con $c_{p,c}=4.18\,\mathrm{kJ/(kg\cdot K)}$:
> $$\dot{m}_{c,\rm min} = \frac{\dot{Q}}{c_{p,c}(T_{c,2}-T_{c,1})} = \frac{120\,335}{4.18\times(30-20)} = \frac{120\,335}{41.8} = 2878\,\mathrm{kg/s}.$$
>
> **Paso 3 — Verificar consistencia termodinámica.** En un condensador (corriente caliente isotérmica), la corriente "min" es siempre la de agua de enfriamiento: $C_c = 2878\times4.18 = 12{,}030\,\mathrm{kW/K}$ y $C_h\to\infty$ (cambio de fase). El calor máximo sería:
> $$\dot{Q}_{\rm max} = C_c(T_{\rm sat}-T_{c,1}) = 12\,030\times20 = 240\,600\,\mathrm{kW} > \dot{Q}. \checkmark$$
> Con $\varepsilon_{\rm min} = \dot{Q}/\dot{Q}_{\rm max} = 120\,335/240\,600=0.50$. Coherente.
>
> **Paso 4 — Temperatura de aproximación (approach).** La diferencia mínima entre corrientes ocurre en el extremo de salida del agua ($T_{c,2}=30\,°\mathrm{C}$) vs. el vapor saturado ($T_{\rm sat}=40\,°\mathrm{C}$):
> $$\Delta T_{\rm approach} = T_{\rm sat} - T_{c,2} = 40-30 = 10\,\mathrm{K}.$$
> Esta diferencia mínima es la que controla el tamaño del intercambiador: cuanto menor sea, mayor debe ser el área $A$.
>
> **Paso 5 — Verificación de generación de entropía.** El vapor condensado sale como líquido saturado a $40\,°\mathrm{C}$: $s_{h,2}=s_f(40\,°\mathrm{C})=0.5725$, $s_{h,1}=s_g(40\,°\mathrm{C})=8.2570\,\mathrm{kJ/(kg\cdot K)}$. $\Delta s_h = 0.5725-8.2570=-7.685\,\mathrm{kJ/(kg\cdot K)}$. $\Delta s_c=4.18\ln(303.15/293.15)=4.18\times0.0336=0.140\,\mathrm{kJ/(kg\cdot K)}$. $\dot{S}_{\rm gen}=50\times(-7.685)+2878\times0.140=-384.2+403.0=+18.8\,\mathrm{kW/K}>0$ ✓.
>
> $\boxed{\dot{Q}=120.3\,\mathrm{MW},\quad \dot{m}_c=2878\,\mathrm{kg/s},\quad \Delta T_{\rm approach}=10\,\mathrm{K}.}$ $\blacksquare$

> [!warning]
> El factor de obstrucción (fouling) degrada $U$ con el tiempo: $1/U_{\rm real} = 1/U_{\rm limpio} + R_f$. Valores típicos de $R_f$: agua de río $\approx 2\times10^{-4}$ m²·K/W, agua del mar $\approx 1\times10^{-4}$ m²·K/W. Un intercambiador diseñado sin margen para fouling tendrá $T_{c,2}$ insuficiente a los 6–12 meses de operación.

> [!referencia]
> Borgnakke & Sonntag, §6.6; Çengel & Boles, §13-1 al §13-4; Moran & Shapiro, §12.1–12.4.
