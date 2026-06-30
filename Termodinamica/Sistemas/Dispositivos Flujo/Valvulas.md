---
title: Válvulas de Estrangulamiento
order: 5
tags:
  - termodinamica
  - dispositivos-flujo
  - valvulas
  - estrangulamiento
draft: false
aliases:
  - throttling valve
  - válvula
  - estrangulamiento
  - válvula de expansión
---

# Válvulas de Estrangulamiento

> [!definicion]
> Una **válvula de estrangulamiento** (o dispositivo de expansión) es un volumen de control estacionario con un estrechamiento irreversible: el fluido pasa a través de un orificio o constricción que causa una **caída de presión brusca** sin trabajo de eje ($\dot{W}=0$) ni transferencia de calor ($\dot{Q}\approx0$). La energía cinética es despreciable antes y después.
>
> *¿Qué es "estrangulamiento"?* A diferencia de la expansión en una turbina (reversible, con producción de trabajo), el estrangulamiento es una irreversibilidad pura: la presión cae sin producir ningún trabajo útil. Toda la caída de presión se disipa en viscosidad y turbulencia en la zona del cuello.
>
> *¿Por qué la entalpía se conserva?* Sin trabajo, sin calor y con EC despreciable, la SFEE da $h_1 = h_2$. Este resultado es la base del efecto Joule–Thomson: para un gas real, a entalpía constante la temperatura puede subir o bajar dependiendo del fluido y el rango de operación.
>
> *Aplicaciones:* válvulas de expansión en ciclos de refrigeración, tubos capilares en refrigeradores domésticos, válvulas de control en tuberías industriales, válvulas reductoras de presión (PRV).

![[valvula_estrangulamiento_vc.svg|440]]
*Válvula de estrangulamiento. El fluido pasa por el orificio y emerge a menor presión. El volumen específico $v_2 > v_1$ (el fluido ocupa más volumen). Para vapor en la región bifásica, parte del líquido se vaporiza; para gas ideal, la temperatura permanece igual; para gas real, cambia según el coeficiente Joule–Thomson.*

---

## Balance de energía: $h_1 = h_2$

> [!teorema]
> Para una válvula de estrangulamiento adiabática, estacionaria, sin trabajo de eje, despreciando $\Delta EC$ y $\Delta EP$:
> $$\boxed{h_1 = h_2.}$$
> El proceso es **isoentálpico** pero altamente **irreversible**: $s_2 > s_1$ (la presión cae a entalpía constante, y en el diagrama $h$-$s$ el punto 2 está a la derecha de 1).

> [!demostracion]
> **Hipótesis:** VC estacionario, $\dot{Q}=0$, $\dot{W}=0$, $\Delta EC \approx 0$, $\Delta EP = 0$, una sola corriente.
>
> **Paso 1 — Primera ley del VC.** Con todos los términos nulos:
> $$\dot{Q} - \dot{W} = \dot{m}\!\left[(h_2-h_1) + \frac{C_2^2-C_1^2}{2} + g(z_2-z_1)\right] = 0.$$
>
> **Paso 2 — Aplicar hipótesis.** Con $\dot{Q}=0$, $\dot{W}=0$, $\Delta EC\approx0$, $\Delta EP=0$:
> $$\dot{m}(h_2-h_1) = 0 \implies h_2 = h_1.$$
>
> **Paso 3 — Verificar que la EC es despreciable.** Las velocidades en la válvula son bajas salvo en la zona del cuello, pero los estados 1 y 2 se miden lejos del cuello. La diferencia de energía cinética típica: $\Delta EC \sim 1\,\mathrm{kJ/kg} \ll \Delta h \sim 100$–$500\,\mathrm{kJ/kg}$. La aproximación es válida.
>
> **Paso 4 — Segunda ley: irreversibilidad.** Aplicando el balance de entropía con $\dot{Q}=0$:
> $$\dot{S}_{\rm gen} = \dot{m}(s_2-s_1) \geq 0.$$
> Por la segunda ley, $s_2 \geq s_1$. La igualdad solo se daría en un proceso reversible sin caída de presión, que no es el caso. Para el estrangulamiento: $s_2 > s_1$ siempre.
>
> **Paso 5 — Consecuencia en el diagrama $P$-$h$.** En el diagrama $P$-$h$ (usado en refrigeración), el estrangulamiento es una **línea vertical**: el proceso baja en la ordenada $P$ a $h$ constante. En el diagrama $T$-$s$: el proceso se desplaza hacia la derecha (mayor entropía) a menores presiones. $\blacksquare$

---

## Efecto Joule–Thomson

> [!teoria]
> ¿Qué le pasa a la temperatura cuando cae la presión a $h$ constante? Depende del fluido.
>
> El **coeficiente de Joule–Thomson** mide cuánto cambia $T$ por unidad de caída de presión a $h$ constante:
> $$\mu_{\rm JT} = \left(\frac{\partial T}{\partial P}\right)_h.$$
>
> | Región | Signo de $\mu_{\rm JT}$ | Efecto de la expansión |
> |:---|:---:|:---|
> | Gas ideal ($Pv=RT$) | $0$ | $T$ no cambia |
> | Gas real a $T>T_{\rm inv}$ | $< 0$ | $T$ **sube** (poco útil) |
> | Gas real a $T<T_{\rm inv}$ | $> 0$ | $T$ **baja** (base de la licuefacción) |
> | Líquido o mezcla bifásica | — | se aplica directamente $h_1=h_2$ con tablas |
>
> *Temperatura de inversión* $T_{\rm inv}$: para N₂ ≈ 621 K, O₂ ≈ 764 K, H₂ ≈ 204 K. Para licuar gases, primero hay que enfriarlos por debajo de $T_{\rm inv}$ y luego expandir.

---

## Aplicación: ciclo de refrigeración por compresión de vapor

> [!teoria]
> En un ciclo de refrigeración estándar (Rankine inverso):
>
> - **Compresor** (1→2): sube presión y $h$ del vapor.
> - **Condensador** (2→3): extrae calor, el vapor se licua; $h$ baja.
> - **Válvula de expansión** (3→4): cae presión a $h=\text{cte}$; se vaporiza parcialmente.
> - **Evaporador** (4→1): absorbe calor del espacio frío; $h$ sube.
>
> El título de vapor a la salida de la válvula:
> $$x_4 = \frac{h_3 - h_{f}(P_4)}{h_{fg}(P_4)}.$$
>
> El COP del ciclo:
> $$\mathrm{COP_R} = \frac{q_L}{w_c} = \frac{h_1-h_4}{h_2-h_1}.$$

---

## Ejemplo: válvula de expansión en ciclo de refrigeración con R-134a

> [!ejemplo]
> En un sistema de refrigeración con R-134a, el líquido saturado sale del condensador a $P_3=800\,\mathrm{kPa}$ y se expande hasta $P_4=140\,\mathrm{kPa}$. Determinar: (a) $h_3$ y $T_3$; (b) $h_4$ y $x_4$ a la salida de la válvula; (c) $q_{\rm evap}$ si el vapor sale saturado del evaporador ($x_1=1$).

> [!solucion]
> **Paso 1 — Estado 3: líquido saturado a $800\,\mathrm{kPa}$.** De tablas de saturación del R-134a a $800\,\mathrm{kPa}$:
> $$T_{\rm sat}(800\,\mathrm{kPa}) = 31.3\,°\mathrm{C}, \quad h_3 = h_f = 95.47\,\mathrm{kJ/kg}.$$
>
> **Paso 2 — Proceso de estrangulamiento.** El proceso es isoentálpico:
> $$h_4 = h_3 = 95.47\,\mathrm{kJ/kg}.$$
>
> **Paso 3 — Estado 4: mezcla bifásica a $140\,\mathrm{kPa}$.** De tablas a $140\,\mathrm{kPa}$:
> $T_{\rm sat}=-18.8\,°\mathrm{C}$; $h_f=27.06\,\mathrm{kJ/kg}$; $h_{fg}=209.48\,\mathrm{kJ/kg}$.
> $$x_4 = \frac{h_4-h_f}{h_{fg}} = \frac{95.47-27.06}{209.48} = \frac{68.41}{209.48} = 0.327.$$
>
> **Paso 4 — Estado 1: vapor saturado a $140\,\mathrm{kPa}$.**
> $$h_1 = h_g(140\,\mathrm{kPa}) = h_f + h_{fg} = 27.06+209.48 = 236.54\,\mathrm{kJ/kg}.$$
>
> **Paso 5 — Calor del evaporador.**
> $$q_{\rm evap} = h_1 - h_4 = 236.54 - 95.47 = 141.1\,\mathrm{kJ/kg}.$$
> La válvula de expansión genera una mezcla con 32.7% de vapor; esa fracción no absorbe calor adicional en el evaporador (ya es vapor). El 67.3% que sigue siendo líquido es el que absorbe los $141.1\,\mathrm{kJ/kg}$.
>
> $\boxed{h_4=95.47\,\mathrm{kJ/kg},\quad x_4=0.327,\quad q_{\rm evap}=141.1\,\mathrm{kJ/kg}.}$ $\blacksquare$

> [!warning]
> El estrangulamiento es una **irreversibilidad inevitable** en el ciclo de refrigeración estándar. El trabajo potencial perdido es $w_{\rm perdido}=T_0(s_4-s_3)$. Sustituir la válvula por una **turbina de expansión** recuperaría parte de ese trabajo (ciclo Lorentzen), pero es mecánicamente complejo. En plantas criogénicas de gran escala (licuación de GNL) sí se usan expansores.

> [!referencia]
> Borgnakke & Sonntag, §6.5; Çengel & Boles, §11-2; Moran & Shapiro, §10.2.
