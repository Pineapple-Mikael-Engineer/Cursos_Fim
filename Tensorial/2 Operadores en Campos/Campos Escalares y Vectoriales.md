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

> [!ejemplo] Campo de dos líneas de carga
> ![[campo_dos_cargas.svg|480]]
>
> Equipotenciales (dorado) y líneas de campo (verde) del potencial de dos cargas $\pm\lambda_0$; las líneas cruzan perpendicularmente a las equipotenciales y van de $+$ a $-$.

> [!ejemplo]
> **Una silla de montar: $\Phi=-xy$.** Sus equipotenciales $-xy=$ cte son hipérbolas en el plano $x$–$y$. El campo asociado es
> $$-\vec\nabla\Phi=y\,\hat{e}_x+x\,\hat{e}_y.$$
> Sus líneas de campo salen de $\dfrac{dy}{dx}=\dfrac{x}{y}\Rightarrow y\,dy=x\,dx\Rightarrow y^2-x^2=c$: hipérbolas **perpendiculares** a las equipotenciales. La densidad de líneas crece al acercarse al origen, indicando un campo más intenso allí.

> [!ejemplo] Silla $\Phi=-xy$
> ![[campo_silla.svg|430]]
>
> Equipotenciales hiperbólicas y líneas de campo de $\Phi=-xy$, perpendiculares entre sí.

> [!ejemplo] Línea de campo por un punto dado
> **Hallar la línea de $\vec v=(y,\,x)$ que pasa por $P=(2,1)$.** Usamos la ecuación de las líneas de campo paso a paso.
>
> **Paso 1 — plantear la ecuación.** Con $v_x=y$, $v_y=x$,
> $$\frac{dy}{dx}=\frac{v_y}{v_x}=\frac{x}{y}.$$
>
> **Paso 2 — separar variables e integrar.**
> $$y\,dy=x\,dx\ \Rightarrow\ \int y\,dy=\int x\,dx\ \Rightarrow\ \frac{y^2}{2}=\frac{x^2}{2}+C\ \Rightarrow\ y^2-x^2=c,\quad c=2C.$$
>
> **Paso 3 — fijar la constante con el punto.** Imponiendo que la línea pase por $P=(2,1)$:
> $$c=y_P^2-x_P^2=1^2-2^2=1-4=-3.$$
>
> **Paso 4 — escribir la línea.** La línea de campo buscada es la hipérbola
> $$y^2-x^2=-3\quad\Longleftrightarrow\quad x^2-y^2=3,$$
> que efectivamente pasa por $(2,1)$ ($4-1=3$ ✓). Su tangente en $P$ tiene pendiente $\dfrac{dy}{dx}=\dfrac{x}{y}=\dfrac{2}{1}=2$, igual a la dirección de $\vec v(P)=(1,2)$.

---

## En qué consiste

> [!teoria]
> **Campo escalar.** Tiene un valor único por punto, así que basta dibujar las superficies $\Phi=$ cte (equipotenciales, contornos o geodésicas). Donde están más juntas, $\Phi$ varía más rápido.
>
> **Campo vectorial.** Se representa por líneas tangentes al campo. Si las líneas vienen dadas por $y=y(x)$, su pendiente debe igualar la del vector:
> $$\frac{dy}{dx}=\frac{v_y}{v_x}.$$
> Integrando esa ecuación diferencial se obtiene la familia de líneas de campo (una por cada constante de integración). La **densidad** de líneas codifica la magnitud: más líneas por unidad de área ⇒ campo más intenso.

> [!demostracion] Ecuación de las líneas de campo $dy/dx=v_y/v_x$
> **Paso 1 — condición de tangencia.** Una línea de campo es, por definición, tangente al vector $\vec v$ en cada punto. Si un desplazamiento infinitesimal $d\vec r=(dx,dy,dz)$ avanza a lo largo de la línea, debe ser **paralelo** a $\vec v=(v_x,v_y,v_z)$.
>
> **Paso 2 — paralelismo en componentes.** Dos vectores paralelos tienen componentes proporcionales (el cruce $d\vec r\times\vec v=0$):
> $$\frac{dx}{v_x}=\frac{dy}{v_y}=\frac{dz}{v_z}.$$
>
> **Paso 3 — despejar la pendiente en el plano.** Tomando el par $x$–$y$ y reordenando,
> $$\frac{dy}{dx}=\frac{v_y}{v_x}.\qquad\blacksquare$$
> Integrar esta ecuación diferencial da la familia de líneas de campo; cada constante de integración selecciona la línea que pasa por un punto dado.

> [!teorema] El gradiente es perpendicular a las equipotenciales
> $$\vec v=-\vec\nabla\Phi\ \Rightarrow\ \vec\nabla\Phi\perp(\text{superficie }\Phi=\text{cte}),$$
> es decir, las líneas de $\vec v$ cruzan ortogonalmente a las equipotenciales de $\Phi$.

> [!demostracion]
> **Paso 1 — desplazamiento tangente a la equipotencial.** Sea $d\vec r$ un desplazamiento infinitesimal **contenido** en la superficie $\Phi=$ cte. Como $\Phi$ no cambia al movernos sobre ella, su variación es nula:
> $$d\Phi=0.$$
>
> **Paso 2 — diferencial total como producto punto.** Por la regla de la cadena, la variación de $\Phi$ ante un desplazamiento cualquiera es
> $$d\Phi=\frac{\partial\Phi}{\partial x_i}\,dx_i=\vec\nabla\Phi\cdot d\vec r.$$
>
> **Paso 3 — concluir ortogonalidad.** Combinando los dos pasos, para todo $d\vec r$ tangente a la equipotencial,
> $$\vec\nabla\Phi\cdot d\vec r=0\ \Rightarrow\ \vec\nabla\Phi\perp d\vec r.$$
> Como esto vale para **cualquier** tangente, $\vec\nabla\Phi$ es normal a la superficie $\Phi=$ cte. Y como $\vec v=-\vec\nabla\Phi$ es (anti)paralelo a $\vec\nabla\Phi$, las líneas de campo son perpendiculares a las equipotenciales. $\blacksquare$

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
