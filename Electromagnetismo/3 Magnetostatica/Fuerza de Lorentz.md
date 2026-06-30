---
title: Fuerza de Lorentz
order: 1
tags:
  - electromagnetismo
  - teoria
  - magnetostatica
draft: false
aliases:
  - Fuerza de Lorentz
  - Fuerza magnética
---

# Fuerza de Lorentz $\vec F=q(\vec E+\vec v\times\vec B)$

> [!definicion]
> La **fuerza de Lorentz** es la fuerza total que un campo electromagnético ejerce sobre una carga puntual $q$ que se mueve con velocidad $\vec v$:
> $$\vec F=q\big(\vec E+\vec v\times\vec B\big).$$
> Tiene dos contribuciones: la **eléctrica** $q\vec E$, paralela al campo $\vec E$ e independiente del movimiento; y la **magnética** $q\,\vec v\times\vec B$, que depende de la velocidad y es siempre **perpendicular** a $\vec v$ (y a $\vec B$). Esta última es el motor de toda la magnetostática: es la única manera en que el campo $\vec B$ se deja "sentir".

---

> [!info]
> **Nota 1 del capítulo [[3 Magnetostatica/index | Magnetostática]].** Es la **ley de fuerza** del campo magnético, análoga a $\vec F=q\vec E$ de la electrostática. Sus hermanas son [[Ley de Biot-Savart]] (cómo las corrientes *crean* $\vec B$) y [[Ley de Ampere]] (la ley de fuente integral). Aquí estudiamos cómo $\vec B$ *actúa* sobre cargas y corrientes. **Referencia.** Griffiths, *Introduction to Electrodynamics*, cap. 5 ("Magnetostatics"), §5.1.

---

## El campo magnético no realiza trabajo

> [!teorema] La fuerza magnética no hace trabajo
> Sobre una carga puntual, la fuerza magnética $\vec F_{\text{mag}}=q\,\vec v\times\vec B$ **no realiza trabajo**: la energía cinética de la carga se conserva, y $\vec B$ solo puede **cambiar la dirección** de $\vec v$, nunca su rapidez $|\vec v|$.

> [!demostracion]
> **Paso 1 — Trabajo elemental.** El trabajo que una fuerza $\vec F$ hace sobre la carga al desplazarse $d\vec l=\vec v\,dt$ es, por definición,
> $$dW=\vec F\cdot d\vec l=\vec F\cdot\vec v\,dt.$$
>
> **Paso 2 — Sustituir la fuerza magnética.** Para la parte magnética $\vec F=q\,\vec v\times\vec B$:
> $$dW=q\,(\vec v\times\vec B)\cdot\vec v\,dt.$$
>
> **Paso 3 — El triple producto se anula.** El vector $\vec v\times\vec B$ es **perpendicular** a $\vec v$ por la definición misma del producto cruz, de modo que su proyección sobre $\vec v$ es nula:
> $$(\vec v\times\vec B)\cdot\vec v=0.$$
> (Equivalentemente, el producto mixto $\vec v\cdot(\vec v\times\vec B)$ tiene dos factores repetidos, y por tanto se anula.) Luego
> $$dW=0.$$
>
> **Paso 4 — Consecuencia energética.** Por el teorema trabajo–energía, $dW=d\big(\tfrac12 m v^2\big)$. Como $dW=0$ en todo instante, la energía cinética —y con ella la rapidez $|\vec v|$— permanece constante. La fuerza magnética **curva** la trayectoria sin acelerar ni frenar la carga. $\blacksquare$

> [!warning]
> Que la fuerza magnética sobre una **carga aislada** no trabaje **no significa** que el magnetismo sea energéticamente inerte en un circuito. En un motor, por ejemplo, sí hay transferencia de energía: pero el trabajo lo realiza la **fuente** (la fem que mantiene la corriente contra la fuerza electromotriz inducida), **no** el campo $\vec B$. El campo magnético solo redistribuye y reorienta; la cuenta energética la paga siempre la fuente.

---

## Movimiento ciclotrónico

> [!proposicion] Carga en un campo magnético uniforme
> Una carga $q$ que entra con velocidad $\vec v$ **perpendicular** a un campo $\vec B$ uniforme describe una **circunferencia** de radio
> $$r=\frac{m v}{q B}\qquad\text{(radio de ciclotrón)},$$
> recorrida con **frecuencia angular**
> $$\omega=\frac{q B}{m}\qquad\text{(frecuencia de ciclotrón)},$$
> que es **independiente de la rapidez** $v$.

> [!demostracion]
> **Paso 1 — La fuerza es centrípeta.** Como $\vec F=q\,\vec v\times\vec B$ es perpendicular a $\vec v$ y a $\vec B$, con $\vec v\perp\vec B$ la fuerza está contenida en el plano del movimiento y apunta siempre hacia un punto fijo: actúa como una **fuerza centrípeta**. Su módulo es $F=qvB$ (porque $\vec v\perp\vec B\Rightarrow|\vec v\times\vec B|=vB$).
>
> **Paso 2 — Igualar a la fuerza centrípeta.** Una trayectoria circular de radio $r$ a rapidez constante $v$ exige una fuerza centrípeta $m v^2/r$. Igualando:
> $$q v B=\frac{m v^2}{r}.$$
>
> **Paso 3 — Despejar el radio.** Cancelando un factor $v$ (la carga se mueve, $v\neq 0$):
> $$\boxed{\,r=\frac{m v}{q B}\,.}$$
>
> **Paso 4 — Frecuencia angular.** La velocidad angular es $\omega=v/r$; sustituyendo $r$:
> $$\omega=\frac{v}{r}=\frac{v}{\,m v/(qB)\,}=\frac{q B}{m}.$$
> El factor $v$ se cancela: **todas las cargas de la misma especie giran con la misma frecuencia**, sin importar lo rápido que vayan. Las más veloces describen círculos más grandes, pero tardan lo mismo en cerrarlos. $\blacksquare$

> [!teoria] Trayectoria helicoidal
> Si $\vec v$ tiene una componente **paralela** a $\vec B$, esa componente no siente fuerza (porque $\vec v_\parallel\times\vec B=\vec 0$) y avanza a rapidez constante. La componente **perpendicular** sigue girando con radio $r=mv_\perp/(qB)$. La superposición de un giro circular y un avance uniforme da una **hélice** enrollada alrededor de las líneas de $\vec B$: así quedan atrapadas las partículas cargadas en los cinturones de radiación y en las botellas magnéticas.

![[lorentz_fuerza.svg|620]]
*(a) Una carga positiva con $\vec B$ saliente del plano describe una órbita circular: la fuerza $q\,\vec v\times\vec B$ apunta siempre hacia el centro, perpendicular a $\vec v$, y por eso no trabaja. (b) Un hilo recto que transporta corriente $I$ en un campo $\vec B$ uniforme experimenta una fuerza $\vec F=I\vec L\times\vec B$, perpendicular tanto al hilo como al campo.*

---

## Fuerza sobre una corriente

> [!teorema] Fuerza magnética sobre un conductor con corriente
> Sobre un conductor que transporta una densidad de corriente $\vec J$ en un campo $\vec B$, la fuerza magnética es
> $$\vec F=\int(\vec J\times\vec B)\,d\tau=\int I\,d\vec l\times\vec B.$$
> Para un hilo recto con corriente $I$ constante en un campo $\vec B$ **uniforme**, esto se reduce a
> $$\vec F=I\,\vec L\times\vec B,$$
> donde $\vec L$ es el vector que va del principio al final del segmento.

> [!demostracion]
> **Paso 1 — Sumar la fuerza sobre los portadores.** En un conductor hay $n$ portadores por unidad de volumen, cada uno con carga $q$ y velocidad de arrastre $\vec v$. La fuerza magnética sobre los portadores contenidos en un volumen $d\tau$ es la suma de las fuerzas individuales:
> $$d\vec F=(n\,d\tau)\,q\,(\vec v\times\vec B)=(n q\,\vec v)\times\vec B\;d\tau.$$
>
> **Paso 2 — Identificar la densidad de corriente.** La densidad de corriente es precisamente $\vec J=n q\,\vec v$ (carga por unidad de volumen por velocidad de arrastre). Entonces:
> $$d\vec F=(\vec J\times\vec B)\,d\tau\qquad\Longrightarrow\qquad \vec F=\int(\vec J\times\vec B)\,d\tau.$$
>
> **Paso 3 — Pasar a corriente de hilo.** Para un conductor filiforme de sección $A$, el volumen es $d\tau=A\,dl$ y la corriente vale $I=J A$. Como $\vec J$ apunta a lo largo del hilo, $\vec J\,d\tau=\vec J\,A\,dl=(J A)\,d\vec l=I\,d\vec l$. Por tanto:
> $$\vec F=\int I\,d\vec l\times\vec B.$$
>
> **Paso 4 — Caso uniforme.** Si $I$ y $\vec B$ son constantes, $I$ sale de la integral y $\vec B$ es factor común del producto cruz:
> $$\vec F=I\left(\int d\vec l\right)\times\vec B=I\,\vec L\times\vec B,\qquad \vec L=\int d\vec l.$$
> En un segmento recto $\vec L$ es simplemente el vector del tramo, de longitud $L$. $\blacksquare$

---

## Ejemplo

> [!ejemplo]
> **(a)** Un protón ($q=1{,}60\times10^{-19}\ \text{C}$, $m=1{,}67\times10^{-27}\ \text{kg}$) entra con rapidez $v=3{,}0\times10^{6}\ \text{m/s}$, perpendicular a un campo uniforme $B=0{,}50\ \text{T}$. Halla el radio y la frecuencia de su órbita. **(b)** Un segmento recto de hilo de longitud $L=0{,}20\ \text{m}$ transporta una corriente $I=8{,}0\ \text{A}$ perpendicular a un campo uniforme $B=0{,}50\ \text{T}$. Halla el módulo de la fuerza sobre el hilo.

> [!solucion]
> **(a) Radio ciclotrónico.** Por la fórmula deducida $r=mv/(qB)$:
> $$r=\frac{(1{,}67\times10^{-27})(3{,}0\times10^{6})}{(1{,}60\times10^{-19})(0{,}50)}\ \text{m}=\frac{5{,}01\times10^{-21}}{8{,}0\times10^{-20}}\ \text{m}\approx 6{,}3\times10^{-2}\ \text{m}.$$
> Es decir, $r\approx 6{,}3\ \text{cm}$.
>
> **Frecuencia angular.** Por $\omega=qB/m$:
> $$\omega=\frac{(1{,}60\times10^{-19})(0{,}50)}{1{,}67\times10^{-27}}\ \text{rad/s}\approx 4{,}8\times10^{7}\ \text{rad/s}.$$
> La frecuencia ordinaria es $f=\omega/2\pi\approx 7{,}6\times10^{6}\ \text{Hz}\approx 7{,}6\ \text{MHz}$, y **no depende** de $v$.
>
> **(b) Fuerza sobre el hilo.** Con $\vec L\perp\vec B$, el módulo de $\vec F=I\vec L\times\vec B$ es $F=I L B$:
> $$F=(8{,}0)(0{,}20)(0{,}50)\ \text{N}=0{,}80\ \text{N}.$$
> La fuerza es perpendicular al hilo y al campo (dirección dada por la regla de la mano derecha para $\vec L\times\vec B$). $\blacksquare$

---

## En qué consiste

La fuerza de Lorentz es la **definición operativa** de los campos: $\vec E$ y $\vec B$ se *miden* por la fuerza que ejercen sobre una carga de prueba. La parte eléctrica es directa —empuja en la dirección de $\vec E$—, pero la parte magnética es geométricamente más sutil: al ser $q\,\vec v\times\vec B$ siempre perpendicular a $\vec v$, el campo magnético actúa como un "timón" que **dobla** trayectorias sin gastar energía.

De ahí cuelgan los tres resultados clave de esta nota:

- **No trabaja** ($dW=0$): $\vec B$ conserva la energía cinética; solo cambia direcciones. Esto distingue radicalmente a la magnetostática de la electrostática.
- **Movimiento ciclotrónico**: una carga en $\vec B$ uniforme gira en círculos (o hélices) con un periodo que solo depende de $q/m$ y de $B$, no de la rapidez. Es la base del ciclotrón, el espectrómetro de masas y el confinamiento de plasmas.
- **Fuerza sobre corrientes** $\vec F=I\vec L\times\vec B$: como una corriente es carga en movimiento, la fuerza de Lorentz sumada sobre todos los portadores da la fuerza sobre el conductor. Es el principio del motor eléctrico y del galvanómetro.

Conviene leerla junto a [[Ley de Biot-Savart]]: una establece cómo $\vec B$ *actúa*, la otra cómo $\vec B$ se *crea*. Entre ambas describen por completo la interacción magnética entre corrientes.

---

## Resumen

> [!resumen]
> | Concepto | Expresión | Lectura |
> |:---|:---|:---|
> | Fuerza de Lorentz | $\vec F=q(\vec E+\vec v\times\vec B)$ | fuerza total sobre una carga |
> | Parte magnética | $q\,\vec v\times\vec B$, $\ \perp\vec v$ | nunca trabaja |
> | Trabajo magnético | $dW=q(\vec v\times\vec B)\cdot\vec v\,dt=0$ | conserva $\tfrac12 m v^2$ |
> | Radio de ciclotrón | $r=\dfrac{m v}{q B}$ | crece con $v$ |
> | Frecuencia de ciclotrón | $\omega=\dfrac{q B}{m}$ | independiente de $v$ |
> | Fuerza sobre corriente | $\vec F=\displaystyle\int I\,d\vec l\times\vec B$ | suma sobre portadores |
> | Hilo recto uniforme | $\vec F=I\,\vec L\times\vec B$ | $\;\vec L=$ vector del tramo |

> [!corolario]
> La fuerza magnética es **perpendicular a la velocidad** y por eso **no realiza trabajo**: $\vec B$ curva trayectorias y reorienta corrientes, pero la energía la aporta siempre la fuente. De este único hecho se derivan el giro ciclotrónico (radio $r=mv/qB$, frecuencia $\omega=qB/m$) y la fuerza $\vec F=I\vec L\times\vec B$ sobre un conductor.

> [!referencia]
> Griffiths, *Introduction to Electrodynamics*, cap. 5 ("Magnetostatics"), §5.1. Para más profundidad: Jackson, *Classical Electrodynamics*, cap. 5; Landau–Lifshitz, *Teoría clásica de campos*, vol. 2.
