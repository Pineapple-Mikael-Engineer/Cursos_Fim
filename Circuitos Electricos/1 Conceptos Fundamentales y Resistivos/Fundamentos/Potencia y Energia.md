---
title: Potencia y Energia
order: 3
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - potencia
draft: false
aliases:
  - potencia y energia
  - potencia instantanea
  - power and energy
---

# Potencia y Energía $p=vi$, $W=\displaystyle\int p\,dt$

> [!definicion]
> La **potencia instantánea** en un elemento es el producto de su tensión por su corriente,
> $$p=vi\quad[\text{W}],$$
> el ritmo al que el elemento intercambia energía. Su **signo** depende del [[Convenio de Signos| convenio]] (pasivo: $p>0$ absorbe). La **energía** transferida entre dos instantes es la integral de la potencia,
> $$W=\int_{t_1}^{t_2} p\,dt\quad[\text{J}].$$

---

> [!info]
> Tercera nota de [[Fundamentos/index| Fundamentos]] del [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Cierra la tríada $i$–$v$–$p$ iniciada en [[Variables del Circuito]] y aplica el [[Convenio de Signos]]. La disipación en resistencias se detalla en [[Resistencia y Ley de Ohm]]; la suma global, en [[Balance de Potencias]].

---

## Ejemplo

> [!ejemplo] Energía disipada por un resistor, y caso de potencia variable
> **(a)** Un resistor disipa una potencia **constante** $p=25\ \text{W}$ durante $t=1\ \text{h}$. ¿Cuánta energía consume, en julios y en vatios-hora?
>
> Con potencia constante, $W=p\,t$. En el SI el tiempo va en segundos, $1\ \text{h}=3600\ \text{s}$:
> $$W=p\,t=25\ \text{W}\cdot 3600\ \text{s}=90\,000\ \text{J}=90\ \text{kJ}.$$
> En vatios-hora basta usar el tiempo en horas:
> $$W=25\ \text{W}\cdot 1\ \text{h}=25\ \text{Wh}=0{,}025\ \text{kWh}.$$
>
> > [!solucion]
> > $W=90\ \text{kJ}=25\ \text{Wh}$ (equivalencia: $1\ \text{Wh}=3600\ \text{J}$).
>
> **(b)** Por un elemento (convenio pasivo) circula $i(t)=2t\ \text{A}$ con una tensión constante $v=4\ \text{V}$. Hallar la energía absorbida entre $t_1=0$ y $t_2=3\ \text{s}$.
>
> La potencia instantánea es $p(t)=v\,i(t)=4\cdot 2t=8t\ \text{W}$, creciente con el tiempo. La energía es su integral:
> $$W=\int_0^3 8t\,dt=\Big[\,4t^2\,\Big]_0^3=4\cdot 9=36\ \text{J}.$$
>
> > [!solucion]
> > $W=36\ \text{J}$. Como $p>0$ en todo el intervalo, el elemento **absorbe** energía.

---

## En qué consiste

> [!teoria] De la potencia a la energía
> La potencia $p=vi$ es la derivada de la energía respecto al tiempo, $p=dw/dt$, así que mide el **ritmo** de transferencia, no la cantidad total. Para acumular energía se integra:
> $$W=\int_{t_1}^{t_2} p\,dt.$$
> Cuando $p$ es constante esto se reduce a $W=p\,t$ (área de un rectángulo); cuando $p(t)$ varía, $W$ es el **área bajo la curva** $p(t)$. El signo de $p$ se hereda del convenio: con convenio pasivo, los tramos con $p>0$ aportan energía absorbida y los tramos con $p<0$ energía devuelta. En un resistor $p=vi=Ri^2=v^2/R\ge 0$ siempre, por lo que solo puede absorber (disipar).

> [!info] El kilovatio-hora
> El julio es una unidad de energía pequeña para usos prácticos. En electrotecnia y facturación se usa el **kilovatio-hora** $\text{kWh}$, la energía de $1\ \text{kW}$ durante $1\ \text{h}$:
> $$1\ \text{kWh}=1000\ \text{W}\cdot 3600\ \text{s}=3{,}6\times 10^{6}\ \text{J}=3{,}6\ \text{MJ}.$$
> Es la unidad que aparece en el contador eléctrico de una vivienda.

> [!proposicion] Potencia media
> Para procesos variables interesa la **potencia media** en un intervalo, que es la energía dividida por la duración:
> $$P_{\text{med}}=\frac{W}{t_2-t_1}=\frac{1}{t_2-t_1}\int_{t_1}^{t_2}p\,dt.$$
> En el ejemplo (b), $P_{\text{med}}=36\ \text{J}/3\ \text{s}=12\ \text{W}$, coincidente con el valor de $p$ en el punto medio por ser $p(t)$ lineal.

> [!warning] Vatios y vatios-hora no son lo mismo
> El vatio mide **potencia** (energía por segundo); el vatio-hora mide **energía** (potencia por tiempo). Decir "consume $25\ \text{Wh}$" describe energía acumulada; "consume $25\ \text{W}$" describe el ritmo instantáneo. Confundirlos es el error de unidades más común del capítulo.

---

## Resumen

> [!resumen] Fórmulas de potencia y energía
> | Magnitud | Fórmula | Unidad |
> |:---|:---|:---|
> | Potencia instantánea | $p=vi$ | $\text{W}$ |
> | En un resistor | $p=Ri^2=\dfrac{v^2}{R}\ge 0$ | $\text{W}$ |
> | Energía | $W=\displaystyle\int_{t_1}^{t_2} p\,dt$ | $\text{J}$ |
> | Energía ($p$ constante) | $W=p\,t$ | $\text{J}$ |
> | Potencia media | $P_{\text{med}}=\dfrac{W}{t_2-t_1}$ | $\text{W}$ |
> | Equivalencia | $1\ \text{kWh}=3{,}6\ \text{MJ}$ | — |

> [!corolario]
> La potencia conecta el mundo eléctrico ($v$, $i$) con el energético ($w$). Su signo —vía el convenio— distingue absorber de entregar, y su integral da la energía facturable en kWh.

> [!referencia]
> Fraile Mora, cap. 1, §1.4–1.5. Relacionadas: [[Convenio de Signos]], [[Resistencia y Ley de Ohm]] y [[Balance de Potencias]].
