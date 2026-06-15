---
title: Carta Psicrométrica
tags:
  - termodinamica
  - teoria
  - psicrometria
  - carta-psicrometrica
  - diagramas
draft: false
aliases:
  - Carta Psicrométrica
  - Diagrama Psicrométrico
  - Carta de Mollier Aire Húmedo
---

# Carta Psicrométrica

> [!definicion]
> La **carta psicrométrica** (diagrama de Mollier para aire húmedo) es la representación gráfica del estado termodinámico del aire húmedo a presión constante ($P=101.325\,\mathrm{kPa}$). Los ejes son la **temperatura de bulbo seco** $T$ (abscisa) y la **razón de humedad** $\omega$ (ordenada). El estado de un aire húmedo determinado queda como un **punto** en el plano; todo proceso psicrométrico es una **trayectoria** entre dos puntos. La carta condensa en un solo gráfico las cinco propiedades $\{T,\,\omega,\,\phi,\,h,\,T_{bh}\}$: conocidas dos de ellas, las tres restantes se leen directamente.

---

## Estructura general de la carta

> [!teoria] Ejes y región válida
> La carta psicrométrica estándar (ASHRAE, a $P=101.325\,\mathrm{kPa}$) cubre:
> - **Eje horizontal ($x$):** temperatura de bulbo seco $T$ en el rango $0$–$50\,°\mathrm{C}$ (confort) o hasta $120\,°\mathrm{C}$ (alta temperatura).
> - **Eje vertical ($y$):** razón de humedad $\omega$ en $\mathrm{kg\,vapor/kg\,a.s.}$, de $0$ a $\approx0.030$.
> - **Límite superior:** la curva de saturación ($\phi=100\%$), que marca el máximo $\omega$ posible a cada $T$. Por encima de ella el vapor condensa: estado de niebla, no de aire húmedo.
> - **Región útil:** toda el área por debajo y a la derecha de la curva de saturación.

![[carta_psicrometrica_estructura.svg|520]]
*Vista general de la carta psicrométrica. La curva de saturación ($\phi=100\%$, línea curva gruesa izquierda) cierra la región útil por arriba. Los ejes $T$ y $\omega$ son las coordenadas del estado. Las cinco familias de curvas se superponen en el mismo plano.*

---

## Las cinco familias de curvas

> [!teoria] Curvas de humedad relativa $\phi=\text{cte}$
> Cada curva de humedad relativa constante conecta los estados con la misma fracción $P_v/P_{\rm sat}(T)$. Al aumentar $T$ a $\omega$ fija, $P_{\rm sat}$ crece pero $P_v$ no cambia, por lo que $\phi$ disminuye: las curvas de $\phi=\text{cte}$ se alejan de la curva de saturación hacia la derecha. La curva $\phi=50\%$ es la condición de confort estándar en climatización; la $\phi=0\%$ coincide con el eje horizontal ($\omega=0$, aire completamente seco).
>
> $$\omega = 0.622\,\frac{\phi\,P_{\rm sat}(T)}{P-\phi\,P_{\rm sat}(T)}.$$
>
> ![[carta_curvas_phi.svg|460]]
> *Familia de curvas $\phi=\text{cte}$: de $10\%$ a $100\%$ en incrementos de $10\%$. Todas arrancan del origen y divergen hacia la derecha porque $P_{\rm sat}(T)$ crece exponencialmente con $T$.*

> [!teoria] Curvas de temperatura de bulbo húmedo $T_{bh}=\text{cte}$
> Las líneas de $T_{bh}$ constante son las líneas de proceso del **saturador adiabático**: el aire que se humidifica adiabáticamente hasta la saturación sigue una de estas líneas y llega a la curva $\phi=100\%$ en el punto $(T_{bh},\,\omega_{\rm sat}(T_{bh}))$. En la carta estándar estas líneas son casi rectas con **pendiente negativa** (a medida que $T$ aumenta, $\omega$ disminuye a lo largo de la misma línea de $T_{bh}$).
>
> La pendiente aproximada de una línea $T_{bh}=\text{cte}$ en el plano $(T,\omega)$:
> $$\left.\frac{d\omega}{dT}\right|_{T_{bh}} \approx -\frac{c_{pa}}{h_{fg}(T_{bh})} \approx -\frac{1.005}{2450} \approx -4.1\times10^{-4}\,\mathrm{(kg/kg)/K}.$$
>
> ![[carta_curvas_Tbh.svg|460]]
> *Familia de líneas $T_{bh}=\text{cte}$: casi paralelas, con pendiente negativa, convergiendo en la curva de saturación. El punto de intersección de cada línea con $\phi=100\%$ es exactamente $(T_{bh},\,\omega_{\rm sat}(T_{bh}))$.*

> [!demostracion] Pendiente de la línea de bulbo húmedo
> Del balance del saturador adiabático ([[index | Psicrometría]]):
> $$\omega = \omega_{bh} - \frac{c_{pa}(T-T_{bh})}{h_{fg}(T_{bh})}.$$
> Diferenciando a $T_{bh}=\text{cte}$:
> $$\frac{d\omega}{dT} = -\frac{c_{pa}}{h_{fg}(T_{bh})}.$$
> Con $c_{pa}=1.005\,\mathrm{kJ/(kg\cdot K)}$ y $h_{fg}\approx2450\,\mathrm{kJ/kg}$ en el rango $15$–$30\,°\mathrm{C}$:
> $$\frac{d\omega}{dT}\approx-\frac{1.005}{2450}=-4.1\times10^{-4}\,\mathrm{(kg\,vapor/kg\,a.s.)/K.} \qquad \blacksquare$$
> Las líneas de $T_{bh}$ son casi rectas porque $h_{fg}$ varía poco en el rango de confort.

> [!teoria] Líneas de entalpía $h=\text{cte}$
> La entalpía del aire húmedo por kg de aire seco:
> $$h = c_{pa}\,T + \omega\,(h_{fg,0}+c_{pv}\,T) = (1.005+1.86\,\omega)\,T + 2501\,\omega.$$
> Las líneas de $h=\text{cte}$ en el plano $(T,\omega)$ tienen pendiente:
> $$\left.\frac{d\omega}{dT}\right|_{h} = -\frac{1.005+1.86\,\omega}{h_{fg,0}+c_{pv}\,T} \approx -\frac{1.005}{2501+1.86\,T}.$$
> Esta pendiente es **ligeramente más negativa** que la de $T_{bh}=\text{cte}$. Por eso, en la carta, las líneas de $h$ y las de $T_{bh}$ son casi paralelas pero no idénticas: la escala de entalpía se imprime usualmente en el borde de la curva de saturación, y las líneas de $h=\text{cte}$ se prolongan desde allí con una ligera divergencia respecto a las de $T_{bh}$.
>
> ![[carta_curvas_h.svg|460]]
> *Líneas de entalpía constante $h=\text{cte}$ (kJ/kg a.s.), casi paralelas a las de $T_{bh}$. La escala de $h$ se lee en el borde izquierdo (curva de saturación). A efectos prácticos de ingeniería de confort, $h=\text{cte}$ y $T_{bh}=\text{cte}$ se usan como equivalentes (error $<2\%$).*

> [!teoria] Líneas de temperatura de rocío $T_d=\text{cte}$
> A $T_d$ constante, la presión parcial del vapor $P_v=P_{\rm sat}(T_d)$ es fija, y como $\omega=0.622\,P_v/(P-P_v)$, también lo es $\omega$. Las **líneas de $T_d=\text{cte}$ son horizontales** ($\omega=\text{cte}$) en el plano $(T,\omega)$. Cada horizontal cruza la curva de saturación en el punto $T=T_d$, que es el estado al que el aire llegaría si se enfriara sin cambiar $\omega$.
>
> ![[carta_lineas_Td.svg|380]]
> *Las líneas de $T_d=\text{cte}$ son horizontales ($\omega=\text{cte}$). La temperatura de rocío se lee en la curva de saturación: trazar horizontal desde el estado hasta $\phi=100\%$ y leer la abscisa.*

> [!teoria] Líneas de volumen específico $v=\text{cte}$
> El volumen específico del aire húmedo por kg de aire seco:
> $$v = \frac{R_a\,T}{P-P_v} = \frac{(R_u/M_a)\,T}{P-\omega\,P/(0.622+\omega)}.$$
> Las líneas de $v=\text{cte}$ tienen **pendiente positiva** en el plano $(T,\omega)$: a mayor $T$ se necesita menor $\omega$ para mantener el mismo $v$. Son las menos visibles en la carta estándar de confort, pero son esenciales para calcular caudales volumétricos $\dot{V}=\dot{m}_a\,v$.

---

## Lectura del estado en la carta

> [!proposicion] Determinación completa del estado a partir de dos variables conocidas
> El estado del aire húmedo queda completamente determinado por **dos propiedades independientes**. Las combinaciones más frecuentes en ingeniería son:

> [!teoria] Par $(T,\,\phi)$ — el más común en campo
> 1. Localizar $T$ en el eje horizontal.
> 2. Seguir verticalmente hasta la curva $\phi=\text{cte}$ dada → punto de estado.
> 3. Leer $\omega$ en el eje vertical.
> 4. Seguir horizontal hasta $\phi=100\%$ → leer $T_d$ en el eje horizontal.
> 5. Interpolar entre líneas de $T_{bh}$ → leer $T_{bh}$.
> 6. Interpolar entre líneas de $h$ → leer $h$.
> 7. Interpolar entre líneas de $v$ → leer $v$.
>
> ![[carta_lectura_T_phi.svg|480]]
> *Localización de un estado dado $(T=28\,°\mathrm{C},\,\phi=60\%)$. Desde el punto se trazan: horizontal (→ $T_d$ en $\phi=100\%$), oblicua de $T_{bh}$ (→ $T_{bh}$ en $\phi=100\%$), oblicua de $h$ (→ $h$ en la escala del borde).*

> [!teoria] Par $(T,\,T_{bh})$ — el más común en medición directa
> El psicrómetro de Assmann mide directamente $T$ (bulbo seco) y $T_{bh}$ (bulbo húmedo).
> 1. Trazar vertical desde $T_{bh}$ hasta $\phi=100\%$ → punto $(T_{bh},\,\omega_{\rm sat}(T_{bh}))$ sobre la curva de saturación.
> 2. Seguir la línea $T_{bh}=\text{cte}$ hasta la temperatura de bulbo seco $T$ → punto de estado.
> 3. Leer $\omega$, $\phi$, $T_d$, $h$, $v$ como en el caso anterior.
>
> ![[carta_lectura_T_Tbh.svg|480]]
> *Determinación del estado desde $(T,T_{bh})$: el punto en la curva de saturación actúa como ancla de la línea de bulbo húmedo.*

---

## Validez y limitaciones

> [!warning]
> La carta psicrométrica estándar es válida solo a $P=101.325\,\mathrm{kPa}$. Para aplicaciones a altitud (p. ej. $P=85\,\mathrm{kPa}$ en Ciudad de México, $2240\,\mathrm{m}$) debe usarse una carta a la presión local o calcular directamente con las ecuaciones:
> - $\omega=0.622\,P_v/(P-P_v)$ con $P$ local.
> - $\phi=P_v/P_{\rm sat}(T)$ sin cambio (no depende de $P$).
> - $h=(1.005+1.86\,\omega)T+2501\,\omega$ sin cambio (propiedad intensiva de masa).
> A menor $P$, el aire puede contener más humedad absoluta ($\omega$ más alto) a la misma $T$ y $\phi$, porque $P-P_v$ es menor.

> [!info]
> **Carta de alta temperatura.** Para procesos industriales ($T>60\,°\mathrm{C}$, p. ej. secadores) existen cartas extendidas hasta $120\,°\mathrm{C}$ o $200\,°\mathrm{C}$. La forma de las curvas es la misma; cambia la escala y los valores de $\omega$ máximo aumentan considerablemente.

---

## Ejemplo: localización de tres estados en la carta

> [!ejemplo]
> Localizar en la carta psicrométrica los siguientes estados del aire a $P=101.325\,\mathrm{kPa}$ y leer todas sus propiedades:
>
> | Estado | Dato 1 | Dato 2 |
> |:---:|:---:|:---:|
> | A | $T=20\,°\mathrm{C}$ | $\phi=50\%$ |
> | B | $T=35\,°\mathrm{C}$ | $T_{bh}=25\,°\mathrm{C}$ |
> | C | $T=15\,°\mathrm{C}$ | $\omega=0.010\,\mathrm{kg/kg}$ |

> [!solucion]
> **Estado A** ($T=20\,°\mathrm{C}$, $\phi=50\%$).
>
> $P_{\rm sat}(20)=2.338\,\mathrm{kPa}$; $P_v=0.50\times2.338=1.169\,\mathrm{kPa}$.
> $$\omega_A=0.622\times\frac{1.169}{101.325-1.169}=0.622\times\frac{1.169}{100.156}=0.00726\,\mathrm{kg/kg}.$$
> $$h_A=(1.005+1.86\times0.00726)\times20+2501\times0.00726=1.01851\times20+18.15=20.37+18.15=38.52\,\mathrm{kJ/kg}.$$
> $T_{d,A}$: $P_{\rm sat}(T_d)=1.169\,\mathrm{kPa}\implies T_{d,A}\approx9.3\,°\mathrm{C}$ (de tablas interpolando).
> $T_{bh,A}\approx14.0\,°\mathrm{C}$ (de carta o iteración en la ecuación del saturador).
> $v_A=0.2870\times293.15/(101.325-1.169)=84.134/100.156=0.8400\,\mathrm{m^3/kg\,a.s.}$
>
> **Estado B** ($T=35\,°\mathrm{C}$, $T_{bh}=25\,°\mathrm{C}$).
>
> $P_{\rm sat}(25)=3.170\,\mathrm{kPa}$; $\omega_{bh}=0.622\times3.170/(101.325-3.170)=0.622\times3.170/98.155=0.02011\,\mathrm{kg/kg}$.
> $h_{fg}(25)\approx2442\,\mathrm{kJ/kg}$.
> $$\omega_B=\omega_{bh}-\frac{c_{pa}(T-T_{bh})}{h_{fg}(T_{bh})}=0.02011-\frac{1.005\times(35-25)}{2442}=0.02011-\frac{10.05}{2442}=0.02011-0.004115=0.01600\,\mathrm{kg/kg}.$$
> $P_v=\omega_B\times P/(0.622+\omega_B)=0.01600\times101.325/0.638=2.542\,\mathrm{kPa}$.
> $\phi_B=2.542/P_{\rm sat}(35)=2.542/5.629=0.452=45.2\%$.
> $T_{d,B}$: $P_{\rm sat}(T_d)=2.542\,\mathrm{kPa}\implies T_{d,B}\approx21.0\,°\mathrm{C}$.
> $h_B=(1.005+1.86\times0.01600)\times35+2501\times0.01600=(1.005+0.02976)\times35+40.02=1.03476\times35+40.02=36.22+40.02=76.24\,\mathrm{kJ/kg}$.
>
> **Estado C** ($T=15\,°\mathrm{C}$, $\omega=0.010\,\mathrm{kg/kg}$).
>
> $P_v=0.010\times101.325/(0.622+0.010)=1.013/0.632=1.603\,\mathrm{kPa}$.
> $\phi_C=P_v/P_{\rm sat}(15)=1.603/1.706=93.9\%$.
> $T_{d,C}$: $P_{\rm sat}(T_d)=1.603\,\mathrm{kPa}\implies T_{d,C}\approx14.0\,°\mathrm{C}$ (muy cerca de $T$, confirma $\phi$ alta).
> $h_C=(1.005+1.86\times0.010)\times15+2501\times0.010=(1.005+0.0186)\times15+25.01=1.0236\times15+25.01=15.354+25.01=40.36\,\mathrm{kJ/kg}$.
>
> ![[carta_tres_estados_ABC.svg|480]]
> *Los tres estados A, B y C en la carta psicrométrica. A: confort estándar (bajo $\omega$, $\phi=50\%$). B: clima tropical húmedo (alto $\omega$ y $T$). C: frío húmedo (cerca de la curva de saturación). Las líneas de $T_{bh}$ permiten leer $h$ y relacionar estados.*

> [!referencia]
> Çengel & Boles, *Termodinámica*, §14-2 a 14-3; ASHRAE *Fundamentals Handbook* cap. 1 (carta psicrométrica y tablas de aire húmedo); Moran & Shapiro §12.5.
