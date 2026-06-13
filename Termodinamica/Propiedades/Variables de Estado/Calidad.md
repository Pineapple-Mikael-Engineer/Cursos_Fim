---
title: "Calidad $x$"
tags:
  - termodinamica
  - propiedades
  - variables_de_estado
  - calidad
draft: false
aliases:
  - quality
  - x
  - título de vapor
---

# Calidad $x$

> [!definicion]
> En la región bifásica líquido–vapor, la **calidad** (o título de vapor) es la fracción másica de vapor en la mezcla saturada:
> $$
> x = \frac{m_g}{m_g + m_f} = \frac{m_{vapor}}{m_{total}}, \qquad 0 \le x \le 1
> $$
> - $x = 0$: líquido saturado.
> - $x = 1$: vapor saturado.
>
> Solo está definida dentro de la campana de saturación, donde [[Presion]] y [[Temperatura]] son dependientes y se requiere una tercera propiedad para fijar el estado.

## Regla de la palanca

> [!teorema]
> Cualquier propiedad específica $y \in \{v, u, h, s\}$ de la mezcla se obtiene interpolando entre las fases saturadas con la calidad:
> $$
> y = y_f + x\,y_{fg}, \qquad y_{fg} = y_g - y_f
> $$
>
> Despejando, la calidad se mide a partir de cualquier propiedad específica conocida:
> $$
> x = \frac{y - y_f}{y_{fg}}
> $$
>
> Las propiedades de las fases ($y_f$, $y_g$) se leen en las tablas de saturación a la presión o temperatura dada.

> [!demostracion]
> **Origen de la regla.** El volumen total es suma de las contribuciones de cada fase:
> $$
> V = m_f v_f + m_g v_g
> $$
> Dividiendo entre $m = m_f + m_g$ y usando $m_g/m = x$, $m_f/m = 1-x$:
> $$
> v = (1-x)v_f + x\,v_g = v_f + x(v_g - v_f) = v_f + x\,v_{fg}
> $$
> El argumento es idéntico para $U$, $H$, $S$ por ser extensivas, lo que extiende la fórmula a $u$, $h$, $s$.

> [!ejemplo]
> **Calidad a partir de la entropía.** Agua a $P = 100\ \text{kPa}$ con $s = 5.0\ \text{kJ/kg·K}$. De tablas: $s_f = 1.3026$, $s_g = 7.3594\ \text{kJ/kg·K}$.
> $$
> x = \frac{5.0 - 1.3026}{7.3594 - 1.3026} = \frac{3.6974}{6.0568} = 0.6105
> $$
> El estado es una mezcla con $\sim 61\%$ de vapor en masa.

## Interpretación y límites

> [!warning]
> - La calidad es una fracción **másica**, no volumétrica: con $v_g \gg v_f$, una calidad baja ya ocupa casi todo el volumen en fase vapor.
> - No está definida fuera de la región bifásica: para líquido comprimido o vapor sobrecalentado el estado se fija con $(P,T)$ y hablar de calidad carece de sentido.
> - En equilibrio, $T = T_{sat}(P)$ es independiente de $x$: añadir vapor a la mezcla no cambia $T$ ni $P$ mientras coexistan ambas fases.

## Relación con otras propiedades

> [!info]
> - Cierra el estado en la región de saturación junto con $P$ o $T$ (ver [[Presion]], [[Temperatura]]).
> - Se usa para evaluar [[Volumen Especifico]], [[Energia Interna]], [[Entalpia]] y [[Entropia]] de mezclas saturadas.
> - Determina el estado de salida en [[Toberas]], [[Turbinas]] y [[Valvulas]] cuando el proceso termina dentro de la campana.

> [!info]
> **Convención de notación**:
> - $x$: calidad (fracción másica de vapor), adimensional
> - subíndice $f$: líquido saturado; $g$: vapor saturado; $fg$: diferencia $g - f$
