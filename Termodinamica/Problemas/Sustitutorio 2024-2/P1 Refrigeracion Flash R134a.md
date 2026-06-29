---
title: "P1 — Refrigeración R-134a de dos etapas con cámara flash"
order: 2
tags: [termodinamica, problemas, refrigeracion]
draft: false
aliases: [flash R134a dos etapas, refrigeración compresión doble]
---

# P1 — Refrigeración R-134a de dos etapas con cámara flash

> [!definicion] Enunciado
> Un ciclo de refrigeración con **R-134a** de **dos etapas de compresión** con **cámara flash** que opera a $0{,}45$ MPa. El evaporador trabaja a $-10\,^\circ$C y la presión del condensador es $1{,}6$ MPa; la eficiencia adiabática de los compresores es $0{,}86$. El flujo másico por el evaporador es $0{,}11$ kg/s. En los estados 1 y 3 el refrigerante sale como **vapor saturado**, y como **líquido saturado** en 5 y 7. Se pide: **(1,2)** llenar el cuadro de estados; **(3)** flujo por el compresor de alta [kg/s]; **(4)** capacidad de refrigeración [kW]; **(5)** COP.

## Estrategia

> [!teoria]
> Ciclo de [[Conversión de Energía/Refrigeración/Compresión de Vapor | compresión de vapor]] con economizador flash: el líquido del condensador se estrangula a la presión intermedia y la cámara flash separa vapor (3, va al compresor de alta) y líquido (7, va al evaporador). El [[Sistemas/Dispositivos Flujo/Compresores | compresor]] de baja sube $1\to2$; en el punto 9 se mezcla con el vapor flash (3) antes del compresor de alta $9\to4$.

![[VCR_diagrama_Ph.svg|360]]

> [!info] Cuadro de estados (R-134a, valores de tabla)
> | Estado | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
> |:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
> | $T$ [°C] | −10 | ≈14{,}6 | 11{,}3 | ≈66{,}7 | 57{,}9 | 11{,}3 | 11{,}3 | −10 | ≈15 |
> | $P$ [MPa] | 0{,}20 | 0{,}45 | 0{,}45 | 1{,}6 | 1{,}6 | 0{,}45 | 0{,}45 | 0{,}20 | 0{,}45 |
> | $h$ [kJ/kg] | 244{,}5 | 263{,}1 | 257{,}5 | 289{,}9 | 135{,}9 | 135{,}9 | 68{,}8 | 68{,}8 | 261{,}1 |
> | $s$ [kJ/kg·K] | 0{,}938 | — | 0{,}927 | — | — | — | — | — | 0{,}940 |

> [!solucion] (3) Flujo por el compresor de alta
> Calidad tras el estrangulamiento $5\to6$ a $0{,}45$ MPa: $x_6=\dfrac{h_6-h_f}{h_{fg}}=\dfrac{135{,}9-68{,}8}{257{,}5-68{,}8}=0{,}356$. El líquido ($1-x_6$) alimenta el evaporador:
> $$\dot m_{total}=\frac{\dot m_{evap}}{1-x_6}=\frac{0{,}11}{0{,}644}=\boxed{0{,}171\ \text{kg/s}}.$$

> [!solucion] (4) Capacidad de refrigeración
> $$\dot Q_L=\dot m_{evap}(h_1-h_8)=0{,}11(244{,}5-68{,}8)=\boxed{19{,}3\ \text{kW}}.$$

> [!solucion] (5) COP
> Compresor de baja ($\dot m_{evap}$): $\dot W_L=0{,}11(263{,}1-244{,}5)=2{,}05$ kW. Compresor de alta ($\dot m_{total}$): $\dot W_H=0{,}171(289{,}9-261{,}1)=4{,}92$ kW.
> $$\mathrm{COP}=\frac{\dot Q_L}{\dot W_L+\dot W_H}=\frac{19{,}3}{6{,}97}=\boxed{2{,}77}.$$

> [!info] Nota
> Entalpías del R-134a tomadas de tabla (interpoladas para los estados sobrecalentados $2,4,9$); cotejar con CATT3. El estado 9 sale del balance de mezcla $\dot m_{total}h_9=\dot m_{evap}h_2+\dot m_{flash}h_3$.

> [!referencia]
> [[Conversión de Energía/Refrigeración/Compresión de Vapor | Compresión de Vapor]] · [[Sistemas/Dispositivos Flujo/Flash | Flash]] · [[Sistemas/Dispositivos Flujo/Compresores | Compresores]]
