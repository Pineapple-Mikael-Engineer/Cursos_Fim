---
title: Fasores
tags:
  - circuitos-electricos
  - teoria
  - fasores
  - index
draft: false
aliases:
  - fasores
  - representación fasorial
---

# Fasores

> [!definicion]
> Un **fasor** es la representación de una senoide de régimen permanente por un **número complejo**
> $\overline{V}=V\angle\varphi$ que retiene su amplitud (como valor eficaz $V$) y su fase $\varphi$,
> omitiendo la frecuencia $\omega$ (común a todo el circuito). Convierte el manejo de senoides en
> **álgebra de números complejos**: es el cambio de variable que hace tratable la corriente alterna.

> [!info]
> Primera sección del [[5 Circuitos AC Sinusoidal y Fasores/index| capítulo 5]]. Toma la
> [[Onda Sinusoidal]] del capítulo 4 y la "congela" en un complejo; sobre los fasores se construyen la
> [[Impedancia y Admitancia/index| impedancia]] y todo el [[Analisis Fasorial/index| análisis fasorial]]. Fraile Mora, cap. 2, §2.3.

---

## De la senoide al complejo

> [!teoria] Tres ideas, tres notas
> El paso al fasor se entiende en tres movimientos:
>
> - **Qué es un fasor.** Una senoide queda fijada por amplitud y fase; eso es justo un número
>   complejo, escrito en forma polar $V\angle\varphi$ o exponencial $V e^{j\varphi}$. Operar senoides
>   se vuelve sumar y multiplicar complejos. → [[Representacion de Fasores]].
>
> - **Cómo se aplica a R, L y C.** En cada elemento, tensión y corriente fasoriales guardan una
>   relación de fase fija: en la resistencia van **en fase**; en el inductor la tensión **adelanta**
>   $90^\circ$; en el condensador la corriente **adelanta** $90^\circ$. → [[Fasores Electricos]].
>
> - **Por qué se puede.** El fasor vive en el **dominio de la frecuencia**: derivar en el tiempo es
>   multiplicar por $j\omega$ en fasores. Pasar del tiempo a la frecuencia y volver es el puente que
>   lo justifica todo. → [[Dominio del Tiempo y Frecuencia]].

> [!info] Por qué el fasor lleva el valor eficaz
> Por convenio de ingeniería (norma del curso), el módulo del fasor es el **valor eficaz**
> $V=V_m/\sqrt2$, no la amplitud de pico. Así las fórmulas de potencia salen directas (sin factores
> $\tfrac12$), y "$\overline{V}=230\angle0^\circ$" significa una red de $230\ \text{V}$ eficaces.

> [!info] Las notas de esta sección
> | Nota | Contenido |
> |:---|:---|
> | [[Representacion de Fasores]] | el fasor $\overline{V}=V\angle\varphi=Ve^{j\varphi}$; formas y operaciones |
> | [[Fasores Electricos]] | fase de $v$ e $i$ en R, L y C; diagramas fasoriales |
> | [[Dominio del Tiempo y Frecuencia]] | la transformación fasorial; $d/dt\to j\omega$ |

> [!corolario]
> Representar la senoide por un fasor es el truco que vertebra todo el análisis de CA: a partir de
> aquí, los circuitos sinusoidales se resuelven como resistivos, pero con números complejos.

> [!referencia]
> Fraile Mora, cap. 2, §2.3-2.4. Siguiente sección: [[Impedancia y Admitancia/index| Impedancia y admitancia]].
