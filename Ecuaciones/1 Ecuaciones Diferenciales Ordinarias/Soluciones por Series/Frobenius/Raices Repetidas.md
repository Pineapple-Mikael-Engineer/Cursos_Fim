---
title: Raíces Repetidas
order: 5
tags:
  - ecuaciones
  - edo
  - teoria
  - series
  - frobenius
draft: false
aliases:
  - raíces repetidas
  - raíz indicial doble
  - segunda solución logarítmica
  - repeated indicial root
---

# Raíces Repetidas

> [!definicion]
> Si la [[Ecuacion Indicial| ecuación indicial]] tiene una **raíz doble** $r_1=r_2=r$, el método de Frobenius entrega **una sola** solución en serie $y_1=x^{r}\sum_{n\ge0}a_n x^n$. La segunda solución independiente **siempre** lleva un término logarítmico:
> $$y_2=y_1\,\ln x+x^{r}\sum_{n=1}^{\infty}c_n x^n.$$

> [!info]
> El caso más forzado del [[Frobenius/index| método de Frobenius]]: con una raíz indicial doble no hay escapatoria, el $\ln x$ es **obligatorio** (a diferencia de [[Raices Diferencia Entera| diferencia entera]], donde a veces se evita). Comparte con él la técnica de derivar respecto al parámetro $r$.

---

## Ejemplo

> [!ejemplo] Bessel de orden cero
> **$x^2y''+xy'+x^2y=0$** tiene en $x=0$ un punto singular regular con $p_0=1,q_0=0$, ecuación indicial $r^2=0$ → **raíz doble** $r=0$. La primera solución es la función de Bessel
> $$y_1=J_0(x)=\sum_{n=0}^{\infty}\frac{(-1)^n}{(n!)^2}\left(\frac{x}{2}\right)^{2n}=1-\frac{x^2}{4}+\frac{x^4}{64}-\dots$$
> La segunda, por el teorema de abajo, es $y_2=J_0(x)\ln x+\sum_{n\ge1}c_nx^{2n}$, que tras normalizar es la función de Bessel de segunda especie $Y_0(x)$: **diverge** como $\ln x$ cuando $x\to0^+$. Por eso en problemas físicos regulares en el origen se descarta $Y_0$ y se queda solo $J_0$.

---

## En qué consiste

> [!teorema] La segunda solución con $\ln x$
> Si $r$ es raíz **doble** de la ecuación indicial, una segunda solución independiente de la primera $y_1=x^{r}\sum a_nx^n$ es
> $$y_2=y_1\,\ln x+x^{r}\sum_{n=1}^{\infty}c_n x^n,$$
> con coeficientes $c_n$ determinados al sustituir en la EDO.

> [!demostracion] De dónde sale el logaritmo (derivar en $r$)
> **Paso 1 — familia parametrizada.** Construimos $y(x,r)=x^{r}\sum_{n\ge0}a_n(r)\,x^n$ dejando $r$ libre; al sustituir en la EDO, $L[y(x,r)]=a_0\,I(r)\,x^{r}$, donde $I(r)=r(r-1)+p_0r+q_0$ es el **polinomio indicial** (los demás coeficientes se anularon por la recurrencia).
>
> **Paso 2 — usar que la raíz es doble.** Como $r$ es raíz doble, $I(r)=0$ **y** $I'(r)=0$. Entonces $y(x,r)$ es solución (es $y_1$), y derivando respecto a $r$:
> $$L\!\left[\frac{\partial y}{\partial r}\right]=a_0\,\frac{\partial}{\partial r}\big(I(r)\,x^{r}\big)=a_0\big(I'(r)+I(r)\ln x\big)x^{r}=0,$$
> porque $I(r)=I'(r)=0$. Así $\dfrac{\partial y}{\partial r}\Big|_{r}$ es **también** solución.
>
> **Paso 3 — identificar el término logarítmico.** Como $\dfrac{\partial}{\partial r}x^{r}=x^{r}\ln x$,
> $$\frac{\partial y}{\partial r}=\underbrace{x^{r}\ln x\sum a_n x^n}_{=\,y_1\ln x}+\;x^{r}\sum a_n'(r)\,x^n=y_1\ln x+x^{r}\sum c_n x^n.$$
> Esta es $y_2$, independiente de $y_1$. $\blacksquare$

> [!algoritmo] Resolver con raíz doble
> 1. Halla la raíz doble $r$ y la primera solución $y_1=x^{r}\sum a_nx^n$.
> 2. Propón $y_2=y_1\ln x+x^{r}\sum_{n\ge1}c_nx^n$.
> 3. Sustituye en la EDO; los términos en $\ln x$ se cancelan (porque $y_1$ es solución) y queda una recurrencia para los $c_n$ con una fuente que viene de $y_1'/x$.
> 4. Resuelve los $c_n$ (alternativa equivalente: **reducción de orden** $y_2=y_1\!\int e^{-\int p}/y_1^2$).

> [!warning]
> $y_2$ **no** es de Frobenius pura: el $\ln x$ la hace **singular** en $x=0$. En aplicaciones físicas con regularidad en el origen, esta segunda solución suele descartarse.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Condición | raíz indicial **doble** $r_1=r_2=r$ |
> | Primera solución | $y_1=x^{r}\sum a_nx^n$ |
> | Segunda solución | $y_2=y_1\ln x+x^{r}\sum_{n\ge1}c_nx^n$ |
> | Origen del $\ln x$ | $\partial_r x^{r}=x^{r}\ln x$ (raíz doble ⇒ $I=I'=0$) |
> | Ejemplo | Bessel orden 0: $J_0$ y $Y_0$ |

> [!corolario]
> Con raíz doble la singularidad "agota" una sola serie de potencias; la segunda solución **nace del logaritmo**, que aparece de forma natural al derivar $x^{r}$ respecto al exponente. Es el mismo mecanismo que el factor $x$ en las [[Coeficientes Constantes Homogenea| raíces características repetidas]], trasladado al mundo de las singularidades.

> [!referencia]
> - El caso que a veces evita el log: [[Raices Diferencia Entera]].
> - El caso limpio: [[Raices Diferencia No Entera]].
> - De dónde sale la raíz doble: [[Ecuacion Indicial]].
> - Las funciones resultantes: [[Funciones Especiales/index]].
