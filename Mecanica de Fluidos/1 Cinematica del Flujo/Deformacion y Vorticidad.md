---
title: Deformación y Vorticidad
order: 4
tags:
  - fluidos
  - teoria
  - cinematica
draft: false
aliases:
  - Deformación y vorticidad
  - Tensor de rapidez de deformación
  - Vorticidad
---

# Deformación y Vorticidad $e_{kk}=\nabla\cdot\vec v,\qquad \vec\omega=\nabla\times\vec v$

> [!definicion]
> El **tensor de rapidez de deformación** es la parte **simétrica** del gradiente de velocidad,
> $$e_{ij}=\tfrac12\!\left(\partial_i v_j+\partial_j v_i\right),$$
> y mide cómo un elemento fluido **se deforma** (se estira y se cizalla) por unidad de tiempo. Su traza es la **dilatación**
> $$e_{kk}=\partial_k v_k=\nabla\cdot\vec v,$$
> la tasa relativa de cambio de **volumen**. La **vorticidad** es el rotacional del campo de velocidades,
> $$\vec\omega=\nabla\times\vec v,\qquad \omega_i=\epsilon_{ijk}\,\partial_j v_k,$$
> y vale **el doble de la velocidad angular local** del elemento fluido: codifica su **rotación rígida**, la parte **antisimétrica** $\omega_{ij}$ del gradiente.

---

> [!info]
> Nota de la sección [[1 Cinematica del Flujo/index | Cinemática del Flujo]] (capítulo 1). Toma como punto de partida la descomposición $\partial_j v_i=e_{ij}+\omega_{ij}$ de la hermana [[Tensor Gradiente de Velocidad]] y desarrolla el **significado físico** de cada pieza; la siguiente, [[Teorema del Transporte de Reynolds]], usará la dilatación $\nabla\cdot\vec v$ para derivar la continuidad. Notación SI, convenio de suma de Einstein, $\delta_{ij}$, $\epsilon_{ijk}$. **Referencia.** Landau-Lifshitz, Vol. 6 (*Mecánica de Fluidos*), §1; Batchelor, *An Introduction to Fluid Dynamics*, cap. 2.

---

## Significado de las componentes

> [!teoria] Diagonales = estiramiento, fuera de la diagonal = cizalla
> Partimos de la velocidad **relativa** entre dos puntos materiales vecinos separados por $d\vec x$ (de [[Tensor Gradiente de Velocidad]]):
> $$dv_i=\partial_j v_i\,dx_j=\underbrace{e_{ij}\,dx_j}_{\text{deforma}}+\underbrace{\omega_{ij}\,dx_j}_{\text{rota}}.$$
> El tensor simétrico $e_{ij}$ es lo que **cambia la forma y el tamaño** del elemento. Sus componentes se leen así:
> - **Diagonales** $e_{11},e_{22},e_{33}$ (no se suma): tasa de **estiramiento** por unidad de longitud a lo largo de cada eje. Una $e_{ii}>0$ alarga el elemento en la dirección $i$; $e_{ii}<0$ lo acorta.
> - **Fuera de la diagonal** $e_{ij}$ con $i\neq j$: tasa de **cizalla**, es decir, la mitad de la rapidez con que **disminuye el ángulo recto** entre dos líneas materiales inicialmente alineadas con los ejes $i$ y $j$.

> [!proposicion] La componente diagonal $e_{11}$ es la elongación relativa en $x$
> Para un segmento material $\delta x$ alineado con el eje $x$, su tasa de estiramiento relativa es
> $$\frac{1}{\delta x}\,\frac{D(\delta x)}{Dt}=\partial_x v_x=e_{11}.$$

> [!demostracion]
> **Paso 1 — El segmento material.** Tomamos dos partículas fluidas sobre el eje $x$, en $x$ y en $x+\delta x$ (con $\delta x>0$ pequeño), a la misma $y,z$. Su separación es $\delta x = x_{(2)}-x_{(1)}$.
>
> **Paso 2 — Cómo cambia la separación.** Cada extremo se mueve con la velocidad local. Derivando **siguiendo el material** (derivada material $D/Dt$):
> $$\frac{D(\delta x)}{Dt}=\frac{D x_{(2)}}{Dt}-\frac{D x_{(1)}}{Dt}=v_x(x+\delta x,y,z,t)-v_x(x,y,z,t).$$
>
> **Paso 3 — Desarrollo de Taylor.** Como $\delta x$ es pequeño,
> $$v_x(x+\delta x)-v_x(x)=\frac{\partial v_x}{\partial x}\,\delta x+\mathcal O(\delta x^2).$$
> Luego
> $$\frac{D(\delta x)}{Dt}=\partial_x v_x\,\delta x+\mathcal O(\delta x^2).$$
>
> **Paso 4 — Tasa relativa.** Dividiendo entre $\delta x$ y tomando $\delta x\to 0$:
> $$\frac{1}{\delta x}\,\frac{D(\delta x)}{Dt}=\partial_x v_x=e_{11}.$$
> Por simetría del razonamiento, $e_{22}=\partial_y v_y$ y $e_{33}=\partial_z v_z$ son las elongaciones relativas en $y$ y $z$. $\blacksquare$

---

## Dilatación = divergencia

> [!teorema] La traza es la tasa relativa de cambio de volumen
> Para un elemento fluido de volumen $\delta V$,
> $$\frac{1}{\delta V}\,\frac{D(\delta V)}{Dt}=e_{kk}=\partial_k v_k=\nabla\cdot\vec v.$$

> [!demostracion]
> **Paso 1 — Un paralelepípedo material.** Tomamos un elemento fluido en forma de pequeño paralelepípedo de aristas $\delta x,\delta y,\delta z$ alineadas con los ejes, de volumen
> $$\delta V=\delta x\,\delta y\,\delta z.$$
> Cada arista es un segmento material, así que evoluciona según el Paso 4 de la proposición anterior.
>
> **Paso 2 — Cada arista se estira a su tasa.** Por el resultado recién probado,
> $$\frac{D(\delta x)}{Dt}=(\partial_x v_x)\,\delta x,\qquad
> \frac{D(\delta y)}{Dt}=(\partial_y v_y)\,\delta y,\qquad
> \frac{D(\delta z)}{Dt}=(\partial_z v_z)\,\delta z.$$
>
> **Paso 3 — Derivada del producto.** Como $\delta V=\delta x\,\delta y\,\delta z$, la regla del producto aplicada a la derivada material da
> $$\frac{D(\delta V)}{Dt}=\frac{D(\delta x)}{Dt}\,\delta y\,\delta z+\delta x\,\frac{D(\delta y)}{Dt}\,\delta z+\delta x\,\delta y\,\frac{D(\delta z)}{Dt}.$$
>
> **Paso 4 — Sustituir las tres tasas.**
> $$\frac{D(\delta V)}{Dt}=(\partial_x v_x)\,\delta x\,\delta y\,\delta z+(\partial_y v_y)\,\delta x\,\delta y\,\delta z+(\partial_z v_z)\,\delta x\,\delta y\,\delta z.$$
> Factorizando $\delta V=\delta x\,\delta y\,\delta z$:
> $$\frac{D(\delta V)}{Dt}=\big(\partial_x v_x+\partial_y v_y+\partial_z v_z\big)\,\delta V=(\partial_k v_k)\,\delta V.$$
>
> **Paso 5 — Tasa relativa.** Dividiendo entre $\delta V$:
> $$\frac{1}{\delta V}\,\frac{D(\delta V)}{Dt}=\partial_k v_k=e_{kk}=\nabla\cdot\vec v.$$
> La **dilatación** es, pues, la divergencia del campo de velocidades. $\blacksquare$

> [!corolario] Flujo incompresible $\Leftrightarrow$ divergencia nula
> Un flujo es **incompresible** cuando el volumen de todo elemento material se conserva, $\dfrac{D(\delta V)}{Dt}=0$ para todo elemento. Por el teorema, esto equivale a
> $$\boxed{\;\nabla\cdot\vec v=0\;}$$
> en todo el dominio. Es la forma cinemática de la condición de incompresibilidad: la traza del tensor de deformación se anula, es decir, $e_{ij}$ es **puramente desviadora** (sólo cizalla y estiramientos que se compensan, sin cambio de volumen).

---

## Vorticidad y rotación local

> [!teoria] La vorticidad es el doble de la velocidad angular local
> La parte **antisimétrica** del gradiente de velocidad,
> $$\omega_{ij}=\tfrac12\!\left(\partial_j v_i-\partial_i v_j\right),$$
> describe una **rotación rígida** del elemento fluido. Un tensor antisimétrico de $3\times3$ tiene sólo tres componentes independientes, que empaquetamos en un vector axial: la **vorticidad** $\vec\omega=\nabla\times\vec v$.

> [!proposicion] Relación $\omega_{ij}\leftrightarrow\vec\omega$
> $$\omega_{ij}=-\tfrac12\,\epsilon_{ijk}\,\omega_k,\qquad \omega_k=\epsilon_{kij}\,\partial_i v_j,\qquad \vec\omega=\nabla\times\vec v.$$

> [!demostracion]
> **Paso 1 — Vorticidad en índices.** Por definición del rotacional,
> $$\omega_k=(\nabla\times\vec v)_k=\epsilon_{kij}\,\partial_i v_j.$$
>
> **Paso 2 — Contraer con $\epsilon$.** Multiplicamos por $\epsilon_{klm}$ y usamos la identidad $\epsilon_{kij}\epsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}$:
> $$\epsilon_{klm}\,\omega_k=\epsilon_{klm}\epsilon_{kij}\,\partial_i v_j=(\delta_{li}\delta_{mj}-\delta_{lj}\delta_{mi})\,\partial_i v_j=\partial_l v_m-\partial_m v_l.$$
>
> **Paso 3 — Identificar la parte antisimétrica.** El lado derecho es $\partial_l v_m-\partial_m v_l=2\,\omega_{ml}=-2\,\omega_{lm}$. Por tanto
> $$\omega_{lm}=-\tfrac12\,\epsilon_{klm}\,\omega_k,$$
> que es la relación buscada (renombrando índices). La velocidad relativa por rotación es $dv_i^{\text{rot}}=\omega_{ij}\,dx_j=\tfrac12(\vec\omega\times d\vec x)_i$, es decir, una rotación rígida de **velocidad angular** $\vec\Omega_{\text{loc}}=\tfrac12\vec\omega$. Luego la vorticidad es **el doble** de la velocidad angular local. $\blacksquare$

> [!corolario] Flujo irrotacional
> Un flujo es **irrotacional** cuando $\vec\omega=\nabla\times\vec v=0$ en todo punto. Entonces $\omega_{ij}=0$: el elemento fluido se deforma pero **no gira**. En tal caso existe (localmente) un **potencial de velocidades** $\phi$ con $\vec v=\nabla\phi$, pues $\nabla\times\nabla\phi=0$ idénticamente.

---

## Circulación y teorema de Stokes

> [!teorema] La circulación es el flujo de vorticidad
> La **circulación** de $\vec v$ a lo largo de una curva cerrada $C$ que bordea una superficie $S$ es igual al flujo de la vorticidad a través de $S$:
> $$\Gamma=\oint_C\vec v\cdot d\vec l=\int_S(\nabla\times\vec v)\cdot d\vec A=\int_S\vec\omega\cdot d\vec A.$$

> [!demostracion]
> **Paso 1 — Definición.** La circulación es la integral de línea de la velocidad sobre la curva cerrada $C$, orientada,
> $$\Gamma=\oint_C\vec v\cdot d\vec l.$$
>
> **Paso 2 — Teorema de Stokes.** Para un campo suave $\vec v$ y una superficie $S$ con borde $\partial S=C$ (orientación según la regla de la mano derecha),
> $$\oint_C\vec v\cdot d\vec l=\int_S(\nabla\times\vec v)\cdot d\vec A.$$
> En índices, $\oint_C v_i\,dl_i=\int_S \epsilon_{ijk}\,\partial_j v_k\,dA_i$.
>
> **Paso 3 — Sustituir la vorticidad.** Como $\nabla\times\vec v=\vec\omega$,
> $$\Gamma=\int_S\vec\omega\cdot d\vec A.$$
> La circulación mide, pues, **cuánta vorticidad atraviesa** la superficie. En particular, en un flujo **irrotacional** ($\vec\omega=0$) la circulación es nula sobre toda curva que borde una región sin singularidades. $\blacksquare$

---

## Ejemplo

> [!ejemplo] Vórtice rígido vs. vórtice libre (potencial)
> Compara los dos flujos azimutales canónicos en coordenadas cilíndricas $(r,\theta,z)$. En ambos $\vec v=v_\theta(r)\,\hat\theta$, con líneas de corriente **circulares**, pero su vorticidad es **opuesta**.
> 1. **Vórtice rígido** (rota como un sólido): $\vec v=\Omega\,r\,\hat\theta$, con $\Omega$ constante.
> 2. **Vórtice libre / potencial**: $\vec v=\dfrac{K}{r}\,\hat\theta$, con $K$ constante.
>
> Calcula $\vec\omega=\nabla\times\vec v$ y la circulación de cada uno.

> [!solucion]
> **Paso 1 — Rotacional en cilíndricas.** Para $\vec v=v_\theta(r)\,\hat\theta$ (sin dependencia en $\theta,z$), la única componente del rotacional que sobrevive es la axial:
> $$\omega_z=(\nabla\times\vec v)_z=\frac{1}{r}\,\frac{\partial}{\partial r}\!\big(r\,v_\theta\big).$$
>
> **Paso 2 — Vórtice rígido.** Con $v_\theta=\Omega r$:
> $$\omega_z=\frac{1}{r}\,\frac{d}{dr}\!\big(r\cdot\Omega r\big)=\frac{1}{r}\,\frac{d}{dr}\!\big(\Omega r^2\big)=\frac{1}{r}\,(2\Omega r)=2\Omega.$$
> Luego $\boxed{\vec\omega=2\Omega\,\hat z}$ en **todo** el fluido: es **rotacional**, y la vorticidad ($2\Omega$) es justo el doble de la velocidad angular $\Omega$, como predice la teoría. El elemento fluido gira sobre sí mismo igual que cualquier punto de un disco rígido.
>
> **Paso 3 — Vórtice libre.** Con $v_\theta=K/r$:
> $$\omega_z=\frac{1}{r}\,\frac{d}{dr}\!\left(r\cdot\frac{K}{r}\right)=\frac{1}{r}\,\frac{d}{dr}\,(K)=0\qquad(r\neq 0).$$
> Luego $\boxed{\vec\omega=0}$ salvo en el origen: es **irrotacional** pese a que las líneas de corriente son círculos. Toda la vorticidad está concentrada en $r=0$ (una singularidad tipo delta de Dirac, $\vec\omega=\Gamma_0\,\delta^2(\vec r)\,\hat z$).
>
> **Paso 4 — Circulación.** Sobre un círculo de radio $r$ centrado en el eje, $d\vec l=r\,d\theta\,\hat\theta$:
> $$\Gamma=\oint_C\vec v\cdot d\vec l=\int_0^{2\pi} v_\theta\,r\,d\theta.$$
> - Vórtice rígido: $\Gamma=\int_0^{2\pi}(\Omega r)\,r\,d\theta=2\pi\Omega r^2=\int_S 2\Omega\,dA$ (crece con el área, coherente con $\vec\omega=2\Omega\hat z$ uniforme).
> - Vórtice libre: $\Gamma=\int_0^{2\pi}\dfrac{K}{r}\,r\,d\theta=2\pi K$, **constante** para todo $r>0$: toda la circulación proviene de la vorticidad encerrada en el origen. Por Stokes, $\Gamma=\int_S\vec\omega\cdot d\vec A=2\pi K$ aunque $\vec\omega=0$ en $S\setminus\{0\}$, porque la singularidad está dentro. $\blacksquare$

> [!warning] Líneas curvas $\neq$ vorticidad
> La vorticidad **no** es lo mismo que tener trayectorias curvas. El vórtice libre tiene líneas de corriente **circulares** y aun así es **irrotacional** ($\vec\omega=0$): un elemento fluido recorre un círculo pero **no gira sobre sí mismo** (una boya flotando mantiene su orientación). La vorticidad mide el giro **local** del elemento —cuánto rotan sus líneas materiales unas respecto de otras—, no la curvatura del **camino** que sigue su centro. Curvatura de la trayectoria y rotación local son cosas distintas.

---

## En qué consiste

> [!teoria] La descomposición, en una frase
> El gradiente de velocidad $\partial_j v_i$ —toda la información del movimiento relativo cerca de un punto— se parte en dos piezas con significado físico nítido: la **deformación** $e_{ij}$ (cambia forma y tamaño) y la **rotación** $\omega_{ij}$ (giro rígido, vorticidad). Dentro de la deformación, la **traza** $\nabla\cdot\vec v$ aísla el cambio de **volumen** (dilatación), y lo que queda es **cizalla** pura. La vorticidad $\vec\omega=\nabla\times\vec v$ aísla el **giro**. Tres números clave —divergencia (volumen), parte desviadora de $e_{ij}$ (forma) y vorticidad (rotación)— resumen cómo se mueve un elemento fluido.

![[deformacion_vorticidad.svg|640]]
*Las tres formas en que cambia un elemento fluido: dilatación (la traza $e_{kk}=\nabla\cdot\vec v$ cambia el volumen), cizalla (la componente $e_{xy}$ deforma el ángulo recto sin cambiar el área) y vorticidad ($\vec\omega=\nabla\times\vec v$, giro rígido del elemento). Las dos primeras son la parte simétrica $e_{ij}$; la tercera es la antisimétrica $\omega_{ij}$.*

---

## Resumen

> [!resumen]
> | Objeto | Definición (índices) | Significado físico |
> |:---|:---|:---|
> | Rapidez de deformación | $e_{ij}=\tfrac12(\partial_i v_j+\partial_j v_i)$ | parte simétrica del gradiente: deforma |
> | Estiramiento | $e_{ii}$ (sin suma) | elongación relativa en el eje $i$: $\tfrac{1}{\delta x_i}\tfrac{D(\delta x_i)}{Dt}$ |
> | Cizalla | $e_{ij}$, $i\neq j$ | tasa de cambio del ángulo entre líneas materiales |
> | Dilatación | $e_{kk}=\partial_k v_k=\nabla\cdot\vec v$ | tasa relativa de cambio de volumen $\tfrac{1}{\delta V}\tfrac{D(\delta V)}{Dt}$ |
> | Incompresible | $\nabla\cdot\vec v=0$ | el volumen de cada elemento se conserva |
> | Vorticidad | $\omega_i=\epsilon_{ijk}\partial_j v_k$, $\vec\omega=\nabla\times\vec v$ | doble de la velocidad angular local (giro) |
> | Irrotacional | $\vec\omega=0$ | no hay giro local; existe $\phi$ con $\vec v=\nabla\phi$ |
> | Circulación | $\Gamma=\oint_C\vec v\cdot d\vec l=\int_S\vec\omega\cdot d\vec A$ | flujo de vorticidad a través de $S$ (Stokes) |

> [!corolario] Lo esencial
> El gradiente de velocidad se descompone en deformación más rotación, $\partial_j v_i=e_{ij}+\omega_{ij}$. Su **traza** da la dilatación $\nabla\cdot\vec v$ (cambio de volumen; nula si el flujo es incompresible) y su **parte antisimétrica** da la vorticidad $\vec\omega=\nabla\times\vec v$ (doble de la velocidad angular local; nula si el flujo es irrotacional). La **circulación** es el flujo de vorticidad por Stokes. El contraste vórtice rígido (rotacional) vs. vórtice libre (irrotacional, con líneas circulares) muestra que la vorticidad mide el giro **local**, no la curvatura de la trayectoria.

> [!referencia]
> Landau-Lifshitz, Vol. 6 (*Mecánica de Fluidos*), §1 y §8 (vorticidad y circulación). Batchelor, *An Introduction to Fluid Dynamics*, cap. 2 (§2.3 deformación, §2.6 vorticidad). Continúa en [[Teorema del Transporte de Reynolds]]; base tomada de [[Tensor Gradiente de Velocidad]]; índice del capítulo en [[1 Cinematica del Flujo/index | Cinemática del Flujo]].
