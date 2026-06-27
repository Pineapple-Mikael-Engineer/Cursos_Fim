---
title: Volumen de Control
order: 2
tags:
  - termodinamica
  - sistemas
  - volumen-de-control
draft: false
aliases:
  - control volume
  - sistema abierto
  - volúmenes de control
  - VC
---

# Volumen de Control

> [!definicion]
> Un **volumen de control** (VC) — también llamado *sistema abierto* — es una región del espacio de frontera fija o deformable, **a través de la cual puede fluir masa**. Es el modelo de todos los equipos termodinámicos que tienen corrientes de entrada y salida: turbinas, compresores, calderas, reactores continuos.
>
> *¿Por qué la entalpía y no la energía interna?* Cada kilogramo de fluido que cruza la frontera del VC trae consigo su energía interna $u$, pero además tiene que hacer un trabajo de "empuje" para abrirse paso: el fluido de atrás empuja con presión $P$ y el volumen específico que ocupa es $v$. Este trabajo de flujo vale exactamente $Pv$ por kilogramo. En total, la energía que transporta cada corriente es:
> $$\theta = \underbrace{u + Pv}_{=h} + \frac{C^2}{2} + gz.$$
> La entalpía $h = u + Pv$ es, pues, la propiedad natural de los sistemas abiertos.

![[volumen_de_control_generico.svg|440]]
*Volumen de control genérico con $n_e$ entradas e $n_s$ salidas. La frontera (superficie de control) puede ser fija o deformable. A través de ella cruzan calor $\dot{Q}$, trabajo $\dot{W}$ y corrientes másicas $\dot{m}$. Dentro del VC las propiedades pueden variar en el tiempo (transitorio) o permanecer constantes (estacionario).*

---

## Origen del trabajo de flujo: derivación del término $h = u + Pv$

> [!demostracion]
> **Hipótesis:** fluido en flujo unidimensional; el control de volumen tiene una entrada de área $A$ con presión $P$, velocidad $C$ y densidad $\rho=1/v$.
>
> **Paso 1 — Inventario de energía transportada.** En un intervalo $dt$, un volumen $dV = CA\,dt$ de fluido atraviesa la frontera. Su masa es $dm = \rho\,dV = CA\,dt/v$. Este fluido porta energía interna $u\,dm$.
>
> **Paso 2 — Trabajo de empuje.** Para que el fluido entre al VC, el fluido de aguas arriba ejerce una fuerza $F=PA$ sobre la cara de entrada. El trabajo realizado en el intervalo $dt$ es:
> $$\delta W_{\rm flujo} = F\,C\,dt = PA\cdot C\,dt = P\cdot(CA\,dt) = P\cdot dV = P v\,dm.$$
>
> **Paso 3 — Energía total por unidad de masa.** La energía total que cruza la frontera por kilogramo de fluido es la suma de la interna más el trabajo de empuje:
> $$\frac{\delta E_{\rm masa}}{dm} = u + Pv = h.$$
>
> **Paso 4 — Incluir EC y EP.** Si además el fluido tiene velocidad $C$ y altura $z$:
> $$\theta = h + \frac{C^2}{2} + gz.$$
>
> **Paso 5 — Implicación para el balance de energía.** Cada corriente contribuye al balance de energía del VC con $\dot{m}\,\theta$, no con $\dot{m}\,u$. La diferencia $\dot{m}\,Pv$ es el trabajo de flujo, invisible en el [[Sistemas Cerrados | sistema cerrado]] donde no hay cruce de masa. $\blacksquare$

---

## Balances generales del VC

> [!teorema]
> Para un VC con $n_e$ entradas ($i$) y $n_s$ salidas ($e$), en forma de tasa:
>
> **Balance de masa:**
> $$\frac{dm_{\rm vc}}{dt} = \sum_{i}\dot{m}_i - \sum_{e}\dot{m}_e.$$
>
> **Balance de energía:**
> $$\frac{dE_{\rm vc}}{dt} = \dot{Q} - \dot{W} + \sum_{i}\dot{m}_i\theta_i - \sum_{e}\dot{m}_e\theta_e,$$
> donde $\dot{W}$ incluye solo trabajo de eje (no el trabajo de flujo, ya absorbido en $h$).
>
> **Balance de entropía:**
> $$\frac{dS_{\rm vc}}{dt} = \sum_k\frac{\dot{Q}_k}{T_k} + \sum_{i}\dot{m}_i s_i - \sum_{e}\dot{m}_e s_e + \dot{S}_{\rm gen}, \quad \dot{S}_{\rm gen}\geq0.$$
>
> El caso más frecuente — equipo en operación continua — es el [[Flujo Estacionario | flujo estacionario]], donde las derivadas temporales se anulan.

---

## Comparación SC vs. VC

> [!teoria]
> | Característica | Sistema cerrado (SC) | Volumen de control (VC) |
> |:---|:---|:---|
> | Masa | Fija ($dm=0$) | Variable (hay flujo) |
> | Propiedad energética natural | $U$ (energía interna) | $h$ (entalpía) |
> | Trabajo de frontera | $\int P\,dV$ | Incluido en $h$ vía $Pv$ |
> | Forma diferencial 1ª ley | $dU=\delta Q-\delta W$ | $dE_{\rm vc}=\dot{Q}-\dot{W}+\sum\dot{m}\theta$ |
> | Modelo típico | Pistón-cilindro, batch | Turbina, compresor, tobera |
>
> La transición de SC a VC es conceptual: el mismo gas puede tratarse como SC si se "sigue" la masa, o como VC si se fija un volumen y se permite el paso de masa.

---

## Ejemplo: llenado de un recipiente rígido

> [!ejemplo]
> Un recipiente rígido de $V=0.5\,\mathrm{m^3}$, inicialmente evacuado, se conecta a una línea de suministro de vapor a $P_L=1\,\mathrm{MPa}$, $T_L=300\,°\mathrm{C}$ ($h_L=3051.2\,\mathrm{kJ/kg}$). La conexión se mantiene abierta hasta que la presión en el recipiente iguala $P_L$. El proceso es adiabático. Determinar la temperatura final del vapor en el recipiente.

> [!solucion]
> **Paso 1 — VC: el recipiente rígido.** Una sola entrada (línea), sin salida, sin trabajo de eje ($\dot{W}=0$), adiabático ($\dot{Q}=0$).
>
> **Paso 2 — Balance de masa.** $m_2 - 0 = m_{\rm entra}$. Toda la masa que entra queda en el recipiente.
>
> **Paso 3 — Balance de energía (no estacionario).** Con $E_{\rm vc,1}=0$ (recipiente vacío):
> $$U_{2} - 0 = 0 - 0 + m_{\rm entra}\,h_L \implies m_2 u_2 = m_2 h_L.$$
> Luego $u_2 = h_L = 3051.2\,\mathrm{kJ/kg}$.
>
> **Paso 4 — Determinar el estado final.** A $P_2=1\,\mathrm{MPa}$ y $u_2=3051.2\,\mathrm{kJ/kg}$. De tablas de vapor sobrecalentado a $1\,\mathrm{MPa}$: $u(300\,°\mathrm{C})=2793.2$, $u(400\,°\mathrm{C})=2957.3$, $u(500\,°\mathrm{C})=3131.4$. Interpolando para $u_2=3051.2$: $T_2=400+(3051.2-2957.3)/(3131.4-2957.3)\times100\approx454\,°\mathrm{C}$.
>
> **Paso 5 — Razonabilidad.** El vapor final ($454\,°\mathrm{C}$) está más caliente que la línea ($300\,°\mathrm{C}$) porque el trabajo de flujo $Pv$ de la línea se convierte en energía interna adicional al comprimirse el vapor en el recipiente.
>
> $\boxed{T_2 \approx 454\,°\mathrm{C},\quad u_2=h_L=3051.2\,\mathrm{kJ/kg}.}$ $\blacksquare$

> [!info]
> **Notación:** $\dot{m}$ flujo másico [kg/s]; $C$ velocidad [m/s]; $z$ altura [m]; $\theta = h+C^2/2+gz$ energía específica de la corriente. Subíndices $i$: entrada; $e$: salida. Balances detallados: [[Balance de Masa VC]], [[Balance de Energia VC]], [[Balance de Entropia VC]].

> [!referencia]
> Borgnakke & Sonntag, Cap. 6; Çengel & Boles, Cap. 5; Moran & Shapiro, Cap. 4.
