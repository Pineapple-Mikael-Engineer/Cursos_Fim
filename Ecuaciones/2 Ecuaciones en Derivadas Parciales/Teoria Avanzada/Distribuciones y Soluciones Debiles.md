---
title: Distribuciones y Soluciones Débiles
tags:
  - ecuaciones
  - edp
  - teoria
  - avanzado
  - distribuciones
draft: false
aliases:
  - distribuciones
  - funciones generalizadas
  - solución débil
  - derivada débil
  - Distributions
  - Weak Solutions
---

# Distribuciones y Soluciones Débiles

> [!definicion]
> Una **distribución** (o **función generalizada**) es un **funcional lineal continuo** sobre el
> espacio de las **funciones de prueba** $\varphi$ —funciones infinitamente suaves y de **soporte
> compacto** (que valen cero fuera de un intervalo acotado)—. Escribimos su acción como
> $\langle T,\varphi\rangle$. Toda función localmente integrable $f$ define una distribución vía
> $\langle f,\varphi\rangle=\int f\,\varphi\,dx$, pero hay distribuciones que **no** provienen de
> ninguna función: la **delta de Dirac** $\delta$, definida por
> $$\langle\delta,\varphi\rangle=\varphi(0).$$
> La gran ventaja es que **toda** distribución es derivable cuantas veces se quiera: la **derivada
> débil** $T'$ se define **trasladando la derivada a la función de prueba**,
> $$\langle T',\varphi\rangle=-\langle T,\varphi'\rangle,$$
> que es justo la fórmula de integración por partes sin término de borde (porque $\varphi$ se anula
> en el infinito).

> [!info]
> Pieza de panorama de la [[Teoria Avanzada/index| Teoría Avanzada de EDP]]. Es el lenguaje que da
> sentido a las soluciones **no diferenciables** —los choques de las
> [[Leyes de Conservacion| leyes de conservación]]— y el marco natural de los
> [[Espacios de Sobolev| espacios de Sobolev]] y la [[Solucion Fundamental| solución fundamental]].
> Cierra el [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]].

---

## Ejemplo

> [!ejemplo] La derivada débil del escalón es la delta
> Tomemos el **escalón de Heaviside**
> $$H(x)=\begin{cases}0,&x<0\\[2pt]1,&x>0,\end{cases}$$
> que tiene un salto en el origen y **no es derivable** en sentido clásico ahí. Como distribución,
> sin embargo, sí tiene derivada, y resulta ser nada menos que la delta:
> $$H'=\delta.$$
> Intuitivamente, la "derivada" de un salto de altura $1$ es un pico infinitamente alto y angosto de
> **área** $1$ localizado justo en el salto: exactamente lo que es $\delta$. La demostración formal
> (abajo) consiste solo en aplicar la definición de derivada débil e integrar.

---

## En qué consiste

> [!teoria]
> La idea central es renunciar a preguntar **"¿cuánto vale la función en cada punto?"** y preguntar en
> su lugar **"¿cuánto mide la función al promediarla contra cada test $\varphi$?"**. Una distribución
> es precisamente esa **regla de promedios**: te da un número $\langle T,\varphi\rangle$ por cada
> función de prueba. Dos funciones que coinciden salvo en un conjunto de medida nula dan la misma
> distribución, así que perdemos el valor puntual —pero ganamos algo enorme—: **podemos derivar
> objetos que no eran derivables**. La definición $\langle T',\varphi\rangle=-\langle T,\varphi'\rangle$
> no inventa nada nuevo: si $T$ proviene de una función suave $f$, una integración por partes da
> $\int f'\varphi=-\int f\varphi'$, y el término de borde desaparece porque $\varphi$ tiene soporte
> compacto. Lo que hacemos es **tomar esa identidad como definición** cuando $T$ ya no es suave. Como
> $\varphi$ es $C^\infty$, podemos repetir el truco: $\langle T^{(k)},\varphi\rangle=(-1)^k\langle
> T,\varphi^{(k)}\rangle$. Toda distribución es infinitamente derivable.

> [!teorema] La derivada débil del Heaviside es la delta
> Sea $H$ el escalón de Heaviside. Entonces, en el sentido de las distribuciones,
> $$H'=\delta.$$

> [!demostracion]
> **Paso 1 — Aplicar la definición de derivada débil.** Por definición,
> $$\langle H',\varphi\rangle=-\langle H,\varphi'\rangle=-\int_{-\infty}^{\infty}H(x)\,\varphi'(x)\,dx.$$
>
> **Paso 2 — Usar que $H$ vale $0$ a la izquierda y $1$ a la derecha.** El integrando se anula para
> $x<0$, así que
> $$\langle H',\varphi\rangle=-\int_{0}^{\infty}\varphi'(x)\,dx.$$
>
> **Paso 3 — Integrar y usar el soporte compacto.** El teorema fundamental del cálculo da
> $$-\int_{0}^{\infty}\varphi'(x)\,dx=-\big[\varphi(x)\big]_{0}^{\infty}=-\big(\varphi(\infty)-\varphi(0)\big).$$
> Como $\varphi$ tiene soporte compacto, $\varphi(\infty)=0$, y queda
> $$\langle H',\varphi\rangle=\varphi(0)=\langle\delta,\varphi\rangle.$$
>
> Como esto vale para **toda** función de prueba $\varphi$, las distribuciones $H'$ y $\delta$
> coinciden. $\blacksquare$

> [!definicion] Solución débil de una EDP
> Sea $L$ un operador diferencial y $L^*$ su **adjunto formal** (el operador que se obtiene al pasar
> todas las derivadas al otro lado por integración por partes). Decimos que $u$ es **solución débil**
> de $Lu=f$ si
> $$\int u\,(L^*\varphi)\,dx=\int f\,\varphi\,dx\qquad\text{para TODA función de prueba }\varphi.$$
> En esta formulación **ninguna derivada actúa sobre $u$**: todas se han trasladado a la suave
> $\varphi$. Por eso $u$ **no necesita ser diferenciable** —ni siquiera continua— para resolver la
> ecuación. Toda solución clásica es solución débil; el recíproco es falso, y ahí está la ganancia.

> [!info]
> La $\delta$ no es una rareza abstracta: ya apareció en el curso como
> [[Calor en Dominio Infinito| dato inicial puntual]] (un "pinchazo" de calor de área unidad) y como
> la **fuente** que define la [[Solucion Fundamental| solución fundamental]] $-\nabla^2\Phi=\delta$
> (la respuesta al impulso en espacio libre).

> [!proposicion] Por qué importan en EDP
> Las soluciones débiles **amplían el catálogo de soluciones admisibles** justo donde la física lo
> exige: frentes de onda, ondas de choque, esquinas, fuentes puntuales. Una función con un **salto**
> —un choque de una [[Leyes de Conservacion| ley de conservación]]— no es derivable en sentido
> clásico y, sin embargo, **sí es solución débil**: la forma integral de la ley no contiene derivadas
> de $u$ y sigue teniendo pleno sentido a través de la discontinuidad. La condición de
> Rankine-Hugoniot que fija la velocidad del choque es exactamente lo que exige la formulación débil.

> [!warning]
> No toda solución débil es físicamente correcta: una ley de conservación puede tener **varias**
> soluciones débiles para el mismo dato inicial. Hace falta una **condición de entropía** adicional
> para seleccionar la "buena" (la que respeta la flecha del tiempo). Pasar a lo débil agranda el
> espacio de soluciones, y a veces lo agranda **de más**.

---

## Resumen

> [!resumen]
>
> | Concepto | Definición | Idea clave |
> |---|---|---|
> | Función de prueba $\varphi$ | $C^\infty$ de soporte compacto | el "objeto contra el que se promedia" |
> | Distribución $T$ | funcional lineal continuo $\varphi\mapsto\langle T,\varphi\rangle$ | regla de promedios; generaliza función |
> | Delta de Dirac $\delta$ | $\langle\delta,\varphi\rangle=\varphi(0)$ | impulso unitario; no es función |
> | Derivada débil $T'$ | $\langle T',\varphi\rangle=-\langle T,\varphi'\rangle$ | toda distribución es $C^\infty$ |
> | Solución débil de $Lu=f$ | $\int u\,L^*\varphi=\int f\,\varphi\ \ \forall\varphi$ | $u$ no necesita ser derivable |
>
> Resultado de cabecera: $H'=\delta$ (la derivada del escalón es la delta).

> [!corolario]
> El precio de poder derivar cualquier cosa es perder el **valor puntual**: una distribución solo
> "vive" a través de sus promedios contra funciones de prueba. A cambio, la EDP $Lu=f$ se reescribe
> como una **identidad de integrales** que admite soluciones discontinuas —el primer paso hacia los
> [[Espacios de Sobolev| espacios de Sobolev]] y la formulación variacional—.

> [!referencia]
> Cierre del [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]], dentro de la
> [[Teoria Avanzada/index| Teoría Avanzada]]. Continúa en
> [[Espacios de Sobolev| espacios de Sobolev]] y [[EDP No Lineales| EDP no lineales]].
