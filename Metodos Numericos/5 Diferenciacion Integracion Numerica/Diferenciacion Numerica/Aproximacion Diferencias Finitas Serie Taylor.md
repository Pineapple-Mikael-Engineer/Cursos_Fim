---
title: Aproximación por Diferencias Finitas y Serie de Taylor
tags:
  - metodos-numericos
  - teoria
  - diferenciacion-integracion
  - diferenciacion-numerica
draft: false
aliases:
  - Diferencias finitas
  - Deducción por Taylor
  - Finite differences
---

# Aproximación por Diferencias Finitas (Serie de Taylor)

> [!definicion]
> Una **fórmula de diferencias finitas** aproxima una derivada como combinación lineal de valores de $f$ en nodos equiespaciados de paso $h$. Se deduce de la **serie de Taylor**, que también proporciona el término de error.

> [!info]
> La serie de Taylor es el motor unificado: imponiendo qué derivada se quiere y qué términos se cancelan, se determinan los coeficientes y el [[Orden Error Progresiva Regresiva Centrada|orden]] de la fórmula. El mismo método genera esquemas de cualquier orden y para cualquier derivada.

---

## Deducción de la primera derivada

> [!teorema]
> Desarrollando $f(x\pm h)$ por Taylor:
> $$f(x+h) = f(x) + hf'(x) + \tfrac{h^2}{2}f''(x) + \tfrac{h^3}{6}f'''(x) + \cdots$$
> Se obtienen tres aproximaciones de $f'(x)$:
> $$\text{progresiva: } \frac{f(x+h)-f(x)}{h} = f'(x) + O(h),$$
> $$\text{regresiva: } \frac{f(x)-f(x-h)}{h} = f'(x) + O(h),$$
> $$\text{centrada: } \frac{f(x+h)-f(x-h)}{2h} = f'(x) + O(h^2).$$

> [!demostracion]
> **Centrada.** Restando los desarrollos de $f(x+h)$ y $f(x-h)$:
> $$f(x+h) - f(x-h) = 2hf'(x) + \tfrac{2h^3}{6}f'''(x) + O(h^5).$$
> Dividiendo entre $2h$:
> $$\frac{f(x+h)-f(x-h)}{2h} = f'(x) + \tfrac{h^2}{6}f'''(\xi).$$
> Los términos de orden par en $h$ se **cancelan** por la simetría, dejando error $O(h^2)$ — una potencia más que las fórmulas asimétricas.

---

## Segunda derivada

> [!teorema]
> **Sumando** los desarrollos de $f(x\pm h)$:
> $$\frac{f(x+h) - 2f(x) + f(x-h)}{h^2} = f''(x) + \tfrac{h^2}{12}f^{(4)}(\xi) = f''(x) + O(h^2).$$
> Es la fórmula centrada de segunda derivada, base del [[Construccion Sistema Tridiagonal Lineal|método de diferencias finitas para EDOs/EDPs]].

---

## Método de coeficientes indeterminados

> [!teoria]
> Para una fórmula general $f^{(d)}(x) \approx \frac{1}{h^d}\sum_k a_k f(x + k h)$ sobre un conjunto de nodos $\{k h\}$:
> 1. Desarrollar cada $f(x+kh)$ por Taylor.
> 2. Imponer que el coeficiente de $f^{(d)}$ sea $1$ y los de las demás derivadas (hasta el orden deseado) sean $0$.
> 3. Resolver el sistema lineal para los $a_k$.
>
> El número de nodos determina el orden alcanzable; el primer término no cancelado da el error.

---

## Ejemplo: tabla de fórmulas

> [!ejemplo]
> **Fórmulas comunes (paso $h$):**
>
> | Derivada | Fórmula | Error |
> |:---|:---|:---:|
> | $f'$ progresiva | $\frac{f(x+h)-f(x)}{h}$ | $O(h)$ |
> | $f'$ centrada | $\frac{f(x+h)-f(x-h)}{2h}$ | $O(h^2)$ |
> | $f'$ centrada 4 puntos | $\frac{-f(x+2h)+8f(x+h)-8f(x-h)+f(x-2h)}{12h}$ | $O(h^4)$ |
> | $f''$ centrada | $\frac{f(x+h)-2f(x)+f(x-h)}{h^2}$ | $O(h^2)$ |
>
> Más puntos → mayor orden, a costa de más evaluaciones y mayor sensibilidad al [[Inestabilidad Error Redondeo Paso h|redondeo]].

---

## Relación con la interpolación

> [!info]
> Las diferencias finitas equivalen a derivar el [[Newton Diferencias Divididas/index|polinomio interpolante]]: la fórmula de orden $p$ es la derivada del interpolante en $p+1$ nodos. Las [[Relacion Diferencias Divididas Derivadas|diferencias divididas]] son la versión no equiespaciada, $f[x_0,x_1] \approx f'$.

---

## Relación con otras notas

> [!info]
> - El orden de cada esquema y su comparación: [[Orden Error Progresiva Regresiva Centrada]].
> - Cómo subir el orden combinando pasos: [[Extrapolacion Richardson Aceleracion Convergencia]].
> - El límite práctico al reducir $h$: [[Inestabilidad Error Redondeo Paso h]].
> - La conexión con interpolación: [[Relacion Diferencias Divididas Derivadas]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Origen | serie de Taylor |
| Progresiva/regresiva | $O(h)$ |
| Centrada (1.ª deriv.) | $O(h^2)$ |
| Centrada (2.ª deriv.) | $\frac{f(x+h)-2f(x)+f(x-h)}{h^2}$, $O(h^2)$ |
| General | coeficientes indeterminados |

> [!corolario]
> Las fórmulas de diferencias finitas se deducen de la serie de Taylor: combinando desarrollos de $f$ en nodos vecinos se aíslan derivadas y se lee el término de error. La simetría de la fórmula centrada cancela los términos de orden par, dándole orden $O(h^2)$ frente al $O(h)$ de las asimétricas. El método de coeficientes indeterminados generaliza la construcción a cualquier derivada y orden. Equivalen a derivar el [[Newton Diferencias Divididas/index|interpolante]], y su [[Orden Error Progresiva Regresiva Centrada|orden]] y [[Inestabilidad Error Redondeo Paso h|estabilidad]] determinan su utilidad práctica.
