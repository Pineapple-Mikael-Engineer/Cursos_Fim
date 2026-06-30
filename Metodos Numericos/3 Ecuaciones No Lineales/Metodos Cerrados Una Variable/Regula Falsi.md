---
title: Regula Falsi
order: 2
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-no-lineales
  - metodos-cerrados
  - regula-falsi
draft: false
aliases:
  - Regula Falsi
  - Método de la falsa posición
  - False position method
---

# Método de Regula Falsi (Falsa Posición)

> [!definicion]
> El **método de Regula Falsi** (o método de la falsa posición) es un método cerrado para encontrar raíces de $f(x)=0$ que, partiendo de un intervalo $[a, b]$ con $f(a)f(b) < 0$, utiliza interpolación lineal entre $(a, f(a))$ y $(b, f(b))$ para aproximar la raíz, en lugar del punto medio de la bisección.

> [!info]
> Es una mejora del [[Biseccion]] que busca acelerar la convergencia usando información de la pendiente de $f$. Su convergencia sigue siendo lineal, pero con un factor de convergencia potencialmente menor que el de bisección.

---

## Ejemplo

> [!ejemplo]
> **Encontrar la raíz de $f(x) = x^2 - 2$ en $[1, 2]$ (solución $x = \sqrt{2} \approx 1.414213562$).**
>
> | $k$ | $a_k$ | $b_k$ | $c_k$ | $f(c_k)$ | Nuevo intervalo |
> |:---|:---|:---|:---|:---|:---|
> | 0 | 1.0000 | 2.0000 | 1.3333 | -0.2222 | $[1.3333, 2.0000]$ |
> | 1 | 1.3333 | 2.0000 | 1.4000 | -0.0400 | $[1.4000, 2.0000]$ |
> | 2 | 1.4000 | 2.0000 | 1.4118 | -0.0069 | $[1.4118, 2.0000]$ |
> | 3 | 1.4118 | 2.0000 | 1.4138 | -0.0012 | $[1.4138, 2.0000]$ |
> | 4 | 1.4138 | 2.0000 | 1.4142 | -0.0002 | $[1.4142, 2.0000]$ |
> | 5 | 1.4142 | 2.0000 | 1.4142 | -0.0000 | — |
>
> **Comparación con bisección:**
>
> | Iteración | Bisección ($c_k$) | Regula Falsi ($c_k$) |
> |:---|:---|:---|
> | 1 | 1.5000 | 1.3333 |
> | 2 | 1.2500 | 1.4000 |
> | 3 | 1.3750 | 1.4118 |
> | 4 | 1.4375 | 1.4138 |
> | 5 | 1.4063 | 1.4142 |
>
> Regula Falsi converge más rápido en este ejemplo (5 iteraciones vs 10+ de bisección).

---

## En qué consiste el método

> [!teoria]
> **Algoritmo de Regula Falsi.**
>
> Dado $f$ continua en $[a, b]$ con $f(a)f(b) < 0$:
>
> 1. Calcular $c$ por interpolación lineal entre $(a, f(a))$ y $(b, f(b))$:
>    $$c = b - f(b) \cdot \frac{b - a}{f(b) - f(a)} = \frac{a f(b) - b f(a)}{f(b) - f(a)}$$
>
> 2. Si $|f(c)| < \text{tol}$ o $|b-a| < \text{tol}$, parar: $c$ es la raíz
>
> 3. Si $f(a)f(c) < 0$, entonces la raíz está en $[a, c]$; actualizar $b = c$
>
> 4. Si $f(c)f(b) < 0$, entonces la raíz está en $[c, b]$; actualizar $a = c$
>
> 5. Repetir desde el paso 1
>
> **Interpretación geométrica:**
>
> En lugar de usar el punto medio (bisección), se traza la recta secante entre $(a, f(a))$ y $(b, f(b))$. La intersección de esta recta con el eje $x$ es la aproximación $c$. Como $f(a)$ y $f(b)$ tienen signos opuestos, $c$ siempre está dentro del intervalo.

---

## Deducción de la fórmula

> [!demostracion]
> La recta que pasa por $(a, f(a))$ y $(b, f(b))$ tiene ecuación:
> $$y = f(a) + \frac{f(b) - f(a)}{b - a}(x - a)$$
>
> Para encontrar la intersección con el eje $x$ ($y = 0$):
> $$0 = f(a) + \frac{f(b) - f(a)}{b - a}(c - a)$$
>
> Despejando $c$:
> $$-\frac{f(a)(b - a)}{f(b) - f(a)} = c - a$$
> $$c = a - \frac{f(a)(b - a)}{f(b) - f(a)} = \frac{a f(b) - b f(a)}{f(b) - f(a)}$$
>
> Forma alternativa (más estable numéricamente cuando $f(b)$ es pequeño):
> $$c = b - f(b) \cdot \frac{b - a}{f(b) - f(a)}$$

---

## Teorema de convergencia

> [!teorema]
> Sea $f$ continua en $[a, b]$ con $f(a)f(b) < 0$ y $f$ estrictamente monótona en $[a, b]$. El método de Regula Falsi genera una sucesión $\{c_k\}$ que converge a la única raíz $r \in (a, b)$. La convergencia es lineal, pero el factor de convergencia puede ser muy cercano a $1$ (convergencia lenta) en casos de estancamiento.

> [!demostracion]
> **Paso 1: Existencia y unicidad.**
>
> Por el [[Teorema de Bolzano y Metodo Grafico]], existe al menos una raíz. La monotonía garantiza unicidad.
>
> **Paso 2: La raíz está siempre en el intervalo.**
>
> Por construcción, en cada iteración se actualiza $a$ o $b$ manteniendo $f(a)f(b) < 0$, por lo tanto $r \in [a, b]$ siempre.
>
> **Paso 3: Convergencia.**
>
> La longitud del intervalo no necesariamente tiende a cero (puede ocurrir estancamiento), pero el punto $c_k$ converge a $r$ porque la interpolación lineal mejora en cada iteración. Para funciones cóncavas o convexas, un extremo puede no actualizarse, lo que causa convergencia unilateral.

---

## Estancamiento unilateral (el problema principal)

> [!warning]
> **El problema del estancamiento.**
>
> Cuando $f$ es convexa o cóncava en $[a, b]$, uno de los extremos del intervalo puede permanecer fijo para siempre. Por ejemplo, en $f(x) = x^2 - 2$ en $[1, 2]$:
> - $a = 1$ (con $f(1) = -1$) nunca se actualiza
> - Solo $b$ se mueve hacia la raíz
> - El intervalo no se reduce (sigue siendo $[1, 2]$) aunque $c_k \to r$
>
> **Consecuencia:** La convergencia se vuelve lineal con factor cercano a $1$, perdiendo la ventaja sobre bisección.

> [!ejemplo]
> **Estancamiento en $f(x) = x^2 - 2$.**
>
> | $k$ | $a$ (fijo) | $b$ | $c$ | $f(c)$ |
> |:---|:---|:---|:---|:---|
> | 0 | 1.0000 | 2.0000 | 1.3333 | -0.2222 |
> | 1 | 1.0000 | 1.3333 | 1.4000 | -0.0400 |
> | 2 | 1.0000 | 1.4000 | 1.4118 | -0.0069 |
> | 3 | 1.0000 | 1.4118 | 1.4138 | -0.0012 |
>
> El extremo $a = 1$ nunca cambia. El intervalo no se reduce, pero $c$ se acerca a la raíz.

---

## Modificaciones para evitar estancamiento (Illinois, Pegasus)

> [!info]
> **Variantes del método de Regula Falsi.**
>
> Para evitar el estancamiento, se han propuesto modificaciones que ajustan el peso de uno de los extremos cuando se detecta que permanece fijo.
>
> **Método Illinois:**
> - Si el mismo extremo se ha mantenido durante dos iteraciones consecutivas, se reduce a la mitad el valor de $f$ en ese extremo para la siguiente interpolación.
>
> **Método Pegasus:**
> - Similar a Illinois, pero con un factor de ajuste más sofisticado que preserva ciertas propiedades de convergencia.
>
> Estas modificaciones logran convergencia superlineal ($p \approx 1.6$) en muchos casos, comparable al [[Metodo Secante Orden Convergencia Fi]].

---

## Algoritmo

> [!algoritmo]
> **Pseudocódigo de Regula Falsi (versión básica).**
>
> ```
> función regula_falsi(f, a, b, tol, max_iter)
>     si f(a) * f(b) >= 0
>         error("No hay cambio de signo en [a, b]")
>     
>     para k = 1 hasta max_iter
>         c = (a * f(b) - b * f(a)) / (f(b) - f(a))
>         
>         si |f(c)| < tol o |b - a| < tol
>             retornar c, k
>         
>         si f(a) * f(c) < 0
>             b = c
>         sino
>             a = c
>     
>     retornar c, max_iter
> ```

> [!algoritmo]
> **Implementación en Python (versión básica).**
>
> ```python
> def regula_falsi(f, a, b, tol=1e-10, max_iter=100):
>     """
>     Método de Regula Falsi (falsa posición) para encontrar una raíz de f(x)=0 en [a, b].
>     
>     Parámetros:
>     - f: función continua
>     - a, b: extremos del intervalo (f(a)*f(b) < 0)
>     - tol: tolerancia
>     - max_iter: iteraciones máximas
>     
>     Retorna:
>     - c: aproximación a la raíz
>     - iter: número de iteraciones
>     """
>     if f(a) * f(b) >= 0:
>         raise ValueError("f(a) y f(b) deben tener signos opuestos")
>     
>     fa = f(a)
>     fb = f(b)
>     
>     for k in range(max_iter):
>         c = (a * fb - b * fa) / (fb - fa)
>         fc = f(c)
>         
>         if abs(fc) < tol or abs(b - a) < tol:
>             return c, k + 1
>         
>         if fa * fc < 0:
>             b = c
>             fb = fc
>         else:
>             a = c
>             fa = fc
>     
>     return c, max_iter
> 
> # Ejemplo
> f = lambda x: x**2 - 2
> raiz, iters = regula_falsi(f, 1, 2, tol=1e-10)
> print(f"Raíz: {raiz}")
> print(f"Iteraciones: {iters}")
> ```

> [!algoritmo]
> **Implementación en Python (método Illinois, anti-estancamiento).**
>
> ```python
> def regula_falsi_illinois(f, a, b, tol=1e-10, max_iter=100):
>     """
>     Método de Regula Falsi con modificación Illinois.
>     """
>     if f(a) * f(b) >= 0:
>         raise ValueError("f(a) y f(b) deben tener signos opuestos")
>     
>     fa = f(a)
>     fb = f(b)
>     lado = 0  # 0: ningún extremo fijo, 1: izquierdo fijo, 2: derecho fijo
>     
>     for k in range(max_iter):
>         c = (a * fb - b * fa) / (fb - fa)
>         fc = f(c)
>         
>         if abs(fc) < tol or abs(b - a) < tol:
>             return c, k + 1
>         
>         if fa * fc < 0:
>             # La raíz está en [a, c]
>             if lado == 1:
>                 fa = fa / 2  # Reducir peso del extremo fijo
>             b = c
>             fb = fc
>             lado = 1
>         else:
>             # La raíz está en [c, b]
>             if lado == 2:
>                 fb = fb / 2
>             a = c
>             fa = fc
>             lado = 2
>     
>     return c, max_iter
> ```

---

## Ventajas y desventajas

> [!info]
> **Ventajas de Regula Falsi.**
>
> - **Más rápido que bisección:** En funciones convexas o cóncavas, la convergencia es más rápida.
> - **No requiere derivadas:** A diferencia de [[Newton Raphson/index]].
> - **Garantía de convergencia:** Al igual que bisección, mantiene el encierro de la raíz.
> - **Fácil de implementar:** Solo requiere evaluaciones de $f$.
>
> **Desventajas.**
>
> - **Estancamiento unilateral:** Un extremo puede quedar fijo, reduciendo la velocidad de convergencia.
> - **Convergencia lineal:** Sigue siendo lineal, no cuadrática como Newton.
> - **Requiere intervalo inicial:** Debe conocerse $[a, b]$ con $f(a)f(b) < 0$.
> - **No se extiende a varias variables:** Como todos los métodos cerrados.

---

## Comparación con otros métodos

| Método | Orden | Ventaja | Desventaja |
|:---|:---|:---|:---|
| [[Biseccion]] | $p=1$, factor $1/2$ | Robusto, error predecible | Lento |
| **Regula Falsi** | $p=1$, factor variable | Más rápido que bisección | Estancamiento |
| Regula Falsi (Illinois) | $p \approx 1.6$ | Superlineal | Más complejo |
| [[Newton Raphson/index]] | $p=2$ | Muy rápido | Requiere derivada, puede diverger |
| [[Metodo Secante Orden Convergencia Fi]] | $p \approx 1.618$ | Sin derivada, rápido | Puede diverger |

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| **Tipo** | Método cerrado (requiere intervalo con cambio de signo) |
| **Aproximación** | Interpolación lineal entre $(a, f(a))$ y $(b, f(b))$ |
| **Convergencia** | Garantizada para $f$ continua |
| **Orden de convergencia** | Lineal ($p=1$) |
| **Factor de convergencia** | Variable (puede ser cercano a $1$ en estancamiento) |
| **Principal problema** | Estancamiento unilateral |
| **Soluciones** | Modificaciones Illinois, Pegasus |
| **Ventaja** | Más rápido que bisección en funciones convexas/cóncavas |
| **Desventaja** | Puede ser muy lento por estancamiento |

> [!corolario]
> Regula Falsi mejora la bisección usando interpolación lineal, lo que acelera la convergencia en muchos casos. Sin embargo, el estancamiento unilateral puede degradar su rendimiento. Las modificaciones (Illinois, Pegasus) corrigen este problema y logran convergencia superlineal. Para máxima velocidad (y si se dispone de derivada), se prefiere [[Newton Raphson/index]]. Para robustez garantizada, [[Biseccion]] sigue siendo la opción más segura.