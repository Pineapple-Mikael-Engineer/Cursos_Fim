---
title: Combustión
tags:
  - termodinamica
  - teoria
  - mezclas
  - combustion
  - estequiometria
draft: false
aliases:
  - Combustión
  - Combustion
  - Reacciones de Combustión
---

# Combustión $\mathrm{C_xH_y} + a_{\rm est}\left(\mathrm{O_2}+3.76\,\mathrm{N_2}\right)\to x\,\mathrm{CO_2}+\frac{y}{2}\mathrm{H_2O}+3.76\,a_{\rm est}\,\mathrm{N_2}$

> [!definicion]
> La **combustión** es una reacción química exotérmica entre un **combustible** (hidrocarburo $\mathrm{C_xH_y}$, alcohol, carbono, etc.) y un **oxidante** (normalmente aire). El análisis termodinámico de la combustión determina: (1) la **estequiometría** (cantidad de aire teórico y composición de productos), (2) el **calor liberado** (poder calorífico), y (3) la **temperatura de llama** (temperatura adiabática de llama). A diferencia de las mezclas no reactivas, la composición cambia y las propiedades se calculan usando **entalpías de formación** $\bar{h}_f^\circ$.

> [!info]
> **Contexto.** La combustión es la base energética de las turbinas de gas (ciclo Brayton), motores de combustión interna (Otto, Diesel) y calderas de vapor (ciclo Rankine). Su análisis permite calcular las condiciones de entrada/salida de la cámara de combustión.

---

## Estequiometría de la combustión

### Combustión estequiométrica (teórica)

> [!proposicion] Combustión estequiométrica de $\mathrm{C_xH_y}$
> Con aire seco ($\mathrm{O_2}+3.76\,\mathrm{N_2}$ por mol de $\mathrm{O_2}$, donde $3.76=79/21$):
> $$\mathrm{C_xH_y} + a_{\rm est}\left(\mathrm{O_2}+3.76\,\mathrm{N_2}\right) \to x\,\mathrm{CO_2}+\frac{y}{2}\mathrm{H_2O}+3.76\,a_{\rm est}\,\mathrm{N_2}$$
> Balance de $\mathrm{O_2}$: $a_{\rm est} = x + y/4$. La **relación aire-combustible másica estequiométrica**:
> $$\mathrm{AF}_{\rm est} = \frac{a_{\rm est}(32+3.76\times28)}{M_{\rm comb}} = \frac{137.28\,a_{\rm est}}{M_{\rm comb}}.$$

> [!teoria] Exceso de aire y relación de equivalencia
> $$\%\,\text{exceso} = \frac{\mathrm{AF}-\mathrm{AF}_{\rm est}}{\mathrm{AF}_{\rm est}}\times100, \qquad \Phi = \frac{\mathrm{AF}_{\rm est}}{\mathrm{AF}}.$$
> - $\Phi<1$: mezcla **pobre** (lean) — exceso de $\mathrm{O_2}$ en productos; combustión completa.
> - $\Phi=1$: estequiométrica.
> - $\Phi>1$: mezcla **rica** (rich) — $\mathrm{CO}$, $\mathrm{H_2}$ en productos; ver [[Combustion Incompleta]].

> [!demostracion] Combustión con exceso de aire
> Con $\Phi<1$ (porcentaje de exceso $e=1/\Phi-1$), la reacción con exceso de $\mathrm{O_2}$ y $\mathrm{N_2}$:
> $$\mathrm{C_xH_y}+\frac{a_{\rm est}}{\Phi}\left(\mathrm{O_2}+3.76\,\mathrm{N_2}\right)\to x\,\mathrm{CO_2}+\frac{y}{2}\mathrm{H_2O}+\frac{a_{\rm est}}{\Phi}(1-\Phi)\,\mathrm{O_2}+3.76\frac{a_{\rm est}}{\Phi}\,\mathrm{N_2}.$$
> Balance de $\mathrm{O_2}$: entra $a_{\rm est}/\Phi$ moles. Se consumen $a_{\rm est}$ (estequiométrico). Sobra $a_{\rm est}/\Phi - a_{\rm est} = a_{\rm est}(1/\Phi-1)$ moles de $\mathrm{O_2}$ sin reaccionar. $\blacksquare$

---

## Entalpía de formación y energía de reacción

> [!teoria] Entalpía de formación estándar $\bar{h}_f^\circ$
> La **entalpía de formación estándar** $\bar{h}_f^\circ$ es la entalpía de reacción para formar **1 mol** de una sustancia desde sus **elementos en estado de referencia** a $T^\circ=25\,°\mathrm{C}$, $P^\circ=1\,\mathrm{atm}$. Por convención, los elementos puros en estado estable tienen $\bar{h}_f^\circ=0$. La entalpía de reacción a $T^\circ$ es:
> $$\bar{h}_R^\circ = \sum_{\rm prod} n_i\,\bar{h}_{f,i}^\circ - \sum_{\rm react} n_j\,\bar{h}_{f,j}^\circ < 0\quad(\text{exotérmica}).$$

Valores relevantes:

| Sustancia | Estado | $\bar{h}_f^\circ$ (kJ/kmol) |
|:---|:---:|:---:|
| $\mathrm{CO_2}(g)$ | gas | $-393\,520$ |
| $\mathrm{H_2O}(g)$ | vapor | $-241\,826$ |
| $\mathrm{H_2O}(l)$ | líquido | $-285\,826$ |
| $\mathrm{CO}(g)$ | gas | $-110\,530$ |
| $\mathrm{CH_4}(g)$ | gas | $-74\,850$ |
| $\mathrm{C_3H_8}(g)$ | gas | $-103\,850$ |
| $\mathrm{C_8H_{18}}(l)$ | líquido | $-249\,950$ |
| $\mathrm{N_2}(g)$, $\mathrm{O_2}(g)$, $\mathrm{H_2}(g)$, $\mathrm{C}(s)$ | — | $0$ |

 > [!proposicion] Poder calorífico: PCS y PCI
> $$\mathrm{PCS} = -\bar{h}_R^\circ\big|_{H_2O(l)}, \qquad \mathrm{PCI} = -\bar{h}_R^\circ\big|_{H_2O(g)}.$$
> $$\mathrm{PCS} = \mathrm{PCI} + n_{H_2O}\,h_{fg}(25\,°\mathrm{C})\cdot\frac{M_{H_2O}}{M_{\rm comb}}, \qquad h_{fg}(25\,°\mathrm{C})=2441.7\,\mathrm{kJ/kg}.$$

> [!warning]
> Los motores de combustión interna y turbinas descargan agua como vapor ($T_{\rm escape}\gg100\,°\mathrm{C}$): usar el **PCI**. Solo las calderas de condensación recuperan el calor de condensación y se refieren al **PCS**.

---

## Ejemplo: combustión completa de propano

> [!ejemplo]
> Propano ($\mathrm{C_3H_8}$) quema completamente con $150\%$ de aire teórico a $P=101.325\,\mathrm{kPa}$. Reactivos a $25\,°\mathrm{C}$. Determinar:
> (a) Reacción balanceada.
> (b) Relación aire-combustible $\mathrm{AF}$.
> (c) Composición de los productos (análisis de Orsat, base seca).
> (d) PCI y PCS del propano.

> [!solucion]
> **Datos.** $\mathrm{C_3H_8}$: $x=3$, $y=8$, $M=44.09\,\mathrm{kg/kmol}$, $\bar{h}_f^\circ=-103850\,\mathrm{kJ/kmol}$.
>
> **(a) Estequiometría.** $a_{\rm est}=x+y/4=3+2=5$. Con 150% de aire teórico ($\Phi=1/1.5$, exceso $e=50\%$):
>
> $$\mathrm{C_3H_8}+\frac{5}{1/1.5}\,(\mathrm{O_2}+3.76\,\mathrm{N_2})\to$$
> $$7.5\,(\mathrm{O_2}+3.76\,\mathrm{N_2})\to 3\,\mathrm{CO_2}+4\,\mathrm{H_2O}+(7.5-5)\,\mathrm{O_2}+3.76\times7.5\,\mathrm{N_2}$$
> $$\mathrm{C_3H_8}+7.5\,\mathrm{O_2}+28.2\,\mathrm{N_2}\to 3\,\mathrm{CO_2}+4\,\mathrm{H_2O}+2.5\,\mathrm{O_2}+28.2\,\mathrm{N_2}.$$
>
> Verificación: C: $3=3$ ✓; H: $8=8$ ✓; O: $15=6+4+5=15$ ✓; N: $56.4=56.4$ ✓.
>
> **(b) Relación AF.**
> $$m_{\rm aire}=7.5\times(32+3.76\times28)=7.5\times137.28=1029.6\,\mathrm{kg/kmol\,C_3H_8}.$$
> $$\mathrm{AF}=\frac{1029.6}{44.09}=23.35\,\mathrm{kg\,aire/kg\,C_3H_8}.$$
> AF estequiométrico: $\mathrm{AF}_{\rm est}=5\times137.28/44.09=15.57$. $150\%$ de $15.57=23.36$. ✓
>
> **(c) Análisis de Orsat (base seca = sin $\mathrm{H_2O}$).**
> Total seco: $3\,\mathrm{CO_2}+2.5\,\mathrm{O_2}+28.2\,\mathrm{N_2}=33.7\,\mathrm{mol}$.
>
> | Componente | mol | $\%$ vol (seco) |
> |:---:|:---:|:---:|
> | $\mathrm{CO_2}$ | 3.0 | 8.90% |
> | $\mathrm{O_2}$ | 2.5 | 7.42% |
> | $\mathrm{N_2}$ | 28.2 | 83.68% |
>
> **(d) PCI y PCS.**
> $$\bar{h}_R^\circ\big|_{H_2O(g)}=\left[3(-393520)+4(-241826)\right]-\left[(-103850)+0+0\right]$$
> $$=[{-1180560-967304}]-[-103850]=-2147864+103850=-2043014\,\mathrm{kJ/kmol}.$$
> $$\mathrm{PCI}=\frac{2043014}{44.09}=46340\,\mathrm{kJ/kg\,C_3H_8}\approx46.34\,\mathrm{MJ/kg}.$$
>
> Para PCS: $\mathrm{H_2O}$ sale como líquido ($4\,\mathrm{mol}$ de $\mathrm{H_2O}$, $\bar{h}_f^\circ=-285826$):
> $$\bar{h}_R^\circ\big|_{H_2O(l)}=[3(-393520)+4(-285826)]-[-103850]=-1180560-1143304+103850=-2220014\,\mathrm{kJ/kmol}.$$
> $$\mathrm{PCS}=\frac{2220014}{44.09}=50350\,\mathrm{kJ/kg}\approx50.35\,\mathrm{MJ/kg}. \qquad \blacksquare$$
>
> La diferencia $\mathrm{PCS}-\mathrm{PCI}=4010\,\mathrm{kJ/kg}$ corresponde exactamente al calor de condensación de los $4\,\mathrm{mol}$ de $\mathrm{H_2O}$: $4\times18.015\times2441.7/44.09=4010\,\mathrm{kJ/kg}$. ✓

---

## Notas de esta sección

> [!info] Mapa
> - [[Temperatura Adiabatica de Llama]] — balance entálpico completo para determinar $T_{\rm AFT}$; ejemplo con metano y exceso de aire; método iterativo con tablas de entalpía.

> [!referencia]
> Çengel & Boles, *Termodinámica*, cap. 15; Moran & Shapiro, cap. 13; Borgnakke & Sonntag, cap. 13. Tablas de entalpía de formación: NIST-JANAF o Apéndice A de Moran & Shapiro.
