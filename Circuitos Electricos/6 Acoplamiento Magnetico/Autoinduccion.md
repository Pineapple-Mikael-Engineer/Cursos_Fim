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
> La **autoinducción** $L$ (henrios) es la propiedad de una bobina de **oponerse a los cambios de su
> propia corriente**: la corriente $i$ crea un flujo que **se enlaza a sí mismo** y, por la ley de
> Faraday, induce en la bobina una tensión
> $$v=L\,\frac{di}{dt},\qquad L=\frac{\lambda}{i}=\frac{N\phi}{i}.$$
> Es el caso "una sola bobina" del [[Inductor]]; aquí se la mira como **punto de partida** del
> acoplamiento entre dos bobinas.

> [!info]
> Base del [[6 Acoplamiento Magnetico/index| acoplamiento magnético]]. La construcción del elemento
> (relación $L=N^2/\mathcal{R}=\mu N^2A/\ell$, dependencia $L\propto N^2$, energía $\tfrac12 Li^2$) se
> desarrolla en [[Inductor]]; cuando una **segunda** bobina recoge parte del flujo aparece la
> [[Inductancia Mutua]]. Fraile Mora, cap. 1, §1.19.

---

## Ejemplo

> [!ejemplo]
> **Autoinductancia y tensión inducida.** Una bobina de $N=200$ espiras tiene $\phi=0{,}5\ \text{mWb}$
> por espira con $i=2\ \text{A}$. Hallar $L$ y la tensión inducida si $di/dt=100\ \text{A/s}$.
>
> $$L=\frac{N\phi}{i}=\frac{200\cdot 0{,}5\times10^{-3}}{2}=0{,}05\ \text{H}=50\ \text{mH},\qquad
> v=L\frac{di}{dt}=0{,}05\cdot 100=5\ \text{V}.$$
>
> > [!solucion]
> > $L=50\ \text{mH}$, $v=5\ \text{V}$. La tensión solo aparece **mientras la corriente cambia**: con
> > $di/dt=0$ la bobina ideal es un cortocircuito.

---

## El puente hacia la inducción mutua

> [!teoria]
> La autoinducción es el acoplamiento de una bobina **consigo misma**: su flujo concatenado
> $\lambda=N\phi$ es proporcional a su corriente, y $L=\lambda/i$ es la constante. La
> [[Inductancia Mutua]] es la **misma idea** aplicada a **otra** bobina: la fracción del flujo de la
> primera que enlaza a la segunda induce en ella $v_2=M\,di_1/dt$. Por eso $L$ y $M$ comparten
> unidades (henrios) y, en el par acoplado, cada tensión suma su término propio ($L$) y el mutuo ($M$).

> [!warning]
> No confundir el flujo $\phi$ (por **espira**) con el concatenado $\lambda=N\phi$: por eso $L\propto
> N^2$ (ver [[Inductor]]). La autoinducción es **siempre $\ge0$**; el término mutuo, en cambio, puede
> sumar o restar según la [[Regla de los Puntos]].

> [!referencia]
> Fraile Mora, cap. 1, §1.19. Elemento (derivación completa): [[Inductor]]. Acoplamiento con otra
> bobina: [[Inductancia Mutua]]. Energía del par: [[Energia en Bobinas Acopladas]].
