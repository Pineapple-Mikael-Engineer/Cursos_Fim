---
title: Laplace en Cilindro
order: 4
tags:
  - ecuaciones
  - edp
  - teoria
  - laplace
  - bessel
draft: false
aliases:
  - Laplace en un cilindro
  - separación cilíndrica
  - funciones de Bessel
  - Fourier-Bessel
  - Laplace in a cylinder
---

# Laplace en Cilindro

> [!definicion]
> En **coordenadas cilíndricas** $(r,\theta,z)$, la ecuación de Laplace es
> $$\nabla^2u=u_{rr}+\frac1r u_r+\frac1{r^2}u_{\theta\theta}+u_{zz}=0.$$
> La [[Tecnica de Separacion| separación]] $u=R(r)\,\Theta(\theta)\,Z(z)$ desacopla la ecuación en tres EDO: $\Theta$ queda **periódica** (índice $m=0,1,2,\dots$, $\Theta_m=\cos m\theta, \operatorname{sen} m\theta$); $Z$ da exponenciales o senos según el signo de la constante de separación $k^2$; y la parte **radial** obedece la **ecuación de Bessel**
> $$r^2R''+rR'+(k^2r^2-m^2)R=0,$$
> cuyas soluciones son las funciones de **Bessel** $J_m(kr)$ y $Y_m(kr)$ (o las **modificadas** $I_m(kr)$, $K_m(kr)$ si la constante entra con el signo opuesto). Bessel es, para la simetría cilíndrica, lo que el seno es para la cartesiana.

> [!info]
> Tercer escalón geométrico del [[Ecuacion de Laplace y Poisson/index| bloque de Laplace]]: tras el [[Laplace en Rectangulo| rectángulo]] (senos/$\sinh$) y el [[Laplace en Disco| disco]] (Fourier/Poisson), el cilindro **añade el eje $z$** y con él las funciones de Bessel. Es el antecesor directo de [[Laplace en Esfera]], donde la simetría esférica trae los armónicos esféricos.

---

## Ejemplo

> [!ejemplo] Potencial dentro de un cilindro con tapa a potencial $f$
> Cilindro $r\le a$, $0\le z\le L$, con lados a potencial cero, base a cero y **tapa** $u(r,\theta,L)=f(r)$ (dato con simetría axial, sin dependencia en $\theta$, así que $m=0$).
>
> **Paso 1 — Separar.** Con $u=R(r)Z(z)$ (axial, $\Theta=1$), de $\frac1{rR}(rR')'+\frac{Z''}{Z}=0$ tomamos $\frac{Z''}{Z}=k^2>0$ (crece hacia la tapa). La parte radial cumple entonces $\frac1r(rR')'+k^2R=0$, es decir
> $$r^2R''+rR'+k^2r^2R=0,$$
> que es la ecuación de Bessel de orden $m=0$ con argumento $kr$.
>
> **Paso 2 — Parte radial regular.** La solución general es $R=c_1J_0(kr)+c_2Y_0(kr)$. Como el dominio **incluye el eje** $r=0$ y $Y_0$ **diverge** allí, se descarta $c_2=0$:
> $$R(r)=J_0(kr).$$
>
> **Paso 3 — Cuantizar $k$ con los ceros de Bessel.** El lado del cilindro a cero exige $u(a,\theta,z)=0$, es decir $R(a)=J_0(ka)=0$. Esto **cuantiza** $k$: si $\alpha_n$ es el $n$-ésimo **cero de $J_0$** ($J_0(\alpha_n)=0$), entonces
> $$k_n=\frac{\alpha_n}{a},\qquad R_n(r)=J_0\!\Big(\frac{\alpha_n r}{a}\Big),\quad n=1,2,\dots$$
>
> **Paso 4 — Parte axial.** Con $Z''=k_n^2Z$ y la base $u(r,\theta,0)=0$ ($Z(0)=0$), queda $Z_n(z)=\sinh(k_n z)$.
>
> **Paso 5 — Serie de Fourier-Bessel.** Superponiendo,
> $$u(r,z)=\sum_{n=1}^\infty c_n\,J_0\!\Big(\frac{\alpha_n r}{a}\Big)\,\sinh(k_n z),$$
> e imponiendo la tapa $u(r,L)=f(r)$ se obtienen los $c_n$ por **ortogonalidad de Bessel**:
> $$c_n\sinh(k_n L)=\frac{2}{a^2J_1(\alpha_n)^2}\int_0^a f(r)\,J_0\!\Big(\frac{\alpha_n r}{a}\Big)\,r\,dr.$$
> El papel que en el disco jugaba la serie de Fourier lo juega aquí la **serie de Fourier-Bessel**.

---

## En qué consiste

> [!teoria] El reparto de las tres direcciones
> La separación cilíndrica reparte el trabajo entre las tres coordenadas:
> - **$\theta$** (angular): siempre **periódica**, da $\cos m\theta,\operatorname{sen} m\theta$ con $m$ entero. Fija el **orden** $m$ de las Bessel.
> - **$z$** (axial): según el signo de la constante de separación, da $\sinh/\cosh$ (modos que crecen/decaen) o $\operatorname{sen}/\cos$ (modos oscilantes). Es la dirección "abierta".
> - **$r$** (radial): obedece **Bessel**; el signo de la constante decide entre $J_m,Y_m$ (oscilatorias, problema interior con dato en la tapa) y $I_m,K_m$ (monótonas, problema con dato en el lado lateral).
>
> La **condición homogénea** en $r=a$ o en $z$ es la que cuantiza el espectro: o bien los ceros de Bessel $J_m(k a)=0$, o bien $\sin(k L)=0$, según dónde esté el dato.

> [!info]
> **Por qué Bessel.** Al separar la parte radial del laplaciano en simetría cilíndrica aparece el término $\frac1r R'$ y el $\frac{m^2}{r^2}R$, que convierten la ecuación armónica simple en la de Bessel. $J_m$ es literalmente la "función trigonométrica" de esta geometría: oscila pero con amplitud decreciente y espaciado de ceros no uniforme. El catálogo y propiedades de estas funciones se desarrollan en [[Funciones Especiales/index]].

> [!warning]
> Distinguir bien las dos soluciones radiales: $J_m(kr)$ es **regular** en $r=0$, mientras que $Y_m(kr)$ es **singular** ($Y_m\to-\infty$ cuando $r\to0$). Si el dominio **incluye el eje** (cilindro macizo), se **descarta** $Y_m$ por física: el potencial no puede divergir en el centro. $Y_m$ solo sobrevive en dominios tipo **corona cilíndrica** ($0<b\le r\le a$), que excluyen el eje. El mismo cuidado vale para $K_m$ frente a $I_m$ en el caso modificado.

## Resumen

> [!resumen]
> | Dirección | Ecuación | Soluciones | Quién la fija |
> |---|---|---|---|
> | $\theta$ | $\Theta''+m^2\Theta=0$ | $\cos m\theta,\operatorname{sen} m\theta$ | periodicidad ($m$ entero) |
> | $z$ | $Z''\mp k^2Z=0$ | $\sinh/\cosh$ o $\operatorname{sen}/\cos$ | dato axial |
> | $r$ | $r^2R''+rR'+(k^2r^2-m^2)R=0$ | $J_m,Y_m$ (o $I_m,K_m$) | ceros de Bessel / dato lateral |
> | regularidad | — | se descarta $Y_m$ (o $K_m$) si entra el eje | $r=0\in\Omega$ |

> [!corolario]
> El cilindro es el disco "con altura": la periodicidad angular y la regularidad en el eje siguen mandando, pero la coordenada radial pasa de $r^n$ a las **funciones de Bessel**, y el dato sobre una cara se desarrolla en **serie de Fourier-Bessel** usando los ceros de $J_m$ y su ortogonalidad.

> [!referencia]
> - El siguiente paso geométrico: [[Laplace en Esfera]].
> - El caso plano sin eje $z$: [[Laplace en Disco]].
> - Las funciones de Bessel en detalle: [[Funciones Especiales/index]].
> - Marco general: [[Ecuacion de Laplace y Poisson/index]].
