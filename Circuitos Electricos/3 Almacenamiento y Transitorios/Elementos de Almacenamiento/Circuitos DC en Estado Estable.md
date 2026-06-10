---
title: Circuitos DC en Estado Estable
tags:
  - circuitos-electricos
  - teoria
  - transitorios
  - estado-estable
draft: false
aliases:
  - circuitos DC en estado estable
  - régimen permanente DC
  - estado estable
  - DC steady state
---

# Circuitos DC en Estado Estable

> [!definicion]
> En **régimen permanente de corriente continua** (cuando ya se extinguió todo transitorio y nada
> varía en el tiempo) las derivadas se anulan, $\dfrac{d}{dt}(\cdot)=0$. Como consecuencia, el
> **condensador** se comporta como un **circuito abierto**, porque
> $$i_C=C\,\frac{dv}{dt}=0,$$
> y el **inductor** se comporta como un **cortocircuito**, porque
> $$v_L=L\,\frac{di}{dt}=0.$$
> El circuito se reduce entonces a uno puramente **resistivo**, que se resuelve con las técnicas de
> análisis de redes de continua.

> [!info]
> Es la consecuencia directa, en estado estable, de las leyes constitutivas del [[Capacitor]] y del
> [[Inductor]] como [[Elementos de Almacenamiento/index| elementos de almacenamiento]] del
> [[3 Almacenamiento y Transitorios/index| capítulo 3]]. Es, además, la herramienta práctica para
> hallar los valores **iniciales** ($t=0^-$) y **finales** ($t\to\infty$) que se usan en
> [[Condiciones Iniciales]]. Fraile Mora, cap. 4.

---

## Ejemplo

> [!ejemplo]
> **Red con $L$ y $C$ en régimen permanente DC.**
>
> El circuito de la figura se alimenta con una fuente de continua $V_s=12\ \text{V}$ y contiene una
> resistencia $R_1=4\ \Omega$, un inductor $L$, un condensador $C$ y una resistencia
> $R_2=8\ \Omega$. El condensador está conectado **en paralelo** con $R_2$. Suponiendo que el
> circuito lleva mucho tiempo conectado (todo transitorio se extinguió), hallar la **corriente** de
> la malla, la tensión del condensador $v_C$ y la corriente del inductor $i_L$.
>
> ![[dc_estable.svg|620]]
>
> *(a) circuito con $L$ y $C$; (b) en DC permanente el inductor es un corto y el condensador un
> abierto, quedando una red resistiva.*
>
> > [!solucion]
> > **Paso 1 — Reemplazar los elementos almacenadores.** En régimen permanente DC el inductor se
> > convierte en un **cortocircuito** ($L\to$ corto) y el condensador en un **circuito abierto**
> > ($C\to$ abierto). Al abrirse, el condensador no deja pasar corriente por su rama, de modo que
> > la única corriente circula por $V_s$, $R_1$ y $R_2$, que quedan **en serie** (el inductor,
> > ahora un corto, simplemente cierra la malla sin caída de tensión).
> >
> > **Paso 2 — Corriente de la malla.** Por la ley de Ohm aplicada a la serie:
> > $$i=\frac{V_s}{R_1+R_2}=\frac{12\ \text{V}}{4\ \Omega+8\ \Omega}=\frac{12}{12}=1\ \text{A}.$$
> > Como el inductor está en esa misma rama serie, esta es justamente la corriente que lo
> > atraviesa: $i_L=i=1\ \text{A}$.
> >
> > **Paso 3 — Tensión del condensador.** El condensador, en abierto, queda en paralelo con $R_2$,
> > así que su tensión es la misma que la caída en $R_2$:
> > $$v_C=v_{R_2}=i\,R_2=1\ \text{A}\cdot 8\ \Omega=8\ \text{V}.$$
> >
> > **Resultado:** $\boxed{i_L=1\ \text{A}}$ y $\boxed{v_C=8\ \text{V}}$. Con estos valores, la
> > energía almacenada en cada elemento es
> > $$W_L=\tfrac12 L\,i_L^2,\qquad W_C=\tfrac12 C\,v_C^2,$$
> > que permanece constante mientras el régimen sea permanente (ningún elemento intercambia energía
> > neta con el resto del circuito).

---

## En qué consiste

> [!teoria]
> La razón es puramente la **definición de las leyes constitutivas**. Tanto el condensador
> ($i_C=C\,dv/dt$) como el inductor ($v_L=L\,di/dt$) responden a **variaciones** de su variable de
> estado. En estado estable nada varía, $d/dt=0$, y por tanto:
> - El condensador tiene $i_C=0$ aunque su tensión $v_C$ sea no nula $\Rightarrow$ se comporta como
>   un **abierto** (no conduce, pero sostiene tensión).
> - El inductor tiene $v_L=0$ aunque su corriente $i_L$ sea no nula $\Rightarrow$ se comporta como
>   un **corto** (no cae tensión, pero conduce corriente).
>
> Este análisis tiene un papel doble en los transitorios: el régimen permanente **antes** de
> conmutar fija los valores **iniciales** ($v_C(0^-)$, $i_L(0^-)$), y el régimen permanente
> **después** de la conmutación fija los valores **finales** ($v_C(\infty)$, $i_L(\infty)$). Ambos
> alimentan la solución exponencial del transitorio.

> [!algoritmo]
> 1. **Sustituir** cada condensador por un **circuito abierto** y cada inductor por un
>    **cortocircuito**.
> 2. **Resolver** la red puramente resistiva resultante con las técnicas habituales (leyes de
>    Kirchhoff, análisis de mallas o de nodos, divisores de tensión/corriente).
> 3. **Leer** las magnitudes de interés: $v_C$ es la **tensión** en los terminales del abierto (la
>    que vería el condensador) e $i_L$ es la **corriente** que atraviesa el corto (la que vería el
>    inductor).

> [!warning]
> Esta reducción ($C\to$ abierto, $L\to$ corto) vale **solo en régimen permanente de continua**,
> nunca durante el transitorio: en plena carga/descarga las derivadas no son nulas y los elementos
> sí cuentan. Tampoco aplica con fuentes que varían en el tiempo (por ejemplo en **AC**), donde el
> condensador y el inductor presentan impedancia y **no** se reducen a un abierto y un corto.

---

## Resumen

> [!resumen]
> | Elemento | Ley | En DC ($d/dt=0$) | Equivale a | Magnitud a leer |
> |:---:|:---:|:---:|:---:|:---:|
> | Condensador | $i_C=C\,\dfrac{dv}{dt}$ | $i_C=0$ | **Circuito abierto** | $v_C$ (tensión en el abierto) |
> | Inductor | $v_L=L\,\dfrac{di}{dt}$ | $v_L=0$ | **Cortocircuito** | $i_L$ (corriente por el corto) |
>
> En el ejemplo: $i_L=1\ \text{A}$ y $v_C=8\ \text{V}$ sobre la red serie $R_1$–$R_2$ con
> $V_s=12\ \text{V}$.

> [!corolario]
> En un circuito de continua en estado estable, **toda** la corriente que llega a un condensador es
> nula y **toda** la tensión sobre un inductor es nula. Por ello, en estado estable, un condensador
> jamás disipa ni transfiere potencia ($p_C=v_C\,i_C=0$) y un inductor tampoco ($p_L=v_L\,i_L=0$):
> su energía almacenada permanece constante.

> [!referencia]
> Fraile Mora, J. *Circuitos Eléctricos*, cap. 4 (régimen transitorio y permanente). Véanse las
> leyes constitutivas en [[Capacitor]] e [[Inductor]], y la aplicación a valores inicial/final en
> [[Condiciones Iniciales]].
