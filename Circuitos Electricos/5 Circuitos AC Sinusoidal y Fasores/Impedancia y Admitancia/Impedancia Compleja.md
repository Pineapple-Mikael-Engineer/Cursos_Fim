---
title: Impedancia Compleja
tags:
  - circuitos-electricos
  - teoria
  - impedancia
draft: false
aliases:
  - impedancia compleja
  - impedancia
  - reactancia
  - complex impedance
---

# Impedancia Compleja $\;Z=R+jX$

> [!definicion]
> La **impedancia** de un elemento o circuito en régimen sinusoidal es el cociente de sus fasores de
> tensión y corriente,
> $$Z=\frac{\overline{V}}{\overline{I}}=R+jX\quad[\Omega],$$
> con parte real la **resistencia** $R$ (disipa, en fase) y parte imaginaria la **reactancia** $X$
> (desfasa $90^\circ$, almacena). Su **módulo** $|Z|=\sqrt{R^2+X^2}$ es cuánto se opone al paso de
> corriente, y su **argumento** $\varphi=\arctan(X/R)$ es el desfase que introduce.

> [!info]
> El concepto central de [[Impedancia y Admitancia/index| Impedancia y admitancia]] ([[5 Circuitos AC Sinusoidal y Fasores/index| capítulo 5]]). Resume en un complejo los desfases de
> [[Fasores]]; su inversa es la [[Admitancia]]. Fraile Mora, cap. 2, §2.7.

---

## Ejemplo

> [!ejemplo]
> **Impedancia de una rama RL serie.**
>
> Una resistencia $R=3\ \Omega$ en serie con un inductor de reactancia $X_L=\omega L=4\ \Omega$, a la
> frecuencia de trabajo. Hallar su impedancia.
>
> ![[triangulo_impedancia.svg|470]]
>
> *La impedancia se representa como un vector en el plano complejo: $R$ en el eje real, $X$ en el
> imaginario, $Z$ la hipotenusa. Su ángulo $\varphi$ es el desfase entre tensión y corriente.*
>
> **Paso 1 — Forma rectangular.** $Z=R+jX_L=3+j4\ \Omega$.
>
> **Paso 2 — Módulo y ángulo.**
> $$|Z|=\sqrt{3^2+4^2}=5\ \Omega,\qquad \varphi=\arctan\frac{4}{3}\approx53^\circ.$$
>
> > [!solucion]
> > $Z=3+j4=5\angle53^\circ\ \Omega$. Ante una tensión $\overline{V}$, la corriente es
> > $\overline{I}=\overline{V}/Z$: su módulo se divide por $5$ y su fase atrasa $53^\circ$ (carga
> > **inductiva**, la corriente va por detrás de la tensión).

---

## En qué consiste

> [!teoria] Resistencia y reactancia
> La impedancia separa dos comportamientos:
> - **Resistencia $R$** (real, $\ge0$): la oposición que **disipa** energía; tensión y corriente en
>   fase. No depende de la frecuencia.
> - **Reactancia $X$** (imaginaria): la oposición que **desfasa** $90^\circ$ sin disipar; **sí**
>   depende de la frecuencia:
>   $$X_L=\omega L\ (>0,\ \text{inductiva}),\qquad X_C=-\frac{1}{\omega C}\ (<0,\ \text{capacitiva}).$$
>   Una reactancia **positiva** (neta inductiva) hace que la corriente **atrase**; una **negativa**
>   (capacitiva), que **adelante**.

> [!proposicion] Las impedancias elementales
> | Elemento | $Z$ | $\lvert Z\rvert$ | desfase |
> |:---|:---|:---|:---|
> | Resistencia | $R$ | $R$ | $0^\circ$ |
> | Inductor | $j\omega L$ | $\omega L$ | $+90^\circ$ |
> | Condensador | $\dfrac{1}{j\omega C}=-\dfrac{j}{\omega C}$ | $\dfrac{1}{\omega C}$ | $-90^\circ$ |
>
> El inductor "pesa" más a alta frecuencia ($X_L\propto\omega$); el condensador, a baja
> ($\lvert X_C\rvert\propto1/\omega$).

> [!teoria] El triángulo de impedancias
> Representar $Z=R+jX$ en el plano complejo da un triángulo rectángulo: cateto horizontal $R$, cateto
> vertical $X$, hipotenusa $|Z|$ y ángulo $\varphi$. Ese mismo ángulo es el **desfase tensión-corriente**
> y, más adelante, el ángulo del **factor de potencia** $\cos\varphi$ ([[Factor de Potencia]]): el
> triángulo de impedancias y el de potencias son semejantes.

> [!warning]
> La impedancia es un número complejo, pero **no** un fasor: no representa una senoide, sino una
> **relación** entre dos (tensión y corriente). Por eso no "gira" con $e^{j\omega t}$. Y depende de la
> **frecuencia**: a otra $\omega$, otra $Z$.

## Resumen

> [!resumen]
> | Magnitud | Expresión |
> |:---|:---|
> | Impedancia | $Z=\overline{V}/\overline{I}=R+jX$ |
> | Módulo | $\lvert Z\rvert=\sqrt{R^2+X^2}$ |
> | Ángulo (desfase) | $\varphi=\arctan(X/R)$ |
> | Reactancia inductiva | $X_L=\omega L$ |
> | Reactancia capacitiva | $X_C=-1/\omega C$ |

> [!corolario]
> La impedancia compleja es la "resistencia" de la CA: dice cuánto se opone al paso de corriente
> ($|Z|$) y cuánto la desfasa ($\varphi$) en un solo número. Con ella, la ley de Ohm $\overline{V}=Z
> \overline{I}$ y todos los métodos resistivos valen en alterna.

> [!referencia]
> Fraile Mora, cap. 2, §2.7. Origen físico: [[Respuesta de Elementos Pasivos]]. Inversa: [[Admitancia]].
> Se asocia en [[Asociacion de Impedancias]].
