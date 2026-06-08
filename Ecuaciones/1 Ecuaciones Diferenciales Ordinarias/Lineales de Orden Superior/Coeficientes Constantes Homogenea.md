---
title: Coeficientes Constantes Homogénea
tags:
  - ecuaciones
  - edo
  - teoria
  - lineales
  - ecuacion-caracteristica
draft: false
aliases:
  - ecuación característica
  - coeficientes constantes
  - characteristic equation
  - constant coefficients
---

# EDO Lineal Homogénea con Coeficientes Constantes

> [!definicion]
> Para la EDO homogénea con **coeficientes constantes**
> $$a_n y^{(n)}+a_{n-1}y^{(n-1)}+\dots+a_1y'+a_0y=0,$$
> se prueba $y=e^{rx}$ y resulta el **polinomio característico**
> $$a_n r^{n}+a_{n-1}r^{n-1}+\dots+a_1 r+a_0=0.$$
> Cada raíz $r$ aporta una solución $e^{rx}$. Resolver la EDO se reduce a **hallar las raíces** de un
> polinomio y leer las soluciones según sean reales, complejas o repetidas.

> [!info]
> El caso **resoluble por álgebra** del bloque [[Lineales de Orden Superior/index | lineales de orden superior]]. Da el $y_h$ que luego se completa con una particular ([[No Homogenea/index | no homogénea]]). Es el motor de las [[Oscilaciones/index | oscilaciones]]: el oscilador
> $m\ddot x+c\dot x+kx=0$ es exactamente este caso de segundo orden.

---

## Ejemplo

> [!ejemplo] Tres regímenes de raíces (segundo orden)
> **(a) Raíces reales distintas:** $y''-5y'+6y=0$. Característica $r^2-5r+6=(r-2)(r-3)=0$ → $r=2,3$.
> $$y=c_1e^{2x}+c_2e^{3x}.$$
>
> **(b) Raíces complejas:** $y''+4y=0$. Característica $r^2+4=0$ → $r=\pm 2i$. Con la fórmula de Euler,
> $$y=c_1\cos 2x+c_2\operatorname{sen}2x.$$
>
> **(c) Raíz repetida:** $y''-6y'+9y=0$. Característica $r^2-6r+9=(r-3)^2=0$ → $r=3$ doble. La segunda
> solución gana un factor $x$:
> $$y=(c_1+c_2x)\,e^{3x}.$$

> [!ejemplo] Un PVI completo
> **Resolver $y''+2y'+5y=0$, con $y(0)=1,\ y'(0)=0$.** Característica $r^2+2r+5=0$ →
> $r=\dfrac{-2\pm\sqrt{4-20}}{2}=-1\pm2i$. Solución general (parte real $-1$ → factor $e^{-x}$, parte
> imaginaria $2$ → $\cos2x,\operatorname{sen}2x$):
> $$y=e^{-x}\big(c_1\cos2x+c_2\operatorname{sen}2x\big).$$
> Imponiendo $y(0)=1$: $c_1=1$. Derivando y usando $y'(0)=0$:
> $y'=e^{-x}\!\big[(-c_1+2c_2)\cos2x+(-c_2-2c_1)\operatorname{sen}2x\big]$, en $x=0$: $-c_1+2c_2=0\Rightarrow c_2=\tfrac12$.
> $$\boxed{\,y=e^{-x}\Big(\cos2x+\tfrac12\operatorname{sen}2x\Big)\,}$$
> una oscilación **amortiguada** (envolvente $e^{-x}$).

---

## En qué consiste

> [!teorema] La sustitución $e^{rx}$ y el polinomio característico
> Para $L[y]=a_ny^{(n)}+\dots+a_0y$ con $a_i$ constantes, $y=e^{rx}$ es solución **si y solo si** $r$
> es raíz del polinomio característico $P(r)=a_nr^n+\dots+a_0$.

> [!demostracion]
> **Paso 1 — derivar la exponencial.** $\dfrac{d^k}{dx^k}e^{rx}=r^k e^{rx}$.
>
> **Paso 2 — sustituir.** $L[e^{rx}]=\big(a_nr^n+\dots+a_1r+a_0\big)e^{rx}=P(r)\,e^{rx}$.
>
> **Paso 3 — concluir.** Como $e^{rx}\neq0$, $L[e^{rx}]=0\iff P(r)=0$. Cada raíz da una solución
> exponencial. $\blacksquare$
> En notación de operador, $L=a_n\prod_k(D-r_k)$: la EDO **factoriza** como el polinomio, y cada
> factor $(D-r_k)$ tiene núcleo $e^{r_kx}$.

> [!proposicion] Los tres casos de raíces (segundo orden)
> Para $ay''+by'+cy=0$, según el discriminante $\Delta=b^2-4ac$:
> | $\Delta$ | Raíces | Solución general |
> |:--:|:--|:--|
> | $\Delta>0$ | reales distintas $r_1\neq r_2$ | $c_1e^{r_1x}+c_2e^{r_2x}$ |
> | $\Delta<0$ | complejas $\alpha\pm i\beta$ | $e^{\alpha x}(c_1\cos\beta x+c_2\operatorname{sen}\beta x)$ |
> | $\Delta=0$ | repetida $r$ | $(c_1+c_2x)\,e^{rx}$ |

> [!demostracion] Caso complejo: de $e^{(\alpha+i\beta)x}$ a senos y cosenos
> Si $r=\alpha\pm i\beta$, dos soluciones complejas son $e^{(\alpha\pm i\beta)x}$. Por la **fórmula de
> Euler** $e^{i\beta x}=\cos\beta x+i\operatorname{sen}\beta x$:
> $$e^{(\alpha+i\beta)x}=e^{\alpha x}(\cos\beta x+i\operatorname{sen}\beta x).$$
> Como $L$ tiene coeficientes reales, las partes **real** e **imaginaria** de una solución compleja son
> cada una solución real: $e^{\alpha x}\cos\beta x$ y $e^{\alpha x}\operatorname{sen}\beta x$. Son
> independientes, así que generan todas las soluciones reales. $\blacksquare$

> [!demostracion] Caso repetido: de dónde sale el factor $x$
> Si $r$ es raíz **doble**, $e^{rx}$ es una solución pero falta una segunda independiente. Por
> [[Reduccion de Orden | reducción de orden]] se prueba $y_2=v(x)e^{rx}$; al sustituir, los términos en
> $v$ y $v'$ se cancelan (porque $r$ anula $P$ **y** $P'$) y queda $v''=0$, de donde $v=x$. Así
> $y_2=x\,e^{rx}$, y la solución general es $(c_1+c_2x)e^{rx}$. Para una raíz de multiplicidad $m$ se
> obtienen $e^{rx},xe^{rx},\dots,x^{m-1}e^{rx}$. $\blacksquare$

> [!algoritmo] Resolver la homogénea con coeficientes constantes
> 1. Escribe el **polinomio característico** $P(r)=0$ (sustituye $y^{(k)}\to r^k$).
> 2. **Halla las raíces** (con multiplicidades).
> 3. Para cada raíz, escribe sus soluciones:
>    - real simple $r$ → $e^{rx}$;
>    - par complejo $\alpha\pm i\beta$ → $e^{\alpha x}\cos\beta x,\ e^{\alpha x}\operatorname{sen}\beta x$;
>    - raíz de multiplicidad $m$ → $e^{rx},xe^{rx},\dots,x^{m-1}e^{rx}$.
> 4. La solución general es la **combinación** con $n$ constantes; fíjalas con las condiciones.

## Resumen

> [!resumen]
> | Raíz | Aporte a $y_h$ |
> |---|---|
> | real simple $r$ | $e^{rx}$ |
> | complejas $\alpha\pm i\beta$ | $e^{\alpha x}\cos\beta x,\ e^{\alpha x}\operatorname{sen}\beta x$ |
> | repetida (mult. $m$) | $e^{rx},xe^{rx},\dots,x^{m-1}e^{rx}$ |
> | total | $n$ soluciones independientes → $y_h=\sum c_iy_i$ |

> [!corolario]
> Con coeficientes constantes, una EDO de orden $n$ se **resuelve exactamente** convirtiéndola en un
> problema algebraico: las raíces del polinomio característico. La forma de la solución (exponencial,
> oscilante, con factor $x$) la dicta el **tipo de raíz**, y eso traduce directamente la física:
> parte real → crecimiento/decaimiento, parte imaginaria → oscilación.

> [!referencia]
> - Generalización a grado $n$ y multiplicidades: [[Orden n Coeficientes Constantes]].
> - De dónde sale la segunda solución repetida: [[Reduccion de Orden]].
> - La aplicación física: [[Oscilaciones/index]].
