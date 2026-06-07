---
title: Campos Escalares y Vectoriales
tags:
  - analisis-tensorial
  - teoria
  - calculo-vectorial
  - campos
draft: false
aliases:
  - campos escalares
  - campos vectoriales
  - lineas de campo
  - equipotenciales
  - scalar field
  - vector field
---

# Campos Escalares y Vectoriales

> [!definicion]
> Un **campo escalar** $\Phi(\vec r)$ asigna un número a cada punto; se dibuja por sus **superficies equipotenciales** ($\Phi=$ cte). Un **campo vectorial** $\vec v(\vec r)$ asigna un vector a cada punto; se dibuja por sus **líneas de campo**, tangentes a $\vec v$ en cada punto, cuya densidad indica la magnitud. Ambos se relacionan: $\vec E=-\vec\nabla\Phi$ es perpendicular a las equipotenciales.

> [!info]
> Primera sección del [[index | capítulo 2]] (libro, cap. 2.1). Es el sustrato sobre el que actúan los [[Operadores Diferenciales/index | operadores diferenciales]]: el [[Operadores Diferenciales/Gradiente | gradiente]] genera un campo vectorial a partir de uno escalar, y su geometría (perpendicularidad a las equipotenciales) se entiende mejor con estos dibujos.

---

## Ejemplo

> [!ejemplo]
> **Potencial de dos líneas de carga.** Dos líneas con carga $\pm\lambda_0$ en $(x,y)=(\pm1,0)$ producen el potencial
> $$\Phi=\lambda_0\ln\!\left[\frac{(x+1)^2+y^2}{(x-1)^2+y^2}\right].$$
>
> **Equipotenciales** ($\Phi=$ cte): por la simetría en $z$ son cilindros; en el plano $x$–$y$ son circunferencias alrededor de cada línea. $\Phi=0$ sobre el eje $y$ (equidistante de ambas cargas).
>
> **Campo eléctrico** $\vec E=-\vec\nabla\Phi$:
> $$E_x=4\lambda_0\frac{x^2-y^2-1}{[(x-1)^2+y^2][(x+1)^2+y^2]},\qquad E_y=4\lambda_0\frac{2xy}{[(x-1)^2+y^2][(x+1)^2+y^2]}.$$
>
> **Líneas de campo:** se obtienen integrando $\dfrac{dy}{dx}=\dfrac{E_y}{E_x}=\dfrac{2xy}{x^2-y^2-1}$, que da la familia
> $$x^2+(y-c)^2=1+c^2,$$
> circunferencias centradas en $y=c$ de radio $\sqrt{1+c^2}$. Cruzan perpendicularmente a las equipotenciales y van de la carga $+$ a la $-$.

> [!ejemplo]
> **Una silla de montar: $\Phi=-xy$.** Sus equipotenciales $-xy=$ cte son hipérbolas en el plano $x$–$y$. El campo asociado es
> $$-\vec\nabla\Phi=y\,\hat{e}_x+x\,\hat{e}_y.$$
> Sus líneas de campo salen de $\dfrac{dy}{dx}=\dfrac{x}{y}\Rightarrow y\,dy=x\,dx\Rightarrow y^2-x^2=c$: hipérbolas **perpendiculares** a las equipotenciales. La densidad de líneas crece al acercarse al origen, indicando un campo más intenso allí.

---

## En qué consiste

> [!teoria]
> **Campo escalar.** Tiene un valor único por punto, así que basta dibujar las superficies $\Phi=$ cte (equipotenciales, contornos o geodésicas). Donde están más juntas, $\Phi$ varía más rápido.
>
> **Campo vectorial.** Se representa por líneas tangentes al campo. Si las líneas vienen dadas por $y=y(x)$, su pendiente debe igualar la del vector:
> $$\frac{dy}{dx}=\frac{v_y}{v_x}.$$
> Integrando esa ecuación diferencial se obtiene la familia de líneas de campo (una por cada constante de integración). La **densidad** de líneas codifica la magnitud: más líneas por unidad de área ⇒ campo más intenso.

> [!proposicion] Relación escalar–vectorial
> Si $\vec v=-\vec\nabla\Phi$, entonces las líneas de $\vec v$ son **perpendiculares** a las equipotenciales de $\Phi$. Es consecuencia de que el [[Operadores Diferenciales/Gradiente | gradiente]] apunta en la dirección de máximo crecimiento, normal a las superficies de nivel.

## Resumen

> [!resumen]
> | Concepto | Escalar | Vectorial |
> |---|---|---|
> | Asigna | un número $\Phi(\vec r)$ | un vector $\vec v(\vec r)$ |
> | Se dibuja con | equipotenciales $\Phi=$ cte | líneas de campo |
> | Ecuación del dibujo | superficies de nivel | $dy/dx=v_y/v_x$ |
> | Densidad indica | rapidez de cambio de $\Phi$ | magnitud de $\vec v$ |
> | Relación | $\vec E=-\vec\nabla\Phi$ ⟂ equipotenciales | |

> [!corolario]
> Los campos son el objeto sobre el que actúa todo el capítulo. Un campo escalar se visualiza por sus equipotenciales y uno vectorial por sus líneas de campo (solución de $dy/dx=v_y/v_x$); ambos quedan ligados por el gradiente, que es perpendicular a las superficies de nivel. Esta imagen geométrica guía la interpretación física del [[Operadores Diferenciales/Gradiente | gradiente]], la [[Operadores Diferenciales/Divergencia | divergencia]] y el [[Operadores Diferenciales/Rotor | rotor]].

> [!referencia]
> - Gradiente y su geometría: [[Operadores Diferenciales/Gradiente]].
> - Operadores que actúan sobre campos: [[Operadores Diferenciales/index]].
> - Integrar campos sobre caminos y superficies: [[Operadores Integrales/index]].
