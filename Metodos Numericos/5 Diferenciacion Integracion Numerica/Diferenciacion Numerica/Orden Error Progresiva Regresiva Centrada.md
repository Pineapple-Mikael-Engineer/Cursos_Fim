---
title: Orden de Error — Progresiva, Regresiva y Centrada
tags:
  - metodos-numericos
  - teoria
  - diferenciacion-integracion
  - diferenciacion-numerica
  - error-numerico
draft: false
aliases:
  - Orden de error de diferencias finitas
  - Progresiva regresiva centrada
  - Forward backward central difference
---

# Orden de Error: Progresiva, Regresiva y Centrada

> [!definicion]
> El **orden de error de truncamiento** de una fórmula de [[Aproximacion Diferencias Finitas Serie Taylor|diferencias finitas]] es la potencia $p$ tal que el error es $O(h^p)$. Mide cuán rápido converge la aproximación a la derivada exacta al reducir el paso $h$.

> [!info]
> Las fórmulas **asimétricas** (progresiva, regresiva) tienen orden $O(h)$; la **centrada** tiene orden $O(h^2)$ por cancelación de simetría. El orden determina cuánto baja el error al halvar $h$ (factor $2$ para $O(h)$, factor $4$ para $O(h^2)$).

---

## Las tres fórmulas de primera derivada

> [!teorema]
> Con el término de error explícito de Taylor:
> $$\text{Progresiva: } f'(x) = \frac{f(x+h)-f(x)}{h} - \frac{h}{2}f''(\xi),$$
> $$\text{Regresiva: } f'(x) = \frac{f(x)-f(x-h)}{h} + \frac{h}{2}f''(\xi),$$
> $$\text{Centrada: } f'(x) = \frac{f(x+h)-f(x-h)}{2h} - \frac{h^2}{6}f'''(\xi).$$

> [!demostracion]
> **Progresiva.** De $f(x+h) = f(x) + hf'(x) + \tfrac{h^2}{2}f''(\xi)$, despejando:
> $$\frac{f(x+h)-f(x)}{h} = f'(x) + \tfrac{h}{2}f''(\xi),$$
> error $O(h)$. **Centrada.** El término en $f''$ aparece con signo **opuesto** en $f(x+h)$ y $f(x-h)$; al restar se cancela, quedando el de $f'''$ dividido por $2h$, error $O(h^2)$.

---

## Por qué la centrada es mejor

> [!teoria]
> En una fórmula simétrica, los desarrollos de $f(x+h)$ y $f(x-h)$ contienen $f''(x)$ con el **mismo** signo (se cancela al restar) y $f'''(x)$ con signos opuestos. El resultado: todos los términos de orden **par** desaparecen, y la fórmula gana un orden "gratis" usando el mismo número de puntos efectivos. Es el principio general: **la simetría duplica el orden**.

---

## Ejemplo: verificación del orden

> [!ejemplo]
> **$f(x)=\sin x$ en $x=1$ ($f'(1)=\cos 1 \approx 0.540302$).** Error al halvar $h$:
>
> | $h$ | Error progresiva | factor | Error centrada | factor |
> |:---:|:---:|:---:|:---:|:---:|
> | $0.1$ | $4.2\times10^{-2}$ | — | $9.0\times10^{-4}$ | — |
> | $0.05$ | $2.1\times10^{-2}$ | 2.0 | $2.3\times10^{-4}$ | 4.0 |
> | $0.025$ | $1.05\times10^{-2}$ | 2.0 | $5.6\times10^{-5}$ | 4.0 |
>
> El error de la progresiva se halva (factor $2$, orden $1$); el de la centrada se cuartea (factor $4$, orden $2$). Confirma $O(h)$ y $O(h^2)$.

---

## Verificación empírica del orden

> [!info]
> El orden $p$ se estima del cociente de errores al halvar $h$:
> $$p \approx \log_2\frac{E(h)}{E(h/2)}.$$
> Factor $2 \Rightarrow p=1$; factor $4 \Rightarrow p=2$; factor $16 \Rightarrow p=4$. Es la prueba estándar para validar la implementación de un esquema.

> [!warning]
> El orden es **asintótico** ($h\to0$) y supone aritmética exacta. Para $h$ muy pequeño, el [[Inestabilidad Error Redondeo Paso h|redondeo]] rompe la tendencia y el error deja de seguir $O(h^p)$.

---

## Fórmulas de mayor orden

> [!info]
> | Fórmula | Orden | Puntos |
> |:---|:---:|:---:|
> | Progresiva/regresiva | $O(h)$ | 2 |
> | Centrada | $O(h^2)$ | 2 (simétricos) |
> | Progresiva de 3 puntos | $O(h^2)$ | 3 |
> | Centrada de 5 puntos | $O(h^4)$ | 4 |
>
> Las asimétricas de mayor orden son útiles en los **bordes** del dominio, donde no hay puntos a ambos lados (condiciones de frontera).

---

## Relación con otras notas

> [!info]
> - La deducción por Taylor de cada fórmula: [[Aproximacion Diferencias Finitas Serie Taylor]].
> - Cómo elevar el orden combinando pasos: [[Extrapolacion Richardson Aceleracion Convergencia]].
> - El límite del orden por redondeo: [[Inestabilidad Error Redondeo Paso h]].
> - El mismo concepto de orden en integración: [[Trapecio Compuesto Convergencia O h2]].

---

## Resumen

| Fórmula | Error | Orden |
|:---|:---|:---:|
| Progresiva | $-\frac{h}{2}f''$ | 1 |
| Regresiva | $+\frac{h}{2}f''$ | 1 |
| Centrada | $-\frac{h^2}{6}f'''$ | 2 |
| Verificación | $p \approx \log_2(E(h)/E(h/2))$ | — |

> [!corolario]
> El orden de error mide la potencia de $h$ en el truncamiento: las fórmulas asimétricas (progresiva, regresiva) son $O(h)$ y la centrada $O(h^2)$, porque su simetría cancela los términos de orden par del desarrollo de Taylor. Empíricamente, halvar $h$ reduce el error por $2^p$, lo que permite verificar el orden con $p \approx \log_2(E(h)/E(h/2))$. Esta jerarquía solo vale en el régimen asintótico: el [[Inestabilidad Error Redondeo Paso h|redondeo]] la rompe para $h$ muy pequeño, y la [[Extrapolacion Richardson Aceleracion Convergencia|extrapolación de Richardson]] permite ascender de orden sistemáticamente.
