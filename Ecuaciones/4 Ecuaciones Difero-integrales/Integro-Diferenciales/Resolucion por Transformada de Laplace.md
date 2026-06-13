---
title: Resolución de Integro-Diferenciales por Transformada de Laplace
tags:
  - ecuaciones
  - difero-integrales
  - teoria
  - integro-diferenciales
  - laplace
  - convolucion
draft: false
aliases:
  - integro-diferenciales por Laplace
  - método de Laplace integro-diferencial
  - núcleo de convolución
  - solving integro-differential equations with Laplace transform
---

# Resolución de Integro-Diferenciales por Transformada de Laplace

> [!definicion]
> Cuando el núcleo es de **convolución** —depende sólo de la diferencia, $K(t-s)$—, una ecuación
> integro-diferencial de **Volterra** se resuelve con la
> [[Transformada de Laplace/index| transformada de Laplace]]. El motivo es doble: la transformada
> convierte la **derivada** en multiplicar por $s$ ($\mathcal{L}\{\varphi'\}=s\Phi-\varphi(0)$) y la
> **integral de convolución** en un producto ($\mathcal{L}\{K*\varphi\}=\hat K(s)\,\Phi(s)$). La
> ecuación, que mezclaba derivar e integrar, se vuelve **algebraica** en $\Phi(s)=\mathcal{L}\{\varphi\}$;
> se despeja $\Phi$ y se **antitransforma** para recuperar $\varphi(t)$.

> [!info]
> El método estrella de la sección [[Integro-Diferenciales/index| integro-diferenciales]]. Sólo aplica
> si el núcleo es de convolución; para un núcleo general $K(t,s)$ se usa
> [[Reduccion a Sistemas| reducción a sistemas]]. La clasificación previa (Volterra/orden/linealidad)
> está en [[Concepto y Clasificacion| concepto y clasificación]]. La misma técnica resuelve las
> [[Ecuaciones de Convolucion| ecuaciones de convolución]] de Volterra.

---

## Ejemplo

> [!ejemplo] $\varphi'(t)=1-\displaystyle\int_{0}^{t}\varphi(s)\,ds$, con $\varphi(0)=0$
> El núcleo es $K(t-s)=1$ (constante), que **sí** es de convolución: la integral es $1*\varphi$. Se
> resuelve de principio a fin.
>
> **Paso 1 — transformar término a término.** Llamamos $\Phi(s)=\mathcal{L}\{\varphi(t)\}$ y aplicamos
> Laplace a cada parte:
> - $\mathcal{L}\{\varphi'(t)\}=s\Phi-\varphi(0)=s\Phi$ (porque $\varphi(0)=0$);
> - $\mathcal{L}\{1\}=\dfrac{1}{s}$;
> - $\mathcal{L}\left\{\int_0^t\varphi(s)\,ds\right\}=\dfrac{\Phi}{s}$ (integrar de $0$ a $t$ es dividir por $s$).
>
> Queda la ecuación **algebraica**:
> $$s\Phi=\frac{1}{s}-\frac{\Phi}{s}.$$
>
> **Paso 2 — despejar $\Phi$.** Multiplicamos por $s$ y agrupamos:
> $$s^{2}\Phi=1-\Phi\ \Longrightarrow\ \Phi\,(s^{2}+1)=1\ \Longrightarrow\ \Phi(s)=\frac{1}{s^{2}+1}.$$
>
> **Paso 3 — antitransformar.** Reconocemos la transformada del seno:
> $$\varphi(t)=\mathcal{L}^{-1}\!\left\{\frac{1}{s^{2}+1}\right\}=\operatorname{sen}t.$$
>
> **Paso 4 — verificar.** Con $\varphi=\operatorname{sen}t$: $\varphi'=\cos t$, y por otro lado
> $$1-\int_0^t\operatorname{sen}s\,ds=1-\big(1-\cos t\big)=\cos t.$$
> Ambos lados coinciden y $\varphi(0)=\operatorname{sen}0=0$. ✓ La solución es $\boxed{\varphi(t)=\operatorname{sen}t}$.

---

## En qué consiste

> [!teorema] Fórmula maestra para Volterra de primer orden con núcleo de convolución
> Para el problema
> $$\varphi'(t)=f(t)+\lambda\int_{0}^{t}K(t-s)\,\varphi(s)\,ds,\qquad \varphi(0)=\varphi_0,$$
> con $F=\mathcal{L}\{f\}$, $\hat K=\mathcal{L}\{K\}$ y $\Phi=\mathcal{L}\{\varphi\}$, la transformada de
> la solución es
> $$\Phi(s)=\frac{F(s)+\varphi_0}{\,s-\lambda\,\hat K(s)\,},$$
> y $\varphi(t)=\mathcal{L}^{-1}\{\Phi(s)\}$.

> [!demostracion]
> **Paso 1 — transformar la ecuación completa.** Aplicamos $\mathcal{L}$ a ambos lados. Por la regla de
> la derivada, $\mathcal{L}\{\varphi'\}=s\Phi-\varphi(0)=s\Phi-\varphi_0$. El término libre da $F(s)$.
> Para la integral usamos el **teorema de convolución**: como $\int_0^t K(t-s)\varphi(s)\,ds=(K*\varphi)(t)$,
> $$\mathcal{L}\{K*\varphi\}=\hat K(s)\,\Phi(s).$$
> La ecuación se transforma en
> $$s\Phi-\varphi_0=F(s)+\lambda\,\hat K(s)\,\Phi.$$
>
> **Paso 2 — agrupar en $\Phi$.** Pasamos todos los términos con $\Phi$ a la izquierda:
> $$s\Phi-\lambda\,\hat K(s)\,\Phi=F(s)+\varphi_0\ \Longrightarrow\ \big(s-\lambda\,\hat K(s)\big)\,\Phi=F(s)+\varphi_0.$$
>
> **Paso 3 — despejar y antitransformar.** Dividiendo,
> $$\Phi(s)=\frac{F(s)+\varphi_0}{s-\lambda\,\hat K(s)},$$
> y la solución es $\varphi(t)=\mathcal{L}^{-1}\{\Phi(s)\}$, que en la práctica se calcula por
> **fracciones parciales** o reconociendo transformadas tabuladas. $\blacksquare$

> [!algoritmo] Método de Laplace para integro-diferenciales de convolución
> 1. **Verificar convolución.** Confirmar que el núcleo depende sólo de $t-s$ (Volterra). Si no, parar y
>    usar [[Reduccion a Sistemas| reducción a sistemas]].
> 2. **Transformar** cada término: $\varphi^{(n)}\to s^n\Phi-(\text{datos iniciales})$; integral de
>    convolución $K*\varphi\to\hat K(s)\,\Phi$; término libre $f\to F(s)$.
> 3. **Despejar $\Phi(s)$**, una incógnita algebraica.
> 4. **Antitransformar** $\Phi(s)$: fracciones parciales y tabla de transformadas inversas.
> 5. **Verificar** sustituyendo en la ecuación y comprobando las condiciones iniciales.

> [!info] Por qué funciona tan bien
> La transformada de Laplace **diagonaliza** simultáneamente dos operaciones que en el dominio del
> tiempo son distintas y enredadas: derivar (operador $D$) e integrar-por-convolución (operador $K*$).
> En el dominio $s$, $D$ es "multiplicar por $s$" y $K*$ es "multiplicar por $\hat K(s)$"; ambas se
> vuelven productos por números (dependientes de $s$). Por eso una ecuación que mezcla las dos colapsa a
> un cociente de funciones de $s$.

## Limitaciones

> [!warning] Necesita convolución y transformabilidad
> - Si el núcleo es $K(t,s)$ **genuino** (no se reduce a $K(t-s)$), el teorema de convolución **no
>   aplica** y el método falla: hay que ir a [[Reduccion a Sistemas| reducir a un sistema]].
> - La antitransformada $\mathcal{L}^{-1}\{\Phi\}$ puede no tener forma cerrada si $s-\lambda\hat K(s)$
>   tiene ceros complicados; a veces sólo se obtiene una serie o una integral de Bromwich.
> - Requiere que $f$, $K$ y $\varphi$ sean de **orden exponencial** para que sus transformadas existan.

## Resumen

> [!resumen]
> | Operación en $t$ | Se vuelve en $s$ |
> |:---|:---|
> | $\varphi'(t)$ | $s\Phi-\varphi_0$ |
> | $\displaystyle\int_0^t K(t-s)\varphi(s)\,ds$ | $\hat K(s)\,\Phi(s)$ |
> | $f(t)$ | $F(s)$ |
> | ecuación integro-diferencial | ecuación **algebraica** en $\Phi$ |
> | solución | $\Phi=\dfrac{F+\varphi_0}{s-\lambda\hat K}$, luego $\mathcal{L}^{-1}$ |

> [!corolario]
> Con núcleo de convolución, resolver una integro-diferencial es **despejar un cociente y mirar una
> tabla**: Laplace transforma derivar-e-integrar en multiplicar-y-dividir. El ejemplo
> $\varphi'=1-\int_0^t\varphi$ que da $\operatorname{sen}t$ es el caso testigo del método.

> [!referencia]
> - La transformada en sí: [[Transformada de Laplace/index]].
> - Cuando no hay convolución: [[Reduccion a Sistemas]].
> - El mismo truco en otra familia: [[Ecuaciones de Convolucion]].
> - Clasificación previa: [[Concepto y Clasificacion]].
> - Marco de la sección: [[Integro-Diferenciales/index]].
