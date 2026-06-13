---
title: Deducción del Momento Angular
tags:
  - dinamica
  - teoria
  - inercia
draft: false
aliases:
  - deducción del momento angular
  - H=Iω deducción
  - angular momentum derivation
---

# Deducción del Momento Angular $\;\vec H=\mathbf I_c\vec\omega+m\,\vec r_{c/o}\times\vec v_c$

> [!definicion]
> Integrando el momento angular elemental $d\vec H^o=\vec r_{p/o}\times\vec v_p\,dm$ sobre el cuerpo
> rígido, con **el desarrollo tensorial completo**, se obtiene
> $$\boxed{\;\vec H^o=\mathbf I_c\vec\omega+m\,\vec r_{c/o}\times\vec v_c\;}$$
> y, con origen en el centro de masa ($O=C$), $\vec H^c=\mathbf I_c\vec\omega$. El tensor de inercia
> **no se postula**: aparece al contraer $\int r_i r_j\,dm=Q_{ij}$.

> [!info]
> Una de las [[Deducciones/index | deducciones]] de la [[3 Inercia/index | inercia]]; hermana de
> [[Deduccion del Torque]] y [[Deduccion de la Energia Cinetica]]; usa el [[Tensor de Inercia]].
> Goldstein §5.

---

## Ejemplo

> [!ejemplo]
> **El momento angular no es paralelo a la velocidad angular.**
>
> Un cuerpo gira en torno a su CM ($O=C$), de modo que $\vec H^c=\mathbf I_c\vec\omega$. Si $\vec\omega$
> va sobre un eje **principal** ($\mathbf I_c\vec\omega=I\vec\omega$), entonces $\vec H=I\vec\omega$,
> paralelo a $\vec\omega$.
>
> > [!solucion]
> > En general $\vec H\nparallel\vec\omega$: el tensor "tuerce" la dirección. Solo coinciden en los
> > **ejes principales**. Por eso una rueda mal balanceada bambolea: su $\vec H$ no apunta como su
> > $\vec\omega$.

---

## En qué consiste

> [!definicion] Convenios y herramientas
> Notación indicial con suma sobre repetidos; $\vec r\equiv\vec r_{p/c}$; segundo momento
> $Q_{ij}=\int r_i r_j\,dm$ y tensor $\mathbf I=\mathrm{Tr}(\mathbf Q)\mathbb 1-\mathbf Q$
> ($I_{ij}=Q_{kk}\delta_{ij}-Q_{ij}$). Propiedad del CM: $\int\vec r\,dm=\vec0$. Doble producto:
> $\vec r\times(\vec\omega\times\vec r)=\vec\omega\,r^2-\vec r\,(\vec r\cdot\vec\omega)$.

![[cuerpo_inercia.svg|420]]

*Se integra sobre el cuerpo: cada elemento $dm$ a posición $\vec r$ aporta su momento angular.*

> [!teorema] Punto de partida
> Con $\vec v_p=\vec v_c+\vec\omega\times\vec r$ (velocidad de un punto del sólido) y
> $\vec r_{p/o}=\vec r+\vec r_{c/o}$,
> $$\vec H^o=\int_N\vec r_{p/o}\times\vec v_p\,dm=\underbrace{\int_N\vec r\times\vec v_p\,dm}_{I_1}+\underbrace{\int_N\vec r_{c/o}\times\vec v_p\,dm}_{I_2}.$$

> [!demostracion] Término $I_1$ — produce $\mathbf I_c\vec\omega$
> $$I_1=\int_N\vec r\times(\vec v_c+\vec\omega\times\vec r)\,dm=\int_N\vec r\times\vec v_c\,dm+\int_N\vec r\times(\vec\omega\times\vec r)\,dm.$$
> **Primer término (muere por el CM):** $\displaystyle\int_N\vec r\times\vec v_c\,dm=\Big(\int_N\vec r\,dm\Big)\times\vec v_c=\vec0$.
> **Segundo término:** por el doble producto,
> $\vec r\times(\vec\omega\times\vec r)=\vec\omega\,r^2-\vec r\,(\vec r\cdot\vec\omega)$. En componentes,
> $$\vec r\,(\vec r\cdot\vec\omega)=r_i\hat e_i\,(r_j\omega_j)=r_i r_j\,\omega_j\,\hat e_i\ \Rightarrow\ \int_N r_i r_j\,\omega_j\,\hat e_i\,dm=Q_{ij}\,\omega_j\,\hat e_i=\mathbf Q\vec\omega,$$
> y $\displaystyle\int_N\vec\omega\,r^2\,dm=\Big(\int_N r_kr_k\,dm\Big)\vec\omega=Q_{kk}\vec\omega=\mathrm{Tr}(\mathbf Q)\,\mathbb 1\,\vec\omega$.
> Restando,
> $$I_1=\big[\mathrm{Tr}(\mathbf Q)\,\mathbb 1-\mathbf Q\big]\vec\omega=\mathbf I_c\vec\omega.\qquad\blacksquare$$

> [!demostracion] Término $I_2$ — el momento orbital del CM
> $$I_2=\int_N\vec r_{c/o}\times(\vec v_c+\vec\omega\times\vec r)\,dm.$$
> $\vec r_{c/o}$ y $\vec v_c$ son **constantes** respecto a la integral. El sumando con $\vec\omega\times\vec r$ muere:
> $$\int_N\vec r_{c/o}\times(\vec\omega\times\vec r)\,dm=\vec r_{c/o}\times\Big(\vec\omega\times\underbrace{\int_N\vec r\,dm}_{\vec0}\Big)=\vec0.$$
> Y el de $\vec v_c$ da $\displaystyle\int_N\vec r_{c/o}\times\vec v_c\,dm=\vec r_{c/o}\times\vec v_c\int_N dm=m\,\vec r_{c/o}\times\vec v_c$. $\blacksquare$

> [!proposicion] Forma final: espín + orbital
> $\vec H^o=\mathbf I_c\vec\omega+m\,\vec r_{c/o}\times\vec v_c$. El primer término es el momento angular
> de **espín** (rotación propia); el segundo, el **orbital** del CM (como una partícula con toda la masa
> en $C$). En $O=C$ queda solo el espín, $\vec H^c=\mathbf I_c\vec\omega$.

> [!warning]
> $\vec H$ **no** es paralelo a $\vec\omega$ salvo en ejes principales (el tensor cambia su dirección).
> El resultado limpio $\mathbf I_c\vec\omega$ exige tomar momentos respecto al **CM** o a un punto fijo.
> Derivando esta expresión respecto al tiempo se obtiene el [[Deduccion del Torque | torque]] (y de ahí
> Euler).

## Resumen

> [!resumen]
> | Término | Contracción | Resultado |
> |:---|:---|:---|
> | $I_1$ | $\vec r(\vec r\cdot\vec\omega)\to Q_{ij}\omega_j$; $\,r^2\to Q_{kk}$ | $\mathbf I_c\vec\omega$ (espín) |
> | $I_2$ | $\int\vec r\,dm=\vec0$ | $m\,\vec r_{c/o}\times\vec v_c$ (orbital) |
> | Total | — | $\vec H^o=\mathbf I_c\vec\omega+m\,\vec r_{c/o}\times\vec v_c$ |

> [!corolario]
> El momento angular del sólido se **integra**, no se postula: la combinación $r^2\mathbb 1-\vec r\vec r$
> que sobrevive es exactamente el tensor de inercia. Esa es la gracia de hacerlo con tensores: ver de
> dónde sale $\mathbf I_c\vec\omega$.

> [!referencia]
> Goldstein §5. Hermanas: [[Deduccion del Torque]], [[Deduccion de la Energia Cinetica]]. Tensor:
> [[Tensor de Inercia]].
