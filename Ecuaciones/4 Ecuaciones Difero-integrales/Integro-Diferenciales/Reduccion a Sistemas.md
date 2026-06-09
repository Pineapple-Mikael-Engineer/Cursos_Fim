---
title: Reducción de Integro-Diferenciales a Sistemas
tags:
  - ecuaciones
  - difero-integrales
  - teoria
  - integro-diferenciales
  - sistemas
draft: false
aliases:
  - reducción a sistemas
  - integro-diferencial a EDO
  - nueva variable integral
  - reducing integro-differential equations to systems
---

# Reducción de Integro-Diferenciales a Sistemas

> [!definicion]
> Una ecuación integro-diferencial se convierte en un **sistema de EDO de primer orden** (o, según se
> mire, en una EDO de orden superior o en una ecuación integral pura) introduciendo la **integral como
> una nueva variable**. Si se define
> $$\psi(t)=\int_{0}^{t}K(t,s)\,\varphi(s)\,ds,$$
> derivar $\psi$ con la **regla de Leibniz** produce una segunda ecuación que **acopla** $\varphi$ y
> $\psi$: el problema original pasa a ser un sistema en las incógnitas $(\varphi,\psi)$, que se resuelve
> con las técnicas estándar de sistemas lineales.

> [!info]
> El método **general** de la sección [[Integro-Diferenciales/index| integro-diferenciales]]: sirve
> aunque el núcleo **no** sea de convolución, donde [[Resolucion por Transformada de Laplace| Laplace]]
> no llega. La clasificación previa está en [[Concepto y Clasificacion| concepto y clasificación]]. El
> sistema resultante se ataca por [[Sistemas Lineales Autovalores| autovalores]] (notación de Krasnov:
> incógnita $\varphi$, núcleo $K$).

---

## Ejemplo

> [!ejemplo] $\varphi'(t)=\varphi(t)+\displaystyle\int_{0}^{t}\varphi(s)\,ds$, con $\varphi(0)=1$
> El núcleo es $K=1$; introducimos la integral como variable y resolvemos.
>
> **Paso 1 — definir la nueva variable.** Sea
> $$\psi(t)=\int_{0}^{t}\varphi(s)\,ds.$$
> Por el teorema fundamental del cálculo, su derivada es $\psi'(t)=\varphi(t)$. Además $\psi(0)=0$
> (integral de $0$ a $0$).
>
> **Paso 2 — reescribir la ecuación.** La original $\varphi'=\varphi+\int_0^t\varphi$ se vuelve
> $\varphi'=\varphi+\psi$. Junto con $\psi'=\varphi$ obtenemos un **sistema de primer orden**:
> $$\begin{cases}\varphi'=\varphi+\psi,\\[2pt]\psi'=\varphi,\end{cases}\qquad
> \begin{pmatrix}\varphi\\ \psi\end{pmatrix}'=
> \begin{pmatrix}1&1\\ 1&0\end{pmatrix}\!\begin{pmatrix}\varphi\\ \psi\end{pmatrix},\qquad
> \varphi(0)=1,\ \psi(0)=0.$$
>
> **Paso 3 — resolver por autovalores.** El polinomio característico de $\begin{pmatrix}1&1\\1&0\end{pmatrix}$
> es $\lambda^{2}-\lambda-1=0$, cuyas raíces son la **razón áurea** y su conjugada:
> $$\lambda_{\pm}=\frac{1\pm\sqrt{5}}{2}.$$
> La solución general es $\varphi(t)=A\,e^{\lambda_{+}t}+B\,e^{\lambda_{-}t}$ (ver
> [[Sistemas Lineales Autovalores| autovalores]] para el cálculo de $A,B$ con los datos iniciales).
>
> **Atajo equivalente — derivar otra vez.** En lugar de armar el sistema, se puede **derivar** la
> ecuación original: de $\varphi'=\varphi+\int_0^t\varphi$ sale
> $$\varphi''=\varphi'+\varphi\ \Longrightarrow\ \varphi''-\varphi'-\varphi=0,$$
> la misma EDO de coeficientes constantes (mismo polinomio $\lambda^2-\lambda-1=0$). La derivación
> "gasta" la integral y deja una EDO pura; la condición extra $\varphi'(0)=\varphi(0)+0=1$ sale de
> evaluar la ecuación original en $t=0$.

---

## En qué consiste

> [!teoria] Las tres formas equivalentes
> Una integro-diferencial admite **tres disfraces**, todos equivalentes; se elige el más cómodo:
> - **Integro-diferencial** (original): mezcla $\varphi'$ y $\int\varphi$.
> - **Sistema de EDO de primer orden**: introduciendo $\psi=\int K\varphi$ como variable, se obtiene un
>   sistema en $(\varphi,\psi,\dots)$ — útil para resolver numéricamente o por autovalores.
> - **Ecuación integral pura** (sin derivadas): **integrando** la ecuación de $0$ a $t$ se elimina
>   $\varphi'$ y queda una ecuación de Volterra de segunda especie en $\varphi$.
>
> El puente lo da la regla de Leibniz para derivar una integral de límite variable:
> $$\frac{d}{dt}\int_{0}^{t}K(t,s)\,\varphi(s)\,ds=K(t,t)\,\varphi(t)+\int_{0}^{t}\frac{\partial K}{\partial t}(t,s)\,\varphi(s)\,ds.$$
> Si $\partial K/\partial t=0$ (núcleo separable simple o constante) el término integral desaparece y el
> acoplamiento es puramente algebraico, como en el ejemplo.

> [!algoritmo] Reducir a un sistema
> 1. **Nombrar la integral.** Definir $\psi(t)=\int_0^t K(t,s)\varphi(s)\,ds$ (una variable por cada
>    integral distinta). Anotar $\psi(0)=0$.
> 2. **Derivar $\psi$** con la regla de Leibniz; expresar $\psi'$ en términos de $\varphi$ y, si hace
>    falta, de $\psi$.
> 3. **Sustituir** $\int K\varphi=\psi$ en la ecuación original para escribirla sin integral.
> 4. **Ensamblar el sistema** de primer orden en $(\varphi,\psi,\dots)$ con sus condiciones iniciales.
> 5. **Resolver** el sistema (por [[Sistemas Lineales Autovalores| autovalores]] si es lineal de
>    coeficientes constantes) o, alternativamente, **derivar de nuevo** para colapsarlo en una sola EDO
>    de orden superior.

> [!proposicion] Cuándo conviene cada camino
> | Situación | Forma preferida |
> |:---|:---|
> | núcleo de convolución $K(t-s)$ | [[Resolucion por Transformada de Laplace\|Laplace]] (más directo) |
> | núcleo constante o separable | reducir a **sistema** o derivar a una EDO |
> | varios términos integrales | **una variable nueva por integral**, sistema mayor |
> | resolución numérica | sistema de primer orden (se integra con Runge-Kutta) |

## Limitaciones

> [!warning] El núcleo debe permitir cerrar el sistema
> La reducción sólo produce un sistema **finito** si al derivar $\psi$ se regenera $\varphi$ o $\psi$
> (núcleos constantes, polinómicos en $t$, separables, exponenciales). Con un núcleo $K(t,s)$ arbitrario,
> $\psi'$ vuelve a contener una **nueva integral** y el proceso no se cierra; entonces conviene la forma
> de **ecuación integral pura** (integrando) o un método numérico directo. Además, cada integral
> distinta añade una variable: con muchos términos el sistema crece deprisa.

## Resumen

> [!resumen]
> | Paso | Acción |
> |:---|:---|
> | Variable nueva | $\psi=\int_0^t K\varphi$, con $\psi(0)=0$ |
> | Derivar (Leibniz) | $\psi'=K(t,t)\varphi+\int\partial_t K\,\varphi$ |
> | Sistema | $(\varphi,\psi)'=A\,(\varphi,\psi)$ + datos iniciales |
> | Atajo | derivar la original → EDO de orden $n{+}1$ |
> | Resolver | [[Sistemas Lineales Autovalores\|autovalores]] / numérico |

> [!corolario]
> Reducir a un sistema es la salida **universal**: a costa de añadir variables (una por integral),
> convierte la integro-diferencial en EDO ordinarias, terreno conocido. El ejemplo
> $\varphi'=\varphi+\int_0^t\varphi$ revela su parentesco con la razón áurea, ya sea como sistema
> $\begin{pmatrix}1&1\\1&0\end{pmatrix}$ o como la EDO $\varphi''-\varphi'-\varphi=0$.

> [!referencia]
> - Cuando hay convolución (atajo): [[Resolucion por Transformada de Laplace]].
> - El sistema resultante: [[Sistemas Lineales Autovalores]].
> - Clasificación previa: [[Concepto y Clasificacion]].
> - Marco de la sección: [[Integro-Diferenciales/index]].
