---
title: Consistencia, Estabilidad y Convergencia (Teorema de Lax)
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-frontera
  - diferencias-finitas
  - convergencia
draft: false
aliases:
  - Teorema de Lax
  - Equivalencia de Lax
  - Consistencia estabilidad convergencia
  - Lax equivalence theorem
---

# Consistencia, Estabilidad y Convergencia (Teorema de Lax)

> [!definicion]
> Las tres propiedades que definen un buen esquema de [[Metodo Diferencias Finitas/index|diferencias finitas]]:
> - **Consistencia:** el esquema discreto aproxima la EDO continua; su **error de truncamiento local** $\tau_h \to 0$ cuando $h\to0$.
> - **Estabilidad:** la solución discreta no se amplifica sin control; el operador discreto inverso está **uniformemente acotado**.
> - **Convergencia:** la solución discreta $\mathbf y_h$ tiende a la exacta $y$ cuando $h\to0$.

> [!info]
> El **teorema de equivalencia de Lax** las une: para un problema lineal bien planteado, **consistencia + estabilidad ⟺ convergencia**. Es el resultado central que justifica todo el método: basta verificar dos propiedades locales/algebraicas para garantizar la convergencia global.

---

## Teorema de equivalencia de Lax

> [!teorema]
> Para un esquema de diferencias finitas **lineal** y **consistente** aplicado a un problema lineal bien planteado:
> $$\text{estabilidad} \;\Longleftrightarrow\; \text{convergencia}.$$
> Más precisamente, si el error de truncamiento es $\tau_h = O(h^p)$ (consistencia de orden $p$) y el esquema es estable ($\|A_h^{-1}\| \leq C$ uniformemente), entonces el error global es $\|\mathbf y_h - y\| = O(h^p)$.

> [!demostracion]
> Sea $A_h\mathbf y_h = \mathbf b_h$ el sistema discreto y $\mathbf y^*$ la restricción de la solución exacta a la malla. Por consistencia, $\mathbf y^*$ satisface el sistema salvo el truncamiento: $A_h\mathbf y^* = \mathbf b_h + \boldsymbol\tau_h$ con $\|\boldsymbol\tau_h\| = O(h^p)$. Restando,
> $$A_h(\mathbf y^* - \mathbf y_h) = \boldsymbol\tau_h \;\Rightarrow\; \mathbf y^* - \mathbf y_h = A_h^{-1}\boldsymbol\tau_h.$$
> Por estabilidad $\|A_h^{-1}\| \leq C$, de modo que
> $$\|\mathbf y^* - \mathbf y_h\| \leq \|A_h^{-1}\|\,\|\boldsymbol\tau_h\| \leq C\,O(h^p) = O(h^p).$$
> La convergencia (y su orden) se hereda directamente del truncamiento, **amplificado** por la cota de estabilidad. $\blacksquare$

> [!info]
> Es la versión "PVF" de la relación [[Error Local Truncamiento vs Error Global Acumulado|error local → error global]] del PVI: la consistencia da el error local, la estabilidad controla su propagación, y juntas dan convergencia. La cota $\|A_h^{-1}\|$ es el análogo discreto del [[Condicionamiento Numerico Numero Condicion|número de condición]].

---

## Consistencia: orden del esquema

> [!teorema]
> El error de truncamiento local del esquema centrado para $y''$ es
> $$\tau_i = \frac{y(x_{i-1}) - 2y(x_i) + y(x_{i+1})}{h^2} - y''(x_i) = \frac{h^2}{12}y^{(4)}(\xi_i) = O(h^2).$$
> El esquema es **consistente de orden 2**: $\tau_h\to0$ como $h^2$. Sin consistencia, el esquema no aproxima la ecuación correcta.

---

## Estabilidad: cota uniforme del inverso

> [!teorema]
> El esquema es **estable** si $\|A_h^{-1}\| \leq C$ **independiente de $h$**. Para el operador $-y''$ con condiciones Dirichlet, la matriz $A_h$ es [[Teorema Diagonal Dominante Estricta|diagonal dominante]] / simétrica definida positiva, y se prueba $\|A_h^{-1}\|_\infty \leq \frac{(b-a)^2}{8}$, acotado uniformemente. Luego es estable.

> [!warning]
> **La estabilidad puede fallar.** Si la cota $\|A_h^{-1}\|$ **crece** al refinar (por ejemplo, en problemas con autovalores cercanos a cero, o esquemas mal diseñados), el esquema es inestable: refinar la malla **no** mejora —o empeora— la solución, aunque sea consistente. Consistencia sola no basta; por eso el teorema de Lax exige ambas.

---

## Ejemplo: verificación del orden

> [!ejemplo]
> **$-y''=\pi^2\sin(\pi x)$, $y(0)=y(1)=0$** (exacta $y=\sin(\pi x)$). Error máximo al halvar $h$:
>
> | $N$ | $h$ | error máximo | factor |
> |:---:|:---:|:---:|:---:|
> | 4 | 0.250 | $3.2\times10^{-2}$ | — |
> | 8 | 0.125 | $8.1\times10^{-3}$ | 4.0 |
> | 16 | 0.0625 | $2.0\times10^{-3}$ | 4.0 |
>
> El error baja como $O(h^2)$ (factor 4 al halvar $h$), confirmando consistencia orden 2 + estabilidad ⟹ convergencia orden 2, exactamente lo que predice Lax.

---

## El teorema de Lax en EDPs

> [!info]
> El teorema de equivalencia de Lax es aún **más** central en EDPs de evolución (calor, ondas), donde la estabilidad impone condiciones sobre la relación entre paso temporal y espacial (condición CFL). En PVF (1D estacionario) la estabilidad suele venir gratis por la diagonal dominancia, pero el principio es idéntico y fundamental.

---

## Relación con otras notas

> [!info]
> - El truncamiento centrado que da la consistencia: [[Discretizacion Dominio y Aproximacion Centrada]].
> - La matriz cuya cota inversa da la estabilidad: [[Construccion Sistema Tridiagonal Lineal]] y [[Teorema Diagonal Dominante Estricta]].
> - El análogo en PVI: [[Error Local Truncamiento vs Error Global Acumulado]] y [[Regiones Estabilidad Absoluta A Estabilidad]].
> - La cota de estabilidad como condicionamiento: [[Condicionamiento Numerico Numero Condicion]].

---

## Resumen

| Propiedad | Significado | Cómo se verifica |
|:---|:---|:---|
| Consistencia | $\tau_h \to 0$ | truncamiento de Taylor, $O(h^p)$ |
| Estabilidad | $\|A_h^{-1}\| \leq C$ uniforme | diagonal dominancia / SDP |
| Convergencia | $\|\mathbf y_h - y\| \to 0$ | **Lax**: consistencia + estabilidad |
| Cota de error | $O(h^p)$ | $\|A_h^{-1}\|\,\|\tau_h\|$ |

> [!corolario]
> El teorema de equivalencia de Lax establece que, para esquemas lineales sobre problemas bien planteados, **consistencia + estabilidad ⟺ convergencia**: la consistencia ($\tau_h=O(h^p)$, vía truncamiento de Taylor) da el error local, la estabilidad ($\|A_h^{-1}\|\leq C$ uniforme, vía [[Teorema Diagonal Dominante Estricta|diagonal dominancia]]) controla su amplificación, y juntas garantizan error global $O(h^p)$. Es la versión PVF de la relación [[Error Local Truncamiento vs Error Global Acumulado|local→global]] del PVI y el fundamento teórico de las diferencias finitas, decisivo además en EDPs vía la condición CFL.
