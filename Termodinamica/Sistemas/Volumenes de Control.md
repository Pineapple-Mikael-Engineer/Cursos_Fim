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
> Un **volumen de control** (VC) — también llamado *sistema abierto* — es una región del espacio de frontera fija o deformable, **a través de la cual puede fluir masa**. Es el modelo de todos los equipos con corrientes de entrada y salida: turbinas, compresores, calderas, toberas, reactores continuos.
>
> *¿Por qué la entalpía y no la energía interna?* Cada kilogramo que cruza la frontera trae su energía interna $u$, pero además realiza un **trabajo de empuje** $Pv$ para abrirse paso. La energía que transporta cada corriente es por tanto
> $$\theta = \underbrace{u + Pv}_{=\,h} + \frac{C^2}{2} + gz,$$
> de modo que la entalpía $h=u+Pv$ es la propiedad natural de los sistemas abiertos. La deducción del trabajo de flujo $Pv$ está en [[Balance de Energia VC]].

![[volumen_de_control_generico.svg|440]]
*Volumen de control genérico con $n_e$ entradas e $n_s$ salidas. La frontera (superficie de control) puede ser fija o deformable. A través de ella cruzan calor $\dot{Q}$, trabajo de eje $\dot{W}$ y corrientes másicas $\dot{m}$. Las propiedades internas pueden variar en el tiempo (transitorio) o permanecer constantes (estacionario).*

> [!info]
> Esta nota es el **encuadre** del modelo: qué es un VC, por qué la entalpía es su variable natural y cuándo elegirlo. Los balances en detalle viven en [[Conservacion/Volumenes de Control/index | Conservación — Volumen de Control]].

---

## Sistema cerrado vs. volumen de control

> [!teoria]
> La elección del modelo depende de si **cruza masa la frontera**:
>
> | Característica | [[Sistemas Cerrados \| Sistema cerrado (SC)]] | Volumen de control (VC) |
> |:---|:---|:---|
> | Masa | Fija ($dm=0$) | Variable (hay flujo) |
> | Frontera | Sigue a la masa | Fija/deformable en el espacio |
> | Propiedad energética natural | $U$ (energía interna) | $h$ (entalpía, incluye $Pv$) |
> | Trabajo característico | Frontera móvil $\int P\,dV$ | Trabajo de eje $\dot W_{\rm eje}$ |
> | Modelo típico | Pistón-cilindro, batch | Turbina, compresor, tobera |
>
> La transición SC → VC es conceptual: el mismo gas se trata como SC si se "sigue" la masa, o como VC si se fija un volumen y se permite el paso de masa. Lo que aparece al abrir la frontera es el conjunto de términos de flujo $\dot m\,\theta$.

> [!teoria] Cuándo modelar como VC
> Conviene el volumen de control cuando el fluido **circula de forma continua** por el dispositivo. El caso dominante es el [[Flujo Estacionario | flujo estacionario]] (turbinas, bombas, intercambiadores en operación normal), donde las derivadas temporales se anulan. El caso **transitorio** (llenado o vaciado de tanques) conserva las derivadas $d/dt$ — ver el ejemplo más abajo.

---

## Balances generales (resumen y delegación)

> [!teorema]
> Para un VC con entradas $i$ y salidas $e$, en forma de tasa:
> $$\frac{dm_{\rm vc}}{dt} = \sum_i\dot m_i - \sum_e\dot m_e,$$
> $$\frac{dE_{\rm vc}}{dt} = \dot Q - \dot W + \sum_i\dot m_i\theta_i - \sum_e\dot m_e\theta_e, \qquad \theta = h+\tfrac{C^2}{2}+gz,$$
> $$\frac{dS_{\rm vc}}{dt} = \sum_k\frac{\dot Q_k}{T_k} + \sum_i\dot m_i s_i - \sum_e\dot m_e s_e + \dot S_{\rm gen}, \qquad \dot S_{\rm gen}\ge0.$$
> Aquí $\dot W$ es solo trabajo de eje (el de flujo ya está en $h$). Las deducciones, las hipótesis y los ejemplos de cada balance están en [[Balance de Masa VC]], [[Balance de Energia VC]], [[Balance de Entropia VC]] y [[Balance de Exergia VC]].

---

## Ejemplo: llenado de un recipiente rígido (VC transitorio)

> [!ejemplo]
> Un recipiente rígido de $V=0.5\,\mathrm{m^3}$, inicialmente evacuado, se conecta a una línea de suministro de vapor a $P_L=1\,\mathrm{MPa}$, $T_L=300\,°\mathrm{C}$ ($h_L=3051.2\,\mathrm{kJ/kg}$). La conexión se mantiene abierta hasta que la presión en el recipiente iguala $P_L$. El proceso es adiabático. Determinar la temperatura final del vapor.

> [!solucion]
> **Paso 1 — VC: el recipiente.** Una sola entrada, sin salida, sin trabajo de eje ($\dot{W}=0$), adiabático ($\dot{Q}=0$). Es **transitorio**: el contenido del VC cambia con el tiempo.
>
> **Paso 2 — Balance de masa.** $m_2 - 0 = m_{\rm entra}$: toda la masa que entra queda dentro.
>
> **Paso 3 — Balance de energía no estacionario.** Integrando $dE_{\rm vc}/dt = \dot m\,h_L$ con $E_{\rm vc,1}=0$ (vacío):
> $$U_2 - 0 = m_{\rm entra}\,h_L \implies m_2 u_2 = m_2 h_L \implies u_2 = h_L = 3051.2\,\mathrm{kJ/kg}.$$
>
> **Paso 4 — Estado final.** A $P_2=1\,\mathrm{MPa}$ y $u_2=3051.2\,\mathrm{kJ/kg}$. De tablas de vapor sobrecalentado a $1\,\mathrm{MPa}$: $u(400\,°\mathrm{C})=2957.3$, $u(500\,°\mathrm{C})=3131.4$. Interpolando: $T_2 = 400 + (3051.2-2957.3)/(3131.4-2957.3)\times100 \approx 454\,°\mathrm{C}$.
>
> **Paso 5 — Razonabilidad.** El vapor final ($454\,°\mathrm{C}$) queda más caliente que la línea ($300\,°\mathrm{C}$): el trabajo de flujo $Pv$ con que la línea empuja el vapor hacia el recipiente se convierte en energía interna ($u_2=h_L>u_L$). Es la firma del término de flujo que distingue el VC del SC.
>
> $\boxed{T_2 \approx 454\,°\mathrm{C},\quad u_2=h_L=3051.2\,\mathrm{kJ/kg}.}$ $\blacksquare$

---

## Relación con otras notas

> [!info]
> - [[Conservacion/Volumenes de Control/index | Conservación — Volumen de Control]] — los cuatro balances (masa, energía, entropía, exergía) en detalle.
> - [[Sistemas Cerrados]] — el modelo complementario, con masa fija.
> - [[Flujo Estacionario]] — el caso estacionario (SFSS) y sus consecuencias.
> - [[Balance de Energia VC]] — deducción del trabajo de flujo $h=u+Pv$.

> [!info]
> **Notación:** $\dot{m}$ flujo másico [kg/s]; $C$ velocidad [m/s]; $z$ altura [m]; $\theta=h+C^2/2+gz$ energía específica de la corriente. Subíndices $i$: entrada; $e$: salida.

> [!referencia]
> Borgnakke & Sonntag, Cap. 6; Çengel & Boles, Cap. 5; Moran & Shapiro, Cap. 4.
