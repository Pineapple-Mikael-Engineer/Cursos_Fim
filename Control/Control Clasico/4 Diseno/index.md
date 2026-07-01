---
title: Diseño
order: 4
tags:
  - control-clasico
  - diseno
  - index
draft: false
aliases:
  - diseño
  - diseño de controladores
  - control design
---

# Diseño

> [!definicion]
> **Diseñar** un sistema de control es elegir y ajustar un controlador para que la planta cumpla unas especificaciones (estabilidad, rapidez, sobrepico, error permanente). El control clásico ofrece dos grandes marcos gráficos: el **lugar de las raíces** —diseño en el **plano $s$**, moviendo los polos de lazo cerrado con la ganancia y compensadores— y la **respuesta en frecuencia** —diseño con Bode/Nyquist, sobre márgenes de ganancia y fase—.

> [!info]
> Cierra el curso: aplica lo visto en [[3 Analisis/index| análisis]] para **sintetizar** el controlador. Las dos vías (raíces y frecuencia) son complementarias; la nota de selección orienta cuándo usar cada una. Ogata, cap. 6–9; Nise, cap. 8–11.

## Dos marcos de diseño

> [!teoria] Lugar de raíces, frecuencia y elección
> - **Lugar de las raíces**: dibuja cómo se mueven los polos de lazo cerrado al variar la ganancia; permite **colocar** los polos dominantes donde den el transitorio deseado, añadiendo compensadores de adelanto/atraso. → [[Lugar Raices/index| Lugar de raíces]].
> - **Respuesta en frecuencia**: diseña sobre los diagramas de **Bode/Nyquist**, ajustando **márgenes de ganancia y fase** para robustez y ancho de banda. → [[Respuesta Frecuencia/index| Respuesta en frecuencia]].
> - **Selección del método**: criterios para decidir entre plano $s$ y frecuencia según las especificaciones y la información disponible de la planta. → [[Seleccion Metodo]].

## Mapa de la sección

> [!info] Las subsecciones
> | Elemento | Contenido |
> |:---|:---|
> | [[Lugar Raices/index\| Lugar de raíces]] | diseño en el plano $s$; compensadores adelanto/atraso |
> | [[Respuesta Frecuencia/index\| Respuesta en frecuencia]] | Bode/Nyquist; márgenes de ganancia y fase |
> | [[Seleccion Metodo]] | cuándo usar cada enfoque |

> [!corolario]
> El lugar de raíces piensa en **dónde están los polos**; la respuesta en frecuencia, en **cuánta ganancia y fase** hay a cada frecuencia. Dominar ambos y saber cuál conviene es el objetivo final del control clásico.

> [!referencia]
> Ogata, *Ingeniería de Control Moderna*, cap. 6–9. Nise, *Control Systems Engineering*, cap. 8–11.
