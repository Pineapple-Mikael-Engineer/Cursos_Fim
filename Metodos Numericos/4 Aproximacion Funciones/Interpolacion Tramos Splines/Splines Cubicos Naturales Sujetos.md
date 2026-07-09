---
title: Splines Cúbicos Naturales y Sujetos
order: 2
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - splines
draft: false
aliases:
  - Splines cúbicos
  - Spline natural
  - Spline sujeto
  - Cubic spline
---

# Splines Cúbicos: Naturales y Sujetos

> [!definicion]
> Un **spline cúbico** interpolante es una función $S \in C^2[a,b]$ que en cada subintervalo $[x_i, x_{i+1}]$ es un polinomio cúbico $S_i$, con $S(x_i) = y_i$ y empalmes de primera y segunda derivada continuos en los nodos internos.

> [!info]
> Es el spline de uso estándar: suficientemente suave ($C^2$) para parecer una curva continua sin esquinas ni cambios bruscos de curvatura, y de [[Convergencia y Estabilidad vs Polinomios Grado Alto|convergencia]] $O(h^4)$. Las condiciones de frontera —natural o sujeto— cierran los grados de libertad sobrantes.

---

## Grados de libertad y condiciones

> [!teoria]
> Con $n$ subintervalos hay $n$ cúbicas, $4n$ coeficientes. Las condiciones disponibles:
> - Interpolación: $2n$ ($S_i(x_i)=y_i$, $S_i(x_{i+1})=y_{i+1}$).
> - Continuidad $C^1$ y $C^2$ en los $n-1$ nodos internos: $2(n-1)$.
>
> Total $4n - 2$ condiciones para $4n$ incógnitas: faltan **2**, que aportan las condiciones de frontera.

> [!info]
> | Tipo de frontera | Condición | Cuándo usar |
> |:---|:---|:---|
> | **Natural** | $S''(x_0) = S''(x_n) = 0$ | sin información de pendiente en extremos |
> | **Sujeto** (*clamped*) | $S'(x_0) = f'(a)$, $S'(x_n) = f'(b)$ | se conocen las derivadas en los extremos |
> | **Not-a-knot** | $S'''$ continua en $x_1$ y $x_{n-1}$ | por defecto en software (p. ej. MATLAB) |

---

## Construcción

> [!teorema]
> Sea $S$ un spline cúbico interpolante y definamos
> $$
> M_i=S''(x_i),\qquad h_i=x_{i+1}-x_i.
> $$
>
> Entonces las condiciones de continuidad de $S'$ y $S''$ en los nodos interiores implican que los momentos $M_i$ satisfacen el sistema lineal tridiagonal
> $$
> h_{i-1}M_{i-1}
> +2(h_{i-1}+h_i)M_i
> +h_iM_{i+1}
> =
> 6\left(
> \frac{y_{i+1}-y_i}{h_i}
> -
> \frac{y_i-y_{i-1}}{h_{i-1}}
> \right),
> $$
> para $i=1,\dots,n-1$.
>
> Una vez determinados los $M_i$, cada tramo cúbico queda completamente determinado.


> [!demostracion]
> Cada tramo $S_i(x)$ es un polinomio cúbico. En lugar de expresar sus cuatro coeficientes directamente, resulta más conveniente describirlo mediante los valores conocidos
> $$
> S_i(x_i)=y_i,\qquad
> S_i(x_{i+1})=y_{i+1},
> $$
> y las segundas derivadas en los extremos,
> $$
> M_i=S''(x_i),
> \qquad
> M_{i+1}=S''(x_{i+1}).
> $$
>
> Estas cuatro cantidades determinan de manera única el tramo cúbico (véase [[Condiciones Continuidad C2 y Sistema Tridiagonal]]).
>
> Al derivar la expresión obtenida para $S_i(x)$ y evaluar en los extremos del intervalo se obtienen fórmulas para $S_i'(x_i)$ y $S_i'(x_{i+1})$ en función de $M_i$, $M_{i+1}$, $y_i$, $y_{i+1}$ y $h_i$.
>
> En cada nodo interior $x_i$ concurren dos tramos consecutivos, $S_{i-1}$ y $S_i$. Como el spline pertenece a $C^1$, debe cumplirse
> $$
> S_{i-1}'(x_i)=S_i'(x_i).
> $$
>
> Sustituyendo las expresiones de ambas derivadas y simplificando se obtiene
> $$
> h_{i-1}M_{i-1}
> +2(h_{i-1}+h_i)M_i
> +h_iM_{i+1}
> =
> 6\left(
> \frac{y_{i+1}-y_i}{h_i}
> -
> \frac{y_i-y_{i-1}}{h_{i-1}}
> \right),
> $$
> para cada nodo interior.
>
> Como existen $n-1$ nodos interiores, se obtienen $n-1$ ecuaciones lineales. Las dos ecuaciones restantes provienen de las [[Condiciones de Frontera Splines|condiciones de frontera]] (natural, sujeto o *not-a-knot*), completando así el sistema para determinar todos los momentos $M_i$.

> [!tip]
> La incógnita del problema **no son los coeficientes de cada cúbica**, sino los valores
> $$
> M_i=S''(x_i).
> $$
> Una vez conocidos estos "momentos", la expresión de cada polinomio cúbico se obtiene directamente. Gracias a ello, el problema pasa de resolver $4n$ coeficientes a resolver un sistema tridiagonal de solo $n+1$ incógnitas.

> [!info]
> Las condiciones de frontera fijan las ecuaciones primera y última: natural impone $M_0 = M_n = 0$; sujeto añade ecuaciones con $f'(a), f'(b)$. El detalle del montaje está en [[Condiciones Continuidad C2 y Sistema Tridiagonal]].

---

## Ejemplo

> [!ejemplo]
> **Spline cúbico natural por $(0,0), (1,1), (2,0)$** ($h_0=h_1=1$). Una sola ecuación interna ($i=1$) con $M_0=M_2=0$:
> $$2(1+1)M_1 = 6\left(\frac{0-1}{1} - \frac{1-0}{1}\right) = -12 \;\Rightarrow\; M_1 = -3.$$
> Reconstruyendo:
> $$S_0(x) = -\tfrac{1}{2}x^3 + \tfrac{3}{2}x \ \text{en } [0,1], \qquad S_1(x) = \tfrac{1}{2}(x-2)^3\cdot? \ \dots$$
> Verificación de continuidad: $S(0)=0$, $S(1)=1$, $S(2)=0$, con $S''(0)=S''(2)=0$ y $S', S''$ continuas en $x=1$. La curva es una "joroba" suave sin esquinas.

---

## Error de aproximación

> [!teorema]
> Para $f \in C^4[a,b]$ y spline cúbico **sujeto** con $h = \max h_i$:
> $$\max_{[a,b]}|f - S| \leq \frac{5}{384}\,h^4\,\max_{[a,b]}|f^{(4)}|, \qquad \max|f' - S'| = O(h^3), \qquad \max|f'' - S''| = O(h^2).$$
> Convergencia $O(h^4)$ en valor, frente al $O(h^2)$ de los [[Splines Lineales Continuidad C0|splines lineales]].

> [!warning]
> El spline **natural** pierde precisión cerca de los extremos (solo $O(h^2)$ allí) porque $S''=0$ no suele coincidir con $f''$. El spline **sujeto** mantiene $O(h^4)$ global si se conocen las derivadas de frontera; *not-a-knot* es el compromiso por defecto sin esa información.

---

## Relación con otras notas

> [!info]
> - El sistema lineal que se resuelve para construirlo: [[Condiciones Continuidad C2 y Sistema Tridiagonal]].
> - La propiedad variacional que lo caracteriza: [[Propiedad Minima Curvatura]].
> - La comparación con polinomios de grado alto: [[Convergencia y Estabilidad vs Polinomios Grado Alto]].
> - El caso $C^0$ más simple: [[Splines Lineales Continuidad C0]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Definición | cúbicas a tramos, $C^2$ |
| Grados de libertad faltantes | 2 (condiciones de frontera) |
| Natural | $S''=0$ en extremos |
| Sujeto | $S'=f'$ en extremos |
| Sistema | tridiagonal en $M_i = S''(x_i)$, $O(n)$ |
| Error | $\frac{5}{384}h^4\max\|f^{(4)}\|$ (sujeto) |

> [!corolario]
> El spline cúbico es la interpolante $C^2$ por tramos de uso estándar: $n$ cúbicas con $4n-2$ condiciones de interpolación y continuidad, cerradas por dos condiciones de frontera (natural $S''=0$, sujeto $S'=f'$, o not-a-knot). Su construcción se reduce a un [[Condiciones Continuidad C2 y Sistema Tridiagonal|sistema tridiagonal]] diagonal dominante para las segundas derivadas, resoluble en $O(n)$, y alcanza convergencia $O(h^4)$ (sujeto). Suave, estable y de mínima curvatura, es la respuesta directa al [[Fenomeno Runge y Nodos Chebyshev|fenómeno de Runge]] de los polinomios de grado alto.
