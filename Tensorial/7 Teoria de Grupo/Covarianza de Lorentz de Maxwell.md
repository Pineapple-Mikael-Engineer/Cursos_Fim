---
title: Covarianza de Lorentz de las Ecuaciones de Maxwell
tags:
  - analisis-tensorial
  - teoria
  - teoria-grupos
  - covarianza
  - lorentz
draft: false
aliases:
  - tensor del campo electromagnetico
  - tensor de Faraday
  - Maxwell tensorial
  - cuadripotencial
  - cuadricorriente
  - Lorentz covariance of Maxwell equations
  - electromagnetic field tensor
---

# Covarianza de Lorentz de las Ecuaciones de Maxwell $F^{\mu\nu}$

> [!definicion]
> Las cuatro ecuaciones de Maxwell se reescriben como **dos** ecuaciones tensoriales en el [[Grupo Homogeneo de Lorentz | espacio de Minkowski]], haciendo **manifiesta** su covarianza de Lorentz. La pieza central es el **tensor del campo electromagnetico**
> $$F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu=-F^{\nu\mu},$$
> un tensor **antisimetrico de rango 2** construido del [[Grupo Homogeneo de Lorentz | cuadripotencial]] $A^\mu$. Reune $\vec E$ y $\vec B$ en un solo objeto. Las dos Maxwell **inhomogeneas** se condensan en $\partial F_{\mu\nu}/\partial x_\nu=i_\mu$ y las dos **homogeneas** en $t^{\lambda\mu\nu}+t^{\nu\lambda\mu}+t^{\mu\nu\lambda}=0$.

> [!info]
> Seccion **7.5** del [[index | capitulo 7]] (libro, cap. 7.5) y **cierre del curso**. Una ley fisica covariante bajo [[6 Determinantes y Matrices/Matrices Ortogonales | rotaciones]] se escribe escalar=escalar, vector=vector, tensor=tensor; covariante bajo [[Grupo Homogeneo de Lorentz | Lorentz]], lo mismo pero con cuadrivectores y tensores de Minkowski. Usa el [[5 Coordenadas No Ortogonales/Covarianza Contravarianza en Tensores | algebra de indices co/contravariantes]] y el [[5 Coordenadas No Ortogonales/Derivadas Parciales Co y Contravariantes | gradiente cuadridimensional]] $\partial^\mu$. Aqui culmina todo: el electromagnetismo es **una sola ecuacion tensorial**.

---

## Ejemplo

> [!ejemplo] Un campo magnetico puro se ve como campo electrico
> Un sistema $S$ tiene **solo** campo magnetico, $\vec E=0$, $\vec B\neq 0$. Una particula con carga $q$ en reposo en $S$ no siente fuerza ($\vec F=q\vec E=0$). Veamos que ve un observador $S'$ que se mueve con velocidad pequena $\vec v=v\,\hat e_z$ junto a la particula.
>
> **Paso 1 — partir de las transformaciones de los campos.** Para un *boost* a lo largo de $z$, con $\beta=v/c\ll 1$ (luego $1/\sqrt{1-\beta^2}\approx 1$):
> $$E'_x=\frac{E_x-vB_y}{\sqrt{1-\beta^2}}\approx -vB_y,\qquad E'_y=\frac{E_y+vB_x}{\sqrt{1-\beta^2}}\approx vB_x,\qquad E'_z=E_z=0,$$
> usando $E_x=E_y=E_z=0$ en $S$.
>
> **Paso 2 — reconocer el producto vectorial.** Con $\vec v=v\,\hat e_z$, el producto cruz $\vec v\times\vec B$ tiene componentes $(\vec v\times\vec B)_x=v_y B_z-v_z B_y=-vB_y$ y $(\vec v\times\vec B)_y=v_z B_x-v_x B_z=vB_x$. Comparando con el Paso 1:
> $$\boxed{\ \vec E'=\vec v\times\vec B\ }\qquad\Longrightarrow\qquad \vec F=q\vec E'=q\,\vec v\times\vec B.$$
>
> **Conclusion.** En $S'$ la particula **si** siente fuerza, la fuerza magnetica usual $\vec F=q\vec v\times\vec B$. Lo que en $S$ era "puramente magnetico" es en $S'$ una mezcla de $\vec E$ y $\vec B$: **$\vec E$ y $\vec B$ no son objetos independientes**, son las componentes de un mismo tensor $F^{\mu\nu}$ vistas desde sistemas distintos. De hecho esta es la **definicion operacional** del campo magnetico (ec. 7.125).

---

## En qué consiste

> [!teoria] De los potenciales a la ecuacion de onda
> Maxwell en el vacio (ec. 7.103):
> $$\vec\nabla\times\vec E=-\frac{\partial\vec B}{\partial t},\quad \vec\nabla\times\vec H=\frac{\partial\vec D}{\partial t}+\rho\vec v,\quad \vec\nabla\cdot\vec D=\rho,\quad \vec\nabla\cdot\vec B=0,$$
> con $\vec D=\varepsilon_0\vec E$ y $\vec B=\mu_0\vec H$. Se introducen los potenciales escalar $\varphi$ y vectorial $\vec A$:
> $$\vec B=\vec\nabla\times\vec A,\qquad \vec E=-\frac{\partial\vec A}{\partial t}-\vec\nabla\varphi.$$
> Estos satisfacen automaticamente las dos Maxwell **homogeneas**. La divergencia de $\vec A$ queda libre; se fija con el **gauge de Lorenz**
> $$\vec\nabla\cdot\vec A+\varepsilon_0\mu_0\frac{\partial\varphi}{\partial t}=0,$$
> que **desacopla** las ecuaciones para $\vec A$ y $\varphi$. Sustituyendo en las dos Maxwell inhomogeneas y usando $\varepsilon_0\mu_0=1/c^2$, se obtienen dos ecuaciones de onda gemelas:
> $$\left[\nabla^2-\frac{1}{c^2}\frac{\partial^2}{\partial t^2}\right]\vec A=-\mu_0\rho\vec v,\qquad \left[\nabla^2-\frac{1}{c^2}\frac{\partial^2}{\partial t^2}\right]\varphi=-\frac{\rho}{\varepsilon_0}.$$

> [!info] El d'Alembertiano
> El operador de onda es el **d'Alembertiano**, un escalar de Lorentz:
> $$\partial^2=\nabla^2-\frac{1}{c^2}\frac{\partial^2}{\partial t^2}=-\partial^\mu\partial_\mu.$$
> Es el "Laplaciano cuadridimensional" en [[Grupo Homogeneo de Lorentz | Minkowski]]. Que sea un escalar es lo que permite empaquetar las dos ecuaciones de onda en una sola ecuacion tensorial.

> [!definicion] Cuadripotencial y cuadricorriente
> Definimos el **cuadripotencial** $A^\mu$ y la **cuadricorriente** $i^\mu$:
> $$A^k=c\varepsilon_0 A_k\ (k=1,2,3),\quad A^0=\varepsilon_0\varphi;\qquad i^0=\rho,\quad i^k=\frac{\rho v_k}{c}\ (k=1,2,3).$$
> Con ellos, las **dos** ecuaciones de onda se condensan en una sola:
> $$\boxed{\ \partial^2 A^\mu=i^\mu\ }\qquad(\mu=0,1,2,3).$$

> [!demostracion] $i^\mu$ es un cuadrivector
> La ecuacion $\partial^2 A^\mu=i^\mu$ **parece** tensorial, pero eso no basta. Hay que probar que $i^\mu$ transforma como un cuadrivector de Minkowski.
>
> **Paso 1 — la carga es invariante.** Un elemento de carga es $de=\rho\,dx_1 dx_2 dx_3$, y la carga electrica es un **invariante** de Lorentz (la misma en todo sistema).
>
> **Paso 2 — el volumen 4D es invariante.** El elemento de volumen cuadridimensional $dx_1 dx_2 dx_3 dx_0$ tambien es invariante (jacobiano de Lorentz $=1$).
>
> **Paso 3 — como transforma $\rho$.** Comparando los Pasos 1 y 2: como $de=\rho\,dx_1 dx_2 dx_3$ es invariante y $dx_1 dx_2 dx_3 dx_0$ es invariante, $\rho$ debe transformar igual que $x_0=ct$. Por eso ponemos $\rho=i^0$, la **componente cero** de un cuadrivector.
>
> **Paso 4 — las componentes espaciales.** Expandiendo $i^1$:
> $$i^1=\frac{\rho v_x}{c}=\frac{\rho}{c}\frac{dx_1}{dt}=i^0\frac{dx_1}{dt}.$$
> Como $i^0$ transforma como $dx_0$ (Paso 3), entonces $i^1$ transforma como $dx_1$. Analogamente $i^2\sim dx_2$, $i^3\sim dx_3$, es decir $i^\lambda$ transforma como $dx^\lambda$.
>
> **Paso 5 — cierre por la regla del cuociente.** Luego $i^\lambda$ **es** un cuadrivector. Como $\partial^2$ es escalar y $\partial^2 A^\mu=i^\mu$ vale en todo sistema cartesiano, por la **regla del cuociente** $A^\mu$ es tambien un cuadrivector, y $\partial^2 A^\mu=i^\mu$ es una legitima ecuacion tensorial. $\blacksquare$

> [!definicion] El tensor del campo electromagnetico
> A partir del cuadripotencial se construye el **tensor del campo electromagnetico** (tensor de Faraday):
> $$F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu=-F^{\nu\mu},$$
> antisimetrico de rango 2 (es un tensor porque $A^\mu$ es un cuadrivector). Reescribiendo $\vec E$ y $\vec B$ en terminos de $A^\mu$ (ec. 7.115), sus componentes son
> $$F_{\mu\nu}=\varepsilon_0\begin{pmatrix}0 & E_x & E_y & E_z\\ -E_x & 0 & -cB_z & cB_y\\ -E_y & cB_z & 0 & -cB_x\\ -E_z & -cB_y & cB_x & 0\end{pmatrix}.$$
> **Idea central:** en Minkowski $\vec E$ y $\vec B$ **no** son dos vectores separados, sino las componentes de **un** tensor de rango 2. La diagonal nula y la antisimetria dejan solo $6$ componentes independientes: las $3$ de $\vec E$ y las $3$ de $\vec B$.

> [!proposicion] Maxwell en forma tensorial
> Con $F_{\mu\nu}$ las cuatro ecuaciones colapsan en dos:
> - **Inhomogeneas** ($\vec\nabla\cdot\vec D=\rho$ y $\vec\nabla\times\vec H$): una divergencia cuadridimensional del tensor,
> $$\frac{\partial F_{\mu\nu}}{\partial x_\nu}=i_\mu.$$
> El lado izquierdo es la contraccion del tensor de rango 3 $\partial F^{\mu\nu}/\partial x_\lambda$, luego un vector.
> - **Homogeneas** ($\vec\nabla\times\vec E$ y $\vec\nabla\cdot\vec B=0$): con $t^{\lambda\mu\nu}=\partial^\lambda F^{\mu\nu}$ (tensor de rango 3),
> $$t^{\lambda\mu\nu}+t^{\nu\lambda\mu}+t^{\mu\nu\lambda}=0\qquad(\lambda,\mu,\nu\ \text{distintos}),$$
> la **identidad de Bianchi**. Es la suma ciclica de derivadas de $F$, p. ej. $\partial F_{23}/\partial x_1+\partial F_{31}/\partial x_2+\partial F_{12}/\partial x_3=0$ para $\vec\nabla\cdot\vec B=0$.

> [!info] Transformacion de $\vec E$ y $\vec B$ bajo un *boost*
> Como $\vec E$ y $\vec B$ son componentes del mismo tensor $F^{\mu\nu}$, un *boost* los **mezcla**. Para un *boost* en $z$ con $\beta=v/c$, $\gamma=(1-\beta^2)^{-1/2}$ (ec. 7.123-7.124):
>
> | Componente | Transformacion |
> |:---|:---|
> | $E'_x$ | $\gamma\left(E_x-v\,B_y\right)$ |
> | $E'_y$ | $\gamma\left(E_y+v\,B_x\right)$ |
> | $E'_z$ | $E_z$ |
> | $B'_x$ | $\gamma\left(B_x+\dfrac{v}{c^2}E_y\right)$ |
> | $B'_y$ | $\gamma\left(B_y-\dfrac{v}{c^2}E_x\right)$ |
> | $B'_z$ | $B_z$ |
>
> Las componentes paralelas al *boost* ($E_z$, $B_z$) no cambian; las transversales se mezclan. En el limite $\vec E=0$ esto da $\vec E'=\vec v\times\vec B$ (ver `## Ejemplo`).

> [!proposicion] Invariante electromagnetico
> Las propiedades tensoriales permiten construir invariantes. Uno importante es el producto escalar de los cuadrivectores $A^\lambda$ e $i_\lambda$:
> $$A^\lambda i_\lambda=\varepsilon_0\left(\rho\varphi-\vec A\cdot\vec J\right),\qquad \text{invariante.}$$
> El termino $\rho\varphi$ es el acoplamiento electrostatico (energia por unidad de volumen) y $\vec A\cdot\vec J$ la interaccion dinamica campo-corriente. Este invariante $A^\lambda i_\lambda$ aparece en el **lagrangiano** electromagnetico.

## Resumen

> [!resumen]
> | Objeto | Definicion | Papel |
> |:---|:---|:---|
> | Cuadripotencial | $A^\mu=(\varepsilon_0\varphi,\,c\varepsilon_0\vec A)$ | reune $\varphi$ y $\vec A$ |
> | Cuadricorriente | $i^\mu=(\rho,\,\rho\vec v/c)$ | reune $\rho$ y $\vec J$; es cuadrivector |
> | d'Alembertiano | $\partial^2=\nabla^2-\dfrac{1}{c^2}\partial_t^2=-\partial^\mu\partial_\mu$ | escalar de Lorentz |
> | Ec. de onda | $\partial^2 A^\mu=i^\mu$ | condensa las 2 inhomogeneas (potenciales) |
> | Tensor de campo | $F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu$ | antisimetrico, reune $\vec E$ y $\vec B$ |
> | Maxwell inhomogeneas | $\partial F_{\mu\nu}/\partial x_\nu=i_\mu$ | $\vec\nabla\cdot\vec D=\rho$, $\vec\nabla\times\vec H$ |
> | Maxwell homogeneas | $t^{\lambda\mu\nu}+t^{\nu\lambda\mu}+t^{\mu\nu\lambda}=0$ | Bianchi: $\vec\nabla\times\vec E$, $\vec\nabla\cdot\vec B=0$ |
> | Invariante | $A^\lambda i_\lambda=\varepsilon_0(\rho\varphi-\vec A\cdot\vec J)$ | aparece en el lagrangiano |

> [!corolario]
> Aqui converge **todo el curso**. El [[5 Coordenadas No Ortogonales/Notacion Subindices Superindices | algebra de indices]] co/contravariantes, los [[index | tensores]] como objetos con ley de transformacion definida, la [[5 Coordenadas No Ortogonales/Covarianza Contravarianza en Tensores | regla del cuociente]] y el [[Grupo Homogeneo de Lorentz | grupo de Lorentz]] culminan en un solo enunciado: el electromagnetismo es **una ecuacion tensorial**. Las cuatro ecuaciones de Maxwell, los campos $\vec E$ y $\vec B$, los potenciales $\varphi$ y $\vec A$ y las cargas $\rho$ y $\vec J$ no son piezas sueltas, sino las componentes de unos pocos tensores de Minkowski: $A^\mu$, $i^\mu$ y $F^{\mu\nu}$. Su covarianza de Lorentz, antes oculta tras la notacion vectorial 3D, se vuelve **manifiesta**. Asi el analisis tensorial deja de ser herramienta de calculo y se revela como el **idioma** en que estan escritas las leyes de la fisica.

> [!referencia]
> - La simetria subyacente: [[Grupo Homogeneo de Lorentz]] · [[index | Teoria de Grupo]].
> - Indices, metrica y subir/bajar: [[5 Coordenadas No Ortogonales/index]] · [[5 Coordenadas No Ortogonales/Derivadas Parciales Co y Contravariantes]].
> - Analogo bajo rotaciones reales: [[6 Determinantes y Matrices/Matrices Ortogonales]].
