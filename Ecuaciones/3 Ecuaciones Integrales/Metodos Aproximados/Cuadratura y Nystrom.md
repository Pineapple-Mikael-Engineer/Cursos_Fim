---
title: Cuadratura y Nyström
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - metodos-aproximados
  - nystrom
draft: false
aliases:
  - cuadratura y Nyström
  - método de Nyström
  - Nyström method
  - quadrature method
---

# Cuadratura y Nyström

> [!definicion]
> El **método de Nyström** discretiza la ecuación integral reemplazando la integral por una
> **cuadratura numérica**:
> $$\int_a^b K(x,t)\,\varphi(t)\,dt\;\approx\;\sum_{j=1}^{N}w_j\,K(x,t_j)\,\varphi(t_j),$$
> con **nodos** $t_j$ y **pesos** $w_j$ de una regla (trapecio, Simpson, Gauss…). Imponiendo la ecuación
> en esos **mismos** nodos $x=t_i$ y abreviando $\varphi_i=\varphi(t_i)$, $f_i=f(t_i)$, queda
> $$\varphi_i=f_i+\lambda\sum_{j=1}^{N}w_j\,K(t_i,t_j)\,\varphi_j,\qquad i=1,\dots,N,$$
> es decir un sistema lineal $(\mathsf{I}-\lambda\mathsf{A})\boldsymbol\varphi=\mathbf{f}$ con
> $$\mathsf{A}_{ij}=w_j\,K(t_i,t_j).$$
> Las incógnitas son directamente los **valores nodales** $\varphi_i$ de la solución.

> [!info]
> Es el método **estándar en la práctica** para Fredholm de 2ª especie, base de los métodos de
> elementos de frontera (BEM), acústica y electromagnetismo. A diferencia de la
> [[Sustitucion Nucleo Degenerado| sustitución del núcleo]] (que aproxima $K$) y de
> [[Metodo de Colocacion| colocación]]/Galerkin (que aproximan $\varphi$ por una base), Nyström
> **aproxima la integral** directamente y resuelve los valores de $\varphi$ en los nodos. La matriz
> $\mathsf{A}$ es **llena** (cada nodo se acopla con todos), y la calidad del método es la de la
> **cuadratura** que se elija. Parte de los [[Metodos Aproximados/index| métodos aproximados]] del
> [[3 Ecuaciones Integrales/index| capítulo]].

---

## Ejemplo

> [!ejemplo] Convergencia de los métodos
> ![[convergencia_metodos.svg|470]]
>
> Error frente al número de nodos/términos $N$ (escala log): colocación y Galerkin de bajo orden
> convergen **polinomialmente** (rectas de pendiente moderada en log–log), mientras que Nyström con
> **cuadratura gaussiana** sobre un núcleo suave converge **espectralmente** (la curva se desploma:
> el error cae más rápido que cualquier potencia de $N$). Por eso, a igualdad de tamaño de sistema,
> Nyström-Gauss suele ser el más preciso para núcleos regulares.

> [!ejemplo] Matriz de Nyström con la regla del trapecio
> Discreticemos por Nyström
> $$\varphi(x)=1+\tfrac12\int_{0}^{1}(x+t)\,\varphi(t)\,dt$$
> con la **regla del trapecio** sobre $N=3$ nodos equiespaciados $t_1=0,\ t_2=\tfrac12,\ t_3=1$
> ($h=\tfrac12$). Los pesos del trapecio compuesto son
> $w_1=\tfrac{h}{2}=\tfrac14,\ w_2=h=\tfrac12,\ w_3=\tfrac{h}{2}=\tfrac14$.
>
> **Paso 1 — tabla del núcleo.** $K(t_i,t_j)=t_i+t_j$:
> $$\big(K(t_i,t_j)\big)=\begin{pmatrix}0&\tfrac12&1\\[2pt]\tfrac12&1&\tfrac32\\[2pt]1&\tfrac32&2\end{pmatrix}.$$
>
> **Paso 2 — matriz $\mathsf{A}_{ij}=w_jK(t_i,t_j)$** (multiplica la **columna** $j$ por $w_j$):
> $$\mathsf{A}=\begin{pmatrix}0&\tfrac14&\tfrac14\\[2pt]\tfrac18&\tfrac12&\tfrac38\\[2pt]\tfrac14&\tfrac34&\tfrac12\end{pmatrix}.$$
>
> **Paso 3 — sistema $(\mathsf{I}-\tfrac12\mathsf{A})\boldsymbol\varphi=\mathbf{f}$**, con $\mathbf{f}=(1,1,1)^{\!\top}$
> y $\lambda=\tfrac12$:
> $$\mathsf{I}-\tfrac12\mathsf{A}=\begin{pmatrix}1&-\tfrac18&-\tfrac18\\[2pt]-\tfrac{1}{16}&\tfrac34&-\tfrac{3}{16}\\[2pt]-\tfrac18&-\tfrac38&\tfrac34\end{pmatrix}.$$
>
> **Paso 4 — resuelve.** Resolviendo el sistema $3\times3$ se obtiene
> $$\varphi_1\approx1.703,\qquad \varphi_2\approx2.141,\qquad \varphi_3\approx2.579,$$
> que son los valores nodales de la solución en $0,\tfrac12,1$. Compárense con la solución exacta
> $\varphi(x)=\tfrac{12}{7}+\tfrac67 x$: $\varphi(0)=1.714$, $\varphi(\tfrac12)=2.143$, $\varphi(1)=2.571$.
> Con apenas tres nodos del **trapecio** el error ya es de pocas milésimas; con cuadratura de **Gauss**
> de igual tamaño sería aún menor.
>
> **Paso 5 — extiende a todo $x$ (interpolación de Nyström).** No interpolamos los puntos a mano: la
> propia ecuación da el valor en cualquier $x$,
> $$\varphi(x)=1+\tfrac12\sum_{j=1}^{3}w_j\,(x+t_j)\,\varphi_j,$$
> que es la fórmula natural y de la **misma precisión** que la cuadratura.

---

## En qué consiste

> [!teoria] La interpolación de Nyström
> El método entrega los valores $\varphi_i$ en los nodos, pero la solución se necesita en **todo**
> $[a,b]$. La extensión natural no es interpolar los $\varphi_i$ con un polinomio cualquiera, sino
> reusar la **propia fórmula de cuadratura**:
> $$\boxed{\;\varphi(x)=f(x)+\lambda\sum_{j=1}^{N}w_j\,K(x,t_j)\,\varphi_j\;}$$
> Esta **interpolante de Nyström** evalúa $x$ en el núcleo (no en una base ajena), de modo que **hereda
> la precisión de la cuadratura**: si la regla integra bien, $\varphi(x)$ es tan exacta entre nodos como
> en ellos. La consecuencia clave es sobre la **convergencia**: el error global del método es el error
> de la cuadratura sobre la integral $\int K\varphi$. Para núcleos **suaves**, la cuadratura
> **gaussiana** converge **espectralmente** (exponencialmente en $N$), mucho más rápido que la
> convergencia polinómica de Galerkin/colocación de bajo orden. Si el núcleo tiene singularidades (p.ej.
> $\log|x-t|$ o $|x-t|^{-\alpha}$), conviene una cuadratura **adaptada** a esa singularidad para no
> perder el orden.

> [!algoritmo] Resolver por Nyström
> 1. **Elige una cuadratura** $\{(t_j,w_j)\}_{j=1}^N$ en $[a,b]$ (Gauss–Legendre para núcleos suaves;
>    reglas especiales si $K$ es singular).
> 2. **Ensambla** la matriz $\mathsf{A}_{ij}=w_j\,K(t_i,t_j)$ y el vector $f_i=f(t_i)$.
> 3. **Resuelve** el sistema lineal denso $(\mathsf{I}-\lambda\mathsf{A})\boldsymbol\varphi=\mathbf{f}$
>    por eliminación gaussiana (coste $O(N^3)$).
> 4. **Reconstruye** $\varphi$ en cualquier $x$ con la interpolante de Nyström
>    $\varphi(x)=f(x)+\lambda\sum_j w_j K(x,t_j)\varphi_j$.

> [!proposicion]
> Si $K$ es **simétrico** ($K(x,t)=K(t,x)$) y se usan pesos $w_j>0$, la matriz $\mathsf{A}$ es
> **similar** a una simétrica (vía la transformación $\widetilde{\mathsf{A}}=\mathsf{W}^{1/2}\mathsf{A}\mathsf{W}^{-1/2}$
> con $\mathsf{W}=\operatorname{diag}(w_j)$). Sus **autovalores** son reales y aproximan los inversos de
> las [[Raices Caracteristicas y Funciones Propias| raíces características]] del núcleo: Nyström también
> sirve para **estimar el espectro** (compárese con [[Raices Caracteristicas Aproximadas| Ritz, trazas y Kellog]]).

> [!info] Por qué es el método estándar
> Nyström no requiere elegir ni integrar funciones base: solo **evaluar el núcleo** en pares de nodos.
> Eso lo hace directo de programar y muy preciso con Gauss para núcleos suaves; por ello domina en BEM,
> acústica y dispersión. Su talón de Aquiles es que la matriz es **llena** ($O(N^2)$ memoria,
> $O(N^3)$ resolución), lo que en problemas grandes se mitiga con métodos rápidos (FMM, matrices
> jerárquicas) que aceleran el producto matriz–vector.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Idea | sustituir $\int K\varphi$ por cuadratura $\sum_j w_j K(x,t_j)\varphi_j$ |
> | Sistema | $(\mathsf{I}-\lambda\mathsf{A})\boldsymbol\varphi=\mathbf{f}$, $\mathsf{A}_{ij}=w_jK(t_i,t_j)$ |
> | Incógnitas | valores nodales $\varphi_i=\varphi(t_i)$ |
> | Interpolación | $\varphi(x)=f(x)+\lambda\sum_j w_j K(x,t_j)\varphi_j$ |
> | Convergencia | la de la cuadratura (espectral con Gauss si $K$ es suave) |
> | Matriz | **llena**; $O(N^2)$ memoria, $O(N^3)$ resolver |

> [!corolario]
> Nyström es "resolver la integral con una regla de cuadratura y pedir que la ecuación se cumpla en los
> nodos". Su elegancia está en la **interpolación**: la misma fórmula que discretiza la integral extiende
> la solución a todo el intervalo sin perder orden. Por simplicidad y precisión es el caballo de batalla
> numérico para [[Fredholm Segunda Especie| Fredholm de 2ª especie]] con núcleos suaves.

> [!referencia]
> - La proyección por puntos hermana: [[Metodo de Colocacion]].
> - Aproximar el núcleo en vez de la integral: [[Sustitucion Nucleo Degenerado]].
> - Panorama de los métodos: [[Metodos Aproximados/index]].
