---
title: Lugar de las Raíces (Root Locus)
order: 1
tags:
  - control-clasico
  - diseño
  - lugar-raices
draft: false
aliases:
  - root locus
  - lgr
  - lugar de las raíces
---

# Lugar de las Raíces (Root Locus)

> [!definicion]
> El **lugar de las raíces** es el lugar geométrico de los polos de lazo cerrado de un sistema cuando la ganancia $K$ varía de $0$ a $\infty$. Para realimentación con $G(s)$ en directa y $H(s)$ en retorno, esos polos son las raíces de la **ecuación característica**:
> $$1+KG(s)H(s)=0\qquad\Longleftrightarrow\qquad KG(s)H(s)=-1.$$
> En $K=0$ los polos de lazo cerrado están en los polos de $G(s)H(s)$; en $K\to\infty$, en sus ceros finitos o en el infinito. Se traza con reglas, sin resolver la ecuación para cada $K$.

> [!info] Subnotas de esta sección
> - [[Condicion Angulo Magnitud | Condiciones de ángulo y magnitud]]: el criterio $\sum\angle=180^\circ(2k+1)$ que decide si $s\in$ LGR y el $K$ asociado. Base de todo lo demás.
> - [[Reglas Construccion | Reglas de construcción]]: las siete reglas para trazar el LGR a mano, con ejemplo completo.
> - [[Trayectoria eje real y Asintotas | Eje real y asíntotas]]: tramos del eje real y asíntotas ($\sigma_a$, $\theta_a$).
> - [[Puntos Ruptura | Puntos de ruptura]]: dónde las ramas dejan el eje real, vía $dK/ds=0$.
> - [[Angulos Salida Llegada | Ángulos de salida/llegada]]: dirección de salida en polos/ceros complejos.
> - [[Cruce Eje Imaginario | Cruce con el eje imaginario]]: ganancia crítica $K_{\text{crítico}}$ y frontera de estabilidad.
> - Compensadores: [[Lead | lead]] (mejora transitorio) y [[Lag | lag]] (mejora error estacionario).

---

## Ejemplo

> [!ejemplo]
> **LGR completo de $G(s)H(s)=\dfrac{K}{s(s+2)}$** (recorre todas las subnotas).
>
> ![[lgr_ejemplo_angulos.svg|600]]
>
> **1. Ramas.** Polos $0,-2$ ($n=2$), sin ceros → **2 ramas**.
>
> **2. Eje real** ([[Trayectoria eje real y Asintotas]]): tramo $(-2,0)$ (1 polo a la derecha, impar) → es LGR.
>
> **3. Asíntotas:** $n-m=2$, $\sigma_a=\dfrac{0+(-2)}{2}=-1$, $\theta_a=\pm90^\circ$.
>
> **4. Punto de ruptura** ([[Puntos Ruptura]]): $K=-s(s+2)$, $\dfrac{dK}{ds}=-(2s+2)=0\Rightarrow s=-1$; ahí $K=1$.
>
> **5. Condición de magnitud** ([[Condicion Angulo Magnitud]]) en $s=-1$: $K=\dfrac{|{-1}|\cdot|1|}{1}=1$ (coincide con el breakaway).
>
> **6. Para $K>1$** las ramas son complejas: $s^2+2s+K=0\Rightarrow s=-1\pm j\sqrt{K-1}$, suben por la vertical $\sigma=-1$ (la asíntota). El sistema es estable para todo $K>0$.
>
> **Trazo final:** dos ramas salen de $0$ y $-2$, se juntan en $s=-1$ con $K=1$ y se separan verticalmente hacia $\pm j\infty$ a lo largo de la asíntota.

---

## En qué consiste

> [!teoria] De la realimentación a $1+KG(s)H(s)=0$
> ![[lgr_diagrama_bloques.svg|400]]
>
> La transferencia de lazo cerrado es $T(s)=\dfrac{KG(s)}{1+KG(s)H(s)}$. Sus polos son las raíces del denominador, es decir de la ecuación característica $1+KG(s)H(s)=0$. El LGR es el dibujo de cómo migran esas raíces al barrer $K$.

> [!teorema] Condición de ángulo (pertenencia al LGR)
> $$\sum_i\angle(s+z_i)-\sum_j\angle(s+p_j)=180^\circ(2k+1).$$
>
> ![[lgr_angulo_vectores.svg|600]]

> [!teorema] Condición de magnitud (valor de $K$)
> $$K=\frac{\prod_j\|s+p_j\|}{\prod_i\|s+z_i\|}.$$

> [!info] Usos
> 1. Visualizar el movimiento de los polos al variar $K$.
> 2. Hallar el rango de $K$ para estabilidad (cruce con $j\omega$).
> 3. Diseñar compensadores [[Lead | lead]]/[[Lag | lag]] para reubicar polos.
> 4. Analizar el efecto de añadir polos y ceros.

---

## Resumen

> [!resumen]
> | Regla / concepto | Fórmula | Subnota |
> |---|---|---|
> | Ecuación característica | $1+KG(s)H(s)=0$ | — |
> | Ángulo (¿$s\in$ LGR?) | $\sum\angle(s+z_i)-\sum\angle(s+p_j)=180^\circ(2k+1)$ | [[Condicion Angulo Magnitud]] |
> | Magnitud (valor de $K$) | $K=\dfrac{\prod\|s+p_j\|}{\prod\|s+z_i\|}$ | [[Condicion Angulo Magnitud]] |
> | Ramas / simetría | $n$ ramas, simétricas al eje real | [[Reglas Construccion]] |
> | Eje real | nº impar a la derecha | [[Trayectoria eje real y Asintotas]] |
> | Asíntotas | $\sigma_a=\dfrac{\sum p-\sum z}{n-m}$, $\theta_a=\dfrac{180^\circ(2k+1)}{n-m}$ | [[Trayectoria eje real y Asintotas]] |
> | Ruptura | $dK/ds=0$ | [[Puntos Ruptura]] |
> | Cruce $j\omega$ | Routh-Hurwitz o $s=j\omega$ | [[Cruce Eje Imaginario]] |

> [!corolario]
> El LGR convierte el problema algebraico "¿dónde están los polos de lazo cerrado para cada $K$?" en un trazo geométrico regido por la [[Condicion Angulo Magnitud | condición de ángulo]]. Con las [[Reglas Construccion | reglas de construcción]] se obtiene la estabilidad, el $K_{\text{crítico}}$ y el punto de partida para [[Lead | compensar]] el sistema.

> [!warning]
> 1. El LGR muestra solo los **polos** de lazo cerrado, no sus ceros.
> 2. Supone $K$ **real y positivo** y realimentación negativa ($H(s)\neq1$ → usar $G(s)H(s)$).
> 3. Con varios parámetros simultáneos se requieren técnicas más avanzadas.
> 4. No da por sí solo la respuesta temporal (sobrepico, etc.) sin cálculos adicionales.

> [!referencia]
> - Estabilidad y $K_{\text{crítico}}$: [[Cruce Eje Imaginario]] y [[Routh Hurwitz/Ajuste Parametros | ajuste de parámetros]].
> - Compensación: [[Lead]], [[Lag]].
> - Polos y ceros de $G(s)H(s)$: [[Polos Ceros]].
