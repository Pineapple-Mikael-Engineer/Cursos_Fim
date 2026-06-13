---
title: Transformada de Laplace
tags:
  - control-clasico
  - teoria
  - modelado
draft: false
aliases:
  - Laplace
  - transformada de Laplace
---

# Transformada de Laplace

> [!definicion]
> La transformada de Laplace convierte una función del tiempo $f(t)$ (con $t\ge 0$) en una función $F(s)$ de variable compleja $s=\sigma+j\omega$:
> $$F(s)=\mathcal{L}\{f(t)\}=\int_{0^-}^{\infty} f(t)\,e^{-st}\,dt.$$
> Su utilidad en control es que **transforma EDOs en ecuaciones algebraicas** (derivar $\to$ multiplicar por $s$) y la **convolución en producto**, de modo que un sistema LTI queda como $Y(s)=G(s)\,U(s)$.

> [!info]
> Es la herramienta base del bloque de [[Funcion Transferencia/index | modelado]]. Se apoya en su [[Tabla Pares | tabla de pares]] $f(t)\leftrightarrow F(s)$, sus [[Propiedades | propiedades operativas]] y el teorema de [[Convolucion | convolución]]. El resultado directo es la [[Funcion Transferencia/index | función de transferencia]].

---

## Ejemplo

> [!ejemplo] De EDO a función de transferencia
> Modelar $\dot{y}+2y=u$ con $y(0)=y_0$ y obtener la respuesta a un escalón $u(t)=1$, $y_0=0$.
>
> **Paso 1 — Transformar término a término** (propiedad de [[Propiedades | derivación]] $\mathcal{L}\{\dot y\}=sY-y(0)$):
> $$sY(s)-y_0+2Y(s)=U(s).$$
>
> **Paso 2 — Despejar $Y(s)$** (queda algebraico):
> $$(s+2)Y(s)=U(s)+y_0\;\Longrightarrow\;Y(s)=\underbrace{\frac{1}{s+2}}_{G(s)}U(s)+\frac{y_0}{s+2}.$$
> El primer término es la respuesta forzada ($G(s)=1/(s+2)$ es la FT); el segundo, la respuesta a la CI.
>
> **Paso 3 — Sustituir entrada** ($U(s)=1/s$, $y_0=0$) y expandir en [[Tabla Pares | fracciones parciales]]:
> $$Y(s)=\frac{1}{s(s+2)}=\frac{1/2}{s}-\frac{1/2}{s+2}.$$
>
> **Paso 4 — Antitransformar con la tabla:**
> $$y(t)=\tfrac{1}{2}\bigl(1-e^{-2t}\bigr),\qquad t\ge 0.$$
> Valor final $y(\infty)=\tfrac12$ (coincide con $\lim_{s\to0}sY(s)$), polo en $s=-2$ → estable, constante de tiempo $\tau=1/2$ s.

---

## En qué consiste

> [!teoria]
> $F(s)$ "pesa" la señal $f(t)$ contra una familia de exponenciales complejas $e^{-st}$. La parte real $\sigma$ controla un decaimiento que **fuerza la convergencia** de la integral; la parte imaginaria $j\omega$ aporta el contenido oscilatorio. Por eso $s$ unifica en una sola variable el crecimiento/decaimiento y la frecuencia, y los **polos** de $F(s)$ (raíces del denominador) determinan la forma de $f(t)$: reales negativos → exponenciales decrecientes, complejos → senoides amortiguadas.

> [!definicion] Transformada inversa
> $$f(t)=\mathcal{L}^{-1}\{F(s)\}=\frac{1}{2\pi j}\int_{\sigma-j\infty}^{\sigma+j\infty}F(s)\,e^{st}\,ds.$$
> En la práctica nunca se calcula esta integral: se descompone $F(s)$ en [[Tabla Pares | fracciones parciales]] y se identifica cada término en la tabla de pares.

> [!teorema] Condiciones de existencia
> La integral converge (existe $F(s)$) si:
> 1. $f(t)$ es continua por tramos en $[0,\infty)$.
> 2. $f(t)$ es de **orden exponencial**: existen $M>0$ y $\sigma_0$ con $|f(t)|\le M e^{\sigma_0 t}$.
>
> Entonces $F(s)$ existe para $\Re(s)>\sigma_0$ (región de convergencia, ROC).

---

## Herramientas

> [!info] Pares fundamentales
> Subconjunto más usado (versión extendida en [[Tabla Pares | tabla de pares]]):
>
> | $f(t)$, $t\ge0$ | $F(s)$ | ROC |
> |---|---|---|
> | $\delta(t)$ | $1$ | todo $s$ |
> | $u(t)$ (escalón) | $\dfrac{1}{s}$ | $\Re(s)>0$ |
> | $t^n$ | $\dfrac{n!}{s^{n+1}}$ | $\Re(s)>0$ |
> | $e^{-at}$ | $\dfrac{1}{s+a}$ | $\Re(s)>-a$ |
> | $\sin(\omega t)$ | $\dfrac{\omega}{s^2+\omega^2}$ | $\Re(s)>0$ |
> | $\cos(\omega t)$ | $\dfrac{s}{s^2+\omega^2}$ | $\Re(s)>0$ |
> | $e^{-at}\sin(\omega t)$ | $\dfrac{\omega}{(s+a)^2+\omega^2}$ | $\Re(s)>-a$ |
> | $e^{-at}\cos(\omega t)$ | $\dfrac{s+a}{(s+a)^2+\omega^2}$ | $\Re(s)>-a$ |

> [!info] Propiedades operativas
> Subconjunto clave (demostraciones y ejemplos en [[Propiedades | propiedades]]):
>
> | Propiedad | $f(t)$ | $F(s)$ |
> |---|---|---|
> | Linealidad | $a f_1+b f_2$ | $a F_1+b F_2$ |
> | Derivación | $f'(t)$ | $sF(s)-f(0^-)$ |
> | Derivación 2.ª | $f''(t)$ | $s^2F(s)-sf(0^-)-f'(0^-)$ |
> | Integración | $\int_0^t f\,d\tau$ | $\dfrac{1}{s}F(s)$ |
> | Retardo en $t$ | $f(t-a)u(t-a)$ | $e^{-as}F(s)$ |
> | Traslación en $s$ | $e^{-at}f(t)$ | $F(s+a)$ |
> | [[Convolucion \| Convolución]] | $(f*g)(t)$ | $F(s)\,G(s)$ |
> | Valor final | $\lim_{t\to\infty}f(t)$ | $\lim_{s\to0}sF(s)$ |

> [!info] Función de transferencia
> Para un sistema LTI con CI nulas, la FT es el cociente de transformadas:
> $$G(s)=\frac{\mathcal{L}\{\text{salida}\}}{\mathcal{L}\{\text{entrada}\}}=\frac{Y(s)}{U(s)}.$$
> Es el objeto central del resto del curso → [[Funcion Transferencia/index | función de transferencia]].

> [!info] En MATLAB
> ```matlab
> syms t s y0
> Y = laplace(diff(sym('y(t)')) + 2*sym('y(t)'));  % transformar EDO
> G = tf(1, [1 2]);        % G(s) = 1/(s+2)
> step(G)                  % respuesta al escalon
> ilaplace(1/(s*(s+2)))    % antitransformar -> 1/2 - exp(-2t)/2
> ```

---

## Limitaciones

> [!warning]
> 1. **Unilateral:** solo describe señales para $t\ge0$; ignora el pasado $t<0$.
> 2. **Convergencia:** requiere que $f(t)$ sea de orden exponencial; señales como $e^{t^2}$ no tienen transformada.
> 3. **Solo LTI:** no aplica directamente a sistemas no lineales o variantes en el tiempo; antes hay que [[Linealizacion/index | linealizar]].

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Definición | $F(s)=\int_{0^-}^{\infty}f(t)e^{-st}dt$ |
> | Variable | $s=\sigma+j\omega$ (compleja) |
> | Efecto clave | EDO → ecuación algebraica; $\dfrac{d}{dt}\to s$ |
> | Convolución | $f*g \to F(s)G(s)$ |
> | Inversa | fracciones parciales + tabla de pares |
> | Sistema LTI | $Y(s)=G(s)U(s)$ |

> [!corolario]
> La transformada de Laplace es el cambio de variable que linealiza el cálculo dinámico: transformar una EDO la vuelve álgebra en $s$, despejar $Y(s)$ y antitransformar con [[Tabla Pares | tabla de pares]] y [[Propiedades | propiedades]] devuelve $y(t)$. El cociente $Y(s)/U(s)$ con CI nulas es la [[Funcion Transferencia/index | función de transferencia]], piedra angular de todo el análisis de control clásico.

> [!referencia]
> - Tabla de pares $f(t)\leftrightarrow F(s)$: [[Tabla Pares]].
> - Propiedades operativas y demostraciones: [[Propiedades]].
> - Teorema de convolución: [[Convolucion]].
> - Objeto resultante: [[Funcion Transferencia/index]].
