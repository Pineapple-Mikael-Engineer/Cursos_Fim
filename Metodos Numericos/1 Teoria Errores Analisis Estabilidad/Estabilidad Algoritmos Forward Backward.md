---
title: Estabilidad de Algoritmos (Forward y Backward)
tags:
  - metodos-numericos
  - teoria
  - error-numerico
  - estabilidad
draft: false
aliases:
  - Estabilidad numérica
  - Forward stability
  - Backward stability
  - Análisis regresivo
  - Análisis de error hacia atrás
---

# Estabilidad de Algoritmos: Análisis Hacia Adelante y Hacia Atrás

> [!definicion]
> La **estabilidad** es una propiedad del **algoritmo** (no del problema) que mide cuánto error introduce su ejecución en aritmética de punto flotante. Un algoritmo es **estable** si la solución que calcula es la solución exacta de un problema *cercano* al original.

> [!info]
> La estabilidad se separa del [[Condicionamiento Numerico Numero Condicion|condicionamiento]], que es propiedad del problema. Un problema mal condicionado no admite solución numérica precisa con ningún algoritmo; un algoritmo inestable arruina la solución incluso de un problema bien condicionado. Estabilidad + buen condicionamiento son ambos necesarios para un resultado fiable.

---

## Las dos medidas del error

Sea $y = f(x)$ el resultado exacto y $\tilde y = \tilde f(x)$ el resultado calculado por el algoritmo.

> [!definicion]
> - **Error hacia adelante** (*forward error*): la diferencia entre el resultado calculado y el exacto,
> $$\frac{\|\tilde y - y\|}{\|y\|}.$$
> - **Error hacia atrás** (*backward error*): el menor $\Delta x$ tal que el resultado calculado es *exacto* para un dato perturbado,
> $$\tilde y = f(x + \Delta x), \qquad \text{error hacia atrás} = \frac{\|\Delta x\|}{\|x\|}.$$

> [!teoria]
> El análisis hacia atrás, introducido por Wilkinson, traslada el error del **resultado** a los **datos**: en lugar de preguntar "¿cuánto se equivocó el cálculo?", pregunta "¿de qué problema ligeramente distinto es esta la respuesta exacta?". Esto desacopla la responsabilidad del algoritmo (error hacia atrás) de la sensibilidad del problema (condicionamiento).

---

## Relación fundamental: forward ≲ condición × backward

> [!teorema]
> Para un problema con [[Condicionamiento Numerico Numero Condicion|número de condición]] $\kappa$, los tres conceptos se relacionan por:
> $$\underbrace{\frac{\|\tilde y - y\|}{\|y\|}}_{\text{error hacia adelante}} \;\lesssim\; \underbrace{\kappa}_{\text{condición del problema}} \;\cdot\; \underbrace{\frac{\|\Delta x\|}{\|x\|}}_{\text{error hacia atrás}}.$$

> [!demostracion]
> Si $\tilde y = f(x + \Delta x)$, una expansión de primer orden de $f$ alrededor de $x$ da
> $$\tilde y - y = f(x + \Delta x) - f(x) \approx f'(x)\,\Delta x.$$
> Tomando normas relativas y usando la definición del número de condición $\kappa = \dfrac{\|x\|\,\|f'(x)\|}{\|f(x)\|}$:
> $$\frac{\|\tilde y - y\|}{\|y\|} \approx \frac{\|f'(x)\Delta x\|}{\|f(x)\|} \leq \frac{\|x\|\,\|f'(x)\|}{\|f(x)\|}\cdot\frac{\|\Delta x\|}{\|x\|} = \kappa\cdot\frac{\|\Delta x\|}{\|x\|}.$$

> [!info]
> Esta es la **regla de oro** del análisis numérico: el error que percibe el usuario (hacia adelante) es el producto de algo que controla el algoritmo (error hacia atrás) por algo que controla el problema (condición). Un algoritmo *estable hacia atrás* garantiza error hacia atrás del orden de la [[Epsilon Maquina y Precision Relativa|unidad de redondeo]] $u$; el error hacia adelante resultante es entonces $\lesssim \kappa\,u$.

---

## Tipos de estabilidad

> [!definicion]
> - **Estable hacia atrás** (*backward stable*): el error hacia atrás es del orden de $u$, es decir, $\tilde y = f(x+\Delta x)$ con $\|\Delta x\|/\|x\| = O(u)$. Es la noción más fuerte y deseable.
> - **Estable hacia adelante** (*forward stable*): el error hacia adelante es del orden de $\kappa\,u$, comparable al de un algoritmo estable hacia atrás, aunque no exista un $\Delta x$ pequeño que lo explique.
> - **Inestable**: el error crece más rápido que $\kappa\,u$ (típicamente por [[Perdida Significancia y Cancelacion Catastrofica|cancelación catastrófica]] o crecimiento de factores intermedios).

> [!info]
> Estable hacia atrás $\Rightarrow$ estable hacia adelante (por la relación fundamental), pero el recíproco no se cumple. Por eso el objetivo de diseño es siempre la **estabilidad regresiva**: implica buen comportamiento sin importar el condicionamiento del problema concreto.

---

## Ejemplo: suma de punto flotante

> [!ejemplo]
> **La suma en coma flotante es estable hacia atrás.** Sea el cálculo de $s = a + b$. El resultado redondeado satisface, con $|\delta| \leq u$:
> $$\tilde s = (a + b)(1 + \delta) = a(1+\delta) + b(1+\delta) = \tilde a + \tilde b.$$
> El resultado calculado es la suma **exacta** de datos perturbados $\tilde a = a(1+\delta)$, $\tilde b = b(1+\delta)$, con perturbación relativa $\leq u$. Luego la suma es backward stable.
>
> **El producto interno también lo es.** Para $s = \sum_{i=1}^n x_i y_i$ evaluado en orden, el resultado calculado satisface
> $$\tilde s = \sum_{i=1}^n x_i y_i (1 + \theta_i), \qquad |\theta_i| \leq \gamma_n = \frac{n u}{1 - n u} \approx n u.$$
> El error hacia atrás crece linealmente con $n$, pero sigue siendo $O(u)$ para $n$ moderado.

---

## Ejemplo: una fórmula inestable y su reparación

> [!ejemplo]
> **Raíces de $ax^2 + bx + c = 0$.** La fórmula clásica $x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ es inestable para la raíz pequeña cuando $b^2 \gg 4ac$: al evaluar $-b + \sqrt{b^2-4ac}$ con $b>0$ se restan dos cantidades casi iguales y ocurre [[Perdida Significancia y Cancelacion Catastrofica|cancelación catastrófica]].
>
> Con $a=1$, $b=10^8$, $c=1$ (raíces $\approx -10^{-8}$ y $\approx -10^8$) en doble precisión, la raíz pequeña sale con pocos dígitos correctos.
>
> **Reparación (estable):** calcular la raíz de mayor módulo y obtener la otra por la relación de Vieta $x_1 x_2 = c/a$:
> $$x_1 = \frac{-b - \operatorname{sgn}(b)\sqrt{b^2-4ac}}{2a}, \qquad x_2 = \frac{c}{a\,x_1}.$$
> El problema (las raíces) está bien condicionado; solo la **implementación** era inestable. El análisis distingue ambas cosas.

---

## Diagrama del análisis hacia atrás

> [!teoria]
> El análisis regresivo se visualiza con dos caminos de $x$ a $\tilde y$:
>
> - **Camino directo:** $x \xrightarrow{\;\tilde f\;} \tilde y$ (lo que hace el algoritmo).
> - **Camino indirecto:** $x \xrightarrow{+\Delta x} x+\Delta x \xrightarrow{\;f\;} \tilde y$ (función exacta sobre dato perturbado).
>
> Que ambos caminos lleguen al mismo $\tilde y$ con $\Delta x$ pequeño *es* la estabilidad hacia atrás. El error hacia adelante mide la distancia vertical $\tilde y \to y$; la condición $\kappa$ es la amplificación que sufre $\Delta x$ al pasar por $f$.

---

## Estabilidad de algoritmos matriciales

> [!info]
> Resultados clásicos de estabilidad hacia atrás (Wilkinson, Higham):
>
> | Algoritmo | Estabilidad hacia atrás |
> |:---|:---|
> | Sustitución directa/regresiva (triangular) | Siempre estable |
> | [[Eliminacion Gaussiana]] con [[Pivoteo Parcial Total Estabilidad\|pivoteo parcial]] | Estable en la práctica ($\|\Delta A\| \lesssim \rho\, n\, u\, \|A\|$) |
> | Eliminación de Gauss **sin** pivoteo | Inestable en general |
> | [[Factorizacion Cholesky Matrices Definidas Positivas\|Cholesky]] | Incondicionalmente estable |
> | Factorización QR (Householder) | Estable hacia atrás |
>
> El factor de crecimiento $\rho$ de la [[Pivoteo Parcial Total Estabilidad|eliminación con pivoteo]] es la cantidad que puede degradar la estabilidad; en la práctica $\rho = O(1)$, aunque existen matrices patológicas con $\rho = 2^{n-1}$.

---

## Relación con otras notas

> [!info]
> - El error introducido por cada operación elemental nace de la [[Representacion Punto Flotante IEEE 754|representación en punto flotante]] y se cuantifica con la [[Epsilon Maquina y Precision Relativa|unidad de redondeo]] $u$.
> - El mecanismo más común de inestabilidad es la [[Perdida Significancia y Cancelacion Catastrofica|cancelación catastrófica]].
> - Cómo se acumulan estos errores en cadenas de operaciones matriciales se desarrolla en [[Propagacion Errores Operaciones Matriciales]].
> - La sensibilidad del problema, factor que multiplica al error hacia atrás, es el [[Condicionamiento Numerico Numero Condicion|número de condición]].

---

## Resumen

| Concepto | Pertenece a | Mide |
|:---|:---|:---|
| Error hacia adelante | resultado | $\|\tilde y - y\|/\|y\|$ |
| Error hacia atrás | algoritmo | menor $\|\Delta x\|/\|x\|$ con $\tilde y = f(x+\Delta x)$ |
| Condición $\kappa$ | problema | amplificación de perturbaciones |
| Relación clave | — | forward $\lesssim \kappa\cdot$ backward |
| Backward stable | objetivo de diseño | error hacia atrás $= O(u)$ |

> [!corolario]
> La estabilidad es responsabilidad del algoritmo y se mide mejor hacia atrás: un algoritmo backward stable produce la respuesta exacta de un problema casi idéntico, con perturbación del orden de la unidad de redondeo. El error que finalmente observa el usuario obedece a forward $\lesssim \kappa \cdot$ backward, de modo que la calidad de un cálculo numérico requiere simultáneamente un algoritmo estable y un problema bien condicionado. El diseño de algoritmos numéricos —[[Pivoteo Parcial Total Estabilidad|pivoteo]], reordenamiento de operaciones, evitar [[Perdida Significancia y Cancelacion Catastrofica|cancelación]]— persigue justamente la estabilidad regresiva.
