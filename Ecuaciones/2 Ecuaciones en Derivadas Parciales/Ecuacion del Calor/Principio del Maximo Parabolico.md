---
title: Principio del Maximo Parabolico
order: 5
tags:
  - ecuaciones
  - edp
  - teoria
  - calor
  - maximo
draft: false
aliases:
  - principio del máximo parabólico
  - principio del máximo para el calor
  - frontera parabólica
  - parabolic maximum principle
---

# Principio del Maximo Parabolico

> [!definicion]
> El **principio del máximo** para la ecuación del calor afirma que, en el cilindro espacio-temporal $Q_T=[0,L]\times[0,T]$, una solución de $u_t=\alpha^2u_{xx}$ alcanza su **máximo** (y, por simetría, su **mínimo**) en la **frontera parabólica**: el borde inicial $t=0$ o los lados $x=0$ y $x=L$. **Nunca** en el interior ni en la **tapa superior** $t=T$ (salvo que $u$ sea constante). Físicamente: la difusión **no fabrica** puntos más calientes que el dato inicial o que lo que imponen los bordes — el calor solo se reparte y se atenúa, jamás se concentra para crear un pico nuevo.

> [!info]
> Es uno de los pilares teóricos de la [[Ecuacion del Calor/index| ecuación del calor]], dentro del [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]]. Da una vía **independiente** de demostrar la unicidad del problema de Dirichlet, complementaria al [[Metodo de Energia Unicidad| método de energía]]. Se aplica a las soluciones obtenidas por [[Separacion Calor Dirichlet| separación con Dirichlet]]: garantiza que esa serie es la **única** solución y que es **estable**.

---

## Ejemplo

> [!ejemplo] Una barra que solo puede enfriarse hacia el equilibrio
> Una barra $[0,L]$ parte de un perfil $u(x,0)=f(x)$ con $0\le f(x)\le 100$ grados, y mantenemos sus extremos a $0$ grados: $u(0,t)=u(L,t)=0$. El principio del máximo dice que, para todo $x$ y todo $t>0$,
> $$0\le u(x,t)\le 100.$$
> El razonamiento: el **máximo** de $u$ en el cilindro $[0,L]\times[0,T]$ vive en la frontera parabólica. Allí $u$ vale $f(x)\le100$ (en $t=0$) o $0$ (en los lados $x=0,L$). Luego el máximo global es $\le100$. Análogamente el mínimo es $\ge0$. **Conclusión sin resolver nada:** la barra nunca supera los $100$ grados ni baja de $0$. La difusión no puede generar un punto a $120$ grados a partir de un dato acotado por $100$ — sería crear calor de la nada. Esto es justo lo contrario de lo que ocurriría con un término fuente.

## En qué consiste

> [!teoria]
> La intuición es de cálculo elemental. En un **máximo interior** de una función de $x$, la segunda derivada espacial cumple $u_{xx}\le0$ (cóncava hacia abajo). Si además es máximo en el tiempo alcanzado por primera vez, $u_t\ge0$. Pero la ecuación pide $u_t=\alpha^2u_{xx}$: el lado izquierdo $\ge0$ y el derecho $\le0$ solo casan si ambos son cero, lo que no fuerza contradicción por sí mismo (la igualdad débil no basta). El truco para volverlo estricto es **perturbar** $u$ con un pequeño término que rompa el empate, demostrarlo para la perturbación, y dejar que la perturbación tienda a cero.

> [!teorema] Principio del máximo (débil)
> Sea $u$ continua en $Q_T=[0,L]\times[0,T]$ y solución de $u_t=\alpha^2u_{xx}$ en el interior. Entonces
> $$\max_{Q_T}u=\max_{\partial_pQ_T}u,$$
> donde $\partial_pQ_T$ es la **frontera parabólica**: $\{t=0\}\cup\{x=0\}\cup\{x=L\}$ (todo el borde **menos** la tapa superior $t=T$). El mismo enunciado vale para el mínimo cambiando $u$ por $-u$.

> [!demostracion] Por perturbación
> **Paso 1 — Perturbar.** Para $\varepsilon>0$ definimos
> $$v(x,t)=u(x,t)+\varepsilon x^2.$$
> Calculamos cuánto incumple $v$ la ecuación del calor:
> $$v_t-\alpha^2v_{xx}=\underbrace{(u_t-\alpha^2u_{xx})}_{=0}-\alpha^2\varepsilon\cdot 2
> =-2\alpha^2\varepsilon<0.$$
> Es decir, $v$ satisface la **desigualdad estricta** $v_t-\alpha^2v_{xx}<0$. Esa estrictez es justo lo que faltaba para forzar una contradicción.
>
> **Paso 2 — Descartar máximo interior o en la tapa para $v$.** Supongamos que $v$ alcanzase su máximo en un punto $(x_0,t_0)$ con $0<x_0<L$ y $0<t_0\le T$ (interior o tapa superior). En tal punto, por ser máximo en $x$: $v_{xx}(x_0,t_0)\le0$. Y en $t$: si $t_0<T$ es máximo interno en tiempo, $v_t=0$; si $t_0=T$ es máximo en el extremo del intervalo, $v_t\ge0$. En ambos casos
> $$v_t(x_0,t_0)-\alpha^2v_{xx}(x_0,t_0)\ge0,$$
> en **contradicción** con el Paso 1, que daba $<0$ en todo el interior. Luego $v$ **no** puede tener su máximo ahí: debe alcanzarlo en la frontera parabólica.
>
> **Paso 3 — Quitar la perturbación.** Para todo $(x,t)\in Q_T$,
> $$u(x,t)\le v(x,t)\le\max_{\partial_pQ_T}v\le\max_{\partial_pQ_T}u+\varepsilon L^2.$$
> Haciendo $\varepsilon\to0$ se obtiene $u(x,t)\le\max_{\partial_pQ_T}u$ para todo punto, es decir $\max_{Q_T}u=\max_{\partial_pQ_T}u$. $\blacksquare$

> [!proposicion] Tres consecuencias inmediatas
> Sea el problema $u_t=\alpha^2u_{xx}$ en $[0,L]\times[0,T]$ con dato inicial y de frontera dados.
> 1. **Comparación.** Si dos datos cumplen $f_1\le f_2$ (en $t=0$ y en los bordes), entonces $u_1\le u_2$ en todo $Q_T$. Aplíquese el principio del mínimo a $u_2-u_1$, cuya frontera parabólica es $\ge0$.
> 2. **Unicidad (Dirichlet).** Si $u_1,u_2$ tienen los **mismos** datos inicial y de frontera, $w=u_1-u_2$ se anula en toda la frontera parabólica; por el principio, $\max w=\min w=0$, luego $w\equiv0$ y $u_1\equiv u_2$. La solución es **única**.
> 3. **Estabilidad.** Si los datos difieren a lo sumo en $\delta$ en la frontera parabólica, las soluciones difieren a lo sumo en $\delta$ en todo $Q_T$: $\|u_1-u_2\|_\infty\le\delta$. Una perturbación pequeña del dato produce una respuesta pequeña — el problema está **bien planteado**.

> [!warning]
> El principio depende de la **ausencia de fuentes**. Para $u_t=\alpha^2u_{xx}+g$ con $g>0$ (una fuente que **inyecta** calor) sí pueden aparecer máximos interiores: nada impide que un punto se caliente más que la frontera si lo estamos calentando activamente. El enunciado limpio es para la ecuación **homogénea**; con fuente se obtienen versiones con desigualdades corregidas.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Dominio | cilindro $Q_T=[0,L]\times[0,T]$ |
> | Frontera parabólica | $\{t=0\}\cup\{x=0\}\cup\{x=L\}$ (sin la tapa $t=T$) |
> | Enunciado | $\max_{Q_T}u=\max_{\partial_pQ_T}u$ (ídem mínimo) |
> | Técnica de prueba | perturbar $v=u+\varepsilon x^2$, luego $\varepsilon\to0$ |
> | Clave | $v_t-\alpha^2v_{xx}=-2\alpha^2\varepsilon<0$ impide máximo interior |
> | Consecuencias | comparación, unicidad (Dirichlet), estabilidad |
> | Requisito | sin fuentes ($g=0$) |

> [!corolario]
> El principio del máximo formaliza el rasgo de que el calor **suaviza**: como no puede crear picos nuevos, la amplitud (rango entre máximo y mínimo) **no aumenta** con el tiempo. Es el reflejo, en el espacio físico, de que cada modo de Fourier decae — el mismo "olvido" que en [[Calor en Dominio Infinito| dominio infinito]] hace que la gaussiana se aplane.

> [!referencia]
> - La otra vía a la unicidad: [[Metodo de Energia Unicidad]].
> - Las soluciones a las que se aplica: [[Separacion Calor Dirichlet]].
> - El índice del tema: [[Ecuacion del Calor/index]].
