---
title: Ecuaciones Simétricas No Homogéneas
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - fredholm
  - nucleos-simetricos
  - schmidt
draft: false
aliases:
  - fórmula de Schmidt
  - ecuaciones simétricas no homogéneas
  - desarrollo en autofunciones
  - Schmidt formula
---

# Ecuaciones Simétricas No Homogéneas

> [!definicion]
> Para la ecuación de Fredholm de **2ª especie** con núcleo **simétrico**,
> $$\varphi(x)=f(x)+\lambda\int_a^b K(x,t)\,\varphi(t)\,dt,$$
> la solución se obtiene **desarrollando en funciones propias** (**fórmula de Schmidt**):
> $$\boxed{\;\varphi(x)=f(x)+\lambda\sum_{n}\frac{f_n}{\lambda_n-\lambda}\,\varphi_n(x)\;},\qquad f_n=\langle f,\varphi_n\rangle=\int_a^b f\,\varphi_n\,dx,$$
> válida siempre que $\lambda$ **no** sea una raíz característica del núcleo ($\lambda\neq\lambda_n$ para
> todo $n$). Es la versión integral de resolver $(\mathsf{I}-\lambda\mathsf{A})\mathbf{x}=\mathbf{f}$
> diagonalizando: cada modo propio se resuelve por separado.

> [!info]
> El **objetivo práctico** de los [[Nucleos Simetricos/index| núcleos simétricos]]: resolver la
> ecuación. Apoya su construcción en [[Teoria de Hilbert-Schmidt| Hilbert-Schmidt]] (que desarrolla
> $K\varphi$) y se relaciona con [[Teorema de Mercer| Mercer]]. La condición $\lambda\neq\lambda_n$ y
> qué pasa al violarla son justamente la [[Alternativa de Fredholm| alternativa de Fredholm]].

---

## Ejemplo

> [!ejemplo] Resolver con el núcleo de Green y $f$ sencillo
> Considera, en $[0,\pi]$,
> $$\varphi(x)=f(x)+\lambda\int_0^\pi G(x,t)\,\varphi(t)\,dt,\qquad f(x)=\operatorname{sen}(x),$$
> con $G$ el núcleo de Green de $-u''$, de espectro $\lambda_n=n^2$ y
> $\varphi_n(x)=\sqrt{2/\pi}\,\operatorname{sen}(nx)$.
>
> **Coeficientes de $f$.** Como $f=\operatorname{sen}(x)=\sqrt{\pi/2}\,\varphi_1$, todos los
> $f_n=\langle f,\varphi_n\rangle$ se anulan salvo $f_1=\sqrt{\pi/2}$. La proyección de $f$ tiene un solo
> modo.
>
> **Fórmula de Schmidt.** Solo sobrevive el término $n=1$:
> $$\varphi(x)=\operatorname{sen}(x)+\lambda\,\frac{f_1}{\lambda_1-\lambda}\,\varphi_1(x)
>   =\operatorname{sen}(x)+\frac{\lambda}{1-\lambda}\operatorname{sen}(x)=\frac{1}{1-\lambda}\operatorname{sen}(x),$$
> (válido si $\lambda\neq1$). En efecto, $\varphi=\frac{\operatorname{sen}x}{1-\lambda}$ cumple la
> ecuación, pues $\int_0^\pi G(x,t)\operatorname{sen}(t)\,dt=\operatorname{sen}(x)$ (es la función propia
> de $\lambda_1=1$). Cuando $\lambda\to1$ la solución **explota**: $\lambda=1$ es la primera raíz
> característica y $f=\operatorname{sen}x$ no es ortogonal a $\varphi_1$ — el caso de resonancia.

---

## En qué consiste

> [!teoria]
> La idea es **diagonalizar**: como las $\varphi_n$ son base ortonormal, escribe la incógnita y el dato
> en esa base, $\varphi=\sum_n c_n\varphi_n$ y $f=\sum_n f_n\varphi_n$. El operador integral actúa
> diagonalmente, $K\varphi_n=\varphi_n/\lambda_n$, así que la ecuación, que mezcla todo a través de la
> integral, se **desacopla** en una ecuación escalar **independiente por cada modo** $n$. Resolver una
> ecuación integral se reduce a resolver infinitas ecuaciones de primer grado triviales.

> [!teorema] Fórmula de Schmidt
> Si $K$ es simétrico con espectro $\{(\lambda_n,\varphi_n)\}$ y $\lambda\neq\lambda_n$ para todo $n$, la
> ecuación $\varphi=f+\lambda K\varphi$ tiene solución **única**
> $$\varphi(x)=f(x)+\lambda\sum_n\frac{f_n}{\lambda_n-\lambda}\,\varphi_n(x),\qquad f_n=\langle f,\varphi_n\rangle.$$

> [!demostracion]
> **Paso 1 — desarrollar en la base propia.** Pon $\varphi=\sum_n c_n\varphi_n$ y $f=\sum_n f_n\varphi_n$
> con $f_n=\langle f,\varphi_n\rangle$. Buscamos los coeficientes $c_n$.
>
> **Paso 2 — sustituir y usar la acción diagonal.** En el término integral,
> $K\varphi=\sum_n c_n\,K\varphi_n=\sum_n c_n\,\dfrac{\varphi_n}{\lambda_n}$, porque cada $\varphi_n$ es
> función propia. La ecuación $\varphi=f+\lambda K\varphi$ queda
> $$\sum_n c_n\varphi_n=\sum_n f_n\varphi_n+\lambda\sum_n\frac{c_n}{\lambda_n}\varphi_n.$$
>
> **Paso 3 — igualar coeficientes.** Por ortonormalidad de las $\varphi_n$, los coeficientes de cada
> modo deben coincidir:
> $$c_n=f_n+\frac{\lambda}{\lambda_n}\,c_n\;\Longrightarrow\;c_n\Big(1-\frac{\lambda}{\lambda_n}\Big)=f_n\;\Longrightarrow\;c_n=\frac{\lambda_n\,f_n}{\lambda_n-\lambda}.$$
>
> **Paso 4 — reensamblar.** Entonces
> $$\varphi=\sum_n c_n\varphi_n=\sum_n\frac{\lambda_n f_n}{\lambda_n-\lambda}\varphi_n
>   =\sum_n f_n\varphi_n+\sum_n\Big(\frac{\lambda_n}{\lambda_n-\lambda}-1\Big)f_n\varphi_n
>   =f+\lambda\sum_n\frac{f_n}{\lambda_n-\lambda}\varphi_n,$$
> que es la fórmula de Schmidt. La solución es única porque cada $c_n$ queda determinado sin ambigüedad
> mientras $\lambda\neq\lambda_n$. $\blacksquare$

> [!warning] Resonancia: cuando $\lambda\to\lambda_n$
> Si $\lambda$ se acerca a una raíz característica $\lambda_k$, el denominador $\lambda_k-\lambda\to0$ y
> el término $k$-ésimo **explota** —la solución se hace infinita— **salvo** que el numerador también se
> anule, es decir $f_k=\langle f,\varphi_k\rangle=0$ (que $f$ sea **ortogonal** a $\varphi_k$). Esta es
> exactamente la [[Alternativa de Fredholm| alternativa de Fredholm]] vista por dentro:
> - si $\lambda\neq\lambda_n$: solución **única** (la fórmula);
> - si $\lambda=\lambda_k$ y $f\perp\varphi_k$: **infinitas** soluciones (se añade $\alpha\varphi_k$ libre);
> - si $\lambda=\lambda_k$ y $f\not\perp\varphi_k$: **ninguna** solución.

> [!info]
> El método es idéntico a resolver $(\mathsf{I}-\lambda\mathsf{A})\mathbf{x}=\mathbf{f}$ con
> $\mathsf{A}$ simétrica: diagonalizas, divides componente a componente por $1-\lambda/\lambda_n$, y
> reconstruyes. Que la integral —un acoplamiento global— se desacople en escalares es el regalo del
> núcleo simétrico.

## Resumen

> [!resumen]
> | Concepto | Contenido |
> |---|---|
> | Ecuación | $\varphi=f+\lambda\int_a^b K\varphi$, $K$ simétrico |
> | Solución (Schmidt) | $\varphi=f+\lambda\sum_n\frac{f_n}{\lambda_n-\lambda}\varphi_n$, $f_n=\langle f,\varphi_n\rangle$ |
> | Validez | $\lambda\neq\lambda_n$ (no es raíz característica) |
> | Coeficientes | $c_n=\frac{\lambda_n f_n}{\lambda_n-\lambda}$ |
> | Resonancia $\lambda\to\lambda_k$ | explota salvo $f\perp\varphi_k$ → [[Alternativa de Fredholm\|alternativa]] |

> [!corolario]
> Con núcleo simétrico, resolver Fredholm de 2ª especie es **proyectar el dato sobre las funciones
> propias y dividir cada modo por $\lambda_n-\lambda$**. Toda la dificultad se concentra en el espectro,
> y la existencia/unicidad queda decidida modo a modo: la alternativa de Fredholm hecha aritmética.

> [!referencia]
> - La maquinaria de desarrollo: [[Teoria de Hilbert-Schmidt]].
> - El núcleo como serie espectral: [[Teorema de Mercer]].
> - La dicotomía existencia/unicidad: [[Alternativa de Fredholm]].
> - Panorama: [[Nucleos Simetricos/index]].
