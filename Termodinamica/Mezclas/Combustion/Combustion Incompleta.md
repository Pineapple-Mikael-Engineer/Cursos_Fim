---
title: Combustión Incompleta
order: 1
tags:
  - termodinamica
  - mezclas
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

# Combustión Incompleta

> [!definicion]
> La **combustión incompleta** ocurre cuando la mezcla combustible-oxidante es **rica** ($\Phi>1$, aire insuficiente) o cuando hay baja temperatura de llama, tiempos de residencia cortos, o mala mezcla turbulenta. Los productos contienen **CO**, $\mathrm{H_2}$ y eventualmente hidrocarburos sin quemar (UHC). Implica: (1) pérdida de eficiencia energética, (2) emisiones contaminantes reguladas, y (3) riesgo de intoxicación en espacios confinados.
>
> *¿Por qué aparece el CO?* La oxidación del carbono tiene dos rutas posibles:
> $$\mathrm{C}+\tfrac{1}{2}\mathrm{O_2}\to\mathrm{CO}\quad(\bar{h}_R=-110\,530\,\mathrm{kJ/kmol})$$
> $$\mathrm{C}+\mathrm{O_2}\to\mathrm{CO_2}\quad(\bar{h}_R=-393\,520\,\mathrm{kJ/kmol}).$$
>
> La primera solo libera el 28% del calor disponible del carbono; el 72% restante queda "latente" en el enlace C≡O del CO. El CO puede seguir oxidándose si hay $\mathrm{O_2}$: $\mathrm{CO}+\tfrac{1}{2}\mathrm{O_2}\to\mathrm{CO_2}$ ($\bar{h}_R=-282\,990\,\mathrm{kJ/kmol}$). En una mezcla rica, el $\mathrm{O_2}$ se agota antes de completar esta segunda etapa.

![[combustion_incompleta_esquema.svg|440]]
*Diagrama de equilibrio parcial: con $\Phi > 1$ el O₂ alcanza para oxidar todo el H a H₂O y parte del C a CO₂; el carbono restante forma CO. La fracción entre CO₂ y CO depende de cuánto $\mathrm{O_2}$ disponible hay para el carbono.*

---

## Balanceo para mezcla rica: CO en productos

> [!proposicion]
> Para $\mathrm{C_xH_y}$ con $a$ moles de $\mathrm{O_2}$ ($a < a_{\rm est}$), bajo la hipótesis de equilibrio parcial, los productos son:
> $$\mathrm{C_xH_y}+a(\mathrm{O_2}+3.76\,\mathrm{N_2})\to b\,\mathrm{CO_2}+(x-b)\mathrm{CO}+\frac{y}{2}\mathrm{H_2O}+3.76a\,\mathrm{N_2},$$
> donde
> $$\boxed{b = 2a - x - \frac{y}{2}}.$$
>
> Rango de validez: $b \geq 0$ exige $a \geq (x+y/2)/2$; $x-b \geq 0$ (existe CO) exige $a \leq a_{\rm est} = x+y/4$.

> [!demostracion]
> **Hipótesis:** (1) Todo el H se oxida a $\mathrm{H_2O}$ (reacción más rápida cinéticamente). (2) El $\mathrm{O_2}$ restante oxida C a $\mathrm{CO_2}$ primero; si no alcanza, el resto queda como CO. (3) N₂ inerte.
>
> **Paso 1 — O₂ consumido por el hidrógeno.** Para producir $y/2$ moles de $\mathrm{H_2O}$ se necesitan $y/4$ moles de $\mathrm{O_2}$: $\mathrm{H_y}+y/4\,\mathrm{O_2}\to y/2\,\mathrm{H_2O}$.
>
> **Paso 2 — O₂ disponible para el carbono.** Después de oxidar el H, quedan:
> $$n_{\mathrm{O_2,\,para\,C}} = a - \frac{y}{4}.$$
>
> **Paso 3 — Distribución del carbono.** Sean $b$ moles de $\mathrm{CO_2}$ y $(x-b)$ moles de CO. El $\mathrm{O_2}$ consumido: 1 mol por mol de $\mathrm{CO_2}$, $1/2$ mol por mol de CO:
> $$b\cdot1 + (x-b)\cdot\tfrac{1}{2} = a - \frac{y}{4}.$$
>
> **Paso 4 — Despejar $b$.** Expandiendo el lado izquierdo:
> $$b + \frac{x-b}{2} = a-\frac{y}{4} \implies \frac{b}{2}+\frac{x}{2} = a-\frac{y}{4} \implies b = 2a - x - \frac{y}{2}.$$
>
> **Paso 5 — Verificación de límites.** Si $a=a_{\rm est}=x+y/4$: $b=2(x+y/4)-x-y/2=2x+y/2-x-y/2=x$ → todo el C es $\mathrm{CO_2}$, cero CO ✓ (combustión completa en el límite). Si $a=(x+y/2)/2$: $b=2(x+y/2)/2-x-y/2=x+y/2-x-y/2=0$ → todo el C sale como CO, cero $\mathrm{CO_2}$ ✓ (caso extremo). $\blacksquare$

---

## Análisis de Orsat: composición medida → reacción real

> [!teoria]
> El **aparato de Orsat** mide la composición de los gases de combustión secos por absorción química secuencial:
>
> 1. $\mathrm{CO_2}$: absorbido por $\mathrm{KOH}$ al 33%.
> 2. $\mathrm{O_2}$: absorbido por pirogalol alcalino.
> 3. $\mathrm{CO}$: absorbido por cloruro cuproso ($\mathrm{CuCl}$).
> 4. $\mathrm{N_2}$: por diferencia (todo lo que no reaccionó).
>
> El resultado es un **análisis base seca** (el $\mathrm{H_2O}$ condensa antes de entrar al aparato): fracciones volumétricas $y_{\mathrm{CO_2}}$, $y_{\mathrm{O_2}}$, $y_{\mathrm{CO}}$, $y_{\mathrm{N_2}}$ con $\sum=1$.

> [!proposicion]
> Procedimiento para reconstruir la reacción real a partir del análisis de Orsat (base de cálculo: 100 mol de gases secos):
>
> **Balance de N₂** → moles de $\mathrm{O_2}$ del aire:
> $$n_{\mathrm{O_2,aire}} = n_{\mathrm{N_2}}/3.76.$$
>
> **Balance de C** → moles de combustible:
> $$n_C = n_{\mathrm{CO_2}}+n_{\mathrm{CO}}; \quad n_{\rm comb} = n_C/x.$$
>
> **Balance de O** → $\mathrm{H_2O}$ condensada (no medida por Orsat):
> $$n_{\mathrm{H_2O}} = 2n_{\mathrm{O_2,aire}} - 2n_{\mathrm{CO_2}} - n_{\mathrm{CO}} - 2n_{\mathrm{O_2,gases}}.$$
>
> **Relación AF:**
> $$\mathrm{AF} = \frac{n_{\mathrm{O_2,aire}}\times137.28}{n_C\times M_C + n_H\times M_H}.$$

---

## Pérdida de eficiencia por CO

> [!proposicion]
> La fracción del poder calorífico perdida por la presencia de CO en los gases:
> $$\eta_{\rm comb} = 1 - \frac{n_{\mathrm{CO}}\times|{\bar{h}_{R,\mathrm{CO}}}|}{n_{\rm comb}\times\mathrm{PCI}}, \qquad |\bar{h}_{R,\mathrm{CO}}| = 282\,990\,\mathrm{kJ/kmol}.$$
>
> Para $\mathrm{CH_4}$ con 1% de CO en productos secos: pérdida ≈ 1.4% del PCI. En una caldera de $10\,\mathrm{MW}$: $140\,\mathrm{kW}$ desperdiciados. Por eso los quemadores modernos operan con ligero exceso de aire ($\Phi \approx 0.90$–$0.95$).

---

## Ejemplo: análisis de gases de motor de gasolina

> [!ejemplo]
> Un motor de gasolina (combustible: octano $\mathrm{C_8H_{18}}$, $M=114.22\,\mathrm{kg/kmol}$) produce gases de escape con el siguiente análisis de Orsat (base seca):
> $$\mathrm{CO_2}:\,12.0\%,\quad\mathrm{O_2}:\,0.5\%,\quad\mathrm{CO}:\,2.5\%,\quad\mathrm{N_2}:\,85.0\%.$$
> Determinar: (a) moles de reactivos y productos por mol de combustible; (b) AF real; (c) $\Phi$; (d) pérdida por CO.

> [!solucion]
> **Base de cálculo:** 100 mol de gases secos.
>
> $n_{\mathrm{CO_2}}=12.0$; $n_{\mathrm{O_2}}=0.5$; $n_{\mathrm{CO}}=2.5$; $n_{\mathrm{N_2}}=85.0$.
>
> **(a) Reconstrucción de la reacción.**
>
> $\mathrm{O_2}$ del aire: $n_{\mathrm{O_2,aire}}=85.0/3.76=22.61\,\mathrm{mol}$.
>
> Balance de carbono: $n_C=12.0+2.5=14.5\,\mathrm{mol\,C}$. Para octano ($x=8$): $n_{\mathrm{C_8H_{18}}}=14.5/8=1.8125\,\mathrm{mol}$.
>
> Balance de H: átomos H en combustible $= 1.8125\times18=32.625$; $n_{\mathrm{H_2O}}=32.625/2=16.31\,\mathrm{mol}$.
>
> Verificación con balance de O: O entra $=2\times22.61=45.22$; O en productos $=2\times12.0+2.5+16.31+2\times0.5=43.81$. Diferencia 1.41 mol O (< 4%, error de redondeo aceptable).
>
> **Por mol de combustible** (dividiendo por 1.8125):
> $$\mathrm{C_8H_{18}}+12.48\,\mathrm{O_2}+46.90\,\mathrm{N_2}\to6.62\,\mathrm{CO_2}+1.38\,\mathrm{CO}+9.0\,\mathrm{H_2O}+0.276\,\mathrm{O_2}+46.90\,\mathrm{N_2}.$$
>
> **(b) Relación AF real.**
> $m_{\rm aire}=12.48\times137.28=1713\,\mathrm{kg/kmol\,comb}$.
> $$\mathrm{AF}=1713/114.22=15.00\,\mathrm{kg\,aire/kg\,comb}.$$
>
> **(c) Relación de equivalencia.** $a_{\rm est}=8+18/4=12.5$. $\mathrm{AF}_{\rm est}=12.5\times137.28/114.22=15.04$.
> $$\Phi=15.04/15.00=1.003\approx1.00.$$
>
> La mezcla es casi estequiométrica pero con ligera tendencia rica ($\Phi>1$): coexisten CO ($2.5\%$) y $\mathrm{O_2}$ ($0.5\%$) por no uniformidad de la mezcla en el cilindro (combustión heterogénea real).
>
> **(d) Pérdida por CO.** CO producido: $1.38$ mol por mol de $\mathrm{C_8H_{18}}$.
> PCI del octano $\approx 44430\,\mathrm{kJ/kg}=44430\times114.22=5.075\times10^6\,\mathrm{kJ/kmol}$.
> Calor latente en CO: $1.38\times282990=390520\,\mathrm{kJ/kmol\,comb}$.
> $$\%\,\text{pérdida}=390520/(5.075\times10^6)\times100=7.7\%.$$
>
> Los catalizadores de tres vías (TWC) oxidan el CO residual: $\mathrm{CO}+\tfrac{1}{2}\mathrm{O_2}\to\mathrm{CO_2}$, recuperando ese 7.7% y eliminando la emisión contaminante.
>
> $\boxed{\mathrm{AF}=15.00\,\mathrm{kg/kg},\quad\Phi=1.003,\quad\text{pérdida por CO}=7.7\%.}$ $\blacksquare$

> [!referencia]
> Çengel & Boles, §15-3; Moran & Shapiro, §13.2; Borgnakke & Sonntag, §13.3. Normas de emisión: EPA Tier 3, Euro 6 ($\mathrm{CO}<1.0\,\mathrm{g/km}$ para gasolina).
