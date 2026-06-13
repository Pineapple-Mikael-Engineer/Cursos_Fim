---
title: Linealización
tags:
  - control-clasico
  - teoria
  - modelado
draft: false
aliases:
  - linealizacion
  - aproximación lineal
---

# Linealización

> [!definicion]
> **Linealizar** un sistema no lineal $\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},\mathbf{u})$ es aproximarlo por un sistema lineal alrededor de un **punto de equilibrio** $(\mathbf{x}_0,\mathbf{u}_0)$, donde $\mathbf{f}(\mathbf{x}_0,\mathbf{u}_0)=\mathbf{0}$. Con las [[Variables Desviacion | variables de desviación]] $\delta\mathbf{x}=\mathbf{x}-\mathbf{x}_0$, $\delta\mathbf{u}=\mathbf{u}-\mathbf{u}_0$ el resultado es:
> $$\delta\dot{\mathbf{x}}=\mathbf{A}\,\delta\mathbf{x}+\mathbf{B}\,\delta\mathbf{u},\qquad \mathbf{A}=\left.\frac{\partial\mathbf{f}}{\partial\mathbf{x}}\right|_0,\quad \mathbf{B}=\left.\frac{\partial\mathbf{f}}{\partial\mathbf{u}}\right|_0.$$
> Las matrices $\mathbf{A},\mathbf{B}$ son las [[Jacobiano | jacobianas]] evaluadas en el equilibrio; la justificación es el truncamiento a primer orden de la [[Serie Taylor | serie de Taylor]].

> [!info]
> Carpeta de la sección **Modelado**. Reúne las tres piezas del método: [[Serie Taylor | serie de Taylor]] (base teórica), [[Jacobiano | matriz jacobiana]] (cálculo multivariable de $\mathbf{A},\mathbf{B}$) y [[Variables Desviacion | variables de desviación]] (cambio de variable al origen). El modelo lineal resultante se lleva a [[Espacio Estados/index | espacio de estados]] o a [[Funcion Transferencia/index | función de transferencia]].

---

## Ejemplo

> [!ejemplo]
> **Linealizar el péndulo con amortiguamiento, con números.** Modelo no lineal con $g=9.81\ \text{m/s}^2$, $l=0.5\ \text{m}$, $m=1\ \text{kg}$, $b=0.1\ \text{N·m·s}$:
> $$ml^2\ddot{\theta}+b\dot{\theta}+mgl\sin\theta=u.$$
>
> **Paso 1 — Estados.** $x_1=\theta$, $x_2=\dot{\theta}$:
> $$\dot{x}_1=x_2=f_1,\qquad \dot{x}_2=-\frac{g}{l}\sin x_1-\frac{b}{ml^2}x_2+\frac{1}{ml^2}u=f_2.$$
>
> **Paso 2 — Equilibrio.** Con $u_0=0$: $f_1=0\Rightarrow x_{20}=0$; $f_2=0\Rightarrow\sin x_{10}=0\Rightarrow x_{10}=0$ (péndulo colgando). Verificación: $\mathbf{f}(\mathbf{x}_0,0)=\mathbf{0}$ ✓.
>
> **Paso 3 — Jacobianas** (ver [[Jacobiano]]):
> $$\mathbf{A}=\left.\begin{bmatrix}0&1\\[2pt]-\frac{g}{l}\cos x_1&-\frac{b}{ml^2}\end{bmatrix}\right|_{x_1=0}=\begin{bmatrix}0&1\\-19.62&-0.4\end{bmatrix},\qquad \mathbf{B}=\begin{bmatrix}0\\\frac{1}{ml^2}\end{bmatrix}=\begin{bmatrix}0\\4\end{bmatrix}.$$
>
> Cálculo: $\dfrac{g}{l}=\dfrac{9.81}{0.5}=19.62$, $\dfrac{b}{ml^2}=\dfrac{0.1}{1\cdot0.25}=0.4$, $\dfrac{1}{ml^2}=\dfrac{1}{0.25}=4$.
>
> **Paso 4 — Modelo lineal** en [[Variables Desviacion | desviación]] ($\delta x_i=x_i-0$):
> $$\delta\dot{x}_1=\delta x_2,\qquad \delta\dot{x}_2=-19.62\,\delta x_1-0.4\,\delta x_2+4\,\delta u.$$
>
> **Paso 5 — Polos del linealizado.** $\det(s\mathbf{I}-\mathbf{A})=s^2+0.4s+19.62=0\Rightarrow s=-0.2\pm 4.42j$. Estable y subamortiguado: el péndulo oscila y se asienta, justo lo esperado físicamente cerca de la vertical inferior.

---

## En qué consiste

> [!teoria]
> Casi todo sistema físico es no lineal, pero las herramientas potentes (función de transferencia, lugar de raíces, Bode, Nyquist, Routh) requieren un modelo **lineal**. La salida es: cerca de un equilibrio, una superficie suave se confunde con su plano tangente. El método tiene tres ingredientes acoplados, uno por nota hija:
>
> | Pieza | Pregunta que responde | Nota |
> |---|---|---|
> | Serie de Taylor | ¿por qué el truncamiento a 1.er orden es lícito? | [[Serie Taylor]] |
> | Jacobiano | ¿cómo se calculan $\mathbf{A},\mathbf{B},\mathbf{C},\mathbf{D}$ con varios estados? | [[Jacobiano]] |
> | Variables de desviación | ¿cómo trasladar el equilibrio al origen y obtener la FT? | [[Variables Desviacion]] |

> [!teorema] Sistema linealizado
> Para $\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},\mathbf{u})$, $\mathbf{y}=\mathbf{h}(\mathbf{x},\mathbf{u})$ con equilibrio $(\mathbf{x}_0,\mathbf{u}_0)$:
> $$\delta\dot{\mathbf{x}}=\mathbf{A}\,\delta\mathbf{x}+\mathbf{B}\,\delta\mathbf{u},\qquad \delta\mathbf{y}=\mathbf{C}\,\delta\mathbf{x}+\mathbf{D}\,\delta\mathbf{u},$$
> con $\mathbf{A}=\partial_{\mathbf{x}}\mathbf{f}|_0$, $\mathbf{B}=\partial_{\mathbf{u}}\mathbf{f}|_0$, $\mathbf{C}=\partial_{\mathbf{x}}\mathbf{h}|_0$, $\mathbf{D}=\partial_{\mathbf{u}}\mathbf{h}|_0$. La demostración (Taylor + equilibrio + desprecio de orden superior) está en [[Serie Taylor]].

---

## Algoritmo

> [!algoritmo]
> Para linealizar cualquier sistema $\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},\mathbf{u})$:
> 1. **Estados.** Escribir el modelo en forma de estado $\dot{x}_i=f_i(\mathbf{x},\mathbf{u})$.
> 2. **Equilibrio.** Resolver $\mathbf{f}(\mathbf{x}_0,\mathbf{u}_0)=\mathbf{0}$ para el punto de operación.
> 3. **Jacobianas.** Calcular $\mathbf{A},\mathbf{B}$ (y $\mathbf{C},\mathbf{D}$ si hay salida) y **evaluarlas** en $(\mathbf{x}_0,\mathbf{u}_0)$ — ver [[Jacobiano]].
> 4. **Desviación.** Definir $\delta\mathbf{x}=\mathbf{x}-\mathbf{x}_0$, $\delta\mathbf{u}=\mathbf{u}-\mathbf{u}_0$ — ver [[Variables Desviacion]].
> 5. **Modelo lineal.** Escribir $\delta\dot{\mathbf{x}}=\mathbf{A}\,\delta\mathbf{x}+\mathbf{B}\,\delta\mathbf{u}$ y, si se desea, su FT $\delta Y(s)/\delta U(s)$.

> [!info] En MATLAB
> ```matlab
> syms x1 x2 u g l m b real
> f = [x2;
>      -g/l*sin(x1) - b/(m*l^2)*x2 + 1/(m*l^2)*u];
> A = subs(jacobian(f,[x1 x2]), {x1,x2,u}, {0,0,0});
> B = subs(jacobian(f,u),       {x1,x2,u}, {0,0,0});
> % Numerico: g=9.81; l=.5; m=1; b=.1; eval -> sistema lineal
> sys = ss(double(A), double(B), [1 0], 0);
> ```

---

## Limitaciones

> [!warning]
> 1. **Solo local.** La aproximación falla lejos del equilibrio; no captura saturación, histéresis ni fricción de Coulomb.
> 2. **Un equilibrio por linealización.** Sistemas con varios equilibrios (p. ej. péndulo en $0$ y en $\pi$) exigen linealizar cada uno por separado.
> 3. **Estabilidad solo local.** Que el linealizado sea estable **no garantiza** estabilidad global del no lineal; puede haber ciclos límite, bifurcaciones o caos.
> 4. **Casos degenerados.** Si $\mathbf{A}$ tiene autovalores en el eje imaginario, la linealización no decide la estabilidad (Hartman–Grobman no aplica).

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Objeto | $\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},\mathbf{u})$ no lineal |
> | Punto base | equilibrio $\mathbf{f}(\mathbf{x}_0,\mathbf{u}_0)=\mathbf{0}$ |
> | Cambio de variable | $\delta\mathbf{x}=\mathbf{x}-\mathbf{x}_0$, $\delta\mathbf{u}=\mathbf{u}-\mathbf{u}_0$ |
> | Modelo lineal | $\delta\dot{\mathbf{x}}=\mathbf{A}\,\delta\mathbf{x}+\mathbf{B}\,\delta\mathbf{u}$ |
> | $\mathbf{A},\mathbf{B}$ | jacobianas evaluadas en el equilibrio |
> | Validez | desviaciones pequeñas, $\mathbf{f}$ diferenciable |

> [!corolario]
> Linealizar es sustituir la superficie $\mathbf{f}$ por su plano tangente en el equilibrio: la [[Serie Taylor | serie de Taylor]] justifica el truncamiento, el [[Jacobiano | jacobiano]] da los coeficientes y las [[Variables Desviacion | variables de desviación]] trasladan el equilibrio al origen. El premio es poder usar todo el arsenal lineal sobre $\delta\dot{\mathbf{x}}=\mathbf{A}\,\delta\mathbf{x}+\mathbf{B}\,\delta\mathbf{u}$, a costa de validez solo local.

> [!referencia]
> - Base teórica: [[Serie Taylor]].
> - Cálculo de $\mathbf{A},\mathbf{B},\mathbf{C},\mathbf{D}$: [[Jacobiano]].
> - Cambio de variable y FT: [[Variables Desviacion]].
> - Destino del modelo lineal: [[Espacio Estados/index]], [[Funcion Transferencia/index]].
