---
title: Tensor de Campo
order: 2
tags:
  - electromagnetismo
  - teoria
  - covariante
draft: false
aliases:
  - Tensor de campo electromagnético
  - Tensor de Faraday
  - F^μν
---

# Tensor de Campo $F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu$

---

> [!definicion] Tensor de campo electromagnético
> Sea el cuadripotencial $A^\mu=(V/c,\;\vec A)$ y el operador derivada contravariante $\partial^\mu=\left(\dfrac1c\partial_t,\;-\nabla\right)$. El **tensor de campo** (o tensor de Faraday) es el tensor antisimétrico de rango $2$
> $$\boxed{\;F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu\;}$$
> Sus seis componentes independientes codifican simultáneamente al campo eléctrico $\vec E$ y al campo magnético $\vec B$. En él, $\vec E$ y $\vec B$ dejan de ser dos vectores tridimensionales independientes y pasan a ser **un único objeto geométrico** del espaciotiempo de Minkowski.

---

> [!info] Ubicación y dependencias
> - **Sección:** [[6 Formulacion Covariante/index | Formulación Covariante]].
> - **Notas hermanas:** [[Cuadrivectores]], [[Maxwell Covariante]], [[Tensor Energia-Momento]].
> - **Usa:** [[Potenciales y Gauge]] (de donde provienen $V$ y $\vec A$).
> - **Bibliografía:** Griffiths, *Introduction to Electrodynamics*, cap. 12; Landau & Lifshitz, *Teoría Clásica de Campos* (Vol. 2).
> - **Convenios:** métrica $\eta_{\mu\nu}=\mathrm{diag}(+,-,-,-)$, índices griegos $\mu,\nu,\dots\in\{0,1,2,3\}$, índices latinos $i,j,\dots\in\{1,2,3\}$, suma de Einstein sobre índices repetidos. Coordenadas $x^\mu=(ct,\;\vec r)$.

---

## Ejemplo

> [!ejemplo] Una carga en reposo, vista desde un tren en marcha
> Una carga puntual $q$ está **en reposo** en el marco $S$. Allí solo existe campo eléctrico, el de Coulomb:
> $$\vec E=\frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\hat r,\qquad \vec B=\vec 0 .$$
> El tensor de campo en $S$ tiene únicamente componentes $E$.
>
> Observamos la misma carga desde un marco $S'$ que se mueve con velocidad $-v\,\hat x$ respecto a $S$ (equivalentemente: la carga se mueve con $+v\,\hat x$ en $S'$). Como $F^{\mu\nu}$ es un tensor, basta aplicarle un boost. Usando las reglas de mezcla que se demuestran más abajo (con $B_y=B_z=0$ en $S$):
> $$E'_x=E_x,\qquad E'_y=\gamma E_y,\qquad E'_z=\gamma E_z,$$
> $$B'_x=0,\qquad B'_y=\gamma\frac{v}{c^2}E_z,\qquad B'_z=-\gamma\frac{v}{c^2}E_y .$$

> [!solucion] El campo magnético aparece de la nada
> En $S'$ la carga se mueve, y al boostear el campo puramente eléctrico **brota un campo magnético** $\vec B'$. Escribiéndolo de forma compacta, en $S'$
> $$\vec B'=-\frac{\vec v}{c^2}\times\vec E' ,$$
> es decir, el campo magnético de una carga en movimiento uniforme es exactamente el campo eléctrico transformado, girado por la velocidad. No hubo que resolver ninguna ecuación de Maxwell nueva: el magnetismo de una corriente es la **electrostática vista desde otro marco**.
>
> **Comprobación con un invariante.** En $S$ se cumple $\vec E\cdot\vec B=0$ (no hay $\vec B$). Más abajo demostramos que $\vec E\cdot\vec B$ es invariante Lorentz, así que en $S'$ también $\vec E'\cdot\vec B'=0$: en efecto, $\vec B'=-\tfrac{\vec v}{c^2}\times\vec E'$ es perpendicular a $\vec E'$. $\blacksquare$

---

## En qué consiste

### 1. Antisimetría y conteo de componentes

> [!proposicion] $F^{\mu\nu}$ es antisimétrico y tiene 6 componentes independientes
> $$F^{\mu\nu}=-F^{\nu\mu}.$$

> [!demostracion] Antisimetría
> **Paso 1 — Definición.** Por construcción,
> $$F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu .$$
>
> **Paso 2 — Intercambio de índices.** Permutamos $\mu\leftrightarrow\nu$ en la expresión anterior:
> $$F^{\nu\mu}=\partial^\nu A^\mu-\partial^\mu A^\nu .$$
>
> **Paso 3 — Comparación.** El segundo miembro es el opuesto del de $F^{\mu\nu}$:
> $$F^{\nu\mu}=-\bigl(\partial^\mu A^\nu-\partial^\nu A^\mu\bigr)=-F^{\mu\nu}.$$
>
> **Paso 4 — Conteo.** Un tensor antisimétrico de rango $2$ en $4$ dimensiones cumple $F^{\mu\mu}=-F^{\mu\mu}\Rightarrow F^{\mu\mu}=0$ (los $4$ elementos diagonales se anulan) y $F^{\mu\nu}=-F^{\nu\mu}$ (de los $16-4=12$ restantes, la mitad son independientes). Quedan
> $$\frac{4\cdot 4-4}{2}=6$$
> componentes independientes: exactamente las $3$ de $\vec E$ y las $3$ de $\vec B$. $\blacksquare$

### 2. $\vec E$ y $\vec B$ como componentes de $F^{\mu\nu}$

Esta es la deducción central. Necesitamos dos ingredientes. Primero, la **definición de los campos** a partir de los potenciales (ver [[Potenciales y Gauge]]):
$$\vec E=-\nabla V-\partial_t\vec A,\qquad \vec B=\nabla\times\vec A .$$
Segundo, las componentes **contravariantes** del cuadripotencial y del operador derivada:
$$A^\mu=(A^0,A^1,A^2,A^3)=\left(\tfrac{V}{c},\,A_x,\,A_y,\,A_z\right),$$
$$\partial^\mu=(\partial^0,\partial^1,\partial^2,\partial^3)=\left(\tfrac1c\partial_t,\,-\partial_x,\,-\partial_y,\,-\partial_z\right).$$
El signo $-$ de las componentes espaciales de $\partial^\mu$ proviene de subir el índice de $\partial_\mu=\partial/\partial x^\mu=(\tfrac1c\partial_t,\nabla)$ con la métrica: $\partial^\mu=\eta^{\mu\nu}\partial_\nu$, y $\eta^{ii}=-1$.

> [!demostracion] Las componentes temporales-espaciales dan $\vec E/c$
> **Paso 1 — Componente $F^{01}$.** Aplicamos la definición con $\mu=0$, $\nu=1$:
> $$F^{01}=\partial^0 A^1-\partial^1 A^0 .$$
>
> **Paso 2 — Sustituimos las componentes.** Con $\partial^0=\tfrac1c\partial_t$, $A^1=A_x$, $\partial^1=-\partial_x$, $A^0=V/c$:
> $$F^{01}=\frac1c\partial_t A_x-(-\partial_x)\frac{V}{c}=\frac1c\bigl(\partial_t A_x+\partial_x V\bigr).$$
>
> **Paso 3 — Reconocemos $E_x$.** De $\vec E=-\nabla V-\partial_t\vec A$, su componente $x$ es $E_x=-\partial_x V-\partial_t A_x$, luego $\partial_t A_x+\partial_x V=-E_x$. Por tanto
> $$F^{01}=\frac1c(-E_x)=-\frac{E_x}{c}.$$
>
> **Paso 4 — Las otras dos.** Análogamente, con $\nu=2,3$:
> $$F^{02}=\frac1c\partial_t A_y-(-\partial_y)\frac{V}{c}=\frac1c(\partial_t A_y+\partial_y V)=-\frac{E_y}{c},$$
> $$F^{03}=\frac1c\partial_t A_z-(-\partial_z)\frac{V}{c}=\frac1c(\partial_t A_z+\partial_z V)=-\frac{E_z}{c}.$$
> Así, la **primera fila** de $F^{\mu\nu}$ es $\left(0,\,-E_x/c,\,-E_y/c,\,-E_z/c\right)$, y por antisimetría la primera columna es su opuesta. $\blacksquare$

> [!demostracion] Las componentes espaciales-espaciales dan $\vec B$
> **Paso 1 — Componente $F^{12}$.** Con $\mu=1$, $\nu=2$:
> $$F^{12}=\partial^1 A^2-\partial^2 A^1=-\partial_x A_y-(-\partial_y A_x)=-\partial_x A_y+\partial_y A_x .$$
>
> **Paso 2 — Reconocemos el rotacional.** La componente $z$ de $\nabla\times\vec A$ es $(\nabla\times\vec A)_z=\partial_x A_y-\partial_y A_x=B_z$. Por tanto
> $$F^{12}=-\bigl(\partial_x A_y-\partial_y A_x\bigr)=-(\nabla\times\vec A)_z=-B_z .$$
>
> **Paso 3 — Componente $F^{13}$.** Con $\mu=1$, $\nu=3$:
> $$F^{13}=\partial^1 A^3-\partial^3 A^1=-\partial_x A_z+\partial_z A_x=-\bigl(\partial_x A_z-\partial_z A_x\bigr).$$
> Como $(\nabla\times\vec A)_y=\partial_z A_x-\partial_x A_z=B_y$, se tiene $\partial_x A_z-\partial_z A_x=-B_y$, luego
> $$F^{13}=-(-B_y)=+B_y .$$
>
> **Paso 4 — Componente $F^{23}$.** Con $\mu=2$, $\nu=3$:
> $$F^{23}=\partial^2 A^3-\partial^3 A^2=-\partial_y A_z+\partial_z A_y=-\bigl(\partial_y A_z-\partial_z A_y\bigr)=-(\nabla\times\vec A)_x=-B_x .$$
> Reuniendo: $F^{12}=-B_z$, $F^{23}=-B_x$, $F^{13}=+B_y$. $\blacksquare$

> [!teorema] Matriz del tensor de campo contravariante
> Juntando las seis componentes independientes y completando por antisimetría:
> $$F^{\mu\nu}=\begin{pmatrix}0 & -E_x/c & -E_y/c & -E_z/c\\[2pt] E_x/c & 0 & -B_z & B_y\\[2pt] E_y/c & B_z & 0 & -B_x\\[2pt] E_z/c & -B_y & B_x & 0\end{pmatrix}.$$
> La fila/columna $0$ aloja a $\vec E/c$; el bloque espacial $3\times3$ aloja a $\vec B$ en forma antisimétrica (la posición $ij$ guarda $-\epsilon_{ijk}B_k$).

> [!demostracion] Versión covariante $F_{\mu\nu}$ (bajando índices)
> **Paso 1 — Regla de bajada.** Bajamos los dos índices con la métrica:
> $$F_{\mu\nu}=\eta_{\mu\alpha}\eta_{\nu\beta}F^{\alpha\beta}.$$
>
> **Paso 2 — Componentes mixtas (un índice temporal, uno espacial), p. ej. $F_{01}$.** Aquí $\mu=0$ aporta $\eta_{00}=+1$ y $\nu=1$ aporta $\eta_{11}=-1$:
> $$F_{01}=\eta_{00}\,\eta_{11}\,F^{01}=(+1)(-1)\left(-\frac{E_x}{c}\right)=+\frac{E_x}{c}.$$
> Cada elemento con **exactamente un** índice espacial recoge un único factor $-1$, así que **las $\vec E$ cambian de signo**.
>
> **Paso 3 — Componentes espaciales (dos índices espaciales), p. ej. $F_{12}$.** Ahora $\eta_{11}=\eta_{22}=-1$:
> $$F_{12}=\eta_{11}\,\eta_{22}\,F^{12}=(-1)(-1)\,F^{12}=F^{12}=-B_z .$$
> Dos factores $-1$ se cancelan: **las $\vec B$ no cambian de signo**.
>
> **Paso 4 — Matriz resultante.**
> $$F_{\mu\nu}=\begin{pmatrix}0 & E_x/c & E_y/c & E_z/c\\[2pt] -E_x/c & 0 & -B_z & B_y\\[2pt] -E_y/c & B_z & 0 & -B_x\\[2pt] -E_z/c & -B_y & B_x & 0\end{pmatrix}.$$
> Es decir, $F_{\mu\nu}$ se obtiene de $F^{\mu\nu}$ por el cambio $\vec E\to-\vec E$, dejando $\vec B$ intacto. $\blacksquare$

### 3. El tensor dual $\tilde F^{\mu\nu}$

> [!definicion] Tensor dual de Faraday
> Con el símbolo de Levi-Civita totalmente antisimétrico $\epsilon^{\mu\nu\rho\sigma}$ (convenio $\epsilon^{0123}=+1$), el **dual** de $F$ es
> $$(\!*F)^{\mu\nu}=\tilde F^{\mu\nu}=\frac12\,\epsilon^{\mu\nu\rho\sigma}F_{\rho\sigma}.$$

> [!demostracion] El dual intercambia $\vec E/c\leftrightarrow\vec B$
> **Paso 1 — Una componente temporal, p. ej. $\tilde F^{01}$.** Solo contribuyen los términos con $\{\rho,\sigma\}=\{2,3\}$:
> $$\tilde F^{01}=\frac12\bigl(\epsilon^{0123}F_{23}+\epsilon^{0132}F_{32}\bigr)=\frac12\bigl((+1)F_{23}+(-1)F_{32}\bigr)=\frac12\bigl(F_{23}-F_{32}\bigr)=F_{23},$$
> donde usamos $\epsilon^{0132}=-1$ y $F_{32}=-F_{23}$. Como $F_{23}=-B_x$,
> $$\tilde F^{01}=-B_x .$$
>
> **Paso 2 — Una componente espacial, p. ej. $\tilde F^{12}$.** Contribuyen $\{\rho,\sigma\}=\{0,3\}$:
> $$\tilde F^{12}=\frac12\bigl(\epsilon^{1203}F_{03}+\epsilon^{1230}F_{30}\bigr)=\frac12\bigl((+1)F_{03}+(-1)F_{30}\bigr)=F_{03}.$$
> (Se usa $\epsilon^{1203}=+1$, pues $(1,2,0,3)$ es permutación par de $(0,1,2,3)$.) Con $F_{03}=E_z/c$,
> $$\tilde F^{12}=\frac{E_z}{c}.$$
>
> **Paso 3 — Patrón.** Comparando con $F^{\mu\nu}$, la operación dual realiza la sustitución
> $$\frac{\vec E}{c}\longrightarrow \vec B,\qquad \vec B\longrightarrow -\frac{\vec E}{c}.$$
> $\blacksquare$

> [!teorema] Matriz del tensor dual
> $$\tilde F^{\mu\nu}=\begin{pmatrix}0 & -B_x & -B_y & -B_z\\[2pt] B_x & 0 & E_z/c & -E_y/c\\[2pt] B_y & -E_z/c & 0 & E_x/c\\[2pt] B_z & E_y/c & -E_x/c & 0\end{pmatrix}.$$
> El dual es la herramienta que, junto con $F$, escribe **las cuatro ecuaciones de Maxwell** en forma covariante (ver [[Maxwell Covariante]]).

### 4. Transformación de Lorentz de los campos

> [!proposicion] Mezcla de $\vec E$ y $\vec B$ bajo un boost en $x$
> Para un boost de velocidad $v$ a lo largo de $\hat x$ (con $\beta=v/c$, $\gamma=1/\sqrt{1-\beta^2}$):
> $$E'_x=E_x,\qquad E'_y=\gamma\bigl(E_y-vB_z\bigr),\qquad E'_z=\gamma\bigl(E_z+vB_y\bigr),$$
> $$B'_x=B_x,\qquad B'_y=\gamma\Bigl(B_y+\tfrac{v}{c^2}E_z\Bigr),\qquad B'_z=\gamma\Bigl(B_z-\tfrac{v}{c^2}E_y\Bigr).$$

> [!demostracion] De la ley tensorial a las reglas de mezcla
> **Paso 1 — Ley de transformación.** Por ser $F^{\mu\nu}$ un tensor de rango $2$,
> $$F'^{\mu\nu}=\Lambda^\mu{}_\alpha\,\Lambda^\nu{}_\beta\,F^{\alpha\beta},$$
> con la matriz del boost en $x$
> $$\Lambda^\mu{}_\alpha=\begin{pmatrix}\gamma & -\gamma\beta & 0 & 0\\ -\gamma\beta & \gamma & 0 & 0\\ 0 & 0 & 1 & 0\\ 0 & 0 & 0 & 1\end{pmatrix}.$$
>
> **Paso 2 — $E'_x$ es invariante.** Calculamos $F'^{01}$. Como $\Lambda$ solo mezcla los índices $0$ y $1$, la suma se restringe a $\alpha,\beta\in\{0,1\}$:
> $$F'^{01}=\Lambda^0{}_\alpha\Lambda^1{}_\beta F^{\alpha\beta}=\Lambda^0{}_0\Lambda^1{}_1 F^{01}+\Lambda^0{}_1\Lambda^1{}_0 F^{10}+\Lambda^0{}_0\Lambda^1{}_0 F^{00}+\Lambda^0{}_1\Lambda^1{}_1 F^{11}.$$
> Los dos últimos términos se anulan porque $F^{00}=F^{11}=0$. Con $F^{10}=-F^{01}$:
> $$F'^{01}=\gamma\cdot\gamma\,F^{01}+(-\gamma\beta)(-\gamma\beta)(-F^{01})=\gamma^2 F^{01}\bigl(1-\beta^2\bigr)=\gamma^2 F^{01}\cdot\frac1{\gamma^2}=F^{01}.$$
> Como $F^{01}=-E_x/c$, esto dice $-E'_x/c=-E_x/c$, es decir $\boxed{E'_x=E_x}$.
>
> **Paso 3 — $E'_y$ mezcla con $B_z$.** Calculamos $F'^{02}$. El índice $2$ no se transforma ($\Lambda^2{}_\beta=\delta^2_\beta$), así que $\beta=2$ fijo; el índice $0$ recorre $\alpha\in\{0,1\}$:
> $$F'^{02}=\Lambda^0{}_\alpha\Lambda^2{}_2 F^{\alpha 2}=\Lambda^0{}_0 F^{02}+\Lambda^0{}_1 F^{12}=\gamma F^{02}-\gamma\beta\,F^{12}.$$
> Sustituyendo $F^{02}=-E_y/c$ y $F^{12}=-B_z$:
> $$-\frac{E'_y}{c}=\gamma\left(-\frac{E_y}{c}\right)-\gamma\beta(-B_z)=-\frac{\gamma}{c}\bigl(E_y-c\beta B_z\bigr)=-\frac{\gamma}{c}\bigl(E_y-vB_z\bigr).$$
> Multiplicando por $-c$: $\boxed{E'_y=\gamma(E_y-vB_z)}$.
>
> **Paso 4 — $B'_z$ mezcla con $E_y$.** Calculamos $F'^{12}$. De nuevo $\beta=2$ fijo y $\alpha\in\{0,1\}$:
> $$F'^{12}=\Lambda^1{}_\alpha\Lambda^2{}_2 F^{\alpha 2}=\Lambda^1{}_0 F^{02}+\Lambda^1{}_1 F^{12}=-\gamma\beta\,F^{02}+\gamma\,F^{12}.$$
> Con $F^{02}=-E_y/c$, $F^{12}=-B_z$:
> $$-B'_z=-\gamma\beta\left(-\frac{E_y}{c}\right)+\gamma(-B_z)=\gamma\frac{\beta}{c}E_y-\gamma B_z=-\gamma\Bigl(B_z-\frac{v}{c^2}E_y\Bigr),$$
> usando $\beta/c=v/c^2$. Luego $\boxed{B'_z=\gamma\bigl(B_z-\tfrac{v}{c^2}E_y\bigr)}$.
>
> **Paso 5 — Las restantes.** Repitiendo el procedimiento con $F'^{03}$ y $F'^{13}$ se obtienen, de forma idéntica salvo signos del bloque $\{1,3\}$,
> $$E'_z=\gamma(E_z+vB_y),\qquad B'_y=\gamma\Bigl(B_y+\frac{v}{c^2}E_z\Bigr).$$
> Y $B'_x=B_x$ se sigue de $F'^{23}=F^{23}$, pues el boost no toca los índices $2,3$. $\blacksquare$

> [!teoria] Lectura física de la mezcla
> Las componentes **paralelas** al boost no cambian ($E_\parallel,B_\parallel$); las **perpendiculares** se mezclan entre sí. Un campo puramente eléctrico en un marco adquiere componente magnética en otro, y viceversa. No tiene sentido absoluto preguntar "¿cuánto vale $\vec B$?": la respuesta depende del observador. Lo único absoluto es $F^{\mu\nu}$.

### 5. Invariantes de Lorentz

A partir de $F$ se construyen dos escalares que **todo observador inercial mide igual**.

> [!demostracion] $F_{\mu\nu}F^{\mu\nu}=2\bigl(B^2-E^2/c^2\bigr)$
> **Paso 1 — Carácter escalar.** El producto $F_{\mu\nu}F^{\mu\nu}$ tiene todos los índices contraídos, luego es un invariante Lorentz (un escalar).
>
> **Paso 2 — Desarrollo de la suma.** Por la antisimetría conviene separar el bloque temporal ($0i$) del espacial ($ij$):
> $$F_{\mu\nu}F^{\mu\nu}=\sum_{i}\bigl(F_{0i}F^{0i}+F_{i0}F^{i0}\bigr)+\sum_{i<j}\bigl(F_{ij}F^{ij}+F_{ji}F^{ji}\bigr).$$
> Como $F_{i0}F^{i0}=F_{0i}F^{0i}$ y $F_{ji}F^{ji}=F_{ij}F^{ij}$ (ambos factores cambian de signo), cada par duplica:
> $$F_{\mu\nu}F^{\mu\nu}=2\sum_i F_{0i}F^{0i}+2\sum_{i<j}F_{ij}F^{ij}.$$
>
> **Paso 3 — Términos eléctricos.** Para $i=1$: $F^{01}=-E_x/c$ y $F_{01}=+E_x/c$, luego $F_{01}F^{01}=-E_x^2/c^2$. Sumando las tres:
> $$2\sum_i F_{0i}F^{0i}=2\left(-\frac{E_x^2+E_y^2+E_z^2}{c^2}\right)=-\frac{2E^2}{c^2}.$$
>
> **Paso 4 — Términos magnéticos.** Para $(i,j)=(1,2)$: $F^{12}=-B_z$ y $F_{12}=-B_z$ (las $\vec B$ no cambian al bajar índices), luego $F_{12}F^{12}=B_z^2$. Sumando los tres pares $\{12\},\{13\},\{23\}$:
> $$2\sum_{i<j}F_{ij}F^{ij}=2\bigl(B_z^2+B_y^2+B_x^2\bigr)=2B^2.$$
>
> **Paso 5 — Resultado.**
> $$\boxed{\,F_{\mu\nu}F^{\mu\nu}=2\!\left(B^2-\frac{E^2}{c^2}\right)\,}$$
> es el mismo número en todo marco inercial. $\blacksquare$

> [!demostracion] $F_{\mu\nu}\tilde F^{\mu\nu}=-\dfrac{4}{c}\,\vec E\cdot\vec B$
> **Paso 1 — Carácter escalar.** De nuevo todos los índices están contraídos, así que es invariante.
>
> **Paso 2 — Uso del dual.** Recordando que $\tilde F^{\mu\nu}$ surge de $F^{\mu\nu}$ por $\vec E/c\to\vec B$, $\vec B\to-\vec E/c$, contraemos directamente con $F_{\mu\nu}$. El bloque temporal de $F_{\mu\nu}$ contiene $\pm E/c$ y el de $\tilde F^{\mu\nu}$ contiene $\mp B$; el bloque espacial de $F_{\mu\nu}$ contiene $\pm B$ y el de $\tilde F^{\mu\nu}$ contiene $\pm E/c$. Cada producto cruzado aporta un término $\propto E_iB_i/c$.
>
> **Paso 3 — Suma explícita (parte temporal).** Por ejemplo $i=1$: $F_{01}=E_x/c$, $\tilde F^{01}=-B_x$, y con el par $0i,i0$ duplicando,
> $$2\sum_i F_{0i}\tilde F^{0i}=2\left(\frac{E_x}{c}(-B_x)+\frac{E_y}{c}(-B_y)+\frac{E_z}{c}(-B_z)\right)=-\frac{2}{c}\,\vec E\cdot\vec B .$$
>
> **Paso 4 — Suma explícita (parte espacial).** Análogamente, el bloque $ij$ aporta otro $-\tfrac{2}{c}\vec E\cdot\vec B$ idéntico (la estructura $-B_z\cdot E_z/c+\dots$ reproduce el producto escalar). Sumando ambos bloques:
> $$\boxed{\,F_{\mu\nu}\tilde F^{\mu\nu}=-\frac{4}{c}\,\vec E\cdot\vec B\,}\ \propto\ \vec E\cdot\vec B .$$
> $\blacksquare$

> [!corolario] Consecuencias físicas de los invariantes
> Como $B^2-E^2/c^2$ y $\vec E\cdot\vec B$ son invariantes:
> - Si en un marco $\vec E\perp\vec B$ (es decir $\vec E\cdot\vec B=0$), **lo son en todos** los marcos.
> - Si en un marco $|E|=c|B|$ (es decir $B^2-E^2/c^2=0$), **lo es en todos**.
> - Una **onda electromagnética plana** en el vacío cumple $E=cB$ y $\vec E\perp\vec B$; por tanto **ambos invariantes se anulan en todo marco**: ningún observador puede "frenar" la onda hasta ver solo campo eléctrico o solo magnético. El carácter luminoso del campo es absoluto.

> [!warning] $\vec E$ y $\vec B$ no son objetos relativistas
> Por separado, $\vec E$ y $\vec B$ **no** son cuadrivectores ni tienen significado independiente del marco: lo que un observador llama "campo eléctrico" otro lo ve mezclado con magnético. Solo el conjunto $F^{\mu\nu}$ (y su dual) es un genuino objeto del espaciotiempo. En consecuencia, la distinción entre "fuerza eléctrica" y "fuerza magnética" **depende del observador**; la fuerza de Lorentz total $f^\mu=q\,F^{\mu}{}_{\nu}u^\nu$ sí es covariante.

![[boost_EB.svg|620]]
*Un boost en $\hat x$ convierte el campo puramente eléctrico de una carga en reposo (izquierda) en un par $\vec E',\vec B'$ acoplado en el marco donde la carga se mueve (derecha): el magnetismo es electricidad vista desde otro marco.*

---

## Resumen

> [!resumen] Tensor de campo electromagnético
> | Objeto \| Expresión |
> | :-- | :-- |
> | Definición \| $F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu$ |
> | Antisimetría \| $F^{\mu\nu}=-F^{\nu\mu}$ ⇒ $6$ componentes independientes |
> | Componentes \| $F^{0i}=-E_i/c$, \ \ $F^{ij}=-\epsilon_{ijk}B_k$ |
> | Covariante \| $F_{\mu\nu}$: las $\vec E$ cambian de signo, las $\vec B$ no |
> | Dual \| $\tilde F^{\mu\nu}=\tfrac12\epsilon^{\mu\nu\rho\sigma}F_{\rho\sigma}$ ($\vec E/c\to\vec B$, $\vec B\to-\vec E/c$) |
> | Boost en $x$ \| $E'_x=E_x$, \ $E'_y=\gamma(E_y-vB_z)$, \ $B'_z=\gamma(B_z-\tfrac{v}{c^2}E_y)$ |
> | Invariante 1 \| $F_{\mu\nu}F^{\mu\nu}=2(B^2-E^2/c^2)$ |
> | Invariante 2 \| $F_{\mu\nu}\tilde F^{\mu\nu}=-\tfrac{4}{c}\,\vec E\cdot\vec B$ |

> [!corolario] Idea para recordar
> $F^{\mu\nu}$ unifica $\vec E$ y $\vec B$ en un único tensor antisimétrico: sus seis casillas son los seis números $(\vec E,\vec B)$, sus dos invariantes $B^2-E^2/c^2$ y $\vec E\cdot\vec B$ son absolutos, y un boost simplemente reordena esas casillas. La electricidad y el magnetismo son **dos caras del mismo objeto geométrico** vistas desde marcos distintos.

> [!referencia] Para profundizar
> - **Griffiths**, *Introduction to Electrodynamics*, cap. 12 — construcción de $F^{\mu\nu}$ y transformación de campos.
> - **Landau & Lifshitz**, *Teoría Clásica de Campos* (Vol. 2), §23–25 — tensor de campo e invariantes.
> - Notas relacionadas: [[Cuadrivectores]], [[Potenciales y Gauge]], [[Maxwell Covariante]], [[Tensor Energia-Momento]].
