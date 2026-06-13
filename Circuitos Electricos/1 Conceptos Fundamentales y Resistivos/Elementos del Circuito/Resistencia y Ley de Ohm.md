---
title: Resistencia y Ley de Ohm
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - resistencia
draft: false
aliases:
  - resistencia
  - ley de ohm
  - conductancia
  - resistor
  - resistance
  - ohm's law
  - conductance
---

# Resistencia y Ley de Ohm $v=Ri$

> [!definicion]
> La **resistencia** $R$ es el elemento pasivo que se opone al paso de la corriente y disipa su
> energía en forma de calor. Su comportamiento lo describe la **ley de Ohm**, la relación
> **algebraica y lineal** entre la tensión en bornes y la corriente que lo atraviesa
> $$v=Ri,$$
> con $R$ medida en ohmios ($\Omega$). Por ser algebraica (no diferencial), es la pieza que hace que
> los circuitos puramente resistivos se resuelvan con simple álgebra.

---

> [!info]
> Primera nota de [[Elementos del Circuito/index| Elementos del circuito]], en el
> [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Usa el convenio de signos y la
> potencia de [[Potencia y Energia]]; es la base de la [[Resistencias en Serie y Paralelo| reducción de resistencias]] y se opone a la fuente, el elemento activo de
> [[Elementos Activos y Pasivos]].

---

## Ejemplo

> [!ejemplo] Una resistencia en convenio pasivo
> Por una resistencia de $R=100\ \Omega$ circula una corriente $i=0.5\ \text{A}$ que **entra por el
> borne $+$** de la tensión $v$ (convenio pasivo). Calculamos la tensión y la potencia.
>
> ![[simbolo_resistencia.svg|300]]
> Resistencia en convenio pasivo: la corriente $i$ entra por el borne $+$ de $v$.
>
> **Tensión** por la ley de Ohm:
> $$v=Ri=100\ \Omega\times 0.5\ \text{A}=50\ \text{V}.$$
>
> **Potencia** disipada (convenio pasivo, $p>0$ significa que **absorbe**):
> $$p=vi=50\ \text{V}\times 0.5\ \text{A}=25\ \text{W},$$
> que coincide, como debe, con
> $$p=Ri^2=100\times(0.5)^2=25\ \text{W}=\frac{v^2}{R}=\frac{50^2}{100}=25\ \text{W}.$$
>
> La resistencia absorbe $25\ \text{W}$ y los convierte íntegramente en calor.

---

## En qué consiste

> [!teoria] Resistencia, conductancia y disipación
> La **ley de Ohm** afirma que en un resistor la tensión es **proporcional** a la corriente,
> $$v=Ri.$$
> La constante de proporcionalidad $R$ es la **resistencia** ($\Omega$). Por ser una recta que pasa
> por el origen, el resistor es un elemento **lineal**: duplicar la corriente duplica la tensión.
>
> A veces conviene la relación inversa. Se define la **conductancia**
> $$G=\frac{1}{R}\quad[\text{S}]\quad(\text{siemens}),$$
> con lo que la ley de Ohm se escribe $i=Gv$. Una resistencia grande (poca corriente para mucha
> tensión) equivale a una conductancia pequeña.
>
> La resistencia **siempre disipa**. Sustituyendo la ley de Ohm en $p=vi$ se obtiene
> $$p=vi=Ri^2=\frac{v^2}{R}\ge 0,$$
> y al ser un cuadrado el resultado nunca es negativo: en convenio pasivo $p\ge0$, de modo que la
> resistencia **absorbe** energía en todo instante y la entrega al entorno como calor (efecto Joule).
> Nunca la devuelve al circuito; en eso se distingue de los elementos que la almacenan.

> [!proposicion] De qué depende el valor de $R$
> La resistencia no es solo un número abstracto: depende de la geometría y el material del conductor.
> Para un conductor homogéneo de longitud $\ell$ y sección $A$,
> $$R=\rho\,\frac{\ell}{A},$$
> donde $\rho$ es la **resistividad** del material ($\Omega\cdot\text{m}$). El conductor es más
> resistivo cuanto más largo, cuanto más estrecho y cuanto peor conductor es el material. Su inversa
> $\sigma=1/\rho$ es la **conductividad**.

> [!info] El resistor óhmico
> Un dispositivo es **óhmico** cuando su característica $v$-$i$ es una **recta por el origen**: $R$ es
> constante e independiente de $v$ o $i$. Su pendiente es justamente $R$ (o $1/G$). Los dispositivos
> cuya característica $v$-$i$ se **curva** (diodos, lámparas a alta temperatura) son **no óhmicos**;
> en ellos $R$ deja de ser una constante y el análisis lineal de este capítulo no se aplica
> directamente.

> [!warning]
> Dos límites conceptuales útiles. Una resistencia **nula** ($R=0$) es un **cortocircuito**:
> $v=0$ sea cual sea la corriente. Una resistencia **infinita** ($R\to\infty$, $G=0$) es un
> **circuito abierto**: $i=0$ sea cual sea la tensión. Confundir uno con otro invierte por completo
> el resultado del análisis.

---

## Resumen

> [!resumen] Lo esencial
> | Magnitud | Símbolo | Relación | Unidad |
> |:---|:---:|:---|:---:|
> | Resistencia | $R$ | $v=Ri$ | $\Omega$ |
> | Conductancia | $G$ | $i=Gv$, $G=1/R$ | $\text{S}$ |
> | Potencia disipada | $p$ | $p=Ri^2=v^2/R\ge0$ | $\text{W}$ |
> | Resistividad | $\rho$ | $R=\rho\,\ell/A$ | $\Omega\cdot\text{m}$ |

> [!corolario]
> La ley de Ohm es **algebraica**: relaciona $v$ e $i$ en el **mismo instante**, sin derivadas ni
> integrales. Por eso una red de resistencias y fuentes se resuelve con un sistema de ecuaciones
> lineales, no con ecuaciones diferenciales. Esta es la razón profunda de que los circuitos
> resistivos sean el punto de partida del curso.

> [!referencia]
> Fraile Mora, cap. 1, §1.3. Continúa con [[Fuentes Independientes]] y con la
> [[Resistencias en Serie y Paralelo| reducción de resistencias]].
