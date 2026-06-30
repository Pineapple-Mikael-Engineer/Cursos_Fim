---
title: Solución de d'Alembert
order: 3
tags:
  - ecuaciones
  - edp
  - teoria
  - onda
  - dalembert
draft: false
aliases:
  - solución de d'Alembert
  - fórmula de d'Alembert
  - dAlembert solution
  - traveling waves
---

# Solución de d'Alembert

> [!definicion]
> En la **recta entera** $-\infty<x<\infty$, el problema de Cauchy $u_{tt}=c^2u_{xx}$ con $u(x,0)=f(x)$ y $u_t(x,0)=g(x)$ tiene la **solución de d'Alembert**
> $$u(x,t)=\tfrac12\big[f(x-ct)+f(x+ct)\big]+\frac{1}{2c}\int_{x-ct}^{x+ct} g(s)\,ds.$$
> Es la suma de **dos pulsos** que viajan, uno a la derecha ($x-ct$) y otro a la izquierda ($x+ct$), a velocidad $c$, más una contribución integral de la velocidad inicial.

> [!info]
> Es la segunda vía de resolución de la [[Ecuacion de Onda/index| ecuación de onda]], complementaria de la [[Separacion Onda y Modos Normales| separación en modos normales]] (que vale en dominios acotados). Se apoya en el [[Metodo de las Caracteristicas| método de las características]] y en las [[Formas Canonicas| formas canónicas]] de las EDP de segundo orden, y es el punto de partida hacia las [[Ondas en 2D y 3D| ondas en 2D y 3D]]. Hace visible la **propagación a velocidad finita**.

---

## Ejemplo

> [!ejemplo] Dominio de dependencia y cono de influencia
> ![[cono_dependencia.svg|470]]
>
> Mirando la fórmula, el valor $u(x_0,t_0)$ depende **únicamente** de los datos sobre el segmento $[x_0-ct_0,\,x_0+ct_0]$: el valor de $f$ en sus dos extremos y la integral de $g$ en su interior. Ese segmento es el **dominio de dependencia**, la base del triángulo invertido (las dos rectas características $x\pm ct=\text{cte}$ que bajan desde $(x_0,t_0)$). Recíprocamente, un dato colocado en un solo punto $x_*$ del eje $t=0$ solo puede **influir** en los puntos $(x,t)$ con $|x-x_*|\le ct$: su **cono de influencia**, que se abre hacia arriba a velocidad $c$. Nada de lo que ocurre fuera de esa región puede afectar al punto, ni el punto puede afectar nada fuera de su cono.

## En qué consiste

> [!teoria]
> La clave es que el operador de onda **se factoriza**: $\partial_{tt}-c^2\partial_{xx}=(\partial_t-c\partial_x)(\partial_t+c\partial_x)$. Cada factor es un operador de **transporte**: $\partial_t\pm c\partial_x$ aniquila a cualquier función que dependa solo de $x\mp ct$. Por eso la solución general es una superposición de dos perturbaciones rígidas, una que se desplaza hacia la derecha y otra hacia la izquierda, **sin deformarse**. La forma con que entran depende de los datos: la posición $f$ se reparte mitad y mitad entre los dos pulsos, y la velocidad $g$ se "integra" en una onda que llena el segmento entre ambos frentes.

> [!teorema] Fórmula de d'Alembert
> Si $f\in C^2$ y $g\in C^1$, la única solución $C^2$ del problema de Cauchy en la recta es
> $$u(x,t)=\tfrac12\big[f(x-ct)+f(x+ct)\big]+\frac{1}{2c}\int_{x-ct}^{x+ct} g(s)\,ds.$$

> [!demostracion]
> **Paso 1 — Coordenadas características.** Introducimos $\xi=x-ct$ y $\eta=x+ct$. Por la regla de la cadena, $\partial_x=\partial_\xi+\partial_\eta$ y $\partial_t=-c\,\partial_\xi+c\,\partial_\eta$. Calculando $u_{tt}-c^2u_{xx}$ en las nuevas variables, los términos puros se cancelan y queda
> $$u_{tt}-c^2u_{xx}=-4c^2\,u_{\xi\eta}=0\ \Longrightarrow\ u_{\xi\eta}=0.$$
> Integrar $u_{\xi\eta}=0$ es inmediato: integrando en $\eta$, $u_\xi$ no depende de $\eta$; integrando en $\xi$,
> $$u=F(\xi)+G(\eta)=F(x-ct)+G(x+ct),$$
> con $F,G$ arbitrarias. Esta es **la** forma de toda solución: dos ondas viajeras.
>
> **Paso 2 — Imponer los datos iniciales.** En $t=0$, $\xi=\eta=x$:
> $$u(x,0)=F(x)+G(x)=f(x).$$
> Para la velocidad, $u_t=-cF'(x-ct)+cG'(x+ct)$, y en $t=0$:
> $$u_t(x,0)=-cF'(x)+cG'(x)=g(x).$$
>
> **Paso 3 — Despejar $F$ y $G$.** De la segunda relación, $-F'+G'=g/c$; integrando entre un $x_0$ fijo y $x$:
> $$-F(x)+G(x)=\frac1c\int_{x_0}^{x}g(s)\,ds + \text{cte}.$$
> Junto con $F+G=f$, resolvemos el sistema:
> $$F(x)=\frac{f(x)}{2}-\frac{1}{2c}\int_{x_0}^{x}g,\qquad G(x)=\frac{f(x)}{2}+\frac{1}{2c}\int_{x_0}^{x}g.$$
> Sustituyendo $F(x-ct)$ y $G(x+ct)$, las constantes y el límite $x_0$ se cancelan y las dos integrales se combinan en $\frac{1}{2c}\int_{x-ct}^{x+ct}g$:
> $$u(x,t)=\tfrac12\big[f(x-ct)+f(x+ct)\big]+\frac{1}{2c}\int_{x-ct}^{x+ct}g(s)\,ds.\qquad\blacksquare$$

> [!proposicion] Velocidad finita de propagación
> El valor $u(x_0,t_0)$ depende **solo** de los datos iniciales en el intervalo $[x_0-ct_0,\,x_0+ct_0]$; modificar $f$ o $g$ fuera de ahí **no lo altera en absoluto**. Esto es lo contrario del [[Ecuacion del Calor/index| calor]], donde la solución en cualquier punto depende de **todos** los datos iniciales a la vez, e instantáneamente (velocidad de propagación infinita). La onda respeta un límite de velocidad $c$: la información viaja, pero no más rápido que sus frentes.

> [!warning]
> La fórmula propaga los datos **sin suavizarlos**: si $f$ tiene una esquina (no es $C^2$), esa esquina viaja intacta y $u$ hereda la misma falta de regularidad a lo largo de las características. Es otra diferencia con el calor, que borra de inmediato cualquier irregularidad del dato inicial.

## Resumen

> [!resumen]
> | Elemento | Significado |
> |---|---|
> | $\tfrac12 f(x-ct)$ | medio pulso de posición viajando a la derecha |
> | $\tfrac12 f(x+ct)$ | medio pulso de posición viajando a la izquierda |
> | $\tfrac1{2c}\int_{x-ct}^{x+ct} g$ | aporte de la velocidad inicial |
> | Dominio de dependencia | $[x_0-ct_0,\,x_0+ct_0]$ |
> | Cono de influencia | $\{(x,t):\,\lvert x-x_*\rvert\le ct\}$ |

> [!corolario]
> Resolver la onda en la recta es **literalmente** descomponerla en dos pulsos viajeros. La estructura de características $x\pm ct$ codifica el rasgo físico central de las EDP hiperbólicas: la información se propaga a velocidad finita, dentro de conos, y sin difuminarse.

> [!referencia]
> - La técnica subyacente: [[Metodo de las Caracteristicas]] y [[Formas Canonicas]].
> - El salto a más dimensiones: [[Ondas en 2D y 3D]].
> - El panorama de la sección: [[Ecuacion de Onda/index]].
