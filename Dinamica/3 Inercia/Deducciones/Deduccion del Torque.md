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
> Integrando el torque elemental $d\vec\tau^o=\vec r_{p/o}\times\vec a_p\,dm$ sobre un cuerpo rígido, y
> haciendo **explícita toda el álgebra tensorial**, se obtiene
> $$\boxed{\;\vec\tau^o=\mathbf I_c\vec\alpha+\vec\omega\times(\mathbf I_c\vec\omega)+\vec r_{c/o}\times\vec F\;}$$
> y, con origen en el centro de masa ($O=C$), la **ecuación de Euler**
> $\vec\tau^c=\mathbf I_c\vec\alpha+\vec\omega\times(\mathbf I_c\vec\omega)$.

> [!info]
> La deducción central de las [[Deducciones/index | Deducciones]] de la [[3 Inercia/index | inercia]].
> El tensor de inercia **no se postula**: emerge al contraer los índices. El término giroscópico
> $\vec\omega\times(\mathbf I\vec\omega)$ es también el que da el [[Operador Derivada en Base Movil | operador en base móvil]] sobre $\vec H$. Se usa en [[Ecuaciones de Euler 3D]]. Goldstein §5.

---

## Ejemplo

> [!ejemplo]
> **Girar sobre un eje principal no cuesta torque.**
>
> Un cuerpo gira con $\vec\omega$ **constante** ($\vec\alpha=\vec0$) en torno a un **eje principal**
> $\hat e$ ($\mathbf I\vec\omega=I\vec\omega$). ¿Qué torque hace falta?
>
> $$\vec\tau=\mathbf I\underbrace{\vec\alpha}_{\vec0}+\vec\omega\times(\mathbf I\vec\omega)=\vec\omega\times(I\vec\omega)=I(\vec\omega\times\vec\omega)=\vec0.$$
>
> > [!solucion]
> > $\vec\tau=\vec0$: la rotación estacionaria sobre un eje **principal** se mantiene sola. Si el eje
> > **no** es principal, $\mathbf I\vec\omega\nparallel\vec\omega$ y aparece el **torque giroscópico**
> > $\vec\omega\times(\mathbf I\vec\omega)\neq\vec0$: los cojinetes lo sufren (vibración).

---

## En qué consiste

> [!definicion] Convenios y herramientas
> Se usa notación indicial con suma sobre índices repetidos, el **segundo momento**
> $Q_{ij}=\int r_i r_j\,dm$ (simétrico) y el **tensor de inercia** $\mathbf I=\mathrm{Tr}(\mathbf Q)\,\mathbb 1-\mathbf Q$,
> es decir $I_{ij}=Q_{kk}\,\delta_{ij}-Q_{ij}$. Herramientas: la propiedad del centro de masa
> $\int\vec r_{p/c}\,dm=\vec0$, la identidad del doble producto vectorial
> $\vec A\times(\vec B\times\vec C)=\vec B(\vec A\cdot\vec C)-\vec C(\vec A\cdot\vec B)$ y la del
> símbolo de Levi-Civita $\epsilon_{ijk}\epsilon_{mnk}=\delta_{im}\delta_{jn}-\delta_{in}\delta_{jm}$.

![[cuerpo_inercia.svg|420]]

*Se integra sobre el cuerpo: cada elemento $dm$ a posición $\vec r$ aporta su torque $d\vec\tau=\vec r\times\vec a\,dm$.*

> [!teorema] Punto de partida
> Con $d\vec F_p=\vec a_p\,dm$, la cinemática rígida
> $\vec a_p=\vec a_c+\vec\alpha\times\vec r+\vec\omega\times(\vec\omega\times\vec r)$ (escribo
> $\vec r\equiv\vec r_{p/c}$) y $\vec r_{p/o}=\vec r+\vec r_{c/o}$, el torque total es
> $$\vec\tau^o=\int_N \vec r_{p/o}\times\vec a_p\,dm=\underbrace{\int_N \vec r\times\vec a_p\,dm}_{I_1}+\underbrace{\int_N \vec r_{c/o}\times\vec a_p\,dm}_{I_2}.$$

> [!demostracion] Término $I_1$ — Paso 1: la parte de $\vec a_c$ muere
> $$I_1=\int_N \vec r\times\big[\vec a_c+\vec\alpha\times\vec r+\vec\omega\times(\vec\omega\times\vec r)\big]\,dm.$$
> El primer sumando se va por el centro de masa:
> $$\int_N \vec r\times\vec a_c\,dm=\Big(\underbrace{\int_N \vec r\,dm}_{=\,\vec0}\Big)\times\vec a_c=\vec0.$$
> Quedan dos integrales, $I_1=J_1+J_2$, con
> $J_1=\int_N\vec r\times(\vec\alpha\times\vec r)\,dm$ y
> $J_2=\int_N\vec r\times[\vec\omega\times(\vec\omega\times\vec r)]\,dm$.

> [!demostracion] Término $I_1$ — Paso 2: $J_1$ produce $\mathbf I_c\vec\alpha$
> Por el doble producto, $\vec r\times(\vec\alpha\times\vec r)=\vec\alpha\,(\vec r\cdot\vec r)-\vec r\,(\vec r\cdot\vec\alpha)=\vec\alpha\,r^2-\vec r\,(\vec r\cdot\vec\alpha)$.
> Desarrollo **en componentes** el segundo término:
> $$\vec r\,(\vec r\cdot\vec\alpha)=r_i\hat e_i\,(r_j\alpha_j)=r_i r_j\,\alpha_j\,\hat e_i,$$
> de modo que su integral es
> $$\int_N r_i r_j\,\alpha_j\,\hat e_i\,dm=\Big(\int_N r_i r_j\,dm\Big)\alpha_j\,\hat e_i=Q_{ij}\,\alpha_j\,\hat e_i=\mathbf Q\,\vec\alpha.$$
> El primer término da $\displaystyle\int_N\vec\alpha\,r^2\,dm=\vec\alpha\int_N r^2\,dm=\Big(\int_N r_kr_k\,dm\Big)\vec\alpha=Q_{kk}\,\vec\alpha=\mathrm{Tr}(\mathbf Q)\,\mathbb 1\,\vec\alpha$.
> Restando,
> $$J_1=\big[\mathrm{Tr}(\mathbf Q)\,\mathbb 1-\mathbf Q\big]\vec\alpha=\mathbf I_c\,\vec\alpha.\qquad\blacksquare$$

> [!demostracion] Término $I_1$ — Paso 3: $J_2$ produce $\vec\omega\times(\mathbf I_c\vec\omega)$
> Primero simplifico el integrando con el doble producto **dos veces**. Como
> $\vec\omega\times(\vec\omega\times\vec r)=\vec\omega(\vec\omega\cdot\vec r)-\vec r\,\omega^2$,
> $$\vec r\times[\vec\omega\times(\vec\omega\times\vec r)]=\vec r\times\big[\vec\omega(\vec\omega\cdot\vec r)-\vec r\,\omega^2\big]=(\vec r\times\vec\omega)(\vec\omega\cdot\vec r)-\underbrace{(\vec r\times\vec r)}_{\vec0}\,\omega^2=(\vec r\times\vec\omega)(\vec r\cdot\vec\omega).$$
> Ahora a **índices**, con $\vec r\times\vec\omega=r_i\omega_j\,\epsilon_{ijl}\hat e_l$ y
> $\vec r\cdot\vec\omega=r_k\omega_k$:
> $$J_2=\int_N r_i\,\omega_j\,r_k\,\omega_k\,\epsilon_{ijl}\,\hat e_l\,dm=\Big(\int_N r_i r_k\,dm\Big)\omega_j\omega_k\,\epsilon_{ijl}\,\hat e_l=Q_{ik}\,\omega_k\,\omega_j\,\epsilon_{ijl}\,\hat e_l.$$
> Reconozco que $Q_{ik}\omega_k=(\mathbf Q\vec\omega)_i$ y que $\omega_j\,\epsilon_{ijl}\hat e_l$ es la
> componente $l$ de $(\mathbf Q\vec\omega)\times\vec\omega$:
> $$J_2=(\mathbf Q\vec\omega)_i\,\omega_j\,\epsilon_{ijl}\,\hat e_l=(\mathbf Q\vec\omega)\times\vec\omega.$$
> Falta pasar de $\mathbf Q$ a $\mathbf I_c$. Como
> $\mathbf I_c\vec\omega=\mathrm{Tr}(\mathbf Q)\vec\omega-\mathbf Q\vec\omega$ y
> $\vec\omega\times\vec\omega=\vec0$,
> $$\vec\omega\times(\mathbf I_c\vec\omega)=\mathrm{Tr}(\mathbf Q)\,\underbrace{\vec\omega\times\vec\omega}_{\vec0}-\vec\omega\times(\mathbf Q\vec\omega)=-\vec\omega\times(\mathbf Q\vec\omega)=(\mathbf Q\vec\omega)\times\vec\omega.$$
> Por tanto $J_2=\vec\omega\times(\mathbf I_c\vec\omega)$, y $I_1=J_1+J_2=\mathbf I_c\vec\alpha+\vec\omega\times(\mathbf I_c\vec\omega)$. $\blacksquare$

> [!demostracion] Término $I_2$ — el brazo del centro de masa
> $$I_2=\int_N \vec r_{c/o}\times\big[\vec a_c+\vec\alpha\times\vec r+\vec\omega\times(\vec\omega\times\vec r)\big]\,dm.$$
> El vector $\vec r_{c/o}$ es **constante** (sale de la integral); en los dos últimos sumandos queda un
> $\int_N\vec r\,dm=\vec0$ y mueren. Sobrevive solo el de $\vec a_c$:
> $$I_2=\vec r_{c/o}\times\vec a_c\int_N dm=\vec r_{c/o}\times(m\,\vec a_c)=\vec r_{c/o}\times\vec F,$$
> con $\vec F=m\vec a_c$ la resultante externa (Newton para el CM). $\blacksquare$

> [!proposicion] Forma final, Euler y componentes
> Sumando, $\vec\tau^o=\mathbf I_c\vec\alpha+\vec\omega\times(\mathbf I_c\vec\omega)+\vec r_{c/o}\times\vec F$.
> Con origen en el CM ($\vec r_{c/o}=\vec0$),
> $\vec\tau^c=\mathbf I_c\vec\alpha+\vec\omega\times(\mathbf I_c\vec\omega)$. En **ejes principales**
> (con $\vec H=(I_1\omega_1,I_2\omega_2,I_3\omega_3)$ y desarrollando $\vec\omega\times\vec H$):
> $\tau_1=I_1\dot\omega_1-(I_2-I_3)\omega_2\omega_3$ y cíclicas — las ecuaciones de Euler clásicas.

> [!warning]
> El término giroscópico $\vec\omega\times(\mathbf I\vec\omega)$ **no** existe en 2D (allí $\vec\omega\parallel\mathbf I\vec\omega\parallel\hat k$): es genuinamente 3D. El paso clave del Paso 3 es que
> $\vec r\times\vec r=\vec0$ colapsa el doble producto; sin eso no aparecería la estructura
> $(\mathbf Q\vec\omega)\times\vec\omega$. La fórmula con $\vec r_{c/o}\times\vec F$ vale para cualquier
> $O$; conviene $O=C$ o un punto fijo.

## Resumen

> [!resumen]
> | Paso | Contracción | Resultado |
> |:---|:---|:---|
> | $J_1$ | $\vec r(\vec r\cdot\vec\alpha)\to Q_{ij}\alpha_j$; $\,r^2\to Q_{kk}$ | $\mathbf I_c\vec\alpha$ |
> | $J_2$ | $r_i r_k\,\omega_k\omega_j\epsilon_{ijl}\to (\mathbf Q\vec\omega)\times\vec\omega$ | $\vec\omega\times(\mathbf I_c\vec\omega)$ |
> | $I_2$ | $\int\vec r\,dm=\vec0$ | $\vec r_{c/o}\times\vec F$ |
> | Total | — | $\vec\tau^o=\mathbf I_c\vec\alpha+\vec\omega\times(\mathbf I_c\vec\omega)+\vec r_{c/o}\times\vec F$ |

> [!corolario]
> La ecuación de Euler no es un axioma: se **integra** desde $d\vec\tau=\vec r\times\vec a\,dm$, y el
> tensor de inercia $\mathbf I=\mathrm{Tr}(\mathbf Q)\mathbb 1-\mathbf Q$ **aparece** al contraer los
> índices $Q_{ij}=\int r_ir_j\,dm$. Ese es el sentido de deducirlo con tensores: ver nacer la
> estructura, no postularla.

> [!referencia]
> Goldstein §5. Mismo término vía operador: [[Operador Derivada en Base Movil]]. Hermanas:
> [[Deduccion del Momento Angular]], [[Deduccion de la Energia Cinetica]]. Aplicación:
> [[Ecuaciones de Euler 3D]].
