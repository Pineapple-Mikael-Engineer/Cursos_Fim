---
title: Fuentes Dependientes
order: 3
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - fuentes
draft: false
aliases:
  - fuentes dependientes
  - fuentes controladas
  - VCVS
  - VCCS
  - CCVS
  - CCCS
  - dependent sources
  - controlled sources
---

# Fuentes Dependientes (controladas)

> [!definicion]
> Una **fuente dependiente** o **controlada** es un elemento activo cuyo valor **no es fijo**, sino proporcional a otra tensión $v_x$ o corriente $i_x$ medida en algún punto del propio circuito. Se dibuja con un **rombo** (frente al círculo de las independientes). Según qué impongan (tensión o corriente) y qué las controle (tensión o corriente), hay **cuatro** tipos: VCVS, VCCS, CCVS y CCCS.

---

> [!info]
> Tercera nota de [[Elementos del Circuito/index| Elementos del circuito]], en el [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Generalizan a las [[Fuentes Independientes]] y son la base de los modelos de transistores y amplificadores; su valor se fija con una [[Ecuaciones de Restriccion| ecuación de restricción]].

---

## Ejemplo

> [!ejemplo] Una VCVS resuelta con su ecuación de control
> En el circuito, una fuente $v_s=2\ \text{V}$ alimenta una resistencia $R_1=1\ \Omega$ por la que circula $i_x$; la tensión sobre $R_1$ es la variable de control $v_x$. Una **VCVS** de ganancia $\mu=4$ entrega $v=\mu v_x$ sobre una carga $R_L=8\ \Omega$. Resolvemos.
>
> ![[fuentes_dependientes.svg|480]]
> Los cuatro tipos de fuente dependiente (rombo): VCVS, VCCS, CCVS, CCCS.
>
> **Paso 1 — variable de control.** Toda la $v_s$ cae sobre $R_1$, luego
> $$v_x=v_s=2\ \text{V}.$$
>
> **Paso 2 — ecuación de la fuente.** La VCVS impone
> $$v=\mu\,v_x=4\times 2\ \text{V}=8\ \text{V}.$$
>
> **Paso 3 — la carga.** Esa tensión actúa sobre $R_L=8\ \Omega$:
> $$i_L=\frac{v}{R_L}=\frac{8\ \text{V}}{8\ \Omega}=1\ \text{A},\qquad
> p_L=v\,i_L=8\ \text{W}.$$
>
> La fuente no tiene un valor propio: vale $8\ \text{V}$ **porque** $v_x$ vale $2\ \text{V}$. Si cambiase la entrada, cambiaría su salida en la misma proporción $\mu$.

---

## En qué consiste

> [!teoria] Los cuatro tipos
> Una fuente dependiente queda definida por **qué impone** (tensión o corriente) y por **qué la controla** (una tensión $v_x$ o una corriente $i_x$ del circuito). Combinando ambas elecciones resultan cuatro casos, cada uno con su constante característica:
>
> - **VCVS** — fuente de **tensión** controlada por **tensión**: $\;v=\mu\,v_x$. La ganancia $\mu$ es adimensional.
> - **VCCS** — fuente de **corriente** controlada por **tensión**: $\;i=g\,v_x$. La **transconductancia** $g$ se mide en siemens ($\text{S}$).
> - **CCVS** — fuente de **tensión** controlada por **corriente**: $\;v=r\,i_x$. La **transresistencia** $r$ se mide en ohmios ($\Omega$).
> - **CCCS** — fuente de **corriente** controlada por **corriente**: $\;i=\beta\,i_x$. La ganancia $\beta$ es adimensional.
>
> En las siglas inglesas, la primera letra indica el **control** (V/C) y la segunda lo que la fuente **es** (V/C): así *VCVS* = *Voltage-Controlled Voltage Source*.

> [!algoritmo] Resolver un circuito con fuente dependiente
> **Paso 1.** Identifica con claridad la **variable de control** ($v_x$ o $i_x$) y dónde se mide; márcala en el esquema. **Paso 2.** Escribe la **ecuación de la fuente** ($v=\mu v_x$, $i=g v_x$, $v=r i_x$ o $i=\beta i_x$) como una **ecuación adicional**, tratando la fuente como independiente *de valor incógnito*. **Paso 3.** Plantea las leyes de Kirchhoff del resto del circuito. **Paso 4.** Resuelve el sistema acoplado: la variable de control y las demás incógnitas se determinan **a la vez**. Nunca dejes la fuente con un número fijo "a mano".

> [!proposicion] Por qué importan: transistores y amplificadores
> Las fuentes dependientes no son una curiosidad: son el **corazón de los modelos activos**. Un transistor en pequeña señal se modela como una **VCCS** (la corriente de salida la controla la tensión de entrada) o como una **CCCS** (corriente de salida controlada por la de base). Un amplificador operacional ideal es esencialmente una **VCVS** de ganancia enorme. Sin este elemento no se podría modelar la **amplificación**, que ninguna combinación de resistencias y fuentes independientes produce.

> [!warning]
> Una fuente dependiente **no** se puede "apagar" arbitrariamente: su valor está atado a la variable de control. Al aplicar superposición o hallar equivalentes de Thévenin, las fuentes **independientes** se anulan, pero las **dependientes se mantienen activas** y se acompañan de su ecuación de control. Olvidarlo es el error más frecuente con estas fuentes.

---

## Resumen

> [!resumen] Los cuatro tipos en una tabla
> | Tipo | Impone | Controlada por | Ecuación | Constante (unidad) |
> |:---:|:---:|:---:|:---:|:---:|
> | VCVS | tensión | tensión $v_x$ | $v=\mu\,v_x$ | $\mu$ (adim.) |
> | VCCS | corriente | tensión $v_x$ | $i=g\,v_x$ | $g$ ($\text{S}$) |
> | CCVS | tensión | corriente $i_x$ | $v=r\,i_x$ | $r$ ($\Omega$) |
> | CCCS | corriente | corriente $i_x$ | $i=\beta\,i_x$ | $\beta$ (adim.) |

> [!corolario]
> Toda fuente dependiente añade **una ecuación** (la de control) al sistema del circuito y se dibuja con **rombo**. Resolver con ellas es, en el fondo, resolver Kirchhoff con esa restricción extra acoplada.

> [!referencia]
> Fraile Mora, cap. 1, §1.5. Relacionado: [[Fuentes Independientes]] y [[Ecuaciones de Restriccion]].
