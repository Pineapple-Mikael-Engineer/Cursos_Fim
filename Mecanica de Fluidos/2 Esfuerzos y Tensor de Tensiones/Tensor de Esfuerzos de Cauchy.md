---
title: Tensor de Esfuerzos de Cauchy
tags:
  - fluidos
  - teoria
  - esfuerzos
draft: false
aliases:
  - Tensor de esfuerzos de Cauchy
  - Tracción
  - Estado de tensiones
---

# Tensor de Esfuerzos de Cauchy $t_i=\sigma_{ij}\,n_j$

---

> [!definicion]
> En un punto de un medio continuo, la **tracción** $\vec t(\hat n)$ es la fuerza de superficie por unidad de área que el material situado del lado hacia el que apunta la **normal exterior** $\hat n$ ejerce sobre el material del otro lado. El **tensor de esfuerzos de Cauchy** $\sigma_{ij}$ es el tensor de segundo orden que relaciona linealmente la normal con la tracción:
> $$
> t_i=\sigma_{ij}\,n_j ,\qquad \vec t=\boldsymbol\sigma\,\hat n .
> $$
> Componente a componente, $\sigma_{ij}$ es la componente $i$ de la tracción que actúa sobre el plano cuya normal exterior es $\hat e_j$. Sus elementos diagonales $\sigma_{11},\sigma_{22},\sigma_{33}$ son esfuerzos **normales** (de tracción/compresión) y los de fuera de la diagonal son esfuerzos **cortantes** (de cizalla). El tensor es **simétrico**, $\sigma_{ij}=\sigma_{ji}$, de modo que el estado de tensión en un punto queda determinado por $6$ números independientes.

---

> [!info]
> Esta nota pertenece a la sección [[2 Esfuerzos y Tensor de Tensiones/index | Esfuerzos y Tensor de Tensiones]]. Sus notas hermanas son [[Presion y Esfuerzos Viscosos]] y [[Fluido Newtoniano]]: el tensor de Cauchy se descompone en una parte de presión (isótropa) y una parte viscosa, y el cierre de esa parte viscosa con [[Tensor Gradiente de Velocidad]] da la ley constitutiva del fluido newtoniano. Aquí construimos el objeto puramente cinemático-mecánico (sin invocar todavía constitutiva alguna): el **tetraedro de Cauchy** y la **simetría** por momento angular.
>
> Referencias: Landau & Lifshitz, *Mecánica de Fluidos* (Vol. 6) §15; Batchelor, *An Introduction to Fluid Dynamics* §1.3; Aris, *Vectors, Tensors and the Basic Equations of Fluid Mechanics* cap. 5.

---

## Fuerzas másicas y fuerzas de superficie

En un fluido (o sólido deformable) actúan **dos clases** de fuerzas sobre una porción de material $V$ limitada por la superficie $S$:

- **Fuerzas másicas (de volumen):** actúan a distancia sobre cada elemento de masa. Por ejemplo la gravedad. Se escriben como una densidad por unidad de masa $\vec f$, de modo que la fuerza sobre un elemento de volumen $dV$ es $\rho\,\vec f\,dV$. Escalan con el **volumen**, $\sim\ell^3$.
- **Fuerzas de superficie (de contacto):** actúan a través de la frontera $S$ por contacto directo entre las moléculas de un lado y del otro. Se escriben como una densidad por unidad de **área**, la tracción $\vec t$, de modo que la fuerza sobre un elemento de superficie $dA$ es $\vec t\,dA$. Escalan con el **área**, $\sim\ell^2$.

La fuerza total sobre $V$ es entonces
$$
\vec F=\int_V \rho\,\vec f\,dV+\oint_S \vec t(\hat n)\,dA .
$$

El hecho **no trivial** es que $\vec t$, que en principio podría depender de la forma local de la superficie de manera arbitraria, depende de ella sólo a través de la normal exterior $\hat n$, y además **linealmente**. Eso es lo que demuestra el tetraedro de Cauchy.

---

![[tetraedro_cauchy.svg|420]]

*El tetraedro de Cauchy: tres caras apoyadas en los planos coordenados (con normales $-\hat e_1,-\hat e_2,-\hat e_3$ y áreas $dA_j=n_j\,dA$) y una cara oblicua de área $dA$ con normal exterior $\hat n$ y tracción $\vec t$. El balance de fuerzas en el límite $\ell\to0$ da $t_i=\sigma_{ij}\,n_j$.*

---

## En qué consiste

### El teorema del tetraedro de Cauchy

> [!teorema] Existencia del tensor de esfuerzos
> En cada punto de un medio continuo existe un tensor de segundo orden $\sigma_{ij}$, independiente de $\hat n$, tal que la tracción sobre cualquier plano de normal exterior $\hat n$ vale
> $$
> t_i(\hat n)=\sigma_{ij}\,n_j .
> $$

> [!demostracion]
> **Paso 1 — Construcción del tetraedro.** Alrededor del punto $P$ tomamos un **tetraedro infinitesimal** con vértice en $P$. Tres de sus caras descansan sobre los planos coordenados: la cara perpendicular a $\hat e_j$ tiene normal exterior $-\hat e_j$. La cuarta cara, **oblicua**, tiene área $dA$ y normal exterior $\hat n=(n_1,n_2,n_3)$, con $n_jn_j=1$.
>
> **Paso 2 — Áreas proyectadas.** El área de la cara coordenada perpendicular a $\hat e_j$ es la proyección de la cara oblicua sobre ese plano. Geométricamente, si $\hat n$ forma con $\hat e_j$ un ángulo cuyo coseno es $\hat n\cdot\hat e_j=n_j$, entonces
> $$
> dA_j=(\hat n\cdot\hat e_j)\,dA=n_j\,dA .
> $$
> Esto se ve también con el teorema de proyección de áreas: el vector de área de la cara oblicua es $\vec{dA}=\hat n\,dA$, y su componente $j$ es justamente $n_j\,dA$, que es el área de la cara que mira a $\hat e_j$.
>
> **Paso 3 — Tracciones sobre cada cara.** Sea $\sigma_{ij}$ la componente $i$ de la tracción sobre la cara de normal exterior $+\hat e_j$. Por el principio de acción y reacción (tercera ley de Newton para el continuo), la tracción sobre la cara de normal $-\hat e_j$ es $-\sigma_{ij}$. La tracción sobre la cara oblicua es $\vec t(\hat n)$, con componentes $t_i$.
>
> **Paso 4 — Segunda ley de Newton para el tetraedro.** Llamemos $\ell$ a la escala lineal del tetraedro, de modo que las áreas son $\sim\ell^2$ y el volumen $dV\sim\ell^3$. La segunda ley de Newton para la porción de fluido contenida en el tetraedro es
> $$
> \underbrace{\rho\,\vec a\,dV}_{\text{inercia}\ \sim\ \ell^3}
> =\underbrace{\rho\,\vec f\,dV}_{\text{másica}\ \sim\ \ell^3}
> +\underbrace{\vec t(\hat n)\,dA}_{\text{oblicua}\ \sim\ \ell^2}
> +\sum_{j=1}^{3}\underbrace{\big(-\sigma_{ij}\big)\,dA_j}_{\text{caras coordenadas}\ \sim\ \ell^2}.
> $$
> En componentes, usando $dA_j=n_j\,dA$:
> $$
> \rho\,a_i\,dV-\rho\,f_i\,dV=t_i\,dA-\sigma_{ij}\,n_j\,dA .
> $$
>
> **Paso 5 — Argumento de escalas (por qué muere el volumen).** Dividimos toda la ecuación entre el área $dA\sim\ell^2$:
> $$
> \big(\rho\,a_i-\rho\,f_i\big)\,\frac{dV}{dA}=t_i-\sigma_{ij}\,n_j .
> $$
> El cociente $dV/dA\sim\ell^3/\ell^2=\ell$. Al **contraer el tetraedro al punto**, $\ell\to0$, el miembro izquierdo se anula porque $\rho$, $a_i$ y $f_i$ permanecen acotados mientras $\ell\to0$:
> $$
> \lim_{\ell\to0}\big(\rho\,a_i-\rho\,f_i\big)\,\ell=0 .
> $$
> Las fuerzas másicas e inerciales escalan como $\ell^3$ y las de superficie como $\ell^2$; en el límite las de superficie **dominan** y deben equilibrarse por sí solas. Queda
> $$
> t_i-\sigma_{ij}\,n_j=0\quad\Longrightarrow\quad \boxed{\,t_i=\sigma_{ij}\,n_j\,}.
> $$
>
> **Paso 6 — Carácter tensorial.** Como $t_i$ y $n_j$ son vectores (componentes de objetos físicos que se transforman como tales bajo rotaciones del sistema de coordenadas) y la relación $t_i=\sigma_{ij}n_j$ es lineal y válida para **todo** $\hat n$, el cociente $\sigma_{ij}$ debe transformarse como un **tensor de segundo orden**:
> $$
> \sigma'_{kl}=R_{ki}\,R_{lj}\,\sigma_{ij},\qquad R\ \text{matriz de rotación}.
> $$
> Por la regla del cociente, $\sigma_{ij}$ es un tensor: codifica TODO el estado de tensión en el punto $P$. $\blacksquare$

### Simetría del tensor

> [!teorema] Simetría del tensor de esfuerzos
> En ausencia de pares de cuerpo (momentos distribuidos por unidad de volumen), el tensor de esfuerzos es **simétrico**:
> $$
> \sigma_{ij}=\sigma_{ji}.
> $$

> [!demostracion]
> **Paso 1 — Elemento cúbico.** Tomamos un cubo infinitesimal de lado $\ell$ centrado en $P$, con aristas paralelas a los ejes coordenados. Calculamos el **momento angular** respecto del centro y aplicamos el balance de momento (segunda ley de Newton para rotaciones).
>
> **Paso 2 — Momento de las tensiones cortantes.** Consideremos el momento alrededor del eje $\hat e_3$. Lo producen las componentes cortantes $\sigma_{12}$ y $\sigma_{21}$:
> - Sobre las dos caras perpendiculares a $\hat e_2$ (en $x_2=\pm\ell/2$) actúa la componente $\sigma_{12}$ (tracción en dirección $\hat e_1$). Cada cara tiene área $\ell^2$, así que la fuerza es $\sigma_{12}\,\ell^2$, con brazo $\ell/2$. Las dos caras opuestas tienen normales opuestas y tracciones opuestas, formando un **par** cuyo momento se suma:
> $$
> M_3^{(12)}=\big(\sigma_{12}\,\ell^2\big)\cdot\frac{\ell}{2}\cdot 2=\sigma_{12}\,\ell^3 .
> $$
> - Sobre las dos caras perpendiculares a $\hat e_1$ (en $x_1=\pm\ell/2$) actúa la componente $\sigma_{21}$ (tracción en dirección $\hat e_2$), con fuerza $\sigma_{21}\,\ell^2$ y brazo $\ell/2$. Este par genera momento en sentido **contrario**:
> $$
> M_3^{(21)}=-\big(\sigma_{21}\,\ell^2\big)\cdot\frac{\ell}{2}\cdot 2=-\sigma_{21}\,\ell^3 .
> $$
> El momento neto de las tensiones de superficie alrededor de $\hat e_3$ es
> $$
> M_3=\big(\sigma_{12}-\sigma_{21}\big)\,\ell^3 .
> $$
>
> **Paso 3 — Momento de inercia e inercia rotacional.** El balance de momento angular es $M_3=I\,\dot\omega_3$. El momento de inercia del cubo respecto de su eje central es
> $$
> I=\frac{1}{6}\,\rho\,\ell^5
> $$
> (proporcional a la masa $\rho\ell^3$ por una longitud al cuadrado $\sim\ell^2$). Las fuerzas másicas también contribuyen con momentos $\sim\ell^4$ (fuerza $\rho f\ell^3$ por brazo $\ell$), pero ambos términos son de orden superior frente a $\ell^3$.
>
> **Paso 4 — Argumento de escalas.** El balance queda
> $$
> \big(\sigma_{12}-\sigma_{21}\big)\,\ell^3=\frac{1}{6}\,\rho\,\dot\omega_3\,\ell^5+\mathcal O(\ell^4).
> $$
> Dividiendo entre $\ell^3$ y tomando $\ell\to0$:
> $$
> \sigma_{12}-\sigma_{21}=\lim_{\ell\to0}\Big(\tfrac{1}{6}\rho\,\dot\omega_3\,\ell^2+\mathcal O(\ell)\Big)=0 .
> $$
> Los momentos de las tensiones cortantes escalan como $\ell^3$ y la inercia rotacional como $\ell^5$; al contraer el cubo al punto la inercia **desaparece** y el balance exige
> $$
> \sigma_{12}=\sigma_{21}.
> $$
>
> **Paso 5 — Generalización.** Repitiendo el mismo argumento alrededor de los ejes $\hat e_1$ y $\hat e_2$ se obtiene $\sigma_{23}=\sigma_{32}$ y $\sigma_{31}=\sigma_{13}$. Compactamente, en ausencia de pares de cuerpo,
> $$
> \boxed{\,\sigma_{ij}=\sigma_{ji}\,}.\qquad\blacksquare
> $$

> [!corolario] Consecuencias de la simetría
> Por ser $\sigma_{ij}$ simétrico y real, posee $6$ componentes independientes (en lugar de $9$) y es **diagonalizable**: existe una base ortonormal de **ejes principales** $\{\hat e^{(1)},\hat e^{(2)},\hat e^{(3)}\}$ en la que
> $$
> \sigma_{ij}=\mathrm{diag}(\sigma_1,\sigma_2,\sigma_3),
> $$
> con $\sigma_1,\sigma_2,\sigma_3$ las **tensiones principales** (autovalores reales). En esos ejes los esfuerzos cortantes se anulan: la tracción es puramente normal sobre los planos principales.

> [!warning]
> - La tracción **depende del plano**: $\vec t=\vec t(\hat n)$. Hablar del "esfuerzo en un punto" como si fuera un vector es incorrecto; el estado de tensión en un punto es un **tensor**, $\sigma_{ij}$, y de él se extrae el vector tracción una vez fijado $\hat n$.
> - El signo importa: $\hat n$ es la **normal exterior** al material sobre el que se calcula la fuerza. La tracción sobre la cara opuesta (normal $-\hat n$) es $\vec t(-\hat n)=-\vec t(\hat n)$, por la tercera ley de Newton.

---

## Ejemplo

> [!ejemplo]
> En un punto de un fluido el tensor de esfuerzos (en pascales) vale, en cierta base ortonormal,
> $$
> \boldsymbol\sigma=\begin{pmatrix} 50 & 20 & 0\\[2pt] 20 & 30 & 10\\[2pt] 0 & 10 & 40 \end{pmatrix}\ \mathrm{Pa}.
> $$
> Sobre un plano cuya normal exterior es $\hat n=\dfrac{1}{3}(2,\,2,\,1)$ (unitaria, pues $2^2+2^2+1^2=9$), calcula: (a) el vector tracción $\vec t$; (b) su componente normal $t_n$; (c) su componente cortante $t_s$.

> [!solucion]
> **Paso 1 — Componentes de la normal.** $n_1=\tfrac{2}{3}\approx0,667$, $n_2=\tfrac{2}{3}\approx0,667$, $n_3=\tfrac{1}{3}\approx0,333$.
>
> **Paso 2 — Tracción $t_i=\sigma_{ij}n_j$.** Multiplicamos la matriz por $\hat n$:
> $$
> t_1=\sigma_{1j}n_j=50\cdot\tfrac{2}{3}+20\cdot\tfrac{2}{3}+0\cdot\tfrac{1}{3}=\tfrac{100+40+0}{3}=\tfrac{140}{3}\approx 46,667\ \mathrm{Pa}.
> $$
> $$
> t_2=\sigma_{2j}n_j=20\cdot\tfrac{2}{3}+30\cdot\tfrac{2}{3}+10\cdot\tfrac{1}{3}=\tfrac{40+60+10}{3}=\tfrac{110}{3}\approx 36,667\ \mathrm{Pa}.
> $$
> $$
> t_3=\sigma_{3j}n_j=0\cdot\tfrac{2}{3}+10\cdot\tfrac{2}{3}+40\cdot\tfrac{1}{3}=\tfrac{0+20+40}{3}=\tfrac{60}{3}=20\ \mathrm{Pa}.
> $$
> Por tanto
> $$
> \vec t=\left(\tfrac{140}{3},\ \tfrac{110}{3},\ 20\right)\ \mathrm{Pa}\approx(46,667;\ 36,667;\ 20,000)\ \mathrm{Pa}.
> $$
>
> **Paso 3 — Componente normal $t_n=\vec t\cdot\hat n=\sigma_{ij}n_in_j$.**
> $$
> t_n=t_1n_1+t_2n_2+t_3n_3
> =\tfrac{140}{3}\cdot\tfrac{2}{3}+\tfrac{110}{3}\cdot\tfrac{2}{3}+20\cdot\tfrac{1}{3}.
> $$
> $$
> t_n=\frac{280}{9}+\frac{220}{9}+\frac{20}{3}=\frac{280+220+60}{9}=\frac{560}{9}\approx 62,222\ \mathrm{Pa}.
> $$
> Es positiva: el esfuerzo normal es de **tracción** sobre ese plano.
>
> **Paso 4 — Módulo de la tracción.**
> $$
> |\vec t|^2=t_1^2+t_2^2+t_3^2=\left(\tfrac{140}{3}\right)^2+\left(\tfrac{110}{3}\right)^2+20^2
> =\frac{19600+12100}{9}+400=\frac{31700}{9}+400.
> $$
> $$
> |\vec t|^2=\frac{31700+3600}{9}=\frac{35300}{9}\approx 3922,22\ \mathrm{Pa}^2.
> $$
>
> **Paso 5 — Componente cortante** $t_s=\sqrt{|\vec t|^2-t_n^2}$.
> $$
> t_n^2=\left(\tfrac{560}{9}\right)^2=\frac{313600}{81}\approx 3871,60\ \mathrm{Pa}^2.
> $$
> $$
> t_s=\sqrt{3922,22-3871,60}=\sqrt{50,62}\approx 7,115\ \mathrm{Pa}.
> $$
>
> **Resultado.** $\vec t\approx(46,667;\ 36,667;\ 20,000)\ \mathrm{Pa}$, con $t_n\approx 62,222\ \mathrm{Pa}$ (tracción) y $t_s\approx 7,115\ \mathrm{Pa}$ de cizalla sobre el plano. $\blacksquare$

---

## Resumen

> [!resumen] Tensor de esfuerzos de Cauchy de un vistazo
>
> | Concepto | Expresión | Significado |
> |---|---|---|
> | Tracción | $t_i=\sigma_{ij}\,n_j$ | fuerza de superficie por área sobre el plano de normal $\hat n$ |
> | Componente del tensor | $\sigma_{ij}$ | comp. $i$ de la tracción sobre la cara de normal $\hat e_j$ |
> | Esfuerzo normal | $t_n=\sigma_{ij}\,n_i n_j$ | proyección de $\vec t$ sobre $\hat n$ |
> | Esfuerzo cortante | $t_s=\sqrt{\,\lvert\vec t\rvert^2-t_n^2\,}$ | componente de $\vec t$ tangente al plano |
> | Simetría | $\sigma_{ij}=\sigma_{ji}$ | balance de momento angular; $6$ comp. independientes |
> | Ejes principales | $\sigma_{ij}=\mathrm{diag}(\sigma_1,\sigma_2,\sigma_3)$ | base donde la cizalla se anula |

> [!corolario]
> El tetraedro de Cauchy demuestra que el estado de tensión en un punto es un **tensor de segundo orden**, no un vector: una vez conocido $\sigma_{ij}$, la tracción sobre cualquier plano se obtiene contrayendo con su normal. La simetría (de momento angular) reduce el tensor a $6$ grados de libertad y garantiza ejes principales reales. En el siguiente paso, $\sigma_{ij}$ se descompone en una parte de presión isótropa y una parte viscosa (véase [[Presion y Esfuerzos Viscosos]]), cuya forma constitutiva fija el [[Fluido Newtoniano]] mediante el [[Tensor Gradiente de Velocidad]].

> [!referencia]
> - L. D. Landau y E. M. Lifshitz, *Mecánica de Fluidos* (Curso de Física Teórica, Vol. 6), §15.
> - G. K. Batchelor, *An Introduction to Fluid Dynamics*, §1.3.
> - R. Aris, *Vectors, Tensors and the Basic Equations of Fluid Mechanics*, cap. 5.
