---
title: Problema de Abel
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - volterra
  - abel
draft: false
aliases:
  - problema de Abel
  - ecuación integral de Abel
  - tautócrona
  - Abel integral equation
---

# Problema de Abel

> [!definicion]
> La **ecuación integral de Abel** es una Volterra de **primera especie** con **núcleo singular**
> $1/\sqrt{x-t}$:
> $$f(x)=\int_{0}^{x}\frac{\varphi(t)}{\sqrt{x-t}}\,dt.$$
> Aunque el núcleo se vuelve infinito en $t=x$, la integral converge, y la ecuación se **invierte**
> explícitamente:
> $$\varphi(x)=\frac{1}{\pi}\,\frac{d}{dx}\int_{0}^{x}\frac{f(t)}{\sqrt{x-t}}\,dt.$$
> Históricamente es la **primera** ecuación integral resuelta (Abel, 1823).

> [!info]
> Caso emblemático de [[Volterra/index| Volterra de primera especie]] con núcleo
> [[Singulares/index| singular]]. Es de **convolución** ($K=K(x-t)$), así que también se resuelve con
> [[Ecuaciones de Convolucion| transformada de Laplace]]. Su origen es un problema de mecánica: la
> curva de descenso en tiempo prescrito.

---

## Ejemplo

> [!ejemplo] La tautócrona: una curva de tiempo de bajada constante
> ![[abel_tautocrona.svg|470]]
>
> **El problema físico de Abel.** Una cuenta resbala sin rozamiento por una curva bajo la gravedad. Si
> parte del reposo a la altura $y$, el **tiempo de bajada** hasta el fondo depende de la forma de la
> curva. Por conservación de energía, la velocidad a la altura $h$ es $v=\sqrt{2g(y-h)}$, y el tiempo
> total es
> $$T(y)=\int_0^y\frac{s'(h)}{\sqrt{2g(y-h)}}\,dh,$$
> con $s'(h)$ la longitud de arco por unidad de altura. Es **exactamente** una ecuación de Abel: dado
> el tiempo $T(y)$, hallar la forma $\varphi(h)=s'(h)$.
>
> **La tautócrona.** Si se pide que $T(y)=T_0$ sea **constante** (mismo tiempo de bajada desde
> *cualquier* altura), al invertir la ecuación de Abel resulta $s'(h)\propto 1/\sqrt{h}$, que integrada
> da una **cicloide**. Por eso un péndulo cicloidal es **isócrono** (Huygens): la cuenta tarda lo mismo
> en bajar salga de donde salga.

---

## En qué consiste

> [!teorema] Fórmula de inversión de Abel
> Si $f$ es continua con $f(0)=0$, la solución de $f(x)=\displaystyle\int_0^x\frac{\varphi(t)}{\sqrt{x-t}}\,dt$ es
> $$\varphi(x)=\frac{1}{\pi}\frac{d}{dx}\int_0^x\frac{f(t)}{\sqrt{x-t}}\,dt.$$

> [!demostracion] Por convolución / transformada de Laplace
> **Paso 1 — reconocer la convolución.** El lado derecho es $f=K*\varphi$ con $K(x)=x^{-1/2}$. La
> transformada de Laplace del núcleo es $\mathcal{L}\{x^{-1/2}\}=\sqrt{\pi/s}$.
>
> **Paso 2 — transformar.** Por el teorema de convolución, $F(s)=\sqrt{\pi/s}\;\Phi(s)$, de donde
> $$\Phi(s)=\frac{1}{\sqrt{\pi}}\,\sqrt{s}\,F(s).$$
>
> **Paso 3 — preparar la antitransformada.** Escribimos $\sqrt{s}\,F(s)=\dfrac{1}{\sqrt{s}}\cdot s\,F(s)$.
> Como $sF(s)\leftrightarrow f'(x)$ (con $f(0)=0$) y $1/\sqrt{s}\leftrightarrow 1/\sqrt{\pi x}$,
> $$\Phi(s)=\frac{1}{\pi}\,\frac{1}{\sqrt{s}}\,\big(sF(s)\big)\ \Longleftrightarrow\ \varphi(x)=\frac{1}{\pi}\int_0^x\frac{f'(t)}{\sqrt{x-t}}\,dt,$$
> que, integrando por partes, equivale a $\varphi(x)=\dfrac{1}{\pi}\dfrac{d}{dx}\displaystyle\int_0^x\dfrac{f(t)}{\sqrt{x-t}}\,dt$. $\blacksquare$
>
> La clave es que **convolucionar $1/\sqrt{x}$ consigo mismo da una constante** ($\pi$): $K*K=\pi$, así
> que aplicar el núcleo "dos veces" deshace la integral —una **media derivada** repetida es una
> derivada entera—.

> [!info] Conexión con el cálculo fraccionario
> La ecuación de Abel **es** una **integral fraccionaria de orden $1/2$**: $f=\sqrt{\pi}\,I^{1/2}\varphi$
> en el sentido de [[Calculo Fraccionario/index| Riemann-Liouville]]. Invertirla es aplicar la
> **derivada fraccionaria** $D^{1/2}$. Abel inventó, sin nombrarlo, el cálculo fraccionario.

> [!algoritmo] Resolver una ecuación de Abel
> 1. Verifica la forma $f(x)=\int_0^x\varphi(t)/\sqrt{x-t}\,dt$ (y $f(0)=0$).
> 2. Aplica la fórmula de inversión $\varphi=\frac{1}{\pi}\frac{d}{dx}\int_0^x f(t)/\sqrt{x-t}\,dt$.
> 3. Equivalente: vía Laplace, $\Phi(s)=\frac{1}{\sqrt{\pi}}\sqrt{s}\,F(s)$.

> [!warning]
> Es de **primera especie** con núcleo **singular**: pequeñas perturbaciones de $f$ pueden amplificarse
> (la inversión deriva). Es un **problema inverso** —se mide $T(y)$ y se reconstruye la curva—, con la
> sensibilidad típica de esos problemas.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Ecuación | $f(x)=\int_0^x \varphi(t)/\sqrt{x-t}\,dt$ |
> | Inversión | $\varphi=\frac1\pi\frac{d}{dx}\int_0^x f/\sqrt{x-t}\,dt$ |
> | Método | convolución / Laplace ($\mathcal{L}\{x^{-1/2}\}=\sqrt{\pi/s}$) |
> | Física | curva de descenso; tautócrona = cicloide |
> | Generaliza | núcleo $1/(x-t)^\alpha$, $0<\alpha<1$ |

> [!corolario]
> Abel resolvió la primera ecuación integral de la historia con una idea que sigue viva: el núcleo
> $1/\sqrt{x-t}$ es una **media integración**, y aplicarlo dos veces integra una vez. De ahí salen el
> cálculo fraccionario y la solución de la tautócrona (la cicloide isócrona).

> [!referencia]
> - El método general de convolución: [[Ecuaciones de Convolucion]].
> - La generalización singular: [[Ecuacion de Abel Generalizada]].
> - El cálculo que anticipó: [[Calculo Fraccionario/index]].
