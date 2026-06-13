---
title: Tipo de Sistema
tags:
  - control-clasico
  - analisis
  - error-estacionario
draft: false
aliases:
  - tipo de sistema
  - tipo del sistema
  - número de integradores
  - system type
---

# Tipo de Sistema

> [!definicion]
> El **tipo** $N$ de un sistema es el número de **integradores** (polos en el origen $s=0$) de la ganancia de lazo abierto $L(s)=G(s)H(s)$:
> $$L(s)=\frac{K\,\prod(s+z_i)}{s^{N}\,\prod(s+p_j)},\qquad N=\#\{\text{polos en }s=0\}.$$
> Cada integrador permite seguir **una entrada más** sin error: tipo 0 sigue escalones con error finito; tipo 1 los sigue exactos y deja error fijo en rampa; tipo 2 sigue rampas exactas y deja error en parábola.

> [!info]
> Hija de [[index | Error Estacionario]]. Es el factor más decisivo de $e_{ss}$: junto con el [[Coeficientes Kp Kv Ka | coeficiente de error]] lo fija por completo. Resultado tabulado en [[Tabla Tipos]]; deducción del límite en [[Formula General]].

---

## Ejemplo

> [!ejemplo] Determinar el tipo y leer el seguimiento
> Tres plantas en realimentación unitaria. Clasificar y decir qué entrada sigue cada una con error finito.
>
> | $L(s)$ | Polos en $s=0$ | Tipo | Sigue con error finito |
> |---|---|---|---|
> | $\dfrac{10(s+2)}{(s+1)(s+5)}$ | 0 | **0** | escalón ($e_{ss}=\tfrac{1}{1+K_p}$) |
> | $\dfrac{10(s+2)}{s(s+5)}$ | 1 | **1** | rampa ($e_{ss}=\tfrac{1}{K_v}$); escalón exacto |
> | $\dfrac{10(s+2)}{s^2(s+5)}$ | 2 | **2** | parábola ($e_{ss}=\tfrac{1}{K_a}$); rampa exacta |
>
> **Caso tipo 2 con números.** Para $L(s)=\dfrac{10(s+2)}{s^2(s+5)}$, la ganancia estática tras extraer los $s$:
> $$K_a=\lim_{s\to0}s^2L(s)=\lim_{s\to0}\frac{10(s+2)}{s+5}=\frac{10\cdot2}{5}=4.$$
> Ante parábola $r(t)=t^2/2$: $e_{ss}=1/K_a=1/4=0.25$. Ante rampa y escalón: $0$ (los dos integradores los siguen exactos).

> [!ejemplo] Seguimiento de rampa según el tipo
> ![[error_tipo_sistema.svg|560]]
>
> Tipo 0 no sigue la rampa ($e_{ss}\to\infty$, la salida se queda atrás); tipo 1 la sigue con desfase constante $1/K_v$; tipo 2 la sigue sin error ($e_{ss}=0$).

---

## En qué consiste

> [!teoria]
> Un integrador $1/s$ en $L(s)$ hace que $L\to\infty$ cuando $s\to0$. Como el error en realimentación unitaria es $E=\frac{1}{1+L}R$, ese crecimiento de $L$ aplasta el error de las entradas cuyo $R(s)$ no diverja más rápido. La entrada de prueba de orden $k$ tiene $R(s)=1/s^{k+1}$ (escalón $k=0$, rampa $k=1$, parábola $k=2$): el sistema la sigue con error **nulo** si $N>k$, **finito** si $N=k$, e **infinito** si $N<k$.

> [!teorema] Error estacionario según tipo y entrada
> | Tipo $N$ | Escalón | Rampa | Parábola |
> |---|---|---|---|
> | 0 | $\dfrac{1}{1+K_p}$ | $\infty$ | $\infty$ |
> | 1 | $0$ | $\dfrac{1}{K_v}$ | $\infty$ |
> | 2 | $0$ | $0$ | $\dfrac{1}{K_a}$ |
>
> (Demostración por casos en [[Tabla Tipos]].)

> [!regla] Mnemotecnia
> El sistema sigue con error **nulo** las entradas de orden **menor** que su tipo, con error **finito** la de orden igual, y **no puede** seguir las de orden mayor.

---

## Receta

> [!algoritmo] Contar integradores
> 1. Escribir $L(s)=G(s)H(s)$ en forma factorizada.
> 2. Contar los polos en $s=0$ → ese número es $N$.
> 3. Extraer los $s$ del denominador; la constante restante $K$ define los [[Coeficientes Kp Kv Ka | coeficientes de error]] del tipo correspondiente.
>
> ```matlab
> L = tf(10*[1 2], conv([1 0 0],[1 5]));   % 10(s+2)/(s^2(s+5))
> N = sum(pole(L)==0)                       % tipo: nº de polos en el origen
> Ka = dcgain(minreal(tf([1 0 0],1)*L))     % s^2 L(s) evaluado en s=0
> ```

---

## Subir el tipo

> [!info] La acción integral sube el tipo
> Añadir un [[Integral I | integrador]] (acción I de un [[PID/index | PID]], o un [[Lag | compensador lag]]) **incrementa $N$ en 1**:
> $$G_c(s)=\frac{K_i}{s}\;\Rightarrow\;N\to N+1.$$
> Así un tipo 0 con offset pasa a tipo 1 y anula el error ante escalón.

> [!warning] Coste de subir el tipo
> 1. Cada integrador añade $-90°$ de fase y reduce el [[Margenes MF MG | margen de fase]] → **desestabiliza**.
> 2. No se puede subir el tipo indefinidamente sin comprometer la estabilidad; rara vez se pasa de $N=2$.

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Definición | $N=\#$ polos en $s=0$ de $L(s)=GH$ |
> | Efecto | sigue sin error entradas de orden $<N$ |
> | Tipo 0 | escalón finito, rampa/parábola $\infty$ |
> | Tipo 1 | escalón $0$, rampa finita, parábola $\infty$ |
> | Tipo 2 | escalón/rampa $0$, parábola finita |
> | Subir $N$ | acción integral $K_i/s$ (a costa de fase) |

> [!corolario]
> El tipo es un simple conteo de polos en el origen, pero gobierna por sí solo qué entradas el lazo puede seguir: cada integrador "promueve" el sistema una clase de señal (posición → velocidad → aceleración). La magnitud exacta del error la dan los [[Coeficientes Kp Kv Ka | coeficientes]], y la regla práctica se lee directa en [[Tabla Tipos]].

> [!referencia]
> - Coeficientes de error: [[Coeficientes Kp Kv Ka]].
> - Tabla tipo × entrada: [[Tabla Tipos]].
> - Fórmula del error: [[Formula General]] · [[index | Error Estacionario]].
> - Subir el tipo: [[Integral I]] · [[Lag]] · [[PID/index]].
