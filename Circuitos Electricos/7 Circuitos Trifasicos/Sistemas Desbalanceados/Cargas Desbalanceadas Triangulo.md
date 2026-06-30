---
title: Cargas Desbalanceadas en Triángulo
tags:
  - circuitos-electricos
  - teoria
  - trifasico
draft: false
aliases:
  - triángulo desequilibrado
  - triángulo desbalanceado
  - unbalanced delta
  - unbalanced triangle
---

# Cargas Desbalanceadas en Triángulo

> [!definicion]
> En un **triángulo desequilibrado** las tres impedancias de rama son distintas ($Z_{ab}\neq Z_{bc}\neq Z_{ca}$). Como cada rama está conectada entre dos líneas, **ve directamente la tensión de línea** (que sigue siendo equilibrada porque la fija la fuente), de modo que las corrientes de fase se calculan **independientemente**, rama a rama:
> $$\overline{I}_{ab}=\frac{\overline{V}_{ab}}{Z_{ab}},\qquad \overline{I}_{bc}=\frac{\overline{V}_{bc}}{Z_{bc}},\qquad \overline{I}_{ca}=\frac{\overline{V}_{ca}}{Z_{ca}}.$$
> Lo que **se pierde** con el desequilibrio es la relación $\sqrt3$: las corrientes de línea ya no son $\sqrt3$ veces las de fase, sino la **diferencia** (por LKC) de dos corrientes de fase en cada vértice.

> [!info]
> Es el caso desequilibrado de la [[Conexion Triangulo|conexión triángulo]], dentro de [[Sistemas Desbalanceados/index|sistemas desbalanceados]] del [[7 Circuitos Trifasicos/index|capítulo 7]]. Resulta **más simple** que la [[Cargas Desbalanceadas Estrella|estrella sin neutro]]: aquí no hay desplazamiento del punto neutro porque cada rama recibe siempre la tensión de línea completa. Cuando hace falta descomponer el desequilibrio en secuencias se recurre a [[Componentes Simetricas|componentes simétricas]]. Fraile Mora, cap. 3 §3.10.

---

## Ejemplo

> [!ejemplo] Triángulo resistivo desequilibrado a 400 V
> Un triángulo se alimenta con una tensión de línea equilibrada de $V_L=400\ \text{V}$:
> $$\overline{V}_{ab}=400\angle0^\circ\ \text{V},\qquad \overline{V}_{bc}=400\angle{-}120^\circ\ \text{V},\qquad \overline{V}_{ca}=400\angle{+}120^\circ\ \text{V}.$$
> Las cargas son resistivas pero desiguales: $Z_{ab}=40\ \Omega$, $Z_{bc}=40\ \Omega$, $Z_{ca}=20\ \Omega$. Hallar las **corrientes de fase** y la **corriente de línea** $\overline{I}_a$.
>
> > [!solucion]
> > **Paso 1 — corrientes de fase** (cada rama es un problema monofásico independiente, tensión de línea / impedancia de rama):
> > $$\overline{I}_{ab}=\frac{400\angle0^\circ}{40}=10\angle0^\circ\ \text{A},$$
> > $$\overline{I}_{bc}=\frac{400\angle{-}120^\circ}{40}=10\angle{-}120^\circ\ \text{A},$$
> > $$\overline{I}_{ca}=\frac{400\angle{+}120^\circ}{20}=20\angle{+}120^\circ\ \text{A}.$$
> >
> > **Paso 2 — corriente de línea** $\overline{I}_a$ por LKC en el vértice $a$ ($\overline{I}_a=\overline{I}_{ab}-\overline{I}_{ca}$). Pasamos a binómica:
> > $$\overline{I}_{ab}=10\angle0^\circ=10+j0,$$
> > $$\overline{I}_{ca}=20\angle120^\circ=20(-0{,}5+j\,0{,}866)=-10+j17{,}32.$$
> > $$\overline{I}_a=\overline{I}_{ab}-\overline{I}_{ca}=(10+j0)-(-10+j17{,}32)=20-j17{,}32\ \text{A}.$$
> > En polar:
> > $$\overline{I}_a=\sqrt{20^2+17{,}32^2}\,\angle\arctan\!\frac{-17{,}32}{20}=26{,}5\angle{-}40{,}9^\circ\ \text{A}.$$
> >
> > **Resultado:** corrientes de fase $10$, $10$ y $20\ \text{A}$; corriente de línea $\overline{I}_a\approx26{,}5\angle{-}40{,}9^\circ\ \text{A}$. Nótese que $26{,}5\neq\sqrt3\cdot10$ ni $\sqrt3\cdot20$: con desequilibrio **la relación $\sqrt3$ ya no se cumple**, la corriente de línea hay que obtenerla por LKC.

---

## En qué consiste

> [!teoria]
> La clave del triángulo desequilibrado es que **la tensión de línea no depende de la carga**: la impone la fuente y permanece equilibrada pase lo que pase con las impedancias. Por tanto cada rama del triángulo es un **problema monofásico independiente**:
> $$\overline{I}_{rama}=\frac{\overline{V}_{linea}}{Z_{rama}}.$$
> Una vez conocidas las tres corrientes de fase, las **corrientes de línea** se obtienen aplicando LKC en cada vértice (la corriente de línea que entra es la diferencia de las dos corrientes de rama que concurren en ese vértice):
> $$\overline{I}_a=\overline{I}_{ab}-\overline{I}_{ca},\qquad \overline{I}_b=\overline{I}_{bc}-\overline{I}_{ab},\qquad \overline{I}_c=\overline{I}_{ca}-\overline{I}_{bc}.$$
> La **potencia total** es la suma directa de la disipada por las tres ramas, cada una calculada con la tensión de línea que la alimenta:
> $$P=\frac{V_L^2}{R_{ab}}+\frac{V_L^2}{R_{bc}}+\frac{V_L^2}{R_{ca}}\quad\text{(cargas resistivas)},$$
> o en general $P=\sum V_L\,I_{rama}\cos\varphi_{rama}$.

> [!algoritmo] Resolución del triángulo desequilibrado
> 1. **Tensiones de línea.** Tomar las tres tensiones de línea equilibradas $\overline{V}_{ab}$, $\overline{V}_{bc}$, $\overline{V}_{ca}$ (las fija la fuente).
> 2. **Corriente de cada rama.** $\overline{I}_{rama}=\overline{V}_{linea}/Z_{rama}$, una por una y de forma independiente.
> 3. **Corrientes de línea.** Aplicar LKC en cada vértice: $\overline{I}_a=\overline{I}_{ab}-\overline{I}_{ca}$, $\overline{I}_b=\overline{I}_{bc}-\overline{I}_{ab}$, $\overline{I}_c=\overline{I}_{ca}-\overline{I}_{bc}$.
> 4. **Potencia.** Sumar la potencia de las tres ramas.

> [!proposicion] No hay desplazamiento de tensiones
> A diferencia de la [[Cargas Desbalanceadas Estrella|estrella sin neutro]], el triángulo desequilibrado **no** sufre desplazamiento del punto de referencia ni reparto desigual de tensiones: cada rama recibe **siempre** la tensión de línea completa, sea cual sea su impedancia. Por eso el desequilibrio en triángulo es notablemente **más sencillo de resolver** que en estrella sin neutro, donde el corrimiento del neutro acopla las tres fases.

> [!warning]
> **NO** aplicar $I_L=\sqrt3\,I_F$ cuando hay desequilibrio: esa relación solo es válida en régimen equilibrado. Con cargas desiguales las corrientes de línea deben obtenerse **por LKC, una a una**, y sus módulos pueden ser todos distintos. Lo que sí se conserva, al no existir neutro, es que las **tres corrientes de línea suman cero**: $\overline{I}_a+\overline{I}_b+\overline{I}_c=0$.

---

## Resumen

> [!resumen]
> | Aspecto | Triángulo desequilibrado |
> |---|---|
> | Tensión sobre cada rama | Tensión de línea **completa** y equilibrada (la fija la fuente) |
> | Corriente de fase | Independiente por rama: $\overline{I}_{rama}=\overline{V}_{linea}/Z_{rama}$ |
> | Corriente de línea | Por LKC en cada vértice: $\overline{I}_a=\overline{I}_{ab}-\overline{I}_{ca}$, etc. |
> | Relación $\sqrt3$ | **No** se cumple ($I_L\neq\sqrt3\,I_F$) |
> | Desplazamiento | **No** existe (cada rama ve $V_L$ íntegra) |
> | Potencia total | Suma de las tres ramas: $\sum V_L\,I_{rama}\cos\varphi_{rama}$ |
> | Suma de corrientes de línea | $\overline{I}_a+\overline{I}_b+\overline{I}_c=0$ (sin neutro) |

> [!corolario]
> El triángulo desequilibrado se resuelve casi "a ojo": cada rama por separado con $\overline{V}_{linea}/Z_{rama}$, y luego una resta de fasores por vértice. Toda la dificultad se traslada a un par de operaciones LKC, sin sistemas de ecuaciones acoplados como en la [[Cargas Desbalanceadas Estrella|estrella sin neutro]]. Si el desequilibrio debe analizarse en términos de secuencias (positiva, negativa, homopolar), se acude a [[Componentes Simetricas|componentes simétricas]].

> [!referencia]
> Fraile Mora, *Circuitos Eléctricos*, cap. 3 §3.10 (cargas desequilibradas en triángulo). Véase también [[Conexion Triangulo|conexión triángulo]] equilibrada y [[Sistemas Desbalanceados/index|sistemas desbalanceados]].
