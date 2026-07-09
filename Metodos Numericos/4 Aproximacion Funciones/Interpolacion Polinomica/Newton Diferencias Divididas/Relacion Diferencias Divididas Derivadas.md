---
title: Relación entre Diferencias Divididas y Derivadas
order: 3
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - interpolacion
  - newton-interpolacion
draft: false
aliases:
  - Diferencias divididas y derivadas
  - Interpolación de Hermite
  - Teorema del valor medio para diferencias divididas
---

# Relación entre Diferencias Divididas y Derivadas

> [!definicion]
> La **diferencia dividida** de orden $k$ es una aproximación discreta de la $k$-ésima derivada: para nodos en un intervalo pequeño,
> $$f[x_0, x_1, \dots, x_k] \approx \frac{f^{(k)}(\xi)}{k!}.$$
> En el límite de nodos confluentes, la aproximación se vuelve exacta.

> [!info]
> Esta identidad conecta las [[Tabla Diferencias Divididas y Coeficientes|diferencias divididas]] con el cálculo diferencial, fundamenta la [[Error Interpolacion Formula Cauchy|fórmula del error]] y permite extender la interpolación de [[Newton Diferencias Divididas/index|Newton]] al caso de **Hermite** (prescribir derivadas además de valores).

---

## Teorema del valor medio para diferencias divididas

> [!teorema]
> Si $f \in C^k[a,b]$ y $x_0, \dots, x_k$ son nodos distintos en $[a,b]$, existe $\xi \in (\min x_i, \max x_i)$ tal que
> $$f[x_0, x_1, \dots, x_k] = \frac{f^{(k)}(\xi)}{k!}.$$

> [!demostracion]
> Sea $p_k$ el polinomio interpolador de grado a lo más $k$ que coincide con $f$ en los nodos $x_0,x_1,\dots,x_k$. Definimos la función error
> $$
> e(x)=f(x)-p_k(x).
> $$
>
> Como $p_k(x_i)=f(x_i)$ para todo $i=0,\dots,k$, se cumple que $e(x_i)=0$. Es decir, $e$ posee $k+1$ ceros distintos.
>
> Aplicando el teorema de Rolle entre cada par de ceros consecutivos, existe al menos un punto donde $e'(x)=0$, por lo que $e'$ posee al menos $k$ ceros. Aplicando nuevamente Rolle a $e'$, se concluye que $e''$ posee al menos $k-1$ ceros. Repitiendo este razonamiento sucesivamente, después de $k$ aplicaciones existe un punto $\xi\in(\min x_i,\max x_i)$ tal que
> $$
> e^{(k)}(\xi)=0.
> $$
>
> Por otra parte,
> $$
> e^{(k)}(x)=f^{(k)}(x)-p_k^{(k)}(x).
> $$
>
> Escribiendo $p_k$ en la forma de Newton,
> $$
> p_k(x)=\sum_{i=0}^{k}f[x_0,\dots,x_i]\prod_{j=0}^{i-1}(x-x_j),
> $$
> observamos que todos los términos, excepto el último, tienen grado menor que $k$; por tanto, su $k$-ésima derivada es nula. Solo permanece el término
> $$
> f[x_0,\dots,x_k]\prod_{j=0}^{k-1}(x-x_j),
> $$
> cuyo coeficiente líder es precisamente $f[x_0,\dots,x_k]$. Como la $k$-ésima derivada de un polinomio de grado $k$ es $k!$ veces su coeficiente líder, se obtiene
> $$
> p_k^{(k)}(x)=k!\,f[x_0,\dots,x_k].
> $$
>
> Finalmente, evaluando en el punto $\xi$ donde $e^{(k)}(\xi)=0$,
> $$
> 0=f^{(k)}(\xi)-k!\,f[x_0,\dots,x_k],
> $$
> y despejando,
> $$
> \boxed{f[x_0,\dots,x_k]=\frac{f^{(k)}(\xi)}{k!}.}
> $$

> [!info]
> Para $k=1$ esto recupera el teorema del valor medio clásico: $f[x_0,x_1] = \frac{f(x_1)-f(x_0)}{x_1-x_0} = f'(\xi)$.

---

## Nodos confluentes: interpolación de Hermite

> [!teorema] **Nodos confluentes**
>  Sean $m+1$ nodos que se aproximan al mismo punto $x_0$. Entonces la diferencia dividida de orden $m$ converge a la derivada correspondiente:
> $$
> \boxed{
> \lim_{x_1,\dots,x_m\to x_0}
> f[x_0,x_1,\dots,x_m]
> =
> \frac{f^{(m)}(x_0)}{m!}.
> }
> $$
>
> En particular, cuando todos los nodos coinciden se define
> $$
> f[\underbrace{x_0,\dots,x_0}_{m+1}]
> :=
> \frac{f^{(m)}(x_0)}{m!}.
> $$
>
> Esta extensión permite construir la [[Interpolacion Hermite/index|interpolación de Hermite]], donde además de interpolar los valores de la función también se imponen los valores de sus derivadas.

> [!demostracion]
> Del teorema del valor medio para diferencias divididas sabemos que, si los nodos son distintos,
> $$
> f[x_0,\dots,x_m]
> =
> \frac{f^{(m)}(\xi)}{m!},
> $$
> para algún punto $\xi$ comprendido entre los nodos.
>
> Si ahora hacemos que los nodos $x_1,\dots,x_m$ se aproximen a $x_0$, el punto $\xi$ también converge a $x_0$. Como $f^{(m)}$ es continua, se obtiene
> $$
> \lim_{\xi\to x_0}f^{(m)}(\xi)
> =
> f^{(m)}(x_0),
> $$
> y, por consiguiente,
> $$
> \lim_{x_1,\dots,x_m\to x_0}
> f[x_0,\dots,x_m]
> =
> \frac{f^{(m)}(x_0)}{m!}.
> $$
>
> Este resultado justifica definir las diferencias divididas con nodos repetidos mediante derivadas, lo que hace posible extender la [[Newton Diferencias Divididas/index|interpolación de Newton]] al caso de la [[Interpolacion Hermite/index|interpolación de Hermite]].


> [!ejemplo]
> **Hermite con $f(0)=1$, $f'(0)=2$, $f(1)=3$.** Se duplica el nodo $0$. Tabla con nodos $(0, 0, 1)$:
>
> | $x_i$ | $f[\,]$ | orden 1 | orden 2 |
> |:---:|:---:|:---:|:---:|
> | 0 | 1 | | |
> | 0 | 1 | $f'(0)=2$ | |
> | 1 | 3 | $\frac{3-1}{1-0}=2$ | $\frac{2-2}{1-0}=0$ |
>
> El interpolador es $H(x) = 1 + 2(x-0) + 0\cdot(x-0)^2 = 1 + 2x$. Verifica $H(0)=1$, $H'(0)=2$, $H(1)=3$. ✓

---

## Consecuencias

> [!proposicion]
> 1. **Diferencias divididas como derivadas discretas:** la columna de orden $k$ de la tabla aproxima $f^{(k)}/k!$; base de la [[Diferenciacion Numerica/index|diferenciación numérica]].
> 2. **Suavidad y magnitud:** si $f^{(k)}$ es grande, las diferencias divididas de orden $k$ lo son; explican por qué funciones poco suaves interpolan mal.
> 3. **Error de interpolación:** la diferencia dividida del nodo siguiente da el [[Error Interpolacion Formula Cauchy|término de error]] exacto.

---

## Relación con otras notas

> [!info]
> - La recurrencia que produce estas cantidades: [[Tabla Diferencias Divididas y Coeficientes]].
> - El término de error que esta identidad fundamenta: [[Error Interpolacion Formula Cauchy]].
> - La diferenciación numérica como aplicación: [[Aproximacion Diferencias Finitas Serie Taylor]].
> - Panorama: [[Newton Diferencias Divididas/index]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Identidad | $f[x_0,\dots,x_k] = f^{(k)}(\xi)/k!$ |
| Caso $k=1$ | teorema del valor medio |
| Nodos confluentes | $f[x_0,\dots,x_0] = f^{(m)}(x_0)/m!$ |
| Aplicación | interpolación de Hermite |
| Demostración | Rolle iterado sobre el error |

> [!corolario]
> Las diferencias divididas son derivadas discretas: $f[x_0,\dots,x_k] = f^{(k)}(\xi)/k!$ para algún $\xi$ interior, generalización del teorema del valor medio que se prueba con Rolle iterado sobre el error de interpolación. En el límite de nodos confluentes la igualdad se vuelve exacta, $f[x_0,\dots,x_0] = f^{(m)}(x_0)/m!$, lo que extiende [[Newton Diferencias Divididas/index|Newton]] a la interpolación de Hermite con valores y derivadas. Esta conexión sustenta tanto el [[Error Interpolacion Formula Cauchy|término de error de Cauchy]] como la [[Diferenciacion Numerica/index|diferenciación numérica]].
