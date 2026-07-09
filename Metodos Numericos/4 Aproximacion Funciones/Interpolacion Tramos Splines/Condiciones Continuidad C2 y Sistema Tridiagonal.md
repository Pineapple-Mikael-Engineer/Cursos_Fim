---
title: Condiciones de Continuidad C² y Sistema Tridiagonal
order: 3
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - splines
  - sistemas-lineales
draft: false
aliases:
  - Sistema tridiagonal de splines
  - Continuidad C2
  - Momentos del spline
  - Tridiagonal spline system
---

# Condiciones de Continuidad $C^2$ y Sistema Tridiagonal

> [!definicion]
> La construcción del [[Splines Cubicos Naturales Sujetos|spline cúbico]] reduce las condiciones de continuidad $C^2$ a un **sistema lineal tridiagonal** para los momentos $M_i = S''(x_i)$ (segundas derivadas en los nodos). Una vez conocidos los $M_i$, cada tramo cúbico queda determinado.

> [!info]
> El sistema es **tridiagonal, simétrico y diagonal dominante**, por lo que se resuelve en $O(n)$ con el algoritmo de Thomas (eliminación gaussiana sin pivoteo, estable aquí). Es el paso computacional central de la interpolación por splines.

---

## Derivación del sistema

> [!teoria]
> Cada tramo del spline es un polinomio cúbico, por lo que podría escribirse como
> $$
> S_i(x)=a_i+b_i(x-x_i)+c_i(x-x_i)^2+d_i(x-x_i)^3.
> $$
> Esto introduce $4n$ coeficientes desconocidos.
>
> Una formulación mucho más conveniente consiste en tomar como incógnitas los **momentos**
> $$
> M_i=S''(x_i),
> $$
> es decir, las segundas derivadas en los nodos. Como la segunda derivada de una cúbica es un polinomio lineal, cada tramo puede reconstruirse completamente a partir de los valores $M_i$, $M_{i+1}$ y de los datos de interpolación.

> [!lema]
> En cada intervalo $[x_i,x_{i+1}]$, la segunda derivada del spline viene dada por
> $$
> S_i''(x)
> =
> M_i\frac{x_{i+1}-x}{h_i}
> +
> M_{i+1}\frac{x-x_i}{h_i},
> \qquad
> h_i=x_{i+1}-x_i.
> $$

> [!demostracion]
> Como $S_i$ es un polinomio cúbico, $S_i''$ tiene grado uno; por tanto, debe ser una función lineal.
>
> Además,
> $$
> S_i''(x_i)=M_i,
> \qquad
> S_i''(x_{i+1})=M_{i+1}.
> $$
>
> La única función lineal que toma esos valores en los extremos del intervalo es la interpolación lineal entre ambos puntos, es decir,
> $$
> S_i''(x)
> =
> M_i\frac{x_{i+1}-x}{h_i}
> +
> M_{i+1}\frac{x-x_i}{h_i}.
> $$

> [!teorema]
> Sean
> $$
> M_i=S''(x_i),
> \qquad
> h_i=x_{i+1}-x_i.
> $$
> Entonces los momentos satisfacen el sistema
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

> [!demostracion]
> Del lema anterior sabemos que
> $$
> S_i''(x)
> =
> M_i\frac{x_{i+1}-x}{h_i}
> +
> M_{i+1}\frac{x-x_i}{h_i},
> \qquad
> h_i=x_{i+1}-x_i.
> $$
>
> Integrando una vez respecto de $x$,
> $$
> S_i'(x)
> =
> -M_i\frac{(x_{i+1}-x)^2}{2h_i}
> +
> M_{i+1}\frac{(x-x_i)^2}{2h_i}
> +
> C_1,
> $$
> donde $C_1$ es una constante de integración.
>
> Integrando nuevamente,
> $$
> S_i(x)
> =
> \frac{M_i(x_{i+1}-x)^3}{6h_i}
> +
> \frac{M_{i+1}(x-x_i)^3}{6h_i}
> +
> C_1x
> +
> C_2,
> $$
> siendo $C_2$ otra constante.
>
> Las condiciones de interpolación
> $$
> S_i(x_i)=y_i,
> \qquad
> S_i(x_{i+1})=y_{i+1},
> $$
> permiten determinar $C_1$ y $C_2$. Sustituyendo estos valores se obtiene la expresión clásica del tramo cúbico:
> $$
> S_i(x)
> =
> \frac{M_i(x_{i+1}-x)^3+M_{i+1}(x-x_i)^3}{6h_i}
> +
> \left(
> \frac{y_i}{h_i}
> -
> \frac{M_ih_i}{6}
> \right)
> (x_{i+1}-x)
> +
> \left(
> \frac{y_{i+1}}{h_i}
> -
> \frac{M_{i+1}h_i}{6}
> \right)
> (x-x_i).
> $$
>
> Derivando esta expresión,
> $$
> S_i'(x_i)
> =
> \frac{y_{i+1}-y_i}{h_i}
> -
> \frac{h_i}{6}(2M_i+M_{i+1}),
> $$
> mientras que el tramo anterior verifica
> $$
> S_{i-1}'(x_i)
> =
> \frac{y_i-y_{i-1}}{h_{i-1}}
> +
> \frac{h_{i-1}}{6}(M_{i-1}+2M_i).
> $$
>
> Como el spline pertenece a $C^1$,
> $$
> S_{i-1}'(x_i)=S_i'(x_i).
> $$
>
> Reordenando los términos se obtiene
> $$
> h_{i-1}M_{i-1}
> +
> 2(h_{i-1}+h_i)M_i
> +
> h_iM_{i+1}
> =
> 6\left(
> \frac{y_{i+1}-y_i}{h_i}
> -
> \frac{y_i-y_{i-1}}{h_{i-1}}
> \right),
> $$
> válida para cada nodo interior. Junto con las dos condiciones de frontera, estas ecuaciones determinan todos los momentos $M_i$.
## Estructura tridiagonal

> [!info]
> Las $n-1$ ecuaciones internas forman el sistema
> $$\begin{pmatrix} 2(h_0+h_1) & h_1 & & \\ h_1 & 2(h_1+h_2) & h_2 & \\ & \ddots & \ddots & \ddots \\ & & h_{n-2} & 2(h_{n-2}+h_{n-1}) \end{pmatrix}\!\begin{pmatrix} M_1 \\ M_2 \\ \vdots \\ M_{n-1} \end{pmatrix} = 6\begin{pmatrix} \delta_1 \\ \delta_2 \\ \vdots \\ \delta_{n-1} \end{pmatrix},$$
> con $\delta_i = \frac{y_{i+1}-y_i}{h_i} - \frac{y_i-y_{i-1}}{h_{i-1}}$. Es **estrictamente diagonal dominante** ($2(h_{i-1}+h_i) > h_{i-1}+h_i$), lo que asegura solución única y estabilidad sin pivoteo (véase [[Teorema Diagonal Dominante Estricta]]).

> [!info]
> **Cierre por frontera.** Las dos ecuaciones faltantes vienen de las condiciones de borde:
> - **Natural:** $M_0 = M_n = 0$ (se eliminan del sistema).
> - **Sujeto:** ecuaciones extra que ligan $M_0, M_1$ (y $M_{n-1}, M_n$) con $f'(a), f'(b)$.

> [!proposicion]
> La matriz del sistema es **tridiagonal**, **simétrica** y **estrictamente diagonal dominante**.

> [!demostracion]
> Cada ecuación relaciona únicamente los momentos
> $$
> M_{i-1},
> \qquad
> M_i,
> \qquad
> M_{i+1},
> $$
> por lo que solamente aparecen elementos distintos de cero en la diagonal principal y en las dos diagonales adyacentes; de ahí que la matriz sea tridiagonal.
>
> Además, el coeficiente diagonal vale
> $$
> 2(h_{i-1}+h_i),
> $$
> mientras que la suma de los módulos de los coeficientes fuera de la diagonal es
> $$
> h_{i-1}+h_i.
> $$
>
> Como $h_i>0$ para todo intervalo,
> $$
> 2(h_{i-1}+h_i)
> >
> h_{i-1}+h_i,
> $$
> luego la matriz es estrictamente diagonal dominante. Por el [[Teorema Diagonal Dominante Estricta]], el sistema posee solución única y puede resolverse de forma estable mediante el algoritmo de Thomas.

---

## Algoritmo de Thomas

> [!algoritmo]
> **Resolución tridiagonal $O(n)$** del sistema $a_i M_{i-1} + b_i M_i + c_i M_{i+1} = d_i$:
>
> ```
> # Eliminación hacia adelante
> para i = 2 .. n-1:
>     w = a[i] / b[i-1]
>     b[i] = b[i] - w * c[i-1]
>     d[i] = d[i] - w * d[i-1]
> # Sustitución hacia atrás
> M[n-1] = d[n-1] / b[n-1]
> para i = n-2 .. 1:
>     M[i] = (d[i] - c[i] * M[i+1]) / b[i]
> ```
>
> Coste $O(n)$ en tiempo y memoria, frente al $\frac{2}{3}n^3$ de un sistema denso. Es eliminación gaussiana especializada a la estructura tridiagonal.

---

## Ejemplo

> [!ejemplo]
> **Spline natural, nodos $(0,0),(1,1),(2,0),(3,-1)$**, $h_i=1$. Ecuaciones internas ($i=1,2$) con $M_0=M_3=0$:
> $$\begin{cases} 4M_1 + M_2 = 6(\tfrac{0-1}{1}-\tfrac{1-0}{1}) = -12 \\ M_1 + 4M_2 = 6(\tfrac{-1-0}{1}-\tfrac{0-1}{1}) = 0 \end{cases}$$
> Resolviendo el sistema $2\times2$: $M_1 = -\tfrac{16}{5} = -3.2$, $M_2 = \tfrac{4}{5} = 0.8$. Con estos momentos se reconstruyen las tres cúbicas.

---

## Relación con otras notas

> [!info]
> - El spline que este sistema construye: [[Splines Cubicos Naturales Sujetos]].
> - La propiedad de diagonal dominancia que garantiza estabilidad: [[Teorema Diagonal Dominante Estricta]].
> - La eliminación gaussiana que el algoritmo de Thomas especializa: [[Eliminacion Gaussiana]].
> - El sentido variacional del resultado: [[Propiedad Minima Curvatura]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Incógnitas | momentos $M_i = S''(x_i)$ |
| Ecuación interna | $h_{i-1}M_{i-1} + 2(h_{i-1}+h_i)M_i + h_iM_{i+1} = 6\delta_i$ |
| Matriz | tridiagonal, simétrica, diagonal dominante |
| Cierre | natural ($M_0=M_n=0$) o sujeto |
| Solución | algoritmo de Thomas, $O(n)$ |

> [!corolario]
> Las condiciones de continuidad $C^2$ del spline cúbico se reducen, vía continuidad de la primera derivada, a un sistema tridiagonal para los momentos $M_i = S''(x_i)$. La matriz es estrictamente [[Teorema Diagonal Dominante Estricta|diagonal dominante]], lo que garantiza solución única y permite resolverla con el algoritmo de Thomas en $O(n)$ sin pivoteo. Las condiciones de frontera (natural o sujeto) aportan las dos ecuaciones restantes. Resuelto el sistema, las cúbicas quedan determinadas, completando la construcción del [[Splines Cubicos Naturales Sujetos|spline cúbico]] cuya [[Propiedad Minima Curvatura|mínima curvatura]] justifica su suavidad.
