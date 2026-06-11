---
title: Deducción de la Energía Cinética
tags:
  - dinamica
  - teoria
  - inercia
draft: false
aliases:
  - energía cinética del sólido
  - teorema de König rotacional
  - kinetic energy rigid body
---

# Deducción de la Energía Cinética $\;T=\tfrac12 m v_c^2+\tfrac12\,\vec\omega\cdot\mathbf I_c\,\vec\omega$

> [!definicion]
> Integrando la energía cinética elemental $dT=\tfrac12 v_p^2\,dm$ sobre el cuerpo rígido se obtiene,
> **sin postular nada**, la **descomposición de König**
> $$\boxed{\;T=\tfrac12 m v_c^2+\tfrac12\,\vec\omega\cdot\mathbf I_c\,\vec\omega\;}$$
> la energía de **traslación** del centro de masa $C$ más la energía de **rotación** alrededor de él.

> [!info]
> Una de las deducciones de la [[Deducciones/index | inercia]]; hermana de
> [[Deduccion del Momento Angular]] y [[Deduccion del Torque]]. Usa el segundo momento
> $Q_{ij}=\int r_ir_j\,dm$ y el [[Tensor de Inercia]] $\mathbf I_c=\mathrm{Tr}(\mathbf Q)\mathbb 1-\mathbf Q$.
> Referencia: Goldstein §5.

---

## Ejemplo

> [!ejemplo]
> **Un cilindro que rueda sin deslizar.**
>
> Cilindro de masa $m$, radio $R$, con $I_c=\tfrac12 mR^2$, que **rueda sin deslizar** a velocidad del
> centro $v_c$. La condición de rodadura fija $\omega=v_c/R$. Por König,
> $$T=\tfrac12 m v_c^2+\tfrac12\Big(\tfrac12 mR^2\Big)\Big(\frac{v_c}{R}\Big)^2=\tfrac12 m v_c^2+\tfrac14 m v_c^2=\tfrac34 m v_c^2.$$
>
> > [!solucion]
> > $T=\tfrac34 m v_c^2$. La fracción rotacional es $\dfrac{\tfrac14}{\tfrac34}=\tfrac13$: **un tercio**
> > de la energía cinética total es de rotación, y dos tercios de traslación.

---

## En qué consiste

> [!teorema] Punto de partida
> La energía cinética del sólido es la integral sobre el cuerpo $N$
> $$T=\int_N\tfrac12 v_p^2\,dm,\qquad \vec v_p=\vec v_c+\vec\omega\times\vec r_{p/c},$$
> con $\vec v_p$ la velocidad de cada punto material según la cinemática rígida.

> [!demostracion] Descomposición de König
> **Paso 1 — Desarrollar $v_p^2$.** Con $\vec v_p=\vec v_c+\vec\omega\times\vec r_{p/c}$,
> $$v_p^2=\vec v_p\cdot\vec v_p=v_c^2+2\,\vec v_c\cdot(\vec\omega\times\vec r_{p/c})+(\vec\omega\times\vec r_{p/c})\cdot(\vec\omega\times\vec r_{p/c}).$$
> **Paso 2 — El término lineal se anula (propiedad del CM).** Como $\vec v_c$ y $\vec\omega$ son comunes
> a todo el cuerpo, salen de la integral:
> $$\int_N\vec v_c\cdot(\vec\omega\times\vec r_{p/c})\,dm=\vec v_c\cdot\Big(\vec\omega\times\int_N\vec r_{p/c}\,dm\Big)=0,$$
> pues $\int_N\vec r_{p/c}\,dm=\vec0$ por definición del centro de masa. El término constante $v_c^2$ da,
> con el factor $\tfrac12$ y $\int_N dm=m$, la energía de traslación $\tfrac12 m v_c^2$.
> **Paso 3 — El término cuadrático.** Indexando $\vec\omega\times\vec r=\omega_i r_j\,\epsilon_{ijk}\,\hat e_k$
> y usando la identidad $\epsilon_{ijk}\epsilon_{mnk}=\delta_{im}\delta_{jn}-\delta_{in}\delta_{jm}$,
> $$(\vec\omega\times\vec r)\cdot(\vec\omega\times\vec r)=\epsilon_{ijk}\epsilon_{mnk}\,\omega_i r_j\omega_m r_n=\omega_i\omega_i\,r_jr_j-(\omega_ir_i)(\omega_jr_j)=\omega^2 r^2-(\vec\omega\cdot\vec r)^2.$$
> Integrando sobre $dm$, con $\int r_ir_j\,dm=Q_{ij}$ y $\int r^2\,dm=\mathrm{Tr}(\mathbf Q)$,
> $$\int_N\big[\omega^2 r^2-(\vec\omega\cdot\vec r)^2\big]dm=\vec\omega\cdot\big[\mathrm{Tr}(\mathbf Q)\mathbb 1-\mathbf Q\big]\cdot\vec\omega=\vec\omega\cdot\mathbf I_c\,\vec\omega,$$
> ya que $\mathbf I_c=\mathrm{Tr}(\mathbf Q)\mathbb 1-\mathbf Q$. Con el factor $\tfrac12$, esto aporta
> $\tfrac12\,\vec\omega\cdot\mathbf I_c\,\vec\omega$.
> **Suma.** Reuniendo los tres pasos,
> $$T=\tfrac12 m v_c^2+\tfrac12\,\vec\omega\cdot\mathbf I_c\,\vec\omega.\qquad\blacksquare$$

> [!proposicion] Ejes principales y positividad
> En **ejes principales** del cuerpo, $\mathbf I_c$ es diagonal y la energía de rotación se reduce a
> $$T_{rot}=\tfrac12\big(I_1\omega_1^2+I_2\omega_2^2+I_3\omega_3^2\big).$$
> Como cada $I_i>0$ y la forma cuadrática $\tfrac12\,\vec\omega\cdot\mathbf I_c\,\vec\omega>0$ para todo
> $\vec\omega\neq\vec0$, el tensor de inercia es **definido positivo**.

> [!warning]
> La separación **traslación + rotación** (König) exige medir la rotación respecto al **centro de masa**:
> solo entonces se anula el término cruzado del Paso 2. Por otro lado, la fórmula
> $T_{rot}=\tfrac12\,\vec\omega\cdot\mathbf I\,\vec\omega$ requiere usar el tensor $\mathbf I$ en el
> **mismo** punto en que se evalúa $\vec\omega$ (el CM, o un punto fijo del cuerpo).

## Resumen

> [!resumen]
> | Concepto | Expresión |
> |:---|:---|
> | König (CM) | $T=\tfrac12 m v_c^2+\tfrac12\,\vec\omega\cdot\mathbf I_c\,\vec\omega$ |
> | Traslación | $\tfrac12 m v_c^2$ |
> | Rotación | $\tfrac12\,\vec\omega\cdot\mathbf I_c\,\vec\omega$ |
> | Ejes principales | $T_{rot}=\tfrac12\sum_i I_i\omega_i^2$ |

> [!corolario]
> La energía cinética del sólido no es un axioma: se **integra** desde $dT=\tfrac12 v_p^2\,dm$, y el
> tensor de inercia emerge al reducir el término cuadrático. El cruzado se anula por el CM (König) y la
> forma rotacional, definida positiva, confirma que $\mathbf I_c\succ 0$.

> [!referencia]
> Goldstein §5. Tensor: [[Tensor de Inercia]]. Hermanas: [[Deduccion del Momento Angular]],
> [[Deduccion del Torque]]. Índice: [[Deducciones/index]].
