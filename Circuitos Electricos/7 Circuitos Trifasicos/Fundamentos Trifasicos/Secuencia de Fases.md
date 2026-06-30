---
title: Secuencia de Fases
tags:
  - circuitos-electricos
  - teoria
  - trifasico
draft: false
aliases:
  - secuencia de fases
  - orden de fases
  - phase sequence
  - phase rotation
---

# Secuencia de Fases

> [!definicion]
> La **secuencia de fases** es el **orden** en que las tres tensiones de un sistema trifásico alcanzan su valor máximo. Hay dos posibilidades. La **secuencia directa** (positiva) sigue el orden $a\to b\to c$, con
> $$\overline{V}_a=V\angle0^\circ,\quad \overline{V}_b=V\angle{-}120^\circ,\quad \overline{V}_c=V\angle{+}120^\circ;$$
> la **secuencia inversa** (negativa) sigue el orden $a\to c\to b$. La secuencia determina el **sentido de giro** de los motores trifásicos.

> [!info]
> Es una propiedad del orden de las tensiones de [[Generacion de Tensiones Trifasicas| generación trifásica]], dentro de [[Fundamentos Trifasicos/index| Fundamentos]] ([[7 Circuitos Trifasicos/index| capítulo 7]]). Afecta a las conexiones [[Conexion Estrella| en estrella]] y, sobre todo, al sentido de giro de los motores. Fraile Mora, cap. 3, §3.2.

---

## Ejemplo

> [!ejemplo]
> **De directa a inversa.**
>
> Dado un sistema en secuencia directa $abc$, ¿cómo se obtiene la secuencia inversa?
>
> **Paso 1 — Punto de partida.** En directa, los fasores se ordenan $a\to b\to c$:
> $$\overline{V}_a=V\angle0^\circ,\quad \overline{V}_b=V\angle{-}120^\circ,\quad \overline{V}_c=V\angle{+}120^\circ.$$
>
> **Paso 2 — Intercambiar dos fases.** Permutamos dos fases cualesquiera, por ejemplo $b$ y $c$. El nuevo orden de lectura es $a\to c\to b$, es decir, la secuencia $acb$, que es **inversa**.
>
> > [!solucion]
> > Permutar **dos** fases cualesquiera invierte la secuencia. En un motor trifásico, intercambiar dos de sus tres conductores convierte la secuencia $abc$ en $acb$ y, con ella, **invierte el sentido de giro**.

---

## En qué consiste

> [!teoria] Secuencia y campo magnético giratorio
> En **secuencia directa**, los fasores giran en sentido antihorario y pasan por $a,b,c$ en ese orden; en **inversa**, por $a,c,b$. El **campo magnético giratorio** que crea el devanado trifásico de un motor sigue la secuencia de las tensiones que lo alimentan: gira en el mismo sentido en que se suceden las fases. Por eso, **invertir la secuencia invierte el giro** del motor. En la práctica, para cambiar el sentido de un motor trifásico basta **permutar dos de sus tres conductores** de alimentación —no hace falta tocar el interior de la máquina—. La secuencia importa también al conectar **generadores en paralelo**: ambos deben tener la misma secuencia (además de igual tensión y frecuencia) o no podrán acoplarse.

> [!proposicion] Solo hay dos ordenaciones cíclicas
> Las dos secuencias son las **dos únicas** ordenaciones cíclicas distintas de tres fases. Las rotaciones cíclicas no cambian la secuencia:
> $$abc=bca=cab\quad(\text{directa}),\qquad acb=cba=bac\quad(\text{inversa}).$$
> Lo que cuenta es el **orden cíclico**, no cuál de las fases se llame "primera": empezar a contar por $a$, por $b$ o por $c$ describe la misma secuencia.

> [!warning]
> No confundir **secuencia** con **etiquetas**: renombrar las fases (cambiar qué conductor llamamos $a$, $b$ o $c$) **no** cambia la secuencia física del sistema. Y el giro solo se invierte permutando **dos** conductores; permutar los **tres** (una rotación cíclica completa) deja la secuencia **igual** y el motor gira en el mismo sentido.

## Resumen

> [!resumen]
> | Aspecto | Directa (positiva) | Inversa (negativa) |
> |:---|:---|:---|
> | Orden | $abc$ ($a\to b\to c$) | $acb$ ($a\to c\to b$) |
> | Fasores | $V\angle0^\circ,\ V\angle{-}120^\circ,\ V\angle{+}120^\circ$ | $V\angle0^\circ,\ V\angle{+}120^\circ,\ V\angle{-}120^\circ$ |
> | Giro del motor | un sentido | sentido contrario |
> | Cómo invertirla | — | permutar **dos** conductores |
> | Ordenaciones equivalentes | $abc=bca=cab$ | $acb=cba=bac$ |

> [!corolario]
> Toda la diferencia entre las dos secuencias se reduce a permutar dos fases. Esa operación trivial sobre los cables es, físicamente, la que invierte el campo giratorio y con él el sentido de marcha de cualquier motor trifásico.

> [!referencia]
> Fraile Mora, cap. 3, §3.2. Origen de las tensiones: [[Generacion de Tensiones Trifasicas]]. Conexión afectada: [[Conexion Estrella]]. Contexto: [[Fundamentos Trifasicos/index]], [[7 Circuitos Trifasicos/index]].
