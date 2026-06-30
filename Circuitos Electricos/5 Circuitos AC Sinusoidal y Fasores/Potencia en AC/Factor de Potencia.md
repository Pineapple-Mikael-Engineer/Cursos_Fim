---
title: Factor de Potencia
tags:
  - circuitos-electricos
  - teoria
  - potencia
  - factor-potencia
draft: false
aliases:
  - factor de potencia
  - cos fi
  - power factor
---

# Factor de Potencia $\;\cos\varphi=\dfrac{P}{S}$

> [!definicion]
> El **factor de potencia (FP)** es el cociente entre la potencia **activa** y la **aparente**,
> $$\text{FP}=\cos\varphi=\frac{P}{\lvert S\rvert}=\frac{P}{VI},$$
> y mide qué fracción de la potencia que entrega la red es **útil**. Vale entre $0$ y $1$: $\text{FP}=1$ (carga resistiva, todo es activa) es ideal; un FP bajo significa mucha potencia reactiva circulando sin trabajar. Se especifica como **inductivo** (en atraso) o **capacitivo** (en adelanto).

> [!info]
> La medida de eficiencia de la [[Potencia en AC/index| potencia en CA]] ([[5 Circuitos AC Sinusoidal y Fasores/index| capítulo 5]]); es el coseno del ángulo del triángulo de [[Potencia en Regimen Sinusoidal]]. Cuando es bajo, se [[Correccion del Factor de Potencia| corrige]]. Fraile Mora, cap. 2, §2.11.

---

## Ejemplo

> [!ejemplo]
> **El precio de un FP bajo.**
>
> Una carga consume $P=1200\ \text{W}$ a $V=100\ \text{V}$. Comparar la corriente con factor de potencia $\cos\varphi=0{,}6$ (inductivo) frente a $\cos\varphi=1$.
>
> ![[triangulo_potencias.svg|450]]
>
> *Para una misma $P$ (cateto horizontal), cuanto menor es $\cos\varphi$ mayor es la hipotenusa $S$ —y con ella la corriente que hay que transportar.*
>
> **Paso 1 — Con $\cos\varphi=0{,}6$.** $S=\dfrac{P}{\cos\varphi}=\dfrac{1200}{0{,}6}=2000\ \text{VA}$, y la corriente $I=\dfrac{S}{V}=\dfrac{2000}{100}=20\ \text{A}$.
>
> **Paso 2 — Con $\cos\varphi=1$.** $S=P=1200\ \text{VA}$, $I=\dfrac{1200}{100}=12\ \text{A}$.
>
> > [!solucion]
> > Con FP $0{,}6$ la red transporta $20\ \text{A}$ para entregar los mismos $1200\ \text{W}$ que con FP $1$ necesitarían solo $12\ \text{A}$: un **67 % más de corriente**, con más pérdidas $RI^2$ y cables más gruesos. Por eso un FP bajo se penaliza y se corrige.

---

## En qué consiste

> [!teoria] Qué significa y por qué importa
> El FP es el **coseno del desfase** $\varphi$ entre tensión y corriente. Como $P=VI\cos\varphi$, para una potencia activa dada:
> $$I=\frac{P}{V\cos\varphi},$$
> es decir, **cuanto menor es $\cos\varphi$, mayor es la corriente** necesaria. Esa corriente extra no hace trabajo (es reactiva), pero **sí** calienta los conductores ($RI^2$), satura transformadores y ocupa capacidad de la red. De ahí que las compañías **penalicen** un FP bajo.

> [!info] Inductivo vs. capacitivo
> El FP por sí solo no distingue si la corriente atrasa o adelanta; por eso se añade el calificativo:
> - **FP en atraso (inductivo):** $\overline{I}$ atrasa a $\overline{V}$, $Q>0$. Es el caso habitual (motores, transformadores, balastos).
> - **FP en adelanto (capacitivo):** $\overline{I}$ adelanta, $Q<0$. Menos común (líneas largas en vacío, exceso de condensadores).
>
> Dos cargas con $\cos\varphi=0{,}8$ pueden ser opuestas (una inductiva, otra capacitiva): hay que indicar siempre el sentido.

> [!proposicion] FP, potencias y ángulo
> Del triángulo de potencias salen todas las relaciones:
> $$\cos\varphi=\frac{P}{S},\quad \operatorname{sen}\varphi=\frac{Q}{S},\quad \tan\varphi=\frac{Q}{P}.$$
> Mejorar el FP es **reducir $\varphi$** (acercar $Q$ a cero) **sin cambiar $P$**.

> [!warning]
> FP $=1$ no significa "máxima potencia", sino que **toda** la aparente es activa (nada de reactiva). Y un FP alto no implica eficiencia energética del aparato: mide el **desfase**, no el rendimiento de conversión. El calificativo inductivo/capacitivo es imprescindible.

## Resumen

> [!resumen]
> | Concepto | Expresión |
> |:---|:---|
> | Factor de potencia | $\cos\varphi=P/S$ |
> | Corriente para un $P$ | $I=P/(V\cos\varphi)$ |
> | Inductivo / capacitivo | $Q>0$ (atraso) / $Q<0$ (adelanto) |
> | Relaciones | $\operatorname{sen}\varphi=Q/S$, $\tan\varphi=Q/P$ |

> [!corolario]
> El factor de potencia condensa en un número la eficiencia de la transferencia: a igual potencia útil, un FP bajo cuesta corriente, pérdidas e instalación. Subirlo —[[Correccion del Factor de Potencia| corregirlo]]— es directo y rentable.

> [!referencia]
> Fraile Mora, cap. 2, §2.11. Base: [[Potencia en Regimen Sinusoidal]]. Solución al FP bajo: [[Correccion del Factor de Potencia]].
