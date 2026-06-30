---
title: Estabilidad de Lyapunov
order: 7
tags:
  - ecuaciones
  - edo
  - teoria
  - sistemas
  - estabilidad
draft: false
aliases:
  - estabilidad de lyapunov
  - función de lyapunov
  - método directo de lyapunov
  - lyapunov stability
  - asymptotic stability
---

# Estabilidad de Lyapunov

> [!definicion]
> Sea $\mathbf{x}_*$ un **equilibrio** de $\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x})$, es decir $\mathbf{f}(\mathbf{x}_*)=\mathbf{0}$. Se dice que:
> - $\mathbf{x}_*$ es **estable (en el sentido de Lyapunov)** si las trayectorias que empiezan cerca permanecen cerca para siempre: para todo $\varepsilon>0$ existe $\delta>0$ tal que
>   $$\lVert\mathbf{x}(0)-\mathbf{x}_*\rVert<\delta \;\Longrightarrow\; \lVert\mathbf{x}(t)-\mathbf{x}_*\rVert<\varepsilon\ \ \forall\, t\ge0.$$
> - $\mathbf{x}_*$ es **asintóticamente estable** si además es estable y existe $\delta_0>0$ tal que
>   $$\lVert\mathbf{x}(0)-\mathbf{x}_*\rVert<\delta_0\;\Longrightarrow\;\lim_{t\to\infty}\mathbf{x}(t)=\mathbf{x}_*.$$
> - $\mathbf{x}_*$ es **inestable** si no es estable: existe algún $\varepsilon$ para el que ningún $\delta$ sirve (hay trayectorias que arrancan arbitrariamente cerca y se alejan).

> [!info]
> Una nota del bloque [[Sistemas y Dinamica/index| sistemas y dinámica]], dentro del [[1 Ecuaciones Diferenciales Ordinarias/index| capítulo de EDO]]. Es la **teoría del comportamiento a largo plazo** cerca de un equilibrio. Para sistemas lineales la estabilidad se lee del espectro ([[Sistemas Lineales Autovalores| autovalores]]); para los no lineales se decide casi siempre por [[Linealizacion y Hartman-Grobman| linealización]], y cuando esa falla —o cuando se quiere una conclusión **global**— se usa el **método directo** de esta nota. La imagen geométrica vive en el [[Puntos de Equilibrio y Plano de Fase| plano de fase]].

---

## Ejemplo

> [!ejemplo] Una función de Lyapunov que decide la estabilidad
> **Estudiar el equilibrio $\mathbf{x}_*=(0,0)$ del sistema**
> $$\dot x_1=-x_1+x_2-x_1(x_1^2+x_2^2),\qquad \dot x_2=-x_1-x_2-x_2(x_1^2+x_2^2).$$
> El término no lineal hace difícil resolverlo, pero no hace falta resolver nada. **Paso 1 — proponer una "energía".** Tómese $V(\mathbf{x})=x_1^2+x_2^2$. Es **definida positiva**: $V(0,0)=0$ y $V>0$ en cualquier otro punto. **Paso 2 — derivar a lo largo de las trayectorias.** Por la regla de la cadena,
> $$\dot V=\frac{\partial V}{\partial x_1}\dot x_1+\frac{\partial V}{\partial x_2}\dot x_2
> =2x_1\dot x_1+2x_2\dot x_2.$$
> Sustituyendo $\dot x_1,\dot x_2$ y simplificando (los términos cruzados $+x_1x_2$ y $-x_1x_2$ se cancelan):
> $$\dot V=-2(x_1^2+x_2^2)-2(x_1^2+x_2^2)^2=-2V-2V^2.$$
> **Paso 3 — leer el signo.** Como $\dot V<0$ en todo punto salvo en el origen, la "energía" $V$ **decrece estrictamente** sobre cada trayectoria: el sistema cae inevitablemente al fondo del cuenco $V=0$. Por el teorema de abajo, $(0,0)$ es **asintóticamente estable** (de hecho globalmente, porque $\dot V<0$ en todo el plano).

> [!ejemplo] El péndulo amortiguado: la energía física es una Lyapunov natural
> Para $\ddot\theta+c\dot\theta+\dfrac{g}{\ell}\operatorname{sen}\theta=0$ con roce $c>0$, la **energía mecánica** $E=\tfrac12\ell^2\dot\theta^2+g\ell(1-\cos\theta)$ cumple $\dot E=-c\,\ell^2\dot\theta^2\le0$: el rozamiento **disipa** energía. Esa $E$ es una función de Lyapunov "regalada por la física" y demuestra que el reposo abajo ($\theta=0$) es estable; con un argumento extra (LaSalle) se ve que es **asintóticamente estable**. La moraleja: muchas funciones de Lyapunov son **la energía del sistema**.

---

## En qué consiste

> [!teoria]
> La estabilidad describe **qué hace el sistema si lo perturbas un poco** desde el equilibrio. Hay dos caminos para decidirla:
> 1. **Indirecto (espectral).** Si el sistema es lineal —o se ha linealizado— la estabilidad se lee de los autovalores de la matriz: la parte real de cada autovalor dice si el modo asociado crece o decae.
> 2. **Directo (geométrico).** Buscar una función escalar $V(\mathbf{x})$ que actúe como una "energía" o "distancia al equilibrio": si esa energía **no crece** sobre las trayectorias, el sistema no puede escapar, y queda atrapado en los conjuntos de nivel $\{V\le c\}$.

> [!teorema] Estabilidad del sistema lineal $\dot{\mathbf{x}}=A\mathbf{x}$
> Para el equilibrio $\mathbf{x}_*=\mathbf{0}$ de un sistema **lineal** con $A$ constante:
> - es **asintóticamente estable** $\iff$ **todos** los autovalores de $A$ cumplen $\operatorname{Re}\lambda<0$;
> - es **estable (no asintóticamente)** si $\operatorname{Re}\lambda\le0$ para todos y los que tienen $\operatorname{Re}\lambda=0$ son **simples** (no deficientes);
> - es **inestable** si **algún** autovalor tiene $\operatorname{Re}\lambda>0$ (o si hay uno con $\operatorname{Re}\lambda=0$ repetido y deficiente, que aporta un factor $t$ que crece).

> [!demostracion] Por qué la parte real manda (esquema)
> **Paso 1 — modos.** Cada autovalor $\lambda$ produce un modo $\mathbf{v}\,e^{\lambda t}$ ([[Sistemas Lineales Autovalores| autovalores]]). Su tamaño es $\lVert\mathbf{v}\,e^{\lambda t}\rVert=\lVert\mathbf{v}\rVert\,e^{(\operatorname{Re}\lambda)\,t}$. **Paso 2 — decaer o crecer.** Si $\operatorname{Re}\lambda<0$, $e^{(\operatorname{Re}\lambda)t}\to0$; si $\operatorname{Re}\lambda>0$, explota; si $\operatorname{Re}\lambda=0$, queda acotado (oscila sin decaer) **siempre que** el autovalor sea simple. **Paso 3 — superponer.** La solución general es suma de modos; tiende a $\mathbf{0}$ si y solo si **todos** decaen, está acotada si ninguno crece, y escapa si alguno crece. $\blacksquare$

> [!teorema] Método directo de Lyapunov
> Sea $V$ una función $C^1$ en un entorno de $\mathbf{x}_*$, **definida positiva** ($V(\mathbf{x}_*)=0$ y $V(\mathbf{x})>0$ para $\mathbf{x}\neq\mathbf{x}_*$), y sea
> $$\dot V(\mathbf{x})=\nabla V(\mathbf{x})\cdot\mathbf{f}(\mathbf{x})$$
> su derivada **a lo largo de las trayectorias**. Entonces:
> - si $\dot V\le0$ en el entorno, $\mathbf{x}_*$ es **estable**;
> - si $\dot V<0$ para todo $\mathbf{x}\neq\mathbf{x}_*$, $\mathbf{x}_*$ es **asintóticamente estable**.
>
> A una tal $V$ se la llama **función de Lyapunov**.

> [!demostracion] Idea geométrica del método directo
> **Paso 1 — los conjuntos de nivel encajonan.** Como $V$ es definida positiva, sus conjuntos de nivel $\{V=c\}$ son superficies cerradas que rodean a $\mathbf{x}_*$, anidadas como las capas de una cebolla; cuanto menor es $c$, más cerca del equilibrio. **Paso 2 — $V$ no crece.** A lo largo de una trayectoria, $\dfrac{d}{dt}V(\mathbf{x}(t))=\nabla V\cdot\dot{\mathbf{x}}=\nabla V\cdot\mathbf{f}=\dot V\le0$. Luego la trayectoria solo puede **bajar o quedarse** en capas de menor o igual nivel: una vez dentro de $\{V\le c\}$, **no puede salir**. **Paso 3 — atrapamiento $\Rightarrow$ estabilidad.** Dado $\varepsilon$, se elige una capa $\{V\le c\}$ contenida en la bola de radio $\varepsilon$; todo lo que arranque dentro de esa capa (un cierto $\delta$) queda atrapado, luego permanece a distancia $<\varepsilon$. Eso es la definición de estable. **Paso 4 — descenso estricto $\Rightarrow$ atracción.** Si además $\dot V<0$, la energía decrece estrictamente y no puede estancarse en ningún nivel $c>0$; obligada a seguir bajando, la trayectoria alcanza $V=0$, esto es $\mathbf{x}_*$. Por tanto el equilibrio es asintóticamente estable. $\blacksquare$

> [!proposicion] Inestabilidad por Lyapunov (Chetaev, idea)
> El método también detecta **inestabilidad**: si existe $V$ con $V(\mathbf{x}_*)=0$ que toma valores **positivos** arbitrariamente cerca de $\mathbf{x}_*$ y allí $\dot V>0$, entonces $\mathbf{x}_*$ es inestable (hay una "cuesta abajo" de energía creciente por la que el sistema se escapa).

> [!warning]
> Encontrar una función de Lyapunov es un **arte**, no un algoritmo: no hay receta general. Por eso, que **no encuentres** una $V$ adecuada **no demuestra** que el equilibrio sea inestable; solo significa que ese método no concluyó. Para sistemas mecánicos, **prueba primero con la energía**; para lineales estables existe siempre una $V$ cuadrática $V=\mathbf{x}^{\!\top}P\mathbf{x}$ (ecuación de Lyapunov $A^{\!\top}P+PA=-Q$), pero hallarla a mano puede ser laborioso.

## Resumen

> [!resumen]
> | Concepto | Condición |
> |---|---|
> | Estable | trayectorias cercanas **permanecen** cerca ($\varepsilon$-$\delta$) |
> | Asintóticamente estable | estable **y** $\mathbf{x}(t)\to\mathbf{x}_*$ |
> | Inestable | no estable (alguna trayectoria se aleja) |
> | Lineal: asint. estable | todos los $\operatorname{Re}\lambda<0$ |
> | Lineal: estable | $\operatorname{Re}\lambda\le0$, los nulos simples |
> | Lyapunov: $V>0$, $\dot V\le0$ | estable |
> | Lyapunov: $V>0$, $\dot V<0$ | asintóticamente estable |

> [!corolario]
> La estabilidad **no exige resolver** la ecuación. Para lineales la decide el signo de las partes reales de los autovalores; para no lineales, una función de Lyapunov $V$ —típicamente la energía— certifica que el equilibrio atrapa a sus vecinos sin necesidad de conocer las trayectorias. El método directo es además el único que da conclusiones **globales** y el que sobrevive cuando la linealización no decide.

> [!referencia]
> - El criterio espectral, en detalle: [[Sistemas Lineales Autovalores]].
> - Cuando se linealiza para usarlo: [[Linealizacion y Hartman-Grobman]].
> - El retrato geométrico de los equilibrios: [[Puntos de Equilibrio y Plano de Fase]].
