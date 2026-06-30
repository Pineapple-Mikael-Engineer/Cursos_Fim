---
title: Raíces con Diferencia Entera
order: 4
tags:
  - ecuaciones
  - edo
  - teoria
  - series
  - frobenius
draft: false
aliases:
  - raíces diferencia entera
  - segunda solución logarítmica
  - integer difference roots
---

# Raíces con Diferencia Entera

> [!definicion]
> Si las raíces indiciales cumplen $r_1-r_2=N$ con $N$ **entero positivo**, la raíz **mayor** $r_1$ siempre da una solución de Frobenius $y_1=x^{r_1}\sum_{n\ge0}a_nx^n$. La raíz **menor** $r_2$ **puede** dar otra serie limpia o requerir un término **logarítmico**:
> $$y_2=C\,y_1\,\ln x+x^{r_2}\sum_{n\ge0}c_n x^n,$$
> donde la constante $C$ puede resultar **cero** (sin logaritmo) o no.

> [!info]
> Caso intermedio del [[Frobenius/index| método de Frobenius]], fijado por la [[Ecuacion Indicial| ecuación indicial]]. Más delicado que el de [[Raices Diferencia No Entera| diferencia no entera]] (donde no hay log) y menos forzado que el de [[Raices Repetidas| raíz repetida]] (donde el log es obligatorio).

---

## Ejemplo

> [!ejemplo] Cuándo aparece el logaritmo (mecanismo)
> Al construir la serie para la raíz **menor** $r_2$, la recurrencia despeja $c_n$ con un denominador que se **anula justo en $n=N$** (porque $r_2+N=r_1$ es la otra raíz indicial):
> $$\underbrace{\big[(r_2+n)(r_2+n-1)+p_0(r_2+n)+q_0\big]}_{=\,0\ \text{en}\ n=N}\,c_n=-(\text{términos previos}).$$
> - Si el lado derecho **también se anula** en $n=N$, entonces $c_N$ queda **libre** y la serie continúa: la segunda solución es **otra serie de Frobenius pura** ($C=0$, sin $\ln x$).
> - Si el lado derecho **no** se anula, no hay $c_N$ posible: la serie sola es **inconsistente** y hace falta el término $C\,y_1\ln x$ (con $C\neq0$) para absorber el desajuste.

> [!ejemplo] Bessel de orden entero: aparece el logaritmo
> Para la ecuación de [[Funciones Especiales/index| Bessel]] de orden $\nu=1$, las raíces son $r=\pm1$ (diferencia $N=2$). La solución de la raíz mayor es $J_1(x)$; la de la raíz menor **exige** logaritmo, dando la segunda solución $Y_1(x)$ (función de Bessel de segunda especie), que se comporta como $\sim\ln x$ cerca de $x=0$ y por eso **diverge** en el origen.

> [!ejemplo] Un caso sin logaritmo
> No toda diferencia entera trae logaritmo: en ecuaciones como $x y''+(1-x)y'+\lambda y=0$ con $\lambda$ entero (tipo Laguerre), la recurrencia de la raíz menor se cierra sola ($C=0$) y se obtienen **dos** series de Frobenius. Hay que **verificar** la recurrencia, no suponer.

---

## En qué consiste

> [!teorema] Estructura de la segunda solución
> Si $r_1-r_2=N\in\mathbb{Z}^{+}$, existe una segunda solución de la forma
> $$y_2=C\,y_1\ln x+x^{r_2}\sum_{n=0}^{\infty}c_n x^n,\qquad c_0\neq0,$$
> con una constante $C$ (posiblemente nula) determinada por la recurrencia. Cuando $C=0$, $y_2$ es una serie de Frobenius ordinaria; cuando $C\neq0$, aparece la singularidad logarítmica.

> [!teoria] Por qué el logaritmo
> El $\ln x$ es **inevitable** cuando la serie pura no puede compensar el "choque" entre las dos raíces. La vía sistemática para hallar $C$ y los $c_n$ es **reducción de orden** a partir de $y_1$, o derivar respecto al parámetro $r$ la familia $y(x,r)$ y evaluar adecuadamente (la misma técnica que en [[Raices Repetidas| raíces repetidas]]): $\partial_r x^r=x^r\ln x$ es la fuente del término logarítmico.

> [!algoritmo] Resolver el caso de diferencia entera
> 1. Halla $y_1$ con la raíz **mayor** $r_1$ (siempre serie de Frobenius).
> 2. Intenta la serie de la raíz **menor** $r_2$; observa el coeficiente en $n=N$.
> 3. Si la recurrencia se cierra ($C=0$) → segunda serie pura. Si se rompe → añade $C\,y_1\ln x$ y resuelve los $c_n$ (por reducción de orden).

> [!warning]
> **Verifica siempre** si la recurrencia se rompe en $n=N$: suponer logaritmo "por defecto" en toda diferencia entera es un error frecuente.

## Resumen

> [!resumen]
> | Situación | Segunda solución |
> |---|---|
> | $r_1-r_2=N\in\mathbb{Z}^+$ | $y_2=C\,y_1\ln x+x^{r_2}\sum c_nx^n$ |
> | recurrencia se cierra en $n=N$ | $C=0$: serie de Frobenius pura |
> | recurrencia se rompe | $C\neq0$: aparece $\ln x$ |
> | método para $C,c_n$ | reducción de orden / derivar en $r$ |

> [!corolario]
> La diferencia entera es el caso **ambiguo**: la raíz mayor nunca falla, pero la menor exige **comprobar** la recurrencia. El logaritmo aparece solo si la serie pura es incapaz de resolver el desajuste en $n=N$; cuando lo hace, es la firma de la segunda solución (como en $Y_n$ de Bessel).

> [!referencia]
> - El caso sin complicaciones: [[Raices Diferencia No Entera]].
> - El caso con log obligatorio: [[Raices Repetidas]].
> - De dónde salen las raíces: [[Ecuacion Indicial]].
> - Marco: [[Frobenius/index]].
