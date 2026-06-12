---
title: Maxwell Covariante
tags:
  - electromagnetismo
  - teoria
  - covariante
draft: false
aliases:
  - Maxwell covariante
  - Ecuaciones de Maxwell tensoriales
  - Identidad de Bianchi
---

# Maxwell Covariante $\partial_\mu F^{\mu\nu}=\mu_0 J^\nu,\quad \partial_\mu(\!*F)^{\mu\nu}=0$

> [!definicion]
> Las **cuatro ecuaciones de Maxwell** se condensan en **dos** ecuaciones tensoriales sobre el espaciotiempo de Minkowski. La **inhomogénea**, que contiene las fuentes,
> $$\partial_\mu F^{\mu\nu}=\mu_0 J^\nu,$$
> reúne la **ley de Gauss eléctrica** y la **ley de Ampère–Maxwell**; la **homogénea**,
> $$\partial_\mu(\!*F)^{\mu\nu}=0\qquad\Longleftrightarrow\qquad \partial_\lambda F_{\mu\nu}+\partial_\mu F_{\nu\lambda}+\partial_\nu F_{\lambda\mu}=0\quad(\textbf{identidad de Bianchi}),$$
> reúne la **ley de Gauss magnética** y la **ley de Faraday**. Aquí $F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu$ es el [[Tensor de Campo]], $(*F)^{\mu\nu}=\tfrac12\epsilon^{\mu\nu\rho\sigma}F_{\rho\sigma}$ su **dual de Hodge**, y $J^\nu=(c\rho,\vec J)$ la cuadricorriente. Toda la teoría de Maxwell vive en dos líneas manifiestamente covariantes.

---

> [!info]
> **Sección [[6 Formulacion Covariante/index | Formulación Covariante]].** Notas hermanas: [[Tensor de Campo]] (de donde sale la matriz $F^{\mu\nu}$ y su dual), [[Cuadrivectores]] (espaciotiempo, métrica, $J^\mu$, $A^\mu$) y [[Tensor Energia-Momento]]. Esta nota **reescribe en forma tensorial** las [[Ecuaciones de Maxwell]] del enfoque vectorial: es el mismo contenido físico, vestido para que su simetría de Lorentz sea visible.
> **Convenio.** Métrica $\eta_{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1)$; índices griegos $0\!-\!3$, latinos $1\!-\!3$; convenio de suma de Einstein; unidades SI; $c=1/\sqrt{\mu_0\varepsilon_0}$, de modo que $\mu_0 c^2=1/\varepsilon_0$.
> **Referencia.** Griffiths cap. 12; Landau-Lifshitz Vol. 2.

> [!proposicion] La matriz de campo de la que partimos
> De [[Tensor de Campo]], el tensor contravariante con dos índices arriba es
> $$F^{\mu\nu}=\begin{pmatrix} 0 & -E_x/c & -E_y/c & -E_z/c \\ E_x/c & 0 & -B_z & B_y \\ E_y/c & B_z & 0 & -B_x \\ E_z/c & -B_y & B_x & 0 \end{pmatrix},$$
> antisimétrico, $F^{\mu\nu}=-F^{\nu\mu}$. Las componentes **temporal-espaciales** $F^{0i}=-E_i/c$ guardan el campo eléctrico; las **espaciales** $F^{ij}=-\epsilon_{ijk}B_k$ guardan el magnético. El **cuadrigradiente** que contraemos contra ella es $\partial_\mu=\dfrac{\partial}{\partial x^\mu}=\left(\dfrac1c\partial_t,\ \nabla\right)$, con índice **abajo**. Todo lo que sigue es contraer estos dos objetos.

---

## Ejemplo

> [!ejemplo] La componente $\nu=0$ reproduce la ley de Gauss
> Verificar **a mano**, sin atajos, que la ecuación inhomogénea $\partial_\mu F^{\mu\nu}=\mu_0 J^\nu$ tomada en $\nu=0$ devuelve $\nabla\cdot\vec E=\rho/\varepsilon_0$.

> [!solucion]
> **Paso 1 — Desarrollar la suma sobre $\mu$.** Con $\nu=0$, la suma de Einstein recorre $\mu=0,1,2,3$:
> $$\partial_\mu F^{\mu 0}=\partial_0 F^{00}+\partial_1 F^{10}+\partial_2 F^{20}+\partial_3 F^{30}.$$
>
> **Paso 2 — Anular la diagonal.** Por antisimetría $F^{00}=0$, luego $\partial_0 F^{00}=0$. Quedan los tres términos espaciales.
>
> **Paso 3 — Sustituir las componentes.** De la matriz, $F^{10}=E_x/c$, $F^{20}=E_y/c$, $F^{30}=E_z/c$. Con $\partial_1=\partial_x$, etc.:
> $$\partial_\mu F^{\mu 0}=\frac{\partial}{\partial x}\frac{E_x}{c}+\frac{\partial}{\partial y}\frac{E_y}{c}+\frac{\partial}{\partial z}\frac{E_z}{c}=\frac1c\left(\partial_x E_x+\partial_y E_y+\partial_z E_z\right)=\frac1c\,\nabla\cdot\vec E.$$
>
> **Paso 4 — Igualar a la fuente.** El lado derecho con $\nu=0$ es $\mu_0 J^0=\mu_0(c\rho)=\mu_0 c\,\rho$. Por tanto
> $$\frac1c\,\nabla\cdot\vec E=\mu_0 c\,\rho\quad\Longrightarrow\quad \nabla\cdot\vec E=\mu_0 c^2\,\rho.$$
>
> **Paso 5 — Usar $\mu_0 c^2=1/\varepsilon_0$.** Como $c^2=1/(\mu_0\varepsilon_0)$, se tiene $\mu_0 c^2=1/\varepsilon_0$, de donde
> $$\boxed{\ \nabla\cdot\vec E=\frac{\rho}{\varepsilon_0}\ }\qquad(\textbf{ley de Gauss eléctrica}).\qquad\blacksquare$$

---

## En qué consiste

> [!teoria] Dos tensores, cuatro leyes
> La fuerza de la formulación es contable: una ecuación con índice libre $\nu$ es, en realidad, **cuatro** ecuaciones (una por cada valor $\nu=0,1,2,3$). La inhomogénea entrega Gauss eléctrico ($\nu=0$) y las tres componentes de Ampère–Maxwell ($\nu=1,2,3$); la homogénea entrega Gauss magnético y las tres de Faraday. Cuatro más cuatro componentes, empaquetadas en dos enunciados tensoriales. Demostramos cada uno por separado, contrayendo índices sin condensar.

> [!teorema] La inhomogénea contiene Gauss eléctrico y Ampère–Maxwell
> $$\partial_\mu F^{\mu\nu}=\mu_0 J^\nu\quad\Longleftrightarrow\quad \nabla\cdot\vec E=\frac{\rho}{\varepsilon_0}\quad\text{y}\quad \nabla\times\vec B-\frac1{c^2}\partial_t\vec E=\mu_0\vec J.$$

> [!demostracion]
> **Caso $\nu=0$** ya se hizo en el ejemplo: da $\nabla\cdot\vec E=\rho/\varepsilon_0$. Pasamos al **caso espacial** $\nu=i\in\{1,2,3\}$, que es el laborioso.
>
> **Paso 1 — Desplegar la suma sobre $\mu$.**
> $$\partial_\mu F^{\mu i}=\partial_0 F^{0i}+\partial_1 F^{1i}+\partial_2 F^{2i}+\partial_3 F^{3i}=\partial_0 F^{0i}+\partial_j F^{ji}.$$
> El primer término es **temporal** (la corriente de desplazamiento); el segundo, una suma sobre $j=1,2,3$, es **espacial** (el rotacional de $\vec B$).
>
> **Paso 2 — El término temporal.** Con $\partial_0=\tfrac1c\partial_t$ y $F^{0i}=-E_i/c$:
> $$\partial_0 F^{0i}=\frac1c\,\partial_t\!\left(-\frac{E_i}{c}\right)=-\frac1{c^2}\,\partial_t E_i.$$
>
> **Paso 3 — El término espacial.** Con $F^{ji}=-\epsilon_{jik}B_k$ y $\epsilon_{jik}=-\epsilon_{ijk}$:
> $$\partial_j F^{ji}=\partial_j(-\epsilon_{jik}B_k)=\epsilon_{ijk}\,\partial_j B_k.$$
> Pero $\epsilon_{ijk}\partial_j B_k$ es exactamente la componente $i$-ésima del rotacional: $(\nabla\times\vec B)_i=\epsilon_{ijk}\partial_j B_k$. Luego $\partial_j F^{ji}=(\nabla\times\vec B)_i$.
>
> **Paso 4 — Sumar los dos términos.**
> $$\partial_\mu F^{\mu i}=-\frac1{c^2}\partial_t E_i+(\nabla\times\vec B)_i.$$
>
> **Paso 5 — Igualar a la fuente.** El lado derecho con $\nu=i$ es $\mu_0 J^i=\mu_0 (\vec J)_i$. Igualando componente a componente y reordenando:
> $$(\nabla\times\vec B)_i-\frac1{c^2}\partial_t E_i=\mu_0 (\vec J)_i\quad\Longrightarrow\quad \boxed{\ \nabla\times\vec B-\frac1{c^2}\partial_t\vec E=\mu_0\vec J\ }.$$
> Es la **ley de Ampère–Maxwell**, con la corriente de desplazamiento $\tfrac1{c^2}\partial_t\vec E=\mu_0\varepsilon_0\partial_t\vec E$ surgiendo del término temporal del tensor. Las dos ecuaciones con fuentes quedan demostradas. $\blacksquare$

> [!teorema] La homogénea contiene Gauss magnético y Faraday
> $$\partial_\mu(\!*F)^{\mu\nu}=0\quad\Longleftrightarrow\quad \nabla\cdot\vec B=0\quad\text{y}\quad \nabla\times\vec E+\partial_t\vec B=0.$$

> [!demostracion]
> El **dual de Hodge** $(*F)^{\mu\nu}=\tfrac12\epsilon^{\mu\nu\rho\sigma}F_{\rho\sigma}$ intercambia los papeles de $\vec E$ y $\vec B$: explícitamente equivale a sustituir $\vec E/c\to\vec B$ y $\vec B\to-\vec E/c$ en la matriz de $F^{\mu\nu}$. Es decir,
> $$(\!*F)^{\mu\nu}=\begin{pmatrix} 0 & -B_x & -B_y & -B_z \\ B_x & 0 & E_z/c & -E_y/c \\ B_y & -E_z/c & 0 & E_x/c \\ B_z & E_y/c & -E_x/c & 0 \end{pmatrix},$$
> con $(*F)^{0i}=-B_i$ y $(*F)^{ji}=+\tfrac1c\epsilon_{jik}E_k$.
>
> **Paso 1 — Caso $\nu=0$.** Desplegando la suma sobre $\mu$ y anulando la diagonal:
> $$\partial_\mu(\!*F)^{\mu 0}=\partial_i(\!*F)^{i0}=\partial_1 B_x+\partial_2 B_y+\partial_3 B_z=\nabla\cdot\vec B,$$
> donde se usó $(*F)^{i0}=B_i$. Igualando a cero:
> $$\boxed{\ \nabla\cdot\vec B=0\ }\qquad(\textbf{ley de Gauss magnética}).$$
>
> **Paso 2 — Caso $\nu=i$, término temporal.** Con $\partial_0=\tfrac1c\partial_t$ y $(*F)^{0i}=-B_i$:
> $$\partial_0(\!*F)^{0i}=\frac1c\partial_t(-B_i)=-\frac1c\partial_t B_i.$$
>
> **Paso 3 — Caso $\nu=i$, término espacial.** Con $(*F)^{ji}=\tfrac1c\epsilon_{jik}E_k$ y $\epsilon_{jik}=-\epsilon_{ijk}$:
> $$\partial_j(\!*F)^{ji}=\frac1c\,\epsilon_{jik}\,\partial_j E_k=-\frac1c\,\epsilon_{ijk}\,\partial_j E_k=-\frac1c\,(\nabla\times\vec E)_i.$$
>
> **Paso 4 — Sumar e igualar a cero.**
> $$\partial_\mu(\!*F)^{\mu i}=-\frac1c\partial_t B_i-\frac1c(\nabla\times\vec E)_i=0.$$
> Multiplicando por $-c$ y reagrupando en forma vectorial:
> $$\boxed{\ \nabla\times\vec E+\partial_t\vec B=0\ }\qquad(\textbf{ley de Faraday}).\qquad\blacksquare$$

> [!proposicion] La homogénea es automática para todo potencial
> Si el campo proviene de un cuadripotencial, $F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu$, la identidad de Bianchi se cumple **por estructura**, sin imponer nada.

> [!demostracion]
> **Paso 1 — Sustituir $F$ en la suma cíclica.** En la forma con índices abajo $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$, escribimos los tres términos de Bianchi:
> $$\partial_\lambda F_{\mu\nu}=\partial_\lambda\partial_\mu A_\nu-\partial_\lambda\partial_\nu A_\mu,$$
> $$\partial_\mu F_{\nu\lambda}=\partial_\mu\partial_\nu A_\lambda-\partial_\mu\partial_\lambda A_\nu,$$
> $$\partial_\nu F_{\lambda\mu}=\partial_\nu\partial_\lambda A_\mu-\partial_\nu\partial_\mu A_\lambda.$$
>
> **Paso 2 — Sumar y emparejar.** Las derivadas parciales conmutan, $\partial_\alpha\partial_\beta=\partial_\beta\partial_\alpha$. Los seis términos se cancelan por pares:
> $$\underbrace{\partial_\lambda\partial_\mu A_\nu-\partial_\mu\partial_\lambda A_\nu}_{=0}+\underbrace{-\partial_\lambda\partial_\nu A_\mu+\partial_\nu\partial_\lambda A_\mu}_{=0}+\underbrace{\partial_\mu\partial_\nu A_\lambda-\partial_\nu\partial_\mu A_\lambda}_{=0}=0.$$
>
> **Paso 3 — Interpretar.** Es la versión cuadridimensional de $\nabla\cdot(\nabla\times\vec A)=0$ de [[Identidades Vectoriales]]: la **antisimetría** del símbolo de Levi-Civita (en el dual) contrae contra la **simetría** de la segunda derivada $\partial\partial$, y el resultado se anula idénticamente. Por eso Gauss magnético y Faraday **no necesitan fuentes**: son consecuencia de que $\vec E$ y $\vec B$ derivan de un potencial. $\blacksquare$

> [!teorema] La conservación de la carga sale gratis
> $$\partial_\mu F^{\mu\nu}=\mu_0 J^\nu\quad\Longrightarrow\quad \partial_\nu J^\nu=0\qquad(\textbf{continuidad}).$$

> [!demostracion]
> **Paso 1 — Aplicar $\partial_\nu$ a la inhomogénea.** Contraemos un nuevo cuadrigradiente sobre el índice libre $\nu$:
> $$\partial_\nu\partial_\mu F^{\mu\nu}=\mu_0\,\partial_\nu J^\nu.$$
>
> **Paso 2 — Analizar el lado izquierdo.** El objeto $\partial_\nu\partial_\mu$ es **simétrico** en $\mu\nu$ (las parciales conmutan: $\partial_\nu\partial_\mu=\partial_\mu\partial_\nu$), mientras que $F^{\mu\nu}$ es **antisimétrico** ($F^{\mu\nu}=-F^{\nu\mu}$). La contracción de un objeto simétrico con uno antisimétrico sobre el **mismo** par de índices es cero. En detalle, renombrando los índices mudos $\mu\leftrightarrow\nu$:
> $$\partial_\nu\partial_\mu F^{\mu\nu}=\partial_\mu\partial_\nu F^{\nu\mu}=\partial_\nu\partial_\mu(-F^{\mu\nu})=-\,\partial_\nu\partial_\mu F^{\mu\nu}.$$
> Una cantidad igual a su opuesta es nula: $\partial_\nu\partial_\mu F^{\mu\nu}=0$.
>
> **Paso 3 — Concluir.** El lado izquierdo se anula, luego
> $$0=\mu_0\,\partial_\nu J^\nu\quad\Longrightarrow\quad \boxed{\ \partial_\nu J^\nu=0\ }\quad\Longleftrightarrow\quad \partial_t\rho+\nabla\cdot\vec J=0.$$
> La **ecuación de continuidad** no se postula: es una **consecuencia estructural** de la antisimetría de $F^{\mu\nu}$. El electromagnetismo no puede sino conservar la carga. $\blacksquare$

> [!teorema] Maxwell en el potencial: la ecuación de onda
> Sustituyendo $F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu$ en la inhomogénea y fijando el **gauge de Lorenz** $\partial_\mu A^\mu=0$, las cuatro componentes obedecen una sola ecuación de onda:
> $$\boxed{\ \Box A^\nu=\mu_0 J^\nu\ },\qquad \Box\equiv\partial_\mu\partial^\mu=\frac1{c^2}\partial_t^2-\nabla^2.$$

> [!demostracion]
> **Paso 1 — Sustituir el tensor.**
> $$\partial_\mu F^{\mu\nu}=\partial_\mu(\partial^\mu A^\nu-\partial^\nu A^\mu)=\partial_\mu\partial^\mu A^\nu-\partial_\mu\partial^\nu A^\mu.$$
>
> **Paso 2 — Reordenar el segundo término.** Las parciales conmutan, así que $\partial_\mu\partial^\nu A^\mu=\partial^\nu(\partial_\mu A^\mu)$:
> $$\partial_\mu F^{\mu\nu}=\partial_\mu\partial^\mu A^\nu-\partial^\nu(\partial_\mu A^\mu)=\mu_0 J^\nu.$$
> Esta es Maxwell en el potencial, **válida en cualquier gauge**.
>
> **Paso 3 — Imponer el gauge de Lorenz.** Elegimos $\partial_\mu A^\mu=0$ (siempre posible; ver [[Potenciales y Gauge]]). El segundo término se anula y queda
> $$\partial_\mu\partial^\mu A^\nu=\mu_0 J^\nu\quad\Longrightarrow\quad \Box A^\nu=\mu_0 J^\nu.$$
> Una **única** ecuación de onda con fuente gobierna las cuatro componentes $A^\nu=(V/c,\vec A)$; desplegada, son la ecuación de $V$ y las tres de $\vec A$ del enfoque vectorial, ahora unificadas. $\blacksquare$

![[maxwell_colapso.svg|600]]
*Las cuatro ecuaciones vectoriales de Maxwell se agrupan en dos tensoriales: Gauss eléctrico y Ampère–Maxwell (con fuentes) forman la inhomogénea $\partial_\mu F^{\mu\nu}=\mu_0 J^\nu$; Gauss magnético y Faraday (sin fuentes) forman la identidad de Bianchi $\partial_\mu(\!*F)^{\mu\nu}=0$.*

> [!warning] La elegancia es física, no cosmética
> Compactar cuatro ecuaciones en dos no es un truco de notación. Las dos ecuaciones tensoriales son **manifiestamente covariantes**: tienen la **misma forma en todo marco inercial**, porque sus dos lados son tensores que se transforman igual bajo Lorentz. Las cuatro ecuaciones vectoriales esconden esa simetría —mezclan $\vec E$ y $\vec B$, que un boost intercambia— y por eso un cambio de observador las deforma de modo aparatoso. Hacer visible la covariancia es lo que convierte a Maxwell en la **plantilla de toda teoría de campos** moderna: el modelo a imitar para la relatividad general, las teorías gauge y el modelo estándar.

---

## Resumen

> [!resumen]
> | Ecuación tensorial | Índice $\nu$ | Ley vectorial \| recuperada |
> |:---|:---|:---|
> | $\partial_\mu F^{\mu\nu}=\mu_0 J^\nu$ | $\nu=0$ | $\nabla\cdot\vec E=\rho/\varepsilon_0$ \| (Gauss eléctrico) |
> | $\partial_\mu F^{\mu\nu}=\mu_0 J^\nu$ | $\nu=i$ | $\nabla\times\vec B-\tfrac1{c^2}\partial_t\vec E=\mu_0\vec J$ \| (Ampère–Maxwell) |
> | $\partial_\mu(\!*F)^{\mu\nu}=0$ | $\nu=0$ | $\nabla\cdot\vec B=0$ \| (Gauss magnético) |
> | $\partial_\mu(\!*F)^{\mu\nu}=0$ | $\nu=i$ | $\nabla\times\vec E+\partial_t\vec B=0$ \| (Faraday) |
> | $\partial_\nu J^\nu=0$ | — | $\partial_t\rho+\nabla\cdot\vec J=0$ \| (continuidad, gratis) |
> | $\Box A^\nu=\mu_0 J^\nu$ | — | ondas de $V$ y $\vec A$ \| (gauge de Lorenz) |

> [!corolario] Lo que hay que retener
> La inhomogénea $\partial_\mu F^{\mu\nu}=\mu_0 J^\nu$ guarda las ecuaciones **con fuentes**; la homogénea $\partial_\mu(\!*F)^{\mu\nu}=0$ —la identidad de Bianchi— guarda las ecuaciones **sin fuentes** y es **automática** en cuanto $F^{\mu\nu}$ deriva de un potencial $A^\mu$. La **conservación de la carga** y la **ecuación de onda** $\Box A^\nu=\mu_0 J^\nu$ caen como consecuencias de la estructura, no como postulados. Las propiedades de $F^{\mu\nu}$ que lo hacen posible (antisimetría, invariantes, transformación bajo boost) están en [[Tensor de Campo]]; la energía y el momento del campo, en [[Tensor Energia-Momento]].

> [!referencia]
> Griffiths, *Introduction to Electrodynamics*, cap. 12 ("Electrodynamics and Relativity"). Landau-Lifshitz, **Vol. 2** (*Teoría Clásica de Campos*), §§ 26–30. Jackson, cap. 11.
