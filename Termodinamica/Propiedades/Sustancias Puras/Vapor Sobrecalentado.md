---
title: Vapor Sobrecalentado
order: 5
tags:
  - termodinamica
  - teoria
  - sustancias-puras
  - vapor-sobrecalentado
  - gas-real
draft: false
aliases:
  - Vapor Sobrecalentado
  - Superheated Steam
  - Región de Vapor
---

# Vapor Sobrecalentado $Z=\frac{Pv}{RT},\quad \text{grado de sobrecalentamiento}=T-T_{\rm sat}(P)$

> [!definicion]
> El **vapor sobrecalentado** es la región donde la temperatura del fluido supera la temperatura de saturación a la presión dada: $T > T_{\rm sat}(P)$. Equivalentemente, $P < P_{\rm sat}(T)$. El estado está fijado por dos propiedades independientes $(T,P)$. El **grado de sobrecalentamiento** $\Delta T_{\rm sh}=T-T_{\rm sat}(P)$ cuantifica la distancia a la cúpula; a mayor $\Delta T_{\rm sh}$, el vapor se aproxima al comportamiento de gas ideal.

> [!info]
> **Contexto.** El vapor sobrecalentado es el fluido de trabajo en la sección de expansión del ciclo Rankine (entre la caldera y la turbina). El sobrecalentamiento aumenta la eficiencia del ciclo y reduce la humedad al final de la expansión.

---

## Tablas de vapor sobrecalentado

Las tablas de vapor sobrecalentado (Tabla A-6 CATT3) tabulan $v$, $u$, $h$, $s$ como función de $(T,P)$. La estructura es: para cada presión fija $P_i$, se dan propiedades en múltiples temperaturas $T>T_{\rm sat}(P_i)$.

**Presiones típicas tabuladas:** 0.01, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.5, 15.0, 17.5, 20.0, 25.0, 30.0 MPa.

**Interpolación.** Si el estado $(T,P)$ no coincide exactamente con una entrada de la tabla, se usa interpolación lineal. Si ambas variables requieren interpolación, la interpolación bilineal es:

$$y(T,P) \approx y(T_1,P_1)\,\frac{(T_2-T)(P_2-P)}{(T_2-T_1)(P_2-P_1)} + y(T_2,P_1)\,\frac{(T-T_1)(P_2-P)}{(T_2-T_1)(P_2-P_1)}$$
$$+ y(T_1,P_2)\,\frac{(T_2-T)(P-P_1)}{(T_2-T_1)(P_2-P_1)} + y(T_2,P_2)\,\frac{(T-T_1)(P-P_1)}{(T_2-T_1)(P_2-P_1)}.$$

En la práctica, en la zona de vapor sobrecalentado se suele interpolar primero en $T$ (a $P$ fija) y luego en $P$, o viceversa.

![[vapor_sobrecalentado_region.svg|440]]
*Diagrama $T$–$v$: la región de vapor sobrecalentado es el área a la derecha de la línea de vapor saturado ($x=1$). Las curvas de presión constante (isobaras) son casi hipérbolas; a baja presión y alta temperatura se aproximan a las isobaras del gas ideal ($Pv=RT$, hipérbolas exactas). El grado de sobrecalentamiento es la distancia horizontal desde la línea $x=1$ hasta la isobara dada.*

---

## Aproximación de gas ideal

A suficiente distancia del punto crítico (presiones bajas o temperaturas altas), el vapor se comporta como gas ideal. El criterio cuantitativo es el **factor de compresibilidad**:

$$Z \equiv \frac{Pv}{RT},$$

con $R = R_u/M$ la constante de gas específica. Para gas ideal perfecto: $Z=1$. Las desviaciones $Z\neq1$ miden las interacciones intermoleculares.

> [!proposicion] Condición para usar gas ideal
> El vapor puede tratarse como gas ideal cuando $P_r = P/P_c \ll 1$ (baja presión reducida) o cuando $T_r = T/T_c \gg 1$ (alta temperatura reducida). Regla práctica: $Z>0.99$ (error $<1\%$) cuando $P_r < 0.01$ o $T_r > 2$.

Para el agua: $P_c=22.09\,\mathrm{MPa}$, $T_c=647.3\,\mathrm{K}$, $R=0.4615\,\mathrm{kJ/(kg\cdot K)}$.

A $T=300\,°\mathrm{C}$, $P=0.1\,\mathrm{MPa}$: $P_r=0.0045$, $T_r=0.886$. Tablas dan $v=2.639\,\mathrm{m^3/kg}$; gas ideal predice $v=RT/P=0.4615\times573.15/100=2.644\,\mathrm{m^3/kg}$. Error $0.2\%$: gas ideal es excelente.

A $T=300\,°\mathrm{C}$, $P=10\,\mathrm{MPa}$: $P_r=0.453$. Tablas: $v=0.02580\,\mathrm{m^3/kg}$; gas ideal predice $0.02644\,\mathrm{m^3/kg}$. Error $2.5\%$: la aproximación empieza a fallar.

---

## Diagrama generalizado de compresibilidad

Las ecuaciones de estado reales (Van der Waals, Peng-Robinson, Redlich-Kwong) capturan las desviaciones $Z\neq1$. El **diagrama generalizado de compresibilidad** (Nelson-Obert) traza $Z$ como función de $P_r$ y $T_r$ usando el **principio de estados correspondientes**: todas las sustancias siguen aproximadamente la misma $Z(P_r,T_r,\omega)$, donde $\omega$ es el factor acéntrico.

> [!proposicion] Principio de estados correspondientes
> Dos fluidos en los mismos estados reducidos $(T_r,P_r)$ tienen aproximadamente el mismo factor $Z$, independientemente de la sustancia. Esto permite usar el diagrama generalizado cuando no se dispone de tablas específicas.

![[factor_compresibilidad_Z.svg|460]]
*Diagrama generalizado de compresibilidad $Z(P_r, T_r)$. Para $T_r>2$: $Z\approx1$ para cualquier $P_r<10$. El mínimo de $Z$ ocurre cerca de la curva de saturación y se pronuncia para $T_r$ cercanos a 1.*

---

## Ejemplo complejo: turbina de vapor con interpolación bilineal y análisis de exergía

> [!ejemplo]
> Vapor de agua entra a una turbina a $P_1=3.5\,\mathrm{MPa}$, $T_1=450\,°\mathrm{C}$ y se expande hasta la presión de condensador $P_2=10\,\mathrm{kPa}$. La turbina opera en régimen estacionario y adiabático, con $\dot{m}=20\,\mathrm{kg/s}$ y **eficiencia isentrópica $\eta_T=0.85$** (dato). La temperatura ambiente es $T_0=25\,°\mathrm{C}=298.15\,\mathrm{K}$.
>
> Determinar:
> (a) Estado 1: $h_1$, $s_1$ por interpolación bilineal en tablas.
> (b) Estado isentrópico de salida $2s$: calidad $x_{2s}$ y $h_{2s}$.
> (c) Estado real de salida 2: $h_2$, calidad $x_2$ y $s_2$ (a partir de $\eta_T$).
> (d) Potencia real $\dot{W}_T$.
> (e) Tasa de destrucción de exergía $\dot{E}_{d}$.

> [!solucion]
> **Parte (a) — Estado 1: interpolación en tablas de vapor sobrecalentado.**
>
> $T_1=450\,°\mathrm{C}$ y $P_1=3.5\,\mathrm{MPa}$. Tablas A-6 dan datos a $P=3.0\,\mathrm{MPa}$ y $P=4.0\,\mathrm{MPa}$:
>
> | $P$ (MPa) | $T$ (°C) | $h$ (kJ/kg) | $s$ (kJ/(kg·K)) |
> |:---:|:---:|:---:|:---:|
> | 3.0 | 400 | 3230.9 | 6.9212 |
> | 3.0 | 500 | 3456.5 | 7.2338 |
> | 4.0 | 400 | 3213.6 | 6.7690 |
> | 4.0 | 500 | 3445.3 | 7.0901 |
>
> Interpolación primero en $T$ (a cada $P$):
> A $P=3.0\,\mathrm{MPa}$, $T=450\,°\mathrm{C}$:
> $$h(3.0,450)=3230.9+\frac{450-400}{500-400}(3456.5-3230.9)=3230.9+0.5\times225.6=3343.7\,\mathrm{kJ/kg}.$$
> $$s(3.0,450)=6.9212+0.5\times(7.2338-6.9212)=6.9212+0.1563=7.0775\,\mathrm{kJ/(kg\cdot K)}.$$
>
> A $P=4.0\,\mathrm{MPa}$, $T=450\,°\mathrm{C}$:
> $$h(4.0,450)=3213.6+0.5\times(3445.3-3213.6)=3213.6+115.85=3329.5\,\mathrm{kJ/kg}.$$
> $$s(4.0,450)=6.7690+0.5\times(7.0901-6.7690)=6.7690+0.1606=6.9296\,\mathrm{kJ/(kg\cdot K)}.$$
>
> Interpolación en $P$ de $3.0$ a $4.0\,\mathrm{MPa}$ para $P_1=3.5\,\mathrm{MPa}$:
> $$h_1=3343.7+\frac{3.5-3.0}{4.0-3.0}(3329.5-3343.7)=3343.7+0.5\times(-14.2)=3343.7-7.1=3336.6\,\mathrm{kJ/kg}.$$
> $$s_1=7.0775+0.5\times(6.9296-7.0775)=7.0775-0.0740=7.0036\,\mathrm{kJ/(kg\cdot K)}.$$
>
> **Parte (b) — Estado isentrópico de salida $2s$ ($s_{2s}=s_1$, $P_2=10\,\mathrm{kPa}$).**
> Tabla de saturación a $P=10\,\mathrm{kPa}$: $T_{\rm sat}=45.81\,°\mathrm{C}$, $h_f=191.83\,\mathrm{kJ/kg}$, $h_{fg}=2392.8\,\mathrm{kJ/kg}$, $h_g=2584.6\,\mathrm{kJ/kg}$, $s_f=0.6493\,\mathrm{kJ/(kg\cdot K)}$, $s_{fg}=7.5009\,\mathrm{kJ/(kg\cdot K)}$, $s_g=8.1502\,\mathrm{kJ/(kg\cdot K)}$.
> Como $s_f < s_{2s}=7.0036 < s_g$, el estado isentrópico es bifásico:
> $$x_{2s}=\frac{s_{2s}-s_f}{s_{fg}}=\frac{7.0036-0.6493}{7.5009}=0.8471.$$
> $$h_{2s}=h_f+x_{2s}h_{fg}=191.83+0.8471\times2392.8=2218.9\,\mathrm{kJ/kg}.$$
>
> **Parte (c) — Estado real de salida a partir de $\eta_T$.**
> De la definición $\eta_T=(h_1-h_2)/(h_1-h_{2s})$ se despeja el salto real:
> $$h_1-h_2=\eta_T(h_1-h_{2s})=0.85\times(3336.6-2218.9)=0.85\times1117.7=950.0\,\mathrm{kJ/kg},$$
> $$h_2=3336.6-950.0=2386.6\,\mathrm{kJ/kg}.$$
> Como $h_f < h_2 < h_g$, la salida real también es bifásica; su calidad y entropía son **resultado**, no dato:
> $$x_2=\frac{h_2-h_f}{h_{fg}}=\frac{2386.6-191.83}{2392.8}=0.917,$$
> $$s_2=s_f+x_2\,s_{fg}=0.6493+0.917\times7.5009=7.529\,\mathrm{kJ/(kg\cdot K)}.$$
> La irreversibilidad eleva la calidad de salida de $x_{2s}=0.847$ a $x_2=0.917$: la expansión real disipa parte del salto entálpico y termina más seca (mayor $h_2$, mayor $s_2$) que la isentrópica.
>
> **Parte (d) — Potencia real.**
> Balance de energía (adiabático, estacionario, $\Delta\mathrm{Ec}=0$):
> $$\dot{W}_T = \dot{m}(h_1-h_2)=20\times950.0=19000\,\mathrm{kW}\approx19.0\,\mathrm{MW}.$$
>
> **Parte (e) — Destrucción de exergía.**
> Para una turbina adiabática $\dot{S}_{\rm gen}=\dot{m}(s_2-s_1)\ge0$ es obligatorio:
> $$\dot{S}_{\rm gen}=20\times(7.529-7.0036)=20\times0.5254=10.51\,\mathrm{kW/K}>0,$$
> $$\dot{E}_d = T_0\,\dot{S}_{\rm gen} = 298.15\times10.51=3133\,\mathrm{kW}\approx3.13\,\mathrm{MW}.$$
> El signo positivo de $\dot{S}_{\rm gen}$ — garantizado por $s_2>s_1$, ya que la irreversibilidad de la turbina real siempre aumenta la entropía del fluido — confirma la consistencia del estado de salida obtenido. $\blacksquare$

> [!warning]
> En tablas de vapor sobrecalentado, verificar siempre que $T > T_{\rm sat}(P)$ antes de interpolar. Si $T=T_{\rm sat}(P)$ y $x=1$: usar la fila de vapor saturado. Si $T<T_{\rm sat}(P)$ y se obtuvo una propiedad de tablas de vapor: hubo un error de lectura.

---

## Propiedades en el límite de gas ideal

Para vapor sobrecalentado a baja presión, la ecuación de estado $Pv=RT$ predice correctamente $v$. Las propiedades calóricas del gas ideal:
$$h_{\rm ig}(T) = h_{\rm ig}(T_{\rm ref}) + \int_{T_{\rm ref}}^T c_p(T')\,dT', \qquad s_{\rm ig}(T,P)=s_{\rm ig}(T_{\rm ref},P_{\rm ref})+\int_{T_{\rm ref}}^T \frac{c_p}{T'}\,dT'-R\ln\frac{P}{P_{\rm ref}}.$$

Para el agua vapor en el rango $100$–$900\,°\mathrm{C}$, $c_p$ varía de $1.87$ a $2.37\,\mathrm{kJ/(kg\cdot K)}$; el modelo de gas ideal con $c_p=$ cte no es preciso para cálculos de turbinas; se deben usar las tablas.

> [!referencia]
> Çengel & Boles, *Termodinámica*, §3-6; Moran & Shapiro §11.3; Borgnakke & Sonntag §2.8. Para el factor $Z$ y correlaciones generalizadas: Poling, Prausnitz & O'Connell, *The Properties of Gases and Liquids*, cap. 2.
