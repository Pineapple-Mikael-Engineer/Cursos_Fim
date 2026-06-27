---
title: Mezclas Termodinámicas
order: 3
tags:
  - termodinamica
  - mezclas
  - index
draft: false
aliases:
  - Mezclas
  - Mezclas Termodinámicas
---

# Mezclas Termodinámicas

> [!definicion]
> Una **mezcla** es un sistema termodinámico formado por dos o más sustancias puras. La novedad respecto a una sustancia pura es que el **estado ya no queda fijado solo por $T$ y $P$**: se necesita además la **composición** (fracciones molares o másicas de cada componente). Esto obliga a generalizar todos los balances de masa y energía.
>
> *¿Por qué importa?* El aire que respiras es una mezcla de N₂, O₂, Ar y vapor de agua. El gas natural que alimenta una caldera es una mezcla de metano, etano y propano. La llama de una vela es el resultado de la reacción de una mezcla combustible-oxidante. Comprender mezclas es comprender casi todo lo que ocurre en ingeniería térmica real.
>
> La sección se divide en tres ramas según el tipo de mezcla:
> - **No reactivas (gases ideales):** la composición no cambia; se usa la regla de Dalton.
> - **Aire húmedo (psicrometría):** mezcla de aire seco y vapor de agua; el vapor puede condensar.
> - **Reactivas (combustión):** la composición cambia por la reacción; se necesitan entalpías de formación.

![[mezclas_clasificacion.svg|460]]
*Clasificación de las mezclas estudiadas en esta sección. Las no reactivas se tratan con la ley de Dalton; el aire húmedo es el caso especial de interés en climatización y meteorología; las reactivas requieren química de la combustión.*

---

## Principio unificador: aditividad de extensivas

> [!teorema]
> Para cualquier mezcla de gases ideales, las propiedades extensivas específicas se obtienen sumando las contribuciones de cada componente ponderadas por su fracción:
> $$u_{\rm mezcla} = \sum_i y_i\,u_i(T), \qquad h_{\rm mezcla} = \sum_i y_i\,h_i(T).$$
>
> La **entropía** es la excepción: depende de la presión **parcial** de cada componente ($P_i = y_i P$), no de la presión total. Por eso la mezcla de dos gases distintos siempre genera entropía, incluso si todo ocurre adiabáticamente (paradoja de Gibbs):
> $$\Delta s_{\rm mezcla} = -R_u\sum_i y_i\ln y_i > 0.$$

---

## Composición de la mezcla

> [!proposicion]
> Dos formas equivalentes de especificar la composición:
>
> **Fracción molar:** $y_i = n_i / \sum_k n_k$, con $\sum_i y_i = 1$.
>
> **Fracción másica:** $fm_i = m_i / \sum_k m_k$, con $\sum_i fm_i = 1$.
>
> **Masa molecular aparente** (necesaria para pasar de base molar a base másica):
> $$M = \sum_i y_i M_i \quad [\mathrm{kg/kmol}].$$
>
> *Dato clave:* el análisis volumétrico de un gas (cromatografía, método de Orsat) entrega directamente las **fracciones molares**, porque para gases ideales la fracción volumétrica coincide con la molar ($V_i/V = y_i$).

---

## Mapa de notas

> [!info]
> - [[Mezclas de Gases]] — modelos de Dalton y Amagat; entropía de mezcla; propiedades $u$, $h$, $s$; ejemplo con gas de síntesis.
> - [[Psicrometria/index \| Psicrometría]] — aire húmedo: razón de humedad $\omega$, humedad relativa $\phi$, temperatura de rocío $T_d$, entalpía del aire húmedo.
> - [[Psicrometria/Carta Psicrometrica \| Carta Psicrométrica]] — lectura del diagrama; las cinco familias de curvas.
> - [[Psicrometria/Procesos Psicrometricos \| Procesos Psicrométricos]] — calentamiento, enfriamiento, humidificación, deshumidificación, mezcla de corrientes.
> - [[Psicrometria/Torres de Enfriamiento \| Torres de Enfriamiento]] — contacto directo aire–agua; balances de masa y energía; agua de maquillaje.
> - [[Combustion/index \| Combustión]] — estequiometría, relación aire-combustible, poder calorífico PCS/PCI.
> - [[Combustion/Combustion Incompleta \| Combustión Incompleta]] — mezcla rica; análisis de Orsat; pérdida por CO.
> - [[Combustion/Temperatura Adiabatica de Llama \| Temperatura Adiabática de Llama]] — balance entálpico; $T_{\rm AFT}$; efecto del exceso de aire.

> [!referencia]
> Borgnakke & Sonntag, caps. 12–13; Çengel & Boles, caps. 13–15; Moran & Shapiro, caps. 12–13.
