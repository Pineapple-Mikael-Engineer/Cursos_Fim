---
titulo: Espacios Vectoriales
tema: Álgebra Lineal
dificultad: intermedio
fuente: Axler, Linear Algebra Done Right, Cap. 1
cssclasses:
  - idea
draft: true
---


# Espacios Vectoriales

Un espacio vectorial es la estructura algebraica fundamental sobre la que se construye todo el álgebra lineal. Captura de manera abstracta la idea de "objetos que se pueden sumar y escalar".

---

## Definición fundamental

> [!definicion] Espacio vectorial
>  Un **espacio vectorial** sobre un campo $\mathbb{F}$ (usualmente $\mathbb{R}$ o $\mathbb{C}$) es un conjunto $V$ equipado con dos operaciones:
> 
> - **Suma:** $+: V \times V \to V$
> - **Producto escalar:** $\cdot, : \mathbb{F} \times V \to V$
> 
> que satisfacen los 8 axiomas vectoriales.

> [!definicion] Subespacio vectorial 
> Un subconjunto $W \subseteq V$ es un **subespacio** si es cerrado bajo suma y producto escalar, y contiene al vector cero: $$W \neq \emptyset, \quad u + v \in W, \quad \alpha v \in W \quad \forall, u,v \in W,, \alpha \in \mathbb{F}$$

---

## Los 8 axiomas

> [!axioma] Axiomas del espacio vectorial
>  Para todo $u, v, w \in V$ y $\alpha, \beta \in \mathbb{F}$:
> 
> 1. **Conmutatividad:** $u + v = v + u$
> 2. **Asociatividad:** $(u+v)+w = u+(v+w)$
> 3. **Identidad aditiva:** $\exists, \mathbf{0} \in V$ tal que $v + \mathbf{0} = v$
> 4. **Inverso aditivo:** $\exists, {-v}$ tal que $v + (-v) = \mathbf{0}$
> 5. **Identidad multiplicativa:** $1 \cdot v = v$
> 6. **Compatibilidad:** $\alpha(\beta v) = (\alpha\beta)v$
> 7. **Distributividad 1:** $\alpha(u+v) = \alpha u + \alpha v$
> 8. **Distributividad 2:** $(\alpha+\beta)v = \alpha v + \beta v$

---

## Teoría de base

> [!teoria] Perspectiva abstracta
>  La potencia de la definición abstracta es que un mismo teorema probado para "espacios vectoriales en general" se aplica simultáneamente a $\mathbb{R}^n$, a espacios de funciones continuas $C[a,b]$, a espacios de polinomios $\mathcal{P}_n$, y a matrices $M_{m\times n}$.
> 
> Esta abstracción no es decorativa: permite transportar intuición geométrica de $\mathbb{R}^3$ a contextos muy distintos.

---

## Resultados principales

> [!teorema] Unicidad del elemento neutro 
> El vector cero de un espacio vectorial es **único**. Si $\mathbf{0}$ y $\mathbf{0}'$ son ambos identidades aditivas, entonces: $$\mathbf{0} = \mathbf{0} + \mathbf{0}' = \mathbf{0}'$$

> [!teorema] Unicidad del inverso aditivo 
> Para cada $v \in V$, su inverso aditivo $-v$ es único. Si $w$ satisface $v + w = \mathbf{0}$, entonces $w = -v$.

---

## Demostración

> [!demostracion] Unicidad del vector cero
>  Supongamos que $\mathbf{0}$ y $\mathbf{0}'$ son ambos identidades aditivas en $V$.
> 
> Como $\mathbf{0}'$ es identidad: $\quad \mathbf{0} = \mathbf{0} + \mathbf{0}'$
> 
> Como $\mathbf{0}$ es identidad: $\quad \mathbf{0} + \mathbf{0}' = \mathbf{0}'$
> 
> Por transitividad: $\mathbf{0} = \mathbf{0}'$. $\quad\square$

---

## Lemas útiles

> [!lema] El cero escalar anula todo vector 
> Para todo $v \in V$: $\quad 0 \cdot v = \mathbf{0}$
> 
> _Prueba:_ $0 \cdot v = (0+0)\cdot v = 0 \cdot v + 0 \cdot v$, luego restando $0 \cdot v$ de ambos lados obtenemos $\mathbf{0} = 0 \cdot v$.

> [!lema] El escalar menos uno invierte Para todo $v \in V$: $\quad (-1) \cdot v = -v$

---

## Corolarios

> [!corolario] Caracterización de subespacios
>  $W \subseteq V$ es subespacio si y solo si para todo $\alpha, \beta \in \mathbb{F}$ y $u, v \in W$: $$\alpha u + \beta v \in W$$ Es decir, basta verificar que $W$ es cerrado bajo **combinaciones lineales**.

---

## Proposición

> [!proposicion] Intersección de subespacios 
> Si ${W_i}_{i \in I}$ es una familia de subespacios de $V$, entonces su intersección: $$\bigcap_{i \in I} W_i$$ es también un subespacio de $V$.

---

## Ejemplos concretos

> [!ejemplo] Verificar que $\mathcal{P}_2(\mathbb{R})$ es espacio vectorial 
> El conjunto de polinomios de grado $\leq 2$: $$\mathcal{P}_2(\mathbb{R}) = {a_0 + a_1 x + a_2 x^2 \mid a_i \in \mathbb{R}}$$
> 
> **Suma:** $(a_0 + a_1x + a_2x^2) + (b_0 + b_1x + b_2x^2) = (a_0+b_0) + (a_1+b_1)x + (a_2+b_2)x^2$ ✓
> 
> **Escalar:** $\lambda(a_0 + a_1x + a_2x^2) = \lambda a_0 + \lambda a_1 x + \lambda a_2 x^2$ ✓
> 
> **Cero:** $p(x) = 0$ ✓ → Por lo tanto $\mathcal{P}_2(\mathbb{R})$ es espacio vectorial de dimensión 3.

---

## Notas y advertencias

> [!note] 
> No todo conjunto con suma y escalar es espacio vectorial Los números naturales $\mathbb{N}$ con la suma usual **no** forman espacio vectorial: no existe inverso aditivo para ningún elemento positivo.

> [!warning] 
> Cuidado con el campo base $\mathbb{R}^2$ como espacio vectorial sobre $\mathbb{R}$ tiene dimensión 2. Pero $\mathbb{C}$ como espacio vectorial sobre $\mathbb{R}$ también tiene dimensión 2. Sin embargo, $\mathbb{C}$ sobre $\mathbb{C}$ tiene dimensión 1. **El campo base importa.**

> [!tip] 
> Verificación rápida de subespacio Para verificar que $W$ es subespacio, solo necesitas comprobar **tres cosas**: $\mathbf{0} \in W$, cerrado bajo suma, cerrado bajo escalar.