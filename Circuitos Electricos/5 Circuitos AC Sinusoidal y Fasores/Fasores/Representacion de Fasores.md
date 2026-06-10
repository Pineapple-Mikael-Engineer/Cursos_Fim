---
title: Representación de Fasores
tags:
  - circuitos-electricos
  - teoria
  - fasores
draft: false
aliases:
  - representación de fasores
  - fasor
  - notación fasorial
  - phasor representation
---

# Representación de Fasores $\;\overline{V}=V\angle\varphi$

> [!definicion]
> Un **fasor** representa la senoide $v(t)=V_m\operatorname{sen}(\omega t+\varphi)$ por el número
> complejo
> $$\overline{V}=V\angle\varphi=V\,e^{j\varphi}=V\cos\varphi+jV\operatorname{sen}\varphi,$$
> cuyo **módulo** es el valor eficaz $V=V_m/\sqrt2$ y cuyo **argumento** es la fase $\varphi$. Guarda
> lo que distingue una senoide de otra (amplitud y fase) y omite la frecuencia $\omega$, común a todo
> el circuito.

> [!info]
> El concepto base de la sección [[Fasores/index| Fasores]] ([[5 Circuitos AC Sinusoidal y Fasores/index| capítulo 5]]). Aplica la idea a R, L y C en [[Fasores Electricos]] y se justifica en
> [[Dominio del Tiempo y Frecuencia]]. Fraile Mora, cap. 2, §2.3.

---

## Ejemplo

> [!ejemplo]
> **De la senoide al fasor, y suma de fasores.**
>
> Representar $v(t)=311\,\operatorname{sen}(\omega t+30^\circ)\ \text{V}$ y sumarle
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
> > frecuencia se reduce a **sumar dos complejos**.

---

## En qué consiste

> [!teoria] Tres formas del mismo número
> Un fasor se escribe de tres maneras equivalentes, y se elige la cómoda para cada operación:
> - **Polar:** $V\angle\varphi$ — directa para **multiplicar y dividir** (módulos se multiplican/dividen,
>   ángulos se suman/restan).
> - **Exponencial:** $V e^{j\varphi}$ — la misma, útil para derivar/integrar (aparece el factor
>   $j\omega$).
> - **Rectangular (binómica):** $a+jb$ con $a=V\cos\varphi$, $b=V\operatorname{sen}\varphi$ — directa
>   para **sumar y restar**.
>
> La unidad imaginaria es $j=\sqrt{-1}$ (en electricidad, **no** $i$, reservada a la corriente). El
> factor $j$ es un **giro de $+90^\circ$**: multiplicar por $j$ rota el fasor un cuarto de vuelta.

> [!teoria] El fasor es un vector giratorio congelado
> La senoide es la proyección de un vector que gira a velocidad $\omega$
> ([[Generacion de Tension Alterna| como en el alternador]]). El fasor es ese vector **detenido en
> $t=0$**: como todos giran a la misma $\omega$, sus posiciones **relativas** (las fases) no cambian, y
> basta una "foto" para operar. Recuperar la senoide es volver a girar: $v(t)=\operatorname{Im}\{\sqrt2\,
> \overline{V}\,e^{j\omega t}\}$.

> [!proposicion] Operar senoides = operar complejos
> | Operación con senoides | Con fasores |
> |:---|:---|
> | sumar/restar (igual $\omega$) | sumar/restar en rectangular |
> | derivar $d/dt$ | multiplicar por $j\omega$ |
> | integrar $\int dt$ | dividir por $j\omega$ |
> | desfasar $+90^\circ$ | multiplicar por $j$ |
>
> Estas reglas son las que convierten ecuaciones diferenciales en algebraicas.

> [!warning]
> El módulo del fasor es el **valor eficaz** ($V=V_m/\sqrt2$), no el pico (norma del curso). Y los
> fasores solo se suman/comparan entre senoides de **igual frecuencia**; con frecuencias distintas, no
> hay un fasor común. La unidad imaginaria es $j$, no $i$.

## Resumen

> [!resumen]
> | Forma | Expresión |
> |:---|:---|
> | Polar | $\overline{V}=V\angle\varphi$ |
> | Exponencial | $\overline{V}=V e^{j\varphi}$ |
> | Rectangular | $\overline{V}=V\cos\varphi+jV\operatorname{sen}\varphi$ |
> | Módulo | $V=V_m/\sqrt2$ (valor eficaz) |
> | Recuperar $v(t)$ | $v=\operatorname{Im}\{\sqrt2\,\overline{V}e^{j\omega t}\}$ |

> [!corolario]
> El fasor reduce cada senoide a un punto del plano complejo. Sumar, derivar o desfasar senoides se
> vuelve aritmética compleja: ese es el motor del análisis de CA, que en [[Fasores Electricos]] se
> aplica a los elementos del circuito.

> [!referencia]
> Fraile Mora, cap. 2, §2.3. Aplicación a R, L, C: [[Fasores Electricos]]. Justificación:
> [[Dominio del Tiempo y Frecuencia]].
