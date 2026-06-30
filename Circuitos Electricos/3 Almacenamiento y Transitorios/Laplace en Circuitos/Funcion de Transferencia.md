---
title: Función de Transferencia
tags:
  - circuitos-electricos
  - teoria
  - transitorios
  - laplace
  - funcion-transferencia
draft: false
aliases:
  - función de transferencia
  - polos y ceros
  - diagrama de polos y ceros
  - transfer function
---

# Función de Transferencia $H(s)$

> [!definicion]
> La **función de transferencia** $H(s)$ es el cociente entre la transformada de la **salida** y la de la **entrada**, con condiciones iniciales nulas:
> $$H(s)=\frac{Y(s)}{X(s)}=\frac{N(s)}{D(s)}.$$
> Las raíces del numerador $N(s)$ son los **ceros**; las del denominador $D(s)$, los **polos**. Los polos son las **frecuencias naturales** del circuito —las mismas raíces de la ecuación característica— y su posición en el plano $s$ resume toda la dinámica.

> [!info]
> La lectura dinámica de [[Laplace en Circuitos/index| Laplace en circuitos]] ([[3 Almacenamiento y Transitorios/index| capítulo 3]]). Conecta el dominio de $s$ con los [[Regimenes de Amortiguamiento| regímenes de amortiguamiento]] del segundo orden. Fraile Mora, cap. 4, §4.8.

---

## Ejemplo

> [!ejemplo]
> **Leer la dinámica en el plano $s$.**
>
> Un circuito de segundo orden subamortiguado tiene la función de transferencia $H(s)=\dfrac{\omega_0^2}{s^2+2\alpha s+\omega_0^2}$, con polos en $s=-\alpha\pm j\omega_d$ y (en este caso) un cero en el eje real. Su **diagrama de polos y ceros**:
>
> ![[polos_ceros.svg|560]]
>
> *Polos ($\times$) y cero ($\circ$). La **parte real** $-\alpha$ de los polos es el amortiguamiento (rapidez del decaimiento); la **parte imaginaria** $\pm\omega_d$, la frecuencia de oscilación. Estar en el **semiplano izquierdo** garantiza que la respuesta decae (estable).*
>
> > [!solucion]
> > Polos complejos conjugados $\Rightarrow$ respuesta oscilante $e^{-\alpha t}\cos\omega_d t$ (subamortiguado). Si los polos fueran reales, no oscilaría; si estuvieran en el eje imaginario, oscilaría sin amortiguarse; en el semiplano derecho, crecería (inestable).

---

## En qué consiste

> [!teoria] Cada polo es un modo de la respuesta natural
> El denominador $D(s)$ de $H(s)$ es el **polinomio característico** del circuito. Por eso cada polo aporta un término a la respuesta natural:
> - **Polo real** $s=-a$ → término $e^{-at}$ (exponencial; régimen sobre/críticamente amortiguado).
> - **Par complejo** $s=-\alpha\pm j\omega_d$ → término $e^{-\alpha t}\cos(\omega_d t+\varphi)$ (oscilación amortiguada; régimen subamortiguado).
>
> Así, **mirar dónde están los polos equivale a conocer la forma de la respuesta** sin resolver nada: es la versión en el plano $s$ de los [[Regimenes de Amortiguamiento| regímenes de amortiguamiento]].

> [!teorema] Estabilidad por la posición de los polos
> Un circuito (lineal, invariante) es **estable** —su respuesta natural se extingue— **si y solo si todos sus polos están en el semiplano izquierdo** ($\operatorname{Re}(s)<0$).
> - Polos en el semiplano **izquierdo**: la respuesta **decae** (estable).
> - Polos en el eje **imaginario**: oscilación **mantenida** (límite).
> - Polos en el semiplano **derecho**: la respuesta **crece** (inestable).

> [!info] Qué hacen los ceros
> Los **ceros** no crean modos nuevos, pero **moldean las amplitudes**: en un cero $H(s)=0$, esa frecuencia se **bloquea** a la salida. Polos y ceros juntos determinan por completo $H(s)$ (salvo una constante) y, con ella, la respuesta a cualquier entrada: $Y(s)=H(s)\,X(s)$.

> [!proposicion] La respuesta al impulso es $H(s)$ antitransformada
> Si la entrada es un impulso, $X(s)=1$ ([[Funciones Singulares| $\delta(t)$]]), y entonces $Y(s)=H(s)$: la **respuesta al impulso** $h(t)=\mathcal{L}^{-1}\{H(s)\}$ caracteriza por completo al circuito. La respuesta a cualquier otra entrada es la convolución de $h(t)$ con esa entrada.

> [!warning]
> $H(s)$ se define con **condiciones iniciales nulas**: describe la respuesta **forzada** a la entrada. El efecto de las condiciones iniciales se añade aparte (como fuentes en el dominio de $s$, ver [[Circuitos en el Dominio de s]]). Y la entrada y la salida deben quedar claras: hay un $H(s)$ distinto para cada par entrada-salida.

## Resumen

> [!resumen]
> | Concepto | Significado |
> |:---|:---|
> | $H(s)=Y(s)/X(s)$ | salida/entrada, condiciones iniciales nulas |
> | Polos (raíces de $D(s)$) | frecuencias naturales; cada uno, un modo |
> | Polo real $-a$ | término $e^{-at}$ |
> | Par complejo $-\alpha\pm j\omega_d$ | término $e^{-\alpha t}\cos\omega_d t$ |
> | Ceros (raíces de $N(s)$) | moldean amplitudes; bloquean frecuencias |
> | Estabilidad | todos los polos con $\operatorname{Re}(s)<0$ |

> [!corolario]
> La función de transferencia y su diagrama de polos y ceros **dibujan** la dinámica del circuito: la posición de cada polo dice si decae o crece, si oscila y a qué ritmo. Es el lenguaje que unifica transitorios, estabilidad y —ya en el siguiente capítulo— la respuesta en frecuencia.

> [!referencia]
> Fraile Mora, cap. 4, §4.8. Base: [[Circuitos en el Dominio de s]]. Conecta con: [[Regimenes de Amortiguamiento]]. Aplicación: [[Solucion de Transitorios con Laplace]].
