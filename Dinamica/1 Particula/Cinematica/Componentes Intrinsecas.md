---
title: Componentes Intrínsecas (Triedro de Frenet)
tags:
  - dinamica
  - teoria
  - particula
  - cinematica
draft: false
aliases:
  - componentes intrínsecas
  - triedro de Frenet
  - Frenet-Serret
  - curvatura y torsión
  - tangencial normal binormal
---

# Componentes Intrínsecas: el Triedro de Frenet $(\hat t,\hat n,\hat b)$

> [!definicion]
> Las **componentes intrínsecas** describen el movimiento en una base **ligada a la trayectoria**, el
> **triedro de Frenet-Serret**, que es **tridimensional**:
> - **tangente** $\hat t=\dfrac{\vec v}{v}$ (en el sentido del movimiento),
> - **normal principal** $\hat n$ (hacia el centro de curvatura, en el plano en que la curva se dobla),
> - **binormal** $\hat b=\hat t\times\hat n$ (perpendicular a ambos).
>
> La curva se caracteriza por la **curvatura** $\kappa=1/\rho$ (cuánto gira $\hat t$) y la **torsión**
> $\tau$ (cuánto se sale la curva del plano). La aceleración vive en el plano $(\hat t,\hat n)$:
> $$\vec a=\dot v\,\hat t+\frac{v^2}{\rho}\,\hat n.$$

> [!info]
> Primera nota de la [[Cinematica/index | cinemática de la partícula]]. El triedro de Frenet es una
> **base móvil**: sus versores giran con la partícula, igual que en el
> [[Operador Derivada en Base Movil | operador derivada en base móvil]]. Referencia: Taylor §1.7.

---

## Ejemplo

> [!ejemplo]
> **La aceleración no tiene componente binormal.**
>
> Una partícula recorre una curva alabeada (no plana) con rapidez $v$. Mostrar que su aceleración
> queda contenida en el **plano osculador** $(\hat t,\hat n)$, sin proyección sobre $\hat b$.
>
> ![[coordenadas_cinematica.svg|480]]
>
> *El plano osculador es el que contiene $\hat t$ y $\hat n$ (el de la figura, izquierda); la binormal
> $\hat b=\hat t\times\hat n$ sale de la página. La aceleración vive en ese plano.*
>
> **Paso 1 — Aceleración.** De $\vec v=v\,\hat t$ se obtiene (deducción abajo)
> $\vec a=\dot v\,\hat t+\dfrac{v^2}{\rho}\,\hat n$.
>
> **Paso 2 — Proyección binormal.** $\vec a\cdot\hat b=\dot v\,(\hat t\cdot\hat b)+\dfrac{v^2}{\rho}(\hat n\cdot\hat b)=0+0=0$.
>
> > [!solucion]
> > $\vec a\cdot\hat b=0$: **toda** la aceleración está en el plano osculador, por mucho que la curva
> > se retuerza en el espacio ($\tau\neq0$). La torsión describe cómo gira ese plano, pero no añade
> > aceleración fuera de él.

---

## En qué consiste

> [!teorema] Aceleración en el triedro de Frenet
> Con $\vec v=v\,\hat t$,
> $$\boxed{\;\vec a=\dot v\,\hat t+\frac{v^2}{\rho}\,\hat n\;}$$
> donde $\dot v$ es la **aceleración tangencial** (cambia la rapidez) y $v^2/\rho=\kappa v^2$ la
> **normal** o **centrípeta** (cambia la dirección), siempre hacia el centro de curvatura. **No hay
> componente binormal.**

> [!demostracion]
> **Paso 1 — Derivar $\vec v=v\,\hat t$:** $\vec a=\dot v\,\hat t+v\,\dfrac{d\hat t}{dt}$.
> **Paso 2 — Regla de la cadena con la longitud de arco $s$:**
> $\dfrac{d\hat t}{dt}=\dfrac{d\hat t}{ds}\dfrac{ds}{dt}=v\,\dfrac{d\hat t}{ds}$.
> **Paso 3 — Primera fórmula de Frenet:** $\dfrac{d\hat t}{ds}=\kappa\,\hat n=\dfrac{1}{\rho}\hat n$ (ver
> abajo). Sustituyendo, $\vec a=\dot v\,\hat t+v\!\left(v\,\dfrac{1}{\rho}\hat n\right)=\dot v\,\hat t+\dfrac{v^2}{\rho}\hat n$.
> Como $\dfrac{d\hat t}{ds}$ no tiene parte en $\hat b$, la aceleración tampoco. $\blacksquare$

> [!teorema] Fórmulas de Frenet-Serret
> Al avanzar sobre la curva, el triedro gira según
> $$\frac{d\hat t}{ds}=\kappa\,\hat n,\qquad \frac{d\hat n}{ds}=-\kappa\,\hat t+\tau\,\hat b,\qquad \frac{d\hat b}{ds}=-\tau\,\hat n,$$
> con $\kappa=1/\rho\ge0$ la **curvatura** y $\tau$ la **torsión**.

> [!demostracion]
> **$\hat t$:** $\hat t$ es unitario ($\hat t\cdot\hat t=1$), luego $d\hat t/ds\perp\hat t$. Se define
> la dirección de ese vector como $\hat n$ y su módulo como la **curvatura** $\kappa$:
> $d\hat t/ds=\kappa\,\hat n$.
> **$\hat b$:** de $\hat b\cdot\hat b=1$, $d\hat b/ds\perp\hat b$. De $\hat b\cdot\hat t=0$,
> derivando, $\dfrac{d\hat b}{ds}\cdot\hat t+\hat b\cdot\dfrac{d\hat t}{ds}=\dfrac{d\hat b}{ds}\cdot\hat t+\hat b\cdot(\kappa\hat n)=\dfrac{d\hat b}{ds}\cdot\hat t=0$.
> Así $d\hat b/ds$ es perpendicular a $\hat b$ y a $\hat t$, luego es paralelo a $\hat n$; se define la
> **torsión** por $d\hat b/ds=-\tau\,\hat n$.
> **$\hat n$:** como $\hat n=\hat b\times\hat t$,
> $\dfrac{d\hat n}{ds}=\dfrac{d\hat b}{ds}\times\hat t+\hat b\times\dfrac{d\hat t}{ds}=(-\tau\hat n)\times\hat t+\hat b\times(\kappa\hat n)=\tau\,\hat b-\kappa\,\hat t$.
> $\blacksquare$

> [!proposicion] El triedro es una base móvil (vector de Darboux)
> Las tres fórmulas se resumen en $\dfrac{d\hat e}{ds}=\vec\Omega\times\hat e$ con el **vector de
> Darboux** $\vec\Omega=\tau\,\hat t+\kappa\,\hat b$: el triedro de Frenet **gira** al avanzar, como
> cualquier base ligada a un cuerpo. Es el mismo mecanismo del
> [[Operador Derivada en Base Movil | operador en base móvil]], aquí parametrizado por el arco $s$.

> [!proposicion] La torsión mide la no-planaridad
> $\tau=0$ en todo punto $\iff$ la curva es **plana** (contenida en su plano osculador, que entonces
> es fijo). Una circunferencia tiene $\tau=0$ y $\kappa=1/R$ constantes; una **hélice** tiene $\kappa$ y
> $\tau$ ambos constantes y no nulos.

> [!warning]
> El triedro intrínseco es **3D**: aunque la aceleración no tenga componente binormal, $\hat b$ y la
> torsión existen y describen cómo se **alabea** la trayectoria. No confundir el **radio de curvatura**
> $\rho=1/\kappa$ (local, de la trayectoria) con ninguna coordenada radial. La normal $\hat n$ apunta
> siempre hacia el lado **cóncavo** (centro de curvatura), nunca hacia afuera.

## Resumen

> [!resumen]
> | Magnitud | Expresión |
> |:---|:---|
> | Triedro | $\hat t=\vec v/v$, $\hat n$ (normal principal), $\hat b=\hat t\times\hat n$ |
> | Velocidad | $\vec v=v\,\hat t$ |
> | Aceleración | $\vec a=\dot v\,\hat t+\dfrac{v^2}{\rho}\,\hat n$ (sin componente $\hat b$) |
> | Frenet-Serret | $\hat t'=\kappa\hat n$, $\;\hat n'=-\kappa\hat t+\tau\hat b$, $\;\hat b'=-\tau\hat n$ |
> | Curvatura / torsión | $\kappa=1/\rho$ (se dobla) / $\tau$ (se alabea) |

> [!corolario]
> La descripción intrínseca separa el movimiento en "acelerar" ($\dot v\,\hat t$) y "girar"
> ($v^2/\rho\,\hat n$), siempre en el plano osculador. La estructura completa —tangente, normal,
> binormal, curvatura y torsión— hace de la trayectoria una curva del espacio, no del plano.

> [!referencia]
> Taylor, §1.7. Base móvil general: [[Operador Derivada en Base Movil]]. Otras coordenadas:
> [[Coordenadas Cilindricas]] y [[Coordenadas Esfericas]].
