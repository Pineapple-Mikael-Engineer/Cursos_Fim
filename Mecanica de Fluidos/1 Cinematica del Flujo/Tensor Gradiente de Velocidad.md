---
title: Tensor Gradiente de Velocidad
tags:
  - fluidos
  - teoria
  - cinematica
draft: false
aliases:
  - Tensor gradiente de velocidad
  - Descomposición del gradiente de velocidad
---

# Tensor Gradiente de Velocidad $\partial_j v_i=e_{ij}+\omega_{ij}$

> [!definicion] Tensor gradiente de velocidad
> Sea $\vec v(\vec x,t)$ el campo de velocidades de un fluido. El **tensor gradiente de velocidad** es el tensor de segundo orden cuyas componentes son las derivadas espaciales de la velocidad,
> $$L_{ij}\equiv\partial_j v_i=\frac{\partial v_i}{\partial x_j},$$
> y describe, a primer orden, cómo varía la velocidad entre dos puntos materiales vecinos. Se descompone de forma **única** en una parte simétrica y una antisimétrica,
> $$\boxed{\;\partial_j v_i=e_{ij}+\omega_{ij}\;}$$
> donde $e_{ij}=\tfrac12(\partial_i v_j+\partial_j v_i)$ es el **tensor rapidez de deformación** (simétrico) y $\omega_{ij}=\tfrac12(\partial_j v_i-\partial_i v_j)$ es el **tensor de rotación o giro** (antisimétrico).

> [!info] Ubicación y referencias
> Esta nota pertenece a la sección [[1 Cinematica del Flujo/index | Cinemática del Flujo]]. Sus notas hermanas son [[Deformacion y Vorticidad]] y [[Descripcion Euleriana y Lagrangiana]].
>
> Referencias principales: Landau & Lifshitz, *Mecánica de Fluidos* (Vol. 6) §1; Batchelor, *An Introduction to Fluid Dynamics*, cap. 2; Aris, *Vectors, Tensors and the Basic Equations of Fluid Mechanics*, cap. 4.

---

## Velocidad relativa entre puntos vecinos

> [!teoria] El gradiente como aproximación a primer orden
> Consideremos dos puntos materiales del fluido en el mismo instante $t$: uno en $\vec x$, con velocidad $v_i(\vec x)$, y otro infinitesimalmente próximo en $\vec x+d\vec x$, con velocidad $v_i(\vec x+d\vec x)$. La velocidad **relativa** entre ambos se obtiene del desarrollo de Taylor del campo.

> [!demostracion] La velocidad relativa es $dv_i=\partial_j v_i\,dx_j$
> **Paso 1 — Desarrollo de Taylor del campo.** Desarrollamos cada componente $v_i$ alrededor del punto $\vec x$ a primer orden en el desplazamiento $d\vec x$:
> $$v_i(\vec x+d\vec x)=v_i(\vec x)+\frac{\partial v_i}{\partial x_j}\,dx_j+\mathcal O(|d\vec x|^2).$$
> Aquí la suma sobre $j=1,2,3$ está implícita por el convenio de Einstein.
>
> **Paso 2 — Diferencia de velocidades.** Definimos la velocidad relativa $dv_i\equiv v_i(\vec x+d\vec x)-v_i(\vec x)$. Restando el término de orden cero (que es la **traslación** común a todo el entorno):
> $$dv_i=\frac{\partial v_i}{\partial x_j}\,dx_j+\mathcal O(|d\vec x|^2).$$
>
> **Paso 3 — Identificación del tensor.** A primer orden, la aplicación lineal que transforma el desplazamiento $dx_j$ en la velocidad relativa $dv_i$ es precisamente el tensor gradiente de velocidad:
> $$\boxed{\;dv_i=\partial_j v_i\,dx_j=L_{ij}\,dx_j\;},\qquad L_{ij}\equiv\frac{\partial v_i}{\partial x_j}.$$
> El objeto $L_{ij}$ es un tensor de segundo orden: lleva dos índices libres, $i$ (componente de la velocidad) y $j$ (dirección de derivación). $\blacksquare$

> [!warning] Convenio de índices
> Aquí fijamos $L_{ij}=\partial v_i/\partial x_j=\partial_j v_i$: el **primer** índice numera la componente de la velocidad y el **segundo** la dirección en que derivamos. Algunos autores (p. ej. en notación matricial $L=\nabla\vec v$ con otra convención) usan $L_{ij}=\partial_i v_j$, que es la **traspuesta** de la nuestra. La diferencia es crucial porque al separar la parte antisimétrica el **signo** de $\omega_{ij}$ cambia. Fija tu convenio y sé consistente en toda la nota.

---

## Descomposición única en simétrico + antisimétrico

> [!proposicion] Todo tensor de 2º orden se descompone de forma única
> Cualquier tensor $A_{ij}$ se escribe de manera **única** como suma de un tensor simétrico $S_{ij}=S_{ji}$ y uno antisimétrico $A'_{ij}=-A'_{ji}$.

> [!demostracion] Existencia y unicidad de la descomposición
> **Paso 1 — Existencia (truco de sumar y restar).** Sumamos y restamos la mitad del tensor traspuesto $A_{ji}$:
> $$A_{ij}=\underbrace{\tfrac12\!\left(A_{ij}+A_{ji}\right)}_{\displaystyle S_{ij}}+\underbrace{\tfrac12\!\left(A_{ij}-A_{ji}\right)}_{\displaystyle A'_{ij}}.$$
>
> **Paso 2 — Verificación de las simetrías.** Para la parte simétrica, intercambiamos $i\leftrightarrow j$:
> $$S_{ji}=\tfrac12(A_{ji}+A_{ij})=\tfrac12(A_{ij}+A_{ji})=S_{ij}\quad\checkmark$$
> Para la parte antisimétrica:
> $$A'_{ji}=\tfrac12(A_{ji}-A_{ij})=-\tfrac12(A_{ij}-A_{ji})=-A'_{ij}\quad\checkmark$$
>
> **Paso 3 — Unicidad.** Supongamos otra descomposición $A_{ij}=\tilde S_{ij}+\tilde A'_{ij}$ con $\tilde S$ simétrico y $\tilde A'$ antisimétrico. Tomando la traspuesta (intercambiando índices) y usando las simetrías:
> $$A_{ji}=\tilde S_{ji}+\tilde A'_{ji}=\tilde S_{ij}-\tilde A'_{ij}.$$
> Sumando y restando esta ecuación con $A_{ij}=\tilde S_{ij}+\tilde A'_{ij}$:
> $$A_{ij}+A_{ji}=2\tilde S_{ij}\;\Rightarrow\;\tilde S_{ij}=\tfrac12(A_{ij}+A_{ji})=S_{ij},$$
> $$A_{ij}-A_{ji}=2\tilde A'_{ij}\;\Rightarrow\;\tilde A'_{ij}=\tfrac12(A_{ij}-A_{ji})=A'_{ij}.$$
> Las dos partes quedan **completamente determinadas**: la descomposición es única. $\blacksquare$

> [!corolario] Descomposición del gradiente de velocidad
> Aplicando la proposición a $A_{ij}=\partial_j v_i$:
> $$\partial_j v_i=\underbrace{\tfrac12(\partial_j v_i+\partial_i v_j)}_{\displaystyle e_{ij}}+\underbrace{\tfrac12(\partial_j v_i-\partial_i v_j)}_{\displaystyle \omega_{ij}}=e_{ij}+\omega_{ij},$$
> con
> $$e_{ij}=\tfrac12(\partial_i v_j+\partial_j v_i)=e_{ji}\quad\text{(rapidez de deformación, simétrico)},$$
> $$\omega_{ij}=\tfrac12(\partial_j v_i-\partial_i v_j)=-\omega_{ji}\quad\text{(tensor de rotación, antisimétrico)}.$$
> El tensor simétrico $e_{ij}$ tiene $6$ componentes independientes; el antisimétrico $\omega_{ij}$ tiene solo $3$. En total $6+3=9$, las componentes del tensor completo. Ver [[Deformacion y Vorticidad]].

---

## El tensor antisimétrico y la vorticidad

> [!teorema] Equivalencia $\omega_{ij}\leftrightarrow$ vector axial vorticidad
> En tres dimensiones, el tensor antisimétrico de rotación se identifica con un **vector axial** $\vec\omega$, la **vorticidad**:
> $$\omega_{ij}=-\tfrac12\,\epsilon_{ijk}\,\omega_k,\qquad \vec\omega=\nabla\times\vec v\;\Longleftrightarrow\;\omega_k=\epsilon_{klm}\,\partial_l v_m.$$

> [!demostracion] De $\omega_{ij}$ a la vorticidad $\vec\omega$
> **Paso 1 — Tres componentes independientes.** Un tensor antisimétrico $\omega_{ij}=-\omega_{ji}$ tiene diagonal nula ($\omega_{11}=\omega_{22}=\omega_{33}=0$, pues $\omega_{ii}=-\omega_{ii}\Rightarrow\omega_{ii}=0$ sin sumar) y solo $3$ componentes distintas: $\omega_{12}$, $\omega_{23}$, $\omega_{31}$. Esto sugiere asociarle un vector de $3$ componentes.
>
> **Paso 2 — Propuesta de identificación.** Postulamos la relación lineal $\omega_{ij}=-\tfrac12\,\epsilon_{ijk}\,\omega_k$ y despejamos $\omega_k$ contrayendo con $\epsilon_{ijp}$:
> $$\epsilon_{ijp}\,\omega_{ij}=-\tfrac12\,\epsilon_{ijp}\,\epsilon_{ijk}\,\omega_k.$$
>
> **Paso 3 — Contracción de dos índices de $\epsilon$.** Usamos la identidad $\epsilon_{ijp}\,\epsilon_{ijk}=2\,\delta_{pk}$ (que se obtiene de $\epsilon_{ijk}\epsilon_{ilm}=\delta_{jl}\delta_{km}-\delta_{jm}\delta_{kl}$ contrayendo $j$ con $l$):
> $$\epsilon_{ijp}\,\omega_{ij}=-\tfrac12\,(2\,\delta_{pk})\,\omega_k=-\delta_{pk}\,\omega_k=-\omega_p.$$
> Por tanto $\omega_p=-\epsilon_{ijp}\,\omega_{ij}=\epsilon_{pij}\,\omega_{ij}$ (reordenando el Levi-Civita con una permutación cíclica).
>
> **Paso 4 — Sustituir la definición de $\omega_{ij}$.** Reemplazamos $\omega_{ij}=\tfrac12(\partial_j v_i-\partial_i v_j)$:
> $$\omega_p=\epsilon_{pij}\cdot\tfrac12(\partial_j v_i-\partial_i v_j)=\tfrac12\,\epsilon_{pij}\,\partial_j v_i-\tfrac12\,\epsilon_{pij}\,\partial_i v_j.$$
> En el segundo término renombramos los índices mudos $i\leftrightarrow j$: $\epsilon_{pij}\partial_i v_j=\epsilon_{pji}\partial_j v_i=-\epsilon_{pij}\partial_j v_i$. Así ambos términos se suman:
> $$\omega_p=\tfrac12\,\epsilon_{pij}\,\partial_j v_i+\tfrac12\,\epsilon_{pij}\,\partial_j v_i=\epsilon_{pij}\,\partial_j v_i.$$
>
> **Paso 5 — Reconocer el rotacional.** Reordenando $\epsilon_{pij}\partial_j v_i=\epsilon_{plm}\partial_l v_m$ (renombrando $j\to l$, $i\to m$ y usando $\epsilon_{pij}=\epsilon_{pji}\cdot(-1)$ con cuidado; aquí basta renombrar):
> $$\omega_p=\epsilon_{plm}\,\partial_l v_m=(\nabla\times\vec v)_p.$$
> Hemos demostrado que el vector axial asociado a $\omega_{ij}$ es exactamente la vorticidad $\vec\omega=\nabla\times\vec v$. $\blacksquare$

> [!demostracion] La parte antisimétrica es una rotación rígida
> **Paso 1 — Acción de $\omega_{ij}$ sobre el desplazamiento.** La contribución antisimétrica a la velocidad relativa es $dv_i^{(\text{rot})}=\omega_{ij}\,dx_j$. Sustituimos $\omega_{ij}=-\tfrac12\,\epsilon_{ijk}\,\omega_k$:
> $$dv_i^{(\text{rot})}=-\tfrac12\,\epsilon_{ijk}\,\omega_k\,dx_j.$$
>
> **Paso 2 — Reconocer un producto vectorial.** Recordamos que $(\vec a\times\vec b)_i=\epsilon_{ijk}a_j b_k$. Reordenamos el Levi-Civita: $-\epsilon_{ijk}\omega_k\,dx_j=\epsilon_{ikj}\,\omega_k\,dx_j=\epsilon_{ijk}\,\omega_j\,dx_k$ (renombrando $j\leftrightarrow k$ tras la permutación). Entonces:
> $$dv_i^{(\text{rot})}=\tfrac12\,\epsilon_{ijk}\,\omega_j\,dx_k=\tfrac12\,(\vec\omega\times d\vec x)_i.$$
>
> **Paso 3 — Interpretación.** Tenemos
> $$\boxed{\;dv_i^{(\text{rot})}=\omega_{ij}\,dx_j=\tfrac12\,(\vec\omega\times d\vec x)_i\;}$$
> Esto es exactamente la velocidad de una **rotación rígida** $\vec v_{\text{rot}}=\vec\Omega\times d\vec x$ con velocidad angular $\vec\Omega=\vec\omega/2$. Es decir, localmente el entorno del punto gira como un sólido rígido con velocidad angular igual a la **mitad de la vorticidad**. $\blacksquare$

---

## Interpretación física completa

> [!teoria] Descomposición del movimiento relativo
> Reuniendo los términos de orden cero (traslación), simétrico (deformación) y antisimétrico (rotación), el campo de velocidades cerca de un punto material se descompone en tres movimientos elementales:
> $$v_i(\vec x+d\vec x)=\underbrace{v_i(\vec x)}_{\text{traslación}}+\underbrace{e_{ij}\,dx_j}_{\text{deformación}}+\underbrace{\tfrac12(\vec\omega\times d\vec x)_i}_{\text{rotación rígida}}.$$
> Para la **velocidad relativa** (ya restada la traslación):
> $$dv_i=e_{ij}\,dx_j+\tfrac12\,(\vec\omega\times d\vec x)_i.$$
> Cada elemento de fluido **se deforma** (lo controla $e_{ij}$, simétrico, asociado a estiramiento y cizalle) y **rota rígidamente** (lo controla $\vec\omega/2$, la mitad de la vorticidad). La traslación es el término de orden cero, común a todo el entorno y ya sustraído. Ver [[Deformacion y Vorticidad]] para el detalle de $e_{ij}$.

---

## Ejemplo

> [!ejemplo] Flujo cortante simple (cizalle)
> Considera el flujo cortante simple $\vec v=(\dot\gamma\,y,\;0,\;0)$, donde $\dot\gamma>0$ es la **tasa de cizalle** constante. El fluido se mueve solo en $x$, con rapidez proporcional a la altura $y$. Calcula su tensor gradiente de velocidad y sepáralo en deformación y rotación.

> [!solucion] Cizalle = mitad deformación + mitad rotación
> **Paso 1 — Componentes de la velocidad.** Con $x_1=x$, $x_2=y$, $x_3=z$:
> $$v_1=\dot\gamma\,x_2,\qquad v_2=0,\qquad v_3=0.$$
>
> **Paso 2 — Tensor gradiente $\partial_j v_i$.** La única derivada no nula es $\partial_2 v_1=\partial v_1/\partial x_2=\dot\gamma$. En forma matricial (fila $i$, columna $j$):
> $$L_{ij}=\partial_j v_i=\begin{pmatrix}0 & \dot\gamma & 0\\[2pt] 0 & 0 & 0\\[2pt] 0 & 0 & 0\end{pmatrix}.$$
>
> **Paso 3 — Parte simétrica (rapidez de deformación).** $e_{ij}=\tfrac12(\partial_i v_j+\partial_j v_i)$. La única pareja no trivial es
> $$e_{12}=\tfrac12(\partial_1 v_2+\partial_2 v_1)=\tfrac12(0+\dot\gamma)=\tfrac{\dot\gamma}{2}=e_{21}.$$
> Por tanto
> $$e_{ij}=\begin{pmatrix}0 & \dot\gamma/2 & 0\\[2pt] \dot\gamma/2 & 0 & 0\\[2pt] 0 & 0 & 0\end{pmatrix}.$$
> Su traza es $e_{ii}=0$: el cizalle simple es **incompresible** (ver $\nabla\cdot\vec v=e_{ii}=0$).
>
> **Paso 4 — Parte antisimétrica (rotación).** $\omega_{ij}=\tfrac12(\partial_j v_i-\partial_i v_j)$:
> $$\omega_{12}=\tfrac12(\partial_2 v_1-\partial_1 v_2)=\tfrac12(\dot\gamma-0)=\tfrac{\dot\gamma}{2},\qquad \omega_{21}=-\tfrac{\dot\gamma}{2}.$$
> $$\omega_{ij}=\begin{pmatrix}0 & \dot\gamma/2 & 0\\[2pt] -\dot\gamma/2 & 0 & 0\\[2pt] 0 & 0 & 0\end{pmatrix}.$$
>
> **Paso 5 — Vorticidad asociada.** Usando $\omega_k=\epsilon_{klm}\partial_l v_m$, la única componente no nula es la $z$:
> $$\omega_3=\epsilon_{3lm}\partial_l v_m=\partial_1 v_2-\partial_2 v_1=0-\dot\gamma=-\dot\gamma.$$
> Es decir $\vec\omega=(0,0,-\dot\gamma)$, o bien $\omega_z=-\dot\gamma$. Comprobamos la relación $\omega_{12}=-\tfrac12\epsilon_{12k}\omega_k=-\tfrac12\epsilon_{123}\omega_3=-\tfrac12(1)(-\dot\gamma)=\tfrac{\dot\gamma}{2}\;\checkmark$.
>
> **Paso 6 — Conclusión.** El cizalle simple se reparte **exactamente por mitades**: el tensor original tenía la componente $L_{12}=\dot\gamma$, y al descomponer queda
> $$e_{12}=\frac{\dot\gamma}{2}\quad(\text{deformación}),\qquad \omega_z=-\dot\gamma\;\Rightarrow\;\frac{\omega_z}{2}=-\frac{\dot\gamma}{2}\quad(\text{rotación}).$$
> El flujo cortante simple es **mitad deformación pura, mitad rotación rígida**. $\blacksquare$

> [!warning] El cizalle no es deformación pura
> Aunque visualmente el cizalle simple parece solo "estirar diagonalmente" el fluido, lleva una **rotación escondida** ($\omega_z=-\dot\gamma\neq 0$). No confundas cizalle con deformación pura: solo la mitad de $\dot\gamma$ deforma; la otra mitad hace girar el elemento. Por eso un fluido cizallado tiene vorticidad no nula.

---

## En qué consiste

> [!teoria] Idea central
> El tensor gradiente de velocidad $L_{ij}=\partial_j v_i$ es el "ADN cinemático" del flujo en torno a un punto: contiene **toda** la información del movimiento relativo a primer orden. Su lectura física se obtiene partiéndolo en dos piezas con significado limpio:
> - **Parte simétrica $e_{ij}$** — cómo cambian distancias y ángulos: estiramientos (diagonal) y cizalles (fuera de la diagonal). Es la **deformación**.
> - **Parte antisimétrica $\omega_{ij}$** — equivalente al vector vorticidad $\vec\omega=\nabla\times\vec v$. Describe una **rotación rígida** local con velocidad angular $\vec\omega/2$, sin deformar.
>
> La descomposición es **única** y **covariante** (válida en cualquier base ortonormal), por eso separa de modo inequívoco "deformar" de "rotar". Esta separación es el cimiento para la ley constitutiva de los fluidos newtonianos, donde el esfuerzo viscoso depende solo de $e_{ij}$ (la rotación rígida no genera esfuerzo). Ver [[Descripcion Euleriana y Lagrangiana]] para el marco de campos y [[Deformacion y Vorticidad]] para la física de cada parte.

![[gradiente_velocidad.svg|620]]
*El gradiente de velocidad descompuesto en deformación pura ($e_{ij}$, izquierda: el círculo material se vuelve elipse) más rotación rígida ($\omega_{ij}$, derecha: el círculo gira sin deformarse). El flujo general es la superposición de ambos.*

---

## Resumen

> [!resumen] Tabla de objetos cinemáticos
>
> | Objeto | Definición indicial | Simetría | Componentes indep. | Significado físico |
> \|---\|---\|---\|---\|---\|
> | Gradiente de velocidad $L_{ij}$ | $\partial_j v_i$ | ninguna | $9$ | Movimiento relativo total a 1.er orden |
> | Rapidez de deformación $e_{ij}$ | $\tfrac12(\partial_i v_j+\partial_j v_i)$ | simétrico | $6$ | Estiramiento y cizalle (deformación) |
> | Tensor de giro $\omega_{ij}$ | $\tfrac12(\partial_j v_i-\partial_i v_j)$ | antisimétrico | $3$ | Rotación rígida local |
> | Vorticidad $\vec\omega$ | $\omega_k=\epsilon_{klm}\partial_l v_m=(\nabla\times\vec v)_k$ | vector axial | $3$ | Doble de la velocidad angular local |

> [!corolario] Resultados clave
> - **Velocidad relativa:** $dv_i=\partial_j v_i\,dx_j$ (Taylor a 1.er orden, restada la traslación).
> - **Descomposición única:** $\partial_j v_i=e_{ij}+\omega_{ij}$, simétrico $+$ antisimétrico.
> - **Relación giro–vorticidad:** $\omega_{ij}=-\tfrac12\,\epsilon_{ijk}\,\omega_k$ con $\vec\omega=\nabla\times\vec v$.
> - **Movimiento relativo:** $dv_i=e_{ij}\,dx_j+\tfrac12(\vec\omega\times d\vec x)_i=\text{deformación}+\text{rotación rígida }(\vec\omega/2)$.
> - **Cizalle simple:** mitad deformación ($e_{xy}=\dot\gamma/2$), mitad rotación ($\omega_z=-\dot\gamma$).

> [!referencia] Para profundizar
> - Landau & Lifshitz, *Mecánica de Fluidos* (Vol. 6), §1.
> - Batchelor, *An Introduction to Fluid Dynamics*, cap. 2 (§2.3, análisis del movimiento local).
> - Aris, *Vectors, Tensors and the Basic Equations of Fluid Mechanics*, cap. 4.
> - Notas hermanas: [[Deformacion y Vorticidad]], [[Descripcion Euleriana y Lagrangiana]]. Índice de la sección: [[1 Cinematica del Flujo/index | Cinemática del Flujo]].
