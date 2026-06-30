---
title: Primer Orden y Características
order: 2
tags:
  - ecuaciones
  - edp
  - teoria
  - caracteristicas
  - primer-orden
  - index
draft: false
aliases:
  - Método de Características
  - First-Order PDE
  - Method of Characteristics
---

# Primer Orden y Características

> [!definicion]
> Una **EDP de primer orden** $a\,u_x+b\,u_y=c$ se resuelve siguiendo unas curvas privilegiadas del plano —las **curvas características**— a lo largo de las cuales la ecuación en derivadas parciales **se reduce a una EDO ordinaria**. Resolver la EDP es, entonces, transportar el dato inicial a lo largo de estas curvas.

> [!info]
> Sección del capítulo [[2 Ecuaciones en Derivadas Parciales/index| Ecuaciones en Derivadas Parciales]]. Es la puerta de entrada a la idea de **propagación**: aquí nace la [[Solucion de dAlembert| solución de d'Alembert]] de la onda y el lenguaje con el que se entienden los **choques** y las [[Leyes de Conservacion| leyes de conservación]].

---

## La idea central: la EDP es una EDO disfrazada

> [!teoria]
> Mira la ecuación $a\,u_x+b\,u_y=c$ con ojos geométricos. El lado izquierdo es exactamente la **derivada direccional** de $u$ en la dirección del vector $(a,b)$:
> $$a\,u_x+b\,u_y=(a,b)\cdot\nabla u=\frac{du}{ds}\Big|_{\text{dirección }(a,b)}.$$
> La EDP **no dice nada** sobre cómo cambia $u$ en otras direcciones; solo fija cómo cambia $u$ **al avanzar en la dirección $(a,b)$**. Por eso es natural seguir las curvas cuyo vector tangente es justamente $(a,b)$: las curvas con
> $$\frac{dx}{a}=\frac{dy}{b}\;(=dt).$$
> Estas son las **características**. Sobre cada una de ellas, parametrizada por $t$, la regla de la cadena convierte la EDP en
> $$\frac{du}{dt}=a\,u_x+b\,u_y=c,$$
> es decir, una **EDO ordinaria** $\dfrac{du}{dt}=c$. La derivada parcial desaparece porque, al movernos sobre la característica, solo "vemos" la dirección que la EDP controla.

> [!teoria] La información se propaga
> La consecuencia profunda es que **el valor de $u$ en un punto solo depende del dato inicial en el pie de la característica que pasa por él**. La información no se difunde a todas partes instantáneamente (como en el [[Ecuacion del Calor/index| calor]]): viaja por canales bien definidos, las características, a **velocidad finita**. En la ecuación de transporte $u_t+c\,u_x=0$ esto es literal: el perfil inicial $f(x)$ se desliza rígidamente a velocidad $c$ ([[Metodo de las Caracteristicas| método de las características]]).
>
> Cuando los coeficientes dependen de la propia $u$ —caso **cuasilineal**— las características cambian de pendiente según el valor que transportan y **pueden cruzarse**. Dos pies distintos que llegan al mismo punto exigirían dos valores de $u$ a la vez: la solución clásica deja de existir y se forma una **onda de choque** ([[Cuasilineal y No Lineal| cuasilineal]], [[Ondas de Choque y Burgers| Burgers]]).

> [!info] Mapa de la sección
> | Nota | Qué resuelve |
> |---|---|
> | [[Metodo de las Caracteristicas\|Método de las características]] | el caso **lineal**: ecuaciones características $\dfrac{dx}{dt}=a,\ \dfrac{dy}{dt}=b,\ \dfrac{du}{dt}=c$ y transporte |
> | [[Cuasilineal y No Lineal\|Cuasilineal y no lineal]] | características que dependen de $u$, tiras de Charpit, cruce y tiempo de quiebre |
> | [[Leyes de Conservacion\|Leyes de conservación]] | $u_t+f(u)_x=0$, forma integral y velocidad del choque (Rankine-Hugoniot) |
> | [[Ondas de Choque y Burgers\|Ondas de choque y Burgers]] | formación del choque, rarefacción y regularización viscosa |

---

## Por qué empezar por aquí

> [!teoria]
> Las EDP de primer orden son el laboratorio donde se ve **en estado puro** el mecanismo de propagación que reaparece en toda la física matemática. No necesitan separación de variables ni series de Fourier: basta con resolver **EDO a lo largo de curvas**. Por eso son el mejor punto de partida para entender:
> - **propagación a velocidad finita** (frente que avanza),
> - **dependencia del dominio** (de qué datos depende la solución en un punto),
> - y la aparición genuina de **singularidades** (choques) a partir de datos perfectamente suaves.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Objeto | $a\,u_x+b\,u_y=c$ (primer orden) |
> | Idea | la EDP $=$ derivada direccional en $(a,b)$ $\Rightarrow$ EDO sobre la característica |
> | Características | curvas con $\dfrac{dx}{a}=\dfrac{dy}{b}=dt$ |
> | Sobre la característica | $\dfrac{du}{dt}=c$ (EDO) |
> | Caso cuasilineal | características dependen de $u$ $\Rightarrow$ pueden cruzarse $\Rightarrow$ **choque** |

> [!corolario]
> Toda esta sección descansa en una sola frase: **resolver una EDP de primer orden es transportar los datos iniciales a lo largo de las características, donde la ecuación es una simple EDO**. Lo que cambie —coeficientes constantes, variables o dependientes de $u$— solo cambia *qué tan ordenadas* son esas curvas, y por tanto si la solución se mantiene suave o se rompe en un choque.

> [!referencia]
> - Empieza por el [[Metodo de las Caracteristicas| método de las características]] (caso lineal, con figura).
> - Para el cruce de características y la no linealidad: [[Cuasilineal y No Lineal]].
> - El marco conservativo y los choques: [[Leyes de Conservacion]] y [[Ondas de Choque y Burgers]].
