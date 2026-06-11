---
title: Sistemas de Partículas
tags:
  - dinamica
  - teoria
  - particula
  - sistemas
draft: false
aliases:
  - centro de masa
  - teorema de König
  - movimiento del centro de masa
  - systems of particles
  - center of mass
  - König theorem
---

# Sistemas de Partículas $\;\vec r_G=\dfrac1m\sum_i m_i\vec r_i$

> [!definicion]
> Un **sistema de partículas** es un conjunto de $N$ masas $m_i$ (con masa total $m=\sum_i m_i$) cuyas
> posiciones $\vec r_i$ evolucionan bajo fuerzas **externas** $\vec F_i^{ext}$ e **internas** $\vec F_{ij}$
> (la que la partícula $j$ ejerce sobre la $i$). Su punto representativo es el **centro de masa** (CM):
> $$\boxed{\;\vec r_G=\frac1m\sum_i m_i\vec r_i,\qquad m=\sum_i m_i\;}$$
> De él se derivan el **momento lineal total** $\vec P=\sum_i m_i\vec v_i=m\vec v_G$ y el **momento
> angular total** $\vec H_O=\sum_i\vec r_i\times m_i\vec v_i$. El sistema se gobierna por **tres teoremas**,
> todos consecuencia de la segunda ley de Newton más la **3ª ley** (las fuerzas internas se cancelan):
> $$\sum\vec F_{ext}=m\vec a_G,\qquad \frac{d\vec H_O}{dt}=\sum\vec M_{O,ext},\qquad
> T=\tfrac12 m v_G^2+T_{rel}\ \text{(König)}.$$

> [!info]
> Quinta sección de la [[1 Particula/index | partícula]] ([[Dinamica/index | Dinámica]]): es el **puente
> al [[4 Cuerpo Rigido/index| cuerpo rígido]]**, pues un sólido es un sistema de partículas **rígidamente
> unidas** (las distancias $|\vec r_i-\vec r_j|$ son fijas). Generaliza [[Impulso y Momento]] de una
> partícula a $N$ partículas: el momento total y su momento angular obedecen leyes idénticas a las de un
> punto material situado en el CM. Toma la cinética de [[Cinetica de la Particula]] partícula a partícula
> y la **suma**. Referencia: Taylor, *Classical Mechanics*, cap. 3.

---

## Ejemplo

> [!ejemplo]
> **Proyectil que explota en vuelo.**
>
> Un proyectil de masa $m$ se lanza describiendo una **parábola** bajo la gravedad. En cierto instante
> **explota** en el aire fragmentándose en varios pedazos que salen en todas direcciones. ¿Qué
> trayectoria sigue el **centro de masa** del conjunto tras la explosión?
>
> La clave es distinguir fuerzas internas de externas: la explosión es un fenómeno **interno** (las
> fuerzas que separan los fragmentos son pares acción-reacción entre ellos). La única fuerza **externa**
> sigue siendo el peso.
>
> > [!solucion]
> > **Antes de explotar.** La fuerza externa neta es el peso, $\sum\vec F_{ext}=m\vec g$, luego por el
> > teorema del movimiento del CM:
> > $$m\vec a_G=m\vec g\ \Rightarrow\ \vec a_G=\vec g.$$
> > El CM cae con aceleración $\vec g$: describe una **parábola**.
> > **Durante y después de la explosión.** Las fuerzas internas **no aparecen** en $\sum\vec F_{ext}$
> > (se cancelan por pares, 3ª ley). La fuerza externa **no cambia**: sigue siendo $m\vec g$. Por tanto
> > $$\vec a_G=\vec g\quad\text{(sin alterar)}.$$
> > **Conclusión.** El centro de masa **sigue exactamente la misma parábola** que habría seguido el
> > proyectil sin explotar, como si nada hubiera pasado. La explosión solo **redistribuye** los
> > fragmentos alrededor de ese punto fantasma; cada pedazo traza su propia parábola, pero su CM
> > prosigue imperturbable. (Si un fragmento cae verticalmente, otro debe adelantarse para que el
> > promedio ponderado mantenga la curva.)

---

## En qué consiste

> [!teoria] Internas vs. externas: por qué el CM lo resume todo
> - Sobre cada partícula $i$ actúan dos clases de fuerzas: las **externas** $\vec F_i^{ext}$ (peso,
>   contactos con el exterior, campos) y las **internas** $\vec F_{ij}$ que le ejercen las demás
>   partículas del sistema. La **3ª ley** impone $\vec F_{ij}=-\vec F_{ji}$.
> - Al **sumar** la segunda ley sobre todas las partículas, las internas aparecen siempre en **pares
>   opuestos** y se cancelan. Lo que sobrevive es solo lo externo: el sistema entero responde como un
>   **único punto material** de masa $m$ situado en el CM.
> - Esa cancelación vale para el **momento lineal** (movimiento del CM) y para el **momento angular**
>   (si las fuerzas internas son **centrales**), pero **no para la energía**: el trabajo de las fuerzas
>   internas **no** se anula en general (una explosión interna inyecta energía cinética).
> - Por eso un sólido se analiza en dos pasos: la **traslación** de su CM (este capítulo) y su
>   **rotación** alrededor de él → [[4 Cuerpo Rigido/index| cuerpo rígido]].

> [!teorema] Movimiento del centro de masa
> La fuerza externa neta determina la aceleración del CM como si toda la masa estuviera en él:
> $$\boxed{\;\sum\vec F_{ext}=m\,\vec a_G\;}$$

> [!demostracion]
> **Paso 1 — Segunda ley en cada partícula.** Para la partícula $i$, la fuerza neta es la externa más la
> suma de las internas que le ejercen las demás:
> $$\vec F_i^{ext}+\sum_{j}\vec F_{ij}=m_i\vec a_i.$$
> **Paso 2 — Sumar sobre todas las partículas.** Sumando en $i$:
> $$\sum_i\vec F_i^{ext}+\sum_i\sum_j\vec F_{ij}=\sum_i m_i\vec a_i.$$
> **Paso 3 — Las internas se cancelan (3ª ley).** En la doble suma cada par aparece dos veces:
> $\vec F_{ij}+\vec F_{ji}=\vec0$ porque $\vec F_{ij}=-\vec F_{ji}$. Luego
> $$\sum_i\sum_j\vec F_{ij}=\vec0.$$
> **Paso 4 — Identificar la aceleración del CM.** Como $\vec r_G=\frac1m\sum_i m_i\vec r_i$, derivando
> dos veces (las $m_i$ son constantes):
> $$\sum_i m_i\vec a_i=\frac{d^2}{dt^2}\sum_i m_i\vec r_i=\frac{d^2}{dt^2}\big(m\,\vec r_G\big)=m\,\vec a_G.$$
> **Paso 5 — Conclusión.** Reuniendo los pasos 2-4, $\displaystyle\sum_i\vec F_i^{ext}=m\,\vec a_G$, es
> decir $\sum\vec F_{ext}=m\vec a_G$. $\blacksquare$

> [!teorema] Momento angular del sistema
> La derivada del momento angular total respecto a un punto fijo $O$ iguala el momento de las fuerzas
> **externas**:
> $$\boxed{\;\frac{d\vec H_O}{dt}=\sum\vec M_{O,ext},\qquad \vec H_O=\sum_i\vec r_i\times m_i\vec v_i\;}$$

> [!demostracion]
> **Paso 1 — Derivar el momento angular total.** Con $O$ fijo,
> $$\frac{d\vec H_O}{dt}=\frac{d}{dt}\sum_i\vec r_i\times m_i\vec v_i
> =\sum_i\dot{\vec r}_i\times m_i\vec v_i+\sum_i\vec r_i\times m_i\vec a_i.$$
> **Paso 2 — El primer término se anula.** Como $\dot{\vec r}_i=\vec v_i$, cada sumando es
> $\vec v_i\times m_i\vec v_i=\vec0$ (producto vectorial de un vector consigo mismo). Queda
> $$\frac{d\vec H_O}{dt}=\sum_i\vec r_i\times m_i\vec a_i.$$
> **Paso 3 — Insertar la segunda ley.** Con $m_i\vec a_i=\vec F_i^{ext}+\sum_j\vec F_{ij}$:
> $$\frac{d\vec H_O}{dt}=\sum_i\vec r_i\times\vec F_i^{ext}+\sum_i\sum_j\vec r_i\times\vec F_{ij}.$$
> **Paso 4 — Los momentos internos se cancelan por pares.** Agrupando el par $(i,j)$:
> $$\vec r_i\times\vec F_{ij}+\vec r_j\times\vec F_{ji}
> =\vec r_i\times\vec F_{ij}-\vec r_j\times\vec F_{ij}=(\vec r_i-\vec r_j)\times\vec F_{ij},$$
> donde se usó $\vec F_{ji}=-\vec F_{ij}$. Si las fuerzas internas son **centrales** —dirigidas a lo
> largo de la recta que une las partículas— entonces $\vec F_{ij}$ es **paralela** a $\vec r_i-\vec r_j$,
> y su producto vectorial es $\vec0$. Así toda la doble suma se anula.
> **Paso 5 — Conclusión.** Sobrevive solo el momento de las fuerzas externas:
> $$\frac{d\vec H_O}{dt}=\sum_i\vec r_i\times\vec F_i^{ext}=\sum\vec M_{O,ext}.\qquad\blacksquare$$

> [!teorema] Teorema de König (energía cinética)
> La energía cinética de un sistema se separa en la del CM más la del movimiento **relativo** a él:
> $$\boxed{\;T=\tfrac12\,m\,v_G^2+\underbrace{\tfrac12\sum_i m_i v_i'^2}_{T_{rel}}\;}$$
> donde $\vec v_i'=\vec v_i-\vec v_G$ es la velocidad de la partícula $i$ **vista desde el CM**.

> [!demostracion]
> **Paso 1 — Descomponer cada velocidad.** Toda velocidad se escribe como la del CM más la relativa:
> $$\vec v_i=\vec v_G+\vec v_i',\qquad \vec v_i'=\vec v_i-\vec v_G.$$
> **Paso 2 — Sustituir en la energía cinética.** Usando $v_i^2=\vec v_i\cdot\vec v_i$:
> $$T=\sum_i\tfrac12 m_i\,\vec v_i\cdot\vec v_i
> =\sum_i\tfrac12 m_i(\vec v_G+\vec v_i')\cdot(\vec v_G+\vec v_i').$$
> **Paso 3 — Desarrollar el producto escalar.** Cada término genera tres piezas:
> $$T=\underbrace{\sum_i\tfrac12 m_i v_G^2}_{\text{(A)}}
> +\underbrace{\sum_i\tfrac12 m_i v_i'^2}_{\text{(B)}}
> +\underbrace{\vec v_G\cdot\sum_i m_i\vec v_i'}_{\text{(C)}}.$$
> **Paso 4 — Evaluar cada pieza.** En **(A)**, $\vec v_G$ es común a todas, así que
> $\sum_i\tfrac12 m_i v_G^2=\tfrac12\big(\sum_i m_i\big)v_G^2=\tfrac12 m v_G^2$. La pieza **(B)** es por
> definición $T_{rel}$.
> **Paso 5 — El término cruzado (C) se anula.** Las posiciones relativas al CM cumplen
> $\sum_i m_i\vec r_i'=\sum_i m_i(\vec r_i-\vec r_G)=m\vec r_G-m\vec r_G=\vec0$. Derivando esta identidad,
> $$\sum_i m_i\vec v_i'=\frac{d}{dt}\sum_i m_i\vec r_i'=\frac{d}{dt}\vec0=\vec0,$$
> es decir, **el momento total medido desde el CM es nulo**. Por tanto (C)$=\vec v_G\cdot\vec0=0$.
> **Paso 6 — Conclusión.** Reuniendo (A)+(B)+(C):
> $$T=\tfrac12 m v_G^2+\tfrac12\sum_i m_i v_i'^2=\tfrac12 m v_G^2+T_{rel}.\qquad\blacksquare$$

> [!proposicion] El CM se mueve como un punto material
> El centro de masa se mueve **como si** toda la masa $m$ y **toda** la fuerza externa estuvieran
> concentradas en él: obedece $\sum\vec F_{ext}=m\vec a_G$, idéntica a la segunda ley de una sola
> partícula. Por eso un cuerpo extenso se analiza **primero por su CM** (traslación, como punto material)
> y **luego por su rotación** alrededor de él (momento angular). Esta separación traslación + rotación es
> la estrategia que estructura todo el estudio del [[4 Cuerpo Rigido/index| cuerpo rígido]].

> [!warning]
> - Las fuerzas internas se cancelan para el **movimiento del CM** y para el **momento** (lineal y
>   angular, si son centrales), pero **NO para la energía**. Una explosión o un muelle interno **aumenta**
>   $T_{rel}$ aunque $\vec P=m\vec v_G$ no cambie: la energía cinética total **no se conserva** aunque el
>   momento lineal sí.
> - La cancelación del momento angular interno exige que las fuerzas internas sean **centrales** (a lo
>   largo de la recta que une las partículas). Es la hipótesis habitual (gravitación, fuerzas elásticas,
>   contactos), pero conviene tenerla presente.
> - $\vec H_O$ y $\sum\vec M_{O,ext}$ deben calcularse respecto al **mismo punto $O$**, y este debe ser
>   **fijo** en un marco inercial (o ser el propio CM) para que valga $d\vec H_O/dt=\sum\vec M_{O,ext}$.

## Resumen

> [!resumen]
> | Concepto | Definición / ecuación |
> |:---|:---|
> | Centro de masa | $\vec r_G=\dfrac1m\sum_i m_i\vec r_i$, con $m=\sum_i m_i$ |
> | Momento lineal total | $\vec P=\sum_i m_i\vec v_i=m\vec v_G$ |
> | Movimiento del CM | $\sum\vec F_{ext}=m\,\vec a_G$ |
> | Momento angular | $\dfrac{d\vec H_O}{dt}=\sum\vec M_{O,ext}$, con $\vec H_O=\sum_i\vec r_i\times m_i\vec v_i$ |
> | König (energía) | $T=\tfrac12 m v_G^2+T_{rel}$, con $T_{rel}=\tfrac12\sum_i m_i v_i'^2$ |
> | Identidad del CM | $\sum_i m_i\vec r_i'=\vec0$, $\;\sum_i m_i\vec v_i'=\vec0$ |

> [!corolario]
> Las tres leyes del punto material **sobreviven** al pasar a $N$ partículas, con el CM como
> representante: $\sum\vec F_{ext}=m\vec a_G$ generaliza $\sum\vec F=m\vec a$; $d\vec H_O/dt=\sum\vec M_{ext}$
> generaliza el momento angular de [[Impulso y Momento]]; y König desglosa la energía de
> [[Trabajo y Energia]] en **traslación + rotación interna**. Si $\sum\vec F_{ext}=\vec0$, el momento
> total $\vec P$ **se conserva** y el CM va en línea recta a velocidad constante; si $\sum\vec M_{O,ext}=\vec0$,
> se conserva $\vec H_O$. Estos tres resultados son la base directa de la dinámica del
> [[4 Cuerpo Rigido/index| cuerpo rígido]].

> [!referencia]
> Taylor, *Classical Mechanics*, cap. 3 (momento, CM, sistemas de partículas). Generaliza
> [[Impulso y Momento]] y la cinética de [[Cinetica de la Particula]]; la energía remite a
> [[Trabajo y Energia]]. Continúa en [[4 Cuerpo Rigido/index]]. Capítulo: [[1 Particula/index]].
