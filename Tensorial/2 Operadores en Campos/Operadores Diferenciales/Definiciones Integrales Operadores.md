---
title: Definiciones Integrales de los Operadores
tags:
  - analisis-tensorial
  - teoria
  - calculo-vectorial
  - operadores
draft: false
aliases:
  - definiciones integrales
  - operadores como limite integral
  - integral definitions of operators
---

# Definiciones Integrales de los Operadores

> [!definicion]
> Los tres operadores diferenciales admiten una **definición integral**, como límite del cociente entre una integral de superficie sobre una superficie cerrada $S$ y el volumen $V$ que encierra, cuando ambos tienden a un punto:
> $$\vec\nabla\Phi=\lim_{S,V\to0}\frac{\oint_S\Phi\,d\vec\sigma}{\int_V d\tau},\quad
> \vec\nabla\cdot\vec A=\lim_{S,V\to0}\frac{\oint_S d\vec\sigma\cdot\vec A}{\int_V d\tau},\quad
> \vec\nabla\times\vec A=\lim_{S,V\to0}\frac{\oint_S d\vec\sigma\times\vec A}{\int_V d\tau}.$$
> Gradiente, divergencia y rotor se distinguen sólo por cómo $d\vec\sigma$ se combina con el integrando: producto directo, punto o cruz.

> [!info]
> Sección **2.4** del libro, dentro de [[index | operadores diferenciales]]. Estas formas no dependen del sistema de coordenadas: son la **base de los teoremas integrales** (Gauss, Stokes), que se obtienen sumando volúmenes diferenciales contiguos. Ver [[Teoremas Integrales/index | teoremas integrales]]. La forma del rotor con $d\vec\sigma\times\vec A$ ya se había obtenido en la deducción del [[Rotor | rotor]] (cap. 2.3.3).

---

## Ejemplo

> [!ejemplo]
> **La definición integral de la divergencia reproduce $\partial A_i/\partial x_i$.** Tomamos el cubo diferencial $d\tau=dx\,dy\,dz$ con vértice en $(x_0,y_0,z_0)$ y evaluamos $\oint_S d\vec\sigma\cdot\vec A$ por sus seis caras.
>
> **Par de caras en $z$.** La cara superior tiene normal saliente $+\hat{e}_z$ y la inferior $-\hat{e}_z$, ambas de área $dx\,dy$:
> $$\big[A_z(z_0+dz)-A_z(z_0)\big]dx\,dy.$$
> Por Taylor, $A_z(z_0+dz)=A_z(z_0)+(\partial A_z/\partial z)\,dz$, de modo que la contribución es $\dfrac{\partial A_z}{\partial z}\,dx\,dy\,dz$.
>
> **Las tres direcciones.** Sumando los tres pares de caras:
> $$\oint_S d\vec\sigma\cdot\vec A=\left(\frac{\partial A_x}{\partial x}+\frac{\partial A_y}{\partial y}+\frac{\partial A_z}{\partial z}\right)dx\,dy\,dz=\frac{\partial A_i}{\partial x_i}\,d\tau.$$
>
> **Cociente y límite.** Dividiendo por $\int_V d\tau=d\tau$:
> $$\vec\nabla\cdot\vec A=\lim_{S,V\to0}\frac{\oint_S d\vec\sigma\cdot\vec A}{\int_V d\tau}=\frac{\partial A_i}{\partial x_i}.$$
> Es el mismo conteo de flujo por las seis caras de la [[Divergencia | ecuación de continuidad]], ahora con signos dados por la normal saliente.

---

## En qué consiste

> [!teoria]
> Las definiciones diferenciales ($\vec\nabla\Phi=\hat{e}_i\partial\Phi/\partial x_i$, etc.) sólo valen en cartesianas y se escriben con derivadas espaciales. Las **definiciones integrales** son geométricas e independientes del sistema de coordenadas: capturan al operador como "flujo del campo a través de una superficie que se cierra sobre un punto, por unidad de volumen". Sus deducciones son análogas a la del [[Rotor | rotor]] (ec. 2.63) y se encuentran en los textos de cálculo.

> [!proposicion] Puente con los teoremas integrales
> Escrita como $\vec\nabla\cdot\vec A\,d\tau=\oint_S d\vec\sigma\cdot\vec A$ en el límite, la definición integral se aplica a dos volúmenes adyacentes: las contribuciones de su **superficie común se cancelan** (normales opuestas). Sumando volúmenes diferenciales contiguos hasta formar un volumen $V$ encerrado por $S$ se obtiene el **teorema de Gauss**,
> $$\int_V d\tau\,\vec\nabla\cdot\vec A=\oint_S d\vec\sigma\cdot\vec A.$$
> El mismo mecanismo, con la forma del rotor, conduce al teorema de Stokes.

> [!info] Las tres definiciones
> | Operador | Definición integral | Combinación de $d\vec\sigma$ |
> |---|---|---|
> | Gradiente $\vec\nabla\Phi$ | $\lim\dfrac{\oint_S\Phi\,d\vec\sigma}{\int_V d\tau}$ | producto directo |
> | Divergencia $\vec\nabla\cdot\vec A$ | $\lim\dfrac{\oint_S d\vec\sigma\cdot\vec A}{\int_V d\tau}$ | producto punto |
> | Rotor $\vec\nabla\times\vec A$ | $\lim\dfrac{\oint_S d\vec\sigma\times\vec A}{\int_V d\tau}$ | producto cruz |

> [!warning]
> La definición integral del rotor con $\oint_S d\vec\sigma\times\vec A$ (integral de superficie poco común) reemplaza a la forma de circulación $\lim\,\oint_C d\vec r\cdot\vec v/\int_S d\sigma$ del cap. 2.3.3, que es algo torpe porque exige tres integrales con distintas orientaciones de $S$ para las tres componentes. Ambas describen el mismo rotor.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Forma general | $\lim_{S,V\to0}\,\big(\oint_S \cdots d\vec\sigma\big)/\int_V d\tau$ |
> | Ventaja | independiente de coordenadas |
> | Gradiente | $\Phi\,d\vec\sigma$ |
> | Divergencia | $d\vec\sigma\cdot\vec A$ |
> | Rotor | $d\vec\sigma\times\vec A$ |
> | Para qué sirven | base de los teoremas de Gauss y Stokes |

> [!corolario]
> Las definiciones integrales reescriben gradiente, divergencia y rotor como flujos por unidad de volumen, sin referencia a coordenadas. Al sumar volúmenes contiguos cuyas caras internas se cancelan, conducen directamente a los [[Teoremas Integrales/index | teoremas integrales]], que elevan los operadores de la escala infinitesimal a la macroscópica.

> [!referencia]
> - Teoremas que se construyen sobre ellas: [[Teoremas Integrales/index]].
> - Conteo de flujo por las seis caras: [[Divergencia]] (ecuación de continuidad).
> - Forma de circulación del rotor: [[Rotor]].
> - Integrales de superficie y volumen: [[Operadores Integrales/index]].
