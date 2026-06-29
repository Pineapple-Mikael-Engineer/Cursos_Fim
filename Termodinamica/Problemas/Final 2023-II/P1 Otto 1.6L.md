---
title: "P1 — Motor Otto de 1,6 L (4 cilindros)"
order: 2
tags: [termodinamica, problemas, ciclos, otto]
draft: false
aliases: [Otto 1.6 litros, motor 76 kW]
---

# P1 — Motor Otto de 1,6 L (4 cilindros)

> [!definicion] Enunciado
> Un motor Otto ideal de $1{,}6$ litros de cilindrada, **4 tiempos y 4 cilindros**, con una relación de compresión $r_k=6{,}2$, entrega una potencia de $76{,}1$ kW, siendo el coeficiente adiabático $k=1{,}4$. Se pide: **(1)** el volumen muerto de cada cilindro [cm³]; **(2)** el rendimiento del motor [%]; **(3)** el calor absorbido [kW]; **(4)** el calor rechazado [kW].

![[otto_diagrama_Pv.svg|340]]

> [!solucion] (1) Volumen muerto
> Cilindrada por cilindro $=1600/4=400\ \text{cm}^3=V_1-V_2$, con $V_1/V_2=6{,}2$:
> $$V_2=\frac{V_1-V_2}{r_k-1}=\frac{400}{5{,}2}=\boxed{76{,}9\ \text{cm}^3}.$$

> [!solucion] (2) Rendimiento
> $$\eta=1-\frac{1}{r_k^{\,k-1}}=1-(6{,}2)^{-0{,}4}=\boxed{51{,}8\%}.$$

> [!solucion] (3) y (4) Calor absorbido y rechazado
> $$\dot Q_{in}=\frac{\dot W}{\eta}=\frac{76{,}1}{0{,}518}=\boxed{146{,}9\ \text{kW}},\qquad \dot Q_{out}=\dot Q_{in}-\dot W=146{,}9-76{,}1=\boxed{70{,}8\ \text{kW}}.$$

> [!info] Verificación
> Coincide con la clave ($\eta=51{,}8\%$). $\eta$ depende solo de $r_k$.

> [!referencia]
> [[Conversión de Energía/Ciclos de Combustión Interna/Ciclo Otto | Ciclo Otto]] · [[Gas Ideal]]
