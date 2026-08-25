---
title: Formulario — Teoría de Errores, Análisis y Estabilidad
order: 99
tags:
  - metodos-numericos
  - formulario
  - errores
draft: true
aliases:
  - formulario errores
  - formulas teoria de errores
---

# Formulario — Teoría de Errores, Análisis y Estabilidad

## Representación en Punto Flotante IEEE 754

**Valor de un número flotante.**
$$x = (-1)^s \cdot (1 + f) \cdot 2^{e - \text{sesgo}}$$
$s\in\{0,1\}$: bit de signo; $e$: exponente sesgado; $f$: fracción del significando; $\text{sesgo}$: constante de la precisión.

**Fracción almacenada.**
$$f = b_1 2^{-1} + b_2 2^{-2} + \dots + b_{p-1} 2^{-(p-1)}$$
$p$: precisión ($24$ simple, $53$ doble); $b_i\in\{0,1\}$: bits de la mantisa.

**Espaciado en rango normalizado.** $1 \leq e \leq 2^k-2$, significando efectivo $M = 1.f$.

**Cota del error de redondeo al representar.**
$$\frac{|x - \text{fl}(x)|}{|x|} \leq u$$
$u$: unidad de redondeo; para doble, $u = 2^{-52} \approx 2.22 \times 10^{-16}$.

**No-asociatividad.**
$$(a + b) + c \neq a + (b + c)$$

**Parámetros de los formatos.**

| Parámetro | binary32 | binary64 |
| :-- | :-: | :-: |
| Bits totales | $32$ | $64$ |
| Signo $s$ | $1$ | $1$ |
| Exponente $e$ | $8$ | $11$ |
| Mantisa $f$ | $23$ | $52$ |
| Sesgo | $127$ | $1023$ |

---

## Épsilon de Máquina y Precisión Relativa $u$

**Definición operativa.**
$$\text{fl}(1 + \varepsilon_{\text{mach}}) > 1$$
$\varepsilon_{\text{mach}}=u$: menor positivo tal que $1+u$ es distinto de $1$.

**Valor en binary64.**
$$u = 2^{-52} \approx 2.220446049250313 \times 10^{-16}$$

**Valor en binary32.**
$$u = 2^{-23} \approx 1.1920928955078125 \times 10^{-7}$$

**Espaciado entre flotantes consecutivos en $[2^E, 2^{E+1})$.**
$$\Delta x = 2^{E - (p - 1)}$$
$E$: exponente real; $p$: precisión.

**Épsilon de máquina en función de la precisión.**
$$u = 2^{0 - (p - 1)} = 2^{-(p - 1)}$$

**Cota del error relativo de redondeo.**
$$\frac{|x - \text{fl}(x)|}{|x|} \leq u \qquad\Longleftrightarrow\qquad \text{fl}(x) = x(1 + \delta),\ \ |\delta| \leq u$$

**Modelo estándar del error de redondeo.**
$$\text{fl}(x \circ y) = (x \circ y)(1 + \delta), \quad |\delta| \leq u$$
$\circ \in \{+, -, \times, \div\}$; redondeo *round to nearest, ties to even*.

**Dígitos decimales de precisión.**
$$\text{dígitos} \approx -\log_{10}(u) \approx 16 \ \ (\text{doble})$$

**Límite de crecimiento del error.**
$$\text{error} \sim O(u \cdot \kappa)$$
$\kappa$: número de condición del problema.

---

## Pérdida de Significancia y Cancelación Catastrófica

**Operandos con error de redondeo.**
$$\tilde{a} = a(1 + \delta_a), \quad \tilde{b} = b(1 + \delta_b), \quad |\delta_a|, |\delta_b| \leq u$$

**Diferencia de operandos con error.**
$$\tilde{a} - \tilde{b} = (a - b) + (a\delta_a - b\delta_b)$$

**Error relativo de la diferencia.**
$$\frac{|(\tilde{a} - \tilde{b}) - (a - b)|}{|a - b|} = \frac{|a\delta_a - b\delta_b|}{|a - b|}$$

**Factor de amplificación (cancelación).**
$$\approx \frac{|a|}{|a - b|} \gg 1 \quad \text{si } a \approx b$$

**Fórmula cuadrática estándar (inestable para la raíz pequeña).**
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

**Función con cancelación cerca de $x=0$.**
$$f(x) = \frac{1 - \cos x}{x^2}$$

**Reformulación estable (identidad trigonométrica).**
$$1 - \cos x = 2 \sin^2\!\left(\tfrac{x}{2}\right) \quad\Longrightarrow\quad f(x) = 2\left(\frac{\sin(x/2)}{x}\right)^2$$

**Serie alternante.**
$$S = \sum_{k=1}^{\infty} \frac{(-1)^{k+1}}{k} = \ln 2 \approx 0.6931471805599453$$

**Racionalización de $\sqrt{x+1}-\sqrt{x}$ (estable).**
$$f(x) = \sqrt{x+1} - \sqrt{x} = \frac{(x+1) - x}{\sqrt{x+1} + \sqrt{x}} = \frac{1}{\sqrt{x+1} + \sqrt{x}}$$

**Varianza — fórmula de una pasada (inestable).**
$$\sigma^2 = \frac{1}{n}\sum x_i^2 - \left(\frac{1}{n}\sum x_i\right)^2$$

**Varianza — fórmula de dos pasadas (estable).**
$$\sigma^2 = \frac{1}{n}\sum (x_i - \bar{x})^2$$
$\bar{x}$: media de los datos.

---

## Condicionamiento Numérico y Número de Condición $\kappa(A)$

**Número de condición de una matriz.**
$$\kappa(A) = \|A\| \cdot \|A^{-1}\|$$
$\|\cdot\|$: norma matricial inducida; $\kappa(A)=\infty$ si $A$ singular.

**Número de condición espectral.**
$$\kappa_2(A) = \frac{\sigma_{\max}(A)}{\sigma_{\min}(A)}$$
$\sigma_{\max},\sigma_{\min}$: valores singulares máximo y mínimo de $A$.

**Sensibilidad ante perturbaciones en $b$.**
$$\frac{\|\Delta x\|}{\|x\|} \leq \kappa(A) \cdot \frac{\|\Delta b\|}{\|b\|}$$

**Sensibilidad ante perturbaciones en $A$.**
$$\frac{\|\Delta x\|}{\|x\|} \leq \frac{\kappa(A)}{1 - \kappa(A)\frac{\|\Delta A\|}{\|A\|}} \cdot \frac{\|\Delta A\|}{\|A\|}$$
Válida si $\|\Delta A\| < 1/\|A^{-1}\|$; para $\|\Delta A\|\to 0$ tiende a $\kappa(A)\frac{\|\Delta A\|}{\|A\|}$.

**Propiedades.**
$$\kappa(A) \geq 1, \qquad \kappa(\alpha A) = \kappa(A)\ (\alpha \neq 0), \qquad \kappa_2(A)=1 \text{ si } A^T A = I$$

**Equivalencia de normas.**
$$c_1 \kappa_\alpha(A) \leq \kappa_\beta(A) \leq c_2 \kappa_\alpha(A), \quad c_1,c_2 > 0$$

**Interpretación geométrica.**
$$\kappa_2(A) = \frac{\sigma_1}{\sigma_n}, \qquad \sigma_1 \geq \sigma_2 \geq \dots \geq \sigma_n > 0$$
$\sigma_i$: semiejes del hiperelipsoide imagen de la esfera unitaria.

**Cota de error para algoritmo estable.**
$$\frac{\|\tilde{x} - x\|}{\|x\|} \lesssim \kappa(A) \cdot u \cdot \rho$$
$\rho$: factor de crecimiento de la eliminación; $u$: unidad de redondeo.

**Regla práctica de dígitos correctos.**
$$\text{dígitos correctos} \approx -\log_{10}(u) - \log_{10}(\kappa(A))$$

**Estimador de Skeel.**
$$\kappa_S(A) = \big\| \,|A^{-1}| \cdot |A|\, \big\|_\infty$$

**Convergencia del gradiente conjugado.**
$$\frac{\|x_k - x^*\|_A}{\|x_0 - x^*\|_A} \leq 2 \left( \frac{\sqrt{\kappa_2(A)} - 1}{\sqrt{\kappa_2(A)} + 1} \right)^k$$

**Precondicionamiento.**
$$\kappa_2(M^{-1}A) \ll \kappa_2(A), \qquad M \approx A$$

**Número de condición por tipo de problema.**

| Problema | $\kappa$ |
| :-- | :-- |
| Evaluación de $f(x)$ | $\kappa_f(x) = \left\| \dfrac{x\, f'(x)}{f(x)} \right\|$ |
| Raíz simple de $f(x)=0$ | $\kappa = 1/\|f'(r)\|$ |
| Interpolación polinómica | $\kappa \approx$ condición de la matriz de Vandermonde |
| PVI de EDO | $\kappa \approx e^{L t}$ ($L$: constante de Lipschitz) |
| Mínimos cuadrados | $\kappa(A^T A) = [\kappa_2(A)]^2$ |

**Condicionamiento de mínimos cuadrados.**
$$\kappa_{\text{LS}}(A) = \kappa_2(A) + \frac{\kappa_2(A)^2 \cdot \|r\|_2}{\|A\|_2 \cdot \|x\|_2}$$
$r = b - Ax$: residuo.

---

## Estabilidad de Algoritmos (Forward y Backward)

**Error hacia adelante (*forward*).**
$$\frac{\|\tilde y - y\|}{\|y\|}$$
$y=f(x)$: resultado exacto; $\tilde y$: resultado calculado.

**Error hacia atrás (*backward*).**
$$\tilde y = f(x + \Delta x), \qquad \text{error hacia atrás} = \frac{\|\Delta x\|}{\|x\|}$$

**Relación fundamental (regla de oro).**
$$\frac{\|\tilde y - y\|}{\|y\|} \;\lesssim\; \kappa \cdot \frac{\|\Delta x\|}{\|x\|}$$
$\kappa$: número de condición del problema.

**Número de condición (forma diferencial).**
$$\kappa = \frac{\|x\|\,\|f'(x)\|}{\|f(x)\|}$$

**Estable hacia atrás.**
$$\tilde y = f(x+\Delta x), \qquad \frac{\|\Delta x\|}{\|x\|} = O(u)$$

**Estable hacia adelante.**
$$\frac{\|\tilde y - y\|}{\|y\|} = O(\kappa\, u)$$

**Implicación.**
$$\text{backward stable} \Rightarrow \text{forward stable}$$

**Suma en coma flotante (backward stable).**
$$\tilde s = (a + b)(1 + \delta) = a(1+\delta) + b(1+\delta) = \tilde a + \tilde b, \qquad |\delta| \leq u$$

**Producto interno (backward stable).**
$$\tilde s = \sum_{i=1}^n x_i y_i (1 + \theta_i), \qquad |\theta_i| \leq \gamma_n = \frac{n u}{1 - n u} \approx n u$$

**Fórmula cuadrática estable (Vieta).**
$$x_1 = \frac{-b - \operatorname{sgn}(b)\sqrt{b^2-4ac}}{2a}, \qquad x_2 = \frac{c}{a\,x_1}$$

**Eliminación gaussiana con pivoteo parcial.**
$$\|\Delta A\| \lesssim \rho\, n\, u\, \|A\|, \qquad \rho = O(1)\ \text{(en la práctica)},\ \ \rho \leq 2^{n-1}\ \text{(peor caso)}$$

---

## Propagación de Errores en Operaciones Matriciales

**Modelo estándar de aritmética flotante.**
$$\operatorname{fl}(a \circ b) = (a \circ b)(1 + \delta), \qquad |\delta| \leq u$$
$\circ \in \{+, -, \times, /\}$.

**Constante de cadenas de $n$ operaciones.**
$$\gamma_n = \frac{n u}{1 - n u} \approx n u \qquad (n u < 1)$$

**Producto escalar–vector.**
$$\operatorname{fl}(\alpha x) = \alpha x + e, \qquad \|e\|_\infty \leq u\,|\alpha|\,\|x\|_\infty$$

**Suma de vectores.**
$$\operatorname{fl}(x + y) = (x + y) + e, \qquad \|e\|_\infty \leq u\,\|x + y\|_\infty$$

**Producto interno.**
$$\operatorname{fl}(x^T y) = (x + \Delta x)^T y, \qquad |\Delta x_i| \leq \gamma_n |x_i|$$
$$|\operatorname{fl}(x^Ty) - x^Ty| \leq \gamma_n \sum_i |x_i||y_i| = \gamma_n |x|^T|y|$$

**Producto matriz–vector.**
$$\operatorname{fl}(Ax) = (A + \Delta A)x, \qquad |\Delta A| \leq \gamma_n |A|$$

**Producto matriz–matriz.**
$$\operatorname{fl}(AB) = AB + E, \qquad |E| \leq \gamma_n |A||B|$$

**Recurrencia del producto interno.**
$$\tilde s_1 = x_1 y_1 (1 + \delta_1), \qquad \tilde s_k = \big(\tilde s_{k-1} + x_k y_k (1 + \delta_k)\big)(1 + \varepsilon_k), \quad |\delta_i|,|\varepsilon_i| \leq u$$

**Cota de producto de factores.**
$$\prod_{j}(1+\eta_j) = 1 + \theta, \qquad |\theta| \leq \gamma_n \quad (\leq n \text{ factores})$$

**Asociatividad rota.**
$$\operatorname{fl}(\operatorname{fl}(a+b)+c) \neq \operatorname{fl}(a+\operatorname{fl}(b+c))$$

**Resolución de $Ax=b$ con pivoteo parcial.**
$$(A + \Delta A)\,\tilde x = b, \qquad \frac{\|\Delta A\|_\infty}{\|A\|_\infty} \leq \rho\, n\, \gamma_n \approx \rho\, n^2 u$$

**Error hacia adelante heredado.**
$$\frac{\|\tilde x - x\|}{\|x\|} \lesssim \kappa(A)\, \rho\, n^2 u$$

**Modelo estadístico de redondeo (comportamiento medio).**
$$\text{error efectivo} \sim \sqrt{n}\,u$$
