---
title: Teoría de Errores, Análisis y Estabilidad
order: 1
tags:
  - metodos-numericos
  - teoria
  - errores
  - index
draft: false
aliases:
  - teoría de errores
  - análisis de errores
  - estabilidad numérica
  - error analysis
---

# Teoría de Errores, Análisis y Estabilidad

> [!definicion]
> El cálculo numérico trabaja con **números de precisión finita**, así que casi ningún resultado es exacto. Esta sección estudia **de dónde salen los errores** (representar los reales en la máquina), **cómo se propagan** al operar, y cómo distinguir si el problema es sensible (**condicionamiento**) o si es el algoritmo el que amplifica el error (**estabilidad**). Es la base que dice cuánto fiarse de cualquier resultado numérico.

> [!info]
> Primer bloque del curso: antes de resolver sistemas, raíces o integrales conviene saber **qué error es inevitable y cuál es culpa del método**. Todo lo demás se apoya aquí. Bibliografía típica: Burden–Faires, cap. 1; Chapra–Canale, cap. 3–4.

## Las tres preguntas del bloque

> [!teoria] Representar, propagar, amplificar
> - **¿Cómo se guarda un real?** En **punto flotante** (norma IEEE 754), con una mantisa finita; el mínimo salto relativo es el **épsilon de máquina**. → [[Representacion Punto Flotante IEEE 754]], [[Epsilon Maquina y Precision Relativa]].
> - **¿Cómo se propaga el error al operar?** Sumas y productos arrastran el redondeo; restar cantidades casi iguales provoca **cancelación catastrófica** (pérdida de cifras significativas). → [[Perdida Significancia y Cancelacion Catastrofica]], [[Propagacion Errores Operaciones Matriciales]].
> - **¿Culpa del problema o del algoritmo?** El **número de condición** mide cuánto amplifica el **problema** un error en los datos; la **estabilidad** (forward/backward) mide si el **algoritmo** añade error de más. Un problema mal condicionado no lo arregla ningún método. → [[Condicionamiento Numerico Numero Condicion]], [[Estabilidad Algoritmos Forward Backward]].

## Mapa de la sección

> [!info] Las notas
> | Nota | Contenido |
> |:---|:---|
> | [[Representacion Punto Flotante IEEE 754]] | cómo se almacena un real; mantisa y exponente |
> | [[Epsilon Maquina y Precision Relativa]] | el salto relativo mínimo; precisión de la máquina |
> | [[Perdida Significancia y Cancelacion Catastrofica]] | restar casi iguales destruye cifras |
> | [[Condicionamiento Numerico Numero Condicion]] | sensibilidad del problema a los datos |
> | [[Estabilidad Algoritmos Forward Backward]] | si el algoritmo amplifica el error |
> | [[Propagacion Errores Operaciones Matriciales]] | acumulación del error al operar con matrices |

> [!corolario]
> Un resultado numérico solo vale lo que valen sus errores: hay que separar el que impone la **máquina** (redondeo), el que impone el **problema** (condicionamiento) y el que añade el **algoritmo** (estabilidad). Con esa distinción, el resto del curso se lee sabiendo qué precisión esperar.

> [!referencia]
> Burden–Faires, *Análisis Numérico*, cap. 1. Chapra–Canale, *Métodos Numéricos para Ingenieros*, cap. 3–4.
