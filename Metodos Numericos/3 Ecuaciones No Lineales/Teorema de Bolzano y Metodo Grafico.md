---
title: Teorema de Bolzano y Metodo Grafico
order: 1
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-no-lineales
  - localizacion
  - bolzano
draft: false
aliases:
  - Teorema de Bolzano
  - Método gráfico
  - Localización de raíces
---

# Teorema de Bolzano y Método Gráfico

> [!definicion]
> La **localización de raíces** es el proceso de identificar intervalos que contengan raíces de $f(x)=0$ antes de aplicar un método iterativo. Es un paso fundamental para [[Metodos Cerrados Una Variable/index|métodos cerrados]] como bisección o regula falsi.

---

## Teorema de Bolzano (existencia)

> [!teorema]
> Sea $f: [a, b] \to \mathbb{R}$ una función continua en $[a, b]$. Si $f(a) \cdot f(b) < 0$ (es decir, $f(a)$ y $f(b)$ tienen signos opuestos), entonces existe al menos un $c \in (a, b)$ tal que $f(c) = 0$.

> [!demostracion]
> **Paso 1: Construcción de sucesiones por bisección.**
>
> Sin pérdida de generalidad, supóngase $f(a) < 0$ y $f(b) > 0$. Defínanse $a_1 = a$, $b_1 = b$, y $c_1 = \frac{a_1 + b_1}{2}$.
>
> - Si $f(c_1) = 0$, la raíz es $c_1$ y el teorema queda demostrado.
> - Si $f(c_1) > 0$, entonces $f(a_1) < 0$ y $f(c_1) > 0$; se define $a_2 = a_1$, $b_2 = c_1$.
> - Si $f(c_1) < 0$, entonces $f(c_1) < 0$ y $f(b_1) > 0$; se define $a_2 = c_1$, $b_2 = b_1$.
>
> Este proceso genera sucesiones $\{a_k\}$ (creciente y acotada superiormente) y $\{b_k\}$ (decreciente y acotada inferiormente), ambas convergentes.
>
> **Paso 2: Convergencia al mismo límite.**
>
> Por construcción, $b_k - a_k = \frac{b - a}{2^{k-1}}$, por lo tanto:
> $$\lim_{k \to \infty} (b_k - a_k) = 0$$
>
> Como $a_k \leq c \leq b_k$ para algún $c$, se tiene:
> $$\lim_{k \to \infty} a_k = \lim_{k \to \infty} b_k = c$$
>
> **Paso 3: $c$ es raíz.**
>
> Por continuidad de $f$, $\lim_{k \to \infty} f(a_k) = f(c)$ y $\lim_{k \to \infty} f(b_k) = f(c)$. Pero $f(a_k) < 0$ y $f(b_k) > 0$ para todo $k$, por lo tanto:
> $$f(c) \leq 0 \quad \text{y} \quad f(c) \geq 0$$
>
> La única posibilidad es $f(c) = 0$.

> [!warning]
> El teorema garantiza **existencia** pero no unicidad. Puede haber múltiples raíces en $[a, b]$.

---

## Método gráfico

> [!info]
> **Estrategia práctica para localizar raíces.**
>
> 1. **Evaluación sistemática:** Se evalúa $f$ en una malla de puntos $x_0, x_1, \dots, x_m$ y se buscan cambios de signo:
>    $$f(x_i) \cdot f(x_{i+1}) < 0 \quad \Rightarrow \quad \text{raíz en } (x_i, x_{i+1})$$
>
> 2. **Gráfico de $f(x)$:** La forma más directa. Se observa dónde la curva cruza el eje $x$.
>
> 3. **Análisis asintótico:** Para $x \to \pm\infty$, el signo de $f(x)$ está determinado por el término dominante (útil para acotar el dominio de búsqueda).
>
> 4. **Teorema de Sturm:** Para polinomios, permite contar raíces reales en un intervalo sin calcularlas.

> [!ejemplo]
> **Localizar raíces de $f(x) = e^{-x} - \cos(x)$ en $[0, 4]$.**
>
> Evaluación en puntos clave:
>
> | $x$ | $f(x)$ | Signo |
> |:---|:---|:---|
> | 0.0 | 1.0000 - 1.0000 = 0.0000 | raíz exacta |
> | 0.5 | 0.6065 - 0.8776 = -0.2711 | negativo |
> | 1.0 | 0.3679 - 0.5403 = -0.1724 | negativo |
> | 1.5 | 0.2231 - 0.0707 = 0.1524 | positivo |
> | 2.0 | 0.1353 - (-0.4161) = 0.5514 | positivo |
> | 2.5 | 0.0821 - (-0.8011) = 0.8832 | positivo |
> | 3.0 | 0.0498 - (-0.9900) = 1.0398 | positivo |
> | 3.5 | 0.0302 - (-0.9365) = 0.9667 | positivo |
> | 4.0 | 0.0183 - (-0.6536) = 0.6719 | positivo |
>
> **Análisis:**
> - Raíz en $x = 0$ (exacta)
> - Cambio de signo entre $x=1.0$ (negativo) y $x=1.5$ (positivo) → raíz en $(1.0, 1.5)$
> - No hay otros cambios de signo en $[0, 4]$

---

## Multiplicidad de raíces

> [!definicion]
> Sea $r$ una raíz de $f$ tal que $f(r) = 0$. La **multiplicidad** $m$ de $r$ es el mayor entero tal que:
> $$f(r) = f'(r) = \cdots = f^{(m-1)}(r) = 0, \quad f^{(m)}(r) \neq 0$$
>
> - **Raíz simple:** $m = 1$. La función cruza el eje.
> - **Raíz múltiple:** $m \geq 2$. Si $m$ es par, la función toca el eje sin cruzarlo; si $m$ es impar, lo cruza con tangente horizontal.

> [!info]
> **Detección práctica de multiplicidad.**
>
> - Si $f$ cambia de signo en $r$, la multiplicidad es impar.
> - Si $f$ no cambia de signo en $r$, la multiplicidad es par.
> - En métodos numéricos, raíces múltiples causan convergencia lenta en el [[Metodos Abiertos Una Variable/Newton Raphson/index|método de Newton]] (lineal en lugar de cuadrática).

> [!ejemplo]
> - $f(x) = (x-1)^2$: raíz $x=1$ de multiplicidad 2 (par). $f(x) \geq 0$ para todo $x$, no hay cambio de signo.
> - $f(x) = (x-1)^3$: raíz $x=1$ de multiplicidad 3 (impar). $f$ cambia de signo en $x=1$.

---

## Relación con métodos numéricos

> [!info]
> - Una vez localizada una raíz en $[a, b]$ con $f(a)f(b) < 0$, se puede aplicar [[Biseccion|bisección]] o [[Metodos Cerrados Una Variable/Regula Falsi/index|regula falsi]].
> - La precisión de la localización inicial afecta la velocidad de convergencia de los [[Metodos Abiertos Una Variable/index|métodos abiertos]] (Newton, secante).
> - El análisis de multiplicidad es crucial para entender la convergencia de Newton en raíces múltiples.

---

## Resumen

| Concepto | Descripción |
|:---|:---|
| **Teorema de Bolzano** | $f$ continua, $f(a)f(b) < 0 \Rightarrow \exists c \in (a, b): f(c)=0$ |
| **Método gráfico** | Evaluación sistemática para encontrar cambios de signo |
| **Raíz simple** | $f(r)=0$, $f'(r)\neq 0$ → cambio de signo |
| **Raíz múltiple** | $f^{(m)}(r)\neq 0$, $m \geq 2$ → puede o no cambiar signo |

> [!corolario]
> La localización de raíces es el primer paso indispensable en la resolución numérica de ecuaciones no lineales. El teorema de Bolzano garantiza existencia bajo condiciones débiles (continuidad y cambio de signo). El método gráfico (evaluación sistemática) permite identificar intervalos que contienen raíces. Una vez localizadas, se puede proceder con [[Metodos Cerrados Una Variable/index|métodos cerrados]] (bisección, regula falsi) o, si se dispone de una buena aproximación inicial, con [[Metodos Abiertos Una Variable/index|métodos abiertos]] (Newton, secante). El concepto de multiplicidad es fundamental para interpretar el comportamiento de la función cerca de la raíz.