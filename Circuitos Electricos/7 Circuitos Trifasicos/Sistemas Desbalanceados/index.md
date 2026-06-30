---
title: Sistemas Desbalanceados
tags:
  - circuitos-electricos
  - teoria
  - trifasico
  - index
draft: false
aliases:
  - sistemas desbalanceados
  - cargas desequilibradas
  - sistemas trifásicos desequilibrados
---

# Sistemas Desbalanceados

> [!definicion]
> Un sistema trifásico está **desequilibrado** cuando sus tres tensiones o sus tres cargas **no** son iguales (distinto módulo, o no exactamente a $120^\circ$). Entonces se pierde el atajo del equivalente por fase: hay que resolver **cada fase por separado**, el **neutro lleva corriente** y la potencia deja de ser constante. Se analiza directamente o con **componentes simétricas**.

> [!info]
> Cuarta y última sección del [[7 Circuitos Trifasicos/index| capítulo 7]] —y del curso—. Levanta la hipótesis de equilibrio de las [[Conexiones Balanceadas/index| conexiones balanceadas]]; usa mallas, nodos y [[Teorema de Millman| Millman]]. Fraile Mora, cap. 3, §3.10.

---

## Cuando se rompe la simetría

> [!teoria] Estrella, triángulo y el neutro
> Sin equilibrio, las tres corrientes de fase ya **no** suman cero. En **estrella con neutro**, ese desbalance se cierra por el **conductor neutro**, que ahora lleva $\overline{I}_N=\overline{I}_a+\overline{I}_b+\overline{I}_c\neq0$; si **no** hay neutro, el punto común se **desplaza** y hay que hallar su tensión ([[Teorema de Millman| Millman]]). → [[Cargas Desbalanceadas Estrella]]. En **triángulo**, cada rama ve la tensión de línea (equilibrada) pero conduce su propia corriente, y las de línea ya no guardan el factor $\sqrt3$. → [[Cargas Desbalanceadas Triangulo]].

> [!teoria] La herramienta general: componentes simétricas
> Cualquier conjunto de tres fasores desequilibrados se descompone en **tres** conjuntos equilibrados —secuencia **positiva**, **negativa** y **homopolar** (cero)—, cada uno tratable por separado:
>
> ![[componentes_simetricas.svg|660]]
>
> *Las tres secuencias en que se descompone un sistema desequilibrado: positiva ($abc$), negativa ($acb$) y homopolar (las tres en fase). Sumándolas se reconstruye el original.*
>
> Es el método de **Fortescue**, base del análisis de faltas y desequilibrios en sistemas de potencia. → [[Componentes Simetricas]].

## Mapa de la sección

> [!info] Las notas de esta sección
> | Nota | Contenido |
> |:---|:---|
> | [[Cargas Desbalanceadas Estrella]] | corriente de neutro; sin neutro, [[Teorema de Millman\| Millman]] |
> | [[Cargas Desbalanceadas Triangulo]] | cada rama por su lado; pérdida del $\sqrt3$ |
> | [[Componentes Simetricas]] | descomposición en secuencias (Fortescue) |

> [!corolario]
> Al romperse la simetría, el trifásico se vuelve tres problemas monofásicos acoplados por el neutro o los nudos. Resolverlos —directamente o por componentes simétricas— completa el dominio del sistema trifásico real, donde el equilibrio perfecto es solo una idealización.

> [!referencia]
> Fraile Mora, cap. 3, §3.10. Anterior: [[Potencia Trifasica/index| Potencia trifásica]]. Cierra el curso de **Circuitos Eléctricos (ML 140)**.
