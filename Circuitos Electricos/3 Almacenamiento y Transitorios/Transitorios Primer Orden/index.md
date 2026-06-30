---
title: Transitorios de Primer Orden
order: 2
tags:
  - circuitos-electricos
  - teoria
  - transitorios
  - primer-orden
  - index
draft: false
aliases:
  - transitorios de primer orden
  - circuitos de primer orden
  - respuesta exponencial
---

# Transitorios de Primer Orden

> [!definicion]
> Un circuito de **primer orden** tiene **un solo** elemento almacenador (un $C$ o un $L$) junto con resistencias. Tras una conmutación, su respuesta es una **única exponencial** gobernada por la **constante de tiempo** $\tau$: la variable parte de su valor inicial $x_0$ y se acerca exponencialmente a su valor final $x_\infty$. La fórmula que lo resume todo es
> $$x(t)=x_\infty+(x_0-x_\infty)\,e^{-t/\tau}.$$

> [!info]
> Segunda sección del [[3 Almacenamiento y Transitorios/index| capítulo 3]]. Usa las leyes y la continuidad de [[Capacitor]] e [[Inductor]] y el análisis en [[Circuitos DC en Estado Estable| DC estable]] (para $x_0$ y $x_\infty$). Es el primer encuentro con la dinámica antes de los [[Transitorios Segundo Orden/index| de segundo orden]]. Fraile Mora, cap. 4, §4.4-4.5.

---

## Por qué la respuesta es una exponencial

> [!teoria] Una sola derivada ⇒ una sola exponencial
> Al aplicar Kirchhoff a un circuito con **un** almacenador, la ley del elemento aporta **una** derivada y se obtiene una **ecuación diferencial lineal de primer orden**:
> $$\frac{dx}{dt}+\frac{1}{\tau}\,x = \frac{x_\infty}{\tau}.$$
> Su solución es la suma de dos partes:
> - la **respuesta forzada** $x_\infty$ (el régimen permanente que imponen las fuentes), y
> - la **respuesta natural** $(x_0-x_\infty)e^{-t/\tau}$, una exponencial que **se extingue**.
>
> La exponencial aparece porque es la única función cuya derivada es proporcional a ella misma: es la "forma natural" de relajarse de un circuito de primer orden. La rapidez la fija $\tau$ → [[Constante de Tiempo]]; la receta general, [[Respuesta Completa Primer Orden]].

> [!teoria] RC y RL: los dos circuitos, otra vez duales
> Solo hay dos circuitos de primer orden, y son **duales**:
> - El **RC**: el condensador se carga/descarga a través de la resistencia, con $\tau=RC$. La variable natural es la **tensión** $v_C$ (que no salta). → [[Circuito RC]].
> - El **RL**: el inductor se magnetiza/desmagnetiza a través de la resistencia, con $\tau=L/R$. La variable natural es la **corriente** $i_L$ (que no salta). → [[Circuito RL]].
>
> Ambos siguen exactamente la misma fórmula; cambia solo qué es $\tau$ y cuál es la variable de estado.

> [!info] El método de los tres datos
> Resolver **cualquier** transitorio de primer orden se reduce a hallar tres números y sustituir en $x(t)=x_\infty+(x_0-x_\infty)e^{-t/\tau}$:
> $$x_0=x(0^+)\ \text{(valor inicial)},\quad x_\infty=x(\infty)\ \text{(valor final)},\quad \tau\ \text{(constante de tiempo)}.$$
> No hace falta resolver la ecuación diferencial cada vez. Lo desarrolla [[Respuesta Completa Primer Orden]].

## Mapa de la sección

> [!info] Qué desarrolla cada hija
> | Nota | Contenido |
> |:---|:---|
> | [[Circuito RC]] | carga y descarga del condensador; $v_C(t)$, $\tau=RC$ |
> | [[Circuito RL]] | magnetización del inductor; $i_L(t)$, $\tau=L/R$ |
> | [[Constante de Tiempo]] | qué es $\tau$, el $63\%$, la regla de los $5\tau$ |
> | [[Respuesta Completa Primer Orden]] | el método general $x_\infty+(x_0-x_\infty)e^{-t/\tau}$ |

> [!corolario]
> Un circuito de primer orden no tiene más misterio que una exponencial: a dónde va ($x_\infty$), de dónde parte ($x_0$) y cómo de rápido ($\tau$). Dominar RC y RL —duales— y el método de los tres datos resuelve toda esta sección.

> [!referencia]
> Fraile Mora, cap. 4, §4.4-4.5. Anterior: [[Elementos de Almacenamiento/index| Elementos de almacenamiento]]. Siguiente: [[Transitorios Segundo Orden/index| Transitorios de segundo orden]].
