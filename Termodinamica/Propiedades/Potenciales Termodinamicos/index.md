---
title: "Potenciales Termodinámicos"
order: 2
tags:
  - termodinamica
  - potenciales_termodinamicos
  - index
draft: false
aliases:
  - thermodynamic potentials
  - potenciales termodinámicos
  - energías libres
---

# Potenciales Termodinámicos

> [!definicion]
> Los **potenciales termodinámicos** son cuatro funciones de estado — $U$, $H$, $F$, $G$ — derivadas de la **relación fundamental** $dU = T\,dS - P\,dV$ mediante **transformadas de Legendre**. Cada una está optimizada para un par de variables independientes: la que se obtiene con variables naturales $(S,V)$ es $U$; intercambiando $V$ por $P$ se obtiene $H(S,P)$; intercambiando $S$ por $T$ se obtiene $F(T,V)$; intercambiando ambos se obtiene $G(T,P)$. La importancia es práctica: para cada par de variables que se mantienen fijas en un proceso, hay un potencial cuyo mínimo caracteriza el equilibrio, y cuyo diferencial genera directamente las relaciones entre propiedades.

---

## Por qué existen cuatro potenciales: el problema con $U(S,V)$

> [!teoria]
> La relación fundamental $dU = T\,dS - P\,dV$ es exacta y completa: toda la termodinámica de una sustancia simple compresible está contenida en ella. Pero sus variables naturales $(S, V)$ son inconvenientes:
> - $S$ (entropía) no es directamente medible ni fácilmente controlable en el laboratorio.
> - $V$ (volumen) es fijo en recipientes rígidos pero variable en procesos a presión constante.
>
> En la práctica, los procesos industriales se llevan a cabo a $P$ constante (reactores abiertos, turbinas, calderas) o a $T$ constante (baños térmicos, condensadores). Se necesita una forma de la energía termodinámica que tenga como variables naturales las que uno realmente controla. La solución es la **transformada de Legendre**.

---

## La transformada de Legendre: intercambiar una variable extensiva por su conjugada intensiva

> [!teoria]
> Si $U = U(S,V)$ con $dU = T\,dS - P\,dV$, se puede construir una nueva función que cambie una variable:
>
> **Intercambiar $V$ por $P$** (conjugada de $V$): sumar $PV$ a $U$:
> $$H \equiv U + PV \implies dH = T\,dS + V\,dP. \quad \text{Variables naturales: }(S,P).$$
>
> **Intercambiar $S$ por $T$** (conjugada de $S$): restar $TS$ a $U$:
> $$F \equiv U - TS \implies dF = -S\,dT - P\,dV. \quad \text{Variables naturales: }(T,V).$$
>
> **Intercambiar ambos** ($S\to T$ y $V\to P$):
> $$G \equiv U - TS + PV = H - TS \implies dG = -S\,dT + V\,dP. \quad \text{Variables naturales: }(T,P).$$
>
> En todos los casos, la transformada sustituye una variable extensiva ($S$ o $V$) por su conjugada intensiva ($T$ o $P$), sin perder información: el potencial original se puede recuperar. El precio es que la información ahora está codificada en un potencial diferente.

![[potenciales_cuadro_Born.svg|380]]
*Cuadro mágico de Born: los cuatro potenciales en las esquinas del cuadrado; las variables de estado en los lados. Cada potencial tiene como variables naturales los dos lados adyacentes. Las flechas sobre los lados indican el signo de la derivada correspondiente: hacia la flecha → derivada positiva; contra la flecha → negativa.*

---

## Los cuatro potenciales: tabla maestra

> [!teoria]
> | Potencial | Definición | Diferencial | Variables naturales | Derivadas primeras |
> |:---|:---|:---|:---:|:---|
> | [[Energia Interna\|Energía Interna]] $U$ | — | $dU = T\,dS - P\,dV$ | $(S,\,V)$ | $T=(\partial U/\partial S)_V$; $-P=(\partial U/\partial V)_S$ |
> | [[Entalpia]] $H$ | $U+PV$ | $dH = T\,dS + V\,dP$ | $(S,\,P)$ | $T=(\partial H/\partial S)_P$; $V=(\partial H/\partial P)_S$ |
> | [[Helmholtz]] $F$ | $U-TS$ | $dF = -S\,dT - P\,dV$ | $(T,\,V)$ | $-S=(\partial F/\partial T)_V$; $-P=(\partial F/\partial V)_T$ |
> | [[Gibbs]] $G$ | $H-TS$ | $dG = -S\,dT + V\,dP$ | $(T,\,P)$ | $-S=(\partial G/\partial T)_P$; $V=(\partial G/\partial P)_T$ |
>
> De la igualdad de derivadas cruzadas de cada diferencial surgen las cuatro [[Maxwell | relaciones de Maxwell]] (una por potencial).

---

## Significado físico de cada potencial

> [!teoria]
> - **$U(S,V)$**: energía total microscópica del sistema (cinética + potencial de interacción molecular). Es la fuente de toda la termodinámica, pero incómoda como variable de trabajo.
> - **$H(S,P)$**: energía que "lleva" un fluido en flujo estacionario — incluye $U$ más el trabajo de empuje $PV$ necesario para mover el fluido contra la presión. Por eso los balances de flujo usan $h$, no $u$.
> - **$F(T,V)$**: "energía libre de Helmholtz" — la parte de $U$ que puede convertirse en trabajo a temperatura constante. En un proceso isotérmico reversible, el trabajo extraído es exactamente $-\Delta F$. Útil en procesos a temperatura controlada.
> - **$G(T,P)$**: "energía libre de Gibbs" — la parte de $H$ disponible como trabajo útil (no de frontera $PdV$) a $T$ y $P$ constantes. Es el potencial más relevante en química, cambios de fase y equilibrio: la mayoría de los procesos industriales ocurren a $P$ ≈ cte y con baño térmico.

---

## Criterios de equilibrio: el potencial correcto para cada condición

> [!proposicion]
> Para un sistema **aislado** (constante $U$ y $V$), el equilibrio maximiza $S$:
> $$\delta S = 0, \quad \delta^2 S < 0 \qquad (U,V \text{ const.})$$
> Equivalentemente, para las condiciones controladas más comunes:
>
> | Condición externa | El equilibrio corresponde al mínimo de: |
> |:---|:---|
> | $S$ y $V$ constantes | $U$ (energía interna) |
> | $S$ y $P$ constantes | $H$ (entalpía) |
> | $T$ y $V$ constantes | $F$ (Helmholtz) |
> | $T$ y $P$ constantes | $G$ (Gibbs) ← condición más común en ingeniería |
>
> El criterio de mínimo en $G$ a $(T,P)$ constantes es el que rige los cambios de fase (ebullición, solidificación), las reacciones químicas reversibles y el equilibrio entre fases en mezclas.

---

## Mapa de notas

> [!info]
> - [[Energia Interna]] (order 1) — $U(S,V)$; relación fundamental; experimento de Joule.
> - [[Entalpia]] (order 2) — $H(S,P)$; flujo estacionario; por qué $h$ y no $u$.
> - [[Entropia]] (order 3) — $S$; segunda ley; producción de entropía; Boltzmann.
> - [[Helmholtz]] (order 4) — $F(T,V)$; trabajo máximo isotérmico.
> - [[Gibbs]] (order 5) — $G(T,P)$; equilibrio de fases; potencial químico; Gibbs-Duhem.
> - [[Exergia]] (order 6) — trabajo útil máximo respecto al ambiente; destrucción de exergía.
> - Las cuatro relaciones de Maxwell derivadas de estos potenciales se desarrollan en [[Maxwell]].

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, §12.1–12.3; Callen, *Thermodynamics*, caps. 5–6; Çengel & Boles, *Termodinámica*, §12-1; Moran & Shapiro, §11.1.
