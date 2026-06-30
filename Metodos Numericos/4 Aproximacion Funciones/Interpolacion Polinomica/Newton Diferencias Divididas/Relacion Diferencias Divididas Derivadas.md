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
> Sea $p_k$ el interpolador de $f$ en los $k+1$ nodos. La función error $e(x) = f(x) - p_k(x)$ se anula en $x_0,\dots,x_k$ ($k+1$ ceros). Por el teorema de Rolle aplicado repetidamente, $e^{(k)}$ tiene al menos un cero $\xi$ en el intervalo. Como $p_k$ tiene grado $k$, su coeficiente director es $f[x_0,\dots,x_k]$ y $p_k^{(k)}(x) = k!\,f[x_0,\dots,x_k]$ constante. Entonces
> $$0 = e^{(k)}(\xi) = f^{(k)}(\xi) - k!\,f[x_0,\dots,x_k] \;\Longrightarrow\; f[x_0,\dots,x_k] = \frac{f^{(k)}(\xi)}{k!}.$$

> [!info]
> Para $k=1$ esto recupera el teorema del valor medio clásico: $f[x_0,x_1] = \frac{f(x_1)-f(x_0)}{x_1-x_0} = f'(\xi)$.

---

## Nodos confluentes: interpolación de Hermite

> [!teorema]
> Cuando varios nodos coinciden, la diferencia dividida toma el valor de la derivada:
> $$f[\underbrace{x_0, \dots, x_0}_{m+1}] = \frac{f^{(m)}(x_0)}{m!}.$$
> Esto permite construir el **interpolador de Hermite**, que coincide con $f$ y con sus derivadas hasta cierto orden en los nodos, usando la misma [[Tabla Diferencias Divididas y Coeficientes|tabla de diferencias divididas]] con nodos repetidos.

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
