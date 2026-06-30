---
title: Teoremas Integrales
order: 2
tags:
  - electromagnetismo
  - teoria
  - calculo-vectorial
draft: false
aliases:
  - Teorema de la divergencia
  - Teorema de Stokes
  - Gauss y Stokes
---

# Teoremas Integrales $\oint_S\vec F\cdot d\vec A=\int_V\nabla\cdot\vec F\,dV$

---

> [!definicion]
> Los **teoremas integrales** del cálculo vectorial son la generalización del **teorema fundamental del cálculo** a varias dimensiones. Todos comparten la misma estructura: la integral de una "derivada" de $\vec F$ sobre una **región** es igual a la integral del propio $\vec F$ sobre la **frontera** de esa región.
>
> $$\int_{\text{región}}(\text{derivada de }\vec F)=\int_{\partial(\text{región})}\vec F$$
>
> En una dimensión, $\displaystyle\int_a^b f'(x)\,dx=f(b)-f(a)$: la región es el segmento $[a,b]$ y su frontera son los dos extremos $\{a,b\}$. Al subir de dimensión, la "derivada" toma la forma de **gradiente**, **divergencia** o **rotacional**, y la frontera pasa a ser una curva, una superficie o un volumen. Esa única idea —relacionar interior con borde— es la maquinaria sobre la que se construye **todo** el electromagnetismo: de ella nacen las formas integral y diferencial de las ecuaciones de Maxwell, y los potenciales $V$ y $\vec A$.

---

> [!info]
> **Ubicación.** Curso de Electromagnetismo, sección [[1 Calculo Vectorial/index | Cálculo Vectorial]].
>
> **Notas hermanas.** [[Campos y Operadores]] (define $\nabla$, divergencia, rotacional, gradiente), [[Identidades Vectoriales]] (identidades que se demuestran con estos teoremas), [[Delta de Dirac y Singularidades]] (qué ocurre cuando los campos divergen, p. ej. $\nabla\cdot(\hat r/r^2)$).
>
> **Referencia.** Griffiths, *Introduction to Electrodynamics*, cap. 1 (Vector Analysis), secciones 1.3.4–1.3.6 y 1.6.
>
> **Convenios.** Unidades SI, vectores con flecha $\vec F$, convenio de suma de Einstein (índices repetidos se suman), decimales con coma.

---

## Ejemplo

> [!ejemplo] Verificación del teorema de la divergencia
> Sea el campo
> $$\vec F=(xy)\,\hat x+(2yz)\,\hat y+(3zx)\,\hat z,$$
> y sea $V$ el cubo unitario $0\le x\le 1$, $0\le y\le 1$, $0\le z\le 1$, con frontera $S$ (sus seis caras). Comprueba explícitamente que
> $$\oint_S\vec F\cdot d\vec A=\int_V(\nabla\cdot\vec F)\,dV.$$
>
> > [!solucion]
> > **Lado derecho (volumen).** La divergencia es
> > $$\nabla\cdot\vec F=\partial_x(xy)+\partial_y(2yz)+\partial_z(3zx)=y+2z+3x.$$
> > Integramos sobre el cubo:
> > $$\int_V(y+2z+3x)\,dV=\int_0^1\!\!\int_0^1\!\!\int_0^1(y+2z+3x)\,dx\,dy\,dz.$$
> > Por simetría, cada uno de los tres términos integra una variable lineal sobre $[0,1]$ (que da $\tfrac12$) y constante en las otras dos (que dan $1$):
> > $$\int_V y\,dV=\tfrac12,\qquad \int_V 2z\,dV=2\cdot\tfrac12=1,\qquad \int_V 3x\,dV=3\cdot\tfrac12=\tfrac32.$$
> > $$\boxed{\int_V(\nabla\cdot\vec F)\,dV=\tfrac12+1+\tfrac32=3.}$$
> >
> > **Lado izquierdo (flujo por las seis caras).** En cada cara, $d\vec A$ apunta hacia afuera y solo sobrevive la componente normal de $\vec F$.
> >
> > | Cara | Normal $\hat n$ | $\vec F\cdot\hat n$ en la cara | Flujo $\displaystyle\iint\vec F\cdot d\vec A$ |
> > |---|---|---|---|
> > | $x=1$ | $+\hat x$ | $xy=y$ | $\int_0^1\!\!\int_0^1 y\,dy\,dz=\tfrac12$ |
> > | $x=0$ | $-\hat x$ | $-xy=0$ | $0$ |
> > | $y=1$ | $+\hat y$ | $2yz=2z$ | $\int_0^1\!\!\int_0^1 2z\,dx\,dz=1$ |
> > | $y=0$ | $-\hat y$ | $-2yz=0$ | $0$ |
> > | $z=1$ | $+\hat z$ | $3zx=3x$ | $\int_0^1\!\!\int_0^1 3x\,dx\,dy=\tfrac32$ |
> > | $z=0$ | $-\hat z$ | $-3zx=0$ | $0$ |
> >
> > Sumando las seis contribuciones:
> > $$\oint_S\vec F\cdot d\vec A=\tfrac12+0+1+0+\tfrac32+0=3.$$
> >
> > **Conclusión.** Ambos lados valen $3$. El teorema se verifica: $\;\oint_S\vec F\cdot d\vec A=\int_V(\nabla\cdot\vec F)\,dV=3.\;\blacksquare$

---

## En qué consiste

> [!teoria] El teorema fundamental del cálculo, generalizado
> Recordemos el teorema fundamental del cálculo en una variable:
> $$\int_a^b \frac{df}{dx}\,dx=f(b)-f(a).$$
> Léelo así: *la integral de la derivada de $f$ sobre un intervalo se reduce a evaluar $f$ en la frontera del intervalo*. Esta es la plantilla universal. Subiendo de dimensión y según qué "derivada" use el operador $\nabla$, obtenemos los tres teoremas centrales del cálculo vectorial:
>
> | Operador $\nabla$ | Teorema | Región | Frontera |
> |---|---|---|---|
> | gradiente $\nabla\varphi$ | del **gradiente** | curva $C$ de $a$ a $b$ | extremos $\{a,b\}$ |
> | divergencia $\nabla\cdot\vec F$ | de la **divergencia** (Gauss) | volumen $V$ | superficie cerrada $S$ |
> | rotacional $\nabla\times\vec F$ | de **Stokes** | superficie $S$ | curva cerrada $C$ |
>
> En cada caso: **integral de la derivada sobre la región $=$ integral de $\vec F$ (o $\varphi$) sobre la frontera**. El teorema de **Green** es el caso plano del de Stokes. Veámoslos uno a uno, con su demostración.

---

> [!teorema] Teorema del gradiente
> Sea $\varphi$ un campo escalar diferenciable y $C$ una curva que va de un punto $a$ a un punto $b$. Entonces
> $$\int_a^b\nabla\varphi\cdot d\vec l=\varphi(b)-\varphi(a).$$
> El valor de la integral depende **solo de los extremos**, no del camino seguido.

> [!demostracion]
> **Paso 1 — Diferencial de $\varphi$ a lo largo del camino.** Al movernos un paso infinitesimal $d\vec l=(dx,dy,dz)$ sobre la curva, el campo escalar cambia en
> $$d\varphi=\frac{\partial\varphi}{\partial x}dx+\frac{\partial\varphi}{\partial y}dy+\frac{\partial\varphi}{\partial z}dz=\partial_i\varphi\,dx_i=\nabla\varphi\cdot d\vec l.$$
> Esta es la regla de la cadena escrita vectorialmente: el cambio de $\varphi$ es la proyección de su gradiente sobre el desplazamiento.
>
> **Paso 2 — Sumar (integrar) los cambios a lo largo de $C$.** Sumamos todos los cambios infinitesimales desde $a$ hasta $b$. La suma telescópica de los $d\varphi$ es simplemente el cambio total de $\varphi$:
> $$\int_a^b\nabla\varphi\cdot d\vec l=\int_a^b d\varphi=\varphi(b)-\varphi(a).$$
> Este es el teorema fundamental del cálculo aplicado a la variable que parametriza la curva. $\blacksquare$

> [!corolario] Independencia del camino y circulación nula
> Como el resultado solo depende de los extremos $a$ y $b$:
> 1. La integral de línea $\int_a^b\nabla\varphi\cdot d\vec l$ es **independiente del camino**.
> 2. Si la curva es **cerrada** ($a=b$), entonces
> $$\oint_C\nabla\varphi\cdot d\vec l=\varphi(a)-\varphi(a)=0.$$
> Todo gradiente tiene circulación nula sobre cualquier lazo. Esta es la semilla del concepto de **campo conservativo** y del **potencial** electrostático $\vec E=-\nabla V$.

---

> [!teorema] Teorema de la divergencia (Gauss)
> Sea $\vec F$ un campo vectorial diferenciable y $V$ un volumen con frontera la superficie cerrada $S$, orientada con la normal hacia afuera. Entonces el **flujo** neto a través de $S$ iguala la integral de la divergencia en $V$:
> $$\oint_S\vec F\cdot d\vec A=\int_V(\nabla\cdot\vec F)\,dV.$$

![[teorema_gauss.svg|420]]

*Figura 1. El flujo saliente neto a través de la superficie $S$ es igual a la "producción" total de campo (la divergencia integrada) en el volumen $V$ que encierra.*

> [!demostracion] Demostración por cubitos: cancelación telescópica de caras internas
> **Paso 1 — Significado físico de la divergencia.** Por definición, la divergencia es el **flujo neto saliente por unidad de volumen** de un cubito infinitesimal $dV$:
> $$\nabla\cdot\vec F=\lim_{dV\to0}\frac{1}{dV}\oint_{\partial(dV)}\vec F\cdot d\vec A
> \quad\Longrightarrow\quad
> (\nabla\cdot\vec F)\,dV=\oint_{\partial(dV)}\vec F\cdot d\vec A.$$
> Es decir, para un cubito, $(\nabla\cdot\vec F)\,dV$ **es** el flujo total que sale por sus seis caras.
>
> **Paso 2 — Trocear el volumen.** Rellenamos $V$ con muchos cubitos diminutos. Sumamos la igualdad anterior sobre todos ellos:
> $$\int_V(\nabla\cdot\vec F)\,dV=\sum_{\text{cubitos}}(\nabla\cdot\vec F)\,dV=\sum_{\text{cubitos}}\;\oint_{\partial(\text{cubito})}\vec F\cdot d\vec A.$$
>
> **Paso 3 — Cancelación de las caras internas.** Dos cubitos vecinos comparten una cara interna. Para uno de ellos, la normal hacia afuera apunta, digamos, hacia $+\hat x$; para el vecino, esa **misma** cara tiene normal hacia afuera $-\hat x$. El flujo $\vec F\cdot d\vec A$ por esa cara compartida aparece, pues, **dos veces con signos opuestos** y se cancela:
> $$(\vec F\cdot\hat x)\,dA+(\vec F\cdot(-\hat x))\,dA=0.$$
> Esta es una cancelación **telescópica**: toda cara compartida por dos cubitos interiores desaparece de la suma.
>
> **Paso 4 — Solo sobreviven las caras de la frontera.** Las únicas caras que **no** tienen vecino son las que dan a la frontera $S$. Por tanto, de la suma sobre todas las caras de todos los cubitos quedan únicamente las caras exteriores:
> $$\sum_{\text{cubitos}}\oint_{\partial(\text{cubito})}\vec F\cdot d\vec A=\oint_S\vec F\cdot d\vec A.$$
> Combinando con el Paso 2:
> $$\int_V(\nabla\cdot\vec F)\,dV=\oint_S\vec F\cdot d\vec A.\qquad\blacksquare$$

---

> [!teorema] Teorema de Stokes (del rotacional)
> Sea $\vec F$ un campo vectorial diferenciable y $S$ una superficie cuya frontera es la curva cerrada $C$. Entonces la **circulación** de $\vec F$ a lo largo de $C$ iguala el flujo del rotacional a través de $S$:
> $$\oint_C\vec F\cdot d\vec l=\int_S(\nabla\times\vec F)\cdot d\vec A.$$
> La orientación de $d\vec A$ y el sentido de recorrido de $C$ se ligan por la **regla de la mano derecha**: si los dedos de la mano derecha siguen el sentido de $C$, el pulgar marca el sentido de $d\vec A$.

![[teorema_stokes.svg|420]]

*Figura 2. La circulación de $\vec F$ a lo largo del borde $C$ es igual al flujo del rotacional $\nabla\times\vec F$ a través de cualquier superficie $S$ apoyada en $C$. La normal $d\vec A$ se elige por la mano derecha respecto al sentido de $C$.*

> [!demostracion] Demostración por cuadritos: cancelación de aristas internas
> **Paso 1 — Significado físico del rotacional.** Por definición, la componente del rotacional normal a una superficie es la **circulación por unidad de área** de un cuadrito infinitesimal $dA$:
> $$(\nabla\times\vec F)\cdot\hat n=\lim_{dA\to0}\frac{1}{dA}\oint_{\partial(dA)}\vec F\cdot d\vec l
> \quad\Longrightarrow\quad
> (\nabla\times\vec F)\cdot d\vec A=\oint_{\partial(dA)}\vec F\cdot d\vec l.$$
> Para un cuadrito, $(\nabla\times\vec F)\cdot d\vec A$ **es** la circulación a lo largo de su perímetro.
>
> **Paso 2 — Teselar la superficie.** Cubrimos $S$ con muchos cuadritos diminutos, todos orientados de forma coherente (misma cara "arriba"). Sumamos:
> $$\int_S(\nabla\times\vec F)\cdot d\vec A=\sum_{\text{cuadritos}}\;\oint_{\partial(\text{cuadrito})}\vec F\cdot d\vec l.$$
>
> **Paso 3 — Cancelación de las aristas internas.** Dos cuadritos vecinos comparten una arista interna. Por la orientación coherente, cada cuadrito recorre esa **misma** arista en **sentido opuesto** al de su vecino. Las dos contribuciones $\vec F\cdot d\vec l$ son iguales y de signo contrario, y se cancelan. Toda arista interior compartida desaparece de la suma.
>
> **Paso 4 — Solo sobrevive el borde.** Las únicas aristas sin vecino son las que tocan el borde $C$. Tras la cancelación queda exactamente la circulación a lo largo de la frontera:
> $$\sum_{\text{cuadritos}}\oint_{\partial(\text{cuadrito})}\vec F\cdot d\vec l=\oint_C\vec F\cdot d\vec l.$$
> Combinando con el Paso 2:
> $$\int_S(\nabla\times\vec F)\cdot d\vec A=\oint_C\vec F\cdot d\vec l.\qquad\blacksquare$$

---

> [!teorema] Teorema de Green (caso plano de Stokes)
> Sea $S$ una región del plano $xy$ con frontera la curva cerrada $C$ recorrida en sentido antihorario, y sean $P(x,y)$ y $Q(x,y)$ funciones diferenciables. Entonces
> $$\oint_C\big(P\,dx+Q\,dy\big)=\iint_S\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dx\,dy.$$

> [!demostracion]
> **Paso 1 — Elegir el campo plano.** Tomamos $\vec F=P\,\hat x+Q\,\hat y$ (sin componente $z$, y dependiente solo de $x,y$). Entonces
> $$\vec F\cdot d\vec l=P\,dx+Q\,dy.$$
>
> **Paso 2 — Rotacional del campo plano.** Calculamos el rotacional; solo sobrevive la componente $\hat z$:
> $$\nabla\times\vec F=\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)\hat z.$$
>
> **Paso 3 — Aplicar Stokes.** La superficie es plana, de modo que $d\vec A=\hat z\,dx\,dy$ y $(\nabla\times\vec F)\cdot d\vec A=(\partial_x Q-\partial_y P)\,dx\,dy$. Sustituyendo en el teorema de Stokes:
> $$\oint_C(P\,dx+Q\,dy)=\iint_S\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dx\,dy.\qquad\blacksquare$$

---

> [!proposicion] Equivalencias: campos conservativos y solenoidales
> Estas dos cadenas de equivalencias son consecuencia directa de Stokes y de Gauss, y son el **origen de los potenciales** del electromagnetismo.
>
> **Campo conservativo (irrotacional).** Para un campo $\vec F$ definido en una región simplemente conexa, son equivalentes:
> $$\nabla\times\vec F=0
> \;\Longleftrightarrow\;
> \oint_C\vec F\cdot d\vec l=0\ \text{para todo lazo }C
> \;\Longleftrightarrow\;
> \vec F=-\nabla\varphi.$$
> *Por Stokes:* si $\nabla\times\vec F=0$, el flujo del rotacional es nulo sobre cualquier $S$, luego toda circulación se anula; si toda circulación se anula, la integral de línea no depende del camino y define un potencial $\varphi$. (El signo $-$ es convenio físico.)
>
> **Campo solenoidal (sin divergencia).** Para un campo $\vec F$ definido en una región adecuada, son equivalentes:
> $$\nabla\cdot\vec F=0
> \;\Longleftrightarrow\;
> \oint_S\vec F\cdot d\vec A=0\ \text{para toda superficie cerrada }S
> \;\Longleftrightarrow\;
> \vec F=\nabla\times\vec A.$$
> *Por Gauss:* si $\nabla\cdot\vec F=0$, el flujo a través de cualquier superficie cerrada es nulo; recíprocamente, un campo de flujo cerrado nulo se escribe como rotacional de un **potencial vector** $\vec A$.

> [!warning] De dónde salen los potenciales $V$ y $\vec A$
> Estas equivalencias **no son un tecnicismo matemático**: son la raíz física de los potenciales del electromagnetismo.
> - El campo electrostático cumple $\nabla\times\vec E=0$, así que es **conservativo** $\Rightarrow$ existe el potencial escalar $V$ con $\vec E=-\nabla V$.
> - El campo magnético cumple siempre $\nabla\cdot\vec B=0$, así que es **solenoidal** $\Rightarrow$ existe el potencial vector $\vec A$ con $\vec B=\nabla\times\vec A$.
>
> Toda la formulación con potenciales de la electrodinámica descansa sobre los teoremas integrales de esta nota.

---

## Resumen

> [!resumen] Los teoremas integrales de un vistazo
>
> | Teorema | Región | Frontera | Enunciado |
> |---|---|---|---|
> | **del Gradiente** | curva $C$ de $a$ a $b$ | extremos $\{a,b\}$ | $\displaystyle\int_a^b\nabla\varphi\cdot d\vec l=\varphi(b)-\varphi(a)$ |
> | **de la Divergencia** (Gauss) | volumen $V$ | superficie cerrada $S$ | $\displaystyle\oint_S\vec F\cdot d\vec A=\int_V\nabla\cdot\vec F\,dV$ |
> | **de Stokes** (rotacional) | superficie $S$ | curva cerrada $C$ | $\displaystyle\oint_C\vec F\cdot d\vec l=\int_S(\nabla\times\vec F)\cdot d\vec A$ |
> | **de Green** (Stokes plano) | región plana $S$ | curva cerrada $C$ | $\displaystyle\oint_C(P\,dx+Q\,dy)=\iint_S(\partial_x Q-\partial_y P)\,dx\,dy$ |
>
> Patrón único: *integral de la derivada sobre la región $=$ integral del campo sobre la frontera*.

> [!corolario] Consecuencias para el electromagnetismo
> - $\nabla\times\vec F=0\ \Leftrightarrow\ \oint_C\vec F\cdot d\vec l=0\ \Leftrightarrow\ \vec F=-\nabla\varphi$ &nbsp;(**conservativo** $\to$ potencial $V$, $\vec E=-\nabla V$).
> - $\nabla\cdot\vec F=0\ \Leftrightarrow\ \oint_S\vec F\cdot d\vec A=0\ \Leftrightarrow\ \vec F=\nabla\times\vec A$ &nbsp;(**solenoidal** $\to$ potencial vector $\vec A$, $\vec B=\nabla\times\vec A$).
> - Gauss y Stokes traducen entre las formas **integral** y **diferencial** de las leyes de Maxwell.

> [!referencia]
> - Griffiths, D. J. *Introduction to Electrodynamics*, 4.ª ed., cap. 1 (Vector Analysis), §§ 1.3.4–1.3.6 (teoremas fundamentales) y § 1.6 (teoría de campos).
> - Notas hermanas: [[Campos y Operadores]], [[Identidades Vectoriales]], [[Delta de Dirac y Singularidades]].
> - Índice del curso: [[1 Calculo Vectorial/index | Cálculo Vectorial]].
