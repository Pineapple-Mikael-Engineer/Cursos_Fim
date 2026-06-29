---
title: "P3 — Motor Diesel (encendido por compresión)"
order: 4
tags: [termodinamica, problemas, ciclos, diesel]
draft: false
aliases: [Diesel encendido compresión, motor 4 cilindros 840 rpm]
---

# P3 — Motor Diesel (encendido por compresión)

> [!definicion] Enunciado
> En un motor teórico de encendido por compresión, la relación aire-combustible es $16$, con un combustible de $PC=36\,900$ kJ/kg. Al final de la expansión (antes de la apertura de la lumbrera de escape) el volumen ocupado por el gas en cada cilindro es $5$ litros y la temperatura $1545$ K. El motor es de **4 tiempos, 4 cilindros**, gira a $840$ RPM, y al inicio de la compresión la temperatura es $300$ K y la presión $100$ kPa. Se pide: **(10)** relación de corte $r_c$; **(11)** volumen muerto por cilindro [cm³]; **(12)** masa de gases expulsada [kg/min]; **(13)** consumo de combustible [kg/h]; **(14)** potencia teórica [kW]. ($k=1{,}4$, $c_p=1{,}0035$, $R=0{,}287$.)

![[diesel_diagrama_Pv.svg|340]]

> [!solucion] (10) Relación de corte
> El estado 4 (fin de expansión) está sobre la isócora de admisión ($V_4=V_1$). Para el Diesel aire-estándar $T_4/T_1=r_c^{\,k}$:
> $$r_c=\left(\frac{T_4}{T_1}\right)^{1/k}=\left(\frac{1545}{300}\right)^{1/1{,}4}=\boxed{3{,}224}.$$

> [!solucion] (11) Volumen muerto
> La combustión fija $T_2$ (con $\dot m_c PC=\dot m_a c_p(T_3-T_2)$, $\dot m_a/\dot m_c=16$, $T_3=r_c T_2$):
> $$\frac{PC}{16}=c_p\,T_2\,(r_c-1)\Rightarrow T_2=\frac{36\,900/16}{1{,}0035(2{,}224)}=1033\ \text{K}.$$
> Compresión isentrópica $T_2=T_1\,r_k^{k-1}\Rightarrow r_k=(T_2/T_1)^{1/(k-1)}=(3{,}444)^{2{,}5}=22{,}0$. Con $V_1=V_4=5000$ cm³:
> $$V_2=\frac{V_1}{r_k}=\frac{5000}{22{,}0}=\boxed{227\ \text{cm}^3}.$$

> [!solucion] (12) y (13) Flujos de masa
> Masa de aire por cilindro y ciclo: $m_a=\dfrac{P_1V_1}{R\,T_1}=\dfrac{100(5000\times10^{-6})}{0{,}287(300)}=5{,}81\times10^{-3}$ kg. Ciclos/min (4 tiempos) $=\tfrac{840}{2}\times4=1680$.
> $$\dot m_{gases}=(m_a+m_a/16)\cdot1680=6{,}17\times10^{-3}\cdot1680=\boxed{10{,}4\ \text{kg/min}},$$
> $$\dot m_{comb}=\frac{m_a}{16}\cdot1680\cdot60=3{,}63\times10^{-4}\cdot100\,800=\boxed{36{,}6\ \text{kg/h}}.$$

> [!solucion] (14) Potencia teórica
> $$\eta_D=1-\frac{1}{r_k^{k-1}}\frac{r_c^{k}-1}{k(r_c-1)}=1-\frac{1}{22^{0{,}4}}\cdot\frac{3{,}224^{1{,}4}-1}{1{,}4(2{,}224)}=61{,}6\%.$$
> $Q_{in}/\text{ciclo}=m_c PC=3{,}63\times10^{-4}(36\,900)=13{,}4$ kJ:
> $$\dot W=\eta_D\,Q_{in}\cdot\frac{1680}{60}=0{,}616(13{,}4)(28)=\boxed{231\ \text{kW}}.$$

> [!info] Nota
> La clave solo dejó respondida $r_c=3{,}224$ (coincide). Los incisos 11–14 se completan aquí (requieren deducir $r_k\approx22$ a partir de la combustión y $r_c$).

> [!referencia]
> [[Conversión de Energía/Ciclos de Combustión Interna/Ciclo Diesel | Ciclo Diesel]] · [[Gas Ideal]] · [[Combustion/index | Combustión]]
