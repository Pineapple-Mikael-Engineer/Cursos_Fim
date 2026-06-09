---
title: Funcion de Green y Condiciones
tags:
  - ecuaciones
  - edp
  - teoria
  - funcion-green
  - frontera
draft: false
aliases:
  - función de Green con condiciones de frontera
  - corrección armónica
  - Green's function boundary conditions
  - representation formula
---

# Función de Green y Condiciones

> [!definicion]
> La **función de Green** de un dominio $\Omega$ es la solución fundamental **adaptada a las
> fronteras**. Se construye sumando a la [[Solucion Fundamental| solución fundamental]] $\Phi$ una
> **corrección armónica** $h$:
> $$G(\mathbf{x},\boldsymbol{\xi})=\Phi(\mathbf{x}-\boldsymbol{\xi})+h(\mathbf{x},\boldsymbol{\xi}),
> \qquad \nabla^2_{\mathbf{x}}\,h=0\ \text{ en }\Omega,$$
> donde $h$ se elige (sin singularidades dentro de $\Omega$, por eso armónica) de modo que $G$ cumpla
> la condición de frontera. Para **Dirichlet** se pide
> $$G(\mathbf{x},\boldsymbol{\xi})=0\quad\text{cuando }\mathbf{x}\in\partial\Omega.$$
> Así $G$ sigue teniendo el impulso $\delta$ en $\boldsymbol{\xi}$ (lo aporta $\Phi$; $h$ es armónica
> y no añade fuente), pero ahora respeta la geometría del dominio.

> [!info]
> Es la segunda pieza de [[Funciones de Green para EDP/index| Funciones de Green para EDP]] y vive en
> el [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]]. Parte de la
> [[Solucion Fundamental]] y, cuando la geometría es simple (plano, esfera), la corrección $h$ se
> obtiene explícitamente con el [[Metodo de las Imagenes]]. La fórmula de representación que aquí se
> demuestra convierte la EDP en una **ecuación integral**, puente hacia el
> [[3 Ecuaciones Integrales/index| capítulo de ecuaciones integrales]].

---

## Ejemplo

> [!ejemplo] La función de Green del semiespacio
> Tomemos $\Omega=\{z>0\}$, el **semiespacio** en 3D, con Dirichlet en el plano $z=0$. La solución
> fundamental sola, $\Phi(\mathbf{x}-\boldsymbol{\xi})=\dfrac{1}{4\pi\lvert\mathbf{x}-\boldsymbol{\xi}\rvert}$,
> **no** se anula en $z=0$. La corrección que lo arregla es el potencial de una **fuente imagen**
> colocada en el punto reflejado $\boldsymbol{\xi}^*=(\xi_1,\xi_2,-\xi_3)$, con signo opuesto:
> $$G(\mathbf{x},\boldsymbol{\xi})=\frac{1}{4\pi\lvert\mathbf{x}-\boldsymbol{\xi}\rvert}
> -\frac{1}{4\pi\lvert\mathbf{x}-\boldsymbol{\xi}^*\rvert}.$$
> Aquí $h=-\Phi(\mathbf{x}-\boldsymbol{\xi}^*)$ es armónica dentro de $\Omega$ (su singularidad cae en
> $z<0$, fuera del dominio), y sobre el plano $z=0$ ambos términos tienen el **mismo denominador**
> (los puntos $\boldsymbol{\xi}$ y $\boldsymbol{\xi}^*$ equidistan), así que $G=0$, justo lo pedido.
>
> Para el **disco** o la **esfera** la idea es la misma, pero la imagen no es una simple reflexión:
> se coloca en el **punto inverso** respecto de la esfera y con la carga escalada (imagen de Kelvin).
> La construcción detallada de estas $h$ es el contenido de [[Metodo de las Imagenes]]; aquí basta
> con quedarnos con la receta: $G=\Phi+\text{(potencial de imágenes)}$.

## En qué consiste

> [!teoria]
> La lógica de la descomposición $G=\Phi+h$ es de "divide y vencerás":
> - $\Phi$ aporta la **física local** correcta: la singularidad $\delta$ en $\boldsymbol{\xi}$. Sin
>   ella no habría respuesta al impulso.
> - $h$ aporta el **ajuste global** a la frontera. Como debe ser armónica dentro de $\Omega$ (no
>   puede introducir nuevas fuentes), no toca la ecuación $LG=\delta$ en el interior; solo "endereza"
>   los valores en $\partial\Omega$.
>
> Encontrar $h$ es, por tanto, resolver un problema de **Laplace** ($\nabla^2 h=0$) con el dato de
> frontera $h=-\Phi$ sobre $\partial\Omega$ (para que la suma se anule). Eso, en general, es difícil;
> el [[Metodo de las Imagenes]] lo resuelve de un plumazo cuando hay simetría.

> [!teorema] Fórmula de representación de la solución
> Sea $G$ la función de Green de $\Omega$ con $G=0$ en $\partial\Omega$. La solución del problema de
> Dirichlet
> $$-\nabla^2 u=f\ \text{ en }\Omega,\qquad u=g\ \text{ en }\partial\Omega,$$
> viene dada explícitamente por
> $$u(\mathbf{x})=\int_\Omega G(\mathbf{x},\boldsymbol{\xi})\,f(\boldsymbol{\xi})\,d\boldsymbol{\xi}
> \;-\;\oint_{\partial\Omega}\frac{\partial G}{\partial n_{\boldsymbol{\xi}}}(\mathbf{x},\boldsymbol{\xi})\,
> g(\boldsymbol{\xi})\,dS_{\boldsymbol{\xi}}.$$
> El primer término propaga la **fuente interior** $f$; el segundo propaga el **dato de frontera**
> $g$ a través de la derivada normal de $G$ (el **núcleo de Poisson** del dominio).

> [!demostracion]
> **Paso 1 — La segunda identidad de Green.** Para dos funciones suaves $u,v$ en $\Omega$,
> $$\int_\Omega\big(u\,\nabla^2 v-v\,\nabla^2 u\big)\,d\boldsymbol{\xi}
> =\oint_{\partial\Omega}\Big(u\,\frac{\partial v}{\partial n}-v\,\frac{\partial u}{\partial n}\Big)\,dS.$$
> Es la versión "simétrica" del teorema de la divergencia y es la herramienta natural porque el
> laplaciano es autoadjunto.
>
> **Paso 2 — Elegir $v=G$.** Tomamos $v(\boldsymbol{\xi})=G(\mathbf{x},\boldsymbol{\xi})$ (con
> $\mathbf{x}$ fijo) y usamos las dos propiedades de $G$: dentro, $\nabla^2 G=-\delta(\boldsymbol{\xi}-\mathbf{x})$;
> en la frontera, $G=0$. El término de volumen del lado izquierdo se parte en dos:
> $$\int_\Omega\!\big(u\,\nabla^2 G-G\,\nabla^2 u\big)
> =\int_\Omega\! u\,(-\delta(\boldsymbol{\xi}-\mathbf{x}))\,d\boldsymbol{\xi}
> -\int_\Omega\! G\,(-f)\,d\boldsymbol{\xi}
> =-u(\mathbf{x})+\int_\Omega G\,f.$$
> Se usó $\nabla^2 u=-f$ y la propiedad de filtrado de la delta, $\int u\,\delta(\boldsymbol{\xi}-\mathbf{x})=u(\mathbf{x})$.
>
> **Paso 3 — El lado de frontera.** En $\partial\Omega$ es $G=0$, así que el término
> $G\,\partial_n u$ se anula y solo sobrevive $u\,\partial_n G=g\,\partial_n G$:
> $$\oint_{\partial\Omega}\Big(u\,\frac{\partial G}{\partial n}-G\,\frac{\partial u}{\partial n}\Big)\,dS
> =\oint_{\partial\Omega} g\,\frac{\partial G}{\partial n}\,dS.$$
>
> **Paso 4 — Igualar y despejar.** Igualando los dos lados de la identidad de Green,
> $$-u(\mathbf{x})+\int_\Omega G\,f=\oint_{\partial\Omega} g\,\frac{\partial G}{\partial n}\,dS,$$
> y despejando $u(\mathbf{x})$ se obtiene la fórmula de representación enunciada. $\blacksquare$

> [!proposicion] Simetría (reciprocidad)
> La función de Green del laplaciano es **simétrica**:
> $$G(\mathbf{x},\boldsymbol{\xi})=G(\boldsymbol{\xi},\mathbf{x}).$$
> Físicamente es el **principio de reciprocidad**: la respuesta medida en $\mathbf{x}$ ante una fuente
> en $\boldsymbol{\xi}$ es la misma que la respuesta en $\boldsymbol{\xi}$ ante una fuente en
> $\mathbf{x}$. Se demuestra aplicando la segunda identidad de Green a $G(\mathbf{x},\cdot)$ y
> $G(\mathbf{y},\cdot)$: ambas se anulan en la frontera, el término de borde desaparece, y las dos
> deltas dan $G(\mathbf{x},\mathbf{y})=G(\mathbf{y},\mathbf{x})$. Es el reflejo de que $-\nabla^2$
> es un operador **autoadjunto**.

> [!info] Puente con las ecuaciones integrales
> La fórmula $u(\mathbf{x})=\int_\Omega G(\mathbf{x},\boldsymbol{\xi})\,f(\boldsymbol{\xi})\,d\boldsymbol{\xi}$
> (cuando $g=0$) es una **ecuación integral** con **núcleo** $G$: la solución se expresa integrando el
> dato contra $G$. La función de Green es así la **inversa integral** del operador diferencial, y la
> simetría $G(\mathbf{x},\boldsymbol{\xi})=G(\boldsymbol{\xi},\mathbf{x})$ es la versión continua de que
> "la inversa de una matriz simétrica es simétrica". Esto enlaza directamente con el
> [[3 Ecuaciones Integrales/index| capítulo de ecuaciones integrales]], donde núcleos de este tipo
> se estudian por sí mismos.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Función de Green | $G=\Phi+h$, con $\nabla^2 h=0$ en $\Omega$ |
> | Dirichlet | $G=0$ en $\partial\Omega$ |
> | Hallar $h$ | resolver Laplace con dato $h=-\Phi$ en la frontera |
> | Representación | $u=\displaystyle\int_\Omega G\,f\,d\boldsymbol{\xi}-\oint_{\partial\Omega}\partial_n G\,g\,dS$ |
> | Herramienta | segunda identidad de Green |
> | Simetría | $G(\mathbf{x},\boldsymbol{\xi})=G(\boldsymbol{\xi},\mathbf{x})$ (reciprocidad) |
> | Geometrías simples | $h$ por [[Metodo de las Imagenes\|imágenes]] |

> [!corolario]
> La función de Green resume **todo** el problema —operador, dominio y condición de frontera— en un
> único núcleo: una vez conocida, la solución para **cualquier** $f$ y $g$ se obtiene integrando, sin
> volver a resolver la EDP. Es la inversa integral de $-\nabla^2$ sobre $\Omega$, y su simetría
> expresa la reciprocidad fuente-medida.

> [!referencia]
> - La pieza de espacio libre: [[Solucion Fundamental]].
> - Construir $h$ por simetría: [[Metodo de las Imagenes]].
> - Núcleos integrales en general: [[3 Ecuaciones Integrales/index]].
> - El índice de la sección: [[Funciones de Green para EDP/index]].
