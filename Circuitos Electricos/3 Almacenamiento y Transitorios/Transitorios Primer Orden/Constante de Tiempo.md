---
title: Constante de Tiempo
tags:
  - circuitos-electricos
  - teoria
  - transitorios
  - primer-orden
  - constante-tiempo
draft: false
aliases:
  - constante de tiempo
  - tau
  - time constant
---

# Constante de Tiempo

> [!definicion]
> La **constante de tiempo** $\tau$ mide la **rapidez** de un transitorio de primer orden. Vale $\tau=RC$ en un [[Circuito RC]] y $\tau=L/R$ en un [[Circuito RL]]; en ambos casos tiene unidades de **segundos** ($\Omega\cdot\text{F}=\text{s}$, $\text{H}/\Omega=\text{s}$). En un tiempo $\tau$ la variable completa el $63{,}2\%$ de su cambio total ($1-e^{-1}$), y tras $5\tau$ el transitorio se considera **extinguido** ($99{,}3\%$).

> [!info]
> Parámetro central de los [[Transitorios Primer Orden/index| transitorios de primer orden]] del [[3 Almacenamiento y Transitorios/index| capítulo 3]]; aparece en la fórmula de la [[Respuesta Completa Primer Orden]] como el factor $e^{-t/\tau}$. Se calcula con la resistencia equivalente del [[Teorema de Thevenin| equivalente de Thévenin]] vista por el elemento almacenador. Fraile Mora, cap. 4, §4.5.

---

## Ejemplo

> [!ejemplo]
> **La curva universal $1-e^{-t/\tau}$.**
>
> Interpretar la curva normalizada del cambio de una variable de primer orden hacia su valor final. Se trata de leer qué fracción del cambio total se ha completado tras $\tau$, $2\tau$, $3\tau$ y $5\tau$, y de entender el papel de la **tangente en el origen**.
>
> ![[constante_tiempo.svg|620]]
>
> *La fracción del cambio total: $63{,}2\%$ en $\tau$, $86{,}5\%$ en $2\tau$, $95\%$ en $3\tau$, $99{,}3\%$ en $5\tau$. La tangente en el origen alcanza el valor final justo en $t=\tau$.*
>
> **Lectura de la curva.** La pendiente inicial de la exponencial es $1/\tau$: si ese ritmo de arranque se mantuviera constante, la variable llegaría a su valor final exactamente en $t=\tau$. Pero el ritmo se frena conforme nos acercamos al valor final, de modo que en $\tau$ solo se ha cubierto el $63{,}2\%$. Cada $\tau$ adicional recupera el $63{,}2\%$ **de lo que faltaba**, y por eso el avance se acelera en porcentaje acumulado pero nunca termina en tiempo finito.
>
> **Régimen permanente.** A efectos prácticos, a los $5\tau$ el cambio está al $99{,}3\%$ y se asume **régimen permanente**: el transitorio se da por extinguido y la variable se toma igual a su valor final.
>
> > [!solucion]
> > Fracción del cambio total completada en cada múltiplo de $\tau$:
> >
> > | Tiempo | $1-e^{-t/\tau}$ | Cambio completado | Falta |
> > |:---|:---|:---|:---|
> > | $\tau$ | $1-e^{-1}$ | $63{,}2\%$ | $36{,}8\%$ |
> > | $2\tau$ | $1-e^{-2}$ | $86{,}5\%$ | $13{,}5\%$ |
> > | $3\tau$ | $1-e^{-3}$ | $95{,}0\%$ | $5{,}0\%$ |
> > | $5\tau$ | $1-e^{-5}$ | $99{,}3\%$ | $0{,}7\%$ |
> >
> > Tras $5\tau$ se considera el transitorio extinguido (régimen permanente).

---

## En qué consiste

> [!teoria] Significado físico
> La constante de tiempo $\tau$ es el **tiempo característico de relajación** del circuito: marca la escala temporal en la que el sistema olvida su condición inicial y se acomoda a su valor final. Cuanto **mayor** es $\tau$, más **lento** es el transitorio.
>
> Visto sobre el decaimiento puro $e^{-t/\tau}$, la variable cae a $1/e\approx37\%$ de su valor en cada intervalo de duración $\tau$: queda un $37\%$ tras $\tau$, un $37\%$ de ese $37\%$ tras $2\tau$, y así sucesivamente. La **tangente en el origen** ofrece la interpretación complementaria: tiene pendiente $\pm1/\tau$, de modo que si el ritmo inicial del cambio se mantuviera, el transitorio terminaría exactamente en $t=\tau$.

> [!proposicion] Medir $\tau$ a partir de una curva experimental
> Dada una respuesta medida en el laboratorio, $\tau$ se lee de tres formas equivalentes:
> - **(a) Por el $63\%$:** $\tau$ es la abscisa donde la variable alcanza el $63{,}2\%$ de su cambio total (subida hacia el valor final).
> - **(b) Por la tangente:** $\tau$ es el punto donde la **tangente inicial** corta el valor final.
> - **(c) En decaimiento:** $\tau$ es el instante en que la variable cae al $37\%$ de su valor inicial.

> [!algoritmo] Calcular $\tau$ de un circuito
> **Paso 1 —** Hallar la **resistencia equivalente** $R_{eq}$ vista por el elemento almacenador desde sus bornes (su [[Teorema de Thevenin| equivalente de Thévenin]]), con las **fuentes anuladas** (cortocircuito las de tensión, abiertas las de corriente). **Paso 2 —** Aplicar la fórmula según el tipo:
> - [[Circuito RC]]: $\tau=R_{eq}\,C$.
> - [[Circuito RL]]: $\tau=L/R_{eq}$.

> [!warning]
> En $\tau$ interviene la $R_{eq}$ que **ve el elemento**, no una $R$ cualquiera del dibujo: hay que calcular el Thévenin desde los bornes del almacenador. Y cuidado con el lugar de la $R$: en el RC es $\tau=RC$ (la $R$ **multiplica**), mientras que en el RL es $\tau=L/R$ (la $R$ **divide**). Confundir ambas invierte el efecto de la resistencia sobre la rapidez.

## Resumen

> [!resumen]
> | Concepto | RC | RL |
> |:---|:---|:---|
> | $\tau$ | $R_{eq}\,C$ | $L/R_{eq}$ |
> | Unidad | $\Omega\cdot\text{F}=\text{s}$ | $\text{H}/\Omega=\text{s}$ |
> | $R_{eq}$ grande | $\tau$ grande (lento) | $\tau$ pequeño (rápido) |
> | En $t=\tau$ | $63{,}2\%$ del cambio | $63{,}2\%$ del cambio |
> | En $t=5\tau$ | $99{,}3\%$ (extinguido) | $99{,}3\%$ (extinguido) |
> | Pendiente inicial | $1/\tau$ | $1/\tau$ |

> [!corolario]
> $\tau$ resume en un solo número toda la dinámica de un transitorio de primer orden: fija su rapidez, su escala de relajación ($1/e$ por $\tau$) y su duración práctica ($5\tau$). Es el parámetro que entra en el exponente de la [[Respuesta Completa Primer Orden]] y el que distingue, vía la posición de la $R$, al [[Circuito RC]] de su dual el [[Circuito RL]].

> [!referencia]
> Fraile Mora, cap. 4, §4.5. Aparece en: [[Circuito RC]] ($\tau=RC$), [[Circuito RL]] ($\tau=L/R$), [[Respuesta Completa Primer Orden]]. Cálculo de $R_{eq}$: [[Teorema de Thevenin]].
