---
title: "Gas real"
tags:
  - termodinamica
  - propiedades
  - ecuaciones_de_estado
  - gas_real
draft: false
aliases:
  - real gas
  - van der Waals
  - factor de compresibilidad
  - Z
---

# Gas real

> [!definicion]
> Sustancia gaseosa cuyo comportamiento se aparta del [[Gas Ideal]] por las **fuerzas atractivas intermoleculares** y el **volumen propio** de las moléculas. El apartamiento se cuantifica con el factor de compresibilidad:
> $$
> Z = \frac{Pv}{RT}, \qquad Z = 1 \text{ (ideal)}, \quad Z \ne 1 \text{ (real)}
> $$

## Ecuación de van der Waals

> [!teorema]
> La ecuación cúbica prototipo (forma molar):
> $$
> \left(P + \frac{a}{\bar v^{\,2}}\right)(\bar v - b) = R_u T
> $$
> - $a/\bar v^{\,2}$: presión interna por atracción molecular.
> - $b$: covolumen, volumen excluido por las moléculas.
>
> Las constantes se fijan imponiendo el punto crítico como punto de inflexión, $\left(\partial P/\partial \bar v\right)_{T_c} = \left(\partial^2 P/\partial \bar v^{\,2}\right)_{T_c} = 0$:
> $$
> a = \frac{27 R_u^2 T_c^2}{64 P_c}, \qquad b = \frac{R_u T_c}{8 P_c}
> $$

## Consecuencias sobre las propiedades

> [!proposicion]
> A diferencia del [[Gas Ideal]], en un gas real la [[Energia Interna]] depende del volumen. De la ecuación térmica de la energía (ver [[Maxwell]] y [[TdS]]):
> $$
> \left(\frac{\partial \bar u}{\partial \bar v}\right)_T = T\left(\frac{\partial P}{\partial T}\right)_{\bar v} - P = \frac{a}{\bar v^{\,2}} \;>\; 0
> $$
> El cálculo completo de $\Delta \bar u$, $\Delta \bar s$ y $c_p - c_v$ para van der Waals se desarrolla en [[Problema 04]].

## Factor de compresibilidad y estados correspondientes

> [!info]
> En términos reducidos $P_r = P/P_c$, $T_r = T/T_c$, el **principio de estados correspondientes** afirma que $Z \approx Z(P_r, T_r)$ es casi universal para gases no polares, lo que da las cartas de compresibilidad generalizadas. Tendencias:
> - $T_r$ alta o $P_r \to 0$: $Z \to 1$ (comportamiento ideal).
> - $P_r$ moderada, $T_r$ baja: $Z < 1$ (dominan las atracciones).
> - $P_r$ alta: $Z > 1$ (domina el covolumen).

## Ecuaciones de estado mejoradas

> [!info]
> Refinan van der Waals con mejor ajuste cerca del punto crítico y en fase líquida:
> - Redlich–Kwong y Soave–Redlich–Kwong (SRK),
> - Peng–Robinson (PR), estándar en ingeniería de procesos.
>
> Todas comparten la estructura "repulsión (covolumen) + atracción" y se reducen al [[Gas Ideal]] en el límite $P \to 0$.

## Relación con otras notas

> [!info]
> - Caso general de la [[Ecuaciones de Estado/index | ecuación de estado]]; límite ideal en [[Gas Ideal]].
> - Aplicación de propiedades: [[Problema 04]] (van der Waals con [[Maxwell]] y [[TdS]]).
> - Relevante cerca de la saturación y del punto crítico, donde el modelo ideal falla.

> [!info]
> **Convención de notación**:
> - $Z = Pv/RT$: factor de compresibilidad; $P_r$, $T_r$: reducidas; subíndice $c$: crítico.
> - $a$, $b$: constantes de van der Waals; barra: magnitudes molares; $R_u$: constante universal.
