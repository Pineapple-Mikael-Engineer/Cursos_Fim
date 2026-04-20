---
title: Inductancia Mutua — Deducción Formal y Fundamento Energético
tags:
  - induccion
  - inductancia_mutua
  - maxwell
  - energia_magnetica
  - potencial_vectorial
draft: true
---

# Inductancia Mutua — Desarrollo Completo

La inductancia mutua no es una definición arbitraria.

Es una consecuencia directa de:

1. La ley de Ampère
2. La ley de Faraday
3. La energía almacenada en el campo magnético
4. El principio de reciprocidad electromagnética

---

# 1) Campo Magnético Producido por una Corriente

Partimos de la ley de Ampère (régimen magnetostático):

$$
\nabla \times \mathbf{B} = \mu_0 \mathbf{J}
$$

La solución general para el campo producido por una distribución de corriente es:

$$
\mathbf{B}(\mathbf{r}) =
\frac{\mu_0}{4\pi}
\int
\frac{\mathbf{J}(\mathbf{r}') \times (\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^3}
\, dV'
$$

o, equivalentemente:

$$
\mathbf{B}(\mathbf{r}) =
\frac{\mu_0}{4\pi}
\int
\frac{\mathbf{J}(\mathbf{r}') \times \hat{\mathbf{R}}}{R^2}
\, dV'
$$

donde:

- $\mathbf{R} = \mathbf{r} - \mathbf{r}'$
- $R = |\mathbf{R}|$
- $\hat{\mathbf{R}} = \mathbf{R}/R$

Este campo ocupa la totalidad del espacio.

---

# 2) Flujo Mutuo como Integral de Campo

Considérese la bobina 1 portando una corriente $I_1$.

El flujo magnético que atraviesa la bobina 2 es:

$$
\Phi_{12} =
\int_{S_2}
\mathbf{B}_1 \cdot d\mathbf{A}
$$

Dado que el sistema es lineal, $\mathbf{B}_1$ es proporcional a $I_1$:

$$
\mathbf{B}_1 = I_1 \, \mathbf{b}_1
$$

donde $\mathbf{b}_1$ es el campo por unidad de corriente. Sustituyendo:

$$
\Phi_{12} = I_1
\int_{S_2}
\mathbf{b}_1 \cdot d\mathbf{A}
$$

Se define entonces la inductancia mutua $M_{12}$ como:

$$
M_{12} \equiv
\int_{S_2}
\mathbf{b}_1 \cdot d\mathbf{A}
$$

Obteniéndose la relación fundamental:

$$
\boxed{
\Phi_{12} = M_{12} I_1
}
$$

Lejos de ser una definición arbitraria, esta expresión es una consecuencia directa de la linealidad de las ecuaciones de Maxwell en régimen magnetostático.

---

# 3) Demostración de la Simetría $M_{12} = M_{21}$

## 3.1) Argumento Energético

Considérese la energía magnética total almacenada en el sistema:

$$
W = \frac{1}{2}
\int_{\mathbb{R}^3}
\mathbf{B} \cdot \mathbf{H}
\, dV
$$

Si existen dos distribuciones de corriente, se tiene:

$$
\mathbf{B} = \mathbf{B}_1 + \mathbf{B}_2
$$
$$
\mathbf{H} = \mathbf{H}_1 + \mathbf{H}_2
$$

Sustituyendo en la expresión de la energía:

$$
W =
\frac{1}{2}
\int
(\mathbf{B}_1 + \mathbf{B}_2)
\cdot
(\mathbf{H}_1 + \mathbf{H}_2)
\, dV
$$

Desarrollando el producto:

$$
W =
\frac{1}{2}
\int
\mathbf{B}_1 \cdot \mathbf{H}_1
\, dV
+
\frac{1}{2}
\int
\mathbf{B}_2 \cdot \mathbf{H}_2
\, dV
+
\frac{1}{2}
\int
\mathbf{B}_1 \cdot \mathbf{H}_2
\, dV
+
\frac{1}{2}
\int
\mathbf{B}_2 \cdot \mathbf{H}_1
\, dV
$$

Para un medio lineal, homogéneo e isótropo, se cumple la relación constitutiva $\mathbf{B} = \mu \mathbf{H}$, con $\mu$ escalar constante. En estas condiciones, los dos primeros términos representan las autoenergías:

$$
\frac{1}{2}L_1 I_1^2
\quad \text{y} \quad
\frac{1}{2}L_2 I_2^2
$$

La energía de interacción $W_m$ es la suma de los dos términos cruzados. Dado que $\mu$ es un escalar que conmuta en el producto, ambas integrales son idénticas:

$$
\int
\mathbf{B}_1 \cdot \mathbf{H}_2
\, dV
=
\int
\mathbf{B}_2 \cdot \mathbf{H}_1
\, dV
$$

Por lo tanto:

$$
W_m =
\int
\mathbf{B}_1 \cdot \mathbf{H}_2
\, dV
$$

Pero esta energía de interacción también debe ser expresable, desde el punto de vista circuital, como:

$$
W_m = M I_1 I_2
$$

Igualando ambas expresiones y aplicando el mismo argumento de simetría a la configuración inversa, se demuestra que:

$$
\boxed{
M_{12} = M_{21}
}
$$

La simetría de la inductancia mutua no es una coincidencia geométrica, sino una consecuencia fundamental de la estructura cuadrática y definida positiva de la energía magnética en un medio lineal y recíproco.

## 3.2) Deducción usando el Potencial Vectorial (Alternativa Elegante)

En magnetostática, el campo magnético se deriva de un potencial vectorial:

$$
\mathbf{B} = \nabla \times \mathbf{A}
$$

El potencial vectorial debido a una distribución de corriente es:

$$
\mathbf{A}(\mathbf{r}) =
\frac{\mu_0}{4\pi}
\int
\frac{\mathbf{J}(\mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|}
\, dV'
$$

El flujo enlazado por la bobina 2 debido a la corriente $I_1$ en la bobina 1 puede expresarse como la circulación del potencial vectorial $\mathbf{A}_1$ a lo largo de la bobina 2:

$$
\Phi_{12} =
\oint_{C_2}
\mathbf{A}_1 \cdot d\mathbf{l}_2
$$

Sustituyendo la expresión integral de $\mathbf{A}_1$ y considerando que la corriente es filamentaria ($\mathbf{J} \, dV' = I_1 \, d\mathbf{l}_1$), se obtiene la fórmula de Neumann:

$$
M_{12} =
\frac{\mu_0}{4\pi}
\oint_{C_2}
\oint_{C_1}
\frac{d\mathbf{l}_1 \cdot d\mathbf{l}_2}{R}
$$

Esta expresión es **completamente simétrica** en los índices 1 y 2, tanto en los diferenciales de línea como en la distancia $R = |\mathbf{r}_1 - \mathbf{r}_2|$. Por lo tanto, sin necesidad de apelar a la energía, se demuestra directamente que:

$$
\boxed{M_{12} = M_{21}}
$$

Esta es una demostración geométrica directa de la reciprocidad.

---

# 4) Separación del Flujo: Mutuo y de Dispersión

El flujo total en la bobina 1 es la superposición del flujo debido a su propia corriente y el debido a la corriente en la bobina 2:

$$
\Phi_1 =
\Phi_{11} + \Phi_{12}
$$

El flujo propio $\Phi_{11}$ puede a su vez descomponerse en:

- $\Phi_{1m}$: flujo que enlaza ambas bobinas (flujo común o mutuo).
- $\Phi_{1d}$: flujo que solo enlaza a la bobina 1 (flujo de dispersión).

$$
\Phi_{11} =
\Phi_{1m} + \Phi_{1d}
$$

Dado que la inductancia propia se define como $L_1 = \Phi_{11}/I_1$, se puede escribir:

$$
L_1 =
L_{1m} + L_{1d}
$$

Análogamente, para la segunda bobina:

$$
L_2 =
L_{2m} + L_{2d}
$$

En un sistema perfectamente acoplado, el flujo común verifica:

$$
M = L_{1m} = L_{2m}
$$

La magnitud de la inductancia de dispersión depende exclusivamente de la geometría del sistema y aumenta cuando las bobinas se separan, no comparten un núcleo de alta permeabilidad o no están correctamente alineadas.

---

# 5) Coeficiente de Acoplamiento

Se define el coeficiente de acoplamiento $k$ como:

$$
k = \frac{M}{\sqrt{L_1 L_2}}
$$

Para demostrar su cota superior, se parte de la condición de energía positiva definida para cualquier par de corrientes $(I_1, I_2)$ no nulas:

$$
W =
\frac{1}{2}L_1 I_1^2
+
\frac{1}{2}L_2 I_2^2
+
M I_1 I_2
> 0
$$

Esta expresión puede reescribirse como una forma cuadrática. Para que sea siempre positiva, su discriminante debe ser negativo, lo que impone la condición:

$$
M^2 < L_1 L_2
$$

o, en el caso límite de energía nula para una combinación particular de corrientes (acoplamiento máximo):

$$
|M| = \sqrt{L_1 L_2}
$$

Combinando ambas posibilidades, se obtiene:

$$
|M| \le \sqrt{L_1 L_2}
$$

Y, por lo tanto:

$$
0 \le |k| \le 1
$$

La condición $M^2 \le L_1 L_2$ es equivalente a exigir que la **matriz de inductancias** sea **definida positiva**, un concepto fundamental en álgebra lineal y en la teoría de sistemas.

El límite superior $k=1$ se alcanza en el caso ideal sin flujo de dispersión, donde todo el campo producido por una bobina enlaza a la otra. Esta es la situación idealizada del transformador perfecto.

---

# 6) Ecuaciones Diferenciales del Sistema

Aplicando la ley de Faraday a cada bobina:

$$
v_1 = \frac{d\Phi_1}{dt}
$$

$$
v_2 = \frac{d\Phi_2}{dt}
$$

Sustituyendo las expresiones de los flujos totales en función de las inductancias:

$$
\Phi_1 = L_1 I_1 + M I_2
$$

$$
\Phi_2 = L_2 I_2 + M I_1
$$

Se obtienen las ecuaciones diferenciales que gobiernan el sistema:

$$
\boxed{
v_1 =
L_1 \frac{dI_1}{dt}
+
M \frac{dI_2}{dt}
}
$$
$$
\boxed{
v_2 =
L_2 \frac{dI_2}{dt}
+
M \frac{dI_1}{dt}
}
$$

![[acoplamiento-1.svg]]

La simetría de estas ecuaciones refleja directamente la simetría $M_{12} = M_{21}$ deducida anteriormente.

---

# 7) Interpretación en Términos de la Matriz de Inductancias

Todo el sistema de dos bobinas puede describirse de forma compacta mediante una matriz de inductancias $\mathbf{L}$:

$$
\mathbf{L} =
\begin{pmatrix}
L_1 & M \\
M & L_2
\end{pmatrix}
$$

Esta matriz posee propiedades fundamentales que emanan de la física subyacente:

- **Simétrica:** $L_{12} = L_{21}$, como se ha demostrado.
- **Definida positiva:** Para cualquier vector de corrientes no nulo $\mathbf{I} = (I_1, I_2)^T$, la energía $W = \frac{1}{2} \mathbf{I}^T \mathbf{L} \mathbf{I} > 0$. Esto impone las condiciones $L_1>0$, $L_2>0$ y $L_1 L_2 > M^2$, que ya conocemos.
- Es una consecuencia directa de la energía magnética, que es una forma cuadrática de las corrientes.

Esta formulación matricial no es solo una notación elegante; es la puerta de entrada al análisis de sistemas multipuerta, a la teoría de redes y al estudio de modos propios de oscilación en circuitos acoplados.

---

# 8) Interpretación Física Profunda

La inductancia mutua no es una propiedad intrínseca de los conductores o "entre cables". Es una propiedad del campo magnético en el espacio que los rodea.

Las bobinas no son más que delimitaciones geométricas que nos permiten cuantificar el flujo de este campo. La energía magnética no se almacena en el cobre, sino que está distribuida en todo el volumen del espacio donde la densidad de energía $u = \frac{1}{2} \mathbf{B} \cdot \mathbf{H}$ es no nula.

La inductancia mutua emerge, por tanto, de la interacción energética de los campos generados por distintas fuentes en una región común del espacio.

---

# Resultado Final

La inductancia mutua surge inevitablemente de:

- La linealidad de las ecuaciones de Maxwell en medios lineales.
- El principio de conservación de la energía.
- La estructura cuadrática de la energía magnética.
- El principio de reciprocidad, implícito en la simetría de las interacciones y demostrable tanto por la energía como por la geometría del potencial vectorial.

No es una definición arbitraria ni un mero artificio matemático.
Es una consecuencia estructural profunda del electromagnetismo clásico.