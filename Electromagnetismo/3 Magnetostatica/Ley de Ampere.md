---
title: Ley de Ampère
tags:
  - electromagnetismo
  - teoria
  - magnetostatica
draft: false
aliases:
  - Ley de Ampère
  - Teorema de Ampère
---

# Ley de Ampère $\oint_C\vec B\cdot d\vec l=\mu_0 I_{\text{enc}}$

> [!definicion]
> La **ley de Ampère** afirma que la **circulación** del campo magnético $\vec B$ a lo largo de una curva cerrada $C$ es proporcional a la **corriente neta** que atraviesa cualquier superficie $S$ apoyada en esa curva. En sus dos formas equivalentes:
> $$\boxed{\ \oint_C\vec B\cdot d\vec l=\mu_0\,I_{\text{enc}}\ }\qquad\text{(forma integral)},$$
> $$\boxed{\ \nabla\times\vec B=\mu_0\,\vec J\ }\qquad\text{(forma diferencial)}.$$
> Aquí $\mu_0$ es la permeabilidad del vacío, $I_{\text{enc}}=\displaystyle\int_S\vec J\cdot d\vec A$ es la corriente encerrada por $C$, y la orientación de $d\vec l$ (sentido de recorrido) fija la de $d\vec A$ por la **regla de la mano derecha**. La curva $C$ se llama **lazo amperiano**.

---

> [!info]
> **Sección [[3 Magnetostatica/index | Magnetostática]]** (capítulo 3 del curso). Es la ley de **fuente** del campo magnético: el análogo de la ley de Gauss para $\vec B$, pero para la *circulación* en lugar del *flujo*. Notas hermanas: [[Ley de Biot-Savart]] (de donde se deduce el campo del hilo que aquí verificamos) y [[Potencial Vector]]. La equivalencia entre ambas formas usa el **teorema de Stokes** ([[Teoremas Integrales]]).
> **Referencia.** Griffiths, *Introduction to Electrodynamics*, cap. 5.

---

## Equivalencia de las dos formas

> [!teorema] Integral $\Leftrightarrow$ diferencial (vía Stokes)
> Las dos formas de la ley de Ampère son **equivalentes**: una se obtiene de la otra aplicando el teorema de Stokes a una superficie arbitraria $S$ con borde $C=\partial S$.

> [!demostracion]
> Partimos de la forma diferencial $\nabla\times\vec B=\mu_0\vec J$.
>
> **Paso 1 — Integramos sobre una superficie.** Tomamos una superficie $S$ cualquiera cuyo borde sea la curva cerrada $C$ y proyectamos la ecuación diferencial sobre el elemento de área $d\vec A$:
> $$\int_S(\nabla\times\vec B)\cdot d\vec A=\mu_0\int_S\vec J\cdot d\vec A.$$
>
> **Paso 2 — Stokes en el miembro izquierdo.** El [[Teoremas Integrales | teorema de Stokes]] convierte el flujo del rotacional en la circulación a lo largo del borde:
> $$\int_S(\nabla\times\vec B)\cdot d\vec A=\oint_{C}\vec B\cdot d\vec l.$$
>
> **Paso 3 — Identificamos la corriente encerrada.** Por definición de densidad de corriente, el flujo de $\vec J$ a través de $S$ es la corriente que atraviesa $C$:
> $$\int_S\vec J\cdot d\vec A=I_{\text{enc}}.$$
>
> **Paso 4 — Encadenamos.** Sustituyendo los pasos 2 y 3 en el paso 1:
> $$\oint_{C}\vec B\cdot d\vec l=\int_S(\nabla\times\vec B)\cdot d\vec A=\mu_0\int_S\vec J\cdot d\vec A=\mu_0\,I_{\text{enc}}.$$
>
> El resultado **no depende de la superficie $S$ elegida** (solo de su borde $C$), porque $\nabla\cdot\vec J=0$ en magnetostática: dos superficies con el mismo borde encierran la misma corriente. El recíproco (integral $\Rightarrow$ diferencial) se obtiene encogiendo $C$ a un punto y leyendo el rotacional como circulación por unidad de área. $\blacksquare$

---

> [!proposicion] Verificación con el hilo infinito
> La ley integral es consistente con el campo de un hilo recto infinito que transporta corriente $I$, cuyo módulo (de [[Ley de Biot-Savart]]) es $B=\dfrac{\mu_0 I}{2\pi s}$ a distancia $s$ del hilo, con $\vec B$ azimutal (en círculos alrededor del hilo).

> [!demostracion]
> **Paso 1 — Elegimos el lazo.** Tomamos como curva $C$ un **círculo** de radio $s$ centrado en el hilo y contenido en el plano perpendicular a él. Por la simetría cilíndrica del problema, $\vec B$ tiene la misma magnitud en todo el círculo y es **tangente** a él (paralelo a $d\vec l$), de modo que $\vec B\cdot d\vec l=B\,dl$.
>
> **Paso 2 — Calculamos la circulación.** Como $B$ es constante sobre el círculo, sale de la integral:
> $$\oint_C\vec B\cdot d\vec l=\oint_C B\,dl=B\oint_C dl=B\,(2\pi s).$$
>
> **Paso 3 — Sustituimos el campo del hilo.** Con $B=\dfrac{\mu_0 I}{2\pi s}$:
> $$\oint_C\vec B\cdot d\vec l=\frac{\mu_0 I}{2\pi s}\,(2\pi s)=\mu_0 I.$$
>
> El radio $s$ **se cancela**: la circulación vale $\mu_0 I$ sea cual sea el tamaño del círculo, exactamente la ley de Ampère con $I_{\text{enc}}=I$. Más aún, puede probarse que el resultado vale para **cualquier lazo cerrado** que rodee el hilo (no solo círculos): lo que cuenta es que encierre la corriente, no su forma. $\blacksquare$

---

![[ampere_simetrias.svg|640]]
*Los tres lazos amperianos clásicos. **(a) Hilo infinito**: lazo circular concéntrico; $\vec B$ es azimutal y constante sobre el círculo. **(b) Solenoide infinito**: lazo rectangular con un lado dentro (paralelo al eje) y otro fuera; solo contribuye el lado interior. **(c) Toroide**: lazo circular interior de radio $r$; $\vec B$ rodea el núcleo y es nulo fuera del bobinado.*

---

## Cálculos por simetría

> [!regla] Cuándo sirve Ampère
> La ley de Ampère permite **despejar** $\vec B$ de la circulación solo cuando la simetría garantiza que, sobre el lazo bien elegido, $\vec B$ es **constante en magnitud** y **tangente** (o nulo) al lazo. Entonces $\oint\vec B\cdot d\vec l=B\,L$ con $L$ la longitud del tramo donde $\vec B\neq 0$, y se despeja $B$. Las tres situaciones canónicas son: hilo, solenoide y toroide.

> [!teorema] Hilo recto infinito
> A distancia $s$ de un hilo infinito con corriente $I$:
> $$B=\frac{\mu_0 I}{2\pi s},\qquad \vec B\ \text{azimutal.}$$

> [!demostracion]
> **Paso 1 — Simetría y lazo.** La simetría cilíndrica obliga a que $\vec B$ dependa solo de $s$ y sea azimutal. Elegimos un círculo amperiano de radio $s$ perpendicular al hilo.
>
> **Paso 2 — Circulación.** Como en la verificación anterior, $\displaystyle\oint_C\vec B\cdot d\vec l=B\,(2\pi s)$.
>
> **Paso 3 — Corriente encerrada y despeje.** El círculo encierra todo el hilo, $I_{\text{enc}}=I$, luego $B\,(2\pi s)=\mu_0 I$ y por tanto
> $$B=\frac{\mu_0 I}{2\pi s}.\qquad\blacksquare$$

> [!teorema] Solenoide infinito
> Para un solenoide infinito con $n$ vueltas por unidad de longitud y corriente $I$:
> $$B=\mu_0\,n\,I\ \text{ (dentro, paralelo al eje)},\qquad B=0\ \text{ (fuera)}.$$

La deducción completa se hace en el **ejemplo resuelto** de más abajo.

> [!teorema] Toroide
> Para un toroide con $N$ vueltas totales y corriente $I$, a distancia $r$ del eje de simetría:
> $$B=\frac{\mu_0\,N\,I}{2\pi r}\ \text{ (dentro del bobinado)},\qquad B=0\ \text{ (fuera)}.$$

> [!demostracion]
> **Paso 1 — Simetría.** Por la simetría de revolución, $\vec B$ es **azimutal** (circula a lo largo del núcleo) y su módulo depende solo de $r$, la distancia al eje del toroide.
>
> **Paso 2 — Lazo interior.** Tomamos un círculo amperiano de radio $r$ **dentro** del bobinado, coaxial con el eje. Allí $\vec B$ es tangente y constante:
> $$\oint_C\vec B\cdot d\vec l=B\,(2\pi r).$$
>
> **Paso 3 — Corriente encerrada.** El círculo atraviesa las $N$ espiras, cada una con corriente $I$, todas en el mismo sentido: $I_{\text{enc}}=N\,I$. Entonces
> $$B\,(2\pi r)=\mu_0\,N\,I\ \Rightarrow\ B=\frac{\mu_0\,N\,I}{2\pi r}.$$
>
> **Paso 4 — Exterior nulo.** Un lazo de radio mayor que el toroide encierra $N$ espiras de ida y $N$ de vuelta (la corriente entra y sale): $I_{\text{enc}}=0$, luego $B=0$ fuera. Un lazo en el "agujero" central no encierra corriente alguna, así que también allí $B=0$. $\blacksquare$

---

## Ejemplo

> [!ejemplo] Campo dentro de un solenoide infinito
> Un solenoide muy largo (idealmente infinito) tiene $n$ vueltas por unidad de longitud, cada una con corriente $I$. Calcular el campo $\vec B$ en su interior usando la ley de Ampère.

> [!solucion]
> **Paso 1 — Simetría del campo.** Por la simetría de traslación a lo largo del eje y de rotación, en un solenoide infinito el campo solo puede ser **paralelo al eje** ($\hat z$) dentro, y su magnitud depende a lo sumo de la distancia al eje. Un argumento de simetría adicional (sumar las contribuciones de espiras simétricas) cancela toda componente radial y azimutal: $\vec B=B(s)\,\hat z$.
>
> **Paso 2 — El campo exterior es nulo.** Lejos, un solenoide infinito no produce campo: tomando dos lazos rectangulares exteriores a distintas distancias se prueba que $B$ fuera es uniforme, y como debe anularse en el infinito, $B_{\text{fuera}}=0$.
>
> **Paso 3 — Lazo amperiano rectangular.** Elegimos un rectángulo $C$ con un lado de longitud $L$ **dentro** del solenoide (paralelo al eje) y el lado opuesto **fuera**, unidos por dos lados perpendiculares al eje (ver figura, caso b). Recorremos $C$ en sentido antihorario visto según $\hat z$.
>
> **Paso 4 — Descomponemos la circulación.** La integral se parte en los cuatro lados:
> $$\oint_C\vec B\cdot d\vec l=\underbrace{\int_{\text{dentro}}\!\!\vec B\cdot d\vec l}_{=\,B\,L}+\underbrace{\int_{\text{fuera}}\!\!\vec B\cdot d\vec l}_{=\,0\ (B_{\text{fuera}}=0)}+\underbrace{\int_{\perp}\!\!\vec B\cdot d\vec l}_{=\,0\ (\vec B\,\perp\,d\vec l)}.$$
> Los dos lados perpendiculares al eje no contribuyen porque allí $\vec B\parallel\hat z$ es **perpendicular** a $d\vec l$; el lado exterior no contribuye porque $B_{\text{fuera}}=0$. Queda solo el lado interior:
> $$\oint_C\vec B\cdot d\vec l=B\,L.$$
>
> **Paso 5 — Corriente encerrada.** El rectángulo atraviesa todas las espiras contenidas en la longitud $L$. Como hay $n$ vueltas por unidad de longitud y cada una lleva $I$:
> $$I_{\text{enc}}=n\,L\,I.$$
>
> **Paso 6 — Aplicamos Ampère y despejamos.** Igualando circulación y corriente:
> $$B\,L=\mu_0\,(n\,L\,I)\ \Rightarrow\ B=\mu_0\,n\,I.$$
> El resultado es **uniforme** (no depende de $s$): el campo dentro de un solenoide infinito vale $\vec B=\mu_0 n I\,\hat z$, y es nulo fuera. $\blacksquare$

---

> [!warning] Límites de validez
> - **Solo en magnetostática.** La ley de Ampère en la forma $\nabla\times\vec B=\mu_0\vec J$ exige $\nabla\cdot\vec J=0$ (corrientes estacionarias). Tomando la divergencia se ve que $0=\nabla\cdot(\nabla\times\vec B)=\mu_0\,\nabla\cdot\vec J$, lo que **falla** cuando hay cargas que se acumulan o varían en el tiempo (p. ej. al cargar un condensador). En ese caso hay que añadir la **corriente de desplazamiento** $\varepsilon_0\,\partial_t\vec E$, dando $\nabla\times\vec B=\mu_0\vec J+\mu_0\varepsilon_0\,\partial_t\vec E$. Eso ya es [[4 Electrodinamica/index | Electrodinámica]].
> - **Solo es práctica con simetría.** Ampère siempre es **verdadera**, pero solo permite **calcular** $\vec B$ cuando la simetría (cilíndrica, traslacional o toroidal) deja sacar $B$ de la integral. Sin simetría suficiente hay que recurrir a [[Ley de Biot-Savart]] o al [[Potencial Vector]].

---

## Resumen

> [!resumen]
>
> | Configuración | Lazo amperiano | $I_{\text{enc}}$ | Campo $\vec B$ |
> |:---|:---|:---|:---|
> | Hilo infinito | círculo de radio $s$ | $I$ | $B=\dfrac{\mu_0 I}{2\pi s}$, azimutal |
> | Solenoide infinito | rectángulo (un lado dentro) | $n L I$ | $B=\mu_0 n I$ dentro; $0$ fuera |
> | Toroide | círculo de radio $r$ | $N I$ | $B=\dfrac{\mu_0 N I}{2\pi r}$ dentro; $0$ fuera |
> | General | — | $\displaystyle\int_S\vec J\cdot d\vec A$ | $\oint_C\vec B\cdot d\vec l=\mu_0 I_{\text{enc}}$ |

> [!corolario]
> La ley de Ampère es la **ley de fuente** del magnetismo: la corriente es lo que hace circular a $\vec B$, igual que la carga hace divergir a $\vec E$. Sus dos formas — $\oint_C\vec B\cdot d\vec l=\mu_0 I_{\text{enc}}$ y $\nabla\times\vec B=\mu_0\vec J$— son equivalentes vía Stokes, y juntas con $\nabla\cdot\vec B=0$ cierran la magnetostática. Al permitir campos variables en el tiempo, la corriente de desplazamiento la convierte en la cuarta ecuación de Maxwell.

> [!referencia]
> Griffiths, *Introduction to Electrodynamics*, cap. 5 ("Magnetostatics"), §5.3 ("The Divergence and Curl of $\vec B$"). Profundización: Jackson, cap. 5.
