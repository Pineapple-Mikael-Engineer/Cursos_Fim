---
title: Tensor de Inercia
tags:
  - dinamica
  - teoria
  - inercia
draft: false
aliases:
  - tensor de inercia
  - momentos de inercia
  - productos de inercia
  - convención de signo de inercia
  - inertia tensor
---

# Tensor de Inercia $\;I_{ij}=\int(r^2\delta_{ij}-r_i r_j)\,dm$

> [!definicion]
> El **tensor de inercia** respecto a un punto es la matriz simétrica $3\times3$
> $$\mathbf I=\begin{pmatrix} I_{xx} & I_{xy} & I_{xz}\\ I_{xy} & I_{yy} & I_{yz}\\ I_{xz} & I_{yz} & I_{zz}\end{pmatrix},\qquad I_{ij}=\int(r^2\delta_{ij}-r_i r_j)\,dm,$$
> cuya **diagonal** son los **momentos de inercia** ($I_{xx}=\int(y^2+z^2)\,dm$, …) y cuyos elementos
> **fuera de la diagonal** son los **productos de inercia** ($I_{xy}=-\int xy\,dm$, …). En forma
> compacta, con el segundo momento $Q_{ij}=\int r_i r_j\,dm$: $\ \mathbf I=\mathrm{Tr}(\mathbf Q)\,\mathbb 1-\mathbf Q$.

> [!info]
> El objeto central de la [[3 Inercia/index | inercia]] ([[Dinamica/index | Dinámica]]). De él salen
> $\vec H$, $T$ y $\vec\tau$ (→ [[Deducciones/index | Deducciones]]); se diagonaliza en
> [[Ejes Principales de Inercia | ejes principales]] y se traslada con el
> [[Teorema del Eje Paralelo | eje paralelo]]. Referencia: Goldstein §5.3.

---

## Ejemplo

> [!ejemplo]
> **Tensor de dos masas puntuales (aparece un producto de inercia).**
>
> Dos masas $m$ en $(a,a,0)$ y $(-a,-a,0)$. Hallar su tensor de inercia respecto al origen.
>
> ![[cuerpo_inercia.svg|460]]
>
> *Cada masa $dm$ a posición $\vec r$ aporta $r^2\delta_{ij}-r_ir_j$; aquí la suma sustituye a la
> integral.*
>
> **Diagonal.** $I_{xx}=\sum m(y^2+z^2)=m a^2+m a^2=2ma^2$; igual $I_{yy}=2ma^2$;
> $I_{zz}=\sum m(x^2+y^2)=2(m\cdot2a^2)=4ma^2$.
> **Productos.** $I_{xy}=-\sum m\,xy=-\big(m\,a^2+m\,a^2\big)=-2ma^2$; $I_{xz}=I_{yz}=0$ (todo $z=0$).
>
> > [!solucion]
> > $$\mathbf I=ma^2\begin{pmatrix} 2 & -2 & 0\\ -2 & 2 & 0\\ 0 & 0 & 4\end{pmatrix}.$$
> > El producto $I_{xy}\neq0$ indica que la masa está **mal alineada** con los ejes $x,y$: éstos **no**
> > son principales (lo serían las diagonales del cuadrado).

---

## En qué consiste

> [!teoria] Qué mide cada elemento
> - **Momentos de inercia** (diagonal): $I_{xx}=\int(y^2+z^2)\,dm$ mide la **resistencia a rotar**
>   alrededor del eje $x$ (cuánta masa hay lejos de ese eje).
> - **Productos de inercia** (fuera): $I_{xy}=-\int xy\,dm$ mide el **acoplamiento** entre los ejes
>   $x$ e $y$; es nulo si la distribución es simétrica respecto a un plano coordenado.
>
> La forma compacta $\mathbf I=\mathrm{Tr}(\mathbf Q)\,\mathbb 1-\mathbf Q$ con $Q_{ij}=\int r_ir_j\,dm$
> evita errores de signo: define el tensor **sin ambigüedad**.

> [!warning] Las dos convenciones de signo (no mezclarlas)
> Hay dos notaciones que confunden:
> - **Componentes del tensor** (la de este curso): $I_{xy}=-\int xy\,dm$ **ya lleva el signo**, y la
>   matriz se escribe **directa** con los $I_{ij}$, sin signos extra.
> - **Productos de ingeniería:** $P_{xy}=\int xy\,dm$ (sin signo), y entonces la matriz lleva
>   $-P_{xy}$ fuera de la diagonal.
>
> La relación es $I_{xy}=-P_{xy}$. El error clásico es usar $I_{xy}=-\int xy\,dm$ **y además** poner un
> signo en la matriz: se aplica el menos **dos veces**. Regla: **una convención y mantenerla**; en
> caso de duda, trabajar con $Q_{ij}$ y $\mathbf I=\mathrm{Tr}(\mathbf Q)\mathbb 1-\mathbf Q$.

> [!proposicion] Propiedades estructurales
> - **Simétrico:** $I_{ij}=I_{ji}$, luego es **diagonalizable** por rotación ortogonal
>   ([[Ejes Principales de Inercia | ejes principales]]).
> - **Definido positivo:** $\vec\omega\cdot\mathbf I\vec\omega=2T_{rot}>0$ para todo $\vec\omega\neq\vec0$
>   (la energía de rotación es positiva).
> - **Depende del punto y de la orientación** de los ejes, no del estado de movimiento: es pura
>   geometría de masas.

> [!warning]
> $\mathbf I$ depende del **punto** de referencia (usar el [[Teorema del Eje Paralelo]] para cambiarlo)
> y de la **orientación** de los ejes. No confundir el **tensor de inercia de masa** ($dm$, para
> rotación) con el **momento de inercia de área** ($dA$, para flexión de vigas):
> ver [[Momentos de Inercia de Figuras]].

## Resumen

> [!resumen]
> | Elemento | Fórmula | Significado |
> |:---|:---|:---|
> | Momento $I_{xx}$ | $\int(y^2+z^2)\,dm$ | resistencia a rotar (eje $x$) |
> | Producto $I_{xy}$ | $-\int xy\,dm$ | acoplamiento $x$–$y$ |
> | Forma compacta | $\mathbf I=\mathrm{Tr}(\mathbf Q)\mathbb 1-\mathbf Q$ | $Q_{ij}=\int r_ir_j\,dm$ |
> | Propiedades | simétrico, definido positivo | diagonalizable |

> [!corolario]
> El tensor de inercia resume en seis números (3 momentos + 3 productos) toda la distribución de masa
> relevante para la rotación. Elegir bien los ejes —los principales— anula los productos y simplifica
> todo lo que sigue.

> [!referencia]
> Goldstein §5.3. Diagonalización: [[Ejes Principales de Inercia]]. Cambio de punto:
> [[Teorema del Eje Paralelo]]. Lo que produce: [[Deducciones/index]].
