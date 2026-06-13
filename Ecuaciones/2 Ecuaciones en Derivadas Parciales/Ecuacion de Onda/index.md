---
title: Ecuación de Onda
tags:
  - ecuaciones
  - edp
  - teoria
  - onda
  - index
draft: false
aliases:
  - ecuación de onda
  - wave equation
---

# Ecuación de Onda

> [!definicion]
> La **ecuación de onda** describe perturbaciones que se **propagan** sin deformarse a velocidad
> finita $c$ (una cuerda, el sonido, la luz):
> $$u_{tt}=c^2\,u_{xx}\qquad(\text{1D}),\qquad u_{tt}=c^2\,\nabla^2u\ \ (\text{general}).$$
> Es la EDP **hiperbólica** prototipo: **conserva** la energía, **no suaviza** (transmite los picos)
> y propaga la información dentro de un **cono** a velocidad $c$.

> [!info]
> Segunda ecuación madre del [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]] (tipo
> **hiperbólico**, ver [[Clasificacion Segundo Orden| clasificación]]). Admite **dos** métodos
> complementarios: [[Separacion Onda y Modos Normales| separación de variables]] (modos) en dominios
> acotados y la [[Solucion de dAlembert| solución de d'Alembert]] (características) en la recta.

---

## Qué la hace especial: propagación a velocidad finita

> [!teoria]
> Frente al calor, la onda es su **opuesto cualitativo**, por ser hiperbólica:
> 1. **Velocidad finita.** Una perturbación en un punto solo afecta a la región alcanzable a
>    velocidad $c$: el **cono de influencia**. El valor en $(x,t)$ depende solo del **dominio de
>    dependencia** $[x-ct,\,x+ct]$ del dato inicial. Nada viaja más rápido que $c$.
> 2. **No suaviza; conserva.** Las esquinas del dato inicial se **propagan** intactas (no se liman),
>    y la **energía** total se conserva (sistema sin disipación).
> 3. **Reversibilidad.** La ecuación es simétrica en $t\to-t$: la película de una onda se puede pasar
>    al revés. No hay flecha del tiempo.
> 4. **Dos datos iniciales.** Al ser de segundo orden en $t$, requiere $u(x,0)$ **y** $u_t(x,0)$
>    (posición y velocidad), como la segunda ley de Newton.
>
> La síntesis de todo esto es la [[Solucion de dAlembert| fórmula de d'Alembert]]
> $u=\tfrac12[f(x-ct)+f(x+ct)]+\tfrac1{2c}\int_{x-ct}^{x+ct}g$, que separa la onda en dos pulsos que
> viajan a izquierda y derecha.

> [!info] Recorrido de la sección
> | Nota | Aporte |
> |---|---|
> | [[Derivacion de Onda\|Derivación]] | de Newton sobre una cuerda a $u_{tt}=c^2u_{xx}$ |
> | [[Separacion Onda y Modos Normales\|Separación y Modos Normales]] | armónicos de una cuerda fija; timbre |
> | [[Solucion de dAlembert\|Solución de d'Alembert]] | dos pulsos; dominio de dependencia |
> | [[Ondas en 2D y 3D\|Ondas en 2D y 3D]] | principio de Huygens; Kirchhoff/Poisson |
> | [[Energia de la Onda\|Energía de la Onda]] | conservación ⇒ unicidad |

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Ecuación | $u_{tt}=c^2u_{xx}$ (hiperbólica) |
> | Datos | $u(x,0)=f$ **y** $u_t(x,0)=g$ + frontera |
> | Método (acotado) | modos normales $\operatorname{sen}\frac{n\pi x}{L}\cos\frac{n\pi ct}{L}$ |
> | Método (recta) | d'Alembert: $\tfrac12[f(x{-}ct){+}f(x{+}ct)]+\tfrac1{2c}\int g$ |
> | Rasgos | propaga, conserva energía, reversible |

> [!corolario]
> La onda es la ecuación de la **memoria**: lo que entra, viaja y vuelve sin perderse. Su solución es
> una **superposición de modos** (en una cuerda) o de dos pulsos viajeros (en la recta); en ambos
> casos la energía se conserva y la información respeta el límite de velocidad $c$.

> [!referencia]
> - De dónde sale: [[Derivacion de Onda]].
> - Las dos vías: [[Separacion Onda y Modos Normales]] y [[Solucion de dAlembert]].
> - El contraste parabólico: [[Ecuacion del Calor/index]].
