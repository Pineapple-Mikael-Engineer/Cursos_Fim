---
title: Residuo vs Error Relativo de la Solución
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - sistemas-lineales
  - error-numerico
draft: false
aliases:
  - Residuo y error
  - Residual vs error
  - Error hacia atrás de un sistema lineal
---

# Residuo frente a Error Relativo de la Solución

> [!definicion]
> Dada una solución aproximada $\tilde x$ del sistema $Ax = b$ (con solución exacta $x = A^{-1}b$):
> - El **residuo** es $r = b - A\tilde x$. Es siempre calculable.
> - El **error** es $e = x - \tilde x$. No es observable sin conocer $x$.
>
> Ambos se vinculan por $A e = A(x - \tilde x) = b - A\tilde x = r$, es decir $e = A^{-1} r$.

> [!info]
> El residuo mide *cuánto incumple* $\tilde x$ la ecuación; el error mide *cuán lejos* está de la solución. La relación $e = A^{-1}r$ muestra que un residuo pequeño se traduce en error pequeño solo si $A^{-1}$ no amplifica, esto es, si $A$ está [[Condicionamiento Numerico Numero Condicion|bien condicionada]].

---

## Cota fundamental residuo–error

> [!teorema]
> Para $A$ no singular y $b \neq 0$, el error relativo está acotado por el residuo relativo a través del [[Condicionamiento Numerico Numero Condicion|número de condición]]:
> $$\frac{1}{\kappa(A)}\,\frac{\|r\|}{\|b\|} \;\leq\; \frac{\|e\|}{\|x\|} \;\leq\; \kappa(A)\,\frac{\|r\|}{\|b\|}.$$

> [!demostracion]
> **Cota superior.** De $e = A^{-1}r$ y $\|b\| = \|Ax\| \leq \|A\|\|x\|$:
> $$\|e\| = \|A^{-1}r\| \leq \|A^{-1}\|\,\|r\|, \qquad \frac{1}{\|x\|} \leq \frac{\|A\|}{\|b\|}.$$
> Multiplicando:
> $$\frac{\|e\|}{\|x\|} \leq \|A^{-1}\|\,\|A\|\,\frac{\|r\|}{\|b\|} = \kappa(A)\,\frac{\|r\|}{\|b\|}.$$
>
> **Cota inferior.** De $r = Ae$ y $\|x\| = \|A^{-1}b\| \leq \|A^{-1}\|\|b\|$:
> $$\|r\| \leq \|A\|\,\|e\|, \qquad \frac{1}{\|x\|} \geq \frac{1}{\|A^{-1}\|\|b\|}.$$
> Luego $\dfrac{\|r\|}{\|b\|} \leq \|A\|\|A^{-1}\|\,\dfrac{\|e\|}{\|x\|} = \kappa(A)\dfrac{\|e\|}{\|x\|}$, que reordenada da la cota inferior.

> [!info]
> Las dos desigualdades encierran el error entre $\frac{1}{\kappa}$ y $\kappa$ veces el residuo relativo. Si $\kappa(A) \approx 1$, residuo y error coinciden en orden de magnitud. Si $\kappa(A) \gg 1$, el residuo deja de ser indicador fiable del error.

---

## Ejemplo: residuo engañoso

> [!ejemplo]
> **Sistema mal condicionado.** Con
> $$A = \begin{pmatrix} 1 & 1 \\ 1 & 1.0001 \end{pmatrix}, \quad b = \begin{pmatrix} 2 \\ 2.0001 \end{pmatrix}, \quad x = \begin{pmatrix} 1 \\ 1 \end{pmatrix},$$
> tomemos $\tilde x = (2,\,0)^T$.
>
> | Cantidad | Valor |
> |:---|:---|
> | Residuo $r = b - A\tilde x$ | $(0,\,-10^{-4})^T$ |
> | Residuo relativo $\|r\|_\infty/\|b\|_\infty$ | $\approx 5\times10^{-5}$ |
> | Error $e = x - \tilde x$ | $(-1,\,1)^T$ |
> | Error relativo $\|e\|_\infty/\|x\|_\infty$ | $1$ |
> | $\kappa_\infty(A)$ | $\approx 4\times10^{4}$ |
>
> El residuo relativo es $\sim 10^{-5}$ pero el error relativo es $1$: el cociente es justamente del orden de $\kappa(A)$. Confiar en el residuo habría dado una falsa sensación de exactitud.

---

## Residuo y error hacia atrás

> [!teorema]
> El residuo relativo coincide (en norma) con el **error hacia atrás normalizado** de la solución calculada. Concretamente, $\tilde x$ resuelve exactamente el sistema perturbado $(A + \Delta A)\tilde x = b$ con
> $$\Delta A = \frac{r\,\tilde x^T}{\tilde x^T \tilde x}, \qquad \frac{\|\Delta A\|_2}{\|A\|_2} = \frac{\|r\|_2}{\|A\|_2\,\|\tilde x\|_2}.$$

> [!demostracion]
> Con $\Delta A = r\tilde x^T/(\tilde x^T\tilde x)$ se verifica
> $$(A + \Delta A)\tilde x = A\tilde x + \frac{r\,\tilde x^T \tilde x}{\tilde x^T\tilde x} = A\tilde x + r = A\tilde x + (b - A\tilde x) = b.$$
> Como $\operatorname{rango}(\Delta A) = 1$, $\|\Delta A\|_2 = \|r\|_2\|\tilde x\|_2/\|\tilde x\|_2^2 = \|r\|_2/\|\tilde x\|_2$. (Teorema de Rigal–Gaches: este $\Delta A$ es el de **menor** norma posible.)

> [!info]
> Esta es la lectura clave: **un residuo pequeño certifica estabilidad hacia atrás, no precisión hacia adelante**. La solución calculada es la respuesta exacta de un sistema casi idéntico; cuánto se parezca esa respuesta a la del sistema original depende del [[Condicionamiento Numerico Numero Condicion|condicionamiento]], según la relación [[Estabilidad Algoritmos Forward Backward|forward $\lesssim \kappa\cdot$ backward]].

---

## Refinamiento iterativo

> [!algoritmo]
> **Recuperar precisión usando el residuo.** Dado $\tilde x$ y su factorización [[Factorizacion LU/index|LU]] de $A$:
>
> ```
> repetir:
>     r = b - A x̃              // calcular en precisión extendida si es posible
>     resolver A δ = r          // reutiliza la factorización LU (O(n²))
>     x̃ = x̃ + δ
> hasta ||δ|| / ||x̃|| < tol
> ```
>
> Cada paso recupera aproximadamente $-\log_{10}(\kappa(A)\,u)$ dígitos. El residuo, calculado en mayor precisión, es lo que permite la corrección.

---

## Relación con otras notas

> [!info]
> - El factor $\kappa(A)$ que separa residuo de error se define en [[Condicionamiento Numerico Numero Condicion]].
> - La interpretación del residuo como error hacia atrás pertenece al marco de [[Estabilidad Algoritmos Forward Backward]].
> - El análisis de cómo $\kappa(A)$ amplifica perturbaciones en los datos se desarrolla en [[Sensibilidad Solucion Numero Condicion]].

---

## Resumen

| Cantidad | Definición | Observable |
|:---|:---|:---|
| Residuo $r$ | $b - A\tilde x$ | sí, $O(n^2)$ |
| Error $e$ | $x - \tilde x = A^{-1}r$ | no |
| Cota | $\frac{1}{\kappa}\frac{\|r\|}{\|b\|} \leq \frac{\|e\|}{\|x\|} \leq \kappa\frac{\|r\|}{\|b\|}$ | — |
| Error hacia atrás | $\|\Delta A\|/\|A\| = \|r\|/(\|A\|\|\tilde x\|)$ | sí |

> [!corolario]
> El residuo es calculable y el error no; los conecta el número de condición mediante $e = A^{-1}r$ y la doble cota $\frac{1}{\kappa}\frac{\|r\|}{\|b\|} \leq \frac{\|e\|}{\|x\|} \leq \kappa\frac{\|r\|}{\|b\|}$. Un residuo pequeño solo prueba que la solución es exacta para un sistema vecino (estabilidad hacia atrás); la precisión efectiva exige además $\kappa(A)$ moderado. El residuo, sin embargo, no es inútil: alimenta el refinamiento iterativo que recupera dígitos perdidos. El estudio de la amplificación por $\kappa(A)$ continúa en [[Sensibilidad Solucion Numero Condicion]].
