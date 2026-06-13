---
title: Diagrama de Nyquist
tags:
  - control-clasico
  - analisis
  - respuesta-frecuencial
  - nyquist
  - index
draft: false
aliases:
  - Nyquist
  - diagrama de Nyquist
  - Nyquist plot
---

# Diagrama de Nyquist

> [!definicion]
> El **diagrama de Nyquist** es la traza polar de la [[Respuesta Frecuencial/index | respuesta en frecuencia]] de lazo abierto $L(j\omega)=G(j\omega)H(j\omega)$ en el plano complejo, recorrida para $\omega$ de $-\infty$ a $+\infty$. Sobre esa curva cerrada se cuenta cuántas veces rodea al **punto crítico** $-1+j0$ y, mediante el criterio
> $$Z = N + P,$$
> se decide la estabilidad de **lazo cerrado** (raíces de $1+L=0$) a partir de datos de **lazo abierto**.

> [!info]
> Índice de la subcarpeta **Nyquist** dentro de [[Respuesta Frecuencial/index | Respuesta Frecuencial]]. Notas hermanas: [[Diagrama Polar]] (trazado), [[Criterio Nyquist]] (conteo $Z=N+P$) y [[Margenes MF MG | Márgenes]] (distancia a $-1$). Vista cartesiana equivalente: [[Bode/index | Bode]].

---

## Ejemplo

> [!ejemplo]
> **Lectura completa de un Nyquist.** Sea $L(s)=\dfrac{6}{s(s+1)(s+2)}$ con realimentación unitaria. Decidir estabilidad de lazo cerrado leyendo el diagrama.
>
> ![[nyquist_diagrama_polar.svg|550]]
>
> **Paso 1 — Polos de lazo abierto en el SPD ($P$):** los polos de $L$ son $s=0,-1,-2$. Ninguno tiene parte real positiva, luego $P=0$ (el polo en el origen se trata aparte, con el rodeo del contorno).
>
> **Paso 2 — Cruce del eje real.** Con $s=j\omega$,
> $$L(j\omega)=\frac{6}{j\omega(j\omega+1)(j\omega+2)}=\frac{-6\cdot 3\omega^2 - j\,6\omega(2-\omega^2)}{\dots},$$
> cuya parte imaginaria se anula en $\omega_{pc}=\sqrt2$ rad/s. Allí $L(j\sqrt2)=-\dfrac{6}{6}=-1$.
>
> **Paso 3 — Posición relativa a $-1$.** Con $K=6$ el cruce cae **exactamente** sobre $-1$: la curva pasa por el punto crítico. El número de rodeos netos es $N=0$ pero hay contacto → **estabilidad marginal** (oscilación sostenida a $\omega=\sqrt2$).
>
> **Paso 4 — Conclusión.** $Z=N+P=0+0=0$ con la curva tocando $-1$: el lazo cerrado está al **borde** de la inestabilidad. Para $K<6$ el cruce se mueve a $-K/6>-1$ (a la derecha de $-1$), $N=0$ y el sistema es **estable**; para $K>6$ el cruce pasa a la izquierda de $-1$, $N=2$ y $Z=2$ → **inestable**.

---

## En qué consiste

> [!teoria]
> El diagrama traduce cada valor de frecuencia en un punto del plano complejo. Para una $\omega$ dada se toman la magnitud $|L(j\omega)|$ y la fase $\angle L(j\omega)$ —los mismos datos del [[Bode/index | Bode]]— y se ubica el punto en coordenadas polares. Al barrer $\omega$ de $0$ a $\infty$ se obtiene el **lugar polar**; añadiéndole su reflejo conjugado ($\omega:-\infty\to0$) y, si hay polos en el eje imaginario, un arco de radio infinito, se cierra el **contorno de Nyquist**.
>
> La potencia del método está en que sobre esa curva cerrada el [[Criterio Nyquist | principio del argumento]] cuenta los rodeos a $-1$ y entrega $Z=N+P$ sin calcular las raíces de $1+L=0$. Funciona con **retardos** $e^{-Ts}$ y con sistemas **inestables en lazo abierto** ($P>0$), casos donde [[Routh Hurwitz/index | Routh-Hurwitz]] o el [[Lugar Raices/index | lugar de raíces]] resultan incómodos.

> [!info] Componentes del estudio
> | Nota | Qué aporta |
> |---|---|
> | [[Diagrama Polar]] | trazar $L(j\omega)$: cortes con ejes, comportamiento en $0$ e $\infty$ |
> | [[Criterio Nyquist]] | el conteo $Z=N+P$ y el contorno de Nyquist |
> | [[Margenes MF MG]] | distancia a $-1$ como margen de ganancia y de fase |

---

## Relación con Bode

> [!info] Misma información, distinta vista
> | | [[Bode/index \| Bode]] | Nyquist |
> |---|---|---|
> | Ejes | magnitud/fase vs $\omega$ | plano complejo (Re, Im) |
> | Frecuencia | explícita (eje) | parámetro de la curva |
> | Estabilidad | márgenes | rodeos a $-1$ ($Z=N+P$) |
> | Lazo abierto inestable | difícil | **directo** |
> | Construcción manual | asíntotas (fácil) | punto a punto |

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Objeto | traza polar de $L(j\omega)$, $\omega:-\infty\to\infty$ |
> | Punto crítico | $-1+j0$ |
> | Criterio | $Z=N+P$ |
> | $Z$ | polos de lazo cerrado inestables |
> | $P$ | polos de lazo abierto en el SPD |
> | $N$ | rodeos netos a $-1$ (horario $+$) |
> | Estable $\iff$ | $Z=0$ |

> [!corolario]
> El diagrama de Nyquist concentra en una sola curva cerrada toda la información de estabilidad de lazo cerrado: basta contar rodeos a $-1$ y sumar los polos inestables de lazo abierto. Es la única herramienta clásica que decide estabilidad de forma exacta con retardos y con plantas inestables en lazo abierto, y de paso cuantifica la robustez vía los [[Margenes MF MG | márgenes]].

> [!referencia]
> - Trazado: [[Diagrama Polar]].
> - Criterio exacto: [[Criterio Nyquist]].
> - Robustez (distancia a $-1$): [[Margenes MF MG]].
> - Vista cartesiana: [[Bode/index]].
