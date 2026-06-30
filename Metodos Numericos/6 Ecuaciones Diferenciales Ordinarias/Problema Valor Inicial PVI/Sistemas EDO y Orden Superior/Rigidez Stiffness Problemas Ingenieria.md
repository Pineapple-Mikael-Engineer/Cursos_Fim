---
title: Rigidez (Stiffness) en Problemas de Ingeniería
order: 3
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-inicial
  - estabilidad
  - rigidez
draft: false
aliases:
  - Rigidez
  - Stiffness
  - Sistemas rígidos
  - Problemas stiff
---

# Rigidez (Stiffness) en Problemas de Ingeniería

> [!definicion]
> Un sistema de EDOs es **rígido** (*stiff*) cuando contiene **escalas de tiempo muy dispares**: componentes que decaen rapidísimo coexisten con otras lentas. Formalmente, la [[Acoplamiento Metodos Sistemas Runge Kutta|jacobiana]] $J = \partial\mathbf f/\partial\mathbf y$ tiene autovalores con $\operatorname{Re}(\lambda_i)<0$ de magnitudes muy distintas, con **razón de rigidez** $\frac{\max|\operatorname{Re}\lambda_i|}{\min|\operatorname{Re}\lambda_i|} \gg 1$.

> [!info]
> En sistemas rígidos, los métodos explícitos se ven forzados a pasos minúsculos por **estabilidad** —no por precisión—, volviéndose inviables aunque la solución sea suave. La rigidez **obliga** a métodos implícitos [[Euler Implicito Estabilidad Incondicional|A-estables]]. Es omnipresente en cinética química, circuitos y problemas de capa límite.

---

## El síntoma de la rigidez

> [!teoria]
> Tras un transitorio rápido (las componentes veloces decaen y desaparecen), la solución es **suave** y un paso grande bastaría para la precisión. Pero un método explícito debe mantener $h$ pequeño para que $h\lambda_{\text{rápido}}$ permanezca en su [[Regiones Estabilidad Absoluta A Estabilidad|región de estabilidad]], **aunque** esa componente rápida ya valga cero. La estabilidad, no la precisión, dicta el paso.

> [!warning]
> **La paradoja:** integrar una solución lisa con un método explícito puede requerir millones de pasos, no porque la solución lo exija, sino porque el método explotaría con pasos grandes. Es contraintuitivo: el problema "fácil" (suave) es numéricamente "difícil".

---

## Ejemplo: cinética química

> [!ejemplo]
> **Reacción con escalas dispares:**
> $$\dot y_1 = -1000\,y_1 + y_2, \qquad \dot y_2 = -y_2.$$
> Autovalores de la jacobiana: $\lambda_1 = -1000$ (rápido), $\lambda_2 = -1$ (lento). Razón de rigidez $1000$.
>
> | Método | Paso $h$ necesario | Pasos hasta $t=10$ |
> |:---|:---:|:---:|
> | [[RK4 Clasico Tabla Butcher y Orden Cuatro\|RK4]] (explícito) | $h \lesssim 2.78/1000 \approx 0.0028$ | $\sim3600$ |
> | [[Euler Implicito Estabilidad Incondicional\|Euler implícito]] | $h \sim 0.1$ (por precisión) | $\sim100$ |
>
> Tras $t\approx0.005$, la componente rápida $\sim e^{-1000t}$ es despreciable y la solución es lisa, pero RK4 sigue atado a $h<0.0028$. Euler implícito (A-estable) usa pasos $30\times$ mayores.

---

## La solución: métodos implícitos

> [!info]
> Los métodos para problemas rígidos comparten la [[Euler Implicito Estabilidad Incondicional|A-estabilidad]] (región que cubre todo el semiplano izquierdo):
>
> | Método | Tipo | Orden | A-estable |
> |:---|:---|:---:|:---:|
> | Euler implícito | implícito | 1 | sí |
> | Trapezoidal (Crank-Nicolson) | implícito | 2 | sí |
> | **BDF** (Gear) | multipaso implícito | 1–6 | hasta orden 2 (A), más (A($\alpha$)) |
> | RK implícito (Radau) | implícito | hasta $2s-1$ | sí (L-estable) |
>
> El precio: cada paso resuelve un sistema (lineal o no) con la [[Newton Raphson Multivariable/index|jacobiana]], pero los pasos grandes compensan con creces.

---

## Detección y software

> [!info]
> - **Detección:** estimar la razón de rigidez por los autovalores de $J$, o detectar que un integrador explícito reduce drásticamente $h$ sin que la solución lo justifique.
> - **Software:** `scipy.integrate.solve_ivp(method='BDF')` o `'Radau'` para problemas rígidos; `'LSODA'` cambia automáticamente entre explícito e implícito según detecte rigidez.

> [!algoritmo]
> **Integración de un sistema rígido.**
>
> ```python
> from scipy.integrate import solve_ivp
>
> def rigido(t, y):
>     return [-1000*y[0] + y[1], -y[1]]
>
> # BDF: implícito, idóneo para rigidez
> sol = solve_ivp(rigido, [0, 10], [1.0, 1.0],
>                 method='BDF', rtol=1e-6, atol=1e-9)
> ```

---

## Relación con otras notas

> [!info]
> - El método A-estable básico: [[Euler Implicito Estabilidad Incondicional]].
> - El concepto de región de estabilidad: [[Regiones Estabilidad Absoluta A Estabilidad]].
> - La jacobiana cuyos autovalores definen la rigidez: [[Acoplamiento Metodos Sistemas Runge Kutta]].
> - El Newton interno de los implícitos: [[Newton Raphson Multivariable/index]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Definición | autovalores de $J$ de magnitudes muy dispares |
| Razón de rigidez | $\max|\operatorname{Re}\lambda|/\min|\operatorname{Re}\lambda| \gg 1$ |
| Síntoma | explícitos atados a $h$ minúsculo por estabilidad |
| Solución | métodos implícitos A-estables (BDF, Radau) |
| Costo | sistema por paso (Newton + jacobiana) |
| Software | `BDF`, `Radau`, `LSODA` |

> [!corolario]
> Un sistema es rígido cuando su jacobiana tiene autovalores de magnitudes muy dispares: las componentes rápidas, aunque ya decaídas, obligan a los métodos explícitos a pasos minúsculos por [[Regiones Estabilidad Absoluta A Estabilidad|estabilidad]], no por precisión. La cura son los métodos implícitos [[Euler Implicito Estabilidad Incondicional|A-estables]] (BDF, Radau), que usan pasos grandes a costa de resolver un sistema con la [[Newton Raphson Multivariable/index|jacobiana]] en cada paso. La rigidez es ubicua en ingeniería —cinética química, circuitos, capas límite— y reconocerla es esencial: usar un método explícito en un problema rígido es el error más común y costoso de la simulación.
