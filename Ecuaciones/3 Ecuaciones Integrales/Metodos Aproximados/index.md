---
title: Métodos Aproximados
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - metodos-aproximados
  - index
draft: false
aliases:
  - métodos aproximados
  - métodos numéricos integrales
  - approximate methods
---

# Métodos Aproximados

> [!definicion]
> Cuando una ecuación integral no se resuelve en forma cerrada (el caso habitual), se **aproxima**.
> Todas las técnicas convierten la ecuación $\varphi=f+\lambda\int K\varphi$ en un **sistema lineal
> finito**, por uno de tres caminos: **degenerar** el núcleo, **proyectar** sobre una base finita
> (Galerkin, colocación), o **discretizar** la integral con una cuadratura (Nyström).

> [!info]
> Cara **computacional** del [[3 Ecuaciones Integrales/index| capítulo]]. Es la práctica de
> [[Fredholm Segunda Especie| Fredholm]] cuando el núcleo es general: todo se reduce a resolver
> $(\mathsf{I}-\lambda\mathsf{A})\mathbf{c}=\mathbf{f}$ para una matriz $\mathsf{A}$ que aproxima el
> operador integral. La base teórica es el [[Nucleo Degenerado| núcleo degenerado]].

---

## Las tres ideas (y por qué todas dan una matriz)

> [!teoria]
> El operador integral $K\varphi=\int_a^b K(x,t)\varphi(t)\,dt$ es de **dimensión infinita**; cada
> método lo **proyecta a dimensión finita** de una forma distinta:
> 1. **Degenerar el núcleo** ([[Sustitucion Nucleo Degenerado| sustitución]]): aproximar
>    $K\approx\sum_{i=1}^N a_i(x)b_i(t)$ (por Taylor, Fourier o interpolación) → la ecuación se vuelve
>    **exactamente** un sistema $N\times N$.
> 2. **Proyección** ([[Metodo de Bubnov-Galiorkin| Galerkin]] y [[Metodo de Colocacion| colocación]]):
>    buscar $\varphi\approx\sum c_i\phi_i$ en una base $\{\phi_i\}$ e imponer la ecuación, o bien en
>    **media** contra las $\phi_j$ (Galerkin) o **exactamente en $N$ puntos** (colocación).
> 3. **Cuadratura** ([[Cuadratura y Nystrom| Nyström]]): reemplazar la integral por una **suma
>    ponderada** $\int K\varphi\approx\sum_j w_j K(x,t_j)\varphi(t_j)$ → un sistema en los valores
>    nodales $\varphi(t_j)$.
>
> En los tres casos la matriz resultante hereda las propiedades del núcleo (simetría → matriz
> simétrica; los autovalores de la matriz aproximan las
> [[Raices Caracteristicas y Funciones Propias| raíces características]] —[[Raices Caracteristicas Aproximadas| Ritz, trazas, Kellog]]—).

> [!info] Recorrido de la sección
> | Nota | Idea |
> |---|---|
> | [[Sustitucion Nucleo Degenerado\|Sustitución del Núcleo]] | $K\approx\sum a_ib_i$ → sistema finito |
> | [[Aproximaciones Sucesivas Numericas\|Aproximaciones Sucesivas]] | iterar la resolvente numéricamente |
> | [[Metodo de Bubnov-Galiorkin\|Bubnov-Galiorkin]] | proyección en **media** (residuo ⟂ base) |
> | [[Metodo de Colocacion\|Colocación]] | imponer la ecuación en $N$ **puntos** |
> | [[Cuadratura y Nystrom\|Cuadratura y Nyström]] | discretizar la integral con pesos |
> | [[Raices Caracteristicas Aproximadas\|Raíces Características Aproximadas]] | Ritz, trazas, Kellog |

## Resumen

> [!resumen]
> | Método | Qué hace | Resultado |
> |---|---|---|
> | Núcleo degenerado | trunca $K$ | sistema $N\times N$ exacto |
> | Galerkin | residuo ⟂ base | sistema (mejor en media $L^2$) |
> | Colocación | exacto en puntos | sistema (más simple de montar) |
> | Nyström | cuadratura de la integral | sistema en valores nodales |

> [!corolario]
> Resolver una ecuación integral numéricamente es **discretizar un operador a una matriz**. La
> elección del método es la elección de **cómo** proyectar el infinito al finito —en media, en puntos
> o por cuadratura—; todos convergen al refinar, y la calidad depende de cuán bien la base o los nodos
> capturen el núcleo y la solución.

> [!referencia]
> - El fundamento: [[Nucleo Degenerado]].
> - El más usado en la práctica: [[Cuadratura y Nystrom]].
> - Estimar el espectro: [[Raices Caracteristicas Aproximadas]].
