---
title: Derivada de Grünwald-Letnikov
tags:
  - ecuaciones
  - difero-integrales
  - teoria
  - calculo-fraccionario
  - grunwald-letnikov
draft: false
aliases:
  - derivada de Grünwald-Letnikov
  - diferencias finitas fraccionarias
  - Grünwald-Letnikov derivative
---

# Derivada de Grünwald-Letnikov $D^{\alpha}_{GL}$

> [!definicion]
> La **derivada de Grünwald-Letnikov** generaliza la definición de la derivada como **límite de
> diferencias finitas**, sustituyendo el orden entero por un orden real $\alpha$:
> $$D^{\alpha}f(x)=\lim_{h\to0}\frac{1}{h^{\alpha}}\sum_{k=0}^{[x/h]}(-1)^{k}\binom{\alpha}{k}f(x-kh),$$
> donde el **coeficiente binomial generalizado** se define mediante la función Gamma,
> $$\binom{\alpha}{k}=\frac{\Gamma(\alpha+1)}{\Gamma(k+1)\,\Gamma(\alpha-k+1)},$$
> que tiene sentido para $\alpha$ **no entero** (la factorial $\alpha!$ por sí sola no lo tendría). El
> símbolo $[x/h]$ es la parte entera: el número de pasos $h$ que caben en $[0,x]$.

> [!info]
> Es una de las tres definiciones equivalentes del [[Calculo Fraccionario/index| cálculo fraccionario]], junto con [[Derivada de Riemann-Liouville| Riemann-Liouville]] (vía integral) y
> [[Derivada de Caputo| Caputo]]. Pertenece al capítulo
> [[4 Ecuaciones Difero-integrales/index| Ecuaciones Difero-integrales]]. Su virtud es ser la
> definición más **directa de implementar**: su forma de suma ya es un esquema numérico. Todas estas
> definiciones son casos del [[Operador Differintegral| operador differintegral]] $D^{\alpha}/I^{-\alpha}$.

---

## Ejemplo

> [!ejemplo] Los primeros pesos para $\alpha=\tfrac12$ y una aproximación con pocos términos
> Queremos los coeficientes $w_k^{(\alpha)}=(-1)^k\binom{\alpha}{k}$ para $\alpha=\tfrac12$. Usamos la
> **recursión** $w_0=1$, $w_k=w_{k-1}\left(1-\dfrac{\alpha+1}{k}\right)$.
>
> **Paso 1 — el primer peso.** Por definición $w_0=1$.
>
> **Paso 2 — recursión con $\alpha+1=\tfrac32$.**
> $$w_1=w_0\left(1-\frac{3/2}{1}\right)=1\cdot\left(-\frac12\right)=-\frac12,$$
> $$w_2=w_1\left(1-\frac{3/2}{2}\right)=-\frac12\cdot\frac14=-\frac18,$$
> $$w_3=w_2\left(1-\frac{3/2}{3}\right)=-\frac18\cdot\frac12=-\frac{1}{16},$$
> $$w_4=w_3\left(1-\frac{3/2}{4}\right)=-\frac{1}{16}\cdot\frac58=-\frac{5}{128}.$$
> Obtenemos $w_0=1,\ w_1=-\tfrac12,\ w_2=-\tfrac18,\ w_3=-\tfrac{1}{16},\ w_4=-\tfrac{5}{128},\dots$
> Salvo el primero, **todos son negativos** y decrecen lentamente: ahí está la **cola larga** (memoria)
> del operador.
>
> **Paso 3 — aproximar $D^{1/2}f(x)$.** Con paso $h$ y truncando en $N$ términos,
> $$D^{1/2}f(x)\approx h^{-1/2}\big[f(x)-\tfrac12 f(x-h)-\tfrac18 f(x-2h)-\tfrac{1}{16}f(x-3h)-\cdots\big].$$
> Tomemos $f(x)=x$ con $x=1$ y $h=0.25$ ($N=4$ términos): $f(1)=1,\ f(0.75)=0.75,\ f(0.5)=0.5,\ f(0.25)=0.25$.
> $$\sum_k w_k f(x-kh)=1(1)-\tfrac12(0.75)-\tfrac18(0.5)-\tfrac{1}{16}(0.25)=1-0.375-0.0625-0.0156=0.5469.$$
> $$D^{1/2}f(1)\approx (0.25)^{-1/2}\cdot 0.5469=2\cdot 0.5469=1.094.$$
>
> **Comparación con el valor exacto.** La fórmula de potencias da $D^{1/2}x=\dfrac{\Gamma(2)}{\Gamma(3/2)}x^{1/2}=\dfrac{1}{\sqrt{\pi}/2}\sqrt{x}=\dfrac{2}{\sqrt{\pi}}\sqrt{x}\approx1.128\sqrt{x}$, que en $x=1$ vale $\approx1.128$. Con solo $4$ términos ya estamos al $3\%$; refinando $h$ converge al valor exacto.

---

## En qué consiste

> [!teoria]
> La idea es **reescribir** la derivada ordinaria como límite de diferencias y luego dejar que el orden
> sea cualquier real. Recordemos las diferencias hacia atrás:
> - orden $1$: $f'(x)=\lim_{h\to0}\dfrac{f(x)-f(x-h)}{h}$ — pesos $(1,-1)$;
> - orden $2$: $f''(x)=\lim_{h\to0}\dfrac{f(x)-2f(x-h)+f(x-2h)}{h^{2}}$ — pesos $(1,-2,1)$.
>
> En ambos los coeficientes son $(-1)^k\binom{n}{k}$ con $n$ entero, y la suma **se corta sola** porque
> $\binom{n}{k}=0$ para $k>n$. Al poner $\alpha$ **no entero**, $\binom{\alpha}{k}$ ya **nunca se anula**:
> la suma se extiende sobre **toda la historia** $f(x),f(x-h),f(x-2h),\dots$ hasta el origen. Esa es la
> **no localidad** —el rasgo esencial del cálculo fraccionario—: $D^{\alpha}f(x)$ depende de los valores
> pasados de $f$, no solo de su entorno inmediato. Para funciones suficientemente suaves, $D^{\alpha}_{GL}$
> **coincide** con [[Derivada de Riemann-Liouville| Riemann-Liouville]]; son dos caras del mismo operador.

> [!algoritmo] Esquema numérico recursivo
> El cálculo eficiente **no** evalúa cada $\binom{\alpha}{k}$ por separado (caro y mal condicionado),
> sino que actualiza los pesos con una recursión de un solo producto:
> $$w_0^{(\alpha)}=1,\qquad w_k^{(\alpha)}=w_{k-1}^{(\alpha)}\left(1-\frac{\alpha+1}{k}\right),\quad k=1,2,\dots$$
> Entonces, con paso $h$ y $N=[x/h]+1$ nodos,
> $$\boxed{\,D^{\alpha}f(x)\approx h^{-\alpha}\sum_{k=0}^{N-1} w_k^{(\alpha)}\,f(x-kh).\,}$$
> **Esquema:**
> 1. Fijar $\alpha$, $h$ y el número de nodos $N$.
> 2. Generar $w_0,\dots,w_{N-1}$ por la recursión (un producto por paso, $O(N)$).
> 3. Acumular $S=\sum_k w_k\,f(x-kh)$.
> 4. Devolver $h^{-\alpha}S$.
>
> Este es el **esquema de Grünwald-Letnikov**, base de los métodos en diferencias finitas para
> derivadas e integrales fraccionarias.

> [!teorema] Equivalencia de la recursión con el binomio
> La recursión $w_k=w_{k-1}\big(1-\tfrac{\alpha+1}{k}\big)$ reproduce exactamente
> $w_k=(-1)^k\binom{\alpha}{k}$.

> [!demostracion] Por inducción sobre $k$
> **Paso 1 — base.** Para $k=0$: $(-1)^0\binom{\alpha}{0}=1=w_0$.
>
> **Paso 2 — razón entre coeficientes consecutivos.** De la definición con Gamma,
> $$\frac{\binom{\alpha}{k}}{\binom{\alpha}{k-1}}=\frac{\Gamma(\alpha+1)/[\Gamma(k+1)\Gamma(\alpha-k+1)]}{\Gamma(\alpha+1)/[\Gamma(k)\Gamma(\alpha-k+2)]}=\frac{\Gamma(k)}{\Gamma(k+1)}\cdot\frac{\Gamma(\alpha-k+2)}{\Gamma(\alpha-k+1)}=\frac{1}{k}\,(\alpha-k+1),$$
> usando $\Gamma(k+1)=k\,\Gamma(k)$ y $\Gamma(\alpha-k+2)=(\alpha-k+1)\Gamma(\alpha-k+1)$.
>
> **Paso 3 — incluir el signo.** Como $w_k=(-1)^k\binom{\alpha}{k}$,
> $$\frac{w_k}{w_{k-1}}=-\frac{\binom{\alpha}{k}}{\binom{\alpha}{k-1}}=-\frac{\alpha-k+1}{k}=\frac{k-\alpha-1}{k}=1-\frac{\alpha+1}{k}.$$
> Luego $w_k=w_{k-1}\big(1-\tfrac{\alpha+1}{k}\big)$, que es la recursión enunciada. $\blacksquare$

> [!proposicion] Recupera lo entero
> Para $\alpha=1$ la suma da $\dfrac{f(x)-f(x-h)}{h}$ (pesos $1,-1$ y $\binom{1}{k}=0$ si $k\ge2$); para
> $\alpha=2$ da la segunda diferencia $\dfrac{f(x)-2f(x-h)+f(x-2h)}{h^{2}}$. Así $D^{\alpha}_{GL}$
> **interpola con continuidad** entre las derivadas enteras al variar $\alpha$.

> [!warning]
> El truncamiento introduce dos fuentes de error: el paso $h$ (orden de aproximación) y el **corte** de
> la cola en $N$ términos. Como los pesos decaen lentamente ($w_k\sim k^{-\alpha-1}$), descartar la cola
> sacrifica memoria lejana; en problemas con historia larga conviene la **memoria corta** (truncar a una
> ventana fija) solo si la física lo justifica. Además, evaluar $\binom{\alpha}{k}$ con factoriales para
> $k$ grande es numéricamente inestable: **siempre** usar la recursión.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Definición | $D^{\alpha}f(x)=\lim_{h\to0}h^{-\alpha}\sum_{k}(-1)^{k}\binom{\alpha}{k}f(x-kh)$ |
> | Binomio generalizado | $\binom{\alpha}{k}=\dfrac{\Gamma(\alpha+1)}{\Gamma(k+1)\Gamma(\alpha-k+1)}$ |
> | Pesos | $w_k^{(\alpha)}=(-1)^k\binom{\alpha}{k}$ |
> | Recursión | $w_0=1,\ w_k=w_{k-1}\big(1-\tfrac{\alpha+1}{k}\big)$ |
> | Caso $\alpha=1$ | $\dfrac{f(x)-f(x-h)}{h}$ |
> | Caso $\alpha=2$ | $\dfrac{f(x)-2f(x-h)+f(x-2h)}{h^{2}}$ |
> | Esquema | $D^{\alpha}f(x)\approx h^{-\alpha}\sum_k w_k\,f(x-kh)$ |

> [!corolario]
> Grünwald-Letnikov es la definición **algorítmica** del cálculo fraccionario: convierte un operador
> integral no local en una suma ponderada de la historia, con pesos calculables por una recursión de
> coste $O(N)$. Por eso es la puerta de entrada a los **métodos numéricos** para derivadas e integrales
> fraccionarias, mientras que [[Derivada de Caputo| Caputo]] domina la formulación analítica.

> [!referencia]
> - Definición equivalente vía integral: [[Derivada de Riemann-Liouville]].
> - El operador unificado: [[Operador Differintegral]].
> - El capítulo y la teoría general: [[Calculo Fraccionario/index]].
