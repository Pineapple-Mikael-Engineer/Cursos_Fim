---
title: Autoinducción
tags:
  - circuitos-electricos
  - teoria
  - acoplamiento-magnetico
draft: false
aliases:
  - autoinducción
  - autoinductancia
  - self-inductance
---

# Autoinducción $\;L$

> [!definicion]
> La **autoinducción** $L$ (en henrios, $\text{H}$) es la propiedad de una bobina de **oponerse a los
> cambios de su propia corriente**: la corriente $i$ crea un flujo magnético que **enlaza a la propia
> bobina** y, por la ley de Faraday, induce en ella una tensión
> $$v=L\,\frac{di}{dt}.$$
> Es la versión "una sola bobina" del [[Inductor| inductor]]: $L$ es la constante de proporcionalidad
> entre el flujo concatenado $\lambda=N\phi$ y la corriente, $L=\lambda/i=N\phi/i$.

> [!info]
> El punto de partida de [[Induccion Magnetica/index| Inducción magnética]] ([[6 Acoplamiento Magnetico/index| capítulo 6]]). Cuando una **segunda** bobina recoge parte del flujo de la primera
> aparece la [[Inductancia Mutua]], y su intensidad relativa la mide el
> [[Coeficiente de Acoplamiento]]. Fraile Mora, cap. 1, §1.19.

---

## Ejemplo

> [!ejemplo]
> **Autoinductancia y tensión inducida de una bobina.**
>
> Una bobina de $N=200$ espiras tiene un flujo de $\phi=0{,}5\ \text{mWb}$ por espira cuando circula
> $i=2\ \text{A}$. Hallar su autoinductancia $L$ y la tensión inducida si la corriente cambia a razón
> de $di/dt=100\ \text{A/s}$.
>
> **Paso 1 — Autoinductancia** (a partir del flujo concatenado $\lambda=N\phi=L\,i$):
> $$L=\frac{N\phi}{i}=\frac{200\cdot 0{,}5\times10^{-3}}{2}=0{,}05\ \text{H}=50\ \text{mH}.$$
>
> **Paso 2 — Tensión inducida** (ley de Faraday con $L$ constante):
> $$v=L\,\frac{di}{dt}=0{,}05\cdot 100=5\ \text{V}.$$
>
> > [!solucion]
> > $L=50\ \text{mH}$ y $v=5\ \text{V}$. La tensión solo aparece **mientras la corriente cambia**: con
> > corriente constante ($di/dt=0$) la bobina ideal se comporta como un cortocircuito.

---

## En qué consiste

> [!teoria] De dónde sale $L$
> La corriente $i$ por la bobina crea un flujo magnético $\phi$ por espira; con $N$ espiras, el **flujo
> concatenado** (o enlazado) es $\lambda=N\phi$. Para medios lineales $\lambda$ es proporcional a $i$,
> y la constante de proporcionalidad es justamente la autoinducción:
> $$L=\frac{\lambda}{i}=\frac{N\phi}{i}.$$
> La ley de Faraday da entonces la tensión en bornes, $v=d\lambda/dt=L\,di/dt$ (con $L$ constante).
> Geométricamente, $L=N^2/\mathcal{R}$ —con $\mathcal{R}$ la **reluctancia** del circuito magnético— o,
> para un solenoide largo, $L=\mu N^2 A/\ell$. Crece con el **cuadrado** del número de espiras. La
> energía almacenada en el campo es $W=\tfrac12 L i^2$.

> [!proposicion] Cómo aumentar $L$
> La autoinductancia escala con $L\propto N^2$: **doblar** las espiras **cuadruplica** $L$. Un núcleo
> **ferromagnético** ($\mu$ grande) reduce la reluctancia $\mathcal{R}$ y por tanto **aumenta mucho**
> $L$ para el mismo número de espiras.

> [!warning]
> La autoinducción es el caso particular del acoplamiento de una bobina **consigo misma**; la
> [[Inductancia Mutua]] es el acoplamiento con **otra** bobina. No confundir el flujo $\phi$ (por
> **espira**) con el flujo **concatenado** $\lambda=N\phi$: en $L=N\phi/i$ interviene $N$ dos veces (una
> en $\lambda=N\phi$ y otra implícita al cerrarse el lazo magnético), de ahí el $N^2$.

## Resumen

> [!resumen]
> | Concepto | Expresión |
> |:---|:---|
> | Autoinductancia | $L=N\phi/i=\lambda/i$ |
> | Geometría / núcleo | $L=N^2/\mathcal{R}=\mu N^2 A/\ell$ |
> | Tensión inducida | $v=L\,di/dt$ |
> | Energía almacenada | $W=\tfrac12 L i^2$ |
> | Dependencia con $N$ | $L\propto N^2$ |

> [!corolario]
> La autoinducción concentra en un solo número $L$ toda la geometría y el material de la bobina: dado
> $L$, la tensión queda fijada por la ley $v=L\,di/dt$ sin volver a los flujos. Es la base sobre la que
> se construye la [[Inductancia Mutua]] cuando aparece una segunda bobina.

> [!referencia]
> Fraile Mora, cap. 1, §1.19. Elemento: [[Inductor]]. Acoplamiento con otra bobina:
> [[Inductancia Mutua]]. Intensidad del acoplamiento: [[Coeficiente de Acoplamiento]]. Contexto:
> [[Induccion Magnetica/index]].
