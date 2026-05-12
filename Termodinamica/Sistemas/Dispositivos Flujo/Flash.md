---
title: "Flash (Vaporización instantánea)"
tags:
  - termodinamica
  - dispositivos_flujo
  - separacion
  - equilibrio_fases
draft: false
aliases:
  - flash drum
  - vaporizacion instantanea
  - equilibrio
---

# Flash (Vaporización instantánea) $\Delta P \rightarrow \text{Separacion}$

> [!definicion]
> Un proceso de **Flash** es una técnica de separación de una sola etapa donde una corriente líquida a alta presión y temperatura se expande bruscamente (a través de una válvula o tobera) hacia una cámara a menor presión. La drástica caída de presión provoca que una fracción del líquido se **vaporice instantáneamente** o "flashee". En la cámara, llamada **Tambor de Flash**, las dos fases se separan por gravedad: el vapor más ligero sale por la parte superior y el líquido más pesado, por la inferior.

## Hipótesis estándar para análisis

> [!info]
> 1.  **Una entrada, dos salidas:** Una corriente de alimentación ($F$), una corriente de vapor saliente ($V$) y una corriente de líquido saliente ($L$).
> 2.  **Equilibrio Termodinámico:** Las fases de vapor y líquido que abandonan el tambor están en equilibrio entre sí a la **temperatura** ($T_{tambor}$) y **presión** ($P_{tambor}$) del tambor. Es una suposición clave para el diseño.
> 3.  **Adiabático:** El proceso a través de la válvula y en el tambor se considera sin intercambio de calor con el exterior ($Q=0$).
> 4.  **Sin Trabajo de Eje:** No hay dispositivos que realicen o extraigan trabajo ($W=0$).
> 5.  **Sistema en Estado Estacionario:** Las propiedades dentro del tambor y en las corrientes de salida no cambian con el tiempo.

## Ecuaciones de gobierno (Modelo Flash)

> [!teorema]
> El modelo de un flash se rige por tres ecuaciones fundamentales que deben cumplirse simultáneamente.
>
> **1. Balance de Materia Global y por Componente**
>
> *   **Global:** La masa que entra es igual a la que sale.
>     $$F = L + V$$
>
> *   **Por Componente ($i$):** La masa de un componente en la alimentación se divide entre la fase líquida y la fase vapor.
>     $$F z_i = L x_i + V y_i$$
>
> *Donde $z_i$, $x_i$, $y_i$ son las fracciones molares del componente $i$ en la alimentación, el líquido y el vapor, respectivamente.*
>
> **2. Relaciones de Equilibrio de Fases**
>
> Para cada componente en el equilibrio, su fugacidad en la fase líquida y vapor es igual. Una forma común es usando la **ley de Raoult** modificada o coeficientes de distribución ($K_i$):
> $$
> y_i = K_i(T, P, x, y) \cdot x_i
> $$
> Donde $K_i$ no es una constante, sino que depende fuertemente de la temperatura, la presión y la composición de la mezcla. Para mezclas ideales a baja presión, $K_i \approx P_i^{sat}(T)/P$.
>
> **3. Balance de Energía**
>
> Para un flash **adiabático**, la entalpía de la alimentación se reparte entre las corrientes de salida.
> $$
> F \cdot h_F = V \cdot H_V + L \cdot h_L
> $$
> *Donde $h_F$, $H_V$ y $h_L$ son las entalpías específicas de la alimentación, el vapor de salida y el líquido de salida, respectivamente.*

## El Flash como un Dispositivo

> [!ejemplo]
> **Operación de un Tambor de Flash y su uso en el mundo real**
>
> 1.  **Alimentación:** Una corriente líquida caliente y a alta presión entra al sistema.
> 2.  **Válvula de Expansión:** Pasa por una **válvula de estrangulamiento** (como las que ya estudiamos), donde ocurre la caída de presión ($P_2 \ll P_1$). Este proceso es isentálpico ($h = \text{cte.}$).
> 3.  **Formación de Vapor:** La presión cae por debajo de la presión de burbuja del líquido. Para mantener el equilibrio, el líquido debe "hervir" o vaporizarse. La energía para este cambio de fase (el calor latente de vaporización) la extrae del propio líquido, causando un **descenso de temperatura** (efecto auto-refrigerante).
> 4.  **Separación en el Tambor:** La mezcla de dos fases entra a un gran recipiente cilíndrico llamado **Tambor de Flash**. La baja velocidad (debido al gran diámetro) permite que las gotas de líquido más pesadas caigan al fondo por gravedad, mientras que el vapor más ligero asciende. Un **eliminador de niebla** en la salida del vapor ayuda a retener cualquier gota remanente.
> 5.  **Salidas:** Se obtienen dos productos: un **vapor** enriquecido con los componentes más volátiles y un **líquido** residual enriquecido con los componentes menos volátiles.

> [!info]
> **Aplicaciones Comunes**
> *   **Refino de Petróleo y Gas Natural:** Es la etapa básica en la **destilación de crudo**. Un horno calienta el crudo y su presión se reduce drásticamente en una **Torre de Destilación Atmosférica**, que opera como un tambor de flash gigante y multicomponente, separando el crudo en fracciones como gas, nafta, queroseno, etc..
> *   **Plantas de Energía (Ciclo Rankine):** A la salida de la turbina de vapor, el vapor de escape se condensa parcialmente. El **condensador** actúa como un tambor de flash, separando el agua líquida del vapor remanente.
> *   **Desalinización de Agua (MSF):** En las plantas de destilación flash multi-etapa, el agua de mar caliente pasa por varias etapas a presión cada vez más baja, "flasheando" o evaporándose instantáneamente y separándose del agua salada concentrada.
> *   **Plantas Químicas y Petroquímicas:** Se usa como un separador preliminar (simple y económico) antes de enviar una corriente a una columna de destilación más compleja.
> *   **Sistemas de Refrigeración:** Tras la válvula de expansión, el refrigerante líquido se evapora parcialmente en un **separador de líquido** que actúa como un pequeño tambor de flash antes de entrar al evaporador.

## Relaciones con otras notas

> [!info]
> -   [[Valvulas]] (El dispositivo que provoca el "flasheo").
> -   [[Intercambiadores de Calor]] (Se usan para precalentar la alimentación antes del flash).
> -   [[Ciclos de Refrigeracion]] (El proceso de expansión en la válvula es un flash).
> -   [[Mezclas de Gases]] (Fundamental para entender el equilibrio de fases multicomponente).
> -   [[Equilibrio de Fases]] (Tema central para el cálculo de las composiciones de salida).

> [!warning]
> En un examen, el "problema del flash" es clásico. Normalmente se te dan las propiedades de la alimentación y la $P$ (y a veces la $T$) del tambor. Hay que resolver las tres ecuaciones (masa, equilibrio, energía) de forma iterativa, porque $K_i$ y las entalpías dependen de las composiciones y la temperatura. Es un problema de prueba y error.

