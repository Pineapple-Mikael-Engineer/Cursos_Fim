---
title: Sistemas Y-Y, Delta-Delta, Y-Delta
tags:
  - circuitos-electricos
  - teoria
  - trifasico
draft: false
aliases:
  - sistemas Y-Y, Δ-Δ, Y-Δ
  - combinaciones fuente-carga
  - configuraciones trifásicas
  - three-phase configurations
  - source-load combinations
---

# Sistemas Y-Y, Δ-Δ, Y-Δ

> [!definicion]
> La **fuente** y la **carga** de un sistema trifásico pueden ir, cada una, en **estrella (Y)** o en
> **triángulo (Δ)**, lo que da **cuatro combinaciones**: **Y-Y**, **Δ-Δ**, **Y-Δ** y **Δ-Y**. Todas
> se resuelven con el mismo método: **llevar a Y** la parte que esté en Δ (con $Z_Y=Z_\Delta/3$),
> analizar **una sola fase** y aplicar las relaciones $\sqrt3$ para volver a las magnitudes de línea.

> [!info]
> Reúne las dos [[Conexiones Balanceadas/index| conexiones]] del [[7 Circuitos Trifasicos/index| capítulo 7]]
> en sus combinaciones prácticas fuente-carga; se apoya en [[Conexion Estrella]] y en
> [[Conexion Triangulo]], usa [[Estrella Triangulo Kennelly]] para convertir Δ→Y y desemboca en el
> [[Circuito Equivalente Monofasico]]. Fraile Mora, cap. 3, §3.5-3.6.

---

## Ejemplo

> [!ejemplo]
> **Sistema Y-Δ.**
>
> Una fuente en **estrella** de tensión de fase $230\ \text{V}$ (por tanto $V_L=\sqrt3\cdot230\approx400\ \text{V}$)
> alimenta una carga en **triángulo** de impedancia por rama $Z_\Delta=30\angle40^\circ\ \Omega$. Hallar
> la corriente de fase de la carga y la corriente de línea.
>
> **Paso 1 — Tensión que ve la carga.** En Δ, la tensión de fase de la rama es la propia tensión de
> línea: $V_F^{\text{carga}}=V_L=400\ \text{V}$.
>
> **Paso 2 — Corriente de fase (en la rama del triángulo).**
> $$I_F=\frac{V_F^{\text{carga}}}{Z_\Delta}=\frac{400}{30}\approx13{,}3\ \text{A}\quad(\angle-40^\circ).$$
>
> **Paso 3 — Corriente de línea.** En Δ, $I_L=\sqrt3\,I_F$:
> $$I_L=\sqrt3\cdot13{,}3\approx23\ \text{A}.$$
>
> > [!solucion]
> > $I_F\approx13{,}3\ \text{A}$ en cada rama del triángulo; $I_L\approx23\ \text{A}$ por cada línea.
> > La carga en Δ "ve" la **tensión de línea completa** ($400\ \text{V}$), no la de fase de la fuente.

---

## En qué consiste

> [!teoria] Las cuatro combinaciones
> - **Y-Y** — la más directa: cada rama de la fuente alimenta una rama de la carga a través de su
>   línea, y los dos puntos comunes (neutros) pueden unirse por un cuarto hilo. Las relaciones $\sqrt3$
>   están en las **tensiones** a ambos lados.
> - **Δ-Δ** — **sin neutro**: la tensión de línea coincide con la de fase en los dos lados; el $\sqrt3$
>   está en las **corrientes**. Permite seguir funcionando si una rama falla (Δ abierto).
> - **Y-Δ** y **Δ-Y** — **mixtas**. Lo habitual es **transmitir en Y** (con neutro disponible) y
>   **consumir en Δ** (muchos motores), o al revés en los devanados de transformadores. Para analizarlas
>   se **convierte** la parte en Δ a su Y equivalente con $Z_Y=Z_\Delta/3$ ([[Estrella Triangulo Kennelly]]).
>
> En todos los casos, una vez todo está en Y, el sistema es un Y-Y y basta estudiar **una fase**
> ([[Circuito Equivalente Monofasico]]).

> [!algoritmo] Resolver cualquier combinación
> 1. **Convertir a Y** toda fuente o carga que esté en **Δ**, usando $Z_Y=Z_\Delta/3$.
> 2. Queda un sistema **Y-Y**; tomar **una sola fase** ([[Circuito Equivalente Monofasico]]), con la
>    tensión de fase de la fuente y la impedancia de la rama en Y.
> 3. **Resolver** esa fase: $\overline{I}_F=\overline{V}_F/\overline{Z}_Y$, tensiones en cada elemento, etc.
> 4. **Volver a las magnitudes reales** (línea y fase) con las relaciones $\sqrt3$ según la conexión
>    **original** de cada lado, deshaciendo la conversión Δ→Y donde la hubo.

> [!proposicion] La conversión clave
> $Z_Y=Z_\Delta/3$ (con $Z_\Delta=3\,Z_Y$). Una carga **equilibrada** en triángulo equivale, vista
> **desde las líneas**, a una en estrella con un **tercio** de impedancia por rama. Es lo que permite
> reducir Δ-Y o Y-Δ a un Y-Y y aplicar el análisis monofásico.

> [!warning]
> Al convertir Δ→Y, **no olvidar deshacer** la conversión al reportar las corrientes/tensiones de las
> **ramas reales** del triángulo: las de fase del Δ se obtienen de las de línea con $\sqrt3$ y $30^\circ$,
> y **no** coinciden con las de la Y equivalente (esa es un artificio de cálculo). En **Y-Y sin neutro**
> con carga **equilibrada** no pasa nada (el neutro lleva $0$); con **desequilibrio**, el neutro
> importa y su ausencia desplaza el potencial.

## Resumen

> [!resumen]
> | Combinación | Neutro | $V$ línea vs fase | $I$ línea vs fase | Método |
> |:---|:---|:---|:---|:---|
> | **Y-Y** | sí (4 hilos) | $V_L=\sqrt3\,V_F$ (ambos) | $I_L=I_F$ (ambos) | directo, una fase |
> | **Δ-Δ** | no | $V_L=V_F$ (ambos) | $I_L=\sqrt3\,I_F$ (ambos) | directo, una fase |
> | **Y-Δ** | en la fuente | fuente $V_L=\sqrt3\,V_F$; carga $V_L=V_F$ | fuente $I_L=I_F$; carga $I_L=\sqrt3\,I_F$ | $Z_Y=Z_\Delta/3$ → Y-Y |
> | **Δ-Y** | en la carga | fuente $V_L=V_F$; carga $V_L=\sqrt3\,V_F$ | fuente $I_L=\sqrt3\,I_F$; carga $I_L=I_F$ | $Z_Y=Z_\Delta/3$ → Y-Y |

> [!corolario]
> No hay cuatro métodos, sino **uno**: convertir todo a Y con $Z_Y=Z_\Delta/3$, resolver **una fase**
> y volver con $\sqrt3$. La combinación solo decide **dónde** hay neutro y en qué magnitud (tensión o
> corriente) aparece el $\sqrt3$ a cada lado.

> [!referencia]
> Fraile Mora, cap. 3, §3.5-3.6. Conexiones base: [[Conexion Estrella]], [[Conexion Triangulo]].
> Conversión: [[Estrella Triangulo Kennelly]]. Análisis por fase: [[Circuito Equivalente Monofasico]].
