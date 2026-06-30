---
title: Carta Psicrométrica
order: 1
tags:
  - termodinamica
  - psicrometria
  - carta-psicrometrica
  - diagramas
draft: false
aliases:
  - Carta Psicrométrica
  - Diagrama Psicrométrico
---

# Carta Psicrométrica

> [!definicion]
> La **carta psicrométrica** es la representación gráfica del estado del aire húmedo a presión constante ($P = 101.325\,\mathrm{kPa}$). El eje horizontal es la **temperatura de bulbo seco** $T$ (°C) y el eje vertical es la **razón de humedad** $\omega$ (kg vapor/kg a.s.). Cada punto del plano es un **estado termodinámico completo** del aire húmedo; cada proceso HVAC es una **trayectoria** entre dos puntos.
>
> *Ventaja principal:* conocidas dos propiedades cualesquiera del aire húmedo, las cinco restantes ($T$, $\omega$, $\phi$, $T_{bh}$, $T_d$, $h$, $v$) se leen directamente en la intersección de las curvas correspondientes — sin necesidad de resolver iterativamente el sistema de ecuaciones.
>
> La carta se vuelve inútil por encima de la **curva de saturación** ($\phi=100\%$): allí el vapor condensa y el estado ya no es de "aire húmedo" sino de niebla.

![[carta_psicrometrica_estructura.svg|520]]
*Vista general de la carta psicrométrica a $P=101.325\,\mathrm{kPa}$. La curva de saturación ($\phi=100\%$) es el límite superior izquierdo. Las cinco familias de curvas se superponen en el mismo plano; cada familia tiene una forma y dirección característica.*

---

## Curvas de humedad relativa $\phi = \text{cte}$

> [!teoria]
> La ecuación de cada curva es:
> $$\omega = 0.622\,\frac{\phi\,P_{\rm sat}(T)}{P - \phi\,P_{\rm sat}(T)}.$$
>
> Como $P_{\rm sat}(T)$ crece exponencialmente con $T$ (ecuación de Clausius-Clapeyron), a $\omega$ fija la humedad relativa **disminuye al calentar**: el vapor no cambia pero el máximo posible aumenta. Por eso las curvas de $\phi = \text{cte}$ **divergen hacia la derecha** al alejarse de la curva de saturación.
>
> La curva $\phi = 0\%$ es el eje horizontal ($\omega = 0$, aire completamente seco). La curva $\phi = 100\%$ (saturación) es el límite superior: conecta los puntos de máxima humedad posible a cada $T$.

![[carta_curvas_phi.svg|460]]
*Familia de curvas $\phi = \text{cte}$: 10%, 20%, …, 100%. A mayor temperatura, las curvas se separan más entre sí porque $P_{\rm sat}$ crece más rápido.*

---

## Líneas de bulbo húmedo $T_{bh} = \text{cte}$

> [!teoria]
> Las líneas de $T_{bh}$ constante representan el proceso del **saturador adiabático**: el aire que se humidifica adiabáticamente hasta la saturación sigue una de estas líneas hasta llegar a $\phi=100\%$ en el punto $(T_{bh},\,\omega_{\rm sat}(T_{bh}))$.
>
> Su pendiente en el plano $(T,\omega)$ es negativa: al aumentar $T$ a lo largo de la misma línea de $T_{bh}$, $\omega$ disminuye (el aire estaba menos húmedo de lo que necesitaría para saturar a esa temperatura).

> [!proposicion]
> Pendiente de una línea de bulbo húmedo constante:
> $$\left.\frac{d\omega}{dT}\right|_{T_{bh}} \approx -\frac{c_{pa}}{h_{fg}(T_{bh})} \approx -\frac{1.005}{2450} \approx -4.1\times10^{-4}\,\mathrm{(kg/kg)/K}.$$

> [!demostracion]
> **Hipótesis:** aproximación lineal del balance del saturador (ver [[Psicrometria/index | Psicrometría]]).
>
> **Paso 1 — Ecuación de la línea.** Del balance del saturador adiabático:
> $$\omega = \omega_{bh} - \frac{c_{pa}}{h_{fg}(T_{bh})}(T - T_{bh}).$$
>
> **Paso 2 — Forma de línea recta.** Esta es una ecuación lineal en $T$, con $T_{bh}$, $\omega_{bh}$ y $h_{fg}(T_{bh})$ todos constantes a lo largo de la línea. Tiene la forma $\omega = A - B\cdot T$ con $B = c_{pa}/h_{fg}(T_{bh}) > 0$.
>
> **Paso 3 — Pendiente.** Diferenciando a $T_{bh} = \text{cte}$:
> $$\frac{d\omega}{dT} = -\frac{c_{pa}}{h_{fg}(T_{bh})}.$$
>
> **Paso 4 — Valor numérico.** Con $c_{pa} = 1.005\,\mathrm{kJ/(kg\cdot K)}$ y $h_{fg}(T_{bh}) \approx 2450\,\mathrm{kJ/kg}$ (rango 15–30°C):
> $$\frac{d\omega}{dT} = -1.005/2450 = -4.1\times10^{-4}\,\mathrm{(kg\,vapor/kg\,a.s.)/K}.$$
>
> **Paso 5 — Por qué son casi rectas.** $h_{fg}$ varía poco en el rango de confort (2430 a 2450 kJ/kg entre 15 y 30°C): la pendiente es casi constante, lo que hace que las líneas de $T_{bh}$ sean casi rectas en la carta. $\blacksquare$

![[carta_curvas_Tbh.svg|460]]
*Familia de líneas $T_{bh} = \text{cte}$: casi paralelas, pendiente negativa, convergiendo en la curva de saturación. Cada línea intersecta $\phi=100\%$ exactamente en el punto $(T_{bh},\,\omega_{\rm sat}(T_{bh}))$.*

---

## Líneas de entalpía $h = \text{cte}$

> [!teoria]
> La entalpía del aire húmedo:
> $$h = (1.005 + 1.86\,\omega)\,T + 2501\,\omega.$$
>
> Las líneas de $h = \text{cte}$ en el plano $(T,\omega)$ tienen pendiente:
> $$\left.\frac{d\omega}{dT}\right|_h = -\frac{1.005 + 1.86\,\omega}{2501 + 1.86\,T}.$$
>
> Esta pendiente es **ligeramente más negativa** que la de $T_{bh} = \text{cte}$. Por eso, en la carta psicrométrica, las líneas de $h$ y las de $T_{bh}$ son casi paralelas pero no idénticas. En ingeniería de confort se usan como equivalentes con error < 2%.
>
> La escala de $h$ se imprime en el borde de la curva de saturación; cada línea de $h = \text{cte}$ parte de ese borde y tiene pendiente ligeramente más pronunciada que la de $T_{bh}$ correspondiente.

![[carta_curvas_h.svg|460]]
*Líneas de entalpía constante $h = \text{cte}$ (kJ/kg a.s.). Casi paralelas a las de $T_{bh}$; se leen en la escala del borde izquierdo.*

---

## Líneas de temperatura de rocío $T_d = \text{cte}$

> [!teoria]
> A $T_d$ constante, $P_v = P_{\rm sat}(T_d)$ es constante. Como $\omega = 0.622\,P_v/(P-P_v)$, también $\omega$ es constante. Las líneas de $T_d = \text{cte}$ son **horizontales** ($\omega = \text{cte}$) en el plano $(T,\omega)$.
>
> Para leer $T_d$ desde la carta: trazar una horizontal desde el estado hacia la izquierda hasta la curva $\phi=100\%$; la abscisa en ese punto es $T_d$.

---

## Líneas de volumen específico $v = \text{cte}$

> [!teoria]
> El volumen específico por kg de aire seco:
> $$v = \frac{R_a\,T}{P - P_v} = \frac{0.2870\,(T+273.15)}{P - \omega P/(0.622+\omega)} \quad [\mathrm{m^3/kg\,a.s.}].$$
>
> Las líneas de $v = \text{cte}$ tienen **pendiente positiva leve** en el plano $(T,\omega)$: al calentar el aire ($T\uparrow$) a $v$ fijo, el volumen se mantiene disminuyendo $\omega$ (menos vapor). Son esenciales para convertir caudales másicos a volumétricos en diseño de ductos y ventiladores.

---

## Lectura del estado desde dos propiedades

> [!proposicion]
> Las dos combinaciones más comunes en práctica:
>
> **Par $(T,\phi)$** — más frecuente en campo (termómetro + higrómetro):
> 1. Localizar $T$ en el eje horizontal.
> 2. Subir verticalmente hasta la curva $\phi = \text{cte}$ → punto de estado.
> 3. Leer $\omega$ en el eje vertical.
> 4. Trazar horizontal hasta $\phi=100\%$ → $T_d$ en el eje horizontal.
> 5. Interpolar entre líneas de $T_{bh}$ → $T_{bh}$.
> 6. Interpolar entre líneas de $h$ → $h$.
>
> **Par $(T, T_{bh})$** — psicrómetro de Assmann (mide bulbo seco y húmedo directamente):
> 1. Localizar $T_{bh}$ en el eje horizontal y subir hasta $\phi=100\%$ → punto ancla.
> 2. Seguir la línea $T_{bh} = \text{cte}$ hasta $T$ → punto de estado.
> 3. Leer $\omega$, $\phi$, $T_d$, $h$ como antes.

![[carta_lectura_T_phi.svg|480]]
*Localización del estado $(T=28\,°\mathrm{C},\,\phi=60\%)$. Desde el punto se trazan la horizontal (→ $T_d$), la oblicua de $T_{bh}$, y la oblicua de $h$.*

---

## Ejemplo: lectura de tres estados en la carta

> [!ejemplo]
> Localizar y calcular todas las propiedades de los estados:
>
> | Estado | Dato 1 | Dato 2 |
> |:---:|:---:|:---:|
> | A | $T=20\,°\mathrm{C}$ | $\phi=50\%$ |
> | B | $T=35\,°\mathrm{C}$ | $T_{bh}=25\,°\mathrm{C}$ |
> | C | $T=15\,°\mathrm{C}$ | $\omega=0.010\,\mathrm{kg/kg}$ |

> [!solucion]
> **Estado A** ($T=20\,°\mathrm{C}$, $\phi=50\%$).
>
> $P_{\rm sat}(20) = 2.338\,\mathrm{kPa}$; $P_v = 0.50\times2.338 = 1.169\,\mathrm{kPa}$.
>
> $\omega_A = 0.622\times1.169/(101.325-1.169) = 0.622\times1.169/100.156 = 0.00726\,\mathrm{kg/kg}$.
>
> $h_A = (1.005+1.86\times0.00726)\times20 + 2501\times0.00726 = 1.0185\times20+18.15 = 20.37+18.15 = 38.5\,\mathrm{kJ/kg}$.
>
> $T_{d,A}$: $P_{\rm sat}(T_d)=1.169\,\mathrm{kPa}$ → $T_{d,A} \approx 9.3\,°\mathrm{C}$.
>
> $v_A = 0.2870\times293.15/(101.325-1.169) = 84.13/100.16 = 0.8400\,\mathrm{m^3/kg\,a.s.}$
>
> **Estado B** ($T=35\,°\mathrm{C}$, $T_{bh}=25\,°\mathrm{C}$).
>
> $P_{\rm sat}(25) = 3.170\,\mathrm{kPa}$; $\omega_{bh} = 0.622\times3.170/(101.325-3.170) = 0.02011\,\mathrm{kg/kg}$.
>
> $h_{fg}(25) \approx 2442\,\mathrm{kJ/kg}$.
>
> $\omega_B = 0.02011 - 1.005\times(35-25)/2442 = 0.02011-0.004115 = 0.01600\,\mathrm{kg/kg}$.
>
> $P_{v,B} = 0.01600\times101.325/0.638 = 2.542\,\mathrm{kPa}$; $\phi_B = 2.542/P_{\rm sat}(35) = 2.542/5.629 = 45.2\%$.
>
> $h_B = (1.005+1.86\times0.01600)\times35+2501\times0.01600 = 1.03476\times35+40.02 = 76.2\,\mathrm{kJ/kg}$.
>
> **Estado C** ($T=15\,°\mathrm{C}$, $\omega=0.010\,\mathrm{kg/kg}$).
>
> $P_v = 0.010\times101.325/0.632 = 1.603\,\mathrm{kPa}$; $\phi_C = 1.603/1.706 = 93.9\%$.
>
> $T_{d,C}$: $P_{\rm sat}(T_d)=1.603\,\mathrm{kPa}$ → $T_{d,C} \approx 14.0\,°\mathrm{C}$ (cerca de $T$, confirma $\phi$ alta).
>
> $h_C = (1.005+1.86\times0.010)\times15+2501\times0.010 = 1.0236\times15+25.01 = 40.4\,\mathrm{kJ/kg}$.
>
> $\boxed{h_A=38.5,\quad h_B=76.2,\quad h_C=40.4\;\mathrm{kJ/kg\,a.s.}}$ $\blacksquare$

> [!warning]
> La carta psicrométrica estándar es válida solo a $P=101.325\,\mathrm{kPa}$. En ciudades de altitud elevada ($P \approx 85\,\mathrm{kPa}$ a 1500 m) el mismo $\omega$ corresponde a una humedad relativa diferente: usar las ecuaciones directamente con $P$ local o una carta a la presión correcta.

> [!referencia]
> Çengel & Boles, §14-2 a 14-3; ASHRAE Fundamentals Handbook, cap. 1; Moran & Shapiro, §12.5.
