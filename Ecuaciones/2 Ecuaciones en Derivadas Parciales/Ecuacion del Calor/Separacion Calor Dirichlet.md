---
title: Calor con Condiciones de Dirichlet (Extremos Fríos)
tags:
  - ecuaciones
  - edp
  - teoria
  - calor
  - separacion-variables
draft: false
aliases:
  - calor con Dirichlet
  - extremos a temperatura fija
  - serie de senos calor
  - heat equation Dirichlet
---

# Calor con Condiciones de Dirichlet (Extremos Fríos)

> [!definicion]
> Resolver la ecuación del calor en una barra $[0,L]$ cuyos **extremos se mantienen a temperatura fija
> cero** —condiciones de **Dirichlet**— partiendo de un perfil inicial $f(x)$:
> $$u_t=\alpha^2 u_{xx},\qquad u(0,t)=u(L,t)=0,\qquad u(x,0)=f(x).$$
> Se ataca por [[Tecnica de Separacion| separación de variables]]: las autofunciones que respetan los
> extremos fríos son **senos**, y la solución es una **serie de senos** cuyos modos decaen
> exponencialmente, $\displaystyle u(x,t)=\sum_n b_n\operatorname{sen}\frac{n\pi x}{L}\,e^{-\alpha^2(n\pi/L)^2t}$.

> [!info]
> Es el caso canónico de la sección [[Ecuacion del Calor/index| Ecuación del Calor]] y la aplicación
> estrella de la [[Tecnica de Separacion| técnica de separación]]. Usa el desarrollo en
> [[Series de Fourier| serie de Fourier de senos]] para ajustar el dato inicial. El contraste con
> extremos **aislados** está en [[Separacion Calor Neumann| condiciones de Neumann]]. Pertenece al
> [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]].

---

## Ejemplo

> [!ejemplo] Barra de longitud $L$ con un perfil triangular inicial
> Tomemos una barra con los extremos en hielo ($u(0,t)=u(L,t)=0$) y un calentamiento inicial en forma
> de **triángulo** centrado, con altura $H$:
> $$f(x)=\begin{cases}\dfrac{2H}{L}\,x, & 0\le x\le L/2,\\[2mm]\dfrac{2H}{L}\,(L-x), & L/2\le x\le L.\end{cases}$$
>
> **Paso 1 — separar.** Con $u=X(x)T(t)$ la EDP $XT'=\alpha^2X''T$ se divide entre $\alpha^2XT$:
> $$\frac{T'}{\alpha^2T}=\frac{X''}{X}=-\lambda.$$
> Las condiciones $u(0,t)=u(L,t)=0$ se traducen en $X(0)=X(L)=0$ (con $T\neq0$).
>
> **Paso 2 — problema de autovalores.** De $X''+\lambda X=0$ con $X(0)=X(L)=0$, solo $\lambda>0$ da
> soluciones no triviales. Escribiendo $\lambda=\mu^2$, $X=A\cos\mu x+B\operatorname{sen}\mu x$; la
> condición $X(0)=0$ mata el coseno ($A=0$) y $X(L)=B\operatorname{sen}\mu L=0$ cuantiza $\mu L=n\pi$:
> $$\lambda_n=\Big(\frac{n\pi}{L}\Big)^2,\qquad X_n(x)=\operatorname{sen}\frac{n\pi x}{L},\qquad n=1,2,3,\dots$$
>
> **Paso 3 — parte temporal.** Cada modo cumple $T'=-\alpha^2\lambda_n T$, de donde
> $$T_n(t)=e^{-\alpha^2(n\pi/L)^2\,t}.$$
>
> **Paso 4 — superponer.** Por linealidad sumamos todos los modos:
> $$u(x,t)=\sum_{n=1}^{\infty}b_n\,\operatorname{sen}\frac{n\pi x}{L}\,e^{-\alpha^2(n\pi/L)^2\,t}.$$
>
> **Paso 5 — ajustar el dato inicial.** En $t=0$ las exponenciales valen $1$, así que $f(x)=\sum_n
> b_n\operatorname{sen}\frac{n\pi x}{L}$, la serie de senos de $f$. Por ortogonalidad,
> $$b_n=\frac{2}{L}\int_0^{L}f(x)\,\operatorname{sen}\frac{n\pi x}{L}\,dx.$$
> Para el triángulo, la integral (simétrica respecto de $L/2$) da el clásico
> $$b_n=\frac{8H}{n^2\pi^2}\operatorname{sen}\frac{n\pi}{2}=\begin{cases}\dfrac{8H}{n^2\pi^2}(-1)^{(n-1)/2}, & n\ \text{impar},\\[1mm]0, & n\ \text{par}.\end{cases}$$
> Solo sobreviven los **armónicos impares** ($b_1=\tfrac{8H}{\pi^2}$, $b_3=-\tfrac{8H}{9\pi^2}$, …), y al
> caer como $1/n^2$ la serie converge rápido. La solución completa es
> $$u(x,t)=\frac{8H}{\pi^2}\sum_{m=0}^{\infty}\frac{(-1)^m}{(2m+1)^2}\operatorname{sen}\frac{(2m+1)\pi x}{L}\,e^{-\alpha^2((2m+1)\pi/L)^2 t}.$$

> [!ejemplo] Un solo modo: el caso más limpio
> Si en cambio el dato es **ya** una autofunción, $f(x)=\operatorname{sen}\dfrac{\pi x}{L}$, entonces
> $b_1=1$ y todos los demás $b_n=0$. La solución no cambia de forma, solo se desinfla:
> $$u(x,t)=\operatorname{sen}\frac{\pi x}{L}\,e^{-\alpha^2(\pi/L)^2 t}.$$
> Cada modo de Fourier es una **forma propia** que decae rígidamente; toda la riqueza de la solución
> general viene de **mezclar** estas formas.

---

## En qué consiste

> [!teoria] Por qué a tiempos largos sobrevive un solo modo
> Cada armónico decae con su propia constante de tiempo $\tau_n=1/(\alpha^2\lambda_n)=L^2/(\alpha^2 n^2\pi^2)$.
> Como $\lambda_n=(n\pi/L)^2$ **crece** con $n$, los modos más oscilantes (los $n$ grandes, que dibujan
> los detalles finos) decaen **muchísimo más rápido**: el modo $n$ se apaga $n^2$ veces más deprisa que
> el fundamental. Pasado un transitorio, **todo** lo que queda es el primer modo $n=1$:
> $$u(x,t)\;\approx\;b_1\,\operatorname{sen}\frac{\pi x}{L}\,e^{-\alpha^2(\pi/L)^2 t}\;\longrightarrow\;0.$$
> La barra termina con la forma suave de medio seno, encogiéndose hacia cero (los extremos fríos
> "chupan" todo el calor). Esta jerarquía de decaimientos es la versión cuantitativa del **suavizado**:
> primero se borran las arrugas, al final se va el calor.

> [!algoritmo] Resolver el problema de Dirichlet del calor
> 1. **Verifica la homogeneidad.** Las condiciones de frontera deben ser **cero**. Si fueran $u(0,t)=A$,
>    $u(L,t)=B$, resta primero la recta estacionaria $v(x)=A+(B-A)x/L$ y trabaja con $w=u-v$.
> 2. **Separa** $u=XT$ y obtén $X''+\lambda X=0$ con $X(0)=X(L)=0$.
> 3. **Autovalores:** $\lambda_n=(n\pi/L)^2$, autofunciones $X_n=\operatorname{sen}\dfrac{n\pi x}{L}$.
> 4. **Temporal:** $T_n=e^{-\alpha^2\lambda_n t}$.
> 5. **Coeficientes:** $b_n=\dfrac{2}{L}\displaystyle\int_0^L f(x)\operatorname{sen}\dfrac{n\pi x}{L}\,dx$
>    (serie de senos del dato inicial).
> 6. **Escribe** $u=\sum_n b_n\operatorname{sen}\dfrac{n\pi x}{L}\,e^{-\alpha^2(n\pi/L)^2 t}$.

> [!warning] Frontera no homogénea
> Si los extremos **no** están a cero (por ejemplo a temperaturas $A$ y $B$ constantes), la separación
> directa falla: la condición sobre $X$ dejaría de ser homogénea y no cuantizaría. La salida es **restar
> la solución estacionaria** $v(x)=A+(B-A)x/L$ (la recta que satisface $v''=0$ y los bordes), resolver el
> problema de Dirichlet **homogéneo** para $w=u-v$ con dato inicial $f-v$, y sumar $v$ al final.

---

## Resumen

> [!resumen]
> | Ingrediente | Resultado |
> |---|---|
> | Frontera | $u(0,t)=u(L,t)=0$ (Dirichlet) |
> | Autovalores | $\lambda_n=(n\pi/L)^2$ |
> | Autofunciones | $X_n=\operatorname{sen}\dfrac{n\pi x}{L}$ (senos) |
> | Coeficientes | $b_n=\dfrac{2}{L}\int_0^L f\operatorname{sen}\dfrac{n\pi x}{L}\,dx$ |
> | Solución | $\sum_n b_n\operatorname{sen}\dfrac{n\pi x}{L}\,e^{-\alpha^2(n\pi/L)^2t}$ |
> | Límite $t\to\infty$ | $u\to0$ (los extremos fríos vacían la barra) |

> [!corolario]
> Con extremos a cero, **toda** la energía térmica acaba escapando: $u\to0$. El último en irse es el
> modo fundamental $\operatorname{sen}\dfrac{\pi x}{L}$, el de menor curvatura y, por tanto, menor
> decaimiento. Es el contraste exacto con [[Separacion Calor Neumann| los extremos aislados]], donde
> el calor no puede salir y la barra tiende a su temperatura **media**.

> [!referencia]
> - El caso de extremos aislados: [[Separacion Calor Neumann]].
> - El método general: [[Tecnica de Separacion]].
> - El desarrollo del dato inicial: [[Series de Fourier]].
> - Visión global: [[Ecuacion del Calor/index]].
