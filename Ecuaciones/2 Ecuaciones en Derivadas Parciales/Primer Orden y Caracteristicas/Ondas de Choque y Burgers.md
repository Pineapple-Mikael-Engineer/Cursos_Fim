---
title: Ondas de Choque y Burgers
order: 4
tags:
  - ecuaciones
  - edp
  - teoria
  - caracteristicas
  - choques
draft: false
aliases:
  - Ecuación de Burgers
  - Onda de choque
  - Onda de rarefacción
  - Burgers equation
  - Shock wave
---

# Ondas de Choque y Burgers

> [!definicion]
> La ecuación de **Burgers no viscosa**
> $$u_t+u\,u_x=0$$
> es el modelo mínimo de **formación de choques**. Como cada punto viaja a velocidad igual a su propia altura $u$:
> - datos iniciales **decrecientes** $\Rightarrow$ las características **convergen** $\Rightarrow$ se forma un **choque** (discontinuidad) en tiempo finito;
> - datos iniciales **crecientes** $\Rightarrow$ las características **divergen** $\Rightarrow$ se abre una **onda de rarefacción** (un abanico que rellena el hueco).

> [!info]
> Cierra la sección [[Primer Orden y Caracteristicas/index| Primer Orden y Características]] juntando todo: las características de [[Cuasilineal y No Lineal| Burgers]] y la velocidad de choque de [[Leyes de Conservacion| Rankine-Hugoniot]]. Es el puente hacia la difusión cuando se añade viscosidad.

---

## Ejemplo

> [!ejemplo] Formación del choque y tiempo de quiebre
> Sea $u(x,0)=f(x)$ un dato que **baja** suavemente de $1$ (a la izquierda) a $0$ (a la derecha), con $f$ decreciente. Las características son las rectas
> $$x=x_0+f(x_0)\,t,\qquad u=f(x_0).$$
> Dos características vecinas, salidas de $x_0$ y $x_0+dx_0$, se **cruzan** cuando sus posiciones coinciden. Derivando $x$ respecto del pie e igualando a cero (la condición de cruce de rectas infinitamente próximas):
> $$\frac{\partial x}{\partial x_0}=1+f'(x_0)\,t=0\quad\Longrightarrow\quad t=-\frac{1}{f'(x_0)}.$$
> El **primer** cruce —el nacimiento del choque— ocurre en el **tiempo de quiebre**
> $$\boxed{\,t_*=-\frac{1}{\displaystyle\min_{x_0} f'(x_0)}\,}\;>0,$$
> que solo es positivo si $f'<0$ en algún punto, es decir, si el dato **decrece** en algún lado. Para $t<t_*$ la solución $u=f(x-ut)$ es suave y única; en $t=t_*$ aparece la primera pendiente infinita ($u_x\to\infty$), y para $t>t_*$ continúa como una discontinuidad. Tras el quiebre, el choque entre $u_L$ y $u_R$ viaja a la velocidad de [[Leyes de Conservacion| Rankine-Hugoniot]]
> $$s=\frac{u_L+u_R}{2}.$$

> [!ejemplo] Onda de rarefacción (dato creciente)
> Tomemos ahora el escalón **creciente**
> $$u(x,0)=\begin{cases}0,& x<0,\\[2pt]1,& x>0.\end{cases}$$
> Las características que salen de $x_0<0$ tienen velocidad $0$ (verticales) y las de $x_0>0$ velocidad $1$: **divergen**, dejando una cuña $0<x<t$ por la que **no pasa ninguna** característica del dato. El hueco se rellena con una **onda de rarefacción**: la solución autosemejante que depende solo de $\xi=x/t$. Imponiendo $u_t+uu_x=0$ a una $u=g(x/t)$ se obtiene $u=x/t$ en la cuña, de modo que
> $$u(x,t)=\begin{cases}0,& x\le 0,\\[2pt] x/t,& 0<x<t,\\[2pt] 1,& x\ge t.\end{cases}$$
> Es continua: el abanico de rectas $u=x/t$ conecta suavemente los dos estados. (La alternativa discontinua —un "choque de rarefacción"— existe matemáticamente pero **viola la condición de entropía** y se descarta.)

---

## En qué consiste

> [!teoria] Dos destinos según la pendiente del dato
> Todo se decide por el signo de $f'$, porque la velocidad de cada punto es $u=f(x_0)$:
> | Dato | $f'$ | Características | Resultado |
> |---|---|---|---|
> | decreciente | $f'<0$ | **convergen** | **choque** en $t_*=-1/\min f'$ |
> | creciente | $f'>0$ | **divergen** | **rarefacción** (abanico $u=x/t$) |
> | constante a trozos, escalón bajante | salto $u_L>u_R$ | convergen | choque inmediato, $s=\tfrac{u_L+u_R}2$ |
>
> El choque **comprime** la información (muchas características entran en él); la rarefacción la **estira** (las características se separan y hay que interpolar). Son las dos únicas maneras genéricas en que Burgers responde a un salto.

> [!info] Regularización viscosa
> La ecuación de **Burgers viscosa**
> $$u_t+u\,u_x=\nu\,u_{xx},\qquad \nu>0,$$
> añade difusión. El término $\nu u_{xx}$ **impide** la pendiente infinita: en lugar de una discontinuidad, el choque se vuelve un **frente suave** de ancho $\sim\nu$ que viaja a la misma velocidad de Rankine-Hugoniot. En el límite $\nu\to 0^+$ ese frente colapsa al choque ideal, y la solución límite es **justamente** la que satisface la condición de entropía. Así, la viscosidad evanescente *selecciona* la solución débil física, y conecta este capítulo con la [[Ecuacion del Calor/index| difusión]]. (De hecho, la transformación de Cole-Hopf linealiza Burgers viscosa convirtiéndola en la ecuación del calor.)

> [!warning] Condición de entropía y unicidad
> Para $t>t_*$ hay **muchas** soluciones débiles del mismo problema; solo una es física. La **condición de entropía** la selecciona exigiendo que las características **entren** al choque, nunca que salgan:
> $$f'(u_L)>s>f'(u_R)\quad\text{(para Burgers: } u_L>u_R\text{)}.$$
> Un salto que **subiera** ($u_L<u_R$) tendría características saliendo del frente: no es un choque admisible, y la solución correcta es la **rarefacción**. Esta es la regla que da **unicidad** a la solución débil y la que el límite viscoso reproduce automáticamente.

> [!proposicion]
> Tras el quiebre, la posición del choque **no** se obtiene de las características (ya se cruzaron): se integra su EDO $\dot\xi=s(t)=\tfrac{u_L(t)+u_R(t)}2$ con los estados que el choque va separando, usando la conservación global de $\int u\,dx$ como control.

## Resumen

> [!resumen]
> | Fenómeno | Dato | Fórmula clave |
> |---|---|---|
> | Choque | decreciente / escalón bajante | $t_*=-1/\min f'$, $\quad s=\tfrac{u_L+u_R}{2}$ |
> | Rarefacción | creciente / escalón subiente | $u=x/t$ en la cuña |
> | Viscosidad | $u_t+uu_x=\nu u_{xx}$ | frente suave de ancho $\sim\nu$ |
> | Selección | varias soluciones débiles | condición de entropía $f'(u_L)>s>f'(u_R)$ |

> [!corolario]
> Burgers no viscosa es la lección completa de la no linealidad de primer orden: a partir de datos perfectamente suaves, una densidad **comprime** y forma choques en tiempo finito $t_*$, o **estira** y abre rarefacciones, según solo el signo de la pendiente inicial. La velocidad del choque sale de Rankine-Hugoniot, la unicidad de la entropía, y la suavización física de un toque de viscosidad.

> [!referencia]
> - La regla de la velocidad del choque y su prueba: [[Leyes de Conservacion]] (Rankine-Hugoniot).
> - De dónde viene el cruce de características: [[Cuasilineal y No Lineal]].
> - Vuelta al mapa de la sección: [[Primer Orden y Caracteristicas/index]].
