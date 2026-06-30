---
title: Cuadrivectores
order: 1
tags:
  - electromagnetismo
  - teoria
  - covariante
draft: false
aliases:
  - Cuadrivectores
  - Espaciotiempo de Minkowski
  - Métrica de Minkowski
---

# Cuadrivectores $x^\mu=(ct,\vec x),\quad \eta_{\mu\nu}=\mathrm{diag}(+,-,-,-)$

> [!definicion]
> Un **cuadrivector** $A^\mu$ ($\mu=0,1,2,3$) es un objeto de cuatro componentes que, bajo un cambio de observador inercial, se transforma **exactamente como** la cuadriposición $x^\mu=(ct,\vec x)$ del espaciotiempo de Minkowski:
> $$A'^\mu=\Lambda^\mu{}_\nu\,A^\nu,$$
> donde $\Lambda^\mu{}_\nu$ es una **transformación de Lorentz**. El espaciotiempo viene equipado con la **métrica de Minkowski**
> $$\eta_{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1),$$
> que define el **producto escalar invariante** $A\cdot B=\eta_{\mu\nu}A^\mu B^\nu$ y, con él, la noción de longitud y ángulo en el espaciotiempo. La componente $0$ es temporal; las componentes $1,2,3$ son espaciales y forman el trivector $\vec A$.

---

> [!info]
> Primera nota de la sección [[6 Formulacion Covariante/index | Formulación Covariante]]. Aquí se monta el **andamiaje**: espaciotiempo, métrica, índices arriba/abajo, invariantes y boosts de Lorentz. Las hermanas lo usan: [[Tensor de Campo]] construye $F^{\mu\nu}$ a partir del cuadripotencial $A^\mu$, y [[Maxwell Covariante]] escribe las ecuaciones del campo con el cuadrigradiente $\partial_\mu$ y la cuadricorriente $J^\mu$ definidos aquí. **Convenio.** Métrica $\eta_{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1)$ (el de **Landau** y física de partículas); índices griegos $0\!-\!3$, latinos $1\!-\!3$; convenio de suma de Einstein. **Referencia.** Griffiths cap. 12; **Landau-Lifshitz Vol. 2** (*Teoría Clásica de Campos*).

---

## Espaciotiempo y el intervalo invariante

> [!teoria] El intervalo es lo que todos los observadores comparten
> La relatividad especial parte de un hecho: la velocidad de la luz $c$ es la misma para todo observador inercial. La consecuencia geométrica es que ni las distancias ni los tiempos son absolutos, pero **sí lo es** una combinación de ambos: el **intervalo** entre dos sucesos infinitesimalmente próximos,
> $$ds^2=c^2dt^2-d\vec x^{\,2}=c^2dt^2-dx^2-dy^2-dz^2.$$
> Definiendo la **cuadriposición diferencial** $dx^\mu=(c\,dt,\,dx,\,dy,\,dz)$ y la métrica $\eta_{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1)$, el intervalo se escribe como una **contracción de índices**:
> $$ds^2=\eta_{\mu\nu}\,dx^\mu dx^\nu.$$

> [!demostracion] El intervalo como contracción $\eta_{\mu\nu}dx^\mu dx^\nu$
> Desarrollamos la doble suma sobre $\mu,\nu=0,1,2,3$ usando que $\eta_{\mu\nu}$ es **diagonal**, de modo que solo sobreviven los términos con $\mu=\nu$.
>
> **Paso 1 — Reducir la doble suma a la diagonal.** Como $\eta_{\mu\nu}=0$ para $\mu\neq\nu$,
> $$\eta_{\mu\nu}\,dx^\mu dx^\nu=\sum_{\mu=0}^{3}\eta_{\mu\mu}\,(dx^\mu)^2=\eta_{00}(dx^0)^2+\eta_{11}(dx^1)^2+\eta_{22}(dx^2)^2+\eta_{33}(dx^3)^2.$$
>
> **Paso 2 — Sustituir las componentes de la métrica.** Con $\eta_{00}=+1$ y $\eta_{11}=\eta_{22}=\eta_{33}=-1$,
> $$\eta_{\mu\nu}\,dx^\mu dx^\nu=(dx^0)^2-(dx^1)^2-(dx^2)^2-(dx^3)^2.$$
>
> **Paso 3 — Identificar las componentes físicas.** Con $dx^0=c\,dt$ y $(dx^1,dx^2,dx^3)=(dx,dy,dz)$,
> $$\eta_{\mu\nu}\,dx^\mu dx^\nu=c^2dt^2-dx^2-dy^2-dz^2=c^2dt^2-d\vec x^{\,2}=ds^2.\qquad\blacksquare$$

El signo relativo entre el tiempo y el espacio clasifica los intervalos. Cada par de sucesos cae en una de tres categorías, y esa categoría **no depende del observador** porque $ds^2$ es invariante.

> [!proposicion] Clasificación de intervalos y cono de luz
> | Tipo | Signo | Significado físico |
> |:---|:---:|:---|
> | **Temporal** | $ds^2>0$ | predomina el tiempo; existe un marco donde ambos sucesos ocurren en el mismo lugar; **pueden** conectarse causalmente con $v<c$ |
> | **Espacial** | $ds^2<0$ | predomina el espacio; existe un marco donde son **simultáneos**; **no** hay conexión causal |
> | **Nulo (de luz)** | $ds^2=0$ | conectados por un rayo de luz; definen el **cono de luz** |
>
> El cono de luz, $ds^2=0$, separa el futuro y el pasado causales (interior temporal) de la región de "otro lugar" (exterior espacial).

![[cono_luz.svg|400]]
*El cono de luz: futuro, pasado y región espacial en el espaciotiempo de Minkowski. La superficie $ds^2=0$ delimita lo causalmente alcanzable; su forma es la huella de la métrica $\eta_{\mu\nu}$ con su signo relativo entre tiempo y espacio.*

---

## Índices arriba y abajo: subir y bajar con la métrica

> [!definicion] Componentes contravariantes y covariantes
> Un cuadrivector tiene dos juegos de componentes ligados por la métrica:
> - **Contravariantes** (índice arriba): $A^\mu=(A^0,\vec A)$ — se transforman como $dx^\mu$.
> - **Covariantes** (índice abajo): $A_\mu=\eta_{\mu\nu}A^\nu$ — se obtienen **bajando** el índice con $\eta_{\mu\nu}$.
>
> La operación inversa, **subir** el índice, usa la métrica inversa $\eta^{\mu\nu}$:
> $$A^\mu=\eta^{\mu\nu}A_\nu,\qquad\text{con}\qquad \eta^{\mu\lambda}\eta_{\lambda\nu}=\delta^\mu{}_\nu.$$

> [!lema] La inversa de la métrica es ella misma
> Para $\eta_{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1)$ se cumple $\eta^{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1)$, es decir, $\eta^{\mu\nu}$ tiene **las mismas componentes** que $\eta_{\mu\nu}$.
>
> **Paso 1 — Plantear la condición de inversa.** Debe valer $\eta^{\mu\lambda}\eta_{\lambda\nu}=\delta^\mu{}_\nu$. Como ambas son diagonales, la suma sobre $\lambda$ solo retiene $\lambda=\mu=\nu$:
> $$\eta^{\mu\lambda}\eta_{\lambda\nu}=\eta^{\mu\mu}\,\eta_{\mu\nu}\quad(\text{sin suma}).$$
>
> **Paso 2 — Imponer la delta.** Para $\mu=\nu$ se necesita $\eta^{\mu\mu}\eta_{\mu\mu}=1$. Como cada $\eta_{\mu\mu}=\pm1$ y $(\pm1)^2=1$, basta tomar $\eta^{\mu\mu}=\eta_{\mu\mu}$. Para $\mu\neq\nu$ ambos lados son $0$. Luego $\eta^{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1)$. $\blacksquare$

> [!demostracion] Bajar el índice cambia el signo a la parte espacial
> Queremos mostrar que si $A^\mu=(A^0,A^1,A^2,A^3)=(A^0,\vec A)$, entonces $A_\mu=(A^0,-\vec A)$.
>
> **Paso 1 — Componente temporal $A_0$.** Por definición $A_0=\eta_{0\nu}A^\nu$. Como $\eta_{0\nu}$ solo es no nula para $\nu=0$ (valor $+1$):
> $$A_0=\eta_{00}A^0=(+1)\,A^0=A^0.$$
>
> **Paso 2 — Componente espacial $A_i$** ($i=1,2,3$). Ahora $A_i=\eta_{i\nu}A^\nu$, y $\eta_{i\nu}$ solo es no nula para $\nu=i$ (valor $-1$):
> $$A_i=\eta_{ii}A^i=(-1)\,A^i=-A^i\quad(\text{sin suma sobre }i).$$
>
> **Paso 3 — Reunir.** Por tanto
> $$A_\mu=(A_0,A_1,A_2,A_3)=(A^0,-A^1,-A^2,-A^3)=(A^0,-\vec A).\qquad\blacksquare$$
>
> Subir de nuevo con $\eta^{\mu\nu}$ devuelve el signo: $\eta^{\mu\nu}A_\nu$ recupera $(A^0,+\vec A)=A^\mu$, como debe ser.

---

## Producto escalar invariante

> [!teorema] Producto escalar de Minkowski
> El producto escalar de dos cuadrivectores es el invariante
> $$A\cdot B=\eta_{\mu\nu}A^\mu B^\nu=A_\mu B^\mu=A^0B^0-\vec A\cdot\vec B.$$

> [!demostracion] Las tres formas coinciden y dan $A^0B^0-\vec A\cdot\vec B$
> **Paso 1 — Desarrollar $\eta_{\mu\nu}A^\mu B^\nu$.** Por ser $\eta$ diagonal, solo $\mu=\nu$:
> $$\eta_{\mu\nu}A^\mu B^\nu=\eta_{00}A^0B^0+\eta_{ii}A^iB^i=A^0B^0-\sum_{i=1}^3 A^iB^i=A^0B^0-\vec A\cdot\vec B.$$
>
> **Paso 2 — Verificar que $A_\mu B^\mu$ da lo mismo.** Usando el resultado anterior, $A_\mu=(A^0,-\vec A)$, así que
> $$A_\mu B^\mu=A_0B^0+A_iB^i=A^0B^0+(-A^i)B^i=A^0B^0-\vec A\cdot\vec B.$$
> Las dos contracciones coinciden: $\eta_{\mu\nu}A^\mu B^\nu=A_\mu B^\mu$, porque bajar el índice de $A$ no es más que aplicar $\eta$. $\blacksquare$

> [!demostracion] El producto escalar es invariante Lorentz
> Sea $A'^\mu=\Lambda^\mu{}_\alpha A^\alpha$ y $B'^\nu=\Lambda^\nu{}_\beta B^\beta$. Calculemos el producto en el marco primado.
>
> **Paso 1 — Escribir el producto transformado.**
> $$A'\cdot B'=\eta_{\mu\nu}A'^\mu B'^\nu=\eta_{\mu\nu}\,(\Lambda^\mu{}_\alpha A^\alpha)(\Lambda^\nu{}_\beta B^\beta)=\big(\eta_{\mu\nu}\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta\big)A^\alpha B^\beta.$$
>
> **Paso 2 — Usar la propiedad definitoria de Lorentz.** Una transformación de Lorentz preserva la métrica (se demuestra más abajo):
> $$\eta_{\mu\nu}\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta=\eta_{\alpha\beta}.$$
>
> **Paso 3 — Concluir.** Sustituyendo,
> $$A'\cdot B'=\eta_{\alpha\beta}A^\alpha B^\beta=A\cdot B.\qquad\blacksquare$$
>
> El producto escalar es el **mismo número** para todos los observadores inerciales. En particular, $A\cdot A=A_\mu A^\mu$ es la "longitud al cuadrado" invariante de un cuadrivector.

---

## Transformación de Lorentz

> [!definicion] Boost en $x$
> Un **boost** a lo largo de $x$ con velocidad $v$ entre dos marcos inerciales se escribe, con $\beta=v/c$ y $\gamma=1/\sqrt{1-\beta^2}$,
> $$ct'=\gamma(ct-\beta x),\qquad x'=\gamma(x-\beta ct),\qquad y'=y,\qquad z'=z.$$
> En forma matricial $x'^\mu=\Lambda^\mu{}_\nu x^\nu$, con
> $$\Lambda^\mu{}_\nu=\begin{pmatrix}\gamma & -\gamma\beta & 0 & 0\\[2pt] -\gamma\beta & \gamma & 0 & 0\\[2pt] 0 & 0 & 1 & 0\\[2pt] 0 & 0 & 0 & 1\end{pmatrix}.$$

> [!demostracion] El boost preserva el intervalo: $\eta_{\mu\nu}\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta=\eta_{\alpha\beta}$
> Verificamos la condición de Lorentz componente a componente. Como $\Lambda$ solo mezcla los índices $0,1$ (los $2,3$ son triviales), basta el bloque temporal-espacial.
>
> **Paso 1 — La contracción a comprobar.** Hay que mostrar $\eta_{\mu\nu}\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta=\eta_{\alpha\beta}$ para cada par $(\alpha,\beta)$. Como $\eta$ es diagonal,
> $$\eta_{\mu\nu}\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta=\eta_{00}\Lambda^0{}_\alpha\Lambda^0{}_\beta+\eta_{11}\Lambda^1{}_\alpha\Lambda^1{}_\beta=\Lambda^0{}_\alpha\Lambda^0{}_\beta-\Lambda^1{}_\alpha\Lambda^1{}_\beta,$$
> (los términos $\mu=2,3$ no aportan en el bloque relevante).
>
> **Paso 2 — Caso $(\alpha,\beta)=(0,0)$.** Con $\Lambda^0{}_0=\gamma$ y $\Lambda^1{}_0=-\gamma\beta$:
> $$\Lambda^0{}_0\Lambda^0{}_0-\Lambda^1{}_0\Lambda^1{}_0=\gamma^2-(-\gamma\beta)^2=\gamma^2(1-\beta^2)=\frac{1-\beta^2}{1-\beta^2}=1=\eta_{00}.\ \checkmark$$
>
> **Paso 3 — Caso $(\alpha,\beta)=(1,1)$.** Con $\Lambda^0{}_1=-\gamma\beta$ y $\Lambda^1{}_1=\gamma$:
> $$\Lambda^0{}_1\Lambda^0{}_1-\Lambda^1{}_1\Lambda^1{}_1=(-\gamma\beta)^2-\gamma^2=\gamma^2(\beta^2-1)=-\frac{1-\beta^2}{1-\beta^2}=-1=\eta_{11}.\ \checkmark$$
>
> **Paso 4 — Caso cruzado $(\alpha,\beta)=(0,1)$.**
> $$\Lambda^0{}_0\Lambda^0{}_1-\Lambda^1{}_0\Lambda^1{}_1=\gamma(-\gamma\beta)-(-\gamma\beta)\gamma=-\gamma^2\beta+\gamma^2\beta=0=\eta_{01}.\ \checkmark$$
>
> **Paso 5 — Concluir.** Por simetría $(1,0)$ da lo mismo que $(0,1)$, y los bloques $2,3$ son la identidad ($\eta_{22}=\eta_{33}=-1$ se preservan trivialmente). Por tanto
> $$\eta_{\mu\nu}\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta=\eta_{\alpha\beta}\quad\text{para todo }(\alpha,\beta).\qquad\blacksquare$$
>
> En consecuencia el intervalo $ds^2=\eta_{\mu\nu}dx^\mu dx^\nu$ y todo producto escalar son invariantes bajo el boost, como ya usamos arriba.

---

## Cuadrivectores físicos y el cuadrigradiente

> [!proposicion] El catálogo de cuadrivectores del electromagnetismo
> | Cuadrivector | Componentes $A^\mu=(A^0,\vec A)$ | Invariante |
> |:---|:---|:---|
> | Cuadriposición | $x^\mu=(ct,\vec x)$ | $x_\mu x^\mu=c^2t^2-\vec x^{\,2}$ |
> | Cuadrivelocidad | $u^\mu=\dfrac{dx^\mu}{d\tau}=\gamma(c,\vec v)$ | $u_\mu u^\mu=c^2$ |
> | Cuadrimomento | $p^\mu=mu^\mu=(E/c,\vec p)$ | $p_\mu p^\mu=m^2c^2$ |
> | Cuadricorriente | $J^\mu=(c\rho,\vec J)$ | — |
> | Cuadripotencial | $A^\mu=(V/c,\vec A)$ | — |
>
> El parámetro $\tau$ es el **tiempo propio**, $d\tau=dt/\gamma$, que es invariante por construcción ($c^2d\tau^2=ds^2$). Por eso $u^\mu=dx^\mu/d\tau$ es un cuadrivector: derivar un cuadrivector respecto a un escalar invariante da otro cuadrivector.

> [!definicion] Cuadrigradiente y d'Alembertiano
> El **cuadrigradiente** se define con **índice abajo**:
> $$\partial_\mu\equiv\frac{\partial}{\partial x^\mu}=\Big(\frac1c\frac{\partial}{\partial t},\,\nabla\Big),\qquad \partial^\mu=\eta^{\mu\nu}\partial_\nu=\Big(\frac1c\frac{\partial}{\partial t},\,-\nabla\Big).$$
> El operador escalar de ondas, el **d'Alembertiano**, es la contracción
> $$\Box\equiv\partial_\mu\partial^\mu=\frac{1}{c^2}\frac{\partial^2}{\partial t^2}-\nabla^2.$$

> [!demostracion] $\partial_\mu\partial^\mu=\frac1{c^2}\partial_t^2-\nabla^2$
> **Paso 1 — Contraer.** Con $\partial_\mu=(\tfrac1c\partial_t,\nabla)$ y $\partial^\mu=(\tfrac1c\partial_t,-\nabla)$,
> $$\partial_\mu\partial^\mu=\partial_0\partial^0+\partial_i\partial^i=\Big(\frac1c\partial_t\Big)\Big(\frac1c\partial_t\Big)+(\partial_i)(-\partial_i).$$
>
> **Paso 2 — Identificar términos.** El primer término es $\tfrac1{c^2}\partial_t^2$; el segundo, $-\partial_i\partial_i=-\nabla^2$:
> $$\partial_\mu\partial^\mu=\frac1{c^2}\frac{\partial^2}{\partial t^2}-\nabla^2=\Box.\qquad\blacksquare$$

> [!warning] Dos trampas de signo
> 1. **Signo de la métrica.** Usamos $\eta_{\mu\nu}=\mathrm{diag}(+,-,-,-)$ (Landau / partículas). El convenio opuesto $(-,+,+,+)$ (relatividad general à la MTW) invierte el signo de $ds^2$ y de todos los productos escalares. Antes de comparar fórmulas con otro libro, **fija el convenio**.
> 2. **El índice de $\partial_\mu$ va ABAJO.** Aunque se escriba $\partial/\partial x^\mu$ con $\mu$ "arriba" en el denominador, el operador es **covariante**: un índice en el denominador cuenta como índice abajo. Por eso $\partial_\mu=(\tfrac1c\partial_t,+\nabla)$ lleva $+\nabla$, y es $\partial^\mu$ el que lleva $-\nabla$.

---

## Conservación de la carga covariante

> [!teorema] $\partial_\mu J^\mu=0$ es la ecuación de continuidad
> La conservación local de la carga, $\partial_t\rho+\nabla\cdot\vec J=0$, es exactamente la anulación de la cuadridivergencia de la cuadricorriente.

> [!demostracion] $\partial_\mu J^\mu=\partial_t\rho+\nabla\cdot\vec J$
> **Paso 1 — Escribir la contracción.** Con $\partial_\mu=(\tfrac1c\partial_t,\nabla)$ y $J^\mu=(c\rho,\vec J)$,
> $$\partial_\mu J^\mu=\partial_0 J^0+\partial_i J^i=\Big(\frac1c\frac{\partial}{\partial t}\Big)(c\rho)+\nabla\cdot\vec J.$$
>
> **Paso 2 — Simplificar el término temporal.** El factor $c$ de $J^0=c\rho$ cancela el $1/c$ de $\partial_0$:
> $$\frac1c\frac{\partial}{\partial t}(c\rho)=\frac{\partial\rho}{\partial t}.$$
>
> **Paso 3 — Reunir.**
> $$\partial_\mu J^\mu=\frac{\partial\rho}{\partial t}+\nabla\cdot\vec J.$$
> Imponer $\partial_\mu J^\mu=0$ es, palabra por palabra, la ecuación de continuidad $\partial_t\rho+\nabla\cdot\vec J=0$. Como $\partial_\mu J^\mu$ es un **escalar** (contracción de índices), su anulación vale en todo marco: la carga se conserva para todo observador. $\blacksquare$

---

## Ejemplo

> [!ejemplo]
> Demuestra, a partir de la cuadrivelocidad $u^\mu=\gamma(c,\vec v)$, que el cuadrimomento $p^\mu=mu^\mu=(E/c,\vec p)$ satisface el invariante $p_\mu p^\mu=m^2c^2$, y deduce la relación energía-momento $E^2=(pc)^2+(mc^2)^2$.

> [!solucion]
> **Paso 1 — Invariante de la cuadrivelocidad.** Calculamos $u_\mu u^\mu$ con $u^\mu=\gamma(c,\vec v)$ y su versión covariante $u_\mu=\gamma(c,-\vec v)$. Contrayendo,
> $$u_\mu u^\mu=u^0u_0+u^iu_i=(\gamma c)(\gamma c)+(\gamma v^i)(-\gamma v^i)=\gamma^2 c^2-\gamma^2\vec v^{\,2}=\gamma^2(c^2-\vec v^{\,2}).$$
> Con $\gamma^2=1/(1-v^2/c^2)$,
> $$u_\mu u^\mu=\frac{c^2-v^2}{1-v^2/c^2}=\frac{c^2(1-v^2/c^2)}{1-v^2/c^2}=c^2.$$
>
> **Paso 2 — Invariante del cuadrimomento.** Como $p^\mu=mu^\mu$ con $m$ escalar invariante,
> $$p_\mu p^\mu=m^2\,u_\mu u^\mu=m^2c^2.$$
>
> **Paso 3 — Desarrollar el mismo invariante en componentes.** Con $p^\mu=(E/c,\vec p)$ y $p_\mu=(E/c,-\vec p)$,
> $$p_\mu p^\mu=p^0p_0+p^ip_i=\Big(\frac Ec\Big)^2-\vec p^{\,2}=\frac{E^2}{c^2}-p^2.$$
>
> **Paso 4 — Igualar las dos expresiones.** Por ser el mismo invariante,
> $$\frac{E^2}{c^2}-p^2=m^2c^2.$$
>
> **Paso 5 — Despejar.** Multiplicando por $c^2$,
> $$E^2=p^2c^2+m^2c^4=(pc)^2+(mc^2)^2.\qquad\blacksquare$$
>
> Para $\vec p=0$ se recupera $E=mc^2$; para $m=0$ (fotón), $E=pc$. El invariante $p_\mu p^\mu=m^2c^2$ encierra **toda** la cinemática relativista de la partícula.

---

## En qué consiste

La idea central es **renunciar a separar tiempo y espacio** y trabajar con un único objeto de cuatro componentes, el cuadrivector, gobernado por la métrica $\eta_{\mu\nu}=\mathrm{diag}(+,-,-,-)$. La métrica hace dos trabajos: define el **intervalo invariante** $ds^2=\eta_{\mu\nu}dx^\mu dx^\nu$ —lo que todos los observadores acuerdan— y permite **subir y bajar índices** ($A_\mu=\eta_{\mu\nu}A^\nu$), distinguiendo las componentes covariantes de las contravariantes por un signo en la parte espacial.

Toda la física se reescribe contrayendo índices. Un **producto escalar** $A_\mu B^\mu=A^0B^0-\vec A\cdot\vec B$ es automáticamente invariante Lorentz, porque las transformaciones $\Lambda^\mu{}_\nu$ están **definidas** por preservar la métrica, $\eta_{\mu\nu}\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta=\eta_{\alpha\beta}$. Así, escribir una ley con índices saturados garantiza que vale en todo marco inercial: ésa es la covariancia manifiesta.

El diccionario físico —cuadriposición, cuadrivelocidad, cuadrimomento, cuadricorriente, cuadripotencial— y el operador $\partial_\mu$ con su d'Alembertiano $\Box$ son las piezas con las que [[Tensor de Campo]] arma $F^{\mu\nu}$ y [[Maxwell Covariante]] colapsa las cuatro ecuaciones en dos. La conservación de la carga $\partial_\mu J^\mu=0$ es el primer ejemplo de una ley física entera escrita en una sola línea de índices.

---

## Resumen

> [!resumen]
> | Concepto | Expresión | Lectura |
> |:---|:---|:---|
> | Métrica | $\eta_{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1)$ | geometría del espaciotiempo |
> | Intervalo | $ds^2=\eta_{\mu\nu}dx^\mu dx^\nu=c^2dt^2-d\vec x^{\,2}$ | invariante Lorentz |
> | Bajar índice | $A_\mu=\eta_{\mu\nu}A^\nu=(A^0,-\vec A)$ | covariante desde contravariante |
> | Subir índice | $A^\mu=\eta^{\mu\nu}A_\nu$, $\ \eta^{\mu\lambda}\eta_{\lambda\nu}=\delta^\mu{}_\nu$ | $\eta^{\mu\nu}=\eta_{\mu\nu}$ |
> | Producto escalar | $A\cdot B=A_\mu B^\mu=A^0B^0-\vec A\cdot\vec B$ | invariante |
> | Boost en $x$ | $ct'=\gamma(ct-\beta x),\ x'=\gamma(x-\beta ct)$ | $\eta_{\mu\nu}\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta=\eta_{\alpha\beta}$ |
> | Cuadrivelocidad | $u^\mu=\gamma(c,\vec v)$ | $u_\mu u^\mu=c^2$ |
> | Cuadrimomento | $p^\mu=(E/c,\vec p)$ | $p_\mu p^\mu=m^2c^2\Rightarrow E^2=(pc)^2+(mc^2)^2$ |
> | Cuadricorriente | $J^\mu=(c\rho,\vec J)$ | $\partial_\mu J^\mu=0$ es continuidad |
> | Cuadripotencial | $A^\mu=(V/c,\vec A)$ | base de $F^{\mu\nu}$ |
> | Cuadrigradiente | $\partial_\mu=(\tfrac1c\partial_t,\nabla)$ | índice ABAJO |
> | d'Alembertiano | $\Box=\partial_\mu\partial^\mu=\tfrac1{c^2}\partial_t^2-\nabla^2$ | operador de ondas |

> [!corolario]
> Una ley física escrita como **igualdad de cuadrivectores** o como **escalar contraído** ($A_\mu B^\mu$, $\partial_\mu J^\mu$, $p_\mu p^\mu$) es **automáticamente invariante Lorentz**. Esto es el motor de todo el capítulo: en vez de transformar $\vec E$, $\vec B$, $\rho$ y $\vec J$ por separado, se agrupan en cuadrivectores y tensores cuyas ecuaciones todo observador ve idénticas. El siguiente paso es promover el cuadripotencial $A^\mu$ al **tensor de campo** $F^{\mu\nu}$ en [[Tensor de Campo]].

> [!referencia]
> Griffiths, *Introduction to Electrodynamics*, cap. 12 ("Electrodynamics and Relativity"). **Landau-Lifshitz, Vol. 2** (*Teoría Clásica de Campos*), caps. 1–3 (intervalo, cuadrivectores, cuadritensores). Jackson, cap. 11.
