---
title: Generación de Tensiones Trifásicas
tags:
  - circuitos-electricos
  - teoria
  - trifasico
draft: false
aliases:
  - generación de tensiones trifásicas
  - alternador trifásico
  - three-phase generation
---

# Generación de Tensiones Trifásicas

> [!definicion]
> Las tres tensiones trifásicas se generan en un **alternador** con **tres devanados idénticos** dispuestos a $120^\circ$ en el estator. Al girar el rotor (un imán o electroimán) a velocidad constante $\omega$, su campo induce en cada devanado una fem senoidal de igual amplitud, pero **desfasada $120^\circ$** respecto a la siguiente —porque los devanados están separados $120^\circ$ en el espacio—.

> [!info]
> El origen físico del sistema de [[Fundamentos Trifasicos/index| fundamentos trifásicos]] ([[7 Circuitos Trifasicos/index| capítulo 7]]); es el [[Generacion de Tension Alterna| alternador]] del capítulo 4, **por triplicado**. Fija la [[Secuencia de Fases| secuencia]]. Fraile Mora, cap. 3, §3.2.

---

## Ejemplo

> [!ejemplo]
> **Las tres tensiones de un generador de 50 Hz.**
>
> Un alternador trifásico de $f=50\ \text{Hz}$ y tensión de pico $V_m=311\ \text{V}$. Escribir sus tres tensiones y comprobar que suman cero.
>
> ![[tres_fases.svg|640]]
>
> *Cada devanado, separado $120^\circ$ del siguiente, induce una senoide desfasada $120^\circ$ (izq.). Los tres fasores forman una estrella simétrica (der.).*
>
> **Paso 1 — Las tres tensiones** (con $\omega=2\pi\cdot50=314\ \text{rad/s}$):
> $$v_a=311\operatorname{sen}\omega t,\quad v_b=311\operatorname{sen}(\omega t-120^\circ),\quad v_c=311\operatorname{sen}(\omega t-240^\circ).$$
>
> **Paso 2 — Suma instantánea.** Por la simetría de tres senoides a $120^\circ$,
> $$v_a+v_b+v_c=0\quad\text{en todo instante}.$$
>
> > [!solucion]
> > Tres senoides iguales de $311\ \text{V}$ de pico ($220\ \text{V}$ eficaces), desfasadas $120^\circ$, cuya suma es cero. Esa anulación es lo que permite, en estrella, prescindir (idealmente) del conductor neutro.

---

## En qué consiste

> [!teoria] Por qué $120^\circ$ y no otro ángulo
> El desfase **lo impone la geometría**: tres devanados repartidos uniformemente en la circunferencia del estator ocupan $360^\circ/3=120^\circ$ cada uno. Cuando el polo del rotor pasa frente a un devanado, induce en él su máximo; un tercio de vuelta después ($120^\circ$ de giro = $120^\circ$ eléctricos) pasa frente al siguiente. Así, la fem de cada uno es la del anterior **retrasada $120^\circ$**: es el alternador monofásico ([[Generacion de Tension Alterna]]) repetido tres veces a $120^\circ$.

> [!proposicion] La suma es cero (sistema equilibrado)
> Para tres senoides de igual amplitud a $120^\circ$,
> $$\operatorname{sen}\omega t+\operatorname{sen}(\omega t-120^\circ)+\operatorname{sen}(\omega t-240^\circ)=0,$$
> en todo instante. En fasores, $\overline{V}_a+\overline{V}_b+\overline{V}_c=V(1\angle0^\circ+1\angle {-}120^\circ+1\angle120^\circ)=0$: los tres vectores cierran un triángulo equilátero.

> [!warning]
> Que sumen cero **solo** vale si el sistema está **equilibrado** (igual amplitud y exactamente $120^\circ$). Con tensiones o cargas desiguales, la suma no es cero y aparece corriente por el [[Cargas Desbalanceadas Estrella| neutro]]. Y el desfase de $120^\circ$ es **eléctrico**: en máquinas multipolo no coincide con $120^\circ$ mecánicos.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |:---|:---|
> | Generación | 3 devanados a $120^\circ$, rotor giratorio |
> | Tensiones | $v_a, v_b, v_c$ iguales, desfasadas $120^\circ$ |
> | Fasores | $V\angle0^\circ$, $V\angle{-}120^\circ$, $V\angle{+}120^\circ$ |
> | Suma (equilibrado) | $v_a+v_b+v_c=0$ |

> [!corolario]
> El alternador trifásico convierte la rotación en tres senoides a $120^\circ$ por pura geometría de los devanados. Su simetría —y el hecho de que sumen cero— es la semilla de todas las propiedades del trifásico.

> [!referencia]
> Fraile Mora, cap. 3, §3.2. Base monofásica: [[Generacion de Tension Alterna]]. Orden: [[Secuencia de Fases]]. Ventajas: [[Ventajas del Trifasico]].
