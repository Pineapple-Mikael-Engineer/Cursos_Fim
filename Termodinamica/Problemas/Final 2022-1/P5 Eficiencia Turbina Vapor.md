---
title: "P5 — Eficiencia isentrópica de turbina de vapor"
order: 6
tags: [termodinamica, problemas, turbina]
draft: false
aliases: [eficiencia isentrópica turbina vapor saturado]
---

# P5 — Eficiencia isentrópica de turbina de vapor

> [!definicion] Enunciado
> Vapor de agua a $4{,}4$ MPa y $385\,^\circ$C se expande en una turbina adiabática a $105$ kPa. ¿Cuál es la eficiencia isentrópica de esta turbina si el vapor sale como **vapor saturado**?

> [!solucion]
> **Entrada** ($4{,}4$ MPa, $385\,^\circ$C, interpolado): $h_1\approx3169$ kJ/kg, $s_1\approx6{,}663$ kJ/kg·K.
> **Salida real** (vapor saturado a $105$ kPa): $h_2\approx2677$ kJ/kg.
> **Salida isentrópica** ($s_{2s}=s_1=6{,}663$ a $105$ kPa, bifásica): $x_{2s}=\dfrac{6{,}663-1{,}303}{6{,}057}=0{,}885$, $h_{2s}=417{,}5+0{,}885(2258)=2416$ kJ/kg.
> $$\eta_T=\frac{h_1-h_2}{h_1-h_{2s}}=\frac{3169-2677}{3169-2416}=\frac{492}{753}=\boxed{65{,}3\%}.$$

> [!info]
> Valores de tabla interpolados (a cotejar con CATT3). La salida real (vapor saturado) está más arriba que la isentrópica (húmeda), por eso $\eta_T<1$.

> [!referencia]
> [[Sistemas/Dispositivos Flujo/Turbinas | Turbinas]] · [[Vapor Sobrecalentado]] · [[Calidad]]
