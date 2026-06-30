---
title: Raices Diferencia No Entera
order: 3
tags:
  - ecuaciones
  - edo
  - teoria
  - series
  - frobenius
  - raices-indiciales
draft: false
aliases:
  - raíces con diferencia no entera
  - caso 1 de Frobenius
  - dos soluciones de Frobenius
  - non-integer difference roots
  - Frobenius case 1
---

# Raices Diferencia No Entera

> [!definicion]
> Sea $x_0=0$ un punto singular **regular** de la EDO, con [[Ecuacion Indicial| ecuación indicial]] de raíces $r_1\ge r_2$. Si la diferencia $r_1-r_2\notin\mathbb{Z}$ **no es entera**, existen **dos** soluciones de Frobenius linealmente independientes, cada una con su propia recurrencia:
> $$y_1=x^{r_1}\sum_{n\ge0}a_nx^n,\qquad y_2=x^{r_2}\sum_{n\ge0}b_nx^n,$$
> con $a_0=b_0=1$. La solución general es $y=C_1y_1+C_2y_2$ y **no aparece ningún logaritmo**.

> [!info]
> Es el caso **más cómodo** del [[Frobenius/index| método de Frobenius]], dentro del bloque [[Soluciones por Series/index| soluciones por series]] del capítulo [[1 Ecuaciones Diferenciales Ordinarias/index| EDO]]. Los otros dos casos (más delicados) son [[Raices Diferencia Entera| diferencia entera positiva]] y [[Raices Repetidas| raíz doble]], donde sí puede aparecer un término $\ln x$.

---

## Ejemplo

> [!ejemplo] Dos series independientes para $2x^2y''+x\,y'-(1+x)\,y=0$
> Buscamos soluciones del tipo $y=x^{r}\sum_{n\ge0}a_nx^{n}=\sum_{n\ge0}a_nx^{n+r}$.
>
> **Paso 1 — derivar y sustituir.** Con $y=\sum a_nx^{n+r}$,
> $$y'=\sum (n+r)a_nx^{n+r-1},\qquad y''=\sum (n+r)(n+r-1)a_nx^{n+r-2}.$$
> Al meter en $2x^2y''+xy'-(1+x)y=0$ y agrupar por $x^{n+r}$:
> $$\sum_{n\ge0}\Big[\,\big(2(n+r)(n+r-1)+(n+r)-1\big)a_n-a_{n-1}\,\Big]x^{n+r}=0,$$
> con el convenio $a_{-1}=0$.
>
> **Paso 2 — ecuación indicial** (término $n=0$, $a_0\ne0$):
> $$2r(r-1)+r-1=2r^2-r-1=(2r+1)(r-1)=0\ \Rightarrow\ r_1=1,\quad r_2=-\tfrac12.$$
> La diferencia $r_1-r_2=\tfrac32\notin\mathbb{Z}$: **caso no entero**, esperamos dos series.
>
> **Paso 3 — recurrencia general** (término $n\ge1$). Llamando $P(n+r)=2(n+r)^2-(n+r)-1$,
> $$a_n=\frac{a_{n-1}}{P(n+r)}=\frac{a_{n-1}}{\big(2(n+r)+1\big)\big((n+r)-1\big)}.$$
>
> **Paso 4 — serie para $r_1=1$.** Aquí $P(n+1)=(2n+3)(n)=n(2n+3)$, luego $a_n=\dfrac{a_{n-1}}{n(2n+3)}$ con $a_0=1$:
> $$a_1=\tfrac{1}{1\cdot5}=\tfrac15,\quad a_2=\tfrac{1}{2\cdot7}\cdot\tfrac15=\tfrac{1}{70},\dots$$
> $$\boxed{\,y_1=x\Big(1+\tfrac15x+\tfrac{1}{70}x^2+\cdots\Big).}$$
>
> **Paso 5 — serie para $r_2=-\tfrac12$.** Ahora $P(n-\tfrac12)=(2n)(n-\tfrac32)=n(2n-3)$, luego $b_n=\dfrac{b_{n-1}}{n(2n-3)}$ con $b_0=1$:
> $$b_1=\tfrac{1}{1\cdot(-1)}=-1,\quad b_2=\tfrac{1}{2\cdot1}\cdot(-1)=-\tfrac12,\dots$$
> $$\boxed{\,y_2=x^{-1/2}\Big(1-x-\tfrac12x^2+\cdots\Big).}$$
> Ninguno de los denominadores $n(2n+3)$ ni $n(2n-3)$ se anula para $n\ge1$ entero, así que **ambas recurrencias corren sin tropiezos** y $y_1,y_2$ son independientes (potencias de arranque $x^1$ y $x^{-1/2}$ distintas).

---

## En qué consiste

> [!teoria] Por qué la diferencia no entera lo simplifica todo
> Al sustituir $y=x^r\sum a_nx^n$, el coeficiente que multiplica a $a_n$ es siempre el **polinomio indicial evaluado en $n+r$**, es decir $P(n+r)$, donde $P(r)=2r^2-r-1$ tiene por raíces $r_1,r_2$. La recurrencia es $P(n+r)\,a_n=(\text{términos anteriores})$. El **único peligro** es que $P(n+r)=0$ para algún $n\ge1$, lo que ocurre cuando $n+r$ coincide con la **otra** raíz, esto es cuando $r_1-r_2=n\in\mathbb{Z}^{+}$. Si la diferencia **no** es entera, $n+r_2$ nunca alcanza a $r_1$ y $n+r_1$ nunca baja a $r_2$: ningún denominador se anula y las dos series viven.

> [!teorema] Existencia de dos soluciones de Frobenius (caso no entero)
> Sea $x=0$ singular regular y sean $r_1\ge r_2$ las raíces de la ecuación indicial con $r_1-r_2\notin\mathbb{Z}$. Entonces la EDO posee dos soluciones independientes
> $$y_1=x^{r_1}\sum_{n\ge0}a_nx^n,\qquad y_2=x^{r_2}\sum_{n\ge0}b_nx^n\quad(a_0=b_0=1),$$
> ambas convergentes en $0<x<R$ (hasta la singularidad más próxima), **sin** términos logarítmicos.

> [!demostracion] Las recurrencias nunca se anulan
> **Paso 1 — forma de la recurrencia.** Sustituyendo $y=x^r\sum a_nx^n$ se obtiene, para cada $n\ge1$,
> $$P(n+r)\,a_n=-\sum_{k=1}^{n} q_k\,a_{n-k},$$
> con $P$ el polinomio indicial (grado $2$, raíces $r_1,r_2$) y $q_k$ los coeficientes de las series de $x p(x)$ y $x^2q(x)$. **Paso 2 — denominador no nulo en $r=r_2$.** $P(n+r_2)=0$ exigiría $n+r_2\in\{r_1,r_2\}$. Como $n\ge1$, descartamos $n+r_2=r_2$; y $n+r_2=r_1$ daría $n=r_1-r_2$, **entero**, contra la hipótesis. Luego $P(n+r_2)\ne0$ y cada $b_n$ se despeja sin ambigüedad. Idéntico para $r=r_1$. **Paso 3 — independencia.** Las dos series arrancan con potencias $x^{r_1}$ y $x^{r_2}$, $r_1\ne r_2$, así que su Wronskiano no es idénticamente nulo: son independientes. $\blacksquare$

> [!algoritmo] Resolver el caso de diferencia no entera
> 1. Escribe $y=x^r\sum_{n\ge0}a_nx^n$, calcula $y',y''$ y sustituye.
> 2. Del término $n=0$ obtén la [[Ecuacion Indicial| ecuación indicial]] $P(r)=0$ y sus raíces $r_1\ge r_2$; comprueba $r_1-r_2\notin\mathbb{Z}$.
> 3. Escribe la recurrencia general $a_n=\dfrac{(\text{anteriores})}{P(n+r)}$.
> 4. Pon $r=r_1$ y genera $\{a_n\}$ → primera serie $y_1$.
> 5. Pon $r=r_2$ y genera $\{b_n\}$ → segunda serie $y_2$.
> 6. La general es $y=C_1y_1+C_2y_2$.

> [!warning]
> "No entera" incluye los **semienteros** $\tfrac12,\tfrac32,\dots$: $\tfrac32\notin\mathbb{Z}$ y el método funciona sin log (como en el ejemplo). El caso problemático es solo $r_1-r_2\in\{1,2,3,\dots\}$, que se trata en [[Raices Diferencia Entera| diferencia entera]].

## Resumen

> [!resumen]
> | Elemento | Caso $r_1-r_2\notin\mathbb{Z}$ |
> |---|---|
> | Nº de soluciones de Frobenius | dos, independientes |
> | Primera | $y_1=x^{r_1}\sum a_nx^n$ |
> | Segunda | $y_2=x^{r_2}\sum b_nx^n$ |
> | Logaritmo | no aparece |
> | Recurrencia | $P(n+r)\,a_n=(\text{anteriores})$, denominador $\ne0$ |
> | General | $y=C_1y_1+C_2y_2$ |

> [!corolario]
> Cuando las raíces indiciales difieren en algo **no entero**, Frobenius entrega de golpe las dos soluciones independientes: basta repetir la misma recurrencia con $r=r_1$ y con $r=r_2$. Es el análogo singular del caso "fácil" de [[Puntos Ordinarios| punto ordinario]].

> [!referencia]
> - Punto de partida: [[Ecuacion Indicial]].
> - Cuando la diferencia **sí** es entera: [[Raices Diferencia Entera]].
> - Cuando la raíz es doble: [[Raices Repetidas]].
> - Marco general: [[Frobenius/index]].
