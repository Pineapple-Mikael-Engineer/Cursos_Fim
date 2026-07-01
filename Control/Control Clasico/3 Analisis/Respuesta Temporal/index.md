---
title: Respuesta Temporal
order: 2
tags:
  - control-clasico
  - analisis
  - respuesta-temporal
  - index
draft: false
aliases:
  - respuesta temporal
  - respuesta en el tiempo
  - time response
---

# Respuesta Temporal

> [!definicion]
> La **respuesta temporal** es la evolución $y(t)$ de la salida ante una entrada de prueba (típicamente el escalón). Se separa en respuesta **transitoria** (el arranque, que decae) y **permanente** (el valor final). Su forma la dictan los **polos** de la función de transferencia: un **primer orden** da una exponencial; un **segundo orden**, una respuesta que puede oscilar; y los sistemas de **orden superior** suelen aproximarse por sus **polos dominantes**.

> [!info]
> Parte del [[3 Analisis/index| análisis]] de sistemas: traduce la ubicación de los polos en comportamiento observable (rapidez, sobrepico, oscilación). Usa las [[Señales Prueba/index| señales de prueba]] como entrada. Ogata, cap. 5; Nise, cap. 4.

## De los polos a la forma de $y(t)$

> [!teoria] Primer orden, segundo orden y reducción
> - **Primer orden**: caracterizado por la **constante de tiempo** $\tau$; respuesta exponencial sin sobrepico. → [[Primer Orden]].
> - **Segundo orden**: gobernado por $\omega_n$ y $\zeta$; según el amortiguamiento aparece **sobrepico**, tiempo de subida y de establecimiento. → [[Segundo Orden/index| Segundo orden]].
> - **Orden superior y reducción**: los sistemas reales tienen muchos polos, pero unos pocos **dominantes** (los más lentos, cercanos al eje imaginario) marcan la respuesta; el resto se desprecia. → [[Orden Superior]], [[Reduccion Orden]].

## Mapa de la sección

> [!info] Las notas
> | Nota | Contenido |
> |:---|:---|
> | [[Primer Orden]] | constante de tiempo $\tau$; respuesta exponencial |
> | [[Segundo Orden/index\| Segundo orden]] | $\omega_n$, $\zeta$; sobrepico y establecimiento |
> | [[Orden Superior]] | polos dominantes; efecto de ceros |
> | [[Reduccion Orden]] | aproximar un sistema por sus polos dominantes |

> [!corolario]
> Toda la respuesta temporal se lee en el **plano $s$**: la parte real de los polos fija la rapidez de decaimiento y la imaginaria, la oscilación. Reducir a los polos dominantes permite tratar un sistema complejo como uno de primer o segundo orden.

> [!referencia]
> Ogata, *Ingeniería de Control Moderna*, cap. 5. Nise, *Control Systems Engineering*, cap. 4.
