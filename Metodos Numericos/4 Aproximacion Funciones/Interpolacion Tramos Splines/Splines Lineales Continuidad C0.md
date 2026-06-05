---
title: Splines Lineales y Continuidad C⁰
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - splines
draft: false
aliases:
  - Splines lineales
  - Interpolación lineal a tramos
  - Linear spline
  - Continuidad C0
---

# Splines Lineales y Continuidad $C^0$

> [!definicion]
> Un **spline lineal** interpola los datos $\{(x_i, y_i)\}_{i=0}^n$ uniendo puntos consecutivos con segmentos de recta. En cada subintervalo $[x_i, x_{i+1}]$,
> $$S_i(x) = y_i + \frac{y_{i+1} - y_i}{x_{i+1} - x_i}(x - x_i), \qquad x \in [x_i, x_{i+1}].$$

> [!info]
> Es el spline más simple: continuo ($C^0$) pero no derivable en los nodos (tiene "esquinas"). Su virtud es la robustez total —nunca oscila ni sobrepasa los datos— a costa de poca suavidad. Es la base de la integración por [[Trapecio Error Truncamiento Segunda Derivada|regla del trapecio]].

---

## Propiedades

> [!proposicion]
> 1. **Continuidad $C^0$:** $S$ es continua, $S(x_i) = y_i$, pero $S'$ salta en los nodos internos.
> 2. **Localidad:** cada segmento depende solo de dos datos; modificar un $y_i$ afecta solo a los dos tramos adyacentes.
> 3. **Sin oscilación:** $S$ está acotada entre $\min y_i$ y $\max y_i$ (no hay *overshoot*), inmune al [[Fenomeno Runge y Nodos Chebyshev|fenómeno de Runge]].
> 4. **Construcción $O(n)$:** sin resolver sistemas; cada pendiente es una diferencia dividida de orden 1.

---

## Ejemplo

> [!ejemplo]
> **Datos $(0,0), (1,1), (2,0), (3,1)$.** Spline lineal:
>
> | Tramo | $S_i(x)$ |
> |:---|:---|
> | $[0,1]$ | $x$ |
> | $[1,2]$ | $1 - (x-1) = 2 - x$ |
> | $[2,3]$ | $0 + (x-2) = x - 2$ |
>
> Continuo en $x=1,2$ pero con cambio de pendiente: $S'(1^-) = 1$, $S'(1^+) = -1$. Las esquinas son visibles.

---

## Error de aproximación

> [!teorema]
> Si $f \in C^2[a,b]$ y $h = \max_i (x_{i+1}-x_i)$, el spline lineal interpolante satisface
> $$\max_{[a,b]}|f(x) - S(x)| \leq \frac{h^2}{8}\,\max_{[a,b]}|f''(x)|.$$

> [!demostracion]
> En cada tramo $[x_i, x_{i+1}]$, $S_i$ es el [[Error Interpolacion Formula Cauchy|interpolador]] lineal de $f$. Por la fórmula de Cauchy con $n=1$,
> $$f(x) - S_i(x) = \frac{f''(\xi)}{2}(x - x_i)(x - x_{i+1}).$$
> El factor $|(x-x_i)(x-x_{i+1})|$ alcanza su máximo $h_i^2/4$ en el punto medio. Luego $|f - S_i| \leq \frac{h_i^2}{8}\max|f''|$, y tomando $h = \max h_i$ se obtiene la cota global. Convergencia $O(h^2)$.

---

## Ventajas y limitaciones

> [!info]
> **Ventajas.** Trivial de construir ($O(n)$), local, sin oscilación, base de la integración por trapecios y de gráficos rápidos.

> [!warning]
> **Limitaciones.**
> - **No suave:** las esquinas hacen $S' $ discontinua; inadecuado donde se requiere derivada (velocidad, curvatura).
> - **Convergencia solo $O(h^2)$:** para alta precisión hace falta $h$ muy pequeño. Los [[Splines Cubicos Naturales Sujetos|splines cúbicos]] dan $O(h^4)$ con la misma malla.
> - La derivada numérica de un spline lineal es constante a tramos (escalonada), mala aproximación de $f'$.

---

## Relación con otras notas

> [!info]
> - La versión suave que corrige las esquinas: [[Splines Cubicos Naturales Sujetos]].
> - La comparación de convergencia: [[Convergencia y Estabilidad vs Polinomios Grado Alto]].
> - Su integración da la [[Trapecio Error Truncamiento Segunda Derivada|regla del trapecio]].
> - Panorama: [[Interpolacion Tramos Splines/index]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Definición | rectas por tramos, $S(x_i)=y_i$ |
| Continuidad | $C^0$ (esquinas) |
| Construcción | $O(n)$, sin sistema |
| Error | $\frac{h^2}{8}\max|f''|$, $O(h^2)$ |
| Oscilación | ninguna |
| Limitación | no derivable en nodos |

> [!corolario]
> El spline lineal une los datos con segmentos rectos: continuo $C^0$, local, de construcción inmediata en $O(n)$ y completamente inmune a la oscilación, pero con esquinas en los nodos y convergencia solo $O(h^2)$. Es la interpolante más robusta y la base de la regla del [[Trapecio Error Truncamiento Segunda Derivada|trapecio]]. Cuando se necesita suavidad (derivadas continuas) o mayor orden de convergencia, se asciende a los [[Splines Cubicos Naturales Sujetos|splines cúbicos]] $C^2$.
