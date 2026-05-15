---
title: Teorema Punto Fijo Banach Contraccion
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-no-lineales
  - punto-fijo
  - banach
draft: false
aliases:
  - Teorema de la contracción de Banach
  - Teorema del punto fijo de Banach
  - Banach fixed point theorem
---

# Teorema del Punto Fijo de Banach (Contracción)

> [!definicion]
> Una función $g: D \subset \mathbb{R} \to \mathbb{R}$ es una **contracción** en un intervalo $I \subset D$ si:
> 1. $g(I) \subset I$ (invarianza del intervalo)
> 2. Existe una constante $L \in [0, 1)$ tal que para todo $x, y \in I$:
>    $$|g(x) - g(y)| \leq L |x - y|$$
>
> La constante $L$ se llama **constante de Lipschitz** o **factor de contracción**.

> [!info]
> Si $g$ es diferenciable, una condición suficiente para que sea contracción en $I$ es:
> $$\max_{x \in I} |g'(x)| \leq L < 1$$

---

## Ejemplo

> [!ejemplo]
> **Verificar si $g(x) = \cos(x)$ es contracción en $[0, 1]$.**
>
> $g$ es diferenciable con $g'(x) = -\sin(x)$. En $[0, 1]$:
> $$|g'(x)| = |\sin(x)| \leq \sin(1) \approx 0.8415 < 1$$
>
> Además, $g([0,1]) = [\cos(1), 1] \approx [0.5403, 1] \subset [0, 1]$.
>
> Por lo tanto, $g$ es contracción con constante $L = \sin(1) \approx 0.8415$.
>
> **Aplicación:** La ecuación $x = \cos(x)$ tiene una única solución en $[0, 1]$ (aproximadamente $0.7391$).

---

## Enunciado del teorema

> [!teorema] [Teorema del Punto Fijo de Banach]
> Sea $g: I \to \mathbb{R}$ una contracción en un intervalo cerrado $I \subset \mathbb{R}$, es decir:
> - $g(I) \subset I$
> - Existe $L \in [0, 1)$ tal que $|g(x) - g(y)| \leq L |x - y|$ para todo $x, y \in I$
>
> Entonces:
> 1. **Existencia:** $g$ tiene un único punto fijo $r \in I$ tal que $r = g(r)$.
> 2. **Convergencia:** Para cualquier $x^{(0)} \in I$, la sucesión definida por $x^{(k+1)} = g(x^{(k)})$ converge a $r$.
> 3. **Cota de error:** Se cumple:
>    $$|x^{(k)} - r| \leq \frac{L^k}{1-L} |x^{(1)} - x^{(0)}| \quad \text{(cota a priori)}$$
>    $$|x^{(k)} - r| \leq \frac{L}{1-L} |x^{(k)} - x^{(k-1)}| \quad \text{(cota a posteriori)}$$

---

## Demostración

> [!demostracion]
> **Paso 1: Unicidad.**
>
> Supóngase que existen dos puntos fijos $r$ y $s$ en $I$, es decir:
> $$r = g(r), \qquad s = g(s)$$
>
> Entonces: $|r-s| = |g(r)-g(s)| \leq L|r-s|$
>
> Como $0 \leq L < 1$, se tiene: $(1-L)|r-s| \leq 0$
>
> Pero $1-L > 0$ y además $|r-s| \geq 0$, por lo tanto necesariamente:
> $$|r-s| = 0$$
>
> En consecuencia:
> $$r=s$$
>
> Por lo tanto, el punto fijo es único.
>
> **Paso 2: La sucesión está bien definida.**
>
> Dado $x^{(0)} \in I$, se define la sucesión iterativa:
> $$x^{(k+1)} = g(x^{(k)})$$
>
> Como $g(I)\subset I$, se tiene:
> $$x^{(1)} = g(x^{(0)}) \in I$$
>
> Supóngase ahora que $x^{(k)} \in I$. Entonces:
> $$x^{(k+1)} = g(x^{(k)}) \in I$$
>
> ya que nuevamente $g(I)\subset I$.
>
> Por inducción:
> $$x^{(k)} \in I \qquad \forall k \geq 0$$
>
> Es decir, todas las iteraciones permanecen dentro del intervalo $I$.
>
> **Paso 3: Acotación de las diferencias sucesivas.**
>
> Por la propiedad de contracción:
> $$|x^{(k+1)} - x^{(k)}|
> = |g(x^{(k)}) - g(x^{(k-1)})|
> \leq L |x^{(k)} - x^{(k-1)}|$$
>
> Aplicando nuevamente la desigualdad:
> $$|x^{(k)} - x^{(k-1)}|
> \leq L |x^{(k-1)} - x^{(k-2)}|$$
>
> y continuando inductivamente:
> $$|x^{(k+1)} - x^{(k)}|
> \leq L^k |x^{(1)} - x^{(0)}|$$
>
> para todo $k \geq 0$.
>
> Esto muestra que las diferencias entre iteraciones consecutivas decrecen geométricamente.
>
> **Paso 4: La sucesión es de Cauchy.**
>
> Sean $m>k$. Por la desigualdad triangular:
> $$|x^{(m)} - x^{(k)}|
> \leq \sum_{j=k}^{m-1} |x^{(j+1)} - x^{(j)}|$$
>
> Usando la estimación anterior:
> $$|x^{(j+1)} - x^{(j)}|
> \leq L^j |x^{(1)} - x^{(0)}|$$
>
> se obtiene:
> $$|x^{(m)} - x^{(k)}|
> \leq \sum_{j=k}^{m-1} L^j |x^{(1)} - x^{(0)}|$$
>
> Factorizando:
> $$|x^{(m)} - x^{(k)}|
> \leq |x^{(1)} - x^{(0)}|
> \sum_{j=k}^{m-1} L^j$$
>
> Como la suma es geométrica:
> $$\sum_{j=k}^{m-1} L^j
> = L^k \frac{1-L^{m-k}}{1-L}$$
>
> entonces:
> $$|x^{(m)} - x^{(k)}|
> \leq
> L^k \frac{1-L^{m-k}}{1-L}
> |x^{(1)} - x^{(0)}|$$
>
> Además, como $0 \leq L < 1$:
> $$1-L^{m-k} \leq 1$$
>
> por lo tanto:
> $$|x^{(m)} - x^{(k)}|
> \leq
> \frac{L^k}{1-L}
> |x^{(1)} - x^{(0)}|$$
>
> Como $L^k \to 0$ cuando $k \to \infty$, se concluye que:
> $$|x^{(m)} - x^{(k)}| \to 0$$
>
> para todo $m>k$.
>
> Por definición, la sucesión $\{x^{(k)}\}$ es de Cauchy.
>
> Como $\mathbb{R}$ es completo, existe un número $r \in \mathbb{R}$ tal que:
> $$x^{(k)} \to r$$
>
> Además, como todas las iteraciones pertenecen a $I$ y el intervalo $I$ es cerrado, se tiene:
> $$r \in I$$
>
> **Paso 5: El límite es punto fijo.**
>
> Como $g$ es contracción, es continua. Entonces:
> $$x^{(k+1)} = g(x^{(k)})$$
>
> Tomando límite cuando $k \to \infty$:
> $$\lim_{k\to\infty} x^{(k+1)}
> =
> \lim_{k\to\infty} g(x^{(k)})$$
>
> Como $x^{(k)} \to r$, por continuidad de $g$:
> $$r = g(r)$$
>
> Por lo tanto, el límite de la sucesión es un punto fijo de $g$.
>
> Como en el Paso 1 se probó que el punto fijo es único, toda sucesión generada por la iteración converge necesariamente al mismo punto fijo $r$.
>
> **Paso 6: Cotas de error.**
>
> Haciendo $m \to \infty$ en:
> $$|x^{(m)} - x^{(k)}|
> \leq
> \frac{L^k}{1-L}
> |x^{(1)} - x^{(0)}|$$
>
> y usando que $x^{(m)} \to r$, se obtiene:
> $$|r - x^{(k)}|
> \leq
> \frac{L^k}{1-L}
> |x^{(1)} - x^{(0)}|
> \qquad \text{(cota a priori)}$$
>
> Para la cota a posteriori, se usa que:
> $$|x^{(k+1)} - x^{(k)}|
> \leq
> L |x^{(k)} - x^{(k-1)}|$$
>
> y se aplica un razonamiento análogo usando la serie geométrica asociada a las diferencias sucesivas.
---

## Cota de error

> [!corolario]
> Para el método de punto fijo $x^{(k+1)} = g(x^{(k)})$ con $g$ contracción de constante $L$, se cumple:
>
> **Cota a priori** (se calcula antes de iterar):
> $$|x^{(k)} - r| \leq \frac{L^k}{1-L} |x^{(1)} - x^{(0)}|$$
>
> **Cota a posteriori** (se calcula durante la iteración):
> $$|x^{(k)} - r| \leq \frac{L}{1-L} |x^{(k)} - x^{(k-1)}|$$
>
> **Cota geométrica:**
> $$|x^{(k)} - r| \leq L |x^{(k-1)} - r|$$

> [!ejemplo]
> Para $g(x) = \cos(x)$ en $[0, 1]$, $L = \sen(1) \approx 0.8415$. Si $x^{(0)} = 0$:
> - $x^{(1)} = \cos(0) = 1$
> - $|x^{(1)} - x^{(0)}| = 1$
> - Error a priori en $k=10$: $|x^{(10)} - r| \leq \frac{0.8415^{10}}{1-0.8415} \cdot 1 \approx \frac{0.173}{0.1585} \approx 1.09$ (muy gruesa)
>
> La cota a posteriori suele ser más ajustada.

---

## Condiciones suficientes de convergencia

> [!info]
> **Verificación práctica de contracción.**
>
> Para funciones diferenciables, una condición suficiente para que $g$ sea contracción en $I$ es:
> $$\max_{x \in I} |g'(x)| \leq L < 1$$
>
> **Convergencia local vs global:**
>
> - **Global:** Las condiciones $g(I) \subset I$ y $|g'(x)| \leq L < 1$ para todo $x \in I$ garantizan convergencia desde cualquier punto de $I$.
>
> - **Local:** Si solo se cumple $|g'(r)| < 1$ en el punto fijo $r$, entonces existe una vecindad $V$ de $r$ tal que la iteración converge para $x^{(0)} \in V$ (convergencia local).

> [!warning]
> El teorema de Banach proporciona condiciones **suficientes**, no necesarias. Puede haber convergencia incluso si $g$ no es contracción global, siempre que $|g'(r)| < 1$.

---

## Relación con el método de punto fijo

> [!info]
> El teorema de Banach es la base teórica del método de [[Metodos Numericos/3 Ecuaciones No Lineales/Metodos Abiertos Una Variable/Punto Fijo Aproximaciones Sucesivas/index]]. Garantiza:
>
> - **Existencia:** La ecuación $x = g(x)$ tiene solución única en $I$.
> - **Convergencia:** La iteración $x^{(k+1)} = g(x^{(k)})$ converge desde cualquier punto inicial en $I$.
> - **Estimación de error:** Las cotas a priori y a posteriori permiten determinar cuántas iteraciones se necesitan.
>
> **Aplicación a $f(x)=0$:**
>
> Para resolver $f(x)=0$, se construye $g(x) = x - f(x)$ o $g(x) = x + c f(x)$ con $c \neq 0$. La condición $|g'(r)| < 1$ equivale a $|1 + c f'(r)| < 1$, lo que guía la elección de $c$.

---

## Resumen

| Aspecto                  | Descripción                                                    |
| :----------------------- | :------------------------------------------------------------- |
| **Hipótesis**            | $g(I) \subset I$ y $\| g(x)-g(y) \| \leq L \| x-y\|$ con $L<1$ |
| **Existencia**           | Un único punto fijo $r \in I$                                  |
| **Convergencia**         | Global (desde cualquier $x^{(0)} \in I$)                       |
| **Orden**                | Lineal ($p=1$)                                                 |
| **Constante asintótica** | $L$ (o $\| g'(r)\|$ si es diferenciable)                       |
| **Cota a priori**        | $\| x^{(k)}-r \| \leq \frac{L^k}{1-L} \| x^{(1)}-x^{(0)}\|$    |
|                          | $\| x^{(k)}-r\| \leq \frac{L}{1-L}\| x^{(k)}-x^{(k-1)} \|$     |

> [!corolario]
> El teorema del punto fijo de Banach es el resultado fundamental que garantiza la convergencia del método de aproximaciones sucesivas. Proporciona condiciones suficientes claras (invarianza del intervalo y contracción) y cotas de error explícitas. Para el método de [[Metodos Numericos/3 Ecuaciones No Lineales/Metodos Abiertos Una Variable/Punto Fijo Aproximaciones Sucesivas/index]], este teorema justifica por qué la iteración $x^{(k+1)} = g(x^{(k)})$ converge y cómo estimar el error. Las condiciones de contracción se relajan en la práctica al análisis de convergencia local basado en $|g'(r)| < 1$, tema desarrollado en [[Funcion Iteracion g x y Convergencia Local]].