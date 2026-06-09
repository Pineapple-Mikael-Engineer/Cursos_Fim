---
title: Ondas en 2D y 3D
tags:
  - ecuaciones
  - edp
  - teoria
  - onda
  - huygens
draft: false
aliases:
  - ondas en 2D y 3D
  - principio de Huygens
  - fórmula de Kirchhoff
  - fórmula de Poisson
  - Huygens principle
---

# Ondas en 2D y 3D

> [!definicion]
> En dimensiones superiores la ecuación de onda es $u_{tt}=c^2\nabla^2u$. Su solución ya no se reduce
> a dos pulsos viajeros como en la recta: en **3D**, la **fórmula de Kirchhoff** expresa $u$ como un
> **promedio de los datos sobre esferas** de radio $ct$; en **2D**, la **fórmula de Poisson** lo hace
> sobre **discos**. Esa diferencia entre "cáscara esférica" y "disco lleno" tiene una consecuencia
> física profunda: el **principio de Huygens**.

> [!info]
> Generaliza la [[Solucion de dAlembert| solución de d'Alembert]] (caso 1D) de la
> [[Ecuacion de Onda/index| ecuación de onda]] a dos y tres dimensiones. La conservación de energía
> que la sostiene se trata en [[Energia de la Onda]]. Aquí presentamos el panorama —Kirchhoff,
> Poisson, Huygens— sin desarrollar todo el aparato de promedios esféricos.

---

## Ejemplo

> [!ejemplo] Por qué se oye nítido y por qué el estanque deja estela
> Compara dos perturbaciones **localizadas** (un destello de luz/sonido en 3D, una piedra en un
> estanque en 2D):
> - **En 3D (un flash o un chasquido).** La señal se percibe en un instante **agudo** —el frente
>   esférico— y, una vez que pasa, vuelve el **silencio total**. Por eso un relámpago se ve como un
>   destello y no como un resplandor que se apaga lentamente, y por eso podemos comunicarnos con
>   palabras nítidas: cada sílaba llega y se va sin arrastrar una cola que emborrone la siguiente.
> - **En 2D (la piedra en el agua).** El frente de onda pasa, pero **detrás queda un rastro** que
>   decae: las ondas circulares que siguen agitándose después de que la cresta principal ya cruzó.
>   En el plano, una perturbación instantánea deja **cola**.
>
> La diferencia no es un capricho del medio: es matemática pura, y tiene nombre: el **principio de
> Huygens**.

## En qué consiste

> [!teoria]
> En 3D, la solución en $(x,t)$ se obtiene **promediando los datos iniciales sobre la esfera** de
> centro $x$ y radio $ct$: solo importa lo que estaba a distancia **exactamente** $ct$. En 2D, en
> cambio, hay que promediar sobre el **disco** completo de radio $ct$: importa todo lo que estaba a
> distancia **menor o igual** que $ct$. Esa es la raíz de la diferencia: en 3D el pasado relevante es
> una **cáscara** (un instante), en 2D es un **volumen** (toda la historia hasta ese radio), y por eso
> el segundo arrastra cola.

> [!teorema] Principio de Huygens
> En **dimensiones espaciales impares $\ge 3$** (en particular en 3D, el mundo físico), una
> perturbación inicialmente confinada a una región pequeña se percibe en cada punto durante un
> **intervalo nítido** y luego cesa por completo: el frente es **agudo y sin cola**. En **dimensiones
> pares** (en particular en 2D) **no** se cumple: tras el paso del frente persiste un **rastro que
> decae** lentamente.

> [!info] Panorama de las fórmulas
> Sin entrar en todo el detalle técnico, las soluciones explícitas son:
> - **Kirchhoff (3D).** $u(x,t)$ se escribe con **promedios esféricos** de $f$ y $g$ sobre la esfera
>   $|y-x|=ct$; la dependencia es solo de esa cáscara, lo que produce el frente limpio.
> - **Poisson (2D).** $u(x,t)$ se escribe con integrales sobre el **disco** $|y-x|\le ct$, con un peso
>   $\big(c^2t^2-|y-x|^2\big)^{-1/2}$ que pondera todo el interior; ese peso es el que genera la cola.
>
> Ambas reducen a [[Solucion de dAlembert| d'Alembert]] al bajar a 1D, y todas comparten el rasgo
> hiperbólico esencial: **velocidad finita de propagación**, con la información confinada al cono
> $|y-x|\le ct$.

> [!proposicion]
> El principio de Huygens es la razón física de que vivamos en un mundo **acústicamente y ópticamente
> legible**: en 3D una señal emitida llega "de una pieza" y desaparece, permitiendo distinguir
> sonidos e imágenes sucesivos. Si el espacio fuera bidimensional, cada sonido dejaría una reverberación
> que se solaparía con el siguiente y la comunicación nítida sería imposible.

## Resumen

> [!resumen]
> | Dimensión | Fórmula | Promedio sobre | ¿Huygens? |
> |---|---|---|---|
> | 1D | d'Alembert | dos puntos / segmento | frente limpio |
> | 2D | Poisson | **disco** $\|y-x\|\le ct$ | **no**: hay cola |
> | 3D | Kirchhoff | **esfera** $\|y-x\|=ct$ | **sí**: frente agudo |

> [!corolario]
> Subir de dimensión no cambia la ecuación ($u_{tt}=c^2\nabla^2u$) pero sí la **textura** de sus
> soluciones: la diferencia entre promediar sobre una cáscara (3D) o un volumen (2D) es la diferencia
> entre oír una palabra clara y ver una estela en el agua. El principio de Huygens es, en el fondo, un
> regalo de la dimensionalidad impar del espacio.

> [!referencia]
> - El caso 1D del que todo parte: [[Solucion de dAlembert]].
> - La energía que se conserva en todas las dimensiones: [[Energia de la Onda]].
> - El panorama de la sección: [[Ecuacion de Onda/index]].
