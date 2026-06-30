---
title: Campos y Operadores
order: 1
tags:
  - electromagnetismo
  - teoria
  - calculo-vectorial
draft: false
aliases:
  - Operadores diferenciales
  - Gradiente divergencia rotacional
---

# Campos y Operadores $\nabla\varphi,\ \nabla\cdot\vec F,\ \nabla\times\vec F$

> [!definicion] Operadores diferenciales y el nabla
> Un **campo escalar** $\varphi(\vec r)$ asigna un número a cada punto del espacio; un **campo vectorial** $\vec F(\vec r)$ asigna un vector. Sobre ellos actúan los cuatro operadores diferenciales del cálculo vectorial, todos construidos a partir del **operador nabla**
> $$\nabla \;=\; \hat e_i\,\partial_i, \qquad \partial_i \equiv \frac{\partial}{\partial x_i},$$
> entendido como un "vector de derivadas" (con suma de Einstein sobre $i=1,2,3$, y $\hat e_i$ la base cartesiana). Con él se definen:
> $$\nabla\varphi \;\text{(gradiente)},\qquad \nabla\cdot\vec F \;\text{(divergencia)},\qquad \nabla\times\vec F \;\text{(rotacional)},\qquad \nabla^2\varphi \;\text{(laplaciano)}.$$
> El gradiente convierte escalar $\to$ vector; la divergencia, vector $\to$ escalar; el rotacional, vector $\to$ vector; el laplaciano, escalar $\to$ escalar. Son la base diferencial de todo el electromagnetismo (las ecuaciones de Maxwell se escriben con $\nabla\cdot$ y $\nabla\times$).

---

> [!info] Ubicación y referencias
> - **Curso:** Electromagnetismo, sección [[1 Calculo Vectorial/index | Cálculo Vectorial]].
> - **Notas hermanas:** [[Teoremas Integrales]] (Gauss y Stokes conectan estos operadores con flujo y circulación globales), [[Identidades Vectoriales]] (cómo se combinan: $\nabla\times\nabla\varphi=0$, $\nabla\cdot(\nabla\times\vec F)=0$, etc.) y [[Delta de Dirac y Singularidades]] (qué pasa cuando estos operadores actúan sobre $1/r$).
> - **Referencia base:** Griffiths, *Introduction to Electrodynamics*, cap. 1.
> - **Convenio:** unidades SI, vectores con flecha $\vec F$, base cartesiana ortonormal $\hat e_i$, suma de Einstein sobre índices repetidos, $\delta_{ij}$ (delta de Kronecker) y $\epsilon_{ijk}$ (símbolo de Levi-Civita).

---

## Ejemplo

> [!ejemplo] Un cálculo con los tres operadores de golpe
> Sea el campo escalar $\varphi(\vec r)=x^2 y + z$ y el campo vectorial
> $$\vec F(\vec r)=\big(y,\; -x,\; z^2\big),$$
> ambos en coordenadas cartesianas $(x,y,z)=(x_1,x_2,x_3)$. Calcula $\nabla\varphi$, $\nabla\cdot\vec F$ y $\nabla\times\vec F$, y evalúalos en el punto $P=(1,\,2,\,3)$.
>
> > [!solucion]-
> > **Gradiente** — derivamos $\varphi$ respecto a cada coordenada:
> > $$\nabla\varphi=\big(\partial_x\varphi,\ \partial_y\varphi,\ \partial_z\varphi\big)=\big(2xy,\ x^2,\ 1\big).$$
> > En $P=(1,2,3)$: $\ \nabla\varphi\big|_P=(2\cdot1\cdot2,\ 1^2,\ 1)=(4,\ 1,\ 1)$.
> >
> > **Divergencia** — sumamos las derivadas "diagonales" $\partial_i F_i$:
> > $$\nabla\cdot\vec F=\partial_x(y)+\partial_y(-x)+\partial_z(z^2)=0+0+2z=2z.$$
> > En $P$: $\ \nabla\cdot\vec F\big|_P=2\cdot3=6$. Como $6>0$, el punto $P$ se comporta como una **fuente** del campo.
> >
> > **Rotacional** — con la regla determinante $(\nabla\times\vec F)_i=\epsilon_{ijk}\partial_j F_k$:
> > $$\nabla\times\vec F=\big(\partial_y F_z-\partial_z F_y,\ \ \partial_z F_x-\partial_x F_z,\ \ \partial_x F_y-\partial_y F_x\big).$$
> > Componente a componente, con $F_x=y,\ F_y=-x,\ F_z=z^2$:
> > $$\big(\partial_y z^2-\partial_z(-x),\ \ \partial_z y-\partial_x z^2,\ \ \partial_x(-x)-\partial_y y\big)=(0-0,\ 0-0,\ -1-1)=(0,\ 0,\ -2).$$
> > El rotacional es **constante** $(0,0,-2)$: el campo $(y,-x,\cdot)$ "gira" en sentido horario en el plano $xy$, de ahí la componente $z$ negativa.
> >
> > **Verificación dimensional rápida.** Si $\varphi$ tiene unidades $[\varphi]$ y las coordenadas son metros, $\nabla\varphi$ tiene unidades $[\varphi]/\mathrm{m}$, $\nabla\cdot\vec F$ tiene $[\vec F]/\mathrm{m}$ y $\nabla\times\vec F$ también $[\vec F]/\mathrm{m}$: cada operador introduce un factor $1/\mathrm{m}$ por la derivada espacial. $\blacksquare$

---

## En qué consiste

> [!teoria] Campos escalares y vectoriales
> En el espacio físico cada punto está rotulado por $\vec r=x_i\,\hat e_i$. Una **función de campo** es cualquier asignación punto $\mapsto$ valor:
> - **Campo escalar** $\varphi(\vec r)$: un número en cada punto (temperatura, potencial eléctrico $V$, densidad). Sus "curvas de nivel" (o superficies de nivel en 3D) son los lugares $\varphi=\text{cte}$.
> - **Campo vectorial** $\vec F(\vec r)=F_i(\vec r)\,\hat e_i$: un vector en cada punto (campo eléctrico $\vec E$, velocidad de un fluido $\vec v$). Se visualiza con flechas o con líneas de campo tangentes a $\vec F$.
>
> Los operadores diferenciales miden **cómo cambia** el campo de un punto a otro. El nabla $\nabla=\hat e_i\,\partial_i$ es la herramienta común: aunque se escribe como vector, es un operador, y el orden importa ($\nabla\varphi\neq\varphi\nabla$, $\nabla\cdot\vec F$ es escalar pero $\vec F\cdot\nabla$ es operador).

![[campos_escalar_vectorial.svg|460]]

*Izquierda: campo escalar $\varphi$ con sus curvas de nivel. Derecha: campo vectorial $\vec F$ representado por flechas / líneas de campo.*

---

### Gradiente

> [!definicion] Gradiente
> El **gradiente** de un campo escalar $\varphi$ es el campo vectorial $\nabla\varphi$ definido por la relación con el **diferencial total** $d\varphi$ a lo largo de un desplazamiento $d\vec l$:
> $$\boxed{\,d\varphi=\nabla\varphi\cdot d\vec l\,}.$$
> Es decir, $\nabla\varphi$ es el vector que, proyectado sobre $d\vec l$, reproduce el cambio de $\varphi$.

> [!proposicion] Forma cartesiana del gradiente
> En coordenadas cartesianas, $(\nabla\varphi)_i=\partial_i\varphi$, esto es $\nabla\varphi=(\partial_x\varphi,\,\partial_y\varphi,\,\partial_z\varphi)$.
>
> > [!demostracion]-
> > **Paso 1 — diferencial total.** Para un desplazamiento $d\vec l=dx_i\,\hat e_i$, la regla de la cadena da el diferencial total de $\varphi$:
> > $$d\varphi=\frac{\partial\varphi}{\partial x_i}\,dx_i=\partial_i\varphi\,dx_i \qquad(\text{suma sobre }i).$$
> > **Paso 2 — escribir como producto escalar.** Sea $\nabla\varphi=(\nabla\varphi)_j\,\hat e_j$ un vector aún por determinar. Su producto con $d\vec l$ es
> > $$\nabla\varphi\cdot d\vec l=(\nabla\varphi)_j\,\hat e_j\cdot \hat e_i\,dx_i=(\nabla\varphi)_j\,\delta_{ji}\,dx_i=(\nabla\varphi)_i\,dx_i,$$
> > usando $\hat e_j\cdot\hat e_i=\delta_{ji}$ y la propiedad de filtro de la delta de Kronecker. **Paso 3 — igualar.** La definición exige $d\varphi=\nabla\varphi\cdot d\vec l$ para **todo** $d\vec l$. Comparando el Paso 1 con el Paso 2:
> > $$\partial_i\varphi\,dx_i=(\nabla\varphi)_i\,dx_i\quad\forall\,dx_i\ \Longrightarrow\ (\nabla\varphi)_i=\partial_i\varphi.\qquad\blacksquare$$

![[gradiente.svg|360]]

*El gradiente $\nabla\varphi$ (flechas) es perpendicular a las curvas de nivel $\varphi=\text{cte}$ y apunta hacia los valores crecientes de $\varphi$.*

> [!proposicion] El gradiente es perpendicular a las superficies de nivel
> Sobre una superficie de nivel $\varphi=\text{cte}$, el gradiente $\nabla\varphi$ es ortogonal a la superficie en cada punto.
>
> > [!demostracion]-
> > **Paso 1 — moverse sobre la superficie.** Si $d\vec l$ es un desplazamiento **tangente** a la superficie de nivel, entonces nos quedamos en $\varphi=\text{cte}$ y por tanto $\varphi$ no cambia: $d\varphi=0$. **Paso 2 — usar la definición.** Pero $d\varphi=\nabla\varphi\cdot d\vec l$, luego
> > $$\nabla\varphi\cdot d\vec l=0\qquad\text{para todo }d\vec l\text{ tangente.}$$
> > **Paso 3 — concluir.** Un vector ortogonal a todo desplazamiento tangente a la superficie es, por definición, **normal** a la superficie. Por tanto $\nabla\varphi\perp\{\varphi=\text{cte}\}$. $\blacksquare$

> [!proposicion] El gradiente apunta en la dirección de máximo crecimiento
> De entre todas las direcciones, $\nabla\varphi$ señala aquella en que $\varphi$ crece más rápido, y $|\nabla\varphi|$ es esa tasa máxima de crecimiento por unidad de longitud.
>
> > [!demostracion]-
> > **Paso 1 — desplazamiento de longitud fija.** Tomemos $d\vec l$ de módulo fijo $|d\vec l|$ y dirección variable, formando un ángulo $\theta$ con $\nabla\varphi$. Por la definición del producto escalar:
> > $$d\varphi=\nabla\varphi\cdot d\vec l=|\nabla\varphi|\,|d\vec l|\cos\theta.$$
> > **Paso 2 — maximizar en $\theta$.** Con $|\nabla\varphi|$ y $|d\vec l|$ fijos, $d\varphi$ es máximo cuando $\cos\theta=1$, es decir $\theta=0$: el desplazamiento alineado con $\nabla\varphi$. **Paso 3 — tasa máxima.** En ese caso $d\varphi=|\nabla\varphi|\,|d\vec l|$, de donde la derivada direccional máxima es $d\varphi/|d\vec l|=|\nabla\varphi|$. (Análogamente, $\theta=\pi$ da el descenso más rápido y $\theta=\pi/2$ da $d\varphi=0$, consistente con la superficie de nivel.) $\blacksquare$

---

### Divergencia

> [!definicion] Divergencia (flujo por unidad de volumen)
> La **divergencia** de $\vec F$ en un punto mide el flujo neto que sale de un volumen infinitesimal por unidad de volumen:
> $$\boxed{\ \nabla\cdot\vec F=\lim_{V\to0}\frac1V\oint_S \vec F\cdot d\vec A\ },$$
> donde $S$ es la superficie cerrada que rodea a $V$ y $d\vec A$ apunta hacia afuera. Si $\nabla\cdot\vec F>0$ el punto es una **fuente** (sale más de lo que entra); si $<0$, un **sumidero**.

![[divergencia.svg|460]]

*Divergencia positiva (fuente, flechas saliendo) frente a divergencia nula (lo que entra iguala lo que sale).*

> [!proposicion] Forma cartesiana de la divergencia
> $\displaystyle \nabla\cdot\vec F=\partial_i F_i=\partial_x F_x+\partial_y F_y+\partial_z F_z$.
>
> > [!demostracion]-
> > **Paso 1 — cubito infinitesimal.** Centramos un paralelepípedo de lados $dx,dy,dz$ (volumen $V=dx\,dy\,dz$) en el punto $\vec r$. Calcularemos el flujo $\oint_S\vec F\cdot d\vec A$ sumando las contribuciones de las seis caras, agrupadas en tres pares opuestos.
> >
> > **Paso 2 — par de caras $\perp x$.** Las dos caras normales a $\hat e_1$ tienen área $dy\,dz$ y normales $\pm\hat e_1$. Sólo cuenta $F_x$.
> > - Cara en $x+\tfrac{dx}{2}$ (normal $+\hat e_1$): aporta $+F_x\!\left(x+\tfrac{dx}{2}\right)dy\,dz$.
> > - Cara en $x-\tfrac{dx}{2}$ (normal $-\hat e_1$): aporta $-F_x\!\left(x-\tfrac{dx}{2}\right)dy\,dz$.
> >
> > Sumando y desarrollando por **Taylor** a primer orden, $F_x\!\left(x\pm\tfrac{dx}{2}\right)\approx F_x\pm\tfrac{dx}{2}\,\partial_x F_x$, los términos $F_x$ se cancelan y queda
> > $$\Big[\partial_x F_x\Big]\,dx\,dy\,dz.$$
> >
> > **Paso 3 — los otros dos pares.** Idéntico razonamiento para las caras $\perp y$ (con $F_y$) y $\perp z$ (con $F_z$):
> > $$\big[\partial_y F_y\big]\,dx\,dy\,dz,\qquad \big[\partial_z F_z\big]\,dx\,dy\,dz.$$
> >
> > **Paso 4 — flujo total y límite.** El flujo neto es la suma:
> > $$\oint_S\vec F\cdot d\vec A=\big(\partial_x F_x+\partial_y F_y+\partial_z F_z\big)\,dx\,dy\,dz=\big(\partial_i F_i\big)\,V.$$
> > Dividiendo por $V$ y tomando $V\to0$:
> > $$\nabla\cdot\vec F=\lim_{V\to0}\frac1V\oint_S\vec F\cdot d\vec A=\partial_i F_i.\qquad\blacksquare$$

---

### Rotacional

> [!definicion] Rotacional (circulación por unidad de área)
> La componente del **rotacional** de $\vec F$ a lo largo de una normal $\hat n$ mide la circulación de $\vec F$ por unidad de área alrededor de una curva pequeña en el plano $\perp\hat n$:
> $$\boxed{\ (\nabla\times\vec F)\cdot\hat n=\lim_{A\to0}\frac1A\oint_C \vec F\cdot d\vec l\ },$$
> con $C$ recorrida en el sentido dado por $\hat n$ por la regla de la mano derecha. Mide la tendencia del campo a "girar" localmente.

![[rotacional.svg|360]]

*El rotacional mide la circulación de $\vec F$ alrededor de un lazo infinitesimal; aquí la componente $z$ del giro en el plano $xy$.*

> [!proposicion] Forma cartesiana del rotacional
> $\displaystyle (\nabla\times\vec F)_i=\epsilon_{ijk}\,\partial_j F_k$, equivalente al determinante simbólico
> $$\nabla\times\vec F=\begin{vmatrix}\hat e_1 & \hat e_2 & \hat e_3\\[2pt] \partial_x & \partial_y & \partial_z\\[2pt] F_x & F_y & F_z\end{vmatrix}.$$
>
> > [!demostracion]-
> > **Paso 1 — cuadrito en el plano $xy$.** Calculamos la componente $z$ tomando $\hat n=\hat e_3$ y una curva rectangular $C$ de lados $dx,dy$ (área $A=dx\,dy$) centrada en $\vec r$, recorrida en sentido antihorario: derecha $\to$ arriba $\to$ izquierda $\to$ abajo. Como $d\vec l$ vive en el plano $xy$, sólo entran $F_x$ y $F_y$.
> >
> > **Paso 2 — ramas horizontales (aportan $F_x$).**
> > - Rama inferior ($y-\tfrac{dy}{2}$, sentido $+\hat e_1$): $+F_x\!\left(y-\tfrac{dy}{2}\right)dx$.
> > - Rama superior ($y+\tfrac{dy}{2}$, sentido $-\hat e_1$): $-F_x\!\left(y+\tfrac{dy}{2}\right)dx$.
> >
> > Por **Taylor**, $F_x\!\left(y\pm\tfrac{dy}{2}\right)\approx F_x\pm\tfrac{dy}{2}\,\partial_y F_x$, los $F_x$ se cancelan y suman
> > $$-\big(\partial_y F_x\big)\,dy\,dx.$$
> >
> > **Paso 3 — ramas verticales (aportan $F_y$).**
> > - Rama derecha ($x+\tfrac{dx}{2}$, sentido $+\hat e_2$): $+F_y\!\left(x+\tfrac{dx}{2}\right)dy$.
> > - Rama izquierda ($x-\tfrac{dx}{2}$, sentido $-\hat e_2$): $-F_y\!\left(x-\tfrac{dx}{2}\right)dy$.
> >
> > Análogamente, suman $+\big(\partial_x F_y\big)\,dx\,dy$.
> >
> > **Paso 4 — circulación total y límite.**
> > $$\oint_C\vec F\cdot d\vec l=\big(\partial_x F_y-\partial_y F_x\big)\,dx\,dy=\big(\partial_x F_y-\partial_y F_x\big)\,A.$$
> > Dividiendo por $A$ y tomando $A\to0$:
> > $$(\nabla\times\vec F)_z=\partial_x F_y-\partial_y F_x.$$
> > **Paso 5 — generalizar por permutación cíclica.** Repitiendo en los planos $yz$ y $zx$ se obtienen las otras componentes, todas resumibles en
> > $$(\nabla\times\vec F)_i=\epsilon_{ijk}\,\partial_j F_k,$$
> > pues $\epsilon_{3jk}\partial_j F_k=\partial_1 F_2-\partial_2 F_1=\partial_x F_y-\partial_y F_x$ reproduce el caso recién calculado. $\blacksquare$

> [!warning] El rotacional sólo es un vector en 3D
> La expresión $(\nabla\times\vec F)_i=\epsilon_{ijk}\partial_j F_k$ usa el símbolo $\epsilon_{ijk}$ de **tres** índices, propio de $\mathbb R^3$. En 2D el rotacional se reduce a un único escalar $\partial_x F_y-\partial_y F_x$, y en dimensión $n>3$ el objeto natural ya no es un vector sino un **tensor antisimétrico** (la 2-forma $\partial_j F_k-\partial_k F_j$). Por eso $\nabla\times$ es exclusivo del espacio tridimensional.

---

### Laplaciano

> [!definicion] Laplaciano
> El **laplaciano** de un campo escalar es la divergencia de su gradiente:
> $$\nabla^2\varphi=\nabla\cdot(\nabla\varphi).$$

> [!proposicion] Forma cartesiana del laplaciano
> $\displaystyle \nabla^2\varphi=\partial_i\partial_i\varphi=\partial_x^2\varphi+\partial_y^2\varphi+\partial_z^2\varphi$.
>
> > [!demostracion]-
> > **Paso 1 — gradiente.** Por la forma cartesiana del gradiente, $(\nabla\varphi)_i=\partial_i\varphi$. **Paso 2 — divergencia del gradiente.** Aplicamos $\nabla\cdot(\,\cdot\,)=\partial_i(\,\cdot\,)_i$ al vector $\nabla\varphi$:
> > $$\nabla^2\varphi=\nabla\cdot(\nabla\varphi)=\partial_i\,(\nabla\varphi)_i=\partial_i\,\partial_i\varphi.$$
> > Desarrollando la suma sobre $i$: $\ \partial_i\partial_i\varphi=\partial_x^2\varphi+\partial_y^2\varphi+\partial_z^2\varphi$. $\blacksquare$
>
> Para un campo **vectorial**, el laplaciano actúa componente a componente en cartesianas:
> $$\nabla^2\vec F=\big(\partial_j\partial_j F_i\big)\,\hat e_i,$$
> es decir $(\nabla^2\vec F)_i=\partial_j\partial_j F_i$. (Cuidado: esto sólo es así en cartesianas; en coordenadas curvilíneas $\nabla^2\vec F\neq(\nabla^2 F_i)\hat e_i$ porque los $\hat e_i$ también varían.)

---

> [!proposicion] Formas indiciales — resumen operativo
> En coordenadas cartesianas, con suma de Einstein:
> $$
> \begin{aligned}
> (\nabla\varphi)_i &= \partial_i\varphi, \\[4pt]
> \nabla\cdot\vec F &= \partial_i F_i, \\[4pt]
> (\nabla\times\vec F)_i &= \epsilon_{ijk}\,\partial_j F_k, \\[4pt]
> \nabla^2\varphi &= \partial_i\partial_i\varphi.
> \end{aligned}
> $$
> Esta notación es la palanca para probar las identidades vectoriales: basta manipular $\delta_{ij}$ y $\epsilon_{ijk}$ (ver [[Identidades Vectoriales]]).

---

## Resumen

> [!resumen] Los cuatro operadores
>
> | Operador | Símbolo | Entrada $\to$ salida | Forma indicial | Significado geométrico |
> |---|---|---|---|---|
> | Gradiente | $\nabla\varphi$ | escalar $\to$ vector | $(\nabla\varphi)_i=\partial_i\varphi$ | $\perp$ a niveles; máximo crecimiento |
> | Divergencia | $\nabla\cdot\vec F$ | vector $\to$ escalar | $\partial_i F_i$ | flujo por unidad de volumen (fuente/sumidero) |
> | Rotacional | $\nabla\times\vec F$ | vector $\to$ vector | $\epsilon_{ijk}\partial_j F_k$ | circulación por unidad de área (giro) |
> | Laplaciano | $\nabla^2\varphi$ | escalar $\to$ escalar | $\partial_i\partial_i\varphi$ | $\nabla\cdot(\nabla\varphi)$; curvatura/promedio |

> [!corolario] Por qué importan en electromagnetismo
> Las ecuaciones de Maxwell son afirmaciones directas sobre estos operadores: $\nabla\cdot\vec E=\rho/\varepsilon_0$ (la carga es fuente de $\vec E$), $\nabla\cdot\vec B=0$ (no hay monopolos), $\nabla\times\vec E=-\partial_t\vec B$ y $\nabla\times\vec B=\mu_0\vec J+\mu_0\varepsilon_0\,\partial_t\vec E$. El potencial cumple $\vec E=-\nabla V$ y, en electrostática, $\nabla^2 V=-\rho/\varepsilon_0$ (ecuación de Poisson). Dominar gradiente, divergencia, rotacional y laplaciano es dominar la maquinaria diferencial de todo el curso.

> [!referencia] Fuentes
> - Griffiths, D. J. *Introduction to Electrodynamics*, cap. 1 ("Vector Analysis").
> - Notas hermanas: [[Teoremas Integrales]], [[Identidades Vectoriales]], [[Delta de Dirac y Singularidades]].
> - Índice del curso: [[1 Calculo Vectorial/index | Cálculo Vectorial]].
