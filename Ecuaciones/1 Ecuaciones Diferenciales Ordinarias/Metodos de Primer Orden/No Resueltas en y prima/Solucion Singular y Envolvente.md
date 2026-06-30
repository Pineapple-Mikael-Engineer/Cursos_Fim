---
title: Solucion Singular y Envolvente
order: 3
tags:
  - ecuaciones
  - edo
  - teoria
  - primer-orden
  - no-resueltas
  - envolvente
draft: false
aliases:
  - solución singular
  - envolvente
  - c-discriminante
  - p-discriminante
  - singular solution
  - envelope
---

# Solución Singular y Envolvente

> [!definicion]
> Una **solución singular** de una EDO es una solución que **no se obtiene de la solución general** para ningún valor de la constante de integración. Aparece típicamente como la **envolvente** de la familia uniparamétrica de curvas solución: una curva que es **tangente a cada miembro** de la familia en algún punto. Por ser tangente, comparte pendiente con la familia en cada punto y por eso satisface la misma ecuación diferencial, pese a no pertenecer a ella.

> [!info]
> Concepto transversal del bloque [[No Resueltas en y prima/index| no resueltas en $y'$]]. Es la pieza que explica la "solución extra" que aparece en [[Clairaut]] y [[Lagrange]] al derivar la ecuación. Conecta con la teoría general de [[Curvas Integrales y Soluciones| curvas integrales]]: la solución general es una **familia** de curvas integrales, y la envolvente es una curva integral adicional que las "borda".

---

## Ejemplo

> [!ejemplo] Familia de rectas y su envolvente
> ![[envolvente_clairaut.svg|460]]
>
> Las rectas $y=cx-\tfrac{c^2}{4}$ (verde) son todas tangentes a la parábola envolvente $y=x^2$ (dorado), que es la solución singular.
>
> **Hallar la envolvente de la familia de rectas $F(x,y,c)=y-cx+\tfrac{c^2}{4}=0$.**
>
> **Paso 1 — la familia.** $F(x,y,c)=y-cx+\dfrac{c^{2}}{4}=0$, es decir $y=cx-\dfrac{c^{2}}{4}$ (un haz de rectas, una por cada $c$).
>
> **Paso 2 — derivar respecto al parámetro $c$.** Tratamos $c$ como variable y $x,y$ fijos:
> $$\frac{\partial F}{\partial c}=-x+\frac{c}{2}=0.$$
>
> **Paso 3 — eliminar $c$** entre $F=0$ y $\partial F/\partial c=0$. De la segunda, $c=2x$. Sustituyendo en la familia:
> $$y=(2x)\,x-\frac{(2x)^{2}}{4}=2x^{2}-x^{2}=x^{2}.$$
> La envolvente es la **parábola**
> $$\boxed{\,y=x^{2}\,}$$
>
> **Paso 4 — verificar.** Cada recta del haz toca a $y=x^2$ en un solo punto y con la misma pendiente: en $x_0$ la tangente a la parábola es $y=2x_0 x - x_0^2$, que es exactamente el miembro $c=2x_0$ de la familia. La parábola es así la envolvente, tangente a todas las rectas, y es la **solución singular**.

---

## En qué consiste

> [!teoria]
> La **envolvente** de una familia uniparamétrica $F(x,y,c)=0$ es una curva tangente a todos sus miembros. ¿Cómo encontrarla? Sobre la envolvente, al variar infinitesimalmente el parámetro $c$, el punto de tangencia se desplaza **a lo largo** de la propia envolvente; eso obliga a que, en esos puntos, además de $F=0$ se cumpla $\partial F/\partial c=0$. Por tanto la envolvente se obtiene **eliminando $c$** del sistema
> $$\{\,F(x,y,c)=0,\qquad \partial F/\partial c=0\,\}.$$
> El resultado de esa eliminación se llama **c-discriminante** de la familia.
>
> Existe una vía equivalente que parte de la **propia EDO** en lugar de la solución general. Si la ecuación se escribe $\Phi(x,y,p)=0$ con $p=y'$, la solución singular se obtiene eliminando $p$ del **p-discriminante**
> $$\{\,\Phi(x,y,p)=0,\qquad \partial \Phi/\partial p=0\,\}.$$
> La razón de que la envolvente **satisfaga la EDO** es geométrica: en cada uno de sus puntos comparte tangente (luego pendiente $p=y'$) con un miembro de la familia, que sí la satisface; al tener el mismo $(x,y,y')$ que una solución, la envolvente resuelve la misma ecuación.

> [!demostracion] Por qué en la envolvente $\partial F/\partial c=0$
> **Paso 1 — parametrizar la envolvente por $c$.** Como la envolvente toca a un miembro distinto de la familia en cada punto, a cada valor del parámetro $c$ le corresponde su **punto de tangencia** $\big(x(c),\,y(c)\big)$. Ese punto está sobre la curva número $c$, de modo que
> $$F\big(x(c),\,y(c),\,c\big)=0\qquad\text{para todo }c.$$
>
> **Paso 2 — derivar respecto a $c$** (regla de la cadena, porque $x,y$ dependen de $c$):
> $$F_x\,x'(c)+F_y\,y'(c)+F_c=0.$$
>
> **Paso 3 — usar la tangencia.** El vector $\big(x'(c),y'(c)\big)$ es tangente a la **envolvente**; pero por definición la envolvente es tangente al miembro $c$ en ese punto, así que ese mismo vector es también tangente a la curva $F(x,y,c)=0$ (con $c$ fijo). La tangente de esa curva cumple $F_x\,dx+F_y\,dy=0$, es decir $F_x\,x'+F_y\,y'=0$.
>
> **Paso 4 — concluir.** Sustituyendo en el Paso 2, los dos primeros sumandos se cancelan y queda
> $$F_c\big(x(c),y(c),c\big)=0.$$
> Luego sobre la envolvente se cumplen **simultáneamente** $F=0$ y $\partial F/\partial c=0$: eliminar $c$ entre ambas (el **c-discriminante**) la produce. $\blacksquare$

> [!ejemplo] La vía del p-discriminante: $(y')^2=4y$
> Hallemos la solución singular **sin** pasar por la solución general, usando solo la ecuación.
>
> **Paso 1 — escribir $\Phi(x,y,p)=0$** con $p=y'$:  $\Phi=p^{2}-4y=0$.
>
> **Paso 2 — derivar respecto a $p$:**  $\dfrac{\partial\Phi}{\partial p}=2p=0\ \Rightarrow\ p=0$.
>
> **Paso 3 — eliminar $p$:** con $p=0$ en $\Phi=0$ queda $-4y=0$, es decir $\boxed{y=0}$.
>
> **Paso 4 — verificar:** $y=0\Rightarrow y'=0$ y $0^2=4\cdot 0$ ✓.
>
> Geométricamente: la solución **general** de $(y')^2=4y$ es la familia de parábolas $y=(x+c)^2$ (en efecto $y'=2(x+c)$ y $(y')^2=4(x+c)^2=4y$), y la recta $y=0$ es su **envolvente** —tangente a todas en el vértice—. El p-discriminante la obtuvo **directamente de la EDO**, sin conocer la familia. Compáralo con el c-discriminante del ejemplo de las rectas: dos caminos, la misma curva.

> [!algoritmo] Calcular la envolvente (solución singular) por c-discriminante
> 1. Escribe la familia de soluciones $F(x,y,c)=0$.
> 2. **Deriva** respecto al parámetro: $\dfrac{\partial F}{\partial c}=0$.
> 3. **Elimina $c$** entre $F=0$ y $\partial F/\partial c=0$.
> 4. **Verifica** que la curva resultante satisface la EDO (no toda eliminación es solución).

> [!proposicion]
> En la [[Clairaut| ecuación de Clairaut]] $y=cx+\psi(c)$, el c-discriminante reproduce exactamente la solución singular hallada al derivar la EDO: la envolvente del haz de rectas es la solución singular de la Clairaut. Ambos métodos —derivar la EDO (p-discriminante) o derivar la familia respecto al parámetro (c-discriminante)— conducen a la misma curva.

> [!warning]
> No todo c-discriminante (ni p-discriminante) es una solución de la EDO. La eliminación puede arrojar el **lugar de puntos singulares** de las curvas (cúspides, nodos, puntos de retroceso) en lugar de una envolvente. Por eso el **paso de verificación es obligatorio**: hay que comprobar que la curva obtenida realmente satisface la ecuación diferencial antes de declararla solución singular.

> [!info] Conexión física — la cáustica
> La envolvente es el mismo objeto que la **cáustica** en óptica: cuando un haz de rayos se refleja o refracta, la curva brillante que se forma (por ejemplo, en el fondo de una taza iluminada) es la **envolvente de la familia de rayos**. Cada rayo es tangente a la cáustica, igual que cada recta de una Clairaut es tangente a su envolvente.

## Resumen

> [!resumen]
> | Concepto | Definición / cálculo |
> |---|---|
> | Solución singular | no se obtiene de la general para ningún $c$ |
> | Envolvente | curva tangente a todos los miembros de la familia |
> | c-discriminante | eliminar $c$ de $\{F=0,\ \partial_c F=0\}$ |
> | p-discriminante | eliminar $p$ de $\{\Phi=0,\ \partial_p\Phi=0\}$ |
> | Verificación | comprobar que satisface la EDO (puede ser falso positivo) |

> [!corolario]
> La solución singular es un objeto **geométrico**: la envolvente de la familia de curvas integrales. Se calcula derivando respecto al parámetro (c-discriminante) o respecto a $p=y'$ en la EDO (p-discriminante), y siempre debe **verificarse**. Es lo que distingue a las ecuaciones [[No Resueltas en y prima/index| no resueltas en $y'$]] de los tipos lineales, donde no hay envolventes.

> [!referencia]
> - Donde aparece de forma natural: [[Clairaut]] (envolvente del haz de rectas).
> - Método general que puede generarla: [[Lagrange]].
> - Teoría de fondo: [[Curvas Integrales y Soluciones]].
> - Vuelta al bloque: [[No Resueltas en y prima/index]].
