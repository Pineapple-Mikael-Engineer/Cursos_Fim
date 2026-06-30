---
title: Ecuaciones de Fredholm
order: 4
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - fredholm
  - index
draft: false
aliases:
  - ecuaciones de Fredholm
  - Fredholm equations
---

# Ecuaciones de Fredholm

> [!definicion]
> Una **ecuación integral de Fredholm** tiene los **límites fijos**:
> $$\varphi(x)=f(x)+\lambda\int_{a}^{b}K(x,t)\,\varphi(t)\,dt\quad(\text{2ª especie}),\qquad f(x)=\int_{a}^{b}K(x,t)\,\varphi(t)\,dt\quad(\text{1ª especie}).$$
> Al integrar siempre sobre **todo** $[a,b]$, es un problema **global**: a diferencia de [[Volterra/index| Volterra]], puede tener una, ninguna o infinitas soluciones según el valor de $\lambda$ frente al **espectro** del núcleo.

> [!info]
> La familia **espectral** del [[3 Ecuaciones Integrales/index| capítulo de ecuaciones integrales]]. Es el análogo continuo de un sistema lineal $\mathbf{x}=\mathbf{f}+\lambda A\mathbf{x}$: el núcleo $K$ hace de matriz, con sus **autovalores** y **funciones propias**. Aparece al reducir problemas de frontera ([[Reduccion de Problemas de Frontera| reducción de PVF]]) y conecta con [[Sturm-Liouville/index| Sturm-Liouville]].

---

## La clave: Fredholm es álgebra lineal en dimensión infinita

> [!teoria]
> Escribe la ecuación como $(\mathbb{I}-\lambda K)\varphi=f$, con $K$ el **operador integral** $K\varphi=\int_a^b K(x,t)\varphi(t)\,dt$. Es idéntica a un sistema lineal $(\mathsf{I}-\lambda \mathsf{A})\mathbf{x}=\mathbf{f}$, solo que en un espacio de **funciones**. De ahí todo:
> - **Cuándo hay solución única.** Si $\lambda$ **no** es un autovalor del núcleo, $(\mathbb{I}-\lambda K)$ es invertible y la solución es única (resolvente). Si $\lambda$ **es** autovalor, o no hay solución o hay infinitas — la [[Alternativa de Fredholm| alternativa de Fredholm]].
> - **El espectro del núcleo.** La ecuación homogénea $\varphi=\lambda\int K\varphi$ tiene solución no trivial solo para ciertos $\lambda=\lambda_n$ (**raíces características**), con sus **funciones propias** ([[Raices Caracteristicas y Funciones Propias| autovalores y funciones propias]]).
> - **Métodos según el núcleo.** [[Nucleo Degenerado| núcleo degenerado]] $K=\sum a_i(x)b_i(t)$ → sistema lineal **finito**; núcleo general → [[Determinantes de Fredholm| determinantes de Fredholm]] o [[Nucleos Iterados y Resolvente| resolvente]]; núcleo **simétrico** → la potente [[Nucleos Simetricos/index| teoría de Hilbert-Schmidt]] (autofunciones ortogonales, como una diagonalización).

> [!info] Recorrido de la sección
> | Nota | Aporte |
> |---|---|
> | [[Fredholm Segunda Especie\|Fredholm de 2ª Especie]] | la ecuación estándar; existencia según $\lambda$ |
> | [[Fredholm Primera Especie y Problemas Mal Planteados\|1ª Especie y Mal Planteamiento]] | problema inverso; regularización de Tikhonov |
> | [[Nucleo Degenerado\|Núcleo Degenerado]] | $K=\sum a_ib_i$ → sistema lineal finito |
> | [[Determinantes de Fredholm\|Determinantes de Fredholm]] | resolvente como cociente de series enteras |
> | [[Nucleos Iterados y Resolvente\|Núcleos Iterados y Resolvente]] | serie de Neumann (si $\lvert\lambda\rvert$ pequeño) |
> | [[Raices Caracteristicas y Funciones Propias\|Raíces Características y Funciones Propias]] | el espectro del núcleo |
> | [[Alternativa de Fredholm\|Alternativa de Fredholm]] | existencia/unicidad; la dicotomía |
> | [[Nucleos Simetricos/index\|Núcleos Simétricos]] | Hilbert-Schmidt, Mercer (diagonalización) |
> | [[Reduccion de Problemas de Frontera\|Reducción de Problemas de Frontera]] | PVF → Fredholm vía función de Green |

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Forma (2ª especie) | $(\mathbb{I}-\lambda K)\varphi=f$, límites fijos $\int_a^b$ |
> | Existencia | única si $\lambda\notin$ espectro; si no, [[Alternativa de Fredholm\|alternativa]] |
> | Núcleo degenerado | reduce a **sistema lineal finito** |
> | Núcleo general | [[Determinantes de Fredholm\|determinantes]] / [[Nucleos Iterados y Resolvente\|resolvente]] |
> | Núcleo simétrico | [[Nucleos Simetricos/index\|Hilbert-Schmidt]]: autofunciones ortogonales |

> [!corolario]
> Fredholm es **álgebra lineal en dimensión infinita**: el núcleo es una matriz, $\lambda$ juega el papel de un (inverso de) autovalor, y resolver depende de si $\lambda$ está o no en el **espectro**. Por eso, a diferencia de Volterra (siempre resoluble), Fredholm hereda toda la riqueza —y las sutilezas— de los sistemas lineales y sus autovalores.

> [!referencia]
> - El caso más simple y operativo: [[Nucleo Degenerado]].
> - El corazón teórico: [[Raices Caracteristicas y Funciones Propias]] y [[Alternativa de Fredholm]].
> - La teoría más fina: [[Nucleos Simetricos/index]].
