---
title: "Problema 07 — Mezcla expandiéndose por una tobera"
tags:
  - termodinamica
  - problemas
  - mezclas
  - volumen_de_control
draft: false
aliases:
  - tobera mezcla isentrópica
  - expansión mezcla CO2 O2
---

# Problema 07 — Mezcla expandiéndose por una tobera

> [!definicion] Enunciado
> Una mezcla de $\text{CO}_2$ y $\text{O}_2$ con fracciones molares $y_{\text{CO}_2} = 0{,}8$ e $y_{\text{O}_2} = 0{,}2$ se expande **isentrópica** y estacionariamente por una [[Toberas | tobera]] desde $700\ \text{K}$, $5\ \text{atm}$, $C_1 = 3\ \text{m/s}$ hasta $p_2 = 1\ \text{atm}$. Se desprecia la energía potencial.
>
> Se pide:
> 1. La temperatura de salida.
> 2. Las variaciones de entropía del $\text{CO}_2$ y del $\text{O}_2$.
> 3. La velocidad de salida.

## Estrategia

> [!teoria]
> [[Volumenes de Control | Volumen de control]] en [[Flujo Estacionario]], adiabático y sin trabajo. La mezcla es de [[Gas Ideal | gases ideales]] de composición constante (ver [[Mezclas de Gases]]). La condición isentrópica $\Delta \bar s_{mezcla} = 0$ fija $T_2$; el [[Balance de Energia VC]] da la velocidad. Como la composición no cambia, $p_{i2}/p_{i1} = p_2/p_1$.

## Inciso 1 — Temperatura de salida

> [!solucion]
> La entropía específica de la mezcla no varía: $\bar s_2 - \bar s_1 = y_{\text{O}_2}\Delta\bar s_{\text{O}_2} + y_{\text{CO}_2}\Delta\bar s_{\text{CO}_2} = 0$. Con $\Delta\bar s_i = \bar s_i^{\circ}(T_2) - \bar s_i^{\circ}(T_1) - R_u\ln(p_2/p_1)$ y $\sum y_i = 1$:
> $$
> y_{\text{O}_2}\,\bar s_{\text{O}_2}^{\circ}(T_2) + y_{\text{CO}_2}\,\bar s_{\text{CO}_2}^{\circ}(T_2) = y_{\text{O}_2}\,\bar s_{\text{O}_2}^{\circ}(T_1) + y_{\text{CO}_2}\,\bar s_{\text{CO}_2}^{\circ}(T_1) + R_u\ln\frac{p_2}{p_1}
> $$
> Con valores de tabla A-23 a $T_1 = 700\ \text{K}$ ($\bar s_{\text{O}_2}^{\circ} = 231{,}358$, $\bar s_{\text{CO}_2}^{\circ} = 250{,}663$) y $R_u\ln(1/5) = -13{,}38$:
> $$
> 0{,}2\,\bar s_{\text{O}_2}^{\circ}(T_2) + 0{,}8\,\bar s_{\text{CO}_2}^{\circ}(T_2) = 233{,}42\ \text{kJ/kmol·K}
> $$

> [!solucion]
> Se resuelve por **iteración** en la tabla (suponer $T_2$, leer $\bar s_i^{\circ}$, comprobar):
>
> | $T_2$ supuesta | $0{,}2\,\bar s_{\text{O}_2}^{\circ} + 0{,}8\,\bar s_{\text{CO}_2}^{\circ}$ |
> |:---:|:---:|
> | $510\ \text{K}$ | $0{,}2(221{,}206) + 0{,}8(235{,}700) = 232{,}80$ |
> | $520\ \text{K}$ | $0{,}2(221{,}812) + 0{,}8(236{,}575) = 233{,}62$ |
>
> Interpolando para $233{,}42$:
> $$
> T_2 = 510 + 10\,\frac{233{,}42 - 232{,}80}{233{,}62 - 232{,}80} = 517{,}6\ \text{K}
> $$

## Inciso 2 — Cambios de entropía de los componentes

> [!solucion]
> Cada componente cambia su entropía aunque la de la mezcla sea constante. Con $\bar s_i^{\circ}(T_2)$ a $517{,}6\ \text{K}$ y $R_u\ln(p_2/p_1)$, donde $p_{i2}/p_{i1}=p_2/p_1=1/5$:
> $$
> \Delta\bar s_{\text{O}_2} = 221{,}667 - 231{,}358 - 8{,}314\,\ln(0{,}2) = +3{,}69\ \text{kJ/kmol·K}
> $$
> $$
> \Delta\bar s_{\text{CO}_2} = 236{,}365 - 250{,}663 - 8{,}314\,\ln(0{,}2) = -0{,}92\ \text{kJ/kmol·K}
> $$

## Inciso 3 — Velocidad de salida

> [!solucion]
> [[Balance de Energia VC]] adiabático, sin trabajo, sin $\Delta\text{EP}$:
> $$
> 0 = (h_1 - h_2) + \frac{C_1^2 - C_2^2}{2} \;\Rightarrow\; C_2 = \sqrt{C_1^2 + 2(h_1 - h_2)}
> $$
> El salto entálpico por unidad de masa usa $M = 0{,}8(44) + 0{,}2(32) = 41{,}6\ \text{kg/kmol}$ y las $\bar h_i(T)$ de tabla:
> $$
> h_1 - h_2 = \frac{1}{M}\big[y_{\text{O}_2}(\bar h_1 - \bar h_2)_{\text{O}_2} + y_{\text{CO}_2}(\bar h_1 - \bar h_2)_{\text{CO}_2}\big] = \frac{0{,}2(21184 - 15320) + 0{,}8(27125 - 18468)}{41{,}6} = 194{,}7\ \text{kJ/kg}
> $$
> $$
> C_2 = \sqrt{3^2 + 2\,(194{,}7 \times 10^3)} = 624\ \text{m/s}
> $$

> [!info] Verificación física
> $\Delta\bar s_{\text{O}_2} > 0$ y $\Delta\bar s_{\text{CO}_2} < 0$ reflejan una transferencia interna de entropía del $\text{CO}_2$ al $\text{O}_2$; ponderadas por $y_i$ se cancelan y la mezcla es isentrópica, como en toda [[Toberas | tobera]] ideal. La energía térmica se convierte en cinética ($C_2 \gg C_1$), el efecto buscado del dispositivo.

## Notas usadas

> [!referencia]
> [[Mezclas de Gases]] · [[Toberas]] · [[Flujo Estacionario]] · [[Balance de Energia VC]] · [[Balance de Entropia VC]] · [[Entropia]] · [[Entalpia]] · [[Problema 01]] · Moran & Shapiro, Ej. 12.4.

> [!info]
> **Convención de notación**:
> - $\bar s_i^{\circ}(T)$: entropía molar de referencia de tabla (a $1\ \text{atm}$); $C$: velocidad [m/s].
> - $M = \sum y_i M_i$: masa molecular aparente; barra: magnitud molar.
