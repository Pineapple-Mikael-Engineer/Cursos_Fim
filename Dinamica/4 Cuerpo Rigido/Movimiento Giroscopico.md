---
title: Movimiento Giroscópico
tags:
  - dinamica
  - teoria
  - cuerpo-rigido
draft: false
aliases:
  - giróscopo
  - precesión
  - gyroscopic motion
  - precession
---

# Movimiento Giroscópico $\vec M=\vec\Omega\times\vec H$

> [!definicion]
> Un **giróscopo** es un cuerpo que gira deprisa sobre su eje (spin $\vec\omega$). Sometido a un torque $\vec M$ perpendicular a su eje, **no cae**: su eje **precesa** (gira) en dirección perpendicular al torque, con velocidad de precesión $\vec\Omega$ tal que
> $$\vec M=\vec\Omega\times\vec H\quad\Longrightarrow\quad M=\Omega\,I\omega\ \ (\text{spin rápido},\ \vec\Omega\perp\vec H).$$

> [!info]
> Es el efecto estrella de la cinética 3D del [[4 Cuerpo Rigido/index | cuerpo rígido]]: el término giroscópico $\vec\omega\times(\mathbf I\vec\omega)$ de las [[Ecuaciones de Euler 3D]] en acción, vía el [[Operador Derivada en Base Movil | operador]] aplicado sobre $\vec H$. Goldstein §5.7.

---

## Ejemplo

> [!ejemplo] Rotor pivotado bajo su peso
> Un rotor de momento de inercia $I$ gira con spin $\omega$ en un eje horizontal pivotado en $O$; su peso $mg$ actúa a distancia $L$ del pivote. Hallar la velocidad de precesión $\Omega$.
>
> ![[giroscopo.svg|520]]

> [!solucion]
> El momento angular del rotor apunta a lo largo del eje, $\vec H\approx I\omega$ (spin rápido). El peso genera un torque respecto al pivote
> $$M=mgL,$$
> **horizontal** y **perpendicular** a $\vec H$ (que es horizontal a lo largo del eje). De la condición de precesión estacionaria $M=\Omega\,I\omega$ se despeja
> $$\boxed{\ \Omega=\dfrac{mgL}{I\omega}\ }.$$
> El eje precesa **horizontalmente** en vez de caer; cuanto **más rápido** el spin, **más lenta** la precesión.

---

## En qué consiste

> [!teoria]
> En el spin rápido el momento angular se alinea con el eje de giro, $\vec H\approx I\vec\omega$, de módulo casi constante. La segunda ley para rotaciones $\vec M=\dfrac{d\vec H}{dt}$ obliga entonces a que $\vec H$ **cambie de dirección** —no de módulo— y ese giro del vector $\vec H$ es la **precesión**. El operador en base móvil traduce ese giro en $\vec\Omega\times\vec H$, cerrando la ecuación maestra $\vec M=\vec\Omega\times\vec H$. La clave geométrica: el torque no tumba el eje, lo **arrastra de lado**.

> [!teorema] Precesión estacionaria
> Para un giróscopo de spin rápido $\omega$ y momento de inercia axial $I$, sometido a un torque $\vec M$ perpendicular al eje, el eje precesa con velocidad angular $\vec\Omega$ que satisface
> $$\vec M=\vec\Omega\times\vec H,\qquad \vec H\approx I\vec\omega,$$
> y en módulo, con $\vec\Omega\perp\vec H$,
> $$M=\Omega\,I\omega\quad\Longrightarrow\quad \Omega=\dfrac{M}{I\omega}.$$

> [!demostracion]
> Para spin rápido el momento angular se concentra en el eje, $\vec H\approx I\vec\omega$, dirigido a lo largo del eje del rotor. Partimos de la ley de rotación
> $$\vec M=\dfrac{d\vec H}{dt}.$$
> Si el eje (y con él $\vec H$) precesa rígidamente con velocidad angular $\vec\Omega$, el [[Operador Derivada en Base Movil | operador derivada en base móvil]] aplicado a $\vec H$ da
> $$\dfrac{d\vec H}{dt}=\underbrace{\left(\dfrac{d\vec H}{dt}\right)_{\text{rel}}}_{=\,0}+\;\vec\Omega\times\vec H=\vec\Omega\times\vec H,$$
> pues el **módulo** de $\vec H$ no cambia (solo su dirección gira con $\vec\Omega$), de modo que su derivada relativa al eje es nula. Igualando ambas expresiones,
> $$\vec M=\vec\Omega\times\vec H.$$
> Tomando módulos con $\vec\Omega\perp\vec H$ (precesión perpendicular al momento angular),
> $$M=\Omega\,H=\Omega\,I\omega\quad\Longrightarrow\quad \Omega=\dfrac{M}{I\omega}.\qquad\blacksquare$$

> [!proposicion] La respuesta es perpendicular al torque
> El eje **no** se mueve en la dirección del torque, sino **perpendicular** a él: empujar el eje hacia un lado lo hace girar hacia otro. Esta contraintuición es la base de la **brújula giroscópica**, la **estabilidad** de bicicletas y proyectiles rayados, y los **girostabilizadores**.

> [!warning]
> La fórmula $M=\Omega\,I\omega$ es la **aproximación de spin rápido** (precesión estacionaria); en general el eje además **nuta** (oscila), término que aquí se desprecia. Ojo: $\vec\Omega$ (precesión, **lenta**) y $\vec\omega$ (spin, **rápida**) son rotaciones **distintas**; la velocidad angular total es su **suma** $\vec\omega_{\text{tot}}=\vec\omega+\vec\Omega$.

---

## Resumen

> [!resumen]
> | Concepto | Resultado |
> |---|---|
> | Ecuación maestra | $\vec M=\vec\Omega\times\vec H$ |
> | Momento angular (spin rápido) | $\vec H\approx I\vec\omega$ (a lo largo del eje) |
> | Velocidad de precesión | $\Omega=\dfrac{M}{I\omega}$ |
> | Dirección de la respuesta | **perpendicular** al torque |
> | Validez | spin rápido; nutación despreciada |

> [!corolario]
> A mayor spin $\omega$, **menor** precesión $\Omega$: un giróscopo veloz es muy **rígido** direccionalmente y resiste cambios de orientación, lo que explica su uso como referencia de orientación inercial. Si $\omega\to 0$, $\Omega\to\infty$ y la aproximación colapsa: el cuerpo simplemente cae.

> [!referencia]
> - [[Ecuaciones de Euler 3D]] — origen del término giroscópico $\vec\omega\times(\mathbf I\vec\omega)$.
> - [[Operador Derivada en Base Movil]] — herramienta para $\dfrac{d\vec H}{dt}=\vec\Omega\times\vec H$.
> - [[Deduccion del Momento Angular]] — de dónde sale $\vec H=\mathbf I\vec\omega$.
> - [[4 Cuerpo Rigido/index]] — marco general de la cinética 3D.
> - Goldstein, *Classical Mechanics*, §5.7.
