---
title: Álgebra de Diagramas de Bloques
tags:
  - control-clasico
  - teoria
  - modelado
draft: false
aliases:
  - reducción de diagramas
  - bloques
  - diagramas de bloques
---

# Álgebra de Diagramas de Bloques

> [!definicion]
> Un diagrama de bloques representa un sistema con **bloques** (cada uno una FT $G(s)$), **flechas** (señales) y **sumadores** (suman/restan señales). Reducirlo es combinar bloques hasta una sola FT equivalente mediante tres reglas:
> $$\text{Serie: }G_1G_2,\qquad\text{Paralelo: }G_1+G_2,\qquad\text{Lazo: }\frac{G}{1+GH}.$$

> [!info]
> Es la herramienta para obtener la FT de lazo cerrado a partir de la interconexión de las [[Funcion Transferencia/index | funciones de transferencia]] de planta, sensor y controlador. El resultado $T(s)=G/(1+GH)$ alimenta el análisis de [[Polos Ceros | polos]] y [[Estabilidad/index | estabilidad]] del sistema realimentado.

---

## Ejemplo

> [!ejemplo] Reducción serie y paralelo
> **Serie (cascada):** la salida de uno alimenta al siguiente.
> ![[Algebra_Bloques_02.svg|400]]
> $$G_{eq}(s)=G_1(s)\,G_2(s).$$
>
> **Paralelo:** misma entrada, salidas sumadas.
> ![[Algebra_Bloques_03.svg|400]]
> $$G_{eq}(s)=G_1(s)+G_2(s).$$
>
> Numérico: $G_1=\dfrac{2}{s+1}$, $G_2=\dfrac{3}{s+2}$. Serie $\Rightarrow\dfrac{6}{(s+1)(s+2)}$; paralelo $\Rightarrow\dfrac{2}{s+1}+\dfrac{3}{s+2}=\dfrac{5s+7}{(s+1)(s+2)}$.

> [!ejemplo] Lazo cerrado con realimentación negativa
> ![[Algebra_Bloques_04.svg|400]]
> $$T(s)=\frac{G(s)}{1+G(s)H(s)},\qquad H=1\Rightarrow T=\frac{G}{1+G}.$$
> Numérico: $G=\dfrac{4}{s+1}$, $H=1$:
> $$T=\frac{4/(s+1)}{1+4/(s+1)}=\frac{4}{s+5}.$$
> El lazo movió el polo de $-1$ a $-5$ (más rápido) y la ganancia estática de $4$ a $4/5=0.8$.

> [!ejemplo] Reducción de lazos anidados
> ![[Algebra_Bloques_06.svg|400]]
>
> **Paso 1 — Lazo interno** ($G_2$ realimentado por $H_1$):
> $$T_1=\frac{G_2}{1+G_2 H_1}.$$
>
> **Paso 2 — Diagrama equivalente:**
> ![[Algebra_Bloques_08.svg|400]]
>
> **Paso 3 — Lazo externo** ($G_1 T_1$ realimentado por $H_2$):
> $$T_{eq}=\frac{G_1 T_1}{1+G_1 T_1 H_2}.$$
>
> **Paso 4 — Sustituir $T_1$ y simplificar:**
> $$T_{eq}=\frac{G_1\cdot\frac{G_2}{1+G_2 H_1}}{1+G_1 H_2\cdot\frac{G_2}{1+G_2 H_1}}=\frac{G_1 G_2}{1+G_2 H_1+G_1 G_2 H_2}.$$

---

## Demostración del lazo cerrado

> [!teorema] FT de lazo con realimentación negativa
> $$T(s)=\frac{G(s)}{1+G(s)H(s)}.$$

> [!demostracion]
> **Paso 1 — Sumador** (realimentación negativa), siendo $E$ su salida:
> $$E(s)=U(s)-H(s)Y(s).$$
> **Paso 2 — Bloque directo:** $Y(s)=G(s)E(s)$.
> **Paso 3 — Sustituir:** $Y=G[U-HY]=GU-GHY$.
> **Paso 4 — Agrupar:** $Y(1+GH)=GU$.
> **Paso 5 — Despejar $T=Y/U$:** $\displaystyle T=\frac{G}{1+GH}.\ \blacksquare$

> [!proposicion] Realimentación positiva
> Si el sumador es positivo ($E=U+HY$), la misma deducción con signo $+$ da
> $$T(s)=\frac{G(s)}{1-G(s)H(s)}.$$

---

## Reglas de reducción

> [!info] Mover sumadores y bifurcaciones
> | Operación | Equivalencia |
> |---|---|
> | Mover sumador **antes** de un bloque $G$ | la rama que entra se multiplica por $1/G$ |
> | Mover sumador **después** de un bloque $G$ | la rama que entra se multiplica por $G$ |
> | Mover bifurcación **antes** de $G$ | añadir bloque $1/G$ en la rama |
> | Mover bifurcación **después** de $G$ | añadir bloque $G$ en la rama |
>
> Estas equivalencias permiten deshacer lazos cruzados hasta dejar lazos anidados reducibles con las tres reglas básicas.

> [!teorema] Forma canónica (lazo sin caminos cruzados)
> $$T(s)=\frac{\text{suma de productos de caminos directos}}{1-\text{suma de productos de lazos}}.$$
> Para un lazo simple sin camino alternativo: $T=\dfrac{G_1G_2G_3}{1+G_1G_2G_3 H}$.

---

## Limitaciones

> [!warning]
> 1. El álgebra de bloques supone que **todos** los bloques son LTI.
> 2. Con **lazos cruzados** no se aplica directamente: reordenar sumadores/bifurcaciones primero, o usar la fórmula de ganancia de Mason.
> 3. Los sumadores deben ser **lineales** (sin saturación ni otras no linealidades).

---

## Resumen

> [!resumen]
> | Conexión | $G_{eq}(s)$ |
> |---|---|
> | Serie | $G_1 G_2$ |
> | Paralelo | $G_1+G_2$ |
> | Realimentación negativa | $G/(1+GH)$ |
> | Realimentación unitaria | $G/(1+G)$ |
> | Realimentación positiva | $G/(1-GH)$ |
> | Lazos anidados | reducir de dentro hacia afuera |

> [!corolario]
> Reducir un diagrama es aplicar tres reglas —serie, paralelo y lazo— de dentro hacia afuera, moviendo sumadores y bifurcaciones cuando haya cruces. El producto final, $T(s)=G/(1+GH)$, es la FT de lazo cerrado sobre la que se analiza estabilidad y respuesta del sistema realimentado.

> [!referencia]
> - Bloques individuales: [[Funcion Transferencia/index]].
> - Polos del lazo cerrado: [[Polos Ceros]].
> - Estabilidad del lazo: [[Estabilidad/index]].
