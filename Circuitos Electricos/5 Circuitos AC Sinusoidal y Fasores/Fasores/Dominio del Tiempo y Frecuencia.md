---
title: Dominio del Tiempo y Frecuencia
tags:
  - circuitos-electricos
  - teoria
  - fasores
draft: false
aliases:
  - dominio del tiempo y frecuencia
  - transformación fasorial
  - transformada fasorial
  - time and frequency domain
  - phasor transform
---

# Dominio del Tiempo y Frecuencia: la Transformación Fasorial

> [!definicion]
> La **transformación fasorial** lleva una senoide del **dominio del tiempo**
> $$v(t)=V_m\operatorname{sen}(\omega t+\varphi)$$
> a un **fasor** en el **dominio de la frecuencia**
> $$\overline{V}=V\angle\varphi,\qquad V=\frac{V_m}{\sqrt2}.$$
> En el tiempo, las ecuaciones del circuito son **diferenciales**; en el dominio de la frecuencia se
> vuelven **algebraicas**, porque **derivar** pasa a **multiplicar por $j\omega$**. Trabajar con
> fasores es, entonces, cambiar de dominio para resolver con álgebra de números complejos lo que en el
> tiempo exigiría resolver ecuaciones diferenciales.

> [!info]
> Cierra los fundamentos de la sección [[Fasores/index| Fasores]]
> ([[5 Circuitos AC Sinusoidal y Fasores/index| capítulo 5]]) explicando **por qué funciona** la
> [[Representacion de Fasores| representación fasorial]]: justifica que la senoide y su fasor sean
> intercambiables y que las reglas $d/dt\to j\omega$ e $\int\to 1/j\omega$ sean legítimas. Es el
> paralelo en CA de lo que [[Laplace en Circuitos/index| Laplace]] hace con los transitorios. Fraile
> Mora, cap. 2, §2.4-2.5.

---

## Ejemplo

> [!ejemplo]
> **La misma señal en dos dominios, y la derivada.**
>
> Tomemos $v(t)=V_m\operatorname{sen}(\omega t+\varphi)$. Queremos (a) su fasor y (b) el fasor de su
> derivada $\dfrac{dv}{dt}$, sin volver a derivar a mano.
>
> ![[tiempo_frecuencia.svg|620]]
>
> *La misma señal: a la izquierda, la senoide en el tiempo; a la derecha, su fasor en el plano
> complejo. Pasar de una a otra es la transformación fasorial.*
>
> **(a) La correspondencia.** La senoide y el fasor son dos vistas del mismo objeto:
> $$v(t)=V_m\operatorname{sen}(\omega t+\varphi)\;\longleftrightarrow\;\overline{V}=V\angle\varphi.$$
> Se conserva amplitud (vía el valor eficaz $V=V_m/\sqrt2$) y fase $\varphi$; la frecuencia $\omega$ no
> aparece en el fasor porque es común a todo el circuito.
>
> **(b) La derivada.** En el dominio de la frecuencia, derivar en el tiempo equivale a **multiplicar
> por $j\omega$**:
> $$\frac{dv}{dt}\;\longleftrightarrow\;j\omega\,\overline{V}.$$
> Como $j=1\angle90^\circ$, multiplicar por $j\omega$ es **escalar el módulo por $\omega$** y **girar la
> fase $+90^\circ$**: el fasor de la derivada es $\omega V\angle(\varphi+90^\circ)$. Coherente con que
> $\dfrac{d}{dt}\operatorname{sen}(\omega t+\varphi)=\omega\operatorname{sen}(\omega t+\varphi+90^\circ)$.
>
> > [!solucion]
> > La correspondencia es **biunívoca**: a cada senoide de frecuencia $\omega$ le toca un único fasor y
> > viceversa. Y derivar/integrar en el tiempo equivalen, respectivamente, a $\times\,j\omega$ y
> > $\div\,j\omega$ en frecuencia. Por eso una ecuación diferencial del circuito se transforma en una
> > **ecuación algebraica** entre fasores.

---

## En qué consiste

> [!teoria] Por qué funciona la transformación
> La clave es el **régimen permanente**: un circuito **lineal** excitado por una senoide responde, una
> vez extinguido el transitorio, con senoides de la **misma frecuencia**; lo único que cambia entre
> entrada y salida son el **módulo** y la **fase**. Como $\omega$ es idéntica en todas las señales, se
> puede "factorizar" y dejar de escribirla: basta llevar la cuenta de módulo y fase, que es justo lo
> que guarda el fasor.
>
> Bajo esa hipótesis, cada operación del tiempo tiene un reflejo algebraico en frecuencia, y el
> dominio de la frecuencia **cambia ecuaciones diferenciales por algebraicas**. Resuelto el problema
> entre fasores, la **transformación inversa** recupera la señal real volviendo a girar el fasor a
> velocidad $\omega$:
> $$v(t)=\operatorname{Im}\bigl\{\sqrt2\,\overline{V}\,e^{j\omega t}\bigr\}.$$
> El factor $\sqrt2$ deshace el paso a valor eficaz y $e^{j\omega t}$ reintroduce la rotación que el
> fasor había "congelado".

> [!teoria] Por qué derivar se vuelve multiplicar por $j\omega$
> Escribamos la senoide como parte imaginaria de un giro:
> $v(t)=\operatorname{Im}\{\sqrt2\,\overline{V}\,e^{j\omega t}\}$. Al derivar,
> $$\frac{dv}{dt}=\operatorname{Im}\bigl\{\sqrt2\,\overline{V}\,(j\omega)\,e^{j\omega t}\bigr\},$$
> porque $\dfrac{d}{dt}e^{j\omega t}=j\omega\,e^{j\omega t}$. El factor $j\omega$ "sale" intacto: en el
> dominio de la frecuencia, derivar **es** multiplicar el fasor por $j\omega$. Integrar es la operación
> inversa, dividir por $j\omega$. De ahí salen directamente las relaciones de
> [[Fasores Electricos| $v$–$i$ en R, L y C]] y, agrupadas, la [[Impedancia Compleja| impedancia]].

> [!proposicion] Relación con Laplace
> El factor $j\omega$ es la variable $s$ de Laplace evaluada en el **eje imaginario**, $s=j\omega$. El
> análisis fasorial es, por tanto, el **caso de régimen permanente sinusoidal** del método de
> [[Laplace en Circuitos/index| Laplace]]: donde Laplace escribe $s$, el fasor escribe $j\omega$. Por
> eso una impedancia operacional $Z(s)$ se convierte en $Z(j\omega)$ sin más que sustituir, y la
> función de transferencia evaluada en $s=j\omega$ da la respuesta en frecuencia del circuito.

> [!warning]
> La transformación fasorial **solo** vale en **régimen permanente sinusoidal** y a una **única
> frecuencia**: no describe el **transitorio** (el arranque, la conexión, el cambio brusco); para eso
> se necesita [[Laplace en Circuitos/index| Laplace]], que sí maneja $s$ con parte real. Además, todas
> las senoides del problema deben compartir la **misma $\omega$**; con frecuencias distintas no existe
> un fasor común y hay que recurrir a superposición frecuencia a frecuencia.

## Resumen

> [!resumen]
> | Dominio del tiempo | Dominio de la frecuencia |
> |:---|:---|
> | $v(t)=V_m\operatorname{sen}(\omega t+\varphi)$ | $\overline{V}=V\angle\varphi$, $V=V_m/\sqrt2$ |
> | derivar $\dfrac{d}{dt}$ | multiplicar por $j\omega$ |
> | integrar $\displaystyle\int dt$ | dividir por $j\omega$ (es decir, $\times\,1/j\omega$) |
> | ecuación **diferencial** | ecuación **algebraica** |
> | recuperar $v(t)$ | $v(t)=\operatorname{Im}\{\sqrt2\,\overline{V}e^{j\omega t}\}$ |

> [!corolario]
> Cambiar al dominio de la frecuencia convierte el cálculo diferencial del circuito en **aritmética de
> números complejos**: ahí reside toda la potencia del método fasorial y el origen de la
> [[Impedancia Compleja| impedancia]]. La condición a no olvidar es que todo vale **a una sola
> frecuencia y en régimen permanente**.

> [!referencia]
> Fraile Mora, cap. 2, §2.4-2.5. Base: [[Representacion de Fasores]] y [[Fasores Electricos]].
> Generalización a transitorios: [[Laplace en Circuitos/index]]. Aplicación inmediata:
> [[Impedancia Compleja]].
