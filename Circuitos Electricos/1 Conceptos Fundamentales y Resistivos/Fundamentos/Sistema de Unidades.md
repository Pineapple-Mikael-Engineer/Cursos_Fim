---
title: Sistema de Unidades
order: 4
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - unidades
draft: false
aliases:
  - sistema de unidades
  - unidades SI
  - prefijos
  - SI units
---

# Sistema de Unidades (SI) y Prefijos

> [!definicion]
> El curso usa el **Sistema Internacional (SI)**. Las magnitudes eléctricas se miden en amperio ($\text{A}$), voltio ($\text{V}$), ohmio ($\Omega$), siemens ($\text{S}$), faradio ($\text{F}$), henrio ($\text{H}$), culombio ($\text{C}$), julio ($\text{J}$) y vatio ($\text{W}$). Los valores se expresan con **prefijos** ($\text{p},\text{n},\mu,\text{m},\text{k},\text{M},\text{G}$) que escalan en potencias de $10$, para evitar exponentes incómodos.

---

> [!info]
> Cuarta nota de [[Fundamentos/index| Fundamentos]] del [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Da las unidades de las [[Variables del Circuito| variables del circuito]] y de los elementos pasivos que se introducen en la sección [[Elementos del Circuito/index| Elementos del circuito]].

---

## Ejemplo

> [!ejemplo] Lectura y conversión con prefijos
> Reescribir cada cantidad con el prefijo más adecuado (un solo dígito entero, si es posible):
>
> - **Capacidad** $C=0{,}0047\ \text{F}$. Como $\text{m}=10^{-3}$:
>   $$0{,}0047\ \text{F}=4{,}7\times 10^{-3}\ \text{F}=4{,}7\ \text{mF}.$$
>   (También $=4700\ \mu\text{F}$, valor habitual en condensadores comerciales.)
> - **Resistencia** $R=2200\ \Omega$. Como $\text{k}=10^{3}$:
>   $$2200\ \Omega=2{,}2\times 10^{3}\ \Omega=2{,}2\ \text{k}\Omega.$$
> - **Corriente** $i=0{,}000015\ \text{A}$. Como $\mu=10^{-6}$:
>   $$0{,}000015\ \text{A}=15\times 10^{-6}\ \text{A}=15\ \mu\text{A}.$$
> - **Potencia** $p=3\,500\,000\ \text{W}$. Como $\text{M}=10^{6}$:
>   $$3{,}5\times 10^{6}\ \text{W}=3{,}5\ \text{MW}.$$
>
> > [!solucion]
> > $0{,}0047\ \text{F}=4{,}7\ \text{mF}$; $\;2200\ \Omega=2{,}2\ \text{k}\Omega$; $\;0{,}000015\ \text{A}=15\ \mu\text{A}$; $\;3\,500\,000\ \text{W}=3{,}5\ \text{MW}$.

---

## En qué consiste

> [!teoria] Magnitudes derivadas y coherencia del SI
> El SI parte de unas pocas unidades base; en electrotecnia la fundamental es el **amperio**. El resto se **derivan** de forma coherente: el culombio es $\text{A}\cdot\text{s}$; el voltio es $\text{J/C}=\text{W/A}$; el ohmio es $\text{V/A}$; el siemens es su inverso $\text{A/V}=1/\Omega$; el faradio es $\text{C/V}$ y el henrio es $\text{V}\cdot\text{s/A}=\text{Wb/A}$. Trabajar en unidades SI coherentes garantiza que las fórmulas ($v=Ri$, $p=vi$, $W=\int p\,dt$) den resultados en las unidades correctas **sin factores de conversión**.

> [!info] Magnitudes eléctricas y sus unidades
> | Magnitud | Símbolo | Unidad | Símbolo unidad | En unidades base/derivadas |
> |:---|:---|:---|:---|:---|
> | Corriente | $i,I$ | amperio | $\text{A}$ | base |
> | Carga | $q$ | culombio | $\text{C}$ | $\text{A}\cdot\text{s}$ |
> | Tensión | $v,V$ | voltio | $\text{V}$ | $\text{J/C}=\text{W/A}$ |
> | Resistencia | $R$ | ohmio | $\Omega$ | $\text{V/A}$ |
> | Conductancia | $G$ | siemens | $\text{S}$ | $\text{A/V}=1/\Omega$ |
> | Capacidad | $C$ | faradio | $\text{F}$ | $\text{C/V}$ |
> | Inductancia | $L$ | henrio | $\text{H}$ | $\text{V}\cdot\text{s/A}$ |
> | Energía | $w,W$ | julio | $\text{J}$ | $\text{N}\cdot\text{m}$ |
> | Potencia | $p,P$ | vatio | $\text{W}$ | $\text{J/s}=\text{V}\cdot\text{A}$ |

> [!info] Prefijos del SI más usados
> | Prefijo | Símbolo | Factor | | Prefijo | Símbolo | Factor |
> |:---|:---:|:---|---|:---|:---:|:---|
> | pico | $\text{p}$ | $10^{-12}$ | | kilo | $\text{k}$ | $10^{3}$ |
> | nano | $\text{n}$ | $10^{-9}$ | | mega | $\text{M}$ | $10^{6}$ |
> | micro | $\mu$ | $10^{-6}$ | | giga | $\text{G}$ | $10^{9}$ |
> | mili | $\text{m}$ | $10^{-3}$ | | | | |

> [!warning] Mayúsculas y símbolos correctos
> Los símbolos de unidad que vienen de un nombre propio van en **mayúscula** ($\text{A}$, $\text{V}$, $\text{W}$, $\text{H}$, $\text{F}$, $\Omega$), pero el nombre escrito va en minúscula (amperio, voltio). Ojo a confusiones: $\text{M}=10^6$ (mega) frente a $\text{m}=10^{-3}$ (mili); $\text{k}$ minúscula para kilo (nunca $\text{K}$, que es kelvin). Entre número y unidad va un espacio fino: $5\ \text{A}$, $2{,}2\ \text{k}\Omega$.

---

## Resumen

> [!resumen] Lo esencial
> | Idea | Detalle |
> |:---|:---|
> | Sistema | SI coherente; magnitud base eléctrica: el amperio |
> | Inversos | $G=1/R$ ($\text{S}=1/\Omega$) |
> | Escalado | prefijos en potencias de $10$: $\text{p},\text{n},\mu,\text{m},\text{k},\text{M},\text{G}$ |
> | Notación | número $+$ espacio fino $+$ símbolo: $4{,}7\ \text{mF}$ |

> [!corolario]
> Mantener todo en unidades SI coherentes hace que las leyes del circuito se apliquen sin conversiones; los prefijos son solo una forma compacta de escribir los números, no unidades nuevas.

> [!referencia]
> Fraile Mora, cap. 1, §1.1 y tablas de unidades. Relacionada: [[Variables del Circuito]].
