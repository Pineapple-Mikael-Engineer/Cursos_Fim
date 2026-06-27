---
title: Procesos Termodinámicos
order: 1
tags:
  - termodinamica
  - teoria
  - procesos
  - index
draft: false
aliases:
  - Procesos Termodinamicos
  - Procesos
  - Procesos de gas ideal
---

# Procesos Termodinámicos $W=\displaystyle\int_1^2 P\,dV,\qquad Q=\displaystyle\int_1^2 T\,dS$

> [!definicion]
> Un **proceso** es la trayectoria de estados que sigue un sistema al pasar de un estado de equilibrio $1$ a otro $2$. Un proceso **cuasiestático** (sucesión de estados de equilibrio) admite una curva bien definida en los planos $P$–$v$ y $T$–$s$, sobre la cual el **trabajo de frontera** y el **calor** (reversible) son áreas:
> $$w=\int_1^2 P\,dv\quad(\text{área bajo la curva }P\text{–}v),\qquad q_{\text{rev}}=\int_1^2 T\,ds\quad(\text{área bajo la curva }T\text{–}s).$$
> Los procesos elementales (isotérmico, isobárico, isocórico, adiabático) son **casos particulares** del proceso **politrópico** $Pv^{\,n}=\text{cte}$.

---

> [!info]
> **Ubicación.** Curso de Termodinámica (MN121) · sección **Procesos**. Se apoya en las leyes de [[Primera Ley SC | conservación]] y en las [[Gas Ideal | propiedades del gas ideal]]; alimenta los **ciclos** (Rankine, Brayton, Otto/Diesel) y la [[Entropia | entropía]].
> **Convención.** SI; $w,q$ específicos (por unidad de masa); $\delta q,\delta w$ inexactos, $du,dh,ds$ exactos; $q>0$ hacia el sistema, $w>0$ realizado por el sistema; gas ideal con $Pv=RT$, $c_p-c_v=R$, $\gamma=c_p/c_v$.

---

## Trabajo de frontera y representación

> [!teoria] Las dos áreas: trabajo y calor
> Para un sistema cerrado con frontera móvil cuasiestática, el trabajo es el **área bajo la curva en el plano $P$–$v$**; por eso el camino —no solo los extremos— importa ($\delta w$ es inexacto). En un proceso reversible, el calor es el **área bajo la curva en el plano $T$–$s$**. Estas dos representaciones, $P$–$v$ y $T$–$s$, son las herramientas de lectura de **todo** el curso (y de los ciclos).
>
> ![[piston_cilindro.svg|360]]
> *El trabajo de frontera $\delta w=P\,dv$ proviene del desplazamiento del émbolo; su integral es el área bajo la curva $P$–$v$.*

> [!teoria] Los procesos elementales y su unificación politrópica
> Cada proceso elemental fija una variable y deja una relación $P(v)$ característica. Todos son el politrópico $Pv^n=\text{cte}$ con un exponente $n$ distinto:
>
> ![[procesos_pv_comparacion.svg|420]]
> *En el plano $P$–$v$, desde un mismo estado $1$: el isocórico es vertical ($n\to\infty$), el isobárico horizontal ($n=0$), el isotérmico una hipérbola ($n=1$) y el adiabático una hipérbola más empinada ($n=\gamma$).*
>
> ![[procesos_ts_comparacion.svg|420]]
> *En el plano $T$–$s$: el adiabático reversible es vertical ($s=$cte), el isotérmico horizontal, y el isocórico sube más empinado que el isobárico (porque $c_v<c_p$).*

---

## Resultados para gas ideal

> [!proposicion] Tabla maestra de los procesos (sistema cerrado, gas ideal, masa $m$)
> Con $\Delta u=m c_v\Delta T$ y $\Delta h=m c_p\Delta T$ **siempre** (gas ideal), por proceso:
>
> | Proceso | $n$ | Relación | $w=\int P\,dv$ | $q$ | $\Delta s$ |
> |:---|:--:|:---|:---|:---|:---|
> | Isocórico | $\infty$ | $v=$cte | $0$ | $\Delta u=mc_v\Delta T$ | $mc_v\ln\dfrac{T_2}{T_1}$ |
> | Isobárico | $0$ | $P=$cte | $P(v_2-v_1)=mR\Delta T$ | $\Delta h=mc_p\Delta T$ | $mc_p\ln\dfrac{T_2}{T_1}$ |
> | Isotérmico | $1$ | $Pv=$cte | $mRT\ln\dfrac{v_2}{v_1}$ | $=w$ ($\Delta u=0$) | $mR\ln\dfrac{v_2}{v_1}$ |
> | Adiabático rev. | $\gamma$ | $Pv^\gamma=$cte | $\dfrac{P_1v_1-P_2v_2}{\gamma-1}=-\Delta u$ | $0$ | $0$ |
> | Politrópico | $n$ | $Pv^n=$cte | $\dfrac{P_1v_1-P_2v_2}{n-1}$ | $\Delta u+w$ | $mc_v\ln\dfrac{T_2}{T_1}+mR\ln\dfrac{v_2}{v_1}$ |
>
> Cada fila se deduce en su nota. La columna $w$ es trabajo de frontera cuasiestático; $\Delta u,\Delta h$ valen para cualquier camino entre los mismos $T$.

> [!warning]
> $\Delta u=mc_v\Delta T$ y $\Delta h=mc_p\Delta T$ valen para **gas ideal en cualquier proceso** (porque $u=u(T)$, $h=h(T)$), no solo en el isocórico/isobárico. Lo que cambia con el proceso es **cómo se reparte** esa energía entre $q$ y $w$. No confundir $c_v$ con "calor a volumen constante": es una propiedad, $c_v=(\partial u/\partial T)_v$.

---

## Notas de esta sección

> [!info] Mapa
> - [[Proceso Isocorico]] — $v=$cte; $w=0$, $q_v=\Delta u$.
> - [[Proceso Isobarico]] — $P=$cte; $q_p=\Delta h$.
> - [[Proceso Isotermico]] — $T=$cte; $w=q$, $\Delta u=0$.
> - [[Proceso Adiabatico]] — $q=0$; isentrópico, $Pv^\gamma=$cte.
> - [[Proceso Politropico]] — $Pv^n=$cte; unifica a los cuatro ($n=0,1,\gamma,\infty$).
> - [[Procesos Reversibles e Irreversibles]] — cuasiestático vs real; el trabajo reversible es el extremo y la irreversibilidad genera entropía.

> [!referencia]
> Çengel & Boles, *Termodinámica*, caps. 4 y 7; Moran & Shapiro, *Fundamentos de Termodinámica Técnica*, caps. 2–3 y 6; Borgnakke & Sonntag, *Fundamentals of Thermodynamics*. Tablas/diagramas con **CATT3**.
