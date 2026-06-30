---
title: Acoplamiento Magnético Fasorial
tags:
  - circuitos-electricos
  - teoria
  - acoplamiento-magnetico
  - fasores
draft: false
aliases:
  - acoplamiento magnético fasorial
  - reactancia mutua
  - bobinas acopladas en alterna
  - coupled circuits in AC
---

# Acoplamiento Magnético Fasorial

> [!definicion]
> En **régimen sinusoidal**, un par de bobinas acopladas se describe con **fasores**: la derivada $d/dt$ pasa a $j\omega$, de modo que la **reactancia mutua** vale $j\omega M$ y las ecuaciones del par acoplado se vuelven **algebraicas**,
> $$\overline{V}_1=j\omega L_1\,\overline{I}_1\pm j\omega M\,\overline{I}_2,\qquad
> \overline{V}_2=\pm j\omega M\,\overline{I}_1+j\omega L_2\,\overline{I}_2.$$
> El signo $\pm$ del término mutuo lo fija la [[Regla de los Puntos]] (suma si las dos corrientes entran por los puntos, resta en caso contrario).

> [!info]
> Lleva la [[Inductancia Mutua]] al [[5 Circuitos AC Sinusoidal y Fasores/index| régimen fasorial]], dentro del [[6 Acoplamiento Magnetico/index| capítulo 6]]: con ello el transformador se analiza con [[Impedancia Compleja| impedancias]] y todos los métodos resistivos valen en alterna. Fraile Mora, cap. 1, §1.19.

---

## Del tiempo al fasor

> [!ejemplo]
> El mismo caso del **secundario abierto** de [[Inductancia Mutua]] ($\overline{I}_2=0$), en fasores: con $\omega L_1=4\ \Omega$, $\omega M=6\ \Omega$ e $\overline{I}_1=2\angle0^\circ$,
> $$\overline{V}_1=j\omega L_1\,\overline{I}_1=8\angle90^\circ\ \text{V},\qquad
> \overline{V}_2=j\omega M\,\overline{I}_1=12\angle90^\circ\ \text{V}.$$
> Ambas **adelantan $90^\circ$** a $\overline{I}_1$ (el factor $j$): el secundario abierto no consume, pero "ve" una tensión inducida $\propto\omega M$. El paso clave es $d/dt\to j\omega$; lo demás es idéntico a la versión en el tiempo.

---

## En qué consiste

> [!teoria] La reactancia mutua acopla las mallas
> La reactancia mutua $X_M=\omega M$ enlaza las dos mallas: la corriente de **una** bobina provoca una caída de tensión $j\omega M$ en la malla de la **otra**. En la práctica, al plantear las ecuaciones de malla del circuito acoplado se trata cada término $j\omega M\,\overline{I}$ como una **fuente de tensión dependiente** (controlada por la corriente de la otra malla), con su **signo** dado por los puntos. Una vez escritas las dos ecuaciones, todo el [[5 Circuitos AC Sinusoidal y Fasores/index| análisis fasorial]] habitual —mallas, nodos, Thévenin— se aplica sin cambios.

> [!proposicion] Impedancia reflejada
> Si el secundario alimenta una carga $Z_L$, la impedancia que ve el primario es
> $$\overline{Z}_{in}=j\omega L_1+\frac{(\omega M)^2}{j\omega L_2+Z_L}.$$
> El primer término es la reactancia propia del primario; el segundo es la **impedancia reflejada**: el efecto del secundario "visto" desde el primario a través del acoplo. Crece con $(\omega M)^2$, es decir, con el cuadrado de la reactancia mutua. Lo desarrolla en detalle [[Transformador con Nucleo de Aire]].

> [!warning]
> La reactancia mutua es $j\omega M$ —**positiva imaginaria** y nunca se olvida el $j$—, pero su **signo** en las ecuaciones del par lo fijan los puntos, no su naturaleza. Además **depende de la frecuencia**: a mayor $\omega$, mayor acoplo (más tensión inducida por la misma corriente). En continua ($\omega=0$) no hay inducción mutua.

## Resumen

> [!resumen]
> | Magnitud | Expresión |
> |:---|:---|
> | Ecuación del primario | $\overline{V}_1=j\omega L_1\,\overline{I}_1\pm j\omega M\,\overline{I}_2$ |
> | Ecuación del secundario | $\overline{V}_2=\pm j\omega M\,\overline{I}_1+j\omega L_2\,\overline{I}_2$ |
> | Reactancia mutua | $X_M=\omega M$ (término $j\omega M$) |
> | Signo del término mutuo | lo fija la [[Regla de los Puntos]] |
> | Impedancia reflejada | $\overline{Z}_{in}=j\omega L_1+\dfrac{(\omega M)^2}{j\omega L_2+Z_L}$ |

> [!corolario]
> En alterna, el par de bobinas acopladas se reduce a dos ecuaciones algebraicas con un término de acoplo $j\omega M\,\overline{I}$ tratado como fuente dependiente. Así el circuito magnéticamente acoplado se analiza con las mismas herramientas fasoriales que cualquier red, y el efecto de la carga del secundario se condensa en la impedancia reflejada.

> [!referencia]
> Fraile Mora, cap. 1, §1.19. Origen en continua: [[Inductancia Mutua]]. Signos: [[Regla de los Puntos]]. Herramienta de cálculo: [[Impedancia Compleja]]. Aplicación: [[Transformador con Nucleo de Aire]].
