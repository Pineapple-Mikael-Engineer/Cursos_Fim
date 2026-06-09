---
title: Derivación de la Ecuación del Calor
tags:
  - ecuaciones
  - edp
  - teoria
  - calor
  - difusion
draft: false
aliases:
  - derivación de la ecuación del calor
  - balance de energía calor
  - ley de Fourier
  - heat equation derivation
---

# Derivación de la Ecuación del Calor

> [!definicion]
> La **ecuación del calor** $u_t=\alpha^2 u_{xx}$ no se postula: **se deduce** de dos ingredientes
> físicos en un tramo de barra. El primero es la **conservación de la energía** (el calor que se
> acumula en un trozo es el que entra menos el que sale). El segundo es la **ley de Fourier**, que
> dice que el flujo de calor va **contra el gradiente** de temperatura —del punto caliente al frío—:
> $$q=-k\,u_x.$$
> Combinando ambos y definiendo la **difusividad** $\alpha^2=k/(\rho c)$ se obtiene
> $$\boxed{\ u_t=\alpha^2\,u_{xx}.\ }$$

> [!info]
> Es el punto de partida de toda la sección [[Ecuacion del Calor/index| Ecuación del Calor]]. Una vez
> deducida, se resuelve por [[Separacion Calor Dirichlet| separación de variables con extremos fríos]]
> en una barra finita, o por transformada de Fourier en [[Calor en Dominio Infinito| dominio infinito]].
> Pertenece al [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]] y es la EDP parabólica
> prototipo.

---

## Ejemplo

> [!ejemplo] La difusión suaviza el perfil con el tiempo
> ![[evolucion_calor.svg|470]]
>
> Un perfil inicial con un pico se aplana y ensancha al avanzar el tiempo: el calor fluye de lo
> caliente a lo frío y la temperatura tiende a uniformarse. Esta es la lectura física de los dos
> ingredientes que vamos a montar: la **ley de Fourier** mueve calor a favor de "lo frío" (hacia donde
> $u$ baja) y la **conservación de la energía** garantiza que ese calor no se pierde, solo se redistribuye.
> Donde el perfil es **cóncavo** ($u_{xx}<0$, cima del pico) la temperatura **baja**; donde es
> **convexo** ($u_{xx}>0$, los valles) **sube**. Eso es exactamente lo que dice $u_t=\alpha^2 u_{xx}$:
> el signo de la curvatura manda el sentido del cambio.

---

## En qué consiste

> [!teoria] Las dos piezas físicas
> Pensemos en una barra delgada aislada lateralmente, de modo que el calor solo viaja a lo largo del
> eje $x$. Llamamos $u(x,t)$ a la temperatura y $q(x,t)$ al **flujo de calor** (energía que cruza la
> sección en $x$ por unidad de tiempo y área, positiva si va hacia $+x$). Dos hechos gobiernan la barra:
> - **Conservación de la energía.** El calor no aparece ni desaparece: lo que se acumula en un trozo es
>   lo que entra por un extremo menos lo que sale por el otro.
> - **Ley de Fourier (constitutiva).** El calor fluye **de caliente a frío**, con rapidez proporcional
>   a lo empinado del perfil: $q=-k\,u_x$, donde $k>0$ es la **conductividad térmica**. El signo menos
>   es la clave física: si $u_x>0$ (sube hacia la derecha), el calor va hacia la izquierda ($q<0$).
>
> Cada trozo de barra almacena energía según su masa y su capacidad calorífica: subir la temperatura un
> $\Delta u$ en un tramo de longitud $\Delta x$ y sección unidad cuesta $\rho c\,\Delta x\,\Delta u$ de
> energía, con $\rho$ la densidad y $c$ el calor específico.

> [!teorema] Ecuación del calor en 1D
> Si la temperatura $u(x,t)$ de una barra satisface la conservación de la energía y la ley de Fourier
> $q=-k\,u_x$ con $k,\rho,c$ constantes, entonces
> $$u_t=\alpha^2\,u_{xx},\qquad \alpha^2=\frac{k}{\rho c}\ \ (\text{difusividad}).$$

> [!demostracion]
> **Paso 1 — balance de energía en un tramo.** Aislamos el trozo $[x,x+\Delta x]$. La energía térmica
> que contiene cambia a razón de $\rho c\,\Delta x\,u_t$ (masa por calor específico por tasa de cambio
> de temperatura). Por conservación, esa tasa es **lo que entra por la izquierda menos lo que sale por
> la derecha**:
> $$\rho c\,\Delta x\,u_t \;=\; q(x,t)\;-\;q(x+\Delta x,t).$$
> Entra calor por $x$ (a favor de $+x$) y sale por $x+\Delta x$; de ahí la resta.
>
> **Paso 2 — pasar al límite y meter la ley de Fourier.** Dividimos entre $\Delta x$:
> $$\rho c\,u_t=\frac{q(x,t)-q(x+\Delta x,t)}{\Delta x}\;\xrightarrow[\Delta x\to0]{}\;-\,q_x.$$
> El cociente es **menos** la derivada de $q$ (es la diferencia "izquierda menos derecha"). Ahora
> sustituimos la ley de Fourier $q=-k\,u_x$, así que $q_x=-k\,u_{xx}$ y por tanto
> $$\rho c\,u_t=-q_x=-(-k\,u_{xx})=k\,u_{xx}.$$
>
> **Paso 3 — definir la difusividad.** Dividimos entre $\rho c>0$ y bautizamos el cociente
> $\alpha^2:=k/(\rho c)$:
> $$u_t=\frac{k}{\rho c}\,u_{xx}=\alpha^2\,u_{xx}. \qquad \blacksquare$$

> [!proposicion] Qué mide la difusividad $\alpha^2$
> La constante $\alpha^2=k/(\rho c)$ (unidades $\mathrm{m^2/s}$) dice **qué tan rápido se reparte** el
> calor, no cuánto calor cabe. Un material conduce rápido si conduce bien ($k$ grande) pero almacena
> poco por grado ($\rho c$ pequeño):
> - **Cobre:** $\alpha^2\approx1.1\times10^{-4}\,\mathrm{m^2/s}$ — difunde **muy rápido**, por eso una
>   cuchara metálica se calienta entera casi al instante.
> - **Agua:** $\alpha^2\approx1.4\times10^{-7}\,\mathrm{m^2/s}$, unas mil veces más lento.
> - **Madera:** $\alpha^2\sim10^{-7}\,\mathrm{m^2/s}$ — difunde **lentísimo**; por eso un mango de
>   madera apenas transmite el calor de la olla.
>
> Dimensionalmente, en un tiempo $t$ el calor se reparte sobre una longitud característica
> $\ell\sim\alpha\sqrt{t}$: la difusión avanza con la **raíz** del tiempo, no linealmente.

> [!info] La versión en 3D y la analogía con la difusión
> En tres dimensiones el flujo es un vector $\mathbf q=-k\,\nabla u$ y el mismo balance (ahora con la
> divergencia) da
> $$u_t=\alpha^2\,\nabla^2 u,\qquad \nabla^2u=u_{xx}+u_{yy}+u_{zz}.$$
> La **misma** ecuación describe la **difusión de un soluto**: si $u$ es la concentración, la ley de
> Fourier se llama **segunda ley de Fick**, $\mathbf q=-D\,\nabla u$, y la difusividad es $D$. Calor y
> materia obedecen la misma matemática del esparcimiento.

---

## Resumen

> [!resumen]
> | Pieza | Expresión | Papel |
> |---|---|---|
> | Balance de energía | $\rho c\,\Delta x\,u_t=q(x)-q(x+\Delta x)$ | conservación |
> | Ley de Fourier | $q=-k\,u_x$ | flujo contra el gradiente |
> | Combinación | $\rho c\,u_t=k\,u_{xx}$ | EDP sin normalizar |
> | Difusividad | $\alpha^2=k/(\rho c)$ | velocidad de reparto |
> | Resultado | $u_t=\alpha^2 u_{xx}$ | ecuación del calor |

> [!corolario]
> El signo de $u_{xx}$ decide el destino: donde el perfil es **cóncavo** la temperatura baja y donde es
> **convexo** sube, hasta que la curvatura se anula y se alcanza el equilibrio. Por eso la difusión
> **suaviza**: aniquila las concavidades. Es la firma de las EDP parabólicas.

> [!referencia]
> - Cómo se resuelve con extremos fríos: [[Separacion Calor Dirichlet]].
> - En la recta infinita (transformada de Fourier): [[Calor en Dominio Infinito]].
> - Visión global de la ecuación: [[Ecuacion del Calor/index]].
