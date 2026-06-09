---
title: Espacios de Sobolev
tags:
  - ecuaciones
  - edp
  - teoria
  - avanzado
  - sobolev
draft: false
aliases:
  - espacios de Sobolev
  - formulación variacional
  - forma débil
  - Lax-Milgram
  - Sobolev Spaces
---

# Espacios de Sobolev

> [!definicion]
> El **espacio de Sobolev** $H^k(\Omega)$ es el conjunto de las funciones $u\in L^2(\Omega)$ cuyas
> **derivadas débiles** (en el sentido de las [[Distribuciones y Soluciones Debiles| distribuciones]])
> hasta el orden $k$ también están en $L^2(\Omega)$. Se le dota de la norma
> $$\lVert u\rVert_{H^k}^2=\sum_{\lvert\alpha\rvert\le k}\int_\Omega\lvert D^\alpha u\rvert^2\,dx,$$
> donde $\alpha$ es un multiíndice y $D^\alpha$ la derivada débil correspondiente. Con esta norma
> $H^k$ es un **espacio de Hilbert** (completo y con producto interno). El subespacio $H^1_0(\Omega)$
> está formado por las funciones de $H^1$ con **traza nula**, es decir, que **se anulan en la
> frontera** $\partial\Omega$ —el marco correcto para condiciones de Dirichlet homogéneas—.

> [!info]
> Pieza de panorama de la [[Teoria Avanzada/index| Teoría Avanzada de EDP]]. Es el **espacio donde
> viven las soluciones débiles**: convierte una EDP en una ecuación dentro de un espacio de Hilbert.
> Apoya directamente sobre [[Distribuciones y Soluciones Debiles| distribuciones y soluciones débiles]] y abre la puerta a las [[EDP No Lineales| EDP no lineales]]. Cierra el
> [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]].

---

## Ejemplo

> [!ejemplo] Forma débil del problema de Poisson
> Queremos resolver el problema de Dirichlet
> $$-\nabla^2 u=f\ \text{en }\Omega,\qquad u=0\ \text{en }\partial\Omega.$$
> Multiplicamos por una función de prueba $v\in H^1_0$ e integramos sobre $\Omega$:
> $$-\int_\Omega(\nabla^2 u)\,v=\int_\Omega f\,v.$$
> Una **integración por partes** (fórmula de Green) traslada una derivada de $u$ a $v$; el término de
> borde $\int_{\partial\Omega}(\partial_n u)\,v$ **se anula** porque $v\in H^1_0$ vale cero en la
> frontera. Queda el problema **variacional**:
> $$\boxed{\ \text{hallar }u\in H^1_0\ \text{tal que}\ \int_\Omega\nabla u\cdot\nabla v=\int_\Omega f\,v\quad\forall\,v\in H^1_0.\ }$$
> Observa que en esta forma **solo aparece una derivada primera** de $u$ (no la segunda). Por eso
> $H^1$ —no $C^2$— es el espacio **natural**: pide exactamente que la **energía**
> $\int_\Omega\lvert\nabla u\rvert^2$ sea finita, que es lo único que la formulación necesita. Una
> función con una esquina puede tener energía finita y ser solución débil aunque no sea $C^2$.

---

## En qué consiste

> [!teoria]
> El paso de la EDP a su **forma débil** es el corazón del método. La forma fuerte $-\nabla^2u=f$
> exige que $u$ sea **dos veces** derivable. La forma débil
> $$a(u,v)=\int_\Omega\nabla u\cdot\nabla v=\int_\Omega f\,v=:\ell(v)$$
> reparte las derivadas: **una** sobre $u$ y **una** sobre $v$. Esto rebaja el requisito de
> regularidad a la mitad y simetriza el problema. La cantidad $a(u,v)$ es una **forma bilineal** y
> $\ell(v)$ una **forma lineal** sobre el espacio de Hilbert $H^1_0$. Resolver la EDP equivale ahora
> a una pregunta puramente **funcional**: ¿existe un $u$ en el Hilbert tal que $a(u,v)=\ell(v)$ para
> todo $v$? La respuesta la da un teorema abstracto, sin tocar la EDP de nuevo.

> [!algoritmo] De la EDP fuerte a la forma débil
> 1. **Multiplicar** la EDP $Lu=f$ por una función de prueba $v$ del espacio de Hilbert adecuado.
> 2. **Integrar** sobre el dominio $\Omega$.
> 3. **Integrar por partes** para repartir las derivadas entre $u$ y $v$ (bajar el orden sobre $u$).
> 4. **Anular el término de borde** usando la condición de contorno (p. ej. $v\in H^1_0$).
> 5. Leer la **forma bilineal** $a(u,v)$ y la **forma lineal** $\ell(v)$; el problema es
>    $a(u,v)=\ell(v)\ \forall v$.

> [!teorema] Lax-Milgram (panorama)
> Sea $a(\cdot,\cdot)$ una forma bilineal sobre un espacio de Hilbert $V$ que es
> - **acotada**: $\lvert a(u,v)\rvert\le M\,\lVert u\rVert_V\,\lVert v\rVert_V$, y
> - **coerciva**: $a(u,u)\ge\alpha\,\lVert u\rVert_V^2$ con $\alpha>0$,
>
> y sea $\ell$ una forma lineal acotada sobre $V$. Entonces existe una **única** solución débil
> $u\in V$ del problema $a(u,v)=\ell(v)$ para todo $v\in V$.

> [!demostracion] Esquema
> **Paso 1 — Representar la forma como operador.** Por el teorema de representación de Riesz, para
> cada $u$ fijo la forma $v\mapsto a(u,v)$ es un funcional acotado, luego existe $Au\in V$ con
> $a(u,v)=\langle Au,v\rangle$. Igualmente $\ell(v)=\langle b,v\rangle$ para cierto $b\in V$. El
> problema se vuelve $Au=b$.
>
> **Paso 2 — Usar la coercividad como contracción.** Para $\rho>0$ pequeño, la aplicación
> $T(u)=u-\rho(Au-b)$ resulta ser una **contracción** en $V$ gracias a la coercividad
> ($a(u,u)\ge\alpha\lVert u\rVert^2$ controla por debajo) y a la acotación (controla por arriba).
>
> **Paso 3 — Punto fijo.** Por el teorema de punto fijo de Banach, $T$ tiene un **único** punto fijo
> $u$, y $T(u)=u\iff Au=b$. Esa $u$ es la única solución débil. $\blacksquare$

> [!info] Encajes de Sobolev y regularidad (panorama)
> Los **teoremas de encaje de Sobolev** comparan $H^k$ con espacios de funciones continuas: si $k$ es
> **suficientemente grande respecto a la dimensión** $n$ (concretamente $k-\tfrac n2>m$), entonces
> $$H^k(\Omega)\subset C^m(\Omega).$$
> La consecuencia es la **regularidad**: una solución débil que pertenezca a un $H^k$ con $k$ grande
> es, de hecho, **clásica**. Así se cierra el círculo: buscamos la solución en el espacio débil
> (donde es fácil probar que **existe** y es **única**), y luego un teorema de regularidad la sube a
> $C^m$ y muestra que también resuelve la EDP en sentido fuerte.

> [!proposicion] Por qué $H^1$ y no otro
> La forma débil de Poisson involucra $\int\lvert\nabla u\rvert^2$ —la **energía de Dirichlet**—.
> Pedir que esta integral sea finita es **exactamente** pedir $u\in H^1$. Ni más (no hace falta la
> derivada segunda) ni menos (con solo $L^2$ no podríamos siquiera escribir $\nabla u$). $H^1$ es el
> espacio de energía finita: por eso es el "natural", y por eso es la base del método de **elementos
> finitos**, que busca la solución débil en un subespacio de dimensión finita de $H^1_0$.

---

## Resumen

> [!resumen]
>
> | Concepto | Definición | Para qué sirve |
> |---|---|---|
> | $H^k(\Omega)$ | $u$ y derivadas débiles hasta orden $k$ en $L^2$ | espacio de Hilbert donde viven las soluciones débiles |
> | Norma $\lVert u\rVert_{H^k}$ | $\sum_{\lvert\alpha\rvert\le k}\int\lvert D^\alpha u\rvert^2$ | mide función + derivadas en energía |
> | $H^1_0$ | $H^1$ con **traza nula** | condiciones de Dirichlet homogéneas |
> | Forma débil | $a(u,v)=\ell(v)\ \ \forall v$ | reparte derivadas; EDP $\to$ ecuación de Hilbert |
> | Lax-Milgram | $a$ acotada + coerciva $\Rightarrow$ existe único $u$ | existencia/unicidad; base de elementos finitos |
> | Encaje de Sobolev | $H^k\subset C^m$ si $k-\tfrac n2>m$ | regularidad: solución débil $\to$ clásica |
>
> Idea de cabecera: **bajar el orden** de la EDP por integración por partes para resolverla en el
> espacio de **energía finita** $H^1$.

> [!corolario]
> La estrategia moderna invierte el orden clásico: primero se **garantiza** la existencia y unicidad
> en el espacio débil (Lax-Milgram), y solo después se **mejora la regularidad** (encajes de Sobolev)
> hasta recuperar, cuando es posible, una solución clásica. Existencia primero, suavidad después.

> [!referencia]
> Continúa la línea de [[Distribuciones y Soluciones Debiles| distribuciones y soluciones débiles]]
> dentro de la [[Teoria Avanzada/index| Teoría Avanzada]]. Conduce a las
> [[EDP No Lineales| EDP no lineales]]. Cierre del
> [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]].
