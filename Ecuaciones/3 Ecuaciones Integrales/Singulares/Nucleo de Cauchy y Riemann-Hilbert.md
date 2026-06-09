---
title: Núcleo de Cauchy y Riemann-Hilbert
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - singulares
  - analisis-complejo
draft: false
aliases:
  - núcleo de Cauchy
  - ecuación integral singular de Cauchy
  - problema de Riemann-Hilbert
  - fórmulas de Sokhotski-Plemelj
  - Cauchy singular integral equation
  - Riemann-Hilbert problem
---

# Núcleo de Cauchy y Riemann-Hilbert

> [!definicion]
> Una **ecuación integral singular de Cauchy** tiene el núcleo $1/(t-x)$, que sobre la diagonal $t=x$ no
> es siquiera integrable: hay que entenderla como **valor principal**. Su forma estándar (ecuación
> dominante) sobre un contorno suave $L$ es
> $$a(x)\,\varphi(x)+\frac{b(x)}{\pi i}\,\operatorname{vp}\!\int_L\frac{\varphi(t)}{t-x}\,dt=f(x),
> \qquad x\in L,$$
> donde $a,b,f$ son datos dados sobre $L$ y $\varphi$ es la incógnita. El término $\dfrac{1}{\pi i}
> \operatorname{vp}\!\int_L\dfrac{\varphi(t)}{t-x}\,dt$ es la **transformada de Hilbert** (operador
> singular de Cauchy $S\varphi$). A diferencia de [[Fredholm/index| Fredholm]], el operador $S$ es
> **acotado pero no compacto**, y por eso la teoría es la del **análisis complejo**, no la espectral.

> [!info]
> Sección [[Singulares/index| Singulares]] del capítulo
> [[3 Ecuaciones Integrales/index| Ecuaciones Integrales]]. Es la frontera $\alpha=1$ de las singulares:
> un paso más fuerte que la [[Ecuacion de Abel Generalizada| Abel generalizada]] ($\alpha<1$) y la base
> del [[Metodo de Wiener-Hopf| método de Wiener-Hopf]] (que es el caso particular $L=$ recta real con
> núcleo de convolución). La herramienta central son las **fórmulas de Sokhotski-Plemelj**. Fuente:
> **Krasnov, Kiseliov, Makarenko**, *Ecuaciones integrales* (panorama; el tratado de referencia es
> Muskhelishvili).

---

## Ejemplo

> [!ejemplo] El salto de Plemelj a través del contorno
> ![[plemelj_cauchy.svg|470]]
>
> La **integral de Cauchy** $\Phi(z)=\dfrac{1}{2\pi i}\displaystyle\int_L\dfrac{\varphi(t)}{t-z}\,dt$ es
> una función **analítica** de $z$ a ambos lados del contorno $L$ (a la izquierda define una rama
> $\Phi^+$, a la derecha otra $\Phi^-$). Cuando $z$ se acerca a un punto $x\in L$ desde cada lado, los
> valores límite $\Phi^+(x)$ y $\Phi^-(x)$ **no coinciden**: difieren exactamente en $\varphi(x)$, el
> **salto**. Resolver la ecuación singular equivale a **reconstruir $\Phi$ a partir de su salto** sobre
> $L$, un problema de contorno para una función analítica.

---

## En qué consiste

> [!teorema] Fórmulas de Sokhotski-Plemelj
> Sea $\varphi$ una función que cumple una condición de Hölder sobre el contorno suave $L$, y sea
> $$\Phi(z)=\frac{1}{2\pi i}\int_L\frac{\varphi(t)}{t-z}\,dt,\qquad z\notin L,$$
> su integral de Cauchy (analítica en $\mathbb{C}\setminus L$). Entonces los **valores de frontera** desde
> cada lado existen y valen
> $$\Phi^{\pm}(x)=\pm\frac12\,\varphi(x)+\frac{1}{2\pi i}\,\operatorname{vp}\!\int_L\frac{\varphi(t)}{t-x}\,dt,
> \qquad x\in L.$$
> En consecuencia, **suma** y **salto**:
> $$\Phi^+(x)-\Phi^-(x)=\varphi(x),\qquad
> \Phi^+(x)+\Phi^-(x)=\frac{1}{\pi i}\,\operatorname{vp}\!\int_L\frac{\varphi(t)}{t-x}\,dt.$$

> [!demostracion]
> **Paso 1 — Aislar la singularidad.** Para $z$ cerca de $x_0\in L$ escribimos
> $$\Phi(z)=\frac{1}{2\pi i}\int_L\frac{\varphi(t)-\varphi(x_0)}{t-z}\,dt
> +\frac{\varphi(x_0)}{2\pi i}\int_L\frac{dt}{t-z}.$$
> La primera integral tiene núcleo **acotado** (la condición de Hölder garantiza
> $|\varphi(t)-\varphi(x_0)|\le C|t-x_0|^{\mu}$), así que es **continua** al cruzar $L$ y su límite es el
> valor principal del término correspondiente.
>
> **Paso 2 — El término elemental aporta el salto.** La segunda integral
> $\frac{1}{2\pi i}\int_L\frac{dt}{t-z}$ es el **número de vueltas** del contorno respecto de $z$: vale
> $1$ cuando $z$ está del lado $+$ (encerrado por la porción local) y $0$ del lado $-$; sobre el propio
> $L$ su valor principal es $\tfrac12$ (la mitad de un giro). Por tanto su límite por el lado $\pm$ es
> $\tfrac12\pm\tfrac12$.
>
> **Paso 3 — Recomponer.** Sumando ambos pedazos,
> $$\Phi^{\pm}(x_0)=\frac{1}{2\pi i}\operatorname{vp}\!\int_L\frac{\varphi(t)-\varphi(x_0)}{t-x_0}\,dt
> +\varphi(x_0)\Big(\tfrac12\pm\tfrac12\Big)
> =\pm\tfrac12\varphi(x_0)+\frac{1}{2\pi i}\operatorname{vp}\!\int_L\frac{\varphi(t)}{t-x_0}\,dt.$$
> Restando los dos signos se cancela la integral y queda $\Phi^+-\Phi^-=\varphi$. $\blacksquare$

> [!teoria] El problema de Riemann-Hilbert (panorama)
> Las fórmulas de Plemelj **traducen** la ecuación singular en un problema de **contorno** para funciones
> analíticas. La idea: buscar una función $\Phi(z)$, analítica fuera de $L$ y que se anule en el infinito,
> cuyos valores de frontera satisfagan una **condición de salto** prescrita
> $$\Phi^+(x)=G(x)\,\Phi^-(x)+g(x),\qquad x\in L,$$
> donde $G,g$ se construyen a partir de $a,b,f$ (concretamente $G=(a-b)/(a+b)$). Recuperada $\Phi$, la
> solución es $\varphi=\Phi^+-\Phi^-$.
>
> **Factorización.** El caso homogéneo ($g\equiv0$) pide $\Phi^+=G\,\Phi^-$; se resuelve **factorizando**
> $G$ como cociente de valores de frontera de una función $X$ sin ceros,
> $$G(x)=\frac{X^+(x)}{X^-(x)},\qquad X(z)=\exp\!\Big(\frac{1}{2\pi i}\int_L\frac{\log G(t)}{t-z}\,dt\Big).$$
> Entonces $\Phi^+/X^+=\Phi^-/X^-$ pega ambos lados en una **única** función entera, que por su
> comportamiento en $\infty$ es un **polinomio**. El **índice** (winding number)
> $\kappa=\dfrac{1}{2\pi}\big[\arg G\big]_L$ —cuántas veces gira $G$ al recorrer $L$— decide el grado de
> ese polinomio: si $\kappa>0$ hay $\kappa$ soluciones libres; si $\kappa<0$ hay $-\kappa$ condiciones de
> solubilidad. Es el **análogo singular de la alternativa de Fredholm**, pero contado por un entero
> topológico.

> [!info] Aplicaciones
> El problema de Riemann-Hilbert es ubicuo donde aparece una **distribución desconocida sobre una línea**:
> - **Aerodinámica**: la teoría del **perfil alar** delgado (ecuación de la circulación) es una singular
>   de Cauchy sobre la cuerda.
> - **Elasticidad / fractura**: campos de tensión alrededor de **grietas**; la apertura de la grieta es el
>   salto de una función analítica (Muskhelishvili).
> - **Dispersión y sistemas integrables**: la transformada inversa de scattering y la asintótica de
>   Painlevé se formulan como problemas de Riemann-Hilbert matriciales.

> [!warning]
> El valor principal es **imprescindible**: sin él la integral diverge. Y el signo del núcleo importa:
> $1/(t-x)$ define el salto $\Phi^+-\Phi^-=+\varphi$; con $1/(x-t)$ cambia el signo. La condición de
> **Hölder** (no basta continuidad) es la hipótesis que hace existir los valores de frontera.

## Resumen

> [!resumen]
> | Objeto | Expresión | Papel |
> |---|---|---|
> | Ecuación dominante | $a\varphi+\dfrac{b}{\pi i}\operatorname{vp}\!\int_L\dfrac{\varphi}{t-x}dt=f$ | singular de Cauchy ($\alpha=1$) |
> | Integral de Cauchy | $\Phi(z)=\dfrac{1}{2\pi i}\int_L\dfrac{\varphi(t)}{t-z}dt$ | analítica fuera de $L$ |
> | Plemelj | $\Phi^{\pm}=\pm\tfrac12\varphi+\dfrac{1}{2\pi i}\operatorname{vp}\!\int_L\dfrac{\varphi}{t-x}dt$ | valores de frontera |
> | Salto | $\Phi^+-\Phi^-=\varphi$ | reconstruir $\varphi$ desde el salto |
> | Riemann-Hilbert | $\Phi^+=G\Phi^-+g$, $\ G=\dfrac{a-b}{a+b}$ | problema de contorno |
> | Índice | $\kappa=\dfrac{1}{2\pi}[\arg G]_L$ | número de soluciones / condiciones |

> [!corolario]
> Una ecuación singular de Cauchy se convierte, vía **Sokhotski-Plemelj**, en un **problema de
> Riemann-Hilbert**: hallar una función analítica cuyo salto a través de $L$ esté prescrito. Se resuelve
> **factorizando** $G=X^+/X^-$, y el **índice** (número de giro de $G$) juega el papel del entero que en
> Fredholm decide la alternativa. El análisis complejo —no el espectro— gobierna este mundo.

> [!referencia]
> - El caso débilmente singular previo: [[Ecuacion de Abel Generalizada]].
> - La versión sobre la recta con convolución: [[Metodo de Wiener-Hopf]].
> - El mapa de la sección: [[Singulares/index]].
