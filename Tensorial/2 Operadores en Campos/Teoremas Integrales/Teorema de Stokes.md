---
title: Teorema de Stokes
order: 3
tags:
  - analisis-tensorial
  - teoria
  - calculo-vectorial
  - teoremas-integrales
  - rotor
draft: false
aliases:
  - teorema de Stokes
  - teorema del rotor
  - campo conservativo
  - Stokes theorem
  - curl theorem
---

# Teorema de Stokes

> [!definicion]
> Para todo campo vectorial $\vec A$ y una superficie $S$ (no necesariamente plana) bordeada por el contorno cerrado $C$,
> $$\int_S d\vec\sigma\cdot(\vec\nabla\times\vec A)=\oint_C d\vec r\cdot\vec A.$$
> La **circulación** de $\vec A$ a lo largo del borde $C$ es igual al flujo de su rotor a través de la superficie $S$. La orientación de $d\vec\sigma$ y el sentido de recorrido de $C$ se ligan por la regla de la mano derecha.

> [!info]
> Es el *cap 2.5.3* del [[index | capítulo 2.5]] (Rogan & Muñoz). Se deduce de la [[Operadores Diferenciales/Rotor | definición integral del rotor]] (cap. 2.3), igual que el [[Teorema de Gauss]] se deduce de la divergencia. El contorno se integra con $d\vec r$ de la [[Operadores Integrales/Integral de Linea | integral de línea]] (cap. 2.2). Da lugar a la noción de **campo conservativo**.

---

## Ejemplo

> [!ejemplo]
> **Verificación para $\vec A=(-y,\,x,\,0)$ en el disco de radio $R$ en el plano $z=0$.**
>
> **Rotor.** $\vec\nabla\times\vec A=\Big(\tfrac{\partial A_z}{\partial y}-\tfrac{\partial A_y}{\partial z}\Big)\hat e_x+\Big(\tfrac{\partial A_x}{\partial z}-\tfrac{\partial A_z}{\partial x}\Big)\hat e_y+\Big(\tfrac{\partial A_y}{\partial x}-\tfrac{\partial A_x}{\partial y}\Big)\hat e_z=(1-(-1))\hat e_z=2\,\hat e_z.$
>
> **Lado de la superficie.** Con $d\vec\sigma=\hat e_z\,d\sigma$,
> $$\int_S d\vec\sigma\cdot(\vec\nabla\times\vec A)=\int_S 2\,d\sigma=2\cdot\pi R^2=2\pi R^2.$$
>
> **Lado del contorno.** El borde es la circunferencia $\vec r=(R\cos\theta,\,R\operatorname{sen}\theta,\,0)$, con $d\vec r=(-R\operatorname{sen}\theta,\,R\cos\theta,\,0)\,d\theta$ y $\vec A=(-R\operatorname{sen}\theta,\,R\cos\theta,\,0)$. Entonces $\vec A\cdot d\vec r=R^2(\operatorname{sen}^2\theta+\cos^2\theta)\,d\theta=R^2\,d\theta$, y
> $$\oint_C d\vec r\cdot\vec A=\int_0^{2\pi}R^2\,d\theta=2\pi R^2.$$
>
> Ambos lados coinciden: $2\pi R^2=2\pi R^2$.

---

## Demostración

> [!info] Superficies adyacentes
> ![[stokes_superficies.svg|380]]
>
> Al sumar dos parches con borde común, las integrales de línea del borde interno se cancelan; queda solo el contorno exterior.

> [!teorema]
> $$\int_S d\vec\sigma\cdot(\vec\nabla\times\vec A)=\oint_C d\vec r\cdot\vec A.$$

> [!demostracion]
> **Paso 1 — Definición integral del rotor.** El rotor se define mediante la circulación sobre un contorno infinitesimal que rodea una superficie $d\vec\sigma$:
> $$(\vec\nabla\times\vec A)\cdot d\vec\sigma=\lim_{C\to0}\oint_C d\vec r\cdot\vec A,$$
> donde $C$ es el camino cerrado que encierra $d\vec\sigma$.
>
> **Paso 2 — Dos superficies adyacentes.** Aplicamos la relación a dos elementos de superficie contiguos $d\vec\sigma_1$ y $d\vec\sigma_2$ con un borde común. Sumando,
> $$(\vec\nabla\times\vec A)\cdot d\vec\sigma_1+(\vec\nabla\times\vec A)\cdot d\vec\sigma_2=\oint_{C_1}d\vec r\cdot\vec A+\oint_{C_2}d\vec r\cdot\vec A.$$
>
> **Paso 3 — Cancelación del borde común.** El segmento compartido por $C_1$ y $C_2$ se recorre en sentidos **opuestos** al rodear cada celda (orientación coherente con la mano derecha). Por tanto las dos integrales de línea sobre ese borde interno se anulan, y solo queda el contorno **exterior** $C_{1+2}$ que rodea a $d\vec\sigma_1+d\vec\sigma_2$:
> $$(\vec\nabla\times\vec A)\cdot d\vec\sigma_1+(\vec\nabla\times\vec A)\cdot d\vec\sigma_2=\oint_{C_{1+2}}d\vec r\cdot\vec A.$$
>
> **Paso 4 — Acumular superficies.** Repetimos sumando celdas hasta formar la superficie completa $S$. Todos los bordes **internos** se cancelan por parejas (cada uno recorrido dos veces en sentidos contrarios); solo persiste el contorno externo $C$ que bordea $S$. El resultado es
> $$\int_S d\vec\sigma\cdot(\vec\nabla\times\vec A)=\oint_C d\vec r\cdot\vec A.\qquad\blacksquare$$

---

## Consecuencia: campos conservativos

> [!corolario] Rotor nulo $\Rightarrow$ campo conservativo
> Si $\vec\nabla\times\vec A=0$ en todo el espacio, entonces $\vec A$ deriva de un **potencial escalar** $\Phi$ con $\vec A=-\vec\nabla\Phi$, y su integral de línea es **independiente del camino**.

> [!demostracion]
> **Paso 1 — Circulación nula.** Tomemos dos puntos $1$ y $2$ y dos caminos cualesquiera $A$ y $B$ entre ellos. El camino $A$ seguido del inverso de $B$ es un contorno cerrado $C$. Si $\vec\nabla\times\vec A=0$, Stokes da
> $$\oint_C d\vec r\cdot\vec A=\int_S d\vec\sigma\cdot(\vec\nabla\times\vec A)=0.$$
>
> **Paso 2 — Independencia del camino.** Esa circulación cerrada se descompone como
> $$\int_A d\vec r\cdot\vec A-\int_B d\vec r\cdot\vec A=0\quad\Longrightarrow\quad \int_A d\vec r\cdot\vec A=\int_B d\vec r\cdot\vec A.$$
> La integral entre $1$ y $2$ no depende del camino.
>
> **Paso 3 — Existencia del potencial.** Si la integral solo depende de los extremos, podemos definir una función de la posición $\Phi(\vec r)$ cuyo diferencial total sea
> $$d\Phi=-d\vec r\cdot\vec A.$$
> (El signo negativo es convencional: $\Phi$ crece al moverse contra las líneas de $\vec A$.) Integrando entre $1$ y $2$, $\int_1^2(-d\Phi)=\Phi(1)-\Phi(2)$, consistente con la independencia del camino.
>
> **Paso 4 — Gradiente.** Como $d\Phi=\vec\nabla\Phi\cdot d\vec r$ y a la vez $d\Phi=-\vec A\cdot d\vec r$ para todo $d\vec r$, se concluye
> $$\vec A=-\vec\nabla\Phi.\qquad\blacksquare$$

> [!info]
> Un campo con rotor cero se llama **conservativo**: su circulación a lo largo de cualquier curva cerrada es nula y siempre proviene de un potencial escalar. Es el caso del campo electrostático $\vec E=-\vec\nabla\Phi$.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Enunciado | $\int_S d\vec\sigma\cdot(\vec\nabla\times\vec A)=\oint_C d\vec r\cdot\vec A$ |
> | Conecta | superficie $S$ $\leftrightarrow$ contorno $C=\partial S$ |
> | Origen | definición integral del rotor |
> | Idea clave | los bordes internos se cancelan; sobrevive el contorno externo |
> | Consecuencia | $\vec\nabla\times\vec A=0\Rightarrow$ campo conservativo, $\vec A=-\vec\nabla\Phi$ |

> [!corolario]
> Stokes iguala la circulación de $\vec A$ por el borde con el flujo de su rotor por la superficie. De él se sigue que todo campo irrotacional es conservativo y deriva de un potencial escalar, pieza que el [[Teorema de Helmholtz]] usa en su descomposición.

> [!referencia]
> - Definición de origen: [[Operadores Diferenciales/Rotor]].
> - Análogo para la divergencia: [[Teorema de Gauss]].
> - Descomposición de campos: [[Teorema de Helmholtz]].
