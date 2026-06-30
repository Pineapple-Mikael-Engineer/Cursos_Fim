---
title: Ziegler-Nichols — Curva de Reacción
order: 2
tags:
  - control-clasico
  - controladores
  - pid
  - sintonizacion
draft: false
aliases:
  - Ziegler-Nichols curva de reacción
  - curva de reacción
  - método de la curva S
  - primer método de Z-N
---

# Ziegler-Nichols: Curva de Reacción

> [!definicion]
> Método de sintonización en **lazo abierto**: se aplica un escalón a la planta, se ajusta su respuesta en S a un **primer orden con retardo** (FOPDT) $G(s)\approx K\,e^{-Ls}/(Ts+1)$, se leen de la tangente en la inflexión el retardo $L$ y la constante $T$, y se calculan $K_p$, $T_i$, $T_d$ con la tabla de Ziegler-Nichols.
> $$\text{PID:}\qquad K_p=1.2\,\frac{T}{KL},\qquad T_i=2L,\qquad T_d=0.5\,L.$$

> [!info]
> Vive en [[Sintonizacion/index | sintonización del PID]], junto a su hermana en lazo cerrado [[Ziegler Nichols Oscilacion | oscilación sostenida]]. Modela la planta como [[Primer Orden | primer orden]] con [[Ganancia Estatica | ganancia estática]] $K$; el retardo $e^{-Ls}$ es de [[Sistemas Fase Minima | fase no mínima]].

---

## Ejemplo

> [!ejemplo]
> **Lectura de la curva y cálculo del PID.** Un horno en lazo abierto recibe un escalón de entrada de $\Delta u = 10\%$ (apertura de válvula). La temperatura sube en S desde $50^\circ$ hasta estabilizarse en $90^\circ$. De la tangente en la inflexión se lee: corte con el eje de tiempo en $t=2\ \text{min}$ y llegada al valor final en $t=12\ \text{min}$. Hallar $K$, $L$, $T$ y sintonizar un PID.
>
> ![[zn_curva_reaccion.svg|600]]
>
> **Paso 1 — Ganancia estática $K$** (cambio de salida / cambio de entrada):
> $$\Delta y = 90-50 = 40^\circ,\qquad K=\frac{\Delta y}{\Delta u}=\frac{40^\circ}{10\%}=4\ \tfrac{^\circ}{\%}.$$
>
> **Paso 2 — Retardo $L$** (corte de la tangente con el eje de tiempo):
> $$L = 2\ \text{min}.$$
>
> **Paso 3 — Constante de tiempo $T$** (de donde la tangente corta el eje hasta que alcanza el valor final):
> $$T = 12 - 2 = 10\ \text{min}.$$
>
> **Paso 4 — Controlabilidad** $\theta=L/T=2/10=0.2$: zona de control PID estándar (ni trivial ni dominado por el retardo).
>
> **Paso 5 — Tabla ZN para PID** ($K_p=1.2\,T/(KL)$, $T_i=2L$, $T_d=0.5L$):
> $$K_p=1.2\cdot\frac{10}{4\cdot 2}=1.2\cdot 1.25=1.5,\qquad T_i=2\cdot 2=4\ \text{min},\qquad T_d=0.5\cdot 2=1\ \text{min}.$$
>
> **Paso 6 — Ganancias en forma paralela** ($K_i=K_p/T_i$, $K_d=K_p T_d$):
> $$K_i=\frac{1.5}{4}=0.375\ \text{min}^{-1},\qquad K_d=1.5\cdot 1=1.5\ \text{min}.$$
> Con un PI en vez de PID saldría $K_p=0.9\,T/(KL)=1.125$ y $T_i=3L=6\ \text{min}$. Estas son ganancias **iniciales**: el sobrepico resultante ($\sim25\%$) casi siempre exige ajuste fino.

---

## En qué consiste

> [!teoria]
> La planta se aproxima por un modelo de **primer orden con tiempo muerto** (FOPDT):
> $$G(s)\approx\frac{K\,e^{-Ls}}{Ts+1},$$
> con $K$ = ganancia estática (cociente de los cambios en régimen permanente), $L$ = retardo o tiempo muerto aparente, $T$ = constante de tiempo aparente. Estos tres parámetros se extraen gráficamente de la respuesta al escalón en lazo abierto, que para un proceso sobreamortiguado tiene **forma de S**. La tangente trazada en el **punto de inflexión** (máxima pendiente) fija $L$ (su corte con el eje de tiempos) y $T$ (su recorrido hasta el valor final).

> [!algoritmo]
> 1. En **lazo abierto**, aplicar un escalón $\Delta u$ a la entrada de la planta.
> 2. Registrar la respuesta; verificar que sea **monótona en S** (sobreamortiguada).
> 3. Trazar la **tangente en el punto de inflexión**.
> 4. Leer $L$ (corte de la tangente con el eje de tiempo) y $T$ (recorrido de la tangente hasta el valor final); calcular $K=\Delta y/\Delta u$.
> 5. Sustituir $K$, $L$, $T$ en la **tabla de Ziegler-Nichols** para obtener $K_p$, $T_i$, $T_d$.

> [!info] Tabla de Ziegler-Nichols (curva de reacción)
> | Controlador | $K_p$ | $T_i$ | $T_d$ |
> |---|---|---|---|
> | P | $T/(K L)$ | $\infty$ | $0$ |
> | PI | $0.9\,T/(K L)$ | $3L$ | $0$ |
> | PID | $1.2\,T/(K L)$ | $2L$ | $0.5\,L$ |
>
> La razón $T/L$ (controlabilidad) fija la ganancia: procesos con poco tiempo muerto ($L\ll T$) admiten $K_p$ alta. Recordar $K_i=K_p/T_i$ y $K_d=K_p T_d$.

> [!info] El parámetro clave $\theta=L/T$
> | $\theta=L/T$ | Dificultad | Recomendación |
> |---|---|---|
> | $<0.1$ | fácil | admite ganancia alta |
> | $0.1$–$0.5$ | media | PID estándar (ZN) |
> | $>0.5$ | dominado por retardo | el PID rinde mal; usar predictor de Smith |
>
> El retardo $e^{-Ls}$ es de [[Sistemas Fase Minima | fase no mínima]]: limita la ganancia y se analiza mejor con [[Criterio Nyquist | Nyquist]].

---

## Limitaciones

> [!warning]
> 1. **Requiere respuesta monótona en S:** no aplica a sistemas oscilatorios ni con integrador (sin valor final).
> 2. **Sensible al ruido:** la inflexión es difícil de localizar, y un error en la tangente propaga error a $L$ y $T$.
> 3. **Sobrepico alto:** apunta a decaimiento de $1/4$ de amplitud, $\sim25\%$ de sobrepico; punto de partida que exige ajuste fino.
> 4. **Ventaja sobre la oscilación:** se hace en lazo abierto, sin llevar el proceso al límite de estabilidad — más seguro. Idóneo para procesos térmicos/químicos lentos.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Ensayo | escalón en **lazo abierto** |
> | Modelo | FOPDT $K\,e^{-Ls}/(Ts+1)$ |
> | Se leen | $K$, $L$, $T$ (de la tangente en la inflexión) |
> | PID | $K_p=1.2\,T/(KL)$, $T_i=2L$, $T_d=0.5L$ |
> | Controlabilidad | $\theta=L/T$ |
> | Precisión | baja-media (sobrepico $\sim25\%$) |

> [!corolario]
> El método transforma una sola curva de respuesta al escalón en un PID completo: ajustar la planta a un FOPDT, leer $K$, $L$, $T$ de la tangente y aplicar la tabla. Es la opción **segura** (lazo abierto) frente a la [[Ziegler Nichols Oscilacion | oscilación sostenida]], pero comparte su defecto de sobrepico elevado y solo sirve cuando la respuesta es una S limpia.

> [!referencia]
> - Método alternativo en lazo cerrado: [[Ziegler Nichols Oscilacion]].
> - Modelo FOPDT y ganancia estática: [[Ganancia Estatica]] · [[Primer Orden]].
> - Retardo y fase no mínima: [[Sistemas Fase Minima]] · [[Criterio Nyquist]].
> - Marco y ajuste posterior: [[Sintonizacion/index]] · [[PID]].
