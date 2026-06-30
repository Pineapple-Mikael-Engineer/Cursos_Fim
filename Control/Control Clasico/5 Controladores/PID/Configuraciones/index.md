---
title: Configuraciones del PID (PI, PD, PID)
order: 2
tags:
  - control-clasico
  - controladores
  - pid
  - index
draft: false
aliases:
  - configuraciones PID
  - PI PD PID
  - combinaciones del PID
---

# Configuraciones del PID (PI, PD, PID)

> [!definicion]
> Las tres [[Acciones/index | acciones P, I, D]] rara vez se usan las tres a ciegas: se combinan según las especificaciones. Las configuraciones útiles son cuatro —**P, PI, PD, PID**— y cada una tiene una función concreta y un equivalente en compensación clásica:
> $$\text{PI}=K_p\!\left(1+\tfrac{1}{T_i s}\right)\;\text{(lag)},\quad \text{PD}=K_p(1+T_d s)\;\text{(lead)},\quad \text{PID}=K_p\!\left(1+\tfrac{1}{T_i s}+T_d s\right)\;\text{(lead-lag)}.$$

> [!info]
> Carpeta dentro de [[Acciones/index | acciones del PID]]. Cada configuración tiene su nota: [[PI | PI]], [[PD | PD]], [[PID | PID]]. La elección de ganancias se trata en [[Sintonizacion/index | sintonización]] y el diseño geométrico en [[Lugar Raices/index | lugar de raíces]].

---

## Tabla maestra

> [!info] Las tres configuraciones (más P)
> | Config. | $G_c(s)$ | Equivale a | Mejora | A costa de |
> |---|---|---|---|---|
> | **P** | $K_p$ | ganancia pura | velocidad | deja $e_{ss}$, poco amortiguamiento |
> | **[[PI \| PI]]** | $K_p\left(1+\dfrac{1}{T_i s}\right)$ | compensador **lag** | error estacionario | velocidad, estabilidad |
> | **[[PD \| PD]]** | $K_p(1+T_d s)$ | compensador **lead** | transitorio, estabilidad | sensibilidad al ruido |
> | **[[PID \| PID]]** | $K_p\left(1+\dfrac{1}{T_i s}+T_d s\right)$ | **lead-lag** | ambos | complejidad, sintonización |

---

## Criterio de selección

> [!regla] ¿Qué necesito mejorar?
> - ¿**Error estacionario** inaceptable? → necesitas **I** → [[PI | PI]] o [[PID | PID]].
> - ¿**Sobrepico / oscilación** excesivos? → necesitas **D** → [[PD | PD]] o [[PID | PID]].
> - ¿**Ambos**? → [[PID | PID]].
> - ¿La planta ya tiene integrador y la respuesta es buena? → quizás basta **P**.
> - ¿Hay mucho **ruido**? → evita D → [[PI | PI]] (o PID con derivada filtrada).

> [!teoria] Por qué cada acción
> Cada acción ataca un eje distinto del desempeño y deja los otros casi intactos:
> - **I** añade un polo en el origen ⇒ sube el [[Coeficientes Kp Kv Ka | tipo]] del sistema ⇒ anula $e_{ss}$, pero resta fase (menos estabilidad).
> - **D** añade un cero ⇒ adelanto de fase ⇒ más amortiguamiento y velocidad, pero amplifica ruido.
> - **P** escala todo ⇒ más rápido pero más oscilatorio.
>
> Combinarlas es ubicar polos y ceros del controlador para mover los polos dominantes del lazo cerrado al lugar deseado.

---

## Equivalencia con compensadores

> [!info] PID = lead-lag
> | Acción añadida | Aporta | Equivale a |
> |---|---|---|
> | $+K_i/s$ (integral) | polo en el origen, $-90^\circ$ | **lag** (retardo) |
> | $+K_d s$ (derivativo) | cero, $+90^\circ$ | **lead** (adelanto) |
>
> El [[PID | PID]] introduce **dos ceros y un polo** en el origen: $G_c(s)=\dfrac{K_d s^2+K_p s+K_i}{s}=\dfrac{K_d(s+z_1)(s+z_2)}{s}$. Los ceros se ubican (vía sintonización) para dar lead a media frecuencia ($z_2$) y lag a baja frecuencia ($z_1$ cerca del origen).

---

## Resumen

> [!resumen]
> | Si la planta… | y necesitas… | usa | porque |
> |---|---|---|---|
> | deja offset (tipo 0) | anular $e_{ss}$ | [[PI \| PI]] | polo en origen (lag) |
> | oscila / poco amortiguada | amortiguar y acelerar | [[PD \| PD]] | cero (lead) |
> | ambos problemas | todo a la vez | [[PID \| PID]] | lead-lag |
> | ya buena, con integrador | rapidez | **P** | ganancia pura |

> [!corolario]
> Elegir configuración es identificar qué eje del desempeño falla: el error estacionario pide **I** (lag), el transitorio pide **D** (lead), y cuando fallan ambos se usa el **PID** (lead-lag). El PID es el caso general que contiene a PI y PD como casos particulares; el resto son simplificaciones que se prefieren cuando una de las acciones sobra (sin offset → sin I; con ruido → sin D).

> [!referencia]
> - Configuraciones: [[PI]] · [[PD]] · [[PID]].
> - Acciones que combinan: [[Acciones/index]].
> - Tipo y error estacionario: [[Coeficientes Kp Kv Ka]].
> - Sintonización de las ganancias: [[Sintonizacion/index]].
> - Diseño por lugar de raíces: [[Lugar Raices/index]].
