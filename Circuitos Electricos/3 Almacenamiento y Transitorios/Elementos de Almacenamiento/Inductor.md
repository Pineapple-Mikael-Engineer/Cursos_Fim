---
title: Inductor
order: 2
tags:
  - circuitos-electricos
  - teoria
  - transitorios
  - inductor
draft: false
aliases:
  - inductor
  - bobina
  - inductancia
  - inductor (inductance)
---

# Inductor $\;v=L\,\dfrac{di}{dt}$

> [!definicion]
> El **inductor** (o bobina) almacena energía en el **campo magnético** que crea su corriente. El flujo concatenado es proporcional a la corriente, $\phi=Li$, siendo $L$ la **inductancia** (en henrios, H). Por la ley de Faraday, la tensión es el ritmo del flujo:
> $$v=\frac{d\phi}{dt}=L\,\frac{di}{dt},$$
> y la energía almacenada es $W=\tfrac12 L i^2$. La consecuencia clave: la **corriente** $i_L$ **no puede cambiar de golpe**.

> [!info]
> El **dual** del [[Capacitor]] ($v\leftrightarrow i$, $L\leftrightarrow C$), uno de los [[Elementos de Almacenamiento/index| elementos de almacenamiento]] del [[3 Almacenamiento y Transitorios/index| capítulo 3]]. Su carga y descarga magnética son el [[Circuito RL| transitorio RL]]. Fraile Mora, cap. 1, §1.5.2.

---

## Ejemplo

> [!ejemplo]
> **La tensión sigue la pendiente de la corriente.**
>
> Por un inductor de $L=2\ \text{mH}$ circula una corriente que sube linealmente de $0$ a $5\ \text{A}$ en $1\ \text{ms}$ y luego se mantiene constante. Hallar la tensión.
>
> ![[inductor_vi.svg|470]]
>
> *Mientras $i$ sube con pendiente constante, la tensión $v=L\,di/dt$ es constante; cuando $i$ deja de cambiar, $v$ cae a cero.*
>
> **Paso 1 — Durante la rampa.** La pendiente es $\dfrac{di}{dt}=\dfrac{5\ \text{A}}{1\ \text{ms}}= 5\times10^3\ \text{A/s}$, luego
> $$v=L\,\frac{di}{dt}=2\times10^{-3}\cdot5\times10^3=10\ \text{V}.$$
>
> **Paso 2 — Tras la rampa.** $i$ es constante $\Rightarrow \dfrac{di}{dt}=0 \Rightarrow v=0$: el inductor se comporta como un **cortocircuito**.
>
> > [!solucion]
> > $v=10\ \text{V}$ durante la rampa y $0$ después. La energía almacenada al llegar a $5\ \text{A}$ es $W=\tfrac12 L i^2=\tfrac12(2\,\text{mH})(5)^2=25\ \text{mJ}$.

---

## En qué consiste

> [!teoria] Tensión proporcional al cambio de corriente
> La ley $v=L\,di/dt$ dice que **la tensión no depende del valor de la corriente, sino de su ritmo de cambio**. Un inductor con corriente constante no cae tensión (corto); uno cuya corriente varía rápido genera mucha tensión —de ahí las chispas al abrir un circuito inductivo—. Integrando, la corriente es la **historia** de la tensión:
> $$i(t)=i(t_0)+\frac1L\int_{t_0}^{t} v\,d\tau,$$
> su **memoria**: la corriente actual depende de toda la tensión pasada.

> [!teorema] La corriente del inductor es continua
> Si la tensión $v$ es finita, la corriente $i_L(t)$ es **continua**: no puede dar saltos. En particular, al conmutar en $t=0$,
> $$i_L(0^+)=i_L(0^-).$$

> [!demostracion]
> **Paso 1 — Corriente como integral.** $i_L(t)=i_L(t_0)+\dfrac1L\displaystyle\int_{t_0}^{t} v\,d\tau$. **Paso 2 — Salto nulo.** $i_L(0^+)-i_L(0^-)=\dfrac1L\int_{0^-}^{0^+} v\,d\tau$. Si $v$ está **acotada**, la integral sobre un intervalo de duración nula es $0$, luego $i_L(0^+)=i_L(0^-)$. (Un salto exigiría $v\to\infty$.) Es la dualidad exacta de la continuidad de $v_C$ en el [[Capacitor]]. $\blacksquare$

> [!proposicion] Energía y flujo
> El inductor **no disipa**: $p=vi=Li\,\dfrac{di}{dt}=\dfrac{d}{dt}\!\left(\tfrac12 Li^2\right)$ es la derivada de la energía $W=\tfrac12 Li^2=\dfrac{\phi^2}{2L}$, que devuelve al desmagnetizarse. Físicamente, para un solenoide de $N$ espiras, $L=\dfrac{N^2\mu A}{\ell}$.

> [!info] Comportamiento por régimen
> | Situación | El inductor actúa como |
> |:---|:---|
> | DC en estado estable ($di/dt=0$) | **cortocircuito** ($v=0$) |
> | cambio brusco de corriente | se **opone**: $i_L$ no salta |
> | alta frecuencia (varía rápido) | alta oposición (gran tensión) |

> [!warning]
> Lo que no salta es la **corriente** $i_L$ (ni el flujo $\phi$); la **tensión** sí puede saltar. **Nunca** abrir bruscamente un circuito con un inductor cargado: $di/dt$ enorme produce una sobretensión que puede dañar componentes (arco eléctrico).

## Resumen

> [!resumen]
> | Magnitud | Expresión |
> |:---|:---|
> | Flujo | $\phi=Li$ |
> | Ley $v$-$i$ | $v=L\,di/dt$ |
> | Corriente (memoria) | $i=i_0+\tfrac1L\int v\,dt$ |
> | Energía | $W=\tfrac12 Li^2=\phi^2/2L$ |
> | Continuidad | $i_L(0^+)=i_L(0^-)$ |
> | DC estable | **cortocircuito** |

> [!corolario]
> El inductor es el elemento "de corriente con memoria": almacena flujo, no deja saltar su corriente y en DC se cortocircuita —el espejo exacto del [[Capacitor]]—. Esa dualidad permite traducir cualquier resultado de uno al otro sin rehacer el análisis.

> [!referencia]
> Fraile Mora, cap. 1, §1.5.2. Dual: [[Capacitor]]. Asociación: [[Asociacion de C y L]]. Continuidad: [[Condiciones Iniciales]]. En DC: [[Circuitos DC en Estado Estable]].
