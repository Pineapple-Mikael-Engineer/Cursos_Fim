---
title: Núcleos Simétricos
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - fredholm
  - nucleos-simetricos
  - index
draft: false
aliases:
  - núcleos simétricos
  - teoría de Hilbert-Schmidt
  - symmetric kernels
---

# Núcleos Simétricos

> [!definicion]
> Un núcleo es **simétrico** cuando coincide al intercambiar sus argumentos,
> $$K(x,t)=K(t,x).$$
> Esa simetría hace que el operador integral $K\varphi=\int_a^b K(x,t)\,\varphi(t)\,dt$ sea
> **autoadjunto** ($\langle K\varphi,\psi\rangle=\langle\varphi,K\psi\rangle$), y entonces vale el
> análogo continuo del **teorema espectral**: las raíces características $\lambda_n$ son **reales**, las
> funciones propias $\varphi_n$ son **ortogonales** y el núcleo se **diagonaliza** en su propia base
> propia. Toda la teoría de Fredholm se vuelve, para estos núcleos, transparente.

> [!info]
> La rama **espectral** —y más potente— de [[Fredholm/index| Fredholm]], dentro del
> [[3 Ecuaciones Integrales/index| capítulo de ecuaciones integrales]]. Refina el espectro general de
> [[Raices Caracteristicas y Funciones Propias]] al caso autoadjunto, donde todo es real y ortogonal.
> Mapa de la sección: [[Teoria de Hilbert-Schmidt]], [[Teorema de Mercer]],
> [[Ecuaciones Simetricas No Homogeneas]].

---

## En qué consiste

> [!teoria] Un núcleo simétrico es una matriz simétrica de dimensión infinita
> En álgebra lineal, una **matriz simétrica** $\mathsf{A}=\mathsf{A}^{\mathsf{T}}$ es lo más cómodo que
> hay: es **diagonalizable**, sus autovalores son **reales** y sus autovectores forman una **base
> ortonormal**. Escogiendo esa base, $\mathsf{A}$ se vuelve diagonal y cualquier vector se descompone
> $\mathbf{x}=\sum_n\langle\mathbf{x},\mathbf{e}_n\rangle\mathbf{e}_n$, con $\mathsf{A}\mathbf{e}_n=\mu_n\mathbf{e}_n$.
>
> Un **núcleo simétrico** es exactamente eso, pero en un espacio de **funciones**. El papel de los
> autovectores lo hacen las **funciones propias** $\varphi_n$, y el de los autovalores, los inversos de
> las **raíces características**: $K\varphi_n=\dfrac{1}{\lambda_n}\varphi_n$. La simetría
> $K(x,t)=K(t,x)$ es la versión continua de $\mathsf{A}=\mathsf{A}^{\mathsf{T}}$, y de ella salen, **en
> cadena**, los tres resultados que dominan toda la teoría:
>
> 1. **Hilbert-Schmidt** — las $\varphi_n$ son una base ortonormal del rango de $K$, así que **toda
>    función de la forma $Kg$** se desarrolla en serie de funciones propias,
>    $$Kg=\sum_n\frac{\langle g,\varphi_n\rangle}{\lambda_n}\,\varphi_n.$$
>    Es la versión integral de "proyectar un vector sobre los autovectores de una matriz simétrica".
>    Lo desarrolla [[Teoria de Hilbert-Schmidt]].
>
> 2. **Mercer** — si además el núcleo es **definido positivo**, no solo se desarrolla $Kg$: se
>    desarrolla **el propio núcleo** en su base propia,
>    $$K(x,t)=\sum_{n=1}^\infty\frac{\varphi_n(x)\,\varphi_n(t)}{\lambda_n},$$
>    con convergencia **absoluta y uniforme**. El núcleo **es** su descomposición espectral, igual que
>    una matriz simétrica **es** $\sum_n\mu_n\mathbf{e}_n\mathbf{e}_n^{\mathsf{T}}$. Lo desarrolla
>    [[Teorema de Mercer]].
>
> 3. **Ecuación no homogénea** — la Fredholm de 2ª especie $\varphi=f+\lambda K\varphi$ se resuelve
>    **proyectando** $f$ sobre las $\varphi_n$ (**fórmula de Schmidt**),
>    $$\varphi(x)=f(x)+\lambda\sum_n\frac{\langle f,\varphi_n\rangle}{\lambda_n-\lambda}\,\varphi_n(x),$$
>    exactamente como se resuelve $(\mathsf{I}-\lambda\mathsf{A})\mathbf{x}=\mathbf{f}$ diagonalizando.
>    Lo desarrolla [[Ecuaciones Simetricas No Homogeneas]].
>
> Estos tres encadenados son la **herramienta más potente** disponible para Fredholm: cuando el núcleo
> es simétrico, dejas de luchar con determinantes o series de Neumann y simplemente **diagonalizas**.
> El espectro real y ortogonal que lo hace posible está en
> [[Raices Caracteristicas y Funciones Propias]].

> [!info] Recorrido de la sección
> | Nota | Aporte |
> |---|---|
> | [[Teoria de Hilbert-Schmidt\|Teoría de Hilbert-Schmidt]] | $Kg=\sum_n\frac{\langle g,\varphi_n\rangle}{\lambda_n}\varphi_n$: desarrollar en autofunciones |
> | [[Teorema de Mercer\|Teorema de Mercer]] | el núcleo **es** su serie espectral $K=\sum\varphi_n\varphi_n/\lambda_n$ |
> | [[Ecuaciones Simetricas No Homogeneas\|Ecuaciones Simétricas No Homogéneas]] | fórmula de Schmidt para $\varphi=f+\lambda K\varphi$ |
> | [[Raices Caracteristicas y Funciones Propias\|Raíces y Funciones Propias]] | el espectro real y ortogonal de fondo |

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Simetría | $K(x,t)=K(t,x)$ → operador **autoadjunto** |
> | Espectro | raíces $\lambda_n$ **reales**, funciones propias $\varphi_n$ **ortogonales** |
> | Hilbert-Schmidt | $Kg=\sum_n\frac{\langle g,\varphi_n\rangle}{\lambda_n}\varphi_n$ |
> | Mercer (def. positivo) | $K(x,t)=\sum_n\frac{\varphi_n(x)\varphi_n(t)}{\lambda_n}$, conv. uniforme |
> | No homogénea | Schmidt: $\varphi=f+\lambda\sum_n\frac{f_n}{\lambda_n-\lambda}\varphi_n$ |

> [!corolario]
> Un núcleo simétrico es una **matriz simétrica de dimensión infinita**: diagonalizable, con espectro
> real y base propia ortogonal. Esa única hipótesis —$K(x,t)=K(t,x)$— convierte la teoría general de
> Fredholm en un **problema de autovalores** limpio, donde resolver cualquier ecuación es proyectar
> sobre las funciones propias.

> [!referencia]
> - La pieza central: [[Teoria de Hilbert-Schmidt]].
> - El núcleo como serie espectral: [[Teorema de Mercer]].
> - Resolver la ecuación: [[Ecuaciones Simetricas No Homogeneas]].
> - El espectro de fondo: [[Raices Caracteristicas y Funciones Propias]].
> - Vuelta al panorama general: [[Fredholm/index]].
