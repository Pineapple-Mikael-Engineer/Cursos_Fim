---
title: Laplace en Circuitos
tags:
  - circuitos-electricos
  - teoria
  - transitorios
  - laplace
  - index
draft: false
aliases:
  - Laplace en circuitos
  - transformada de Laplace en circuitos
  - dominio de s
---

# Laplace en Circuitos

> [!definicion]
> La **transformada de Laplace** convierte las **ecuaciones diferenciales** de un circuito en
> **ecuaciones algebraicas** en la variable compleja $s$: derivar se vuelve multiplicar por $s$, e
> integrar, dividir por $s$. Cada elemento adquiere una **impedancia** $Z(s)$ —$R$, $sL$, $1/sC$— y
> **toda** la maquinaria resistiva (Ohm, Kirchhoff, mallas, nodos, Thévenin) se reutiliza tal cual.
> Resuelto el circuito en $s$, se **antitransforma** para recuperar la respuesta $x(t)$.

> [!info]
> Cuarta y última sección del [[3 Almacenamiento y Transitorios/index| capítulo 3]]. Es la
> herramienta **sistemática** que evita resolver a mano las EDO de los
> [[Transitorios Primer Orden/index| transitorios de primer]] y [[Transitorios Segundo Orden/index| segundo orden]]. Fraile Mora, cap. 4, §4.7-4.9 y Apéndice 2.

---

## Por qué Laplace lo simplifica todo

> [!teoria] De resolver EDO a despejar una incógnita
> Resolver un transitorio "a mano" exige plantear y resolver una ecuación diferencial, imponer
> condiciones iniciales y separar respuesta natural y forzada. Laplace **automatiza** todo eso:
>
> ![[laplace_flujo.svg|620]]
>
> *Se transforma el circuito al dominio de $s$ (donde las derivadas son multiplicaciones), se
> **despeja** la incógnita algebraicamente, y se antitransforma. Las condiciones iniciales entran
> solas, y respuesta natural y forzada salen juntas.*
>
> La clave es que en el dominio de $s$ un circuito con $L$ y $C$ se analiza **igual** que uno
> resistivo, usando **impedancias** $Z(s)$. → [[Circuitos en el Dominio de s]].

> [!teoria] Los polos cuentan la historia dinámica
> Al despejar, la incógnita queda como un cociente de polinomios $X(s)=\dfrac{N(s)}{D(s)}$. Las raíces
> de $D(s)$ —los **polos**— son exactamente las **frecuencias naturales** del circuito: las mismas
> raíces de la ecuación característica que clasificaban los
> [[Regimenes de Amortiguamiento| regímenes de amortiguamiento]]. Un polo real da una exponencial; un
> par complejo, una oscilación amortiguada; su parte real (negativa) garantiza que decae. Esa lectura
> es la **función de transferencia** $H(s)$ y su **diagrama de polos y ceros**. →
> [[Funcion de Transferencia]].

## Mapa de la sección

> [!info] Qué desarrolla cada hija
> | Nota | Contenido |
> |:---|:---|
> | [[Transformada de Laplace]] | definición, pares de transformadas y propiedades (derivada, integral) |
> | [[Circuitos en el Dominio de s]] | impedancias $R$, $sL$, $1/sC$; condiciones iniciales como fuentes |
> | [[Funcion de Transferencia]] | $H(s)=Y(s)/X(s)$; polos, ceros y estabilidad |
> | [[Solucion de Transitorios con Laplace]] | el método completo, con ejemplo resuelto |

> [!corolario]
> Laplace traslada el circuito a un mundo donde las ecuaciones diferenciales se vuelven álgebra y todo
> el arsenal de los capítulos 1-2 vuelve a servir. Resuelve transitorio y permanente de un golpe, y de
> paso revela —en los polos— por qué el circuito responde como lo hace.

> [!referencia]
> Fraile Mora, cap. 4, §4.7-4.9 y Apéndice 2. Anterior: [[Transitorios Segundo Orden/index| Transitorios de segundo orden]]. Cierra el [[3 Almacenamiento y Transitorios/index| capítulo 3]].
