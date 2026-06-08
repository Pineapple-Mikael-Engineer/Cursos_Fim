---
title: Coeficientes Indeterminados
tags:
  - ecuaciones
  - edo
  - teoria
  - lineales
  - no-homogenea
  - coeficientes-indeterminados
draft: false
aliases:
  - coeficientes indeterminados
  - método de los coeficientes indeterminados
  - undetermined coefficients
  - method of undetermined coefficients
---

# Método de Coeficientes Indeterminados

> [!definicion]
> Cuando la fuente $f$ de $L[y]=f$ (coeficientes **constantes**) es de **"buena forma"** —un producto
> de **polinomio**, **exponencial** $e^{\alpha x}$ y **seno/coseno** $\cos\beta x$,
> $\operatorname{sen}\beta x$— se propone una particular $y_p$ del **mismo tipo** con coeficientes
> incógnita (los "coeficientes indeterminados"), se sustituye en la EDO y se **igualan coeficientes**
> para despejarlos. Es rápido porque convierte el problema en un **sistema lineal** pequeño, sin
> integrar.

> [!info]
> Una de las dos hijas de [[No Homogenea/index | no homogénea]]: la **rápida**. Solo aplica con
> [[Coeficientes Constantes Homogenea | coeficientes constantes]] y $f$ de "buena forma". Si $f$ no
> encaja (por ejemplo $\sec x$, $\ln x$, $\operatorname{sen}(e^{-x})$) o los coeficientes son variables,
> hay que usar [[No Homogenea/Variacion de Parametros | variación de parámetros]]. Capítulo:
> [[1 Ecuaciones Diferenciales Ordinarias/index | EDO]].

---

## Ejemplo

> [!ejemplo] (a) Exponencial sin resonancia
> **Resolver $y''-3y'+2y=4e^{3x}$.** La homogénea tiene característica $r^2-3r+2=(r-1)(r-2)=0$, raíces
> $1,2$. Como $\alpha=3$ **no** es raíz, propongo $y_p=Ae^{3x}$. Entonces $y_p'=3Ae^{3x}$,
> $y_p''=9Ae^{3x}$, y al sustituir:
> $$(9A-9A+2A)e^{3x}=4e^{3x}\ \Rightarrow\ 2A=4\ \Rightarrow\ A=2.$$
> Luego $y_p=2e^{3x}$ y $y=c_1e^{x}+c_2e^{2x}+2e^{3x}$.

> [!ejemplo] (b) RESONANCIA exponencial
> **Resolver $y''-3y'+2y=e^{x}$.** Ahora $\alpha=1$ **sí** es raíz **simple** de la característica. La
> propuesta ingenua $Ae^{x}$ es solución de la homogénea → daría $0=e^x$, imposible. Aplico la **regla
> de modificación**: multiplico por $x^{s}$ con $s=1$ (multiplicidad de la raíz $1$): $y_p=Axe^{x}$.
> Derivando, $y_p'=A(1+x)e^{x}$, $y_p''=A(2+x)e^{x}$. Sustituyendo:
> $$A\big[(2+x)-3(1+x)+2x\big]e^{x}=A(2+x-3-3x+2x)e^{x}=A(-1)e^{x}=e^{x},$$
> de donde $A=-1$ y $y_p=-xe^{x}$. Solución general $y=c_1e^{x}+c_2e^{2x}-xe^{x}$.

> [!ejemplo] (c) Trigonométrica sin resonancia
> **Resolver $y''+y=\operatorname{sen}2x$.** La homogénea $y''+y=0$ tiene raíces $\pm i$ ($\beta=1$);
> aquí la fuente oscila con $\beta=2\neq1$, **sin** resonancia. Propongo
> $y_p=A\cos2x+B\operatorname{sen}2x$. Entonces $y_p''=-4A\cos2x-4B\operatorname{sen}2x$, y
> $$y_p''+y_p=(-4A+A)\cos2x+(-4B+B)\operatorname{sen}2x=-3A\cos2x-3B\operatorname{sen}2x.$$
> Igualando a $\operatorname{sen}2x$: $-3A=0$ y $-3B=1$, así $A=0$, $B=-\tfrac13$. Luego
> $y_p=-\tfrac13\operatorname{sen}2x$.

> [!ejemplo] (d) RESONANCIA trigonométrica — la amplitud crece
> **Resolver $y''+y=\operatorname{sen}x$.** Ahora la fuente oscila con $\beta=1$, **exactamente** la
> frecuencia natural ($\pm i$ son raíces). La propuesta $A\cos x+B\operatorname{sen}x$ es solución de la
> homogénea → falla. Regla de modificación con $s=1$: $y_p=x(A\cos x+B\operatorname{sen}x)$. Tras
> derivar dos veces y sustituir (los términos en $x$ se cancelan por ser homogéneos) queda
> $$y_p''+y_p=-2A\operatorname{sen}x+2B\cos x=\operatorname{sen}x\ \Rightarrow\ A=-\tfrac12,\ B=0,$$
> de modo que
> $$\boxed{\,y_p=-\tfrac{x}{2}\cos x\,}.$$
> La $y_p$ contiene un factor $x$ que **crece sin cota**: la amplitud de la oscilación aumenta con el
> tiempo. Es el anticipo matemático de la [[Oscilaciones/Oscilaciones Forzadas y Resonancia | resonancia]]
> física: forzar un sistema a su frecuencia natural lo hace oscilar cada vez más fuerte.

---

## En qué consiste

> [!teoria] La tabla de propuestas
> A cada tipo de fuente le corresponde una propuesta del **mismo tipo** (antes de chequear resonancia):
>
> | Fuente $f(x)$ | Propuesta $y_p$ |
> |---|---|
> | polinomio de grado $k$ | polinomio **completo** de grado $k$: $a_kx^k+\dots+a_1x+a_0$ |
> | $e^{\alpha x}$ | $Ae^{\alpha x}$ |
> | $\cos\beta x$ **o** $\operatorname{sen}\beta x$ | $A\cos\beta x+B\operatorname{sen}\beta x$ (¡ambos!) |
> | $e^{\alpha x}\cos\beta x$ | $e^{\alpha x}(A\cos\beta x+B\operatorname{sen}\beta x)$ |
> | producto de los anteriores | **producto** de las propuestas correspondientes |
>
> Dos avisos: para un polinomio hay que poner **todos** los grados hasta $k$ (no solo el término líder),
> y para un seno hay que incluir **también** el coseno (y viceversa), porque al derivar se mezclan.

> [!regla] Regla de modificación (resonancia)
> Si la propuesta de la tabla **ya es solución de la homogénea**, multiplícala por $x^{s}$, donde $s$ es
> la **multiplicidad** de la raíz de la característica asociada a esa fuente:
> - fuente $e^{\alpha x}$ ↔ raíz $r=\alpha$;
> - fuente $\cos\beta x$ / $\operatorname{sen}\beta x$ ↔ raíces $r=\pm i\beta$;
> - fuente $e^{\alpha x}\cos\beta x$ ↔ raíces $r=\alpha\pm i\beta$.
>
> Si esa raíz **no** aparece en la característica, $s=0$ (sin modificación). Si es simple, $s=1$; si es
> doble, $s=2$, etc. El factor $x^{s}$ es justo lo necesario para que la propuesta deje de pertenecer al
> núcleo de $L$.

> [!teorema] Por qué funciona el método
> Si $f$ es una función de "buena forma", entonces $f$ y **todas sus derivadas** generan un espacio
> vectorial de **dimensión finita** $V$, cerrado bajo derivación. El operador $L$ (con coeficientes
> constantes) envía $V$ dentro de $V$. Por tanto existe una $y_p\in V$ (eventualmente en $x^{s}V$ por
> resonancia) y hallarla es resolver un **sistema lineal** de coeficientes.

> [!demostracion]
> **Paso 1 — el espacio cierra bajo derivación.** Cada bloque básico se reproduce al derivar:
> $\dfrac{d}{dx}e^{\alpha x}=\alpha e^{\alpha x}$; $\dfrac{d}{dx}\cos\beta x=-\beta\operatorname{sen}\beta x$
> y $\dfrac{d}{dx}\operatorname{sen}\beta x=\beta\cos\beta x$; y derivar $x^k$ baja el grado. El espacio
> $V$ generado por $f$ y sus derivadas es por ello de **dimensión finita** y satisface $D(V)\subseteq V$.
>
> **Paso 2 — $L$ preserva $V$.** Como $L=a_nD^n+\dots+a_0$ es combinación de potencias de $D$ y cada
> $D^k(V)\subseteq V$, se tiene $L(V)\subseteq V$. Es decir, $L$ restringido a $V$ es un **operador
> lineal de $V$ en $V$** (una matriz, una vez fijada una base de $V$).
>
> **Paso 3 — resolver $L[y_p]=f$ es un sistema lineal.** Buscar $y_p\in V$ con $L[y_p]=f$ es, en la
> base de $V$, resolver $M\mathbf{a}=\mathbf{b}$ para los coeficientes $\mathbf{a}$. Si $L|_V$ es
> invertible (no hay resonancia), hay solución única. Si **no** lo es (resonancia: $f$ o parte de $V$
> está en el núcleo), se amplía el espacio a $x^{s}V$, donde $L$ vuelve a ser sobreyectiva sobre $f$, y
> el sistema vuelve a tener solución. $\blacksquare$

> [!algoritmo] Aplicar coeficientes indeterminados
> 1. Resuelve la **homogénea**: halla las raíces de la característica (con multiplicidades).
> 2. Identifica el **tipo** de $f$ y escribe la propuesta de la **tabla** (polinomio completo; seno+coseno).
> 3. **Chequeo de resonancia:** mira si la propuesta es solución de la homogénea. Si la raíz asociada a
>    $f$ tiene multiplicidad $s\ge1$ en la característica, multiplica la propuesta por $x^{s}$.
> 4. **Sustituye** $y_p$ (y sus derivadas) en $L[y]=f$.
> 5. **Iguala coeficientes** de cada función independiente → sistema lineal; despeja los coeficientes.
> 6. La solución general es $y=y_h+y_p$.

> [!warning]
> Olvidar el **chequeo de resonancia** es el error típico: si la propuesta básica es solución de la
> homogénea, sustituirla da $0=f$ y "no salen" los coeficientes. La señal es esa contradicción: vuelve
> al paso 3 y multiplica por $x^{s}$. También: si $f$ tiene **varios** trozos ($f=f_1+f_2$), usa el
> [[No Homogenea/index | principio de superposición]] y resuelve cada uno por separado.

## Resumen

> [!resumen]
> | Fuente $f$ | Propuesta base | Resonancia |
> |---|---|---|
> | polinomio grado $k$ | polinomio grado $k$ | ×$x^{s}$ si $0$ es raíz |
> | $e^{\alpha x}$ | $Ae^{\alpha x}$ | ×$x^{s}$ si $\alpha$ es raíz |
> | $\cos\beta x$, $\operatorname{sen}\beta x$ | $A\cos\beta x+B\operatorname{sen}\beta x$ | ×$x^{s}$ si $\pm i\beta$ son raíces |
> | $e^{\alpha x}(\cos/\operatorname{sen})\beta x$ | $e^{\alpha x}(A\cos+B\operatorname{sen})\beta x$ | ×$x^{s}$ si $\alpha\pm i\beta$ raíces |
> | producto | producto de propuestas | según la raíz combinada |

> [!corolario]
> El método cambia **cálculo por álgebra**: en vez de integrar, se adivina la forma de $y_p$ (la dicta el
> que las funciones de "buena forma" se reproducen al derivar) y se resuelve un sistema lineal de
> coeficientes. Su único límite es ese: la fuente debe ser de "buena forma" y los coeficientes
> constantes. Fuera de ahí, [[No Homogenea/Variacion de Parametros | variación de parámetros]].

> [!referencia]
> - El método universal alternativo: [[No Homogenea/Variacion de Parametros]].
> - La homogénea y sus raíces: [[Coeficientes Constantes Homogenea]].
> - Por qué $L(V)\subseteq V$: [[Operador Diferencial Lineal]].
> - Vuelta al mapa del bloque: [[No Homogenea/index]].
