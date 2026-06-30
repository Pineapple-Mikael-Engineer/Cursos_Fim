---
title: Puntos Singulares Regulares
order: 1
tags:
  - ecuaciones
  - edo
  - teoria
  - series
  - frobenius
  - puntos-singulares
draft: false
aliases:
  - punto singular regular
  - punto singular irregular
  - clasificación de puntos
  - regular singular point
  - irregular singular point
---

# Puntos Singulares Regulares

> [!definicion]
> Para $y''+p(x)\,y'+q(x)\,y=0$, el punto $x_0$ es **singular** si $p$ o $q$ **no** son analíticas en $x_0$. La singularidad es **REGULAR** (dócil, tratable por Frobenius) si los límites
> $$p_0=\lim_{x\to x_0}(x-x_0)\,p(x),\qquad q_0=\lim_{x\to x_0}(x-x_0)^2\,q(x)$$
> **existen y son finitos** —equivalentemente, si $(x-x_0)\,p$ y $(x-x_0)^2\,q$ son **analíticas** en $x_0$—. Si alguno de esos límites **no** existe (la singularidad es demasiado fuerte), el punto es **singular IRREGULAR** y el método de Frobenius **no garantiza** solución en serie.

> [!info]
> El paso previo del [[Frobenius/index| método de Frobenius]]: antes de proponer cualquier serie hay que **clasificar** el punto. Solo en puntos singulares **regulares** el método funciona con garantía. Si el punto es ordinario, se usan los [[Puntos Ordinarios]].

---

## Ejemplo

> [!ejemplo] Bessel: el origen es singular REGULAR
> **Ecuación de Bessel** $x^2y''+xy'+(x^2-\nu^2)y=0$. Para clasificar $x=0$ la llevamos a la forma estándar dividiendo por $x^2$:
> $$y''+\underbrace{\frac{1}{x}}_{p}\,y'+\underbrace{\frac{x^2-\nu^2}{x^2}}_{q}\,y=0.$$
> **Paso 1 — ¿analíticas?** $p=1/x$ explota en $0$ y $q$ también: **$x=0$ es singular**. **Paso 2 — probar la regularidad:**
> $$x\,p=x\cdot\frac1x=1,\qquad x^2q=x^2\cdot\frac{x^2-\nu^2}{x^2}=x^2-\nu^2.$$
> Ambas son **polinomios**, analíticas en $0$. Los límites $p_0=1$ y $q_0=-\nu^2$ existen. **Conclusión:** $x=0$ es **singular regular** → Frobenius aplica (y produce las funciones de Bessel).

> [!ejemplo] Una singularidad IRREGULAR
> **$x^3y''+y=0$.** En forma estándar $y''+0\cdot y'+\dfrac{1}{x^3}y=0$, así que $p=0$, $q=1/x^3$. El punto $x=0$ es singular. Probamos la regularidad:
> $$x\,p=0\ \text{(bien)},\qquad x^2q=x^2\cdot\frac{1}{x^3}=\frac1x\ \xrightarrow[x\to0]{}\ \infty.$$
> El límite $q_0$ **no existe**: $x^2q$ no es analítica. Por tanto $x=0$ es **singular irregular** y Frobenius **no** garantiza una solución en serie.

> [!ejemplo] El prototipo: la ecuación de Euler
> **$x^2y''+a\,x\,y'+b\,y=0$**, es decir $p=a/x$, $q=b/x^2$. Entonces $xp=a$ y $x^2q=b$ son **constantes** (analíticas): $x=0$ es **singular regular**, el caso "más limpio" posible. Sus soluciones exactas $y=x^{m}$ con $m(m-1)+am+b=0$ son el **molde** de la ecuación indicial: los límites $p_0=a$, $q_0=b$ son justo los coeficientes que aparecerán en [[Ecuacion Indicial| la indicial]].

---

## En qué consiste

> [!teoria] La idea de "singularidad dócil"
> Que $p$ tenga a lo sumo un polo **simple** y $q$ a lo sumo un polo **doble** en $x_0$ es exactamente lo que permite escribir la EDO como
> $$(x-x_0)^2y''+(x-x_0)\big[(x-x_0)p\big]y'+\big[(x-x_0)^2q\big]y=0,$$
> con $(x-x_0)p$ y $(x-x_0)^2q$ **analíticas**. Esa forma es una "ecuación de Euler con coeficientes en serie": el término dominante reproduce a Euler (de ahí el $x^{r}$) y el resto se corrige con la serie $\sum a_n x^n$. Si los polos fueran más fuertes (singularidad irregular), no hay un $x^{r}$ que domine y el método se rompe.

> [!algoritmo] Clasificar un punto $x_0$
> 1. Escribe la EDO en forma estándar $y''+p\,y'+q\,y=0$ (divide por el coeficiente de $y''$).
> 2. ¿Son $p$ y $q$ **analíticas** en $x_0$? Si **sí** → punto **ordinario** (usa [[Puntos Ordinarios]]).
> 3. Si **no**, calcula $p_0=\lim_{x\to x_0}(x-x_0)p$ y $q_0=\lim_{x\to x_0}(x-x_0)^2q$.
> 4. ¿Existen ambos límites (finitos)? Si **sí** → **singular regular** (aplica [[Frobenius/index|Frobenius]]).
> 5. Si **alguno diverge** → **singular irregular** (Frobenius no garantiza solución).

> [!proposicion] Criterio práctico con polos
> Si $p$ tiene en $x_0$ un polo de orden $\le 1$ **y** $q$ un polo de orden $\le 2$, el punto es singular regular. Basta una multiplicación por $(x-x_0)$ y $(x-x_0)^2$ para "limpiar" la singularidad.

> [!warning]
> Hay que pasar **siempre** a la forma estándar $y''+p y'+q y=0$ antes de clasificar: si se trabaja con el coeficiente de $y''$ sin normalizar, $p$ y $q$ no son los correctos y la prueba de los límites falla. Cuidado también con singularidades en el **infinito**: se estudian con el cambio $t=1/x$.

## Resumen

> [!resumen]
> | Tipo de punto | Condición | Método |
> |---|---|---|
> | Ordinario | $p,q$ analíticas | serie de Taylor ([[Puntos Ordinarios\|Puntos Ordinarios]]) |
> | Singular regular | $(x-x_0)p$ y $(x-x_0)^2q$ analíticas | [[Frobenius/index\|Frobenius]] (garantizado) |
> | Singular irregular | algún límite diverge | sin garantía |

> [!corolario]
> La clasificación es una prueba de **dos límites**: $(x-x_0)p$ y $(x-x_0)^2q$. Si ambos existen, la singularidad es dócil y Frobenius funciona; el siguiente paso es montar la [[Ecuacion Indicial| ecuación indicial]] para hallar el exponente $r$.

> [!referencia]
> - El exponente $r$ del método: [[Ecuacion Indicial]].
> - El caso sin singularidad: [[Puntos Ordinarios]].
> - El método completo: [[Frobenius/index]].
