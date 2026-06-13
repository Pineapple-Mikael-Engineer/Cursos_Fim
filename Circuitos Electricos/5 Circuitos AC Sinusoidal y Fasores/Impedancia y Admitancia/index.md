---
title: Impedancia y Admitancia
tags:
  - circuitos-electricos
  - teoria
  - impedancia
  - index
draft: false
aliases:
  - impedancia y admitancia
  - impedancia
---

# Impedancia y Admitancia

> [!definicion]
> La **impedancia** $Z=\dfrac{\overline{V}}{\overline{I}}$ es la generalización compleja de la
> resistencia al régimen sinusoidal: combina la **resistencia** $R$ (parte real, disipa) y la
> **reactancia** $X$ (parte imaginaria, desfasa) en $Z=R+jX$, medida en ohmios. Su inversa es la
> **admitancia** $Y=\dfrac{1}{Z}=G+jB$. Con impedancias, los circuitos de CA se resuelven **igual** que
> los resistivos.

> [!info]
> Segunda sección del [[5 Circuitos AC Sinusoidal y Fasores/index| capítulo 5]]. Convierte los
> desfases de [[Fasores]] en un único número complejo, y es la base del
> [[Analisis Fasorial/index| análisis fasorial]]. Es el equivalente, en régimen sinusoidal, de la
> impedancia $Z(s)$ de [[Circuitos en el Dominio de s| Laplace]] con $s=j\omega$. Fraile Mora, cap. 2,
> §2.7.

---

## Una "resistencia" que también desfasa

> [!teoria] Resistencia, reactancia y su triángulo
> La impedancia tiene dos efectos en uno:
> - su parte **real** $R$ —la **resistencia**— relaciona tensión y corriente **en fase** (disipa);
> - su parte **imaginaria** $X$ —la **reactancia**— las relaciona **a $90^\circ$** (almacena y devuelve).
>
> Para cada elemento, $Z_R=R$, $Z_L=j\omega L$ (reactancia $+\omega L$, inductiva) y
> $Z_C=\dfrac{1}{j\omega C}=-\dfrac{j}{\omega C}$ (reactancia $-1/\omega C$, capacitiva). El módulo
> $|Z|=\sqrt{R^2+X^2}$ y el ángulo $\varphi=\arctan(X/R)$ forman el **triángulo de impedancias**. →
> [[Impedancia Compleja]] y [[Respuesta de Elementos Pasivos]].

> [!teoria] Admitancia: la cara cómoda del paralelo
> Igual que la conductancia $G=1/R$ simplificaba las resistencias en paralelo, la **admitancia**
> $Y=1/Z=G+jB$ (conductancia $G$ + susceptancia $B$) simplifica las **impedancias en paralelo**: se
> **suman** las admitancias. → [[Admitancia]] y [[Asociacion de Impedancias]].

## Mapa de la sección

> [!info] Las notas de esta sección
> | Nota | Contenido |
> |:---|:---|
> | [[Impedancia Compleja]] | $Z=R+jX$; módulo, ángulo, triángulo de impedancias |
> | [[Respuesta de Elementos Pasivos]] | cómo responden R, L, C a la CA; reactancias |
> | [[Admitancia]] | $Y=1/Z=G+jB$; conductancia y susceptancia |
> | [[Asociacion de Impedancias]] | serie ($\sum Z$) y paralelo (vía $Y$) |

> [!corolario]
> La impedancia codifica en un solo número complejo lo que cuesta hacer pasar corriente y cuánto la
> desfasa. Con ella —y su inversa, la admitancia— la ley de Ohm y todos los métodos del análisis
> resistivo se trasladan intactos a la CA.

> [!referencia]
> Fraile Mora, cap. 2, §2.7. Anterior: [[Fasores| Fasores]]. Siguiente:
> [[Analisis Fasorial/index| Análisis fasorial]].
