---
title: Biseccion
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-no-lineales
  - metodos-cerrados
  - biseccion
draft: false
aliases:
  - Bisection method
  - Método de bisección
  - Binary search method
---

# Método de Bisección

> [!definicion]
> El **método de bisección** es un método cerrado para encontrar raíces de $f(x)=0$ que, partiendo de un intervalo $[a, b]$ con $f(a)f(b) < 0$, divide repetidamente el intervalo por la mitad y selecciona el subintervalo que contiene la raíz.

> [!info]
> Es el método más simple y robusto. Su convergencia está garantizada bajo la única condición de que $f$ sea continua en $[a, b]$ y $f(a)f(b) < 0$, condiciones dadas por el [[Teorema de Bolzano y Metodo Grafico]].

---

## Ejemplo

> [!ejemplo]
> **Encontrar la raíz de $f(x) = x^2 - 2$ en $[1, 2]$ (solución $x = \sqrt{2} \approx 1.414213562$).**
>
> | $k$ | $a_k$ | $b_k$ | $c_k = (a_k+b_k)/2$ | $f(c_k)$ | Nuevo intervalo |
> |:---|:---|:---|:---|:---|:---|
> | 0 | 1.0000 | 2.0000 | 1.5000 | 0.2500 | $[1.0000, 1.5000]$ |
> | 1 | 1.0000 | 1.5000 | 1.2500 | -0.4375 | $[1.2500, 1.5000]$ |
> | 2 | 1.2500 | 1.5000 | 1.3750 | -0.1094 | $[1.3750, 1.5000]$ |
> | 3 | 1.3750 | 1.5000 | 1.4375 | 0.0664 | $[1.3750, 1.4375]$ |
> | 4 | 1.3750 | 1.4375 | 1.4063 | -0.0225 | $[1.4063, 1.4375]$ |
> | 5 | 1.4063 | 1.4375 | 1.4219 | 0.0217 | $[1.4063, 1.4219]$ |
> | 6 | 1.4063 | 1.4219 | 1.4141 | -0.0004 | $[1.4141, 1.4219]$ |
> | 7 | 1.4141 | 1.4219 | 1.4180 | 0.0106 | $[1.4141, 1.4180]$ |
> | 8 | 1.4141 | 1.4180 | 1.4160 | 0.0051 | $[1.4141, 1.4160]$ |
> | 9 | 1.4141 | 1.4160 | 1.4150 | 0.0023 | $[1.4141, 1.4150]$ |
> | 10 | 1.4141 | 1.4150 | 1.4145 | 0.0010 | $[1.4141, 1.4145]$ |
>
> Después de 10 iteraciones, $c_{10} \approx 1.4145$, con error $< (2-1)/2^{10} = 1/1024 \approx 0.001$.

---

## En qué consiste el método

> [!teoria]
> **Algoritmo de bisección.**
>
> Dado $f$ continua en $[a, b]$ con $f(a)f(b) < 0$:
>
> 1. Calcular $c = \frac{a + b}{2}$
> 2. Si $f(c) = 0$ (o $|f(c)| < \text{tol}$), parar: $c$ es la raíz
> 3. Si $f(a)f(c) < 0$, entonces la raíz está en $[a, c]$; actualizar $b = c$
> 4. Si $f(c)f(b) < 0$, entonces la raíz está en $[c, b]$; actualizar $a = c$
> 5. Repetir desde el paso 1
>
> **Interpretación geométrica:**
>
> En cada iteración, se evalúa $f$ en el punto medio $c$. El signo de $f(c)$ determina en qué mitad del intervalo se encuentra la raíz. El intervalo se reduce a la mitad, manteniendo siempre la propiedad $f(a)f(b) < 0$.

---

## Teorema de convergencia y cota de error

> [!teorema]
> Sea $f$ continua en $[a, b]$ con $f(a)f(b) < 0$. El método de bisección genera una sucesión de intervalos $[a_k, b_k]$ y puntos medios $c_k$ tales que:
>
> 1. $c_k \to r$, donde $r$ es una raíz de $f$
> 2. El error en la iteración $k$ satisface:
>    $$|c_k - r| \leq \frac{b - a}{2^k}$$

> [!demostracion]
> **Paso 1: Longitud del intervalo.**
>
> En la iteración $0$, la longitud del intervalo es $L_0 = b - a$.
>
> Cada iteración divide el intervalo por la mitad. Después de $k$ iteraciones, la longitud es:
> $$L_k = \frac{b - a}{2^k}$$
>
> **Paso 2: La raíz está dentro del intervalo.**
>
> Por construcción, en cada iteración la raíz $r$ satisface $a_k \leq r \leq b_k$ (o $b_k \leq r \leq a_k$, dependiendo del orden). Por lo tanto:
> $$|c_k - r| \leq \frac{b_k - a_k}{2} = \frac{L_k}{2} = \frac{b - a}{2^{k+1}}$$
>
> **Paso 3: Convergencia.**
>
> Como $\frac{b - a}{2^{k+1}} \to 0$ cuando $k \to \infty$, se tiene $c_k \to r$.
>
> **Paso 4: Cota de error.**
>
> El punto medio $c_k$ puede estar como máximo a mitad del intervalo de la raíz. Por lo tanto:
> $$|c_k - r| \leq \frac{b_k - a_k}{2} = \frac{b - a}{2^{k+1}} \leq \frac{b - a}{2^k}$$
>
> (La última desigualdad es válida para $k \geq 0$).

> [!corolario]
> Para garantizar un error absoluto $\varepsilon$, es decir, $|c_k - r| \leq \varepsilon$, se necesita:
> $$k \geq \log_2\left(\frac{b - a}{\varepsilon}\right)$$

---

## Orden de convergencia lineal

> [!info]
> El método de bisección tiene **convergencia lineal** ($p = 1$) con factor de convergencia $1/2$:
> $$\lim_{k \to \infty} \frac{|c_{k+1} - r|}{|c_k - r|} = \frac{1}{2}$$
>
> Esto significa que cada iteración reduce el error aproximadamente a la mitad (gana 1 bit de precisión por iteración).
>
> **Comparación con otros métodos:**
> - Bisección: $p = 1$, factor $1/2$
> - [[Regula Falsi]]: $p = 1$, factor variable (puede ser cercano a $1$)
> - [[Newton Raphson/index]]: $p = 2$ (cuadrático)
> - [[Metodo Secante Orden Convergencia Fi]]: $p \approx 1.618$ (superlineal)

---

## Ventaja: robustez vs lentitud

> [!info]
> **Ventajas del método de bisección.**
>
> - **Robustez:** Converge bajo condiciones muy débiles (solo continuidad y cambio de signo)
> - **Error predecible:** La cota de error es conocida a priori: $|c_k - r| \leq (b-a)/2^k$
> - **No requiere derivadas:** A diferencia de [[Newton Raphson/index]]
> - **Siempre converge:** No hay riesgo de divergencia como en los métodos abiertos
>
> **Desventajas.**
>
> - **Lentitud:** Convergencia lineal con factor $1/2$ (solo 1 bit de precisión por iteración)
> - **Requiere intervalo inicial:** Debe conocerse un $[a, b]$ con $f(a)f(b) < 0$
> - **No se extiende a varias variables:** No existe un análogo directo para [[Sistemas Ecuaciones No Lineales/index]]

---

## Algoritmo

> [!algoritmo]
> **Pseudocódigo del método de bisección.**
>
> ```
> función biseccion(f, a, b, tol, max_iter)
>     si f(a) * f(b) >= 0
>         error("No hay cambio de signo en [a, b]")
>     
>     para k = 1 hasta max_iter
>         c = (a + b) / 2
>         
>         si |f(c)| < tol o (b - a)/2 < tol
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
> **Implementación en Python.**
>
> ```python
> def biseccion(f, a, b, tol=1e-10, max_iter=100):
>     """
>     Método de bisección para encontrar una raíz de f(x)=0 en [a, b].
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
>     for k in range(max_iter):
>         c = (a + b) / 2
>         fc = f(c)
>         
>         if abs(fc) < tol or (b - a) / 2 < tol:
>             return c, k + 1
>         
>         if f(a) * fc < 0:
>             b = c
>         else:
>             a = c
>     
>     return c, max_iter
> 
> # Ejemplo
> f = lambda x: x**2 - 2
> raiz, iters = biseccion(f, 1, 2, tol=1e-10)
> print(f"Raíz: {raiz}")
> print(f"Iteraciones: {iters}")
> ```

---

## Limitaciones

> [!warning]
> **Limitaciones del método de bisección.**
>
> 1. **Requiere cambio de signo:** No funciona si $f(a)f(b) > 0$ (aunque pueda haber raíces)
> 2. **Raíces múltiples:** Si la raíz es de multiplicidad par, $f$ no cambia de signo y el método falla (ej: $f(x) = (x-1)^2$ en $[0, 2]$)
> 3. **Funciones discontinuas:** El teorema de Bolzano no se aplica; el método puede fallar
> 4. **Lentitud:** Para alta precisión, se requieren muchas iteraciones (ej: 50 iteraciones para $10^{-15}$)

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| **Tipo** | Método cerrado (requiere intervalo con cambio de signo) |
| **Convergencia** | Garantizada para $f$ continua |
| **Orden de convergencia** | Lineal ($p=1$) |
| **Factor de convergencia** | $1/2$ (un bit por iteración) |
| **Cota de error** | $|c_k - r| \leq (b-a)/2^k$ |
| **Iteraciones para $\varepsilon$** | $k \geq \log_2((b-a)/\varepsilon)$ |
| **Ventaja** | Robusto, simple, error predecible |
| **Desventaja** | Lento, requiere intervalo inicial |

> [!corolario]
> El método de bisección es la base de los métodos cerrados. Su convergencia lenta pero garantizada lo hace ideal como método de respaldo o para obtener una aproximación inicial gruesa. La cota de error $|c_k - r| \leq (b-a)/2^k$ permite predecir exactamente cuántas iteraciones se necesitan para alcanzar una tolerancia dada. Para acelerar la convergencia, se puede combinar con [[Regula Falsi]] o con métodos abiertos como [[Newton Raphson/index]].