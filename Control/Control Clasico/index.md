---
title: Control Clásico
order: 1
tags:
  - control-clasico
  - index
draft: false
aliases:
  - control clásico
  - sistemas de control
  - classical control
---

# Control Clásico

> [!definicion]
> El **control clásico** estudia cómo hacer que un sistema dinámico (la **planta**) se comporte como queremos, realimentando su salida y ajustando un **controlador**. Trabaja con modelos **lineales e invariantes en el tiempo**, la **transformada de Laplace** y la **función de transferencia**, y razona sobre estabilidad y desempeño con herramientas gráficas —**lugar de las raíces** y **respuesta en frecuencia**— en lugar de resolver las ecuaciones diferenciales a mano.

> [!info]
> Curso completo, organizado en cinco bloques que van de lo conceptual a lo aplicado: **fundamentos → modelado → análisis → diseño → controladores**. Modelo de estilo y profundidad: Ogata (*Ingeniería de Control Moderna*) y Nise (*Control Systems Engineering*).

## El hilo del curso

> [!teoria] De la planta al controlador
> - **Fundamentos**: qué es un sistema de control, lazo abierto vs cerrado y por qué realimentar. → [[1 Conceptos Fundamentales/index| Conceptos fundamentales]].
> - **Modelado**: obtener el modelo de la planta en cada dominio físico, pasarlo a Laplace y a función de transferencia (o a espacio de estados). → [[2 Modelado/index| Modelado]].
> - **Análisis**: leer estabilidad, respuesta temporal, error permanente y respuesta en frecuencia a partir de ese modelo. → [[3 Analisis/index| Análisis]].
> - **Diseño**: sintetizar el controlador con el lugar de raíces o en frecuencia. → [[4 Diseno/index| Diseño]].
> - **Controladores**: la familia PID y su sintonización, el caballo de batalla industrial. → [[5 Controladores/index| Controladores]].

## Mapa del curso

> [!info] Los bloques
> | Bloque | Contenido |
> |:---|:---|
> | [[1 Conceptos Fundamentales/index\| Conceptos fundamentales]] | componentes, lazo abierto/cerrado, sensibilidad |
> | [[2 Modelado/index\| Modelado]] | dominios físicos, Laplace, función de transferencia, estado |
> | [[3 Analisis/index\| Análisis]] | estabilidad, respuesta temporal y frecuencial, error |
> | [[4 Diseno/index\| Diseño]] | lugar de raíces y respuesta en frecuencia |
> | [[5 Controladores/index\| Controladores]] | PID: acciones, configuraciones, sintonización |

> [!corolario]
> Todo el control clásico es un mismo bucle: **modelar** la planta, **analizar** su comportamiento en el plano $s$ o en frecuencia, y **diseñar** la realimentación que cumpla las especificaciones. Los cinco bloques recorren ese camino de principio a fin.

> [!referencia]
> Ogata, *Ingeniería de Control Moderna*. Nise, *Control Systems Engineering*. Dorf–Bishop, *Modern Control Systems*.
