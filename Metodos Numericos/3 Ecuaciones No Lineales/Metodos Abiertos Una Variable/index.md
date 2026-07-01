---
title: Métodos Abiertos (Una Variable)
order: 3
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-no-lineales
  - index
draft: false
aliases:
  - métodos abiertos
  - métodos abiertos una variable
  - open methods
---

# Métodos Abiertos (Una Variable)

> [!definicion]
> Los **métodos abiertos** buscan una raíz de $f(x)=0$ partiendo de **uno o dos puntos iniciales** que **no** necesitan encerrar la raíz (a diferencia de los métodos cerrados, como bisección). A cambio de renunciar a la garantía de convergencia, ganan **velocidad**: cuando convergen, lo hacen mucho más rápido —típicamente **orden lineal** (punto fijo) o **cuadrático** (Newton–Raphson)—.

> [!info]
> Una de las dos familias de [[3 Ecuaciones No Lineales/index| ecuaciones no lineales]]; la contraparte de los métodos cerrados. Rápidos pero sin garantía: pueden diverger o ciclar si el arranque es malo. Burden–Faires, cap. 2; Chapra, cap. 6.

## Iterar en vez de encerrar

> [!teoria] Punto fijo, Newton y su orden
> - **Punto fijo**: se reescribe $f(x)=0$ como $x=g(x)$ y se itera $x_{k+1}=g(x_k)$; converge (linealmente) si $|g'(x^\*)|<1$. Es el marco del que salen los demás. → [[Punto Fijo Aproximaciones Sucesivas/index| Punto fijo]].
> - **Newton–Raphson**: usa la derivada, $x_{k+1}=x_k-f(x_k)/f'(x_k)$; **convergencia cuadrática** cerca de la raíz. La secante lo aproxima sin derivada. → [[Newton Raphson/index| Newton–Raphson]].
> - **Comparar el orden**: qué significa orden lineal/cuadrático/superlineal y cómo se traduce en número de iteraciones. → [[Comparacion Analitica Orden Convergencia]].

## Mapa de la sección

> [!info] Las notas y subsecciones
> | Elemento | Contenido |
> |:---|:---|
> | [[Punto Fijo Aproximaciones Sucesivas/index\| Punto fijo]] | $x=g(x)$; condición $\|g'\|<1$; orden lineal |
> | [[Newton Raphson/index\| Newton–Raphson]] | derivada; convergencia cuadrática; secante |
> | [[Comparacion Analitica Orden Convergencia]] | orden de convergencia y su lectura práctica |

> [!corolario]
> Los métodos abiertos cambian **garantía por velocidad**: sin encerrar la raíz pueden fallar, pero cuando aciertan el arranque convergen muy rápido. Punto fijo da el marco teórico y Newton, el caballo de batalla cuadrático.

> [!referencia]
> Burden–Faires, *Análisis Numérico*, cap. 2. Chapra–Canale, cap. 6.
