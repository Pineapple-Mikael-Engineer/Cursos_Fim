---
title: Inducción Magnética
tags:
  - circuitos-electricos
  - teoria
  - acoplamiento-magnetico
  - index
draft: false
aliases:
  - inducción magnética
  - autoinducción e inducción mutua
---

# Inducción Magnética

> [!definicion]
> La **inducción magnética** entre bobinas tiene dos caras: la **autoinducción** $L$ —el flujo que la
> corriente de una bobina crea sobre **sí misma**— y la **inducción mutua** $M$ —el flujo que esa
> corriente crea sobre **otra** bobina cercana—. Cuánto se comparte lo mide el **coeficiente de
> acoplamiento** $k$, y el **signo** del efecto mutuo lo fija la **regla de los puntos**.

> [!info]
> Primera sección del [[6 Acoplamiento Magnetico/index| capítulo 6]]. Generaliza el [[Inductor]] del
> capítulo 3 a pares de bobinas; es la física que después usa el [[Transformador Ideal| transformador]].
> Fraile Mora, cap. 1, §1.19.

---

## Todo nace de la ley de Faraday

> [!teoria] Del flujo propio al flujo compartido
> Una corriente $i$ crea un **flujo magnético** $\phi$; multiplicado por las $N$ espiras que enlaza da
> el **flujo concatenado** $\lambda=N\phi$. La **ley de Faraday** dice que un flujo concatenado
> variable induce tensión, $v=d\lambda/dt$. De ahí salen las dos inducciones:
>
> - Si ese flujo enlaza a la **propia** bobina, $\lambda=L\,i$ y $v=L\,di/dt$: es la **autoinducción**
>   $L$, la oposición de la bobina a cambiar su propia corriente. → [[Autoinduccion]].
> - Si una **fracción** de ese flujo atraviesa una **segunda** bobina cercana, su variación induce
>   tensión en ella: $v_2=M\,di_1/dt$. Esa constante de proporcionalidad es la **inducción mutua**
>   $M$, el canal por el que dos bobinas se comunican **sin tocarse**. → [[Inductancia Mutua]].
>
> Con ambas corrientes presentes, cada tensión suma su autoinducción y la mutua de la vecina; las dos
> bobinas quedan descritas por **ecuaciones acopladas**.

> [!teoria] Por qué $M$ es simétrica y está acotada
> Dos propiedades de $M$ no son casualidad, sino consecuencia de la **energía** almacenada en el campo:
> - **Simetría**, $M_{12}=M_{21}=M$: el acoplamiento "se ve igual" desde cualquiera de las dos bobinas
>   (lo que la 1 induce en la 2 por unidad de $di/dt$ es lo mismo que la 2 induce en la 1).
> - **Cota**, $M\le\sqrt{L_1L_2}$: no puede compartirse más flujo del que cada bobina enlaza consigo
>   misma. El cociente $k=\dfrac{M}{\sqrt{L_1L_2}}\in[0,1]$ —el **coeficiente de acoplamiento**— mide
>   qué fracción se comparte: $k\to0$ casi independientes, $k\to1$ acoplo perfecto. → [[Coeficiente de Acoplamiento]].
>
> Ambas se demuestran exigiendo que la energía $W=\tfrac12 L_1 i_1^2+\tfrac12 L_2 i_2^2\pm M i_1 i_2$
> sea siempre $\ge0$.

> [!teoria] El signo lo pone la geometría del bobinado
> Las ecuaciones del par llevan un término mutuo $\pm M\,di/dt$, y **el signo importa**: cambia el
> resultado del circuito. Ese signo depende de **cómo está enrollada** cada bobina respecto a la otra,
> algo que el dibujo de los devanados no muestra. Se codifica con un **punto** en cada bobina (la
> **regla de los puntos**): si las corrientes entran por terminales homólogos, el flujo mutuo
> **refuerza** al propio ($+M$); si no, lo **debilita** ($-M$). → [[Regla de los Puntos]]. Para **más
> de dos** bobinas, todo se ordena en una **matriz de inductancias**. → [[Acoplamiento Multiple]].

## Mapa de la sección

> [!info] Qué desarrolla cada hija
> | Nota | Qué profundiza |
> |:---|:---|
> | [[Autoinduccion]] | $L=N\phi/i=N^2/\mathcal{R}$; energía $\tfrac12 Li^2$ |
> | [[Inductancia Mutua]] | las ecuaciones acopladas $v_1,v_2$; ejemplo resuelto |
> | [[Regla de los Puntos]] | cómo asignar el signo $\pm M$ en cada caso |
> | [[Coeficiente de Acoplamiento]] | $k$, su rango y su deducción por energía |
> | [[Acoplamiento Multiple]] | varias bobinas; la matriz $[L]$ |

> [!corolario]
> Toda la inducción se reduce a Faraday aplicado al flujo: si enlaza a la propia bobina, da $L$; si
> enlaza a otra, da $M$. La energía obliga a que $M$ sea simétrica y $\le\sqrt{L_1L_2}$, y la geometría
> del bobinado le pone el signo. Con eso queda descrito cualquier conjunto de bobinas acopladas.

> [!referencia]
> Fraile Mora, cap. 1, §1.19. Siguiente: [[Acoplamiento Magnetico Fasorial]] (en régimen sinusoidal) y
> [[Transformador con Nucleo de Aire]].
