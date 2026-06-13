---
title: Comparación Analítica del Orden de Convergencia
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-no-lineales
  - convergencia
draft: false
aliases:
  - Comparación de métodos
  - Orden de convergencia comparado
  - Eficiencia de métodos de raíces
---

# Comparación Analítica del Orden de Convergencia

> [!definicion]
> Una sucesión $\{x^{(k)}\}$ que converge a $r$ tiene **orden de convergencia** $p$ y **constante asintótica** $C$ si
> $$\lim_{k\to\infty}\frac{|x^{(k+1)} - r|}{|x^{(k)} - r|^{p}} = C, \qquad C > 0.$$
> El orden $p$ mide *cuán rápido* decae el error; $p=1$ es lineal, $1<p<2$ superlineal, $p=2$ cuadrático.

> [!info]
> Esta nota reúne y compara los órdenes de los métodos de una variable —[[Biseccion]], [[Regula Falsi]], [[Punto Fijo Aproximaciones Sucesivas/index|punto fijo]], [[Metodo Secante Orden Convergencia Fi|secante]] y [[Newton Raphson/index|Newton]]— desde un criterio común, e introduce el **índice de eficiencia** que pondera orden y costo por iteración.

---

## Tabla maestra de órdenes

> [!info]
> | Método | Orden $p$ | Constante / factor | Evaluaciones/iter | Garantía |
> |:---|:---:|:---|:---:|:---:|
> | [[Biseccion]] | 1 | factor $1/2$ exacto | 1 ($f$) | sí |
> | [[Regula Falsi]] | 1 | factor variable, puede $\to 1$ | 1 ($f$) | sí |
> | [[Punto Fijo Aproximaciones Sucesivas/index\|Punto fijo]] | 1 | $C = |g'(r)|$ (si $\neq 0$) | 1 ($g$) | local |
> | [[Metodo Secante Orden Convergencia Fi\|Secante]] | $\varphi \approx 1.618$ | $C = |f''/2f'|^{1/\varphi}$ | 1 ($f$) | local |
> | [[Newton Raphson/index\|Newton]] (raíz simple) | 2 | $C = |f''(r)/2f'(r)|$ | 2 ($f,f'$) | local |
> | [[Convergencia Lineal Raices Multiples\|Newton]] (raíz múltiple $m$) | 1 | $C = 1 - 1/m$ | 2 | local |

> [!warning]
> **Lineal no es todo igual.** Bisección tiene factor $1/2$ garantizado; punto fijo tiene factor $|g'(r)|$ que puede ser cercano a $1$ (muy lento) o pequeño (rápido). Dos métodos de orden $p=1$ pueden diferir en órdenes de magnitud de velocidad según su constante asintótica.

---

## Dígitos correctos por iteración

> [!teorema]
> Si $|e^{(k)}| \approx 10^{-d_k}$ (es decir, $d_k$ dígitos correctos), el orden $p$ determina la progresión de la precisión:
> $$d_{k+1} \approx p\,d_k - \log_{10}\!\frac{1}{C}.$$
> - **Lineal ($p=1$):** $d_{k+1} \approx d_k + \log_{10}(1/C)$ — se gana un número **constante** de dígitos por paso.
> - **Superlineal/cuadrático ($p>1$):** $d_{k+1} \approx p\,d_k$ — los dígitos se **multiplican** por $p$.

> [!ejemplo]
> **Progresión de dígitos correctos** (partiendo de $d_0 = 1$, raíz $\sqrt2$):
>
> | Iter | Bisección ($+0.3$/paso) | Secante ($\times1.618$) | Newton ($\times2$) |
> |:---:|:---:|:---:|:---:|
> | 0 | 1 | 1 | 1 |
> | 1 | 1.3 | 1.6 | 2 |
> | 2 | 1.6 | 2.6 | 4 |
> | 3 | 1.9 | 4.2 | 8 |
> | 4 | 2.2 | 6.9 | 16 |
> | 5 | 2.5 | 11.1 | 32 |
>
> Bisección suma; secante y Newton multiplican. La brecha se abre exponencialmente: para $15$ dígitos Newton necesita $\sim4$ iteraciones desde $d=1$, la bisección $\sim47$.

---

## Índice de eficiencia: orden por costo

> [!definicion]
> El **índice de eficiencia** pondera el orden contra el número $m$ de evaluaciones de función por iteración:
> $$E = p^{1/m}.$$
> Compara métodos en igualdad de *coste*, no de iteraciones.

> [!teorema]
> Con el supuesto de que evaluar $f'$ cuesta lo mismo que evaluar $f$:
> $$E_{\text{secante}} = \varphi^{1/1} \approx 1.618 \;>\; E_{\text{Newton}} = 2^{1/2} \approx 1.414.$$
> La secante es más eficiente por evaluación que Newton, pese a su menor orden.

> [!warning]
> Si la derivada es **gratis** o muy barata (por ejemplo, $f$ polinómica con $f'$ trivial, o diferenciación automática), Newton recupera la ventaja: en ese caso $m=1$ efectivo y $E_{\text{Newton}} = 2 > 1.618$. La elección depende del costo relativo de $f$ y $f'$.

---

## Criterio de selección

> [!info]
> | Situación | Método recomendado |
> |:---|:---|
> | Solo se garantiza continuidad y cambio de signo | [[Biseccion]] (robusto) |
> | Se dispone de $f'$ barata y buen punto inicial | [[Newton Raphson/index\|Newton]] (cuadrático) |
> | $f'$ cara o desconocida, buen punto inicial | [[Metodo Secante Orden Convergencia Fi\|Secante]] (mejor eficiencia) |
> | Robustez + velocidad | híbrido: bisección hasta acotar, luego Newton/secante (método de Brent) |
> | Raíz múltiple conocida (mult. $m$) | Newton modificado $x - m\,f/f'$ (recupera $p=2$) |

> [!teoria]
> Los métodos de producción (Brent, `scipy.optimize.brentq`) **combinan** garantía y velocidad: usan bisección como red de seguridad y secante/interpolación cuadrática inversa para acelerar cuando el comportamiento local lo permite, capturando lo mejor de cada orden.

---

## Relación con otras notas

> [!info]
> - Cada método y su demostración de orden: [[Biseccion]], [[Regula Falsi]], [[Punto Fijo Aproximaciones Sucesivas/index]], [[Metodo Secante Orden Convergencia Fi]], [[Orden Convergencia Cuadratica Simple]].
> - El caso degenerado de Newton: [[Convergencia Lineal Raices Multiples]].
> - Panorama general del capítulo: [[3 Ecuaciones No Lineales/index]].
> - La extensión multivariable mantiene la jerarquía: [[Sistemas Ecuaciones No Lineales/index]].

---

## Resumen

| Método | $p$ | Eficiencia $p^{1/m}$ | Garantía |
|:---|:---:|:---:|:---:|
| Bisección | 1 | 1.000 | sí |
| Punto fijo | 1 | $\leq 1$ útil si $|g'|<1$ | local |
| Secante | 1.618 | **1.618** | local |
| Newton (simple) | 2 | 1.414 | local |
| Newton (múltiple) | 1 | $<1.414$ | local |

> [!corolario]
> El orden de convergencia $p$ ordena los métodos de una variable: bisección y punto fijo son lineales ($p=1$, dígitos que se suman), la secante es superlineal ($\varphi \approx 1.618$) y Newton cuadrático ($p=2$, dígitos que se duplican). Pero el orden no basta: el índice de eficiencia $p^{1/m}$ revela que la secante supera a Newton cuando la derivada cuesta tanto como la función, y que dos métodos lineales pueden diferir enormemente según su constante asintótica. En la práctica, los algoritmos híbridos combinan la garantía de la [[Biseccion|bisección]] con la velocidad de [[Newton Raphson/index|Newton]] y la [[Metodo Secante Orden Convergencia Fi|secante]]. Esta jerarquía se preserva al pasar a [[Sistemas Ecuaciones No Lineales/index|sistemas multivariables]].
