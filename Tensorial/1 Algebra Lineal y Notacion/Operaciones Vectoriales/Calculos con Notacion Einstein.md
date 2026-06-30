---
title: Cálculos con Notación de Einstein
order: 5
tags:
  - analisis-tensorial
  - teoria
  - notacion-indices
  - einstein
draft: false
aliases:
  - calculos con notacion einstein
  - identidad BAC-CAB
  - doble producto cruz
  - Einstein notation calculations
  - BAC-CAB rule
---

# Cálculos con Notación de Einstein

> [!definicion]
> Dos derivaciones guía que muestran la potencia de la notación de subíndices:
> 1. La **rotación conserva la magnitud**: $\vec{A}\,'\cdot\vec{A}\,'=\vec{A}\cdot\vec{A}$, usando la ortogonalidad $R_{ru}R_{rv}=\delta_{uv}$.
> 2. La identidad del **doble producto cruz** (BAC-CAB): $\vec{A}\times(\vec{B}\times\vec{C})=(\vec{A}\cdot\vec{C})\vec{B}-(\vec{A}\cdot\vec{B})\vec{C}$, vía la identidad $\varepsilon$-$\delta$.

> [!info]
> Es la sección 1.2.3 del libro, dentro de [[index | Operaciones Vectoriales]] del [[../index | capítulo 1]]. Combina la [[Rotacion de Vectores | rotación]] $a_i'=R_{ij}a_j$ y los [[Productos Vectoriales | productos punto y cruz]]. La identidad $\varepsilon_{ijk}\varepsilon_{mnk}=\delta_{im}\delta_{jn}-\delta_{in}\delta_{jm}$ y su prueba se delegan a [[Simbolos Especiales/Identidad Epsilon-Delta]].

---

## Ejemplo

> [!ejemplo] Ejemplo 1 — La rotación conserva la magnitud
> Queremos mostrar que $\vec{A}\,'\cdot\vec{A}\,'=\vec{A}\cdot\vec{A}$, donde $\vec{A}\,'$ es $\vec{A}$ rotado. Por [[Productos Vectoriales | (1.40)]], el producto punto es $\vec{A}\cdot\vec{A}=A_iA_i$; con **índices distintos** para mantener las sumas independientes:
> $$\vec{A}\cdot\vec{A}=A_iA_i,\qquad \vec{A}\,'\cdot\vec{A}\,'=A_j'A_j'.$$
>
> **Paso 1 — Insertar la rotación** $A_i'=R_{ij}A_j$. Para no colisionar índices, escribimos $A_j'=R_{ju}A_u$ con índices mudos $u$ y $v$ separados:
> $$\vec{A}\,'\cdot\vec{A}\,'=A_j'A_j'=R_{ru}A_u\,R_{rv}A_v.$$
> Hay tres sumas implícitas: sobre $r$, $u$ y $v$.
>
> **Paso 2 — Reordenar.** En índices el orden de los factores no importa (son números), así que agrupamos las componentes de $\vec{A}$ y aparte el producto de las matrices:
> $$\vec{A}\,'\cdot\vec{A}\,'=A_uA_v\,R_{ru}R_{rv}.$$
>
> **Paso 3 — Ortogonalidad.** La suma sobre $r$ en $R_{ru}R_{rv}$ contrae el **primer** índice de ambas matrices, es decir $[R]^\dagger[R]$. Como $[R]^\dagger[R]=[1]$, se tiene la condición de ortogonalidad
> $$R_{ru}R_{rv}=\delta_{uv}.$$
>
> **Paso 4 — Contraer la delta.** $\delta_{uv}$ sustituye $v$ por $u$:
> $$\vec{A}\,'\cdot\vec{A}\,'=A_uA_v\,\delta_{uv}=A_uA_u=\vec{A}\cdot\vec{A}.\qquad\blacksquare$$
>
> **Versión matricial (comparación).** El mismo resultado con matrices: $\vec{A}\cdot\vec{A}=[A]^\dagger[A]$ y, como $[A']=[R(\phi)][A]$ implica $[A']^\dagger=[A]^\dagger[R(\phi)]^\dagger$,
> $$\vec{A}\,'\cdot\vec{A}\,'=[A]^\dagger[R(\phi)]^\dagger[R(\phi)][A]=[A]^\dagger[1][A]=[A]^\dagger[A]=\vec{A}\cdot\vec{A}.$$
> Las dos rutas coinciden; la matricial exige cuidar el **orden** de los factores, la de índices no.

> [!ejemplo] Ejemplo 2 — Identidad BAC-CAB
> Derivamos $\vec{A}\times(\vec{B}\times\vec{C})=(\vec{A}\cdot\vec{C})\vec{B}-(\vec{A}\cdot\vec{B})\vec{C}$, "imposible" sin índices. Usamos la forma de subíndices de un vector $\vec{V}=V_i\hat{e}_i$, el punto $\vec{A}\cdot\vec{B}=A_iB_i$ y la cruz $\vec{A}\times\vec{B}=\varepsilon_{ijk}A_iB_j\hat{e}_k$.
>
> **Paso 1 — Cruz interior.** Sea $\vec{D}=\vec{B}\times\vec{C}=\varepsilon_{ijk}B_iC_j\hat{e}_k$.
>
> **Paso 2 — Componente $s$-ésima de $\vec{D}$**, proyectando con $\hat{e}_s$ y usando $\hat{e}_s\cdot\hat{e}_k=\delta_{sk}$:
> $$D_s=\hat{e}_s\cdot\vec{D}=B_iC_j\varepsilon_{ijk}(\hat{e}_s\cdot\hat{e}_k)=B_iC_j\varepsilon_{ijk}\delta_{sk}=B_iC_j\varepsilon_{ijs}.$$
>
> **Paso 3 — Cruz exterior.** Ahora $\vec{A}\times\vec{D}=\varepsilon_{rst}A_rD_s\hat{e}_t$; sustituyendo $D_s$:
> $$\vec{A}\times(\vec{B}\times\vec{C})=A_rB_iC_j\,\varepsilon_{ijs}\varepsilon_{rst}\,\hat{e}_t.$$
>
> **Paso 4 — Identidad $\varepsilon$-$\delta$.** Con el último índice $s$ en común (tras reordenar $\varepsilon_{ijs}\varepsilon_{rst}=\varepsilon_{ijs}\varepsilon_{rts}$ por antisimetría, o aplicando directamente la forma del libro $\varepsilon_{ijk}\varepsilon_{mnk}=\delta_{im}\delta_{jn}-\delta_{in}\delta_{jm}$):
> $$\varepsilon_{ijs}\varepsilon_{rts}=\delta_{ir}\delta_{jt}-\delta_{it}\delta_{jr}.$$
> Su prueba se delega a [[Simbolos Especiales/Identidad Epsilon-Delta]]. Entonces
> $$\vec{A}\times(\vec{B}\times\vec{C})=A_rB_iC_j\,(\delta_{ir}\delta_{jt}-\delta_{it}\delta_{jr})\,\hat{e}_t.$$
>
> **Paso 5 — Contraer las deltas.** El primer término fija $i=r$, $j=t$; el segundo $i=t$, $j=r$:
> $$\vec{A}\times(\vec{B}\times\vec{C})=A_iB_iC_t\hat{e}_t-A_jB_tC_j\hat{e}_t=(A_iB_i)\,C_t\hat{e}_t-(A_jC_j)\,B_t\hat{e}_t.$$
>
> **Paso 6 — Volver a notación vectorial.** Reconociendo $A_iB_i=\vec{A}\cdot\vec{B}$, $A_jC_j=\vec{A}\cdot\vec{C}$, $C_t\hat{e}_t=\vec{C}$ y $B_t\hat{e}_t=\vec{B}$, y reordenando:
> $$\boxed{\vec{A}\times(\vec{B}\times\vec{C})=(\vec{A}\cdot\vec{C})\,\vec{B}-(\vec{A}\cdot\vec{B})\,\vec{C}.}$$
> El penúltimo paso vale solo en cartesianas; el último, ya en forma vectorial, es válido en **cualquier** sistema de coordenadas. $\blacksquare$

---

## En qué consiste

> [!teoria]
> Ambos ejemplos siguen el mismo ciclo de trabajo de la notación de Einstein:
> 1. **Convertir** la expresión vectorial a índices (usar $\vec{V}=V_i\hat{e}_i$, $A_iB_i$, $\varepsilon_{ijk}A_iB_j\hat{e}_k$).
> 2. **Manipular** libremente: reordenar factores, contraer con $\delta_{ij}$ y aplicar la identidad $\varepsilon$-$\delta$.
> 3. **Volver** a notación vectorial, recobrando un resultado independiente del sistema de coordenadas.
>
> El cuidado clave es **renombrar índices mudos** para que ninguno aparezca más de dos veces por término (regla de oro): por eso se introdujeron $u,v$ en el ejemplo 1 y $r,s,t$ frente a $i,j$ en el ejemplo 2.

> [!proposicion] Ortogonalidad de la matriz de rotación
> La condición $R_{ru}R_{rv}=\delta_{uv}$ (equivalente a $[R]^\dagger[R]=[1]$) es lo que garantiza que la rotación preserve la magnitud, y por tanto el producto punto y los ángulos. Una matriz que la cumple es **ortogonal**; las rotaciones son su caso propio (determinante $+1$).

## Resumen

> [!resumen]
> | Ejemplo | Herramienta clave | Resultado |
> |---|---|---|
> | Magnitud bajo rotación | ortogonalidad $R_{ru}R_{rv}=\delta_{uv}$ | $\vec{A}\,'\cdot\vec{A}\,'=\vec{A}\cdot\vec{A}$ |
> | Doble producto cruz | identidad $\varepsilon_{ijk}\varepsilon_{mnk}=\delta_{im}\delta_{jn}-\delta_{in}\delta_{jm}$ | $(\vec{A}\cdot\vec{C})\vec{B}-(\vec{A}\cdot\vec{B})\vec{C}$ |

> [!corolario]
> El primer ejemplo prueba la **equivalencia** entre notación matricial y de Einstein; el segundo, su **superioridad** para derivar identidades vectoriales complicadas en pocas líneas. El método —convertir a índices, contraer, volver a vectores— es el que se reutiliza en todo el cálculo vectorial y tensorial posterior.

> [!referencia]
> - Rotación y su matriz: [[Rotacion de Vectores]].
> - Productos punto y cruz en índices: [[Productos Vectoriales]].
> - Identidad $\varepsilon$-$\delta$ (prueba completa): [[Simbolos Especiales/Identidad Epsilon-Delta]].
> - Símbolos involucrados: [[Simbolos Especiales/Delta Kronecker]] · [[Simbolos Especiales/Simbolo Levi-Civita]].
