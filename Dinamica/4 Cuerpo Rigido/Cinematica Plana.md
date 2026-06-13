---
title: Cinemática Plana
tags:
  - dinamica
  - teoria
  - cuerpo-rigido
  - cinematica
draft: false
aliases:
  - cinemática plana
  - centro instantáneo
  - rodadura
  - plane kinematics
  - instantaneous center
  - rolling without slipping
---

# Cinemática Plana $\;\vec v_B=\vec v_A+\vec\omega\times\vec r_{B/A}$

> [!definicion]
> El **movimiento plano** de un sólido rígido es una **traslación** más una **rotación** con velocidad
> angular $\vec\omega=\omega\hat k$ **perpendicular** al plano (y $\vec\alpha=\dot\omega\,\hat k$). Para dos
> puntos $A$ y $B$ **del mismo sólido**, la velocidad y la aceleración relativas son
> $$\boxed{\;\vec v_B=\vec v_A+\vec\omega\times\vec r_{B/A},\qquad \vec a_B=\vec a_A+\vec\alpha\times\vec r_{B/A}-\omega^2\,\vec r_{B/A}.\;}$$
> El **centro instantáneo de rotación (CIR)** es el punto de **velocidad nula** en torno al cual el sólido
> gira como rotación pura en ese instante.

> [!info]
> Cinemática plana del [[4 Cuerpo Rigido/index | cuerpo rígido]]; es el caso particular de la
> [[Cinematica en 3D | cinemática 3D]] con $\vec\omega\parallel\hat k$ (entonces el término centrípeto
> $-\omega^2\vec r_{B/A}$ no es otra cosa que $\vec\omega\times(\vec\omega\times\vec r_{B/A})$). Alimenta la
> [[Dinamica Plana 2D]]. Referencia: Hibbeler cap. 16.

---

## Ejemplo

> [!ejemplo]
> **Rueda que rueda sin deslizar.**
>
> Una rueda de radio $R$ rueda **sin deslizar** sobre el suelo, con velocidad del centro $G$ igual a
> $v_G$. Hallar la velocidad del **punto de contacto** y la del **punto más alto** de la rueda.
>
> ![[rodadura_cir.svg|520]]
>
> El punto de contacto $C$ con el suelo no desliza: su velocidad es nula, luego $C$ es el **CIR**. Visto
> desde el CIR todo el sólido rota puro: un punto a distancia $d$ del CIR tiene rapidez $\omega d$. El
> centro $G$ está a $R$ del contacto y la cima $T$ a $2R$.
>
> > [!solucion]
> > - Contacto: $v_C=0$ (es el CIR).
> > - Centro: $v_G=\omega R$, de donde $\omega=v_G/R$.
> > - Cima: $v_T=\omega(2R)=2\omega R=2v_G$.
> >
> > El punto más alto se mueve al **doble** de la velocidad del centro, y el CIR está exactamente en el
> > punto de contacto.

---

## En qué consiste

> [!teoria]
> En el plano, $\vec\omega=\omega\hat k$ y $\vec\alpha=\dot\omega\,\hat k$ son siempre **axiales** (un solo
> grado de libertad de rotación). Conocida la velocidad de **un** punto y $\vec\omega$, la fórmula de
> velocidades relativas da la velocidad de **cualquier** otro punto del sólido: el campo de velocidades de
> un cuerpo rígido queda fijado por seis números en 3D y por **tres** en 2D ($v_{Ax},v_{Ay},\omega$).

> [!teorema] Velocidad y aceleración relativas
> Para dos puntos $A,B$ del mismo sólido rígido,
> $$\vec v_B=\vec v_A+\vec\omega\times\vec r_{B/A},\qquad
> \vec a_B=\vec a_A+\vec\alpha\times\vec r_{B/A}-\omega^2\,\vec r_{B/A}.$$

> [!demostracion]
> **Paso 1 — Rigidez:** como $A$ y $B$ pertenecen al mismo sólido, la distancia $|\vec r_{B/A}|$ es
> **constante**; el vector $\vec r_{B/A}$ solo puede **girar** con el cuerpo, es decir con $\vec\omega$.
> **Paso 2 — Derivada de un vector que solo gira:** por el
> [[Operador Derivada en Base Movil | operador en base móvil]] (o derivando directamente la rotación),
> $$\frac{d\vec r_{B/A}}{dt}=\vec\omega\times\vec r_{B/A}.$$
> **Paso 3 — Velocidad:** como $\vec r_{B/A}=\vec r_B-\vec r_A$, derivando,
> $\vec v_B-\vec v_A=\dfrac{d\vec r_{B/A}}{dt}=\vec\omega\times\vec r_{B/A}$, esto es
> $\vec v_B=\vec v_A+\vec\omega\times\vec r_{B/A}$.
> **Paso 4 — Aceleración:** derivamos otra vez,
> $$\vec a_B-\vec a_A=\dot{\vec\omega}\times\vec r_{B/A}+\vec\omega\times\frac{d\vec r_{B/A}}{dt}
> =\vec\alpha\times\vec r_{B/A}+\vec\omega\times(\vec\omega\times\vec r_{B/A}).$$
> **Paso 5 — Caso plano:** con $\vec\omega=\omega\hat k\perp\vec r_{B/A}$, la identidad BAC–CAB da
> $\vec\omega\times(\vec\omega\times\vec r_{B/A})=(\vec\omega\cdot\vec r_{B/A})\vec\omega-\omega^2\vec r_{B/A}=-\omega^2\vec r_{B/A}$.
> Luego $\vec a_B=\vec a_A+\vec\alpha\times\vec r_{B/A}-\omega^2\vec r_{B/A}$. $\blacksquare$

> [!proposicion] Centro instantáneo de rotación
> En cada instante existe un punto $I$ (que puede estar **fuera** del cuerpo) con $\vec v_I=\vec0$. Está
> sobre la **perpendicular** a la velocidad de cada punto, a distancia $d=v/\omega$ de él. Visto desde el
> CIR, el sólido **rota puro**: $v_P=\omega\,d_{P/I}$ para todo punto $P$.
>
> *Justificación:* tomando $A=I$ en la fórmula de velocidades, $\vec v_P=\vec\omega\times\vec r_{P/I}$, que
> es perpendicular a $\vec r_{P/I}$ y de módulo $\omega\,d_{P/I}$. Para localizarlo se intersecan las
> perpendiculares a las velocidades de dos puntos.

> [!proposicion] Rodadura sin deslizar
> Si un disco de radio $R$ rueda sin deslizar, el punto de contacto tiene **velocidad nula** (es el CIR),
> de modo que
> $$v_G=\omega R,\qquad a_G=\alpha R,$$
> la segunda por derivación de la primera. Estas dos relaciones son la **restricción cinemática** de la
> rodadura, no identidades generales.

> [!warning]
> El CIR tiene velocidad nula pero **NO aceleración nula**: no puede usarse como punto fijo para acelerar
> otros puntos (no es válido $\vec a_P=\vec\alpha\times\vec r_{P/I}-\omega^2\vec r_{P/I}$ tomando $\vec a_I=0$).
> El término centrípeto $-\omega^2\vec r_{B/A}$ se **olvida** con frecuencia en la aceleración. Y el CIR
> **se mueve** instante a instante: $v_G=\omega R$ vale para velocidad, pero $a_G=\alpha R$ exige cuidado
> porque el contacto cambia de punto.

## Resumen

> [!resumen]
> | Magnitud | Expresión |
> |:---|:---|
> | Velocidad relativa | $\vec v_B=\vec v_A+\vec\omega\times\vec r_{B/A}$ |
> | Aceleración relativa | $\vec a_B=\vec a_A+\vec\alpha\times\vec r_{B/A}-\omega^2\vec r_{B/A}$ |
> | CIR | punto con $\vec v=\vec0$; $d=v/\omega$; rotación pura $v_P=\omega\,d_{P/I}$ |
> | Rodadura sin deslizar | $v_G=\omega R,\quad a_G=\alpha R$ |

> [!corolario]
> Toda la cinemática plana de un sólido rígido se reduce a **un** campo de velocidades de rotación pura
> alrededor del CIR. La velocidad de cualquier punto se obtiene con $\vec\omega\times\vec r$ desde otro
> punto conocido; la aceleración añade siempre el término centrípeto $-\omega^2\vec r$.

> [!referencia]
> Hibbeler *Dinámica* cap. 16. Caso general: [[Cinematica en 3D]]. Herramienta de derivación:
> [[Operador Derivada en Base Movil]]. Aplicación cinética: [[Dinamica Plana 2D]]. Índice:
> [[4 Cuerpo Rigido/index]].
