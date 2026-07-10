---
title: Construcción General — Etapas s y Orden p
order: 1
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-inicial
  - runge-kutta
draft: false
aliases:
  - Construcción de Runge-Kutta
  - Condiciones de orden
  - Tabla de Butcher
  - Etapas y orden
---

# Construcción General: Etapas $s$ y Orden $p$

> [!definicion]
> Un **método de Runge-Kutta de $s$ etapas** se define por
> $$k_i = f\Big(t_n + c_i h,\ y_n + h\textstyle\sum_{j=1}^s a_{ij}k_j\Big), \qquad y_{n+1} = y_n + h\sum_{i=1}^s b_i k_i,$$
> con coeficientes $\{a_{ij}\}$, pesos $\{b_i\}$ y nodos $\{c_i\}$ recogidos en su **tabla de Butcher**.

> [!info]
> Los coeficientes se eligen imponiendo las **condiciones de orden**: ecuaciones que fuerzan a que la expansión de Taylor del método coincida con la de la solución exacta hasta orden $p$. El número de etapas $s$ acota el orden $p$ alcanzable.

---

## Condiciones de orden

> [!teorema]
> Imponiendo que el método reproduzca la serie de [[Metodos Serie Taylor Orden Superior|Taylor]] hasta orden $p$, los coeficientes deben satisfacer las **condiciones de orden**. Las primeras:
> $$
> \text{orden 1:}\ \sum_i b_i = 1, \qquad \text{orden 2:}\ \sum_i b_i c_i = \tfrac12,
> $$
> $$
> \text{orden 3:}\ \sum_i b_i c_i^2 = \tfrac13,\quad \sum_{i,j} b_i a_{ij} c_j = \tfrac16,
> $$
> junto con la consistencia $c_i = \sum_j a_{ij}$ (los nodos son sumas de filas de $A$).

> [!demostracion]
> **Derivación desde cero: consistencia y condiciones de orden.**
>
> Consideremos un método de Runge–Kutta de **$s$ etapas**:
>
> $$
> k_i
> =
> f\!\left(
> t_n+c_i h,\;
> y_n+
> h\sum_{j=1}^{s}a_{ij}k_j
> \right),
> \qquad
> i=1,\ldots,s,
> $$
>
> $$
> y_{n+1}
> =
> y_n
> +
> h\sum_{i=1}^{s}b_i k_i.
> $$
>
> Antes de comenzar, aclaremos la notación:
>
> - El índice $i$ indica **la etapa que estamos calculando**.
> - El índice $j$ únicamente recorre la suma; **no representa una iteración temporal**.
> - En esta demostración utilizaremos la formulación **general**, válida tanto para métodos explícitos como implícitos.
>
> Más adelante veremos que, para métodos explícitos, muchos coeficientes $a_{ij}$ son cero y cada etapa depende únicamente de las anteriores.
>
> Todas las funciones se desarrollarán alrededor del punto $(t_n,y_n)$. Para simplificar la escritura definimos
>
> $$
> f=f(t_n,y_n),
> \qquad
> f_t=\frac{\partial f}{\partial t},
> \qquad
> f_y=\frac{\partial f}{\partial y},
> $$
>
> y análogamente para las derivadas de orden superior.
>
> ---
>
> **Paso 1. Expansión de una etapa $k_i$.**
>
> Como el punto
>
> $$
> \left(
> t_n+c_i h,\;
> y_n+h\sum_{j=1}^{s}a_{ij}k_j
> \right)
> $$
>
> está próximo a $(t_n,y_n)$ cuando $h$ es pequeño, aplicamos Taylor de primer orden:
>
> $$
> \begin{aligned}
> k_i
> &=
> f
> +
> c_i h\,f_t
> +
> h
> \left(
> \sum_{j=1}^{s}a_{ij}k_j
> \right)
> f_y
> +
> O(h^2).
> \end{aligned}
> $$
>
> Cuando $h\to0$, todas las etapas verifican
>
> $$
> k_j=f+O(h),
> $$
>
> por lo que podemos sustituir
>
> $$
> k_j=f+O(h)
> $$
>
> dentro del término lineal:
>
> $$
> k_i
> =
> f
> +
> c_i h\,f_t
> +
> h
> \left(
> \sum_{j=1}^{s}a_{ij}
> \right)
> f_yf
> +
> O(h^2).
> $$
>
> ---
>
> **Paso 2. Obtención de la condición de consistencia.**
>
> La etapa $k_i$ pretende aproximar la pendiente de la solución exacta en el instante intermedio
>
> $$
> t_n+c_i h.
> $$
>
> Esa pendiente exacta es
>
> $$
> f\!\left(
> t_n+c_i h,\;
> y(t_n+c_i h)
> \right).
> $$
>
> Expandimos nuevamente mediante Taylor:
>
> $$
> f
> +
> c_i h
> \left(
> f_t+f_yf
> \right)
> +
> O(h^2).
> $$
>
> Comparando esta expresión con la obtenida para $k_i$,
>
> $$
> k_i
> =
> f
> +
> c_i h\,f_t
> +
> h
> \left(
> \sum_{j=1}^{s}a_{ij}
> \right)
> f_yf
> +
> O(h^2),
> $$
>
> observamos que ambos desarrollos coincidirán únicamente si los coeficientes de $f_yf$ son iguales.
>
> Por tanto,
>
> $$
> \boxed{
> c_i
> =
> \sum_{j=1}^{s}a_{ij}.
> }
> $$
>
> Esta es la **condición de consistencia** de los nodos.
>
> ---
>
> **Paso 3. Expansión hasta segundo orden.**
>
> Ahora desarrollamos $k_i$ hasta términos de orden $h^2$:
>
> $$
> \begin{aligned}
> k_i
> =&
> f
> +
> c_i h(f_t+f_yf)
> \\
> &
> +
> h^2
> \left[
> \frac{c_i^2}{2}
> \left(
> f_{tt}
> +
> 2f_{ty}f
> +
> f_{yy}f^2
> \right)
> +
> \left(
> \sum_{j=1}^{s}a_{ij}c_j
> \right)
> \left(
> f_yf_t
> +
> f_y^2f
> \right)
> \right]
> +
> O(h^3).
> \end{aligned}
> $$
>
> ---
>
> **Paso 4. Serie de Taylor de la solución exacta.**
>
> La regla de la cadena proporciona
>
> $$
> y'=f,
> $$
>
> $$
> y''=f_t+f_yf,
> $$
>
> $$
> y'''
> =
> f_{tt}
> +
> 2f_{ty}f
> +
> f_{yy}f^2
> +
> f_yf_t
> +
> f_y^2f.
> $$
>
> Luego,
>
> $$
> \begin{aligned}
> y(t_n+h)
> =
> y_n
> &+
> hf
> +
> \frac{h^2}{2}(f_t+f_yf)
> \\
> &
> +
> \frac{h^3}{6}
> \left(
> f_{tt}
> +
> 2f_{ty}f
> +
> f_{yy}f^2
> +
> f_yf_t
> +
> f_y^2f
> \right)
> +
> O(h^4).
> \end{aligned}
> $$
>
> ---
>
> **Paso 5. Comparación con el método.**
>
> Sustituimos la expansión de $k_i$ en
>
> $$
> y_{n+1}
> =
> y_n
> +
> h\sum_{i=1}^{s}b_i k_i.
> $$
>
> Se obtiene
>
> $$
> \begin{aligned}
> y_{n+1}
> =
> y_n
> &+
> h
> \left(
> \sum_{i=1}^{s}b_i
> \right)
> f
> \\
> &
> +
> h^2
> \left(
> \sum_{i=1}^{s}b_ic_i
> \right)
> (f_t+f_yf)
> \\
> &
> +
> h^3
> \Bigg[
> \frac12
> \left(
> \sum_{i=1}^{s}b_ic_i^2
> \right)
> \left(
> f_{tt}
> +
> 2f_{ty}f
> +
> f_{yy}f^2
> \right)
> \\
> &
> \qquad+
> \left(
> \sum_{i=1}^{s}
> \sum_{j=1}^{s}
> b_i a_{ij}c_j
> \right)
> (f_yf_t+f_y^2f)
> \Bigg]
> +
> O(h^4).
> \end{aligned}
> $$
>
> Igualando esta expresión con la serie de Taylor exacta obtenemos las condiciones de orden:
>
> **Orden 1**
>
> $$
> \boxed{
> \sum_{i=1}^{s}b_i=1.
> }
> $$
>
> **Orden 2**
>
> $$
> \boxed{
> \sum_{i=1}^{s}b_ic_i=\frac12.
> }
> $$
>
> **Orden 3**
>
> $$
> \boxed{
> \sum_{i=1}^{s}b_ic_i^2=\frac13,
> }
> $$
>
> $$
> \boxed{
> \sum_{i=1}^{s}
> \sum_{j=1}^{s}
> b_i a_{ij}c_j
> =
> \frac16.
> }
> $$
>
> Estas igualdades garantizan que el desarrollo del método coincide con la serie de Taylor de la solución exacta hasta orden tres.

## La barrera de Butcher: $s$ vs $p$

> [!teorema]
> Para métodos RK **explícitos**, el orden máximo $p$ alcanzable con $s$ etapas es:
>
> | Etapas $s$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
> |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
> | Orden máx. $p$ | 1 | 2 | 3 | 4 | 4 | 5 | 6 | 6 |
>
> Hasta orden 4, $p = s$ (una etapa por orden). A partir de orden 5, hace falta **más** etapas que el orden (**barreras de Butcher**): por eso RK4 es el punto óptimo de eficiencia.

> [!info]
> Esta tabla explica la popularidad de [[RK4 Clasico Tabla Butcher y Orden Cuatro|RK4]]: es el orden más alto que se obtiene con $s=p$ (sin etapas "desperdiciadas"). Subir a orden 5 cuesta una etapa extra; los métodos adaptativos modernos ([[Control Paso Adaptativo RK45 Dormand Prince|Dormand-Prince]]) usan 6-7 etapas para orden 5 con par encajado.

---

## Ejemplo: derivar RK2

> [!ejemplo]
> **Familia RK de 2 etapas.** Con tabla
> $$\begin{array}{c|cc} 0 & 0 & 0 \\ c_2 & c_2 & 0 \\ \hline & b_1 & b_2 \end{array}$$
> las condiciones de orden 2 son $b_1 + b_2 = 1$ y $b_2 c_2 = \tfrac12$. Es un sistema con **un parámetro libre**: eligiendo $c_2$ se obtienen distintos métodos de [[RK2 Heun Euler Modificado Punto Medio|orden 2]]:
> - $c_2 = 1$: $b_1=b_2=\tfrac12$ → **Heun** (trapecio).
> - $c_2 = \tfrac12$: $b_1=0, b_2=1$ → **punto medio**.
>
> Todos son orden 2; difieren en la constante de error.

---

## Explícito vs implícito

> [!info]
> | | Explícito | Implícito |
> |:---|:---|:---|
> | Matriz $A$ | estrictamente triangular inferior | llena o triangular con diagonal |
> | Cálculo de $k_i$ | secuencial, directo | sistema acoplado (Newton) |
> | Orden con $s$ etapas | $\leq s$ (barrera de Butcher) | hasta $2s$ (Gauss-RK) |
> | Estabilidad | condicional | puede ser A-estable |
> | Uso | no rígidos | [[Rigidez Stiffness Problemas Ingenieria\|rígidos]] |
>
> Los RK **implícitos de Gauss** alcanzan orden $2s$ (relacionados con la [[Cuadratura Gaussiana/index|cuadratura gaussiana]]) y son A-estables, ideales para rigidez, a costa de resolver sistemas.

---

## Relación con otras notas

> [!info]
> - La idea de imitar Taylor: [[Metodos Serie Taylor Orden Superior]].
> - Los casos concretos: [[RK2 Heun Euler Modificado Punto Medio]] y [[RK4 Clasico Tabla Butcher y Orden Cuatro]].
> - El uso del par encajado: [[Control Paso Adaptativo RK45 Dormand Prince]].
> - La conexión Gauss-RK: [[Cuadratura Gaussiana/index]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Etapas | $k_i = f(t_n+c_ih, y_n+h\sum a_{ij}k_j)$ |
| Actualización | $y_{n+1} = y_n + h\sum b_i k_i$ |
| Tabla de Butcher | $(c, A, b)$ |
| Condiciones de orden | $\sum b_i=1$, $\sum b_ic_i=\tfrac12$, ... |
| Barrera | $p=s$ hasta orden 4; $p<s$ después |
| Explícito | $A$ estrictamente triangular inferior |

> [!corolario]
> Un método de Runge-Kutta de $s$ etapas se define por su tabla de Butcher $(c, A, b)$, cuyos coeficientes se fijan imponiendo las condiciones de orden que igualan su expansión a la de [[Metodos Serie Taylor Orden Superior|Taylor]] hasta orden $p$. El número de condiciones crece como los árboles de Butcher, y las barreras de Butcher limitan el orden: $p=s$ solo hasta orden 4, lo que hace de [[RK4 Clasico Tabla Butcher y Orden Cuatro|RK4]] el óptimo de eficiencia explícita. Los RK implícitos de Gauss alcanzan orden $2s$ y A-estabilidad —ligados a la [[Cuadratura Gaussiana/index|cuadratura gaussiana]]— para problemas [[Rigidez Stiffness Problemas Ingenieria|rígidos]].
