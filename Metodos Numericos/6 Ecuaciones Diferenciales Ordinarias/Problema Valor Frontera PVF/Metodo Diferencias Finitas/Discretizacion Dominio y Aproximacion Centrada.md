---
title: Discretización del Dominio y Aproximación Centrada
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-frontera
  - diferencias-finitas
draft: false
aliases:
  - Discretización del dominio
  - Aproximación centrada
  - Malla de diferencias finitas
  - Mesh discretization
---

# Discretización del Dominio y Aproximación Centrada

> [!definicion]
> La **discretización** divide el dominio $[a,b]$ en $N$ subintervalos iguales mediante una **malla** de nodos $x_i = a + ih$, $i=0,\dots,N$, con paso $h=(b-a)/N$. En cada nodo interno, las derivadas de la EDO se reemplazan por [[Orden Error Progresiva Regresiva Centrada|diferencias centradas]].

> [!info]
> La aproximación centrada es la elección natural en PVF porque tiene orden $O(h^2)$ y es **simétrica** (usa vecinos a ambos lados), lo que produce un sistema tridiagonal simétrico bien condicionado. Convierte la EDO continua en relaciones algebraicas entre valores nodales.

---

## Fórmulas centradas

> [!teorema]
> Sobre la malla uniforme, las [[Aproximacion Diferencias Finitas Serie Taylor|diferencias centradas]] aproximan:
> $$y'(x_i) \approx \frac{y_{i+1} - y_{i-1}}{2h} + O(h^2), \qquad y''(x_i) \approx \frac{y_{i-1} - 2y_i + y_{i+1}}{h^2} + O(h^2),$$
> donde $y_i \approx y(x_i)$ es la incógnita en el nodo $i$.

> [!demostracion]
> Sumando los desarrollos de Taylor de $y(x_i\pm h)$:
> $$y(x_i+h) + y(x_i-h) = 2y(x_i) + h^2 y''(x_i) + \tfrac{h^4}{12}y^{(4)}(\xi).$$
> Despejando $y''(x_i) = \frac{y_{i-1}-2y_i+y_{i+1}}{h^2} - \frac{h^2}{12}y^{(4)}(\xi)$, error $O(h^2)$. La de $y'$ sale de restar los desarrollos (los términos pares se cancelan).

---

## Sustitución en la EDO

> [!teoria]
> Para un PVF lineal general
> $$y'' = p(x)\,y' + q(x)\,y + r(x),$$
> sustituyendo las diferencias centradas en cada nodo interno $i=1,\dots,N-1$:
> $$\frac{y_{i-1}-2y_i+y_{i+1}}{h^2} = p_i\frac{y_{i+1}-y_{i-1}}{2h} + q_i\,y_i + r_i.$$
> Cada ecuación relaciona **tres** valores consecutivos ($y_{i-1}, y_i, y_{i+1}$), de donde la estructura [[Construccion Sistema Tridiagonal Lineal|tridiagonal]].

---

## Ejemplo

> [!ejemplo]
> **$-T'' = 1$, $T(0)=0$, $T(1)=0$** (fuente de calor uniforme), $N=4$, $h=0.25$. La ecuación nodal $-\frac{T_{i-1}-2T_i+T_{i+1}}{h^2} = 1$, es decir $-T_{i-1}+2T_i-T_{i+1} = h^2 = 0.0625$:
>
> | Nodo $i$ | $x_i$ | Ecuación |
> |:---:|:---:|:---|
> | 1 | 0.25 | $2T_1 - T_2 = 0.0625$ (con $T_0=0$) |
> | 2 | 0.50 | $-T_1 + 2T_2 - T_3 = 0.0625$ |
> | 3 | 0.75 | $-T_2 + 2T_3 = 0.0625$ (con $T_4=0$) |
>
> Solución: $T_1=T_3=0.09375$, $T_2=0.125$, que aproxima la parábola exacta $T(x)=\frac12 x(1-x)$ (máximo $0.125$ en el centro). ✓

---

## Elección del paso

> [!info]
> | Aspecto | Efecto de reducir $h$ |
> |:---|:---|
> | Error de truncamiento | baja como $O(h^2)$ |
> | Tamaño del sistema | crece como $N = (b-a)/h$ |
> | Costo (tridiagonal) | $O(N)$, lineal en nodos |
> | Redondeo | crece (más nodos, $\kappa$ mayor) |
>
> Existe un equilibrio, pero al ser tridiagonal el costo es bajo y se pueden usar mallas finas. El error $O(h^2)$ se verifica halvando $h$ (factor 4).

> [!warning]
> **Mallas no uniformes.** Si la solución tiene gradientes fuertes localizados (capas límite), conviene refinar la malla solo allí. Las fórmulas centradas con paso variable pierden simetría y bajan a $O(h)$ salvo corrección; se usan esquemas adaptados.

---

## Relación con otras notas

> [!info]
> - Las fórmulas centradas y su orden: [[Aproximacion Diferencias Finitas Serie Taylor]] y [[Orden Error Progresiva Regresiva Centrada]].
> - El sistema que resulta: [[Construccion Sistema Tridiagonal Lineal]].
> - La garantía de convergencia: [[Consistencia Estabilidad Convergencia Lax]].
> - Cómo entran las fronteras: [[Tratamiento Condiciones Frontera Dirichlet Neumann]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Malla | $x_i = a + ih$, $h=(b-a)/N$ |
| $y'$ centrada | $(y_{i+1}-y_{i-1})/(2h)$, $O(h^2)$ |
| $y''$ centrada | $(y_{i-1}-2y_i+y_{i+1})/h^2$, $O(h^2)$ |
| Ecuación nodal | relaciona $y_{i-1}, y_i, y_{i+1}$ |
| Estructura | tridiagonal |

> [!corolario]
> La discretización del dominio sustituye la EDO continua por relaciones algebraicas en una malla uniforme, usando diferencias centradas de orden $O(h^2)$ para $y'$ y $y''$. Cada ecuación nodal liga tres valores consecutivos, lo que genera la estructura [[Construccion Sistema Tridiagonal Lineal|tridiagonal]] característica del método. La simetría de las fórmulas centradas da buen condicionamiento y orden cuadrático verificable; su límite son las capas límite, que exigen mallas refinadas. Es el primer paso del [[Metodo Diferencias Finitas/index|método de diferencias finitas]] para PVF.
