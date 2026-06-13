---
title: Calor con Condiciones de Neumann (Extremos Aislados)
tags:
  - ecuaciones
  - edp
  - teoria
  - calor
  - separacion-variables
draft: false
aliases:
  - calor con Neumann
  - extremos aislados
  - serie de cosenos calor
  - heat equation Neumann
---

# Calor con Condiciones de Neumann (Extremos Aislados)

> [!definicion]
> Resolver la ecuación del calor en una barra $[0,L]$ cuyos **extremos están aislados** —no escapa
> calor por ellos, condiciones de **Neumann**—:
> $$u_t=\alpha^2 u_{xx},\qquad u_x(0,t)=u_x(L,t)=0,\qquad u(x,0)=f(x).$$
> Como el flujo es $q=-k\,u_x$, exigir $u_x=0$ en los bordes es exactamente decir **flujo nulo**. Al
> separar variables, las autofunciones que respetan extremos aislados son **cosenos**
> $X_n=\cos\dfrac{n\pi x}{L}$, **incluyendo el modo constante** $n=0$ ($\lambda_0=0$), que es el que
> sobrevive al final.

> [!info]
> Es el reverso del caso [[Separacion Calor Dirichlet| Dirichlet (extremos fríos)]] dentro de la
> sección [[Ecuacion del Calor/index| Ecuación del Calor]]. Se resuelve igual, por
> [[Tecnica de Separacion| separación de variables]], pero el cambio de frontera cambia las
> autofunciones de senos a **cosenos** (serie de cosenos de Fourier). Pertenece al
> [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]].

---

## Ejemplo

> [!ejemplo] Barra aislada con mitad caliente y mitad fría
> Una barra perfectamente aislada en los extremos (y por los lados) parte de la mitad izquierda
> caliente y la derecha a cero:
> $$f(x)=\begin{cases}T_0, & 0\le x<L/2,\\ 0, & L/2<x\le L.\end{cases}$$
>
> **Paso 1 — separar.** Con $u=XT$ llegamos otra vez a $X''+\lambda X=0$, pero ahora las condiciones
> $u_x(0,t)=u_x(L,t)=0$ se traducen en $X'(0)=X'(L)=0$ (derivadas nulas en los bordes).
>
> **Paso 2 — autovalores con frontera de Neumann.** Con $\lambda=\mu^2$, $X=A\cos\mu x+B\operatorname{sen}\mu x$,
> y $X'=\mu(-A\operatorname{sen}\mu x+B\cos\mu x)$. La condición $X'(0)=0$ da $B=0$; la condición
> $X'(L)=-A\mu\operatorname{sen}\mu L=0$ exige $\operatorname{sen}\mu L=0$, esto es $\mu L=n\pi$. Pero
> ahora $\lambda=0$ **sí** sirve: $X''=0$ con $X'(0)=X'(L)=0$ da la constante $X_0=1$. En total
> $$\lambda_n=\Big(\frac{n\pi}{L}\Big)^2,\qquad X_n(x)=\cos\frac{n\pi x}{L},\qquad n=0,1,2,\dots$$
> El **modo $n=0$** ($\lambda_0=0$, $X_0=1$) es la novedad respecto a Dirichlet.
>
> **Paso 3 — temporal.** $T_n=e^{-\alpha^2(n\pi/L)^2 t}$; en particular $T_0=e^{0}=1$: el modo
> constante **no decae**.
>
> **Paso 4 — superponer.** Escribimos la serie de cosenos (con el medio para que la fórmula de los
> coeficientes sea uniforme):
> $$u(x,t)=\frac{a_0}{2}+\sum_{n=1}^{\infty}a_n\cos\frac{n\pi x}{L}\,e^{-\alpha^2(n\pi/L)^2 t},\qquad
> a_n=\frac{2}{L}\int_0^L f(x)\cos\frac{n\pi x}{L}\,dx.$$
>
> **Paso 5 — coeficientes del dato.** El término constante es la **media**:
> $$\frac{a_0}{2}=\frac{1}{L}\int_0^L f\,dx=\frac{1}{L}\Big(T_0\cdot\frac{L}{2}\Big)=\frac{T_0}{2}.$$
> Para $n\ge1$, $a_n=\dfrac{2}{L}\displaystyle\int_0^{L/2}T_0\cos\dfrac{n\pi x}{L}\,dx=\dfrac{2T_0}{n\pi}\operatorname{sen}\dfrac{n\pi}{2}$,
> no nulo solo para $n$ impar. La solución es
> $$u(x,t)=\frac{T_0}{2}+\frac{2T_0}{\pi}\sum_{m=0}^{\infty}\frac{(-1)^m}{2m+1}\cos\frac{(2m+1)\pi x}{L}\,e^{-\alpha^2((2m+1)\pi/L)^2 t}.$$
> Conforme $t\to\infty$ todas las exponenciales mueren y queda $u\to T_0/2$: la barra se **uniformiza**
> a la media de su temperatura inicial, no a cero. El calor no tenía por dónde escapar.

---

## En qué consiste

> [!teoria] El modo constante lo cambia todo
> En Dirichlet el menor autovalor es $\lambda_1=(\pi/L)^2>0$, así que **todos** los modos decaen y
> $u\to0$. En Neumann aparece $\lambda_0=0$: un modo que **no decae**. Físicamente es el promedio de la
> temperatura, y como los extremos aislados impiden que el calor entre o salga, ese promedio es un
> **invariante**. Los demás modos ($n\ge1$) sí decaen —y los más oscilantes primero, igual que antes—,
> de modo que la barra se aplana hacia su valor medio. La difusión sigue suavizando; lo que cambia es
> **a qué** nivel se estabiliza.

> [!teorema] Conservación del calor total y temperatura de equilibrio
> Si $u$ resuelve $u_t=\alpha^2u_{xx}$ en $[0,L]$ con extremos aislados $u_x(0,t)=u_x(L,t)=0$, entonces
> el **calor total** se conserva,
> $$\frac{d}{dt}\int_0^L u(x,t)\,dx=0,$$
> y a tiempos largos la temperatura tiende a la **media del dato inicial**:
> $$u(x,t)\ \xrightarrow[t\to\infty]{}\ \frac{a_0}{2}=\frac{1}{L}\int_0^L f(x)\,dx.$$

> [!demostracion]
> **Paso 1 — integrar la EDP.** Integramos $u_t=\alpha^2u_{xx}$ en $x$ sobre $[0,L]$ e intercambiamos la
> derivada temporal con la integral espacial:
> $$\frac{d}{dt}\int_0^L u\,dx=\int_0^L u_t\,dx=\alpha^2\int_0^L u_{xx}\,dx=\alpha^2\big[u_x\big]_0^L
> =\alpha^2\big(u_x(L,t)-u_x(0,t)\big).$$
> **Paso 2 — usar Neumann.** Las condiciones $u_x(0,t)=u_x(L,t)=0$ anulan el corchete, luego
> $\dfrac{d}{dt}\int_0^L u\,dx=0$: el calor total $\int_0^L u\,dx$ es constante en el tiempo, igual a su
> valor inicial $\int_0^L f\,dx$. Como en la serie todos los términos con $n\ge1$ decaen a cero y solo
> queda el término constante $a_0/2$, el límite es $u\to a_0/2=\frac1L\int_0^L f\,dx$, la media. $\blacksquare$

> [!proposicion] Contraste Dirichlet ↔ Neumann
> Mismo operador del calor, fronteras opuestas, destinos opuestos:
>
> | | Dirichlet (fríos) | Neumann (aislados) |
> |---|---|---|
> | Frontera | $u(0,t)=u(L,t)=0$ | $u_x(0,t)=u_x(L,t)=0$ |
> | Autofunciones | senos $\operatorname{sen}\dfrac{n\pi x}{L}$ | cosenos $\cos\dfrac{n\pi x}{L}$ |
> | Menor autovalor | $\lambda_1=(\pi/L)^2>0$ | $\lambda_0=0$ |
> | Calor total | se escapa por los bordes | se **conserva** |
> | Límite $t\to\infty$ | $u\to0$ | $u\to$ media $\dfrac1L\int_0^L f$ |
>
> La diferencia entera nace del modo $n=0$: Neumann lo tiene (constante, no decae) y Dirichlet no.

---

## Resumen

> [!resumen]
> | Ingrediente | Resultado |
> |---|---|
> | Frontera | $u_x(0,t)=u_x(L,t)=0$ (Neumann, flujo nulo) |
> | Autovalores | $\lambda_n=(n\pi/L)^2$, $n=0,1,2,\dots$ |
> | Autofunciones | $X_n=\cos\dfrac{n\pi x}{L}$ (cosenos, con $X_0=1$) |
> | Coeficientes | $a_n=\dfrac{2}{L}\int_0^L f\cos\dfrac{n\pi x}{L}\,dx$ |
> | Solución | $\dfrac{a_0}{2}+\sum_{n\ge1}a_n\cos\dfrac{n\pi x}{L}\,e^{-\alpha^2(n\pi/L)^2t}$ |
> | Límite $t\to\infty$ | $u\to\dfrac{a_0}{2}=$ temperatura media inicial |

> [!corolario]
> Aislar los extremos convierte el calor en una cantidad **conservada**: la barra no pierde energía, solo
> la reparte hasta quedar a temperatura uniforme igual a la media del dato. Es la diferencia clave con
> [[Separacion Calor Dirichlet| el caso Dirichlet]], donde la barra se vacía hacia cero.

> [!referencia]
> - El caso de extremos fríos: [[Separacion Calor Dirichlet]].
> - El método general: [[Tecnica de Separacion]].
> - Visión global: [[Ecuacion del Calor/index]].
