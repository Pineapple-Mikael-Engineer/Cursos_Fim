---
title: Componentes de un Sistema de Control
order: 3
tags:
  - control-clasico
  - teoria
  - conceptos-fundamentales
draft: false
aliases:
  - componentes del sistema
  - planta actuador sensor
  - elementos de control
  - estructura del lazo
---

# Componentes de un Sistema de Control

## Idea central

> [!teoria] Por qué descomponer el lazo en bloques
> Un sistema de control real es un conjunto de dispositivos físicos heterogéneos: un termopar, un amplificador, una válvula, un horno. Para analizarlo no nos interesa su naturaleza interna sino **qué señal recibe cada uno y qué señal entrega**. Esa abstracción —cada dispositivo es un bloque con una función de transferencia que relaciona su entrada con su salida— es lo que permite tratar con la misma matemática un motor eléctrico y un tanque de líquido.
>
> Identificar los componentes y dibujar el [[Algebra Diagramas | diagrama de bloques]] es siempre el **primer paso** del análisis: convierte un problema de ingeniería física en uno de funciones de transferencia que luego se reducen a la forma estándar $G$ (directa) y $H$ (realimentación).

## Estructura canónica

> [!definicion] Lazo de control realimentado
> Un sistema de control en [[Lazo Abierto Cerrado | lazo cerrado]] se compone de bloques con funciones bien definidas, conectados por **señales** que recorren el lazo desde la referencia hasta la salida y de vuelta por el sensor. Cada bloque transforma su señal de entrada según su función de transferencia; el comparador es el punto donde se genera el error que pone en marcha la corrección.

> [!ejemplo] Diagrama de bloques canónico
> ![[sistema_control_componentes.svg|600]]
>
> Referencia $\to$ comparador $\to$ controlador $\to$ actuador $\to$ planta $\to$ salida, con el sensor cerrando el lazo hacia el comparador.

## Componentes

> [!definicion] Bloques del lazo
> | Componente | Símbolo | Función |
> |---|---|---|
> | **Referencia** | $r(t)$, $R(s)$ | valor deseado de la salida (consigna, *setpoint*) |
> | **Comparador** | $\otimes$ | genera el error $e = r - H y$ |
> | **Controlador** | $G_c(s)$ | procesa el error y genera la señal de control (ver [[Lugar Raices/index | diseño]]) |
> | **Actuador** | parte de $G(s)$ | convierte la señal de control en acción física (motor, válvula, calefactor) |
> | **Planta / proceso** | $G_p(s)$ | el sistema a controlar |
> | **Sensor / transductor** | $H(s)$ | mide la salida y la realimenta |

> [!info] Qué hace cada bloque (con más detalle)
> - **Referencia $r$.** Es la "orden": la velocidad, posición o temperatura que queremos. No es un componente físico sino la señal de entrada; puede ser un escalón (cambio de consigna), una rampa (seguimiento) o una señal arbitraria.
> - **Comparador (detector de error).** Resta a la referencia la salida medida. Físicamente es un amplificador diferencial, un puente o, en control digital, una simple resta en software. Es el único punto del lazo donde "conviven" la referencia y la información de la salida.
> - **Controlador $G_c$.** El cerebro del lazo: decide *cuánto* actuar según el error. Es el bloque que el ingeniero **diseña** (P, PI, PID, [[Lead | adelanto]], [[Lag | atraso]]); el resto suele venir impuesto por la planta.
> - **Actuador.** Traduce la señal de control —normalmente de baja potencia— en una acción física de potencia: un driver que mueve un motor, una electroválvula, una resistencia calefactora. Suele tener su propia dinámica y límites de saturación.
> - **Planta $G_p$.** El proceso a gobernar. Es lo "dado": un horno, un brazo robótico, el nivel de un tanque. Su modelo proviene de las leyes físicas del dominio correspondiente ([[Mecanico Traslacional]], [[Mecanico Rotacional]], [[Electrico]], etc.).
> - **Sensor / transductor $H$.** Mide la variable de salida y la convierte en una señal comparable con la referencia (p. ej. un encoder devuelve un voltaje proporcional a la posición). Su ganancia y dinámica determinan si la realimentación es unitaria o no, y su ruido $n(t)$ limita las prestaciones alcanzables.

## Señales del lazo

> [!definicion] Variables a lo largo del lazo
> | Señal | Nombre | Descripción |
> |---|---|---|
> | $r(t)$ | referencia | entrada deseada |
> | $e(t)$ | error | $e = r - H y$ |
> | $u(t)$ | señal de control | salida del controlador |
> | $y(t)$ | salida controlada | variable de interés |
> | $d(t)$ | perturbación | entrada no deseada (carga, ruido de proceso) |
> | $n(t)$ | ruido de medición | en la rama del sensor |

> [!info] Dónde entra cada señal indeseada
> Las perturbaciones $d(t)$ y el ruido $n(t)$ son lo que distingue un problema real de uno de papel:
> - La **perturbación** entra normalmente en la planta o en su salida (la pendiente que frena el coche, la pieza que carga el motor, la puerta del horno abierta). El lazo la combate con la [[Sensibilidad | función de sensibilidad]] $S$: $Y/D = S = 1/(1+L)$.
> - El **ruido de medición** entra por el sensor y "engaña" al comparador, que ve un error falso. Se cuela en la salida con $-T = -L/(1+L)$. Por eso interesa que $T\to0$ a altas frecuencias, donde vive el ruido.
>
> Un buen diseño busca $S$ pequeña a baja frecuencia (rechazar $d$) y $T$ pequeña a alta frecuencia (rechazar $n$) — el compromiso que estudia [[Sensibilidad]].

## Directa, realimentación y ganancia de lazo

> [!teorema] Agrupación de bloques
> En análisis se agrupan los bloques en serie de la rama directa y de la rama de realimentación:
> $$G(s) = G_c(s)\,G_a(s)\,G_p(s) \quad (\text{directa}), \qquad H(s) \quad (\text{realimentación}),$$
> $$L(s) = G(s)H(s) \quad (\text{ganancia de lazo}).$$
> La reducción de bloques múltiples a esta forma se hace por [[Algebra Diagramas | álgebra de diagramas]]. Una vez en esta forma canónica, todo el análisis (estabilidad, error, lugar de raíces) se hace sobre $G$, $H$ y $L$, sin importar de cuántos dispositivos provenían.

> [!info] Realimentación unitaria
> Si el sensor es ideal ($H = 1$) o su dinámica se absorbe, el lazo es de **realimentación unitaria** y $e = r - y$. Es la forma estándar para el análisis de [[Error Estacionario/index | error estacionario]] y [[Lugar Raices/index | lugar de raíces]]. Cuando $H\neq1$, conviene a veces *reubicar* el sensor (moverlo dentro del lazo por álgebra de bloques) para recuperar la forma unitaria antes de calcular el error.

## Ejemplo resuelto

> [!ejemplo] Control de velocidad de un motor DC — del físico al diagrama
> Sistema: un motor DC cuya velocidad se regula con un PID y se mide con un tacómetro.
>
> | Bloque | Elemento físico | Función de transferencia (ejemplo) |
> |---|---|---|
> | Referencia | voltaje de consigna | $R(s)$ |
> | Comparador | amplificador diferencial | resta $e=r-Hy$ |
> | Controlador | PID electrónico | $G_c(s)=K_p+\dfrac{K_i}{s}+K_d s$ |
> | Actuador | driver de potencia | $G_a(s)=K_a$ (ganancia) |
> | Planta | motor DC | $G_p(s)=\dfrac{K_m}{\tau s+1}$ |
> | Sensor | tacómetro | $H(s)=K_t$ |
>
> **Rama directa:** $G(s)=G_c\,G_a\,G_p$. **Ganancia de lazo:** $L=GH$. Si el tacómetro tiene ganancia $K_t\neq1$, el lazo es de realimentación no unitaria: la velocidad de consigna debe expresarse en las mismas unidades (voltios) que la medida.
>
> El tacómetro mide la velocidad real, el comparador la resta a la consigna y el PID ajusta el voltaje al motor hasta anular el error. Una perturbación típica $d(t)$ sería un par de carga aplicado al eje.

## Resumen

> [!resumen] Componentes y su papel
> | Bloque | FT | Papel en el lazo | ¿Quién lo fija? |
> |---|---|---|---|
> | Comparador | $-$ | genera el error $e=r-Hy$ | la estructura |
> | Controlador | $G_c$ | decide la acción según $e$ | **el diseñador** |
> | Actuador | $G_a$ | potencia la acción física | la tecnología disponible |
> | Planta | $G_p$ | el proceso a controlar | dado por el problema |
> | Sensor | $H$ | mide y realimenta | la instrumentación |
>
> Agrupados: $G=G_c G_a G_p$ (directa), $H$ (realimentación), $L=GH$ (lazo).

> [!corolario] Lo esencial
> Un sistema de control se modela como bloques unidos por señales. De todos ellos, el **controlador** es el único bajo nuestro diseño; la planta y el actuador vienen dados y el sensor define la realimentación. El análisis empieza siempre reduciendo el conjunto a la forma canónica $G$, $H$, $L=GH$, sobre la que se aplican todas las herramientas posteriores. Identificar bien dónde entran la perturbación $d$ y el ruido $n$ es clave, porque determinan qué se le puede exigir realmente al lazo.

## Relación con otras notas

> [!referencia]
> - Configuración del lazo y FT de lazo cerrado: [[Lazo Abierto Cerrado]].
> - Reducción de bloques: [[Algebra Diagramas]].
> - Sensibilidad a cada bloque y rechazo de $d$/$n$: [[Sensibilidad]].
> - Modelado de la planta por dominios: [[Mecanico Traslacional]] · [[Mecanico Rotacional]] · [[Electrico]].
> - Diseño del controlador: [[Lugar Raices/index]] · [[PID/index]].
