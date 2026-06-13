---
title: Problemas Bien Planteados
tags:
  - ecuaciones
  - edp
  - teoria
  - fundamentos
  - hadamard
draft: false
aliases:
  - problema bien planteado
  - condiciones de Hadamard
  - problema mal planteado
  - well-posed problem
  - Hadamard ill-posed
---

# Problemas Bien Planteados (Hadamard)

> [!definicion]
> Un **problema** (una EDP junto con sus datos: condiciones iniciales y/o de frontera) está **bien
> planteado** en el sentido de **Hadamard** si cumple las tres condiciones:
> 1. **Existencia** — hay al menos una solución;
> 2. **Unicidad** — esa solución es única;
> 3. **Dependencia continua** — la solución cambia **poco** si los datos cambian poco (estabilidad).
>
> Si falla **alguna** de las tres, el problema está **mal planteado** (*ill-posed*).

> [!info]
> Cierra el ciclo de los [[Fundamentos/index| fundamentos]]: la
> [[Clasificacion Segundo Orden| clasificación]] dice de qué **tipo** es una EDP, y esta nota dice
> **qué datos** la hacen bien planteada. Cada tipo (elíptico, parabólico, hiperbólico) admite su
> propio juego de [[Tipos de Condiciones| condiciones]]; imponer las equivocadas la vuelve
> irresoluble o inestable.

---

## Ejemplo

> [!ejemplo] El contraejemplo de Hadamard: Cauchy para Laplace
> Considera la ecuación **elíptica** de Laplace $u_{xx}+u_{yy}=0$ con datos de **Cauchy** sobre la
> recta $y=0$:
> $$u(x,0)=0,\qquad u_y(x,0)=\tfrac1n\,\operatorname{sen}(nx),\qquad n\in\mathbb{N}.$$
> Separando variables se obtiene la solución
> $$u_n(x,y)=\frac{1}{n^2}\,\operatorname{sen}(nx)\,\operatorname{senh}(ny).$$
> **Mira los datos cuando $n\to\infty$:** el dato $u_y(x,0)=\tfrac1n\operatorname{sen}(nx)$ tiene
> amplitud $\tfrac1n\to0$, es decir, los datos se acercan **uniformemente** a los del problema con
> datos nulos (cuya solución es $u\equiv0$).
> **Pero mira la solución:** para cualquier $y>0$ fijo,
> $$\lvert u_n(x,y)\rvert\sim\frac{1}{n^2}\,\frac{e^{ny}}{2}\xrightarrow[n\to\infty]{}\infty.$$
> El factor $\operatorname{senh}(ny)$ crece **exponencialmente** y aplasta al $1/n^2$. Datos que
> tienden a cero producen soluciones que **explotan**: falla la **dependencia continua**. Conclusión:
> el problema de **Cauchy** para una EDP **elíptica** está **mal planteado** — Laplace no admite que
> "evolucionemos" datos a partir de una curva.

> [!ejemplo] La ecuación del calor hacia atrás en el tiempo
> La ecuación del calor $u_t=\alpha^2u_{xx}$ **suaviza** y amortigua los modos altos hacia el futuro:
> un modo $\operatorname{sen}(nx)$ decae como $e^{-\alpha^2n^2t}$. Si intentamos resolverla **hacia
> atrás** (dato en $t=T$, buscar $u$ en $t<T$), ese mismo factor se invierte a $e^{+\alpha^2n^2(T-t)}$:
> el más mínimo ruido de alta frecuencia se **amplifica sin cota**. El problema retrógrado es **mal
> planteado**: matemáticamente expresa que la difusión es **irreversible** (no se puede
> "des-difundir" una taza de café fría hasta recuperar el calor inicial).

---

## En qué consiste

> [!teoria] Por qué importan las tres condiciones a la vez
> - Sin **existencia**, buscar la solución es absurdo.
> - Sin **unicidad**, no sabemos cuál de las muchas soluciones describe la física: faltan datos o
>   sobran grados de libertad.
> - Sin **dependencia continua**, aunque exista y sea única, es **inútil en la práctica**: los datos
>   reales siempre tienen error de medida, y un problema inestable convierte un error diminuto en una
>   respuesta arbitrariamente grande. Numéricamente, el redondeo basta para arruinar el cálculo.
>
> Hadamard introdujo este criterio precisamente para distinguir los problemas de la física
> matemática "sanos" de los que, pese a tener ecuaciones impecables, no representan ningún fenómeno
> reproducible.

> [!proposicion] Qué problema es bien planteado para cada tipo
> | Tipo de EDP | Datos bien planteados | Ejemplo prototipo |
> |---|---|---|
> | **Elíptica** | **solo de frontera** (Dirichlet o Neumann) sobre $\partial\Omega$ | Laplace $u_{xx}+u_{yy}=0$ |
> | **Parabólica** | **inicial** ($u$ en $t=0$) **+ frontera** | calor $u_t=\alpha^2u_{xx}$ |
> | **Hiperbólica** | **Cauchy** ($u$ y $u_t$ en $t=0$) **+ frontera** | onda $u_{tt}=c^2u_{xx}$ |

> [!warning]
> Imponer "los datos equivocados" a una EDP la vuelve **irresoluble** o **numéricamente inestable**:
> Cauchy a una elíptica (explota), o evolución retrógrada de una parabólica (amplifica el ruido). El
> tipo de la ecuación **dicta** qué condiciones tienen sentido; no es opcional.

## Resumen

> [!resumen]
> | Condición de Hadamard | Qué garantiza | Si falla… |
> |---|---|---|
> | Existencia | hay solución | el problema no tiene respuesta |
> | Unicidad | la solución es única | faltan/sobran datos; física ambigua |
> | Dependencia continua | estabilidad ante el ruido | inútil en la práctica; numéricamente caótico |

> [!corolario]
> "Bien planteado" no es un lujo teórico: es la condición para que una EDP **modele** algo real y se
> pueda **calcular**. La clave para lograrlo es casar el **tipo** de la EDP con sus
> [[Tipos de Condiciones| condiciones]] —cada tipo exige las suyas.

> [!referencia]
> - El tipo que decide qué datos van: [[Clasificacion Segundo Orden]].
> - El catálogo de condiciones (Cauchy, Dirichlet, Neumann, Robin): [[Tipos de Condiciones]].
> - Marco general: [[Fundamentos/index]].
