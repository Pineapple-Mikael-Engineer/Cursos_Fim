---
title: Lagrange
order: 1
tags:
  - ecuaciones
  - edo
  - teoria
  - primer-orden
  - no-resueltas
  - lagrange
draft: false
aliases:
  - ecuación de Lagrange
  - ecuación de d'Alembert
  - Lagrange equation
---

# Ecuación de Lagrange

> [!definicion]
> La **ecuación de Lagrange** (a veces llamada de d'Alembert) tiene la forma
> $$y=x\,\varphi(y')+\psi(y'),$$
> donde $\varphi$ y $\psi$ son funciones dadas de $y'$. Es **lineal en $x$ e $y$**, pero **no** en $y'$: la derivada entra a través de $\varphi$ y $\psi$, de modo que es una ecuación [[No Resueltas en y prima/index| no resuelta respecto a $y'$]]. Se resuelve **derivando respecto a $x$** y poniendo $u=y'$, lo que produce una EDO **lineal en $x(u)$**; la solución queda en forma **paramétrica**
> $$x=x(u),\qquad y=y(u).$$

> [!info]
> Caso general del bloque [[No Resueltas en y prima/index| no resueltas en $y'$]] (libro, cap. 2.3.3). Su caso particular $\varphi(y')=y'$ es la [[Clairaut| ecuación de Clairaut]]. El método ilustra el truco central del capítulo: derivar para **bajar** el problema a una EDO lineal en la que $u=y'$ hace de variable independiente. Al derivar puede generarse además una [[Solucion Singular y Envolvente| solución singular]].

---

## Ejemplo

> [!ejemplo] Resolver $y=x(1+y')+(y')^3$
> Aquí $\varphi(y')=1+y'$ y $\psi(y')=(y')^3$.
>
> **Paso 1 — derivar respecto a $x$.** Tratando $y'$ como función de $x$ (regla de la cadena):
> $$y'=\frac{d}{dx}\big[x(1+y')+(y')^3\big]=(1+y')+x\,y''+3(y')^2\,y''.$$
> Llamamos $u=y'$ (y $y''=\dfrac{du}{dx}$):
> $$u=(1+u)+x\frac{du}{dx}+3u^{2}\frac{du}{dx}.$$
>
> **Paso 2 — simplificar.** El $u$ de la izquierda cancela con el de la derecha, dejando
> $$0=1+\big(x+3u^{2}\big)\frac{du}{dx}.$$
>
> **Paso 3 — reescribir como lineal en $x(u)$.** Invertimos el papel de las variables: tomamos $u$ como independiente y $x=x(u)$. Dividiendo por $\dfrac{du}{dx}$ y usando $\dfrac{dx}{du}=1/\dfrac{du}{dx}$,
> $$\frac{dx}{du}+x=-3u^{2}.$$
> Es una [[Lineal Primer Orden| EDO lineal]] de primer orden en $x(u)$.
>
> **Paso 4 — factor integrante.** Como el coeficiente de $x$ es $1$, el factor integrante es $e^{\int 1\,du}=e^{u}$:
> $$\frac{d}{du}\big(x\,e^{u}\big)=-3u^{2}e^{u}.$$
> Integrando el lado derecho por partes (dos veces),
> $$\int u^{2}e^{u}\,du=u^{2}e^{u}-2\big(u\,e^{u}-e^{u}\big)=e^{u}\big(u^{2}-2u+2\big),$$
> de modo que
> $$x\,e^{u}=-3\,e^{u}\big(u^{2}-2u+2\big)+c=e^{u}\big(-3u^{2}+6u-6\big)+c.$$
> Despejando $x$ (dividir por $e^u$):
> $$\boxed{\,x(u)=-3u^{2}+6u-6+c\,e^{-u}\,}$$
>
> **Paso 5 — recomponer $y(u)$.** Sustituimos $x(u)$ en la ecuación original $y=x(1+u)+u^{3}$:
> $$y=\big(-3u^{2}+6u-6+c\,e^{-u}\big)(1+u)+u^{3}.$$
> Desarrollando el producto $\big(-3u^{2}+6u-6\big)(1+u)=-3u^{3}+3u^{2}-6$ y sumando $u^3$:
> $$\boxed{\,y(u)=-2u^{3}+3u^{2}-6+c\,e^{-u}(1+u)\,}$$
>
> **Solución paramétrica.** La curva solución, con parámetro $u=y'$, es
> $$\begin{cases}\,x(u)=-3u^{2}+6u-6+c\,e^{-u}\\[2pt] y(u)=-2u^{3}+3u^{2}-6+c\,e^{-u}(1+u)\end{cases}$$

---

## En qué consiste

> [!teoria]
> ¿Por qué derivar **linealiza** el problema? Al derivar $y=x\varphi(u)+\psi(u)$ respecto a $x$, el término $y'$ del lado izquierdo es $u$, y en el derecho aparece $\varphi(u)$ más términos que contienen $\dfrac{du}{dx}$. La ecuación queda
> $$u-\varphi(u)=\big[x\,\varphi'(u)+\psi'(u)\big]\frac{du}{dx}.$$
> Mientras $u\neq\varphi(u)$, podemos dividir y leerla **como lineal en $x(u)$**:
> $$\frac{dx}{du}-\frac{\varphi'(u)}{u-\varphi(u)}\,x=\frac{\psi'(u)}{u-\varphi(u)}.$$
> El truco esencial es **cambiar de variable independiente**: ya no integramos en $x$ sino en $u$, y la no linealidad en $y'$ se disuelve. La forma paramétrica es la consecuencia natural: tenemos $x$ e $y$ ambos como funciones del parámetro $u$. Los valores $u$ que cumplen $u=\varphi(u)$ (donde el método falla al dividir) dan **rectas solución** aparte y pueden contener la [[Solucion Singular y Envolvente| solución singular]].

> [!algoritmo] Resolver una ecuación de Lagrange
> 1. Identifica $\varphi$ y $\psi$ en $y=x\,\varphi(y')+\psi(y')$.
> 2. **Deriva** respecto a $x$ y pon $u=y'$.
> 3. Reagrupa como **lineal en $x(u)$**: $\dfrac{dx}{du}+P(u)\,x=Q(u)$.
> 4. Resuélvela con **factor integrante** $e^{\int P\,du}$ para obtener $x=x(u)$.
> 5. **Sustituye** $x(u)$ en la original para obtener $y=y(u)$; escribe la solución paramétrica.

> [!proposicion]
> Cuando $\varphi(y')=y'$ (es decir, $\varphi$ es la identidad), el coeficiente $u-\varphi(u)$ se anula idénticamente y el método anterior **no produce** una lineal: el problema degenera en el caso [[Clairaut| Clairaut]], cuya solución general es directamente una **familia de rectas**.

## Resumen

> [!resumen]
> | Paso | Acción |
> |---|---|
> | Forma | $y=x\,\varphi(y')+\psi(y')$ |
> | Derivar | respecto a $x$, con $u=y'$ |
> | Reordenar | lineal en $x(u)$: $\dfrac{dx}{du}+P(u)x=Q(u)$ |
> | Resolver | factor integrante $e^{\int P\,du}$ → $x(u)$ |
> | Cerrar | $y(u)$ por sustitución; solución paramétrica $x(u),y(u)$ |

> [!corolario]
> La ecuación de Lagrange es el ejemplo paradigmático de "derivar para linealizar": un problema no lineal en $y'$ se convierte, tomando $u=y'$ como variable independiente, en una EDO **lineal en $x(u)$** resoluble con factor integrante. El precio es que la respuesta sale en forma **paramétrica**.

> [!referencia]
> - Caso particular (identidad $\varphi=y'$): [[Clairaut]].
> - Soluciones extra que puede generar: [[Solucion Singular y Envolvente]].
> - Lineal que se resuelve en el método: [[Lineal Primer Orden]].
> - Vuelta al bloque: [[No Resueltas en y prima/index]].
