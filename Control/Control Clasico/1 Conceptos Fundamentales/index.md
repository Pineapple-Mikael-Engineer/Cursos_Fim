---
title: Conceptos Fundamentales
order: 1
tags:
  - control-clasico
  - conceptos-fundamentales
  - index
draft: false
aliases:
  - conceptos fundamentales
  - fundamentos de control
  - control basics
---

# Conceptos Fundamentales

> [!definicion]
> Antes de modelar o diseñar, hace falta el **vocabulario** del control: qué **componentes** forman un sistema de control (planta, sensor, controlador, actuador, referencia), la diferencia entre operar en **lazo abierto** y en **lazo cerrado**, y por qué realimentar reduce la **sensibilidad** a perturbaciones e incertidumbre. Son las ideas que justifican todo lo que viene después.

> [!info]
> Primer bloque del curso de Control Clásico. Fija el marco conceptual sobre el que se apoyan el [[2 Modelado/index| modelado]], el [[3 Analisis/index| análisis]] y el [[4 Diseno/index| diseño]]. Ogata, cap. 1; Nise, cap. 1.

## Las tres ideas de partida

> [!teoria] Componentes, lazo y sensibilidad
> - **Componentes**: el bucle de control encadena referencia → controlador → actuador → **planta** → salida, con un **sensor** que la mide y la realimenta. → [[Componentes Sistema]].
> - **Lazo abierto vs cerrado**: en lazo abierto la acción no depende de la salida (simple, pero sin corrección de errores); en **lazo cerrado** se realimenta el error y el sistema se autocorrige. → [[Lazo Abierto Cerrado]].
> - **Sensibilidad**: realimentar **reduce** el efecto de variaciones de la planta y de las perturbaciones sobre la salida; es la razón de fondo para cerrar el lazo. → [[Sensibilidad]].

## Mapa de la sección

> [!info] Las notas
> | Nota | Contenido |
> |:---|:---|
> | [[Componentes Sistema]] | planta, sensor, controlador, actuador, referencia |
> | [[Lazo Abierto Cerrado]] | control con y sin realimentación |
> | [[Sensibilidad]] | por qué la realimentación reduce la sensibilidad |

> [!corolario]
> Cerrar el lazo cuesta un sensor y algo de complejidad, pero compra **corrección automática del error** y **robustez** frente a la incertidumbre. Ese trueque es la idea que vertebra todo el control clásico.

> [!referencia]
> Ogata, *Ingeniería de Control Moderna*, cap. 1. Nise, *Control Systems Engineering*, cap. 1.
