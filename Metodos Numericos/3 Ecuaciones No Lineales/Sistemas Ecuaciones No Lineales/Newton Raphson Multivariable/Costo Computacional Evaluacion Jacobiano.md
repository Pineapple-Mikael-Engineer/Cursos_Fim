---
title: Costo Computacional y Evaluación del Jacobiano
order: 3
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-no-lineales
  - sistemas-no-lineales
  - newton-raphson
draft: false
aliases:
  - Costo de Newton multivariable
  - Métodos cuasi-Newton
  - Broyden
  - Computational cost Jacobian
---

# Costo Computacional y Evaluación del Jacobiano

> [!definicion]
> El **costo por iteración** de [[Newton Raphson Multivariable/index|Newton multivariable]] se reparte entre tres tareas: evaluar $F$ ($n$ funciones), formar la [[Matriz Jacobiana y Sistema Lineal Asociado|jacobiana]] $J$ ($n^2$ derivadas) y resolver el sistema lineal $J\,\Delta x = -F$ ($\frac{2}{3}n^3$ flops por [[Factorizacion LU/index|factorización LU]]).

> [!info]
> Para $n$ grande, el término dominante es la resolución del sistema, $O(n^3)$ por iteración. Esto motiva los **métodos cuasi-Newton**, que evitan recalcular y refactorizar $J$ en cada paso, sacrificando la [[Convergencia Local Cuadratica|cuadraticidad]] por un costo mucho menor.

---

## Desglose del costo por iteración

> [!info]
> | Tarea | Costo | Observación |
> |:---|:---|:---|
> | Evaluar $F(x^{(k)})$ | $n\cdot c_f$ | $c_f$ = costo de una componente |
> | Formar $J(x^{(k)})$ | $n^2\cdot c_{f'}$ (analítica) o $n$ evaluaciones de $F$ (dif. finitas) | $n^2$ derivadas parciales |
> | Factorizar $J$ (LU) | $\frac{2}{3}n^3$ | una vez por iteración en Newton puro |
> | Resolver con la factorización | $2n^2$ | sustitución directa/regresiva |
> | **Total por iteración (Newton)** | $O(n^3)$ | dominado por la factorización |

> [!warning]
> **Diferencias finitas para $J$.** Si no hay jacobiana analítica, cada columna $J e_j \approx [F(x + h e_j) - F(x)]/h$ cuesta una evaluación de $F$: **$n$ evaluaciones extra** por iteración, más el error de truncamiento/cancelación que limita la precisión del paso (paso óptimo $h \approx \sqrt{u}\|x\|$).

---

## Métodos cuasi-Newton: amortizar la jacobiana

> [!teoria]
> La idea es **reutilizar** información de la jacobiana entre iteraciones, en vez de recalcular $J$ y refactorizar desde cero:
>
> - **Newton con jacobiana congelada:** mantener $J(x^{(0)})$ y su factorización LU durante varias iteraciones. Cada paso adicional cuesta solo $O(n^2)$ (resolver con la LU ya calculada), pero la convergencia baja a lineal.
> - **Método de Broyden:** actualizar una aproximación $B_k \approx J(x^{(k)})$ con una corrección de **rango 1** que satisface la ecuación de la secante $B_{k+1}(x^{(k+1)} - x^{(k)}) = F(x^{(k+1)}) - F(x^{(k)})$.

> [!teorema]
> **Actualización de Broyden (bueno).** Con $s_k = x^{(k+1)} - x^{(k)}$ y $y_k = F(x^{(k+1)}) - F(x^{(k)})$:
> $$B_{k+1} = B_k + \frac{(y_k - B_k s_k)\,s_k^T}{s_k^T s_k}.$$
> Es la corrección de rango 1 de **mínima norma** consistente con la ecuación de la secante. Aplicando la fórmula de Sherman–Morrison se actualiza directamente $B_k^{-1}$, evitando toda factorización: el costo por iteración baja a $O(n^2)$.

---

## Comparación de costos y convergencia

> [!info]
> | Método | $J$ por iteración | Álgebra lineal/iter | Orden | Costo total a precisión |
> |:---|:---|:---|:---:|:---|
> | Newton puro | recalcula $J$ | $\frac{2}{3}n^3$ (LU) | 2 | pocas iteraciones caras |
> | Newton con $J$ congelada | nunca | $2n^2$ | 1 | muchas iteraciones baratas |
> | **Broyden** | actualización rango 1 | $O(n^2)$ | superlineal | equilibrio |
>
> Broyden logra convergencia **superlineal** con costo $O(n^2)$ por paso: en problemas grandes donde formar/factorizar $J$ domina, supera a Newton puro en tiempo total, aunque necesite más iteraciones.

---

## Ejemplo: conteo para $n = 100$

> [!ejemplo]
> **Sistema de $n = 100$ ecuaciones**, $F$ con componentes de costo moderado.
>
> | Concepto | Newton puro | Broyden |
> |:---|:---:|:---:|
> | Evaluaciones de $F$/iter | $1 + 100$ (si $J$ por dif. finitas) | $1$ |
> | Flops de álgebra lineal/iter | $\frac{2}{3}(100)^3 \approx 6.7\times10^5$ | $\sim (100)^2 = 10^4$ |
> | Orden | 2 | $\approx 1.7$ |
> | Iteraciones típicas | $5$ | $8$ |
>
> Newton converge en menos iteraciones, pero cada una cuesta $\sim 67\times$ más en álgebra lineal y $\sim100\times$ más evaluaciones de $F$. Cuando evaluar $F$ o factorizar $J$ es caro, Broyden gana en tiempo total.

---

## Estrategias para problemas grandes y dispersos

> [!info]
> - **Jacobiana dispersa:** si cada $f_i$ depende de pocas variables, $J$ es dispersa; factorizaciones LU dispersas y coloración de grafos reducen el costo de formarla por diferencias finitas.
> - **Newton inexacto (Newton–Krylov):** resolver $J\Delta x = -F$ **aproximadamente** con un método iterativo ([[Jacobi|Jacobi]]/GMRES) que solo requiere productos $J v$, calculables sin formar $J$: $J v \approx [F(x + hv) - F(x)]/h$. Esencial en discretizaciones de EDPs.
> - **Reuso de factorización:** refactorizar $J$ solo cada pocas iteraciones (Newton "perezoso").

---

## Relación con otras notas

> [!info]
> - La estructura del sistema lineal por paso: [[Matriz Jacobiana y Sistema Lineal Asociado]].
> - La factorización que domina el costo: [[Factorizacion LU/index]] y su [[Costo Computacional vs Eliminacion Gaussiana|conteo de operaciones]].
> - El orden que se sacrifica al aproximar $J$: [[Convergencia Local Cuadratica]].
> - El análogo escalar (secante = cuasi-Newton 1D): [[Metodo Secante Orden Convergencia Fi]].
> - Los métodos iterativos para el sistema interno: [[Jacobi]], [[Gauss Seidel]].

---

## Resumen

| Aspecto | Newton puro | Cuasi-Newton (Broyden) |
|:---|:---|:---|
| Costo álgebra lineal/iter | $\frac{2}{3}n^3$ | $O(n^2)$ |
| $J$ | recalculada + factorizada | actualización rango 1 |
| Orden | cuadrático | superlineal |
| Idóneo | $n$ pequeño, $J$ barata | $n$ grande, $J$ o $F$ caras |

> [!corolario]
> El costo de Newton multivariable está dominado por formar y factorizar la jacobiana, $O(n^3)$ por iteración, a lo que se suman $n$ evaluaciones extra de $F$ si $J$ se aproxima por diferencias finitas. Los métodos cuasi-Newton —jacobiana congelada, Broyden— amortizan ese costo reutilizando o actualizando $J$ con correcciones de rango 1, bajando a $O(n^2)$ por paso a cambio de pasar de convergencia [[Convergencia Local Cuadratica|cuadrática]] a superlineal. Para sistemas grandes y dispersos, Newton–Krylov inexacto resuelve el paso lineal solo con productos $Jv$. La elección replica el compromiso escalar entre [[Orden Convergencia Cuadratica Simple|Newton]] y [[Metodo Secante Orden Convergencia Fi|secante]]: más orden por iteración frente a menos costo por iteración.
