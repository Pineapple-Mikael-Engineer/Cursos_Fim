---
title: Aplicaciones Fraccionarias
tags:
  - ecuaciones
  - difero-integrales
  - teoria
  - calculo-fraccionario
  - aplicaciones
draft: false
aliases:
  - aplicaciones fraccionarias
  - aplicaciones del cálculo fraccionario
  - difusión anómala
  - fractional calculus applications
---

# Aplicaciones del Cálculo Fraccionario

> [!definicion]
> Las **aplicaciones fraccionarias** son los fenómenos físicos que el cálculo de orden fraccionario
> modela **mejor que el de orden entero** porque el orden $\alpha$ captura la **memoria** y la
> **no-localidad** del sistema. Los cuatro pilares son: **difusión anómala** (transporte que no escala
> como $t$), **viscoelasticidad** (materiales entre sólido y fluido), **control de orden fraccionario**
> y **relajación dieléctrica**. En todos ellos $\alpha$ deja de ser un truco matemático y se vuelve un
> **parámetro físico medible**.

> [!info]
> Esta nota vive en [[Calculo Fraccionario/index| Cálculo Fraccionario]], dentro del capítulo
> [[4 Ecuaciones Difero-integrales/index| Ecuaciones Difero-integrales]]. Es la cara **aplicada** de la
> teoría: las ecuaciones de aquí son [[Ecuaciones Diferenciales Fraccionarias| EDF]] cuyas soluciones
> son [[Funcion de Mittag-Leffler| funciones de Mittag-Leffler]], y todas comparten el mismo motor
> conceptual: los [[Ecuaciones con Memoria| sistemas con memoria]]. Para el caso límite entero, compare
> con la [[Ecuacion del Calor/index| ecuación del calor]] clásica.

---

## Ejemplo

> [!ejemplo] Difusión anómala: el exponente es $\alpha$
> ![[difusion_anomala.svg|470]]
>
> Desplazamiento cuadrático medio $\langle x^2\rangle\sim t^{\alpha}$ (escala log-log, la pendiente es
> $\alpha$): **subdifusión** ($\alpha<1$, partículas atrapadas), **difusión normal** ($\alpha=1$,
> browniana) y **superdifusión** ($\alpha>1$, vuelos de Lévy).

La **difusión anómala** es la aplicación central. La difusión clásica obedece la
[[Ecuacion del Calor/index| ecuación del calor]] $\partial_t u=K\,\partial_x^2 u$ y predice un
desplazamiento cuadrático medio **lineal** en el tiempo, $\langle x^2\rangle\sim t$. Pero en medios
desordenados —geles, fluidos abarrotados, medios porosos, el interior de una célula— las partículas
quedan **atrapadas** durante tiempos largos, o por el contrario dan **saltos enormes** ocasionales. El
escalado deja de ser lineal y aparece la **ecuación de difusión fraccionaria en el tiempo**:
$$\frac{\partial^{\alpha}u}{\partial t^{\alpha}}=K\,\frac{\partial^{2}u}{\partial x^{2}},\qquad 0<\alpha\le1,$$
cuya consecuencia medible es
$$\boxed{\;\langle x^{2}(t)\rangle\sim t^{\alpha}\;}$$
en lugar del clásico $\sim t$. El exponente $\alpha$ **es** el dato del experimento: se lee como la
pendiente de la recta en el gráfico log-log de la figura.

> [!info] Regímenes de transporte según $\alpha$
> | Régimen | Orden | Escalado | Física |
> |---|---|---|---|
> | Subdifusión | $0<\alpha<1$ | $\langle x^2\rangle\sim t^{\alpha}$ (lento) | partículas atrapadas, trampas |
> | Difusión normal | $\alpha=1$ | $\langle x^2\rangle\sim t$ | movimiento browniano |
> | Superdifusión | $\alpha>1$ | $\langle x^2\rangle\sim t^{\alpha}$ (rápido) | vuelos de Lévy, turbulencia |

---

## En qué consiste

> [!teoria] Viscoelasticidad: el springpot
> La materia real no es ni un **resorte** perfecto (sólido elástico de Hooke, $\sigma=E\varepsilon$, que
> guarda toda la energía) ni un **amortiguador** perfecto (fluido de Newton, $\sigma=\eta\dot\varepsilon$,
> que la disipa toda): los polímeros, tejidos y geles están **en medio**. El cálculo fraccionario lo
> captura con un único elemento, el **springpot**:
> $$\sigma(t)=E\,D^{\alpha}\varepsilon(t),\qquad 0\le\alpha\le1,$$
> que **interpola** entre ambos extremos:
> - en $\alpha=0$ es el **resorte de Hooke** $\sigma=E\varepsilon$ (sólido elástico);
> - en $\alpha=1$ es el **amortiguador de Newton** $\sigma=E\dot\varepsilon$ (fluido viscoso);
> - para $0<\alpha<1$ es un material **viscoelástico** cuya **relajación de esfuerzos** sigue una
>   [[Funcion de Mittag-Leffler| función de Mittag-Leffler]], es decir, una **ley de potencias**
>   $\sigma(t)\sim t^{-\alpha}$ —exactamente lo que se mide en el laboratorio— y no la exponencial que
>   predicen los modelos clásicos de Maxwell o Kelvin-Voigt (ver [[Ecuaciones con Memoria]]).
>
> Un solo parámetro $\alpha$ reemplaza así a las cadenas infinitas de resortes y amortiguadores que se
> necesitaban para ajustar una ley de potencias con elementos enteros.

> [!info] Más aplicaciones
> - **Control de orden fraccionario** $\mathrm{PI}^{\lambda}\mathrm{D}^{\mu}$: el PID clásico se
>   generaliza permitiendo orden de integración $\lambda$ y de derivación $\mu$ fraccionarios. Da **dos
>   grados de libertad extra** de ajuste, controladores más robustos y mayor tolerancia a variaciones
>   de la planta.
> - **Relajación dieléctrica de Cole-Cole**: la permitividad de muchos materiales no decae
>   exponencialmente (Debye) sino como Mittag-Leffler; el ajuste de Cole-Cole es la huella de un orden
>   $\alpha$ en la polarización.
> - **Electroquímica**: el **elemento de fase constante** (CPE) tiene impedancia $Z(\omega)\sim(i\omega)^{-\alpha}$,
>   que es una **derivada/integral fraccionaria** en el dominio de frecuencia; modela electrodos rugosos y
>   baterías.
> - **Biología**: difusión en membranas, redes neuronales con memoria y dinámica de poblaciones con
>   retardo se describen con operadores fraccionarios, porque el "ahora" depende de **toda** la historia.

> [!proposicion] El hilo común: memoria y no-localidad
> En todos los casos la derivada fraccionaria es una **convolución** con un núcleo de ley de potencias,
> $$D^{\alpha}f(t)\;\sim\;\int_0^{t}(t-\tau)^{-\alpha}\,\dot f(\tau)\,d\tau,$$
> de modo que el estado presente integra **todo el pasado** con un peso que decae lentamente. Esa
> **memoria larga** es la razón física común de la difusión anómala, la relajación viscoelástica, la
> impedancia CPE y la dieléctrica de Cole-Cole: ver [[Ecuaciones con Memoria]].

## Resumen

> [!resumen]
> | Aplicación | Ecuación / modelo | Firma fraccionaria |
> |---|---|---|
> | Difusión anómala | $\partial_t^{\alpha}u=K\,\partial_x^2 u$ | $\langle x^2\rangle\sim t^{\alpha}$ |
> | Viscoelasticidad | springpot $\sigma=E\,D^{\alpha}\varepsilon$ | relajación $\sim t^{-\alpha}$ (Mittag-Leffler) |
> | Control | $\mathrm{PI}^{\lambda}\mathrm{D}^{\mu}$ | 2 grados de libertad extra |
> | Dieléctricos | Cole-Cole | permitividad no-Debye |
> | Electroquímica | CPE | $Z\sim(i\omega)^{-\alpha}$ |

> [!corolario]
> El exponente fraccionario $\alpha$ es un **parámetro físico medible** —cuánta memoria o cuánta anomalía
> tiene el sistema— y no un artificio matemático. Se lee directamente de los datos: como pendiente
> log-log en la difusión, como exponente de la relajación en viscoelasticidad, como fase constante en la
> impedancia. El cálculo fraccionario gana su lugar en la física precisamente porque ese número **se mide**.

> [!referencia]
> - La función que aparece en todas: [[Funcion de Mittag-Leffler]].
> - El mecanismo común: [[Ecuaciones con Memoria]].
> - El límite entero ($\alpha=1$): [[Ecuacion del Calor/index]].
> - Las ecuaciones que se resuelven: [[Ecuaciones Diferenciales Fraccionarias]].
> - Índice del tema: [[Calculo Fraccionario/index]].
