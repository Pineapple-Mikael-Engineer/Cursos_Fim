---
title: Combustión Incompleta
tags:
  - termodinamica
  - teoria
  - combustion
  - combustion-incompleta
  - orsat
  - mezcla-rica
draft: false
aliases:
  - Combustión Incompleta
  - Combustion Incompleta
  - Análisis de Gases de Combustión
  - Orsat
---

# Combustión Incompleta $\Phi>1:\;\mathrm{C_xH_y}\to\mathrm{CO_2}+\mathrm{CO}+\mathrm{H_2}+\mathrm{H_2O}+\mathrm{N_2}$

> [!definicion]
> La **combustión incompleta** ocurre cuando la mezcla combustible-oxidante es **rica** ($\Phi>1$, insuficiencia de aire) o cuando hay mezcla deficiente, baja temperatura de llama o tiempos de residencia insuficientes. Los productos incluyen **CO**, $\mathrm{H_2}$ y en casos extremos hidrocarburos sin quemar (UHC). La combustión incompleta implica: (1) pérdida de eficiencia (calor latente del CO y H₂ no liberado), (2) emisiones contaminantes reguladas por norma, y (3) riesgo de explosión en espacios confinados. El **análisis de Orsat** cuantifica la composición de los gases de combustión y permite determinar la relación aire-combustible real.

---

## Causas y condiciones de combustión incompleta

| Causa | Mecanismo |
|:---|:---|
| Mezcla rica ($\Phi>1$, AF < AF_est) | Exceso de combustible; el $\mathrm{O_2}$ se agota antes de oxidar todo el C a $\mathrm{CO_2}$ |
| Enfriamiento rápido de la llama | Las reacciones de oxidación se congelan antes de completarse |
| Mala mezcla turbulenta | Bolsas de combustible sin contacto con $\mathrm{O_2}$ |
| Extinción en paredes frías (quenching) | Reacciones en cadena se interrumpen cerca de la pared |

El producto principal es el **monóxido de carbono (CO)**, resultado de la oxidación parcial:
$$\mathrm{C} + \frac{1}{2}\mathrm{O_2} \to \mathrm{CO} \qquad \Delta\bar{h}_R^\circ = -110530\,\mathrm{kJ/kmol}$$
en lugar de la completa:
$$\mathrm{C} + \mathrm{O_2} \to \mathrm{CO_2} \qquad \Delta\bar{h}_R^\circ = -393520\,\mathrm{kJ/kmol}.$$
El CO libera solo $28\%$ del calor total disponible del carbono. El $72\%$ restante queda latente en el CO:
$$\mathrm{CO}+\frac{1}{2}\mathrm{O_2}\to\mathrm{CO_2} \qquad \Delta\bar{h}_R^\circ=-282990\,\mathrm{kJ/kmol}.$$

---

## Balanceo estequiométrico con combustión incompleta

Para una **mezcla rica** de hidrocarburo $\mathrm{C_xH_y}$ con $a<a_{\rm est}$ moles de $\mathrm{O_2}$, los productos contienen $\mathrm{CO_2}$, $\mathrm{CO}$, $\mathrm{H_2O}$ y $\mathrm{N_2}$. El balanceo requiere una hipótesis sobre la distribución del carbono entre $\mathrm{CO_2}$ y $\mathrm{CO}$: **hipótesis estándar de equilibrio parcial**: todo el $\mathrm{H}$ se oxida a $\mathrm{H_2O}$ antes de que el carbono se oxide (agua se forma preferencialmente), y el $\mathrm{O_2}$ restante oxida $\mathrm{C}\to\mathrm{CO_2}$; si no alcanza, el resto queda como $\mathrm{CO}$.

Sean $b$ moles de $\mathrm{CO_2}$ y $(x-b)$ moles de $\mathrm{CO}$ en los productos:
$$\mathrm{C_xH_y}+a(\mathrm{O_2}+3.76\,\mathrm{N_2})\to b\,\mathrm{CO_2}+(x-b)\,\mathrm{CO}+\frac{y}{2}\mathrm{H_2O}+3.76a\,\mathrm{N_2}.$$

Balance de oxígeno (el único que determina $b$):
$$2a = 2b+(x-b)+\frac{y}{2} \implies b = 2a - x - \frac{y}{2} + b \implies b = 2a-\frac{y}{2}-(x-b).$$
Simplificando: balance O: $\mathrm{O}_{\rm entrada}=2a$; $\mathrm{O}_{\rm en\,CO_2}=2b$; $\mathrm{O}_{\rm en\,CO}=(x-b)$; $\mathrm{O}_{\rm en\,H_2O}=y/2$.

$$2a = 2b+(x-b)+\frac{y}{2} = b+x+\frac{y}{2} \implies b = 2a-x-\frac{y}{2}.$$

Para que $b\ge0$ (existe $\mathrm{CO_2}$): $a\ge(x+y/2)/2$, y para que $x-b\ge0$ (existe $\mathrm{CO}$): $b=2a-x-y/2\le x$, es decir $a\le x+y/4=a_{\rm est}$.

Luego la combustión incompleta con solo CO (no $\mathrm{H_2}$) aplica cuando:
$$\frac{x+y/2}{2} \le a \le a_{\rm est} = x+\frac{y}{4}.$$

> [!demostracion] Balance completo para combustión parcialmente incompleta
> **Sistema:** $1\,\mathrm{kmol}$ de $\mathrm{C_xH_y}$, $a$ kmol de $\mathrm{O_2}$ (con $a<a_{\rm est}$).
>
> **Hipótesis:** H se oxida completamente a $\mathrm{H_2O}$ (reacción más rápida cinéticamente); el $\mathrm{O_2}$ restante oxida carbono lo más posible.
>
> **Paso 1.** $\mathrm{O_2}$ consumido por el hidrógeno: $y/4$ kmol (para producir $y/2$ kmol de $\mathrm{H_2O}$).
>
> **Paso 2.** $\mathrm{O_2}$ disponible para el carbono: $a-y/4$.
>
> **Paso 3.** Cada mol de $\mathrm{C}\to\mathrm{CO_2}$ consume 1 mol de $\mathrm{O_2}$; cada mol de $\mathrm{C}\to\mathrm{CO}$ consume $1/2$ mol. Con $b$ moles de $\mathrm{CO_2}$ y $x-b$ de $\mathrm{CO}$:
> $$b\cdot1 + (x-b)\cdot\tfrac{1}{2} = a-\frac{y}{4} \implies \frac{b}{2}+\frac{x}{2} = a-\frac{y}{4} \implies b = 2a-x-\frac{y}{2}. \qquad \blacksquare$$

---

## Análisis de Orsat

El **aparato de Orsat** mide la composición de gases secos de combustión por absorción química secuencial:

1. **CO₂**: absorbido por solución de **KOH** (hidróxido de potasio, 33%).
2. **O₂**: absorbido por **pirogalol** alcalino.
3. **CO**: absorbido por **cloruro cuproso** ($\mathrm{CuCl}$ en solución de $\mathrm{HCl}$).
4. **N₂**: por **diferencia** (gases restantes que no reaccionan con los reactivos anteriores).

El resultado es el análisis **base seca** (sin agua, que condensa antes de entrar al aparato): fracciones volumétricas $y_{\mathrm{CO_2}}$, $y_{\mathrm{O_2}}$, $y_{\mathrm{CO}}$, $y_{\mathrm{N_2}}$ con $\sum=1$.

**Determinación de AF desde el análisis de Orsat.** Con base en $100\,\mathrm{mol}$ de gases secos:

**Balance de carbono:**
$$n_C = n_{\mathrm{CO_2}}+n_{\mathrm{CO}} = (y_{\mathrm{CO_2}}+y_{\mathrm{CO}})\times100.$$

**Balance de nitrógeno:**
$$n_{\mathrm{N_2}} = y_{\mathrm{N_2}}\times100 \implies n_{\mathrm{O_2,aire}} = \frac{n_{\mathrm{N_2}}}{3.76}.$$

**Balance de hidrógeno** (necesario para encontrar el agua que se condensó, no medida por Orsat):
La masa de $\mathrm{H}$ en el combustible $= m_{\mathrm{H_2O,total}}\times2/18$. Se calcula cerrando el balance de O:
$$n_{\mathrm{H_2O}} = 2n_{\mathrm{O_2,aire}} - 2n_{\mathrm{CO_2}} - n_{\mathrm{CO}} - 2n_{\mathrm{O_2,gases}}.$$

**Relación AF:**
$$\mathrm{AF} = \frac{m_{\rm aire}}{m_{\rm comb}} = \frac{(n_{\mathrm{O_2,aire}})\times(32+3.76\times28)}{n_C\times M_C + n_H\times M_H}$$

---

## Pérdida de eficiencia por CO en los gases

La fracción del calor perdida por la presencia de CO en los productos:
$$\eta_{\rm comb} = 1 - \frac{n_{\mathrm{CO}}\cdot\lvert\Delta\bar{h}_{R,\mathrm{CO}}\rvert}{n_{\rm comb}\cdot\mathrm{PCI}}.$$

Para $\mathrm{CH_4}$ con $1\%$ de CO en productos secos: la pérdida es $\sim1.4\%$ del PCI, que en una caldera de $10\,\mathrm{MW}$ son $140\,\mathrm{kW}$ desperdiciados. Por eso los quemadores modernos se diseñan con ligero exceso de aire ($\Phi\approx0.9$–$0.95$) para garantizar combustión completa sin producir CO.

---

## Ejemplo complejo: análisis de gases de motor de gasolina

> [!ejemplo]
> Un motor de gasolina (combustible: octano, $\mathrm{C_8H_{18}}$, $M=114.22\,\mathrm{kg/kmol}$) produce gases de escape con el siguiente análisis de Orsat (base seca):
>
> $\mathrm{CO_2}:\,12.0\%$, $\mathrm{O_2}:\,0.5\%$, $\mathrm{CO}:\,2.5\%$, $\mathrm{N_2}:\,85.0\%$.
>
> Determinar: (a) la reacción de combustión real (moles de reactivos y productos), (b) la relación AF real, (c) la relación de equivalencia $\Phi$, (d) la pérdida calorífica por CO.

> [!solucion]
> **Base de cálculo:** $100\,\mathrm{mol}$ de gases secos.
>
> **Composición en la base:** $n_{\mathrm{CO_2}}=12.0$, $n_{\mathrm{O_2}}=0.5$, $n_{\mathrm{CO}}=2.5$, $n_{\mathrm{N_2}}=85.0$ mol.
>
> **(a) Moles de reactivos.**
>
> **Nitrógeno y oxígeno del aire:**
> $$n_{\mathrm{N_2}}=85.0\,\mathrm{mol}\implies n_{\mathrm{O_2,aire}}=\frac{85.0}{3.76}=22.61\,\mathrm{mol}.$$
>
> **Balance de carbono:**
> $$n_C=n_{\mathrm{CO_2}}+n_{\mathrm{CO}}=12.0+2.5=14.5\,\mathrm{mol\,C}.$$
>
> Para octano $\mathrm{C_8H_{18}}$: cada mol contiene 8 átomos de C. Moles de combustible:
> $$n_{\mathrm{C_8H_{18}}}=\frac{14.5}{8}=1.8125\,\mathrm{kmol}.$$
>
> **Balance de hidrógeno (para hallar $n_{\mathrm{H_2O}}$):**
> Átomos H en combustible: $1.8125\times18=32.625$, luego $n_{\mathrm{H_2O}}=32.625/2=16.31\,\mathrm{mol}$.
>
> **Verificación con balance de oxígeno:**
> O entrante (del aire): $2\times22.61=45.22\,\mathrm{mol\,O}$.
> O en productos: $2\times12.0+2.5+16.31+2\times0.5=24.0+2.5+16.31+1.0=43.81\,\mathrm{mol\,O}$.
> Diferencia: $45.22-43.81=1.41\,\mathrm{mol\,O}$ → ajuste por redondeo; en la práctica se itera. Para este ejemplo adoptamos los valores calculados.
>
> **Reacción por mol de combustible** (dividiendo todo por $1.8125$):
> $$\mathrm{C_8H_{18}}+12.48\,\mathrm{O_2}+46.90\,\mathrm{N_2}\to 6.621\,\mathrm{CO_2}+1.379\,\mathrm{CO}+9.0\,\mathrm{H_2O}+0.276\,\mathrm{O_2}+46.90\,\mathrm{N_2}.$$
>
> **(b) Relación AF real.**
> Masa de aire por mol de combustible: $n_{\mathrm{O_2,aire}}/1.8125\times M_{\rm aire} = 12.48\times(32+3.76\times28)/\mathrm{mol\,comb}$:
> $$m_{\rm aire}=12.48\times(32+105.28)=12.48\times137.28=1713.2\,\mathrm{kg/kmol\,comb}.$$
> $$\mathrm{AF}=\frac{1713.2}{114.22}=15.00\,\mathrm{kg\,aire/kg\,comb}.$$
>
> **(c) Relación de equivalencia.**
> Para octano: $a_{\rm est}=8+18/4=8+4.5=12.5$ mol de $\mathrm{O_2}$. $\mathrm{AF}_{\rm est}=12.5\times137.28/114.22=15.04$.
> $$\Phi=\frac{\mathrm{AF}_{\rm est}}{\mathrm{AF}}=\frac{15.04}{15.00}=1.003\approx1.00.$$
> La mezcla es casi estequiométrica pero con ligera tendencia rica ($\Phi=1.003>1$), lo que explica la presencia de CO ($2.5\%$) y la baja concentración de $\mathrm{O_2}$ ($0.5\%$) en los gases: coexisten por la no uniformidad de la mezcla en el cilindro (combustión heterogénea real).
>
> **(d) Pérdida por CO.**
> CO producido: $1.379$ mol por mol de $\mathrm{C_8H_{18}}$.
> PCI del octano: $\approx44430\,\mathrm{kJ/kg}$, es decir $44430\times114.22=5075\times10^3\,\mathrm{kJ/kmol}$.
> Calor "almacenado" en el CO: $1.379\times282990=390144\,\mathrm{kJ/kmol\,comb}$.
> $$\%\,\text{pérdida}=\frac{390144}{5075000}\times100=7.7\%.$$
> Una pérdida del $7.7\%$ del poder calorífico es significativa. Los catalizadores de tres vías (TWC) en vehículos oxidian el CO residual: $\mathrm{CO}+\frac{1}{2}\mathrm{O_2}\to\mathrm{CO_2}$, recuperando esa energía y eliminando las emisiones. $\blacksquare$

> [!referencia]
> Çengel & Boles, *Termodinámica*, §15-3; Moran & Shapiro §13.2; Borgnakke & Sonntag §13.3. Normas de emisión: EPA Tier 3, Euro 6 (CO $<$ 1.0 g/km para gasolina).
