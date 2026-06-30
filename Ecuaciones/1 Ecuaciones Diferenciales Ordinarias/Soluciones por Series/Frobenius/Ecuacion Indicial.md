---
title: Ecuación Indicial
order: 2
tags:
  - ecuaciones
  - edo
  - teoria
  - series
  - frobenius
  - ecuacion-indicial
draft: false
aliases:
  - ecuación indicial
  - exponentes de la singularidad
  - indicial equation
  - indicial roots
---

# Ecuación Indicial

> [!definicion]
> Al sustituir la serie de Frobenius $y=\sum_{n\ge0}a_n x^{n+r}$ (con $a_0\neq0$) en una EDO con punto singular regular en $x=0$, el coeficiente de la **potencia más baja** obliga a
> $$\boxed{\,r(r-1)+p_0\,r+q_0=0\,},\qquad p_0=\lim_{x\to0}x\,p(x),\quad q_0=\lim_{x\to0}x^2 q(x).$$
> Esta es la **ecuación indicial**; sus raíces $r_1\ge r_2$ son los **exponentes** de la singularidad y fijan la potencia dominante $x^{r}$ de cada solución.

> [!info]
> Es el primer paso del [[Frobenius/index| método de Frobenius]], tras verificar que el punto es [[Puntos Singulares Regulares| singular regular]]. La **diferencia** $r_1-r_2$ decide cuál de los tres casos aplica para la segunda solución: [[Raices Diferencia No Entera| no entera]], [[Raices Diferencia Entera| entera]] o [[Raices Repetidas| repetida]].

---

## Ejemplo

> [!ejemplo] Los exponentes de la ecuación de Bessel
> **Hallar la ecuación indicial de $x^2y''+xy'+(x^2-\nu^2)y=0$ en $x=0$.** Aquí $p=\dfrac1x$, $q=\dfrac{x^2-\nu^2}{x^2}$, luego
> $$p_0=\lim_{x\to0}x\cdot\tfrac1x=1,\qquad q_0=\lim_{x\to0}x^2\cdot\tfrac{x^2-\nu^2}{x^2}=-\nu^2.$$
> La ecuación indicial es $r(r-1)+r-\nu^2=r^2-\nu^2=0$, así que
> $$r=\pm\nu.$$
> La diferencia $r_1-r_2=2\nu$ determina el caso: $\nu=\tfrac12$ da diferencia $1$ (entera); $\nu=\tfrac13$ da $\tfrac23$ (no entera); $\nu=0$ da raíz doble.

> [!ejemplo] Una ecuación con raíces fraccionarias
> **$2x^2y''+x\,y'-(x+1)y=0$.** Con $xp=\tfrac12$ y $x^2q=-(x+1)/2$ se tiene $p_0=\tfrac12$, $q_0=-\tfrac12$, y la indicial $r(r-1)+\tfrac12 r-\tfrac12=0$, es decir
> $$2r^2-r-1=0\ \Longrightarrow\ (2r+1)(r-1)=0\ \Longrightarrow\ r_1=1,\ r_2=-\tfrac12.$$
> Diferencia $r_1-r_2=\tfrac32$ (no entera): habrá **dos** series de Frobenius limpias.

---

## En qué consiste

> [!teorema] De dónde sale la ecuación indicial
> Escrita la EDO en la forma $x^2y''+x\,(xp)\,y'+(x^2q)\,y=0$, con $xp=p_0+p_1x+\dots$ y $x^2q=q_0+q_1x+\dots$ analíticas, la serie de Frobenius $y=\sum a_nx^{n+r}$ ($a_0\neq0$) solo es compatible con el término de **menor orden** si $r$ satisface $r(r-1)+p_0r+q_0=0$.

> [!demostracion]
> **Paso 1 — términos de menor orden.** Con $y=a_0x^r+a_1x^{r+1}+\dots$,
> $$x^2y''=a_0\,r(r-1)x^{r}+\dots,\quad x(xp)y'=a_0\,p_0\,r\,x^{r}+\dots,\quad (x^2q)y=a_0\,q_0\,x^{r}+\dots$$
> **Paso 2 — coeficiente de $x^{r}$.** Sumando, el coeficiente de la potencia más baja $x^{r}$ es
> $$a_0\big[r(r-1)+p_0r+q_0\big].$$
> **Paso 3 — concluir.** Como $a_0\neq0$ (es el primer coeficiente no nulo, por definición de Frobenius), el corchete debe anularse: $r(r-1)+p_0r+q_0=0$. $\blacksquare$ Las potencias superiores dan la **recurrencia** ordinaria para $a_1,a_2,\dots$ una vez fijado $r$.

> [!proposicion] La diferencia de raíces gobierna el método
> | $r_1-r_2$ | Segunda solución | Nota |
> |:--|:--|:--|
> | **no entera** | otra serie de Frobenius $x^{r_2}\sum b_nx^n$ | [[Raices Diferencia No Entera]] |
> | **entera $>0$** | a veces con $\ln x$ | [[Raices Diferencia Entera]] |
> | **cero** ($r_1=r_2$) | **siempre** con $\ln x$ | [[Raices Repetidas]] |

> [!algoritmo] Obtener los exponentes
> 1. Verifica que $x=0$ es [[Puntos Singulares Regulares| singular regular]].
> 2. Calcula $p_0=\lim x p$ y $q_0=\lim x^2 q$.
> 3. Resuelve $r(r-1)+p_0r+q_0=0$ → raíces $r_1\ge r_2$.
> 4. Mira $r_1-r_2$ para elegir el caso de la segunda solución.

## Resumen

> [!resumen]
> | Dato | Fórmula |
> |---|---|
> | $p_0$ | $\lim_{x\to0}x\,p(x)$ |
> | $q_0$ | $\lim_{x\to0}x^2 q(x)$ |
> | Indicial | $r(r-1)+p_0r+q_0=0$ |
> | Raíces | $r_1\ge r_2$ (exponentes) |
> | Decisión | el caso lo fija $r_1-r_2$ |

> [!corolario]
> La ecuación indicial es una **cuadrática** (en segundo orden) que extrae, de la singularidad, el comportamiento dominante $x^r$ de las soluciones. Es el "polinomio característico" del método de Frobenius: lo que la ecuación característica es a los coeficientes constantes, la indicial lo es a los puntos singulares regulares.

> [!referencia]
> - Cuándo aplica: [[Puntos Singulares Regulares]].
> - Los tres caminos: [[Raices Diferencia No Entera]], [[Raices Diferencia Entera]], [[Raices Repetidas]].
> - Marco: [[Frobenius/index]].
