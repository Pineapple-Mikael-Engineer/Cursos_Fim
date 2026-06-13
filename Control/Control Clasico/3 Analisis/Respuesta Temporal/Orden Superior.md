---
title: Sistemas de Orden Superior
tags:
  - control-clasico
  - analisis
  - respuesta-temporal
draft: false
aliases:
  - orden superior
  - polos dominantes
  - higher order systems
---

# Sistemas de Orden Superior

> [!definicion]
> Un sistema de orden superior tiene **tres o más polos** (denominador de grado $\ge 3$). Su respuesta es la **superposición** de los modos de todos los polos; no hay fórmulas cerradas de $M_p$, $t_s$ como en [[Segundo Orden/index | segundo orden]]. Cuando un par de **polos dominantes** (los más cercanos al eje $j\omega$) decae mucho más lento que el resto, el sistema se aproxima por uno de segundo orden con ese par.

> [!info]
> Es el caso general de [[Segundo Orden/index | segundo orden]] y la base de la [[Reduccion Orden | reducción de orden]]. El efecto de polos/ceros extra se analiza en [[Polos Ceros]] y [[Sistemas Fase Minima]]; la ubicación de polos en diseño, en [[Lugar Raices/index]].

---

## Ejemplo

> [!ejemplo] Identificar el par dominante y aproximar
> Sea el sistema de tercer orden
> $$G(s)=\frac{60}{(s^2+2s+5)(s+12)},\qquad G(0)=\frac{60}{5\cdot12}=1.$$
>
> ![[polos_dominantes_plano_s.svg|500]]
>
> **Paso 1 — Polos.** El factor cuadrático da $s=-1\pm j2$; el factor lineal da $s=-12$.
> $$\text{Polos: } \;-1\pm j2\;\;(\text{par complejo}),\qquad -12\;\;(\text{real}).$$
>
> **Paso 2 — Test de dominancia.** Comparar partes reales:
> $$\frac{|\operatorname{Re}\{-12\}|}{|\operatorname{Re}\{-1\pm j2\}|}=\frac{12}{1}=12\ge 5\;\checkmark$$
> El polo en $-12$ es $12\times$ más rápido → el par $-1\pm j2$ es **dominante**. No hay ceros que los cancelen.
>
> **Paso 3 — Parámetros del par dominante.** De $s^2+2s+5=s^2+2\zeta\omega_n s+\omega_n^2$:
> $$\omega_n=\sqrt{5}\approx 2.24\ \text{rad/s},\qquad \zeta=\frac{2}{2\omega_n}=\frac{1}{\sqrt5}\approx 0.447.$$
>
> **Paso 4 — Aproximación de 2.º orden** (despreciar $-12$, conservar $G(0)=1$):
> $$G(s)\approx\frac{60/12}{s^2+2s+5}=\frac{5}{s^2+2s+5}.$$
> Se reemplazó el factor $(s+12)$ por su valor DC, $12$. Verificación: $G_{red}(0)=5/5=1=G(0)\;\checkmark$.
>
> **Paso 5 — Estimar el transitorio** con las fórmulas de segundo orden:
> $$M_p=e^{-\zeta\pi/\sqrt{1-\zeta^2}}\approx 20.8\%,\qquad t_s(2\%)\approx\frac{4}{\zeta\omega_n}=\frac{4}{1}=4\ \text{s}.$$
> El polo rápido en $-12$ solo añade un pequeño retardo al inicio (modo $e^{-12t}$, extinto en $\sim 0.3$ s).

---

## En qué consiste

> [!teoria] Respuesta como suma de modos
> Por fracciones parciales, la respuesta al escalón de un sistema de orden $n$ es la suma de las contribuciones de cada [[Polos Ceros | polo]]:
> $$y(t)=y(\infty)+\sum_i A_i e^{-\sigma_i t}+\sum_k B_k e^{-\zeta_k\omega_{nk} t}\sin(\omega_{dk}t+\phi_k).$$
> Cada polo real aporta una exponencial $e^{-\sigma_i t}$; cada par complejo, una senoide amortiguada. El modo que decae **más lento** (polo más cercano al eje $j\omega$) persiste y **domina** la respuesta.

> [!definicion] Par de polos dominantes
> Polos cuya parte real es la **menos negativa** (más cerca del eje imaginario). Decaen más lento que los demás y gobiernan el transitorio.

> [!regla] Criterio de dominancia
> Un par domina si los demás polos tienen parte real al menos **5 veces más negativa**:
> $$\frac{|\operatorname{Re}\{\text{polos no dominantes}\}|}{|\operatorname{Re}\{\text{polos dominantes}\}|}\ge 5,$$
> y no hay ceros cercanos que los cancelen. Entonces el sistema se aproxima como [[Segundo Orden/index | segundo orden]] (ver [[Reduccion Orden]]).

> [!info] Efecto de polos y ceros adicionales
> | Elemento añadido | Efecto |
> |---|---|
> | Polo real lejano (rápido) | despreciable (el modo se extingue rápido) |
> | Polo real **cercano** al par dominante | hace la respuesta más lenta y sobreamortiguada |
> | Cero en el SPI cercano | **aumenta** el sobrepico, adelanta la respuesta |
> | Cero en el SPD ([[Sistemas Fase Minima \| fase no mínima]]) | undershoot inicial (respuesta arranca al revés) |

> [!info] En MATLAB
> ```matlab
> G = tf(60, conv([1 2 5],[1 12]));
> step(G)
> pzmap(G)          % ubicacion de polos y ceros
> damp(G)           % zeta y wn de cada modo
> ```

---

## Limitaciones

> [!warning]
> Las fórmulas de $M_p$, $t_p$, $t_s$ de [[Segundo Orden/index | segundo orden]] solo valen si se cumple la dominancia ($\ge 5\times$) **y** no hay ceros próximos al par dominante. Un cero cercano puede elevar $M_p$ muy por encima de lo que predice $\zeta$, y un polo "no tan rápido" (separación $<5\times$) hace la aproximación poco fiable.

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Definición | denominador de grado $\ge 3$ |
> | Respuesta | superposición de modos de cada polo |
> | Dominantes | par con $\operatorname{Re}$ menos negativa |
> | Criterio | separación $\ge 5\times$ y sin ceros cercanos |
> | Aproximación | 2.º orden con el par dominante |
> | Sin fórmulas cerradas | $M_p$, $t_s$ solo vía dominancia |

> [!corolario]
> En un sistema de orden superior, los polos lejanos del eje $j\omega$ aportan transitorios que se extinguen pronto; los cercanos (dominantes) fijan $\zeta$ y $\omega_n$ efectivos. Si la separación es $\ge 5\times$ y no hay ceros próximos, el sistema se reduce con seguridad a segundo orden (ver [[Reduccion Orden]]), conservando la ganancia DC. En caso contrario, hay que simular la respuesta completa.

> [!referencia]
> - Aproximación al sistema reducido: [[Reduccion Orden]].
> - Modo dominante de 2.º orden: [[Segundo Orden/index]].
> - Efecto de ceros: [[Polos Ceros]] · [[Sistemas Fase Minima]].
> - Ubicación de polos en diseño: [[Lugar Raices/index]].
