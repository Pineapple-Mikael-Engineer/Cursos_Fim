---
title: Serie de Taylor para Linealización
tags:
  - control-clasico
  - teoria
  - linealizacion
draft: false
aliases:
  - serie taylor
  - expansion taylor
  - aproximacion lineal
---

# Serie de Taylor para Linealización

> [!definicion]
> La **serie de Taylor** aproxima una función suave por un polinomio centrado en $x_0$. La **aproximación lineal** (primer orden) conserva solo la recta tangente:
> $$f(x)\approx f(x_0)+f'(x_0)\,(x-x_0).$$
> En el caso vectorial $\mathbf{f}(\mathbf{x})$, la derivada $f'$ se sustituye por la [[Jacobiano | matriz jacobiana]]: $\mathbf{f}(\mathbf{x})\approx\mathbf{f}(\mathbf{x}_0)+\partial_{\mathbf{x}}\mathbf{f}|_{\mathbf{x}_0}(\mathbf{x}-\mathbf{x}_0)$. Esta es la base teórica de la [[Linealizacion/index | linealización]].

> [!info]
> Nota de la carpeta [[Linealizacion/index | Linealización]]. Justifica por qué el método del [[Jacobiano | jacobiano]] es lícito y acota su error; el cambio de variable que lo acompaña está en [[Variables Desviacion | variables de desviación]].

---

## Ejemplo

> [!ejemplo]
> **Linealizar $\sin\theta$ para el péndulo, con números.** Aproximar $f(\theta)=\sin\theta$ alrededor de $\theta_0=0$ y medir el error.
>
> **Paso 1 — Derivadas en $\theta_0=0$:** $f(0)=\sin 0=0$, $f'(\theta)=\cos\theta\Rightarrow f'(0)=1$.
>
> **Paso 2 — Aproximación lineal:**
> $$\sin\theta\approx f(0)+f'(0)(\theta-0)=\theta.$$
> Esta es la célebre aproximación de **ángulos pequeños** $\sin\theta\approx\theta$.
>
> **Paso 3 — Error.** La serie completa es $\sin\theta=\theta-\dfrac{\theta^3}{6}+\dfrac{\theta^5}{120}-\dots$, así que el primer término despreciado es $-\theta^3/6$:
>
> | $\theta$ (rad) | $\theta$ (grados) | $\sin\theta$ | $\theta$ | Error rel. |
> |---|---|---|---|---|
> | $0.1$ | $5.7^\circ$ | $0.09983$ | $0.1$ | $0.17\%$ |
> | $0.2$ | $11.5^\circ$ | $0.19867$ | $0.2$ | $0.67\%$ |
> | $0.5$ | $28.6^\circ$ | $0.47943$ | $0.5$ | $4.3\%$ |
> | $1.0$ | $57.3^\circ$ | $0.84147$ | $1.0$ | $18.8\%$ |
>
> **Regla práctica:** $\theta<0.5$ rad ($\approx30^\circ$) mantiene el error por debajo del $5\%$. Por eso el modelo lineal del péndulo solo vale para oscilaciones pequeñas.

> [!ejemplo]
> **Aplicación al sistema completo.** Modelo $\dot{x}_1=x_2$, $\dot{x}_2=-\frac{g}{l}\sin x_1$, equilibrio $x_{10}=x_{20}=0$. Sustituyendo la expansión de $\sin x_1$:
> $$\dot{x}_2=-\frac{g}{l}\Big(x_1-\tfrac{x_1^3}{6}+\dots\Big)=-\frac{g}{l}x_1+\underbrace{\frac{g}{6l}x_1^3+\dots}_{\text{se desprecia}}.$$
> El modelo linealizado queda $\dot{x}_1=x_2$, $\dot{x}_2=-\frac{g}{l}x_1$: un oscilador armónico de frecuencia $\sqrt{g/l}$. El término cúbico despreciado es justo lo que distingue el péndulo real del armónico ideal.

---

## En qué consiste

> [!definicion] Serie de Taylor (escalar)
> Para $f(x)$ infinitamente diferenciable alrededor de $x_0$:
> $$f(x)=f(x_0)+f'(x_0)(x-x_0)+\frac{f''(x_0)}{2!}(x-x_0)^2+\frac{f'''(x_0)}{3!}(x-x_0)^3+\dots$$

> [!definicion] Serie de Taylor (vectorial)
> Para $\mathbf{f}(\mathbf{x})$ con $\mathbf{x}\in\mathbb{R}^n$:
> $$\mathbf{f}(\mathbf{x})=\mathbf{f}(\mathbf{x}_0)+\left.\frac{\partial\mathbf{f}}{\partial\mathbf{x}}\right|_{\mathbf{x}_0}(\mathbf{x}-\mathbf{x}_0)+\text{(orden superior)},$$
> donde $\partial_{\mathbf{x}}\mathbf{f}$ es la [[Jacobiano | matriz jacobiana]].

> [!teorema] Linealización de un sistema no lineal
> Dado $\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},\mathbf{u})$ con equilibrio $(\mathbf{x}_0,\mathbf{u}_0)$, $\mathbf{f}(\mathbf{x}_0,\mathbf{u}_0)=\mathbf{0}$:
> $$\delta\dot{\mathbf{x}}=\mathbf{A}\,\delta\mathbf{x}+\mathbf{B}\,\delta\mathbf{u},\qquad \mathbf{A}=\left.\frac{\partial\mathbf{f}}{\partial\mathbf{x}}\right|_0,\ \ \mathbf{B}=\left.\frac{\partial\mathbf{f}}{\partial\mathbf{u}}\right|_0.$$

> [!demostracion] Paso 1 — Expandir en Taylor
> Alrededor de $(\mathbf{x}_0,\mathbf{u}_0)$:
> $$\mathbf{f}(\mathbf{x},\mathbf{u})=\mathbf{f}(\mathbf{x}_0,\mathbf{u}_0)+\mathbf{A}(\mathbf{x}-\mathbf{x}_0)+\mathbf{B}(\mathbf{u}-\mathbf{u}_0)+\text{SO},$$
> donde SO agrupa los términos de orden $\ge 2$: $(\mathbf{x}-\mathbf{x}_0)^2$, $(\mathbf{u}-\mathbf{u}_0)^2$, productos cruzados y superiores.

> [!demostracion] Paso 2 — Anular el término constante
> Por ser punto de equilibrio, $\mathbf{f}(\mathbf{x}_0,\mathbf{u}_0)=\mathbf{0}$, que desaparece de la expansión.

> [!demostracion] Paso 3 — Cambiar a variables de desviación
> Con $\delta\mathbf{x}=\mathbf{x}-\mathbf{x}_0$, $\delta\mathbf{u}=\mathbf{u}-\mathbf{u}_0$ y $\dot{\mathbf{x}}=\delta\dot{\mathbf{x}}$ (pues $\mathbf{x}_0$ es constante):
> $$\delta\dot{\mathbf{x}}=\mathbf{A}\,\delta\mathbf{x}+\mathbf{B}\,\delta\mathbf{u}+\text{SO}.$$

> [!demostracion] Paso 4 — Despreciar el orden superior
> Si $\delta\mathbf{x},\delta\mathbf{u}$ son pequeños, SO es despreciable (si $\delta x=0.01$, $(\delta x)^2=10^{-4}$). Queda $\delta\dot{\mathbf{x}}\approx\mathbf{A}\,\delta\mathbf{x}+\mathbf{B}\,\delta\mathbf{u}$. $\blacksquare$

> [!info] Equivalencia con el jacobiano
> El método del [[Jacobiano | jacobiano]] **es** exactamente la aproximación de Taylor de primer orden: las parciales $\partial f_i/\partial x_j$ son los coeficientes lineales, se evalúan en el punto de operación y se desprecia todo lo demás.

---

## Error de la aproximación

> [!teorema] Resto de Lagrange
> En el caso escalar existe $\xi$ entre $x$ y $x_0$ tal que
> $$f(x)=f(x_0)+f'(x_0)(x-x_0)+\frac{f''(\xi)}{2}(x-x_0)^2,$$
> luego el error de la recta tangente es $E=\dfrac{f''(\xi)}{2}(x-x_0)^2$, **proporcional a $(x-x_0)^2$**: al reducir la desviación a la mitad, el error cae a la cuarta parte.

> [!ejemplo] Catálogo de linealizaciones útiles
> Alrededor de $0$:
> $$\sin\theta\approx\theta,\qquad \cos\theta\approx 1,\qquad e^{x}\approx 1+x,\qquad \ln(1+x)\approx x,\qquad (1+x)^n\approx 1+nx.$$
> Caso degenerado: $f(x)=x^2$ da $f(0)=0$, $f'(0)=0$, luego $x^2\approx 0$ — la linealización **pierde toda la dinámica**. Cuando la parcial dominante se anula, hay que linealizar en otro punto o usar análisis no lineal.

---

## Limitaciones

> [!warning]
> 1. **Fuera del equilibrio** la aproximación lineal fracasa (error $\propto$ desviación al cuadrado).
> 2. **No captura bifurcaciones:** cambios cualitativos de la dinámica al variar parámetros.
> 3. **No captura ciclos límite** ni oscilaciones autosostenidas.
> 4. **Derivada nula:** si $f'(x_0)=0$, el comportamiento dominante es cuadrático y el modelo lineal es inservible (caso $x^2$).

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Aproximación lineal | $f(x)\approx f(x_0)+f'(x_0)(x-x_0)$ |
> | Vectorial | $\mathbf{f}\approx\mathbf{f}(\mathbf{x}_0)+\mathbf{J}(\mathbf{x}-\mathbf{x}_0)$ |
> | Error | $E=\tfrac{1}{2}f''(\xi)(x-x_0)^2\propto(x-x_0)^2$ |
> | Caso clave | $\sin\theta\approx\theta$ (válido si $\theta<30^\circ$) |
> | Falla si | $f'(x_0)=0$ o desviación grande |

> [!corolario]
> La serie de Taylor es la maquinaria que legitima la linealización: truncar a primer orden equivale a sustituir la curva por su tangente, con error cuadrático en la desviación. La versión vectorial reemplaza $f'$ por la [[Jacobiano | jacobiana]] y, tras el cambio a [[Variables Desviacion | variables de desviación]], produce el modelo $\delta\dot{\mathbf{x}}=\mathbf{A}\,\delta\mathbf{x}+\mathbf{B}\,\delta\mathbf{u}$ de [[Linealizacion/index | Linealización]].

> [!referencia]
> - Cálculo multivariable de los coeficientes: [[Jacobiano]].
> - Cambio de variable al origen: [[Variables Desviacion]].
> - Marco general: [[Linealizacion/index]].
