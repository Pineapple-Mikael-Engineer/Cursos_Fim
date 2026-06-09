---
title: Ecuaciones Integro-Diferenciales
tags:
  - ecuaciones
  - difero-integrales
  - teoria
  - integro-diferenciales
  - index
draft: false
aliases:
  - ecuaciones integro-diferenciales
  - integro-differential equations
  - sistemas con memoria
---

# Ecuaciones Integro-Diferenciales

> [!definicion]
> Una **ecuación integro-diferencial** contiene, sobre la misma incógnita, **derivadas** $\varphi',
> \varphi'',\dots$ **y** una **integral** $\int K\varphi$. La forma típica (de Volterra) es
> $$\varphi'(t)=f(t)+\lambda\int_{0}^{t}K(t,s)\,\varphi(s)\,ds,\qquad \varphi(0)=\varphi_0.$$
> Modela sistemas con **memoria**: la tasa de cambio actual depende de toda la **historia** de la
> incógnita, no solo de su valor presente.

> [!info]
> Primera rama del [[4 Ecuaciones Difero-integrales/index| capítulo difero-integral]]: la unión
> explícita de lo diferencial y lo integral. Su herramienta maestra es la
> [[Transformada de Laplace/index| transformada de Laplace]] cuando el núcleo es de **convolución**
> $K(t-s)$ — la misma de las [[Ecuaciones de Convolucion| ecuaciones de convolución]] de Volterra.

---

## Por qué aparece la memoria

> [!teoria]
> En una EDO ordinaria $\varphi'=f(t,\varphi)$, el futuro depende **solo del estado presente** (sistema
> sin memoria, markoviano). Pero muchos sistemas reales **recuerdan**: un material viscoelástico
> responde según toda su historia de deformación; una población depende de los nacimientos pasados;
> un circuito con un elemento de memoria "arrastra" su carga previa. Eso introduce el término integral
> $\int_0^t K(t-s)\varphi(s)\,ds$: una **suma ponderada del pasado**, con el núcleo $K$ como **función
> de memoria** (cuánto pesa lo ocurrido hace $t-s$).
>
> La estrategia general es **convertir la memoria en álgebra**:
> - **Laplace** (si $K$ es de convolución): transforma la integral en un producto y la derivada en
>   multiplicar por $s$ → una ecuación **algebraica** ([[Resolucion por Transformada de Laplace| resolución por Laplace]]).
> - **Reducción a sistemas**: introducir la integral como nueva variable convierte la ecuación en un
>   **sistema** de EDO/integrales ([[Reduccion a Sistemas| reducción a sistemas]]).

> [!info] Recorrido de la sección
> | Nota | Aporte |
> |---|---|
> | [[Concepto y Clasificacion\|Concepto y Clasificación]] | Volterra vs Fredholm integro-dif.; orden |
> | [[Resolucion por Transformada de Laplace\|Resolución por Laplace]] | núcleo de convolución → algebraica |
> | [[Reduccion a Sistemas\|Reducción a Sistemas]] | a un sistema de primer orden / ec. integral |
> | [[Ecuaciones con Memoria\|Ecuaciones con Memoria]] | función de memoria; ecuación de renovación |
> | [[Aplicaciones Integro-Diferenciales\|Aplicaciones]] | viscoelasticidad, poblaciones, transporte |

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Forma | $\varphi'(t)=f+\lambda\int_0^t K(t,s)\varphi\,ds$ |
> | Significado | tasa de cambio con **memoria** del pasado |
> | Método (convolución) | [[Transformada de Laplace/index\|Laplace]] → algebraica |
> | Método general | reducir a un sistema |
> | Puente | con núcleo $1/(t-s)^\alpha$ → ecuación **fraccionaria** |

> [!corolario]
> Las integro-diferenciales son EDO **con historia**: el término integral es la huella del pasado
> sobre el presente. Cuando esa memoria es de convolución, Laplace la desenreda de un golpe,
> convirtiendo derivar-e-integrar en multiplicar y dividir.

> [!referencia]
> - El método estrella: [[Resolucion por Transformada de Laplace]].
> - El significado físico: [[Ecuaciones con Memoria]].
> - La generalización: [[Calculo Fraccionario/index]].
