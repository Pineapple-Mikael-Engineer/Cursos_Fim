---
title: Selección del Método de Diseño
tags:
  - control-clasico
  - diseno
draft: false
aliases:
  - selección de método
  - ¿LGR o Bode?
  - ¿lead o lag?
  - elección del compensador
---

# Selección del Método de Diseño

> [!definicion]
> Antes de diseñar hay que tomar **dos decisiones**: (1) la **herramienta** — [[Lugar Raices/index | lugar de raíces]] (plano-$s$) o [[Respuesta Frecuencia/index | respuesta en frecuencia]] (Bode); y (2) el **compensador** — [[Lugar Raices/Lead | Lead]] (transitorio), [[Lugar Raices/Lag | Lag]] (error) o [[Lead Lag | Lead-lag]] (ambos), equivalentes a [[PD]], [[PI]], [[PID]]. La herramienta depende de cómo estén dadas las specs; el compensador, de qué falla en la planta.

> [!info]
> Vive en `4 Diseno/`, sobre sus dos subcarpetas [[Lugar Raices/index]] y [[Respuesta Frecuencia/index]]. Es la nota de decisión previa: el diagnóstico aquí dice a qué nota concreta ir (lead/lag/lead-lag, plano-$s$ o Bode).

---

## Ejemplo

> [!ejemplo]
> **Decidir herramienta y compensador en tres casos.**
>
> **Caso A — Servo con specs temporales.** Planta $G=\dfrac{K}{s(s+4)}$ con modelo conocido. Specs: $M_p\le10\%$, $t_s\le2$ s.
> - *Diagnóstico:* specs **temporales** ($M_p$, $t_s$) y hay modelo paramétrico → herramienta = **lugar de raíces** (ubica polos para el $\zeta$ y $\omega_n$ pedidos).
> - $M_p\le10\%\Rightarrow\zeta\ge0.6$; $t_s=4/(\zeta\omega_n)\le2\Rightarrow\zeta\omega_n\ge2$. El sistema sin compensar es lento → falta velocidad/transitorio → **Lead** ([[PD]]).
>
> **Caso B — Proceso con retardo, solo datos medidos.** Planta identificada por su respuesta en frecuencia, con retardo $e^{-0.3s}$. Specs: $\text{MF}\ge45^\circ$, error a escalón nulo.
> - *Diagnóstico:* hay **retardo** y **no hay modelo paramétrico** limpio (solo Bode medido) → herramienta = **frecuencia (Bode)** (el retardo es solo $-\omega T$ rad de fase, trivial en Bode).
> - "Error a escalón nulo" en un sistema sin integrador → falta ganancia DC → **Lag** ([[PI]]). Si tras el lag la MF cayera, añadir lead → **Lead-lag**.
>
> **Caso C — Specs ya cumplidas salvo ganancia.** Planta estable con buen $\zeta$ pero error grande.
> - *Diagnóstico:* transitorio OK, solo falla el error estacionario y subir $K$ no desestabiliza → basta **ganancia** ([[Proporcional P | P]]); si subir $K$ rompiera la MF, entonces **Lag**.

---

## En qué consiste

> [!info] Comparación de herramientas
> | Criterio | [[Lugar Raices/index \| Lugar de raíces]] | [[Respuesta Frecuencia/index \| Frecuencia (Bode)]] |
> |---|---|---|
> | Especificación natural | $\zeta$, $\omega_n$, polos dominantes | margen de fase, ancho de banda |
> | Necesita modelo | sí (FT con polos/ceros) | no (sirve respuesta medida) |
> | Retardos $e^{-Ts}$ | difícil | **natural** ($-\omega T$ de fase) |
> | Sistemas de orden alto | engorroso | directo |
> | Visualiza transitorio | **sí** (ubicación de polos) | indirecto (vía MF$\to\zeta$) |
> | Intuición de robustez | menor | **márgenes** explícitos |

> [!regla] Qué herramienta
> - Specs **temporales** ($M_p$, $t_s$) y hay modelo → **lugar de raíces**.
> - Specs **frecuenciales** (MF, ancho de banda), hay **retardo**, o solo datos experimentales → **Bode**.
> - Ambos dan el **mismo** compensador; son lenguajes distintos del mismo diseño.

> [!info] Qué compensador según qué mejorar
> | Necesidad | Compensador | Equivalente PID |
> |---|---|---|
> | Transitorio (sobrepico, velocidad, MF) | **[[Lugar Raices/Lead \| Lead]]** | [[PD]] |
> | Error estacionario | **[[Lugar Raices/Lag \| Lag]]** | [[PI]] |
> | Ambos | **[[Lead Lag \| Lead-lag]]** | [[PID]] |
> | Nada (specs ya cumplidas con ganancia) | solo $K$ ([[Proporcional P \| P]]) | P |

> [!teoria] Diagnóstico en dos preguntas
> 1. ¿El **error estacionario** cumple? Si no → lag / acción integral.
> 2. ¿El **transitorio/estabilidad** (MF, $M_p$) cumple? Si no → lead / acción derivativa.
> 3. Combinar según los dos diagnósticos: si fallan ambos, lead-lag; si ninguno, solo ganancia.

> [!info] Lead vs Lag (efectos)
> | | Lead (adelanto) | Lag (retardo) |
> |---|---|---|
> | Pone | cero antes que polo | polo antes que cero |
> | Aporta | fase $+$ | ganancia DC |
> | Ancho de banda | **sube** | **baja** |
> | Mejora | transitorio | error estacionario |
> | Ruido | amplifica | atenúa |
> | Velocidad | más rápido | más lento |

---

## Algoritmo

> [!algoritmo] Flujo de diseño completo
> 1. Traducir specs a objetivos ($\zeta$, $\omega_n$ o MF, ancho de banda, $K_v$).
> 2. Evaluar la planta sin compensar: ¿qué falla, error o transitorio (o ambos)?
> 3. Elegir **herramienta** (plano-$s$ o Bode) según el formato de las specs y la presencia de retardo/modelo.
> 4. Elegir **compensador** (lead/lag/lead-lag/P) según el diagnóstico de qué falla.
> 5. Diseñar, **verificar** (simular respuesta y márgenes) e iterar.

---

## Limitaciones

> [!warning]
> Ningún método es recetario: la elección depende de las especificaciones, el modelo disponible y las características de la planta (retardo, ruido, orden). Plano-$s$ y Bode son intercambiables en teoría, pero uno suele ser mucho más cómodo según el caso. El criterio físico manda sobre la fórmula.

## Resumen

> [!resumen]
> | Decisión | Regla |
> |---|---|
> | Herramienta | specs temporales + modelo → LGR; frecuenciales / retardo / datos → Bode |
> | Falla error | Lag / [[PI]] |
> | Falla transitorio | Lead / [[PD]] |
> | Fallan ambos | Lead-lag / [[PID]] |
> | No falla nada | solo ganancia / [[Proporcional P \| P]] |

> [!corolario]
> Seleccionar el método es responder dos preguntas independientes: el **formato de las specs** (y la presencia de retardo o modelo) elige la herramienta; el **diagnóstico de qué falla** (error vs transitorio) elige el compensador. Lugar de raíces y Bode producen el mismo $K_c\frac{s+z}{s+p}$; lead, lag y lead-lag se corresponden con PD, PI y PID.

> [!referencia]
> - Herramientas: [[Lugar Raices/index]] · [[Respuesta Frecuencia/index]].
> - Compensadores: [[Lugar Raices/Lead]] · [[Lugar Raices/Lag]] · [[Lead Lag]].
> - Controladores equivalentes: [[PID/index]].
> - Criterios de desempeño: [[Segundo Orden/index]] · [[Margenes MF MG]] · [[Error Estacionario/index]].
