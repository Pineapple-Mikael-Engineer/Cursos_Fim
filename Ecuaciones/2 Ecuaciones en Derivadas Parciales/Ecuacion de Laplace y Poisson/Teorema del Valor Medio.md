---
title: Teorema del Valor Medio
order: 7
tags:
  - ecuaciones
  - edp
  - teoria
  - laplace
  - valor-medio
draft: false
aliases:
  - teorema del valor medio
  - propiedad del valor medio
  - mean value property
  - mean value theorem for harmonic functions
---

# Teorema del Valor Medio

> [!definicion]
> **Propiedad del valor medio.** Si $u$ es **armónica** ($\nabla^2u=0$) en un dominio que contiene la bola cerrada $\overline{B_r(P)}$, entonces el valor de $u$ en el centro $P$ es **exactamente el promedio** de sus valores sobre la esfera (o sobre toda la bola) centrada en $P$:
> $$u(P)=\frac{1}{|\partial B_r|}\int_{\partial B_r(P)}u\,dS=\frac{1}{|B_r|}\int_{B_r(P)}u\,dV.$$
> No hay error ni aproximación: el centro **es** la media de su entorno, para **cualquier** radio $r$ admisible.

> [!info]
> Resultado fundacional de la sección [[Ecuacion de Laplace y Poisson/index| Laplace y Poisson]], dentro del [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]]. Es la propiedad que **caracteriza** a las [[Funciones Armonicas| funciones armónicas]] y de la que se deducen el [[Principio del Maximo Eliptico| principio del máximo]], la unicidad de Dirichlet y la suavidad analítica. Su versión bidimensional ya aparece, de hecho, en la fórmula de [[Laplace en Disco| Poisson para el disco]].

---

## Ejemplo

> [!ejemplo]
> **Valor en el centro de un disco.** Sea $u$ armónica en el disco de radio $a$ con dato de frontera $u(a,\theta)=f(\theta)$. La [[Laplace en Disco| fórmula de Poisson]] evaluada en el centro $r=0$ se reduce drásticamente: el núcleo de Poisson en el centro es constante e igual a $\frac{1}{2\pi}$, de modo que
> $$u(0)=\frac{1}{2\pi}\int_0^{2\pi}f(\theta)\,d\theta.$$
> Es decir, **el valor en el centro es el promedio del dato de frontera** —el caso 2D del teorema, leído directamente de la solución explícita—. Si, por ejemplo, $f(\theta)=3+5\cos\theta$, el promedio del coseno sobre un período es cero, así que $u(0)=3$ sin necesidad de calcular nada más en el interior.

---

## En qué consiste

> [!teoria]
> El teorema convierte una ecuación diferencial (local) en una identidad **integral** (global): ser armónica equivale a "no tener grumos", a que cada punto sea la media perfecta de los que lo rodean. Geométricamente, una función armónica es la posición de equilibrio de una membrana elástica: cada punto se asienta exactamente a la altura promedio de su vecindad. Esta es la razón profunda de casi todas las propiedades de lo armónico —máximo en la frontera, suavidad, unicidad—: todas son corolarios de "soy mi propio promedio".

> [!teorema] Propiedad del valor medio
> Si $u$ es armónica en un abierto que contiene $\overline{B_R(P)}$, entonces para todo $0<r\le R$ se cumple $\displaystyle u(P)=\frac{1}{|\partial B_r|}\int_{\partial B_r(P)}u\,dS$.

> [!demostracion]
> Usamos el **teorema de la divergencia** (identidad de Green).
>
> **Paso 1 — Definir el promedio.** Para $P$ fijo, definimos la función del radio
> $$\bar u(r)=\frac{1}{|\partial B_r|}\int_{\partial B_r(P)}u\,dS=\frac{1}{|\partial B_1|}\int_{|\omega|=1}u(P+r\omega)\,dS(\omega),$$
> donde en la segunda forma hemos parametrizado la esfera por vectores unitarios $\omega$, eliminando la dependencia de $r$ del dominio de integración.
>
> **Paso 2 — Derivar respecto de $r$.** Derivando bajo la integral,
> $$\bar u'(r)=\frac{1}{|\partial B_1|}\int_{|\omega|=1}\nabla u(P+r\omega)\cdot\omega\,dS(\omega)=\frac{1}{|\partial B_r|}\int_{\partial B_r(P)}\frac{\partial u}{\partial n}\,dS,$$
> pues $\omega$ es la normal exterior. Por el teorema de la divergencia, este flujo iguala la integral del laplaciano en la bola:
> $$\bar u'(r)=\frac{1}{|\partial B_r|}\int_{B_r(P)}\nabla^2u\,dV=0,$$
> porque $u$ es **armónica** ($\nabla^2u=0$).
>
> **Paso 3 — Concluir.** Como $\bar u'(r)\equiv0$, la función $\bar u$ es **constante** en $r$. Tomando el límite $r\to0^+$ y usando la continuidad de $u$, ese valor constante es $\bar u(0^+)=u(P)$. Por tanto $\bar u(r)=u(P)$ para todo $r$ admisible, que es la igualdad buscada. La versión con bola sólida se obtiene integrando la de esferas sobre $r$. $\blacksquare$

> [!corolario] Recíproco y consecuencias
> El recíproco también es cierto: **si $u$ es continua y satisface la propiedad del valor medio para toda bola pequeña, entonces $u$ es armónica**. Así, la propiedad del valor medio es **equivalente** a la armonicidad —puede tomarse como definición—. De esta caracterización integral se desprenden directamente:
> - el [[Principio del Maximo Eliptico| principio del máximo]] (un máximo interior obligaría a $u$ a ser constante en torno suyo);
> - la **suavidad analítica**: aunque solo se pida $u$ continua, el promediado fuerza que $u$ sea $C^\infty$ e incluso analítica en el interior;
> - las **estimaciones de derivadas** y el **teorema de Liouville** (una armónica acotada en todo $\mathbb{R}^n$ es constante).

> [!proposicion] Submedia y supermedia
> El argumento se generaliza por desigualdades. Si $\nabla^2u\ge0$ ($u$ **subarmónica**), entonces $\bar u'(r)\ge0$ y $u(P)\le$ promedio: la función queda **por debajo** de su media. Si $\nabla^2u\le0$ ($u$ **superarmónica**), $u(P)\ge$ promedio. El caso armónico ($=0$) es la frontera entre ambos: igualdad exacta. Esta es la base de la teoría de funciones sub/superarmónicas y del método de Perron.

> [!warning]
> El radio $r$ debe ser tal que **toda** la bola $\overline{B_r(P)}$ quede dentro del dominio de armonicidad; cerca de la frontera el teorema no aplica con radios grandes. Además, la propiedad relaciona el centro con su esfera completa: **no** dice que $u$ sea constante, solo que su valor central coincide con el promedio. Una armónica no trivial sí varía de punto a punto.

---

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Enunciado | $u$ armónica $\Rightarrow u(P)=$ promedio sobre $\partial B_r(P)$ |
> | Forma | $u(P)=\dfrac{1}{\|\partial B_r\|}\displaystyle\int_{\partial B_r}u\,dS$ |
> | Prueba | definir $\bar u(r)$; $\bar u'(r)=\frac{1}{\|\partial B_r\|}\int_{B_r}\nabla^2u\,dV=0$ |
> | Recíproco | valor medio $\Rightarrow$ armónica (equivalencia) |
> | Caso 2D | valor en el centro del disco = promedio del dato de frontera |
> | Deriva | principio del máximo, suavidad analítica, Liouville |

> [!corolario]
> La propiedad del valor medio es el **corazón** de la teoría elíptica: condensa en una identidad integral todo el carácter de lo armónico. De ella brotan el principio del máximo, la unicidad de Dirichlet y la suavidad infinita. "Ser armónica" no es más que "ser, en cada punto, el promedio exacto del entorno".

> [!referencia]
> - Su consecuencia inmediata: [[Principio del Maximo Eliptico]].
> - El objeto que caracteriza: [[Funciones Armonicas]].
> - Donde aparece su versión 2D explícita: [[Laplace en Disco]].
> - El marco general de la sección: [[Ecuacion de Laplace y Poisson/index]].
