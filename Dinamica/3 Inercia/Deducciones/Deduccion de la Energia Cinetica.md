---
title: Deducción de la Energía Cinética
order: 3
tags:
  - dinamica
  - teoria
  - inercia
draft: false
aliases:
  - deducción de la energía cinética
  - teorema de König rotacional
  - kinetic energy rigid body
---

# Deducción de la Energía Cinética $\;T=\tfrac12 m v_c^2+\tfrac12\,\vec\omega\cdot\mathbf I_c\vec\omega$

> [!definicion]
> Integrando $dT=\tfrac12 v_p^2\,dm$ sobre el cuerpo rígido, con **el desarrollo indicial completo**, se obtiene la descomposición de **König**:
> $$\boxed{\;T=\tfrac12 m v_c^2+\tfrac12\,\vec\omega\cdot\mathbf I_c\,\vec\omega\;}$$
> energía de **traslación** del CM más energía de **rotación**. El tensor de inercia surge al contraer el doble producto con el símbolo de Levi-Civita.

> [!info]
> Deducción de la [[Deducciones/index | inercia]]; hermana de [[Deduccion del Momento Angular]] y [[Deduccion del Torque]]; usa el [[Tensor de Inercia]]. Goldstein §5.

---

## Ejemplo

> [!ejemplo]
> **Un cilindro que rueda: cuánta energía es rotacional.**
>
> Un cilindro ($I_c=\tfrac12 mR^2$) rueda sin deslizar a velocidad $v_c$ ($\omega=v_c/R$). Hallar $T$.
>
> $$T=\tfrac12 m v_c^2+\tfrac12\Big(\tfrac12 mR^2\Big)\Big(\tfrac{v_c}{R}\Big)^2=\tfrac12 m v_c^2+\tfrac14 m v_c^2=\tfrac34 m v_c^2.$$
>
> > [!solucion]
> > $T=\tfrac34 m v_c^2$: **un tercio** de la energía ($\tfrac14$ sobre $\tfrac34$) es rotacional. Por eso un cilindro rueda más despacio que un bloque que desliza: parte de la energía va al giro.

---

## En qué consiste

> [!definicion] Convenios y herramientas
> Notación indicial con suma sobre repetidos; $\vec r\equiv\vec r_{p/c}$; $Q_{ij}=\int r_i r_j\,dm$ y $\mathbf I=\mathrm{Tr}(\mathbf Q)\mathbb 1-\mathbf Q$. Propiedad del CM $\int\vec r\,dm=\vec0$, y la identidad de Levi-Civita $\epsilon_{ijk}\epsilon_{mnk}=\delta_{im}\delta_{jn}-\delta_{in}\delta_{jm}$.

![[cuerpo_inercia.svg|420]]

*Se integra sobre el cuerpo: cada elemento $dm$ a posición $\vec r$ aporta su energía $\tfrac12 v^2\,dm$.*

> [!teorema] Punto de partida
> Con $\vec v_p=\vec v_c+\vec\omega\times\vec r$,
> $$v_p^2=\vec v_p\cdot\vec v_p=v_c^2+2\,\vec v_c\cdot(\vec\omega\times\vec r)+(\vec\omega\times\vec r)\cdot(\vec\omega\times\vec r),$$
> de modo que $T=\displaystyle\int_N\tfrac12 v_p^2\,dm$ se parte en tres integrales.

> [!demostracion] El término lineal muere; el constante da $\tfrac12 m v_c^2$
> **Cruzado:** $\vec v_c$ y $\vec\omega$ son constantes, así que
> $$\int_N\tfrac12\,2\,\vec v_c\cdot(\vec\omega\times\vec r)\,dm=\vec v_c\cdot\Big(\vec\omega\times\underbrace{\int_N\vec r\,dm}_{\vec0}\Big)=0.$$
> **Constante:** $\displaystyle\int_N\tfrac12 v_c^2\,dm=\tfrac12 v_c^2\int_N dm=\tfrac12 m v_c^2$. $\blacksquare$

> [!demostracion] El término cuadrático da $\tfrac12\,\vec\omega\cdot\mathbf I_c\vec\omega$
> Escribo $\vec\omega\times\vec r=\omega_i r_j\,\epsilon_{ijk}\,\hat e_k$. El producto escalar consigo mismo contrae dos Levi-Civita por el índice $k$:
> $$(\vec\omega\times\vec r)\cdot(\vec\omega\times\vec r)=(\omega_i r_j\epsilon_{ijk})(\omega_m r_n\epsilon_{mnk})=\omega_i r_j\,\omega_m r_n\,\epsilon_{ijk}\epsilon_{mnk}.$$
> Usando $\epsilon_{ijk}\epsilon_{mnk}=\delta_{im}\delta_{jn}-\delta_{in}\delta_{jm}$,
> $$\omega_i r_j\omega_m r_n(\delta_{im}\delta_{jn}-\delta_{in}\delta_{jm})=\underbrace{\omega_i\omega_i\,r_j r_j}_{\omega^2 r^2}-\underbrace{(\omega_i r_i)(\omega_j r_j)}_{(\vec\omega\cdot\vec r)^2}.$$
> Integrando cada parte:
> $$\int_N\omega_i\omega_i\,r_j r_j\,dm=\omega_i\omega_i\,Q_{jj}=\vec\omega\cdot\big[\mathrm{Tr}(\mathbf Q)\,\mathbb 1\big]\cdot\vec\omega,\qquad \int_N\omega_i r_i\,\omega_j r_j\,dm=\omega_i\omega_j\,Q_{ij}=\vec\omega\cdot\mathbf Q\cdot\vec\omega.$$
> Por tanto, con el factor $\tfrac12$,
> $$\int_N\tfrac12(\vec\omega\times\vec r)^2\,dm=\tfrac12\,\vec\omega\cdot\big[\mathrm{Tr}(\mathbf Q)\mathbb 1-\mathbf Q\big]\cdot\vec\omega=\tfrac12\,\vec\omega\cdot\mathbf I_c\,\vec\omega.\qquad\blacksquare$$

> [!proposicion] Forma final, ejes principales y positividad
> Sumando, $T=\tfrac12 m v_c^2+\tfrac12\,\vec\omega\cdot\mathbf I_c\vec\omega$. En **ejes principales**, $T_{rot}=\tfrac12(I_1\omega_1^2+I_2\omega_2^2+I_3\omega_3^2)$. Como $T_{rot}>0$ para todo $\vec\omega\neq\vec0$, esta deducción **prueba** que $\mathbf I_c$ es **definido positivo**.

> [!warning]
> La separación traslación+rotación (König) exige tomar la rotación respecto al **CM** (es la propiedad $\int\vec r\,dm=\vec0$ la que mata el término cruzado). $T_{rot}=\tfrac12\vec\omega\cdot\mathbf I\vec\omega$ usa el tensor en el **mismo** punto que $\vec\omega$ (CM o punto fijo). El paso clave es la identidad $\epsilon_{ijk}\epsilon_{mnk}=\delta_{im}\delta_{jn}-\delta_{in}\delta_{jm}$.

## Resumen

> [!resumen]
> | Término | Contracción | Resultado |
> |:---|:---|:---|
> | Constante | $\int dm=m$ | $\tfrac12 m v_c^2$ |
> | Cruzado | $\int\vec r\,dm=\vec0$ | $0$ |
> | Cuadrático | $\epsilon_{ijk}\epsilon_{mnk}=\delta\delta-\delta\delta\to\omega^2r^2-(\vec\omega\cdot\vec r)^2$ | $\tfrac12\,\vec\omega\cdot\mathbf I_c\vec\omega$ |
> | Total | — | $T=\tfrac12 m v_c^2+\tfrac12\,\vec\omega\cdot\mathbf I_c\vec\omega$ |

> [!corolario]
> La energía cinética del sólido se **integra** desde $\tfrac12 v^2\,dm$: la contracción de los dos Levi-Civita hace nacer $\mathrm{Tr}(\mathbf Q)\mathbb 1-\mathbf Q=\mathbf I_c$. Verlo con índices es el sentido de la deducción tensorial.

> [!referencia]
> Goldstein §5. Hermanas: [[Deduccion del Momento Angular]], [[Deduccion del Torque]]. Tensor: [[Tensor de Inercia]].
