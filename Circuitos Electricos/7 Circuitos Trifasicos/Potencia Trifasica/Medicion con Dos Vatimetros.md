---
title: Medición con Dos Vatímetros
order: 2
tags:
  - circuitos-electricos
  - teoria
  - trifasico
draft: false
aliases:
  - medición con dos vatímetros
  - método de los dos vatímetros
  - teorema de Blondel
  - two-wattmeter method
---

# Medición con Dos Vatímetros

> [!definicion]
> El **método de los dos vatímetros** mide la potencia de un sistema trifásico de **tres hilos** con solo **dos** vatímetros (teorema de **Blondel**: bastan $n-1$ para $n$ conductores). Sus bobinas de corriente van en dos líneas ($a$ y $c$) y las de tensión se refieren a la tercera ($b$). La potencia activa total es la **suma** de las dos lecturas:
> $$P=W_1+W_2,$$
> y la reactiva, la **diferencia** escalada: $Q=\sqrt3\,(W_2-W_1)$.

> [!info]
> La forma práctica de medir la [[Potencia en Sistemas Balanceados| potencia trifásica]] del [[7 Circuitos Trifasicos/index| capítulo 7]]; vale para carga equilibrada **o no**, en Y o Δ, a 3 hilos. Fraile Mora, cap. 3, §3.8.

---

## Ejemplo

> [!ejemplo]
> **Lecturas de los dos vatímetros.**
>
> La carga equilibrada anterior ($V_L=400\ \text{V}$, $I_L=23\ \text{A}$, $\varphi=40^\circ$ inductivo, $P\approx12{,}2\ \text{kW}$). Hallar las dos lecturas y comprobar la suma.
>
> ![[dos_vatimetros.svg|600]]
>
> *$W_1$ en la línea $a$, $W_2$ en la $c$, ambas bobinas de tensión referidas a $b$. Cada vatímetro tiene **dos bobinas**: la de **intensidad** (en serie con la línea, con su borne $\pm$ hacia la fuente, por donde entra la corriente) y la de **tensión** (en paralelo, con su $\pm$ en la misma línea). Los bornes homólogos $\pm$ fijan el signo de la lectura.*
>
> **Paso 1 — Las lecturas** (con la fórmula $W_{1,2}=V_L I_L\cos(30^\circ\pm\varphi)$):
> $$W_1=V_L I_L\cos(30^\circ+\varphi)=400\cdot23\cos70^\circ\approx3{,}15\ \text{kW},$$
> $$W_2=V_L I_L\cos(30^\circ-\varphi)=400\cdot23\cos10^\circ\approx9{,}06\ \text{kW}.$$
>
> **Paso 2 — Suma y diferencia.**
> $$W_1+W_2\approx12{,}2\ \text{kW}=P,\qquad \sqrt3\,(W_2-W_1)\approx\sqrt3\cdot5{,}9\approx10{,}2\ \text{kVAr}=Q.$$
>
> > [!solucion]
> > $W_1\approx3{,}15\ \text{kW}$, $W_2\approx9{,}06\ \text{kW}$; su suma da $P\approx12{,}2\ \text{kW}$ y, de la diferencia, $Q\approx10{,}2\ \text{kVAr}$. Dos lecturas bastan para todo.

---

## En qué consiste

> [!teorema] Las lecturas y lo que se obtiene de ellas
> Para una carga equilibrada, las dos lecturas son
> $$W_1=V_L I_L\cos(30^\circ+\varphi),\qquad W_2=V_L I_L\cos(30^\circ-\varphi).$$
> De ellas se extrae **toda** la información:
> $$P=W_1+W_2,\qquad Q=\sqrt3\,(W_2-W_1),\qquad \tan\varphi=\sqrt3\,\frac{W_2-W_1}{W_1+W_2}.$$
> El método da, con dos instrumentos, la potencia activa, la reactiva y el factor de potencia.

> [!teoria] Cómo se conecta el vatímetro: las dos bobinas y sus bornes $\pm$
> Cada vatímetro mide el producto $V I\cos\theta$ con **dos bobinas** y por eso tiene **cuatro bornes**, dos por bobina (ver [[Instrumentos de Medicion]]). La **bobina de intensidad** (de pocas espiras gruesas, baja resistencia) va **en serie** con la línea: por ella circula la corriente de línea. La **bobina de tensión** (de muchas espiras finas, alta resistencia) va **en paralelo**, entre esa línea y la de referencia $b$: a ella se aplica la tensión. Cada bobina marca uno de sus bornes con $\pm$ (el **borne homólogo**). La regla de conexión es: la **corriente entra por el $\pm$** de la bobina de intensidad, y el $\pm$ de la bobina de tensión se conecta a la **misma línea** que el $\pm$ de intensidad. Con esa convención, la aguja deflecta en sentido **positivo** cuando la potencia fluye **de la fuente a la carga**; si se invierte uno de los dos bornes, la lectura cambia de signo. Por eso en el método de los dos vatímetros el **orden de los bornes importa**: una conexión mal orientada falsea el signo de $W_1$ o $W_2$.

> [!proposicion] Una lectura puede ser negativa
> Cuando el factor de potencia es bajo ($\varphi>60^\circ$), el ángulo $30^\circ+\varphi$ supera $90^\circ$ y **$W_1$ se vuelve negativo**: la corriente y la tensión que ve ese vatímetro están desfasadas más de $90^\circ$, así que con los bornes $\pm$ bien conectados la aguja intentaría irse **por debajo de cero**. En la práctica se **invierte la conexión** de una de sus bobinas para leer un valor positivo y luego se **resta** esa lectura. Si $\varphi=60^\circ$ ($\cos\varphi=0{,}5$), ese vatímetro marca **cero**. La suma $W_1+W_2$, en cambio, siempre da la $P$ correcta.

> [!algoritmo] Aplicar el método
> **Paso 1 — Conectar.** Bobinas de corriente **en serie** en dos líneas ($a$ y $c$), con el borne $\pm$ hacia la fuente; bobinas de tensión **en paralelo** a la tercera ($b$), con su $\pm$ en la línea de su propio vatímetro. **Paso 2 — Leer** $W_1$ y $W_2$ (anotar signos). **Paso 3 — Potencia activa:** $P=W_1+W_2$. **Paso 4 — Reactiva y FP:** $Q=\sqrt3(W_2-W_1)$ y $\tan\varphi=\sqrt3(W_2-W_1)/(W_1+W_2)$.

> [!warning]
> Solo sirve para sistemas de **tres hilos** (sin neutro, o con neutro sin corriente). El orden $W_1, W_2$ y el signo importan: una lectura negativa **resta**. La fórmula $Q=\sqrt3(W_2-W_1)$ supone carga **equilibrada**.

## Resumen

> [!resumen]
> | Magnitud | A partir de las lecturas |
> |:---|:---|
> | Activa | $P=W_1+W_2$ |
> | Reactiva | $Q=\sqrt3\,(W_2-W_1)$ |
> | Factor de potencia | $\tan\varphi=\sqrt3\,(W_2-W_1)/(W_1+W_2)$ |
> | $W_1<0$ | si $\varphi>60^\circ$ (FP bajo) |

> [!corolario]
> Dos vatímetros —no tres— bastan para medir la potencia de un sistema trifásico a tres hilos, y de su suma y diferencia salen $P$, $Q$ y el factor de potencia. Es la consecuencia práctica del teorema de Blondel.

> [!referencia]
> Fraile Mora, cap. 3, §3.8. Potencia: [[Potencia en Sistemas Balanceados]]. Factor de potencia: [[Factor de Potencia]] y [[Correccion FP Trifasico]]. El instrumento y sus bobinas: [[Instrumentos de Medicion]].
