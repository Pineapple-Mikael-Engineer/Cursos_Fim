---
title: Deducción del Torque
tags:
  - dinamica
  - teoria
  - inercia
draft: false
aliases:
  - deducción del torque
  - ecuación de Euler deducción
  - torque y tensor de inercia
---

# Deducción del Torque $\;\vec\tau=\mathbf I\vec\alpha+\vec\omega\times(\mathbf I\vec\omega)$

> [!definicion]
> Integrando el torque elemental $d\vec\tau^o=\vec r_{p/o}\times\vec a_p\,dm$ sobre un cuerpo rígido se
> obtiene, **sin postular nada**, la ecuación rotacional
> $$\boxed{\;\vec\tau^o=\mathbf I_c\vec\alpha+\vec\omega\times(\mathbf I_c\vec\omega)+\vec r_{c/o}\times\vec F\;}$$
> y, tomando el origen en el centro de masa ($O=C$, $\vec r_{c/o}=\vec0$), la **ecuación de Euler**
> $\vec\tau^c=\mathbf I_c\vec\alpha+\vec\omega\times(\mathbf I_c\vec\omega)$.

> [!info]
> La deducción central de las [[Deducciones/index | Deducciones]] de la [[3 Inercia/index | inercia]].
> El término giroscópico $\vec\omega\times(\mathbf I\vec\omega)$ es también el que produce el
> [[Operador Derivada en Base Movil | operador en base móvil]] aplicado a $\vec H=\mathbf I\vec\omega$.
> Se usa en [[Ecuaciones de Euler 3D]]. Referencia: Goldstein §5.

---

## Ejemplo

> [!ejemplo]
> **Girar sobre un eje principal no cuesta torque.**
>
> Un cuerpo gira con $\vec\omega$ **constante** ($\vec\alpha=\vec0$) en torno a un **eje principal**
> $\hat e$ (con momento principal $I$, de modo que $\mathbf I\vec\omega=I\vec\omega$). ¿Qué torque hace
> falta?
>
> $$\vec\tau=\mathbf I\underbrace{\vec\alpha}_{\vec0}+\vec\omega\times(\mathbf I\vec\omega)=\vec\omega\times(I\vec\omega)=I(\vec\omega\times\vec\omega)=\vec0.$$
>
> > [!solucion]
> > $\vec\tau=\vec0$: una rotación estacionaria sobre un eje **principal** se mantiene sola. Si el eje
> > **no** es principal, $\mathbf I\vec\omega$ no es paralelo a $\vec\omega$ y aparece el **torque
> > giroscópico** $\vec\omega\times(\mathbf I\vec\omega)\neq\vec0$: los cojinetes lo sufren (vibración).

---

## En qué consiste

> [!teorema] Punto de partida
> Con $d\vec F_p=\vec a_p\,dm$ y la cinemática rígida
> $$\vec a_p=\vec a_c+\vec\alpha\times\vec r_{p/c}+\vec\omega\times(\vec\omega\times\vec r_{p/c}),\qquad \vec r_{p/o}=\vec r_{p/c}+\vec r_{c/o},$$
> el torque total es $\vec\tau^o=\displaystyle\int_N \vec r_{p/o}\times\vec a_p\,dm=I_1+I_2$, separando según
> $\vec r_{p/o}$ aporte $\vec r_{p/c}$ ($I_1$) o $\vec r_{c/o}$ ($I_2$).

> [!demostracion] Término $I_1$ (lo que da el tensor)
> $$I_1=\int_N \vec r_{p/c}\times\big[\vec a_c+\vec\alpha\times\vec r_{p/c}+\vec\omega\times(\vec\omega\times\vec r_{p/c})\big]\,dm.$$
> **Paso 1 — El término de $\vec a_c$ se anula:** $\displaystyle\int_N\vec r_{p/c}\,dm=\vec0$ (definición
> de CM), luego $\int\vec r_{p/c}\times\vec a_c\,dm=\Big(\int\vec r_{p/c}\,dm\Big)\times\vec a_c=\vec0$.
> Quedan $J_1$ (con $\vec\alpha$) y $J_2$ (con $\vec\omega$).
> **Paso 2 — $J_1$:** con la identidad $\vec r\times(\vec\alpha\times\vec r)=\vec\alpha\,r^2-\vec r(\vec r\cdot\vec\alpha)$,
> $$J_1=\int_N\big[\vec\alpha\,r^2-\vec r(\vec r\cdot\vec\alpha)\big]dm=\mathrm{Tr}(\mathbf Q)\,\mathbb 1\cdot\vec\alpha-\mathbf Q\cdot\vec\alpha=\big[\mathrm{Tr}(\mathbf Q)\mathbb 1-\mathbf Q\big]\vec\alpha=\mathbf I_c\vec\alpha,$$
> usando $\int r_ir_j\,dm=Q_{ij}$ y $\mathbf I_c=\mathrm{Tr}(\mathbf Q)\mathbb 1-\mathbf Q$.
> **Paso 3 — $J_2$:** con $\vec r\times[\vec\omega\times(\vec\omega\times\vec r)]=(\vec r\times\vec\omega)(\vec r\cdot\vec\omega)$
> (pues $\vec\omega\times(\vec\omega\times\vec r)=\vec\omega(\vec\omega\cdot\vec r)-\vec r\,\omega^2$ y
> $\vec r\times\vec r=\vec0$), e indexando,
> $$J_2=\int_N (r_i\omega_j r_k\omega_k)\,\epsilon_{ijl}\,\hat e_l\,dm=(\mathbf Q\cdot\vec\omega)\times\vec\omega=\vec\omega\times(\mathbf I_c\vec\omega),$$
> donde la última igualdad usa $\mathbf I_c\vec\omega=\mathrm{Tr}(\mathbf Q)\vec\omega-\mathbf Q\vec\omega$ y
> $\vec\omega\times\vec\omega=\vec0$, así que $\vec\omega\times(\mathbf I_c\vec\omega)=-\vec\omega\times(\mathbf Q\vec\omega)=(\mathbf Q\vec\omega)\times\vec\omega$.
> Por tanto $I_1=\mathbf I_c\vec\alpha+\vec\omega\times(\mathbf I_c\vec\omega)$. $\blacksquare$

> [!demostracion] Término $I_2$ (el del brazo del CM)
> $$I_2=\int_N \vec r_{c/o}\times\big[\vec a_c+\vec\alpha\times\vec r_{p/c}+\vec\omega\times(\vec\omega\times\vec r_{p/c})\big]\,dm.$$
> Como $\vec r_{c/o}$ es **constante** y $\int\vec r_{p/c}\,dm=\vec0$, los dos últimos términos se
> anulan; sobrevive
> $$I_2=\vec r_{c/o}\times\vec a_c\int_N dm=\vec r_{c/o}\times(m\vec a_c)=\vec r_{c/o}\times\vec F,$$
> con $\vec F=m\vec a_c$ la resultante externa. $\blacksquare$

> [!proposicion] Forma final y ecuación de Euler
> Sumando, $\vec\tau^o=\mathbf I_c\vec\alpha+\vec\omega\times(\mathbf I_c\vec\omega)+\vec r_{c/o}\times\vec F$.
> Con origen en el CM ($\vec r_{c/o}=\vec0$),
> $$\vec\tau^c=\mathbf I_c\vec\alpha+\vec\omega\times(\mathbf I_c\vec\omega).$$
> En **ejes principales** del cuerpo, por componentes:
> $\tau_1=I_1\dot\omega_1-(I_2-I_3)\omega_2\omega_3$ (y cíclicas) — las ecuaciones de Euler clásicas.

> [!warning]
> El término giroscópico $\vec\omega\times(\mathbf I\vec\omega)$ **no** existe en 2D (allí $\vec\omega$
> y $\mathbf I\vec\omega$ son paralelos al eje $z$): es genuinamente tridimensional. La fórmula con
> $\vec r_{c/o}\times\vec F$ vale para **cualquier** punto $O$; conviene casi siempre tomar $O=C$ o un
> punto fijo.

## Resumen

> [!resumen]
> | Paso | Resultado |
> |:---|:---|
> | $I_1$ (brazo $\vec r_{p/c}$) | $\mathbf I_c\vec\alpha+\vec\omega\times(\mathbf I_c\vec\omega)$ |
> | $I_2$ (brazo $\vec r_{c/o}$) | $\vec r_{c/o}\times\vec F$ |
> | Torque (punto $O$) | $\vec\tau^o=\mathbf I_c\vec\alpha+\vec\omega\times(\mathbf I_c\vec\omega)+\vec r_{c/o}\times\vec F$ |
> | Euler ($O=C$) | $\vec\tau^c=\mathbf I_c\vec\alpha+\vec\omega\times(\mathbf I_c\vec\omega)$ |

> [!corolario]
> La ecuación de Euler no es un axioma: se **integra** desde $d\vec\tau=\vec r\times\vec a\,dm$, y el
> tensor de inercia aparece solo al separar los términos. El giroscópico $\vec\omega\times(\mathbf I\vec\omega)$
> es el sello de la rotación 3D.

> [!referencia]
> Goldstein §5. Mismo término vía operador: [[Operador Derivada en Base Movil]]. Hermanas:
> [[Deduccion del Momento Angular]], [[Deduccion de la Energia Cinetica]]. Aplicación:
> [[Ecuaciones de Euler 3D]].
