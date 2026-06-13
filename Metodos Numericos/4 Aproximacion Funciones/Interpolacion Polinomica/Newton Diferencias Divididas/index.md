---
title: Newton con Diferencias Divididas
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - interpolacion
  - newton-interpolacion
  - index
draft: false
aliases:
  - Interpolación de Newton
  - Diferencias divididas
  - Divided differences
  - Forma de Newton
---

# Interpolación de Newton con Diferencias Divididas

> [!definicion]
> La **forma de Newton** del [[Existencia Unicidad Polinomio Interpolador|polinomio interpolador]] lo expresa en la base de productos crecientes:
> $$p_n(x) = \sum_{k=0}^n f[x_0,\dots,x_k]\,\prod_{j=0}^{k-1}(x - x_j),$$
> donde los coeficientes $f[x_0,\dots,x_k]$ son las **diferencias divididas** de los datos.

> [!info]
> Es el mismo polinomio que [[Lagrange/index|Lagrange]], pero en una base **incremental**: añadir un nodo agrega un término sin recalcular los anteriores. Combinada con la [[Forma Anidada y Eficiencia Algoritmo Horner|evaluación de Horner]], es el método más práctico cuando se construyen coeficientes explícitos.

---

## Las cuatro piezas

> [!info]
> - **[[Tabla Diferencias Divididas y Coeficientes|Tabla de diferencias divididas]]:** la recurrencia que genera los coeficientes $f[x_0,\dots,x_k]$ en $O(n^2)$.
> - **[[Forma Anidada y Eficiencia Algoritmo Horner|Forma anidada (Horner)]]:** evaluación del polinomio en $O(n)$ por punto.
> - **[[Relacion Diferencias Divididas Derivadas|Relación con derivadas]]:** $f[x_0,\dots,x_k] = f^{(k)}(\xi)/k!$, y la extensión a nodos confluentes (Hermite).
> - **[[Error Interpolacion Formula Cauchy|Error de interpolación]]:** la fórmula de Cauchy, expresable con la diferencia dividida siguiente.

---

## Ejemplo

> [!ejemplo]
> **Interpolar $(0,1), (1,3), (2,2)$ por Newton.** Tabla de diferencias divididas:
>
> | $x_i$ | $f[\,]$ | $f[\,,\,]$ | $f[\,,\,,\,]$ |
> |:---:|:---:|:---:|:---:|
> | 0 | 1 | | |
> | 1 | 3 | $\frac{3-1}{1-0}=2$ | |
> | 2 | 2 | $\frac{2-3}{2-1}=-1$ | $\frac{-1-2}{2-0}=-\frac{3}{2}$ |
>
> Los coeficientes son la **diagonal superior**: $f[x_0]=1$, $f[x_0,x_1]=2$, $f[x_0,x_1,x_2]=-\tfrac32$. Luego
> $$p_2(x) = 1 + 2(x-0) - \tfrac{3}{2}(x-0)(x-1) = -\tfrac32 x^2 + \tfrac72 x + 1,$$
> idéntico al obtenido por [[Lagrange/index|Lagrange]]. Añadir un cuarto nodo solo agregaría un término $f[x_0,x_1,x_2,x_3]\prod(x-x_j)$.

---

## Newton frente a Lagrange

> [!info]
> | | [[Lagrange/index\|Lagrange]] | Newton (diferencias divididas) |
> |:---|:---|:---|
> | Coeficientes | valores $y_i$ directos | diferencias divididas (tabla $O(n^2)$) |
> | Incremental | no | **sí** ($O(n)$ por nodo nuevo) |
> | Evaluación | $O(n)$ baricéntrica | $O(n)$ por [[Forma Anidada y Eficiencia Algoritmo Horner\|Horner]] |
> | Acceso al error | indirecto | directo (diferencia dividida) |
> | Uso típico | teoría, cuadratura | construcción incremental, splines |

---

## Resumen

| Pieza | Nota |
|:---|:---|
| Recurrencia y tabla | [[Tabla Diferencias Divididas y Coeficientes]] |
| Evaluación eficiente | [[Forma Anidada y Eficiencia Algoritmo Horner]] |
| Significado: derivadas y Hermite | [[Relacion Diferencias Divididas Derivadas]] |
| Error de interpolación | [[Error Interpolacion Formula Cauchy]] |

> [!corolario]
> La interpolación de Newton construye el mismo polinomio que Lagrange en una base incremental cuyos coeficientes son las [[Tabla Diferencias Divididas y Coeficientes|diferencias divididas]], calculadas por recurrencia en $O(n^2)$ y evaluadas en $O(n)$ por [[Forma Anidada y Eficiencia Algoritmo Horner|Horner]]. Su carácter incremental —añadir un nodo cuesta solo un término— y su conexión directa con las [[Relacion Diferencias Divididas Derivadas|derivadas]] y con el [[Error Interpolacion Formula Cauchy|error de Cauchy]] la hacen la formulación preferida para construir coeficientes y para fundamentar los [[Interpolacion Tramos Splines/index|splines]] y la [[Diferenciacion Numerica/index|diferenciación numérica]].
