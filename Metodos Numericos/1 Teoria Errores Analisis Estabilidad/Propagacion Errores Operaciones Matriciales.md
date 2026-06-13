---
title: Propagación de Errores en Operaciones Matriciales
tags:
  - metodos-numericos
  - teoria
  - error-numerico
  - algebra-lineal-numerica
draft: false
aliases:
  - Propagación de errores
  - Error en operaciones matriciales
  - Análisis de redondeo matricial
  - Error propagation
---

# Propagación de Errores en Operaciones Matriciales

> [!definicion]
> La **propagación de errores** describe cómo los errores de redondeo de cada operación elemental se acumulan al encadenar productos, sumas y resoluciones de sistemas sobre matrices y vectores. Cuantifica el error hacia atrás total de un algoritmo matricial en términos de la [[Epsilon Maquina y Precision Relativa|unidad de redondeo]] $u$ y la dimensión $n$.

> [!info]
> El resultado central es que las operaciones del álgebra lineal numérica son, en su mayoría, [[Estabilidad Algoritmos Forward Backward|estables hacia atrás]]: el error hacia atrás crece como $O(n\,u)$, no exponencialmente. El error hacia adelante final lo determina el [[Condicionamiento Numerico Numero Condicion|número de condición]].

---

## Modelo estándar de aritmética de punto flotante

> [!axioma]
> Para toda operación elemental $\circ \in \{+, -, \times, /\}$ entre números de máquina, el resultado redondeado satisface
> $$\operatorname{fl}(a \circ b) = (a \circ b)(1 + \delta), \qquad |\delta| \leq u,$$
> donde $u$ es la unidad de redondeo. Este modelo, junto con la ausencia de *underflow*/*overflow*, es la base de todo el análisis de redondeo.

> [!info]
> La constante que controla cadenas de $n$ operaciones es
> $$\gamma_n = \frac{n u}{1 - n u} \approx n u \quad (n u < 1).$$
> Aparece sistemáticamente en las cotas: un producto/suma de $n$ términos arrastra factores $(1+\theta)$ con $|\theta| \leq \gamma_n$.

---

## Cotas para las operaciones básicas

> [!teorema]
> Sean $A, B$ matrices y $x, y$ vectores de tamaño compatible, en aritmética con unidad de redondeo $u$.
>
> 1. **Producto escalar–vector:** $\operatorname{fl}(\alpha x) = \alpha x + e$, con $\|e\|_\infty \leq u\,|\alpha|\,\|x\|_\infty$.
> 2. **Suma de vectores:** $\operatorname{fl}(x + y) = (x + y) + e$, con $\|e\|_\infty \leq u\,\|x + y\|_\infty$.
> 3. **Producto interno:** $\operatorname{fl}(x^T y) = (x + \Delta x)^T y$, con $|\Delta x_i| \leq \gamma_n |x_i|$; equivalentemente $|\operatorname{fl}(x^Ty) - x^Ty| \leq \gamma_n \sum_i |x_i||y_i| = \gamma_n |x|^T|y|$.
> 4. **Producto matriz–vector:** $\operatorname{fl}(Ax) = (A + \Delta A)x$, con $|\Delta A| \leq \gamma_n |A|$ (desigualdad entrada a entrada).
> 5. **Producto matriz–matriz:** $\operatorname{fl}(AB) = AB + E$, con $|E| \leq \gamma_n |A||B|$.

> [!demostracion]
> **Producto interno (caso clave).** Sea $s_k$ la suma parcial calculada de $\sum_{i=1}^k x_i y_i$. Cada producto y cada suma introduce un factor $(1+\delta)$:
> $$\tilde s_1 = x_1 y_1 (1 + \delta_1),$$
> $$\tilde s_k = \big(\tilde s_{k-1} + x_k y_k (1 + \delta_k)\big)(1 + \varepsilon_k), \quad |\delta_i|,|\varepsilon_i| \leq u.$$
> Desplegando la recurrencia, cada término $x_i y_i$ queda multiplicado por un producto de a lo sumo $n$ factores $(1+\cdot)$. Usando la cota $\prod_{j}(1+\eta_j) = 1 + \theta$ con $|\theta| \leq \gamma_n$ cuando hay $\leq n$ factores:
> $$\tilde s = \sum_{i=1}^n x_i y_i (1 + \theta_i), \qquad |\theta_i| \leq \gamma_n.$$
> Reagrupando $\theta_i$ sobre $x_i$ se obtiene $\tilde s = (x + \Delta x)^T y$ con $|\Delta x_i| \leq \gamma_n |x_i|$. Las demás cotas se siguen aplicando esta a cada fila/columna.

---

## Ejemplo numérico

> [!ejemplo]
> **Producto interno de vectores con $n = 4$.** Sean $x = (1,\,10^{8},\,1,\,-10^{8})^T$, $y = (1,1,1,1)^T$. El valor exacto es $x^Ty = 2$.
>
> | Paso | Suma parcial exacta | Suma parcial $\operatorname{fl}$ (doble precisión) |
> |:---|:---|:---|
> | $+\,x_1y_1$ | $1$ | $1.000000000000000$ |
> | $+\,x_2y_2$ | $1.0000001\times10^8$ | $1.00000001\times10^8$ |
> | $+\,x_3y_3$ | $1.0000001\times10^8$ | $1.00000001\times10^8$ |
> | $+\,x_4y_4$ | $2$ | $2.000000000000000$ |
>
> Aquí no hay pérdida porque $u\cdot 10^8 \approx 10^{-8} \ll 1$ y el resultado se recupera. Pero si las magnitudes intermedias fueran $\sim 10^{16}$, el $\pm 1$ se perdería: la cota $\gamma_n |x|^T|y| = \gamma_4 \cdot (2\cdot10^8 + 2)$ revela que el error **absoluto** admisible escala con la magnitud de los términos intermedios, no con el resultado. Reordenar para sumar magnitudes similares (o usar suma compensada de Kahan) reduce el error.

---

## El orden de las operaciones importa

> [!warning]
> Las cotas anteriores acotan el peor caso, pero el error *real* depende del **orden de evaluación**:
>
> - **Suma de muchos términos:** sumar de menor a mayor magnitud reduce el error frente a sumar en orden arbitrario. La **suma compensada de Kahan** logra error $O(u)$ independiente de $n$.
> - **Asociatividad rota:** en punto flotante $\operatorname{fl}(\operatorname{fl}(a+b)+c) \neq \operatorname{fl}(a+\operatorname{fl}(b+c))$ en general; el álgebra no es asociativa.
> - **Productos matriciales encadenados:** $A(BC)$ y $(AB)C$ dan el mismo resultado exacto pero distinto error de redondeo y distinto costo.

---

## Propagación a través de la resolución de sistemas

> [!teorema]
> Al resolver $Ax = b$ por [[Eliminacion Gaussiana]] con [[Pivoteo Parcial Total Estabilidad|pivoteo parcial]], la solución calculada $\tilde x$ es la solución exacta de un sistema perturbado:
> $$(A + \Delta A)\,\tilde x = b, \qquad \frac{\|\Delta A\|_\infty}{\|A\|_\infty} \leq \rho\, n\, \gamma_n \;\approx\; \rho\, n^2 u,$$
> donde $\rho$ es el **factor de crecimiento** de los elementos durante la eliminación. El error hacia adelante hereda entonces el [[Condicionamiento Numerico Numero Condicion|condicionamiento]]:
> $$\frac{\|\tilde x - x\|}{\|x\|} \lesssim \kappa(A)\, \rho\, n^2 u.$$

> [!info]
> Esta es la manifestación matricial de la regla **forward $\lesssim$ condición $\times$ backward**: el algoritmo aporta el factor $\rho\,n^2 u$ (error hacia atrás), el problema aporta $\kappa(A)$. Con pivoteo parcial $\rho$ es típicamente $O(1)$, y la resolución es estable a efectos prácticos.

---

## Acumulación lineal, no exponencial

> [!proposicion]
> Para los algoritmos estándar del álgebra lineal numérica, el error hacia atrás crece **polinomialmente** en $n$ (factores $\gamma_n, n\gamma_n, \dots$), no exponencialmente. La excepción es la eliminación sin pivoteo, donde $\rho$ puede crecer como $2^{n-1}$.

> [!info]
> Las cotas con $\gamma_n$ son pesimistas: suponen que todos los errores se alinean en la misma dirección. En la práctica los $\delta_i$ tienen signos aleatorios y el error efectivo crece como $\sqrt{n}\,u$ (modelo estadístico de redondeo), no como $n u$. Las cotas garantizan el peor caso; el comportamiento medio es mejor.

---

## Relación con otras notas

> [!info]
> - El modelo $\operatorname{fl}(a\circ b)=(a\circ b)(1+\delta)$ se justifica en [[Representacion Punto Flotante IEEE 754]] y [[Epsilon Maquina y Precision Relativa]].
> - La cancelación que dispara el error absoluto se trata en [[Perdida Significancia y Cancelacion Catastrofica]].
> - El marco forward/backward que da sentido a estas cotas es [[Estabilidad Algoritmos Forward Backward]].
> - El factor $\kappa(A)$ que convierte error hacia atrás en error hacia adelante es el [[Condicionamiento Numerico Numero Condicion|número de condición]].

---

## Resumen

| Operación | Resultado calculado | Cota de error |
|:---|:---|:---|
| Suma vectorial | $(x+y)+e$ | $\|e\| \leq u\|x+y\|$ |
| Producto interno | $(x+\Delta x)^Ty$ | $|\Delta x_i| \leq \gamma_n|x_i|$ |
| Matriz–vector | $(A+\Delta A)x$ | $|\Delta A| \leq \gamma_n|A|$ |
| Matriz–matriz | $AB+E$ | $|E| \leq \gamma_n|A||B|$ |
| Resolver $Ax=b$ | $(A+\Delta A)\tilde x=b$ | $\|\Delta A\|/\|A\| \lesssim \rho n^2 u$ |

> [!corolario]
> Los errores de redondeo en operaciones matriciales se propagan de forma controlada: cada operación elemental contribuye un factor $(1+\delta)$ con $|\delta|\leq u$, y al encadenar $n$ de ellas el error hacia atrás escala como $\gamma_n \approx n u$, nunca exponencialmente (salvo eliminación sin pivoteo). Esto hace estables hacia atrás al producto interno, al producto matriz–vector y a la resolución de sistemas con [[Pivoteo Parcial Total Estabilidad|pivoteo]]. El error hacia adelante observado se obtiene multiplicando por el [[Condicionamiento Numerico Numero Condicion|número de condición]] del problema, cerrando la cadena dato → algoritmo → resultado.
