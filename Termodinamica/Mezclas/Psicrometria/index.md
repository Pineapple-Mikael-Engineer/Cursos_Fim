---
title: Psicrometría
order: 1
tags:
  - termodinamica
  - mezclas
  - psicrometria
  - aire-humedo
  - index
draft: false
aliases:
  - Psicrometría
  - Aire Húmedo
  - Psychrometrics
---

# Psicrometría

> [!definicion]
> La **psicrometría** estudia las propiedades termodinámicas del **aire húmedo**: la mezcla binaria de **aire seco** y **vapor de agua**. El aire seco se modela como gas ideal con $M_a = 28.97\,\mathrm{kg/kmol}$; el vapor de agua también se modela como gas ideal con $M_v = 18.015\,\mathrm{kg/kmol}$, pero es **condensable**: puede pasar a líquido si la temperatura baja suficientemente.
>
> *¿Por qué el vapor cambia todo?* A diferencia de los gases permanentes del aire (N₂, O₂, Ar), el vapor de agua puede condensar o evaporarse durante un proceso, liberando o absorbiendo el **calor latente de vaporización** ($h_{fg} \approx 2500\,\mathrm{kJ/kg}$ a temperatura ambiente). Este calor latente domina los balances energéticos en climatización, torres de enfriamiento y secadores industriales.
>
> El estado del aire húmedo queda fijado por **tres variables independientes**: $T$, $P$ y la composición (expresada como razón de humedad $\omega$, humedad relativa $\phi$, o temperatura de rocío $T_d$). Conocidas dos de ellas, la tercera y todas las propiedades derivadas quedan determinadas.

![[diagrama_psicrometrico.svg|500]]
*Carta psicrométrica a $P=101.325\,\mathrm{kPa}$. Cada punto es un estado del aire húmedo. Las cinco familias de curvas permiten leer $\omega$, $\phi$, $T_d$, $T_{bh}$, $h$ y $v$ conocidas dos propiedades. Para lectura detallada ver [[Carta Psicrometrica]].*

---

## Razón de humedad $\omega$

> [!definicion]
> La **razón de humedad** (o razón de mezcla) $\omega$ es la masa de vapor de agua por unidad de masa de **aire seco**:
> $$\omega \equiv \frac{m_v}{m_a} \quad [\mathrm{kg\,vapor/kg\,a.s.}].$$
>
> *¿Por qué normalizar por aire seco y no por la mezcla?* Porque en la mayoría de los procesos psicrométricos el aire seco no cambia de cantidad (es conservativo), pero el vapor sí entra o sale. Al usar $m_a$ como referencia, todos los balances se simplifican: el flujo de referencia es $\dot{m}_a$ (constante), y los cambios en $\omega$ miden directamente cuánto vapor se añadió o retiró.

> [!teorema]
> La razón de humedad en función de las presiones parciales:
> $$\boxed{\omega = 0.622\,\frac{P_v}{P - P_v}}.$$

> [!demostracion]
> **Hipótesis:** aire seco y vapor de agua, ambos modelados como gases ideales; ley de Dalton: $P = P_a + P_v$.
>
> **Paso 1 — Expresar $\omega$ en función de moles.** Por definición:
> $$\omega = \frac{m_v}{m_a} = \frac{n_v M_v}{n_a M_a}.$$
>
> **Paso 2 — Fracción de moles desde la ley de Dalton.** Para gases ideales en la misma mezcla a $(T, V)$: $P_i V = n_i R_u T$. Dividiendo:
> $$\frac{n_v}{n_a} = \frac{P_v}{P_a}.$$
>
> **Paso 3 — Sustituir en $\omega$:**
> $$\omega = \frac{P_v}{P_a}\cdot\frac{M_v}{M_a} = \frac{P_v}{P_a}\cdot\frac{18.015}{28.97} = 0.6220\,\frac{P_v}{P_a}.$$
>
> **Paso 4 — Usar $P_a = P - P_v$:**
> $$\omega = 0.622\,\frac{P_v}{P - P_v}.$$
>
> **Paso 5 — Despejar $P_v$** (útil para el análisis de la carta):
> $$P_v = \frac{\omega\,P}{0.622 + \omega}.$$
>
> Verificación: si $\omega = 0$ (aire seco), $P_v = 0$ ✓. Si $\omega \to \infty$ (solo vapor), $P_v \to P$ ✓. $\blacksquare$

---

## Humedad relativa $\phi$

> [!definicion]
> La **humedad relativa** compara la presión parcial del vapor con la presión de saturación a la misma temperatura:
> $$\phi \equiv \frac{P_v}{P_{\rm sat}(T)} \in [0,\,1].$$
>
> *Interpretación:* $\phi = 1$ (100%) significa que el vapor está en saturación; cualquier enfriamiento adicional causará condensación. $\phi = 0.5$ (50%) significa que hay la mitad del vapor que podría haber a esa $T$. $\phi$ mide la "capacidad restante para absorber humedad" — a $\phi$ bajo, el aire puede evaporar agua rápidamente (buena condición para secar ropa).
>
> Relación entre $\phi$, $\omega$ y $T$ (combinando las definiciones):
> $$\omega = 0.622\,\frac{\phi\,P_{\rm sat}(T)}{P - \phi\,P_{\rm sat}(T)}.$$

---

## Temperatura de rocío $T_d$

> [!definicion]
> La **temperatura de rocío** es la temperatura a la que el aire, enfriado a $\omega$ y $P$ constantes, alcanza la saturación ($\phi = 1$). Es la temperatura mínima de una superficie antes de que se forme condensación sobre ella.
>
> $$P_{\rm sat}(T_d) = P_v = \frac{\omega\,P}{0.622+\omega}.$$
>
> *Uso práctico:* en invierno, si el vidrio de una ventana está a $T < T_d$ del aire interior, se forma empañamiento. En meteorología, $T_d \approx T$ indica humedad relativa alta y riesgo de lluvia.

---

## Temperatura de bulbo húmedo $T_{bh}$

> [!definicion]
> La **temperatura de bulbo húmedo** es la temperatura de equilibrio del aire cuando se humedifica adiabáticamente hasta la saturación. Se mide con un termómetro cuyo bulbo está cubierto por una mecha húmeda.
>
> La ecuación fundamental que determina $\omega$ desde $T_{bh}$ medido proviene del **balance del saturador adiabático**: un dispositivo en que el aire húmedo entra a $(T, \omega)$, se humidifica adiabáticamente hasta la saturación, y sale a $(T_{bh}, \omega_{bh})$. El agua de reposición (*maquillaje*) se inyecta a $T_{bh}$.

> [!teorema]
> Del balance del saturador adiabático, la razón de humedad del aire en función de $T$ y $T_{bh}$:
> $$\boxed{\omega = \omega_{bh} - \frac{c_{pa}(T - T_{bh})}{h_{fg}(T_{bh})}},$$
> donde $\omega_{bh} = 0.622\,P_{\rm sat}(T_{bh})/(P - P_{\rm sat}(T_{bh}))$ y $h_{fg}(T_{bh})$ es el calor latente a $T_{bh}$.

> [!demostracion]
> **Hipótesis:** VC estacionario, adiabático ($\dot{Q}=0$), sin trabajo de eje, sin EC ni EP. Base: 1 kg de aire seco. El agua de maquillaje entra como líquido saturado a $T_{bh}$. El aire sale saturado ($\phi_2=1$) a $T_{bh}$.
>
> **Paso 1 — Balance de masa de vapor.** El aire seco no cambia; el vapor que sale minus el que entra es el agua de maquillaje evaporada:
> $$\dot{m}_{\rm maq}/\dot{m}_a = \omega_{bh} - \omega.$$
>
> **Paso 2 — Balance de energía.** Primera ley por kg de aire seco:
> $$h_a(T) + \omega\,h_v(T) + (\omega_{bh}-\omega)\,h_f(T_{bh}) = h_a(T_{bh}) + \omega_{bh}\,h_v(T_{bh}).$$
>
> **Paso 3 — Reorganizar.** Llevar todos los términos con $\omega$ a un lado:
> $$\omega\,[h_v(T) - h_f(T_{bh})] = [h_a(T_{bh}) - h_a(T)] + \omega_{bh}[h_v(T_{bh}) - h_f(T_{bh})].$$
>
> **Paso 4 — Simplificar.** Usando $h_a(T_{bh}) - h_a(T) = c_{pa}(T_{bh}-T) = -c_{pa}(T-T_{bh})$ y $h_v(T_{bh}) - h_f(T_{bh}) = h_{fg}(T_{bh})$:
> $$\omega\,[h_v(T) - h_f(T_{bh})] = -c_{pa}(T-T_{bh}) + \omega_{bh}\,h_{fg}(T_{bh}).$$
>
> **Paso 5 — Aproximación de denominador.** Para $(T - T_{bh}) \lesssim 15\,°\mathrm{C}$, el término $c_{pv}(T-T_{bh}) \ll h_{fg}(T_{bh}) \approx 2500\,\mathrm{kJ/kg}$, por lo que $h_v(T) - h_f(T_{bh}) \approx h_{fg}(T_{bh})$. Dividiendo:
> $$\omega \approx \omega_{bh} - \frac{c_{pa}(T-T_{bh})}{h_{fg}(T_{bh})}. \qquad \blacksquare$$
>
> Verificación: si $T = T_{bh}$ (aire ya saturado), $\omega = \omega_{bh}$ ✓. Si $T > T_{bh}$ (aire no saturado), $\omega < \omega_{bh}$: el aire seco tiene menos vapor que el saturado a $T_{bh}$ ✓.

---

## Entalpía del aire húmedo

> [!proposicion]
> La entalpía por kg de aire seco, tomando como referencia $T_0 = 0\,°\mathrm{C}$:
> $$h = c_{pa}\,T + \omega\,(h_{fg,0} + c_{pv}\,T) = (1.005 + 1.86\,\omega)\,T + 2501\,\omega \quad [\mathrm{kJ/kg\,a.s.}],$$
> donde $T$ está en °C, $c_{pa} = 1.005\,\mathrm{kJ/(kg\cdot K)}$, $c_{pv} = 1.86\,\mathrm{kJ/(kg\cdot K)}$ y $h_{fg,0} = 2501\,\mathrm{kJ/kg}$ (calor latente a 0°C).
>
> El término $c_{pa} T$ es la entalpía sensible del aire seco; el término $\omega(h_{fg,0}+c_{pv}T)$ es la entalpía del vapor (latente + sensible). A 25°C y $\omega = 0.010$: entalpía sensible = 25.1, entalpía latente = 25.0 — son comparables, lo que muestra la importancia del vapor.

---

## Ejemplo: propiedades del aire de un cuarto

> [!ejemplo]
> Aire a $T=28\,°\mathrm{C}$, $\phi=70\%$, $P=101.325\,\mathrm{kPa}$. Determinar: (a) $P_v$, (b) $\omega$, (c) $T_d$, (d) $h$.

> [!solucion]
> $P_{\rm sat}(28\,°\mathrm{C}) = 3.779\,\mathrm{kPa}$.
>
> **(a)** $P_v = \phi\cdot P_{\rm sat} = 0.70\times3.779 = 2.645\,\mathrm{kPa}$.
>
> **(b)** $\omega = 0.622\times2.645/(101.325-2.645) = 0.622\times2.645/98.68 = 0.01668\,\mathrm{kg/kg}$.
>
> **(c)** $T_d$: $P_{\rm sat}(T_d) = P_v = 2.645\,\mathrm{kPa}$. De tablas: $P_{\rm sat}(22\,°\mathrm{C}) = 2.645\,\mathrm{kPa}$ → $T_d = 22\,°\mathrm{C}$.
>
> **(d)** $h = (1.005+1.86\times0.01668)\times28 + 2501\times0.01668 = 1.036\times28 + 41.7 = 29.0 + 41.7 = 70.7\,\mathrm{kJ/kg\,a.s.}$
>
> El calor latente (41.7) representa el 59% de la entalpía total. Si se enfría a 15°C: $P_{\rm sat}(15°\mathrm{C}) = 1.706 < 2.645 = P_v$ → el aire condensa. El condensado por kg de aire seco: $\omega - \omega' = 0.01668 - 0.622\times1.706/(101.325-1.706) = 0.01668 - 0.01065 = 0.00603\,\mathrm{kg/kg}$.
>
> $\boxed{T_d = 22\,°\mathrm{C},\quad h = 70.7\,\mathrm{kJ/kg\,a.s.}}$ $\blacksquare$

---

## Mapa de notas

> [!info]
> - [[Carta Psicrometrica]] — estructura de la carta; los cinco tipos de curvas; lectura desde $(T,\phi)$ y desde $(T,T_{bh})$.
> - [[Procesos Psicrometricos]] — calentamiento/enfriamiento sensible, deshumidificación, humidificación, mezcla de corrientes; sistema HVAC completo.
> - [[Torres de Enfriamiento]] — balance de masa y energía en contacto directo aire–agua; agua de maquillaje; aproximación de torre.

> [!referencia]
> Borgnakke & Sonntag, cap. 12; Çengel & Boles, cap. 14; Moran & Shapiro, §12.5; ASHRAE Fundamentals, cap. 1.
