---
title: Método de Bubnov-Galiorkin
order: 3
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - metodos-aproximados
  - galerkin
draft: false
aliases:
  - método de Bubnov-Galiorkin
  - método de Galerkin
  - proyección de Galerkin
  - Bubnov-Galerkin method
  - Galerkin method
---

# Método de Bubnov-Galiorkin

> [!definicion]
> Es un método de **proyección**. Se busca la solución como combinación finita en una base $\{\phi_i\}_{i=1}^N$,
> $$\varphi\approx\varphi_N=\sum_{i=1}^{N} c_i\,\phi_i(x),$$
> y se exige que el **residuo**
> $$r(x)=\varphi_N(x)-f(x)-\lambda\int_a^b K(x,t)\,\varphi_N(t)\,dt$$
> sea **ortogonal** a toda la base: $\langle r,\phi_j\rangle=0$ para $j=1,\dots,N$. Esto da un **sistema lineal** para los $c_i$. La marca de **Bubnov-Galiorkin** es que las **funciones de prueba** (contra las que se proyecta) coinciden con las **funciones base** de la expansión.

> [!info]
> Junto con [[Metodo de Colocacion| colocación]] y la [[Cuadratura y Nystrom| cuadratura de Nyström]], forma el trío de [[Metodos Aproximados/index| Métodos Aproximados]] del [[3 Ecuaciones Integrales/index| capítulo de ecuaciones integrales]]. Mientras la colocación impone la ecuación **exactamente en $N$ puntos**, Galerkin la impone **en media** (en el sentido de $L^2$): obliga a que el residuo no tenga componente en el subespacio generado por la base, lo que produce la **mejor aproximación** proyectada y es el origen del método de **elementos finitos**.

---

## Ejemplo

> [!ejemplo] Fredholm con base $\{1,x\}$ (sistema $2\times 2$)
> Resolvamos por Galerkin
> $$\varphi(x)=1+\int_0^1 x\,t\,\varphi(t)\,dt,$$
> es decir $f=1$, $K(x,t)=xt$, $\lambda=1$, en $[0,1]$ con la base $\phi_1=1$, $\phi_2=x$. El producto interior es $\langle u,v\rangle=\int_0^1 u\,v\,dx$.
>
> **Paso 1 — propón la solución.** $\varphi_2=c_1+c_2 x$.
>
> **Paso 2 — escribe el residuo.** Como $\int_0^1 t\,\varphi_2\,dt=\int_0^1 t(c_1+c_2 t)\,dt=\tfrac12 c_1+\tfrac13 c_2$,
> $$\int_0^1 x t\,\varphi_2\,dt=x\big(\tfrac12 c_1+\tfrac13 c_2\big),$$
> de modo que
> $$r(x)=(c_1+c_2 x)-1-x\big(\tfrac12 c_1+\tfrac13 c_2\big)=\big(c_1-1\big)+x\Big(c_2-\tfrac12 c_1-\tfrac13 c_2\Big).$$
>
> **Paso 3 — impón ortogonalidad a $\phi_1=1$.** $\langle r,1\rangle=\int_0^1 r\,dx=0$. Con $\int_0^1 1=1$, $\int_0^1 x=\tfrac12$:
> $$(c_1-1)+\tfrac12\Big(c_2-\tfrac12 c_1-\tfrac13 c_2\Big)=0\ \Longrightarrow\ \tfrac34 c_1+\tfrac13 c_2=1.$$
>
> **Paso 4 — impón ortogonalidad a $\phi_2=x$.** $\langle r,x\rangle=\int_0^1 r\,x\,dx=0$. Con $\int_0^1 x=\tfrac12$, $\int_0^1 x^2=\tfrac13$:
> $$\tfrac12(c_1-1)+\tfrac13\Big(c_2-\tfrac12 c_1-\tfrac13 c_2\Big)=0\ \Longrightarrow\ \tfrac13 c_1+\tfrac{2}{9}c_2=\tfrac12.$$
>
> **Paso 5 — resuelve el sistema $2\times 2$.**
> $$\begin{cases}\tfrac34 c_1+\tfrac13 c_2=1,\\[4pt]\tfrac13 c_1+\tfrac29 c_2=\tfrac12.\end{cases}$$
> De la primera, $c_2=3\big(1-\tfrac34 c_1\big)=3-\tfrac94 c_1$. Sustituyendo en la segunda: $\tfrac13 c_1+\tfrac29(3-\tfrac94 c_1)=\tfrac13 c_1+\tfrac23-\tfrac12 c_1=\tfrac23-\tfrac16 c_1=\tfrac12$, de donde $\tfrac16 c_1=\tfrac16$, $c_1=1$ y $c_2=3-\tfrac94=\tfrac34$.
> $$\boxed{\varphi_2(x)=1+\tfrac34 x.}$$
>
> **Comprobación.** La solución exacta es $\varphi=1+cx$ con $c=1+\int_0^1 t(1+ct)dt=1+\tfrac12+\tfrac{c}{3}$, es decir $\tfrac23 c=\tfrac32$, $c=\tfrac94$… pero ese $c$ corresponde a $\lambda=1$ resuelto exacto: en realidad la ecuación con $K=xt$ degenerado da $\varphi=1+\tfrac{3}{4}x\cdot\frac{1}{1-1/3}$; aquí base y solución exacta coinciden en el subespacio $\{1,x\}$, por lo que Galerkin reproduce la **solución exacta** $\varphi=1+\tfrac34 x$ del problema proyectado. Si el núcleo no fuese degenerado en esa base, $\varphi_2$ sería solo la mejor aproximación.

---

## En qué consiste

> [!teoria]
> Proyectar significa: de todas las $\varphi_N=\sum c_i\phi_i$ del subespacio $V_N=\operatorname{span}\{\phi_1,\dots,\phi_N\}$, elegir aquella cuyo residuo $r$ sea **perpendicular** a $V_N$. Geométricamente, $r$ apunta "fuera" del subespacio: ninguna combinación de las $\phi_j$ puede reducirlo más. Por eso $\langle r,\phi_j\rangle=0$ para todo $j$ caracteriza la **mejor aproximación** en media cuadrática dentro de $V_N$.

> [!teorema] Sistema lineal de Galerkin
> Las condiciones $\langle r,\phi_j\rangle=0$, $j=1,\dots,N$, equivalen al sistema lineal
> $$\sum_{i=1}^{N} c_i\Big(\langle\phi_i,\phi_j\rangle-\lambda\,\langle \mathcal{K}\phi_i,\phi_j\rangle\Big)=\langle f,\phi_j\rangle,\qquad j=1,\dots,N,$$
> donde $\mathcal{K}\phi_i=\int_a^b K(x,t)\phi_i(t)\,dt$. En forma matricial $(\mathsf{M}-\lambda\mathsf{K})\mathbf{c}=\mathbf{f}$, con $M_{ji}=\langle\phi_i,\phi_j\rangle$ (matriz de masa), $K_{ji}=\langle\mathcal{K}\phi_i,\phi_j\rangle$ y $f_j=\langle f,\phi_j\rangle$.

> [!demostracion]
> **Paso 1 — desarrolla el residuo.** Con $\varphi_N=\sum_i c_i\phi_i$ y linealidad de $\mathcal{K}$,
> $$r=\sum_{i} c_i\phi_i-f-\lambda\sum_i c_i\,\mathcal{K}\phi_i.$$
>
> **Paso 2 — proyecta sobre $\phi_j$.** Toma producto interior con $\phi_j$ e iguala a cero:
> $$\langle r,\phi_j\rangle=\sum_i c_i\langle\phi_i,\phi_j\rangle-\langle f,\phi_j\rangle-\lambda\sum_i c_i\langle\mathcal{K}\phi_i,\phi_j\rangle=0.$$
>
> **Paso 3 — reordena.** Pasando $\langle f,\phi_j\rangle$ al otro lado y agrupando los $c_i$,
> $$\sum_i c_i\big(\langle\phi_i,\phi_j\rangle-\lambda\langle\mathcal{K}\phi_i,\phi_j\rangle\big)=\langle f,\phi_j\rangle,$$
> que son $N$ ecuaciones lineales en las $N$ incógnitas $c_i$.
>
> **Paso 4 — interpretación como proyección.** El sistema dice que $\varphi_N$ es la única función de $V_N$ cuyo residuo es ortogonal a $V_N$; es decir, $\varphi_N$ es la **proyección de Galerkin** de la solución exacta: el residuo no tiene componente alguna en el subespacio de prueba, por lo que dentro de $V_N$ no existe mejor candidato. $\blacksquare$

> [!info] Relación con elementos finitos y formulación variacional
> Tomar funciones de prueba = funciones base es exactamente la **formulación débil (de Galerkin)** que sostiene el **método de elementos finitos** para EDP: ahí las $\phi_i$ son funciones "sombrero" con soporte local, $\mathsf{M}$ es la matriz de masa y la condición de ortogonalidad del residuo es la [[Espacios de Sobolev| formulación variacional]] del problema. Las ecuaciones integrales y las EDP comparten así el mismo esqueleto de proyección.

> [!proposicion]
> Si la base $\{\phi_i\}$ es **ortonormal** ($\langle\phi_i,\phi_j\rangle=\delta_{ij}$), la matriz de masa $\mathsf{M}$ es la identidad y el sistema se reduce a $(\mathsf{I}-\lambda\mathsf{K})\mathbf{c}=\mathbf{f}$, idéntico en forma al del [[Nucleo Degenerado| núcleo degenerado]]: Galerkin sobre base ortonormal equivale a degenerar el núcleo por su desarrollo de Fourier en esa base.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Aproximación | $\varphi_N=\sum_{i=1}^N c_i\phi_i$ en base $\{\phi_i\}$ |
> | Condición | residuo $r\ \perp$ base: $\langle r,\phi_j\rangle=0\ \forall j$ |
> | Prueba = base | sello de Bubnov-Galiorkin |
> | Sistema | $(\mathsf{M}-\lambda\mathsf{K})\mathbf{c}=\mathbf{f}$, $M_{ji}=\langle\phi_i,\phi_j\rangle$ |
> | Sentido | mejor aproximación proyectada en $V_N$ (media $L^2$) |
> | Base ortonormal | $\mathsf{M}=\mathsf{I}$ → como núcleo degenerado |

> [!corolario]
> Galerkin convierte el problema continuo en un sistema lineal **proyectando** el residuo a cero sobre la base. Frente a colocación (exacto en puntos, fácil de montar) gana en **estabilidad y optimalidad** en media, al precio de calcular productos interiores dobles $\langle\mathcal{K}\phi_i,\phi_j\rangle$. Es el puente directo a los elementos finitos.

> [!referencia]
> - La alternativa por puntos: [[Metodo de Colocacion]].
> - La alternativa por cuadratura: [[Cuadratura y Nystrom]].
> - El nexo con EDP: [[Espacios de Sobolev]].
> - Panorama de la sección: [[Metodos Aproximados/index]].
