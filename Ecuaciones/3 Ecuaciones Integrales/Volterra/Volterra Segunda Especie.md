---
title: Volterra de Segunda Especie
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - volterra
  - segunda-especie
draft: false
aliases:
  - ecuación de Volterra de segunda especie
  - Volterra segunda especie
  - Volterra equation of the second kind
---

# Volterra de Segunda Especie

> [!definicion]
> Una **ecuación integral de Volterra de segunda especie** busca una función incógnita $\varphi(x)$ que
> aparece **fuera** y **dentro** de una integral con **límite superior variable**:
> $$\varphi(x)=f(x)+\lambda\int_{0}^{x}K(x,t)\,\varphi(t)\,dt,$$
> donde $f(x)$ es el **término libre**, $K(x,t)$ el **núcleo** y $\lambda$ un **parámetro**. Si el núcleo
> es continuo, la solución **existe y es única para todo valor de $\lambda$** —sin excepciones
> espectrales, a diferencia de Fredholm—.

> [!info]
> Es la ecuación central de la [[Volterra/index| familia de Volterra]], dentro del
> [[3 Ecuaciones Integrales/index| capítulo de ecuaciones integrales]]. Cuando $K$ es derivable se
> reduce a un **PVI** por diferenciación; en general se resuelve con la
> [[Resolvente y Nucleos Iterados| resolvente]] o por [[Aproximaciones Sucesivas| aproximaciones sucesivas]]. Su pariente de [[Volterra Primera Especie| primera especie]] se reduce a esta derivando.

---

## Ejemplo

> [!ejemplo] Dos ecuaciones que se vuelven un problema de valor inicial
> **Ejemplo 1 (una derivación).** Resolvamos
> $$\varphi(x)=1+\int_{0}^{x}\varphi(t)\,dt.$$
> El truco es **derivar respecto de $x$**. El término libre $1$ tiene derivada $0$, y para la integral
> usamos la **regla de Leibniz**: derivar $\int_0^x g(t)\,dt$ respecto de $x$ da simplemente el
> integrando evaluado en el extremo, $g(x)$. Por tanto
> $$\varphi'(x)=\varphi(x).$$
> Además, **evaluando la ecuación original en $x=0$** la integral se anula (sus límites coinciden), de
> modo que $\varphi(0)=1$. Tenemos el PVI $\varphi'=\varphi,\ \varphi(0)=1$, cuya solución es
> $$\boxed{\varphi(x)=e^{x}.}$$
> **Verificación.** $1+\int_0^x e^t\,dt = 1+(e^x-1)=e^x=\varphi(x)$. Correcto.
>
> **Ejemplo 2 (dos derivaciones).** Resolvamos
> $$\varphi(x)=x+\int_{0}^{x}(t-x)\,\varphi(t)\,dt.$$
> Aquí el núcleo $K(x,t)=t-x$ **depende de $x$ también dentro de la integral**, así que al derivar hay
> que cuidar los dos efectos: el del extremo y el de derivar el integrando respecto de $x$.
>
> *Reescritura cómoda.* Separamos la integral para sacar la $x$ que no depende de $t$:
> $$\int_0^x (t-x)\varphi(t)\,dt=\int_0^x t\,\varphi(t)\,dt-x\int_0^x \varphi(t)\,dt.$$
> *Primera derivada.* El término del extremo en cada integral se cancela (al evaluar el núcleo $t-x$ en
> $t=x$ da $0$), y solo sobrevive el término de derivar el factor $-x$:
> $$\varphi'(x)=1-\int_0^x \varphi(t)\,dt.$$
> *Segunda derivada.* Volvemos a derivar (Leibniz sobre la integral restante):
> $$\varphi''(x)=-\varphi(x).$$
> *Condiciones iniciales.* En $x=0$ la ecuación original da $\varphi(0)=0$; y la primera derivada en
> $x=0$ da $\varphi'(0)=1$. El PVI $\varphi''=-\varphi,\ \varphi(0)=0,\ \varphi'(0)=1$ tiene solución
> $$\boxed{\varphi(x)=\operatorname{sen}x.}$$
> Un núcleo polinómico ha convertido una ecuación integral en el oscilador armónico.

---

## En qué consiste

> [!teoria]
> La ecuación dice: "el valor de $\varphi$ en $x$ es el dato $f(x)$ **corregido** por toda la historia
> de $\varphi$ entre $0$ y $x$, pesada por el núcleo". Como solo interviene el **pasado** ($t\le x$), no
> hay realimentación global: el problema se va resolviendo "hacia adelante", igual que un PVI avanza en
> el tiempo. Esa es la razón profunda de que **siempre** tenga solución única, sin importar $\lambda$:
> el operador integral es "pequeño" cerca de $x=0$ (intervalo corto) y por eso contractivo.

> [!algoritmo] Cómo resolver una Volterra de 2ª especie
> 1. **¿El núcleo es derivable?** Si $K(x,t)$ (y $f$) son suficientemente suaves, **deriva respecto de
>    $x$** usando la regla de Leibniz hasta eliminar la integral, obteniendo una EDO.
> 2. **Saca las condiciones iniciales** evaluando la ecuación original (y sus derivadas) en $x=0$,
>    donde toda integral $\int_0^0$ se anula.
> 3. **Resuelve el PVI** resultante con los métodos de EDO.
> 4. **Si el núcleo no es derivable** (o no conviene derivar), usa la
>    [[Resolvente y Nucleos Iterados| resolvente]] $\Gamma(x,t;\lambda)$:
>    $\varphi=f+\lambda\int_0^x\Gamma f\,dt$, o las [[Aproximaciones Sucesivas| aproximaciones sucesivas]].
> 5. **Verifica** siempre sustituyendo la solución en la ecuación original.

> [!teorema] Existencia y unicidad
> Si $K(x,t)$ es continua en el triángulo $0\le t\le x\le a$ y $f(x)$ es continua en $[0,a]$, entonces
> la ecuación $\varphi(x)=f(x)+\lambda\int_0^x K(x,t)\varphi(t)\,dt$ tiene una **solución continua única**
> $\varphi(x)$ en $[0,a]$, **cualquiera que sea** el valor de $\lambda$.

> [!info]
> La demostración se delega a [[Aproximaciones Sucesivas]]: se construye la sucesión iterativa
> $\varphi_{n+1}=f+\lambda K\varphi_n$ y se prueba que converge uniformemente (su límite es la única
> solución). Lo distintivo de Volterra es que la cota de error involucra $(x-t)^n/n!$, dominada por una
> exponencial, lo que fuerza la convergencia **sin restringir $\lambda$**.

> [!warning]
> El método de diferenciación **solo aplica si $K$ y $f$ son derivables** las veces necesarias. Con
> núcleos no suaves (p. ej. $1/\sqrt{x-t}$, ver [[Problema de Abel]]) hay que recurrir a la resolvente o
> a transformadas. Además, al evaluar en $x=0$ no olvides que toda integral con ambos límites iguales se
> anula: ahí salen las condiciones iniciales.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Forma | $\varphi(x)=f(x)+\lambda\int_0^x K(x,t)\varphi(t)\,dt$ |
> | Existencia/unicidad | **siempre** ($K$ continuo, todo $\lambda$) |
> | Método rápido | derivar (Leibniz) $\to$ PVI, si $K$ derivable |
> | Método general | [[Resolvente y Nucleos Iterados\|resolvente]] / aproximaciones sucesivas |
> | Condiciones iniciales | evaluar en $x=0$ (integrales $\int_0^0=0$) |
> | Ejemplos | $\varphi=1+\int_0^x\varphi\to e^x$;  $\varphi=x+\int_0^x(t-x)\varphi\to\operatorname{sen}x$ |

> [!corolario]
> Una Volterra de 2ª especie con núcleo suave **es** un problema de valor inicial disfrazado: derivar
> deshace la integral y aparece una EDO con datos en $x=0$. Cuando el núcleo no coopera, la resolvente
> hace el mismo trabajo de forma cerrada.

> [!referencia]
> - El método general en forma cerrada: [[Resolvente y Nucleos Iterados]].
> - La construcción iterativa y su prueba: [[Aproximaciones Sucesivas]].
> - El caso de primera especie: [[Volterra Primera Especie]].
> - Vista de conjunto: [[Volterra/index]].
