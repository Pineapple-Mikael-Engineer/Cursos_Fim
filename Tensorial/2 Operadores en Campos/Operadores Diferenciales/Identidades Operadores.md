---
title: Identidades con Operadores Diferenciales
tags:
  - analisis-tensorial
  - teoria
  - calculo-vectorial
  - identidades
draft: false
aliases:
  - identidades de operadores
  - laplaciano
  - rotor del rotor
  - vector identities
  - laplacian
---

# Identidades con Operadores Diferenciales

> [!definicion]
> Dos identidades fundamentales del cálculo vectorial, demostrables como puro álgebra de índices en notación de Einstein:
> $$\vec\nabla\cdot(\vec\nabla\Phi)=\nabla^2\Phi,\qquad\vec\nabla\times\vec\nabla\times\vec v=\vec\nabla(\vec\nabla\cdot\vec v)-\nabla^2\vec v,$$
> donde el **operador laplaciano** es
> $$\nabla^2=\frac{\partial}{\partial x_i}\frac{\partial}{\partial x_i}=\frac{\partial^2}{\partial x_1^2}+\frac{\partial^2}{\partial x_2^2}+\frac{\partial^2}{\partial x_3^2}.$$

> [!info]
> Sección **2.3.4** del libro, dentro de [[index | operadores diferenciales]]. La notación de Einstein facilita estas demostraciones: se trabaja en cartesianas (bases independientes de la posición) y el resultado se reescribe en notación vectorial. La segunda identidad es **clave para la ecuación de ondas electromagnéticas**, que se deduce de las ecuaciones de Maxwell.

---

## Ejemplo

> [!ejemplo]
> **Laplaciano de un escalar concreto.** Sea $\Phi=x^2+y^2-2z^2$. Aplicando $\nabla^2=\sum_i\partial^2/\partial x_i^2$:
> $$\nabla^2\Phi=\frac{\partial^2\Phi}{\partial x^2}+\frac{\partial^2\Phi}{\partial y^2}+\frac{\partial^2\Phi}{\partial z^2}=2+2-4=0.$$
> $\Phi$ es **armónica** ($\nabla^2\Phi=0$): satisface la ecuación de Laplace, como todo potencial en una región sin cargas. Verifiquemos vía $\vec\nabla\cdot(\vec\nabla\Phi)$:
> $$\vec\nabla\Phi=(2x,\,2y,\,-4z),\qquad\vec\nabla\cdot(\vec\nabla\Phi)=2+2-4=0,$$
> que coincide, ilustrando la primera identidad.

---

## En qué consiste

> [!teorema] Divergencia del gradiente
> $$\vec\nabla\cdot(\vec\nabla\Phi)=\nabla^2\Phi.$$

> [!demostracion]
> **Paso 1.** Escribimos los dos operadores $\vec\nabla$ con índices **independientes** para no violar la regla de oro:
> $$\vec\nabla\cdot(\vec\nabla\Phi)=\hat{e}_i\frac{\partial}{\partial x_i}\cdot\left(\hat{e}_j\frac{\partial}{\partial x_j}\Phi\right).$$
>
> **Paso 2.** En cartesianas las bases no dependen de la posición, $\partial\hat{e}_j/\partial x_i=0$, de modo que $\hat{e}_i$ y $\hat{e}_j$ salen como producto punto:
> $$\vec\nabla\cdot(\vec\nabla\Phi)=(\hat{e}_i\cdot\hat{e}_j)\frac{\partial}{\partial x_i}\left(\frac{\partial}{\partial x_j}\Phi\right).$$
>
> **Paso 3.** Con $\hat{e}_i\cdot\hat{e}_j=\delta_{ij}$, la delta de Kronecker colapsa la suma fijando $j=i$:
> $$\vec\nabla\cdot(\vec\nabla\Phi)=\delta_{ij}\frac{\partial}{\partial x_i}\frac{\partial}{\partial x_j}\Phi=\frac{\partial}{\partial x_i}\frac{\partial}{\partial x_i}\Phi.$$
>
> **Paso 4.** Escribiendo la suma explícita sobre $i=1,2,3$:
> $$\vec\nabla\cdot(\vec\nabla\Phi)=\left(\frac{\partial^2}{\partial x_1^2}+\frac{\partial^2}{\partial x_2^2}+\frac{\partial^2}{\partial x_3^2}\right)\Phi\equiv\nabla^2\Phi.\qquad\blacksquare$$

> [!teorema] Rotor del rotor
> $$\vec\nabla\times\vec\nabla\times\vec v=\vec\nabla(\vec\nabla\cdot\vec v)-\nabla^2\vec v.$$

> [!demostracion]
> **Paso 1.** En notación de Einstein, con dos $\varepsilon$ (uno por cada producto cruz):
> $$\vec\nabla\times\vec\nabla\times\vec v=\frac{\partial}{\partial x_i}\left(\frac{\partial v_s}{\partial x_r}\varepsilon_{rsj}\right)\varepsilon_{ijk}\,\hat{e}_k.$$
>
> **Paso 2.** Reordenamos para aplicar la [[1 Algebra Lineal y Notacion/Simbolos Especiales/Identidad Epsilon-Delta | identidad épsilon-delta]]. Permutando índices en $\varepsilon_{ijk}=-\varepsilon_{ikj}$ para que ambos símbolos compartan el índice mudo $j$ en última posición:
> $$=-\frac{\partial}{\partial x_i}\left(\frac{\partial v_s}{\partial x_r}\right)\varepsilon_{rsj}\varepsilon_{ikj}\,\hat{e}_k.$$
>
> **Paso 3.** Aplicamos $\varepsilon_{rsj}\varepsilon_{ikj}=\delta_{ri}\delta_{sk}-\delta_{rk}\delta_{si}$ (ver [[1 Algebra Lineal y Notacion/Simbolos Especiales/Identidad Epsilon-Delta | Identidad Epsilon-Delta]]):
> $$=-\frac{\partial}{\partial x_i}\left(\frac{\partial v_s}{\partial x_r}\right)(\delta_{ri}\delta_{sk}-\delta_{rk}\delta_{si})\,\hat{e}_k.$$
>
> **Paso 4.** Las deltas colapsan las sumas. En el primer término $r\to i$, $s\to k$; en el segundo $r\to k$, $s\to i$ (el signo global $-$ los intercambia):
> $$=\frac{\partial}{\partial x_i}\left(\frac{\partial v_i}{\partial x_k}\right)\hat{e}_k-\frac{\partial}{\partial x_i}\left(\frac{\partial v_k}{\partial x_i}\right)\hat{e}_k.$$
>
> **Paso 5.** Reagrupamos cada término en notación vectorial. En el primero, $\partial v_i/\partial x_i=\vec\nabla\cdot\vec v$ y el $\partial/\partial x_k\,(\cdot)\hat{e}_k$ exterior es un gradiente; en el segundo, $\partial^2/\partial x_i\partial x_i=\nabla^2$ actúa sobre $v_k\hat{e}_k=\vec v$:
> $$=\frac{\partial}{\partial x_k}\left(\frac{\partial v_i}{\partial x_i}\right)\hat{e}_k-\frac{\partial}{\partial x_i}\frac{\partial}{\partial x_i}\big(v_k\hat{e}_k\big).$$
>
> **Paso 6.** En notación vectorial:
> $$\vec\nabla\times\vec\nabla\times\vec v=\vec\nabla(\vec\nabla\cdot\vec v)-\nabla^2\vec v.\qquad\blacksquare$$

> [!info] Laplaciano escalar y vectorial
> El laplaciano actúa tanto sobre campos escalares como vectoriales. En $\vec\nabla\cdot(\vec\nabla\Phi)=\nabla^2\Phi$ opera sobre un escalar y devuelve un escalar; en el rotor del rotor opera sobre $\vec v$ componente a componente y devuelve un vector. Aplicando esta segunda identidad a los campos de Maxwell aparece $\nabla^2\vec E$ junto a $\partial^2\vec E/\partial t^2$: la **ecuación de ondas** electromagnéticas.

## Resumen

> [!resumen]
> | Identidad | Resultado |
> |---|---|
> | $\vec\nabla\cdot(\vec\nabla\Phi)$ | $\nabla^2\Phi$ |
> | $\nabla^2$ | $\partial^2/\partial x_1^2+\partial^2/\partial x_2^2+\partial^2/\partial x_3^2$ |
> | $\vec\nabla\times\vec\nabla\times\vec v$ | $\vec\nabla(\vec\nabla\cdot\vec v)-\nabla^2\vec v$ |
> | Herramienta clave | $\hat{e}_i\cdot\hat{e}_j=\delta_{ij}$ y $\varepsilon_{rsj}\varepsilon_{ikj}=\delta_{ri}\delta_{sk}-\delta_{rk}\delta_{si}$ |

> [!corolario]
> En cartesianas, las identidades entre operadores se reducen a álgebra de $\delta_{ij}$ y $\varepsilon_{ijk}$. El rotor del rotor, $\vec\nabla\times\vec\nabla\times\vec v=\vec\nabla(\vec\nabla\cdot\vec v)-\nabla^2\vec v$, es el ingrediente que convierte las ecuaciones de Maxwell en la ecuación de ondas electromagnéticas.

> [!referencia]
> - Identidad de índices usada: [[1 Algebra Lineal y Notacion/Simbolos Especiales/Identidad Epsilon-Delta]].
> - Operadores que se combinan: [[Gradiente]], [[Divergencia]], [[Rotor]].
> - Delta de Kronecker: [[1 Algebra Lineal y Notacion/Simbolos Especiales/Delta Kronecker]].
