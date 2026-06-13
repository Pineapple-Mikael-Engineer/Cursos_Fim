---
title: Puntos de Equilibrio y Plano de Fase
tags:
  - ecuaciones
  - edo
  - teoria
  - sistemas
  - plano-de-fase
draft: false
aliases:
  - puntos de equilibrio
  - plano de fase
  - retrato de fase
  - clasificacion de equilibrios
  - equilibrium points
  - phase plane
---

# Puntos de Equilibrio y Plano de Fase

> [!definicion]
> Un **punto de equilibrio** (o punto crítico) del sistema autónomo $\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x})$
> es un $\mathbf{x}_*$ que **anula el campo**, $\mathbf{f}(\mathbf{x}_*)=\mathbf{0}$: la solución que
> arranca allí es **constante**, $\mathbf{x}(t)\equiv\mathbf{x}_*$. El **plano de fase** es el plano
> $(x_1,x_2)$ en el que se dibujan las **trayectorias** (las curvas que recorre $\mathbf{x}(t)$, sin
> dibujar el tiempo); el conjunto de todas ellas es el **retrato de fase**. Cerca de un equilibrio de un
> sistema **lineal** $\dot{\mathbf{x}}=A\mathbf{x}$, la forma del retrato la dictan los **autovalores** de
> $A$.

> [!info]
> Es la cara **cualitativa** del bloque [[Sistemas y Dinamica/index| sistemas y dinámica]]: mientras
> [[Sistemas Lineales Autovalores| autovalores]] da la fórmula de la solución, esta nota lee en esos
> mismos autovalores **qué dibuja** el sistema. Es la antesala de la [[Estabilidad de Lyapunov| estabilidad de Lyapunov]] (¿el equilibrio atrae?) y de la [[Linealizacion y Hartman-Grobman| linealización]] (cómo
> trasladar esta clasificación a sistemas no lineales). Pertenece al [[1 Ecuaciones Diferenciales Ordinarias/index| capítulo de EDO]].

---

## Ejemplo

> [!ejemplo] Retratos de fase de los cuatro tipos de equilibrio
> ![[retratos_fase.svg|520]]
>
> Trayectorias en el plano de fase: silla (autovalores reales de signo opuesto), nodo estable (reales
> negativos), foco estable (complejos con parte real negativa) y centro (imaginarios puros).

> [!ejemplo] Clasificar dos matrices por traza y determinante
> **(a) $A=\begin{pmatrix}1&2\\2&1\end{pmatrix}$.** Traza $\tau=\operatorname{tr}A=2$, determinante
> $\Delta=\det A=1-4=-3<0$. Como $\Delta<0$, los autovalores son reales de **signo opuesto**
> ($\lambda=3,\,-1$, ver [[Sistemas Lineales Autovalores| autovalores]]): el origen es una **silla**
> (inestable). Las trayectorias se acercan por la dirección estable ($\lambda=-1$) y escapan por la
> inestable ($\lambda=3$).
>
> **(b) $A=\begin{pmatrix}-1&-2\\2&-1\end{pmatrix}$.** Traza $\tau=-2$, determinante $\Delta=1+4=5>0$.
> El discriminante es $\tau^2-4\Delta=4-20=-16<0$, luego los autovalores son **complejos**
> ($\lambda=-1\pm 2i$). Como $\tau<0$ (parte real negativa), el origen es un **foco estable**: espirales
> que entran girando hacia el origen.

---

## En qué consiste

> [!teoria]
> Para un lineal plano $\dot{\mathbf{x}}=A\mathbf{x}$ con $A$ de $2\times2$, el único equilibrio (si
> $\det A\neq0$) es el **origen**, y todo el retrato lo codifican dos números: la **traza**
> $\tau=\operatorname{tr}A=\lambda_1+\lambda_2$ y el **determinante** $\Delta=\det A=\lambda_1\lambda_2$.
> En efecto, el polinomio característico es $\lambda^2-\tau\lambda+\Delta=0$, así que
> $$\lambda=\frac{\tau\pm\sqrt{\tau^2-4\Delta}}{2}.$$
> El **signo de $\Delta$** decide si las raíces tienen igual o distinto signo; el del discriminante
> $\tau^2-4\Delta$ decide si son reales o complejas; y el de $\tau$, si crecen o decaen. Con esos tres
> signos basta para nombrar el equilibrio sin resolver el sistema.

> [!proposicion] Clasificación del equilibrio de $\dot{\mathbf{x}}=A\mathbf{x}$ (2×2) por $\tau,\Delta$
> | Condición sobre $\tau=\operatorname{tr}A$, $\Delta=\det A$ | Autovalores | Tipo de equilibrio |
> |:--|:--|:--|
> | $\Delta<0$ | reales de **signo opuesto** | **silla** (inestable) |
> | $\Delta>0$, $\ \tau^2>4\Delta$ | reales del **mismo signo** | **nodo** (estable si $\tau<0$) |
> | $\Delta>0$, $\ \tau^2<4\Delta$, $\ \tau\neq0$ | complejos $\alpha\pm i\beta$ | **foco/espiral** (estable si $\tau<0$) |
> | $\tau=0$, $\ \Delta>0$ | imaginarios puros $\pm i\beta$ | **centro** (órbitas cerradas) |
> | $\tau^2=4\Delta$ | reales repetidos | nodo (propio/impropio), caso frontera |

> [!teoria] Por qué cada caso tiene esa forma
> - **Silla** ($\Delta<0$): un modo crece ($\lambda_+>0$) y otro decae ($\lambda_-<0$). Las trayectorias
>   bajan por la separatriz estable y se van por la inestable, formando ramas hiperbólicas.
> - **Nodo** ($\Delta>0$, reales mismo signo): ambos modos decaen ($\tau<0$) o ambos crecen ($\tau>0$);
>   todas las trayectorias entran (o salen) tangentes a la dirección del autovalor más lento.
> - **Foco** (complejos, $\tau\neq0$): la parte real $\alpha=\tau/2$ da decaimiento/crecimiento y la
>   imaginaria $\beta$ da la rotación; resulta una espiral.
> - **Centro** ($\tau=0$, $\Delta>0$): autovalores $\pm i\beta$ imaginarios puros, sin decaimiento; las
>   trayectorias son **órbitas cerradas** (oscilación perpetua), como un oscilador sin amortiguamiento.

> [!proposicion] Estabilidad según el signo de las partes reales
> El origen de $\dot{\mathbf{x}}=A\mathbf{x}$ es:
> - **asintóticamente estable** si **todos** los autovalores tienen parte real $<0$ (equivale, en 2×2,
>   a $\tau<0$ y $\Delta>0$);
> - **inestable** si algún autovalor tiene parte real $>0$;
> - **marginalmente estable** (centro) si las partes reales son $0$ y los autovalores son simples.
>
> En el plano $(\Delta,\tau)$, la **parábola** $\tau^2=4\Delta$ separa nodos de focos, y el **semieje**
> $\Delta>0,\ \tau=0$ es la frontera de centros entre focos estables e inestables.

> [!info]
> En un sistema **no lineal** $\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x})$, el tipo de un equilibrio
> $\mathbf{x}_*$ se obtiene **linealizando**: se reemplaza $A$ por la matriz jacobiana
> $D\mathbf{f}(\mathbf{x}_*)$ y se aplica esta misma tabla. El [[Linealizacion y Hartman-Grobman| teorema de Hartman-Grobman]] garantiza que, **si el equilibrio es hiperbólico** (ninguna parte real nula), el
> retrato local del no lineal es topológicamente igual al de su linealización. El caso del **centro** es
> delicado: la no linealidad puede convertirlo en foco estable o inestable.

## Resumen

> [!resumen]
> | $\tau,\Delta$ | Autovalores | Tipo | Estabilidad |
> |:--|:--|:--|:--|
> | $\Delta<0$ | reales, signos opuestos | silla | inestable |
> | $\Delta>0,\ \tau^2>4\Delta$ | reales, mismo signo | nodo | $\tau<0$ estable |
> | $\Delta>0,\ \tau^2<4\Delta,\ \tau\neq0$ | complejos | foco | $\tau<0$ estable |
> | $\tau=0,\ \Delta>0$ | imaginarios puros | centro | marginal |

> [!corolario]
> El **plano traza-determinante** es un mapa completo de los retratos lineales planos: con solo
> $\tau$ y $\Delta$ se nombra el equilibrio y se decide su estabilidad, sin resolver una sola ecuación.
> Y como cerca de un equilibrio hiperbólico el sistema no lineal **se parece** a su linealización, esta
> tabla es la herramienta básica del análisis cualitativo en dos dimensiones.

> [!referencia]
> - De dónde salen los autovalores: [[Sistemas Lineales Autovalores]].
> - ¿El equilibrio atrae?: [[Estabilidad de Lyapunov]].
> - Llevarlo a sistemas no lineales: [[Linealizacion y Hartman-Grobman]].
