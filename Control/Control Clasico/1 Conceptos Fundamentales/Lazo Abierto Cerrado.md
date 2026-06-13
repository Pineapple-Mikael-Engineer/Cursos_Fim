---
title: Lazo Abierto y Lazo Cerrado
tags:
  - control-clasico
  - teoria
  - conceptos-fundamentales
draft: false
aliases:
  - lazo abierto
  - lazo cerrado
  - control realimentado
  - open loop
  - closed loop
---

# Lazo Abierto y Lazo Cerrado

## Idea central

> [!teoria] El problema que resuelve la realimentación
> Todo sistema de control persigue lo mismo: que una salida $y(t)$ (temperatura, velocidad, posición) **siga** a una referencia $r(t)$ a pesar de que el mundo real es incierto —el modelo de la planta nunca es exacto, hay perturbaciones, los componentes envejecen—.
>
> Hay dos estrategias para lograrlo:
> - **Lazo abierto:** confiar en un modelo y aplicar la acción "calculada de antemano". Funciona si el modelo es perfecto y no hay perturbaciones. En la práctica, casi nunca.
> - **Lazo cerrado:** **medir** la salida, **compararla** con lo deseado y **corregir** según la diferencia. El sistema se autocorrige usando información del resultado real.
>
> La realimentación es, en una frase, *actuar en función del error*. Toda la teoría de control clásico gira en torno a las consecuencias de cerrar ese lazo: robustez y rechazo de perturbaciones (lo bueno) a cambio del riesgo de inestabilidad (lo delicado).

## Definición

> [!definicion] Control en lazo abierto
> La acción de control **no depende de la salida**: el controlador genera $u$ a partir solo de la referencia $r$, sin medir el resultado.
> $$Y(s) = G(s)\,U(s), \qquad U(s) = G_c(s)\,R(s)$$
>
> No existe ninguna trayectoria de información que vaya de la salida de vuelta a la entrada. El sistema "no sabe" si está acertando.

> [!definicion] Control en lazo cerrado (realimentado)
> La salida se **mide y se compara** con la referencia; el error $e = r - H y$ alimenta al controlador, de modo que la salida influye sobre su propia acción de control.
> $$E(s) = R(s) - H(s)Y(s)$$
>
> El término $H(s)Y(s)$ es la señal de realimentación. El lazo queda "cerrado" porque la salida vuelve al principio formando un bucle.

> [!info] El error como motor del lazo
> En lazo cerrado, lo que mueve al controlador no es la referencia sino el **error**. Si $y$ ya coincide con $r$, el error es cero y el controlador no necesita corregir. Cuando aparece una desviación —por una perturbación o un cambio de consigna— el error se vuelve no nulo y el lazo reacciona hasta anularlo (si el sistema tiene la estructura adecuada; ver [[Error Estacionario/index | error estacionario]]).

## Diagramas de bloques

> [!ejemplo] Lazo abierto
> ![[Lazo_abierto.svg|450]]
>
> El controlador actúa "a ciegas": no hay rama de realimentación. La salida es lo que el modelo predice, sin verificación.

> [!ejemplo] Lazo cerrado con realimentación unitaria
> ![[Retroalimentacion_unitario.svg|450]]
>
> El comparador genera $e = r - y$; el lazo se cierra a través del sensor ideal ($H=1$).

> [!ejemplo] Lazo cerrado con realimentación no unitaria
> ![[Retroalimentacion_no_unitario.svg|450]]
>
> El sensor $H(s)$ aparece en la rama de realimentación: $e = r - Hy$. Modela un transductor con ganancia o dinámica propia.

## Función de transferencia de lazo cerrado

> [!teorema] FT de lazo cerrado
> Para un lazo con directa $G(s)$ y realimentación $H(s)$:
> $$T(s) = \frac{Y(s)}{R(s)} = \frac{G(s)}{1 + G(s)H(s)} = \frac{G}{1 + L}$$
> donde $L(s) = G(s)H(s)$ es la **ganancia de lazo**. Con realimentación unitaria ($H=1$): $T = \dfrac{G}{1+G}$.

> [!demostracion] Cierre del lazo paso a paso
> Partimos de las tres relaciones que definen el lazo:
> $$Y = G\,U, \qquad U = G_c\,E \;\;(\text{absorbido en } G), \qquad E = R - HY.$$
>
> **Paso 1.** Sustituir $E$ en la cadena directa. Como $U$ se genera a partir del error,
> $$Y = G\,(R - HY).$$
>
> **Paso 2.** Distribuir y agrupar todos los términos en $Y$ a la izquierda:
> $$Y = GR - GHY \implies Y + GHY = GR \implies Y\,(1 + GH) = GR.$$
>
> **Paso 3.** Despejar el cociente salida/referencia:
> $$\frac{Y}{R} = \frac{G}{1+GH}.$$
>
> El denominador $1+GH$ es la huella de la realimentación: en lazo abierto sería simplemente $T=G$. Todo lo que la realimentación hace —para bien y para mal— está contenido en ese $1+L$.

> [!info] Ecuación característica
> Los polos de lazo cerrado son las raíces de
> $$1 + G(s)H(s) = 0,$$
> la **ecuación característica**. Nótese que **no** son los polos de $G$: cerrar el lazo *reubica* los polos. Esta ecuación determina la [[Estabilidad/index | estabilidad]] y la [[Segundo Orden/index | respuesta transitoria]], y es la base del [[Lugar Raices/index | lugar de las raíces]], que precisamente dibuja cómo se mueven esas raíces al variar la ganancia.

## Las funciones del lazo: referencia, perturbación y ruido

> [!teorema] Salida ante las tres entradas
> Un lazo realista recibe tres entradas: la referencia $R$, una perturbación $D$ (entra en la planta/salida) y el ruido de medición $N$ (entra por el sensor). Superponiendo:
> $$Y = \underbrace{\frac{G}{1+L}}_{T}\,R \;+\; \underbrace{\frac{1}{1+L}}_{S}\,D \;-\; \underbrace{\frac{L}{1+L}}_{T}\,N.$$
> - $T = \dfrac{L}{1+L}$ es la **sensibilidad complementaria**: gobierna el seguimiento de $R$ y la entrada de ruido $N$.
> - $S = \dfrac{1}{1+L}$ es la **función de [[Sensibilidad]]**: gobierna el rechazo de perturbaciones $D$.
>
> Donde $|L|\gg1$ (baja frecuencia): $S\approx0$, $T\approx1$ → sigue la referencia y rechaza perturbaciones. Donde $|L|\ll1$ (alta frecuencia): $S\approx1$, $T\approx0$ → atenúa el ruido del sensor. Este reparto es la columna vertebral del diseño en frecuencia (ver [[Sensibilidad]]).

## Ejemplo resuelto

> [!ejemplo] Cálculo de $T(s)$ y del valor final
> Sea una planta $G(s)=\dfrac{K}{s(s+2)}$ con realimentación unitaria $H=1$ y $K=8$.
>
> **FT de lazo cerrado:**
> $$T(s)=\frac{G}{1+G}=\frac{\dfrac{8}{s(s+2)}}{1+\dfrac{8}{s(s+2)}}=\frac{8}{s(s+2)+8}=\frac{8}{s^2+2s+8}.$$
>
> **Identificación de 2.º orden** comparando con $\dfrac{\omega_n^2}{s^2+2\zeta\omega_n s+\omega_n^2}$:
> $$\omega_n=\sqrt{8}\approx2.83\ \text{rad/s},\qquad 2\zeta\omega_n=2\Rightarrow\zeta=\frac{1}{\sqrt{8}}\approx0.354.$$
> El lazo es subamortiguado: tendrá [[Sobrepico Mp | sobrepico]] (≈30 %). Nótese que la planta sola no tenía esa dinámica: la realimentación *creó* el par de polos complejos.
>
> **Valor final ante escalón unitario** (teorema del valor final):
> $$y(\infty)=\lim_{s\to0}sT(s)\frac1s=T(0)=\frac{8}{8}=1.$$
> Sigue la referencia con error nulo, gracias al integrador $1/s$ de la planta (sistema [[Tipo Sistema | tipo 1]]).

## Comparación

> [!info] Lazo abierto vs lazo cerrado
> | Aspecto | Lazo abierto | Lazo cerrado |
> |---|---|---|
> | Usa la salida | no | sí (realimentación) |
> | Sensibilidad a parámetros | alta | **reducida** (ver [[Sensibilidad]]) |
> | Rechazo de perturbaciones | nulo | sí |
> | Corrige errores de modelo | no | sí |
> | Estabilidad | la de la planta (siempre estable si la planta lo es) | **puede volverse inestable** |
> | Velocidad de respuesta | la de la planta | ajustable con la ganancia |
> | Costo / complejidad | bajo (sin sensor) | mayor (sensor + comparador) |
>
> En resumen: el lazo cerrado **compra robustez y prestaciones a cambio de complejidad y del riesgo de inestabilidad**. Cuándo vale la pena cerrar el lazo es la primera decisión de diseño.

> [!warning] El precio de cerrar el lazo
> La realimentación puede **desestabilizar** un sistema estable en lazo abierto si la ganancia es alta: los polos de lazo cerrado se desplazan con $K$.
>
> **Ejemplo concreto.** Sea $G(s)=\dfrac{K}{(s+1)(s+2)(s+3)}$, $H=1$. La planta es estable para todo $K>0$ (sus polos están en $-1,-2,-3$). Pero la ecuación característica del lazo cerrado es
> $$1+G=0\;\Longrightarrow\;s^3+6s^2+11s+(6+K)=0.$$
> Aplicando [[Routh Hurwitz/index | Routh-Hurwitz]], el lazo es estable solo si $K<60$. En $K=60$ aparecen un par de polos sobre el eje imaginario en $s=\pm j\sqrt{11}$ (oscilación sostenida de $\omega\approx3.32$ rad/s), y para $K>60$ el sistema **estable en lazo abierto se vuelve inestable en lazo cerrado**.
>
> Este fenómeno —subir la ganancia mejora la precisión pero empeora la estabilidad— es el conflicto central del diseño y la razón de estudiar [[Estabilidad/index | estabilidad]], [[Lugar Raices/index | lugar de raíces]] y los [[Margenes MF MG | márgenes de fase y ganancia]].

## Ejemplo físico

> [!ejemplo] Horno con y sin termostato
> - **Lazo abierto:** se fija la potencia del calefactor según una tabla (p. ej. "70 % para 200 °C"). Si cambia la temperatura ambiente, la carga del horno o el calefactor envejece, la temperatura final se desvía y **nadie la corrige**. El error depende por completo de lo bueno que sea el modelo.
> - **Lazo cerrado:** un termostato mide la temperatura ($H$ = sensor), la compara con la consigna y ajusta la potencia. Si se abre la puerta (perturbación $D$), la temperatura baja, el error crece y el controlador sube la potencia hasta recuperarla. El lazo **compensa lo que el modelo no preveía**.
>
> El mismo razonamiento explica el control de crucero de un coche (la pendiente de la carretera es la perturbación) o el regulador de Watt en una máquina de vapor (el primer lazo de realimentación industrial, 1788).

## En MATLAB

> [!info] Cierre del lazo con `feedback`
> ```matlab
> G = tf(8, [1 2 0]);      % G(s) = 8 / (s^2 + 2s)
> T = feedback(G, 1);      % lazo cerrado con H = 1  ->  8/(s^2+2s+8)
> step(T)                  % respuesta al escalón (sobrepico ~30%)
> damp(T)                  % muestra wn y zeta de los polos de lazo cerrado
> ```
> `feedback(G,H)` calcula $G/(1+GH)$ directamente. Con `H` distinto de 1 se modela realimentación no unitaria.

## Resumen

> [!resumen] Tabla comparativa
> | Concepto | Lazo abierto | Lazo cerrado |
> |---|---|---|
> | Estructura | $Y=GU$, sin retorno | $E=R-HY$, lazo cerrado |
> | FT | $T=G$ | $T=\dfrac{G}{1+GH}=\dfrac{G}{1+L}$ |
> | Polos | los de $G$ | raíces de $1+GH=0$ |
> | Sensibilidad a $G$ | $1$ (total) | $S=\dfrac{1}{1+L}$ (reducida) |
> | Perturbaciones | no se rechazan | atenuadas por $S$ |
> | Riesgo | ninguno (hereda la planta) | inestabilidad si $K$ alto |

> [!corolario] Lo esencial
> Cerrar el lazo significa **actuar sobre el error** $e=r-Hy$. Eso reubica los polos del sistema según $1+GH=0$, atenúa la incertidumbre y las perturbaciones por el factor $S=1/(1+L)$, y permite ajustar las prestaciones con la ganancia. El precio es que una ganancia excesiva puede desestabilizar incluso una planta estable. Todo el diseño clásico consiste en cerrar el lazo lo suficiente para ganar robustez y precisión, sin cruzar la frontera de la inestabilidad.

## Relación con otras notas

> [!referencia]
> - Manipulación de bloques y reducción de lazos: [[Algebra Diagramas]].
> - Reducción de la sensibilidad por realimentación: [[Sensibilidad]].
> - Partes del lazo (planta, actuador, sensor, comparador): [[Componentes Sistema]].
> - Estabilidad del lazo cerrado: [[Estabilidad/index]] · [[Lugar Raices/index]] · [[Margenes MF MG]].
> - Error en régimen permanente: [[Error Estacionario/index]] · [[Tipo Sistema]].
