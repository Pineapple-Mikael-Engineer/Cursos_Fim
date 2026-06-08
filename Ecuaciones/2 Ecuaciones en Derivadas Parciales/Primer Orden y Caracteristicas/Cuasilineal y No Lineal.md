---
title: Cuasilineal y No Lineal
tags:
  - ecuaciones
  - edp
  - teoria
  - caracteristicas
  - cuasilineal
draft: false
aliases:
  - EDP cuasilineal
  - EDP totalmente no lineal
  - Charpit-Lagrange
  - Quasilinear PDE
---

# Cuasilineal y No Lineal

> [!definicion]
> Una EDP de primer orden es **cuasilineal** cuando es lineal en las derivadas pero sus
> coeficientes pueden depender de la incógnita:
> $$a(x,y,u)\,u_x+b(x,y,u)\,u_y=c(x,y,u).$$
> Ahora las características **dependen de $u$**, de modo que su pendiente cambia con el valor que
> transportan y **pueden cruzarse**. Es **totalmente no lineal** cuando la dependencia en las
> derivadas no es lineal,
> $$F(x,y,u,u_x,u_y)=0,$$
> y se resuelve siguiendo **tiras características** (Charpit-Lagrange): un sistema para
> $x,\,y,\,u,\,p=u_x,\,q=u_y$.

> [!info]
> Continúa el [[Metodo de las Caracteristicas| método de las características]] cuando la curva
> deja de ser inocente. Es el origen directo de las [[Leyes de Conservacion| leyes de conservación]]
> y de las [[Ondas de Choque y Burgers| ondas de choque]] del modelo de Burgers.
> Parte de la sección [[Primer Orden y Caracteristicas/index| Primer Orden y Características]].

---

## Ejemplo

> [!ejemplo] Burgers no viscoso $u_t+u\,u_x=0$
> Es el ejemplo arquetípico. Aquí $a=u$ (coeficiente de $u_x$) y la fuente es $c=0$, así que la
> rapidez con que se propaga **cada punto depende de su propia altura $u$**. Las ecuaciones
> características son
> $$\frac{dx}{dt}=u,\qquad \frac{du}{dt}=0.$$
> La segunda dice que **$u$ es constante sobre cada característica**. Pero si $u$ es constante,
> entonces $\dfrac{dx}{dt}=u$ es constante: las características son **rectas**, cada una con su
> propia pendiente $u=f(x_0)$. Arrancando del pie $x_0$ con dato $u(x,0)=f(x)$:
> $$x=x_0+f(x_0)\,t,\qquad u=f(x_0).$$
> Esta es la **solución implícita** $u=f\big(x-u\,t\big)$.
>
> **El cruce.** Las rectas que salen de pies con mayor $f$ van más rápido. Si $f$ es **decreciente**,
> una característica rápida (pie a la izquierda, $u$ grande) **alcanza** a una lenta (pie a la
> derecha, $u$ pequeño): se **cruzan**. En el punto de cruce, la fórmula pretende asignar dos
> valores de $u$ a la vez $\Rightarrow$ la solución se vuelve **multivaluada**. La física no admite
> eso: en su lugar aparece una discontinuidad, un **choque**.

---

## En qué consiste

> [!teoria] Por qué se cruzan las características
> En el caso lineal todas las características comparten geometría (p. ej. rectas paralelas en el
> transporte), así que nunca se tocan. En el caso cuasilineal, la pendiente $\dfrac{dx}{dt}=a(\dots,u)$
> **codifica el valor transportado**: características que llevan valores distintos avanzan a ritmos
> distintos. Donde el dato inicial es **decreciente**, el "material rápido" viene detrás del "lento",
> lo alcanza, y las trayectorias se intersecan. El instante del primer cruce es el **tiempo de
> quiebre** (ver [[Ondas de Choque y Burgers]]), a partir del cual ya no existe solución clásica.

> [!info] El caso totalmente no lineal: tiras características
> Cuando $F(x,y,u,p,q)=0$ con $p=u_x$, $q=u_y$ es no lineal en $p,q$, una sola curva no basta: hay
> que arrastrar también el **plano tangente** a la superficie solución. El sistema de
> **Charpit-Lagrange** propaga la *tira* $(x,y,u,p,q)$:
> $$\frac{dx}{dt}=F_p,\quad \frac{dy}{dt}=F_q,\quad \frac{du}{dt}=p\,F_p+q\,F_q,$$
> $$\frac{dp}{dt}=-(F_x+p\,F_u),\quad \frac{dq}{dt}=-(F_y+q\,F_u).$$
> Las dos últimas ecuaciones (para $p,q$) son lo nuevo: dicen cómo gira el plano tangente al
> avanzar. En el caso cuasilineal se reducen a las características usuales y desaparecen.

> [!info] Conexión con Hamilton-Jacobi y la mecánica
> Las ecuaciones tipo $u_t+H(x,\nabla u)=0$ son **ecuaciones de Hamilton-Jacobi**, EDP de primer
> orden no lineales en $\nabla u$. Sus tiras características son **exactamente las ecuaciones de
> Hamilton** $\dot x=H_p$, $\dot p=-H_x$ de la mecánica clásica: las características de la EDP son
> las **trayectorias del sistema mecánico**, y la acción es la solución $u$. Es la misma idea de
> "transportar datos por curvas", ahora en el espacio de fases.

> [!warning] Vida útil de la solución clásica
> En una EDP cuasilineal, la solución $C^1$ existe **solo hasta el tiempo de quiebre** $t_*$, el
> primer instante en que dos características se cruzan. Para $t>t_*$ hay que abandonar la noción
> clásica y trabajar con **soluciones débiles** que admiten discontinuidades (los choques),
> seleccionadas por una **condición de entropía** —ver [[Leyes de Conservacion]].

> [!proposicion]
> Mientras las características **no se crucen**, la solución implícita $u=f(x-ut)$ (Burgers) es la
> única solución clásica del problema de Cauchy. El cruce no es un defecto del método: es la EDP
> avisando que la solución suave ha dejado de existir.

## Resumen

> [!resumen]
> | Tipo | Forma | Característica | Rasgo |
> |---|---|---|---|
> | Lineal | $a(x,y)u_x+b(x,y)u_y=c$ | independiente de $u$ | nunca se cruzan |
> | Cuasilineal | $a(x,y,u)u_x+b(x,y,u)u_y=c$ | **depende de $u$** | pueden cruzarse $\to$ choque |
> | No lineal | $F(x,y,u,u_x,u_y)=0$ | tiras de Charpit $(x,y,u,p,q)$ | el plano tangente también se propaga |

> [!corolario]
> La no linealidad de primer orden tiene una firma inconfundible: **datos suaves que producen
> singularidades en tiempo finito**. La causa es geométrica —características que se cruzan— y la
> cura es conceptual —cambiar de noción de solución (débil) y de criterio de selección (entropía).

> [!referencia]
> - El marco que da sentido al choque: [[Leyes de Conservacion]] (Rankine-Hugoniot).
> - El estudio detallado del modelo: [[Ondas de Choque y Burgers]].
> - El punto de partida lineal: [[Metodo de las Caracteristicas]].
> - Vuelta al mapa: [[Primer Orden y Caracteristicas/index]].
