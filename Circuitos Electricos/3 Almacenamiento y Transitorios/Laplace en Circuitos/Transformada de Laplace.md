---
title: Transformada de Laplace
tags:
  - circuitos-electricos
  - teoria
  - transitorios
  - laplace
draft: false
aliases:
  - transformada de laplace
  - Laplace transform
  - antitransformada de laplace
  - transformada inversa de laplace
  - pares de laplace
---

# Transformada de Laplace

> [!definicion]
> La **transformada de Laplace** de una función $f(t)$ (causal, con $f(t)=0$ para $t<0$) es
> $$F(s)=\mathcal{L}\{f(t)\}=\int_0^{\infty} f(t)\,e^{-st}\,dt,$$
> donde $s=\sigma+j\omega$ es una variable **compleja**. Convierte funciones del tiempo $f(t)$ en funciones de $s$, y transforma las operaciones del cálculo —**derivar** e **integrar**— en simple **álgebra**.

> [!info]
> La base matemática de [[Laplace en Circuitos/index| Laplace en circuitos]] ([[3 Almacenamiento y Transitorios/index| capítulo 3]]). Sobre ella se construyen [[Circuitos en el Dominio de s]] y la [[Solucion de Transitorios con Laplace| solución de transitorios]]; sus entradas típicas son las [[Funciones Singulares]]. Fraile Mora, Apéndice 2.

---

## Ejemplo

> [!ejemplo]
> **Transformar la exponencial $e^{-at}$.**
>
> Es el par del que salen casi todos los demás. Aplicando la definición:
> $$\mathcal{L}\{e^{-at}\}=\int_0^\infty e^{-at}\,e^{-st}\,dt=\int_0^\infty e^{-(s+a)t}\,dt.$$
> Integrando la exponencial y evaluando (la cota superior se anula si $\operatorname{Re}(s)>-a$):
> $$=\left[-\frac{e^{-(s+a)t}}{s+a}\right]_0^\infty=0-\left(-\frac{1}{s+a}\right).$$
>
> > [!solucion]
> > $$\mathcal{L}\{e^{-at}\}=\frac{1}{s+a}.$$
> > Con $a=0$ se recupera el escalón $\mathcal{L}\{u(t)\}=1/s$; derivando respecto de $a$ se obtiene $t\,e^{-at}\to 1/(s+a)^2$; y con $a=j\omega$ aparecen el seno y el coseno. De este único cálculo nace casi toda la tabla de pares.

---

## En qué consiste

> [!teoria] Pares básicos
> La tabla siguiente reúne las transformadas de las señales que aparecen una y otra vez al excitar un circuito. Se leen en ambos sentidos: hacia la derecha para **transformar** la excitación, hacia la izquierda para **antitransformar** la respuesta.
>
> | $f(t)\;(t\ge 0)$ | $F(s)=\mathcal{L}\{f(t)\}$ |
> |:---|:---|
> | Impulso $\delta(t)$ | $1$ |
> | Escalón $u(t)$ | $\dfrac{1}{s}$ |
> | Rampa $t$ | $\dfrac{1}{s^2}$ |
> | $t^n$ | $\dfrac{n!}{s^{n+1}}$ |
> | $e^{-at}$ | $\dfrac{1}{s+a}$ |
> | $\sin\omega t$ | $\dfrac{\omega}{s^2+\omega^2}$ |
> | $\cos\omega t$ | $\dfrac{s}{s^2+\omega^2}$ |
> | $e^{-at}\sin\omega t$ | $\dfrac{\omega}{(s+a)^2+\omega^2}$ |
> | $e^{-at}\cos\omega t$ | $\dfrac{s+a}{(s+a)^2+\omega^2}$ |
>
> Los tres últimos no son nuevos: son los anteriores con el **desplazamiento en frecuencia** $s\to s+a$, que multiplica la señal por $e^{-at}$ (la amortigua).

> [!proposicion] Propiedades operacionales
> Estas reglas evitan volver a la integral de definición: combinándolas con los pares básicos se transforma (y antitransforma) casi cualquier expresión.
>
> | Propiedad | Regla |
> |:---|:---|
> | Linealidad | $\mathcal{L}\{a\,f+b\,g\}=a\,F(s)+b\,G(s)$ |
> | Derivada $1^\text{er}$ orden | $\mathcal{L}\{f'\}=s\,F(s)-f(0)$ |
> | Derivada $2^\text{do}$ orden | $\mathcal{L}\{f''\}=s^2 F(s)-s\,f(0)-f'(0)$ |
> | Integral | $\mathcal{L}\!\left\{\displaystyle\int_0^t f(\tau)\,d\tau\right\}=\dfrac{F(s)}{s}$ |
> | Despl. en frecuencia | $\mathcal{L}\{e^{-at}f(t)\}=F(s+a)$ |
> | Despl. en tiempo (retardo) | $\mathcal{L}\{f(t-a)\,u(t-a)\}=e^{-as}F(s)$ |
> | Valor inicial | $f(0^+)=\displaystyle\lim_{s\to\infty} s\,F(s)$ |
> | Valor final | $f(\infty)=\displaystyle\lim_{s\to 0} s\,F(s)$ |
>
> La propiedad de la **derivada** es la clave para los circuitos: al transformar las ecuaciones de $L$ y $C$, los términos $-f(0)$ inyectan las **condiciones iniciales** directamente en el álgebra, sin tratarlas aparte.

> [!teoria] Antitransformada por fracciones parciales
> Resuelto el circuito en $s$, la incógnita queda como un cociente de polinomios $F(s)=N(s)/D(s)$. Para volver al tiempo se **descompone en fracciones parciales**, de modo que cada término coincida con una fila de la tabla de pares, y se antitransforma **término a término** por linealidad. La naturaleza de los **polos** (raíces de $D(s)$) dicta la forma de $f(t)$:
> - **Polos reales** $s=-a$ → exponenciales $e^{-at}$ (modos sobreamortiguados, decaimiento puro).
> - **Polos complejos conjugados** $s=-a\pm j\omega$ → senos/cosenos **amortiguados** $e^{-at}\sin\omega t$, $e^{-at}\cos\omega t$ (oscilaciones que decaen).
>
> Así, la posición de los polos en el plano $s$ se traduce de inmediato en el comportamiento temporal del transitorio.

> [!warning]
> La propiedad de la derivada $\mathcal{L}\{f'\}=sF(s)-f(0)$ es la que **incorpora las condiciones iniciales**: nunca olvidar el término $f(0)$, o el transitorio saldrá incompleto. Además, la transformada supone $f(t)=0$ para $t<0$ (señal **causal**): toda la información se refiere a $t\ge 0$, y por eso el límite inferior de la integral es $0$.

## Resumen

> [!resumen]
> | $f(t)$ | $F(s)$ |
> |:---|:---|
> | $\delta(t)$ | $1$ |
> | $u(t)$ | $1/s$ |
> | $t$ | $1/s^2$ |
> | $e^{-at}$ | $1/(s+a)$ |
> | $\sin\omega t$ | $\omega/(s^2+\omega^2)$ |
> | $\cos\omega t$ | $s/(s^2+\omega^2)$ |
> | $f'(t)$ | $sF(s)-f(0)$ |
> | $\int_0^t f$ | $F(s)/s$ |

> [!corolario]
> Laplace **cambia cálculo por álgebra**: ecuaciones diferenciales con condiciones iniciales se vuelven ecuaciones algebraicas en $s$. Es lo que permite tratar [[Circuitos en el Dominio de s| los circuitos en el dominio de $s$]] como si fueran resistivos y obtener el transitorio resolviendo y antitransformando.

> [!referencia]
> Fraile Mora, Apéndice 2. Se aplica en: [[Circuitos en el Dominio de s]] y [[Solucion de Transitorios con Laplace]]. Excitaciones: [[Funciones Singulares]].
