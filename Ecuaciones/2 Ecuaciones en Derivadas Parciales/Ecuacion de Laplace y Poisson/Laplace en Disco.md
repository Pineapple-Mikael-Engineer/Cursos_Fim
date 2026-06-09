---
title: Laplace en Disco
tags:
  - ecuaciones
  - edp
  - teoria
  - laplace
  - poisson
draft: false
aliases:
  - Laplace en un disco
  - fórmula de Poisson
  - núcleo de Poisson
  - Poisson integral formula
  - Laplace on a disk
---

# Laplace en Disco

> [!definicion]
> En el **disco** de radio $a$ conviene usar **coordenadas polares**, donde el laplaciano es
> $$\nabla^2u=u_{rr}+\frac1r\,u_r+\frac1{r^2}\,u_{\theta\theta}=0.$$
> La [[Tecnica de Separacion| separación]] $u=R(r)\,\Theta(\theta)$ da dos problemas acoplados por
> la constante $n^2$. La parte angular $\Theta''+n^2\Theta=0$ debe ser **periódica**
> ($\Theta(\theta+2\pi)=\Theta(\theta)$), lo que cuantiza $n=0,1,2,\dots$ y da
> $\Theta_n=\{\cos n\theta,\ \operatorname{sen} n\theta\}$. La parte radial es la ecuación
> equidimensional $r^2R''+rR'-n^2R=0$, con soluciones $r^{\pm n}$; se descarta $r^{-n}$ por
> singular en el centro, y queda $R_n=r^n$ (con $R_0=1$).

> [!info]
> Es el caso "estrella" de Laplace en geometría curva, dentro del
> [[Ecuacion de Laplace y Poisson/index| bloque de Laplace y Poisson]]. Contrasta con
> [[Laplace en Rectangulo]] (cartesiano, $\sinh$/$\cosh$); aquí la periodicidad angular sustituye a
> los bordes y la regularidad en el centro elige la solución radial. La serie se cierra en la
> **fórmula integral de Poisson**, conectándose con el [[Teorema del Valor Medio]].

---

## Ejemplo

> [!ejemplo] El núcleo de Poisson
> ![[nucleo_poisson.svg|460]]
>
> Para un punto interior cerca de la frontera, el núcleo de Poisson se concentra frente al punto más
> próximo del borde: la solución es un promedio ponderado del dato de frontera.
>
> **Problema.** Resolver $\nabla^2u=0$ en el disco $r\le a$ con dato de frontera $u(a,\theta)=f(\theta)$.
>
> **Paso 1 — Solución en serie.** Superponiendo las soluciones separadas $r^n\cos n\theta$ y
> $r^n\operatorname{sen} n\theta$, y reescalando con $r^n\to (r/a)^n$ para trabajar con valores en el
> borde:
> $$u(r,\theta)=\frac{a_0}{2}+\sum_{n=1}^\infty\Big(\frac{r}{a}\Big)^n\big(a_n\cos n\theta+b_n\operatorname{sen} n\theta\big).$$
>
> **Paso 2 — Ajustar el dato.** En $r=a$ los factores $(r/a)^n$ valen $1$, así que
> $$f(\theta)=\frac{a_0}{2}+\sum_{n=1}^\infty\big(a_n\cos n\theta+b_n\operatorname{sen} n\theta\big).$$
> Esta es exactamente la **serie de Fourier** de $f$ en el círculo, de modo que
> $$a_n=\frac1\pi\int_0^{2\pi}f(\phi)\cos n\phi\,d\phi,\qquad
> b_n=\frac1\pi\int_0^{2\pi}f(\phi)\operatorname{sen} n\phi\,d\phi.$$
> Con esto el problema queda resuelto: la armónica en el interior es la **prolongación** del dato de
> frontera amortiguando cada modo por $(r/a)^n$.

---

## En qué consiste

> [!teorema] Fórmula integral de Poisson
> Sustituyendo los coeficientes de Fourier en la serie y sumando la serie geométrica resultante, la
> solución del problema de Dirichlet en el disco se escribe como una **integral**:
> $$u(r,\theta)=\frac{1}{2\pi}\int_0^{2\pi}
> \frac{a^2-r^2}{a^2-2ar\cos(\theta-\phi)+r^2}\,f(\phi)\,d\phi.$$
> El factor
> $$P(r,\theta-\phi)=\frac{a^2-r^2}{a^2-2ar\cos(\theta-\phi)+r^2}$$
> es el **núcleo de Poisson**: pondera cada valor de frontera $f(\phi)$ según la **cercanía** del
> punto interior $(r,\theta)$ al punto del borde $(a,\phi)$.

> [!demostracion]
> **Paso 1 — Insertar Fourier en la serie.** Metemos $a_n,b_n$ en la serie y agrupamos:
> $$u(r,\theta)=\frac{1}{2\pi}\int_0^{2\pi}f(\phi)
> \Big[1+2\sum_{n=1}^\infty\Big(\frac ra\Big)^n\cos n(\theta-\phi)\Big]d\phi,$$
> usando $\cos n\theta\cos n\phi+\operatorname{sen} n\theta\operatorname{sen} n\phi=\cos n(\theta-\phi)$.
>
> **Paso 2 — Sumar la serie geométrica.** Con $\rho=r/a<1$ y $\psi=\theta-\phi$, escribimos el
> corchete como parte real de una serie geométrica compleja:
> $$1+2\sum_{n=1}^\infty\rho^n\cos n\psi
> =\operatorname{Re}\Big(1+2\sum_{n=1}^\infty(\rho e^{i\psi})^n\Big)
> =\operatorname{Re}\frac{1+\rho e^{i\psi}}{1-\rho e^{i\psi}}.$$
>
> **Paso 3 — Racionalizar.** Multiplicando numerador y denominador por el conjugado
> $1-\rho e^{-i\psi}$ y tomando la parte real,
> $$\operatorname{Re}\frac{1+\rho e^{i\psi}}{1-\rho e^{i\psi}}
> =\frac{1-\rho^2}{1-2\rho\cos\psi+\rho^2}.$$
>
> **Paso 4 — Volver a $r,a$.** Sustituyendo $\rho=r/a$ y multiplicando arriba y abajo por $a^2$,
> $$\frac{1-\rho^2}{1-2\rho\cos\psi+\rho^2}=\frac{a^2-r^2}{a^2-2ar\cos(\theta-\phi)+r^2},$$
> que es justo el núcleo de Poisson. Queda la fórmula integral del teorema. $\blacksquare$

> [!info] Cómo leer el núcleo de Poisson
> El núcleo $P\ge0$ y su integral angular vale $2\pi$, así que la fórmula es un **promedio ponderado
> verdadero** del dato de frontera. Al acercarse al borde ($r\to a$) por la dirección $\theta$, el
> denominador se anula frente a $\phi=\theta$ y $P$ se concentra como una "delta" sobre el punto más
> cercano: la solución recupera con fidelidad el dato $f(\theta)$. Lejos del borde el núcleo es casi
> plano y la solución se parece más a un promedio uniforme.

> [!corolario] Valor medio en el centro
> Evaluando en el centro $r=0$, el núcleo se vuelve constante ($P=1$) y
> $$u(0)=\frac{1}{2\pi}\int_0^{2\pi}f(\phi)\,d\phi.$$
> El valor en el centro es **exactamente el promedio** del dato de frontera: la **propiedad del
> valor medio** de las funciones armónicas, ahora como caso particular de Poisson.

## Resumen

> [!resumen]
> | Elemento | Contenido |
> |---|---|
> | Laplaciano polar | $u_{rr}+\frac1r u_r+\frac1{r^2}u_{\theta\theta}=0$ |
> | Separadas | $\Theta_n=\cos n\theta,\operatorname{sen} n\theta$; $R_n=r^n$ (regular) |
> | Serie | $u=\frac{a_0}{2}+\sum_n (r/a)^n(a_n\cos n\theta+b_n\operatorname{sen} n\theta)$ |
> | Coeficientes | Fourier de $f$ en el círculo |
> | Poisson | $u=\frac1{2\pi}\int_0^{2\pi}\frac{a^2-r^2}{a^2-2ar\cos(\theta-\phi)+r^2}f\,d\phi$ |
> | Centro | $u(0)=$ promedio de $f$ (valor medio) |

> [!corolario]
> En el disco, la **periodicidad** angular reemplaza a las condiciones de borde laterales y la
> **regularidad** en el centro elige $r^n$. La serie de Fourier de $f$ resuelve el problema, y al
> sumarla aparece el núcleo de Poisson: una sola integral que **promedia ponderadamente** la
> frontera y contiene, en su centro, la propiedad del valor medio.

> [!referencia]
> - El contraste cartesiano: [[Laplace en Rectangulo]].
> - El centro como promedio: [[Teorema del Valor Medio]].
> - Las funciones que aparecen en geometrías más ricas: [[Funciones Especiales/index]].
> - Marco general: [[Ecuacion de Laplace y Poisson/index]].
