---
title: Transformador con Núcleo de Aire
tags:
  - circuitos-electricos
  - teoria
  - acoplamiento-magnetico
  - transformador
draft: false
aliases:
  - Transformador de Núcleo de Aire
  - Transformador Real
  - air-core transformer
  - reflected impedance
  - linear transformer
---

# Transformador con Núcleo de Aire

> [!definicion]
> El **transformador con núcleo de aire** (o *transformador lineal*) es un par de bobinas acopladas **reales**, devanadas sobre un soporte **no ferromagnético** (aire, plástico, cerámica), con acoplamiento **parcial** ($k<1$) y **sin** las idealizaciones del [[Transformador Ideal| transformador ideal]] ($k=1$, $L\to\infty$, sin pérdidas). Se analiza directamente con las **ecuaciones del par acoplado** en régimen fasorial, y su efecto sobre el primario se condensa en un único concepto: la **impedancia reflejada**.

> [!info]
> Esta nota presenta el transformador **real** del [[6 Acoplamiento Magnetico/index| capítulo 6]], en contraposición al [[Transformador Ideal| transformador ideal]]. El acoplamiento entre ambos devanados se modela con el término mutuo $j\omega M$ del [[Acoplamiento Magnetico Fasorial| acoplamiento magnético fasorial]], y el grado de acoplo lo mide el [[Coeficiente de Acoplamiento| coeficiente de acoplamiento]] $k$.
>
> Referencia: Fraile Mora, *Circuitos Eléctricos*, cap. 1, §1.19 (transformadores con acoplamiento magnético).

---

## Ejemplo

> [!ejemplo] Impedancia vista desde el primario
> Un transformador de núcleo de aire tiene las reactancias
> $$\omega L_1 = 10\ \Omega, \qquad \omega L_2 = 40\ \Omega, \qquad \omega M = 12\ \Omega,$$
> por lo que su coeficiente de acoplamiento es
> $$k = \frac{\omega M}{\sqrt{\omega L_1\cdot \omega L_2}} = \frac{12}{\sqrt{10\cdot 40}} = \frac{12}{\sqrt{400}} = \frac{12}{20} = 0{,}6 \;<\; 1.$$
> El secundario se cierra sobre una **carga resistiva** $Z_L = 8\ \Omega$. Hallar la impedancia $\overline{Z}_{in}$ vista desde los terminales del primario.

> [!solucion]
> Se aplica directamente la fórmula de la impedancia de entrada del par acoplado (deducida más abajo):
> $$\overline{Z}_{in} = j\omega L_1 + \frac{(\omega M)^2}{j\omega L_2 + Z_L} = j10 + \frac{12^2}{8 + j40} = j10 + \frac{144}{8 + j40}.$$
> Se racionaliza el término reflejado multiplicando por el conjugado del denominador:
> $$\frac{144}{8 + j40} = \frac{144\,(8 - j40)}{8^2 + 40^2} = \frac{144\,(8 - j40)}{64 + 1600} = \frac{144\,(8 - j40)}{1664} \approx 0{,}69 - j3{,}46\ \Omega.$$
> Sumando la reactancia propia del primario $j10$:
> $$\overline{Z}_{in} \approx (0{,}69) + j\,(10 - 3{,}46) = 0{,}69 + j6{,}54\ \Omega.$$
>
> **Interpretación.** La parte real $0{,}69\ \Omega$ es la **resistencia reflejada**: la carga $Z_L$ del secundario, "vista" desde el primario a través del acoplamiento magnético. Es notable que aparezca una parte resistiva en la entrada **aunque el primario sea sin pérdidas** ($\omega L_1$ es reactancia pura); esa resistencia no disipa en el primario, sino que representa la potencia que se transfiere al secundario y se disipa en $Z_L$.

---

## En qué consiste

> [!teoria] El transformador real como par acoplado
> En un transformador de núcleo de aire la permeabilidad del medio es la del vacío, de modo que el flujo magnético **no queda confinado**: una fracción del flujo de cada bobina se cierra por el aire sin enlazar a la otra (**flujo de dispersión**). Por ello el acoplamiento es parcial, $k<1$, y no es lícito tratar la pareja como un transformador ideal. La herramienta correcta es plantear las dos ecuaciones de malla del par acoplado y resolver el circuito como cualquier red fasorial, sin más relaciones especiales que la inductancia mutua $M$.

> [!teorema] Impedancia de entrada e impedancia reflejada
> Sea un transformador con núcleo de aire de inductancias propias $L_1$, $L_2$ e inductancia mutua $M$, con el primario excitado por $\overline{V}_1$ y el secundario cerrado sobre una carga $Z_L$. Las ecuaciones del par acoplado (convención de puntos coherente) son
> $$\overline{V}_1 = j\omega L_1\,\overline{I}_1 + j\omega M\,\overline{I}_2,$$
> $$0 = j\omega M\,\overline{I}_1 + (j\omega L_2 + Z_L)\,\overline{I}_2.$$
> Entonces la **impedancia vista desde el primario** es
> $$\boxed{\;\overline{Z}_{in} = \frac{\overline{V}_1}{\overline{I}_1} = j\omega L_1 + \frac{(\omega M)^2}{j\omega L_2 + Z_L}\;}$$
> donde el segundo sumando
> $$\overline{Z}_{r} = \frac{(\omega M)^2}{j\omega L_2 + Z_L}$$
> es la **impedancia reflejada** (o *acoplada*): la totalidad del secundario —su reactancia propia $j\omega L_2$ más la carga $Z_L$— "aparece" en el primario condensada en un único término.

> [!demostracion]
> Se parte de la segunda ecuación (malla del secundario, sin fuente porque la única excitación está en el primario) y se despeja la corriente secundaria:
> $$0 = j\omega M\,\overline{I}_1 + (j\omega L_2 + Z_L)\,\overline{I}_2 \quad\Longrightarrow\quad \overline{I}_2 = -\frac{j\omega M}{\,j\omega L_2 + Z_L\,}\;\overline{I}_1.$$
> Se sustituye este resultado en la primera ecuación (malla del primario):
> $$\overline{V}_1 = j\omega L_1\,\overline{I}_1 + j\omega M\left(-\frac{j\omega M}{j\omega L_2 + Z_L}\,\overline{I}_1\right) = j\omega L_1\,\overline{I}_1 - \frac{(j\omega M)^2}{j\omega L_2 + Z_L}\,\overline{I}_1.$$
> Como $(j\omega M)^2 = -(\omega M)^2$, el signo negativo de $-(j\omega M)^2$ se vuelve positivo:
> $$\overline{V}_1 = \left[\,j\omega L_1 + \frac{(\omega M)^2}{j\omega L_2 + Z_L}\,\right]\overline{I}_1.$$
> Dividiendo por $\overline{I}_1$ se obtiene $\overline{Z}_{in}$. $\quad\blacksquare$

> [!proposicion] Carácter de la impedancia reflejada
> 1. **Inversión del carácter.** El denominador $j\omega L_2 + Z_L$ es complejo; al invertirlo para formar $\overline{Z}_r = (\omega M)^2/(j\omega L_2 + Z_L)$ se conjuga su argumento. Por ello la impedancia reflejada **invierte el carácter reactivo** del secundario: si el secundario es **inductivo**, refleja **capacitivo** en el primario, y viceversa. (En el ejemplo, la reactancia secundaria $+j40$ se refleja como $-j3{,}46$, contribución capacitiva.)
> 2. **Dependencia del acoplo.** $\overline{Z}_r$ crece con $(\omega M)^2$: cuanto mayor es el acoplamiento (mayor $M$, mayor $k$), **más se nota** la carga del secundario en el primario.
> 3. **Resistencia reflejada sin pérdidas en el primario.** Aunque $j\omega L_1$ sea reactancia pura, $\overline{Z}_r$ aporta una **parte real** a $\overline{Z}_{in}$: es la potencia transferida al secundario, no una disipación del primario.
> 4. **Límite ideal.** Cuando $k\to 1$ y $L_1,L_2\to\infty$ manteniendo $a=\sqrt{L_1/L_2}$, se recupera el [[Transformador Ideal| transformador ideal]] con $\overline{Z}_{in}=a^2\,Z_L$.

---

> [!warning] Precauciones
> - En el transformador **real** siempre $k<1$: existe **flujo de dispersión** que no se acopla entre devanados. **No** se deben usar las relaciones de espiras del ideal ($V_1/V_2 = N_1/N_2$, $Z_{in}=a^2 Z_L$) salvo como **aproximación** válida solo cuando $k\approx 1$.
> - La impedancia reflejada **depende de la frecuencia** (a través de $\omega M$ y de $j\omega L_2$); un transformador de núcleo de aire no presenta la misma $\overline{Z}_{in}$ a distintas $\omega$.
> - Hay que cuidar la **convención de puntos**: un cambio en la orientación relativa de los devanados cambia el signo de $M$, aunque $(\omega M)^2$ —y por tanto $\overline{Z}_r$— no se ve afectado.

---

## Resumen

> [!resumen]
> | Concepto | Expresión | Comentario |
> |---|---|---|
> | Ecuaciones del par | $\overline{V}_1 = j\omega L_1\overline{I}_1 + j\omega M\overline{I}_2$ | malla del primario |
> | | $0 = j\omega M\overline{I}_1 + (j\omega L_2 + Z_L)\overline{I}_2$ | secundario sobre $Z_L$ |
> | Impedancia de entrada | $\overline{Z}_{in} = j\omega L_1 + \dfrac{(\omega M)^2}{\,j\omega L_2 + Z_L\,}$ | vista desde el primario |
> | Impedancia reflejada | $\overline{Z}_{r} = \dfrac{(\omega M)^2}{\,j\omega L_2 + Z_L\,}$ | el secundario "aparece" en el primario |
> | Coeficiente de acoplo | $k = \dfrac{\omega M}{\sqrt{\omega L_1\cdot \omega L_2}} < 1$ | acoplamiento parcial (real) |
> | Límite ideal | $\overline{Z}_{in} = a^2\,Z_L$ | cuando $k\to 1$, $L\to\infty$ |

> [!corolario]
> La utilidad del concepto de impedancia reflejada es **reducir** un circuito con dos mallas acopladas a un **único** circuito de primario equivalente: basta sumar a $j\omega L_1$ el término $\overline{Z}_r$ para tener toda la información del secundario. El transformador de núcleo de aire actúa así como un **transformador de impedancias**, capaz de presentar al primario una impedancia con parte real y reactiva distintas de las de la carga física $Z_L$.

> [!referencia]
> - Fraile Mora, J. *Circuitos Eléctricos*. Cap. 1, §1.19.
> - Notas relacionadas: [[Acoplamiento Magnetico Fasorial]], [[Transformador Ideal]], [[Coeficiente de Acoplamiento]], [[6 Acoplamiento Magnetico/index]].
