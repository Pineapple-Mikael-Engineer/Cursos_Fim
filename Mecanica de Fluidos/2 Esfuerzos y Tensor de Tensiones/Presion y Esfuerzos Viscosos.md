---
title: Presión y Esfuerzos Viscosos
order: 2
tags:
  - fluidos
  - teoria
  - esfuerzos
draft: false
aliases:
  - Presión y esfuerzos viscosos
  - Desviador del esfuerzo
  - Presión mecánica
---

# Presión y Esfuerzos Viscosos $\sigma_{ij}=-p\,\delta_{ij}+\tau_{ij}$

> [!definicion]
> Todo tensor de esfuerzos simétrico $\sigma_{ij}$ de un fluido admite una separación **única** en dos piezas geométricamente independientes: una parte **isótropa**, proporcional al delta de Kronecker $\delta_{ij}$, que mide la **compresión media** en el punto, y un **desviador** de traza nula, que recoge todo el **corte**:
> $$\sigma_{ij}=-p\,\delta_{ij}+\tau_{ij},\qquad p=-\tfrac13\,\sigma_{kk},\qquad \tau_{kk}=0.$$
> La cantidad $p$ es la **presión mecánica** (un escalar, igual en toda dirección) y $\tau_{ij}$ es el **esfuerzo viscoso** o **desviador**, responsable de los cortantes. En un fluido **en reposo** $\tau_{ij}=0$ y solo sobrevive la presión: $\sigma_{ij}=-p\,\delta_{ij}$.

---

> [!info]
> Esta nota pertenece a la sección [[2 Esfuerzos y Tensor de Tensiones/index | Esfuerzos y Tensor de Tensiones]]. Sus hermanas son [[Tensor de Esfuerzos de Cauchy]] (de dónde sale $\sigma_{ij}$ y por qué es simétrico) y [[Fluido Newtoniano]] (la ley que liga $\tau_{ij}$ al movimiento). Aquí solo **separamos** el tensor; allí se le da contenido físico. **Referencia.** Landau-Lifshitz, Vol. 6, §15; Batchelor, *An Introduction to Fluid Dynamics*, §3.3.

---

## En qué consiste

> [!teoria] La idea: media + fluctuación
> Un tensor simétrico de $3\times3$ tiene seis componentes independientes. Conviene partirlo en dos objetos con significados físicos opuestos:
> - su **promedio direccional** (la traza), que actúa igual en toda dirección y representa el **empuje hidrostático**;
> - lo que sobra (el **desviador**), que tiene traza nula y representa el **cizallamiento**, las distorsiones de forma a volumen constante.
>
> La presión es la parte que un fluido en reposo sí soporta; el desviador es la parte que **solo aparece cuando el fluido se mueve y se deforma**. Por eso la separación no es un truco algebraico: distingue lo estático de lo dinámico, lo conservativo de lo disipativo.

> [!definicion] Parte isótropa y parte desviadora
> Para cualquier tensor de segundo orden simétrico $\sigma_{ij}$:
> $$\sigma_{ij}=\underbrace{\tfrac13\,\sigma_{kk}\,\delta_{ij}}_{\text{isótropo}}\;+\;\underbrace{\Big(\sigma_{ij}-\tfrac13\,\sigma_{kk}\,\delta_{ij}\Big)}_{\text{desviador, traza }0}.$$
> El primer sumando es proporcional a $\delta_{ij}$; el segundo tiene traza cero.

> [!demostracion] La descomposición existe, es única y el desviador tiene traza nula
> Trabajamos con convenio de suma de Einstein (índices repetidos se suman de $1$ a $3$).
>
> **Paso 1 — Construcción.** Sumamos y restamos $\tfrac13\sigma_{kk}\delta_{ij}$ al propio tensor, lo que es una identidad trivial:
> $$\sigma_{ij}=\tfrac13\,\sigma_{kk}\,\delta_{ij}+\Big(\sigma_{ij}-\tfrac13\,\sigma_{kk}\,\delta_{ij}\Big).$$
> Llamamos $S_{ij}=\tfrac13\sigma_{kk}\delta_{ij}$ (isótropo) y $D_{ij}=\sigma_{ij}-\tfrac13\sigma_{kk}\delta_{ij}$ (desviador).
>
> **Paso 2 — El desviador tiene traza nula.** Contraemos $D_{ij}$ haciendo $i=j$ y sumando. Usamos que la traza del delta de Kronecker es $\delta_{ii}=\delta_{11}+\delta_{22}+\delta_{33}=3$:
> $$D_{ii}=\sigma_{ii}-\tfrac13\,\sigma_{kk}\,\delta_{ii}=\sigma_{ii}-\tfrac13\,\sigma_{kk}\cdot 3=\sigma_{ii}-\sigma_{kk}=0,$$
> ya que $\sigma_{ii}$ y $\sigma_{kk}$ son el mismo escalar (el índice es mudo). Luego $D_{ii}=0$. $\;\checkmark$
>
> **Paso 3 — Toda la traza vive en la parte isótropa.** La traza de $S_{ij}$ es
> $$S_{ii}=\tfrac13\,\sigma_{kk}\,\delta_{ii}=\tfrac13\,\sigma_{kk}\cdot3=\sigma_{kk},$$
> de modo que $S_{ij}$ se lleva **toda** la traza de $\sigma_{ij}$ y $D_{ij}$ no aporta nada a ella.
>
> **Paso 4 — Unicidad.** Supongamos otra separación $\sigma_{ij}=\alpha\,\delta_{ij}+D'_{ij}$ con $D'_{kk}=0$. Tomando traza: $\sigma_{kk}=\alpha\,\delta_{kk}+D'_{kk}=3\alpha+0$, luego $\alpha=\tfrac13\sigma_{kk}$ queda fijado, y entonces $D'_{ij}=\sigma_{ij}-\tfrac13\sigma_{kk}\delta_{ij}=D_{ij}$. La descomposición es **única**. $\;\blacksquare$

> [!definicion] Presión mecánica y esfuerzo viscoso
> Definimos la **presión mecánica** como **menos** un tercio de la traza,
> $$\boxed{\,p=-\tfrac13\,\sigma_{kk}\,}$$
> El signo menos es físico: $\sigma_{ij}$ mide tracción (positiva hacia afuera), pero un fluido normalmente está **comprimido**, de modo que $\sigma_{kk}<0$ y así $p>0$. La presión es **compresión media**. El **esfuerzo viscoso** es el desviador con el signo de la presión absorbido:
> $$\tau_{ij}=\sigma_{ij}-\tfrac13\,\sigma_{kk}\,\delta_{ij}=\sigma_{ij}+p\,\delta_{ij}.$$
> Despejando $\sigma_{ij}$ se obtiene la fórmula central de la nota:
> $$\sigma_{ij}=-p\,\delta_{ij}+\tau_{ij},\qquad \tau_{kk}=0.$$

![[esfuerzo_descomposicion.svg|620]]
*El esfuerzo total $\sigma_{ij}$ se separa en una parte isótropa $-p\,\delta_{ij}$ (compresión igual en toda dirección, las flechas normales) más el desviador viscoso $\tau_{ij}$ de traza nula (puro cizallamiento, las flechas tangenciales). La presión hincha o comprime el elemento sin deformarlo; el desviador lo distorsiona a volumen constante.*

---

> [!proposicion] Fluido en reposo o ideal: solo presión, y es Pascal
> Si el fluido no se mueve (o es **ideal**, sin viscosidad), no hay deformación que genere fricción interna, así que el desviador se anula, $\tau_{ij}=0$, y el estado de tensión es **puramente isótropo**:
> $$\sigma_{ij}=-p\,\delta_{ij}.$$
> Entonces la tracción sobre **cualquier** plano de normal $\hat n$ es normal a él y de magnitud $p$, independiente de la orientación: es el **principio de Pascal**.

> [!demostracion] La tracción de un fluido en reposo es $-p\,\hat n$ en toda dirección
> Partimos de la relación de Cauchy $t_i=\sigma_{ij}\,n_j$ (ver [[Tensor de Esfuerzos de Cauchy]]) con $\sigma_{ij}=-p\,\delta_{ij}$.
>
> **Paso 1 — Sustituir el tensor isótropo.**
> $$t_i=\sigma_{ij}\,n_j=-p\,\delta_{ij}\,n_j.$$
>
> **Paso 2 — Acción del delta de Kronecker.** La contracción $\delta_{ij}n_j$ selecciona la componente $i$ del vector normal, $\delta_{ij}n_j=n_i$. Por tanto
> $$t_i=-p\,n_i\qquad\Longleftrightarrow\qquad \vec t=-p\,\hat n.$$
>
> **Paso 3 — Lectura física.** La tracción es **antiparalela** a $\hat n$ (hacia adentro: compresión) y su módulo es $|\vec t|=p\,|\hat n|=p$, el **mismo para toda orientación** del plano. No hay componente tangencial: $\vec t$ es siempre **normal**. $\;\blacksquare$
>
> Esto es la **definición operativa de fluido**: en reposo **no soporta esfuerzo cortante**; cualquier corte, por pequeño que sea, lo pone en movimiento. El cortante solo puede existir mientras el fluido se deforma, y vive enteramente en $\tau_{ij}$.

> [!warning] El convenio de signos y los dos significados de "presión"
> Dos finezas que conviene no confundir:
> - **Signo.** Con la convención $t_i=\sigma_{ij}n_j$ (tracción positiva hacia afuera), $p>0$ representa **compresión**; de ahí el $-p\,\delta_{ij}$. Si se invierte el convenio de la tracción, cambia el signo, pero la combinación $-p\,\delta_{ij}+\tau_{ij}$ se mantiene con $p$ siempre como presión positiva en compresión.
> - **Mecánica vs termodinámica.** La presión **mecánica** $p_\text{mec}=-\tfrac13\sigma_{kk}$ y la presión **termodinámica** $p$ (la del estado, de la ecuación de estado) **no son idénticas** en flujo compresible: difieren por la **viscosidad de volumen** $\zeta$,
> $$p_\text{mec}=p-\zeta\,\nabla\cdot\vec v.$$
> En flujo **incompresible** $\nabla\cdot\vec v=0$ y ambas **coinciden exactamente**; el detalle se desarrolla en [[Fluido Newtoniano]].

> [!corolario] Quién disipa energía
> La parte **isótropa** $-p\,\delta_{ij}$ no produce fricción interna en flujo incompresible: la presión hace trabajo reversible (comprime y descomprime). Es el **desviador** $\tau_{ij}$ quien genera los cortantes, la fricción viscosa y, por tanto, la **disipación** de energía mecánica en calor. Toda la irreversibilidad viscosa está en $\tau_{ij}$.

---

## Ejemplo

> [!ejemplo] Cortante simple y un fluido en reposo bajo gravedad
> **(a)** Un flujo de **cortante simple** (placa superior arrastrando el fluido) tiene un esfuerzo viscoso con una sola componente fuera de la diagonal, digamos $\tau_{xy}=\tau_{yx}=\tau\neq0$, y el resto nulo. El tensor total es, en la base $(\hat x,\hat y,\hat z)$,
> $$\sigma_{ij}=-p\,\delta_{ij}+\tau_{ij}=\begin{pmatrix}-p&\tau&0\\[2pt]\tau&-p&0\\[2pt]0&0&-p\end{pmatrix}.$$
> Comprueba la descomposición: $\sigma_{kk}=-3p$, luego $-\tfrac13\sigma_{kk}=p$ (la presión se recupera) y $\tau_{kk}=0$ (la diagonal de $\tau_{ij}$ es nula). $\checkmark$
>
> Calcula la **tracción sobre dos caras** con $t_i=\sigma_{ij}n_j$. Toma $\tau>0$. Para una **cara horizontal**, normal $\hat n=\hat y=(0,1,0)$:
> $$\vec t=\sigma_{ij}n_j=(\tau,\,-p,\,0)=\underbrace{-p\,\hat y}_{\text{normal}}+\underbrace{\tau\,\hat x}_{\text{cortante}}.$$
> Aparece una componente **tangencial** $\tau\,\hat x$: la cara siente cizalla. Para una cara **a $45^\circ$**, normal $\hat n=\tfrac1{\sqrt2}(1,1,0)$:
> $$\vec t=\sigma_{ij}n_j=\tfrac1{\sqrt2}\big(-p+\tau,\;\tau-p,\;0\big)=\tfrac{\tau-p}{\sqrt2}\,(1,1,0).$$
> Esta tracción es **paralela a $\hat n$** (proporcional a $(1,1,0)$): sobre los planos a $45^\circ$ el cortante simple se ve como tracción/compresión pura. En toda cara, **salvo en reposo**, el desviador inyecta una contribución que rompe la simetría de Pascal.
>
> **(b)** Un fluido **en reposo bajo gravedad** ($\vec g=-g\,\hat z$) tiene $\tau_{ij}=0$ y una presión hidrostática $p(z)=p_0+\rho g\,(z_0-z)$, de modo que
> $$\sigma_{ij}=-p(z)\,\delta_{ij}.$$
> La tracción sobre cualquier plano es $\vec t=-p(z)\,\hat n$: **siempre normal**, sin cortante, de magnitud creciente con la profundidad. Recuperamos exactamente el resultado de la demostración de Pascal.

---

## Resumen

> [!resumen]
> | Concepto | Expresión | Significado |
> |:---|:---|:---|
> | Descomposición | $\sigma_{ij}=-p\,\delta_{ij}+\tau_{ij}$ | isótropo + desviador, separación única |
> | Presión mecánica | $p=-\tfrac13\,\sigma_{kk}$ | compresión media; el $-$ hace $p>0$ en compresión |
> | Esfuerzo viscoso | $\tau_{ij}=\sigma_{ij}+p\,\delta_{ij}$, $\ \tau_{kk}=0$ | desviador de traza nula; todo el cortante |
> | Fluido en reposo / ideal | $\sigma_{ij}=-p\,\delta_{ij}\Rightarrow\vec t=-p\,\hat n$ | tracción normal e isótropa (Pascal) |
> | Mecánica vs termodinámica | $p_\text{mec}=p-\zeta\,\nabla\!\cdot\!\vec v$ | coinciden si $\nabla\!\cdot\!\vec v=0$ (incompresible) |

> [!corolario] Lo esencial
> Separar $\sigma_{ij}$ en presión y desviador es **separar lo estático de lo dinámico**: la presión $-p\,\delta_{ij}$ es lo único que sobrevive en reposo (Pascal, tracción normal), mientras que el desviador $\tau_{ij}$ es la **firma del movimiento**: nace de la deformación, produce los cortantes y concentra toda la **disipación viscosa**. Darle a $\tau_{ij}$ una forma explícita en función de la rapidez de deformación $e_{ij}$ es justamente el paso que define al [[Fluido Newtoniano]] y cierra las ecuaciones de Navier–Stokes.

> [!referencia]
> Landau-Lifshitz, Vol. 6 (*Mecánica de Fluidos*), §15 ("El tensor de tensiones"). Batchelor, *An Introduction to Fluid Dynamics*, §3.3. Véase también [[Tensor de Esfuerzos de Cauchy]] para el origen de $\sigma_{ij}$ y su simetría.
