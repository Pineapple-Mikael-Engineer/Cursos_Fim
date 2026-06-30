---
title: Convenio de Signos
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - convenio-signos
draft: false
aliases:
  - convenio de signos
  - convenio pasivo y activo
  - sign convention
---

# Convenio de Signos $p=vi$

> [!definicion]
> El **convenio de signos** fija cómo se orientan la flecha de la corriente y la polaridad de la tensión sobre un elemento, y con ello el significado del signo de la potencia $p=vi$.
> - **Convenio pasivo (receptor):** la corriente **entra por el borne $+$**. Entonces $p=vi\ge 0$ significa que el elemento **absorbe** potencia.
> - **Convenio activo (generador):** la corriente **sale por el borne $+$**. Entonces $p=vi\ge 0$ significa que el elemento **entrega** potencia. Cambiar de convenio cambia el signo de $p$, pero **no** la física: la potencia realmente intercambiada es la misma.

---

> [!info]
> Segunda nota de [[Fundamentos/index| Fundamentos]] del [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Usa las [[Variables del Circuito| variables $i$ y $v$]] y da sentido al signo de la [[Potencia y Energia| potencia]]. Es la base del [[Balance de Potencias| balance de potencias]] de toda la red.

---

## Ejemplo

> [!ejemplo] Un mismo elemento: absorbe o entrega según la orientación
> Un elemento de dos terminales tiene una tensión $v=10\ \text{V}$ entre bornes y lo recorre una corriente $i=2\ \text{A}$. La potencia en juego es
> $$\lvert p\rvert=v\,i=10\ \text{V}\cdot 2\ \text{A}=20\ \text{W}.$$
> Lo que decide si esos $20\ \text{W}$ se absorben o se entregan es **cómo entra la corriente respecto al $+$**:
>
> ![[convenio_signos.svg|420]]
> Izq.: convenio receptor (la corriente entra por $+$, absorbe). Der.: convenio generador (sale por $+$, entrega).
>
> > [!solucion]
> > - **Si la corriente entra por el borne $+$** (convenio receptor): $p=+20\ \text{W}>0$, el elemento **absorbe** $20\ \text{W}$ (p. ej. una resistencia que se calienta).
> > - **Si la corriente sale por el borne $+$** (convenio generador): tomando $p=vi$ con la corriente medida hacia fuera, $p=+20\ \text{W}$ se interpreta como potencia **entregada** $20\ \text{W}$ (p. ej. una batería alimentando el circuito).
> >
> > Si se usa el **convenio pasivo** en ambos casos, la batería daría $p=-20\ \text{W}$: el signo negativo es precisamente la señal de que **entrega** en vez de absorber.

---

## En qué consiste

> [!teoria] Por qué hace falta un convenio
> La potencia $p=vi$ es un producto de dos cantidades con signo, así que su signo depende de cómo se hayan referenciado $v$ e $i$. Para que "absorbe" y "entrega" signifiquen siempre lo mismo, se estandariza la pareja flecha–polaridad. El convenio universal de análisis es el **pasivo**: se dibuja la corriente **entrando por el terminal marcado $+$**. Con esa elección, el signo de $p$ tiene una lectura física directa y única.

> [!regla] Lectura del signo de $p$ (convenio pasivo)
> Con la corriente entrando por el borne $+$:
> - $p>0$ → el elemento **absorbe** (consume) potencia. Es lo normal en resistencias, y en una fuente que se está cargando.
> - $p<0$ → el elemento **entrega** (suministra) potencia. Es lo normal en una fuente que alimenta el circuito.
>
> El convenio **activo** es el mismo cálculo con la corriente saliendo por $+$; equivale a cambiar el signo, por lo que $p>0$ pasa a leerse como "entrega". Se reserva para las fuentes, donde es más natural hablar de potencia entregada.

> [!proposicion] Conservación de la energía
> En cualquier circuito, con todos los elementos en convenio pasivo, la suma de potencias es nula:
> $$\sum_k p_k=0.$$
> Las fuentes dan potencias negativas (entregan) y los elementos pasivos positivas (absorben); en conjunto, lo entregado iguala a lo absorbido. Este es el contenido del balance de potencias.

> [!warning] No mezclar convenios en un mismo cálculo
> Elige un convenio por elemento y sé coherente. Si etiquetas una resistencia en pasivo y obtienes $p<0$, no es que "entregue": es que la corriente real va al revés que tu flecha. El signo lo dice todo siempre que el convenio esté declarado.

---

## Resumen

> [!resumen] Convenios y signo de la potencia
> | Convenio | Corriente respecto a $+$ | $p=vi>0$ significa | Uso típico |
> |:---|:---|:---|:---|
> | Pasivo (receptor) | **entra** por $+$ | el elemento **absorbe** | $R$, $L$, $C$, cargas |
> | Activo (generador) | **sale** por $+$ | el elemento **entrega** | fuentes / generadores |

> [!corolario]
> Un resultado de potencia **sin convenio declarado no tiene significado**. Declarado el convenio (por defecto, pasivo), el signo de $p$ basta para saber si el elemento consume o suministra energía, y el balance $\sum p_k=0$ debe cumplirse siempre.

> [!referencia]
> Fraile Mora, cap. 1, §1.4. Relacionadas: [[Variables del Circuito]], [[Potencia y Energia]] y [[Balance de Potencias]].
