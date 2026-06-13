---
title: Grupo Homogéneo de Lorentz
tags:
  - analisis-tensorial
  - teoria
  - teoria-grupos
  - lorentz
draft: false
aliases:
  - grupo de Lorentz
  - transformaciones de Lorentz
  - espacio de Minkowski
  - Lorentz group
---

# Grupo Homogéneo de Lorentz

> [!definicion]
> El **grupo homogéneo de Lorentz** son las **rotaciones espaciales + transformaciones de Lorentz** (*boosts*) que dejan invariante el intervalo del **espacio de Minkowski**
> $$x_0^2-x_1^2-x_2^2-x_3^2=x^\mu x_\mu,\qquad x^\mu=(x_0,\vec x),\ x_\mu=(x_0,-\vec x),\ x_0=ct,$$
> con el tensor métrico $g_{\mu\nu}=g^{\mu\nu}=\operatorname{diag}(1,-1,-1,-1)$. (Con traslaciones forman el grupo de **Poincaré**.)

> [!info]
> Sección 7.4 del [[index | capítulo 7]] (libro, cap. 7.4). Es la simetría de la **relatividad especial**: las leyes físicas deben ser covariantes bajo Lorentz, igual que son covariantes bajo [[6 Determinantes y Matrices/Matrices Ortogonales | rotaciones]]. Su métrica indefinida (a diferencia de la euclídea) hace que el producto escalar de [[5 Coordenadas No Ortogonales/index | cuadrivectores]] no sea definido positivo. Es la base para escribir [[Covarianza de Lorentz de Maxwell | Maxwell en forma tensorial]].

---

## Ejemplo

> [!ejemplo]
> **Un *boost* a lo largo de $x_1$.** Para velocidad $v$ paralela al eje $x_1$, la transformación de Lorentz que conserva $x_0^2-x_1^2$ es, con la **rapidez** $\rho$ y $\sigma_1$ la matriz de Pauli,
> $$\begin{pmatrix}x'_0\\x'_1\end{pmatrix}=\exp(-\rho\sigma_1)\begin{pmatrix}x_0\\x_1\end{pmatrix}=\begin{pmatrix}\cosh\rho&-\operatorname{senh}\rho\\-\operatorname{senh}\rho&\cosh\rho\end{pmatrix}\begin{pmatrix}x_0\\x_1\end{pmatrix}.$$
> Es una "rotación con ángulo imaginario": donde la rotación euclídea tiene $\cos,\operatorname{sen}$, el *boost* tiene $\cosh,\operatorname{senh}$. Identificando el origen del sistema primado ($x'_1=0\Rightarrow x_1=vt$):
> $$\tanh\rho=\beta=\frac{v}{c},\qquad \cosh\rho=\gamma=\frac{1}{\sqrt{1-\beta^2}},\qquad \operatorname{senh}\rho=\beta\gamma.$$
> Sustituyendo se recuperan las fórmulas usuales $x'_1=\gamma(x_1-\beta x_0)$, $x'_0=\gamma(x_0-\beta x_1)$.

> [!ejemplo] El cono de luz
> ![[cono_de_luz.svg|440]]
>
> La invariancia $x_0^2-\vec x^2=0$ (un pulso de luz desde el origen) define el **cono de luz**, el mismo en todo sistema inercial. Separa el futuro/pasado causal (interior, $x^\mu x_\mu>0$) de las regiones sin contacto causal (exterior). Un *boost* "inclina" los ejes $x'_0,x'_1$ hacia el cono, pero lo deja fijo.

---

## En qué consiste

> [!teoria]
> La rapidez se obtiene como en SO(3) pero con **generador antihermítico imaginario**: partiendo de un *boost* infinitesimal $\delta\beta$ y exponenciando $N$ veces ($\rho=N\,\delta\beta$, $N\to\infty$),
> $$\lim_{N\to\infty}\left(\mathsf{1}-\frac{\rho\sigma_1}{N}\right)^N=\exp(-\rho\sigma_1)=\mathsf{1}\cosh\rho+\sigma_1\operatorname{senh}\rho,$$
> usando $\sigma_1^2=\mathsf{1}$. La diferencia con la rotación real está en el signo de la métrica: la longitud euclídea $\sum x_i^2$ se reemplaza por $x_0^2-\vec x^2$, que **no** es definida positiva.

> [!proposicion] Estructura de grupo
> Los *boosts* en una dirección fija forman un subgrupo (se componen sumando rapideces: $\rho_3=\rho_1+\rho_2$, que es la **regla de adición de velocidades** de Einstein, $\tanh$ no es aditivo pero $\rho$ sí). Los *boosts* en direcciones distintas **no** conmutan, y su composición incluye una rotación (precesión de Thomas). Junto con las rotaciones espaciales forman el grupo homogéneo de Lorentz.

> [!info] Cuadrivectores en Minkowski
> | Objeto | Componentes | Norma (invariante) |
> |---|---|---|
> | Posición | $x^\mu=(ct,\vec x)$ | $c^2t^2-\vec x^2$ |
> | Gradiente | $\partial^\mu=(\partial/\partial x_0,-\vec\nabla)$ | $\partial^\mu\partial_\mu=\partial^2$ (d'Alembertiano) |
> | Métrica | $g_{\mu\nu}=\operatorname{diag}(1,-1,-1,-1)$ | sube/baja índices |

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Grupo | rotaciones + *boosts* (Poincaré con traslaciones) |
> | Invariante | $x_0^2-\vec x^2$ (intervalo de Minkowski) |
> | Métrica | $g_{\mu\nu}=\operatorname{diag}(1,-1,-1,-1)$ |
> | *Boost* | $\cosh\rho,\operatorname{senh}\rho$; $\tanh\rho=\beta$, $\cosh\rho=\gamma$ |
> | vs rotación | ángulo imaginario; métrica indefinida |

> [!corolario]
> El grupo de Lorentz es la simetría del espacio-tiempo: un *boost* es una "rotación hiperbólica" que mezcla espacio y tiempo conservando $x_0^2-\vec x^2$. Su métrica indefinida $\operatorname{diag}(1,-1,-1,-1)$ es lo único que lo distingue formalmente del grupo de rotaciones $SO(3)$. Sobre esta estructura se escriben las leyes físicas en forma **manifiestamente covariante**, culminando con [[Covarianza de Lorentz de Maxwell | el tensor del campo electromagnético]].

> [!referencia]
> - Cuadrivectores y subir/bajar índices: [[5 Coordenadas No Ortogonales/index]].
> - Maxwell como tensor de Lorentz: [[Covarianza de Lorentz de Maxwell]].
> - Análogo euclídeo (rotaciones): [[6 Determinantes y Matrices/Matrices Ortogonales]].
