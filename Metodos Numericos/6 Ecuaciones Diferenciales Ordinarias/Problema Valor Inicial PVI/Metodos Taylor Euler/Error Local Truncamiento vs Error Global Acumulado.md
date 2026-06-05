---
title: Error Local de Truncamiento vs Error Global Acumulado
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-inicial
  - error-numerico
  - convergencia
draft: false
aliases:
  - Error local vs global
  - Error de truncamiento de EDOs
  - Orden de un método de EDOs
  - Local vs global error
---

# Error Local de Truncamiento vs Error Global Acumulado

> [!definicion]
> - El **error local de truncamiento** $\tau_n$ es el cometido en **un** paso, suponiendo el dato exacto: $\tau_n = y(t_{n+1}) - [\,y(t_n) + h\,\Phi(t_n, y(t_n), h)\,]$, donde $\Phi$ es la función incremento del método.
> - El **error global** $e_n = y(t_n) - y_n$ es el acumulado tras $n$ pasos desde la condición inicial.

> [!info]
> La relación clave es que el error global tiene **un orden menos** que el local: si $\tau_n = O(h^{p+1})$, entonces $e_n = O(h^p)$. El método es de **orden $p$**. Se pierde una potencia de $h$ al acumular $N = (t_f-t_0)/h$ pasos.

---

## De local a global: el teorema de convergencia

> [!teorema]
> Sea un método de un paso con error local $\tau_n \leq C\,h^{p+1}$ y función incremento $\Phi$ Lipschitz en $y$ con constante $L_\Phi$. Entonces el error global está acotado por
> $$|e_n| \leq \frac{C\,h^p}{L_\Phi}\Big(e^{L_\Phi(t_n - t_0)} - 1\Big) = O(h^p).$$

> [!demostracion]
> Restando la solución exacta del paso numérico, el error satisface la recurrencia
> $$e_{n+1} = e_n + h\big[\Phi(t_n, y(t_n),h) - \Phi(t_n, y_n, h)\big] + \tau_n.$$
> Tomando valor absoluto y usando Lipschitz de $\Phi$:
> $$|e_{n+1}| \leq (1 + hL_\Phi)|e_n| + Ch^{p+1}.$$
> Esta recurrencia lineal se resuelve: con $|e_0|=0$,
> $$|e_n| \leq Ch^{p+1}\sum_{k=0}^{n-1}(1+hL_\Phi)^k = Ch^{p+1}\frac{(1+hL_\Phi)^n - 1}{hL_\Phi} \leq \frac{Ch^p}{L_\Phi}\big(e^{L_\Phi(t_n-t_0)}-1\big),$$
> usando $(1+hL_\Phi)^n \leq e^{nhL_\Phi} = e^{L_\Phi(t_n-t_0)}$. El error global es $O(h^p)$.

> [!info]
> Aparece la constante de Lipschitz $L_\Phi$ (ligada a la $L$ de [[Teoremas Existencia Unicidad Picard Lindelof|Picard-Lindelöf]]) y el factor $e^{L(t_n-t_0)}$: el error se amplifica **exponencialmente** con el horizonte de integración. Simular a largo plazo es intrínsecamente más difícil.

---

## Por qué se pierde un orden

> [!teoria]
> Cada paso introduce un error local $O(h^{p+1})$. Al integrar hasta $t_f$ hay $N = (t_f-t_0)/h$ pasos, así que en el peor caso (sin cancelación) los errores se suman:
> $$\text{error global} \sim N \cdot O(h^{p+1}) = \frac{t_f-t_0}{h}\cdot O(h^{p+1}) = O(h^p).$$
> Es la misma aritmética que en la [[Trapecio Compuesto Convergencia O h2|integración compuesta]]: sumar $1/h$ contribuciones rebaja el orden en uno.

---

## Ejemplo: verificación del orden

> [!ejemplo]
> **$y'=y$, $y(0)=1$ hasta $t=1$ (exacta $e\approx2.71828$).** Error global al halvar $h$:
>
> | $h$ | [[Euler Explicito Orden 1 Interpretacion Geometrica\|Euler]] (error) | factor | [[RK4 Clasico Tabla Butcher y Orden Cuatro\|RK4]] (error) | factor |
> |:---:|:---:|:---:|:---:|:---:|
> | 0.1 | $1.2\times10^{-1}$ | — | $2.3\times10^{-6}$ | — |
> | 0.05 | $6.6\times10^{-2}$ | 1.9 | $1.4\times10^{-7}$ | 16 |
> | 0.025 | $3.4\times10^{-2}$ | 1.9 | $9\times10^{-9}$ | 16 |
>
> Euler: factor $\approx2 = 2^1$ ⟹ orden 1. RK4: factor $\approx16 = 2^4$ ⟹ orden 4. El cociente $\log_2(E(h)/E(h/2))$ confirma el orden global.

---

## Orden de los métodos comunes

> [!info]
> | Método | Error local | Orden global |
> |:---|:---:|:---:|
> | [[Euler Explicito Orden 1 Interpretacion Geometrica\|Euler]] | $O(h^2)$ | 1 |
> | [[RK2 Heun Euler Modificado Punto Medio\|RK2 / Heun]] | $O(h^3)$ | 2 |
> | [[Metodos Serie Taylor Orden Superior\|Taylor orden $p$]] | $O(h^{p+1})$ | $p$ |
> | [[RK4 Clasico Tabla Butcher y Orden Cuatro\|RK4]] | $O(h^5)$ | 4 |

> [!warning]
> El orden es **asintótico** y supone aritmética exacta. Para $h$ muy pequeño, el redondeo (que crece como $\sim u/h$ por el número de pasos) impone un límite: existe un $h$ óptimo, igual que en la [[Inestabilidad Error Redondeo Paso h|diferenciación numérica]]. Además, el factor $e^{Lt}$ degrada la precisión en horizontes largos.

---

## Relación con otras notas

> [!info]
> - El método de orden 1 base: [[Euler Explicito Orden 1 Interpretacion Geometrica]].
> - La constante $L$ que controla la acumulación: [[Teoremas Existencia Unicidad Picard Lindelof]].
> - El orden alto que reduce el error: [[RK4 Clasico Tabla Butcher y Orden Cuatro]].
> - El teorema que une consistencia, estabilidad y convergencia: [[Consistencia Estabilidad Convergencia Lax]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Error local $\tau_n$ | un paso, $O(h^{p+1})$ |
| Error global $e_n$ | acumulado, $O(h^p)$ |
| Relación | global = local $-1$ orden |
| Cota | $\frac{Ch^p}{L}(e^{L(t_n-t_0)}-1)$ |
| Verificación | $p \approx \log_2(E(h)/E(h/2))$ |

> [!corolario]
> El error local de truncamiento $O(h^{p+1})$ de un método de un paso se acumula sobre $N=(t_f-t_0)/h$ pasos hasta un error global $O(h^p)$ —un orden menos—, con una cota $\frac{Ch^p}{L}(e^{L(t_n-t_0)}-1)$ que crece exponencialmente con el horizonte vía la constante de Lipschitz $L$. Esta es la razón de que la simulación a largo plazo sea difícil y de que convenga el alto orden de [[RK4 Clasico Tabla Butcher y Orden Cuatro|RK4]]. El orden global, verificable por $\log_2(E(h)/E(h/2))$, junto con la [[Regiones Estabilidad Absoluta A Estabilidad|estabilidad]], determina la convergencia según el [[Consistencia Estabilidad Convergencia Lax|teorema de Lax]].
