---
title: Coeficiente de Acoplamiento
tags:
  - circuitos-electricos
  - teoria
  - acoplamiento-magnetico
draft: false
aliases:
  - Coeficiente de Acoplamiento
  - Factor de Acoplamiento
  - Coupling Coefficient
  - Coefficient of Coupling
---

# Coeficiente de Acoplamiento

> [!definicion]
> El **coeficiente de acoplamiento** $k$ mide qué fracción del flujo magnético producido por una bobina enlaza efectivamente a la otra. Se define como la razón entre la inductancia mutua y la media geométrica de las autoinductancias:
> $$k=\dfrac{M}{\sqrt{L_1 L_2}},\qquad 0\le k\le1.$$
> Es una magnitud **adimensional**. Cuando $k\to0$ las bobinas son casi independientes (acoplamiento **débil**, poco flujo compartido); cuando $k\to1$ se tiene **acoplamiento perfecto**, es decir, todo el flujo de una bobina enlaza a la otra.

> [!info]
> El coeficiente de acoplamiento **cuantifica la intensidad** de la [[Inductancia Mutua| inductancia mutua]] entre dos bobinas, dentro del tema de [[Induccion Magnetica/index| Inducción magnética]] ([[6 Acoplamiento Magnetico/index| capítulo 6]]). Se construye a partir de las [[Autoinduccion| autoinductancias]] $L_1$, $L_2$ y de la mutua $M$. El límite $k\to1$ es precisamente la hipótesis idealizada del [[Transformador Ideal| transformador ideal]].
> Referencia: Fraile Mora, cap. 1 §1.19.

---

## Ejemplo

> [!ejemplo] Cálculo del coeficiente y del acoplamiento máximo
> Dos bobinas acopladas magnéticamente tienen autoinductancias $L_1=2\ \text{H}$ y $L_2=8\ \text{H}$, y su inductancia mutua es $M=3\ \text{H}$.
> Se pide hallar el coeficiente de acoplamiento $k$ y compararlo con el valor máximo posible de la mutua.
>
> > [!solucion]
> > Aplicamos la definición:
> > $$k=\dfrac{M}{\sqrt{L_1 L_2}}=\dfrac{3}{\sqrt{2\cdot 8}}=\dfrac{3}{\sqrt{16}}=\dfrac{3}{4}=0{,}75.$$
> > El resultado $k=0{,}75$ indica un **acoplamiento fuerte pero no perfecto**: tres cuartas partes del flujo se comparten.
> >
> > La inductancia mutua **máxima** compatible con estas bobinas correspondería a $k=1$:
> > $$M_{max}=\sqrt{L_1 L_2}=\sqrt{16}=4\ \text{H}.$$
> > Como $M=3\ \text{H} < M_{max}=4\ \text{H}$, el dato es físicamente admisible. Si se pretendiera $M>4\ \text{H}$ se obtendría $k>1$, lo cual es imposible.
> >
> > **Resultado:** $k=0{,}75$ (acoplamiento fuerte) y $M_{max}=4\ \text{H}$.

---

## En qué consiste

> [!teoria] Por qué $0\le k\le1$
> El acotamiento del coeficiente de acoplamiento no es una convención, sino una **consecuencia física**. La inductancia mutua nunca puede superar la media geométrica de las autoinductancias:
> $$M\le\sqrt{L_1 L_2}.$$
> Esta desigualdad se deduce de exigir que la **energía magnética almacenada** en el sistema de dos bobinas sea siempre no negativa, $W\ge0$, para cualquier par de corrientes. La energía
> $$W=\tfrac{1}{2}L_1 i_1^2 \pm M\,i_1 i_2 + \tfrac{1}{2}L_2 i_2^2$$
> es una forma cuadrática definida no negativa solo si $L_1 L_2 - M^2\ge0$, es decir $M\le\sqrt{L_1 L_2}$, lo que obliga a $k\le1$.
>
> La interpretación energética es directa: $k^2$ representa la **fracción de energía (o de flujo) acoplada** entre ambas bobinas. Valores típicos según el medio magnético:
> - **Núcleo de aire**: $k$ bajo, en torno a $0{,}01$–$0{,}5$.
> - **Núcleo ferromagnético común**: $k$ alto, $0{,}95$–$0{,}999$.
> - **Transformador ideal**: $k=1$ (límite teórico inalcanzable en la práctica).

> [!proposicion] Acoplamiento perfecto y relación de transformación
> Con acoplamiento perfecto ($k=1$) la mutua alcanza su valor máximo, $M=\sqrt{L_1 L_2}$, y todo el flujo es compartido por ambos devanados. En ese caso la relación de transformación de tensiones queda fijada por las autoinductancias:
> $$\dfrac{V_2}{V_1}=\sqrt{\dfrac{L_2}{L_1}}=\dfrac{N_2}{N_1},$$
> ya que en un mismo núcleo la autoinductancia es proporcional al cuadrado del número de espiras, $L\propto N^2$. Esta igualdad es el **puente conceptual** con el [[Transformador Ideal]]: el modelo ideal es el caso límite de acoplamiento perfecto.

> [!warning]
> - El coeficiente $k$ **no tiene unidades** y **nunca** supera $1$. Si un cálculo arroja $k>1$, hay un error: los datos $L_1$, $L_2$ y $M$ son incompatibles entre sí.
> - Un $k$ alto **no significa** que el transformador sea "mejor" en todos los contextos. En algunas aplicaciones —ciertos filtros, antenas o circuitos resonantes acoplados— interesa deliberadamente un **acoplamiento débil**.

---

## Resumen

> [!resumen] Tabla de fórmulas clave
> | Concepto | Expresión | Comentario |
> |---|---|---|
> | Coeficiente de acoplamiento | $k=\dfrac{M}{\sqrt{L_1 L_2}}$ | Adimensional |
> | Rango admisible | $0\le k\le 1$ | Consecuencia de $W\ge0$ |
> | Cota de la mutua | $M\le\sqrt{L_1 L_2}$ | $M_{max}=\sqrt{L_1 L_2}$ |
> | Acoplamiento perfecto | $k=1$ | $M=\sqrt{L_1 L_2}$, base del transformador ideal |
> | Relación de transformación ($k=1$) | $\dfrac{V_2}{V_1}=\sqrt{L_2/L_1}=N_2/N_1$ | $L\propto N^2$ |

> [!corolario]
> El coeficiente de acoplamiento condensa en un solo número la calidad del enlace magnético entre dos bobinas. Separa con claridad tres regímenes: acoplamiento débil ($k\to0$, bobinas casi aisladas), acoplamiento fuerte (núcleo ferromagnético, $k\to0{,}99$) y acoplamiento perfecto ($k=1$, idealización del transformador). Conocido $k$ junto con $L_1$ y $L_2$, queda determinada la mutua $M=k\sqrt{L_1 L_2}$, y con ella toda la dinámica del par acoplado.

> [!referencia]
> Fraile Mora, *Circuitos Eléctricos*, cap. 1 §1.19.
> Notas relacionadas: [[Inductancia Mutua]], [[Autoinduccion]], [[Transformador Ideal]], [[Induccion Magnetica/index| Inducción magnética]].
