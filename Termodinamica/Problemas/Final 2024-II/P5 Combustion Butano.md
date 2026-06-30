---
title: "P5 — Combustión de butano con aire húmedo"
order: 6
tags:
  - termodinamica
  - problemas
  - combustion
draft: false
aliases:
  - combustión butano examen final
  - C4H10 aire húmedo
---

# P5 — Combustión de butano con aire húmedo

> [!definicion] Enunciado
> Butano gaseoso $\mathrm{C_4H_{10}(g)}$ a $25\,^\circ$C y $100$ kPa reacciona con **$200\%$ de aire teórico** a $25\,^\circ$C y $100$ kPa. El aire tiene una humedad relativa de $\phi=75\%$. La combustión es completa y los productos salen a $600$ K y $100$ kPa. La temperatura ambiente es $T_0=25\,^\circ$C. Se pide:
> **(11)** entalpía de combustión alta (PCS) del butano a $25\,^\circ$C con aire seco; **(12)** trabajo reversible [kJ/kg] (productos y reactantes a $25\,^\circ$C); **(13)** ecuación de combustión para los datos del problema; **(14)** calor transferido; **(15)** cambio de entropía; **(16)** irreversibilidad [kJ/kg].

## Estrategia

> [!teoria]
> Se aplica el balance estequiométrico de [[Combustion/index | combustión]] con exceso de aire y humedad, y luego balances de energía y entropía de mezclas reactivas usando entalpías de formación $\bar h_f^\circ$ y entropías absolutas $\bar s^\circ$. $M_{\mathrm{C_4H_{10}}}=58{,}12$ kg/kmol.

![[combustion_esquema_reactivos_productos.svg|420]]

## (13) Ecuación de combustión

> [!solucion]
> **Estequiométrica:** $\mathrm{C_4H_{10}}+a(\mathrm{O_2}+3{,}76\,\mathrm{N_2})\to4\,\mathrm{CO_2}+5\,\mathrm{H_2O}+3{,}76a\,\mathrm{N_2}$. Balance de O: $2a=8+5\Rightarrow a=6{,}5$.
> **$200\%$ de aire teórico:** $\mathrm{O_2}=2(6{,}5)=13$, $\mathrm{N_2}=13(3{,}76)=48{,}88$; sobra $\mathrm{O_2}=6{,}5$.
> **Humedad del aire** ($\phi=75\%$ a $25\,^\circ$C, $P_{sat}=3{,}169$ kPa): $P_v=0{,}75(3{,}169)=2{,}377$ kPa. Moles de agua por mol de aire seco:
> $$\frac{N_w}{N_{aire}}=\frac{P_v}{P-P_v}=\frac{2{,}377}{97{,}62}=0{,}02435.$$
> Aire seco total $=13+48{,}88=61{,}88$ mol $\Rightarrow N_w=0{,}02435(61{,}88)=1{,}507$ mol. Ecuación:
> $$\boxed{\mathrm{C_4H_{10}}+13\,\mathrm{O_2}+48{,}88\,\mathrm{N_2}+1{,}507\,\mathrm{H_2O}\to4\,\mathrm{CO_2}+6{,}507\,\mathrm{H_2O}+6{,}5\,\mathrm{O_2}+48{,}88\,\mathrm{N_2}}$$

## (11) Poder calorífico superior (PCS)

> [!solucion]
> Reacción estequiométrica con aire seco y **agua líquida** en productos, todo a $25\,^\circ$C. Con $\bar h_f^\circ$ [kJ/kmol]: $\mathrm{C_4H_{10}(g)}=-126\,150$, $\mathrm{CO_2}=-393\,520$, $\mathrm{H_2O(l)}=-285\,830$:
> $$\bar h_{RP}=[4(-393\,520)+5(-285\,830)]-(-126\,150)=-2\,877\,080\ \text{kJ/kmol}.$$
> $$\mathrm{PCS}=|\bar h_{RP}|=2\,877\,080\ \text{kJ/kmol}=\frac{2\,877\,080}{58{,}12}=\boxed{49\,500\ \text{kJ/kg}}.$$

## (12) Trabajo reversible (reactantes y productos a 25 °C)

> [!solucion]
> Trabajo reversible máximo $=-\Delta G$ de la reacción a $T_0=298{,}15$ K, con $\mathrm{H_2O}$ vapor en productos:
> $$W_{rev}=(H_R-H_P)_{298}-T_0\,(S_R-S_P)_{298}.$$
> Entalpías (con $\mathrm{H_2O(g)}$, $\bar h_f^\circ=-241\,820$):
> $$H_R=-126\,150+1{,}507(-241\,820)=-490\,573,\quad H_P=4(-393\,520)+6{,}507(-241\,820)=-3\,147\,400\ \text{kJ/kmol}.$$
> Entropías absolutas a $298$ K corregidas por presión parcial $\bar s_i=\bar s_i^\circ-R_u\ln y_i$ (con $P=100$ kPa $=P_{ref}$) dan $S_R\approx12\,950$ y $S_P\approx13\,247$ kJ/kmol·K, luego $S_R-S_P\approx-298$.
> $$W_{rev}=2\,656\,830-298{,}15(-298)=2\,745\,600\ \text{kJ/kmol}=\boxed{47\,240\ \text{kJ/kg}}.$$

## (14) Calor transferido

> [!solucion]
> Balance de energía (cámara, productos a $600$ K, reactantes a $298$ K, $W=0$):
> $$Q=H_P(600)-H_R(298)=\sum_P N(\bar h_f^\circ+\Delta\bar h_{600})-\sum_R N\,\bar h_f^\circ.$$
> Con $\Delta\bar h_{600}-\Delta\bar h_{298}$ [kJ/kmol]: $\mathrm{CO_2}=12\,906$, $\mathrm{H_2O}=10\,498$, $\mathrm{O_2}=9\,247$, $\mathrm{N_2}=8\,894$:
> $$H_P(600)=4(-380\,614)+6{,}507(-231\,322)+6{,}5(9\,247)+48{,}88(8\,894)=-2\,532\,800\ \text{kJ/kmol}.$$
> $$Q=-2\,532\,800-(-490\,573)=-2\,042\,250\ \text{kJ/kmol}=\frac{-2\,042\,250}{58{,}12}=\boxed{-35\,140\ \text{kJ/kg}}.$$
> El signo negativo indica calor **cedido**; es menor que el PCS porque los productos salen calientes ($600$ K) y con el agua en fase vapor.

## (15) Cambio de entropía

> [!solucion]
> Entropía de productos (a $600$ K) menos reactantes (a $298$ K), ambas con corrección de presión parcial:
> $$\Delta S=S_P(600)-S_R(298)\approx14\,661-12\,950=\boxed{1712\ \text{kJ/kmol·K}}=29{,}5\ \text{kJ/kg·K}.$$

## (16) Irreversibilidad

> [!solucion]
> Con generación de entropía $\dot S_{gen}=\Delta S_{sist}-Q/T_0$ (calor cedido al ambiente a $T_0$):
> $$S_{gen}=1712-\frac{-2\,042\,250}{298{,}15}=1712+6851=8563\ \text{kJ/kmol·K}.$$
> $$I=T_0\,S_{gen}=298{,}15(8563)=2\,553\,000\ \text{kJ/kmol}=\frac{2\,553\,000}{58{,}12}=\boxed{43\,920\ \text{kJ/kg}}.$$

> [!info] Nota
> Los valores de $\bar h_f^\circ$, $\bar s^\circ$ y $\Delta\bar h_{600}$ se toman de tablas termoquímicas estándar; conviene cotejarlos con las tablas del curso (CATT3). El PCS $\approx49{,}5$ MJ/kg del butano coincide con la literatura, lo que ancla el resto.

## Notas usadas

> [!referencia]
> [[Combustion/index | Combustión]] · [[Temperatura Adiabatica de Llama]] · [[Combustion Incompleta]] · [[Mezclas de Gases]] · [[Entropia]] · [[Exergia]]
