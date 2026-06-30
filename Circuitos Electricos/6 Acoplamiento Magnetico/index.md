---
title: Acoplamiento Magnético
tags:
  - circuitos-electricos
  - teoria
  - acoplamiento-magnetico
  - index
draft: false
aliases:
  - acoplamiento magnético
  - circuitos acoplados magnéticamente
  - inductancia mutua y transformador
  - inducción magnética
---

# Acoplamiento Magnético

> [!definicion]
> Dos bobinas cercanas están **acopladas magnéticamente** cuando el flujo creado por una **enlaza** a
> la otra: un cambio de corriente en la primera **induce** tensión en la segunda. Ese efecto se
> describe con la **inductancia mutua** $M$, que se suma a las **autoinductancias** $L$. Es el
> principio del **transformador**, la máquina que vertebra todo el sistema eléctrico.

> [!info]
> Sexto bloque del curso (sílabo ML 140, semana 12; Fraile Mora, cap. 1, §1.19). Extiende el
> [[Inductor]] del capítulo 3 a **pares** de bobinas, y se analiza en régimen sinusoidal con las
> [[Impedancia y Admitancia/index| impedancias]] del capítulo 5. Es la base de las máquinas
> eléctricas.

---

## Todo nace de la ley de Faraday

> [!teoria] Del flujo propio al flujo compartido
> Una corriente $i$ crea un **flujo magnético** $\phi$; multiplicado por las $N$ espiras que enlaza da
> el **flujo concatenado** $\lambda=N\phi$. La **ley de Faraday** ($v=d\lambda/dt$) da las dos
> inducciones:
> - Si el flujo enlaza a la **propia** bobina, $\lambda=L\,i$ y $v=L\,di/dt$: es la **autoinducción**
>   $L$. → [[Autoinduccion]].
> - Si una **fracción** atraviesa una **segunda** bobina, su variación induce $v_2=M\,di_1/dt$: es la
>   **inducción mutua** $M$, el canal por el que dos bobinas se comunican **sin tocarse**.
>   → [[Inductancia Mutua]].
>
> Con ambas corrientes presentes, cada tensión suma su autoinducción y la mutua de la vecina: las dos
> bobinas quedan descritas por **ecuaciones acopladas**.

> [!teoria] Simetría, cota y signo
> Tres hechos sobre $M$ no son casualidad:
> - **Simetría** ($M_{12}=M_{21}=M$): el acoplamiento "se ve igual" desde cualquiera de las dos bobinas.
> - **Cota** ($M\le\sqrt{L_1L_2}$): no puede compartirse más flujo del que cada bobina enlaza consigo
>   misma. El cociente $k=M/\sqrt{L_1L_2}\in[0,1]$ —el **coeficiente de acoplamiento**— mide qué
>   fracción se comparte (tratado en [[Inductancia Mutua]]). Ambas se deducen exigiendo
>   energía $\ge0$ → [[Energia en Bobinas Acopladas]].
> - **Signo**: el término mutuo $\pm M$ lo fija la geometría del bobinado, codificada con un **punto**
>   en cada bobina → [[Regla de los Puntos]]. Para **más de dos** bobinas, todo se ordena en una
>   **matriz de inductancias** → [[Acoplamiento Multiple]].

> [!teoria] El transformador
> Sobre esta física se construye el **transformador**: con núcleo de aire
> ([[Transformador con Nucleo de Aire]], $k<1$, **impedancia reflejada**) o en el límite ideal
> ([[Transformador Ideal]], $k=1$, **relación de transformación**). En alterna, el par acoplado se
> reduce a ecuaciones algebraicas con el término $j\omega M$ → [[Acoplamiento Magnetico Fasorial]].

## Mapa del capítulo

> [!info] Las notas
> | Nota | Contenido |
> |:---|:---|
> | [[Autoinduccion]] | $L=N\phi/i$; base de una sola bobina (delega en [[Inductor]]) |
> | [[Inductancia Mutua]] | ecuaciones del par $v_1,v_2$; coeficiente de acoplamiento $k$ |
> | [[Regla de los Puntos]] | el signo $\pm M$ del término mutuo |
> | [[Energia en Bobinas Acopladas]] | $W=\tfrac12 L_1i_1^2+\tfrac12 L_2i_2^2\pm M i_1 i_2$; cota de $M$ |
> | [[Acoplamiento Multiple]] | varias bobinas; la matriz $[L]$ |
> | [[Acoplamiento Magnetico Fasorial]] | el par acoplado en régimen sinusoidal ($j\omega M$) |
> | [[Transformador con Nucleo de Aire]] | transformador real; impedancia reflejada |
> | [[Transformador Ideal]] | relación de transformación; reflejo de impedancias |
> | [[Circuito Equivalente con Acoplo Conductivo]] | el equivalente en T (sin acoplo) |

> [!corolario]
> El acoplamiento magnético añade un canal nuevo —el flujo compartido— por el que los circuitos
> interactúan sin tocarse. Dominar $M$, la regla de los puntos y el transformador es entender cómo se
> transmite y transforma la energía eléctrica.

> [!referencia]
> Fraile Mora, cap. 1, §1.19. Viene de [[5 Circuitos AC Sinusoidal y Fasores/index| Circuitos AC sinusoidal y fasores]]; continúa en [[7 Circuitos Trifasicos/index| Circuitos trifásicos]].
