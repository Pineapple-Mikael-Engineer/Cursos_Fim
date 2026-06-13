---
title: Trayectorias Ortogonales e Isogonales
tags:
  - ecuaciones
  - edo
  - teoria
  - primer-orden
  - trayectorias-ortogonales
draft: false
aliases:
  - trayectorias ortogonales
  - trayectorias isogonales
  - curvas ortogonales
  - orthogonal trajectories
  - isogonal trajectories
---

# Trayectorias Ortogonales e Isogonales

> [!definicion]
> Dada una **familia uniparamétrica** de curvas $y_c(x)$ (un parámetro $c$), sus **trayectorias
> ortogonales** son las curvas que cortan a cada miembro de la familia **perpendicularmente** en su
> punto de intersección. Como dos rectas con pendientes $m_1,m_2$ son perpendiculares si y solo si
> $$m_1\,m_2=-1,$$
> la pendiente de la trayectoria ortogonal debe ser el **opuesto del recíproco** de la pendiente de la
> familia en ese punto. Es decir, si la familia satisface la EDO $y_c'=g(x,y)$, la trayectoria
> ortogonal $y$ satisface
> $$y'=-\frac{1}{y_c'}=-\frac{1}{g(x,y)}.$$

> [!info]
> Aplicación geométrica del [[Metodos de Primer Orden/index| catálogo de primer orden]] (libro, cap. 1.1.2.1.1). No es un
> "tipo" nuevo de ecuación, sino una **receta de modelado**: traduce una condición geométrica
> (perpendicularidad) en una EDO que luego se resuelve con los métodos ya conocidos
> ([[Variables Separables| separables]], [[Ecuaciones Homogeneas| homogéneas]]). Para visualizar la
> familia y sus cortes apóyate en el
> [[Campo de Direcciones e Isoclinas| campo de direcciones]]: la
> trayectoria ortogonal es, en cada punto, perpendicular al segmento del campo de la familia.

---

## Ejemplo

> [!ejemplo] Parábolas $y=cx^2$ y sus trayectorias ortogonales
> ![[trayectorias_ortogonales.svg|460]]
>
> La familia de parábolas (dorado) y las elipses ortogonales $x^2+2y^2=k$ (verde) se cortan en ángulo
> recto en cada punto.
>
> **Hallar las trayectorias ortogonales a la familia $y=cx^2$.**
>
> **Paso 1 — eliminar el parámetro $c$ para obtener la EDO de la familia.** Cada parábola tiene su
> propio $c$; necesitamos una ecuación diferencial que **no** dependa de $c$. Derivando $y=cx^2$,
> $$y_c'=2cx.$$
> Pero todavía aparece $c$. Lo despejamos de la familia, $c=\dfrac{y}{x^2}$, y lo sustituimos:
> $$y_c'=2cx=2\cdot\frac{y}{x^2}\cdot x=\frac{2y}{x}.$$
> Esta es la EDO que cumplen **todas** las parábolas a la vez: su pendiente en $(x,y)$ es $2y/x$.
>
> **Paso 2 — imponer la perpendicularidad** $y'\to -1/y_c'$. La trayectoria ortogonal tiene pendiente
> $$y'=-\frac{1}{2y/x}=-\frac{x}{2y}.$$
>
> **Paso 3 — resolver la EDO de las ortogonales.** Es [[Variables Separables| separable]]:
> $$2y\,dy=-x\,dx\ \Longrightarrow\ \int 2y\,dy=-\int x\,dx\ \Longrightarrow\ y^{2}=-\frac{x^{2}}{2}+C.$$
> Multiplicando por $2$ y renombrando la constante $k=2C$,
> $$\boxed{\ x^{2}+2y^{2}=k\ }$$
> que es una **familia de elipses**. Cada elipse corta a cada parábola en ángulo recto.

---

## En qué consiste

> [!teoria]
> La clave conceptual es que una familia uniparamétrica $F(x,y,c)=0$ tiene, en cada punto del plano
> por el que pasa **un** miembro, una **dirección bien definida** (su pendiente). Esa dirección es un
> *campo de direcciones* asociado a la familia. Construir las trayectorias ortogonales equivale a
> **girar $90°$ ese campo** en cada punto y luego integrar.
>
> El paso delicado es el **Paso 1**: para que la condición $y'=-1/y_c'$ tenga sentido necesitamos la
> pendiente de la familia **expresada solo en $(x,y)$**, sin el parámetro $c$. Por eso se deriva
> $F(x,y,c)=0$ y se elimina $c$ usando la propia ecuación de la familia. El resultado $y_c'=g(x,y)$ es
> la **EDO de la familia**: la ecuación cuya solución general es justamente esa familia. Una vez se
> tiene $g$, las ortogonales resuelven $y'=-1/g(x,y)$ y las isogonales una variante con $\tan\alpha$.

> [!demostracion] La condición $m_1m_2=-1$ y de ahí $y'=-1/y_c'$
> **Paso 1 — pendiente como tangente del ángulo.** Una recta de pendiente $m$ forma con el eje $x$ un
> ángulo $\theta$ con $m=\tan\theta$. Tomamos dos rectas, $m_1=\tan\theta_1$ y $m_2=\tan\theta_2$.
>
> **Paso 2 — perpendicularidad.** Son perpendiculares cuando sus ángulos difieren en $90°$, es decir
> $\theta_2=\theta_1+90°$. Entonces
> $$m_2=\tan(\theta_1+90°)=-\cot\theta_1=-\frac{1}{\tan\theta_1}=-\frac{1}{m_1}\ \Longrightarrow\ m_1m_2=-1.$$
>
> **Paso 3 — aplicar a las curvas.** En el punto de corte, la trayectoria ortogonal y el miembro de la
> familia son perpendiculares, luego sus pendientes —$y'$ y $y_c'$— cumplen $y'\,y_c'=-1$, de donde
> $$y'=-\frac{1}{y_c'}.\qquad\blacksquare$$

> [!algoritmo] Hallar las trayectorias ortogonales
> 1. **Parte de la familia** $F(x,y,c)=0$.
> 2. **Deriva** respecto a $x$ y **elimina** el parámetro $c$ (usando la familia) hasta obtener su EDO
>    en forma normal $y_c'=g(x,y)$.
> 3. **Sustituye** $y'\to-\dfrac{1}{y'}$: la EDO de las ortogonales es $y'=-\dfrac{1}{g(x,y)}$.
> 4. **Resuelve** esa EDO con el método que corresponda (separable, homogénea, lineal…).

> [!ejemplo] Variante — la familia $y=cx^5$
> Con el mismo procedimiento: de $y=cx^5$ se tiene $c=y/x^5$ y
> $$y_c'=5cx^4=5\cdot\frac{y}{x^5}\cdot x^4=\frac{5y}{x}.$$
> Las ortogonales cumplen $y'=-\dfrac{x}{5y}$, es decir $5y\,dy=-x\,dx$, e integrando
> $$x^{2}+5y^{2}=k$$
> (de nuevo elipses, ahora más achatadas). Se ve el patrón: para $y=cx^{n}$ la EDO es $y_c'=ny/x$ y las
> ortogonales dan $x^{2}+n\,y^{2}=k$.

> [!info] Trayectorias isogonales
> Si en lugar de cortar a $90°$ se pide que la trayectoria corte a la familia bajo un **ángulo fijo
> $\alpha$**, la condición sobre las pendientes ya no es $m_1m_2=-1$ sino la fórmula de la tangente del
> ángulo entre dos rectas. La EDO de las **trayectorias isogonales** es
> $$y'=\frac{y_c'\mp\tan\alpha}{1\pm y_c'\tan\alpha}.$$
> El caso $\alpha=90°$ ($\tan\alpha\to\infty$) recupera $y'=-1/y_c'$, las ortogonales. Los dos signos
> corresponden a cortar "por un lado o por el otro" de la curva.

> [!demostracion] La fórmula isogonal desde el ángulo entre rectas
> **Paso 1 — tangente del ángulo entre dos rectas.** Si dos rectas tienen pendientes $m$ y $m_c$, el
> ángulo $\alpha$ medido de una a la otra cumple la identidad
> $$\tan\alpha=\frac{m-m_c}{1+m\,m_c}.$$
>
> **Paso 2 — imponer el ángulo fijo.** Para la trayectoria isogonal $m=y'$ y para el miembro de la
> familia $m_c=y_c'$; pedimos que se corten bajo el ángulo $\alpha$:
> $$\tan\alpha=\frac{y'-y_c'}{1+y'\,y_c'}.$$
>
> **Paso 3 — despejar $y'$.** Multiplicando en cruz, $y'-y_c'=\tan\alpha\,(1+y'y_c')$, y agrupando $y'$:
> $$y'\big(1-y_c'\tan\alpha\big)=y_c'+\tan\alpha\ \Longrightarrow\ y'=\frac{y_c'+\tan\alpha}{1-y_c'\tan\alpha}.$$
> El signo opuesto sale de medir el ángulo en sentido contrario ($\alpha\to-\alpha$), dando
> $y'=\dfrac{y_c'-\tan\alpha}{1+y_c'\tan\alpha}$; ambos son la fórmula isogonal.
>
> **Paso 4 — límite ortogonal.** Cuando $\alpha\to90°$, $\tan\alpha\to\infty$; dividiendo numerador y
> denominador por $\tan\alpha$ y tomando el límite queda $y'=-1/y_c'$, las ortogonales. $\blacksquare$

> [!info] Significado físico
> Las trayectorias ortogonales abundan en la física de campos:
> - En **electrostática**, las **líneas de campo** eléctrico son ortogonales a las superficies
>   (curvas) **equipotenciales**: el campo $\mathbf{E}=-\nabla V$ apunta siempre perpendicular a las
>   curvas $V=\text{cte}$.
> - En **flujo de fluidos** (potencial), las **líneas de corriente** son ortogonales a las curvas
>   equipotenciales del flujo.
> - En **conducción de calor**, las líneas de flujo térmico cruzan perpendicularmente a las isotermas.
> En todos estos casos, conocer una familia permite construir la otra resolviendo $y'=-1/y_c'$.

## Resumen

> [!resumen]
> | Paso | Acción |
> |---|---|
> | Familia | $F(x,y,c)=0$ |
> | EDO de la familia | derivar y eliminar $c$ → $y_c'=g(x,y)$ |
> | Ortogonales | sustituir $y'\to-1/y'$ → $y'=-1/g(x,y)$ |
> | Isogonales ($\alpha$) | $y'=\dfrac{y_c'\mp\tan\alpha}{1\pm y_c'\tan\alpha}$ |
> | Cerrar | resolver la EDO resultante |

> [!corolario]
> Hallar trayectorias ortogonales **no requiere un método nuevo**: es un problema de modelado que se
> reduce a (1) extraer la EDO de la familia eliminando el parámetro y (2) girar su campo $90°$
> cambiando $y'\to-1/y'$. El verdadero trabajo es el Paso 1; lo demás es integrar.

> [!referencia]
> - Métodos para cerrar la EDO: [[Variables Separables]], [[Ecuaciones Homogeneas]].
> - Geometría del campo de direcciones de una familia: [[Campo de Direcciones e Isoclinas]].
> - Vuelta al catálogo: [[Metodos de Primer Orden/index]].
