---
title: Flujo Potencial
order: 3
tags:
  - fluidos
  - teoria
  - flujo-ideal
draft: false
aliases:
  - Flujo potencial
  - Potencial de velocidad
  - Flujo irrotacional
---

# Flujo Potencial $\vec v=\nabla\phi,\quad \nabla^2\phi=0$

> [!definicion] Flujo potencial
> Un flujo es **potencial** (o **irrotacional**) cuando su campo de velocidades $\vec v$ deriva de una **función escalar** $\phi(\vec r,t)$, llamada **potencial de velocidad**, mediante
> $$\boxed{\;\vec v=\nabla\phi\;}$$
> Equivalentemente, la **vorticidad** es nula en todo el dominio:
> $$\vec\omega=\nabla\times\vec v=\vec 0.$$
> Si, además, el fluido es **incompresible** ($\nabla\cdot\vec v=0$), el potencial satisface la **ecuación de Laplace**
> $$\boxed{\;\nabla^2\phi=0\;}$$
> y el problema dinámico se reduce a un problema **puramente geométrico y lineal** de teoría de potencial.

> [!info] Ubicación y enlaces
> - **Sección:** [[4 Flujo Ideal/index | 4. Flujo Ideal]].
> - **Notas hermanas:** [[Ecuacion de Bernoulli | Ecuación de Bernoulli]], [[Vorticidad y Teoremas | Vorticidad y Teoremas]].
> - **Prerrequisito cinemático:** [[Deformacion y Vorticidad | Deformación y Vorticidad]] (definición de $\vec\omega$).
> - **Referencia:** Landau & Lifshitz, *Fluid Mechanics* (Vol. 6), §§9–11.
> - **Idea clave:** irrotacional $\Rightarrow$ existe $\phi$; irrotacional + incompresible $\Rightarrow$ $\nabla^2\phi=0$ (lineal $\Rightarrow$ **superposición**).

---

## Existencia del potencial de velocidad

> [!teorema] Existencia del potencial
> Sea $\vec v$ un campo de velocidades definido en una región **simplemente conexa** $\mathcal D$. Si el flujo es **irrotacional**, $\vec\omega=\nabla\times\vec v=\vec 0$ en $\mathcal D$, entonces existe una función escalar $\phi$ tal que
> $$\vec v=\nabla\phi.$$

> [!demostracion] Existencia por circulación nula
> **Paso 1 — Vorticidad nula y circulación.** Tomemos una curva cerrada $C$ cualquiera, frontera de una superficie $S\subset\mathcal D$. La **circulación** de $\vec v$ a lo largo de $C$ es, por el **teorema de Stokes**,
> $$\oint_C \vec v\cdot d\vec\ell=\iint_S (\nabla\times\vec v)\cdot d\vec S=\iint_S \vec\omega\cdot d\vec S.$$
> Como $\vec\omega=\vec 0$ en todo $\mathcal D$ y la región es simplemente conexa (toda $C$ borda una $S$ interior),
> $$\oint_C \vec v\cdot d\vec\ell=0\qquad\text{para toda curva cerrada }C.$$
>
> **Paso 2 — La integral de línea no depende del camino.** Sean dos puntos $A$ y $B$ y dos caminos $\Gamma_1,\Gamma_2$ de $A$ a $B$. El lazo cerrado $\Gamma_1$ seguido de $\Gamma_2$ invertido tiene circulación nula, luego
> $$\int_{\Gamma_1}\vec v\cdot d\vec\ell-\int_{\Gamma_2}\vec v\cdot d\vec\ell=0\;\Longrightarrow\;\int_{\Gamma_1}\vec v\cdot d\vec\ell=\int_{\Gamma_2}\vec v\cdot d\vec\ell.$$
> La integral solo depende de los extremos.
>
> **Paso 3 — Construcción del potencial.** Fijamos un punto base $\vec r_0$ y definimos
> $$\phi(\vec r)\equiv\int_{\vec r_0}^{\vec r}\vec v\cdot d\vec\ell,$$
> que está bien definido por el Paso 2. Por el **teorema del gradiente** (o, en una variable, el teorema fundamental del cálculo aplicado a cada coordenada), un desplazamiento infinitesimal $d\vec r$ produce
> $$d\phi=\vec v\cdot d\vec r=\nabla\phi\cdot d\vec r\quad\text{para todo }d\vec r,$$
> de donde $\vec v=\nabla\phi$.
>
> **Paso 4 — Recíproco (consistencia).** Si $\vec v=\nabla\phi$, entonces $\nabla\times\vec v=\nabla\times\nabla\phi=\vec 0$ por la identidad vectorial universal $\nabla\times\nabla\phi=\vec 0$ (las derivadas parciales cruzadas conmutan). Así, la existencia del potencial **equivale** a la irrotacionalidad. $\blacksquare$

> [!warning] Regiones multiplemente conexas
> En dominios **no** simplemente conexos (p. ej. el exterior de un cilindro), una curva que rodea el agujero no borda una superficie interior, y la circulación $\Gamma=\oint_C\vec v\cdot d\vec\ell$ puede ser **no nula** aunque $\vec\omega=\vec 0$. Entonces $\phi$ es **multivaluado** (salta $\Gamma$ por vuelta). Esto es precisamente lo que permite el **vórtice** y la **sustentación**.

---

## Reducción a la ecuación de Laplace

> [!teorema] Flujo potencial incompresible
> Si el flujo es irrotacional ($\vec v=\nabla\phi$) **e** incompresible ($\nabla\cdot\vec v=0$), entonces el potencial satisface la ecuación de Laplace
> $$\nabla^2\phi=0,$$
> con la condición de contorno de **no penetración** (deslizamiento) sobre las paredes:
> $$\frac{\partial\phi}{\partial n}=\nabla\phi\cdot\hat n=\vec v\cdot\hat n\quad\text{(dada)}.$$

> [!demostracion] De la incompresibilidad a Laplace
> **Paso 1 — Sustituir el potencial en la continuidad.** La incompresibilidad es
> $$\nabla\cdot\vec v=0.$$
> Reemplazando $\vec v=\nabla\phi$,
> $$\nabla\cdot(\nabla\phi)=0.$$
>
> **Paso 2 — Identificar el laplaciano.** Por definición del operador,
> $$\nabla\cdot\nabla\phi=\frac{\partial^2\phi}{\partial x^2}+\frac{\partial^2\phi}{\partial y^2}+\frac{\partial^2\phi}{\partial z^2}\equiv\nabla^2\phi.$$
> Luego
> $$\nabla^2\phi=0.\qquad\blacksquare$$

> [!regla] El problema se vuelve lineal
> La ecuación de Laplace es **lineal y homogénea**. Por tanto, si $\phi_1$ y $\phi_2$ son soluciones, también lo es cualquier combinación
> $$\phi=\alpha\,\phi_1+\beta\,\phi_2.$$
> Esto habilita el **principio de superposición**: flujos complicados se construyen **sumando** soluciones elementales. La no linealidad de Navier–Stokes (el término convectivo $(\vec v\cdot\nabla)\vec v$) se ha esquivado por completo: ya no aparece en la ecuación para $\phi$ (se reabsorbe en la presión vía [[Ecuacion de Bernoulli | Bernoulli]]).

---

## Función de corriente y potencial complejo (2D)

> [!proposicion] Función de corriente
> En un flujo plano e incompresible existe una **función de corriente** $\psi(x,y)$ tal que
> $$u=\frac{\partial\psi}{\partial y},\qquad v=-\frac{\partial\psi}{\partial x}.$$
> Satisface la continuidad **automáticamente** y, si el flujo es irrotacional, también $\nabla^2\psi=0$. Las curvas $\psi=\text{cte}$ son **líneas de corriente**, y son **ortogonales** a las equipotenciales $\phi=\text{cte}$.

> [!demostracion] Propiedades de $\psi$
> **Paso 1 — Continuidad automática.** Con $u=\partial_y\psi$, $v=-\partial_x\psi$,
> $$\nabla\cdot\vec v=\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}=\frac{\partial^2\psi}{\partial x\,\partial y}-\frac{\partial^2\psi}{\partial y\,\partial x}=0,$$
> por igualdad de las derivadas cruzadas. Cualquier $\psi$ suave da un campo incompresible.
>
> **Paso 2 — Laplace para $\psi$.** La componente $z$ de la vorticidad en 2D es
> $$\omega_z=\frac{\partial v}{\partial x}-\frac{\partial u}{\partial y}=-\frac{\partial^2\psi}{\partial x^2}-\frac{\partial^2\psi}{\partial y^2}=-\nabla^2\psi.$$
> Si el flujo es irrotacional, $\omega_z=0\Rightarrow\nabla^2\psi=0$.
>
> **Paso 3 — Ortogonalidad de $\phi$ y $\psi$.** Comparando $\vec v=\nabla\phi$ con la definición de $\psi$,
> $$u=\frac{\partial\phi}{\partial x}=\frac{\partial\psi}{\partial y},\qquad v=\frac{\partial\phi}{\partial y}=-\frac{\partial\psi}{\partial x},$$
> que son las **ecuaciones de Cauchy–Riemann**. Sus gradientes cumplen
> $$\nabla\phi\cdot\nabla\psi=\frac{\partial\phi}{\partial x}\frac{\partial\psi}{\partial x}+\frac{\partial\phi}{\partial y}\frac{\partial\psi}{\partial y}=u(-v)+v\,u=0.$$
> Las familias $\phi=\text{cte}$ y $\psi=\text{cte}$ se cortan en ángulo recto. $\blacksquare$

> [!info] Potencial complejo
> Como $\phi$ y $\psi$ obedecen Cauchy–Riemann, el **potencial complejo**
> $$w(z)=\phi(x,y)+i\,\psi(x,y),\qquad z=x+iy,$$
> es una función **analítica** de $z$. La velocidad se obtiene de
> $$\frac{dw}{dz}=u-iv.$$
> Toda la maquinaria de variable compleja (transformaciones conformes) queda disponible para resolver flujos planos.

---

## Soluciones elementales (superponibles)

> [!teoria] Catálogo básico
> Por linealidad, se construyen flujos sumando estos ladrillos (en 2D; $r,\theta$ polares):
>
> | Flujo | Potencial $\phi$ | Corriente $\psi$ | Descripción |
> \|---\|---\|---\|---\|
> | Uniforme | $U\,x=U r\cos\theta$ | $U\,y=U r\sin\theta$ | Corriente libre a velocidad $U$ |
> | Fuente / sumidero | $\dfrac{m}{2\pi}\ln r$ | $\dfrac{m}{2\pi}\,\theta$ | Caudal $m$ emanando ($m>0$) o absorbido ($m<0$) |
> | Vórtice | $\dfrac{\Gamma}{2\pi}\,\theta$ | $-\dfrac{\Gamma}{2\pi}\ln r$ | Circulación $\Gamma$, velocidad $v_\theta=\Gamma/2\pi r$ |
> | Dipolo (*doublet*) | $\dfrac{\mu\cos\theta}{2\pi r}$ | $-\dfrac{\mu\sin\theta}{2\pi r}$ | Límite fuente+sumidero juntos; intensidad $\mu$ |
>
> Cada uno satisface $\nabla^2\phi=0$ (salvo en su singularidad central). La **suma** de varios sigue siendo solución de Laplace.

---

## En qué consiste

La estrategia del flujo potencial es **cambiar de incógnita**: en vez de resolver las tres componentes acopladas y no lineales de $\vec v$, se resuelve **una sola** ecuación lineal, $\nabla^2\phi=0$, para un escalar. Una vez hallado $\phi$:

1. La **velocidad** sale por derivación, $\vec v=\nabla\phi$.
2. La **presión** sale por [[Ecuacion de Bernoulli | Bernoulli]], $p+\tfrac12\rho v^2+\rho g z=\text{cte}$, una vez conocido $v$.

El precio es físico, no matemático: se **descarta la viscosidad** y se exige irrotacionalidad. Resulta una excelente aproximación **lejos** de las paredes y para cuerpos esbeltos, donde la capa de fluido afectada por la viscosidad es delgada. Cerca del cuerpo (capa límite, estela) el modelo falla, como anuncia la paradoja de d'Alembert más abajo.

---

## Aplicación estelar: flujo alrededor de un cilindro

![[flujo_cilindro.svg|460]]

*Flujo potencial alrededor de un cilindro de radio $a$: las líneas de corriente son simétricas adelante–atrás, los puntos de estancamiento se sitúan en $\theta=0$ y $\theta=\pi$, y la fuerza neta de arrastre es **nula** (paradoja de d'Alembert).*

Superponemos un **flujo uniforme** $U$ (en $+x$) y un **dipolo** de eje $x$ con intensidad ajustada $\mu=2\pi U a^2$. El potencial resultante, en polares, es
$$\phi(r,\theta)=U\cos\theta\left(r+\frac{a^2}{r}\right).$$

> [!demostracion] El cilindro $r=a$ es una línea de corriente
> **Paso 1 — Velocidad en polares.** De $\vec v=\nabla\phi$, las componentes son
> $$v_r=\frac{\partial\phi}{\partial r}=U\cos\theta\left(1-\frac{a^2}{r^2}\right),\qquad v_\theta=\frac1r\frac{\partial\phi}{\partial\theta}=-U\sin\theta\left(1+\frac{a^2}{r^2}\right).$$
>
> **Paso 2 — Componente radial en la pared.** Evaluamos $v_r$ en $r=a$:
> $$v_r\big|_{r=a}=U\cos\theta\left(1-\frac{a^2}{a^2}\right)=U\cos\theta\,(1-1)=0.$$
> El fluido **no penetra** la superficie $r=a$: es una línea de corriente, que identificamos con el contorno del cilindro. Se cumple la condición de frontera $\partial\phi/\partial n=0$. $\blacksquare$

> [!solucion] Velocidad superficial y puntos de estancamiento
> **Velocidad tangencial sobre el cilindro.** En $r=a$,
> $$v_\theta\big|_{r=a}=-U\sin\theta\left(1+1\right)=-2U\sin\theta.$$
> La rapidez del fluido sobre la superficie es $|v_\theta|=2U|\sin\theta|$: **nula** en el frente/trasero y **máxima** ($2U$, el doble de la corriente libre) en los flancos $\theta=\pm\pi/2$.
>
> **Puntos de estancamiento.** Donde $\vec v=\vec 0$ sobre el cilindro: $v_\theta=-2U\sin\theta=0\Rightarrow\sin\theta=0\Rightarrow$
> $$\theta=0\quad\text{(borde de salida)}\qquad\text{y}\qquad\theta=\pi\quad\text{(borde de ataque)}.$$

> [!ejemplo] Verificación de Laplace y distribución de presión
> **Parte A — $\phi$ satisface Laplace.** En polares,
> $$\nabla^2\phi=\frac1r\frac{\partial}{\partial r}\!\left(r\frac{\partial\phi}{\partial r}\right)+\frac1{r^2}\frac{\partial^2\phi}{\partial\theta^2}.$$
> Con $\phi=U\cos\theta\,(r+a^2/r)$:
>
> **Paso 1 —** parte radial. $\partial_r\phi=U\cos\theta(1-a^2/r^2)$, luego $r\,\partial_r\phi=U\cos\theta(r-a^2/r)$ y
> $$\frac1r\frac{\partial}{\partial r}\big[U\cos\theta(r-a^2/r)\big]=\frac1r\,U\cos\theta\left(1+\frac{a^2}{r^2}\right).$$
>
> **Paso 2 —** parte angular. $\partial_\theta^2\phi=-U\cos\theta(r+a^2/r)$, luego
> $$\frac1{r^2}\partial_\theta^2\phi=-\frac{1}{r^2}\,U\cos\theta\left(r+\frac{a^2}{r}\right)=-\frac1r\,U\cos\theta\left(1+\frac{a^2}{r^2}\right).$$
>
> **Paso 3 —** suma. Ambos términos son opuestos:
> $$\nabla^2\phi=\frac1r U\cos\theta\left(1+\frac{a^2}{r^2}\right)-\frac1r U\cos\theta\left(1+\frac{a^2}{r^2}\right)=0.\qquad\checkmark$$
>
> **Parte B — Presión sobre el cilindro (Bernoulli).** Lejos, $p=p_\infty$, $v=U$. Sobre la pared $v=|v_\theta|=2U|\sin\theta|$. Por Bernoulli,
> $$p(\theta)+\tfrac12\rho\,(2U\sin\theta)^2=p_\infty+\tfrac12\rho U^2,$$
> $$\boxed{\,p(\theta)=p_\infty+\tfrac12\rho U^2\big(1-4\sin^2\theta\big)\,}.$$
> Máxima presión en los estancamientos ($\theta=0,\pi$: $p=p_\infty+\tfrac12\rho U^2$), mínima en los flancos ($\theta=\pm\pi/2$: $p=p_\infty-\tfrac32\rho U^2$). **Simétrica** frente–dorso.

> [!teorema] Paradoja de d'Alembert (arrastre nulo)
> Para el cilindro en flujo potencial, la fuerza neta que el fluido ejerce sobre el cuerpo es **cero**; en particular, el **arrastre** $D=0$.

> [!demostracion] Integración de la presión
> **Paso 1 — Fuerza por unidad de longitud.** La presión actúa según $-\hat n$ (hacia adentro), con $\hat n=(\cos\theta,\sin\theta)$. La componente de arrastre (en $\hat x$) es
> $$D=-\oint_{r=a} p\,(\hat n\cdot\hat x)\,a\,d\theta=-a\int_0^{2\pi} p(\theta)\cos\theta\,d\theta.$$
>
> **Paso 2 — Sustituir la presión.** Con $p(\theta)=p_\infty+\tfrac12\rho U^2(1-4\sin^2\theta)$,
> $$D=-a\int_0^{2\pi}\Big[p_\infty+\tfrac12\rho U^2-2\rho U^2\sin^2\theta\Big]\cos\theta\,d\theta.$$
>
> **Paso 3 — Anular término a término.** Cada integral sobre un periodo completo se anula:
> $$\int_0^{2\pi}\cos\theta\,d\theta=0,\qquad\int_0^{2\pi}\sin^2\theta\cos\theta\,d\theta=\Big[\tfrac{\sin^3\theta}{3}\Big]_0^{2\pi}=0.$$
> Por tanto
> $$D=0.$$
> Por la simetría adelante–atrás de $p(\theta)$ (es par en $\theta\to\pi-\theta$ para la parte que importa), la succión del frente compensa exactamente la del dorso. Análogamente la sustentación es nula sin circulación. $\blacksquare$

> [!corolario] Circulación y sustentación (Kutta–Joukowski)
> Si se **añade un vórtice** de circulación $\Gamma$ al potencial, $\phi\to\phi+\frac{\Gamma}{2\pi}\theta$, se rompe la simetría arriba–abajo y aparece una fuerza **transversal** (sustentación) por unidad de longitud
> $$\boxed{\,L=\rho\,U\,\Gamma\,}\qquad\text{(teorema de Kutta–Joukowski),}$$
> mientras el arrastre sigue siendo nulo. Es el mecanismo idealizado de la **sustentación** sobre un perfil alar.

> [!warning] Lo que el flujo potencial ignora
> El modelo **descarta la viscosidad** y predice **arrastre nulo** (d'Alembert), en flagrante contradicción con la experiencia: una esfera o un cilindro reales sí sienten resistencia. La razón es que la viscosidad, por pequeña que sea, genera junto a la pared una **capa límite** que se **desprende**, formando una **estela** turbulenta detrás del cuerpo; esa estela **rompe la simetría** frente–dorso de la presión y produce arrastre. Véase [[5 Flujo Viscoso/index | Capítulo 5: Flujo Viscoso]]. Pese a ello, el flujo potencial describe muy bien el campo **lejano** y, con circulación, la **sustentación** aerodinámica.

---

## Resumen

> [!resumen] Flujo potencial de un vistazo
>
> | Concepto | Expresión | Condición |
> \|---\|---\|---\|
> | Potencial de velocidad | $\vec v=\nabla\phi$ | flujo irrotacional $\vec\omega=\vec 0$ |
> | Ecuación de gobierno | $\nabla^2\phi=0$ (Laplace) | además incompresible $\nabla\cdot\vec v=0$ |
> | Condición de contorno | $\partial\phi/\partial n=\vec v\cdot\hat n$ | no penetración (deslizamiento) |
> | Función de corriente (2D) | $u=\partial_y\psi,\;v=-\partial_x\psi$ | continuidad automática; $\nabla^2\psi=0$ |
> | Potencial complejo | $w(z)=\phi+i\psi$ analítica | $\dfrac{dw}{dz}=u-iv$ |
> | Cilindro | $\phi=U\cos\theta\,(r+a^2/r)$ | $v_\theta\|_{r=a}=-2U\sin\theta$ |
> | Estancamientos | $\theta=0,\pi$ | sobre el cilindro |
> | Presión en pared | $p=p_\infty+\tfrac12\rho U^2(1-4\sin^2\theta)$ | Bernoulli |
> | Arrastre | $D=0$ | paradoja de d'Alembert |
> | Sustentación | $L=\rho U\Gamma$ | con circulación (Kutta–Joukowski) |
>
> **Corolario operativo.** Irrotacional $+$ incompresible $\Rightarrow$ el problema dinámico se reduce a **resolver Laplace**, ecuación **lineal**: se superponen soluciones elementales (uniforme, fuente, vórtice, dipolo) para construir flujos sobre cuerpos. La presión se obtiene a posteriori con Bernoulli. El modelo es exacto en lo matemático pero ciego a la viscosidad: predice arrastre nulo y necesita la **capa límite** del [[5 Flujo Viscoso/index | Capítulo 5]] para explicar la resistencia real.

> [!referencia] Fuentes y notas relacionadas
> - **Landau & Lifshitz**, *Fluid Mechanics* (Vol. 6), §§9–11 (flujo potencial, función de corriente, flujo en torno a cuerpos).
> - **Sección:** [[4 Flujo Ideal/index | 4. Flujo Ideal]].
> - **Hermanas:** [[Ecuacion de Bernoulli | Ecuación de Bernoulli]], [[Vorticidad y Teoremas | Vorticidad y Teoremas]].
> - **Base cinemática:** [[Deformacion y Vorticidad | Deformación y Vorticidad]].
> - **Continuación:** [[5 Flujo Viscoso/index | 5. Flujo Viscoso]] (capa límite, estela, arrastre real).
