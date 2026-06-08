---
title: Fundamentos de EDP
tags:
  - ecuaciones
  - edp
  - teoria
  - fundamentos
  - index
draft: false
aliases:
  - fundamentos EDP
  - clasificación de EDP
---

# Fundamentos de EDP

> [!definicion]
> El marco común antes de resolver: qué es una EDP y su solución, cómo se **clasifican** las de
> segundo orden (elíptica/parabólica/hiperbólica), qué significa que un problema esté **bien
> planteado** (Hadamard) y qué **condiciones** —iniciales y de frontera— corresponden a cada tipo.

> [!info]
> Base del [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]]. Aquí no se resuelve
> ninguna ecuación concreta; se establece el lenguaje y, sobre todo, la **clasificación**, que es la
> que decide después qué método y qué datos usar para el calor, la onda y Laplace.

---

## Por qué la clasificación lo es todo

> [!teoria]
> Una EDO de orden $n$ se resuelve siempre con $n$ datos: el problema "está bien" casi por defecto.
> En las EDP **no**: una misma ecuación puede tener solución única, ninguna o infinitas según
> **qué** condiciones se impongan y **dónde**. La clave es el **tipo** de la EDP, que se lee de un
> **discriminante** —exactamente como las cónicas $Ax^2+Bxy+Cy^2$ son elipse/parábola/hipérbola según
> $B^2-4AC$—. Ese tipo determina:
> - la **física**: difusión (parabólica), propagación (hiperbólica) o equilibrio (elíptica);
> - las **condiciones bien planteadas**: solo de frontera (elíptica), inicial + frontera (parabólica),
>   inicial con dos datos + frontera (hiperbólica);
> - el **comportamiento**: suavizado irreversible, frentes a velocidad finita, o promediado.
>
> Por eso clasificar es el primer reflejo ante cualquier EDP de segundo orden.

> [!info] Recorrido de la sección
> | Nota | Aporte |
> |---|---|
> | [[Concepto y Notacion EDP\|Concepto y Notación]] | orden, linealidad, notación de subíndices $u_x,u_{xx}$ |
> | [[Clasificacion Segundo Orden\|Clasificación de Segundo Orden]] | discriminante → elíptica / parabólica / hiperbólica |
> | [[Formas Canonicas\|Formas Canónicas]] | cambio de variable que reduce cada tipo a su prototipo |
> | [[Problemas Bien Planteados\|Problemas Bien Planteados]] | existencia + unicidad + dependencia continua (Hadamard) |
> | [[Tipos de Condiciones\|Tipos de Condiciones]] | Cauchy, Dirichlet, Neumann, Robin |

## Resumen

> [!resumen]
> | Tipo | Discriminante | Prototipo | Datos bien planteados |
> |---|---|---|---|
> | Elíptica | $B^2-4AC<0$ | Laplace $\nabla^2u=0$ | solo frontera |
> | Parabólica | $B^2-4AC=0$ | calor $u_t=\alpha^2u_{xx}$ | inicial + frontera |
> | Hiperbólica | $B^2-4AC>0$ | onda $u_{tt}=c^2u_{xx}$ | $u,u_t$ iniciales + frontera |

> [!corolario]
> Antes de elegir método, **clasifica**: el tipo de la EDP fija qué datos la hacen bien planteada y
> cómo se comportará la solución. Esta sección es el "manual de instrucciones" del resto del capítulo.

> [!referencia]
> - El corazón de la sección: [[Clasificacion Segundo Orden]].
> - Qué condiciones poner: [[Tipos de Condiciones]] y [[Problemas Bien Planteados]].
> - Después, el método maestro: [[Separacion de Variables y Fourier/index]].
