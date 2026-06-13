---
title: Ventajas del Trifásico
tags:
  - circuitos-electricos
  - teoria
  - trifasico
draft: false
aliases:
  - ventajas del trifásico
  - ventajas del sistema trifásico
  - advantages of three-phase
---

# Ventajas del Trifásico

> [!definicion]
> El sistema **trifásico** se impuso al monofásico por tres ventajas decisivas: (1) entrega una
> **potencia instantánea constante** —no pulsante—, lo que se traduce en un par mecánico uniforme;
> (2) crea un **campo magnético giratorio** que pone en marcha los motores de inducción sin
> dispositivos de arranque; y (3) transporta la misma potencia con **menos material conductor**, es
> decir, con **ahorro de cobre**.

> [!info]
> Esta nota **cierra** los [[Fundamentos Trifasicos/index| fundamentos trifásicos]]
> ([[7 Circuitos Trifasicos/index| capítulo 7]]) explicando el **porqué** del sistema, una vez vistos
> el [[Sistema Polifasico]] y la generación de las tensiones. La primera ventaja se **cuantifica** en
> la [[Potencia en Sistemas Balanceados| potencia trifásica]], que retoma la pulsación monofásica de
> la [[Potencia en Regimen Sinusoidal]]. Fraile Mora, cap. 3, §3.9.

---

## Ejemplo

> [!ejemplo]
> **Cancelación de la potencia pulsante en trifásico.**
>
> En monofásico, con tensión y corriente eficaces $V_{ef}$, $I_{ef}$ y desfase $\varphi$, la potencia
> instantánea vale
> $$p(t)=V_{ef}I_{ef}\cos\varphi-V_{ef}I_{ef}\cos(2\omega t-\varphi),$$
> con un término **constante** y otro que **pulsa** a frecuencia $2\omega$ ([[Potencia en Regimen Sinusoidal]]).
> ¿Qué ocurre al sumar las tres fases de un trifásico equilibrado?
>
> **Paso 1 — Las tres potencias.** Cada fase aporta su propia $p_k(t)$, idéntica en forma pero con la
> corriente y la tensión desfasadas $120^\circ$ entre fases. El término medio $V_{ef}I_{ef}\cos\varphi$
> es **igual** en las tres.
>
> **Paso 2 — Los términos pulsantes.** Al estar las fases a $120^\circ$, sus términos a $2\omega$
> quedan desfasados $2\times120^\circ=240^\circ$ entre sí. Tres cosenos de igual amplitud separados
> $240^\circ$ **suman cero** en todo instante (forman un sistema equilibrado de orden 3).
>
> **Paso 3 — La suma.** Sobreviven solo los tres términos medios:
> $$p(t)=p_a+p_b+p_c=3\,V_{ef}I_{ef}\cos\varphi=\text{constante}.$$
>
> > [!solucion]
> > La potencia trifásica instantánea es **constante** e igual a la potencia **media total**
> > $P=3V_{ef}I_{ef}\cos\varphi$. A diferencia del monofásico, no hay componente pulsante: el generador
> > recibe (y la carga absorbe) un flujo de energía **uniforme** instante a instante.

---

## En qué consiste

> [!teoria] Las tres ventajas, en detalle
> **Potencia constante.** En cada fase la potencia pulsa a $2\omega$, pero las tres pulsaciones están
> desfasadas $240^\circ$ entre sí y **suman cero**. La potencia total es entonces constante e igual a
> la media. Mecánicamente esto es muy valioso: un generador o motor trifásico entrega/absorbe **par
> uniforme**, con **menos vibración** y menor fatiga que una máquina monofásica, cuyo par late dos
> veces por ciclo.
>
> **Campo magnético giratorio.** Tres corrientes desfasadas $120^\circ$ circulando por tres devanados
> dispuestos a $120^\circ$ en el espacio producen un campo magnético resultante de **módulo constante**
> que **gira** a la velocidad angular $\omega$. Este campo giratorio "arrastra" al rotor: es el
> principio del **motor de inducción** (Tesla), que arranca por sí solo, sin escobillas ni dispositivos
> auxiliares. Un sistema monofásico, en cambio, genera un campo **pulsante** (no giratorio), por lo que
> el motor monofásico necesita artificios de arranque.
>
> **Ahorro de cobre.** Para transmitir la **misma potencia**, a la **misma tensión** y con las
> **mismas pérdidas**, el trifásico —que necesita solo **3 hilos**— emplea **menos cobre** que tres
> sistemas monofásicos independientes (que requerirían 6 hilos) o que un monofásico equivalente. Al
> repartir la potencia entre tres conductores y aprovechar la anulación de corrientes, el peso de cobre
> por unidad de potencia transportada baja de forma apreciable, lo que abarata generación y transporte.

> [!proposicion] El neutro no lleva corriente con carga equilibrada
> En una conexión en **estrella equilibrada**, las tres corrientes de línea tienen igual módulo y están
> a $120^\circ$, de modo que su suma —la corriente que retornaría por el neutro— es **cero**:
> $$\underline{I}_a+\underline{I}_b+\underline{I}_c=\underline{I}_N=0.$$
> El conductor de neutro puede entonces ser de **menor sección** o **suprimirse** por completo, dando
> el sistema **a 3 hilos**. Es un ahorro adicional de material que refuerza la tercera ventaja.

> [!warning]
> Las tres ventajas exigen **equilibrio**: tensiones y cargas iguales y a exactamente $120^\circ$. Con
> **desequilibrio**, la cancelación deja de ser perfecta y la potencia total vuelve a **pulsar** algo;
> el campo deja de ser de módulo constante; y el **neutro deja de estar a cero**, llevando corriente de
> retorno (por lo que entonces **no** conviene suprimirlo). Además, el campo giratorio solo gira en el
> sentido correcto si la **secuencia de fases** es la adecuada: invertir dos fases invierte el giro del
> motor.

## Resumen

> [!resumen]
> | Ventaja | En qué consiste | Condición |
> |:---|:---|:---|
> | Potencia constante | Los términos a $2\omega$ (a $240^\circ$) suman $0$; $p(t)=3V_{ef}I_{ef}\cos\varphi$ | Equilibrio |
> | Campo giratorio | Campo de módulo constante que gira a $\omega$ → motor de inducción autoarrancante | Secuencia correcta |
> | Ahorro de cobre | Misma potencia con 3 hilos en vez de 6; menos cobre por kW | Igual $V$ y pérdidas |
> | Neutro sin corriente | $\underline{I}_a+\underline{I}_b+\underline{I}_c=0$ → neutro reducido o suprimido (3 hilos) | Estrella equilibrada |

> [!corolario]
> El trifásico se impuso porque, con **mínimo número de fases** ($n=3$), reúne a la vez **par
> uniforme**, **arranque natural de motores** y **economía de conductor**. Las tres ventajas son **caras
> de una misma moneda**: la coherencia de tres magnitudes a $120^\circ$ en un sistema equilibrado. Por
> eso es el estándar universal de generación y transporte de energía.

> [!referencia]
> Fraile Mora, cap. 3, §3.9. Cuantificación de la potencia constante:
> [[Potencia en Sistemas Balanceados]]. Pulsación monofásica de partida: [[Potencia en Regimen Sinusoidal]].
> Familia general: [[Sistema Polifasico]]. Marco: [[Fundamentos Trifasicos/index]],
> [[7 Circuitos Trifasicos/index]].
