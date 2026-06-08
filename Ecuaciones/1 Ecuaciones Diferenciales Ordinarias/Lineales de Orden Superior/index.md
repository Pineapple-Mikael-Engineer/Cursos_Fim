---
title: Lineales de Orden Superior
tags:
  - ecuaciones
  - edo
  - teoria
  - lineales
  - index
draft: false
aliases:
  - EDO lineales de orden superior
  - ecuación lineal de segundo orden
  - higher order linear ODE
---

# Lineales de Orden Superior

> [!definicion]
> Una **EDO lineal de orden $n$** tiene la forma
> $$y^{(n)}+p_{n-1}(x)\,y^{(n-1)}+\dots+p_1(x)\,y'+p_0(x)\,y=f(x),$$
> donde $y$ y sus derivadas aparecen a la **potencia 1** y sin productos entre ellas. Si $f\equiv0$ es
> **homogénea**; si no, **no homogénea**. Su solución general es
> $$y=y_h+y_p,$$
> la suma de la **solución homogénea** $y_h$ (combinación de $n$ soluciones independientes) y **una**
> solución **particular** $y_p$.

> [!info]
> Tercer bloque del [[1 Ecuaciones Diferenciales Ordinarias/index | capítulo de EDO]]. A diferencia de
> los [[Metodos de Primer Orden/index | métodos de primer orden]] —un catálogo de trucos para tipos
> no lineales— aquí hay **una teoría unificada**: la linealidad. Es la base de los
> [[Sistemas y Dinamica/index | sistemas]], de la [[Transformada de Laplace/index | transformada de Laplace]] y de toda la física de **oscilaciones**.

---

## La estructura lineal: por qué todo encaja

> [!teoria]
> Lo que ordena este bloque es que el operador
> $$L[y]:=y^{(n)}+p_{n-1}(x)y^{(n-1)}+\dots+p_0(x)y$$
> es **lineal**: $L[\alpha y_1+\beta y_2]=\alpha L[y_1]+\beta L[y_2]$. De ahí se sigue casi todo:
> - **Superposición.** Si $y_1,\dots,y_k$ resuelven la homogénea $L[y]=0$, cualquier combinación
>   $c_1y_1+\dots+c_ky_k$ también. Las soluciones de $L[y]=0$ forman un **espacio vectorial**.
> - **Dimensión $n$.** Ese espacio tiene dimensión exactamente $n$: existen $n$ soluciones
>   **linealmente independientes** $y_1,\dots,y_n$ (un *conjunto fundamental*) y toda solución
>   homogénea es $y_h=c_1y_1+\dots+c_ny_n$. La independencia se detecta con el
>   [[Wronskiano e Independencia Lineal | wronskiano]].
> - **No homogénea = homogénea + una particular.** Si $L[y_p]=f$, entonces $L[y]=f$ ⟺ $y-y_p$
>   resuelve la homogénea. Por eso $y=y_h+y_p$: la homogénea aporta los **$n$ grados de libertad**
>   (las constantes que fijan las condiciones), $y_p$ ajusta la **fuente** $f$.

> [!teoria] El plan de ataque (y dónde vive cada pieza)
> Resolver $L[y]=f$ se descompone siempre en dos tareas:
> 1. **Hallar $y_h$** (resolver la homogénea). Con **coeficientes constantes** esto es álgebra: la
>    [[Coeficientes Constantes Homogenea | ecuación característica]]. Con coeficientes variables se
>    necesita [[Reduccion de Orden | reducción de orden]] (si se conoce una solución) o casos
>    especiales como [[Cauchy-Euler | Cauchy-Euler]].
> 2. **Hallar una $y_p$** (vencer la fuente $f$): [[No Homogenea/Coeficientes Indeterminados | coeficientes indeterminados]] cuando $f$ tiene forma "buena" (polinomio·exponencial·seno), o el
>    método universal de [[No Homogenea/Variacion de Parametros | variación de parámetros]].

---

## Mapa del bloque

> [!info]
> | Nota | Rol |
> |---|---|
> | [[Operador Diferencial Lineal\|Operador Diferencial Lineal]] | $L[y]$, linealidad, superposición, espacio de soluciones |
> | [[Wronskiano e Independencia Lineal\|Wronskiano e Independencia Lineal]] | test de independencia $W\neq0$; conjunto fundamental |
> | [[Formula de Abel\|Fórmula de Abel]] | $W$ sin resolver la EDO: $W=W_0e^{-\int p}$ |
> | [[Coeficientes Constantes Homogenea\|Coef. Constantes Homogénea]] | ecuación característica; raíces reales/complejas/repetidas |
> | [[Orden n Coeficientes Constantes\|Orden $n$ Coef. Constantes]] | característica de grado $n$; multiplicidades |
> | [[Reduccion de Orden\|Reducción de Orden]] | segunda solución conocida una |
> | [[Cauchy-Euler\|Cauchy-Euler]] | $x^2y''+axy'+by=0$ → $x=e^t$ |
> | [[No Homogenea/index\|No Homogénea]] | hallar $y_p$: coef. indeterminados y variación de parámetros |
> | [[Oscilaciones/index\|Oscilaciones]] | la aplicación física central: amortiguamiento y resonancia |
> | [[Problemas de Frontera EDO/index\|Problemas de Frontera]] | condiciones en los extremos; función de Green |

## Resumen

> [!resumen]
> | Concepto | Contenido |
> |---|---|
> | Forma | $L[y]=y^{(n)}+\dots+p_0y=f$ |
> | Estructura | $y=y_h+y_p$ |
> | Homogénea | espacio vectorial de **dimensión $n$**; $y_h=\sum c_iy_i$ |
> | Independencia | [[Wronskiano e Independencia Lineal\|wronskiano]] $W\neq0$ |
> | $y_h$ (coef. ctes.) | [[Coeficientes Constantes Homogenea\|ecuación característica]] |
> | $y_p$ | [[No Homogenea/Coeficientes Indeterminados\|coef. indeterminados]] / [[No Homogenea/Variacion de Parametros\|variación de parámetros]] |

> [!corolario]
> La linealidad convierte un problema de cálculo en uno de **álgebra lineal**: el conjunto de
> soluciones es un espacio afín de dimensión $n$ (un punto $y_p$ más un subespacio de dimensión $n$).
> Resolver = encontrar una base de la homogénea + un representante particular. Todo lo demás del
> bloque son técnicas para esas dos tareas.

> [!referencia]
> - Cimiento conceptual: [[Operador Diferencial Lineal]].
> - El caso resoluble por álgebra: [[Coeficientes Constantes Homogenea]].
> - La física que lo motiva: [[Oscilaciones/index]].
