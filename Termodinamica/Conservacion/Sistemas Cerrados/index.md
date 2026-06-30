---
title: "Sistemas Cerrados"
order: 1
tags:
  - termodinamica
  - conservacion
  - sistema_cerrado
  - index
draft: false
---

# Sistemas Cerrados

> [!definicion]
> Un **sistema cerrado** es una región del espacio (o colección de materia) a través de cuya **frontera no pasa masa**. La frontera puede ser real (paredes de un pistón) o imaginaria, rígida o deformable. Lo que define al sistema cerrado no es que no haya transferencia de energía, sino que **la masa total es fija durante el proceso**. Todo lo que cruza la frontera lo hace como calor $Q$ o trabajo $W$, nunca como materia.

---

## Por qué estudiar sistemas cerrados primero

> [!teoria]
> El sistema cerrado es el modelo termodinámico más simple que permite formular las dos leyes con precisión:
>
> 1. **Primera ley:** $\Delta U = Q - W$ — toda la energía que entra al sistema como calor o sale como trabajo se contabiliza en la variación de energía interna.
> 2. **Segunda ley:** $\Delta S \ge \int \delta Q/T$ — la entropía generada por irreversibilidades internas es no negativa.
>
> Los volúmenes de control (sistemas abiertos) añaden complejidad — flujo de masa, entalpía de flujo, estados de entrada y salida — pero se derivan directamente del análisis de SC aplicado a una región con frontas permeables al flujo. Entender SC primero permite apreciar **por qué** $H$ (entalpía) aparece en los balances de VC en lugar de $U$ (energía interna).
>
> **Casos prácticos de sistema cerrado:**
> - Gas en un pistón-cilindro durante compresión o expansión.
> - Recipiente a presión sellado que se calienta o enfría.
> - Gas confinado en un frasco hermético que intercambia calor.
> - Un globo aerostático en vuelo (masa de gas = constante).

---

## Postulado de estado: cuántas propiedades fijan el estado

> [!proposicion]
> Para un sistema cerrado **simple compresible** (el único modo de trabajo reversible es $P\,dV$), el estado termodinámico de equilibrio queda completamente determinado por **dos propiedades intensivas independientes**. Todos los demás valores de propiedades son funciones de esas dos.
>
> Consecuencia operativa: para encontrar $u$, $h$, $s$, $v$ de una sustancia, solo se necesitan dos de las propiedades de la lista $\{T, P, v, x, \ldots\}$. Las tablas y ecuaciones de estado codifican esta dependencia. Ver [[Variables de Estado/index | Variables de Estado]].

---

## Los tres balances del sistema cerrado

> [!teoria]
> Todo el análisis de un proceso en SC se reduce a aplicar tres balances consecutivos:
>
> | Balance | Ecuación | Qué determina |
> |:---|:---|:---|
> | **Masa** | $m = \text{cte}$ | (trivial: la masa no varía) |
> | **Energía** (1.ª ley) | $\Delta U = Q - W$ | Relación entre calor, trabajo y cambio de $U$ |
> | **Entropía** (2.ª ley) | $\Delta S = \int \delta Q/T + S_{\rm gen}$, $S_{\rm gen} \ge 0$ | Dirección del proceso; cuánta irreversibilidad hay |
> | **Exergía** (2.ª ley + entorno) | $\Delta B = \int (1 - T_0/T)\,\delta Q - W_{\rm útil} - B_{\rm dest}$ | Trabajo útil máximo; pérdidas por irreversibilidades |
>
> El balance de exergía es consecuencia de los dos anteriores más el conocimiento del entorno $(T_0, P_0)$; no es una ley independiente.

---

## La frontera y los signos

> [!info]
> **Convención estándar (Borgnakke & Sonntag, Çengel):**
> - $Q > 0$: calor entra al sistema.
> - $W > 0$: trabajo sale del sistema (el sistema hace trabajo sobre el entorno).
> - Por tanto: $\Delta U = Q - W$.
>
> **Tipos de trabajo en SC:**
> - **Trabajo de frontera** (boundary work): $W_b = \int P_{\rm ext}\,dV$. Para proceso cuasiestático: $W_b = \int P\,dV$ (área bajo la curva $P$-$v$).
> - **Trabajo de eje** $W_{\rm eje}$: paletas agitadoras, etc. Entra con signo negativo en la convención positivo-saliente.
> - **Trabajo eléctrico** $W_{\rm elec}$, trabajo de tensión superficial, etc.
>
> El total: $W = W_b + W_{\rm eje} + W_{\rm elec} + \ldots$

![[sistema_cerrado_frontera.svg|400]]
*Sistema cerrado: pistón-cilindro con calor $Q$ entrante desde fuente térmica y trabajo $W_b$ saliente por expansión. La masa $m$ de gas permanece constante. La frontera se desplaza cuando el pistón se mueve.*

---

## Mapa de notas

> [!info]
> - [[Primera Ley SC]] (order 1) — $\Delta U = Q - W$: formulación, trabajo de frontera, casos particulares.
> - [[Segunda Ley SC]] (order 2) — $\Delta S \ge \int \delta Q/T$: producción de entropía, desigualdad de Clausius.
> - [[Balance de Exergia SC]] (order 3) — $\Delta B = (\ldots) - B_{\rm dest}$: Gouy-Stodola; eficiencia de segunda ley.
>
> Para pasar a sistemas con flujo de masa: [[Volumenes de Control/index | Volúmenes de Control]].

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, caps. 4–7 y 10; Çengel & Boles, *Termodinámica*, caps. 4–8; Moran & Shapiro, *Fundamentals of Engineering Thermodynamics*, caps. 2–7.
