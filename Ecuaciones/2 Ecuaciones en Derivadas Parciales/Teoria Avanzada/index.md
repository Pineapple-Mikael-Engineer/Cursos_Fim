---
title: Teoría Avanzada de EDP
tags:
  - ecuaciones
  - edp
  - teoria
  - avanzado
  - index
draft: false
aliases:
  - teoría avanzada EDP
  - soluciones débiles
  - EDP no lineales
---

# Teoría Avanzada de EDP

> [!definicion]
> Mirada **panorámica** a hacia dónde va la teoría moderna de EDP cuando los métodos clásicos
> (separación, características, Green) ya no bastan: cuando la solución **no es derivable**
> (soluciones débiles y **distribuciones**), cuando se busca en el espacio "correcto" (**espacios de
> Sobolev** y formulación variacional), y cuando la ecuación es **no lineal** (solitones, explosión,
> patrones).

> [!info]
> Cierre del [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]], en clave de
> **panorama**: no busca exhaustividad, sino mostrar el puente entre lo elemental del curso y el
> análisis funcional de las EDP. Conecta con las
> [[Distribuciones y Soluciones Debiles| funciones generalizadas]] ya usadas (la $\delta$ de Dirac).

---

## Tres saltos conceptuales

> [!teoria]
> La teoría clásica supone soluciones **suaves**. Pero los fenómenos reales —choques, esquinas,
> fuentes puntuales— producen soluciones que **no** lo son. La matemática moderna da tres saltos para
> acomodarlas:
> 1. **Ampliar qué es "función" y "derivada".** Las **distribuciones** (funciones generalizadas)
>    permiten derivar objetos no diferenciables —incluso la $\delta$ de Dirac— y dan sentido a las
>    **soluciones débiles**: una $u$ resuelve la EDP "en promedio", contra funciones de prueba
>    ([[Distribuciones y Soluciones Debiles| distribuciones y soluciones débiles]]).
> 2. **Elegir el espacio correcto.** Los **espacios de Sobolev** $H^k$ miden función + derivadas en
>    norma $L^2$; ahí viven las soluciones débiles, y la EDP se reescribe como una **formulación
>    variacional** (forma débil) resoluble con álgebra de espacios de Hilbert (Lax-Milgram) —
>    ([[Espacios de Sobolev| espacios de Sobolev]]).
> 3. **Salir de lo lineal.** Sin superposición, aparecen fenómenos nuevos: **solitones** (KdV),
>    **formación de patrones** (reacción-difusión), **explosión** y turbulencia (Navier-Stokes) —
>    ([[EDP No Lineales| EDP no lineales]]).

> [!info] Recorrido de la sección
> | Nota | Aporte |
> |---|---|
> | [[Distribuciones y Soluciones Debiles\|Distribuciones y Soluciones Débiles]] | derivada débil, $\delta$, solución en sentido distribucional |
> | [[Espacios de Sobolev\|Espacios de Sobolev]] | $H^k$, formulación variacional, Lax-Milgram |
> | [[EDP No Lineales\|EDP No Lineales]] | solitones, reacción-difusión, blow-up (panorama) |

## Resumen

> [!resumen]
> | Salto | De | A |
> |---|---|---|
> | Derivada | clásica (suave) | **débil** / distribucional |
> | Espacio | $C^k$ | **Sobolev** $H^k$ |
> | Formulación | fuerte (puntual) | **variacional** (forma débil) |
> | Linealidad | superposición | fenómenos no lineales (solitones, patrones) |

> [!corolario]
> La teoría avanzada **amplía el concepto de solución** para que las EDP de la física —con choques,
> impulsos y no linealidades— tengan respuestas rigurosas. Es el paso del cálculo clásico al análisis
> funcional: cambiar el espacio y el sentido de "resolver" para que el problema tenga sentido.

> [!referencia]
> - El punto de entrada: [[Distribuciones y Soluciones Debiles]].
> - El marco funcional: [[Espacios de Sobolev]].
> - Lo que rompe la linealidad: [[EDP No Lineales]].
