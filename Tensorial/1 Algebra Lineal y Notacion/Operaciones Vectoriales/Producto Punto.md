---
title: Producto Punto
tags:
  - analisis-tensorial
  - teoria
  - notacion-indices
  - producto-punto
draft: false
aliases:
  - producto punto
  - producto escalar
  - producto interno
  - dot product
  - scalar product
---

# Producto Punto $\vec{A}\cdot\vec{B}=A_iB_i$

> [!definicion]
> El **producto punto** (o escalar) de dos vectores es el **escalar**
> $$\vec{A}\cdot\vec{B}=\lvert\vec{A}\rvert\,\lvert\vec{B}\rvert\cos\theta,$$
> con $\theta$ el ángulo entre ambos. En cartesianas ortonormales, usando $\hat{e}_i\cdot\hat{e}_j=\delta_{ij}$, colapsa a una suma simple:
> $$\vec{A}\cdot\vec{B}=A_iB_j\,(\hat{e}_i\cdot\hat{e}_j)=A_iB_j\,\delta_{ij}=A_iB_i,\qquad \vec{A}\cdot\vec{A}=\lvert\vec{A}\rvert^2.$$

> [!info]
> Es la mitad "punto" de la operación 1.2.2 del libro, dentro de [[index | Operaciones Vectoriales]] del [[../index | capítulo 1]]. Introduce la [[Simbolos Especiales/Delta Kronecker | delta de Kronecker]] $\delta_{ij}$ a través de $\hat{e}_i\cdot\hat{e}_j=\delta_{ij}$. Su hermano vectorial es el [[Producto Cruz | producto cruz]]; ambos se comparan en [[Productos Vectoriales]]. Su uso combinado para derivar identidades se ve en [[Calculos con Notacion Einstein]].

---

## Ejemplo

> [!ejemplo]
> **Producto punto numérico.** Sean $\vec{A}=(1,2,3)$ y $\vec{B}=(4,5,6)$. Usando $\vec{A}\cdot\vec{B}=A_iB_i$ (suma sobre $i=1,2,3$):
> $$\vec{A}\cdot\vec{B}=A_1B_1+A_2B_2+A_3B_3=1\cdot4+2\cdot5+3\cdot6=4+10+18=32.$$
> Como caso particular, $\vec{A}\cdot\vec{A}=1+4+9=14=\lvert\vec{A}\rvert^2$, de modo que $\lvert\vec{A}\rvert=\sqrt{14}$.

> [!ejemplo]
> **Ángulo entre dos vectores.** Despejando $\cos\theta$ de la definición geométrica, $\cos\theta=\dfrac{\vec{A}\cdot\vec{B}}{\lvert\vec{A}\rvert\,\lvert\vec{B}\rvert}$. Para $\vec{A}=(1,0,0)$ y $\vec{B}=(1,1,0)$:
> $$\vec{A}\cdot\vec{B}=1\cdot1+0\cdot1+0\cdot0=1,\qquad \lvert\vec{A}\rvert=1,\qquad \lvert\vec{B}\rvert=\sqrt{2}.$$
> $$\cos\theta=\frac{1}{1\cdot\sqrt{2}}=\frac{1}{\sqrt{2}}\;\Longrightarrow\;\theta=45^\circ.$$
> El producto punto es la vía estándar para medir ángulos sin trigonometría explícita.

> [!ejemplo]
> **Proyección escalar.** La componente de $\vec{A}$ en la dirección de $\vec{B}$ (proyección escalar) es
> $$A_{\parallel}=\lvert\vec{A}\rvert\cos\theta=\frac{\vec{A}\cdot\vec{B}}{\lvert\vec{B}\rvert}=\vec{A}\cdot\hat{B},\qquad \hat{B}=\frac{\vec{B}}{\lvert\vec{B}\rvert}.$$
> Para $\vec{A}=(3,4,0)$ y $\vec{B}=(1,0,0)$: $\vec{A}\cdot\vec{B}=3$, $\lvert\vec{B}\rvert=1$, luego $A_{\parallel}=3$ (la sombra de $\vec{A}$ sobre el eje $x$). El **vector** proyección es $\vec{A}_{\parallel}=(\vec{A}\cdot\hat{B})\,\hat{B}=(3,0,0)$.
>
> ![[proyeccion_escalar.svg]]

---

## En qué consiste

> [!teoria]
> El producto punto entre $\vec{A}$ y $\vec{B}$ es el escalar $\vec{A}\cdot\vec{B}=\lvert\vec{A}\rvert\lvert\vec{B}\rvert\cos\theta$, con $\theta$ el ángulo entre ambos. Geométricamente mide cuánto "se solapan" las direcciones: máximo cuando son paralelos ($\theta=0$), cero cuando son perpendiculares ($\theta=90^\circ$), negativo cuando apuntan en sentidos opuestos. Con $\vec{A}\cdot\vec{A}$ se recupera la magnitud al cuadrado, $\vec{A}\cdot\vec{A}=\lvert\vec{A}\rvert^2$, base de toda definición de longitud.

> [!teorema] Producto punto en índices
> En cartesianas ortonormales, el producto punto se reduce a la contracción de las componentes:
> $$\vec{A}\cdot\vec{B}=A_iB_j\,(\hat{e}_i\cdot\hat{e}_j)=A_iB_j\,\delta_{ij}=A_iB_i.$$

> [!demostracion]
> **Paso 1 — Expandir en componentes.** Escribiendo $\vec{A}=A_i\hat{e}_i$ y $\vec{B}=B_j\hat{e}_j$ con índices **distintos** ($i\neq j$ como letras) para mantener las dos sumas independientes, y usando la bilinealidad del producto punto:
> $$\vec{A}\cdot\vec{B}=(A_i\hat{e}_i)\cdot(B_j\hat{e}_j)=A_iB_j\,(\hat{e}_i\cdot\hat{e}_j).$$
> Las componentes $A_i,B_j$ son números y salen del producto; queda el producto de las bases $\hat{e}_i\cdot\hat{e}_j$.
>
> **Paso 2 — Ortonormalidad de la base.** En cartesianas los vectores base son ortonormales, lo que se codifica exactamente con la delta de Kronecker:
> $$\hat{e}_i\cdot\hat{e}_j=\delta_{ij}=\begin{cases}1 & i=j\\ 0 & i\neq j\end{cases}\;\Longrightarrow\;\vec{A}\cdot\vec{B}=A_iB_j\,\delta_{ij}.$$
>
> **Paso 3 — Contraer la delta.** La $\delta_{ij}$ anula todo término con $i\neq j$ y sustituye un índice por el otro (propiedad de sustitución $A_iB_j\delta_{ij}=A_iB_i$):
> $$\vec{A}\cdot\vec{B}=A_iB_j\,\delta_{ij}=A_1B_1+A_2B_2+A_3B_3=A_iB_i.\qquad\blacksquare$$
> El producto punto colapsa de una doble suma ($9$ términos en 3D) a una suma simple ($3$ términos) gracias a $\hat{e}_i\cdot\hat{e}_j=\delta_{ij}$.

> [!proposicion] Propiedades
> | Propiedad | Expresión |
> |---|---|
> | Magnitud | $\vec{A}\cdot\vec{A}=A_iA_i=\lvert\vec{A}\rvert^2\ge0$ |
> | Conmutativa | $\vec{A}\cdot\vec{B}=\vec{B}\cdot\vec{A}$ (pues $A_iB_i=B_iA_i$) |
> | Distributiva | $\vec{A}\cdot(\vec{B}+\vec{C})=\vec{A}\cdot\vec{B}+\vec{A}\cdot\vec{C}$ |
> | Homogeneidad | $(\lambda\vec{A})\cdot\vec{B}=\lambda\,(\vec{A}\cdot\vec{B})$ |
> | Perpendicularidad | $\vec{A}\cdot\vec{B}=0\;\Leftrightarrow\;\vec{A}\perp\vec{B}$ (con $\vec{A},\vec{B}\neq0$) |
>
> La conmutatividad es inmediata en índices: $A_iB_i$ es un producto de números, su orden no altera la suma. La perpendicularidad sale de $\cos90^\circ=0$ en la forma geométrica.

> [!info] Aparición física
> El producto punto da la parte de un vector "a favor" de otro, por lo que mide **trabajo**: la fuerza $\vec{F}$ sobre un desplazamiento $d\vec{r}$ realiza
> $$W=\int d\vec{r}\cdot\vec{F},$$
> y solo la componente de $\vec{F}$ paralela al movimiento contribuye (una fuerza perpendicular no trabaja). También aparece en el flujo $\vec{E}\cdot d\vec{A}$ y en la energía $\tfrac12 m\,\vec{v}\cdot\vec{v}$.

## Resumen

> [!resumen]
> | Aspecto | Expresión |
> |---|---|
> | Definición geométrica | $\vec{A}\cdot\vec{B}=\lvert\vec{A}\rvert\lvert\vec{B}\rvert\cos\theta$ |
> | Forma en índices | $A_iB_j\delta_{ij}=A_iB_i$ |
> | Tipo de resultado | escalar |
> | Magnitud | $\vec{A}\cdot\vec{A}=A_iA_i=\lvert\vec{A}\rvert^2$ |
> | Ángulo | $\cos\theta=\dfrac{\vec{A}\cdot\vec{B}}{\lvert\vec{A}\rvert\lvert\vec{B}\rvert}$ |
> | Nulo $\Leftrightarrow$ | $\vec{A}\perp\vec{B}$ |
> | Caso físico | trabajo $W=\int d\vec{r}\cdot\vec{F}$ |

> [!corolario]
> El producto punto colapsa por $\hat{e}_i\cdot\hat{e}_j=\delta_{ij}$ a la suma $A_iB_i$: una doble suma de bases se reduce a una simple. Es la operación que mide longitudes, ángulos y proyecciones, y la primera aparición de la delta de Kronecker como "contractor" de índices.

> [!referencia]
> - Delta de Kronecker y su propiedad de sustitución: [[Simbolos Especiales/Delta Kronecker]].
> - Operación hermana (vectorial): [[Producto Cruz]].
> - Comparativa punto vs cruz: [[Productos Vectoriales]].
> - Derivaciones que lo usan (invariancia de magnitud): [[Calculos con Notacion Einstein]].
