---
title: Ondas Periódicas Sinusoidales
tags:
  - circuitos-electricos
  - teoria
  - sinusoidal
  - index
draft: false
aliases:
  - ondas periódicas sinusoidales
  - corriente alterna
  - onda alterna
---

# Ondas Periódicas Sinusoidales

> [!definicion]
> Este capítulo estudia la **onda alterna sinusoidal** —la forma de toda la energía de corriente
> alterna (CA)— y las magnitudes que caracterizan **cualquier** onda periódica: el **período** y la
> **frecuencia**, el **valor medio**, el **valor eficaz (RMS)** y los **factores de forma y cresta**.
> La senoide $v(t)=V_m\operatorname{sen}(\omega t+\varphi)$ y, sobre todo, su **valor eficaz** son la
> base del análisis en CA.

> [!info]
> Cuarto bloque del curso (sílabo ML 140, semana 9; Fraile Mora, cap. 2 §2.2). Es la puerta al
> **régimen permanente sinusoidal**: las magnitudes de aquí (especialmente el valor eficaz) son las que
> usan los [[5 Circuitos AC Sinusoidal y Fasores/index| fasores]] del capítulo siguiente. La senoide
> ya apareció como respuesta de los [[Transitorios Segundo Orden/index| circuitos de segundo orden]].

---

## Por qué la senoide, y qué medir de ella

> [!teoria] La onda natural de la electricidad
> La onda sinusoidal es **omnipresente** en electrotecnia por dos razones: se **genera** de forma
> natural al hacer girar una espira en un campo magnético (un alternador → [[Generacion de Tension Alterna]]), y es la forma propia de oscilación de los circuitos $LC$. Además, derivar o integrar una
> senoide **devuelve otra senoide** de la misma frecuencia: por eso el análisis en CA se vuelve tan
> manejable (y dará lugar a los [[5 Circuitos AC Sinusoidal y Fasores/index| fasores]]).

> [!teoria] Cuatro magnitudes describen cualquier onda periódica
> Una onda periódica se caracteriza con unos pocos números:
> - su **forma temporal**: amplitud, [[Caracteristicas de Ondas Periodicas| período, frecuencia y fase]] → la senoide $v=V_m\operatorname{sen}(\omega t+\varphi)$ ([[Onda Sinusoidal]]);
> - su **valor medio** (la componente continua) → [[Valor Medio]];
> - su **valor eficaz (RMS)**, el que determina la **potencia** → [[Valor Eficaz RMS]];
> - sus **factores de forma y cresta**, que comparan esos valores y describen la "puntiagudez" de la
>   onda → [[Factor de Forma y Cresta]].
>
> De todos, el **valor eficaz** es el rey: cuando se dice "$220\ \text{V}$" de la red, es un valor
> eficaz, porque es el que fija el calor y la potencia.

## Mapa del capítulo

> [!info] Las notas de este capítulo
> | Nota | Contenido |
> |:---|:---|
> | [[Onda Sinusoidal]] | $v=V_m\operatorname{sen}(\omega t+\varphi)$: amplitud, $\omega$, fase |
> | [[Caracteristicas de Ondas Periodicas]] | período $T$, frecuencia $f$, $\omega=2\pi f$, fase |
> | [[Valor Medio]] | promedio en un período; $0$ para la senoide, $2V_m/\pi$ rectificada |
> | [[Valor Eficaz RMS]] | $V_{ef}=V_m/\sqrt2$; el valor que da la potencia |
> | [[Factor de Forma y Cresta]] | $V_{ef}/V_{med}$ y $V_m/V_{ef}$; describen la forma |
> | [[Generacion de Tension Alterna]] | el alternador: la senoide como proyección de un giro |

> [!corolario]
> La senoide es la onda de la electricidad, y bastan unas pocas magnitudes para describirla. El valor
> eficaz, en particular, es el puente hacia la potencia y hacia el análisis fasorial del próximo
> capítulo.

> [!referencia]
> Fraile Mora, cap. 2, §2.2. Viene de [[3 Almacenamiento y Transitorios/index| Almacenamiento y transitorios]]; continúa en [[5 Circuitos AC Sinusoidal y Fasores/index| Circuitos AC sinusoidal y fasores]].
