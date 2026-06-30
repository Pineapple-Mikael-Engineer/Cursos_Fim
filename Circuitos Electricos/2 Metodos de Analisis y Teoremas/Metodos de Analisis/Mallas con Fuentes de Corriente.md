---
title: Mallas con Fuentes de Corriente
tags:
  - circuitos-electricos
  - teoria
  - metodos-analisis
  - mallas
draft: false
aliases:
  - supermalla
  - mallas con fuentes de corriente
  - análisis de mallas con fuente de corriente
  - supermesh
  - supermesh analysis
---

# Mallas con Fuentes de Corriente

> [!definicion]
> Cuando una **fuente de corriente** es compartida por dos mallas, **no se puede escribir la LKV de cada malla por separado**: la tensión sobre la fuente de corriente es una **incógnita** (una fuente ideal de corriente impone su corriente, pero deja libre la tensión en sus bornes). La técnica de la **supermalla** rodea las dos mallas por su **contorno exterior** —evitando la rama de la fuente— para escribir **UNA** LKV en la que esa tensión desconocida ya no aparece, y añade la **ecuación de restricción** que la propia fuente proporciona: la diferencia de las corrientes de malla iguala a $I_s$.

> [!info]
> Caso especial del [[Analisis de Mallas]], dentro de [[Metodos de Analisis/index| Métodos de análisis]] del [[2 Metodos de Analisis y Teoremas/index| capítulo 2]]. Es el **dual** del [[Nodos con Fuentes de Voltaje| supernodo]] (allí una fuente de tensión entre dos nodos; aquí una fuente de corriente entre dos mallas). La condición que aporta la fuente es una [[Ecuaciones de Restriccion| ecuación de restricción]]. Fraile Mora, cap. 1, §1.12.

---

## Ejemplo

> [!ejemplo]
> **Dos mallas con una fuente de corriente en la rama central.**
>
> Datos: $V_s = 10\ \text{V}$, $R_1 = 2\ \Omega$, $R_3 = 2\ \Omega$ y una fuente de corriente $I_s = 1\ \text{A}$ situada en la **rama central compartida**, con el sentido **hacia abajo**. Las corrientes de malla son $i_a$ (ventana izquierda) e $i_b$ (derecha), **ambas horarias**.
>
> ![[supermalla.svg|470]]
>
> *La fuente $I_s$ está en la rama central, compartida por las dos mallas; la supermalla es el lazo exterior (a trazos) que la evita.*
>
> **Paso 1 — Restricción de la fuente.** Por la rama central, hacia abajo, circulan la corriente de malla $i_a$ (que baja) y $i_b$ (que sube), de modo que la corriente neta hacia abajo es $i_a-i_b$. La fuente la fija:
> $$i_a - i_b = I_s = 1.$$
>
> **Paso 2 — LKV de la supermalla.** Recorremos el **lazo exterior** (a trazos), que toca $V_s$, $R_1$ y $R_3$ pero **no** la rama de la fuente, por lo que su tensión desconocida no entra:
> $$-V_s + R_1\, i_a + R_3\, i_b = 0 \;\Longrightarrow\; 2\,i_a + 2\,i_b = 10 \;\Longrightarrow\; i_a + i_b = 5.$$
>
> **Paso 3 — Resolver el sistema $2\times2$.** Tenemos la restricción y la LKV de la supermalla:
> $$\begin{cases} i_a + i_b = 5 \\ i_a - i_b = 1 \end{cases} \;\Longrightarrow\; i_a = 3\ \text{A},\quad i_b = 2\ \text{A}.$$
>
> > [!solucion]
> > $i_a = 3\ \text{A}$ e $i_b = 2\ \text{A}$. **Comprobación:** la corriente de la rama central (hacia abajo) es $i_a - i_b = 3 - 2 = 1\ \text{A} = I_s$, justo lo que impone la fuente. El truco de la supermalla nos ahorró introducir como incógnita la tensión sobre $I_s$: solo aparecería si más adelante la necesitáramos, y se despejaría de la LKV de una sola malla **a posteriori**.

---

## En qué consiste

> [!teoria] Por qué no sirve la LKV normal y sí el lazo exterior
> Una fuente **ideal de corriente** fija la corriente que la atraviesa, pero la **tensión** en sus bornes la determina el resto del circuito: es una **incógnita más**. Si escribiéramos la LKV de la malla izquierda, en ella aparecería esa tensión desconocida $v_{I_s}$ —una incógnita extra sin ecuación propia que la acompañe—. La **supermalla** esquiva el problema: al recorrer el **contorno exterior** de las dos mallas se evita la rama de la fuente, así que $v_{I_s}$ **nunca aparece** en la ecuación. A cambio se pierde una LKV (las dos mallas dan **una** sola ecuación), pero la fuente devuelve exactamente la que falta: su **ecuación de restricción** $i_a - i_b = I_s$. El balance de ecuaciones queda intacto.

> [!algoritmo] Análisis con supermalla
> **Paso 1 — Detectar la fuente de corriente compartida** por dos mallas (la que está en una rama común a ambas ventanas).
>
> **Paso 2 — Escribir la restricción.** La diferencia de las corrientes de malla que recorren esa rama, en el sentido de la fuente, iguala a $I_s$: $i_{\text{a}} - i_{\text{b}} = I_s$ (con el signo que corresponda al sentido de $I_s$).
>
> **Paso 3 — LKV de la supermalla.** Plantear **una** LKV recorriendo el **contorno exterior** de las dos mallas, sin pasar por la rama de la fuente.
>
> **Paso 4 — Resolver el sistema** formado por la restricción y la LKV de la supermalla (más las LKV del resto de mallas, si las hubiera).
>
> **Caso simple:** si la fuente de corriente está **solo en una malla** (en una rama no compartida), su corriente de malla es **directamente conocida** —vale $\pm I_s$— y esa malla no necesita LKV.

> [!warning]
> No escribas la LKV de una **malla individual que contenga la fuente de corriente**: introducirías la tensión desconocida sobre la fuente como incógnita sin ecuación. Usa la **supermalla** para esas dos mallas. Cuida además el **signo de la restricción**: $i_a - i_b = I_s$ es válido para el sentido de $I_s$ del ejemplo (hacia abajo, coincidiendo con $i_a$ por la rama central); si la fuente apunta al revés, el signo se invierte.

## Resumen

> [!resumen]
> | Aspecto | Supermalla |
> |:---|:---|
> | Cuándo | fuente de corriente $I_s$ en rama compartida por dos mallas |
> | Problema que evita | la tensión $v_{I_s}$ sobre la fuente es incógnita |
> | LKV | una sola, por el **contorno exterior** (evita la fuente) |
> | Ecuación que aporta la fuente | restricción $i_a - i_b = I_s$ |
> | Nº de ecuaciones | igual que sin la fuente (LKV + restricción) |
> | Dual | [[Nodos con Fuentes de Voltaje\| supernodo]] |
>
> En el ejemplo: $i_a + i_b = 5$ (supermalla) e $i_a - i_b = 1$ (restricción) dan $i_a = 3\ \text{A}$, $i_b = 2\ \text{A}$.

> [!corolario]
> La supermalla mantiene **mínimo** el número de ecuaciones también cuando hay fuentes de corriente: cada fuente de corriente compartida cambia **una LKV por una restricción**, más simple. Si la fuente está en una sola malla, todavía mejor: regala una corriente de malla y elimina una ecuación.

> [!referencia]
> Fraile Mora, cap. 1, §1.12. Método base: [[Analisis de Mallas]]. Dual: [[Nodos con Fuentes de Voltaje]]. La condición de la fuente como [[Ecuaciones de Restriccion| ecuación de restricción]]. Índice del tema: [[Metodos de Analisis/index]].
