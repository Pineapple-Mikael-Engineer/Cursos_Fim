---
title: Aplicaciones Integro-Diferenciales
order: 5
tags:
  - ecuaciones
  - difero-integrales
  - teoria
  - integro-diferenciales
  - aplicaciones
draft: false
aliases:
  - aplicaciones integro-diferenciales
  - integro-differential applications
  - donde aparecen las ecuaciones con memoria
---

# Aplicaciones Integro-Diferenciales

> [!definicion]
> Panorama de **dónde aparecen** las ecuaciones integro-diferenciales en la ciencia y la ingeniería. El hilo común es siempre el mismo: un fenómeno cuya evolución presente **no depende solo del estado actual**, sino de una **suma ponderada de su historia** —un núcleo de memoria $K(t-s)$ que multiplica a la incógnita $\varphi$ bajo una integral, junto a sus derivadas. Allí donde un sistema "recuerda", casi siempre hay una ecuación integro-diferencial detrás.

> [!info]
> Última nota de la rama, dentro de [[Integro-Diferenciales/index| Ecuaciones Integro-Diferenciales]] en el [[4 Ecuaciones Difero-integrales/index| capítulo difero-integral]]. Es el cierre aplicado de [[Ecuaciones con Memoria| Ecuaciones con Memoria]]: aquí se ve que la memoria del núcleo no es una rareza matemática, sino la regla en mecánica de materiales, ecología, epidemiología, transporte, control y electromagnetismo.

---

## Ejemplo

> [!ejemplo] Oscilador con amortiguamiento viscoelástico
> Tome un oscilador masa-resorte ordinario y cambie el amortiguador viscoso por un elemento **viscoelástico** (un polímero, un tejido biológico, un soporte de caucho). La fuerza disipativa ya no es proporcional a la velocidad instantánea, sino a **toda la historia** de velocidades, pesada por el módulo de relajación $G(t-s)$:
> $$m\,\ddot x(t)+\int_{0}^{t}G(t-s)\,\dot x(s)\,ds+k\,x(t)=0.$$
> Compárese con el oscilador amortiguado clásico $m\ddot x+c\dot x+kx=0$. La diferencia es física, no cosmética:
> - En el **amortiguamiento viscoso clásico** la fuerza es $c\,\dot x(t)$: depende **solo** de la velocidad en este instante. Es el caso **sin memoria** (markoviano).
> - En el **amortiguamiento viscoelástico** la fuerza es la integral hereditaria: el material recuerda el movimiento reciente (o lejano, si $G$ tiene cola larga). Esto produce **disipación dependiente de la frecuencia** y, con un núcleo de ley de potencias $G(t)\sim t^{-\alpha}$, un **amortiguamiento fraccionario** que reproduce con notable fidelidad el comportamiento real de polímeros y materiales biológicos.
>
> De hecho, el amortiguador viscoso clásico es el límite de memoria nula $G(t-s)\to c\,\delta(t-s)$, exactamente como en [[Ecuaciones con Memoria| Ecuaciones con Memoria]].

## En qué consiste

> [!teoria] Catálogo de aplicaciones
> Las ecuaciones integro-diferenciales recorren disciplinas muy distintas con la misma estructura de memoria. Un mapa de las más importantes:
>
> **Viscoelasticidad (Boltzmann).** El esfuerzo es la integral hereditaria de la deformación, $\sigma(t)=\int_0^t G(t-s)\,\dot\varepsilon(s)\,ds$. El módulo de relajación $G$ es el núcleo de memoria del material (ver [[Ecuaciones con Memoria]]). Es el ejemplo prototípico de la rama.
>
> **Dinámica de poblaciones con retardo.** El modelo de **Volterra** presa-depredador con un término de memoria reconoce que el efecto de la abundancia de presas sobre los depredadores no es instantáneo: hay gestación, maduración. La **ecuación logística con retardo distribuido**,
> $$\dot N(t)=r\,N(t)\!\left[1-\frac{1}{K}\int_{0}^{t}\!a(t-s)\,N(s)\,ds\right],$$
> reparte el efecto de la población pasada sobre la capacidad de carga mediante el núcleo $a(t-s)$.
>
> **Epidemiología.** Los modelos con **período de infecciosidad distribuido** integran a los infectados de días anteriores: la tasa de nuevos contagios de hoy es $\int_0^t \beta(t-s)\,I(s)\,ds$, donde $\beta(t-s)$ pondera cuán contagioso sigue siendo alguien infectado hace $t-s$. Generaliza los modelos SIR con tasas constantes y captura períodos de incubación realistas.
>
> **Transporte y cinética.** La [[Transferencia Radiativa| transferencia radiativa]] (la ecuación de Boltzmann linealizada para fotones o neutrones) es **integro-diferencial**: la derivada describe el transporte a lo largo del rayo y la integral, la dispersión que redistribuye la radiación sobre todas las direcciones.
>
> **Control.** El término **integral** de un controlador **PID**, $u(t)=K_p e(t)+K_i\!\int_0^t e(s)\,ds+K_d\,\dot e(t)$, hace del lazo cerrado un sistema integro-diferencial; lo mismo ocurre en **sistemas con retardo**, donde la acción presente depende del estado en instantes anteriores.
>
> **Electromagnetismo en medios con memoria.** En un dieléctrico **dispersivo**, la polarización no responde instantáneamente al campo: $P(t)=\varepsilon_0\!\int_0^t \chi(t-s)\,E(s)\,ds$, con la susceptibilidad $\chi(t-s)$ como núcleo de memoria. Al insertarlo en las ecuaciones de Maxwell, estas se vuelven integro-diferenciales.

> [!info] El puente fraccionario
> Muchas de estas aplicaciones, cuando el núcleo de memoria es de **ley de potencias** $K(t-s)\sim (t-s)^{-\alpha}$, se reescriben de forma compacta como ecuaciones **fraccionarias**: el oscilador viscoelástico se convierte en un oscilador con derivada fraccionaria, la difusión con memoria en difusión anómala, etc. La memoria larga es, una y otra vez, la puerta de entrada al [[Calculo Fraccionario/index| cálculo fraccionario]].

## Resumen

> [!resumen]
> | Campo | Qué recuerda el sistema | Núcleo de memoria |
> |---|---|---|
> | Viscoelasticidad | la historia de deformación | módulo de relajación $G(t-s)$ |
> | Poblaciones (Volterra) | la abundancia pasada / retardo | $a(t-s)$ distribuido |
> | Epidemiología | infectados de días previos | infecciosidad $\beta(t-s)$ |
> | Transporte radiativo | dispersión sobre direcciones | núcleo de scattering |
> | Control (PID, retardo) | el error acumulado | integral del error |
> | Electromagnetismo | el campo eléctrico pasado | susceptibilidad $\chi(t-s)$ |

> [!corolario]
> Bajo todas estas aplicaciones late la misma idea: **el presente arrastra al pasado** a través de un núcleo. Donde la memoria sea de ley de potencias, la ecuación integro-diferencial se vuelve fraccionaria; donde sea exponencial, se reduce a una EDO ampliada. La estructura matemática es única; cambia solo el nombre del núcleo según la disciplina.

> [!referencia]
> - El significado físico del núcleo: [[Ecuaciones con Memoria]].
> - Una aplicación de transporte desarrollada: [[Transferencia Radiativa]].
> - La generalización con memoria larga: [[Calculo Fraccionario/index]].
> - Vuelta al índice de la rama: [[Integro-Diferenciales/index]].
