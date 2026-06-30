---
title: Capacitor
order: 1
tags:
  - circuitos-electricos
  - teoria
  - transitorios
  - capacitor
draft: false
aliases:
  - capacitor
  - condensador
  - capacitancia
  - capacitor (capacitance)
---

# Capacitor $\;i=C\,\dfrac{dv}{dt}$

> [!definicion]
> El **condensador** almacena energía en el **campo eléctrico** entre dos conductores. La carga que acumula es proporcional a la tensión, $q=Cv$, siendo $C$ la **capacidad** (en faradios, F). Como la corriente es el ritmo de la carga, su ley es
> $$i=\frac{dq}{dt}=C\,\frac{dv}{dt},$$
> y la energía almacenada es $W=\tfrac12 C v^2$. La consecuencia clave: la **tensión** $v_C$ **no puede cambiar de golpe**.

> [!info]
> Uno de los dos [[Elementos de Almacenamiento/index| elementos de almacenamiento]] del [[3 Almacenamiento y Transitorios/index| capítulo 3]]; **dual** del [[Inductor]] ($v\leftrightarrow i$, $C\leftrightarrow L$). Su carga y descarga son el [[Circuito RC| transitorio RC]]. Fraile Mora, cap. 1, §1.5.3.

---

## Ejemplo

> [!ejemplo]
> **La corriente sigue la pendiente de la tensión.**
>
> Un condensador de $C=10\ \mu\text{F}$ se carga con una tensión que sube linealmente de $0$ a $10\ \text{V}$ en $1\ \text{ms}$ y luego se mantiene constante. Hallar la corriente.
>
> ![[capacitor_iv.svg|470]]
>
> *Mientras $v$ sube con pendiente constante, la corriente $i=C\,dv/dt$ es constante; cuando $v$ deja de cambiar, $i$ cae a cero.*
>
> **Paso 1 — Durante la rampa.** La pendiente es $\dfrac{dv}{dt}=\dfrac{10\ \text{V}}{1\ \text{ms}}= 10^4\ \text{V/s}$, luego
> $$i=C\,\frac{dv}{dt}=10\times10^{-6}\cdot10^4=0{,}1\ \text{A}=100\ \text{mA}.$$
>
> **Paso 2 — Tras la rampa.** $v$ es constante $\Rightarrow \dfrac{dv}{dt}=0 \Rightarrow i=0$: el condensador se comporta como un **circuito abierto**.
>
> > [!solucion]
> > $i=100\ \text{mA}$ durante la rampa y $0$ después. La energía almacenada al llegar a $10\ \text{V}$ es $W=\tfrac12 C v^2=\tfrac12(10\,\mu\text{F})(10)^2=0{,}5\ \text{mJ}$.

---

## En qué consiste

> [!teoria] Corriente proporcional al cambio de tensión
> La ley $i=C\,dv/dt$ dice que **la corriente no depende del valor de la tensión, sino de su ritmo de cambio**. Un condensador con tensión constante no deja pasar corriente (abierto); uno con tensión que varía rápido conduce mucho. Integrando la ley, la tensión es la **historia** de la corriente:
> $$v(t)=v(t_0)+\frac1C\int_{t_0}^{t} i\,d\tau,$$
> de ahí su **memoria**: la tensión actual depende de toda la corriente pasada.

> [!teorema] La tensión del condensador es continua
> Si la corriente $i$ es finita, la tensión $v_C(t)$ es una **función continua** del tiempo: no puede dar saltos. En particular, al conmutar en $t=0$,
> $$v_C(0^+)=v_C(0^-).$$

> [!demostracion]
> **Paso 1 — Tensión como integral.** $v_C(t)=v_C(t_0)+\dfrac1C\displaystyle\int_{t_0}^{t} i\,d\tau$. **Paso 2 — Salto nulo.** El cambio en un intervalo $[\,0^-,0^+]$ es $v_C(0^+)-v_C(0^-)=\dfrac1C\int_{0^-}^{0^+} i\,d\tau$. Si $i$ está **acotada**, la integral sobre un intervalo de duración nula es $0$. Por tanto $v_C(0^+)=v_C(0^-)$. (Un salto exigiría $i\to\infty$, es decir, potencia infinita.) $\blacksquare$

> [!proposicion] Energía y carga
> El condensador **no disipa**: la potencia $p=vi=Cv\,\dfrac{dv}{dt}=\dfrac{d}{dt}\!\left(\tfrac12 Cv^2\right)$ es la derivada de la energía almacenada $W=\tfrac12 Cv^2=\tfrac{q^2}{2C}$. La devuelve íntegra al descargarse. Físicamente, para placas planas $C=\varepsilon\dfrac{A}{d}$ (área $A$, separación $d$, permitividad $\varepsilon$).

> [!info] Comportamiento por régimen
> | Situación | El condensador actúa como |
> |:---|:---|
> | DC en estado estable ($dv/dt=0$) | **circuito abierto** ($i=0$) |
> | cambio brusco de tensión | se **opone**: $v_C$ no salta |
> | alta frecuencia (varía rápido) | baja oposición (deja pasar corriente) |

> [!warning]
> No confundir: lo que no salta es la **tensión** $v_C$ (ni la carga $q$); la **corriente** sí puede dar saltos (p. ej., al conmutar). Y la capacidad $C$ es una propiedad del componente, constante; lo que varía es $v$, $q$ e $i$.

## Resumen

> [!resumen]
> | Magnitud | Expresión |
> |:---|:---|
> | Carga | $q=Cv$ |
> | Ley $v$-$i$ | $i=C\,dv/dt$ |
> | Tensión (memoria) | $v=v_0+\tfrac1C\int i\,dt$ |
> | Energía | $W=\tfrac12 Cv^2=q^2/2C$ |
> | Continuidad | $v_C(0^+)=v_C(0^-)$ |
> | DC estable | circuito **abierto** |

> [!corolario]
> El condensador es el elemento "de tensión con memoria": acumula carga, no deja saltar su tensión y en DC se abre. Su [[Inductor| dual]] hace lo mismo con la corriente. Juntos generan toda la dinámica de los [[Transitorios Primer Orden/index| transitorios]].

> [!referencia]
> Fraile Mora, cap. 1, §1.5.3. Dual: [[Inductor]]. Asociación: [[Asociacion de C y L]]. Continuidad: [[Condiciones Iniciales]]. En DC: [[Circuitos DC en Estado Estable]].
