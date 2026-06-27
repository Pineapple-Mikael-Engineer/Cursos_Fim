---
title: Combustión
order: 2
tags:
  - termodinamica
  - mezclas
  - combustion
  - estequiometria
  - index
draft: false
aliases:
  - Combustión
  - Combustion
  - Reacciones de Combustión
---

# Combustión

> [!definicion]
> La **combustión** es una reacción química exotérmica rápida entre un **combustible** (hidrocarburo $\mathrm{C}_{x}\mathrm{H}_{y}$, alcohol, carbón, etc.) y un **oxidante** (normalmente aire). En termodinámica interesa no la cinética de la reacción, sino su **resultado estacionario**: ¿qué composición tienen los productos? ¿cuánto calor se libera? ¿a qué temperatura llegan los productos?
>
> *¿En qué se diferencia de una mezcla ordinaria?* En una mezcla de gases ideales (como vimos en [[Mezclas de Gases]]) la composición no cambia. En la combustión hay **ruptura y formación de enlaces**: los reactivos (combustible + oxidante) se transforman en productos (CO₂, H₂O, N₂). La energía que proviene de esta diferencia de enlaces se cuantifica mediante las **entalpías de formación** $\bar{h}_f^\circ$.
>
> La aplicación central: las cámaras de combustión de turbinas de gas (ciclo Brayton) y motores de explosión (ciclos Otto y Diesel) son volúmenes de control en que se quema combustible. Conocer la temperatura y composición de los gases calientes que salen determina la eficiencia máxima del ciclo.

![[combustion_esquema_reactivos_productos.svg|480]]
*Esquema de una cámara de combustión. Entran combustible y aire (reactivos); salen CO₂, H₂O, N₂ y posible O₂ en exceso (productos). La temperatura de los productos depende del exceso de aire y del calor cedido a las paredes.*

---

## Composición del aire y estequiometría básica

> [!proposicion]
> El **aire seco** se modela como $21\%\,\mathrm{O_2}$ + $79\%\,\mathrm{N_2}$ en volumen. Por cada mol de $\mathrm{O_2}$ hay $79/21 = 3.76$ moles de $\mathrm{N_2}$. En la reacción se escribe el "oxidante" como la unidad $(\mathrm{O_2} + 3.76\,\mathrm{N_2})$ por mol de $\mathrm{O_2}$.
>
> **Combustión completa estequiométrica** de $\mathrm{C_xH_y}$ con $a_{\rm est}$ moles de $\mathrm{O_2}$:
> $$\mathrm{C_xH_y} + a_{\rm est}(\mathrm{O_2}+3.76\,\mathrm{N_2}) \to x\,\mathrm{CO_2} + \frac{y}{2}\mathrm{H_2O} + 3.76\,a_{\rm est}\,\mathrm{N_2}.$$
>
> Balance de oxígeno ($\mathrm{O}_{\rm entra}=\mathrm{O}_{\rm sale}$):
> $$2a_{\rm est} = 2x + \frac{y}{2} \implies \boxed{a_{\rm est} = x + \frac{y}{4}}.$$

> [!demostracion]
> **Hipótesis:** combustión completa (todo C → CO₂, todo H → H₂O), el N₂ es inerte.
>
> **Paso 1 — Identificar los átomos que se conservan.** En la reacción: C, H, O, N se conservan como átomos (no se crean ni destruyen en química ordinaria). El N₂ del aire entra y sale como N₂ (inerte).
>
> **Paso 2 — Balance de carbono.** La izquierda tiene $x$ átomos de C (en 1 mol de $\mathrm{C_xH_y}$). La derecha tiene $x$ moles de $\mathrm{CO_2}$, cada uno con 1 átomo de C. Balance: $x = x$. ✓ (La cantidad $x$ de $\mathrm{CO_2}$ queda determinada directamente.)
>
> **Paso 3 — Balance de hidrógeno.** La izquierda tiene $y$ átomos de H. La derecha tiene $y/2$ moles de $\mathrm{H_2O}$, cada uno con 2 átomos de H. Balance: $y = y$. ✓ (La cantidad $y/2$ de $\mathrm{H_2O}$ queda determinada directamente.)
>
> **Paso 4 — Balance de oxígeno.** Izquierda: $2a_{\rm est}$ átomos de O (cada mol de $\mathrm{O_2}$ tiene 2). Derecha: $2x$ (del $\mathrm{CO_2}$) $+ y/2$ (del $\mathrm{H_2O}$). Igualando:
> $$2a_{\rm est} = 2x + \frac{y}{2} \implies a_{\rm est} = x + \frac{y}{4}.$$
>
> **Paso 5 — Verificación de casos límite.** Para $\mathrm{CH_4}$ ($x=1$, $y=4$): $a_{\rm est}=1+1=2$. Para $\mathrm{C_3H_8}$ ($x=3$, $y=8$): $a_{\rm est}=3+2=5$. Para $\mathrm{C_8H_{18}}$ ($x=8$, $y=18$): $a_{\rm est}=8+4.5=12.5$. Son los valores clásicos de la literatura. ✓ $\blacksquare$

---

## Exceso de aire y relación de equivalencia

> [!definicion]
> La **relación aire-combustible másica** (AF) mide cuánto aire se suministra por kg de combustible:
> $$\mathrm{AF} = \frac{m_{\rm aire}}{m_{\rm comb}} = \frac{a_{\rm est}/\Phi\times(M_{\mathrm{O_2}}+3.76\,M_{\mathrm{N_2}})}{M_{\rm comb}} = \frac{a_{\rm est}/\Phi\times137.28}{M_{\rm comb}}.$$
>
> La **relación de equivalencia** $\Phi = \mathrm{AF}_{\rm est}/\mathrm{AF}$ caracteriza la riqueza de la mezcla:
>
> | $\Phi$ | Mezcla | $\mathrm{O_2}$ en productos | CO en productos |
> |:---:|:---:|:---:|:---:|
> | $\Phi < 1$ | **pobre** (lean) | Sí (exceso) | No |
> | $\Phi = 1$ | estequiométrica | Traza | No |
> | $\Phi > 1$ | **rica** (rich) | No | Sí |
>
> El **porcentaje de exceso de aire** es $e = (1/\Phi - 1)\times100\%$ (positivo para mezcla pobre).

> [!proposicion]
> Con exceso de aire (mezcla pobre, $\Phi < 1$), la reacción de combustión completa es:
> $$\mathrm{C_xH_y} + \frac{a_{\rm est}}{\Phi}(\mathrm{O_2}+3.76\,\mathrm{N_2}) \to x\,\mathrm{CO_2} + \frac{y}{2}\mathrm{H_2O} + a_{\rm est}\!\left(\frac{1}{\Phi}-1\right)\mathrm{O_2} + 3.76\,\frac{a_{\rm est}}{\Phi}\,\mathrm{N_2}.$$

> [!demostracion]
> **Hipótesis:** mezcla pobre ($\Phi < 1$), combustión completa (todo C → CO₂, todo H → H₂O), N₂ inerte.
>
> **Paso 1 — Aire suministrado.** Se inyectan $a_{\rm est}/\Phi$ moles de $\mathrm{O_2}$ (más que los $a_{\rm est}$ necesarios cuando $\Phi < 1$).
>
> **Paso 2 — Consumo de O₂.** La combustión completa consume exactamente $a_{\rm est}$ moles de $\mathrm{O_2}$ para oxidar todo el C y todo el H (como en la estequiometría base).
>
> **Paso 3 — O₂ sobrante.** El oxígeno sin reaccionar:
> $$n_{\mathrm{O_2,exceso}} = \frac{a_{\rm est}}{\Phi} - a_{\rm est} = a_{\rm est}\!\left(\frac{1}{\Phi}-1\right).$$
>
> **Paso 4 — N₂ en productos.** El N₂ del aire (inerte) pasa directamente a productos:
> $$n_{\mathrm{N_2}} = 3.76\,\frac{a_{\rm est}}{\Phi}.$$
>
> **Paso 5 — Verificación de límites.** Si $\Phi=1$: $n_{\mathrm{O_2,exceso}}=0$ → no hay exceso ✓. Si $\Phi=2/3$ (50% de exceso): $n_{\mathrm{O_2,exceso}}=a_{\rm est}/2$ → la mitad del $\mathrm{O_2}$ queda sin reaccionar ✓. $\blacksquare$

---

## Entalpías de formación y calor de reacción

> [!definicion]
> La **entalpía de formación estándar** $\bar{h}_f^\circ$ es el cambio de entalpía para formar **1 kmol** de una sustancia desde sus **elementos en estado de referencia** a $T^\circ=25\,°\mathrm{C}$, $P^\circ=1\,\mathrm{atm}$. Por convención, los elementos en estado estable tienen $\bar{h}_f^\circ=0$ (O₂(g), N₂(g), H₂(g), C(s) grafito).
>
> La **entalpía de reacción** a $T^\circ$:
> $$\bar{h}_R^\circ = \sum_{\rm prod} n_i\,\bar{h}_{f,i}^\circ - \sum_{\rm react} n_j\,\bar{h}_{f,j}^\circ.$$
>
> Para combustiones: $\bar{h}_R^\circ < 0$ (exotérmico). El calor liberado es $-\bar{h}_R^\circ > 0$.

Valores fundamentales:

| Sustancia | Estado | $\bar{h}_f^\circ$ (kJ/kmol) |
|:---|:---:|---:|
| $\mathrm{CO_2}(g)$ | gas | $-393\,520$ |
| $\mathrm{H_2O}(g)$ | vapor | $-241\,826$ |
| $\mathrm{H_2O}(l)$ | líquido | $-285\,826$ |
| $\mathrm{CO}(g)$ | gas | $-110\,530$ |
| $\mathrm{CH_4}(g)$ | gas | $-74\,850$ |
| $\mathrm{C_3H_8}(g)$ | gas | $-103\,850$ |
| $\mathrm{C_8H_{18}}(l)$ | líquido | $-249\,950$ |

> [!proposicion]
> **Poder calorífico superior (PCS) e inferior (PCI):**
> $$\mathrm{PCS} = -\bar{h}_R^\circ\big|_{\mathrm{H_2O(l)}}, \qquad \mathrm{PCI} = -\bar{h}_R^\circ\big|_{\mathrm{H_2O(g)}}.$$
>
> La diferencia es el calor de condensación del agua formada:
> $$\mathrm{PCS} = \mathrm{PCI} + \frac{n_{\mathrm{H_2O}}\times M_{\mathrm{H_2O}}}{M_{\rm comb}}\times h_{fg}(25\,°\mathrm{C}),$$
> con $h_{fg}(25\,°\mathrm{C}) = 2441.7\,\mathrm{kJ/kg}$.

> [!warning]
> Los motores y turbinas descargan gases de escape a $T \gg 100\,°\mathrm{C}$: el agua sale como **vapor** → usar **PCI**. Solo calderas de condensación recuperan el calor latente y deben usar **PCS**.

---

## Ejemplo: combustión completa de propano

> [!ejemplo]
> Propano ($\mathrm{C_3H_8}$) quema completamente con 150% de aire teórico. Reactivos a $25\,°\mathrm{C}$. Determinar: (a) reacción balanceada; (b) relación AF; (c) composición de productos (análisis de Orsat, base seca); (d) PCI y PCS.

> [!solucion]
> **Datos.** $\mathrm{C_3H_8}$: $x=3$, $y=8$, $M=44.09\,\mathrm{kg/kmol}$. $\bar{h}_f^\circ = -103850\,\mathrm{kJ/kmol}$.
>
> **(a) Reacción.** $a_{\rm est}=3+8/4=3+2=5$. Con 150% de aire: $a=1.5\times5=7.5$ mol de $\mathrm{O_2}$:
> $$\mathrm{C_3H_8}+7.5\,\mathrm{O_2}+7.5\times3.76\,\mathrm{N_2}\to3\,\mathrm{CO_2}+4\,\mathrm{H_2O}+(7.5-5)\,\mathrm{O_2}+28.2\,\mathrm{N_2}.$$
> $$\boxed{\mathrm{C_3H_8}+7.5\,\mathrm{O_2}+28.2\,\mathrm{N_2}\to3\,\mathrm{CO_2}+4\,\mathrm{H_2O}+2.5\,\mathrm{O_2}+28.2\,\mathrm{N_2}.}$$
> Verificación: C: $3=3$ ✓; H: $8=8$ ✓; O: $15=6+4+5=15$ ✓; N: $56.4=56.4$ ✓.
>
> **(b) Relación AF.**
> $m_{\rm aire} = 7.5\times(32+3.76\times28) = 7.5\times137.28 = 1029.6\,\mathrm{kg/kmol\,C_3H_8}$.
> $$\mathrm{AF} = 1029.6/44.09 = 23.35\,\mathrm{kg\,aire/kg\,C_3H_8}.$$
> (Para verificar: $\mathrm{AF}_{\rm est}=5\times137.28/44.09=15.57$; $1.5\times15.57=23.36$ ✓.)
>
> **(c) Análisis de Orsat** (base seca, sin $\mathrm{H_2O}$). Total seco: $3+2.5+28.2=33.7$ mol.
>
> | Componente | mol | % vol seco |
> |:---:|:---:|:---:|
> | $\mathrm{CO_2}$ | 3.0 | 8.90% |
> | $\mathrm{O_2}$ | 2.5 | 7.42% |
> | $\mathrm{N_2}$ | 28.2 | 83.68% |
>
> **(d) PCI y PCS.**
> $$\bar{h}_R^\circ\big|_{\mathrm{H_2O(g)}} = [3(-393520)+4(-241826)] - [(-103850)+0] = -2043014\,\mathrm{kJ/kmol}.$$
> $$\mathrm{PCI} = 2043014/44.09 = 46340\,\mathrm{kJ/kg} \approx 46.3\,\mathrm{MJ/kg}.$$
>
> Con $\mathrm{H_2O(l)}$: $\bar{h}_R^\circ = [3(-393520)+4(-285826)]-[-103850] = -2220014\,\mathrm{kJ/kmol}$.
> $$\mathrm{PCS} = 2220014/44.09 = 50350\,\mathrm{kJ/kg} \approx 50.4\,\mathrm{MJ/kg}.$$
>
> Verificación: $\mathrm{PCS}-\mathrm{PCI}=4010\,\mathrm{kJ/kg}$. Por condensación de $4\,\mathrm{mol}$ de agua: $4\times18.015\times2441.7/44.09=4010\,\mathrm{kJ/kg}$ ✓.
>
> $\boxed{\mathrm{PCI}=46.3\,\mathrm{MJ/kg},\quad\mathrm{PCS}=50.4\,\mathrm{MJ/kg},\quad\mathrm{AF}=23.35\,\mathrm{kg/kg}.}$ $\blacksquare$

---

## Mapa de notas

> [!info]
> - [[Combustion Incompleta]] — mezcla rica ($\Phi>1$); balance con CO en productos; análisis de Orsat inverso (AF desde composición medida); pérdida calorífica por CO.
> - [[Temperatura Adiabatica de Llama]] — temperatura máxima sin pérdidas; balance entálpico completo $H_{\rm react}=H_{\rm prod}$; método iterativo con tablas JANAF; efecto del exceso de aire.

> [!referencia]
> Borgnakke & Sonntag, cap. 13; Çengel & Boles, cap. 15; Moran & Shapiro, cap. 13.
