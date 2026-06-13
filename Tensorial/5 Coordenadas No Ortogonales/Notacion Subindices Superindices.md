---
title: Notacion de Subindices y Superindices
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-no-ortogonales
  - covarianza
draft: false
aliases:
  - notacion subindices superindices
  - convenio arriba abajo
  - regla de oro indices
  - index notation up down
---

# Notacion de Subindices y Superindices

> [!definicion]
> El convenio de la covarianza/contravarianza coloca el índice **arriba o abajo** según el carácter del objeto:
> - **contravariante** = **superíndice**: componente $v^i$, base dual $\hat g^i$;
> - **covariante** = **subíndice**: componente $v_i$, base $\hat g_i$.
>
> **Regla de oro:** en toda contracción, el índice sumado aparece **una vez arriba y una vez abajo**. Así el producto punto queda $\vec A\cdot\vec B=A^iB_i=A_iB^i$, y la delta mixta cierra $t^i{}_j\,g^j{}_k=\delta^i{}_k$.

> [!info]
> Es el cap. 5.2.4 del libro, dentro del [[index | capítulo 5]]. Reemplaza la notación con tilde $\tilde v_i$ que [[Metrica/index | la métrica]] usaba para las componentes covariantes. Es **conceptual**: fija el lenguaje con que se escriben las [[Transformaciones Contravariantes]] y [[Transformaciones Covariantes]] (las matrices $t^i{}_j$, $g^i{}_j$ tienen un índice arriba y uno abajo).
>
> **Notación:** las **posiciones horizontales** importan. Se escribe $t^i{}_j$ (con espacio: $i$ es el primer índice, $j$ el segundo), nunca $t^i_j$ ambiguo, porque al transponer/contraer hace falta saber cuál índice viene primero.

---

## Ejemplo

> [!ejemplo]
> **Expresiones bien y mal formadas.** La regla arriba/abajo actúa como un chequeo de consistencia: si un índice mudo aparece dos veces arriba o dos veces abajo, la expresión está mal.
>
> | Expresión | ¿Correcta? | Por qué |
> |---|---|---|
> | $\vec v=v^i\hat g_i$ | ✓ | $i$ una vez arriba ($v^i$), una abajo ($\hat g_i$) |
> | $\vec v=v_i\hat g_i$ | ✗ | $i$ **dos veces abajo**: no se forma el vector |
> | $\vec v=v_i\hat g^i$ | ✓ | covariantes con base dual: arriba/abajo |
> | $\vec A\cdot\vec B=A^iB_i$ | ✓ | mezcla un arriba y un abajo (escalar invariante) |
> | $\vec A\cdot\vec B=A^iB^i$ | ✗ | $i$ dos veces arriba; falta bajar uno con $M_{ij}$ |
> | $v'^i=t^i{}_j\,v^j$ | ✓ | mudo $j$ abajo en $t$, arriba en $v$; libre $i$ arriba a ambos lados |
> | $\delta^i{}_k=t^i{}_j\,g^j{}_k$ | ✓ | mudo $j$ arriba en $t$, abajo en $g$ |
>
> **Por qué importa la posición horizontal.** En $t^i{}_j v^j$ se suma sobre el **segundo** índice de $t$; en $g^j{}_i v_j$ se suma sobre el **primero**. Escribir $t^i_j$ sin fijar el orden perdería esa distinción, que es justo la que separa las transformaciones [[Transformaciones Contravariantes | contravariantes]] de las [[Transformaciones Covariantes | covariantes]].

---

## En qué consiste

> [!teoria]
> La idea es que cada índice "recuerde" cómo transforma su objeto. Un superíndice marca lo que transforma con $[t]$ contrayendo el segundo índice (contravariante); un subíndice, lo que transforma con $[g]$ contrayendo el primero (covariante). Como las dos leyes son **recíprocas** ($t^i{}_j g^j{}_k=\delta^i{}_k$), al contraer un superíndice con un subíndice los factores $t$ y $g$ se cancelan y el resultado es **invariante**. Esa es la razón profunda de la regla de oro: solo las contracciones arriba/abajo producen escalares (o tensores) bien definidos.

> [!proposicion] El producto interno y la delta mixta
> Con la convención, el producto punto se escribe con índices cruzados de altura:
> $$\vec A\cdot\vec B=A^iB_i=A_iB^i.$$
> El índice sumado $i$ aparece **una vez arriba y una vez abajo** (es lo mismo que mezclar componentes covariantes y contravariantes, como exigía [[Metrica/index | la métrica]] al escribir $\vec A\cdot\vec B=A^i\tilde B_i$). Igualmente, la naturaleza recíproca de $[t]$ y $[g]$ se anota
> $$t^i{}_j\,g^j{}_k=\delta^i{}_k,$$
> con la **delta mixta** $\delta^i{}_k$ (un superíndice, un subíndice): vale $1$ si $i=k$ y $0$ si no, y es la forma covariante/contravariante de la identidad.

> [!proposicion] Las bases heredan la altura opuesta a su componente
> Para que $\vec v=v^i\hat g_i$ tenga índices balanceados, la base $\hat g_i$ debe llevar **subíndice** (covariante): así $i$ queda arriba en $v^i$ y abajo en $\hat g_i$. Coherentemente, la base dual lleva **superíndice** $\hat g^i$ y permite $\vec v=v_i\hat g^i$. Esto encaja con cómo transforman: $\hat g_i$ es covariante y $\hat g^i$ contravariante (ver [[Transformaciones Covariantes]]).

> [!warning] Por qué la convención evita errores
> 1. Un índice **no** debe aparecer más de **dos** veces por término (igual que en Einstein cartesiano).
> 2. Un índice mudo siempre va **una vez arriba y una vez abajo**; dos arriba o dos abajo señala un error (falta subir/bajar con la métrica $M_{ij}$).
> 3. Un índice **libre** debe aparecer a la **misma altura** en ambos lados de la ecuación (en $v'^i=t^i{}_j v^j$, la $i$ libre está arriba en los dos miembros).
> 4. Conserva la **posición horizontal**: $t^i{}_j\neq t_j{}^i$ en general; escribir $t^i_j$ pierde el orden y vuelve ambigua la contracción.

## Resumen

> [!resumen]
> | Carácter | Altura | Componente | Base | Transforma con |
> |---|---|---|---|---|
> | Contravariante | super**índice** | $v^i$ | $\hat g^i$ | $[t]$, contrae 2.º índice |
> | Covariante | sub**índice** | $v_i$ | $\hat g_i$ | $[g]$, contrae 1.er índice |
> | Mezcla (escalar) | arriba+abajo | $A^iB_i=A_iB^i$ | — | invariante |
> | Delta mixta | $\delta^i{}_k$ | \| $t^i{}_j g^j{}_k=\delta^i{}_k$ \| | — | — |

> [!corolario]
> La convención es simple pero poderosa: superíndice = contravariante, subíndice = covariante, y todo índice sumado mezcla una de cada (regla de oro). Con ella, $\vec v=v^i\hat g_i$ es correcto y $v_i\hat g_i$ es un error visible a simple vista; el producto interno $A^iB_i$ es manifiestamente invariante; y las posiciones horizontales de $t^i{}_j$, $g^j{}_i$ distinguen sin ambigüedad las transformaciones covariantes de las contravariantes. Es la notación que se hereda en tensores ([[Metrica/index | métrica]]) y en Relatividad.

> [!referencia]
> - De dónde sale (componentes covariantes con tilde): [[Metrica/index]].
> - Cómo se usan los índices de $[t]$ y $[g]$: [[Transformaciones Contravariantes]] · [[Transformaciones Covariantes]].
> - La convención de Einstein original (cartesiana): [[1 Algebra Lineal y Notacion/Notacion Indices Sumatorias]].
