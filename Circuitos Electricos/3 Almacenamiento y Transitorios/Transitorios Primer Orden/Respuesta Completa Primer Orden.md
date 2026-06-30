---
title: Respuesta Completa Primer Orden
tags:
  - circuitos-electricos
  - teoria
  - transitorios
  - primer-orden
draft: false
aliases:
  - respuesta completa
  - respuesta natural y forzada
  - complete response
  - natural and forced response
---

# Respuesta Completa de Primer Orden

> [!definicion]
> La **respuesta completa** de cualquier variable de un circuito de primer orden es la suma de la **respuesta forzada** (el régimen permanente $x_\infty$ que imponen las fuentes) y la **respuesta natural** (el transitorio $(x_0-x_\infty)\,e^{-t/\tau}$ que se extingue):
> $$x(t)=x_\infty+(x_0-x_\infty)\,e^{-t/\tau}.$$
> Vale para **cualquier** tensión o corriente del circuito, no solo para la variable de estado $v_C$ o $i_L$.

> [!info]
> Es el **método unificador** de los [[Transitorios Primer Orden/index| transitorios de primer orden]] del [[3 Almacenamiento y Transitorios/index| capítulo 3]]: generaliza por igual al [[Circuito RC]] y al [[Circuito RL]]. El valor inicial $x_0$ se obtiene de las [[Condiciones Iniciales]], y la rapidez con que muere el transitorio la fija la [[Constante de Tiempo]]. Fraile Mora, cap. 4, §4.5.

---

## Ejemplo

> [!ejemplo]
> **Descomposición de una respuesta genérica.**
>
> Una variable $x(t)$ de un circuito de primer orden vale $x_0=1$ en $t=0^+$ y tiende a $x_\infty=5$ en régimen permanente, con constante de tiempo $\tau=2\ \text{ms}$. Escribir $x(t)$ y separarla en su parte forzada y su parte natural.
>
> ![[respuesta_completa.svg|620]]
>
> *La respuesta completa (verde) es la suma de la forzada $x_\infty$ (constante) y la natural $(x_0-x_\infty)e^{-t/\tau}$ (decae a cero).*
>
> Sustituyendo los tres datos en la fórmula:
> $$x(t)=x_\infty+(x_0-x_\infty)\,e^{-t/\tau}=5+(1-5)\,e^{-t/2\,\text{ms}}=5-4\,e^{-t/2\,\text{ms}}.$$
>
> > [!solucion]
> > $$x(t)=5-4\,e^{-t/2\,\text{ms}}.$$
> > - **Respuesta forzada:** $x_\infty=5$ (constante, lo que queda cuando $t\to\infty$).
> > - **Respuesta natural:** $-4\,e^{-t/2\,\text{ms}}$ (exponencial de amplitud $x_0-x_\infty=-4$, que se extingue).
> > - En $t=\tau=2\ \text{ms}$: $x(\tau)=5-4e^{-1}=5-1{,}47=3{,}53$, es decir, ya ha recorrido el $63\,\%$ del salto total desde $x_0$ hacia $x_\infty$.

---

## En qué consiste

> [!teoria]
> La idea es **separar** la respuesta en dos piezas con significado físico distinto:
>
> - La **respuesta forzada** $x_\infty$ es lo que queda cuando el transitorio ya murió ($t\to\infty$): la imponen las fuentes y, con excitación DC, es una constante.
> - La **respuesta natural** $(x_0-x_\infty)\,e^{-t/\tau}$ es la **forma propia** del circuito: la exponencial $e^{-t/\tau}$ no depende de las fuentes, solo de la topología ($\tau$); su **amplitud** la fija la condición inicial a través de $x_0-x_\infty$.
>
> El método vale para **cualquier** variable porque todas las tensiones y corrientes del circuito comparten **la misma** $\tau$ (la del único elemento almacenador) y solo difieren en sus valores $x_0$ y $x_\infty$. Para una variable que **no** es de estado (por ejemplo una corriente por una resistencia), el valor inicial $x_0=x(0^+)$ se calcula sustituyendo el condensador por una fuente de tensión $v_C(0^+)$ y el inductor por una fuente de corriente $i_L(0^+)$, y resolviendo el circuito resistivo resultante.

> [!algoritmo]
> Tres datos y una sustitución:
>
> 1. **Valor inicial** $x(0^+)$: usar la continuidad de $v_C$ y de $i_L$ (no saltan) para fijar el estado en $t=0^+$, y de ahí resolver la variable pedida.
> 2. **Valor final** $x(\infty)$: régimen permanente DC, sustituyendo el **condensador por un circuito abierto** y el **inductor por un cortocircuito**.
> 3. **Constante de tiempo** $\tau$: $\tau=R_{eq}\,C$ (circuitos RC) o $\tau=L/R_{eq}$ (circuitos RL), con $R_{eq}$ la resistencia equivalente vista por el elemento almacenador.
> 4. **Sustituir** en $x(t)=x_\infty+(x_0-x_\infty)\,e^{-t/\tau}$.

> [!warning]
> La fórmula directa $x_\infty+(x_0-x_\infty)e^{-t/\tau}$ solo vale si la excitación es **constante** tras la conmutación (fuentes DC). Con otras excitaciones (senoidal, rampa, etc.) hay que resolver la ecuación diferencial completa o usar [[Laplace en Circuitos/index| Laplace]]. Recuerda además que, aunque **todas** las variables comparten la misma $\tau$, cada una tiene **su propio** $x_0$ y su propio $x_\infty$: hay que recalcularlos para cada incógnita.

---

## Resumen

> [!resumen]
> | Pieza | Expresión | Origen | Comportamiento |
> |---|---|---|---|
> | Forzada | $x_\infty$ | fuentes (régimen permanente) | constante (con DC) |
> | Natural | $(x_0-x_\infty)\,e^{-t/\tau}$ | forma propia del circuito | $\to 0$ al crecer $t$ |
> | Completa | $x_\infty+(x_0-x_\infty)\,e^{-t/\tau}$ | suma de ambas | $x_0\to x_\infty$ |
>
> Datos necesarios: $x_0=x(0^+)$, $x_\infty=x(\infty)$ y $\tau$. El factor $x_0-x_\infty$ puede ser negativo (subida) o positivo (bajada); el signo lo da la diferencia entre el valor inicial y el final.

> [!corolario]
> Cualquier transitorio de primer orden con excitación DC queda **completamente determinado** por solo tres números —$x_0$, $x_\infty$ y $\tau$—, sin necesidad de plantear la ecuación diferencial. El [[Circuito RC]] y el [[Circuito RL]] son casos particulares de esta misma fórmula con $x=v_C$ e $x=i_L$, respectivamente.

> [!referencia]
> Fraile Mora, *Circuitos Eléctricos*, cap. 4, §4.5 (respuesta completa: natural más forzada). Véase también [[Circuito RC]], [[Circuito RL]], [[Constante de Tiempo]] y [[Condiciones Iniciales]].
