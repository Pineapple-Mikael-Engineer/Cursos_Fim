---
title: Linealización y Hartman-Grobman
tags:
  - ecuaciones
  - edo
  - teoria
  - sistemas
  - linealizacion
draft: false
aliases:
  - linealización y hartman-grobman
  - jacobiano
  - equilibrio hiperbólico
  - hartman-grobman
  - linearization
---

# Linealización y Hartman-Grobman

> [!definicion]
> Sea $\mathbf{x}_*$ un equilibrio de $\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x})$ (con
> $\mathbf{f}(\mathbf{x}_*)=\mathbf{0}$). Escribiendo la desviación $\mathbf{u}=\mathbf{x}-\mathbf{x}_*$
> y desarrollando $\mathbf{f}$ por Taylor cerca de $\mathbf{x}_*$,
> $$\mathbf{f}(\mathbf{x})=\underbrace{\mathbf{f}(\mathbf{x}_*)}_{=\,\mathbf{0}}+J\,\mathbf{u}+O(\lVert\mathbf{u}\rVert^2),
> \qquad J=D\mathbf{f}(\mathbf{x}_*)=\left[\frac{\partial f_i}{\partial x_j}\right]_{\mathbf{x}_*},$$
> se obtiene la **linealización** del sistema en $\mathbf{x}_*$:
> $$\dot{\mathbf{u}}=J\,\mathbf{u},$$
> donde $J$ es la **matriz jacobiana** evaluada en el equilibrio. Es el sistema **lineal** que mejor
> aproxima al original cerca de $\mathbf{x}_*$.

> [!info]
> Una nota del bloque [[Sistemas y Dinamica/index| sistemas y dinámica]], dentro del
> [[1 Ecuaciones Diferenciales Ordinarias/index| capítulo de EDO]]. Es el **puente** entre lo lineal
> y lo no lineal: convierte el análisis local de un equilibrio cualquiera en el problema, ya resuelto,
> de [[Sistemas Lineales Autovalores| autovalores]]. El resultado que **justifica** el puente es el
> teorema de Hartman-Grobman. Da la **estabilidad** que estudia [[Estabilidad de Lyapunov| Lyapunov]]
> y el **tipo de equilibrio** que dibuja el [[Puntos de Equilibrio y Plano de Fase| plano de fase]].

---

## Ejemplo

> [!ejemplo] El péndulo: un centro engañoso y una silla honesta
> **Clasificar los equilibrios del péndulo $\ddot\theta+\operatorname{sen}\theta=0$.**
> **Paso 1 — pasar a sistema de primer orden.** Con $\theta$ y $\omega=\dot\theta$:
> $$\dot\theta=\omega,\qquad \dot\omega=-\operatorname{sen}\theta.$$
> **Paso 2 — equilibrios.** $\mathbf{f}=\mathbf{0}$ pide $\omega=0$ y $\operatorname{sen}\theta=0$,
> luego $\theta=0,\pi$ (mód $2\pi$): el péndulo **colgando abajo** $(0,0)$ y **erguido arriba**
> $(\pi,0)$.
> **Paso 3 — jacobiano.**
> $$J(\theta,\omega)=\begin{pmatrix}\dfrac{\partial\dot\theta}{\partial\theta}&\dfrac{\partial\dot\theta}{\partial\omega}\\[4pt]\dfrac{\partial\dot\omega}{\partial\theta}&\dfrac{\partial\dot\omega}{\partial\omega}\end{pmatrix}
> =\begin{pmatrix}0&1\\-\cos\theta&0\end{pmatrix}.$$
> **Paso 4 — clasificar.**
> - En $(0,0)$: $J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, autovalores $\lambda=\pm i$. Parte real
>   **cero** → equilibrio **no hiperbólico**: un **centro** lineal. Físicamente, oscilaciones
>   pequeñas alrededor de la posición de reposo abajo.
> - En $(\pi,0)$: $J=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, autovalores $\lambda=\pm1$. Signos
>   opuestos → **silla**, **inestable**. Físicamente, el péndulo invertido: el más leve empujón lo
>   hace caer.
>
> Hartman-Grobman valida la silla de $(\pi,0)$ tal cual; el centro de $(0,0)$ queda **en suspenso**
> (ver advertencia). Aquí el sistema es conservativo y sí es un centro verdadero, pero eso no lo dice
> la linealización: lo dice la energía.

---

## En qué consiste

> [!teoria]
> Cerca de un equilibrio, **el término dominante de $\mathbf{f}$ es su parte lineal** $J\mathbf{u}$,
> porque los restos $O(\lVert\mathbf{u}\rVert^2)$ son despreciables cuando $\mathbf{u}$ es pequeño. La
> apuesta natural es: *el sistema no lineal se comporta como su linealización cerca del equilibrio*.
> Esa apuesta es **correcta** salvo en un caso límite (parte real nula), y precisarla es el contenido
> de Hartman-Grobman.

> [!algoritmo] Análisis local de un equilibrio
> 1. **Equilibrios:** resolver $\mathbf{f}(\mathbf{x})=\mathbf{0}$.
> 2. **Jacobiano:** calcular $J=D\mathbf{f}$ y evaluarlo en **cada** equilibrio.
> 3. **Autovalores:** hallar el espectro de $J$ en cada equilibrio.
> 4. **Clasificar:** leer tipo y estabilidad del espectro (nodo, silla, foco, centro;
>    [[Sistemas Lineales Autovalores| tabla de casos 2×2]]).
> 5. **Validar:** si el equilibrio es **hiperbólico** (ningún $\operatorname{Re}\lambda=0$), la
>    conclusión vale para el sistema no lineal; si no, la linealización **no decide**.

> [!definicion] Equilibrio hiperbólico
> $\mathbf{x}_*$ es **hiperbólico** si **ningún** autovalor de $J=D\mathbf{f}(\mathbf{x}_*)$ tiene
> parte real cero. Los hiperbólicos son los equilibrios "robustos": pequeñas perturbaciones del
> sistema no cambian su tipo.

> [!teorema] Hartman-Grobman
> Si $\mathbf{x}_*$ es un equilibrio **hiperbólico** de $\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x})$,
> entonces existe un entorno de $\mathbf{x}_*$ y un **homeomorfismo** que lleva las trayectorias del
> sistema no lineal a las de su linealización $\dot{\mathbf{u}}=J\mathbf{u}$. Es decir, los dos
> retratos de fase son **topológicamente equivalentes** cerca de $\mathbf{x}_*$: el **tipo** (nodo,
> silla, foco) y la **estabilidad** del equilibrio no lineal se leen directamente de $J$.

> [!demostracion] Por qué el resto no estropea nada (idea)
> **Paso 1 — separar.** Se escribe $\dot{\mathbf{u}}=J\mathbf{u}+\mathbf{g}(\mathbf{u})$ con
> $\mathbf{g}=O(\lVert\mathbf{u}\rVert^2)$, un término **superlineal**.
> **Paso 2 — el caso hiperbólico es "rígido".** Como ningún autovalor está sobre el eje imaginario,
> cada dirección **crece o decae exponencialmente** a tasa no nula (separación entre subespacios
> estable e inestable). Esa tasa exponencial **domina** al resto cuadrático, que es minúsculo cerca
> del origen.
> **Paso 3 — construir el homeomorfismo.** Con esa dominancia se construye un cambio de coordenadas
> continuo, con inversa continua, que endereza las trayectorias curvas hasta hacerlas coincidir
> topológicamente con las rectas/espirales del flujo lineal. La hiperbolicidad es exactamente lo que
> hace posible esa construcción. $\blacksquare$

> [!warning]
> Si **algún** autovalor tiene $\operatorname{Re}\lambda=0$ (equilibrio **no hiperbólico**, p. ej. un
> **centro** lineal con $\lambda=\pm i\beta$), Hartman-Grobman **no aplica** y la linealización **no
> decide**: el término no lineal, por pequeño que sea, puede convertir el centro en una **espiral
> estable**, en una **espiral inestable** o dejarlo como centro. Caso típico: $\dot x=-y+\mu x(x^2+y^2)$,
> $\dot y=x+\mu y(x^2+y^2)$ linealiza siempre a un centro, pero el signo de $\mu$ decide si la espiral
> entra o sale. En estos casos hay que recurrir a [[Estabilidad de Lyapunov| Lyapunov]], a la energía
> o a teoría de bifurcaciones.

## Resumen

> [!resumen]
> | Paso | Acción |
> |---|---|
> | Equilibrios | resolver $\mathbf{f}(\mathbf{x})=\mathbf{0}$ |
> | Jacobiano | $J=D\mathbf{f}(\mathbf{x}_*)$ en cada equilibrio |
> | Espectro | autovalores de $J$ |
> | Hiperbólico ($\operatorname{Re}\lambda\neq0$) | tipo y estabilidad del no lineal $=$ los de $J$ |
> | No hiperbólico ($\operatorname{Re}\lambda=0$) | la linealización **no decide** |

> [!corolario]
> Linealizar **traduce** el problema no lineal local al lenguaje, ya cerrado, de los autovalores. La
> traducción es **fiel** en los equilibrios hiperbólicos —que son la mayoría y los robustos— y
> **falla** justo en la frontera $\operatorname{Re}\lambda=0$, donde el sistema es tan "neutro" que el
> destino lo decide la no linealidad. Por eso el centro del péndulo necesita un argumento físico que
> la matriz jacobiana, por sí sola, no puede dar.

> [!referencia]
> - El idioma al que se traduce: [[Sistemas Lineales Autovalores]].
> - Qué hacer en el caso no hiperbólico: [[Estabilidad de Lyapunov]].
> - El retrato que clasifica los tipos: [[Puntos de Equilibrio y Plano de Fase]].
