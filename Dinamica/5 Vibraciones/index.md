---
title: Vibraciones
order: 5
tags:
  - dinamica
  - teoria
  - vibraciones
  - index
draft: false
aliases:
  - vibraciones
  - oscilaciones
  - oscilador armónico
---

# Vibraciones

> [!definicion]
> Una **vibración** es un movimiento **oscilatorio** en torno a una posición de equilibrio. Su modelo universal es el sistema **masa-resorte-amortiguador**,
> $$m\ddot x+c\dot x+kx=F(t),$$
> cuya **frecuencia natural** es $\omega_n=\sqrt{k/m}$. Según haya o no excitación se distingue vibración **libre** ($F=0$) y **forzada**; según haya o no rozamiento, **amortiguada** o no.

> [!info]
> Quinto y último bloque del curso de [[Dinamica/index | Dinámica]]. Es una aplicación directa de las [[Cinetica de la Particula | leyes de Newton]] a un sistema lineal de un grado de libertad. Referencia: Taylor cap. 5.

---

## El oscilador, modelo de todo equilibrio

> [!teoria] Por qué el masa-resorte es universal
> Cerca de un equilibrio **estable**, cualquier sistema se comporta como un oscilador: desarrollando la energía potencial $V(x)$ en serie en torno al mínimo $x_0$, $V(x)\approx V(x_0)+\tfrac12 V''(x_0)(x-x_0)^2$, la fuerza recuperadora es $-V''(x_0)(x-x_0)$, es decir un **resorte efectivo** $k=V''(x_0)$. Por eso el péndulo, una molécula o un circuito $LC$ oscilan todos como un masa-resorte: dominarlo es dominar las pequeñas oscilaciones de **todo** equilibrio.
>
> ![[masa_resorte.svg|470]]
>
> *El sistema masa-resorte-amortiguador: el resorte $k$ recupera, el amortiguador $c$ disipa, y $m\ddot x+c\dot x+kx=F(t)$.*

> [!teoria] Libre, amortiguada y forzada
> - **Vibración libre.** Sin excitación: el sistema oscila a su frecuencia natural $\omega_n$, y el amortiguamiento $\zeta$ decide si oscila (subamortiguado), vuelve sin oscilar (crítico) o repta (sobreamortiguado). → [[Vibracion Libre]].
> - **Vibración forzada.** Con una excitación armónica, el sistema responde a la frecuencia de ésta; si se acerca a $\omega_n$, la amplitud se dispara: **resonancia**. → [[Vibracion Forzada]].

## Mapa del capítulo

> [!info] Las notas de este capítulo
> | Nota | Contenido |
> |:---|:---|
> | [[Vibracion Libre]] | $\omega_n=\sqrt{k/m}$; regímenes de amortiguamiento ($\zeta$) |
> | [[Vibracion Forzada]] | respuesta estacionaria; resonancia ($r=\omega/\omega_n$) |

> [!corolario]
> Toda la teoría de vibraciones es la ecuación $m\ddot x+c\dot x+kx=F(t)$: su solución libre da la frecuencia natural y el amortiguamiento; su solución forzada, la resonancia. Y como cualquier equilibrio estable se linealiza a un masa-resorte, este capítulo describe las oscilaciones de toda la física.

> [!referencia]
> Taylor cap. 5; Marion-Thornton cap. 3. Viene de [[4 Cuerpo Rigido/index | Cuerpo rígido]]; cierra el curso de **Dinámica**.
