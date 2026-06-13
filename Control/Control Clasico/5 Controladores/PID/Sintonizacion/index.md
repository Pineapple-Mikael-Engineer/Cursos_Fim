---
title: Sintonización del PID
tags:
  - control-clasico
  - controladores
  - pid
  - sintonizacion
  - index
draft: false
aliases:
  - sintonización
  - tuning
  - ajuste de ganancias
---

# Sintonización del PID

> [!definicion]
> **Sintonizar** (*tuning*) un PID es fijar sus tres parámetros $K_p$, $T_i$, $T_d$ (equivalente a $K_p$, $K_i$, $K_d$, con $K_i=K_p/T_i$ y $K_d=K_pT_d$) para cumplir las especificaciones de respuesta. Hay dos vías: **reglas empíricas** a partir de un ensayo (Ziegler-Nichols), que dan ganancias iniciales, y **diseño analítico** sobre el modelo ([[Lugar Raices/index | lugar de raíces]], [[Margenes MF MG | frecuencia]]), que da ganancias precisas.

> [!info] Métodos empíricos de Ziegler-Nichols
> Ensayo simple → tabla → ganancias **iniciales** (1942):
> - **[[Ziegler Nichols Oscilacion | Oscilación sostenida]]** (lazo cerrado): subir $K_p$ hasta oscilación de amplitud constante → ganancia última $K_u$ y periodo $P_u$ → tabla.
> - **[[Ziegler Nichols Curva Reaccion | Curva de reacción]]** (lazo abierto): respuesta al escalón en S → $K$, $L$, $T$ → tabla.

> [!info] Métodos analíticos
> Sobre el modelo de la planta, más precisos:
> - **[[Lugar Raices/index | Lugar de raíces]]:** colocar los ceros del PID para llevar los polos dominantes a la posición deseada ($\zeta$, $\omega_n$).
> - **[[Margenes MF MG | Respuesta en frecuencia]]:** elegir ganancias para un margen de fase objetivo ($\sim45^\circ$–$60^\circ$).

> [!info] Ajuste manual
> Cualitativo, iterando con la tabla de efectos de las [[Acciones/index | acciones]]: subir $K_p$ (rapidez), añadir $K_i$ (error estacionario), añadir $K_d$ (amortiguamiento). Suele rematar las ganancias iniciales de Ziegler-Nichols.

---

## Ejemplo

> [!ejemplo]
> **Mismo objetivo, dos ensayos.** Comparar qué da cada método de Ziegler-Nichols sobre una misma planta sobreamortiguada con retardo.
>
> **Vía curva de reacción (lazo abierto).** Del escalón se leen $K=4$, $L=2\ \text{min}$, $T=10\ \text{min}$. Tabla PID:
> $$K_p=1.2\frac{T}{KL}=1.5,\qquad T_i=2L=4\ \text{min},\qquad T_d=0.5L=1\ \text{min}.$$
> Desarrollo completo en [[Ziegler Nichols Curva Reaccion]].
>
> **Vía oscilación sostenida (lazo cerrado).** Subiendo $K_p$ hasta oscilar se mide $K_u=8$, $P_u=3.63\ \text{s}$. Tabla PID:
> $$K_p=0.6K_u=4.8,\qquad T_i=\frac{P_u}{2}=1.81\ \text{s},\qquad T_d=\frac{P_u}{8}=0.45\ \text{s}.$$
> Desarrollo completo en [[Ziegler Nichols Oscilacion]].
>
> Ambos producen un PID utilizable de inmediato pero con sobrepico $\sim25\%$; el ajuste fino se hace a mano. La curva de reacción es más segura (lazo abierto); la oscilación no necesita modelo.

---

## Comparación de métodos

> [!info] Métodos de sintonización
> | Método | Ensayo | Da | Precisión |
> |---|---|---|---|
> | [[Ziegler Nichols Oscilacion \| Z-N oscilación]] | lazo cerrado, $K_u$/$P_u$ | ganancias iniciales | baja (sobrepico alto) |
> | [[Ziegler Nichols Curva Reaccion \| Z-N curva]] | lazo abierto, curva S | ganancias iniciales | baja-media |
> | [[Lugar Raices/index \| Lugar de raíces]] | modelo | polos exactos | alta |
> | [[Margenes MF MG \| Margen de fase]] | modelo / Bode | márgenes objetivo | alta |

> [!warning] Punto de partida, no final
> Las reglas de Ziegler-Nichols apuntan a un decaimiento de **$1/4$ de amplitud**, que suele dar un **sobrepico alto** ($\sim25\%$). Son un punto de partida que casi siempre requiere ajuste fino posterior.

---

## Resumen

> [!resumen]
> | Vía | Entrada | Salida | Cuándo |
> |---|---|---|---|
> | Empírica (Z-N) | un ensayo | $K_p$, $T_i$, $T_d$ iniciales | sin modelo, rápido |
> | Analítica | modelo / Bode | ganancias precisas | con especificaciones $\zeta$, $\omega_n$, MF |
> | Manual | tabla de efectos | ajuste fino | remate iterativo |

> [!corolario]
> La sintonización va de lo empírico a lo analítico: Ziegler-Nichols entrega en un solo ensayo unas ganancias de arranque, y el lugar de raíces o la respuesta en frecuencia las refinan para cumplir especificaciones exactas. En la práctica se combinan: ZN para empezar, ajuste manual o analítico para terminar.

> [!referencia]
> - Reglas empíricas: [[Ziegler Nichols Oscilacion]] · [[Ziegler Nichols Curva Reaccion]].
> - Diseño analítico: [[Lugar Raices/index]] · [[Margenes MF MG]].
> - Efecto de cada ganancia: [[Acciones/index]] · [[PID]].
