---
title: Formulario — Diferenciación e Integración Numérica
order: 99
tags:
  - metodos-numericos
  - formulario
  - integracion
draft: false
aliases:
  - formulario integracion numerica
  - formulas diferenciacion e integracion
---

# Formulario — Diferenciación e Integración Numérica

## Diferencias finitas (serie de Taylor)

Clave: $h$: paso; $x$: punto; $\xi\in(a,b)$: punto intermedio.

**Desarrollo de Taylor base**
$$f(x+h) = f(x) + hf'(x) + \tfrac{h^2}{2}f''(x) + \tfrac{h^3}{6}f'''(x) + \cdots$$

**Primera derivada — progresiva**
$$\frac{f(x+h)-f(x)}{h} = f'(x) + O(h)$$

**Primera derivada — regresiva**
$$\frac{f(x)-f(x-h)}{h} = f'(x) + O(h)$$

**Primera derivada — centrada**
$$\frac{f(x+h)-f(x-h)}{2h} = f'(x) + \tfrac{h^2}{6}f'''(\xi) = f'(x) + O(h^2)$$

**Primera derivada — centrada 4 puntos**
$$f'(x) \approx \frac{-f(x+2h)+8f(x+h)-8f(x-h)+f(x-2h)}{12h}, \qquad O(h^4)$$

**Segunda derivada — centrada**
$$\frac{f(x+h) - 2f(x) + f(x-h)}{h^2} = f''(x) + \tfrac{h^2}{12}f^{(4)}(\xi) = f''(x) + O(h^2)$$

**Método de coeficientes indeterminados (fórmula general)**
$$f^{(d)}(x) \approx \frac{1}{h^d}\sum_k a_k\, f(x + k h)$$

**Relación con diferencias divididas**
$$f[x_0,x_1] \approx f'$$

---

## Orden de error: progresiva, regresiva, centrada

Clave: $p$: orden de error, $E(h)=O(h^p)$.

**Progresiva (con término de error)**
$$f'(x) = \frac{f(x+h)-f(x)}{h} - \frac{h}{2}f''(\xi)$$

**Regresiva (con término de error)**
$$f'(x) = \frac{f(x)-f(x-h)}{h} + \frac{h}{2}f''(\xi)$$

**Centrada (con término de error)**
$$f'(x) = \frac{f(x+h)-f(x-h)}{2h} - \frac{h^2}{6}f'''(\xi)$$

**Verificación empírica del orden**
$$p \approx \log_2\frac{E(h)}{E(h/2)}$$

**Órdenes por número de puntos**
$$\text{progresiva/regresiva: } O(h); \quad \text{centrada 2 pts: } O(h^2); \quad \text{progresiva 3 pts: } O(h^2); \quad \text{centrada 5 pts: } O(h^4)$$

---

## Extrapolación de Richardson y Romberg

Clave: $A(h)$: aproximación de orden $p$; $q$: salto de orden.

**Expansión de error**
$$A(h) = A + c_p h^p + c_{p+q} h^{p+q} + \cdots$$

**Fórmula de extrapolación**
$$A^{\text{ext}}(h) = \frac{2^p A(h/2) - A(h)}{2^p - 1} = A + O(h^{p+q})$$

**Extrapolación de derivada centrada ($p=2$, $q=2$)**
$$D^{\text{ext}} = \frac{4D(h/2)-D(h)}{3}, \qquad D(h) = \frac{f(h)-f(-h)}{2h}$$

**Tabla de Romberg**
$$R_{k,0} = \text{trapecio con } 2^k \text{ intervalos}, \qquad R_{k,j} = \frac{4^j R_{k,j-1} - R_{k-1,j-1}}{4^j - 1}$$

---

## Inestabilidad y paso óptimo (diferenciación)

Clave: $u$: unidad de redondeo; $M_0=\max|f|$; $M_2=\max|f''|$.

**Error total (diferencia progresiva)**
$$E(h) \lesssim \frac{h}{2}M_2 + \frac{2 u M_0}{h}$$

**Paso óptimo — progresiva ($O(h)$)**
$$h^* = 2\sqrt{\frac{u M_0}{M_2}} \sim \sqrt{u}, \qquad E(h^*) \sim \sqrt{u}$$

**Paso óptimo — centrada ($O(h^2)$)**
$$h^* \sim u^{1/3}, \qquad E(h^*) \sim u^{2/3}$$

**Truco del paso complejo (sin cancelación)**
$$f'(x) \approx \frac{\operatorname{Im}[f(x+ih)]}{h}, \qquad O(h^2)$$

---

## Formulación general de Newton-Cotes

Clave: $x_i = a+ih$: nodos equiespaciados; $h=\frac{b-a}{n}$; $L_i$: polinomios cardinales de Lagrange.

**Fórmula de cuadratura**
$$\int_a^b f(x)\,dx \approx \sum_{i=0}^n w_i f(x_i)$$

**Pesos**
$$w_i = \int_a^b L_i(x)\,dx$$

**Integración del interpolante**
$$\int_a^b f\,dx \approx \int_a^b p_n\,dx = \sum_{i=0}^n f(x_i)\int_a^b L_i(x)\,dx$$

**Error como integral del error de interpolación**
$$\int_a^b f - \int_a^b p_n = \int_a^b \frac{f^{(n+1)}(\xi_x)}{(n+1)!}\prod_i(x-x_i)\,dx$$

**Propiedades: consistencia, simetría, grado de exactitud**
$$\sum_i w_i = b - a, \qquad w_i = w_{n-i}, \qquad \text{grado} = n\ (n\text{ impar}) \text{ o } n+1\ (n\text{ par})$$

**Reglas básicas y pesos** ($h=(b-a)/n$)
$$n=1:\ \tfrac{h}{2}(f_0 + f_1); \quad n=2:\ \tfrac{h}{3}(f_0 + 4f_1 + f_2)$$
$$n=3:\ \tfrac{3h}{8}(f_0 + 3f_1 + 3f_2 + f_3); \quad n=4:\ \tfrac{2h}{45}(7f_0 + 32f_1 + 12f_2 + 32f_3 + 7f_4)$$

---

## Regla del trapecio (cerrada)

Clave: $h=b-a$; $\xi\in(a,b)$.

**Fórmula**
$$\int_a^b f(x)\,dx \approx \frac{h}{2}\big(f(a) + f(b)\big)$$

**Con error de truncamiento** ($f\in C^2$)
$$\int_a^b f(x)\,dx = \frac{h}{2}\big(f(a)+f(b)\big) - \frac{h^3}{12}f''(\xi)$$

Grado de exactitud $1$; signo del error $-\operatorname{sgn}(f'')$.

---

## Regla de Simpson 1/3 (cerrada)

Clave: $h=\frac{b-a}{2}$; nodos $x_0=a$, $x_1=\frac{a+b}{2}$, $x_2=b$.

**Fórmula**
$$\int_a^b f(x)\,dx \approx \frac{h}{3}\big(f_0 + 4f_1 + f_2\big)$$

**Con error de truncamiento** ($f\in C^4$)
$$\int_a^b f(x)\,dx = \frac{h}{3}\big(f_0 + 4f_1 + f_2\big) - \frac{h^5}{90}f^{(4)}(\xi)$$

Grado de exactitud $3$; requiere número par de subintervalos.

---

## Regla de Simpson 3/8 y grado superior (cerradas)

Clave: $h=\frac{b-a}{3}$; nodos $x_0,\dots,x_3$.

**Simpson 3/8**
$$\int_a^b f(x)\,dx \approx \frac{3h}{8}\big(f_0 + 3f_1 + 3f_2 + f_3\big)$$

**Simpson 3/8 con error** ($f\in C^4$)
$$\int_a^b f\,dx = \frac{3h}{8}(f_0 + 3f_1 + 3f_2 + f_3) - \frac{3h^5}{80}f^{(4)}(\xi)$$

**Regla de Boole ($n=4$)**
$$\int_a^b f\,dx = \frac{2h}{45}(7f_0 + 32f_1 + 12f_2 + 32f_3 + 7f_4) - \frac{8h^7}{945}f^{(6)}(\xi)$$

**Combinación 1/3 + 3/8 (número impar de paneles, aquí $n=5$)**
$$\int_{x_0}^{x_5} f \approx \frac{h}{3}(f_0 + 4f_1 + f_2) + \frac{3h}{8}(f_2 + 3f_3 + 3f_4 + f_5)$$

**Errores y grados de exactitud**
$$\text{Trapecio: } -\tfrac{h^3}{12}f'',\ g{=}1; \quad \text{Simpson 1/3: } -\tfrac{h^5}{90}f^{(4)},\ g{=}3; \quad \text{Simpson 3/8: } -\tfrac{3h^5}{80}f^{(4)},\ g{=}3; \quad \text{Boole: } -\tfrac{8h^7}{945}f^{(6)},\ g{=}5$$

---

## Inestabilidad de pesos negativos (grado alto)

Clave: $u$: unidad de redondeo.

**Divergencia de la suma de valores absolutos** ($n\to\infty$)
$$\sum_i |w_i| \to \infty, \qquad \sum_i w_i = b-a$$

**Cota del error de redondeo**
$$E_{\text{redondeo}} \lesssim u\sum_i |w_i|\,\max|f|$$

**Umbral de pesos negativos**
$$n \geq 8 \text{ (cerradas)} \Rightarrow \text{algunos } w_i < 0$$

---

## Trapecio compuesto

Clave: $h=\frac{b-a}{n}$; $n$: número de subintervalos; $f_i=f(x_i)$.

**Fórmula**
$$\int_a^b f(x)\,dx \approx \frac{h}{2}\Big(f_0 + 2\sum_{i=1}^{n-1}f_i + f_n\Big)$$

**Error global** ($f\in C^2$)
$$\int_a^b f\,dx - T_n = -\frac{(b-a)h^2}{12}f''(\xi), \qquad O(h^2)$$

**Fórmula de Euler-Maclaurin**
$$\int_a^b f - T_n = -\frac{h^2}{12}\big[f'(b)-f'(a)\big] - \frac{h^4}{720}\big[f'''(b)-f'''(a)\big] - \cdots$$

**Refinamiento incremental**
$$T_{2n} = \frac{1}{2}T_n + h_{2n}\sum_{\text{nodos nuevos}} f(x_i)$$

---

## Simpson compuesto

Clave: $h=\frac{b-a}{n}$; $n$ par.

**Fórmula**
$$\int_a^b f\,dx \approx \frac{h}{3}\Big(f_0 + 4\!\!\sum_{i\ \text{impar}}\!\!f_i + 2\!\!\sum_{i\ \text{par}}\!\!f_i + f_n\Big)$$

**Error global** ($f\in C^4$)
$$\int_a^b f\,dx - S_n = -\frac{(b-a)h^4}{180}f^{(4)}(\xi), \qquad O(h^4)$$

---

## Fundamentos Gauss-Legendre y polinomios ortogonales

Clave: $P_n$: polinomio de Legendre; nodos = ceros de $P_n$.

**Ortogonalidad**
$$\int_{-1}^1 P_m(x)P_n(x)\,dx = \frac{2}{2n+1}\delta_{mn}$$

**Ortogonalidad a grados menores** ($\deg q < n$)
$$\int_{-1}^1 P_n(x)\,q(x)\,dx = 0$$

**Recurrencia de tres términos**
$$(n+1)P_{n+1}(x) = (2n+1)\,x\,P_n(x) - n\,P_{n-1}(x)$$

**Primeros polinomios**
$$P_0=1,\quad P_1=x,\quad P_2=\tfrac{1}{2}(3x^2-1),\quad P_3=\tfrac{1}{2}(5x^3-3x),\quad P_4=\tfrac{1}{8}(35x^4-30x^2+3)$$

**Ceros (nodos de Gauss)**
$$n{=}2:\ \pm\tfrac{1}{\sqrt3}; \quad n{=}3:\ 0,\ \pm\sqrt{3/5}; \quad n{=}4:\ \pm0.3400,\ \pm0.8611$$

**Idea clave (división por $P_n$)**
$$p = q\,P_n + r, \qquad \int_{-1}^1 p\,dx = \int_{-1}^1 r\,dx$$

**Otras familias**
$$\text{Chebyshev: } w=\tfrac{1}{\sqrt{1-x^2}}; \quad \text{Laguerre: } w=e^{-x} \text{ en } [0,\infty); \quad \text{Hermite: } w=e^{-x^2} \text{ en } (-\infty,\infty)$$

---

## Determinación de nodos y pesos óptimos

Clave: $x_i$: ceros de $P_n$; $w_i$: pesos.

**Peso (forma cerrada)**
$$w_i = \int_{-1}^1 L_i(x)\,dx = \frac{2}{(1-x_i^2)\,[P_n'(x_i)]^2} > 0, \qquad \sum_{i=1}^n w_i = 2$$

**Positividad (aplicar la regla a $L_i^2$)**
$$0 < \int_{-1}^1 L_i^2\,dx = \sum_j w_j L_i(x_j)^2 = w_i$$

**Tabla de nodos y pesos en $[-1,1]$**
$$n{=}1:\ x{=}0,\ w{=}2; \quad n{=}2:\ \pm0.577350,\ w{=}1,1; \quad n{=}3:\ 0,\pm0.774597,\ w{=}0.888889,0.555556$$
$$n{=}4:\ \pm0.339981,\pm0.861136,\ w{=}0.652145,0.347855; \quad n{=}5:\ 0,\pm0.538469,\pm0.906180,\ w{=}0.568889,0.478629,0.236927$$

**Golub-Welsch**
$$\text{nodos} = \text{autovalores de la matriz de Jacobi } J; \qquad w_i = 2\,(v_i^{(1)})^2$$

---

## Grado de exactitud polinómica $2n-1$

Clave: $n$ nodos $\Rightarrow$ exacta para grado $\leq 2n-1$.

**Teorema de exactitud**
$$\int_{-1}^1 p(x)\,dx = \sum_{i=1}^n w_i\, p(x_i) \quad \text{para todo } p \text{ de grado} \leq 2n-1$$

**División base de la prueba**
$$p(x) = q(x)P_n(x) + r(x), \qquad \deg q,\ \deg r \leq n-1$$

**Optimalidad (contraejemplo de grado $2n$)**
$$p(x) = \prod_{i=1}^n (x - x_i)^2, \qquad \sum_i w_i p(x_i) = 0 < \int_{-1}^1 p\,dx$$

**Error de la cuadratura gaussiana** ($f\in C^{2n}$)
$$\int_{-1}^1 f - \sum_i w_i f(x_i) = \frac{2^{2n+1}(n!)^4}{(2n+1)[(2n)!]^3}\,f^{(2n)}(\xi)$$

---

## Comparación de eficiencia frente a Newton-Cotes

Clave: $n$ evaluaciones.

**Grado de exactitud por número de evaluaciones**
$$\text{Newton-Cotes: } \sim n; \qquad \text{Gauss: } 2n-1$$

---

## Cambio de variable a intervalo general

Clave: $t\in[-1,1]$: variable de referencia; $t_i,w_i$: nodos/pesos tabulados.

**Cambio de variable afín**
$$x = \frac{b-a}{2}\,t + \frac{a+b}{2}, \qquad dx = \frac{b-a}{2}\,dt$$

**Cuadratura de Gauss-Legendre en $[a,b]$**
$$\int_a^b f(x)\,dx \approx \frac{b-a}{2}\sum_{i=1}^n w_i\, f\!\left(\frac{b-a}{2}t_i + \frac{a+b}{2}\right)$$

**Gauss compuesto**
$$\int_a^b f\,dx \approx \sum_k \frac{c_{k+1}-c_k}{2}\sum_i w_i\, f(\cdots)$$

**Intervalos infinitos**
$$\int_0^\infty e^{-x}f(x)\,dx \to \text{Gauss-Laguerre}; \quad \int_{-\infty}^\infty e^{-x^2}f(x)\,dx \to \text{Gauss-Hermite}; \quad x = \tfrac{t}{1-t} \text{ a } [0,1)$$
