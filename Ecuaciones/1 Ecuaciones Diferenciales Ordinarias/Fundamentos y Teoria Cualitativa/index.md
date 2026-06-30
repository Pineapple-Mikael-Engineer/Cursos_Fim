---
title: Fundamentos y Teoría Cualitativa de EDO
order: 1
tags:
  - ecuaciones
  - edo
  - teoria
  - fundamentos
  - index
draft: false
aliases:
  - fundamentos EDO
  - teoria cualitativa
  - existencia y unicidad
---

# Fundamentos y Teoría Cualitativa de EDO

> [!definicion]
> Antes de *resolver*, dos preguntas: ¿qué es exactamente una EDO y su solución, y **cuándo** un problema de valor inicial tiene solución y es **única**? La respuesta geométrica es el **campo de direcciones** (la EDO asigna una pendiente a cada punto) y la analítica es el **teorema de existencia y unicidad de Picard**. La unicidad es la cara matemática del **determinismo**.

> [!info]
> Base del [[1 Ecuaciones Diferenciales Ordinarias/index| capítulo de EDO]]. Aquí no se resuelve por tipos (eso es [[Metodos de Primer Orden/index| Métodos de Primer Orden]]); se establece el marco: qué se busca, por qué a veces hay infinitas soluciones o ninguna, y qué condiciones garantizan una sola.

---

## El cambio de pregunta: de "cómo resolver" a "qué garantiza una solución"

> [!teoria]
> Los métodos algebraicos contestan *cómo* hallar $y(x)$ **cuando se puede**. Pero la mayoría de las EDO no se resuelven en funciones elementales, así que primero conviene preguntar algo más básico: dado el PVI $y'=f(x,y),\ y(x_0)=y_0$, ¿**existe** una solución? ¿es **única**? ¿hasta dónde llega?
>
> La clave es reescribir el PVI como una **ecuación integral** equivalente,
> $$y(x)=y_0+\int_{x_0}^{x} f\big(t,y(t)\big)\,dt,$$
> que ya **incorpora la condición inicial** y convierte "derivar" en "integrar" (operación más estable). Sobre esta forma se montan los dos pilares del capítulo:
> - **Existencia** ([[Teorema de Peano|Peano]]): basta que $f$ sea **continua**.
> - **Unicidad** ([[Existencia y Unicidad Picard|Picard]]): hace falta que $f$ sea **Lipschitz** en $y$ —se construye como [[Iteracion de Picard|punto fijo]] de un operador contractivo, y la [[Desigualdad de Gronwall|desigualdad de Gronwall]] la sella.

> [!teoria] Existencia ≠ unicidad: el ejemplo que lo separa
> El PVI $y'=x\,y^{1/2},\ y(0)=0$ tiene **dos** soluciones distintas, $y\equiv0$ y $y=\tfrac{x^4}{16}$ (de hecho infinitas). $f=xy^{1/2}$ **es continua** —por eso *existe* solución (Peano)— pero su derivada $\partial f/\partial y=\tfrac{x}{2\sqrt y}$ explota en $y=0$, así que **no es Lipschitz** y se pierde la unicidad. Este único ejemplo justifica por qué hacen falta *dos* teoremas y no uno: la continuidad da la curva, pero solo la condición de Lipschitz garantiza que sea **la única**.

---

## Recorrido

> [!info] De lo geométrico a lo analítico
> | Nota | Aporte |
> |---|---|
> | [[Concepto General de ODE\|Concepto General de ODE]] | orden, forma normal, PVI, solución implícita, sistema equivalente |
> | [[Campo de Direcciones e Isoclinas\|Campo de Direcciones e Isoclinas]] | imagen geométrica: pendientes e isoclinas |
> | [[Curvas Integrales y Soluciones\|Curvas Integrales y Soluciones]] | solución general/particular/singular; las curvas no se cruzan |
> | [[Existencia y Unicidad Picard\|Existencia y Unicidad (Picard)]] | condición de Lipschitz ⇒ solución única |
> | [[Teorema de Peano\|Teorema de Peano]] | solo continuidad ⇒ existe, pero puede no ser única |
> | [[Iteracion de Picard\|Iteración de Picard]] | construcción **constructiva** de la solución |
> | [[Desigualdad de Gronwall\|Desigualdad de Gronwall]] | herramienta clave: acota y da unicidad/estabilidad |
> | [[Prolongacion de Soluciones\|Prolongación de Soluciones]] | hasta dónde vive la solución (intervalo maximal) |
> | [[Dependencia de Condiciones y Parametros\|Dependencia de Condiciones y Parámetros]] | la solución varía con continuidad respecto a los datos |

---

## La idea unificadora

> [!teoria]
> Una EDO de primer orden $y'=f(x,y)$ **no** da la solución: da su **pendiente** en cada punto. Es un campo de flechas. Una solución es una curva que en todo punto es tangente al campo (una *curva integral*). Las preguntas de fondo son entonces geométricas:
> - ¿Pasa una curva integral por cada punto? → **existencia** ([[Teorema de Peano|Peano]]).
> - ¿Pasa **una sola**? → **unicidad** ([[Existencia y Unicidad Picard|Picard]], vía Lipschitz).
> - ¿Hasta dónde se puede seguir? → **prolongación**.
>
> Cuando la unicidad falla (como en $y'=x\,y^{1/2}$ desde el origen) el sistema deja de ser determinista: el mismo presente admite varios futuros.

## Resumen

> [!resumen]
> | Pregunta | Respuesta | Condición |
> |---|---|---|
> | ¿Qué es una solución? | curva integral del campo de direcciones | tangente a $f$ en cada punto |
> | ¿Existe? | sí | $f$ **continua** (Peano) |
> | ¿Es única? | sí | $f$ **Lipschitz** en $y$ (basta $\partial f/\partial y$ continua) — Picard |
> | ¿Cómo se construye? | límite de [[Iteracion de Picard\|iteraciones de Picard]] | contracción |
> | ¿Hasta dónde vive? | intervalo maximal | hasta que escapa o toca la frontera |

> [!corolario]
> Existencia y unicidad **no** son lo mismo: la continuidad de $f$ asegura que *hay* solución, pero hace falta algo más fuerte (Lipschitz) para que sea *única*. Ese "algo más" es lo que conecta la matemática con el determinismo físico.

> [!referencia]
> - Geometría de partida: [[Campo de Direcciones e Isoclinas]].
> - Teorema central: [[Existencia y Unicidad Picard]].
> - Después de los fundamentos, los métodos: [[Metodos de Primer Orden/index]].
