---
title: Volterra de Primera Especie
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - volterra
  - primera-especie
draft: false
aliases:
  - Volterra de primera especie
  - ecuación de Volterra de 1ª especie
  - Volterra first kind
---

# Volterra de Primera Especie

> [!definicion]
> Una **ecuación de Volterra de primera especie** tiene la incógnita $\varphi$ **solo** dentro de la
> integral, sin término libre fuera:
> $$f(x)=\int_{0}^{x}K(x,t)\,\varphi(t)\,dt.$$
> A diferencia de la [[Volterra Segunda Especie| de 2ª especie]], aquí no hay $\varphi(x)$ aislado, de
> modo que el operador no es invertible "directamente". La estrategia es **derivar respecto a $x$** para
> sacar a $\varphi$ de la integral y reducirla a una de 2ª especie.

> [!info]
> Pertenece a la sección [[Volterra/index| Volterra]] del [[3 Ecuaciones Integrales/index| capítulo de ecuaciones integrales]]. Se reduce a la [[Volterra Segunda Especie| de 2ª especie]] por derivación; el
> caso de núcleo **singular** $1/\sqrt{x-t}$ es el [[Problema de Abel| problema de Abel]]. Es un
> **problema inverso**, sensible al ruido. Fuente: Krasnov, *Ecuaciones integrales*, §4.

---

## Ejemplo

> [!ejemplo] Resolver $\int_0^x e^{x-t}\varphi(t)\,dt=f(x)$
> El núcleo es $K(x,t)=e^{x-t}$, así que en la diagonal $K(x,x)=e^0=1\neq 0$. Resolvemos derivando.
>
> **Paso 1 — derivar con la regla de Leibniz.** Para $g(x)=\int_0^x K(x,t)\varphi(t)\,dt$,
> $$g'(x)=K(x,x)\,\varphi(x)+\int_0^x \frac{\partial K}{\partial x}(x,t)\,\varphi(t)\,dt.$$
> Aquí $K(x,x)=1$ y $\partial_x e^{x-t}=e^{x-t}$, luego
> $$f'(x)=\varphi(x)+\int_0^x e^{x-t}\varphi(t)\,dt.$$
>
> **Paso 2 — reconocer la integral original.** Pero $\int_0^x e^{x-t}\varphi(t)\,dt$ es justamente
> $f(x)$, la ecuación de partida. Sustituyendo,
> $$f'(x)=\varphi(x)+f(x)\ \Longrightarrow\ \boxed{\ \varphi(x)=f'(x)-f(x).\ }$$
>
> **Paso 3 — caso concreto.** Para $f(x)=x$ (que cumple $f(0)=0$, condición necesaria):
> $$\varphi(x)=f'(x)-f(x)=1-x.$$
>
> **Verificación.** $\int_0^x e^{x-t}(1-t)\,dt = e^x\!\int_0^x e^{-t}(1-t)\,dt = e^x\big[t e^{-t}\big]_0^x
> = e^x\,x e^{-x}=x=f(x).$ Correcto. La derivación transformó una ecuación de 1ª especie en una
> expresión **explícita** para $\varphi$.

---

## En qué consiste

> [!teoria]
> La 1ª especie es "más difícil" que la 2ª porque integrar es una operación **suavizante**: $f$ siempre
> sale más regular que $\varphi$, así que recuperar $\varphi$ a partir de $f$ obliga a **derivar**, una
> operación que **amplifica** irregularidades. La idea es derivar una vez respecto a $x$: la regla de
> Leibniz hace aparecer el término de frontera $K(x,x)\varphi(x)$, que pone a $\varphi$ **fuera** de la
> integral. Si $K(x,x)\neq 0$, dividir por él deja la ecuación con la forma estándar de 2ª especie.

> [!teorema] Reducción a segunda especie
> Sea $f(x)=\displaystyle\int_0^x K(x,t)\,\varphi(t)\,dt$ con $K$, $K_x=\partial K/\partial x$ y $f$ de
> clase $C^1$, $f(0)=0$ y $K(x,x)\neq 0$. Entonces es equivalente a la Volterra de **2ª especie**
> $$\varphi(x)=\frac{f'(x)}{K(x,x)}-\frac{1}{K(x,x)}\int_0^x K_x(x,t)\,\varphi(t)\,dt.$$

> [!demostracion]
> **Paso 1 — derivar la ecuación.** Aplicamos $\dfrac{d}{dx}$ a ambos lados. El lado izquierdo da
> $f'(x)$; el derecho, por la **regla de Leibniz** para integrales con límite variable,
> $$\frac{d}{dx}\int_0^x K(x,t)\varphi(t)\,dt = K(x,x)\,\varphi(x)+\int_0^x K_x(x,t)\,\varphi(t)\,dt.$$
>
> **Paso 2 — igualar.** Por tanto $f'(x)=K(x,x)\,\varphi(x)+\displaystyle\int_0^x K_x(x,t)\varphi(t)\,dt$.
>
> **Paso 3 — despejar $\varphi$.** Como $K(x,x)\neq 0$, dividimos:
> $$\varphi(x)=\frac{f'(x)}{K(x,x)}-\frac{1}{K(x,x)}\int_0^x K_x(x,t)\,\varphi(t)\,dt,$$
> que es una Volterra de 2ª especie con núcleo $-K_x/K(x,x)$ y término libre $f'/K(x,x)$.
>
> **Paso 4 — consistencia.** La condición $f(0)=0$ es necesaria: en $x=0$ la integral original es
> nula, luego $f(0)=0$ es **obligatorio** para que exista solución. $\blacksquare$

> [!warning]
> Si $K(x,x)=0$ la reducción **falla**: el término que sacaba a $\varphi$ de la integral desaparece y
> hay que derivar de nuevo (o la ecuación es genuinamente más singular). El caso emblemático es el
> [[Problema de Abel| núcleo de Abel]] $K=1/\sqrt{x-t}$, donde $K(x,x)=\infty$: ahí la inversión no se
> hace con una derivada entera sino con una **derivación fraccionaria** de orden $1/2$.

> [!info] Es un problema inverso
> La 1ª especie es el prototipo de **problema inverso**: se observa el efecto integrado $f$ y se
> reconstruye la causa $\varphi$. Como la solución pasa por **derivar** $f$, pequeñas perturbaciones
> (ruido de medición) en $f$ se amplifican en $\varphi$. Por eso estos problemas se llaman **mal
> planteados** y, en la práctica, requieren regularización.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Forma | $f(x)=\int_0^x K(x,t)\varphi(t)\,dt$ (incógnita solo dentro) |
> | Condición | $f(0)=0$; reducción si $K(x,x)\neq 0$ |
> | Método | derivar (Leibniz) → [[Volterra Segunda Especie\|2ª especie]] |
> | Resultado | $\varphi=\dfrac{f'}{K(x,x)}-\dfrac{1}{K(x,x)}\int_0^x K_x\varphi\,dt$ |
> | Caso singular | $K(x,x)=0$ → [[Problema de Abel\|Abel]], derivada fraccionaria |

> [!corolario]
> La 1ª especie no es un tipo aparte: **derivando** se convierte en 2ª especie, siempre que el núcleo
> no se anule en la diagonal. Cuando sí se anula —como en Abel— aparece la verdadera dificultad y, con
> ella, el cálculo fraccionario. Derivar es la llave, pero también la fuente de su carácter inverso y
> sensible al ruido.

> [!referencia]
> - La forma a la que se reduce: [[Volterra Segunda Especie]].
> - El caso singular que escapa al método: [[Problema de Abel]].
> - Vuelta al índice: [[Volterra/index]].
