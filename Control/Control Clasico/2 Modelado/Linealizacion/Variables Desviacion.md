---
title: Variables de Desviación
tags:
  - control-clasico
  - teoria
  - linealizacion
draft: false
aliases:
  - variables desviacion
  - desviacion
  - delta variables
---

# Variables de Desviación

> [!definicion]
> Las **variables de desviación** miden la separación respecto al punto de operación $(\mathbf{x}_0,\mathbf{u}_0,\mathbf{y}_0)$:
> $$\delta\mathbf{x}=\mathbf{x}-\mathbf{x}_0,\qquad \delta\mathbf{u}=\mathbf{u}-\mathbf{u}_0,\qquad \delta\mathbf{y}=\mathbf{y}-\mathbf{y}_0.$$
> Este cambio de variable **traslada el equilibrio al origen** ($\mathbf{x}=\mathbf{x}_0\Rightarrow\delta\mathbf{x}=\mathbf{0}$), de modo que el modelo [[Linealizacion/index | linealizado]] $\delta\dot{\mathbf{x}}=\mathbf{A}\delta\mathbf{x}+\mathbf{B}\delta\mathbf{u}$ tiene CI nulas y admite directamente una función de transferencia.

> [!info]
> Nota de la carpeta [[Linealizacion/index | Linealización]]. Es el tercer ingrediente del método, junto a la [[Serie Taylor | serie de Taylor]] (base) y el [[Jacobiano | jacobiano]] (cálculo de $\mathbf{A},\mathbf{B}$). Permite conectar el modelo lineal con la [[Funcion Transferencia/index | función de transferencia]].

---

## Ejemplo

> [!ejemplo]
> **Cambio de variable y FT con punto de equilibrio no nulo.** Tanque calentado, salida temperatura $T$, entrada potencia $q$, modelo de primer orden no lineal con pérdida radiativa linealizable:
> $$\dot{T}=\frac{1}{C}\big(q-h(T-T_a)\big),\qquad C=2,\ h=0.5,\ T_a=20.$$
>
> **Paso 1 — Equilibrio** para una potencia de operación $q_0=15$:
> $$0=\frac{1}{C}\big(q_0-h(T_0-T_a)\big)\Rightarrow T_0=T_a+\frac{q_0}{h}=20+\frac{15}{0.5}=50.$$
> Punto de operación $(T_0,q_0)=(50,15)$, con $y_0=T_0=50$.
>
> **Paso 2 — Variables de desviación:**
> $$\delta T=T-50,\qquad \delta q=q-15.$$
>
> **Paso 3 — Sustituir el cambio de variable.** Como $\dot{T}=\delta\dot{T}$ y $T-T_a=(\delta T+50)-20=\delta T+30$:
> $$\delta\dot{T}=\frac{1}{2}\big((\delta q+15)-0.5(\delta T+30)\big)=\frac{1}{2}\big(\delta q-0.5\,\delta T\big).$$
> Los términos constantes ($15-0.5\cdot 30=0$) se cancelan **exactamente** por ser el equilibrio. Queda lineal:
> $$\delta\dot{T}=-0.25\,\delta T+0.5\,\delta q.$$
>
> **Paso 4 — Función de transferencia.** Con CI nula ($\delta T(0)=0$), $\mathcal{L}\{\delta\dot{T}\}=s\,\delta T(s)$:
> $$s\,\delta T(s)=-0.25\,\delta T(s)+0.5\,\delta Q(s)\Rightarrow G(s)=\frac{\delta T(s)}{\delta Q(s)}=\frac{0.5}{s+0.25}.$$
> Sistema estable, constante de tiempo $\tau=1/0.25=4$ s. La FT relaciona **incrementos** de potencia con **incrementos** de temperatura sobre el punto de operación, no valores absolutos.

---

## En qué consiste

> [!info] Propiedad fundamental
> En desviación el equilibrio queda en el **origen**: cuando $\mathbf{x}=\mathbf{x}_0$, $\mathbf{u}=\mathbf{u}_0$, se tiene $\delta\mathbf{x}=\mathbf{0}$, $\delta\mathbf{u}=\mathbf{0}$. Esto coloca las CI del modelo lineal en cero y habilita la transformada de Laplace sin términos de condición inicial.

> [!info] Por qué conviene
> 1. El equilibrio en el origen simplifica el análisis de estabilidad (estabilidad del origen).
> 2. $\delta\mathbf{x}(0)=\mathbf{x}(0)-\mathbf{x}_0$ es la desviación inicial, lista para la respuesta.
> 3. La validez lineal exige $\delta\mathbf{x},\delta\mathbf{u}$ pequeñas — el marco natural del incremento.
> 4. Permite definir una FT $\delta Y(s)=G(s)\,\delta U(s)$ con CI nulas.

> [!teorema] Sistema en variables de desviación
> Derivando $\delta\mathbf{x}=\mathbf{x}-\mathbf{x}_0$ (con $\mathbf{x}_0$ constante) y usando [[Serie Taylor | Taylor]] alrededor de $(\mathbf{x}_0,\mathbf{u}_0)$:
> $$\delta\dot{\mathbf{x}}\approx\mathbf{A}\,\delta\mathbf{x}+\mathbf{B}\,\delta\mathbf{u},\qquad \mathbf{A}=\left.\frac{\partial\mathbf{f}}{\partial\mathbf{x}}\right|_0,\ \mathbf{B}=\left.\frac{\partial\mathbf{f}}{\partial\mathbf{u}}\right|_0.$$

> [!demostracion]
> $\delta\dot{\mathbf{x}}=\dot{\mathbf{x}}-\dot{\mathbf{x}}_0=\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x}_0+\delta\mathbf{x},\mathbf{u}_0+\delta\mathbf{u})$. Expandiendo en Taylor:
> $$\mathbf{f}(\mathbf{x}_0+\delta\mathbf{x},\mathbf{u}_0+\delta\mathbf{u})=\underbrace{\mathbf{f}(\mathbf{x}_0,\mathbf{u}_0)}_{=\,\mathbf{0}}+\mathbf{A}\,\delta\mathbf{x}+\mathbf{B}\,\delta\mathbf{u}+\text{SO}.$$
> El término constante se anula por ser equilibrio; despreciando SO queda $\delta\dot{\mathbf{x}}\approx\mathbf{A}\,\delta\mathbf{x}+\mathbf{B}\,\delta\mathbf{u}$. $\blacksquare$

> [!ejemplo] Péndulo en $\theta_0=\pi/6$ (equilibrio no nulo)
> Equilibrio sostenido por par $u_0=mgl\sin(\pi/6)=0.5\,mgl$. Desviaciones $\delta x_1=x_1-\pi/6$, $\delta u=u-0.5mgl$. Como $\partial_{x_1}f_2=-\frac{g}{l}\cos x_1$ y $\cos(\pi/6)=0.866$:
> $$\mathbf{A}=\begin{bmatrix}0&1\\-0.866\frac{g}{l}&-\frac{b}{ml^2}\end{bmatrix},\qquad \mathbf{B}=\begin{bmatrix}0\\\frac{1}{ml^2}\end{bmatrix}.$$
> La gravedad efectiva es $0.866g$, menor que en la vertical: el cambio de variable expone que la rigidez del péndulo decae al inclinarse.

---

## Salida y función de transferencia

> [!teorema] Salida linealizada
> Para $\mathbf{y}=\mathbf{h}(\mathbf{x},\mathbf{u})$ con $\mathbf{y}_0=\mathbf{h}(\mathbf{x}_0,\mathbf{u}_0)$:
> $$\delta\mathbf{y}\approx\mathbf{C}\,\delta\mathbf{x}+\mathbf{D}\,\delta\mathbf{u},\qquad \mathbf{C}=\left.\frac{\partial\mathbf{h}}{\partial\mathbf{x}}\right|_0,\ \mathbf{D}=\left.\frac{\partial\mathbf{h}}{\partial\mathbf{u}}\right|_0.$$

> [!info] FT en desviación
> Para el modelo lineal, la FT relaciona incrementos con CI nulas:
> $$\delta Y(s)=G(s)\,\delta U(s),\qquad G(s)=\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}+\mathbf{D}.$$
> Toda la teoría de [[Funcion Transferencia/index | función de transferencia]] opera sobre estas variables incrementales, nunca sobre los valores absolutos.

> [!info] Linealidad del operador $\delta$
> 1. $\delta(\dot{\mathbf{x}})=\delta\dot{\mathbf{x}}$ (derivada y desviación conmutan).
> 2. $\delta(\mathbf{x}_1+\mathbf{x}_2)=\delta\mathbf{x}_1+\delta\mathbf{x}_2$.
> 3. $\delta(\alpha\mathbf{x})=\alpha\,\delta\mathbf{x}$, $\alpha$ constante.
> 4. $\delta(\mathbf{x}_1\mathbf{x}_2)\approx x_{10}\,\delta\mathbf{x}_2+x_{20}\,\delta\mathbf{x}_1$ (producto, linealizado).

---

## Limitaciones

> [!warning]
> 1. **Solo desviaciones pequeñas** respecto al punto de operación.
> 2. **El punto base debe ser equilibrio** ($\mathbf{f}(\mathbf{x}_0,\mathbf{u}_0)=\mathbf{0}$); de lo contrario quedan términos constantes sin cancelar.
> 3. **No captura** saturación, histéresis ni otras no linealidades fuertes.
> 4. **Múltiples equilibrios:** una linealización (y un juego de variables de desviación) por cada uno.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Definición | $\delta\mathbf{x}=\mathbf{x}-\mathbf{x}_0$, $\delta\mathbf{u}=\mathbf{u}-\mathbf{u}_0$ |
> | Efecto | equilibrio trasladado al origen |
> | Modelo | $\delta\dot{\mathbf{x}}=\mathbf{A}\delta\mathbf{x}+\mathbf{B}\delta\mathbf{u}$ |
> | Salida | $\delta\mathbf{y}=\mathbf{C}\delta\mathbf{x}+\mathbf{D}\delta\mathbf{u}$ |
> | FT | $\delta Y(s)=G(s)\,\delta U(s)$, CI nulas |
> | Validez | desviaciones pequeñas, base = equilibrio |

> [!corolario]
> Las variables de desviación son el cambio de coordenadas $\delta=(\cdot)-(\cdot)_0$ que lleva el equilibrio al origen: anula los términos constantes, pone CI nulas y deja el modelo lineal $\delta\dot{\mathbf{x}}=\mathbf{A}\delta\mathbf{x}+\mathbf{B}\delta\mathbf{u}$ listo para Laplace. Su producto final es una [[Funcion Transferencia/index | FT]] que relaciona **incrementos** de entrada con incrementos de salida sobre el punto de operación elegido.

> [!referencia]
> - Justificación del truncamiento: [[Serie Taylor]].
> - Cálculo de $\mathbf{A},\mathbf{B},\mathbf{C},\mathbf{D}$: [[Jacobiano]].
> - Marco general: [[Linealizacion/index]].
> - Destino del modelo: [[Funcion Transferencia/index]].
