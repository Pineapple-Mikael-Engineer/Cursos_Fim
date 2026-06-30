---
title: Potencia en AC
tags:
  - circuitos-electricos
  - teoria
  - potencia
  - index
draft: false
aliases:
  - potencia en AC
  - potencia en corriente alterna
  - potencia en régimen sinusoidal
---

# Potencia en AC

> [!definicion]
> En corriente alterna la potencia ya no es un solo número: el desfase $\varphi$ entre tensión y corriente la parte en **tres**. La **activa** $P=VI\cos\varphi$ (W) es la que trabaja; la **reactiva** $Q=VI\operatorname{sen}\varphi$ (VAr), la que oscila en bobinas y condensadores sin consumirse; y la **aparente** $S=VI$ (VA), la que dimensiona los equipos. Se unifican en la potencia compleja $S=\overline{V}\,\overline{I}^{*}=P+jQ$.

> [!info]
> Cuarta sección del [[5 Circuitos AC Sinusoidal y Fasores/index | capítulo 5]]. Aplica los [[Fasores]] y la [[Impedancia Compleja | impedancia]] al **balance de energía**; es la base de la [[Potencia Trifasica/index | potencia trifásica]] del capítulo 7. Fraile Mora, cap. 2, §2.9-2.11.

---

## De la energía que va y viene a la factura

> [!teoria] Por qué tres potencias y no una
> En continua, potencia es $VI$ y basta. En alterna, $v$ e $i$ están **desfasados**, y su producto $p(t)=vi$ —la [[Potencia en Regimen Sinusoidal | potencia instantánea]]— oscila al doble de la frecuencia y **se vuelve negativa** en parte del ciclo: hay energía que la carga **devuelve** a la fuente. De ahí salen las tres potencias:
> - su **media** es la **activa** $P$ (lo que de verdad se consume),
> - su **fluctuación** mide la **reactiva** $Q$ (lo que va y vuelve, en $L$ y $C$),
> - y el producto bruto de eficaces es la **aparente** $S=\sqrt{P^2+Q^2}$.
>
> Todo ello se empaqueta en un número complejo, $S=P+jQ$, y se visualiza en el **triángulo de potencias**. → [[Potencia en Regimen Sinusoidal]].

> [!teoria] El factor de potencia: por qué importa $Q$
> La reactiva no se paga en el contador, pero **ocupa la red**: para entregar la misma $P$ con un $\cos\varphi$ bajo hace falta **más corriente**, más sección de cable y más pérdidas. El cociente $\cos\varphi=P/S$ —el **factor de potencia**— mide esa eficiencia → [[Factor de Potencia]], y se **corrige** con condensadores que aportan $Q<0$ → [[Correccion del Factor de Potencia]]. Cuando lo que se busca es **extraer la máxima potencia** de una fuente, la condición es adaptar la impedancia → [[Maxima Transferencia AC]].

## Mapa de la sección

> [!info] Las notas de esta sección
> | Nota | Contenido |
> |:---|:---|
> | [[Potencia en Regimen Sinusoidal]] | $p(t)$, $P/Q/S$, potencia compleja, triángulo, Boucherot |
> | [[Factor de Potencia]] | $\cos\varphi=P/S$; el coste de un FP bajo |
> | [[Correccion del Factor de Potencia]] | condensadores para subir $\cos\varphi$ |
> | [[Maxima Transferencia AC]] | $Z_L=Z_{Th}^{*}$ |

> [!corolario]
> En CA, dominar la potencia es dominar el **triángulo** $P$–$Q$–$S$: separar lo que se consume de lo que solo se intercambia, y gestionarlo (factor de potencia) para no malgastar red. Es el puente entre el análisis fasorial y la ingeniería eléctrica real.

> [!referencia]
> Fraile Mora, cap. 2, §2.9-2.11. Anterior: [[Analisis Fasorial/index | Análisis fasorial]]. Se extiende a [[Potencia Trifasica/index | potencia trifásica]] en el capítulo 7.
