---
title: Operador Diferencial Lineal
order: 1
tags:
  - ecuaciones
  - edo
  - teoria
  - lineales
  - superposicion
draft: false
aliases:
  - operador diferencial lineal
  - principio de superposición
  - linear differential operator
  - superposition principle
---

# Operador Diferencial Lineal $L[y]$

> [!definicion]
> El lado izquierdo de una EDO lineal define un **operador**
> $$L[y]:=y^{(n)}+p_{n-1}(x)\,y^{(n-1)}+\dots+p_1(x)\,y'+p_0(x)\,y,$$
> que toma una función $y$ y devuelve otra. Es **lineal**:
> $$L[\alpha y_1+\beta y_2]=\alpha\,L[y_1]+\beta\,L[y_2]\qquad(\alpha,\beta\ \text{constantes}).$$
> La EDO se escribe entonces $L[y]=f$ (homogénea si $f\equiv0$). De la linealidad se deduce **toda** la estructura del bloque: superposición, espacio de soluciones de dimensión $n$ y $y=y_h+y_p$.

> [!info]
> Cimiento del bloque [[Lineales de Orden Superior/index| lineales de orden superior]]. Pensar la EDO como "$L$ actuando sobre $y$" la vuelve un problema tipo **entrada–salida** (la fuente $f$ es la entrada), idea que reaparece en la [[Transformada de Laplace/index| transformada de Laplace]] y en la función de transferencia. La independencia de soluciones se mide con el [[Wronskiano e Independencia Lineal| wronskiano]].

---

## Ejemplo

> [!ejemplo]
> **Verificar superposición en $y''-y=0$.** Es $L[y]=y''-y$. Dos soluciones: $y_1=e^{x}$, $y_2=e^{-x}$ (en efecto $y_1''-y_1=e^x-e^x=0$, igual $y_2$). Por superposición, cualquier
> $$y=c_1e^{x}+c_2e^{-x}$$
> resuelve la ecuación. Comprobación directa: $y''=c_1e^x+c_2e^{-x}=y$, luego $y''-y=0$. ✓ Como hay **dos** soluciones independientes y el orden es $2$, esta es la **solución general**.

> [!ejemplo] Superposición con fuentes (descomponer $f$)
> Si $L[y_1]=f_1$ y $L[y_2]=f_2$, entonces $L[y_1+y_2]=f_1+f_2$. Útil para fuentes compuestas: para resolver $y''+y=3x+2\sin x$ se resuelve por separado $y''+y=3x$ y $y''+y=2\sin x$ y se **suman** las particulares. Es el [[Coeficientes Indeterminados| método de superposición]] de fuentes.

---

## En qué consiste

> [!teorema] Principio de superposición (homogénea)
> Si $y_1,\dots,y_k$ resuelven la ecuación homogénea $L[y]=0$, toda combinación lineal $c_1y_1+\dots+c_ky_k$ también la resuelve. Las soluciones de $L[y]=0$ forman un **espacio vectorial**.

> [!demostracion]
> **Paso 1 — linealidad de $L$.** La derivada es lineal: $(\alpha u+\beta v)^{(j)}=\alpha u^{(j)}+\beta v^{(j)}$. Sumando estas igualdades con los pesos $p_j(x)$,
> $$L[\alpha u+\beta v]=\sum_j p_j(x)(\alpha u+\beta v)^{(j)}=\alpha\sum_j p_ju^{(j)}+\beta\sum_j p_jv^{(j)}=\alpha L[u]+\beta L[v].$$
>
> **Paso 2 — aplicar a soluciones.** Si $L[y_i]=0$ para cada $i$, entonces por linealidad
> $$L\!\left[\sum_i c_iy_i\right]=\sum_i c_i\,L[y_i]=\sum_i c_i\cdot 0=0.$$
> La combinación resuelve la homogénea; además $0$ es solución y las combinaciones cierran la suma y el producto por escalar, así que el conjunto es un **subespacio vectorial**. $\blacksquare$

> [!teorema] Estructura de la solución no homogénea
> Si $y_p$ es **una** solución de $L[y]=f$ e $y_h$ recorre las soluciones de $L[y]=0$, entonces la solución general de $L[y]=f$ es
> $$y=y_h+y_p.$$

> [!demostracion]
> **Paso 1 — $y_h+y_p$ resuelve.** $L[y_h+y_p]=L[y_h]+L[y_p]=0+f=f$. ✓
>
> **Paso 2 — toda solución es de esa forma.** Si $L[y]=f$ y $L[y_p]=f$, entonces por linealidad $L[y-y_p]=f-f=0$, así que $y-y_p$ es una solución homogénea $y_h$, de donde $y=y_h+y_p$. $\blacksquare$ El conjunto de soluciones es un **espacio afín**: un punto $y_p$ desplazado por el subespacio de las homogéneas.

> [!teorema] Dimensión del espacio de soluciones
> Si los coeficientes $p_j(x)$ son continuos en un intervalo $I$, el espacio de soluciones de la homogénea de orden $n$ tiene **dimensión exactamente $n$**: existen $n$ soluciones linealmente independientes (un **conjunto fundamental**) y toda solución es combinación de ellas.

> [!info] Por qué la dimensión es $n$
> Por el [[Existencia y Unicidad Picard| teorema de existencia y unicidad]] (la lineal de orden $n$ equivale a un sistema de primer orden con $f$ Lipschitz), fijar los $n$ datos $y(x_0),y'(x_0),\dots,y^{(n-1)}(x_0)$ determina una **única** solución. La aplicación "solución $\mapsto$ vector de datos iniciales $\in\mathbb{R}^n$" es lineal y biyectiva, así que el espacio de soluciones es isomorfo a $\mathbb{R}^n$: dimensión $n$.

> [!info] Notación de operador $D$
> Escribiendo $D=\dfrac{d}{dx}$, el operador es un **polinomio en $D$**: $L=D^n+p_{n-1}D^{n-1}+\dots+p_0$. Con coeficientes constantes ese polinomio **factoriza** como los números, y cada factor $(D-r)$ aporta una solución $e^{rx}$ — la idea detrás de la [[Coeficientes Constantes Homogenea| ecuación característica]].

## Resumen

> [!resumen]
> | Propiedad | Enunciado |
> |---|---|
> | Linealidad | $L[\alpha u+\beta v]=\alpha L[u]+\beta L[v]$ |
> | Superposición | suma de soluciones homogéneas es solución |
> | Espacio homogéneo | subespacio vectorial de dimensión $n$ |
> | No homogénea | $y=y_h+y_p$ (espacio afín) |
> | Datos que la fijan | $y(x_0),\dots,y^{(n-1)}(x_0)$ ($n$ valores) |

> [!corolario]
> Toda la teoría lineal de orden superior es álgebra lineal disfrazada: el operador $L$ es una aplicación lineal entre espacios de funciones, su **núcleo** son las soluciones homogéneas (dimensión $n$) y resolver $L[y]=f$ es hallar la **preimagen** de $f$ —un $y_p$— más el núcleo.

> [!referencia]
> - Medir independencia de las $n$ soluciones: [[Wronskiano e Independencia Lineal]].
> - Construir el conjunto fundamental (coef. ctes.): [[Coeficientes Constantes Homogenea]].
> - Hallar $y_p$: [[No Homogenea/index]].
