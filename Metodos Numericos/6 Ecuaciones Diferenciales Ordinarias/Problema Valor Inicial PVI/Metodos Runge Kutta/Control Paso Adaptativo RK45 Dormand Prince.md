---
title: Control de Paso Adaptativo — RK45 y Dormand-Prince
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-inicial
  - runge-kutta
draft: false
aliases:
  - RK45
  - Paso adaptativo
  - Dormand-Prince
  - Runge-Kutta-Fehlberg
  - Adaptive step size
---

# Control de Paso Adaptativo: RK45 y Dormand-Prince

> [!definicion]
> El **control de paso adaptativo** ajusta automáticamente $h$ en cada paso para mantener el error local bajo una tolerancia. Los métodos **RK45** (pares encajados) calculan dos aproximaciones de órdenes $4$ y $5$ con las **mismas** evaluaciones de $f$, y su diferencia **estima el error**.

> [!info]
> Es la forma en que se integran EDOs en la práctica (`scipy.integrate.solve_ivp`, `ode45` de MATLAB). El paso se reduce donde la solución varía rápido y se agranda donde es suave, logrando precisión uniforme con mínimo costo — esencial para sistemas físicos con escalas de tiempo cambiantes (un cometa acelerando en el perihelio, una reacción que se dispara).

---

## Pares encajados

> [!teorema]
> Un **par encajado** comparte las etapas $k_i$ pero tiene **dos** conjuntos de pesos, $b_i$ (orden $p$) y $\hat b_i$ (orden $p+1$):
> $$y_{n+1} = y_n + h\sum_i b_i k_i \ (\text{orden } p), \qquad \hat y_{n+1} = y_n + h\sum_i \hat b_i k_i \ (\text{orden } p+1).$$
> El **error local estimado** es
> $$\text{err}_n = \|\hat y_{n+1} - y_{n+1}\| \approx C\,h^{p+1}.$$

> [!info]
> La clave de la eficiencia: ambas soluciones usan las **mismas** $k_i$, así que estimar el error es casi gratis (solo una combinación lineal extra). Fehlberg (RKF45) y **Dormand-Prince** (DP, el de `ode45`) son los pares más usados; DP usa 7 etapas con la propiedad FSAL (la última etapa se reutiliza como primera del paso siguiente).

---

## Algoritmo de control

> [!algoritmo]
> **Ajuste del paso por tolerancia.**
>
> ```
> en cada paso:
>     calcular k_i, y_{n+1} (orden p) y ŷ_{n+1} (orden p+1)
>     err = ||ŷ_{n+1} - y_{n+1}||
>     tol = atol + rtol * ||y_n||              # tolerancia mixta abs/rel
>     factor = (tol / err)^(1/(p+1))           # paso ideal
>     si err <= tol:
>         aceptar el paso; y_n ← y_{n+1}; t ← t + h
>     h ← h * min(facmax, max(facmin, 0.9 * factor))   # nuevo paso (con seguridad)
> ```
>
> El factor $0.9$ es de seguridad; `facmin`/`facmax` limitan cambios bruscos. Si el paso se rechaza ($\text{err}>\text{tol}$), se reintenta con $h$ menor sin avanzar.

> [!teoria]
> **Por qué el exponente $1/(p+1)$.** Como $\text{err}\approx C h^{p+1}$, para alcanzar $\text{err}_{\text{nuevo}} = \text{tol}$ con $\text{err}_{\text{nuevo}} = C h_{\text{nuevo}}^{p+1}$ se despeja $h_{\text{nuevo}} = h\,(\text{tol}/\text{err})^{1/(p+1)}$. El control predice el paso que justo cumple la tolerancia.

---

## Ejemplo

> [!ejemplo]
> **Órbita muy excéntrica (cometa).** La velocidad varía enormemente entre el afelio (lento) y el perihelio (rápido). Un integrador adaptativo:
>
> | Región de la órbita | Paso $h$ elegido | Razón |
> |:---|:---:|:---|
> | Afelio (lejos, lento) | grande | solución suave |
> | Perihelio (cerca, rápido) | pequeño | curvatura alta |
>
> Con paso fijo habría que usar el $h$ del perihelio **en toda** la órbita (derroche) o perder precisión en el perihelio. El adaptativo concentra el esfuerzo donde hace falta, reduciendo el número de pasos en órdenes de magnitud.

---

## Uso práctico

> [!algoritmo]
> **Integración adaptativa con SciPy.**
>
> ```python
> from scipy.integrate import solve_ivp
> import numpy as np
>
> # Sistema de Van der Pol (oscilador no lineal)
> def vdp(t, y, mu=5.0):
>     return [y[1], mu*(1 - y[0]**2)*y[1] - y[0]]
>
> sol = solve_ivp(vdp, [0, 30], [2.0, 0.0],
>                 method='RK45', rtol=1e-8, atol=1e-10,
>                 dense_output=True)
> # sol.t tiene pasos NO uniformes: densos donde y varía rápido
> ```

---

## Limitaciones

> [!warning]
> - **Problemas rígidos:** RK45 (explícito) reduce $h$ por **estabilidad**, no por precisión, volviéndose lentísimo. Para rigidez se usan métodos implícitos (`method='Radau'`, `'BDF'`). Ver [[Rigidez Stiffness Problemas Ingenieria]].
> - **Tolerancia engañosa:** controla el error **local**, no el global; en horizontes largos el error global puede exceder la tolerancia.
> - **Conservación:** los métodos adaptativos no preservan invariantes; para mecánica de largo plazo, [[Integradores Simplecticos Conservacion|simplécticos]].

---

## Relación con otras notas

> [!info]
> - El método base de orden fijo: [[RK4 Clasico Tabla Butcher y Orden Cuatro]].
> - La estructura de la tabla de Butcher encajada: [[Construccion General Etapas s y Orden p]].
> - Cuándo el control de paso falla (rigidez): [[Rigidez Stiffness Problemas Ingenieria]] y [[Regiones Estabilidad Absoluta A Estabilidad]].
> - El error local que se estima: [[Error Local Truncamiento vs Error Global Acumulado]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Idea | par de órdenes $p$ y $p+1$, mismas etapas |
| Estimación de error | $\|\hat y - y\| \approx Ch^{p+1}$ |
| Nuevo paso | $h\,(\text{tol}/\text{err})^{1/(p+1)}$ |
| Ejemplos | RKF45, Dormand-Prince (`ode45`) |
| Ventaja | precisión uniforme, mínimo costo |
| Falla en | rigidez, conservación, error global |

> [!corolario]
> El control de paso adaptativo calcula dos soluciones encajadas de órdenes $p$ y $p+1$ con las mismas etapas, usa su diferencia para estimar el error local y ajusta $h \leftarrow h(\text{tol}/\text{err})^{1/(p+1)}$ para mantenerlo bajo tolerancia. Métodos como Dormand-Prince (el `ode45`) concentran el esfuerzo donde la solución varía rápido —indispensable para órbitas excéntricas u osciladores no lineales— y son el estándar de las rutinas de integración. No resuelven, sin embargo, la [[Rigidez Stiffness Problemas Ingenieria|rigidez]] (donde manda la [[Regiones Estabilidad Absoluta A Estabilidad|estabilidad]]) ni la [[Integradores Simplecticos Conservacion|conservación]] de invariantes.
