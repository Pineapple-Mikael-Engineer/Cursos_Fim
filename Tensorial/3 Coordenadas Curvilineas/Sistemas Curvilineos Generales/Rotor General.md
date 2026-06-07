---
title: Rotor en Coordenadas Curvilíneas
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-curvilineas
  - rotor
draft: false
aliases:
  - rotor general
  - rotor curvilineo
  - nabla cruz A curvilineo
  - rotacional general
  - general curl
  - curvilinear curl
---

# Rotor en Coordenadas Curvilíneas $\vec\nabla\times\vec A$

> [!definicion]
> En un sistema curvilíneo ortogonal $(q_1,q_2,q_3)$ con factores de escala $h_i$, el **rotor** de un campo vectorial $\vec A=A_i\,\hat q_i$ se escribe como determinante
> $$\vec\nabla\times\vec A=\frac{1}{h_1h_2h_3}\begin{vmatrix}h_1\hat q_1 & h_2\hat q_2 & h_3\hat q_3\\[2pt] \dfrac{\partial}{\partial q_1} & \dfrac{\partial}{\partial q_2} & \dfrac{\partial}{\partial q_3}\\[6pt] h_1A_1 & h_2A_2 & h_3A_3\end{vmatrix}=\frac{\varepsilon_{ijk}}{h_jh_k}\frac{\partial(h_kA_k)}{\partial q_j}\,\hat q_i,$$
> con la primera componente
> $$[\vec\nabla\times\vec A]_1=\frac{1}{h_2h_3}\left[\frac{\partial(h_3A_3)}{\partial q_2}-\frac{\partial(h_2A_2)}{\partial q_3}\right]$$
> y las otras dos por permutación cíclica $1\to2\to3\to1$.

> [!info]
> Sección **3.4.10** del libro, dentro de [[index | sistemas curvilíneos generales]]. Como la [[Divergencia General | divergencia]], se deduce de su **definición integral** (circulación por unidad de área), no de una comparación diferencial. Las componentes que aparecen dentro de las derivadas son $h_kA_k$ (longitud física por unidad de coordenada a lo largo de cada arista). Reutiliza el desplazamiento $d\vec r=h_i\,dq_i\,\hat q_i$ y la geometría del lazo de [[Geometria Diferencial Local]]. Recupera el [[Rotor | rotor cartesiano]] cuando $h_i=1$.

---

## Ejemplo

> [!ejemplo]
> **Recuperar el rotor cilíndrico.** Cilíndrico $(\rho,\phi,z)$, con $h_\rho=1,\ h_\phi=\rho,\ h_z=1$ y $h_1h_2h_3=\rho$. El determinante es
> $$\vec\nabla\times\vec A=\frac{1}{\rho}\begin{vmatrix}\hat q_\rho & \rho\,\hat q_\phi & \hat q_z\\[2pt] \dfrac{\partial}{\partial\rho} & \dfrac{\partial}{\partial\phi} & \dfrac{\partial}{\partial z}\\[6pt] A_\rho & \rho A_\phi & A_z\end{vmatrix}.$$
> Desarrollando por la primera fila se obtienen las tres componentes:
> $$[\vec\nabla\times\vec A]_\rho=\frac{1}{\rho}\frac{\partial A_z}{\partial\phi}-\frac{\partial A_\phi}{\partial z},\qquad
> [\vec\nabla\times\vec A]_\phi=\frac{\partial A_\rho}{\partial z}-\frac{\partial A_z}{\partial\rho},$$
> $$[\vec\nabla\times\vec A]_z=\frac{1}{\rho}\left[\frac{\partial(\rho A_\phi)}{\partial\rho}-\frac{\partial A_\rho}{\partial\phi}\right].$$
> Con $h_i=1$ el determinante colapsa al rotor cartesiano $\varepsilon_{ijk}\,\partial_jA_k\,\hat e_i$.

---

## Demostración

> [!teorema]
> Para todo campo vectorial $\vec A$ diferenciable, la primera componente del rotor es
> $$[\vec\nabla\times\vec A]_1=\frac{1}{h_2h_3}\left[\frac{\partial(h_3A_3)}{\partial q_2}-\frac{\partial(h_2A_2)}{\partial q_3}\right],$$
> y las restantes se obtienen por permutación cíclica de los índices.

> [!demostracion]
> Se parte de la **definición integral** del rotor proyectado sobre una superficie (circulación por unidad de área), con el sentido de $d\vec\sigma$ fijado por la regla de la mano derecha respecto al contorno $C$:
> $$\vec\nabla\times\vec A\cdot d\vec\sigma=\lim_{C\to0}\oint_C d\vec r\cdot\vec A.$$
>
> **Paso 1 — orientar la cara según $\hat q_1$.** Se elige el lazo $C$ sobre la cara $\perp\hat q_1$, de modo que $d\vec\sigma=h_2h_3\,dq_2\,dq_3\,\hat q_1$. El lado izquierdo aísla entonces la primera componente:
> $$\vec\nabla\times\vec A\cdot d\vec\sigma=h_2h_3\,dq_2\,dq_3\,[\vec\nabla\times\vec A]_1.$$
>
> **Paso 2 — partir el contorno en cuatro tramos.** El lazo rectangular se recorre por $C_a,C_b,C_c,C_d$. Con $d\vec r=h_i\,dq_i\,\hat q_i$, solo aportan las componentes a lo largo de las aristas:
> $$\oint_C d\vec r\cdot\vec A=\int_{C_a}\!h_2A_2\,dq_2+\int_{C_b}\!h_3A_3\,dq_3+\int_{C_c}\!h_2A_2\,dq_2+\int_{C_d}\!h_3A_3\,dq_3.$$
>
> **Paso 3 — par de tramos $C_a,C_c$ (dirección $q_2$).** El tramo $C_a$ está en $q_3$ y se recorre en $+q_2$; el opuesto $C_c$ está en $q_3+dq_3$ y se recorre en $-q_2$:
> $$\int_{C_a}h_2A_2\,dq_2=(h_2A_2)\big|_{q_3}\,dq_2,\qquad\int_{C_c}h_2A_2\,dq_2=-(h_2A_2)\big|_{q_3+dq_3}\,dq_2.$$
> Por Taylor, $(h_2A_2)\big|_{q_3+dq_3}=(h_2A_2)\big|_{q_3}+\dfrac{\partial(h_2A_2)}{\partial q_3}\,dq_3$, y sumando el par el término constante se cancela:
> $$\int_{C_a+C_c}d\vec r\cdot\vec A=-\frac{\partial(h_2A_2)}{\partial q_3}\,dq_2\,dq_3.$$
>
> **Paso 4 — par de tramos $C_b,C_d$ (dirección $q_3$).** De manera análoga, $C_b$ está en $q_2+dq_2$ (sentido $+q_3$) y $C_d$ en $q_2$ (sentido $-q_3$); tras Taylor en $q_2$,
> $$\int_{C_b+C_d}d\vec r\cdot\vec A=+\frac{\partial(h_3A_3)}{\partial q_2}\,dq_2\,dq_3.$$
>
> **Paso 5 — circulación total e identificación.** Sumando los dos pares,
> $$\oint_C d\vec r\cdot\vec A=\left[\frac{\partial(h_3A_3)}{\partial q_2}-\frac{\partial(h_2A_2)}{\partial q_3}\right]dq_2\,dq_3.$$
> Igualando con el lado izquierdo del Paso 1 y cancelando $dq_2\,dq_3$:
> $$[\vec\nabla\times\vec A]_1=\frac{1}{h_2h_3}\left[\frac{\partial(h_3A_3)}{\partial q_2}-\frac{\partial(h_2A_2)}{\partial q_3}\right].$$
>
> **Paso 6 — permutación cíclica y forma compacta.** Reorientando la cara según $\hat q_2$ y $\hat q_3$ se obtienen
> $$[\vec\nabla\times\vec A]_2=\frac{1}{h_1h_3}\left[\frac{\partial(h_1A_1)}{\partial q_3}-\frac{\partial(h_3A_3)}{\partial q_1}\right],\quad
> [\vec\nabla\times\vec A]_3=\frac{1}{h_1h_2}\left[\frac{\partial(h_2A_2)}{\partial q_1}-\frac{\partial(h_1A_1)}{\partial q_2}\right].$$
> Las tres se compactan en la notación de Levi-Civita $[\vec\nabla\times\vec A]_i=\dfrac{\varepsilon_{ijk}}{h_jh_k}\dfrac{\partial(h_kA_k)}{\partial q_j}$ o, equivalentemente, en el determinante de la definición. $\blacksquare$

---

## Resumen

> [!resumen]
> | Aspecto | Expresión |
> |---|---|
> | Componente $i$ | $[\vec\nabla\times\vec A]_i=\dfrac{\varepsilon_{ijk}}{h_jh_k}\dfrac{\partial(h_kA_k)}{\partial q_j}$ |
> | 1-componente | $\dfrac{1}{h_2h_3}\!\left[\partial_{q_2}(h_3A_3)-\partial_{q_3}(h_2A_2)\right]$ (y cíclicas) |
> | Determinante | $\dfrac{1}{h_1h_2h_3}\det[\,h_i\hat q_i;\ \partial_{q_i};\ h_iA_i\,]$ |
> | Origen | definición integral $\lim_{C\to0}\oint_C d\vec r\cdot\vec A$ |
> | Cilíndrico | filas $(\hat q_\rho,\rho\hat q_\phi,\hat q_z),\ (\partial_\rho,\partial_\phi,\partial_z),\ (A_\rho,\rho A_\phi,A_z)$ entre $\rho$ |
> | Cartesiano | $h_i=1\Rightarrow\varepsilon_{ijk}\,\partial_jA_k\,\hat e_i$ |

> [!corolario]
> El rotor curvilíneo refleja la circulación por unidad de área: por eso aparecen las longitudes físicas $h_kA_k$ dentro de las derivadas (la circulación a lo largo de cada arista) y las áreas $h_jh_k$ en el denominador. La forma determinante condensa las tres componentes y deja ver la analogía directa con el caso cartesiano, que se recupera al hacer $h_i=1$.

> [!referencia]
> - Geometría del lazo y elementos diferenciales: [[Geometria Diferencial Local]], [[Elementos Linea Superficie Volumen]].
> - Versión cartesiana: [[Rotor]]; símbolo de Levi-Civita: [[Simbolo Levi-Civita]].
> - Operadores hermanos: [[Gradiente General]], [[Divergencia General]].
