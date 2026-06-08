---
title: Métodos de Primer Orden
tags:
  - ecuaciones
  - edo
  - teoria
  - primer-orden
  - index
draft: false
aliases:
  - métodos de primer orden
  - first order ODE methods
---

# Métodos de Primer Orden

> [!definicion]
> Catálogo de técnicas para resolver una EDO de **primer orden** $y'=f(x,y)$ (o
> $M\,dx+N\,dy=0$). No hay un método universal: se **reconoce el tipo** por la forma de la
> ecuación y se aplica su truco, que casi siempre consiste en **reducirla a una integral** o a un
> tipo ya resuelto (separable o lineal).

> [!info]
> Núcleo operativo del [[../index | capítulo de EDO]] (libro, caps. 1.1–1.3 y 2.1, 2.3). Apóyate
> antes en los [[../Fundamentos y Teoria Cualitativa/index | fundamentos]] (qué es una solución,
> cuándo es única). La estrella transversal es el [[Lineal Primer Orden | factor integrante]], que
> reaparece en [[Bernoulli]], [[Riccati]] y [[../Lineales de Orden Superior/index | orden superior]].

---

## La habilidad real: clasificar, no memorizar

> [!teoria]
> Una EDO de primer orden $y'=f(x,y)$ es, en el fondo, una **integral disfrazada**: la dificultad
> es que $f$ mezcla $x$ e $y$ de un modo que impide integrar de inmediato. Cada "tipo" de este
> capítulo es una **forma reconocible** en la que esa mezcla se puede deshacer, y su método es el
> gesto que la deshace:
> - **separar** las variables a lados distintos ([[Variables Separables]]),
> - hacer un **cambio de variable** que la vuelva separable o lineal ([[Ecuaciones Homogeneas]],
>   [[Coeficientes Lineales]], [[Bernoulli]], [[Riccati]]),
> - reconocer el lado izquierdo como un **diferencial total** ([[Ecuaciones Exactas]]) o
>   **fabricar** uno con un [[Factor Integrante]].
>
> Por eso el trabajo no es recordar nueve fórmulas, sino **diagnosticar la forma**: una misma
> ecuación puede ser lineal *y* exacta a la vez, o lineal en $x$ aunque no en $y$. La regla práctica
> es escribirla en sus dos caras —forma normal $y'=f(x,y)$ y forma diferencial $M\,dx+N\,dy=0$— y
> recorrer la tabla siguiente hasta que una encaje. La teoría de fondo (por qué cada método
> funciona) va al final de esta nota; lo de cada tipo, en su hoja.

---

## Tabla de decisión (clave del capítulo)

> [!algoritmo] ¿Qué método uso?
> Recorre la lista **en orden**; aplica el primero que encaje:
> 
> | # | Si la ecuación se puede escribir como… | Es… | Método |
> |---|---|---|---|
> | 1 | $\dfrac{dy}{dx}=\dfrac{f(x)}{g(y)}$ | **separable** | integrar cada lado — [[Variables Separables]] |
> | 2 | $y'=F\!\left(\tfrac{y}{x}\right)$ ($f$ homogénea grado 0) | **homogénea** | $v=y/x$ — [[Ecuaciones Homogeneas]] |
> | 3 | $(a_1x{+}b_1y{+}c_1)dx+(a_2x{+}b_2y{+}c_2)dy=0$ | **coef. lineales** | trasladar al corte de rectas — [[Coeficientes Lineales]] |
> | 4 | $M\,dx+N\,dy=0$ con $\partial_y M=\partial_x N$ | **exacta** | hallar $f$ con $df=M\,dx{+}N\,dy$ — [[Ecuaciones Exactas]] |
> | 5 | $M\,dx+N\,dy=0$ **no** exacta | inexacta | [[Factor Integrante]] $\mu$ que la vuelve exacta |
> | 6 | $y'+p(x)\,y=q(x)$ | **lineal** | factor integrante $e^{\int p}$ — [[Lineal Primer Orden]] |
> | 7 | $y'+p\,y=q\,y^{n}$ | **Bernoulli** | $u=y^{1-n}$ → lineal — [[Bernoulli]] |
> | 8 | $y'+p\,y^{2}+q\,y=r$ | **Riccati** | con una sol. conocida, $y=y_p+1/u$ — [[Riccati]] |
> | 9 | $y=x\,\varphi(y')+\psi(y')$ | **Lagrange/Clairaut** | derivar y poner $u=y'$ — [[No Resueltas en y prima/index\|No resueltas en $y'$]] |

---

## Por qué funcionan casi todos

> [!teoria]
> Detrás del catálogo hay **una sola idea**: llevar la ecuación a una forma **integrable**.
> - *Separable* lo logra de inmediato (cada variable a un lado).
> - *Homogénea* y *coeficientes lineales* hacen un **cambio de variable** que la vuelve separable.
> - *Exacta* reconoce el lado izquierdo como un **diferencial total** $df$, de modo que $f=$ cte.
> - *Factor integrante* multiplica por $\mu$ para **fabricar** un diferencial total.
> - *Lineal* es el caso estrella: su factor integrante $e^{\int p}$ siempre existe.
> - *Bernoulli* y *Riccati* son no lineales que un cambio convierte en lineales.

> [!regla]
> Reescribe siempre primero en forma normal $y'=f(x,y)$ **y** en forma diferencial
> $M\,dx+N\,dy=0$: una misma ecuación puede ser "lineal en $y$" y a la vez "exacta", y conviene ver
> ambas caras. A veces es **lineal en $x$** aunque no en $y$ (intercambiar los papeles de $x$ e $y$).

## Resumen

> [!resumen]
> | Tipo | Forma | Cambio / truco | Reduce a |
> |---|---|---|---|
> | Separable | $y'=f(x)/g(y)$ | — | dos integrales |
> | Homogénea | $y'=F(y/x)$ | $v=y/x$ | separable |
> | Coef. lineales | rectas $+c_i$ | trasladar al corte | homogénea |
> | Exacta | $\partial_yM=\partial_xN$ | $df=M\,dx+N\,dy$ | $f(x,y)=C$ |
> | Inexacta | $\partial_yM\neq\partial_xN$ | factor $\mu$ | exacta |
> | Lineal | $y'+py=q$ | $\times\,e^{\int p}$ | integral directa |
> | Bernoulli | $y'+py=qy^n$ | $u=y^{1-n}$ | lineal |
> | Riccati | $y'+py^2+qy=r$ | $y=y_p+1/u$ | lineal |

> [!corolario]
> Resolver de primer orden es, en el fondo, **clasificar bien**. El 90 % del trabajo es reconocer a
> qué patrón pertenece la ecuación; el método correcto la convierte casi siempre en una integral.

> [!referencia]
> - Punto de partida: [[Variables Separables]] (a él reducen los demás).
> - El método más reutilizado: [[Lineal Primer Orden]] (factor integrante).
> - Geometría previa: [[../Fundamentos y Teoria Cualitativa/Campo de Direcciones e Isoclinas]].
