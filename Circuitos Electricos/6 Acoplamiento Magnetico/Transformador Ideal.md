---
title: Transformador Ideal
tags:
  - circuitos-electricos
  - teoria
  - acoplamiento-magnetico
  - transformador
draft: false
aliases:
  - transformador ideal
  - relación de transformación
  - reflejo de impedancias
  - ideal transformer
---

# Transformador Ideal

> [!definicion]
> El **transformador ideal** es el límite de un par de bobinas acopladas **sin pérdidas**, con
> acoplamiento **perfecto** ($k=1$) e inductancias muy grandes. Relaciona primario y secundario solo
> por la **relación de transformación** $a=N_1/N_2$ (número de espiras):
> $$\frac{V_1}{V_2}=\frac{N_1}{N_2}=a,\qquad \frac{I_1}{I_2}=\frac{N_2}{N_1}=\frac{1}{a},$$
> de modo que la potencia se **conserva** ($V_1I_1=V_2I_2$): transforma tensión y corriente sin gastar
> energía.

> [!info]
> El modelo idealizado del [[Transformador con Nucleo de Aire| transformador]] en el
> [[6 Acoplamiento Magnetico/index| capítulo 6]]; surge del [[Inductancia Mutua| acoplo perfecto]] ($k=1$). Su capacidad de **reflejar impedancias** lo hace clave en adaptación. Fraile
> Mora, cap. 1, §1.19.

---

## Ejemplo

> [!ejemplo]
> **Transformar tensión y reflejar una carga.**
>
> Un transformador ideal de relación $N_1:N_2=10:1$ tiene $V_1=2300\ \text{V}$ en el primario y
> alimenta una carga $Z_2=23\ \Omega$. Hallar $V_2$, las corrientes y la impedancia vista desde el
> primario.
>
> ![[transformador_ideal.svg|470]]
>
> *Las tensiones van en relación directa $N_1{:}N_2$ y las corrientes en relación inversa. Los puntos
> fijan las polaridades.*
>
> **Paso 1 — Tensión del secundario.** $V_2=V_1\dfrac{N_2}{N_1}=2300\cdot\dfrac{1}{10}=230\ \text{V}$.
>
> **Paso 2 — Corrientes.** En la carga, $I_2=V_2/Z_2=230/23=10\ \text{A}$; en el primario,
> $I_1=I_2\dfrac{N_2}{N_1}=10\cdot\dfrac{1}{10}=1\ \text{A}$.
>
> **Paso 3 — Impedancia reflejada.** Desde el primario, $Z_1=\dfrac{V_1}{I_1}=\dfrac{2300}{1}=2300\
> \Omega=a^2 Z_2=10^2\cdot23$.
>
> > [!solucion]
> > $V_2=230\ \text{V}$, $I_2=10\ \text{A}$, $I_1=1\ \text{A}$. La carga de $23\ \Omega$ se "ve" desde
> > el primario como $a^2 Z_2=2300\ \Omega$. Y la potencia se conserva: $V_1I_1=2300=V_2I_2$.

---

## En qué consiste

> [!teoria] Las tres relaciones y el porqué
> El transformador ideal hace tres cosas a la vez, todas ligadas a la relación de espiras $a=N_1/N_2$:
> - **Tensión** en relación directa: $V_1=a\,V_2$ (más espiras, más tensión). Sale de que el mismo
>   flujo enlaza $N_1$ y $N_2$ espiras: $v=N\,d\phi/dt$.
> - **Corriente** en relación inversa: $I_1=I_2/a$ (más espiras, menos corriente). Sale de que las
>   fuerzas magnetomotrices se compensan, $N_1 I_1=N_2 I_2$.
> - **Potencia** conservada: $V_1I_1=V_2I_2$ (no disipa ni almacena: el ideal no tiene pérdidas).

> [!teorema] Reflejo de impedancias
> Una impedancia $Z_2$ conectada al secundario se ve desde el primario multiplicada por el cuadrado de
> la relación de transformación:
> $$Z_1=a^2\,Z_2=\left(\frac{N_1}{N_2}\right)^2 Z_2.$$
> Es la propiedad más útil: permite **adaptar** una carga a una fuente (máxima transferencia) eligiendo
> la relación de espiras, sin disipar potencia.

> [!demostracion]
> **Paso 1 — Relaciones.** $V_1=aV_2$ e $I_1=I_2/a$.
> **Paso 2 — Cociente.** $Z_1=\dfrac{V_1}{I_1}=\dfrac{aV_2}{I_2/a}=a^2\dfrac{V_2}{I_2}=a^2 Z_2$.
> $\blacksquare$

> [!info] Eleva o reduce
> - **$N_1>N_2$** ($a>1$): **reductor** —baja la tensión, sube la corriente— (el del ejemplo).
> - **$N_1<N_2$** ($a<1$): **elevador** —sube la tensión, baja la corriente—.
>
> Por eso la energía se transporta a **alta tensión** (baja corriente → menos pérdidas $RI^2$) y se
> **reduce** cerca del consumo.

> [!warning]
> El transformador ideal es una **idealización**: $k=1$, sin resistencia ni pérdidas, $L\to\infty$. Un
> [[Transformador con Nucleo de Aire| transformador real]] tiene $k<1$, resistencias y corriente de
> magnetización. Y **solo transforma alterna**: en CC ($d\phi/dt=0$) no induce nada.

## Resumen

> [!resumen]
> | Magnitud | Relación |
> |:---|:---|
> | Tensiones | $V_1/V_2=N_1/N_2=a$ |
> | Corrientes | $I_1/I_2=N_2/N_1=1/a$ |
> | Potencia | $V_1I_1=V_2I_2$ (conservada) |
> | Impedancia reflejada | $Z_1=a^2 Z_2$ |
> | Reductor / elevador | $a>1$ / $a<1$ |

> [!corolario]
> El transformador ideal transforma tensión y corriente por la relación de espiras, conservando la
> potencia, y refleja impedancias por $a^2$. Esas tres propiedades sostienen el transporte de energía y
> la adaptación de cargas en toda la electrotecnia.

> [!referencia]
> Fraile Mora, cap. 1, §1.19. Caso real: [[Transformador con Nucleo de Aire]]. Hipótesis: [[Inductancia Mutua| coeficiente de acoplamiento]] ($k=1$). Adaptación: [[Maxima Transferencia AC]].
