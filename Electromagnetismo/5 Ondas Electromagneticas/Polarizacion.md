---
title: Polarización (ondas)
tags:
  - electromagnetismo
  - teoria
  - ondas
draft: false
aliases:
  - Polarización de la luz
  - Polarización electromagnética
  - Polarización lineal circular elíptica
---

# Polarización $\vec E=E_x\hat x+E_y\hat y$ (estado de $\vec E$)

> [!definicion]
> La **polarización** de una onda electromagnética describe la **dirección y la evolución temporal** del vector campo eléctrico $\vec E$ dentro del plano transversal a la dirección de propagación. Para una onda que viaja en $\hat z$, el campo vive en el plano $xy$, y el modo en que su extremo se mueve allí (recta, círculo o elipse) define el **estado de polarización**.

> [!info]
> Sección [[5 Ondas Electromagneticas/index | Ondas Electromagnéticas]]. Notas hermanas: [[Ondas Planas]], [[Ondas en Medios]]. Referencia: Griffiths, *Introduction to Electrodynamics*, cap. 9.

---

## Base del problema

Una onda plana monocromática que se propaga en la dirección $\hat z$ es **transversal**: su campo eléctrico no tiene componente a lo largo de $\hat z$, sino que oscila en el plano $xy$. Lo más general que podemos escribir es la superposición de dos oscilaciones ortogonales:

$$
\vec E(z,t)=E_x\,\hat x+E_y\,\hat y,
\qquad
\begin{cases}
E_x=E_{0x}\cos(kz-\omega t),\\[4pt]
E_y=E_{0y}\cos(kz-\omega t+\delta).
\end{cases}
$$

Aquí $E_{0x},E_{0y}\ge 0$ son las amplitudes de cada componente y $\delta$ es el **desfase** de $E_y$ respecto de $E_x$. Toda la información sobre la polarización está contenida en dos cantidades: la **razón de amplitudes** $E_{0y}/E_{0x}$ y el **desfase** $\delta$.

> [!teoria]
> La idea central es que, si nos paramos en un plano fijo (por ejemplo $z=0$) y dejamos correr el tiempo, el punto $(E_x,E_y)$ traza una curva en el plano transversal. La **forma de esa curva** —recta, círculo o elipse— es el estado de polarización, y solo depende de $\delta$ y de $E_{0y}/E_{0x}$.

Para simplificar la escritura, definimos la fase
$$
\varphi \equiv kz-\omega t,
$$
de modo que $E_x=E_{0x}\cos\varphi$ y $E_y=E_{0y}\cos(\varphi+\delta)$. Estudiar la polarización es **eliminar $\varphi$** entre ambas ecuaciones para obtener la curva $E_y=f(E_x)$ que describe el extremo del vector.

---

## Polarización lineal ($\delta=0$ o $\delta=\pi$)

> [!proposicion]
> Si el desfase es $\delta=0$ o $\delta=\pi$, el vector $\vec E$ oscila a lo largo de una **recta fija** que pasa por el origen. Se dice que la onda está **linealmente polarizada**.

> [!demostracion]
> **Paso 1 — Caso $\delta=0$.** Las componentes son
> $$
> E_x=E_{0x}\cos\varphi,\qquad E_y=E_{0y}\cos\varphi.
> $$
> Ambas comparten exactamente la misma fase $\varphi$, así que su cociente no depende del tiempo:
> $$
> \frac{E_y}{E_x}=\frac{E_{0y}\cos\varphi}{E_{0x}\cos\varphi}=\frac{E_{0y}}{E_{0x}}=\text{constante}.
> $$
> **Paso 2 — Interpretación.** Una razón $E_y/E_x$ constante es la ecuación de una **recta** $E_y=\dfrac{E_{0y}}{E_{0x}}\,E_x$ que pasa por el origen, con pendiente fija. El vector $\vec E$ crece y decrece en magnitud (oscila), pero **nunca cambia de dirección**: apunta siempre a lo largo de esa recta, formando un ángulo
> $$
> \theta=\arctan\!\left(\frac{E_{0y}}{E_{0x}}\right)
> $$
> con el eje $x$.
>
> **Paso 3 — Caso $\delta=\pi$.** Ahora $E_y=E_{0y}\cos(\varphi+\pi)=-E_{0y}\cos\varphi$, de modo que
> $$
> \frac{E_y}{E_x}=-\frac{E_{0y}}{E_{0x}}=\text{constante}.
> $$
> De nuevo es una recta, pero con pendiente **negativa**: el vector oscila a lo largo de la dirección $\theta=-\arctan(E_{0y}/E_{0x})$.
>
> En ambos casos la traza es un segmento de recta, luego la polarización es lineal. $\blacksquare$

Podemos escribir el campo lineal de forma compacta como
$$
\vec E=E_0\cos(kz-\omega t)\,\hat n,
\qquad
\hat n=\cos\theta\,\hat x+\sin\theta\,\hat y,
$$
donde $\hat n$ es el **vector de polarización** (unitario, fijo) y $E_0=\sqrt{E_{0x}^2+E_{0y}^2}$.

---

## Polarización circular ($\delta=\pm\pi/2$, $E_{0x}=E_{0y}=E_0$)

> [!proposicion]
> Si las dos componentes tienen **igual amplitud** $E_{0x}=E_{0y}=E_0$ y están en **cuadratura** ($\delta=\pm\pi/2$), el extremo de $\vec E$ describe un **círculo** de radio $E_0$. La onda está **circularmente polarizada**.

> [!demostracion]
> **Paso 1 — Escribir las componentes.** Tomemos $\delta=-\pi/2$. Usando $\cos(\varphi-\pi/2)=\sin\varphi$,
> $$
> E_x=E_0\cos\varphi,\qquad
> E_y=E_0\cos\!\left(\varphi-\tfrac{\pi}{2}\right)=E_0\sin\varphi.
> $$
> **Paso 2 — Eliminar la fase.** Sumamos los cuadrados y aplicamos la identidad pitagórica $\cos^2\varphi+\sin^2\varphi=1$:
> $$
> E_x^2+E_y^2=E_0^2\cos^2\varphi+E_0^2\sin^2\varphi=E_0^2\bigl(\cos^2\varphi+\sin^2\varphi\bigr)=E_0^2.
> $$
> **Paso 3 — Interpretación.** La relación $E_x^2+E_y^2=E_0^2$ es la ecuación de una **circunferencia** de radio $E_0$ centrada en el origen. El módulo $|\vec E|=E_0$ es constante: el vector **no cambia de longitud**, solo **gira**. En efecto, su ángulo instantáneo es
> $$
> \psi(t)=\arctan\!\frac{E_y}{E_x}=\arctan\!\frac{\sin\varphi}{\cos\varphi}=\varphi=kz-\omega t,
> $$
> que decrece linealmente con el tiempo: el vector rota uniformemente con velocidad angular $\omega$. $\blacksquare$

> [!regla] Sentido de giro
> El signo de $\delta$ fija la dirección de rotación (visto el observador mirando **hacia la fuente**, es decir, con la onda viniendo hacia él, $-\hat z$):
>
> - $\delta=-\pi/2$ ($E_y=E_0\sin\varphi$): el ángulo $\psi=kz-\omega t$ **decrece**, el vector gira en sentido horario $\Rightarrow$ polarización **dextrógira** (right-circular).
> - $\delta=+\pi/2$ ($E_y=-E_0\sin\varphi$): el ángulo $\psi$ **crece**, el vector gira en sentido antihorario $\Rightarrow$ polarización **levógira** (left-circular).
>
> El criterio de "horario/antihorario" depende del convenio de observación (óptica vs. física), por lo que conviene siempre indicar respecto de qué eje se mira.

---

## Polarización elíptica (caso general)

> [!teorema]
> Para amplitudes y desfase arbitrarios $(E_{0x},E_{0y},\delta)$, el extremo del vector $\vec E$ recorre una **elipse** inscrita en el rectángulo $[-E_{0x},E_{0x}]\times[-E_{0y},E_{0y}]$, cuya ecuación es
> $$
> \left(\frac{E_x}{E_{0x}}\right)^{2}
> +\left(\frac{E_y}{E_{0y}}\right)^{2}
> -2\,\frac{E_x E_y}{E_{0x}E_{0y}}\cos\delta
> =\sin^{2}\delta.
> $$

> [!demostracion]
> **Paso 1 — Partir de las componentes.** Con $\varphi=kz-\omega t$,
> $$
> \frac{E_x}{E_{0x}}=\cos\varphi,
> \qquad
> \frac{E_y}{E_{0y}}=\cos(\varphi+\delta).
> $$
> **Paso 2 — Desarrollar el coseno de la suma.**
> $$
> \frac{E_y}{E_{0y}}=\cos\varphi\cos\delta-\sin\varphi\sin\delta.
> $$
> Sustituyendo $\cos\varphi=E_x/E_{0x}$ y despejando el término con seno:
> $$
> \frac{E_y}{E_{0y}}-\frac{E_x}{E_{0x}}\cos\delta=-\sin\varphi\sin\delta.
> $$
> **Paso 3 — Eliminar la fase.** Necesitamos también $\sin\varphi$. De $\cos\varphi=E_x/E_{0x}$ no usamos su valor directo, sino que **elevamos al cuadrado** la ecuación anterior:
> $$
> \left(\frac{E_y}{E_{0y}}-\frac{E_x}{E_{0x}}\cos\delta\right)^{2}=\sin^{2}\varphi\,\sin^{2}\delta.
> $$
> Por otra parte, $\sin^2\varphi=1-\cos^2\varphi=1-\left(\dfrac{E_x}{E_{0x}}\right)^{2}$. Entonces
> $$
> \left(\frac{E_y}{E_{0y}}-\frac{E_x}{E_{0x}}\cos\delta\right)^{2}
> =\left[1-\left(\frac{E_x}{E_{0x}}\right)^{2}\right]\sin^{2}\delta.
> $$
> **Paso 4 — Expandir el cuadrado del lado izquierdo.**
> $$
> \left(\frac{E_y}{E_{0y}}\right)^{2}
> -2\,\frac{E_x E_y}{E_{0x}E_{0y}}\cos\delta
> +\left(\frac{E_x}{E_{0x}}\right)^{2}\cos^{2}\delta
> =\sin^{2}\delta-\left(\frac{E_x}{E_{0x}}\right)^{2}\sin^{2}\delta.
> $$
> **Paso 5 — Reagrupar el término en $(E_x/E_{0x})^2$.** Pasamos $-\left(\frac{E_x}{E_{0x}}\right)^{2}\sin^{2}\delta$ al lado izquierdo:
> $$
> \left(\frac{E_x}{E_{0x}}\right)^{2}\underbrace{\bigl(\cos^{2}\delta+\sin^{2}\delta\bigr)}_{=\,1}
> +\left(\frac{E_y}{E_{0y}}\right)^{2}
> -2\,\frac{E_x E_y}{E_{0x}E_{0y}}\cos\delta
> =\sin^{2}\delta.
> $$
> **Paso 6 — Resultado.** Como $\cos^2\delta+\sin^2\delta=1$, queda exactamente
> $$
> \left(\frac{E_x}{E_{0x}}\right)^{2}
> +\left(\frac{E_y}{E_{0y}}\right)^{2}
> -2\,\frac{E_x E_y}{E_{0x}E_{0y}}\cos\delta
> =\sin^{2}\delta,
> $$
> que es la ecuación de una **cónica** en $(E_x,E_y)$. Su discriminante es
> $$
> B^2-4AC=\left(\frac{-2\cos\delta}{E_{0x}E_{0y}}\right)^{2}-4\,\frac{1}{E_{0x}^2}\,\frac{1}{E_{0y}^2}
> =\frac{4(\cos^2\delta-1)}{E_{0x}^2E_{0y}^2}=-\frac{4\sin^2\delta}{E_{0x}^2E_{0y}^2}\le 0,
> $$
> y al ser $\le 0$ la cónica es una **elipse** (degenera en recta solo si $\sin\delta=0$). $\blacksquare$

> [!corolario]
> Los estados lineal y circular son **casos particulares** de la elipse:
>
> - $\delta=0,\pi$ $\Rightarrow$ $\sin\delta=0$: la elipse degenera en un **segmento de recta** (lineal).
> - $\delta=\pm\pi/2$ y $E_{0x}=E_{0y}$ $\Rightarrow$ los ejes coinciden y la ecuación se reduce a $E_x^2+E_y^2=E_{0}^2$ (**círculo**).
>
> En general, los ejes de la elipse están girados respecto de $\hat x,\hat y$ un ángulo que depende de $\delta$ y de la razón de amplitudes.

![[polarizacion_tipos.svg|640]]
*La traza del extremo del vector $\vec E$ en el plano transversal $xy$: a la izquierda la polarización lineal (segmento), al centro la circular (círculo) y a la derecha la elíptica (elipse). El sentido de la flecha indica el giro dextrógiro o levógiro.*

---

## Descomposición y polarizadores

> [!teoria] Dos bases naturales
> Cualquier estado de polarización admite **dos descomposiciones equivalentes**:
>
> 1. **Base lineal.** Toda onda es superposición de dos linealmente polarizadas ortogonales ($\hat x$ y $\hat y$) con su desfase relativo $\delta$; es justamente la forma con la que partimos.
> 2. **Base circular.** También puede escribirse como suma de una onda **dextrógira** y una **levógira**. Definiendo los vectores complejos $\hat e_\pm=\tfrac{1}{\sqrt2}(\hat x\pm i\,\hat y)$, una polarización lineal es la suma a partes iguales de ambas circulares, y una elíptica es una combinación con pesos distintos.
>
> Que existan dos bases refleja que el estado de polarización vive en un espacio de **dos dimensiones** (dos amplitudes y una fase relativa, salvo la fase global).

> [!proposicion] Ley de Malus
> Un **polarizador** lineal ideal solo deja pasar la componente de $\vec E$ paralela a su eje de transmisión. Si luz linealmente polarizada de intensidad $I_0$ incide formando un ángulo $\theta$ con el eje, la intensidad transmitida es
> $$
> I=I_0\cos^{2}\theta.
> $$

> [!demostracion]
> **Paso 1 — Proyección del campo.** El polarizador transmite la proyección $E_\parallel=E_0\cos\theta$ del campo incidente sobre su eje.
> **Paso 2 — De campo a intensidad.** La intensidad es proporcional al cuadrado del campo, $I\propto E^2$. Por tanto
> $$
> I=I_0\left(\frac{E_\parallel}{E_0}\right)^{2}=I_0\cos^{2}\theta.
> $$
> $\blacksquare$

> [!info] Parámetros de Stokes
> Una descripción **completa** del estado de polarización (incluida la luz parcialmente polarizada o no polarizada, que los campos $\vec E$ idealizados no capturan) se da con los cuatro **parámetros de Stokes** $(S_0,S_1,S_2,S_3)$: $S_0$ es la intensidad total, $S_1$ mide el exceso de polarización horizontal sobre vertical, $S_2$ el de $+45^\circ$ sobre $-45^\circ$, y $S_3$ el de circular dextrógira sobre levógira. Cumplen $S_0^2\ge S_1^2+S_2^2+S_3^2$ (igualdad para luz totalmente polarizada) y se representan geométricamente sobre la **esfera de Poincaré**.

---

## Ejemplo

> [!ejemplo]
> Una onda que viaja en $\hat z$ tiene componentes
> $$
> E_x=E_0\cos(kz-\omega t),\qquad
> E_y=2E_0\cos\!\left(kz-\omega t+\frac{\pi}{2}\right).
> $$
> Identifica el tipo de polarización y el sentido de giro.

> [!solucion]
> **Paso 1 — Leer los datos.** Las amplitudes son $E_{0x}=E_0$ y $E_{0y}=2E_0$, **distintas**; el desfase es $\delta=+\pi/2$.
>
> **Paso 2 — Descartar lineal y circular.** Como $\delta=\pi/2\neq 0,\pi$, no es lineal. Como las amplitudes son distintas ($E_{0x}\neq E_{0y}$), tampoco es circular. Debe ser **elíptica**.
>
> **Paso 3 — Hallar la elipse.** Sustituimos en la ecuación general con $\cos\delta=\cos(\pi/2)=0$ y $\sin^2\delta=1$:
> $$
> \left(\frac{E_x}{E_0}\right)^{2}+\left(\frac{E_y}{2E_0}\right)^{2}-0=1.
> $$
> Es una elipse **con ejes alineados a $\hat x,\hat y$** (no hay término cruzado porque $\cos\delta=0$), de semieje $E_0$ en $x$ y semieje $2E_0$ en $y$. Está, pues, "estirada" en la dirección vertical.
>
> **Paso 4 — Sentido de giro.** Con $\delta=+\pi/2$ usamos $\cos(\varphi+\pi/2)=-\sin\varphi$, de modo que
> $$
> E_x=E_0\cos\varphi,\qquad E_y=-2E_0\sin\varphi,\qquad \varphi=kz-\omega t.
> $$
> En $z=0$ y $t=0$: $\vec E=(E_0,0)$, sobre el eje $+x$. Un instante después ($t>0$, $\varphi<0$): $\cos\varphi$ apenas cambia y $-\sin\varphi=-\sin(\text{negativo})>0$, así que $E_y$ se hace **positivo**. El vector pasa de $+x$ hacia $+y$: gira en sentido **antihorario** $\Rightarrow$ polarización **elíptica levógira**.
>
> **Conclusión.** Onda **elípticamente polarizada**, elipse de semiejes $(E_0,\,2E_0)$ alineada con los ejes coordenados, girando en sentido **levógiro**. $\blacksquare$

---

## En qué consiste

La polarización es la respuesta a una pregunta sencilla: **¿en qué dirección apunta el campo eléctrico de la onda, y cómo cambia esa dirección con el tiempo?** Como la onda es transversal, $\vec E$ está confinado a un plano (el perpendicular a la propagación), y allí su extremo dibuja una figura.

- Si las dos componentes ortogonales del campo **suben y bajan al unísono** (en fase o en contrafase), el vector se queda sobre una recta: **lineal**.
- Si están **desfasadas un cuarto de período** y tienen igual amplitud, el vector mantiene su longitud y solo **rota**: **circular**.
- En cualquier otro caso, combina rotación y cambio de longitud, y traza una **elipse**: el caso genérico, del que lineal y circular son los extremos.

Toda la riqueza del fenómeno cabe en dos números: la **razón de amplitudes** y el **desfase**. Con ellos se construyen filtros (polarizadores), se analiza la luz reflejada, se diseñan pantallas LCD y gafas 3D, y se mide la estructura de campos astrofísicos.

> [!warning] No confundir con la polarización dieléctrica
> Esta polarización —la **orientación del vector $\vec E$ en una onda**— **no** tiene nada que ver con la **polarización dieléctrica** $\vec P$ de la materia (capítulo 2 de [[index | Electromagnetismo]]), que es el momento dipolar por unidad de volumen inducido en un medio. Comparten nombre por accidente histórico, pero son conceptos físicos distintos: uno describe la geometría de una onda en el vacío; el otro, la respuesta eléctrica de un material. No mezcles $\vec E$ (campo) con $\vec P$ (densidad de dipolos).

---

## Resumen

| Tipo | Condición sobre $\delta$ y amplitudes | Traza de $\vec E$ | $\lvert\vec E\rvert$ |
| --- | --- | --- | --- |
| Lineal | $\delta=0$ o $\delta=\pi$ | Segmento de recta | Oscila |
| Circular | $\delta=\pm\pi/2$ y $E_{0x}=E_{0y}$ | Círculo de radio $E_0$ | Constante |
| Elíptica | Caso general | Elipse | Varía periódicamente |

> [!corolario]
> El estado de polarización queda fijado por **dos parámetros**: la razón de amplitudes $E_{0y}/E_{0x}$ y el desfase $\delta$. La ecuación maestra
> $$
> \left(\frac{E_x}{E_{0x}}\right)^{2}+\left(\frac{E_y}{E_{0y}}\right)^{2}-2\,\frac{E_xE_y}{E_{0x}E_{0y}}\cos\delta=\sin^{2}\delta
> $$
> contiene los tres casos: degenera en recta cuando $\sin\delta=0$ (lineal), en círculo cuando $\cos\delta=0$ con $E_{0x}=E_{0y}$ (circular), y es una elipse genérica en lo demás. Un polarizador filtra estados según la **ley de Malus** $I=I_0\cos^2\theta$, y la descripción completa (incluida luz parcial) se da con los **parámetros de Stokes**.

> [!referencia]
> - Griffiths, *Introduction to Electrodynamics*, 4.ª ed., cap. 9 (ondas electromagnéticas y polarización).
> - Jackson, *Classical Electrodynamics*, cap. 7 (polarización, parámetros de Stokes, esfera de Poincaré).
> - Hecht, *Optics*, cap. 8 (polarización óptica, ley de Malus).
> - Notas hermanas: [[Ondas Planas]], [[Ondas en Medios]]. Índice: [[5 Ondas Electromagneticas/index | Ondas Electromagnéticas]].
