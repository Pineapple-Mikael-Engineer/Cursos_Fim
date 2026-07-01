---
title: Dominios Físicos
order: 1
tags:
  - control-clasico
  - modelado
  - index
draft: false
aliases:
  - dominios físicos
  - modelado por dominios
  - analogías físicas
  - physical domains
---

# Dominios Físicos

> [!definicion]
> Modelar una planta consiste en escribir sus **ecuaciones diferenciales** a partir de las leyes de cada **dominio físico**: eléctrico, mecánico (traslacional y rotacional), de fluidos, térmico o neumático. Lo notable es que todos comparten la **misma estructura matemática** —una variable de "esfuerzo" y otra de "flujo", con elementos que almacenan o disipan energía—, así que existen **analogías** directas entre dominios que permiten tratarlos con las mismas herramientas.

> [!info]
> Parte del [[2 Modelado/index| modelado]] de sistemas: aquí se obtienen las ecuaciones de cada tipo de planta antes de pasarlas a [[Transformada Laplace/index| Laplace]] y a [[Funcion Transferencia/index| función de transferencia]]. Ogata, cap. 2–3; Nise, cap. 2.

## Un método, muchos dominios

> [!teoria] Esfuerzo, flujo y analogías
> En cada dominio hay una variable de **esfuerzo** (tensión, fuerza, par, presión, temperatura) y una de **flujo** (corriente, velocidad, caudal), y tres tipos de elemento: los que **almacenan** energía (inercia y capacidad) y los que la **disipan** (resistencia). Escribir el modelo es aplicar las leyes de balance del dominio (Kirchhoff, Newton, continuidad) y ordenar el resultado como una EDO. Las **analogías** (p. ej. fuerza–tensión, velocidad–corriente) permiten reutilizar la intuición de un dominio en otro.

## Mapa de la sección

> [!info] Los dominios
> | Nota | Dominio |
> |:---|:---|
> | [[Electrico]] | circuitos R, L, C (Kirchhoff) |
> | [[Electronica]] | amplificadores operacionales y etapas activas |
> | [[Mecanico Traslacional]] | masa–resorte–amortiguador (Newton) |
> | [[Mecanico Rotacional]] | inercia, rigidez y fricción rotacionales |
> | [[Fluidos Nivel]] | tanques, caudal y nivel (continuidad) |
> | [[Neumatico]] | sistemas de gas a presión |
> | [[Termico]] | capacidad y resistencia térmicas |

> [!corolario]
> Modelar es siempre lo mismo —balance de energía en variables de esfuerzo y flujo— cambiando solo las leyes del dominio. Reconocer las analogías convierte siete problemas en uno solo, y el resultado (una EDO) es la puerta de entrada al análisis en $s$.

> [!referencia]
> Ogata, *Ingeniería de Control Moderna*, cap. 2–3. Nise, *Control Systems Engineering*, cap. 2.
