---
title: Máxima Transferencia de Potencia
tags:
  - circuitos-electricos
  - teoria
  - teoremas
  - potencia
draft: false
aliases:
  - máxima transferencia de potencia
  - adaptación de impedancias
  - maximum power transfer
---

# Máxima Transferencia de Potencia

> [!definicion]
> Una fuente real —o, equivalentemente, el [[Teorema de Thevenin| equivalente de Thévenin]] ($V_{Th}$ en serie con $R_{Th}$)— entrega la **máxima potencia** a una carga $R_L$ cuando
> $$R_L = R_{Th}.$$
> En ese punto la potencia transferida vale
> $$P_{max} = \frac{V_{Th}^2}{4R_{Th}},$$
> y el **rendimiento es del 50 %**: la mitad de la potencia generada se disipa en $R_{Th}$ y la otra mitad llega a la carga.

> [!info]
> Aplicación directa del [[Teorema de Thevenin]] dentro de [[Teoremas/index| Teoremas de circuitos]] ([[2 Metodos de Analisis y Teoremas/index| capítulo 2]]). Su dual se formula sobre el [[Teorema de Norton]]. Fraile Mora, cap. 1, §1.14 (transferencia máxima de potencia). En régimen sinusoidal el criterio se generaliza a $Z_L = Z_{Th}^{*}$ (impedancia conjugada); ver [[5 Circuitos AC Sinusoidal y Fasores/index| circuitos en AC]].

---

## Ejemplo

> [!ejemplo]
> **Carga que recibe máxima potencia de un equivalente de Thévenin.**
>
> Una red lineal, vista desde sus terminales, se reduce a su equivalente de Thévenin $V_{Th} = 8\ \text{V}$, $R_{Th} = 4\ \Omega$. Se conecta una carga **variable** $R_L$. Hallar el valor de $R_L$ que recibe la máxima potencia y dicha potencia.
>
> ![[max_transferencia.svg|620]]
>
> *La potencia en la carga $P_L(R_L)$ tiene un máximo en $R_L = R_{Th} = 4\ \Omega$, donde $P_{max} = 4\ \text{W}$.*
>
> **Paso 1 — Corriente de malla.** Con $R_{Th}$ y $R_L$ en serie, la corriente que entrega el equivalente es
> $$i_L = \frac{V_{Th}}{R_{Th}+R_L} = \frac{8}{4+R_L}.$$
>
> **Paso 2 — Potencia en la carga.** Por ser $P_L = R_L\,i_L^2$,
> $$P_L(R_L) = \frac{V_{Th}^2\,R_L}{(R_{Th}+R_L)^2} = \frac{64\,R_L}{(4+R_L)^2}.$$
>
> **Paso 3 — Condición de máximo.** $P_L$ se maximiza en $R_L = R_{Th} = 4\ \Omega$ (deducción en la demostración). Sustituyendo,
> $$P_{max} = \frac{V_{Th}^2}{4R_{Th}} = \frac{8^2}{4\cdot 4} = \frac{64}{16} = 4\ \text{W}.$$
>
> > [!solucion]
> > $R_L = 4\ \Omega$, $P_{max} = 4\ \text{W}$. La corriente es $i_L = 8/8 = 1\ \text{A}$; la resistencia interna $R_{Th}$ disipa $R_{Th}\,i_L^2 = 4\ \text{W}$, idéntica a la de la carga, de modo que el **rendimiento** es $\eta = 50\,\%$.

---

## En qué consiste

> [!teoria] Por qué existe un óptimo
> El reparto de la potencia generada entre $R_{Th}$ y $R_L$ enfrenta dos efectos opuestos. Con $R_L$ **muy pequeña** la corriente es grande pero casi toda la caída de tensión ocurre en $R_{Th}$, y $P_L = R_L i_L^2 \to 0$. Con $R_L$ **muy grande** la tensión se transfiere a la carga pero la corriente $i_L \to 0$, y de nuevo $P_L \to 0$. Entre ambos extremos $P_L(R_L)$ crece y luego decrece: existe un único máximo, que se alcanza cuando la carga **iguala** la resistencia interna de la fuente. Esta condición es la **adaptación** (matching).

> [!teorema] Condición de máxima transferencia
> Para una fuente de Thévenin fija ($V_{Th}$, $R_{Th}$ dados) y carga resistiva variable $R_L$, la potencia $P_L = \dfrac{V_{Th}^2 R_L}{(R_{Th}+R_L)^2}$ es máxima si y solo si $R_L = R_{Th}$, y entonces $P_{max} = \dfrac{V_{Th}^2}{4R_{Th}}$.

> [!demostracion]
> **Paso 1 — Función a maximizar.** Con $V_{Th}$ y $R_{Th}$ constantes, $P_L$ depende solo de $R_L$:
> $$P_L(R_L) = \frac{V_{Th}^2\,R_L}{(R_{Th}+R_L)^2}.$$
>
> **Paso 2 — Derivar respecto a $R_L$.** Aplicando la regla del cociente,
> $$\frac{dP_L}{dR_L}
> = V_{Th}^2\,\frac{(R_{Th}+R_L)^2 - R_L\cdot 2(R_{Th}+R_L)}{(R_{Th}+R_L)^4}
> = V_{Th}^2\,\frac{R_{Th}-R_L}{(R_{Th}+R_L)^3}.$$
>
> **Paso 3 — Punto crítico.** El denominador es positivo para $R_L>0$, así que la derivada se anula únicamente cuando $R_{Th}-R_L = 0$, es decir $R_L = R_{Th}$. Como $dP_L/dR_L>0$ para $R_L<R_{Th}$ y $dP_L/dR_L<0$ para $R_L>R_{Th}$, el punto crítico es un **máximo**.
>
> **Paso 4 — Valor máximo.** Sustituyendo $R_L = R_{Th}$:
> $$P_{max} = \frac{V_{Th}^2\,R_{Th}}{(2R_{Th})^2} = \frac{V_{Th}^2\,R_{Th}}{4R_{Th}^2}
> = \frac{V_{Th}^2}{4R_{Th}}. \qquad \blacksquare$$

> [!algoritmo] Cómo aplicar el teorema
> **Paso 1 —** Hallar el [[Teorema de Thevenin| equivalente de Thévenin]] ($V_{Th}$, $R_{Th}$) visto desde los terminales de la carga.
>
> **Paso 2 —** Igualar la carga a la resistencia interna: $R_L = R_{Th}$.
>
> **Paso 3 —** Evaluar la potencia máxima entregada: $P_{max} = \dfrac{V_{Th}^2}{4R_{Th}}$.

> [!warning]
> Máxima **transferencia** de potencia **no** es máxima **eficiencia**: en el punto adaptado el rendimiento es solo del $50\,\%$, porque $R_{Th}$ disipa tanto como la carga. En **sistemas de potencia** (distribución eléctrica) interesa lo contrario, $R_L \gg R_{Th}$, para que casi toda la energía llegue a la carga con alta eficiencia. La adaptación $R_L = R_{Th}$ es propia de **electrónica y procesamiento de señal** (antenas, líneas, amplificadores), donde lo escaso es la potencia disponible de la fuente, no la eficiencia.

## Resumen

> [!resumen]
> | Magnitud | Expresión |
> |:---|:---|
> | Condición de máximo | $R_L = R_{Th}$ |
> | Corriente en el óptimo | $i_L = \dfrac{V_{Th}}{2R_{Th}}$ |
> | Potencia máxima | $P_{max} = \dfrac{V_{Th}^2}{4R_{Th}}$ |
> | Rendimiento en el óptimo | $\eta = 50\,\%$ |
> | Generalización en AC | $Z_L = Z_{Th}^{*}$ |

> [!corolario]
> El teorema reduce el diseño de la carga óptima a un solo dato del circuito: $R_{Th}$. Una vez conocido el [[Teorema de Thevenin| equivalente de Thévenin]], no hace falta reanalizar la red para cada carga; basta igualar $R_L = R_{Th}$ y evaluar $P_{max}$.

> [!referencia]
> Fraile Mora, cap. 1, §1.14. Base teórica: [[Teorema de Thevenin]]. Dual: [[Teorema de Norton]]. Contexto: [[Teoremas/index| Teoremas de circuitos]].
