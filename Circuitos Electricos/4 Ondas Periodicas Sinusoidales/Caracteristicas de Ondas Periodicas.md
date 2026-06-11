---
title: Características de Ondas Periódicas
tags:
  - circuitos-electricos
  - teoria
  - sinusoidal
draft: false
aliases:
  - características de ondas periódicas
  - período frecuencia y frecuencia angular
  - magnitudes temporales
  - periodic waves
  - period frequency angular frequency
---

# Características de Ondas Periódicas $\;x(t)=x(t+T)$

> [!definicion]
> Una onda es **periódica** si se repite cada cierto intervalo de tiempo, es decir,
> $$x(t)=x(t+T)\quad\text{para todo }t,$$
> donde $T$ es el menor intervalo que cumple la igualdad. Toda onda periódica queda descrita por:
> el **período** $T$ (duración de un ciclo, en s), la **frecuencia** $f=1/T$ (ciclos por segundo, en
> Hz), la **frecuencia angular** $\omega=2\pi f=2\pi/T$ (en rad/s), la **amplitud** (valor de pico)
> y la **fase** (posición dentro del ciclo).

> [!info]
> Magnitudes temporales de las [[4 Ondas Periodicas Sinusoidales/index| ondas periódicas]]: son
> comunes a la [[Onda Sinusoidal]] y a cualquier onda repetitiva (triangular, cuadrada, diente de
> sierra...). De estas magnitudes parten luego el [[Valores Caracteristicos]] y el [[Valores Caracteristicos]]. Fraile
> Mora, cap. 2, §2.2.

---

## Ejemplo

> [!ejemplo]
> **Período y frecuencia angular de la red europea.**
>
> La red eléctrica europea opera a $f=50\ \text{Hz}$. Hallar el período $T$ y la frecuencia angular
> $\omega$.
>
> ![[onda_sinusoidal.svg|560]]
>
> *Una onda periódica se repite cada período $T$; su amplitud es la altura del pico y su fase, la
> posición dentro del ciclo.*
>
> **Paso 1 — Período.** El período es el inverso de la frecuencia:
> $$T=\frac{1}{f}=\frac{1}{50}=0{,}02\ \text{s}=20\ \text{ms}.$$
> Cada ciclo de la red dura $20\ \text{ms}$, y en un segundo caben $50$ ciclos.
>
> **Paso 2 — Frecuencia angular.** Un ciclo completo equivale a $2\pi$ radianes de fase, de modo que
> $$\omega=2\pi f=2\pi\cdot50=100\pi\approx314\ \text{rad/s}.$$
> Equivalentemente, $\omega=2\pi/T=2\pi/(20\ \text{ms})\approx314\ \text{rad/s}$.
>
> > [!solucion]
> > $T=20\ \text{ms}$ y $\omega\approx314\ \text{rad/s}$. (Para la red americana, $f=60\ \text{Hz}$,
> > se tendría $T\approx16{,}7\ \text{ms}$ y $\omega\approx377\ \text{rad/s}$.)

---

## En qué consiste

> [!teoria] Las cuatro magnitudes y sus relaciones
> - **Período $T$:** el tiempo que dura un ciclo completo, en segundos. Es la "huella temporal" de la
>   repetición: tras $T$ segundos la onda vuelve a valer lo mismo y a moverse igual.
> - **Frecuencia $f$:** cuántos ciclos ocurren por segundo, $f=1/T$, en hercios ($\text{Hz}$). Período
>   y frecuencia son inversos: a mayor frecuencia, ciclos más cortos.
> - **Frecuencia angular $\omega$:** cuenta **radianes de fase por segundo**. Como un ciclo completo
>   son $2\pi$ rad, se tiene $\omega=2\pi f=2\pi/T$. Es la magnitud natural en el argumento de la
>   senoide ($\operatorname{sen}\omega t$) y en el cálculo fasorial.
> - **Amplitud y fase:** la **amplitud** es el valor de pico (máxima desviación respecto a cero); la
>   **fase** indica en qué punto del ciclo se encuentra la onda en un instante dado.
>
> Las relaciones clave se resumen en una cadena:
> $$f=\frac{1}{T},\qquad \omega=2\pi f=\frac{2\pi}{T}.$$

> [!teoria] Ciclo, período... y por qué no longitud de onda
> Un **ciclo** es una repetición completa del patrón de la onda; el **período** $T$ es su duración. En
> ondas que se propagan por el espacio se define además la **longitud de onda** $\lambda$ (distancia
> entre dos repeticiones espaciales), pero en circuitos de **parámetros concentrados** —los de este
> curso— las dimensiones son pequeñas frente a $\lambda$ y se supone que la señal toma el mismo valor
> en todo el circuito en cada instante. Por eso aquí la descripción es puramente **temporal**: basta
> con $T$, $f$ y $\omega$, sin necesidad de $\lambda$.

> [!proposicion] La senoide es el "ladrillo" de toda onda periódica
> Cualquier onda periódica razonable puede descomponerse como suma de senoides de frecuencias
> múltiplos de la fundamental ($\omega,\,2\omega,\,3\omega,\dots$): es la **serie de Fourier**. Por
> eso el estudio de la CA se centra en la [[Onda Sinusoidal]]: dominada la senoide y la respuesta
> lineal a ella, se obtiene la respuesta a cualquier onda periódica superponiendo sus componentes.

> [!warning]
> No confundir la **frecuencia** $f$ (en $\text{Hz}$) con la **frecuencia angular** $\omega$ (en
> $\text{rad/s}$): siempre $\omega=2\pi f$, nunca $\omega=f$. Y al fijar el período recuérdese su
> orden de magnitud: las redes eléctricas usan $50\ \text{Hz}$ en Europa ($T=20\ \text{ms}$) o
> $60\ \text{Hz}$ en América ($T\approx16{,}7\ \text{ms}$).

## Resumen

> [!resumen]
> | Magnitud | Símbolo | Unidad | Relación |
> |:---|:---|:---|:---|
> | Período | $T$ | $\text{s}$ | $T=1/f=2\pi/\omega$ |
> | Frecuencia | $f$ | $\text{Hz}$ | $f=1/T=\omega/(2\pi)$ |
> | Frecuencia angular | $\omega$ | $\text{rad/s}$ | $\omega=2\pi f=2\pi/T$ |
> | Amplitud | — | (según señal) | valor de pico |
> | Fase | — | $\text{rad}$ o $^\circ$ | posición en el ciclo |

> [!corolario]
> Conocida **una** de las tres magnitudes temporales ($T$, $f$ o $\omega$) quedan determinadas las
> otras dos, pues $f=1/T$ y $\omega=2\pi f$. Estas magnitudes son el punto de partida para definir el
> [[Valores Caracteristicos]] y el [[Valores Caracteristicos]] de la onda.

> [!referencia]
> Fraile Mora, cap. 2, §2.2. Onda central: [[Onda Sinusoidal]]. Valores asociados: [[Valores Caracteristicos]],
> [[Valores Caracteristicos]]. Contexto: [[4 Ondas Periodicas Sinusoidales/index]].
