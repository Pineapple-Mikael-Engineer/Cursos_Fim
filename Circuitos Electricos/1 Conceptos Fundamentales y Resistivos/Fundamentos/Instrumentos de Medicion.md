---
title: Instrumentos de Medicion
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - medicion
draft: false
aliases:
  - instrumentos de medicion
  - amperimetro voltimetro vatimetro
  - measuring instruments
---

# Instrumentos de Medición: Amperímetro, Voltímetro y Vatímetro

> [!definicion]
> - El **amperímetro** mide corriente y se conecta **en serie** con la rama; su resistencia interna
>   debe ser **baja** (ideal $0\ \Omega$) para no estorbar al paso de la corriente.
> - El **voltímetro** mide tensión y se conecta **en paralelo** con el elemento; su resistencia
>   interna debe ser **alta** (ideal $\infty$) para no derivar corriente.
> - El **vatímetro** mide potencia; combina una **bobina amperimétrica en serie** y una **bobina
>   voltimétrica en paralelo**, y entrega $P=VI\cos\varphi$.

---

> [!info]
> Sexta nota de [[Fundamentos/index| Fundamentos]] del
> [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Permite **medir** las
> [[Variables del Circuito| variables del circuito]] y verificar la
> [[Resistencia y Ley de Ohm| ley de Ohm]]; respeta el [[Convenio de Signos| convenio de signos]] al
> conectar el vatímetro (bornes homólogos $\pm$).

---

## Ejemplo

> [!ejemplo] Medir $v$ e $i$ de una resistencia y hallar $R$ por Ohm
> Se quiere conocer la resistencia $R$ de un elemento alimentado por una fuente. Se intercala un
> **amperímetro en serie** para leer la corriente y se conecta un **voltímetro en paralelo** con la
> resistencia para leer su tensión:
>
> ![[instrumentos_conexion.svg|460]]
> Amperímetro en serie con la rama; voltímetro en paralelo con el elemento.
>
> El amperímetro indica $I=2\ \text{A}$ y el voltímetro $V=10\ \text{V}$. Por la
> [[Resistencia y Ley de Ohm| ley de Ohm]],
> $$R=\frac{V}{I}=\frac{10\ \text{V}}{2\ \text{A}}=5\ \Omega.$$
> La potencia disipada, de paso, es $P=VI=10\cdot 2=20\ \text{W}$.
>
> > [!solucion]
> > $R=5\ \Omega$ (y $P=20\ \text{W}$). Esta técnica voltio-amperimétrica es la medida indirecta de
> > resistencia más básica.

---

## En qué consiste

> [!teoria] Por qué cada instrumento se conecta así
> Un **amperímetro** debe dejar pasar la corriente que pretende medir; por eso se pone **en serie** y
> ha de tener resistencia interna mínima: si fuera grande, añadiría una caída de tensión y reduciría
> la propia corriente que mide. El **amperímetro ideal** es un cortocircuito, $0\ \Omega$.
>
> Un **voltímetro** debe medir la diferencia de potencial **sin robar corriente** a la rama; por eso
> se pone **en paralelo** con el elemento y ha de tener resistencia interna muy alta: si fuera baja,
> desviaría parte de la corriente y alteraría el reparto del circuito. El **voltímetro ideal** es un
> circuito abierto, $\infty$.

> [!algoritmo] Cómo conectar cada instrumento
> **Paso 1 — Amperímetro.** Abre la rama por donde quieres medir la corriente e intercala el
> amperímetro **en serie**, respetando la polaridad ($+$ del aparato hacia donde entra la corriente).
> **Paso 2 — Voltímetro.** Sin abrir nada, conecta el voltímetro **en paralelo** entre los dos bornes
> del elemento cuya tensión quieres leer.
> **Paso 3 — Vatímetro.** Pasa la **bobina amperimétrica en serie** con la carga y conecta la
> **bobina voltimétrica en paralelo** con ella; alinea los **bornes homólogos** ($\pm$) para que el
> signo de $P$ sea correcto. La lectura es $P=VI\cos\varphi$.

> [!proposicion] Vatímetro y factor de potencia
> El vatímetro no multiplica simplemente las dos lecturas: mide la **potencia activa**
> $$P=VI\cos\varphi\quad[\text{W}],$$
> donde $\varphi$ es el desfase entre tensión y corriente y $\cos\varphi$ el factor de potencia. En
> corriente continua o en cargas puramente resistivas $\varphi=0$ y $\cos\varphi=1$, de modo que
> $P=VI$, como en el ejemplo.

> [!warning] Efecto de carga del instrumento real
> Ningún instrumento es ideal. Un amperímetro real tiene una pequeña $R_A>0$ que introduce una caída;
> un voltímetro real tiene una $R_V$ finita que deriva algo de corriente. Esta perturbación es el
> **efecto de carga**: la medida modifica ligeramente la magnitud medida. Es despreciable cuando
> $R_A\ll R$ (rama) y $R_V\gg R$ (elemento); si no, hay que corregir. **Nunca** conectes un
> amperímetro en paralelo con una fuente: su baja resistencia provocaría un cortocircuito.

---

## Resumen

> [!resumen] Conexión y resistencia interna
> | Instrumento | Mide | Conexión | Resistencia interna | Ideal | Lectura |
> |:---|:---|:---|:---|:---|:---|
> | Amperímetro | corriente $I$ | **serie** | baja | $0\ \Omega$ | $I$ |
> | Voltímetro | tensión $V$ | **paralelo** | alta | $\infty$ | $V$ |
> | Vatímetro | potencia $P$ | serie $+$ paralelo | mixta | — | $P=VI\cos\varphi$ |

> [!corolario]
> Amperímetro en serie y resistencia baja; voltímetro en paralelo y resistencia alta. Midiendo $V$ e
> $I$ a la vez se obtiene cualquier resistencia por Ohm, $R=V/I$ (método voltio-amperimétrico).

> [!referencia]
> Fraile Mora, cap. 1, §1.7 (medidas eléctricas). Relacionadas: [[Resistencia y Ley de Ohm]] y
> [[Convenio de Signos]].
