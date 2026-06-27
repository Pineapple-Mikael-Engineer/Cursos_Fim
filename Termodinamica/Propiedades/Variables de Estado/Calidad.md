---
title: "Calidad $x$"
order: 4
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
> **Hipótesis:** sistema binario en equilibrio termodinámico; dos fases coexistentes (líquido saturado y vapor saturado) sin efectos de superficie; mezcla homogénea dentro de cada fase.
>
> **Paso 1 — Definición operativa de la calidad.**
> La calidad mide la fracción en masa de la fase vapor:
> $$x = \frac{m_g}{m_g + m_f} = \frac{m_g}{m},$$
> donde $m = m_f + m_g$ es la masa total. Por tanto $m_f/m = 1 - x$. La calidad $x = 0$ corresponde a líquido saturado puro; $x = 1$, a vapor saturado puro.
>
> **Paso 2 — Aditividad extensiva del volumen.**
> El volumen total del sistema es la suma de los volúmenes de las dos fases (propiedad extensiva):
> $$V = V_f + V_g.$$
> Cada fase ocupa su volumen con las propiedades de saturación a la temperatura de la mezcla: $V_f = m_f\,v_f$ y $V_g = m_g\,v_g$.
>
> **Paso 3 — Expresar $V$ en función de las masas y propiedades de saturación.**
> Sustituyendo:
> $$V = m_f\,v_f + m_g\,v_g.$$
>
> **Paso 4 — Dividir por la masa total para obtener $v$ específico.**
> $$v = \frac{V}{m} = \frac{m_f\,v_f + m_g\,v_g}{m} = \frac{m_f}{m}\,v_f + \frac{m_g}{m}\,v_g = (1-x)\,v_f + x\,v_g.$$
>
> **Paso 5 — Reescribir en la forma estándar y generalizar.**
> Expandiendo y agrupando términos:
> $$v = v_f + x\,(v_g - v_f) = v_f + x\,v_{fg}. \qquad \blacksquare$$
> El mismo argumento aplica a $U$, $H$, $S$ porque son extensivas: $Y = m_f y_f + m_g y_g$. Dividiendo por $m$:
> $$y = y_f + x\,y_{fg} \qquad \text{para } y \in \{u, h, s\}.$$
>
> **Verificación de límites:** para $x=0$, $y = y_f$ (líquido saturado puro). Para $x=1$, $y = y_f + y_{fg} = y_g$ (vapor saturado puro). $\checkmark$

> [!ejemplo]
> **Calidad a partir de la entropía.** Agua a $P = 100\ \text{kPa}$ con $s = 5.0\ \text{kJ/kg·K}$. De tablas: $s_f = 1.3026$, $s_g = 7.3594\ \text{kJ/kg·K}$.
> $$
> x = \frac{5.0 - 1.3026}{7.3594 - 1.3026} = \frac{3.6974}{6.0568} = 0.6105
> $$
> El estado es una mezcla con $\sim 61\%$ de vapor en masa.

## Significado físico: calidad ≠ fracción volumétrica

> [!teoria]
> La calidad es una fracción **másica**, pero no corresponde a la fracción **volumétrica** de vapor, y la diferencia es grande. A baja calidad, casi todo el volumen es vapor aunque casi toda la masa sea líquido, porque $v_g \gg v_f$.
>
> Ejemplo con agua a $100\,°\text{C}$ ($v_f = 0.001044\,\text{m}^3/\text{kg}$, $v_g = 1.6720\,\text{m}^3/\text{kg}$):
>
> | $x$ | Fracción en masa de vapor | Fracción volumétrica de vapor $V_g/V$ | Descripción visual |
> |:---:|:---:|:---:|:---|
> | 0 | 0% | 0% | Todo líquido, burbuja inexistente |
> | 0.01 | 1% | 94% | 1% de masa como vapor, pero ocupa casi todo el volumen |
> | 0.1 | 10% | 99.4% | Mezcla con pocas gotas de líquido en vapor |
> | 0.5 | 50% | 99.9% | La mitad de la masa es vapor; visualmente casi todo vapor |
> | 1 | 100% | 100% | Todo vapor saturado |
>
> La fracción volumétrica de vapor se calcula como:
> $$\frac{V_g}{V} = \frac{x\,v_g}{v_f + x\,v_{fg}} \approx \frac{x\,v_g}{x\,v_g} = 1 \quad \text{cuando } v_g \gg v_f.$$
>
> **Implicación práctica:** en ciclos Rankine, la salida de la turbina suele estar en la región bifásica con $x \approx 0.85$–$0.92$. Aunque el 8–15% de la masa sea líquido, ese líquido forma gotas que erosionan los álabes a alta velocidad. Por eso se impone el límite $x \geq 0.88$ en el diseño de turbinas de vapor.

![[calidad_region_bifasica.svg|440]]
*Campana de saturación en el diagrama $T$–$v$ con líneas de calidad constante ($x = 0.2, 0.4, 0.6, 0.8$). Las líneas de $x$ constante convergen al punto crítico. Notar que a $x$ baja el punto se acerca al límite izquierdo ($v_f$, curva líquido saturado) aunque visualmente el vapor ocupe casi todo el volumen.*

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
