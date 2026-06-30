---
title: Principio del Maximo Eliptico
order: 6
tags:
  - ecuaciones
  - edp
  - teoria
  - laplace
  - principio-del-maximo
draft: false
aliases:
  - principio del máximo elíptico
  - principio del máximo fuerte
  - maximum principle
  - elliptic maximum principle
---

# Principio del Máximo Elíptico

> [!definicion]
> Sea $u$ una función **armónica** ($\nabla^2u=0$) y **continua** en un dominio **acotado** $\Omega$ con frontera $\partial\Omega$. Entonces $u$ alcanza tanto su **máximo** como su **mínimo** sobre la **frontera** $\partial\Omega$, y **nunca** en un punto interior —salvo en el caso trivial en que $u$ sea **constante** en todo $\Omega$—. Esta versión, que prohíbe extremos interiores estrictos, es el **principio del máximo fuerte**:
> $$\max_{\overline{\Omega}}u=\max_{\partial\Omega}u,\qquad \min_{\overline{\Omega}}u=\min_{\partial\Omega}u.$$

> [!info]
> Una de las consecuencias estructurales de la sección [[Ecuacion de Laplace y Poisson/index| Laplace y Poisson]], dentro del [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]]. Es el reverso geométrico de la [[Teorema del Valor Medio| propiedad del valor medio]]: si cada punto es el promedio de su entorno, ningún punto interior puede sobresalir por encima de todos sus vecinos. Es la herramienta clave para probar la **unicidad** y la **estabilidad** del problema de Dirichlet sobre [[Funciones Armonicas| funciones armónicas]].

---

## Ejemplo

> [!ejemplo]
> **Temperatura de equilibrio en una placa.** Una placa metálica ocupa el cuadrado $\Omega=[0,1]\times[0,1]$. Su temperatura estacionaria $u(x,y)$ es armónica ($\nabla^2u=0$). Supongamos que en el borde la temperatura varía entre $10^\circ$ y $90^\circ$.
>
> **Paso 1 — Acotar sin resolver.** Sin calcular $u$ en el interior, el principio del máximo garantiza de inmediato
> $$10^\circ\le u(x,y)\le 90^\circ\qquad\text{en todo el interior.}$$
> Físicamente: en equilibrio, ningún punto interior puede estar más caliente que el punto más caliente del borde, ni más frío que el más frío. No hay "focos de calor" internos sin fuente —coherente con que Laplace es la ecuación **sin fuentes**—.
>
> **Paso 2 — Localizar el extremo.** Si alguien afirma que el máximo de $u$ está en el centro $(\tfrac12,\tfrac12)$, sabemos que **se equivoca**: a menos que $u$ sea constante, el máximo vive en $\partial\Omega$. El interior solo **interpola** suavemente los valores del borde.
>
> **Paso 3 — Si la frontera es constante.** Si $u=20^\circ$ en todo el borde, entonces máximo y mínimo coinciden ($20^\circ$), y por el principio $u\equiv20^\circ$ en toda la placa: la única armónica con borde constante es la constante.

---

## En qué consiste

> [!teoria]
> La intuición es directa: una función armónica representa un **equilibrio perfecto** donde cada valor es la **media** de su entorno. Un máximo interior estricto sería un punto **estrictamente mayor** que el promedio de sus vecinos —imposible si el valor *es* ese promedio—. Por eso los "picos" y "valles" están desterrados al borde, donde la condición de valor medio ya no aplica (no hay entorno completo dentro del dominio). El interior de una función armónica es liso y sin relieve propio: solo estira la membrana entre las alturas que le impone la frontera.

> [!teorema] Principio del máximo (versión débil)
> Si $u$ es armónica en $\Omega$ acotado y continua en $\overline{\Omega}$, entonces $\displaystyle\max_{\overline\Omega}u=\max_{\partial\Omega}u$.

> [!demostracion]
> Damos la prueba clásica vía **perturbación**, que evita tecnicismos del valor medio.
>
> **Paso 1 — Perturbar.** Para $\varepsilon>0$ definimos $v(x)=u(x)+\varepsilon|x|^2$. En $\mathbb{R}^n$, $\nabla^2|x|^2=2n$, luego
> $$\nabla^2 v=\nabla^2u+\varepsilon\,\nabla^2|x|^2=0+2n\varepsilon=2n\varepsilon>0.$$
>
> **Paso 2 — $v$ no tiene máximo interior.** En un máximo interior la matriz Hessiana es semidefinida negativa, así que su traza $\nabla^2 v\le0$. Pero acabamos de ver $\nabla^2 v=2n\varepsilon>0$: contradicción. Por tanto $v$ alcanza su máximo en la **frontera**: $\displaystyle\max_{\overline\Omega}v=\max_{\partial\Omega}v$.
>
> **Paso 3 — Quitar la perturbación.** Sea $M=\max_{\partial\Omega}u$ y $R$ el radio máximo de $\Omega$. Para todo $x\in\overline\Omega$,
> $$u(x)\le v(x)\le\max_{\partial\Omega}v\le M+\varepsilon R^2.$$
> Como esto vale para **todo** $\varepsilon>0$, hacemos $\varepsilon\to0$ y obtenemos $u(x)\le M=\max_{\partial\Omega}u$. El mínimo se trata aplicando lo anterior a $-u$ (también armónica). $\blacksquare$

> [!demostracion] Variante vía valor medio (versión fuerte)
> **Paso 1 — Suponer un máximo interior.** Sea $M=\max_{\overline\Omega}u$ y supongamos que se alcanza en un punto **interior** $P$, con $u(P)=M$.
>
> **Paso 2 — Aplicar el valor medio.** Por la [[Teorema del Valor Medio| propiedad del valor medio]], $u(P)$ es el **promedio** de $u$ sobre cualquier esfera pequeña centrada en $P$ y contenida en $\Omega$. Como todos esos valores cumplen $u\le M=u(P)$, el promedio solo puede ser igual a $M$ **si $u\equiv M$ en toda la esfera**.
>
> **Paso 3 — Propagar.** Repitiendo el argumento desde cada nuevo punto, el conjunto $\{u=M\}$ resulta ser a la vez **abierto** (cada punto arrastra una bola entera) y **cerrado** (por continuidad). Como $\Omega$ es **conexo**, ese conjunto es **todo $\Omega$**: $u$ es constante. Luego, si $u$ no es constante, no hay máximo interior. $\blacksquare$

> [!proposicion] Consecuencias para el problema de Dirichlet
> Del principio del máximo se siguen tres resultados centrales:
> 1. **Unicidad.** Si $u_1,u_2$ son armónicas con el mismo dato de frontera $f$, su diferencia $w=u_1-u_2$ es armónica con $w=0$ en $\partial\Omega$. Por el principio, $\max w=\min w=0$, luego $w\equiv0$ y $u_1=u_2$. El problema de Dirichlet tiene **a lo sumo una** solución.
> 2. **Estabilidad.** Si $u_1,u_2$ resuelven Dirichlet con datos $f_1,f_2$, entonces $w=u_1-u_2$ es armónica y $\displaystyle\max_{\overline\Omega}|u_1-u_2|\le\max_{\partial\Omega}|f_1-f_2|$. Pequeñas perturbaciones del dato producen pequeñas perturbaciones de la solución: el problema está **bien planteado**.
> 3. **Comparación.** Si dos armónicas cumplen $u_1\le u_2$ en la frontera, entonces $u_1\le u_2$ en **todo** $\Omega$ (aplicar el principio a $u_1-u_2$). El orden en el borde se hereda al interior.

> [!warning]
> Las hipótesis importan. El principio falla si el dominio es **no acotado** (p. ej. $u=x$ en un semiplano no tiene máximo) o si $u$ **no es continua hasta la frontera**. Para la ecuación de **Poisson** $\nabla^2u=g$ con $g$ de signo definido se obtienen principios análogos pero modificados (sub/superarmónicas): una fuente positiva sí puede crear un mínimo interior.

---

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Enunciado | armónica $\Rightarrow$ máx y mín en la **frontera** |
> | Versión fuerte | sin extremos interiores, salvo $u$ constante |
> | Hipótesis | $\Omega$ acotado y conexo; $u$ continua en $\overline\Omega$ |
> | Pruebas | perturbación $v=u+\varepsilon\|x\|^2$; o valor medio + conexidad |
> | Unicidad | Dirichlet con mismo dato $\Rightarrow$ misma solución |
> | Estabilidad | $\max\|u_1-u_2\|\le\max_{\partial}\|f_1-f_2\|$ |

> [!corolario]
> El principio del máximo es la razón de fondo por la que el problema de Dirichlet está **bien planteado**: la solución es **única**, depende **continuamente** del dato de frontera y respeta el **orden** del borde. Toda la rigidez de lo armónico —el que el interior no pueda "inventar" relieve— queda capturada en este único enunciado.

> [!referencia]
> - El resultado del que se deduce: [[Teorema del Valor Medio]].
> - El objeto sobre el que actúa: [[Funciones Armonicas]].
> - El marco general de la sección: [[Ecuacion de Laplace y Poisson/index]].
