---
title: No Homogénea
order: 8
tags:
  - ecuaciones
  - edo
  - teoria
  - lineales
  - no-homogenea
  - index
draft: false
aliases:
  - EDO no homogénea
  - solución particular
  - nonhomogeneous ODE
  - particular solution
---

# EDO Lineales No Homogéneas

> [!definicion]
> Resolver una EDO lineal **no homogénea** es resolver $L[y]=f$ con la fuente $f\neq0$,
> $$L[y]:=y^{(n)}+p_{n-1}(x)y^{(n-1)}+\dots+p_0(x)y=f(x).$$
> Su solución general se descompone **siempre** en dos piezas,
> $$y=y_h+y_p,$$
> donde $y_h$ es la **solución homogénea** (la combinación de las $n$ soluciones de $L[y]=0$, que ya sabemos hallar) y $y_p$ es **una sola** solución **particular** que "vence" la fuente $f$. Todo el trabajo nuevo se reduce a encontrar **esa única** $y_p$.

> [!info]
> Cuarto bloque de [[Lineales de Orden Superior/index| lineales de orden superior]], dentro del [[1 Ecuaciones Diferenciales Ordinarias/index| capítulo de EDO]]. Aquí se cierra el plan: la homogénea $y_h$ la dan la [[Coeficientes Constantes Homogenea| ecuación característica]] y el [[Operador Diferencial Lineal| operador lineal]]; este bloque añade lo que falta, la particular $y_p$. Es el motor matemático de las [[Oscilaciones/index| oscilaciones forzadas]]: un sistema $m\ddot x+c\dot x+kx=F(t)$ es exactamente $L[y]=f$ con fuente.

---

## Ejemplo

> [!ejemplo] La estructura $y=y_h+y_p$ en acción
> **Resolver $y''-3y'+2y=4e^{3x}$.**
>
> **Paso 1 — la homogénea.** Característica $r^2-3r+2=(r-1)(r-2)=0$ → $r=1,2$. Por tanto
> $$y_h=c_1e^{x}+c_2e^{2x}.$$
>
> **Paso 2 — una particular.** La fuente $4e^{3x}$ es de "buena forma", así que probamos $y_p=Ae^{3x}$. Sustituyendo: $9A-9A+2A=4$ → $A=2$, luego $y_p=2e^{3x}$.
>
> **Paso 3 — sumar.** La solución general es
> $$\boxed{\,y=c_1e^{x}+c_2e^{2x}+2e^{3x}\,}.$$
> Las **dos constantes** viven en $y_h$ (los grados de libertad para las condiciones iniciales); $y_p$ es **un solo** representante fijo que ajusta la fuente. Verifica: cualquier otra particular difiere de $2e^{3x}$ en una solución homogénea, que ya está absorbida en $y_h$.

---

## En qué consiste

> [!teoria] El problema entero se reduce a UNA $y_p$
> La teoría lineal ([[Operador Diferencial Lineal| operador $L$]]) garantiza que el conjunto de soluciones de $L[y]=f$ es un **espacio afín**: fijada cualquier particular $y_p$, **toda** solución es $y_p$ más algo del núcleo de $L$ (la homogénea). En símbolos, si $L[y_p]=f$, entonces
> $$L[y]=f \iff L[y-y_p]=0 \iff y-y_p=y_h.$$
> Como $y_h$ **ya está resuelta** —es $c_1y_1+\dots+c_ny_n$ con el conjunto fundamental de la [[Coeficientes Constantes Homogenea| homogénea]]—, el único problema **nuevo** es producir **una** $y_p$ cualquiera. No importa cuál: dos particulares distintas difieren en una homogénea, que las constantes de $y_h$ ya cubren.
>
> Hay **dos caminos** para fabricar esa $y_p$:
>
> 1. **Coeficientes indeterminados** — rápido, casi sin integrar, pero **solo** cuando $f$ es de "buena forma": un producto de **polinomio**, **exponencial** $e^{\alpha x}$ y **seno/coseno**. La razón es que al derivar estas funciones **se reproducen** (la derivada de $e^{\alpha x}$ es múltiplo de sí misma, la de $\operatorname{sen}\beta x$ es coseno, etc.): vive todo en un espacio finito cerrado bajo derivación, así que se **adivina** una $y_p$ del mismo tipo con coeficientes incógnita y se resuelve un sistema lineal. Detalles en [[Coeficientes Indeterminados| coeficientes indeterminados]].
> 2. **Variación de parámetros** — **universal**: funciona para **cualquier** $f$ continua, e incluso con **coeficientes variables** (con tal de conocer el conjunto fundamental $y_1,\dots,y_n$). El precio es **integrar**. Se construye $y_p=u_1(x)y_1+u_2(x)y_2$ dejando que los "parámetros" $c_i$ se vuelvan funciones $u_i(x)$. Detalles en [[Variacion de Parametros| variación de parámetros]].

> [!teoria] Principio de superposición de fuentes
> La linealidad de $L$ también **divide la fuente**. Si $f=f_1+f_2$ y resolvemos por separado
> $$L[y_{p,1}]=f_1,\qquad L[y_{p,2}]=f_2,$$
> entonces **sumar** las particulares da una particular del total:
> $$L[y_{p,1}+y_{p,2}]=f_1+f_2=f.$$
> Esto deja **descomponer** una fuente complicada en trozos manejables. Por ejemplo, para $y''+y=3e^{2x}+\operatorname{sen}x$ se resuelve la $y_p$ de $3e^{2x}$ y la de $\operatorname{sen}x$ (esta última con resonancia) y se suman. Cada trozo elige el método más cómodo de forma independiente.

> [!info] Las dos hijas: cuándo usar cada una
> | Método | Cuándo usarlo | Coste |
> |---|---|---|
> | [[Coeficientes Indeterminados\|Coeficientes Indeterminados]] | $f$ de "buena forma" (polinomio·$e^{\alpha x}$·$\operatorname{sen}/\cos$) **y** coeficientes constantes | Rápido: resolver un sistema lineal pequeño |
> | [[Variacion de Parametros\|Variación de Parámetros]] | $f$ arbitraria ($\sec x$, $\ln x$, $\operatorname{sen}(e^{-x})$…) **o** coeficientes variables | Integrales (a veces difíciles) |
>
> Regla práctica: si la fuente cabe en la tabla de coeficientes indeterminados, úsalos; en cuanto aparezca un $\tan x$, un $\ln x$ o coeficientes que dependen de $x$, pasa a variación de parámetros.

## Resumen

> [!resumen]
> | Concepto | Contenido |
> |---|---|
> | Problema | $L[y]=f$, con $f\neq0$ |
> | Solución general | $y=y_h+y_p$ |
> | $y_h$ | combinación de las $n$ soluciones homogéneas (ya conocida) |
> | $y_p$ | **una** particular cualquiera; dos difieren en una homogénea |
> | Método rápido | [[Coeficientes Indeterminados\|coef. indeterminados]] (si $f$ de "buena forma") |
> | Método universal | [[Variacion de Parametros\|variación de parámetros]] |
> | Superposición | $f=f_1+f_2\Rightarrow y_p=y_{p,1}+y_{p,2}$ |

> [!corolario]
> Resolver una EDO lineal no homogénea **no** es un problema nuevo de fondo: la teoría lineal ya entrega el espacio de soluciones de la homogénea, y la no homogénea solo añade **trasladar** ese espacio por **una** particular. Por eso el bloque entero gira en torno a una única pregunta —¿cómo construyo una $y_p$?— con dos respuestas según la forma de $f$: adivinar (coeficientes indeterminados) o integrar (variación de parámetros).

> [!referencia]
> - La homogénea que se suma: [[Coeficientes Constantes Homogenea]].
> - El cimiento lineal ($y=y_h+y_p$ como espacio afín): [[Operador Diferencial Lineal]].
> - Método rápido: [[Coeficientes Indeterminados]].
> - Método universal: [[Variacion de Parametros]].
> - La aplicación física (oscilaciones forzadas): [[Oscilaciones/index]].
