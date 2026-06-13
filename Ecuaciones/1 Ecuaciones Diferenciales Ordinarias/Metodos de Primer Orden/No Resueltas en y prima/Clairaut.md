---
title: Clairaut
tags:
  - ecuaciones
  - edo
  - teoria
  - primer-orden
  - no-resueltas
  - clairaut
draft: false
aliases:
  - ecuación de Clairaut
  - Clairaut equation
  - familia de rectas y envolvente
---

# Ecuación de Clairaut

> [!definicion]
> La **ecuación de Clairaut** es el caso particular de [[Lagrange| Lagrange]] en que $\varphi(y')=y'$:
> $$y=x\,y'+\psi(y').$$
> Al derivar respecto a $x$ y poner $u=y'$ se obtiene
> $$u=u+\big(x+\psi'(u)\big)\frac{du}{dx}\ \Longrightarrow\ 0=\big(x+\psi'(u)\big)\frac{du}{dx}.$$
> Un producto nulo abre **dos casos**:
> - **(i)** $\dfrac{du}{dx}=0\ \Rightarrow\ u=c$ constante $\Rightarrow$ **solución general**, una
>   **familia de rectas** $\,y=cx+\psi(c)$.
> - **(ii)** $x+\psi'(u)=0\ \Rightarrow$ **solución singular** (la envolvente), en forma paramétrica
>   $\,x=-\psi'(u),\ \ y=x\,u+\psi(u)$.

> [!info]
> Caso emblemático del bloque [[No Resueltas en y prima/index| no resueltas en $y'$]] (libro, cap. 2.3.4). Es el ejemplo más
> visual de **solución singular como envolvente**: su solución general es un **haz de rectas** y la
> singular es la curva tangente a todas ellas. Para el concepto de envolvente y su cálculo general, ver
> [[Solucion Singular y Envolvente]]; para el método del que es caso particular, [[Lagrange]].

---

## Ejemplo

> [!ejemplo] Resolver $y=x\,y'+(y')^3$
> Aquí $\psi(y')=(y')^3$, de modo que $\psi'(u)=3u^{2}$.
>
> **Paso 1 — derivar respecto a $x$** con $u=y'$:
> $$y'=y'+x\,y''+3(y')^2 y''\ \Longrightarrow\ 0=\big(x+3u^{2}\big)\frac{du}{dx}.$$
>
> **Paso 2 — caso (i): $\dfrac{du}{dx}=0$.** Entonces $u=c$ es constante. Sustituyendo $y'=c$ en la
> ecuación original obtenemos la **solución general**:
> $$\boxed{\,y=cx+c^{3}\,}$$
> una **familia de rectas**, una por cada valor de $c$ (pendiente $c$, ordenada al origen $c^3$).
>
> **Paso 3 — caso (ii): $x+3u^{2}=0$.** Despejando,
> $$x=-3u^{2}\ \Longrightarrow\ u=\pm\sqrt{-\frac{x}{3}}\quad(\text{requiere } x<0).$$
> Sustituyendo en $y=xu+u^{3}$, la **solución singular** es
> $$y_s=x\,u+u^{3}=\pm\,x\sqrt{-\frac{x}{3}}\ \pm\Big(\sqrt{-\frac{x}{3}}\Big)^{3},$$
> una curva definida solo para $x<0$. Esta curva **no** se obtiene de $y=cx+c^3$ para ningún $c$: es la
> **envolvente** del haz de rectas.

---

## En qué consiste

> [!teoria]
> La estructura de Clairaut es transparente porque al derivar el término $xy'$ produce $y'+xy''$, y el
> $y'$ cancela con el del lado izquierdo, dejando un **producto** $\big(x+\psi'(u)\big)\,u'=0$. Cada
> factor da una rama de soluciones:
> - El factor $u'=0$ "congela" la pendiente: cada elección $u=c$ es una **recta**. Juntas forman la
>   solución general, una familia uniparamétrica de líneas rectas.
> - El factor $x+\psi'(u)=0$ describe la **envolvente**: la curva tangente a todas esas rectas. En
>   cada punto de la envolvente pasa, tangente, exactamente una recta de la familia; por eso comparten
>   pendiente y la envolvente satisface la misma EDO. Geométricamente, la envolvente "**envuelve**" el
>   haz de rectas como su borde curvo. El cálculo formal de envolventes (c-discriminante) se desarrolla
>   en [[Solucion Singular y Envolvente]].
>
> Es notable que toda la solución general de una Clairaut sean rectas: la ecuación "dice" que la recta
> tangente $y=cx+\psi(c)$ es ella misma una solución. La envolvente es entonces el objeto geométrico
> que esas tangentes determinan.

> [!algoritmo] Resolver una ecuación de Clairaut
> 1. Reconoce la forma $y=x\,y'+\psi(y')$.
> 2. **Solución general** (directa): reemplaza $y'\to c$ → familia de rectas $y=cx+\psi(c)$.
> 3. **Solución singular**: resuelve el sistema $x+\psi'(u)=0,\ \ y=xu+\psi(u)$ (paramétrico en $u$);
>    si se puede, elimina $u$ para obtener $y_s(x)$.

> [!warning]
> La **solución singular NO se obtiene** de $y=cx+\psi(c)$ para ningún valor de $c$: es una curva
> aparte, ajena a la familia. Por eso al dar "la solución" de una Clairaut hay que reportar **ambas**:
> la familia de rectas (general) y la envolvente (singular). Olvidar la singular deja la solución
> incompleta.

## Resumen

> [!resumen]
> | Caso | Condición | Solución |
> |---|---|---|
> | Forma | — | $y=x\,y'+\psi(y')$ |
> | (i) general | $u'=0\Rightarrow u=c$ | rectas $y=cx+\psi(c)$ |
> | (ii) singular | $x+\psi'(u)=0$ | envolvente $x=-\psi'(u),\ y=xu+\psi(u)$ |

> [!corolario]
> Clairaut es la "máquina de envolventes": su solución general es siempre un **haz de rectas**
> $y=cx+\psi(c)$ y su solución singular es la **envolvente** de ese haz. Es el caso límite de
> [[Lagrange]] donde $\varphi=$ identidad y el método de derivar degenera en un producto de dos
> factores, uno por cada tipo de solución.

> [!referencia]
> - Método general del que es caso particular: [[Lagrange]].
> - Qué es y cómo se calcula la envolvente: [[Solucion Singular y Envolvente]].
> - Vuelta al bloque: [[No Resueltas en y prima/index]].
