---
title: Circuitos AC Sinusoidal y Fasores
order: 5
tags:
  - circuitos-electricos
  - teoria
  - sinusoidal
  - fasores
  - index
draft: false
aliases:
  - circuitos AC sinusoidal
  - régimen permanente sinusoidal
  - análisis fasorial
---

# Circuitos AC Sinusoidal y Fasores

> [!definicion]
> En **régimen permanente sinusoidal**, toda tensión y corriente es una senoide de la misma frecuencia, así que basta representarla por un **fasor**: un número complejo $\overline{V}=V\angle \varphi$ que guarda su amplitud y su fase. Con fasores, las derivadas e integrales se vuelven multiplicaciones por $j\omega$, cada elemento adquiere una **impedancia** $Z$, y **todo** el análisis resistivo (Ohm, Kirchhoff, mallas, nodos, Thévenin) se reutiliza —ahora con números complejos—.

> [!info]
> Quinto bloque del curso (sílabo ML 140, semanas 10-11; Fraile Mora, cap. 2). Es el corazón del análisis de CA: toma la senoide del [[4 Ondas Periodicas Sinusoidales/index| capítulo 4]] y la convierte en álgebra compleja, exactamente como [[Laplace en Circuitos/index| Laplace]] hizo con los transitorios. Culmina en la **potencia** en CA.

---

## La idea: congelar la senoide en un número

> [!teoria] Por qué los fasores funcionan
> En un circuito lineal excitado con una senoide, en régimen permanente **todas** las respuestas son senoides de la **misma frecuencia** $\omega$: solo cambian amplitud y fase ([[Onda Sinusoidal| derivar e integrar conserva la senoide]]). Por eso no hace falta arrastrar $\operatorname{sen}\omega t$ en cada paso: se "congela" la senoide en su **fasor** $\overline{V}=V\angle\varphi$ —un vector giratorio detenido en $t=0$— y se opera con él como con un número complejo. → [[Fasores| Fasores]].

> [!teoria] Impedancia: la "resistencia" compleja
> El premio es enorme: la ley de cada elemento se vuelve **algebraica**. La derivada $L\,di/dt$ pasa a $j\omega L\,\overline{I}$, y la integral del condensador a $\overline{I}/(j\omega C)$. Así cada elemento tiene una **impedancia** $Z$ y se cumple la ley de Ohm generalizada $\overline{V}=Z\, \overline{I}$:
> $$Z_R=R,\qquad Z_L=j\omega L,\qquad Z_C=\frac{1}{j\omega C}.$$
> Con $Z=R+jX$ en vez de $R$, **mallas, nodos, divisores y Thévenin valen igual**. → [[Impedancia y Admitancia/index| Impedancia y admitancia]] y [[Analisis Fasorial/index| Análisis fasorial]].

> [!teoria] Y luego, la potencia
> Con tensiones y corrientes desfasadas, la **potencia** en CA se desdobla: la **activa** $P$ (la que trabaja, en W), la **reactiva** $Q$ (la que va y viene en $L$ y $C$, en VAr) y la **aparente** $S$ (el producto de eficaces, en VA). Su relación y el **factor de potencia** son decisivos en instalaciones. → [[Potencia en AC/index| Potencia en AC]].

## Mapa del capítulo

> [!info] Las cuatro secciones
> | Sección | Qué aporta |
> |:---|:---|
> | [[Fasores\| Fasores]] | representar la senoide por un complejo $\overline{V}=V\angle\varphi$ |
> | [[Impedancia y Admitancia/index\| Impedancia y admitancia]] | $Z=R+jX$, $Y=1/Z$; respuesta de R, L, C |
> | [[Analisis Fasorial/index\| Análisis fasorial]] | mallas, nodos y teoremas en complejo; diagramas |
> | [[Potencia en AC/index\| Potencia en AC]] | activa, reactiva, aparente; factor de potencia |

> [!corolario]
> El fasor convierte el régimen sinusoidal en un problema **algebraico complejo**, idéntico en estructura al resistivo. Aprender a pasar al fasor, manejar impedancias y leer la potencia es todo lo que separa la CA de la CC.

> [!referencia]
> Fraile Mora, cap. 2. Viene de [[4 Ondas Periodicas Sinusoidales/index| Ondas periódicas sinusoidales]]; continúa en [[6 Acoplamiento Magnetico/index| Acoplamiento magnético]].
