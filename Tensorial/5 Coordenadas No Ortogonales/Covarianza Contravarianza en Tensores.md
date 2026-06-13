---
title: Covarianza y Contravarianza en Tensores
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-no-ortogonales
  - covarianza
draft: false
aliases:
  - componentes mixtas
  - tensor metrico es un tensor
  - covariance contravariance tensors
---

# Covarianza y Contravarianza en Tensores

> [!definicion]
> Igual que un vector tiene componentes contravariantes ($v^i$) o covariantes ($v_i$), un tensor admite una representación **puramente contravariante**, **puramente covariante** o **mixta**, del mismo objeto $\overleftrightarrow{T}$:
> $$\overleftrightarrow{T}=T^{ijk}\,\hat g_i\hat g_j\hat g_k=T_{ijk}\,\hat g^i\hat g^j\hat g^k=T^i{}_j{}^k\,\hat g_i\hat g^j\hat g_k.$$
> La **métrica** sube o baja **cada índice** por separado ($M^{ij}$ sube, $M_{ij}$ baja), y las matrices de transformación actúan **un factor por índice**: $t$ (contra) sobre cada superíndice, $g$ (co) sobre cada subíndice.

> [!info]
> Es el cap. 5.2.6 del libro (Rogan & Muñoz). Extiende a tensores la maquinaria de [[Metrica/Covarianza Contravarianza | covarianza/contravarianza]] de vectores. Usa el [[Metrica/Tensor Metrico | tensor métrico]] $M_{ij}$ para subir/bajar índices y las matrices $t^i{}_j,\ g^i{}_j$ de [[Transformaciones Contravariantes]] y [[Transformaciones Covariantes]]. Ver también el [[index | índice del capítulo 5]].
>
> **Notación.** Contravariante = superíndice, covariante = subíndice; la **posición horizontal** de los índices importa ($T^i{}_j{}^k\neq T^{ik}{}_j$). El tensor lleva $\overleftrightarrow{T}$; $M_{ij}=\hat g_i\cdot\hat g_j$ es la métrica covariante y $M^{ij}=\hat g^i\cdot\hat g^j$ la contravariante.

---

## Ejemplo

> [!ejemplo] Subir y bajar índices de un tensor $2\times2$
> Sea un tensor de rango 2 dado en forma **puramente covariante** $T_{ij}$ y una métrica concreta:
> $$[T_{ij}]=\begin{pmatrix}1 & 2\\ 0 & 3\end{pmatrix},\qquad
> [M_{ij}]=\begin{pmatrix}1 & \tfrac12\\[2pt] \tfrac12 & 1\end{pmatrix},\qquad
> [M^{ij}]=[M_{ij}]^{-1}=\frac{1}{3}\begin{pmatrix}4 & -2\\ -2 & 4\end{pmatrix}.$$
> (Se cumple $M^{ik}M_{kj}=\delta^i{}_j$, como debe ser la inversa.)
>
> **Bajar no aplica** (ya está covariante); **subimos el primer índice** con $M^{il}$ para obtener la forma mixta $T^i{}_j=M^{il}T_{lj}$, es decir el producto de matrices $[T^i{}_j]=[M^{ij}][T_{ij}]$:
> $$[T^i{}_j]=\frac{1}{3}\begin{pmatrix}4 & -2\\ -2 & 4\end{pmatrix}\begin{pmatrix}1 & 2\\ 0 & 3\end{pmatrix}
> =\frac{1}{3}\begin{pmatrix}4 & 2\\ -2 & 8\end{pmatrix}.$$
>
> **Subimos también el segundo índice** con $M^{jm}$ para la forma puramente contravariante $T^{ij}=M^{il}M^{jm}T_{lm}=[M][T][M]^{\mathsf T}$ (con $[M]=[M^{ij}]$ simétrica):
> $$[T^{ij}]=\frac{1}{9}\begin{pmatrix}4 & -2\\ -2 & 4\end{pmatrix}\begin{pmatrix}1 & 2\\ 0 & 3\end{pmatrix}\begin{pmatrix}4 & -2\\ -2 & 4\end{pmatrix}
> =\frac{1}{9}\begin{pmatrix}12 & 0\\ 8 & 28\end{pmatrix}.$$
> Las tres tablas $T_{ij}$, $T^i{}_j$, $T^{ij}$ describen **el mismo tensor** $\overleftrightarrow{T}$; cambian de valor porque cambia la base ($\hat g^i\hat g^j$ vs $\hat g_i\hat g_j$, etc.).

---

## En qué consiste

> [!teoria] Una representación, tres (o más) juegos de componentes
> Un vector se escribe $\vec v=v^i\hat g_i=v_i\hat g^i$. Un tensor de rango $\geq2$ es **más flexible**: además de la forma puramente contravariante o covariante, admite formas **mixtas**. Para rango 3:
> $$\overleftrightarrow{T}=T^{ijk}\,\hat g_i\hat g_j\hat g_k=T_{ijk}\,\hat g^i\hat g^j\hat g^k=T^i{}_j{}^k\,\hat g_i\hat g^j\hat g_k.$$
> Todas son representaciones equivalentes del **mismo** $\overleftrightarrow{T}$; cambian solo los valores numéricos de las componentes según qué base ($\hat g_i$ o $\hat g^i$) se use en cada ranura.

> [!proposicion] La métrica sube y baja cada índice por separado
> Como las componentes co/contravariantes de un vector se relacionan por la métrica ($v^i=M^{ij}v_j$, $v_i=M_{ij}v^j$), lo mismo vale **índice por índice** en un tensor. Para pasar de puramente covariante a puramente contravariante se aplica la métrica **una vez por cada índice**:
> $$T^{ijk}=M^{il}M^{jm}M^{kn}\,T_{lmn}.$$
> Para subir o bajar **un solo** índice se usa una sola métrica; p. ej. bajar el índice $i$ de $T^{imk}$ da la forma mixta
> $$T^i{}_j{}^k=M_{jm}\,T^{imk}.$$

> [!proposicion] Transformación tensorial: un factor por índice
> Bajo cambio de coordenadas, cada índice transforma como el vector del mismo tipo: con $t^i{}_j=\partial x'^i/\partial x^j$ (contra) sobre los superíndices y $g^j{}_i=\partial x^j/\partial x'^i$ (co) sobre los subíndices. Por ejemplo, para la forma mixta $T^j{}_{ik}$:
> $$T'^j{}_{ik}=g^l{}_i\,t^j{}_m\,g^n{}_k\,T^m{}_{ln}.$$
> Se usa $t$ para cada índice contravariante y $g$ para cada índice covariante: tantos factores como índices tenga el tensor.

> [!teorema] La métrica **es** un tensor
> Los elementos $M_{ij}=\hat g_i\cdot\hat g_j$, definidos como productos punto de la base, transforman como las componentes de un tensor de rango 2. Por tanto $\overleftrightarrow{M}=M_{ij}\,\hat g^i\hat g^j$ es un tensor genuino, no solo una tabla auxiliar.

> [!demostracion]
> **Paso 1 — Un invariante, dos sistemas.** El producto interno de $\vec A$ y $\vec B$ es un escalar (independiente del sistema). Escrito con componentes contravariantes y la métrica, debe coincidir en el sistema no primado y en el primado:
> $$\vec A\cdot\vec B=A^iB^jM_{ij}=A'^mB'^nM'_{mn}.$$
>
> **Paso 2 — Expresar lo primado en lo no primado.** Las componentes contravariantes transforman con $t$ (ver [[Transformaciones Contravariantes]]): $A'^m=t^m{}_iA^i$ y $B'^n=t^n{}_jB^j$. Sustituyendo en el lado derecho:
> $$A^iB^jM_{ij}=\bigl(t^m{}_iA^i\bigr)\bigl(t^n{}_jB^j\bigr)M'_{mn}=A^iB^j\,t^m{}_i\,t^n{}_j\,M'_{mn}.$$
>
> **Paso 3 — Igualar coeficientes.** Como la igualdad vale para **todo** $\vec A$ y $\vec B$, los coeficientes de $A^iB^j$ deben coincidir:
> $$M_{ij}=t^m{}_i\,t^n{}_j\,M'_{mn}.$$
>
> **Paso 4 — Lectura.** Esta es **exactamente** la ley de transformación de un tensor covariante de rango 2 (un factor $t$ contrayendo sobre el primer índice por cada índice de $M$). Invirtiendo, $M'_{ij}=g^m{}_i\,g^n{}_j\,M_{mn}$. Luego la métrica es, por definición, un tensor. $\blacksquare$

> [!corolario] La métrica mixta es la delta de Kronecker
> Subiendo un índice de $M_{ij}$ con la métrica contravariante se obtiene la forma **mixta** $M^i{}_j=M^{ik}M_{kj}$. Usando las ecuaciones de transformación (o directamente la base dual, $\hat g^i\cdot\hat g_j=\delta^i{}_j$) resulta
> $$M^i{}_j=\hat g^i\cdot\hat g_j=\delta^i{}_j.$$
> La métrica mixta **es** la delta de Kronecker: el tensor métrico es, en realidad, una **generalización** de $\delta^i{}_j$ a bases no ortonormales. En base ortonormal $M_{ij}=\delta_{ij}$ y las tres formas colapsan.

---

## Resumen

> [!resumen]
> | Concepto | Expresión |
> |---|---|
> | Tres representaciones | $\overleftrightarrow{T}=T^{ijk}\hat g_i\hat g_j\hat g_k=T_{ijk}\hat g^i\hat g^j\hat g^k=T^i{}_j{}^k\hat g_i\hat g^j\hat g_k$ |
> | Subir todos los índices | $T^{ijk}=M^{il}M^{jm}M^{kn}T_{lmn}$ |
> | Bajar un solo índice | $T^i{}_j{}^k=M_{jm}T^{imk}$ |
> | Transformación (mixta) | $T'^j{}_{ik}=g^l{}_i\,t^j{}_m\,g^n{}_k\,T^m{}_{ln}$ |
> | Métrica es tensor | $M_{ij}=t^m{}_i\,t^n{}_j\,M'_{mn}$ |
> | Métrica mixta | $M^i{}_j=\hat g^i\cdot\hat g_j=\delta^i{}_j$ |

> [!corolario]
> Un tensor es un solo objeto $\overleftrightarrow{T}$ con muchos juegos de componentes (puro contra, puro co, mixtos), enlazados subiendo/bajando cada índice con la [[Metrica/Tensor Metrico | métrica]]; bajo cambio de base cada índice transforma con su matriz ($t$ arriba, $g$ abajo). La propia métrica $M_{ij}$ es un tensor de rango 2, y su forma mixta $M^i{}_j=\delta^i{}_j$ exhibe que el tensor métrico generaliza la delta de Kronecker a coordenadas no ortogonales.

> [!referencia]
> - Caso vectorial (subir/bajar una sola componente): [[Metrica/Covarianza Contravarianza]].
> - La métrica y la base dual: [[Metrica/Tensor Metrico]].
> - Las matrices $t$ y $g$: [[Transformaciones Contravariantes]] · [[Transformaciones Covariantes]].
> - Derivadas parciales como objetos co/contravariantes: [[Derivadas Parciales Co y Contravariantes]].
