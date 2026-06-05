---
title: Sensibilidad de la Solución y Número de Condición
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - sistemas-lineales
  - error-numerico
draft: false
aliases:
  - Sensibilidad de la solución
  - Perturbación de sistemas lineales
  - Análisis de perturbaciones
---

# Sensibilidad de la Solución y Número de Condición

> [!definicion]
> La **sensibilidad** de un sistema lineal $Ax = b$ mide cuánto cambia la solución $x$ ante perturbaciones en los datos $A$ y $b$. Está cuantificada por el [[Condicionamiento Numerico Numero Condicion|número de condición]] $\kappa(A) = \|A\|\,\|A^{-1}\|$, factor de amplificación del error relativo.

> [!info]
> Esta nota aplica el número de condición al **análisis de fiabilidad** de una solución directa: dadas perturbaciones simultáneas en $A$ y $b$ —ya sean errores de medición en los datos o errores de redondeo del algoritmo—, acota el error relativo de $x$.

---

## Cotas de perturbación

> [!teorema]
> **Perturbación solo en $b$.** Si $A(x + \Delta x) = b + \Delta b$, entonces
> $$\frac{\|\Delta x\|}{\|x\|} \leq \kappa(A)\,\frac{\|\Delta b\|}{\|b\|}.$$
>
> **Perturbación solo en $A$.** Si $(A + \Delta A)(x + \Delta x) = b$ con $\kappa(A)\,\|\Delta A\|/\|A\| < 1$, entonces
> $$\frac{\|\Delta x\|}{\|x\|} \leq \frac{\kappa(A)}{1 - \kappa(A)\frac{\|\Delta A\|}{\|A\|}}\,\frac{\|\Delta A\|}{\|A\|}.$$
>
> **Perturbación simultánea.** Si $(A + \Delta A)(x + \Delta x) = b + \Delta b$, a primer orden
> $$\frac{\|\Delta x\|}{\|x\|} \lesssim \kappa(A)\left(\frac{\|\Delta A\|}{\|A\|} + \frac{\|\Delta b\|}{\|b\|}\right).$$

> [!demostracion]
> **Caso $A$ y $b$ perturbados.** Restando $Ax = b$ de $(A+\Delta A)(x+\Delta x) = b + \Delta b$:
> $$A\,\Delta x + \Delta A\,(x + \Delta x) = \Delta b.$$
> Despejando $\Delta x = A^{-1}\big(\Delta b - \Delta A\,(x+\Delta x)\big)$ y tomando normas:
> $$\|\Delta x\| \leq \|A^{-1}\|\big(\|\Delta b\| + \|\Delta A\|\,\|x + \Delta x\|\big).$$
> Dividiendo entre $\|x\|$, usando $\|A^{-1}\| = \kappa(A)/\|A\|$ y $\|b\| \leq \|A\|\|x\|$, y despreciando el término de segundo orden $\Delta A\,\Delta x$, se obtiene la cota a primer orden.

---

## Ejemplo: amplificación medida

> [!ejemplo]
> **Matriz de Hilbert $H_5$** ($\kappa_2 \approx 4.8\times10^5$), $x = (1,1,1,1,1)^T$, $b = H_5 x$. Se perturba $b$ con $\|\Delta b\|_2/\|b\|_2 \approx 2.3\times10^{-11}$.
>
> | Cantidad | Valor |
> |:---|:---|
> | $\kappa_2(H_5)$ | $4.77\times10^{5}$ |
> | $\|\Delta b\|_2/\|b\|_2$ | $2.3\times10^{-11}$ |
> | $\|\Delta x\|_2/\|x\|_2$ medido | $8.9\times10^{-6}$ |
> | Factor de amplificación | $3.8\times10^{5}$ |
>
> El error de $x$ supera al de $b$ en cinco órdenes de magnitud, justo por debajo de la cota $\kappa_2$. Una perturbación de los datos imperceptible ($\sim10^{-11}$) deja la solución con apenas cinco o seis dígitos correctos.

---

## Regla de los dígitos perdidos

> [!warning]
> **Cuántos dígitos sobreviven.** Al resolver $Ax = b$ con [[Estabilidad Algoritmos Forward Backward|algoritmo estable]] y unidad de redondeo $u$:
> $$\text{dígitos correctos} \;\approx\; -\log_{10}(u) - \log_{10}\kappa(A).$$
> En doble precisión ($u \approx 10^{-16}$, $\approx 16$ dígitos) con $\kappa(A) = 10^8$ quedan solo $\approx 8$ dígitos correctos, **sea cual sea el algoritmo**. La pérdida la dicta el problema, no la implementación.

> [!proposicion]
> **Propiedades que enmarcan la sensibilidad:**
> 1. $\kappa(A) \geq 1$ siempre; las matrices ortogonales tienen $\kappa_2 = 1$ (insensibles).
> 2. $\kappa(\alpha A) = \kappa(A)$: la sensibilidad es invariante de escala.
> 3. $\kappa_2(A) \gg 1$ equivale a que $A$ está cerca (en distancia relativa $1/\kappa_2$) de una matriz singular.
> 4. La cota es **alcanzable**: existen perturbaciones que la saturan, por lo que $\kappa(A)$ no es pesimista en el peor caso.

---

## Lo que la sensibilidad no es

> [!warning]
> - **No depende del algoritmo.** Reduce el error hacia atrás con [[Pivoteo Parcial Total Estabilidad|pivoteo]], no $\kappa(A)$: la sensibilidad es del problema.
> - **No la arregla más precisión.** Aumentar dígitos de trabajo baja $u$, pero el factor $\kappa(A)$ persiste; un problema con $\kappa(A) = 10^{20}$ es irresoluble incluso en cuádruple precisión.
> - **Reformular sí ayuda.** Reescalar filas/columnas, elegir mejor base o usar [[Factorizacion LU/index|factorizaciones]] adaptadas puede reducir el $\kappa$ efectivo del problema reformulado.

---

## Relación con otras notas

> [!info]
> - La definición, propiedades y estimadores de $\kappa(A)$ están en [[Condicionamiento Numerico Numero Condicion]].
> - El vínculo entre residuo medible y error real es [[Residuo vs Error Relativo Solucion]].
> - Que el algoritmo aporte un error hacia atrás $O(u)$ se justifica en [[Estabilidad Algoritmos Forward Backward]] y [[Propagacion Errores Operaciones Matriciales]].

---

## Resumen

| Perturbación | Cota del error relativo de $x$ |
|:---|:---|
| Solo $b$ | $\kappa(A)\,\|\Delta b\|/\|b\|$ |
| Solo $A$ | $\dfrac{\kappa(A)}{1-\kappa\|\Delta A\|/\|A\|}\,\|\Delta A\|/\|A\|$ |
| $A$ y $b$ | $\kappa(A)\big(\|\Delta A\|/\|A\| + \|\Delta b\|/\|b\|\big)$ |
| Dígitos correctos | $-\log_{10}u - \log_{10}\kappa(A)$ |

> [!corolario]
> La sensibilidad de un sistema lineal es una propiedad intrínseca medida por $\kappa(A)$: toda perturbación relativa de los datos se amplifica hasta $\kappa(A)$ veces en la solución, y la regla $-\log_{10}u - \log_{10}\kappa(A)$ predice los dígitos correctos disponibles. Ningún algoritmo —por estable que sea— ni mayor precisión aritmética pueden vencer un mal condicionamiento; solo reformular el problema reduce $\kappa$. Junto con [[Residuo vs Error Relativo Solucion]], esta nota completa el [[Analisis Error Directos/index|análisis de fiabilidad]] de las soluciones obtenidas por métodos directos.
