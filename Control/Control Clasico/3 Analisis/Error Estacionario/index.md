---
title: Error Estacionario
tags:
  - control-clasico
  - analisis
  - error-estacionario
draft: false
aliases:
  - error estacionario
  - steady-state error
  - ess
---

# Error Estacionario

> [!definicion]
> El **error estacionario** es lo que sobra del error cuando el transitorio se apaga: $e_{ss}=\lim_{t\to\infty}e(t)$. Se calcula sin resolver la EDO, con el [[Teorema Valor Inicial Final | teorema del valor final]] sobre $E(s)=R(s)-Y(s)$:
> $$e_{ss}=\lim_{s\to0}sE(s).$$
> En realimentación unitaria, $E(s)=\dfrac{1}{1+G(s)}R(s)$ y el resultado depende solo del **tipo** del sistema (integradores) y de la entrada (escalón/rampa/parábola).

> [!info]
> Marco de la carpeta **Error Estacionario** (en [[Estabilidad/index | Análisis]]). Cuatro hijas desarrollan el cálculo:
> - [[Formula General]] — definición $e_{ss}=\lim sE(s)$, lazo abierto/cerrado, error ante **perturbación**.
> - [[Tipo Sistema]] — número de integradores $N$; qué entradas puede seguir.
> - [[Coeficientes Kp Kv Ka]] — $K_p,K_v,K_a$ y su relación con $e_{ss}$.
> - [[Tabla Tipos]] — tabla $e_{ss}$ por tipo × entrada, lista para consultar.
>
> Solo es válido si el [[Estabilidad/index | sistema en lazo cerrado es estable]].

---

## Ejemplo

> [!ejemplo] Un mismo $G(s)$, tres entradas
> Sistema con realimentación unitaria y $G(s)=\dfrac{10}{s(s+2)}$. Hallar $e_{ss}$ ante escalón, rampa y parábola.
>
> **Paso 1 — Tipo.** Hay un polo en $s=0$ → **tipo 1**. Reescribimos para leer la ganancia estática:
> $$G(s)=\frac{10}{s(s+2)}=\frac{1}{s}\cdot\frac{5}{\,s/2+1\,},\qquad G_0(0)=1.$$
>
> **Paso 2 — Coeficientes de error.**
> $$K_p=\lim_{s\to0}G(s)=\infty,\quad K_v=\lim_{s\to0}sG(s)=\frac{10}{2}=5,\quad K_a=\lim_{s\to0}s^2G(s)=0.$$
>
> **Paso 3 — Error por entrada** (con $E(s)=\frac1{1+G}R$ y el TVF):
>
> | Entrada | $R(s)$ | $e_{ss}=\lim_{s\to0}\dfrac{sR(s)}{1+G(s)}$ | Valor |
> |---|---|---|---|
> | escalón $1(t)$ | $1/s$ | $\dfrac{1}{1+K_p}$ | $0$ |
> | rampa $t$ | $1/s^2$ | $\dfrac{1}{K_v}$ | $0.2$ |
> | parábola $t^2/2$ | $1/s^3$ | $\dfrac{1}{K_a}$ | $\infty$ |
>
> **Lectura:** el integrador permite seguir el escalón sin error y la rampa con error fijo $0.2$, pero la parábola crece más rápido de lo que el lazo puede corregir → error infinito. Subir a tipo 2 (un integrador más) volvería finito el error de parábola.

---

## En qué consiste

> [!teoria]
> El error $e(t)=r(t)-y(t)$ tiene dos partes: el **transitorio**, que decae si el sistema es estable, y el **estacionario**, que permanece. El TVF extrae justo el segundo sin resolver $e(t)$. La estructura del lazo fija $E(s)$:
>
> | Configuración | $E(s)=R(s)-Y(s)$ |
> |---|---|
> | Lazo abierto | $[1-G(s)]R(s)$ |
> | Lazo cerrado unitario | $\dfrac{1}{1+G(s)}R(s)$ |
> | Lazo cerrado general | $\dfrac{1+G(s)H(s)-G(s)}{1+G(s)H(s)}R(s)$ |
>
> En el caso unitario, $1/(1+G)$ hace pequeño el error cuando $G$ es grande cerca de $s=0$; por eso los integradores ($G\to\infty$ en $s=0$) anulan el error de entradas de bajo orden.

> [!info] Las tres configuraciones
> Cada fila de la tabla anterior corresponde a una estructura de lazo:
>
> ![[Lazo_abierto.svg|360]]
> $$Y(s)=G(s)\,R(s)\qquad\text{(lazo abierto)}$$
>
> ![[Retroalimentacion_unitario.svg|360]]
> $$Y(s)=\frac{G(s)}{1+G(s)}\,R(s)\qquad\text{(realimentación unitaria)}$$
>
> ![[Retroalimentacion_no_unitario.svg|360]]
> $$Y(s)=\frac{G(s)}{1+G(s)H(s)}\,R(s)\qquad\text{(realimentación no unitaria)}$$

> [!warning] Error en el comparador
> La señal a la entrada de $G$ vale $\dfrac{1}{1+GH}R(s)$. **No** coincide con $R-Y$ salvo si $H=1$. Detalle en [[Formula General]].

---

## Resumen

> [!resumen]
> | Pieza | Resultado |
> |---|---|
> | Definición | $e_{ss}=\lim_{t\to\infty}e(t)=\lim_{s\to0}sE(s)$ |
> | Caso unitario | $E(s)=\dfrac{1}{1+G(s)}R(s)$ |
> | Depende de | tipo $N$ (integradores) y entrada |
> | Coeficientes | $K_p,K_v,K_a$ → [[Coeficientes Kp Kv Ka]] |
> | Tabla lista | [[Tabla Tipos]] |
> | Condición | lazo cerrado **estable** |

> [!corolario]
> Calcular $e_{ss}$ es un límite, no una EDO: se arma $E(s)=R(s)-Y(s)$ según la configuración y se aplica $\lim_{s\to0}sE(s)$. En realimentación unitaria todo se reduce a comparar el **tipo** del sistema con el **orden** de la entrada, lo que se tabula con $K_p,K_v,K_a$. Las cuatro hijas desarrollan cada pieza; la regla práctica vive en [[Tabla Tipos]].

> [!referencia]
> - Cálculo y perturbaciones: [[Formula General]].
> - Integradores y seguimiento: [[Tipo Sistema]].
> - Coeficientes: [[Coeficientes Kp Kv Ka]].
> - Tabla de consulta: [[Tabla Tipos]].
> - Herramienta base: [[Teorema Valor Inicial Final]].
