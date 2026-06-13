---
title: EDP No Lineales
tags:
  - ecuaciones
  - edp
  - teoria
  - avanzado
  - no-lineal
draft: false
aliases:
  - EDP no lineales
  - solitones
  - reacción-difusión
  - blow-up
  - Nonlinear PDE
---

# EDP No Lineales

> [!definicion]
> Una EDP es **no lineal** cuando la incógnita $u$ o sus derivadas aparecen de forma no lineal (como
> $u\,u_x$, $u^2$, $\sin u$…). El rasgo decisivo es que **falla el principio de superposición**: si
> $u_1$ y $u_2$ son soluciones, $u_1+u_2$ **no** lo es en general. Sin superposición se derrumban casi
> todas las herramientas del curso —separación de variables, series de Fourier, funciones de Green—,
> que descansaban en sumar soluciones simples. **No existe una teoría general** de las EDP no
> lineales: cada ecuación se estudia con métodos propios, y aparecen fenómenos **sin análogo lineal**
> —solitones, formación de patrones, explosión en tiempo finito, turbulencia—.

> [!info]
> Pieza de panorama de la [[Teoria Avanzada/index| Teoría Avanzada de EDP]]. Es el **tercer salto**:
> tras ampliar qué es derivar ([[Distribuciones y Soluciones Debiles| distribuciones]]) y elegir el
> espacio correcto ([[Espacios de Sobolev| espacios de Sobolev]]), aquí se abandona la linealidad.
> Conecta con los choques de [[Ondas de Choque y Burgers| Burgers]]. Cierre del
> [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]].

---

## Ejemplo

> [!ejemplo] Un solitón de Korteweg-de Vries
> La ecuación de **Korteweg-de Vries (KdV)**
> $$u_t+6u\,u_x+u_{xxx}=0$$
> admite **ondas solitarias** llamadas **solitones**, de perfil
> $$u(x,t)=\tfrac{c}{2}\,\operatorname{sech}^2\!\Big(\tfrac{\sqrt c}{2}\,(x-ct)\Big).$$
> Es una joroba con forma de campana ($\operatorname{sech}^2$) que viaja **sin deformarse** a
> velocidad $c$. Lo notable es la relación **altura-velocidad**: cuanto **más alto** es el solitón
> (mayor $c$), **más rápido** viaja y más estrecho es. Si un solitón alto alcanza a uno más bajo, lo
> atraviesa y **ambos reemergen con su forma intacta**, como si fueran partículas (de ahí el sufijo
> "-ón"). Esto ocurre por un equilibrio fino entre la **no linealidad** $6uu_x$ (que tiende a empinar
> el frente, como en un choque) y la **dispersión** $u_{xxx}$ (que tiende a desparramarlo): se
> compensan exactamente y el perfil se estabiliza.

---

## En qué consiste

> [!teoria] Catálogo de fenómenos no lineales
> No hay un teorema único, pero sí una **galería de comportamientos** característicos, cada uno
> ilustrado por una ecuación de cabecera:
>
> - **Solitones** — la ecuación de **Korteweg-de Vries** $u_t+6u\,u_x+u_{xxx}=0$ tiene ondas
>   solitarias que mantienen su forma y **sobreviven a las colisiones**. Nacen del balance entre no
>   linealidad y dispersión. Aparecen en canales de agua poco profunda, fibras ópticas y plasmas.
>
> - **Choques** — la ecuación de **Burgers** $u_t+u\,u_x=0$ (no viscosa) empina sus frentes hasta
>   formar **discontinuidades** en tiempo finito: cada altura viaja a su propia velocidad y las
>   características se cruzan. Es el ejemplo elemental de cómo la no linealidad **destruye la
>   suavidad** (ver [[Ondas de Choque y Burgers| Burgers]]).
>
> - **Formación de patrones** — los sistemas de **reacción-difusión**, como **Fisher-KPP**
>   $u_t=Du_{xx}+u(1-u)$ o el **mecanismo de Turing** (dos especies que difunden a ritmos distintos),
>   muestran algo contraintuitivo: la difusión, que aislada **uniformiza**, al acoplarse con la
>   reacción **crea** estructura espacial estable —manchas, franjas, hexágonos—. Es el modelo de los
>   patrones del pelaje animal y de la morfogénesis en biología.
>
> - **Explosión (blow-up)** — ecuaciones con no linealidades **superlineales**, como
>   $u_t=u_{xx}+u^2$, pueden tener soluciones que **divergen a infinito en tiempo finito**: la
>   solución existe solo hasta un instante $T^*<\infty$ y deja de existir después. El crecimiento se
>   autoalimenta más rápido de lo que la difusión puede disipar.
>
> - **Turbulencia** — las ecuaciones de **Navier-Stokes** gobiernan los fluidos viscosos; su término
>   no lineal $(\mathbf u\cdot\nabla)\mathbf u$ es el responsable de la **turbulencia**. Saber si en
>   3D existen soluciones suaves **globales** (que nunca exploten) es uno de los **problemas del
>   milenio** y permanece **abierto**.

> [!proposicion] Por qué la no linealidad cambia todo
> En una EDP **lineal** el espacio de soluciones es un **espacio vectorial**: se construyen
> soluciones complicadas sumando simples (modos de Fourier, núcleos de Green). En una EDP **no
> lineal** ese espacio **no es vectorial**, y la dinámica puede ser cualitativamente nueva: la
> amplitud influye en la velocidad (solitones), la suavidad se pierde sola (choques), la difusión
> organiza en vez de disipar (Turing), o la solución simplemente **cesa de existir** (blow-up).
> Ninguno de estos fenómenos tiene análogo en el mundo lineal.

> [!warning]
> Esta es una nota de **panorama**, no un tratado. Cada uno de estos temas —solitones e
> integrabilidad, leyes de conservación con choques, reacción-difusión, blow-up, Navier-Stokes— es un
> **campo de investigación propio**, con su propia maquinaria y problemas abiertos. El objetivo aquí
> es solo dibujar el mapa de lo que aguarda más allá de la teoría lineal del curso.

---

## Resumen

> [!resumen]
>
> | Fenómeno | Ecuación de cabecera | Rasgo distintivo |
> |---|---|---|
> | Solitones | KdV $u_t+6uu_x+u_{xxx}=0$ | onda que viaja sin deformarse; sobrevive colisiones |
> | Choques | Burgers $u_t+uu_x=0$ | la suavidad se pierde en tiempo finito |
> | Patrones | reacción-difusión (Fisher-KPP, Turing) | la difusión **crea** estructura espacial |
> | Explosión | $u_t=u_{xx}+u^2$ | la solución diverge en tiempo finito $T^*$ |
> | Turbulencia | Navier-Stokes 3D | regularidad global: **problema del milenio abierto** |
>
> Hilo conductor: sin **superposición** no hay teoría general; cada ecuación es un mundo.

> [!corolario]
> La no linealidad no es una complicación técnica más: es la fuente de la **riqueza** de la física de
> EDP. Justo donde se rompe la superposición aparecen los fenómenos más interesantes —y los problemas
> más difíciles aún sin resolver—.

> [!referencia]
> Tercer y último salto de la [[Teoria Avanzada/index| Teoría Avanzada]], tras
> [[Distribuciones y Soluciones Debiles| distribuciones]] y
> [[Espacios de Sobolev| espacios de Sobolev]]. Modelo elemental de choque en
> [[Ondas de Choque y Burgers| Burgers]]. Cierre del
> [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]].
