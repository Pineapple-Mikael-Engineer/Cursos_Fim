---
title: Teoría de Hilbert-Schmidt
order: 1
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - fredholm
  - nucleos-simetricos
  - hilbert-schmidt
draft: false
aliases:
  - teorema de Hilbert-Schmidt
  - desarrollo en funciones propias
  - Hilbert-Schmidt theorem
---

# Teoría de Hilbert-Schmidt

> [!definicion]
> Un núcleo simétrico, **continuo y no nulo**, posee una sucesión de raíces características **reales** $\lambda_n$ con $\lvert\lambda_n\rvert\to\infty$ y un sistema de funciones propias **ortonormales** $\varphi_n$ (con $\langle\varphi_n,\varphi_m\rangle=\delta_{nm}$). El **teorema de Hilbert-Schmidt** afirma que, para **cualquier** función $g$ integrable, la función $Kg$ se desarrolla en serie de esas funciones propias,
> $$Kg=\sum_{n}\frac{\langle g,\varphi_n\rangle}{\lambda_n}\,\varphi_n,$$
> serie que **converge en media** (y, bajo hipótesis suaves, también puntual y uniformemente). No toda función admite ese desarrollo, pero **toda función de la forma $Kg$** sí: las $\varphi_n$ son base ortonormal del **rango** del operador.

> [!info]
> La pieza central de los [[Nucleos Simetricos/index| núcleos simétricos]] y la versión integral de **diagonalizar una matriz simétrica**. De aquí salen [[Teorema de Mercer]] (desarrollar el propio núcleo) y la [[Ecuaciones Simetricas No Homogeneas| fórmula de Schmidt]] (resolver la ecuación). El espectro real y ortogonal que usa proviene de [[Raices Caracteristicas y Funciones Propias]].

---

## Ejemplo

> [!ejemplo] Desarrollar $Kg$ con el núcleo de Green de $-u''$
> Toma el operador $-u''$ en $[0,\pi]$ con $u(0)=u(\pi)=0$. Su [[Funcion de Green para EDO| función de Green]] es el núcleo simétrico
> $$G(x,t)=\frac{1}{\pi}\begin{cases}x(\pi-t)&x\le t\\ t(\pi-x)&x>t\end{cases},\qquad G(x,t)=G(t,x).$$
> Sus raíces características son $\lambda_n=n^2$ y sus funciones propias ortonormales $\varphi_n(x)=\sqrt{\dfrac{2}{\pi}}\,\operatorname{sen}(nx)$ (con $n=1,2,3,\dots$), pues $\int_0^\pi\varphi_n\varphi_m\,dx=\delta_{nm}$.
>
> Sea $g$ cualquier función en $[0,\pi]$. Hilbert-Schmidt da, **sin resolver ninguna integral con el núcleo**,
> $$ (Gg)(x)=\int_0^\pi G(x,t)\,g(t)\,dt=\sum_{n=1}^\infty\frac{\langle g,\varphi_n\rangle}{n^2}\,\varphi_n(x)
>   =\sum_{n=1}^\infty\frac{2}{\pi n^2}\Big(\int_0^\pi g(t)\operatorname{sen}(nt)\,dt\Big)\operatorname{sen}(nx).$$
> Es decir: $Gg$ es el **desarrollo en serie de senos** de $g$ con cada coeficiente dividido por $n^2$. Esa división por $\lambda_n=n^2$ es la huella de "aplicar $K$": amortigua los modos altos, justo lo que hace integrar dos veces. Por ejemplo, para $g\equiv1$ los coeficientes $\int_0^\pi\operatorname{sen}(nt)\,dt=\frac{1-(-1)^n}{n}$ dan $(Gg)(x)=\frac{4}{\pi}\sum_{k\ge0}\frac{\operatorname{sen}((2k+1)x)}{(2k+1)^3}$, que es la serie de Fourier de la parábola $\frac{x(\pi-x)}{2}$ — exactamente la solución de $-u''=1$ con extremos nulos.

---

## En qué consiste

> [!teoria]
> El operador $K$ con núcleo simétrico es **autoadjunto**, y como toda aplicación autoadjunta lleva el espacio a la clausura del subespacio generado por sus autofunciones. El contenido del teorema es: aunque $g$ arbitraria no tenga por qué desarrollarse en las $\varphi_n$ (puede tener componente en el **núcleo** de $K$, donde $K g=0$), **al aplicar $K$ esa componente desaparece** y lo que queda vive íntegramente en el espacio propio. Por eso $Kg$ —y no $g$— es lo que siempre se desarrolla.

> [!teorema] Desarrollo de Hilbert-Schmidt
> Sea $K$ simétrico, continuo y no nulo en $[a,b]$, con funciones propias ortonormales $\varphi_n$ y raíces características $\lambda_n$. Para toda $g$ de cuadrado integrable, la función $h=Kg$ admite el desarrollo
> $$h=\sum_n\langle h,\varphi_n\rangle\,\varphi_n,\qquad\langle h,\varphi_n\rangle=\frac{\langle g,\varphi_n\rangle}{\lambda_n},$$
> convergente en la norma de la media cuadrática.

> [!demostracion] Esquema
> **Paso 1 — proyectar sobre cada autofunción.** Por la definición de función propia, $K\varphi_n=\dfrac{1}{\lambda_n}\varphi_n$. Calcula la componente de $h=Kg$ a lo largo de $\varphi_n$ usando la **simetría** de $K$ (autoadjunción):
> $$\langle h,\varphi_n\rangle=\langle Kg,\varphi_n\rangle=\langle g,K\varphi_n\rangle=\Big\langle g,\tfrac{1}{\lambda_n}\varphi_n\Big\rangle=\frac{\langle g,\varphi_n\rangle}{\lambda_n}.$$
> Esos son exactamente los coeficientes anunciados.
>
> **Paso 2 — las $\varphi_n$ son base del rango.** Sea $r=h-\sum_n\langle h,\varphi_n\rangle\varphi_n$ el resto de proyectar $h$ sobre todas las autofunciones. Por construcción $r\perp\varphi_n$ para todo $n$, luego $r$ no tiene componente propia: está en el **núcleo** del operador. Pero $h=Kg$ pertenece al **rango** de $K$, que para un operador autoadjunto es ortogonal al núcleo; así que $r$ está a la vez en el rango y en el núcleo, y la única posibilidad es $r=0$.
>
> **Paso 3 — convergencia.** Como $\lvert\lambda_n\rvert\to\infty$, los coeficientes $\langle g,\varphi_n\rangle/\lambda_n$ decaen y la serie de Bessel $\sum_n\lvert\langle h,\varphi_n\rangle\rvert^2$ converge: la serie reproduce $h$ en media cuadrática. $\blacksquare$

> [!proposicion] Por qué no se desarrolla $g$, sino $Kg$
> Si intentaras escribir $g=\sum_n\langle g,\varphi_n\rangle\varphi_n$ fallarías cuando $g$ tenga componente en el núcleo de $K$ (donde $Kg=0$): esa parte es invisible a las $\varphi_n$. El operador $K$ **la borra**, y por eso es $Kg$ —ya filtrado— lo que cae limpiamente en la base propia. Es el mismo fenómeno que en una matriz simétrica singular: solo el rango se diagonaliza con base ortonormal.

> [!info]
> Este teorema es, literalmente, la versión **integral** de diagonalizar una matriz simétrica: las $\varphi_n$ hacen de autovectores ortonormales y los $1/\lambda_n$ de autovalores, de modo que aplicar $K$ es "multiplicar cada coordenada propia por $1/\lambda_n$". Sobre él se montan [[Teorema de Mercer]] y la [[Ecuaciones Simetricas No Homogeneas| resolución de la no homogénea]].

## Resumen

> [!resumen]
> | Concepto | Contenido |
> |---|---|
> | Hipótesis | $K$ simétrico, continuo, no nulo |
> | Espectro | $\lambda_n$ reales, $\lvert\lambda_n\rvert\to\infty$, $\varphi_n$ ortonormales |
> | Tesis | $Kg=\sum_n\frac{\langle g,\varphi_n\rangle}{\lambda_n}\varphi_n$ (en media) |
> | Clave de la prueba | $\langle Kg,\varphi_n\rangle=\frac{\langle g,\varphi_n\rangle}{\lambda_n}$ por autoadjunción |
> | Se desarrolla | $Kg$ (rango), **no** $g$ arbitraria |

> [!corolario]
> Toda función "suavizada por el núcleo" vive en la base propia. Esto convierte cualquier expresión con $K$ en una **serie de funciones propias**, y es la palanca con la que se diagonaliza la ecuación de Fredholm simétrica entera.

> [!referencia]
> - Desarrollar el **propio núcleo**: [[Teorema de Mercer]].
> - Resolver la ecuación no homogénea: [[Ecuaciones Simetricas No Homogeneas]].
> - El espectro de fondo: [[Raices Caracteristicas y Funciones Propias]].
> - Panorama: [[Nucleos Simetricos/index]].
