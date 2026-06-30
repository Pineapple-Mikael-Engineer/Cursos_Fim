---
title: Teoremas del Valor Inicial y Final
order: 5
tags:
  - control-clasico
  - teoria
  - analisis
draft: false
aliases:
  - TVI
  - TVF
  - valor final
  - valor inicial
---

# Teoremas del Valor Inicial y Final

> [!definicion]
> Dos teoremas leen el comportamiento de $f(t)$ en los extremos del tiempo desde su transformada $F(s)$, sin antitransformar:
> $$\text{TVI: }\ f(0^+)=\lim_{s\to\infty}sF(s),\qquad\text{TVF: }\ \lim_{t\to\infty}f(t)=\lim_{s\to0}sF(s).$$
> El **TVF** exige que todos los polos de $sF(s)$ tengan $\Re<0$ (salvo, a lo sumo, un polo simple en $s=0$); el **TVI** no requiere condiciones de estabilidad.

> [!info]
> Son la herramienta para extraer valores de régimen de la [[Funcion Transferencia/index | función de transferencia]]. El TVF sustenta la [[Ganancia Estatica | ganancia estática]] ($y(\infty)=G(0)$ a escalón) y el cálculo del [[Error Estacionario/index | error estacionario]] $e_{ss}=\lim_{s\to0}sE(s)$.

---

## Ejemplo

> [!ejemplo] TVF de un sistema estable de primer orden
> $$F(s)=\frac{2}{s+1}\cdot\frac1s=\frac{2}{s(s+1)}.$$
> **Paso 1 — Verificar hipótesis:** $sF(s)=\dfrac{2}{s+1}$ tiene su único polo en $s=-1$ ($\Re<0$). TVF aplicable. **Paso 2 — Tomar el límite:**
> $$\lim_{t\to\infty}f(t)=\lim_{s\to0}\frac{2}{s+1}=2.$$
> **Verificación:** $f(t)=2(1-e^{-t})\to 2$. ✓

> [!ejemplo] TVI con discontinuidad inicial
> $$F(s)=\frac{2}{s+1}.$$
> $$f(0^+)=\lim_{s\to\infty}s\cdot\frac{2}{s+1}=\lim_{s\to\infty}\frac{2s}{s+1}=2.$$
> **Verificación:** $f(t)=2e^{-t}$, $f(0^+)=2$. ✓

> [!ejemplo] Error estacionario a escalón (uso típico en control)
> Lazo con error $E(s)=\dfrac{1}{1+G(s)}\cdot\dfrac1s$ (escalón). Si el lazo cerrado es estable:
> $$e_{ss}=\lim_{s\to0}sE(s)=\lim_{s\to0}\frac{1}{1+G(s)}=\frac{1}{1+G(0)}.$$
> Para $G(s)=\dfrac{10}{s+2}$: $G(0)=5$ y $e_{ss}=\dfrac{1}{1+5}=\dfrac16\approx0.167$.

> [!ejemplo] TVI de una función con salto (pulso)
> $$F(s)=\frac{1-e^{-sT}}{s}\implies f(0^+)=\lim_{s\to\infty}(1-e^{-sT})=1.$$
> Es un pulso de altura 1 y duración $T$: arranca en 1. ✓

---

## Demostración del TVF

> [!teorema]
> Bajo las hipótesis enunciadas, $\lim_{t\to\infty}f(t)=\lim_{s\to0}sF(s)$.

> [!demostracion]
> **Paso 1 — Laplace de la derivada:**
> $$\int_0^\infty \dot f(t)\,e^{-st}\,dt=sF(s)-f(0^-).$$
> **Paso 2 — Límite $s\to0$:**
> $$\lim_{s\to0}\int_0^\infty\dot f\,e^{-st}\,dt=\lim_{s\to0}[sF(s)-f(0^-)].$$
> **Paso 3 — Intercambiar límite e integral** (convergencia garantizada por las hipótesis):
> $$\int_0^\infty\dot f\,dt=\lim_{t\to\infty}f(t)-f(0^-).$$
> **Paso 4 — Igualar:** $\lim_{t\to\infty}f(t)-f(0^-)=\lim_{s\to0}sF(s)-f(0^-)$. **Paso 5 — Cancelar $f(0^-)$:** $\displaystyle\lim_{t\to\infty}f(t)=\lim_{s\to0}sF(s).\ \blacksquare$

---

## Demostración del TVI

> [!teorema]
> $$f(0^+)=\lim_{s\to\infty}sF(s).$$

> [!demostracion]
> **Paso 1 — Misma identidad:** $\int_0^\infty\dot f\,e^{-st}\,dt=sF(s)-f(0^-)$. **Paso 2 — Límite $s\to\infty$:** como $e^{-st}\to0$ para todo $t>0$, la integral $\to0$. **Paso 3 — Por tanto** $0=\lim_{s\to\infty}sF(s)-f(0^-)$. **Paso 4 — Con $f(0^-)=f(0^+)$** (sin impulso en el origen): $f(0^+)=\lim_{s\to\infty}sF(s).\ \blacksquare$

---

## Cuándo NO aplicar

> [!warning] TVF
> No aplicar si $sF(s)$ tiene algún polo con $\Re\ge0$ distinto de un polo simple en $s=0$ (sistema inestable o con oscilación sostenida).
>
> | $F(s)$ | $f(t)$ | TVF daría | Real |
> |---|---|---|---|
> | $\dfrac{1}{s^2-1}$ vía $\dfrac{1}{s(s-1)}$ | $e^{t}$ | $0$ | $\infty$ (inválido) |
> | $\dfrac{1}{s^2+1}$ | $\sin t$ | $0$ | no existe (inválido) |
> | $\dfrac{1}{s^2}$ | $t$ | $\infty$ | $\infty$ (válido, polo simple en 0) |

> [!warning] TVI
> El límite $\lim_{s\to\infty}sF(s)$ debe existir. Si $f(t)$ contiene un impulso en $t=0$, el TVI devuelve el área del impulso, no el valor de la parte regular.

---

## Resumen

> [!resumen]
> | Teorema | Fórmula | Hipótesis |
> |---|---|---|
> | TVI | $f(0^+)=\lim_{s\to\infty}sF(s)$ | el límite existe |
> | TVF | $\lim_{t\to\infty}f(t)=\lim_{s\to0}sF(s)$ | polos de $sF(s)$ con $\Re<0$ (salvo simple en 0) |
> | Uso TVF | $y(\infty)=G(0)$, $e_{ss}=\lim_{s\to0}sE(s)$ | lazo estable |

> [!corolario]
> El TVF lee el régimen permanente y el TVI el arranque, ambos directamente desde $F(s)$. Su valor práctico en control es calcular ganancias estáticas y errores estacionarios sin resolver la EDO, pero el TVF **solo es lícito si el sistema es estable**: aplicarlo a un sistema oscilante o divergente da resultados falsos.

> [!referencia]
> - Aplicación a valor final: [[Ganancia Estatica]].
> - Cálculo de error: [[Error Estacionario/index]].
> - Marco general: [[Funcion Transferencia/index]].
