---
title: Orden Convergencia Cuadratica Simple
order: 2
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-no-lineales
  - newton-raphson
  - convergencia
draft: false
aliases:
  - Convergencia cuadrática
  - Orden de convergencia 2
  - Quadratic convergence
---

# Orden de Convergencia Cuadrática en Raíces Simples

> [!definicion]
> Sea $\{x^{(k)}\}$ una sucesión que converge a $r$. Se dice que la convergencia es **cuadrática** si existe una constante $C > 0$ tal que:
> $$\lim_{k \to \infty} \frac{\|x^{(k+1)} - r\|}{\|x^{(k)} - r\|^2} = C$$
>
> En particular, para el método de [[Derivacion Geometrica y Serie Taylor|Newton]] con raíces simples ($f'(r) \neq 0$), se cumple:
> $$C = \frac{\|f''(r)\|}{2\|f'(r)\|}$$

> [!info]
> El método de Newton es el ejemplo más conocido de convergencia cuadrática. Esto significa que, asintóticamente, el número de dígitos correctos se **duplica** en cada iteración.

---

## Ejemplo: duplicación de dígitos

> [!ejemplo]
> **Newton aplicado a $f(x) = x^2 - 2$, raíz $r = \sqrt{2} \approx 1.414213562373095$.** $C = \frac{\|2\|}{2\|2\sqrt{2}\|} = \frac{2}{4\sqrt{2}} \approx 0.3536$.
>
> | $k$ | $x^{(k)}$ | Error $e^{(k)}$ | $e^{(k+1)}/(e^{(k)})^2$ | Dígitos correctos |
> |:---|:---|:---|:---|:---|
> | 0 | 2.0 | 5.857864e-01 | — | 0 |
> | 1 | 1.5 | 8.578644e-02 | 0.2500 | 1 |
> | 2 | 1.416666667 | 2.453105e-03 | 0.3333 | 3 |
> | 3 | 1.414215686 | 2.123902e-06 | 0.3536 | 6 |
> | 4 | 1.414213562 | 1.594724e-12 | 0.3536 | 12 |
>
> **Observación:** Los dígitos correctos se duplican aproximadamente en cada iteración (0 → 1 → 3 → 6 → 12). El cociente $e^{(k+1)}/(e^{(k)})^2$ converge a $C \approx 0.3536$.

---

## Comparativa: lineal vs cuadrática

> [!info]
> **Diferencia clave entre convergencia lineal y cuadrática.**
>
> | Tipo | Relación | Dígitos por iteración | Ejemplo |
> |:---|:---|:---|:---|
> | Lineal | $e^{(k+1)} \approx c e^{(k)}$, $c < 1$ | Constante ($-\log_{10} c$) | [[Biseccion]], [[Punto Fijo Aproximaciones Sucesivas/index\|punto fijo]] |
> | Cuadrática | $e^{(k+1)} \approx C (e^{(k)})^2$ | Se duplica | Newton (raíz simple) |
>
> **Ejemplo numérico con $e^{(0)} = 0.1$:**
>
> | Iteración | Lineal ($c=0.5$) | Cuadrática ($C=1$) |
> |:---|:---|:---|
> | 0 | 1.00e-1 | 1.00e-1 |
> | 1 | 5.00e-2 | 1.00e-2 |
> | 2 | 2.50e-2 | 1.00e-4 |
> | 3 | 1.25e-2 | 1.00e-8 |
> | 4 | 6.25e-3 | 1.00e-16 |
>
> La convergencia cuadrática alcanza precisión de máquina en 4 iteraciones, mientras que la lineal requiere muchas más.

---

## Demostración alternativa del orden cuadrático

> [!teorema]
> Sea $g(x) = x - f(x)/f'(x)$. Para raíces simples ($f'(r) \neq 0$), se cumple $g'(r) = 0$ y $g''(r) = \frac{f''(r)}{f'(r)}$. Por lo tanto, la expansión de Taylor de $g$ alrededor de $r$ es:
> $$g(x) = r + \frac{g''(r)}{2}(x - r)^2 + O((x - r)^3)$$

> [!demostracion]
> **Paso 1: Derivadas de $g$.**
>
> $$g(x) = x - \frac{f(x)}{f'(x)}$$
>
> Derivando:
> $$g'(x) = 1 - \frac{(f'(x))^2 - f(x)f''(x)}{(f'(x))^2} = \frac{f(x)f''(x)}{(f'(x))^2}$$
>
> En la raíz $r$, $f(r)=0$, por lo tanto $g'(r) = 0$.
>
> **Paso 2: Segunda derivada.**
>
> Derivando nuevamente y evaluando en $r$ (omitimos los cálculos algebraicos):
> $$g''(r) = \frac{f''(r)}{f'(r)}$$
>
> **Paso 3: Expansión de Taylor.**
>
> Desarrollando $g$ alrededor de $r$:
> $$g(x) = g(r) + g'(r)(x - r) + \frac{g''(r)}{2}(x - r)^2 + O((x - r)^3)$$
>
> Como $g(r) = r$ y $g'(r) = 0$:
> $$g(x) = r + \frac{g''(r)}{2}(x - r)^2 + O((x - r)^3)$$
>
> **Paso 4: Relación con el error.**
>
> Sustituyendo $x = x^{(k)}$ y recordando que $x^{(k+1)} = g(x^{(k)})$:
> $$x^{(k+1)} - r = \frac{g''(r)}{2} (x^{(k)} - r)^2 + O((x^{(k)} - r)^3)$$
>
> Por lo tanto:
> $$\lim_{k \to \infty} \frac{x^{(k+1)} - r}{(x^{(k)} - r)^2} = \frac{g''(r)}{2} = \frac{f''(r)}{2f'(r)}$$

Esta demostración complementa a la presentada en [[Derivacion Geometrica y Serie Taylor]].

---

## Relación con la constante asintótica

> [!definicion]
> La **constante asintótica de convergencia cuadrática** es:
> $$C = \frac{\|f''(r)\|}{2\|f'(r)\|}$$
>
> Cuanto menor sea $C$, más rápida es la convergencia. Si $C$ es muy grande, la convergencia cuadrática puede tardar algunas iteraciones en manifestarse.

> [!ejemplo]
> **Comparación de $C$ para diferentes funciones.**
>
> | Función | Raíz $r$ | $f'(r)$ | $f''(r)$ | $C = \|f''(r)\|/(2\|f'(r)\|)$ |
> |:---|:---|:---|:---|:---|
> | $x^2 - 2$ | $\sqrt{2}$ | $2\sqrt{2} \approx 2.828$ | $2$ | $0.3536$ |
> | $x^3 - 2$ | $\sqrt[3]{2} \approx 1.260$ | $3r^2 \approx 4.762$ | $6r \approx 7.560$ | $0.794$ |
> | $e^x - 2$ | $\ln 2 \approx 0.693$ | $e^r = 2$ | $e^r = 2$ | $0.5$ |
> | $\cos x - x$ | $\approx 0.739$ | $-\sen(r)-1 \approx -1.673$ | $-\cos(r) \approx -0.739$ | $0.221$ |
>
> La constante $C$ varía; valores pequeños indican convergencia más rápida.

---

## Condiciones para garantizar convergencia cuadrática

> [!teorema]
> El método de Newton tiene convergencia cuadrática si se cumplen:
> 1. $f \in C^2$ en una vecindad de $r$
> 2. $f(r) = 0$ (raíz)
> 3. $f'(r) \neq 0$ (raíz simple)
> 4. $x^{(0)}$ está suficientemente cerca de $r$

> [!warning]
> Si alguna de estas condiciones falla:
> - **Raíz múltiple ($f'(r)=0$):** La convergencia se reduce a lineal (constante $c = 1 - 1/m$, donde $m$ es la multiplicidad). Véase [[Convergencia Lineal Raices Multiples]].
> - **$f \notin C^2$:** El orden puede ser menor
> - **$x^{(0)}$ lejos de $r$:** El método puede diverger o converger lentamente al principio. Véase [[Criterios Fallo Divergencia Oscilacion]].

---

## Interpretación práctica: duplicación de dígitos

> [!info]
> **Regla práctica:** En convergencia cuadrática, el número de dígitos decimales correctos se duplica aproximadamente en cada iteración (una vez que se está suficientemente cerca de la raíz).
>
> **Verificación:** Si $\|e^{(k)}\| \approx 10^{-d}$, entonces:
> $$\|e^{(k+1)}\| \approx C \|e^{(k)}\|^2 \approx C \cdot 10^{-2d} \approx 10^{-2d + \log_{10} C}$$
>
> Por lo tanto, los dígitos correctos pasan de $d$ a aproximadamente $2d - \log_{10}(1/C)$.
>
> **Ejemplo:** Para $C = 0.3536$, $\log_{10}(1/C) \approx 0.45$. Si $d=3$, entonces $2d - 0.45 \approx 5.55$ dígitos (se gana aproximadamente $d+1$ dígitos).

---

## Relación con otros métodos

> [!info]
> **Comparación de órdenes de convergencia:**
>
> | Método | Orden $p$ | Característica |
> |:---|:---|:---|
> | [[Biseccion]] | 1 (lineal) | $e^{(k+1)} \approx 0.5 e^{(k)}$ |
> | [[Punto Fijo Aproximaciones Sucesivas/index\|Punto fijo]] | 1 (lineal) | $e^{(k+1)} \approx \|g'(r)\| e^{(k)}$ |
> | [[Metodo Secante Orden Convergencia Fi\|Secante]] | $\approx 1.618$ (superlineal) | $e^{(k+1)} \approx C (e^{(k)})^{1.618}$ |
> | **Newton (raíz simple)** | **2 (cuadrático)** | $e^{(k+1)} \approx C (e^{(k)})^{2}$ |
> | [[Convergencia Lineal Raices Multiples\|Newton (raíz múltiple)]] | 1 (lineal) | $e^{(k+1)} \approx (1 - 1/m) e^{(k)}$ |
>
> El método de Newton es el de mayor orden entre los métodos que no requieren derivadas de orden superior. Por esta razón es el método de elección cuando se dispone de la derivada.

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| **Definición** | $\lim_{k \to \infty} \|e^{(k+1)}\|/\|e^{(k)}\|^2 = C$ |
| **Condición** | $f'(r) \neq 0$ (raíz simple) |
| **Constante** | $C = \|f''(r)\|/(2\|f'(r)\|)$ |
| **Dígitos por iteración** | Se duplican asintóticamente |
| **Demostración** | Vía $g'(r)=0$ en $g(x)=x-f(x)/f'(x)$ |
| **Comparación** | Más rápido que lineal ($p=1$) y superlineal ($p \approx 1.618$) |

> [!corolario]
> El método de Newton exhibe convergencia cuadrática para raíces simples, lo que significa que el error se reduce cuadráticamente ($e^{(k+1)} \approx C (e^{(k)})^2$) y los dígitos correctos se duplican en cada iteración. Este es el resultado más importante del análisis de convergencia de Newton, y justifica su amplia utilización. La constante asintótica $C = \|f''(r)\|/(2\|f'(r)\|)$ determina la velocidad específica: cuanto menor sea $C$, más rápida es la convergencia. Para raíces múltiples, la convergencia se reduce a lineal, tema desarrollado en [[Convergencia Lineal Raices Multiples]].