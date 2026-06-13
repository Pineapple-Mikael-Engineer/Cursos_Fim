---
title: Fasores
tags:
  - circuitos-electricos
  - teoria
  - fasores
draft: false
aliases:
  - fasores
  - representación fasorial
  - fasor
  - notación fasorial
  - transformación fasorial
  - fasores en R L C
  - phasor
---

# Fasores

> [!definicion]
> Un **fasor** es la representación de una senoide de régimen permanente por un **número complejo**
> $$\overline{V}=V\angle\varphi=V\,e^{j\varphi}=V\cos\varphi+jV\operatorname{sen}\varphi,$$
> cuyo **módulo** es el valor eficaz $V=V_m/\sqrt2$ y cuyo **argumento** es la fase $\varphi$. Retiene lo
> que distingue una senoide de otra —amplitud y fase— y omite la frecuencia $\omega$, común a todo el
> circuito. Así, **operar senoides se convierte en álgebra de números complejos**: es el cambio de
> variable que hace tratable la corriente alterna.

> [!info]
> Primera sección del [[5 Circuitos AC Sinusoidal y Fasores/index | capítulo 5]]. Toma la
> [[Onda Sinusoidal]] del capítulo 4 y la "congela" en un complejo; sobre los fasores se construyen la
> [[Impedancia Compleja | impedancia]] y todo el [[Analisis Fasorial/index | análisis fasorial]]. Es el
> paralelo en CA de lo que [[Laplace en Circuitos/index | Laplace]] hace con los transitorios. Fraile
> Mora, cap. 2, §2.3-2.6.

---

## Ejemplo

> [!ejemplo]
> **De la senoide al fasor, y suma de senoides.**
>
> Representar $v_1(t)=311\,\operatorname{sen}(\omega t+30^\circ)\ \text{V}$ y sumarle
> $v_2(t)=311\,\operatorname{sen}(\omega t-60^\circ)\ \text{V}$.
>
> ![[fasor_diagrama.svg|470]]
>
> *Un fasor es un punto del plano complejo: módulo $=$ valor eficaz, ángulo $=$ fase. Sus proyecciones
> dan las partes real ($V\cos\varphi$) e imaginaria ($V\operatorname{sen}\varphi$).*
>
> **Paso 1 — Al fasor.** El valor eficaz es $V=311/\sqrt2\approx220\ \text{V}$, luego
> $\overline{V}_1=220\angle30^\circ$ y $\overline{V}_2=220\angle(-60^\circ)$.
>
> **Paso 2 — Sumar en forma rectangular.**
> $\overline{V}_1=220(\cos30^\circ+j\operatorname{sen}30^\circ)=190{,}5+j110$;
> $\overline{V}_2=220(\cos(-60^\circ)+j\operatorname{sen}(-60^\circ))=110-j190{,}5$.
> $$\overline{V}_1+\overline{V}_2=300{,}5-j80{,}5.$$
>
> **Paso 3 — Volver a polar.** Módulo $\sqrt{300{,}5^2+80{,}5^2}\approx311\ \text{V}$; ángulo
> $\arctan(-80{,}5/300{,}5)\approx-15^\circ$.
>
> > [!solucion]
> > $\overline{V}_1+\overline{V}_2\approx311\angle(-15^\circ)\ \text{V}$, es decir
> > $v_1+v_2\approx440\operatorname{sen}(\omega t-15^\circ)\ \text{V}$. Sumar dos senoides de igual
> > frecuencia —que en el tiempo exigiría identidades trigonométricas— se reduce a **sumar dos
> > complejos**.

---

## El fasor: tres formas y el operador $j$

> [!teoria] Tres formas del mismo número
> Un fasor se escribe de tres maneras equivalentes, y se elige la cómoda para cada operación:
> - **Polar:** $V\angle\varphi$ — directa para **multiplicar y dividir** (los módulos se
>   multiplican/dividen, los ángulos se suman/restan).
> - **Exponencial:** $V e^{j\varphi}$ — la misma, útil para derivar/integrar (aparece el factor
>   $j\omega$) y para demostrar fórmulas.
> - **Rectangular (binómica):** $a+jb$ con $a=V\cos\varphi$, $b=V\operatorname{sen}\varphi$ — directa
>   para **sumar y restar**.
>
> La unidad imaginaria es $j=\sqrt{-1}$ (en electricidad, **no** $i$, reservada a la corriente). El
> factor $j$ es un **giro de $+90^\circ$**: multiplicar por $j$ rota el fasor un cuarto de vuelta
> ($j=1\angle90^\circ$), y $j^2=-1$ es un giro de $180^\circ$.

> [!teoria] El fasor es un vector giratorio congelado
> La senoide es la proyección de un vector que gira a velocidad $\omega$
> ([[Generacion de Tension Alterna | como en el alternador]]). El **fasor es ese vector detenido en
> $t=0$**: como todos los vectores del circuito giran a la **misma** $\omega$, sus posiciones
> **relativas** (las fases) no cambian, y basta una "foto" para operar. Recuperar la senoide es volver
> a girar:
> $$v(t)=\operatorname{Im}\bigl\{\sqrt2\,\overline{V}\,e^{j\omega t}\bigr\},$$
> donde $e^{j\omega t}$ reintroduce la rotación que el fasor había congelado y $\sqrt2$ deshace el paso
> a valor eficaz.

> [!proposicion] Operar senoides = operar complejos
> | Operación con senoides | Con fasores |
> |:---|:---|
> | sumar/restar (igual $\omega$) | sumar/restar en rectangular |
> | derivar $d/dt$ | multiplicar por $j\omega$ |
> | integrar $\int dt$ | dividir por $j\omega$ |
> | desfasar $+90^\circ$ | multiplicar por $j$ |
>
> Estas reglas son las que convierten **ecuaciones diferenciales en algebraicas**: ahí reside toda la
> potencia del método.

## Por qué basta con las senoides: Fourier

> [!teoria] El fasor solo sabe de senoides… y eso es suficiente
> El método fasorial **solo** representa senoides de una frecuencia. Cabría temer que sirviera apenas
> para el caso idealizado de una única senoide. La razón de que sea **general** es el **teorema de
> Fourier**: toda señal **periódica** $v(t)$ (de período $T$, aunque sea cuadrada, triangular o
> deformada) se descompone en una **suma de senoides** —su fundamental y sus armónicos—:
> $$v(t)=V_0+\sum_{n=1}^{\infty}V_n\operatorname{sen}(n\omega_0 t+\varphi_n),\qquad \omega_0=\frac{2\pi}{T}.$$
> Cada término es una senoide pura, y por tanto **tiene su fasor**.
>
> ![[fourier_armonicos.svg|620]]
>
> *Una onda cuadrada reconstruida como suma de su fundamental y sus armónicos impares. Cada armónico es
> una senoide con su propio fasor; sumando unos pocos ya se aproxima la onda.*

> [!teorema] Análisis armónico: resolver y superponer
> En un circuito **lineal** vale la [[Proporcionalidad y Superposicion | superposición]]. Entonces una
> excitación periódica no senoidal se trata así:
> $$\textbf{Paso 1.}\ \text{descomponer } v(t) \text{ en sus armónicos (Fourier).}$$
> $$\textbf{Paso 2.}\ \text{resolver el circuito con fasores para } \textbf{cada} \text{ armónico } n\omega_0 \text{ por separado.}$$
> $$\textbf{Paso 3.}\ \text{superponer en el tiempo las respuestas de todos los armónicos.}$$
> Hay que resolver una vez por armónico **porque la impedancia depende de la frecuencia**
> ($Z_L=j n\omega_0 L$ crece con $n$; $Z_C=1/(jn\omega_0 C)$ decrece): cada armónico "ve" un circuito
> distinto. Así, el fasor —que parecía limitado a una senoide— cubre **cualquier** régimen periódico.

> [!proposicion] Por qué la senoide es la onda "natural" de los circuitos lineales
> La senoide es la **única** forma de onda que un circuito lineal (R, L, C) reproduce sin deformar:
> entra una senoide de frecuencia $\omega$ y sale otra senoide de la **misma** $\omega$ (cambian solo
> módulo y fase). Una onda cuadrada, en cambio, sale deformada (cada armónico se atenúa y desfasa
> distinto). Por eso la senoide es la "base" en la que conviene descomponer: es **autofunción** de los
> elementos lineales, y el fasor es su etiqueta.

> [!warning]
> El análisis armónico exige **linealidad** (para superponer) y **periodicidad** (para que Fourier dé
> una suma discreta de armónicos). Señales no periódicas se tratan con la **transformada** de Fourier o
> de [[Laplace en Circuitos/index | Laplace]] (espectro continuo), no con un número finito de fasores.

## El valor eficaz como módulo del fasor

> [!info] Qué módulo lleva el fasor, y por qué
> Por convenio de ingeniería (norma de este curso), el módulo del fasor es el **valor eficaz**
> $V=V_m/\sqrt2$, no la amplitud de pico. El [[Valores Caracteristicos| valor eficaz]] de una onda cualquiera
> es la raíz de la media de su cuadrado, $V_{ef}=\sqrt{\frac1T\int_0^T v^2\,dt}$ (para la senoide,
> $V_m/\sqrt2$); es el valor de la continua que **disiparía la misma potencia**. Tomarlo como módulo
> tiene una ventaja concreta: las fórmulas de potencia salen **directas**, sin factores $\tfrac12$
> ($S=\overline{V}\,\overline{I}^{*}$, $P=VI\cos\varphi$), y "$\overline{V}=230\angle0^\circ$" significa
> una red de $230\ \text{V}$ **eficaces**, justo lo que se mide y se factura.

## La transformación fasorial (tiempo ↔ frecuencia)

> [!ejemplo]
> **La misma señal en dos dominios, y la derivada sin derivar.**
>
> Para $v(t)=V_m\operatorname{sen}(\omega t+\varphi)$, hallar su fasor y el fasor de $\dfrac{dv}{dt}$.
>
> ![[tiempo_frecuencia.svg|600]]
>
> *La misma señal: a la izquierda, la senoide en el tiempo; a la derecha, su fasor en el plano
> complejo. Pasar de una a otra es la transformación fasorial.*
>
> **Correspondencia.** $v(t)\;\longleftrightarrow\;\overline{V}=V\angle\varphi$ (se conserva amplitud
> vía $V=V_m/\sqrt2$ y fase $\varphi$).
> **Derivada.** $\dfrac{dv}{dt}\;\longleftrightarrow\;j\omega\,\overline{V}$: como $j=1\angle90^\circ$,
> el fasor de la derivada es $\omega V\angle(\varphi+90^\circ)$, coherente con
> $\dfrac{d}{dt}\operatorname{sen}(\omega t+\varphi)=\omega\operatorname{sen}(\omega t+\varphi+90^\circ)$.
>
> > [!solucion]
> > La correspondencia es **biunívoca**, y derivar/integrar en el tiempo equivalen a $\times j\omega$ y
> > $\div\,j\omega$ en frecuencia. Por eso una ecuación diferencial del circuito se vuelve **algebraica**.

> [!teoria] Por qué funciona la transformación
> La clave es el **régimen permanente**: un circuito **lineal** excitado por una senoide responde, una
> vez extinguido el transitorio, con senoides de la **misma frecuencia**; lo único que cambia entre
> entrada y salida son el módulo y la fase. Como $\omega$ es idéntica en todas las señales, se
> "factoriza" y se deja de escribir: basta llevar la cuenta de módulo y fase, que es justo lo que
> guarda el fasor.

> [!demostracion] Derivar **es** multiplicar por $j\omega$
> Escribamos la senoide como parte imaginaria de un giro,
> $v(t)=\operatorname{Im}\{\sqrt2\,\overline{V}\,e^{j\omega t}\}$. Al derivar,
> $$\frac{dv}{dt}=\operatorname{Im}\bigl\{\sqrt2\,\overline{V}\,(j\omega)\,e^{j\omega t}\bigr\},$$
> porque $\dfrac{d}{dt}e^{j\omega t}=j\omega\,e^{j\omega t}$. El factor $j\omega$ "sale" intacto: en el
> dominio de la frecuencia, derivar es multiplicar el fasor por $j\omega$, e integrar es dividir por
> $j\omega$. De ahí salen directamente las relaciones $v$–$i$ de R, L y C. $\blacksquare$

> [!proposicion] Relación con Laplace
> El factor $j\omega$ es la variable $s$ de [[Laplace en Circuitos/index | Laplace]] evaluada en el
> **eje imaginario**, $s=j\omega$. El análisis fasorial es el **caso de régimen permanente sinusoidal**
> de Laplace: donde Laplace escribe $s$, el fasor escribe $j\omega$, y una impedancia $Z(s)$ se vuelve
> $Z(j\omega)$ sin más que sustituir.

## Fasores en los elementos: R, L y C

> [!ejemplo]
> **Las tres relaciones de fase.**
>
> Por los tres elementos circula la misma corriente $\overline{I}=I\angle0^\circ$. ¿Qué fase tiene la
> tensión en cada uno?
>
> ![[fasores_RLC.svg|620]]
>
> *Resistencia: $\overline{V}$ e $\overline{I}$ alineados. Inductor: $\overline{V}$ a $90^\circ$ por
> delante. Condensador: $\overline{I}$ a $90^\circ$ por delante de $\overline{V}$.*
>
> **Resistencia.** $\overline{V}_R=R\,\overline{I}=RI\angle0^\circ$: **en fase**.
> **Inductor.** $\overline{V}_L=j\omega L\,\overline{I}=\omega L\,I\angle90^\circ$: la tensión
> **adelanta** $90^\circ$.
> **Condensador.** $\overline{V}_C=\dfrac{\overline{I}}{j\omega C}=\dfrac{I}{\omega C}\angle(-90^\circ)$:
> la tensión **atrasa** $90^\circ$ (la corriente adelanta).
>
> > [!solucion]
> > $\overline{V}_R$ en fase; $\overline{V}_L$ adelantada $90^\circ$; $\overline{V}_C$ atrasada
> > $90^\circ$ respecto a $\overline{I}$. El cociente $\overline{V}/\overline{I}$ es la
> > [[Impedancia Compleja | impedancia]] de cada elemento.

> [!teoria] De dónde sale cada desfase
> El desfase nace de las leyes $v$–$i$ al pasar al fasor (donde $d/dt\to j\omega$):
> - **Resistencia:** $v=Ri\Rightarrow\overline{V}=R\,\overline{I}$. Sin $j$: **en fase**.
> - **Inductor:** $v=L\dfrac{di}{dt}\Rightarrow\overline{V}=j\omega L\,\overline{I}$. El $j$ adelanta la
>   tensión $90^\circ$ (la corriente "se resiste" a cambiar y va por detrás).
> - **Condensador:** $i=C\dfrac{dv}{dt}\Rightarrow\overline{V}=\overline{I}/(j\omega C)$: la **corriente
>   adelanta** $90^\circ$.

> [!regla] Mnemotecnia "ELI the ICE man"
> En el inductor (**L**), la tensión **E** va antes que la corriente **I**: **E-L-I**. En el condensador
> (**C**), la corriente **I** va antes que la tensión **E**: **I-C-E**.

> [!proposicion] El desfase y la energía
> Que en R no haya desfase y en L, C sí, tiene un significado físico: la resistencia **disipa** (tensión
> y corriente "tiran a la vez"), mientras que $L$ y $C$ solo **almacenan y devuelven** energía —el
> desfase de $90^\circ$ hace que su potencia media sea cero—. Es la semilla de la
> [[Potencia en Regimen Sinusoidal| potencia en elementos puros]].

> [!warning]
> Cuidados al usar fasores: (1) el módulo es el **valor eficaz** $V_m/\sqrt2$, no el pico; (2) solo se
> suman/comparan fasores de **igual frecuencia** (con frecuencias distintas hay que superponer armónico
> a armónico); (3) la unidad imaginaria es $j$, no $i$; (4) todo vale en **régimen permanente
> sinusoidal**, no en el transitorio (para eso, [[Laplace en Circuitos/index | Laplace]]).

## Resumen

> [!resumen] El fasor y sus formas
> | Forma | Expresión |
> |:---|:---|
> | Polar | $\overline{V}=V\angle\varphi$ |
> | Exponencial | $\overline{V}=V e^{j\varphi}$ |
> | Rectangular | $\overline{V}=V\cos\varphi+jV\operatorname{sen}\varphi$ |
> | Módulo | $V=V_m/\sqrt2$ (valor eficaz) |
> | Recuperar $v(t)$ | $v=\operatorname{Im}\{\sqrt2\,\overline{V}e^{j\omega t}\}$ |

> [!resumen] Tiempo ↔ frecuencia y los elementos
> | Tiempo | Frecuencia (fasores) |
> |:---|:---|
> | derivar $d/dt$ | $\times\,j\omega$ |
> | integrar $\int dt$ | $\div\,j\omega$ |
> | resistencia | $\overline{V}=R\,\overline{I}$ ($0^\circ$) |
> | inductor | $\overline{V}=j\omega L\,\overline{I}$ ($+90^\circ$) |
> | condensador | $\overline{V}=\overline{I}/(j\omega C)$ ($-90^\circ$) |
> | onda periódica no senoidal | Fourier: un fasor por armónico, superponer |

> [!corolario]
> El fasor reduce cada senoide a un punto del plano complejo, y por Fourier eso alcanza a **cualquier**
> régimen periódico. Sumar, derivar o desfasar se vuelve aritmética compleja, y las leyes $v$–$i$ de
> R, L, C se convierten en factores ($R$, $j\omega L$, $1/j\omega C$): justo el cociente
> $\overline{V}/\overline{I}$ que define la [[Impedancia Compleja | impedancia]], el siguiente paso.

> [!referencia]
> Fraile Mora, cap. 2, §2.3-2.6. Base: [[Onda Sinusoidal]] y [[Valores Caracteristicos]]. Generaliza a
> transitorios: [[Laplace en Circuitos/index]]. Continúa en: [[Impedancia Compleja]] y
> [[Analisis Fasorial/index]].
