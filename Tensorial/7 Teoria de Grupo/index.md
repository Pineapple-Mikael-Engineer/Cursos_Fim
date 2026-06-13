---
title: Teoría de Grupo
tags:
  - analisis-tensorial
  - teoria
  - teoria-grupos
  - index
draft: false
aliases:
  - teoria de grupo
  - capitulo 7 tensorial
  - grupos de simetria
  - group theory
---

# Teoría de Grupo

> [!definicion]
> Un **grupo** $G$ es un conjunto de operaciones con un producto que cumple cuatro axiomas: **clausura** ($ab\in G$), **asociatividad** ($(ab)c=a(bc)$), **elemento neutro** ($Ia=aI=a$) e **inverso** ($aa^{-1}=a^{-1}a=I$). La teoría de grupo es la matemática de la **simetría**: en física, cada simetría de un sistema conduce a una **ley de conservación**.

> [!info]
> Es el **capítulo 7** del libro (Rogan & Muñoz, Parte I; basado en Arfken & Weber cap. 4), y el **cierre del curso**: aquí toda la maquinaria tensorial desemboca en la física. Se desglosa en:
> - [[Generadores de Grupos Continuos]] — grupos de Lie, generadores, SO(3), SU(2), SU(3) (cap. 7.2).
> - [[Momento Angular Orbital]] — operadores de subida/bajada, $J^2=J(J+1)$ (cap. 7.3).
> - [[Grupo Homogeneo de Lorentz]] — *boosts* y rotaciones, espacio de Minkowski (cap. 7.4).
> - [[Covarianza de Lorentz de Maxwell]] — el tensor $F_{\mu\nu}$, Maxwell en forma tensorial (cap. 7.5).

---

## Ejemplo

> [!ejemplo]
> **El grupo de rotaciones $SO(2)$.** Las rotaciones del plano
> $$\mathsf{R}(\varphi)=\begin{pmatrix}\cos\varphi&\operatorname{sen}\varphi\\-\operatorname{sen}\varphi&\cos\varphi\end{pmatrix}$$
> forman un grupo: el producto de dos rotaciones es otra rotación $\mathsf{R}(\varphi_1)\mathsf{R}(\varphi_2)=\mathsf{R}(\varphi_1+\varphi_2)$ (clausura + asociatividad de matrices), el neutro es $\varphi=0$, y el inverso de $\mathsf{R}(\varphi)$ es $\mathsf{R}(-\varphi)$. Es **abeliano** (conmutativo: el orden de las rotaciones no importa) y **continuo** ($\varphi$ varía de $0$ a $2\pi$): tiene infinitos elementos. Es el ejemplo más simple de **grupo de Lie**.

---

## En qué consiste

> [!teoria]
> El descubrimiento central (Wigner, principios del s. XX): **invariancia $\Rightarrow$ ley de conservación**. La invariancia bajo rotaciones espaciales da la conservación del momento angular; bajo traslaciones, la del momento lineal. La teoría de grupo formaliza estas simetrías y, representando los elementos por **matrices**, las vuelve calculables.
>
> Las matrices ortogonales $n\times n$ forman el grupo $O(n)$ (y $SO(n)$ si $\det=+1$); las unitarias, $U(n)$ y $SU(n)$. Estos grupos **son** la física moderna: $SO(3)$ (rotaciones), $SU(2)$ (spin e isospin), $SU(3)$ (sabor de quarks), el grupo de **Lorentz** (relatividad). El capítulo conecta todo el curso con la física: el [[Momento Angular Orbital | momento angular]] cuantizado, las partículas en multipletes, y las ecuaciones de [[Covarianza de Lorentz de Maxwell | Maxwell escritas como un tensor]].

> [!info] Grupos de la física
> | Grupo | Qué transforma | Física |
> |---|---|---|
> | $SO(3)$ | rotaciones reales 3D | momento angular |
> | $SU(2)$ | spinores complejos 2D | spin $\tfrac12$, isospin |
> | $SU(3)$ | tripletes complejos 3D | sabor / color (quarks, QCD) |
> | Lorentz | espacio-tiempo de Minkowski | relatividad especial |

## Resumen

> [!resumen]
> | Subnota | Aporta |
> |---|---|
> | [[Generadores de Grupos Continuos]] | Lie, $[\mathsf{S}_i,\mathsf{S}_j]=c_{ij}^k\mathsf{S}_k$, SO(3)/SU(2)/SU(3) |
> | [[Momento Angular Orbital]] | $J_\pm$, $J^2=J(J+1)$, cuantización |
> | [[Grupo Homogeneo de Lorentz]] | *boosts*, Minkowski, $\gamma$ |
> | [[Covarianza de Lorentz de Maxwell]] | $F_{\mu\nu}$, Maxwell tensorial |

> [!corolario]
> La teoría de grupo es el destino del curso: la simetría, escrita en el lenguaje tensorial de los capítulos previos, organiza y predice la física. Un grupo de Lie se reconstruye desde sus **generadores** (capítulo 7.2); el momento angular sale de sus relaciones de conmutación; y la unión de $\vec E$ y $\vec B$ en el tensor $F_{\mu\nu}$ hace **manifiesta** la covarianza de Lorentz de Maxwell. Aquí el álgebra tensorial deja de ser herramienta y se vuelve el idioma de las leyes físicas.

> [!referencia]
> - Matrices ortogonales/unitarias (base): [[6 Determinantes y Matrices/Matrices Ortogonales]] · [[6 Determinantes y Matrices/Matrices Hermiticas y Unitarias]].
> - Generadores y álgebras de Lie: [[Generadores de Grupos Continuos]].
> - El cierre físico: [[Covarianza de Lorentz de Maxwell]].
