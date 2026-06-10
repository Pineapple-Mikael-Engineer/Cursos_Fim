---
title: Asociación de C y L
tags:
  - circuitos-electricos
  - teoria
  - transitorios
  - almacenamiento
draft: false
aliases:
  - asociación de C y L
  - asociación de condensadores e inductores
  - condensadores en serie y paralelo
  - inductores en serie y paralelo
  - association of capacitors and inductors
  - series and parallel C and L
---

# Asociación de $C$ y $L$ $\;$ (reglas duales a las de $R$)

> [!definicion]
> Los **condensadores** y los **inductores** se combinan en serie y en paralelo, pero con reglas
> **duales** a las de las resistencias. Para los **condensadores**:
> $$\text{serie:}\quad \frac{1}{C_{eq}}=\sum_k \frac{1}{C_k},\qquad\qquad
> \text{paralelo:}\quad C_{eq}=\sum_k C_k.$$
> Para los **inductores**:
> $$\text{serie:}\quad L_{eq}=\sum_k L_k,\qquad\qquad
> \text{paralelo:}\quad \frac{1}{L_{eq}}=\sum_k \frac{1}{L_k}.$$
> Regla mnemotécnica: los **condensadores** se combinan como las **conductancias** y los
> **inductores** como las **resistencias**.

> [!info]
> Parte de los [[Elementos de Almacenamiento/index| elementos de almacenamiento]] del
> [[3 Almacenamiento y Transitorios/index| capítulo 3]]. Las reglas se deducen de las leyes
> $v$-$i$ del [[Capacitor]] y del [[Inductor]], y son la imagen **dual** de
> [[Resistencias en Serie y Paralelo]]. Fraile Mora, cap. 1, §1.5.

---

## Ejemplo

> [!ejemplo]
> **Las cuatro reglas con números.**
>
> Asociar dos condensadores $C_1=6\ \mu\text{F}$, $C_2=3\ \mu\text{F}$ y dos inductores
> $L_1=2\ \text{mH}$, $L_2=6\ \text{mH}$, en serie y en paralelo.
>
> ![[asociacion_CL.svg|620]]
>
> *Reglas de asociación de condensadores e inductores. Nótese la dualidad con las resistencias.*
>
> **Paso 1 — Condensadores en serie.** Se suman los inversos:
> $$\frac{1}{C_{eq}}=\frac{1}{6}+\frac{1}{3}=\frac{1}{6}+\frac{2}{6}=\frac{3}{6}=\frac{1}{2}
> \;\Rightarrow\; C_{eq}=2\ \mu\text{F}.$$
> El resultado ($2\ \mu\text{F}$) es **menor** que el más pequeño de los dos.
>
> **Paso 2 — Condensadores en paralelo.** Se suman directamente:
> $$C_{eq}=6+3=9\ \mu\text{F}.$$
>
> **Paso 3 — Inductores en serie.** Se suman directamente (como resistencias):
> $$L_{eq}=2+6=8\ \text{mH}.$$
>
> **Paso 4 — Inductores en paralelo.** Se suman los inversos:
> $$\frac{1}{L_{eq}}=\frac{1}{2}+\frac{1}{6}=\frac{3}{6}+\frac{1}{6}=\frac{4}{6}=\frac{2}{3}
> \;\Rightarrow\; L_{eq}=\frac{3}{2}=1{,}5\ \text{mH}.$$
>
> > [!solucion]
> > | Asociación | Condensadores | Inductores |
> > |:---|:---:|:---:|
> > | **Serie** | $C_{eq}=2\ \mu\text{F}$ | $L_{eq}=8\ \text{mH}$ |
> > | **Paralelo** | $C_{eq}=9\ \mu\text{F}$ | $L_{eq}=1{,}5\ \text{mH}$ |
> >
> > En serie, los condensadores **bajan** su capacidad y los inductores la suben; en paralelo, al
> > revés. Es exactamente lo contrario a lo que hacen las resistencias.

---

## En qué consiste

> [!teoria] Deducción de las reglas de los condensadores
> El argumento se apoya en **qué magnitud comparten** los elementos según cómo estén conectados.
>
> **Condensadores en serie.** Al estar en serie circula la misma corriente por todos, así que en un
> mismo intervalo acumulan la **misma carga** $q$. La tensión total es la suma de las tensiones, y
> cada una vale $v_k=q/C_k$:
> $$v=\sum_k v_k=\sum_k \frac{q}{C_k}=q\sum_k \frac{1}{C_k}.$$
> Como para el equivalente $v=q/C_{eq}$, igualando se obtiene
> $$\frac{1}{C_{eq}}=\sum_k \frac{1}{C_k}.$$
>
> **Condensadores en paralelo.** Todos quedan sometidos a la **misma tensión** $v$, y cada uno
> almacena $q_k=C_k v$. La carga total es la suma:
> $$q=\sum_k q_k=v\sum_k C_k \;\Rightarrow\; C_{eq}=\sum_k C_k.$$

> [!teoria] Los inductores, por dualidad
> El [[Inductor]] es el **dual** del [[Capacitor]] bajo el intercambio $v\leftrightarrow i$,
> $C\leftrightarrow L$. Por tanto las reglas se obtienen "girando" las anteriores:
> - En **serie** los inductores comparten la misma corriente $i$; la tensión total
>   $v=\sum L_k\,di/dt$ da $L_{eq}=\sum_k L_k$ (**suma directa**).
> - En **paralelo** comparten la misma tensión; el resultado es la **suma de inversos**
>   $\dfrac{1}{L_{eq}}=\sum_k \dfrac{1}{L_k}$.

> [!teoria] ¿Por qué es "al revés" que las resistencias?
> En una resistencia, la magnitud que se suma al poner elementos en **serie** es la propia $R$ (las
> caídas de tensión $iR$ se suman). En un condensador en serie lo que se suma no es $C$ sino su
> inverso $1/C$, porque lo que crece es la **tensión por unidad de carga**. Dicho de otro modo: la
> capacidad mide cuánta carga cabe por voltio (es como una **conductancia**), y las conductancias se
> suman en **paralelo**, no en serie. De ahí que las reglas de $C$ aparezcan intercambiadas respecto
> a las de $R$, y las de $L$ —que sí se suman en serie— coincidan con las de $R$.

> [!proposicion] Caso de dos elementos (producto sobre suma)
> Para **dos** condensadores en serie y **dos** inductores en paralelo, la suma de inversos se reduce
> a la cómoda forma producto-sobre-suma:
> $$C_{eq}=\frac{C_1 C_2}{C_1+C_2},\qquad\qquad L_{eq}=\frac{L_1 L_2}{L_1+L_2}.$$
> Comprobación con los datos del ejemplo: $C_{eq}=\dfrac{6\cdot 3}{6+3}=\dfrac{18}{9}=2\ \mu\text{F}$
> y $L_{eq}=\dfrac{2\cdot 6}{2+6}=\dfrac{12}{8}=1{,}5\ \text{mH}$, igual que antes.

> [!warning]
> No confundir estas reglas con las de las resistencias. Los **condensadores en serie** dan
> **menos** capacidad que cualquiera de ellos (igual que las resistencias en **paralelo** dan menos
> $R$). El error típico es sumar capacidades en serie: eso solo vale en paralelo. Para inductores
> ocurre lo contrario, así que conviene fijar la pareja: **$C$ se comporta como $G$, $L$ como $R$**.

## Resumen

> [!resumen]
> | Conexión | Condensadores | Inductores |
> |:---|:---:|:---:|
> | **Serie** | $\dfrac{1}{C_{eq}}=\sum_k \dfrac{1}{C_k}$ | $L_{eq}=\sum_k L_k$ |
> | **Paralelo** | $C_{eq}=\sum_k C_k$ | $\dfrac{1}{L_{eq}}=\sum_k \dfrac{1}{L_k}$ |
> | **Dos elementos** | $C_{eq}=\dfrac{C_1 C_2}{C_1+C_2}$ (serie) | $L_{eq}=\dfrac{L_1 L_2}{L_1+L_2}$ (paralelo) |
> | **Comparten** | serie: carga $q$ $\;\mid\;$ paralelo: tensión $v$ | serie: corriente $i$ $\;\mid\;$ paralelo: tensión $v$ |

> [!corolario]
> La asociación de almacenamiento es el **espejo** de la de resistencias: $C$ juega el papel de la
> conductancia $G$ y $L$ el de la resistencia $R$. Si recuerdas las reglas de
> [[Resistencias en Serie y Paralelo]], basta con intercambiar serie$\leftrightarrow$paralelo para
> los condensadores y dejarlas igual para los inductores.

> [!referencia]
> Fraile Mora, cap. 1, §1.5. Leyes base: [[Capacitor]], [[Inductor]]. Caso dual:
> [[Resistencias en Serie y Paralelo]]. Contexto: [[Elementos de Almacenamiento/index]].
