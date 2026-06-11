---
title: Deducción del Momento Angular
tags:
  - dinamica
  - teoria
  - inercia
draft: false
aliases:
  - deducción del momento angular
  - H=Iω
  - angular momentum derivation
---

# Deducción del Momento Angular $\;\vec H^o=\mathbf I_c\vec\omega+m\,\vec r_{c/o}\times\vec v_c$

> [!definicion]
> Integrando el momento angular elemental $d\vec H^o=\vec r_{p/o}\times\vec v_p\,dm$ sobre el cuerpo
> rígido se obtiene, **sin postular nada**,
> $$\boxed{\;\vec H^o=\mathbf I_c\vec\omega+m\,\vec r_{c/o}\times\vec v_c\;}$$
> y, tomando el origen en el centro de masa ($O=C$, $\vec r_{c/o}=\vec0$), el resultado limpio
> $\vec H^c=\mathbf I_c\vec\omega$.

> [!info]
> Una de las [[Deducciones/index | deducciones]] de la [[3 Inercia/index | inercia]]. Hermana de
> [[Deduccion del Torque]] y [[Deduccion de la Energia Cinetica]]; usa el [[Tensor de Inercia]].
> Referencia: Goldstein §5.

---

## Ejemplo

> [!ejemplo]
> **Rotación pura en torno al CM.**
>
> Un cuerpo **rota en torno a su centro de masa** ($O=C$, $\vec r_{c/o}=\vec0$). Entonces el momento
> angular se reduce a
> $$\vec H^c=\mathbf I_c\vec\omega.$$
> Si además $\vec\omega$ va sobre un **eje principal** con momento $I$ (de modo que $\mathbf I_c\vec\omega=I\vec\omega$),
> $$\vec H=I\vec\omega\quad(\parallel\vec\omega).$$
>
> > [!solucion]
> > En general $\vec H$ **no** es paralelo a $\vec\omega$: el tensor $\mathbf I_c$ los "tuerce". Solo
> > sobre los **ejes principales** (autovectores de $\mathbf I_c$) se cumple $\vec H\parallel\vec\omega$,
> > con $\vec H=I\vec\omega$ y $I$ el momento principal correspondiente.

---

## En qué consiste

> [!teorema] Punto de partida
> Con $d\vec H^o=\vec r_{p/o}\times\vec v_p\,dm$, el momento angular total es
> $$\vec H^o=\int_N\vec r_{p/o}\times\vec v_p\,dm.$$
> Sustituyendo la descomposición de posición y la cinemática rígida de velocidad
> $$\vec r_{p/o}=\vec r_{p/c}+\vec r_{c/o},\qquad \vec v_p=\vec v_c+\vec\omega\times\vec r_{p/c},$$
> y expandiendo, se separa en $I_1$ (los términos con brazo $\vec r_{p/c}$) e $I_2$ (los términos con
> brazo $\vec r_{c/o}$).

> [!demostracion] Término $I_1$ (lo que da el tensor)
> $$I_1=\int_N\vec r_{p/c}\times\big[\vec v_c+\vec\omega\times\vec r_{p/c}\big]\,dm.$$
> **Paso 1 — El término de $\vec v_c$ se anula:** como $\vec v_c$ es común a todo el cuerpo,
> $$\int_N\vec r_{p/c}\times\vec v_c\,dm=\Big(\int_N\vec r_{p/c}\,dm\Big)\times\vec v_c=\vec0,$$
> por la definición de CM ($\int\vec r_{p/c}\,dm=\vec0$). Sobrevive el término con $\vec\omega$:
> $$I_1=\int_N\vec r_{p/c}\times(\vec\omega\times\vec r_{p/c})\,dm.$$
> **Paso 2 — Identidad del doble producto:** con $\vec r\times(\vec\omega\times\vec r)=\vec\omega\,r^2-\vec r(\vec r\cdot\vec\omega)$,
> $$I_1=\int_N\big[\vec\omega\,r^2-\vec r(\vec r\cdot\vec\omega)\big]\,dm=\mathrm{Tr}(\mathbf Q)\,\mathbb 1\cdot\vec\omega-\mathbf Q\cdot\vec\omega=\big[\mathrm{Tr}(\mathbf Q)\mathbb 1-\mathbf Q\big]\vec\omega=\mathbf I_c\vec\omega,$$
> usando $Q_{ij}=\int r_ir_j\,dm$ y $\mathbf I_c=\mathrm{Tr}(\mathbf Q)\mathbb 1-\mathbf Q$. $\blacksquare$

> [!demostracion] Término $I_2$ (el del brazo del CM)
> $$I_2=\int_N\vec r_{c/o}\times\big[\vec v_c+\vec\omega\times\vec r_{p/c}\big]\,dm.$$
> **Paso 1 — El término con $\vec\omega\times\vec r_{p/c}$ se anula:** como $\vec r_{c/o}$ es
> **constante**,
> $$\int_N\vec r_{c/o}\times(\vec\omega\times\vec r_{p/c})\,dm=\vec r_{c/o}\times\Big(\vec\omega\times\int_N\vec r_{p/c}\,dm\Big)=\vec0,$$
> de nuevo por $\int\vec r_{p/c}\,dm=\vec0$.
> **Paso 2 — El término de $\vec v_c$ sobrevive:** con $\vec r_{c/o}$ y $\vec v_c$ constantes,
> $$\int_N\vec r_{c/o}\times\vec v_c\,dm=\vec r_{c/o}\times\vec v_c\int_N dm=m\,\vec r_{c/o}\times\vec v_c.$$
> Por tanto $I_2=m\,\vec r_{c/o}\times\vec v_c$. $\blacksquare$

> [!proposicion] Descomposición espín + orbital
> Sumando, $\vec H^o=\mathbf I_c\vec\omega+m\,\vec r_{c/o}\times\vec v_c$. Con origen en el CM ($O=C$),
> $$\vec H^c=\mathbf I_c\vec\omega.$$
> En $O=C$ el momento angular es puramente **de espín** $\mathbf I_c\vec\omega$ (giro propio del cuerpo).
> El término $m\,\vec r_{c/o}\times\vec v_c$ es el momento **orbital** del CM: el que tendría una
> partícula que concentrase toda la masa $m$ en $C$. Así, $\vec H^o=\underbrace{\mathbf I_c\vec\omega}_{\text{espín}}+\underbrace{m\,\vec r_{c/o}\times\vec v_c}_{\text{orbital}}$.

> [!warning]
> $\vec H$ en general **no** es paralelo a $\vec\omega$: solo lo es sobre los **ejes principales** de
> $\mathbf I_c$. Además, el resultado limpio $\vec H=\mathbf I_c\vec\omega$ exige tomar momentos respecto
> al **centro de masa** (o a un punto fijo); para un $O$ arbitrario sobrevive el término orbital
> $m\,\vec r_{c/o}\times\vec v_c$.

## Resumen

> [!resumen]
> | Paso | Resultado |
> |:---|:---|
> | $I_1$ (brazo $\vec r_{p/c}$) | $\mathbf I_c\vec\omega$ (espín) |
> | $I_2$ (brazo $\vec r_{c/o}$) | $m\,\vec r_{c/o}\times\vec v_c$ (orbital) |
> | Momento angular (punto $O$) | $\vec H^o=\mathbf I_c\vec\omega+m\,\vec r_{c/o}\times\vec v_c$ |
> | En el CM ($O=C$) | $\vec H^c=\mathbf I_c\vec\omega$ |

> [!corolario]
> La fórmula no es un postulado: se **integra** desde $d\vec H=\vec r\times\vec v\,dm$, y el tensor de
> inercia aparece solo al separar el término de espín. La descomposición **espín + orbital** es el
> análogo angular de "todo cuerpo se mueve como su CM más un giro propio".

> [!referencia]
> Goldstein §5. Construido sobre el [[Tensor de Inercia]]. Hermanas: [[Deduccion del Torque]],
> [[Deduccion de la Energia Cinetica]]. Índice: [[Deducciones/index]].
