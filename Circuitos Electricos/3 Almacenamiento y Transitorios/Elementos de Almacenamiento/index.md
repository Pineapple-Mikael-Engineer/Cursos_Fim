---
title: Elementos de Almacenamiento
tags:
  - circuitos-electricos
  - teoria
  - transitorios
  - index
draft: false
aliases:
  - elementos de almacenamiento
  - capacitor e inductor
  - condensador y bobina
---

# Elementos de Almacenamiento

> [!definicion]
> Los dos elementos pasivos que **almacenan energía** (en vez de disiparla como la resistencia): el **condensador** $C$, que guarda energía en su **campo eléctrico** ($q=Cv$, $i=C\,dv/dt$), y el **inductor** $L$, que la guarda en su **campo magnético** ($\phi=Li$, $v=L\,di/dt$). Son **duales**: intercambiando $v\leftrightarrow i$ y $C\leftrightarrow L$, las leyes de uno se vuelven las del otro.

> [!info]
> Primera sección del [[3 Almacenamiento y Transitorios/index| capítulo 3]]. Estos elementos y sus propiedades (energía, continuidad, comportamiento en DC) son la base de **todos** los transitorios ([[Transitorios Primer Orden/index| primer]] y [[Transitorios Segundo Orden/index| segundo orden]]). Fraile Mora, cap. 1, §1.5.

---

## Dos elementos duales con memoria

> [!teoria] Almacenar energía es tener memoria
> A diferencia de la resistencia (que responde al instante y disipa $Ri^2$), el condensador y el inductor **acumulan** energía y la devuelven: tienen **memoria**. Esa memoria se traduce en una ley con **derivada** y en una **variable de estado** que no puede cambiar de golpe:
>
> | | Condensador $C$ | Inductor $L$ |
> |:---|:---|:---|
> | almacena en | campo eléctrico | campo magnético |
> | ley | $i=C\dfrac{dv}{dt}$ | $v=L\dfrac{di}{dt}$ |
> | energía | $W=\tfrac12 C v^2$ | $W=\tfrac12 L i^2$ |
> | **no salta** | la **tensión** $v_C$ | la **corriente** $i_L$ |
> | en DC estable | circuito **abierto** | **cortocircuito** |
>
> La columna de la derecha es la de la izquierda con $v\leftrightarrow i$ y $C\leftrightarrow L$: esa **dualidad** ahorra la mitad del trabajo. → [[Capacitor]] y [[Inductor]].

> [!teoria] Tres consecuencias que usaremos siempre
> De esas leyes salen los tres hechos que gobiernan los transitorios:
> - **Energía finita ⇒ continuidad.** Cambiar $v_C$ o $i_L$ de golpe exigiría potencia infinita; por eso $v_C$ e $i_L$ son **continuas**: su valor justo antes de conmutar es el valor inicial justo después. → [[Condiciones Iniciales]].
> - **En DC permanente las derivadas se anulan.** Si nada cambia, $dv/dt=0\Rightarrow i_C=0$ (el condensador es un **abierto**) y $di/dt=0\Rightarrow v_L=0$ (el inductor es un **corto**). → [[Circuitos DC en Estado Estable]].
> - **Se asocian en serie y paralelo** como las resistencias… pero **al revés**: los condensadores se combinan como conductancias y los inductores como resistencias. → [[Asociacion de C y L]].

> [!info] Las notas de esta sección
> | Nota | Contenido |
> |:---|:---|
> | [[Capacitor]] | $i=C\,dv/dt$, energía $\tfrac12 Cv^2$, carga $q=Cv$ |
> | [[Inductor]] | $v=L\,di/dt$, energía $\tfrac12 Li^2$, flujo $\phi=Li$ |
> | [[Asociacion de C y L]] | serie y paralelo de condensadores e inductores |
> | [[Condiciones Iniciales]] | continuidad de $v_C$ e $i_L$; valores en $t=0^{\pm}$ |
> | [[Circuitos DC en Estado Estable]] | $C\to$ abierto, $L\to$ corto |

> [!corolario]
> Con dos elementos duales —uno que no deja saltar la tensión, otro que no deja saltar la corriente— el circuito adquiere dinámica. Sus leyes, su energía y sus reglas de continuidad y DC son todo lo que hace falta para plantear y entender cualquier transitorio.

> [!referencia]
> Fraile Mora, cap. 1, §1.5. Siguiente sección: [[Transitorios Primer Orden/index| Transitorios de primer orden]].
