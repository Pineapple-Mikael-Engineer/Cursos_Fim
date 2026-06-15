---
title: Vapor Sobrecalentado
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
> Vapor de agua entra a una turbina a $P_1=3.5\,\mathrm{MPa}$, $T_1=450\,°\mathrm{C}$. Sale a $P_2=0.2\,\mathrm{MPa}$ con calidad $x_2=0.95$ (mezcla bifásica). La turbina opera en régimen estacionario con $\dot{m}=20\,\mathrm{kg/s}$. La temperatura ambiente es $T_0=25\,°\mathrm{C}=298.15\,\mathrm{K}$, $P_0=100\,\mathrm{kPa}$.
>
> Determinar:
> (a) Estado 1: $h_1$, $s_1$ por interpolación bilineal en tablas.
> (b) Estado 2: $h_2$, $s_2$.
> (c) Potencia real $\dot{W}_T$.
> (d) Eficiencia isentrópica $\eta_T$.
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
> **Parte (b) — Estado 2: mezcla bifásica a $P_2=0.2\,\mathrm{MPa}$, $x_2=0.95$.**
> Tabla A-5 a $P=0.2\,\mathrm{MPa}$: $T_{\rm sat}=120.23\,°\mathrm{C}$, $h_f=504.7\,\mathrm{kJ/kg}$, $h_{fg}=2201.6\,\mathrm{kJ/kg}$, $h_g=2706.3\,\mathrm{kJ/kg}$, $s_f=1.5301\,\mathrm{kJ/(kg\cdot K)}$, $s_{fg}=5.5970\,\mathrm{kJ/(kg\cdot K)}$.
> $$h_2=504.7+0.95\times2201.6=504.7+2091.5=2596.2\,\mathrm{kJ/kg}.$$
> $$s_2=1.5301+0.95\times5.5970=1.5301+5.3172=6.847\,\mathrm{kJ/(kg\cdot K)}.$$
>
> **Parte (c) — Potencia real.**
> Balance de energía (adiabático, estado estacionario, $\Delta\mathrm{Ec}=0$):
> $$\dot{W}_T = \dot{m}(h_1-h_2)=20\times(3336.6-2596.2)=20\times740.4=14808\,\mathrm{kW}\approx14.81\,\mathrm{MW}.$$
>
> **Parte (d) — Eficiencia isentrópica.**
> El estado isentrópico $2s$: $s_{2s}=s_1=7.0036\,\mathrm{kJ/(kg\cdot K)}$, $P_{2s}=0.2\,\mathrm{MPa}$.
> Verificar si $2s$ es bifásico: $s_f=1.5301$, $s_g=s_f+s_{fg}=7.1271\,\mathrm{kJ/(kg\cdot K)}$. Como $s_f < s_{2s} < s_g$, el estado $2s$ es bifásico.
> $$x_{2s}=\frac{s_{2s}-s_f}{s_{fg}}=\frac{7.0036-1.5301}{5.5970}=\frac{5.4735}{5.5970}=0.9779.$$
> $$h_{2s}=504.7+0.9779\times2201.6=504.7+2152.1=2656.8\,\mathrm{kJ/kg}.$$
> $$\eta_T=\frac{h_1-h_2}{h_1-h_{2s}}=\frac{3336.6-2596.2}{3336.6-2656.8}=\frac{740.4}{679.8}=1.089.$$
>
> $\eta_T > 1$: imposible — indica que el estado real 2 ($x_2=0.95$, $h_2=2596.2$) es **más húmedo** que el isentrópico ($x_{2s}=0.978$, $h_{2s}=2656.8$). Esto significa que la expansión real produce más humedad que la isentrópica, lo cual es termodinámicamente posible en presencia de irreversibilidades que favorecen la condensación (efectos de enfriamiento local). En la práctica, $\eta_T > 1$ suele indicar un error en el planteo o en los datos. Si el estado real tuviera $h_2>h_{2s}$ (mayor temperatura final), la eficiencia sería $<1$ como siempre. El ejemplo sirve para resaltar que la calidad $x_2$ debe verificarse con $s_1$.
>
> **Replanteando:** si $x_2$ fuera $x_2=0.90$: $h_2=504.7+0.90\times2201.6=504.7+1981.4=2486.1\,\mathrm{kJ/kg}$, $\dot{W}_T=20\times(3336.6-2486.1)=17010\,\mathrm{kW}$, $\eta_T=(3336.6-2486.1)/(3336.6-2656.8)=850.5/679.8=1.25$: aún $>1$, lo que indica que en el ciclo con esas condiciones la turbina real produce más trabajo que la isentrópica. La única salida consistente es tomar $x_2$ como resultado del cálculo (no como dato), y obtenerla de $h_2=h_1-\dot{W}_T/\dot{m}$ con $\eta_T<1$ dado.
>
> **Parte (e) — Destrucción de exergía.**
> Para el caso $x_2=0.95$, $s_2=6.847\,\mathrm{kJ/(kg\cdot K)}$:
> $$\dot{E}_d = T_0\,\dot{S}_{\rm gen} = T_0\,\dot{m}(s_2-s_1) = 298.15\times20\times(6.847-7.004).$$
> $s_2-s_1=6.847-7.004=-0.157\,\mathrm{kJ/(kg\cdot K)}<0$: la entropía del fluido disminuye, lo que implica $\dot{S}_{\rm gen}<0$ como si fuera un proceso con extracción de calor. Para una turbina adiabática, $\dot{S}_{\rm gen}=\dot{m}(s_2-s_1)\ge0$ es obligatorio. El resultado negativo confirma la inconsistencia del estado 2 con el estado 1 dado. En diseño real, $s_2\ge s_1$ siempre para una turbina adiabática. $\blacksquare$

> [!warning]
> En tablas de vapor sobrecalentado, verificar siempre que $T > T_{\rm sat}(P)$ antes de interpolar. Si $T=T_{\rm sat}(P)$ y $x=1$: usar la fila de vapor saturado. Si $T<T_{\rm sat}(P)$ y se obtuvo una propiedad de tablas de vapor: hubo un error de lectura.

---

## Propiedades en el límite de gas ideal

Para vapor sobrecalentado a baja presión, la ecuación de estado $Pv=RT$ predice correctamente $v$. Las propiedades calóricas del gas ideal:
$$h_{\rm ig}(T) = h_{\rm ig}(T_{\rm ref}) + \int_{T_{\rm ref}}^T c_p(T')\,dT', \qquad s_{\rm ig}(T,P)=s_{\rm ig}(T_{\rm ref},P_{\rm ref})+\int_{T_{\rm ref}}^T \frac{c_p}{T'}\,dT'-R\ln\frac{P}{P_{\rm ref}}.$$

Para el agua vapor en el rango $100$–$900\,°\mathrm{C}$, $c_p$ varía de $1.87$ a $2.37\,\mathrm{kJ/(kg\cdot K)}$; el modelo de gas ideal con $c_p=$ cte no es preciso para cálculos de turbinas; se deben usar las tablas.

> [!referencia]
> Çengel & Boles, *Termodinámica*, §3-6; Moran & Shapiro §11.3; Borgnakke & Sonntag §2.8. Para el factor $Z$ y correlaciones generalizadas: Poling, Prausnitz & O'Connell, *The Properties of Gases and Liquids*, cap. 2.
