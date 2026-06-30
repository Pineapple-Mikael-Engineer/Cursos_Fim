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
> Este capítulo estudia la **onda alterna sinusoidal** —la forma de toda la energía de corriente alterna (CA)— y las magnitudes que caracterizan **cualquier** onda periódica: período y frecuencia, valor de pico, valor medio, valor eficaz (RMS) y los factores de forma y cresta. La senoide $v(t)=V_m\operatorname{sen}(\omega t+\varphi)$ y, sobre todo, su **valor eficaz** son la base del análisis en CA.

> [!info]
> Cuarto bloque del curso (sílabo ML 140, semana 9; Fraile Mora, cap. 2 §2.2). Es la puerta al **régimen permanente sinusoidal**: las magnitudes de aquí (en especial el valor eficaz) son las que usan los [[5 Circuitos AC Sinusoidal y Fasores/index | fasores]] del capítulo siguiente. La senoide ya apareció como respuesta de los [[Transitorios Segundo Orden/index | circuitos de segundo orden]].

---

## Por qué la senoide, y qué medir de ella

> [!teoria] La onda natural de la electricidad
> La onda sinusoidal es **omnipresente** en electrotecnia por tres razones: se **genera** de forma natural al hacer girar una espira en un campo magnético (un alternador → [[Generacion de Tension Alterna]]); es la forma propia de oscilación de los circuitos $LC$; y derivar o integrar una senoide **devuelve otra senoide** de la misma frecuencia, lo que hará tan manejable el análisis en CA (los [[Fasores]]). Más aún: por **Fourier**, **cualquier** onda periódica es una suma de senoides, así que entender la senoide basta para entenderlas todas (el puente Fourier→fasores se desarrolla en [[Fasores]]).

> [!teoria] Qué se mide de una onda periódica
> Una onda periódica se describe con unos pocos números, en dos grupos:
> - su **forma temporal** —amplitud, [[Caracteristicas de Ondas Periodicas | período, frecuencia y fase]]— que para la CA es la senoide $v=V_m\operatorname{sen}(\omega t+\varphi)$ ([[Onda Sinusoidal]]);
> - sus **valores característicos** —pico, **medio** (componente continua), **eficaz (RMS)** y los **factores de forma y cresta**— reunidos en [[Valores Caracteristicos]].
>
> De todos, el **valor eficaz** es el rey: cuando se dice "$220\ \text{V}$" de la red, es eficaz, porque es el que fija el calor y la potencia.

## Mapa del capítulo

> [!info] Las notas de este capítulo
> | Nota | Contenido |
> |:---|:---|
> | [[Onda Sinusoidal]] | $v=V_m\operatorname{sen}(\omega t+\varphi)$: amplitud, $\omega$, fase |
> | [[Caracteristicas de Ondas Periodicas]] | período $T$, frecuencia $f$, $\omega=2\pi f$, fase; Fourier |
> | [[Valores Caracteristicos]] | pico, medio, eficaz (RMS) y factores de forma y cresta |
> | [[Generacion de Tension Alterna]] | el alternador: la senoide como proyección de un giro |

> [!corolario]
> La senoide es la onda de la electricidad —y, por Fourier, la base de todas—; bastan unas pocas magnitudes para describirla. El valor eficaz, en particular, es el puente hacia la potencia y hacia el análisis fasorial del próximo capítulo.

> [!referencia]
> Fraile Mora, cap. 2, §2.2. Viene de [[3 Almacenamiento y Transitorios/index | Almacenamiento y transitorios]]; continúa en [[5 Circuitos AC Sinusoidal y Fasores/index | Circuitos AC sinusoidal y fasores]].
