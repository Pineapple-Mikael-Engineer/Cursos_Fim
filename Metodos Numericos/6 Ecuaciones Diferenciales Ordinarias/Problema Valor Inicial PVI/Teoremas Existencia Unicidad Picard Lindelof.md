---
title: Existencia y Unicidad — Teorema de Picard-Lindelöf
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-inicial
draft: false
aliases:
  - Picard-Lindelöf
  - Existencia y unicidad de EDOs
  - Teorema de existencia y unicidad
  - Condición de Lipschitz
---

# Existencia y Unicidad: Teorema de Picard-Lindelöf

> [!definicion]
> El **teorema de Picard-Lindelöf** garantiza que el [[Problema Valor Inicial PVI/index|problema de valor inicial]] $y' = f(t,y)$, $y(t_0)=y_0$ tiene una **única** solución en un entorno de $t_0$, siempre que $f$ sea continua y **Lipschitz** en $y$.

> [!info]
> La unicidad es la condición previa que da sentido a la simulación: si por un mismo estado inicial pasara más de una trayectoria, "la" solución numérica no aproximaría nada bien definido. La condición de Lipschitz es, además, la que controla la **propagación de errores** en todos los métodos numéricos.

---

## Condición de Lipschitz

> [!definicion]
> $f(t,y)$ es **Lipschitz en $y$** (con constante $L$) en una región $D$ si
> $$\|f(t, y_1) - f(t, y_2)\| \leq L\,\|y_1 - y_2\| \qquad \forall (t,y_1), (t,y_2)\in D.$$
> Si $f$ tiene derivada parcial $\partial f/\partial y$ acotada, entonces $L = \max\|\partial f/\partial y\|$ sirve (por el teorema del valor medio).

> [!info]
> Geométricamente, $L$ acota cuán rápido pueden **separarse o juntarse** dos soluciones vecinas. Es la constante que aparecerá en la cota del [[Error Local Truncamiento vs Error Global Acumulado|error global]]: $\|e_n\| \lesssim \frac{C}{L}(e^{L(t_n-t_0)}-1)h^p$.

---

## Teorema

> [!teorema]
> Sea $f$ continua en $D = [t_0-a, t_0+a]\times\{\|y-y_0\|\leq b\}$ y Lipschitz en $y$ con constante $L$. Entonces el PVI $y'=f(t,y)$, $y(t_0)=y_0$ tiene una **única** solución $y(t)$ en $[t_0-\alpha, t_0+\alpha]$, con $\alpha = \min(a, b/M)$ y $M = \max_D\|f\|$.

> [!demostracion]
> **Iteración de Picard.** El PVI equivale a la ecuación integral $y(t) = y_0 + \int_{t_0}^t f(s, y(s))\,ds$. Se define la sucesión
> $$y^{(0)}(t) = y_0, \qquad y^{(k+1)}(t) = y_0 + \int_{t_0}^t f(s, y^{(k)}(s))\,ds.$$
> El operador $T[y](t) = y_0 + \int_{t_0}^t f(s,y(s))\,ds$ es una **contracción** en norma adecuada: usando Lipschitz,
> $$\|T[y_1] - T[y_2]\|_\infty \leq L\,|t-t_0|\,\|y_1-y_2\|_\infty,$$
> que es contractiva para $|t-t_0|$ pequeño. Por el [[Condicion Contraccion Norma Matricial|teorema de punto fijo de Banach]], $T$ tiene un único punto fijo: la solución única. (La extensión a todo el intervalo se hace por continuación.)

> [!info]
> La iteración de Picard es la versión continua de la [[Condicion Contraccion Norma Matricial|iteración de punto fijo contractiva]], y su análogo discreto justifica la convergencia de los métodos numéricos. La misma constante $L$ gobierna ambas.

---

## Ejemplo: cuándo falla la unicidad

> [!ejemplo]
> **EDO sin unicidad: $y' = \sqrt{|y|}$, $y(0)=0$.** Aquí $f(y)=\sqrt{|y|}$ **no** es Lipschitz en $y=0$ (su pendiente $\to\infty$). El PVI tiene infinitas soluciones:
> $$y(t) \equiv 0 \quad\text{y}\quad y(t) = \tfrac{1}{4}(t-c)^2 \text{ para } t\geq c,\ \forall c\geq 0.$$
> Un método numérico aplicado aquí daría resultados impredecibles. La condición de Lipschitz **excluye** estas patologías.

> [!ejemplo]
> **Explosión en tiempo finito: $y' = y^2$, $y(0)=1$.** $f=y^2$ es Lipschitz **localmente** pero no globalmente; la solución $y(t)=\frac{1}{1-t}$ escapa a $+\infty$ en $t=1$. El teorema solo garantiza existencia **local** ($\alpha$ finito): la solución existe hasta que se sale de la región.

---

## Consecuencias para el cálculo numérico

> [!proposicion]
> 1. **Buena definición:** con $f$ Lipschitz, la trayectoria es única y la simulación aproxima un objeto bien definido.
> 2. **Dependencia continua de los datos:** soluciones con condiciones iniciales próximas se separan a lo sumo como $e^{L t}$ (problema bien condicionado si $L$ moderado; mal condicionado —caótico— si $L$ grande).
> 3. **Cota de error:** la constante $L$ entra directamente en la acumulación del [[Error Local Truncamiento vs Error Global Acumulado|error global]].

> [!warning]
> **Condicionamiento del PVI.** Aunque la solución sea única, si $L$ es grande (o $\partial f/\partial y > 0$ grande) los errores crecen exponencialmente: el problema está **mal condicionado** y ninguna precisión del método lo salva. Es el análogo dinámico del [[Condicionamiento Numerico Numero Condicion|número de condición]]. Los sistemas caóticos (Lorenz) son el caso extremo.

---

## Relación con otras notas

> [!info]
> - El método de un paso más simple sobre esta base: [[Euler Explicito Orden 1 Interpretacion Geometrica]].
> - Cómo $L$ entra en la cota de error: [[Error Local Truncamiento vs Error Global Acumulado]].
> - La contracción análoga discreta: [[Condicion Contraccion Norma Matricial]].
> - La extensión a sistemas (Lipschitz vectorial): [[Reduccion EDO Orden n a Sistema Primer Orden]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Hipótesis | $f$ continua y Lipschitz en $y$ |
| Lipschitz | $\|f(t,y_1)-f(t,y_2)\| \leq L\|y_1-y_2\|$ |
| Conclusión | solución **única** local |
| Prueba | iteración de Picard (contracción de Banach) |
| Sin Lipschitz | posible no unicidad ($y'=\sqrt{|y|}$) |
| Papel de $L$ | controla propagación de errores y condicionamiento |

> [!corolario]
> El teorema de Picard-Lindelöf garantiza solución única del PVI cuando $f$ es Lipschitz en $y$, probándolo con la iteración de Picard como contracción de Banach —la versión continua de la [[Condicion Contraccion Norma Matricial|iteración de punto fijo]]—. La condición de Lipschitz no es un tecnicismo: su constante $L$ controla cuánto se separan soluciones vecinas, define el condicionamiento del problema (exponencial $e^{Lt}$, catastrófico en sistemas caóticos) y aparece en la cota del [[Error Local Truncamiento vs Error Global Acumulado|error global]] de todo método. Sin ella, EDOs como $y'=\sqrt{|y|}$ pierden la unicidad y la simulación carece de sentido.
