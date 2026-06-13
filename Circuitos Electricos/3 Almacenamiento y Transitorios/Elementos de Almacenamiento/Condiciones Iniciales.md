---
title: Condiciones Iniciales
tags:
  - circuitos-electricos
  - teoria
  - transitorios
  - condiciones-iniciales
draft: false
aliases:
  - condiciones iniciales
  - initial conditions
  - continuidad de vC e iL
  - valores en t=0
---

# Condiciones Iniciales $\;v_C(0^+)=v_C(0^-),\ \ i_L(0^+)=i_L(0^-)$

> [!definicion]
> En el instante de **conmutación** ($t=0$, cuando se abre o cierra un interruptor), la **tensión del
> condensador** $v_C$ y la **corriente del inductor** $i_L$ son **continuas**: no pueden saltar. Por
> tanto sus valores justo después de conmutar coinciden con los de justo antes,
> $$v_C(0^+)=v_C(0^-),\qquad i_L(0^+)=i_L(0^-).$$
> Estos valores son las **condiciones iniciales** del transitorio. Las demás magnitudes —la corriente
> $i_C$, la tensión $v_L$ y las corrientes y tensiones de las resistencias— **sí** pueden dar saltos en
> $t=0$.

> [!info]
> Es la propiedad de continuidad del [[Capacitor]] y del [[Inductor]], dentro de los
> [[Elementos de Almacenamiento/index| elementos de almacenamiento]] del
> [[3 Almacenamiento y Transitorios/index| capítulo 3]]. Constituye el **punto de partida** de todo
> [[Circuito RC| transitorio RC]] y [[Circuito RL| transitorio RL]]: sin condiciones iniciales no se
> puede resolver la ecuación diferencial del circuito. Fraile Mora, cap. 4, §4.3.

---

## Ejemplo

> [!ejemplo]
> **Un condensador que cambia de régimen sin saltar.**
>
> Un condensador estaba cargado a $v_C(0^-)=2\ \text{V}$ en un circuito previo. En $t=0$ se conmuta y
> queda conectado a una fuente que lo llevará, en el nuevo régimen permanente, a $8\ \text{V}$. ¿Cuánto
> vale $v_C$ justo después de conmutar, en $t=0^+$?
>
> ![[continuidad_vc.svg|470]]
>
> *La tensión del condensador arranca en su valor previo $v_C(0^-)=2\ \text{V}$ y evoluciona sin
> saltar; el salto (a puntos) está prohibido.*
>
> **Paso 1 — Valor previo.** Antes de conmutar el condensador estaba cargado a $v_C(0^-)=2\ \text{V}$.
>
> **Paso 2 — Continuidad.** Como $v_C$ no puede saltar, justo después de conmutar conserva ese valor:
> $$v_C(0^+)=v_C(0^-)=2\ \text{V}.$$
>
> **Paso 3 — Evolución.** A partir de $t=0^+$ la tensión sube **suavemente** desde $2\ \text{V}$ hacia
> los $8\ \text{V}$ del nuevo régimen permanente. El "salto" directo de $2$ a $8\ \text{V}$ en $t=0$
> (la curva a puntos) está prohibido: exigiría corriente infinita.
>
> > [!solucion]
> > $v_C(0^+)=2\ \text{V}$ (arranca en su valor previo, no en $8\ \text{V}$). La corriente $i_C$, en
> > cambio, **sí** salta en $t=0$: pasa de $0$ (régimen previo) a su nuevo valor inicial, que es
> > precisamente el que carga el condensador hacia los $8\ \text{V}$.

---

## En qué consiste

> [!teoria] Por qué $v_C$ e $i_L$ no pueden saltar
> Un salto instantáneo en $v_C$ exigiría, por $i_C=C\,dv_C/dt$, una corriente $i_C\to\infty$; un salto
> en $i_L$ exigiría, por $v_L=L\,di_L/dt$, una tensión $v_L\to\infty$. Ambos significan **potencia
> infinita**, físicamente imposible con fuentes acotadas. Dicho de otro modo: la energía almacenada
> ($\tfrac12 Cv_C^2$ en el condensador, $\tfrac12 Li_L^2$ en el inductor) no puede cambiar de golpe sin
> potencia infinita, así que $v_C$ e $i_L$ **evolucionan de forma continua**.
>
> Por eso $v_C$ e $i_L$ se llaman **variables de estado**: resumen toda la "memoria" del circuito en un
> instante. El resto de magnitudes ($i_C$, $v_L$, corrientes de resistencias) no son variables de
> estado y **pueden saltar**.

> [!teorema] Cómo se obtienen los valores en $0^-$
> Para hallar $v_C(0^-)$ e $i_L(0^-)$ se analiza el **régimen permanente previo** (el circuito *antes*
> de conmutar, supuesto estable). En DC estable: el **condensador** equivale a un **circuito abierto**
> ($i_C=0$) y el **inductor** a un **cortocircuito** ($v_L=0$), según
> [[Circuitos DC en Estado Estable]]. Con esas equivalencias se resuelve el circuito previo y se leen
> $v_C(0^-)$ e $i_L(0^-)$.

> [!algoritmo] Resolver las condiciones iniciales de un transitorio
> 1. **Antes de conmutar** ($t=0^-$): analizar el circuito en **régimen permanente** (DC: $C$ abierto,
>    $L$ en corto) y obtener $v_C(0^-)$ e $i_L(0^-)$.
> 2. **Continuidad**: aplicar
>    $$v_C(0^+)=v_C(0^-),\qquad i_L(0^+)=i_L(0^-).$$
> 3. **Justo después** ($t=0^+$): para hallar las demás magnitudes iniciales ($i_C$, $v_L$, corrientes
>    y tensiones de resistencias), sustituir el **condensador por una fuente de tensión** de valor
>    $v_C(0^+)$ y el **inductor por una fuente de corriente** de valor $i_L(0^+)$; resolver el circuito
>    resultante (puramente resistivo).
> 4. **Régimen permanente final** ($t\to\infty$): repetir el paso 1 con el circuito ya conmutado para
>    obtener $v_C(\infty)$ e $i_L(\infty)$, necesarios para escribir la solución completa del
>    transitorio.

> [!proposicion] El modelo en $t=0^+$
> En $t=0^+$ el condensador "recuerda" su tensión y el inductor su corriente, de modo que **se comportan
> como fuentes**: $C\to$ fuente de tensión $v_C(0^+)$, $L\to$ fuente de corriente $i_L(0^+)$. El
> circuito en ese instante es **resistivo** (sin derivadas), y se resuelve con las leyes de Kirchhoff
> habituales. Esto permite calcular, por ejemplo, $i_C(0^+)$ o $v_L(0^+)$, que en general **no**
> coinciden con sus valores en $0^-$.

> [!warning]
> Solo $v_C$ e $i_L$ son continuas. **No** asumir que $i_C$ o $v_L$ no saltan: en general sí lo hacen.
> Además, la continuidad puede **fallar** ante **fuentes impulsivas** o no acotadas (un impulso de
> corriente puede cargar un condensador instantáneamente, o un impulso de tensión cambiar de golpe la
> corriente de un inductor): solo con magnitudes **acotadas** se garantiza $v_C(0^+)=v_C(0^-)$ e
> $i_L(0^+)=i_L(0^-)$.

## Resumen

> [!resumen]
> | Magnitud | En $t=0$ | Cómo se obtiene en $0^-$ |
> |:---|:---|:---|
> | $v_C$ (variable de estado) | **continua**: $v_C(0^+)=v_C(0^-)$ | régimen previo, $C$ abierto |
> | $i_L$ (variable de estado) | **continua**: $i_L(0^+)=i_L(0^-)$ | régimen previo, $L$ en corto |
> | $i_C$, $v_L$, resistencias | **pueden saltar** | modelo en $0^+$ ($C$→fuente $V$, $L$→fuente $I$) |
> | $v_C(\infty)$, $i_L(\infty)$ | régimen permanente final | circuito ya conmutado en DC estable |

> [!corolario]
> Las condiciones iniciales son la **memoria** del circuito: $v_C$ e $i_L$ no saltan porque su energía
> no puede cambiar de golpe. Conocer $v_C(0^+)$, $i_L(0^+)$ y los valores finales basta para escribir
> la respuesta completa de cualquier [[Circuito RC| transitorio RC]] o [[Circuito RL| RL]] de primer
> orden.

> [!referencia]
> Fraile Mora, cap. 4, §4.3. Continuidad de la tensión: [[Capacitor]]. Continuidad de la corriente:
> [[Inductor]]. Régimen previo y final: [[Circuitos DC en Estado Estable]]. Aplicación:
> [[Circuito RC]], [[Circuito RL]].
