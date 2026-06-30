---
title: Momento Angular Orbital
order: 2
tags:
  - analisis-tensorial
  - teoria
  - teoria-grupos
  - momento-angular
draft: false
aliases:
  - momento angular
  - operadores de subida y bajada
  - operadores escalera
  - orbital angular momentum
  - ladder operators
---

# Momento Angular Orbital $\vec J,\ J_\pm$

> [!definicion]
> El **momento angular cuántico** es el operador $\vec L=-i\,\vec r\times\vec\nabla$ (con $\hbar=1$), cuyas componentes cumplen las **relaciones de conmutación**
> $$[L_i,L_j]=i\varepsilon_{ijk}L_k,\qquad [\vec L^2,L_i]=0,\qquad \vec L^2=L_x^2+L_y^2+L_z^2.$$
> Estas relaciones **definen** un momento angular. Un momento angular general $\vec J$ (Hermítico, $[J_i,J_j]=i\varepsilon_{ijk}J_k$) tiene autoestados simultáneos $|JM\rangle$ de $J_z$ y $\vec J^2$ con $\vec J^2=J(J+1)$ y $-J\le M\le +J$, construidos con los **operadores de subida y bajada** $J_\pm=J_x\pm iJ_y$.

> [!info]
> Sección **7.3** del [[index | capítulo 7]] (libro, cap. 7.3). El momento angular orbital es el ejemplo físico estrella del paso **álgebra de Lie $\Rightarrow$ espectro cuantizado**: a partir de los [[Generadores de Grupos Continuos | generadores]] de $SO(3)$ y sus conmutadores se deduce, sin resolver ninguna ecuación diferencial, que el momento angular está **cuantizado**. El mismo álgebra describe el spin (donde $J$ puede ser semientero) y se reusa en el [[Grupo Homogeneo de Lorentz | grupo de Lorentz]]. El producto cruz $\vec r\times\vec\nabla$ usa el [[1 Algebra Lineal y Notacion/Simbolos Especiales/Simbolo Levi-Civita | símbolo de Levi-Civita]].

---

## Ejemplo

> [!ejemplo]
> **El triplete $J=1$ ($M=-1,0,1$).** Aplicar subida y bajada a $|1,0\rangle$ con
> $$J_\pm|JM\rangle=\sqrt{(J\mp M)(J\pm M+1)}\;|J,M\pm1\rangle.$$
>
> **Subida** $J_+|1,0\rangle$, con $J=1,\ M=0$:
> $$\sqrt{(J-M)(J+M+1)}=\sqrt{(1-0)(1+0+1)}=\sqrt{2}\ \Rightarrow\ J_+|1,0\rangle=\sqrt{2}\,|1,1\rangle.$$
>
> **Bajada** $J_-|1,0\rangle$, con $J=1,\ M=0$:
> $$\sqrt{(J+M)(J-M+1)}=\sqrt{(1+0)(1-0+1)}=\sqrt{2}\ \Rightarrow\ J_-|1,0\rangle=\sqrt{2}\,|1,-1\rangle.$$
>
> **En los topes el coeficiente se anula**, como debe: $J_+|1,1\rangle=\sqrt{(1-1)(1+1+1)}\,|1,2\rangle=0$ (no hay $M=2$) y $J_-|1,-1\rangle=\sqrt{(1-1)(1+1+1)}\,|1,-2\rangle=0$. La escalera empieza y termina sola.
>
> Tabla de coeficientes del triplete (el factor que multiplica al ket destino):
>
> | Estado $\|JM\rangle$ | $J_+$ sube a | coef. | $J_-$ baja a | coef. |
> |:---:|:---:|:---:|:---:|:---:|
> | $\|1,-1\rangle$ | $\|1,0\rangle$ | $\sqrt{2}$ | — | $0$ |
> | $\|1,0\rangle$ | $\|1,1\rangle$ | $\sqrt{2}$ | $\|1,-1\rangle$ | $\sqrt{2}$ |
> | $\|1,1\rangle$ | — | $0$ | $\|1,0\rangle$ | $\sqrt{2}$ |

---

## En qué consiste

> [!teoria]
> Se trabaja con un momento angular **general** $\vec J$ Hermítico que satisface
> $$[J_i,J_j]=i\varepsilon_{ijk}J_k,\qquad [\vec J^2,J_i]=0.$$
> $\vec J$ puede ser orbital $\vec L$, spin $\vec\sigma/2$, o la suma $\vec L+\vec\sigma/2$, etc. Como $\vec J^2$ conmuta con $J_z$, ambos tienen **autoestados simultáneos** $|JM\rangle$:
> $$J_z|JM\rangle=M|JM\rangle,\qquad \vec J^2|JM\rangle=\lambda|JM\rangle.$$
> Todo el espectro se obtiene del álgebra, sin elegir representación.

> [!definicion] Operadores de subida y bajada
> $$J_+=J_x+iJ_y,\qquad J_-=J_x-iJ_y.$$
> De las relaciones de conmutación de $\vec J$ se siguen:
> $$[J_z,J_+]=+J_+,\qquad [J_z,J_-]=-J_-,\qquad [J_+,J_-]=2J_z,$$
> y dos reescrituras de $\vec J^2$ que serán la clave de la demostración:
> $$\vec J^2=\tfrac12(J_+J_-+J_-J_+)+J_z^2=J_-J_++J_z(J_z+1)=J_+J_--J_z(J_z-1).$$

> [!proposicion] Por qué "suben" y "bajan"
> $J_\pm$ conserva $\lambda$ (porque $[\vec J^2,J_\pm]=0$) y **cambia $M$ en $\pm1$**. En efecto, usando $J_zJ_+=J_+(J_z+1)$:
> $$J_z\big(J_+|JM\rangle\big)=J_+(J_z+1)|JM\rangle=(M+1)\,J_+|JM\rangle.$$
> Luego $J_+|JM\rangle$ es autoestado de $J_z$ con autovalor $M+1$ (**sube**); análogamente $J_-$ da $M-1$ (**baja**).

> [!teorema] Espectro del momento angular
> Para todo momento angular $\vec J$ Hermítico:
> $$\boxed{\ \lambda=J(J+1),\qquad -J\le M\le +J\ }$$
> con $M$ variando de $-J$ a $+J$ en **pasos enteros**.

> [!demostracion]
> **Paso 1 — $J_\pm$ conserva $\lambda$.** Como $\vec J^2$ conmuta con cada $J_i$, conmuta con $J_\pm=J_x\pm iJ_y$. Entonces
> $$\vec J^2\big(J_\pm|JM\rangle\big)=J_\pm\big(\vec J^2|JM\rangle\big)=\lambda\big(J_\pm|JM\rangle\big),$$
> así toda la escalera $\{\dots,J_-|JM\rangle,|JM\rangle,J_+|JM\rangle,\dots\}$ comparte el **mismo** $\lambda$; solo cambia $M$ (Paso anterior).
>
> **Paso 2 — $M$ está acotado.** Tomando el valor esperado de $\vec J^2-J_z^2=J_x^2+J_y^2$ y usando $J_x^\dagger=J_x$, $J_y^\dagger=J_y$:
> $$\langle JM|\,\vec J^2-J_z^2\,|JM\rangle=\langle JM|J_x^2+J_y^2|JM\rangle=\|J_x|JM\rangle\|^2+\|J_y|JM\rangle\|^2\ge0.$$
> Por tanto $\lambda-M^2\ge0$: para $\lambda$ fijo, $M$ no puede crecer indefinidamente. **Existe un $M$ máximo**, llámese $J$.
>
> **Paso 3 — tope superior: $J_+|JJ\rangle=0$.** Si hubiera estado por encima de $M=J$, sería $J_+|JJ\rangle$ con $M=J+1>J$, contradiciendo que $J$ es el máximo. Luego $J_+|JJ\rangle=0$, y también $J_-J_+|JJ\rangle=0$.
>
> **Paso 4 — valor de $\lambda$.** Con la reescritura $\vec J^2=J_-J_++J_z(J_z+1)$ aplicada a $|JJ\rangle$:
> $$0=J_-J_+|JJ\rangle=\big(\vec J^2-J_z^2-J_z\big)|JJ\rangle=(\lambda-J^2-J)|JJ\rangle,$$
> de donde $\lambda-J^2-J=0$, es decir
> $$\lambda=J(J+1)\ge0.$$
>
> **Paso 5 — tope inferior.** Sea $J'$ el **mínimo** $M$. Por el mismo argumento $J_-|JJ'\rangle=0$, y con $\vec J^2=J_+J_--J_z(J_z-1)$:
> $$0=J_+J_-|JJ'\rangle=(\lambda+J'-J'^2)|JJ'\rangle\ \Rightarrow\ \lambda=J'(J'-1).$$
> Igualando con el Paso 4, $J(J+1)=J'(J'-1)=(-J)(-J-1)$, cuya solución física es $J'=-J$.
>
> **Paso 6 — la escalera es entera.** Partiendo de $|JJ\rangle$ y aplicando $J_-$ repetidas veces se llega exactamente a $|J,-J\rangle$; los autovalores recorren $J,\,J-1,\dots,-J$. Como cada paso resta $1$, el descenso de $+J$ a $-J$ es entero:
> $$-J\le M\le +J,\qquad M\in\{-J,-J+1,\dots,J-1,J\}.\qquad\blacksquare$$

> [!proposicion] Normalización
> Eligiendo la raíz positiva y sin factor de fase, las ecuaciones $J_\mp J_\pm|JM\rangle=(J\mp M)(J\pm M+1)|JM\rangle$ dan
> $$J_\pm|JM\rangle=\sqrt{(J\mp M)(J\pm M+1)}\;|J,M\pm1\rangle.$$
> En los extremos el radicando se anula: $J_+|JJ\rangle=0$ y $J_-|J,-J\rangle=0$, cerrando la escalera.

> [!teoria] Cuantización
> Como $M$ va de $-J$ a $+J$ en pasos de $1$, hay $2J+1$ valores y **$2J$ es entero**. Por tanto
> $$J=0,\tfrac12,1,\tfrac32,2,\dots\quad(\text{entero o semientero}).$$
> El **momento angular orbital** $\vec L$ tiene $J=\ell$ **entero**; el **spin** de partículas fundamentales y núcleos puede ser semientero ($\tfrac12,\tfrac32,\dots$). La cuantización es una consecuencia pura de las relaciones de conmutación, no de la dinámica. En [[3 Coordenadas Curvilineas/Sistema Esferico/index | coordenadas esféricas]] los autoestados orbitales son los **armónicos esféricos**:
> $$\langle\theta,\varphi|\ell m\rangle=Y_\ell^m(\theta,\varphi).$$

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |:---|:---|
> | Definición | $\vec L=-i\,\vec r\times\vec\nabla$; $[L_i,L_j]=i\varepsilon_{ijk}L_k$ |
> | Casimir | $\vec J^2\|JM\rangle=J(J+1)\|JM\rangle$, $J_z\|JM\rangle=M\|JM\rangle$ |
> | Escalera | $J_\pm=J_x\pm iJ_y$; $[J_z,J_\pm]=\pm J_\pm$, $[J_+,J_-]=2J_z$ |
> | Acción | $J_\pm$ conserva $J$, lleva $M\to M\pm1$ |
> | Normalización | $J_\pm\|JM\rangle=\sqrt{(J\mp M)(J\pm M+1)}\,\|J,M\pm1\rangle$ |
> | Rango | $-J\le M\le +J$, en $2J+1$ pasos enteros |
> | Cuantización | $J$ entero (orbital) o semientero (spin) |
> | Esféricas | $\langle\theta,\varphi\|\ell m\rangle=Y_\ell^m(\theta,\varphi)$ |

> [!corolario]
> Todo el espectro del momento angular sale del **álgebra** $[J_i,J_j]=i\varepsilon_{ijk}J_k$, sin resolver ecuaciones diferenciales: los operadores de subida y bajada $J_\pm$ generan la escalera de estados $|JM\rangle$, el tope $J_+|JJ\rangle=0$ fija $\lambda=J(J+1)$, y la condición de cerrar la escalera en pasos enteros impone que **$2J$ sea entero**. Esta es la potencia de las técnicas de operadores: la simetría (los [[Generadores de Grupos Continuos | generadores]] de $SO(3)$/$SU(2)$) dicta directamente la cuantización física.

> [!referencia]
> - Generadores y álgebra de Lie de donde sale $[J_i,J_j]=i\varepsilon_{ijk}J_k$: [[Generadores de Grupos Continuos]].
> - Producto cruz $\vec r\times\vec\nabla$ y $\varepsilon_{ijk}$: [[1 Algebra Lineal y Notacion/Simbolos Especiales/Simbolo Levi-Civita]].
> - Armónicos esféricos y coordenadas: [[3 Coordenadas Curvilineas/Sistema Esferico/index]].
> - Marco del capítulo: [[index | Teoría de Grupo]].
