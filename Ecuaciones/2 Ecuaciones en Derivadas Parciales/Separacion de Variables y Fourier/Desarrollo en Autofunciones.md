---
title: Desarrollo en Autofunciones
order: 6
tags:
  - ecuaciones
  - edp
  - teoria
  - fourier
  - autofunciones
draft: false
aliases:
  - desarrollo en autofunciones
  - Fourier generalizado
  - serie de Fourier-Bessel
  - serie de Legendre
  - eigenfunction expansion
  - generalized Fourier series
---

# Desarrollo en Autofunciones (Fourier Generalizado)

> [!definicion]
> Una función $f$ no solo se desarrolla en senos y cosenos: puede expandirse en las **autofunciones** $\{\varphi_n\}$ de **cualquier** problema de [[Sturm-Liouville/index| Sturm-Liouville]],
> $$f(x)=\sum_{n}c_n\,\varphi_n(x),\qquad
> c_n=\frac{\displaystyle\int f(x)\,\varphi_n(x)\,w(x)\,dx}{\displaystyle\int \varphi_n(x)^2\,w(x)\,dx},$$
> donde $w(x)>0$ es la **función de peso** respecto a la cual las autofunciones son **ortogonales**. Esto es el **Fourier generalizado**. Los senos y cosenos son solo el caso particular del **laplaciano** $-X''=\lambda X$ en $[0,L]$ con peso $w\equiv 1$.

> [!info]
> Generaliza las [[Series de Fourier]] usando la maquinaria de las [[Funciones Ortogonales| funciones ortogonales]]. Es la pieza que hace funcionar la [[Separacion de Variables y Fourier/index| separación de variables]] cuando el dominio **no** es un segmento recto, dentro del capítulo de [[2 Ecuaciones en Derivadas Parciales/index| Ecuaciones en Derivadas Parciales]]. Sin él, no se podría ajustar el dato inicial en geometrías curvas.

---

## Ejemplo

> [!ejemplo] Serie de Fourier-Bessel en el disco
> Al separar variables en el disco de radio $a$ (calor o membrana circular), la parte radial conduce a la **ecuación de Bessel**, cuyas soluciones regulares en el centro son $J_0(\alpha r/a)$. La condición de frontera $u=0$ en $r=a$ obliga a que $J_0(\alpha)=0$, es decir $\alpha=\alpha_n$ son los **ceros** de $J_0$ ($\alpha_1\approx2{.}405,\ \alpha_2\approx5{.}520,\dots$). Las autofunciones radiales son
> $$\varphi_n(r)=J_0\!\Big(\frac{\alpha_n r}{a}\Big),\qquad n=1,2,3,\dots$$
> y un perfil radial $f(r)$ se desarrolla como
> $$f(r)=\sum_{n=1}^{\infty}c_n\,J_0\!\Big(\frac{\alpha_n r}{a}\Big)\qquad(\text{serie de Fourier-Bessel}).$$
> **Cálculo de los coeficientes.** El problema de Sturm-Liouville radial tiene **peso $w(r)=r$** (viene del laplaciano en coordenadas polares). Proyectando con la ortogonalidad,
> $$c_n=\frac{\displaystyle\int_0^a f(r)\,J_0\!\big(\tfrac{\alpha_n r}{a}\big)\,r\,dr}
> {\displaystyle\int_0^a J_0\!\big(\tfrac{\alpha_n r}{a}\big)^2\,r\,dr}.$$
> La integral del denominador tiene fórmula cerrada, $\int_0^a J_0(\alpha_n r/a)^2\,r\,dr=\tfrac{a^2}{2}J_1(\alpha_n)^2$, de modo que
> $$c_n=\frac{2}{a^2 J_1(\alpha_n)^2}\int_0^a f(r)\,J_0\!\Big(\frac{\alpha_n r}{a}\Big)\,r\,dr.$$
> Es **exactamente** el mismo gesto que en Fourier clásico (multiplicar por la autofunción, integrar, dividir por su norma); solo cambian la autofunción $J_0$ y el peso $r$.

---

## En qué consiste

> [!teoria] Por qué Fourier no basta: geometrías curvas
> Separar variables en $[0,L]$ recto da $-X''=\lambda X$, cuyas autofunciones son senos/cosenos. Pero en cuanto el dominio se **curva**, el operador espacial deja de ser $\partial_{xx}$ puro:
> - en un **disco/cilindro**, la parte radial es la ecuación de **Bessel** → autofunciones $J_m$;
> - en una **esfera**, la parte polar es la ecuación de **Legendre** → autofunciones $P_\ell$ (polinomios de Legendre), y los [[Laplace en Esfera| armónicos esféricos]] en la angular completa.
>
> Todas comparten la **misma estructura**: son problemas de Sturm-Liouville, sus autofunciones son **ortogonales con un peso** $w$, y por eso el dato inicial o de frontera se ajusta por un **desarrollo** (serie de Fourier-Bessel, serie de Legendre…). La ortogonalidad —no la forma concreta de la autofunción— es lo que garantiza poder despejar cada coeficiente sin que los demás interfieran.

> [!proposicion] La receta es siempre la misma
> Dado un problema de Sturm-Liouville con autofunciones $\{\varphi_n\}$ ortogonales con peso $w$ y un dato $f$:
> 1. **Postular** el desarrollo $f=\sum_n c_n\varphi_n$.
> 2. **Proyectar**: multiplicar por $\varphi_m w$ e integrar. Por ortogonalidad, $\int f\varphi_m w=c_m\int\varphi_m^2 w$.
> 3. **Despejar** $c_m=\dfrac{\int f\varphi_m w\,dx}{\int\varphi_m^2 w\,dx}$.
>
> Cambian $\varphi_n$, $w$ y el intervalo; el **mecanismo** (proyección sobre base ortogonal) es idéntico al de Fourier clásico.

> [!info]
> El peso $w$ **no es decorativo**: es lo que hace ortogonales a las autofunciones. Para Bessel en el disco $w(r)=r$; para Legendre en la esfera $w=1$ en $[-1,1]$ tras el cambio $x=\cos\theta$. Olvidarlo rompe la ortogonalidad y los coeficientes salen mal. Conecta directamente con [[Laplace en Disco]] y [[Laplace en Esfera]], y con el catálogo de [[Funciones Especiales/index| funciones especiales]] que provee las autofunciones.

## Resumen

> [!resumen]
> | Geometría | Operador radial/angular | Autofunciones $\varphi_n$ | Peso $w$ |
> |:--|:--|:--|:--:|
> | Segmento $[0,L]$ | $-X''=\lambda X$ | $\operatorname{sen},\cos$ | $1$ |
> | Disco / cilindro | ec. de Bessel | $J_m(\alpha_n r/a)$ | $r$ |
> | Esfera | ec. de Legendre | $P_\ell(\cos\theta)$ | $1$ (en $x=\cos\theta$) |

> [!corolario]
> "Serie de Fourier" es solo el nombre del caso más simple de una idea mucho más amplia: **proyectar sobre las autofunciones de un operador autoadjunto**. Cambiar la geometría cambia las autofunciones (Bessel, Legendre, …), pero la ortogonalidad con su peso mantiene intacta la fórmula de los coeficientes. Por eso el mismo método resuelve EDP en cajas, discos y esferas.

> [!referencia]
> - La base ortogonal y su producto interno con peso: [[Funciones Ortogonales]].
> - El caso clásico senos/cosenos: [[Series de Fourier]].
> - El problema de autovalores que genera las autofunciones: [[Sturm-Liouville/index]].
> - El catálogo de autofunciones curvas: [[Funciones Especiales/index]].
> - El método global: [[Separacion de Variables y Fourier/index]].
