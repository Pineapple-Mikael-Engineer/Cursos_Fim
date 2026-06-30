---
title: Diagramas Fasoriales
order: 2
tags:
  - circuitos-electricos
  - teoria
  - fasores
draft: false
aliases:
  - Diagramas Fasoriales
  - Diagrama Fasorial
  - Phasor Diagrams
  - Phasor Diagram
---

# Diagramas Fasoriales

> [!definicion]
> Un **diagrama fasorial** representa las tensiones y corrientes de un circuito como **vectores** en el plano complejo. Como los fasores son vectores, las leyes de Kirchhoff se vuelven **sumas vectoriales**: la **LKV** es la suma vectorial de las tensiones de una malla y la **LKC**, la de las corrientes de un nodo. El diagrama muestra de un vistazo **módulos** y **desfases**, revelando quién adelanta y quién atrasa.

> [!info] Ubicación
> Esta nota es el apoyo gráfico del [[Analisis Fasorial/index| análisis fasorial]] ([[5 Circuitos AC Sinusoidal y Fasores/index| capítulo 5]]). Complementa los [[Metodos en Regimen Fasorial| métodos en régimen fasorial]] y se apoya en la [[Fasores]]. Da soporte visual al cálculo de la [[Impedancia Compleja]].
>
> Referencia: Fraile Mora, *Circuitos Eléctricos*, cap. 2 §2.8.

---

## Ejemplo

> [!ejemplo] RL serie, corriente como referencia
> Retomamos el circuito **RL serie** del ejemplo de los métodos en régimen fasorial. Como es un circuito **serie**, conviene tomar la **corriente como referencia** (es la magnitud común a todos los elementos):
>
> $$\overline{I}=20\angle0^\circ\ \text{A} \quad (\text{referencia})$$
>
> Sobre la resistencia la tensión está **en fase** con la corriente, y sobre la inductancia **adelanta** $90^\circ$:
>
> $$\overline{V}_R=60\angle0^\circ\ \text{V} \qquad \overline{V}_L=80\angle90^\circ\ \text{V}$$
>
> La tensión total aplicada es la **suma vectorial** de ambas (LKV):
>
> ![[diagrama_fasorial.svg|470]]
>
> *Tomando $\overline{I}$ como referencia: $\overline{V}_R$ en fase, $\overline{V}_L$ a $90^\circ$, y la tensión total $\overline{V}=\overline{V}_R+\overline{V}_L$ es la suma vectorial (la hipotenusa).*
>
> El cálculo de la suma vectorial es:
>
> $$\overline{V}=\overline{V}_R+\overline{V}_L=60+j80=100\angle53^\circ\ \text{V}$$
>
> El ángulo $53^\circ$ es el **desfase de la tensión respecto a la corriente**: positivo, propio de una **carga inductiva**.
>
> > [!solucion]
> > La tensión total es $\overline{V}=100\angle53^\circ\ \text{V}$, y **adelanta** $53^\circ$ a la corriente $\overline{I}$.
> >
> > Lo esencial: el módulo del resultante **NO es la suma aritmética** ($60+80=140$), sino la **vectorial**:
> >
> > $$|\overline{V}|=\sqrt{60^2+80^2}=100\ \text{V}\neq 140\ \text{V}$$
> >
> > El triángulo $\overline{V}_R$–$\overline{V}_L$–$\overline{V}$ es un **triángulo de tensiones**: $\overline{V}_R$ es el cateto horizontal, $\overline{V}_L$ el vertical y $\overline{V}$ la hipotenusa, con $\tan\varphi=\dfrac{V_L}{V_R}=\dfrac{80}{60}$, de donde $\varphi=53^\circ$.

---

## En qué consiste

> [!teoria] La idea geométrica
> Cada fasor es un vector con módulo (su valor eficaz o de pico) y ángulo (su fase). Al dibujarlos todos en el mismo plano complejo, las leyes de Kirchhoff dejan de ser ecuaciones algebraicas y pasan a ser **operaciones geométricas con vectores**:
>
> - La **LKV** (suma de tensiones en una malla) cierra un **polígono de vectores**.
> - La **LKC** (suma de corrientes en un nodo) cierra otro **polígono de vectores**.
>
> El paso clave es elegir bien la **referencia**, es decir, el fasor al que se le asigna **fase $0^\circ$** (queda sobre el eje real). Todos los demás se dibujan con su **fase relativa** a ese:
>
> - En circuitos **serie** conviene la **corriente** como referencia, porque es **común** a todos los elementos.
> - En circuitos **paralelo** conviene la **tensión**, porque es la **común** a todas las ramas.
>
> Una vez dibujados los fasores, el diagrama da intuición inmediata de quién **adelanta** y quién **atrasa**, y permite incluso resolver el circuito **gráficamente** midiendo el vector resultante.

> [!algoritmo] Construcción de un diagrama fasorial
> 1. **Elegir el fasor de referencia** y colocarlo sobre el eje real (fase $0^\circ$): la **corriente** en circuitos serie, la **tensión** en circuitos paralelo.
> 2. **Dibujar cada fasor** con su **módulo** y su **fase relativa** a la referencia (los inductivos adelantan, los capacitivos atrasan, los resistivos van en fase).
> 3. **Sumar vectorialmente** los fasores que exige la ley correspondiente (LKV en mallas, LKC en nodos), encadenándolos de punta a cola y **cerrando el polígono**.
> 4. **Leer el módulo y el ángulo** del fasor resultante (gráficamente o con $|\cdot|=\sqrt{a^2+b^2}$ y $\varphi=\arctan(b/a)$).

> [!warning] Errores frecuentes
> - Los fasores se suman como **vectores**, nunca aritméticamente: $\lvert\overline{V}_R+\overline{V}_L\rvert\neq V_R+V_L$ salvo que estén exactamente **en fase**.
> - Todos los fasores de un mismo diagrama deben estar a la **misma frecuencia**; si hay varias frecuencias, no se pueden mezclar en un solo diagrama.
> - La **referencia** es solo una elección de **comodidad**: rota el diagrama entero, pero **no cambia** los módulos, los desfases relativos ni el resultado físico.

---

## Resumen

> [!resumen]
> | Concepto | Circuito serie | Circuito paralelo |
> |---|---|---|
> | Fasor de **referencia** | la **corriente** $\overline{I}$ (común) | la **tensión** $\overline{V}$ (común) |
> | Ley de Kirchhoff aplicada | **LKV**: $\sum \overline{V}=0$ | **LKC**: $\sum \overline{I}=0$ |
> | Operación geométrica | suma **vectorial** de tensiones | suma **vectorial** de corrientes |
> | Resultado | polígono de tensiones cerrado | polígono de corrientes cerrado |
> | Módulo del resultante | $\sqrt{a^2+b^2}$ (no la suma aritmética) | $\sqrt{a^2+b^2}$ (no la suma aritmética) |

> [!corolario]
> El diagrama fasorial es la **traducción geométrica** del álgebra compleja del régimen permanente: convierte la LKV y la LKC en **sumas vectoriales** y hace visibles los desfases. En el RL serie del ejemplo, $\overline{V}_R$ y $\overline{V}_L$ forman un triángulo rectángulo cuya hipotenusa $\overline{V}=100\angle53^\circ\ \text{V}$ es la tensión total, prueba de que **la suma de módulos no es el módulo de la suma**.

> [!referencia]
> - Fraile Mora, J. *Circuitos Eléctricos*, cap. 2 §2.8 (diagramas fasoriales).
> - Notas relacionadas: [[Metodos en Regimen Fasorial]], [[Fasores]], [[Impedancia Compleja]], [[Analisis Fasorial/index]].
