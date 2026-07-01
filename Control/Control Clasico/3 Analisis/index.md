---
title: Análisis
order: 3
tags:
  - control-clasico
  - analisis
  - index
draft: false
aliases:
  - análisis
  - análisis de sistemas de control
  - control analysis
---

# Análisis

> [!definicion]
> **Analizar** un sistema de control es extraer de su modelo todo lo que importa para el desempeño: si es **estable**, cómo es su **respuesta en el tiempo** (rapidez, sobrepico), cuánto **error** deja en régimen permanente y cómo responde en **frecuencia**. Es el puente entre tener el modelo (modelado) y decidir cómo mejorarlo (diseño): dice qué falla y cuánto margen hay.

> [!info]
> Tercer bloque del [[Control Clasico/index| Control Clásico]]. Toma el modelo del [[2 Modelado/index| modelado]] y lo evalúa; sus conclusiones marcan las especificaciones del [[4 Diseno/index| diseño]]. Ogata, cap. 4–8; Nise, cap. 4–10.

## Las cuatro preguntas del análisis

> [!teoria] Estabilidad, tiempo, error y frecuencia
> - **Estabilidad**: ¿vuelve el sistema al equilibrio? Se decide por la ubicación de los polos (criterio de **Routh–Hurwitz** sin resolverlos). → [[Estabilidad/index| Estabilidad]].
> - **Respuesta temporal**: forma de $y(t)$ ante las [[Señales Prueba/index| señales de prueba]]; primer y segundo orden, polos dominantes. → [[Respuesta Temporal/index| Respuesta temporal]].
> - **Error estacionario**: cuánto se aparta la salida de la referencia en régimen permanente; tipos de sistema y coeficientes de error. → [[Error Estacionario/index| Error estacionario]].
> - **Respuesta en frecuencia**: comportamiento ante senoides de distinta frecuencia (Bode, Nyquist) y los **márgenes** de estabilidad. → [[Respuesta Frecuencial/index| Respuesta frecuencial]].

## Mapa de la sección

> [!info] Las subsecciones
> | Subsección | Contenido |
> |:---|:---|
> | [[Estabilidad/index\| Estabilidad]] | polos, Routh–Hurwitz |
> | [[Respuesta Temporal/index\| Respuesta temporal]] | primer/segundo orden; polos dominantes |
> | [[Señales Prueba/index\| Señales de prueba]] | impulso, escalón, rampa, parábola |
> | [[Error Estacionario/index\| Error estacionario]] | tipos de sistema; $K_p,K_v,K_a$ |
> | [[Respuesta Frecuencial/index\| Respuesta frecuencial]] | Bode, Nyquist, márgenes |

> [!corolario]
> El análisis mide **estabilidad, velocidad, error y márgenes** a partir de los polos y de la respuesta en frecuencia. De esas cuatro lecturas salen las especificaciones que el diseño debe cumplir.

> [!referencia]
> Ogata, *Ingeniería de Control Moderna*, cap. 4–8. Nise, *Control Systems Engineering*, cap. 4–10.
