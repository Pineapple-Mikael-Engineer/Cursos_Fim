---
title: Potencia en AC
tags:
  - circuitos-electricos
  - teoria
  - potencia
  - index
draft: false
aliases:
  - potencia en AC
  - potencia en corriente alterna
  - potencia activa reactiva aparente
---

# Potencia en AC

> [!definicion]
> En corriente alterna, como la tensión y la corriente están **desfasadas**, la potencia se desdobla
> en tres: la **activa** $P$ (W), la que realmente **trabaja** (se disipa o se convierte); la
> **reactiva** $Q$ (VAr), la que **va y viene** entre la fuente y los campos de $L$ y $C$ sin trabajo
> neto; y la **aparente** $S$ (VA), el producto de los valores eficaces. Forman el **triángulo de
> potencias** $S=P+jQ$, y su cociente, el **factor de potencia** $\cos\varphi=P/S$, mide cuánta es
> útil.

> [!info]
> Cuarta y última sección del [[5 Circuitos AC Sinusoidal y Fasores/index| capítulo 5]] y culminación
> del análisis de CA. Usa los [[Fasores| fasores]], la [[Impedancia Compleja| impedancia]] y
> el [[Valor Eficaz RMS| valor eficaz]]. Es la base de toda la ingeniería de potencia. Fraile Mora,
> cap. 2, §2.9-2.14.

---

## Tres potencias, un triángulo

> [!teoria] De la potencia instantánea a las tres potencias
> La potencia instantánea $p(t)=v(t)\,i(t)$ **oscila** al doble de la frecuencia ($2\omega$); su valor
> **medio** es la potencia **activa** $P=V_{ef}I_{ef}\cos\varphi$ (→ [[Potencia Instantanea]]). Esa
> media depende del desfase $\varphi$:
> - en la **resistencia** ($\varphi=0$) la potencia es siempre positiva: **se disipa** toda;
> - en el **inductor** y el **condensador** ($\varphi=\pm90^\circ$) la media es **cero**: la energía
>   solo se almacena y se devuelve. → [[Potencia en Elementos Puros]].
>
> La parte que va y viene es la potencia **reactiva** $Q=V_{ef}I_{ef}\operatorname{sen}\varphi$, y el
> producto de eficaces es la **aparente** $S=V_{ef}I_{ef}$. → [[Potencia en Sinuidal y Fasorial]] y
> [[Potencia Compleja]].

> [!teoria] El factor de potencia y por qué corregirlo
> El **factor de potencia** $\cos\varphi=P/S$ dice qué fracción de la potencia aparente es útil. Un
> FP bajo (carga muy inductiva) obliga a transportar **más corriente** para entregar el mismo $P$,
> aumentando pérdidas y costes. Conectar un **condensador** que aporte la $Q$ que falta **corrige** el
> factor de potencia sin tocar el $P$. → [[Factor de Potencia]] y [[Correccion del Factor de Potencia]].
> Y la condición de **máxima transferencia** se generaliza a $Z_L=Z_{Th}^{*}$ →
> [[Maxima Transferencia AC]].

## Mapa de la sección

> [!info] Las notas de esta sección
> | Nota | Contenido |
> |:---|:---|
> | [[Potencia Instantanea]] | $p(t)=vi$; oscila a $2\omega$; media $=P$ |
> | [[Potencia en Elementos Puros]] | R disipa; L y C de media nula |
> | [[Potencia en Sinuidal y Fasorial]] | activa $P$, reactiva $Q$, aparente $S$ |
> | [[Potencia Compleja]] | $S=\overline{V}\,\overline{I}^{*}=P+jQ$; triángulo |
> | [[Factor de Potencia]] | $\cos\varphi=P/S$; inductivo vs capacitivo |
> | [[Correccion del Factor de Potencia]] | el condensador que reduce $Q$ |
> | [[Maxima Transferencia AC]] | $Z_L=Z_{Th}^{*}$ |

> [!corolario]
> En CA la potencia tiene tres caras —activa, reactiva, aparente— ligadas por el triángulo $S=P+jQ$. El
> factor de potencia mide la eficiencia de la transferencia, y corregirlo es una de las tareas más
> rentables de la ingeniería eléctrica.

> [!referencia]
> Fraile Mora, cap. 2, §2.9-2.14. Anterior: [[Analisis Fasorial/index| Análisis fasorial]]. Cierra el
> [[5 Circuitos AC Sinusoidal y Fasores/index| capítulo 5]].
