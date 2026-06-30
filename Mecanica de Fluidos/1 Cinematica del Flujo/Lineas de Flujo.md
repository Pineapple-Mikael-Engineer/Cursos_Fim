---
title: Líneas de Flujo
order: 2
tags:
  - fluidos
  - teoria
  - cinematica
draft: false
aliases:
  - Líneas de flujo
  - Líneas de corriente
  - Trayectorias y trazas
---

# Líneas de Flujo $\dfrac{dx}{u}=\dfrac{dy}{v}=\dfrac{dz}{w}$

> [!definicion]
> Las **líneas de flujo** son las curvas con las que visualizamos un campo de velocidades $\vec v(\vec x,t)=(u,v,w)$. Hay tres familias que conviene **no confundir**:
>
> - **Línea de corriente** (*streamline*): curva **tangente en cada punto al campo de velocidades en un instante fijo** $t$. Es una "foto" del campo. Su condición es
> $$d\vec x\times\vec v=\vec 0\qquad\Longleftrightarrow\qquad \dfrac{dx}{u}=\dfrac{dy}{v}=\dfrac{dz}{w}.$$
> - **Trayectoria** (*pathline*): el **camino real que recorre UNA partícula** a lo largo del tiempo. Resuelve $\dfrac{d\vec x}{dt}=\vec v(\vec x,t)$.
> - **Traza** (*streakline*): el lugar de **todas las partículas que han pasado por un punto fijo** (el penacho de humo o de tinta inyectado en ese punto).
>
> En **flujo estacionario** ($\partial_t\vec v=\vec 0$) las tres familias **coinciden**; en flujo no estacionario, en general, **difieren**.

---

> [!info]
> Nota de la sección [[1 Cinematica del Flujo/index | Cinemática del Flujo]]. Hermanas: [[Descripcion Euleriana y Lagrangiana]] (los dos puntos de vista y la derivada material) y [[Tensor Gradiente de Velocidad]] (la estructura local $\partial_j v_i=e_{ij}+\omega_{ij}$). **Referencia.** Landau-Lifshitz, Vol. 6 (*Mecánica de Fluidos*), §1; Batchelor, *An Introduction to Fluid Dynamics*, cap. 2.

---

![[lineas_flujo.svg|460]]
*Líneas de corriente de un campo $\vec v$: en cada punto la curva es tangente al vector velocidad de ese instante. El tubo de corriente está formado por todas las líneas que pasan por una curva cerrada; sus paredes no dejan pasar fluido.*

---

## La condición de tangencia

> [!teoria] Por qué $d\vec x\times\vec v=\vec 0$ es $\dfrac{dx}{u}=\dfrac{dy}{v}=\dfrac{dz}{w}$
> Una línea de corriente, por definición, es **tangente al campo de velocidades** en el instante considerado. Que el desplazamiento infinitesimal $d\vec x=(dx,dy,dz)$ a lo largo de la curva sea paralelo a $\vec v=(u,v,w)$ equivale a que su producto vectorial se anule. Esa única ecuación vectorial esconde el sistema de proporciones que usamos para integrar.

> [!demostracion] De $d\vec x\times\vec v=\vec 0$ al sistema de proporciones
> Dos vectores son paralelos si y solo si su producto vectorial es nulo. Imponemos $d\vec x\,\|\,\vec v$:
> $$d\vec x\times\vec v=\begin{vmatrix}\hat\imath & \hat\jmath & \hat k\\ dx & dy & dz\\ u & v & w\end{vmatrix}=\vec 0.$$
>
> **Paso 1 — Desarrollar el determinante.** Componente a componente,
> $$d\vec x\times\vec v=\big(dy\,w-dz\,v\big)\,\hat\imath-\big(dx\,w-dz\,u\big)\,\hat\jmath+\big(dx\,v-dy\,u\big)\,\hat k.$$
>
> **Paso 2 — Anular cada componente.** Que el vector sea nulo obliga a las tres ecuaciones
> $$dy\,w=dz\,v,\qquad dx\,w=dz\,u,\qquad dx\,v=dy\,u.$$
>
> **Paso 3 — Reescribir como proporciones.** Despejando los cocientes (con $u,v,w\neq 0$):
> $$\frac{dy}{v}=\frac{dz}{w},\qquad \frac{dx}{u}=\frac{dz}{w},\qquad \frac{dx}{u}=\frac{dy}{v}.$$
> Las tres igualdades son la misma cadena escrita por pares; juntándolas,
> $$\boxed{\ \dfrac{dx}{u}=\dfrac{dy}{v}=\dfrac{dz}{w}\ }.$$
>
> El tiempo $t$ entra solo como **parámetro fijo**: $u,v,w$ se evalúan en ese instante. $\blacksquare$

> [!proposicion] Las tres familias de un vistazo
> | Familia | Definición física | Ecuación a integrar | Tiempo |
> |:---|:---|:---|:---|
> | Línea de corriente | tangente a $\vec v$ en un instante fijo | $\dfrac{dx}{u}=\dfrac{dy}{v}=\dfrac{dz}{w}$ | $t$ congelado |
> | Trayectoria | camino real de **una** partícula | $\dfrac{d\vec x}{dt}=\vec v(\vec x,t)$ | $t$ corre |
> | Traza | partículas que pasaron por un punto fijo | une las posiciones a $t$ de partículas soltadas en $\vec x_0$ | $t$ corre |

---

## El teorema de coincidencia en flujo estacionario

> [!teorema] En flujo estacionario, línea de corriente = trayectoria = traza
> Si el campo es **estacionario**, $\partial_t\vec v=\vec 0$, es decir $\vec v=\vec v(\vec x)$ sin depender explícitamente de $t$, entonces las **líneas de corriente, las trayectorias y las trazas son la misma familia de curvas**.

> [!demostracion]
> **Paso 1 — Trayectoria.** Una partícula obedece a $\dfrac{d\vec x}{dt}=\vec v(\vec x,t)$. Como el flujo es estacionario, $\vec v$ no depende de $t$ y el sistema se reduce a un sistema **autónomo**
> $$\frac{d\vec x}{dt}=\vec v(\vec x),\qquad\text{componente a componente }\ \frac{dx}{dt}=u,\ \ \frac{dy}{dt}=v,\ \ \frac{dz}{dt}=w.$$
>
> **Paso 2 — Eliminar el tiempo.** De esas tres relaciones despejamos $dt$ en cada una y las igualamos:
> $$dt=\frac{dx}{u}=\frac{dy}{v}=\frac{dz}{w}.$$
> Estas proporciones son **exactamente** la condición de tangencia de las líneas de corriente del Paso anterior. Por tanto, **la trayectoria recorre una línea de corriente**.
>
> **Paso 3 — Por qué coinciden como curvas.** El campo no cambia con el tiempo: la "foto" tangente a $\vec v$ es la misma en todo instante. Una partícula que arranca en un punto sigue en cada instante la dirección de $\vec v$ en su posición, que es precisamente la tangente a la línea de corriente que pasa por ahí. No puede salirse de esa línea, porque para hacerlo necesitaría una velocidad transversal a $\vec v$, que no existe. Así, la **trayectoria** coincide con la **línea de corriente**.
>
> **Paso 4 — La traza.** Una traza une las partículas que pasaron por un punto fijo $\vec x_0$. En flujo estacionario, **toda** partícula que pase por $\vec x_0$ sigue después la **misma** línea de corriente (la que pasa por $\vec x_0$), porque el campo no cambia entre una partícula y la siguiente. Luego la traza es también esa línea de corriente.
>
> Las tres familias coinciden. $\blacksquare$

> [!warning]
> En flujo **NO estacionario** ($\partial_t\vec v\neq\vec 0$) las tres familias son **distintas**:
> $$\text{línea de corriente}\ \neq\ \text{trayectoria}\ \neq\ \text{traza}.$$
> La razón: al integrar la trayectoria el campo cambia mientras la partícula viaja, mientras que la línea de corriente congela el instante. **Solo coinciden cuando $\partial_t\vec v=\vec 0$.** Cuidado con las fotos de humo o tinta en un túnel de viento: muestran **trazas**, no líneas de corriente; solo si el flujo es estacionario se las puede leer como líneas de corriente.

---

## Tubo de corriente y conservación del caudal

> [!definicion] Tubo de corriente
> Tómese una curva cerrada $C$ que no sea ella misma una línea de corriente, y trácense las líneas de corriente que pasan por cada uno de sus puntos. La superficie así engendrada es un **tubo de corriente**. Por construcción, en cada punto de su pared $\vec v$ es **tangente** a la superficie.

> [!teorema] El caudal se conserva a lo largo del tubo
> En flujo **estacionario e incompresible**, el caudal volumétrico
> $$Q=\int_A\vec v\cdot d\vec A$$
> que atraviesa cualquier sección $A$ del tubo es **el mismo en todas las secciones**.

> [!demostracion]
> Sea el trozo de tubo comprendido entre dos secciones $A_1$ (entrada) y $A_2$ (salida), con la pared lateral $A_\ell$. La frontera cerrada de ese volumen $V$ es $A_1\cup A_2\cup A_\ell$.
>
> **Paso 1 — Incompresibilidad.** Para un fluido incompresible la dilatación es nula (ver [[Tensor Gradiente de Velocidad]]):
> $$\nabla\cdot\vec v=0\quad\text{en todo }V.$$
>
> **Paso 2 — Teorema de la divergencia.** El flujo neto de $\vec v$ por la frontera cerrada es la integral de la divergencia:
> $$\oint_{\partial V}\vec v\cdot d\vec A=\int_V(\nabla\cdot\vec v)\,dV=0.$$
>
> **Paso 3 — Anular la pared.** En la pared lateral $A_\ell$ el campo es tangente al tubo, luego $\vec v\cdot d\vec A=0$ allí (la normal $d\vec A$ es perpendicular a $\vec v$). Entonces solo sobreviven las tapas:
> $$\int_{A_1}\vec v\cdot d\vec A+\int_{A_2}\vec v\cdot d\vec A=0.$$
>
> **Paso 4 — Orientar las normales.** Tomando ambas normales en el sentido del flujo (saliente en $A_2$, entrante en $A_1$, lo que cambia el signo de la primera integral):
> $$\int_{A_2}\vec v\cdot d\vec A=\int_{A_1}\vec v\cdot d\vec A\quad\Longrightarrow\quad Q_2=Q_1.$$
>
> El caudal es **constante a lo largo del tubo**. Como corolario, donde el tubo se estrecha el fluido **acelera** ($\overline{v}_2 A_2=\overline{v}_1 A_1$). $\blacksquare$

---

## Ejemplo

> [!ejemplo] Punto de estancamiento (estacionario) vs. campo no estacionario
> **(a)** Flujo de punto de estancamiento, estacionario: $\vec v=(x,\,-y,\,0)$. **(b)** Flujo no estacionario: $\vec v=(a,\,b\,t,\,0)$ con $a,b>0$ constantes. En ambos hallaremos línea de corriente y trayectoria y veremos si coinciden.

> [!solucion] (a) Campo estacionario $\vec v=(x,-y,0)$
> **Paso 1 — Línea de corriente.** Con $u=x$, $v=-y$:
> $$\frac{dx}{x}=\frac{dy}{-y}\ \Longrightarrow\ \int\frac{dx}{x}=-\int\frac{dy}{y}\ \Longrightarrow\ \ln|x|=-\ln|y|+\text{cte}.$$
> Por tanto
> $$\boxed{\,xy=\text{cte}\,}$$
> una familia de **hipérbolas**: las líneas de corriente del campo.
>
> **Paso 2 — Trayectoria.** Integramos $\dfrac{dx}{dt}=x$ y $\dfrac{dy}{dt}=-y$ con $(x_0,y_0)$ en $t=0$:
> $$x(t)=x_0\,e^{t},\qquad y(t)=y_0\,e^{-t}.$$
>
> **Paso 3 — Comparar.** El producto es
> $$x(t)\,y(t)=x_0 e^{t}\,y_0 e^{-t}=x_0 y_0=\text{cte}.$$
> La trayectoria recorre la **misma hipérbola** $xy=$ cte. **Coinciden**, como predice el teorema (flujo estacionario). $\blacksquare$

> [!solucion] (b) Campo no estacionario $\vec v=(a,\,b\,t,\,0)$
> **Paso 1 — Línea de corriente (instante fijo $t=\tau$).** El tiempo es un parámetro congelado: $u=a$, $v=b\tau$.
> $$\frac{dx}{a}=\frac{dy}{b\tau}\ \Longrightarrow\ \frac{dy}{dx}=\frac{b\tau}{a}\ \Longrightarrow\ y=\frac{b\tau}{a}\,x+\text{cte}.$$
> Es una **recta** cuya pendiente $b\tau/a$ depende del instante $\tau$ elegido.
>
> **Paso 2 — Trayectoria.** Ahora $t$ corre. Con $(x_0,y_0)$ en $t=0$:
> $$\frac{dx}{dt}=a\ \Rightarrow\ x(t)=x_0+a\,t,\qquad \frac{dy}{dt}=b\,t\ \Rightarrow\ y(t)=y_0+\tfrac12 b\,t^{2}.$$
>
> **Paso 3 — Eliminar el tiempo.** De la primera, $t=(x-x_0)/a$; sustituyendo,
> $$y=y_0+\frac{b}{2a^{2}}\,(x-x_0)^{2},$$
> una **parábola**.
>
> **Paso 4 — Comparar.** La línea de corriente es una recta y la trayectoria una parábola: **no coinciden**. Es la firma de un flujo **no estacionario**: la condición de tangencia (instante congelado) y la integración real en el tiempo dan curvas distintas. $\blacksquare$

---

## En qué consiste

> [!teoria] La idea, en una frase
> Las líneas de flujo son tres maneras distintas de **dibujar el mismo campo de velocidades**, según qué se congele:
>
> - La **línea de corriente** congela el **tiempo** y sigue la dirección de $\vec v$ por el espacio: una foto instantánea. Se integra resolviendo $\dfrac{dx}{u}=\dfrac{dy}{v}=\dfrac{dz}{w}$ con $t$ fijo.
> - La **trayectoria** congela la **partícula** y la deja viajar: su historia personal, $\dfrac{d\vec x}{dt}=\vec v$.
> - La **traza** congela el **punto de inyección** y reúne a todos los que pasaron por él: lo que se ve experimentalmente con humo o tinta.
>
> El **flujo estacionario** ($\partial_t\vec v=\vec 0$) es el caso amable: las tres se funden en una. Allí, el **tubo de corriente** se vuelve una tubería virtual sin fugas por sus paredes, y de ahí sale gratis la **conservación del caudal** $Q=\int_A\vec v\cdot d\vec A$: el fluido acelera donde el tubo se estrecha. En cuanto el campo cambia con el tiempo, las tres curvas se separan y hay que distinguirlas con cuidado.

---

## Resumen

> [!resumen]
> | Concepto | Condición / ecuación | Qué describe |
> |:---|:---|:---|
> | Línea de corriente | $d\vec x\times\vec v=\vec 0$, o $\dfrac{dx}{u}=\dfrac{dy}{v}=\dfrac{dz}{w}$ | tangente a $\vec v$ en un instante fijo |
> | Trayectoria | $\dfrac{d\vec x}{dt}=\vec v(\vec x,t)$ | camino real de una partícula |
> | Traza | partículas que pasaron por $\vec x_0$ | penacho de humo/tinta inyectado |
> | Coincidencia | $\partial_t\vec v=\vec 0$ (estacionario) | las tres familias son la misma |
> | Tubo de corriente | $\vec v$ tangente a la pared | sin flujo por las paredes |
> | Caudal | $Q=\int_A\vec v\cdot d\vec A=\text{cte}$ | se conserva a lo largo del tubo (estacionario incompresible) |

> [!corolario]
> En flujo estacionario basta una sola familia de curvas para entenderlo todo: las líneas de corriente **son** las trayectorias **son** las trazas, y el tubo de corriente conserva el caudal. En flujo no estacionario hay que separar los tres conceptos: una foto de humo es una **traza**, no una línea de corriente, y la trayectoria de una partícula puede ser muy distinta de ambas (como la recta frente a la parábola del ejemplo (b)).

> [!referencia]
> Landau-Lifshitz, *Mecánica de Fluidos* (Vol. 6), §1; Batchelor, *An Introduction to Fluid Dynamics*, cap. 2 (líneas de corriente, trayectorias, trazas y tubos de corriente). Continúa en [[Tensor Gradiente de Velocidad]].
