---
title: Identidades Vectoriales
tags:
  - electromagnetismo
  - teoria
  - calculo-vectorial
draft: false
aliases:
  - Identidades del cálculo vectorial
  - BAC-CAB
  - rot(grad)=0 y div(rot)=0
---

# Identidades Vectoriales $\nabla\times(\nabla\varphi)=0,\quad \nabla\cdot(\nabla\times\vec F)=0$

> [!definicion]
> Las **identidades vectoriales** son relaciones que se cumplen para *cualquier* campo (suficientemente diferenciable), con independencia de su forma concreta. Todas se demuestran de una sola manera: traducir el operador a **notación indicial** —$(\nabla\varphi)_i=\partial_i\varphi$, $\nabla\cdot\vec F=\partial_i F_i$, $(\nabla\times\vec F)_i=\epsilon_{ijk}\partial_j F_k$— y manipular los símbolos $\delta_{ij}$ y $\epsilon_{ijk}$ con la **identidad épsilon–delta**
> $$\boxed{\ \epsilon_{ijk}\,\epsilon_{ilm}=\delta_{jl}\,\delta_{km}-\delta_{jm}\,\delta_{kl}\ }$$
> y la **simetría de las derivadas parciales** $\partial_j\partial_k=\partial_k\partial_j$.

---

> [!info]
> **Ubicación.** Curso Electromagnetismo · sección [[1 Calculo Vectorial/index | Cálculo Vectorial]]. Hermanas: [[Campos y Operadores]] (define los operadores), [[Teoremas Integrales]] (Gauss y Stokes), [[Delta de Dirac y Singularidades]] (las identidades fallan en singularidades — ahí nace la delta).
> **Referencia.** Griffiths, *Introduction to Electrodynamics*, cap. 1 (§1.2.6 y portada interior). Las dos identidades nulas $\nabla\times(\nabla\varphi)=0$ y $\nabla\cdot(\nabla\times\vec F)=0$ son la **raíz de los potenciales** $\vec E=-\nabla V$ y $\vec B=\nabla\times\vec A$.

---

## Ejemplo

> [!ejemplo] Verificar $\nabla\cdot(\nabla\times\vec F)=0$ en un caso concreto
> Sea $\vec F=(\,y z^2,\ x^2 z,\ x y^2\,)$. Comprueba que el rotacional tiene divergencia nula.
>
> > [!solucion]
> > **Rotacional** $(\nabla\times\vec F)_i=\epsilon_{ijk}\partial_j F_k$:
> > $$\nabla\times\vec F=\big(\,\partial_y(xy^2)-\partial_z(x^2 z),\ \ \partial_z(yz^2)-\partial_x(xy^2),\ \ \partial_x(x^2 z)-\partial_y(yz^2)\,\big)$$
> > $$=\big(\,2xy-x^2,\ \ 2yz-y^2,\ \ 2xz-z^2\,\big).$$
> > **Divergencia** de ese vector:
> > $$\nabla\cdot(\nabla\times\vec F)=\partial_x(2xy-x^2)+\partial_y(2yz-y^2)+\partial_z(2xz-z^2)$$
> > $$=(2y-2x)+(2z-2y)+(2x-2z)=0.\qquad\checkmark$$
> > No es casualidad: la suma se cancela en pares porque cada término aparece con ambos signos. La identidad general (abajo) muestra que esto pasa **siempre**.

---

## En qué consiste

> [!teoria] La maquinaria: índices, $\delta_{ij}$ y $\epsilon_{ijk}$
> Trabajamos en coordenadas cartesianas con base ortonormal fija $\{\hat e_i\}$ y **convenio de suma de Einstein** (índice repetido $\Rightarrow$ suma de $1$ a $3$). Dos objetos lo hacen todo:
> - **Delta de Kronecker** $\delta_{ij}=\hat e_i\cdot\hat e_j$ ($1$ si $i=j$, $0$ si no). Actúa como "renombrador": $\delta_{ij}A_j=A_i$.
> - **Símbolo de Levi-Civita** $\epsilon_{ijk}$: totalmente antisimétrico, $\epsilon_{123}=+1$. Define el producto vectorial $(\vec A\times\vec B)_i=\epsilon_{ijk}A_j B_k$ y el rotacional $(\nabla\times\vec F)_i=\epsilon_{ijk}\partial_j F_k$.
>
> La pieza maestra es la **contracción de un índice** entre dos épsilon:
> $$\epsilon_{ijk}\,\epsilon_{ilm}=\delta_{jl}\,\delta_{km}-\delta_{jm}\,\delta_{kl}.$$
> (Contrayendo además $j=l$ se obtiene $\epsilon_{ijk}\epsilon_{ijm}=2\,\delta_{km}$, y $\epsilon_{ijk}\epsilon_{ijk}=6$.)

> [!proposicion] Identidad épsilon–delta (la herramienta)
> $$\epsilon_{ijk}\,\epsilon_{ilm}=\delta_{jl}\,\delta_{km}-\delta_{jm}\,\delta_{kl}.$$
>
> > [!demostracion]
> > **Paso 1 — Por qué un determinante.** El producto $\epsilon_{ijk}\epsilon_{ilm}$ es antisimétrico bajo $j\!\leftrightarrow\! k$ y bajo $l\!\leftrightarrow\! m$ (hereda la antisimetría de cada épsilon), y simétrico bajo el intercambio de pares $(jk)\!\leftrightarrow\!(lm)$. El único tensor con esa estructura, construido con deltas, es la combinación $\delta_{jl}\delta_{km}-\delta_{jm}\delta_{kl}$ (un determinante $2\times2$ de Kronecker).
> > **Paso 2 — Fijar la constante.** Basta evaluar un caso no nulo, digamos $j=l=1$, $k=m=2$:
> > $$\epsilon_{i12}\,\epsilon_{i12}=\epsilon_{312}\,\epsilon_{312}=(+1)(+1)=1,$$
> > mientras que el lado derecho da $\delta_{11}\delta_{22}-\delta_{12}\delta_{21}=1\cdot1-0\cdot0=1$. Coinciden, luego la constante es $1$. $\blacksquare$

> [!teorema] El rotacional de un gradiente es nulo
> Para todo campo escalar $\varphi$ de clase $C^2$:
> $$\nabla\times(\nabla\varphi)=\vec 0.$$
>
> > [!demostracion]
> > **Paso 1 — A índices.** La componente $i$-ésima es
> > $$\big[\nabla\times(\nabla\varphi)\big]_i=\epsilon_{ijk}\,\partial_j(\nabla\varphi)_k=\epsilon_{ijk}\,\partial_j\partial_k\varphi.$$
> > **Paso 2 — Simétrico × antisimétrico.** $\partial_j\partial_k\varphi$ es **simétrico** en $j,k$ (las parciales conmutan, $\varphi\in C^2$), mientras que $\epsilon_{ijk}$ es **antisimétrico** en $j,k$. La contracción completa de un tensor simétrico con uno antisimétrico es cero: intercambiando los nombres mudos $j\!\leftrightarrow\!k$,
> > $$\epsilon_{ijk}\partial_j\partial_k\varphi=\epsilon_{ikj}\partial_k\partial_j\varphi=-\,\epsilon_{ijk}\partial_j\partial_k\varphi\ \Rightarrow\ \epsilon_{ijk}\partial_j\partial_k\varphi=0.$$
> > Luego cada componente se anula. $\blacksquare$

> [!teorema] La divergencia de un rotacional es nula
> Para todo campo vectorial $\vec F$ de clase $C^2$:
> $$\nabla\cdot(\nabla\times\vec F)=0.$$
>
> > [!demostracion]
> > **Paso 1 — A índices.**
> > $$\nabla\cdot(\nabla\times\vec F)=\partial_i(\nabla\times\vec F)_i=\partial_i\big(\epsilon_{ijk}\partial_j F_k\big)=\epsilon_{ijk}\,\partial_i\partial_j F_k.$$
> > **Paso 2 — Mismo argumento.** $\partial_i\partial_j F_k$ es simétrico en $i,j$ y $\epsilon_{ijk}$ antisimétrico en $i,j$; su contracción se anula (renombrando $i\!\leftrightarrow\!j$ aparece el signo menos). Por tanto $\nabla\cdot(\nabla\times\vec F)=0$. $\blacksquare$

> [!teorema] Doble rotacional (BAC–CAB del nabla)
> $$\nabla\times(\nabla\times\vec F)=\nabla(\nabla\cdot\vec F)-\nabla^2\vec F.$$
>
> > [!demostracion]
> > **Paso 1 — A índices.** Usando el rotacional dos veces,
> > $$\big[\nabla\times(\nabla\times\vec F)\big]_i=\epsilon_{ijk}\,\partial_j(\nabla\times\vec F)_k=\epsilon_{ijk}\,\partial_j\big(\epsilon_{klm}\partial_l F_m\big)=\epsilon_{ijk}\,\epsilon_{klm}\,\partial_j\partial_l F_m.$$
> > **Paso 2 — Contraer los épsilon.** Reordena el primero a $\epsilon_{kij}$ (ciclar índices no cambia el signo: $\epsilon_{ijk}=\epsilon_{kij}$) para que el índice repetido $k$ quede al frente de ambos:
> > $$\epsilon_{ijk}\epsilon_{klm}=\epsilon_{kij}\epsilon_{klm}=\delta_{il}\,\delta_{jm}-\delta_{im}\,\delta_{jl}.$$
> > **Paso 3 — Sustituir y dejar que las deltas renombren.**
> > $$\big[\cdots\big]_i=\big(\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}\big)\partial_j\partial_l F_m=\partial_j\partial_i F_j-\partial_j\partial_j F_i.$$
> > **Paso 4 — Reconocer los operadores.** El primer término es $\partial_i(\partial_j F_j)=\partial_i(\nabla\cdot\vec F)=[\nabla(\nabla\cdot\vec F)]_i$; el segundo es $(\partial_j\partial_j)F_i=\nabla^2 F_i=[\nabla^2\vec F]_i$. Por tanto
> > $$\nabla\times(\nabla\times\vec F)=\nabla(\nabla\cdot\vec F)-\nabla^2\vec F.\qquad\blacksquare$$
>
> > [!warning]
> > El término $\nabla^2\vec F$ significa $(\nabla^2 F_i)\hat e_i$ **solo en coordenadas cartesianas**, donde los $\hat e_i$ son constantes. En cilíndricas/esféricas el laplaciano vectorial tiene términos extra; usa esta identidad —que es la definición de $\nabla^2\vec F$ en sistemas curvos— en su lugar. De aquí sale la **ecuación de ondas** del campo: al aplicar $\nabla\times$ a las leyes de Faraday y Ampère aparece $\nabla\times(\nabla\times\vec E)$, y con $\nabla\cdot\vec E=0$ en el vacío queda $-\nabla^2\vec E$.

> [!proposicion] Reglas del producto (todas por índices)
> Con $\varphi,\psi$ escalares y $\vec F,\vec G$ vectoriales:
>
> | Identidad | Esbozo indicial |
> |:---|:---|
> | $\nabla(\varphi\psi)=\varphi\,\nabla\psi+\psi\,\nabla\varphi$ | $\partial_i(\varphi\psi)=\varphi\,\partial_i\psi+\psi\,\partial_i\varphi$ (regla de Leibniz) |
> | $\nabla\cdot(\varphi\vec F)=\varphi\,(\nabla\cdot\vec F)+\vec F\cdot\nabla\varphi$ | $\partial_i(\varphi F_i)=\varphi\,\partial_i F_i+F_i\,\partial_i\varphi$ |
> | $\nabla\times(\varphi\vec F)=\varphi\,(\nabla\times\vec F)+(\nabla\varphi)\times\vec F$ | $\epsilon_{ijk}\partial_j(\varphi F_k)=\varphi\,\epsilon_{ijk}\partial_j F_k+\epsilon_{ijk}(\partial_j\varphi)F_k$ |
> | $\nabla\cdot(\vec F\times\vec G)=\vec G\cdot(\nabla\times\vec F)-\vec F\cdot(\nabla\times\vec G)$ | $\partial_i\,\epsilon_{ijk}F_j G_k=\epsilon_{ijk}(\partial_i F_j)G_k+\epsilon_{ijk}F_j(\partial_i G_k)$, y se reordenan los épsilon |
>
> > [!demostracion] La cuarta, en detalle
> > **Paso 1.** $\nabla\cdot(\vec F\times\vec G)=\partial_i\big(\epsilon_{ijk}F_j G_k\big)=\epsilon_{ijk}\big[(\partial_i F_j)G_k+F_j(\partial_i G_k)\big]$ por Leibniz.
> > **Paso 2.** En el primer término, $\epsilon_{ijk}(\partial_i F_j)G_k=G_k\,\epsilon_{kij}\partial_i F_j=\vec G\cdot(\nabla\times\vec F)$ (ciclé $\epsilon_{ijk}=\epsilon_{kij}$ y reconocí el rotacional con índices libres en $k$).
> > **Paso 3.** En el segundo, $\epsilon_{ijk}F_j(\partial_i G_k)=-F_j\,\epsilon_{jik}\partial_i G_k=-\vec F\cdot(\nabla\times\vec G)$ (una transposición $i\!\leftrightarrow\!j$ aporta el signo). Sumando: $\vec G\cdot(\nabla\times\vec F)-\vec F\cdot(\nabla\times\vec G)$. $\blacksquare$

---

## Resumen

> [!resumen] Tabla de identidades
>
> | Identidad | Nombre / uso en EM |
> |:---|:---|
> | $\nabla\times(\nabla\varphi)=\vec 0$ | campo conservativo $\Rightarrow$ existe potencial; $\nabla\times\vec E=0\Rightarrow\vec E=-\nabla V$ |
> | $\nabla\cdot(\nabla\times\vec F)=0$ | campo solenoidal; $\nabla\cdot\vec B=0\Rightarrow\vec B=\nabla\times\vec A$ |
> | $\nabla\times(\nabla\times\vec F)=\nabla(\nabla\cdot\vec F)-\nabla^2\vec F$ | doble rotacional; origen de la **ecuación de ondas** |
> | $\nabla\cdot(\varphi\vec F)=\varphi\,\nabla\cdot\vec F+\vec F\cdot\nabla\varphi$ | reglas de producto (Leibniz vectorial) |
> | $\nabla\cdot(\vec F\times\vec G)=\vec G\cdot(\nabla\times\vec F)-\vec F\cdot(\nabla\times\vec G)$ | base del **teorema de Poynting** |
> | $\epsilon_{ijk}\,\epsilon_{ilm}=\delta_{jl}\delta_{km}-\delta_{jm}\delta_{kl}$ | la herramienta que las demuestra todas |

> [!corolario] Por qué importan
> Las dos identidades nulas son las que **garantizan la existencia de los potenciales**: como $\nabla\cdot\vec B=0$ siempre, $\vec B$ es el rotacional de algún $\vec A$; como $\nabla\times\vec E=0$ en estática, $\vec E$ es el gradiente de algún $-V$. Toda la formulación con potenciales ([[Campos y Operadores]] → electrodinámica) descansa en ellas. Y BAC–CAB del nabla es el paso algebraico exacto que convierte las ecuaciones de Maxwell en la ecuación de ondas.

> [!referencia]
> Griffiths, *Introduction to Electrodynamics*, §1.2–§1.3 y tabla de identidades de portada. Para la identidad épsilon–delta y el cálculo indicial: Jackson, *Classical Electrodynamics*, apéndice; cualquier texto de cálculo tensorial cartesiano.
