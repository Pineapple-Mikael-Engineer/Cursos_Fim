---
title: Sensibilidad $S(s)$
order: 2
tags:
  - control-clasico
  - teoria
  - conceptos-fundamentales
draft: false
aliases:
  - sensibilidad
  - función de sensibilidad
  - sensibilidad complementaria
  - S = 1/(1+GH)
---

# Sensibilidad $S(s)$

## Idea central

> [!teoria] ¿Cuánto importa que el modelo esté mal?
> En [[Lazo Abierto Cerrado | lazo abierto]] todo error del modelo se traslada íntegro a la salida: si la ganancia real de la planta es un 10 % mayor de lo previsto, la salida será un 10 % mayor. La promesa de la realimentación es **atenuar** esa dependencia. La *función de sensibilidad* $S(s)$ es la medida exacta de esa atenuación: dice qué fracción de una variación —del modelo o de una perturbación— sobrevive en la salida tras cerrar el lazo.
>
> Su importancia es doble. Por un lado cuantifica la **robustez** (insensibilidad a incertidumbres). Por otro, junto con su complementaria $T$, formaliza el **compromiso fundamental** del diseño: no se puede ser insensible a todo a la vez. Casi todo el diseño en frecuencia consiste en *moldear* $S(j\omega)$ —dónde la hacemos pequeña y dónde la dejamos crecer—.

## Definición

> [!definicion] Función de sensibilidad
> Mide cuánto afecta a la salida una variación relativa de un parámetro o una perturbación. Para el lazo con ganancia $L = GH$:
> $$S(s) = \frac{1}{1 + G(s)H(s)} = \frac{1}{1+L}$$
>
> Es exactamente el factor $1/(1+L)$ que aparecía en la [[Lazo Abierto Cerrado | FT de lazo cerrado]]. Cuanto mayor es la ganancia de lazo $|L|$, menor es $S$ y más "sorda" se vuelve la salida frente a las imperfecciones.

> [!definicion] Sensibilidad complementaria
> $$T(s) = \frac{G H}{1 + GH} = \frac{L}{1+L}$$
> Coincide (con realimentación unitaria) con la [[Lazo Abierto Cerrado | FT de lazo cerrado]] $Y/R$. Gobierna el seguimiento de la referencia y, con signo negativo, la entrada del ruido de medición.

> [!teorema] Restricción fundamental
> $$S(s) + T(s) = 1 \quad \forall s$$
> No se pueden hacer $S$ y $T$ pequeñas a la vez: reducir la sensibilidad ($S\to0$) implica $T\to1$, y viceversa. Es un **compromiso inevitable** del diseño, válido en *toda* frecuencia y para *cualquier* controlador.

> [!demostracion] La suma es idénticamente 1
> Directamente de las definiciones, con $L=GH$:
> $$S+T=\frac{1}{1+L}+\frac{L}{1+L}=\frac{1+L}{1+L}=1.$$
> No es una aproximación ni depende de la frecuencia: es una identidad algebraica. Por eso el reparto entre rechazar incertidumbre ($S$ baja) y seguir la referencia ($T\approx1$) es un juego de suma cero punto a punto en $\omega$.

## Sensibilidad a variaciones de la planta

> [!teorema] Sensibilidad de $T$ respecto a $G$
> La sensibilidad relativa de la FT de lazo cerrado ante cambios en $G$ es
> $$S_G^T = \frac{\partial T / T}{\partial G / G} = \frac{1}{1 + GH} = S(s).$$
> Un cambio relativo $\Delta G/G$ produce en lazo cerrado un cambio $\Delta T/T \approx S\cdot \Delta G/G$.

> [!demostracion] De la definición de sensibilidad relativa
> La *sensibilidad relativa* de una magnitud $T$ frente a un parámetro $G$ se define como el cociente de variaciones porcentuales, que en el límite es $S_G^T=\dfrac{\partial T}{\partial G}\dfrac{G}{T}$.
>
> **Paso 1.** Derivar $T=\dfrac{G}{1+GH}$ respecto a $G$ (regla del cociente, $H$ constante):
> $$\frac{\partial T}{\partial G} = \frac{(1+GH)\cdot 1 - G\cdot H}{(1+GH)^2} = \frac{1+GH-GH}{(1+GH)^2}=\frac{1}{(1+GH)^2}.$$
>
> **Paso 2.** Multiplicar por $G/T$, con $T=G/(1+GH)$ (es decir $G/T=1+GH$):
> $$S_G^T = \frac{1}{(1+GH)^2}\cdot\frac{G}{T} = \frac{1}{(1+GH)^2}\cdot(1+GH) = \frac{1}{1+GH} = S.$$
>
> Conclusión: la sensibilidad relativa de las prestaciones de lazo cerrado a la planta **es** la función de sensibilidad $S$. El mismo $S$ aparece como factor de atenuación de errores de modelo y de perturbaciones — no es casualidad, es la misma estructura $1/(1+L)$.

> [!info] Por qué el lazo cerrado es robusto
> En **lazo abierto**, $T = G$ y $S_G^T = 1$: el error de modelo se traslada 1:1 a la salida. En **lazo cerrado**, $S_G^T = \dfrac{1}{1+GH}$, que es $\ll 1$ donde la ganancia de lazo $|L|$ es grande. La realimentación **atenúa** el efecto de las incertidumbres de la planta — la razón de fondo para cerrar el lazo (ver [[Lazo Abierto Cerrado]]).

## Ejemplo resuelto

> [!ejemplo] Atenuación numérica de un error de modelo
> Sea $G=K$ (ganancia constante) con realimentación unitaria y $K=99$, de modo que $L=99$ y
> $$S=\frac{1}{1+99}=0.01,\qquad T=\frac{99}{100}=0.99.$$
>
> Supongamos que la ganancia real de la planta resulta ser un **10 % mayor** de lo modelado: $\Delta G/G=0.10$. El cambio en las prestaciones de lazo cerrado es
> $$\frac{\Delta T}{T}\approx S\cdot\frac{\Delta G}{G}=0.01\times0.10=0.001=0.1\%.$$
>
> Un error del **10 %** en la planta se traduce en solo un **0.1 %** en la salida: la realimentación lo dividió por $1+L=100$. En lazo abierto ese mismo 10 % habría aparecido íntegro. Ese factor $100$ es justamente $1/S$, y es lo que se "paga" con ganancia de lazo.

## Comportamiento en frecuencia

> [!ejemplo] $S$ y $T$ frente a la frecuencia
> ![[sensibilidad_S_T_frecuencia.svg|500]]
>
> A bajas frecuencias $|L|\gg1 \Rightarrow S\approx0$, $T\approx1$: buen seguimiento y rechazo de perturbaciones. A altas frecuencias $|L|\ll1 \Rightarrow S\approx1$, $T\approx0$: atenuación del ruido de medición. La transición ocurre cerca de la frecuencia de cruce de ganancia, donde $|L|\approx1$.

> [!info] Reparto de tareas
> | Banda | $|L|$ | $S$ | $T$ | Efecto |
> |---|---|---|---|---|
> | Baja frecuencia | $\gg 1$ | $\approx 0$ | $\approx 1$ | sigue la referencia, rechaza perturbaciones |
> | Alta frecuencia | $\ll 1$ | $\approx 1$ | $\approx 0$ | rechaza ruido del sensor |
>
> La lectura de diseño es clara: queremos **mucha** ganancia de lazo donde están la referencia y las perturbaciones (baja frecuencia) y **poca** donde está el ruido (alta frecuencia). El controlador se diseña para conseguir esa forma de $|L(j\omega)|$.

## Sensibilidad a perturbaciones

> [!teorema] Rechazo de perturbación de salida
> Para una perturbación $D(s)$ que entra en la salida, $Y = T R + S D$. El efecto de la perturbación se atenúa por $S(s)$:
> $$\left.\frac{Y}{D}\right|_{R=0} = S(s) = \frac{1}{1+GH}.$$
> Donde $|L|$ es grande, $S\to0$ y la perturbación se cancela. Si además la ganancia de lazo contiene un integrador ($L$ tiene un polo en $s=0$), entonces $S(0)=0$ y la perturbación constante se rechaza **por completo** en régimen permanente. (Ver [[Formula General | error estacionario ante perturbaciones]].)

## Límites del diseño

> [!warning] Integral de Bode (efecto colchón de agua)
> No se puede reducir $|S|$ en todas las frecuencias: el **teorema de la integral de Bode** impone, para sistemas estables sin polos en el semiplano derecho,
> $$\int_0^\infty \ln|S(j\omega)|\,d\omega = 0.$$
> Como el integrando es negativo donde $|S|<1$ (buena atenuación), debe ser positivo en otra banda donde $|S|>1$ (**amplificación**): bajar $S$ en una zona lo sube en otra, igual que apretar un colchón de agua. El diseño no elimina la sensibilidad, la **reparte**. Por eso aparece siempre un "pico de sensibilidad" $M_s=\max_\omega|S(j\omega)|>1$, cuyo valor se relaciona con los [[Margenes MF MG | márgenes de estabilidad]] (un $M_s$ bajo implica buenos márgenes).

## Resumen

> [!resumen] Funciones de sensibilidad
> | Función | Definición | Gobierna | Se quiere pequeña en… |
> |---|---|---|---|
> | $S$ | $\dfrac{1}{1+L}$ | error de modelo, perturbaciones $D$ | baja frecuencia |
> | $T$ | $\dfrac{L}{1+L}$ | seguimiento de $R$, ruido $N$ | alta frecuencia |
> | Identidad | $S+T=1$ | compromiso inevitable | — |
> | Robustez | $S_G^T=S$ | $\dfrac{\Delta T}{T}\approx S\,\dfrac{\Delta G}{G}$ | — |

> [!corolario] Lo esencial
> La función de sensibilidad $S=1/(1+L)$ mide cuánto sobrevive en la salida una variación del modelo o una perturbación: es el factor por el que la realimentación divide los errores. Su complementaria $T=L/(1+L)$ gobierna el seguimiento, y la identidad $S+T=1$ hace que reducir una signifique aumentar la otra. La estrategia de diseño es lograr $|L|$ grande a baja frecuencia ($S\approx0$: robustez y rechazo) y $|L|$ pequeña a alta frecuencia ($T\approx0$: rechazo de ruido), aceptando que la integral de Bode prohíbe hacer $S$ pequeña en todas partes.

## Relación con otras notas

> [!referencia]
> - Por qué el lazo cerrado reduce la sensibilidad: [[Lazo Abierto Cerrado]].
> - Componentes del lazo y entrada de $d$/$n$: [[Componentes Sistema]].
> - Error y perturbaciones: [[Error Estacionario/index]] · [[Formula General]].
> - Márgenes, pico $M_s$ y forma de $L(j\omega)$: [[Margenes MF MG]] · [[Funcion Transferencia/index]].
