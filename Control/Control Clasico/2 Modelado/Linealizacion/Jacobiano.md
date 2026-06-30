---
title: Jacobiano
order: 6
tags:
  - control-clasico
  - teoria
  - linealizacion
  - matematicas
draft: false
aliases:
  - matriz jacobiana
  - jacobiano
  - derivada parcial vectorial
---

# Jacobiano

> [!definicion]
> La **matriz jacobiana** de $\mathbf{f}(\mathbf{x},\mathbf{u})$ recoge todas las derivadas parciales de primer orden. Para $n$ estados y $m$ entradas, $\partial_{\mathbf{x}}\mathbf{f}$ es $n\times n$ y $\partial_{\mathbf{u}}\mathbf{f}$ es $n\times m$:
> $$\frac{\partial\mathbf{f}}{\partial\mathbf{x}}=\begin{bmatrix}\frac{\partial f_1}{\partial x_1}&\cdots&\frac{\partial f_1}{\partial x_n}\\\vdots&\ddots&\vdots\\\frac{\partial f_n}{\partial x_1}&\cdots&\frac{\partial f_n}{\partial x_n}\end{bmatrix},\qquad (i,j)=\frac{\partial f_i}{\partial x_j}.$$
> En [[Linealizacion/index | linealización]] es la herramienta para obtener $\mathbf{A}$ y $\mathbf{B}$: se calcula la jacobiana y se **evalúa en el equilibrio** $(\mathbf{x}_0,\mathbf{u}_0)$.

> [!info]
> Nota de la carpeta [[Linealizacion/index | Linealización]]. Es la versión multivariable de la derivada que aparece en la [[Serie Taylor | serie de Taylor]]; el modelo $\delta\dot{\mathbf{x}}=\mathbf{A}\delta\mathbf{x}+\mathbf{B}\delta\mathbf{u}$ que produce se interpreta en [[Variables Desviacion | variables de desviación]].

---

## Ejemplo

> [!ejemplo]
> **Jacobiano de un sistema 2×2 evaluado en el equilibrio.** Sistema no lineal con acoplamiento:
> $$\dot{x}_1=x_1x_2+u=f_1,\qquad \dot{x}_2=-x_1^2+3x_2=f_2.$$
>
> **Paso 1 — Equilibrio** con $u_0=0$: de $f_1=0$, $x_1x_2=0$; de $f_2=0$, $x_1^2=3x_2$. La solución trivial es $x_{10}=0$, $x_{20}=0$ (verificación: $f_1=0$, $f_2=0$ ✓).
>
> **Paso 2 — Parciales (forma general):**
> $$\frac{\partial f_1}{\partial x_1}=x_2,\quad \frac{\partial f_1}{\partial x_2}=x_1,\quad \frac{\partial f_1}{\partial u}=1,$$
> $$\frac{\partial f_2}{\partial x_1}=-2x_1,\quad \frac{\partial f_2}{\partial x_2}=3,\quad \frac{\partial f_2}{\partial u}=0.$$
>
> **Paso 3 — Evaluar en $(0,0,0)$:**
> $$\mathbf{A}=\begin{bmatrix}x_2&x_1\\-2x_1&3\end{bmatrix}_{0}=\begin{bmatrix}0&0\\0&3\end{bmatrix},\qquad \mathbf{B}=\begin{bmatrix}1\\0\end{bmatrix}.$$
>
> **Paso 4 — Lectura.** El autovalor $3>0$ de $\mathbf{A}$ revela que el equilibrio es **inestable**; el acoplamiento $x_1x_2$ y el término $-x_1^2$, ambos cuadráticos, desaparecen al linealizar en el origen. Evaluar en otro equilibrio daría una $\mathbf{A}$ distinta — el jacobiano **depende del punto**.

---

## En qué consiste

> [!info] Significado de cada entrada
> $(i,j)=\dfrac{\partial f_i}{\partial x_j}$ es la **sensibilidad** de $\dot{x}_i$ ante una variación pequeña de $x_j$ con las demás fijas: cuánto se acelera el estado $i$ si movemos un poco el estado $j$.

> [!info] Reglas de cálculo
> 1. Constante: $\partial c/\partial x=0$.
> 2. Variable: $\partial x_i/\partial x_j=1$ si $i=j$, $0$ si $i\neq j$.
> 3. Linealidad: $\partial_x(af+bg)=a\,\partial_x f+b\,\partial_x g$.
> 4. Producto: $\partial_x(fg)=(\partial_x f)g+f(\partial_x g)$.
> 5. Cadena: $\partial_x f(g(x))=f'(g)\,\partial_x g$. Útil en $\partial_{x_1}\sin x_1=\cos x_1$.

> [!ejemplo] Masa-resorte-amortiguador (lineal)
> $f_1=x_2$, $f_2=-\frac{k}{m}x_1-\frac{b}{m}x_2+\frac{1}{m}u$:
> $$\mathbf{A}=\begin{bmatrix}0&1\\-\frac{k}{m}&-\frac{b}{m}\end{bmatrix},\qquad \mathbf{B}=\begin{bmatrix}0\\\frac{1}{m}\end{bmatrix}.$$
> Al ser ya lineal, la jacobiana **no depende** del punto de operación.

> [!ejemplo] Péndulo (no lineal)
> $f_1=x_2$, $f_2=-\frac{g}{l}\sin x_1-\frac{b}{ml^2}x_2+\frac{1}{ml^2}u$. La única parcial no trivial es $\partial_{x_1}f_2=-\frac{g}{l}\cos x_1$. Evaluada en $x_{10}=0$ ($\cos 0=1$):
> $$\mathbf{A}=\begin{bmatrix}0&1\\-\frac{g}{l}&-\frac{b}{ml^2}\end{bmatrix},\qquad \mathbf{B}=\begin{bmatrix}0\\\frac{1}{ml^2}\end{bmatrix}.$$

> [!ejemplo] Jacobiana de salida
> Para $y=h(x_1,x_2)=x_1^2+x_2$: $\partial_{\mathbf{x}}h=[\,2x_1\ \ 1\,]$. En $x_1=0$: $\mathbf{C}=[\,0\ \ 1\,]$. Análogamente $\mathbf{D}=\partial_{\mathbf{u}}h|_0$.

---

## Dimensiones y casos

> [!info] SISO vs MIMO
> | Matriz | SISO | MIMO |
> |---|---|---|
> | $\partial_{\mathbf{x}}\mathbf{f}=\mathbf{A}$ | $n\times n$ | $n\times n$ |
> | $\partial_{\mathbf{u}}\mathbf{f}=\mathbf{B}$ | $n\times 1$ | $n\times m$ |
> | $\partial_{\mathbf{x}}\mathbf{h}=\mathbf{C}$ | $1\times n$ | $p\times n$ |
> | $\partial_{\mathbf{u}}\mathbf{h}=\mathbf{D}$ | $1\times 1$ | $p\times m$ |

> [!info] Atajo para sistemas lineales
> Si el sistema ya es $\dot{\mathbf{x}}=\mathbf{A}\mathbf{x}+\mathbf{B}\mathbf{u}$, entonces $\partial_{\mathbf{x}}\mathbf{f}=\mathbf{A}$ y $\partial_{\mathbf{u}}\mathbf{f}=\mathbf{B}$ tal cual, sin depender del punto.

> [!teorema] Linealización = jacobiana en el equilibrio
> Para $\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},\mathbf{u})$ con equilibrio $(\mathbf{x}_0,\mathbf{u}_0)$:
> $$\mathbf{A}=\left.\frac{\partial\mathbf{f}}{\partial\mathbf{x}}\right|_0,\qquad \mathbf{B}=\left.\frac{\partial\mathbf{f}}{\partial\mathbf{u}}\right|_0.$$
> Es la aproximación de [[Serie Taylor | Taylor]] de primer orden; ver [[Linealizacion/index]].

> [!info] Propiedades útiles
> 1. **Autovalores de $\mathbf{A}$:** determinan la estabilidad **local** del equilibrio.
> 2. **Determinante:** $\det(\partial_{\mathbf{x}}\mathbf{f})$ mide el cambio de volumen local (invertibilidad).
> 3. **Rango:** si es $n$, el sistema es localmente invertible alrededor del punto.

---

## Limitaciones

> [!warning]
> 1. **No diferenciable:** si las parciales no existen (p. ej. fricción de Coulomb $\operatorname{sgn}(\dot{x})$), el jacobiano no está definido.
> 2. **Bifurcaciones:** con autovalores nulos en $\mathbf{A}$, la aproximación lineal es insuficiente para decidir la dinámica.
> 3. **Depende del punto:** cambiar el equilibrio cambia $\mathbf{A},\mathbf{B}$; hay que reevaluar.
> 4. **Tiempo discreto:** mismo concepto, pero sobre ecuaciones en diferencias $\mathbf{x}_{k+1}=\mathbf{f}(\mathbf{x}_k,\mathbf{u}_k)$.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Definición | $(i,j)=\partial f_i/\partial x_j$ |
> | Dimensión $\mathbf{A}$ | $n\times n$ |
> | Dimensión $\mathbf{B}$ | $n\times m$ |
> | Uso en control | $\mathbf{A}=\partial_{\mathbf{x}}\mathbf{f}|_0$, $\mathbf{B}=\partial_{\mathbf{u}}\mathbf{f}|_0$ |
> | Estabilidad local | autovalores de $\mathbf{A}$ |
> | Salida | $\mathbf{C}=\partial_{\mathbf{x}}\mathbf{h}|_0$, $\mathbf{D}=\partial_{\mathbf{u}}\mathbf{h}|_0$ |

> [!corolario]
> El jacobiano es el motor de cálculo de la linealización multivariable: derivar parcialmente cada $f_i$ respecto a cada $x_j,u_k$ y **evaluar en el equilibrio** produce directamente $\mathbf{A},\mathbf{B},\mathbf{C},\mathbf{D}$. Como depende del punto de operación, debe recalcularse en cada equilibrio; sus autovalores deciden la estabilidad local del sistema [[Linealizacion/index | linealizado]].

> [!referencia]
> - Justificación teórica (Taylor 1.er orden): [[Serie Taylor]].
> - Interpretación del modelo resultante: [[Variables Desviacion]].
> - Marco general: [[Linealizacion/index]].
