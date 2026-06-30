---
title: Divergencia en Coordenadas Curvilíneas
order: 6
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-curvilineas
  - divergencia
draft: false
aliases:
  - divergencia general
  - divergencia curvilinea
  - nabla punto A curvilineo
  - general divergence
  - curvilinear divergence
---

# Divergencia en Coordenadas Curvilíneas $\vec\nabla\cdot\vec A$

> [!definicion]
> En un sistema curvilíneo ortogonal $(q_1,q_2,q_3)$ con factores de escala $h_i$, la **divergencia** de un campo vectorial $\vec A=A_i\,\hat q_i$ es
> $$\vec\nabla\cdot\vec A=\frac{1}{h_1h_2h_3}\left[\frac{\partial(h_2h_3A_1)}{\partial q_1}+\frac{\partial(h_1h_3A_2)}{\partial q_2}+\frac{\partial(h_1h_2A_3)}{\partial q_3}\right].$$
> Cada $h$ que acompaña a la componente $A_i$ es el **área** de la cara perpendicular a $\hat q_i$ por unidad de coordenada; el prefactor $1/(h_1h_2h_3)$ es el inverso del volumen por unidad de coordenadas.

> [!info]
> Sección **3.4.9** del libro, dentro de [[index | sistemas curvilíneos generales]]. A diferencia del [[Gradiente General | gradiente]], no sale de una comparación diferencial sino de la **definición integral** (flujo por unidad de volumen), porque hay que tener en cuenta cómo cambia el área de las caras al moverse por el espacio. Reutiliza el elemento de volumen $d\tau=h_1h_2h_3\,dq_1dq_2dq_3$ y la geometría de las caras de [[Geometria Diferencial Local]]. Recupera la [[Divergencia | divergencia cartesiana]] del capítulo 2 cuando $h_i=1$.

---

## Ejemplo

> [!ejemplo]
> **Recuperar las divergencias cilíndrica y esférica.** Se sustituyen los factores de escala en la fórmula general.
>
> *Cilíndrico* $(\rho,\phi,z)$, con $h_\rho=1,\ h_\phi=\rho,\ h_z=1$, luego $h_1h_2h_3=\rho$:
> $$\vec\nabla\cdot\vec A=\frac{1}{\rho}\left[\frac{\partial(\rho A_\rho)}{\partial\rho}+\frac{\partial A_\phi}{\partial\phi}+\frac{\partial(\rho A_z)}{\partial z}\right]=\frac{1}{\rho}\frac{\partial(\rho A_\rho)}{\partial\rho}+\frac{1}{\rho}\frac{\partial A_\phi}{\partial\phi}+\frac{\partial A_z}{\partial z}.$$
>
> *Esférico* $(r,\theta,\phi)$, con $h_r=1,\ h_\theta=r,\ h_\phi=r\operatorname{sen}\theta$, luego $h_1h_2h_3=r^2\operatorname{sen}\theta$:
> $$\vec\nabla\cdot\vec A=\frac{1}{r^2\operatorname{sen}\theta}\left[\frac{\partial(r^2\operatorname{sen}\theta\,A_r)}{\partial r}+\frac{\partial(r\operatorname{sen}\theta\,A_\theta)}{\partial\theta}+\frac{\partial(r\,A_\phi)}{\partial\phi}\right],$$
> que se simplifica a
> $$\vec\nabla\cdot\vec A=\frac{1}{r^2}\frac{\partial(r^2A_r)}{\partial r}+\frac{1}{r\operatorname{sen}\theta}\frac{\partial(\operatorname{sen}\theta\,A_\theta)}{\partial\theta}+\frac{1}{r\operatorname{sen}\theta}\frac{\partial A_\phi}{\partial\phi}.$$
> Con $h_i=1$ se recupera $\vec\nabla\cdot\vec A=\partial A_i/\partial x_i$.

---

## Demostración

> [!teorema]
> Para todo campo vectorial $\vec A$ diferenciable,
> $$\vec\nabla\cdot\vec A=\frac{1}{h_1h_2h_3}\left[\frac{\partial(h_2h_3A_1)}{\partial q_1}+\frac{\partial(h_1h_3A_2)}{\partial q_2}+\frac{\partial(h_1h_2A_3)}{\partial q_3}\right].$$

> [!demostracion]
> Se parte de la **definición integral** de la divergencia (flujo neto por unidad de volumen), válida en cualquier geometría:
> $$\vec\nabla\cdot\vec A=\lim_{V\to0}\frac{\oint_S d\vec\sigma\cdot\vec A}{\int_V d\tau},$$
> donde $S$ es la superficie cerrada que encierra el volumen $V$. Se aplica al **volumen diferencial** de aristas $h_1\,dq_1$, $h_2\,dq_2$, $h_3\,dq_3$.
>
> **Paso 1 — denominador (volumen).** El elemento de volumen curvilíneo es el producto de las tres aristas físicas:
> $$\int_V d\tau=h_1h_2h_3\,dq_1\,dq_2\,dq_3.$$
>
> **Paso 2 — cara inferior $\perp\hat q_3$.** La normal exterior es $-\hat q_3$, así que $d\vec\sigma\cdot\hat q_3<0$. El área de la cara es $(h_1\,dq_1)(h_2\,dq_2)$ y la componente que aporta flujo es $A_3$. Todos $A_3,h_1,h_2$ se evalúan en $(q_1,q_2,q_3)$:
> $$\int_{\text{inf}}d\vec\sigma\cdot\vec A=-\,(h_1h_2A_3)\big|_{q_3}\,dq_1\,dq_2.$$
>
> **Paso 3 — cara superior $\perp\hat q_3$.** Está en $q_3+dq_3$ y su normal es $+\hat q_3$, sin signo menos; ahora $h_1,h_2,A_3$ se evalúan en $q_3+dq_3$:
> $$\int_{\text{sup}}d\vec\sigma\cdot\vec A=+\,(h_1h_2A_3)\big|_{q_3+dq_3}\,dq_1\,dq_2.$$
> Es crucial que $h_1$ y $h_2$ —no solo $A_3$— se evalúen en el nuevo $q_3$: el **área de la cara cambia** al avanzar, y ahí está el origen de los productos $h_ih_j$ dentro de la derivada.
>
> **Paso 4 — Taylor y suma del par en $q_3$.** Desarrollando a primer orden,
> $$(h_1h_2A_3)\big|_{q_3+dq_3}=(h_1h_2A_3)\big|_{q_3}+\frac{\partial(h_1h_2A_3)}{\partial q_3}\,dq_3,$$
> el término constante se cancela entre ambas caras y queda
> $$\int_{\text{inf}+\text{sup}}d\vec\sigma\cdot\vec A=\frac{\partial(h_1h_2A_3)}{\partial q_3}\,dq_1\,dq_2\,dq_3.$$
>
> **Paso 5 — las otras cuatro caras.** Repitiendo el argumento para los pares $\perp\hat q_1$ (área $h_2h_3\,dq_2dq_3$, componente $A_1$) y $\perp\hat q_2$ (área $h_1h_3\,dq_1dq_3$, componente $A_2$), el flujo total por las seis caras es
> $$\oint_S d\vec\sigma\cdot\vec A=\left[\frac{\partial(h_2h_3A_1)}{\partial q_1}+\frac{\partial(h_1h_3A_2)}{\partial q_2}+\frac{\partial(h_1h_2A_3)}{\partial q_3}\right]dq_1\,dq_2\,dq_3.$$
>
> **Paso 6 — dividir por el volumen.** Sustituyendo el numerador y el denominador (Paso 1) en la definición, los $dq_1dq_2dq_3$ se cancelan:
> $$\vec\nabla\cdot\vec A=\frac{1}{h_1h_2h_3}\left[\frac{\partial(h_2h_3A_1)}{\partial q_1}+\frac{\partial(h_1h_3A_2)}{\partial q_2}+\frac{\partial(h_1h_2A_3)}{\partial q_3}\right].\qquad\blacksquare$$

---

## Resumen

> [!resumen]
> | Aspecto | Expresión |
> |---|---|
> | General | $\dfrac{1}{h_1h_2h_3}\!\left[\partial_{q_1}(h_2h_3A_1)+\partial_{q_2}(h_1h_3A_2)+\partial_{q_3}(h_1h_2A_3)\right]$ |
> | Origen | definición integral $\lim_{V\to0}\oint d\vec\sigma\cdot\vec A\,/\!\int d\tau$ |
> | Volumen | $d\tau=h_1h_2h_3\,dq_1dq_2dq_3$ |
> | Cilíndrico | $\tfrac1\rho\partial_\rho(\rho A_\rho)+\tfrac1\rho\partial_\phi A_\phi+\partial_z A_z$ |
> | Esférico | $\tfrac{1}{r^2}\partial_r(r^2A_r)+\tfrac{1}{r\operatorname{sen}\theta}\partial_\theta(\operatorname{sen}\theta\,A_\theta)+\tfrac{1}{r\operatorname{sen}\theta}\partial_\phi A_\phi$ |
> | Cartesiano | $h_i=1\Rightarrow\partial A_i/\partial x_i$ |

> [!corolario]
> A diferencia del gradiente, la divergencia no se obtiene reescalando derivadas: los factores de escala entran **dentro** de las derivadas porque el área de cada cara del volumen varía al moverse. Esa es la razón de que aparezcan los productos $h_ih_j$ y el prefactor $1/(h_1h_2h_3)$. Es la versión infinitesimal del teorema de Gauss escrita en geometría curvilínea.

> [!referencia]
> - Geometría de las caras y volumen diferencial: [[Geometria Diferencial Local]], [[Elementos Linea Superficie Volumen]].
> - Versión cartesiana y ecuación de continuidad: [[Divergencia]].
> - Operadores hermanos: [[Gradiente General]], [[Rotor General]].
