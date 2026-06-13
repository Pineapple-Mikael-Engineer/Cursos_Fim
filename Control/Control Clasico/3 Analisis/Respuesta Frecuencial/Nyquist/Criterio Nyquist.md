---
title: Criterio de Nyquist
tags:
  - control-clasico
  - analisis
  - respuesta-frecuencial
  - nyquist
  - estabilidad
draft: false
aliases:
  - criterio de Nyquist
  - Z = N + P
  - estabilidad de Nyquist
---

# Criterio de Nyquist

> [!definicion]
> El **criterio de Nyquist** decide la estabilidad de lazo cerrado contando rodeos del lugar de $L(j\omega)$ al punto $-1+j0$:
> $$Z = N + P,$$
> donde $Z$ = ceros de $1+L$ en el SPD (polos de lazo cerrado inestables), $P$ = polos de $L$ en el SPD (inestables en lazo abierto) y $N$ = rodeos netos del lugar a $-1$ en sentido **horario**. El lazo cerrado es **estable $\iff Z=0$**, es decir $N=-P$.

> [!info]
> Es el resultado central de la subcarpeta [[Nyquist/index | Nyquist]] en [[Respuesta Frecuencial/index | Respuesta Frecuencial]]. Se aplica sobre el [[Diagrama Polar | lugar de Nyquist]]; su lectura cuantitativa son los [[Margenes MF MG | márgenes]]. Equivale algebraicamente a [[Routh Hurwitz/index | Routh-Hurwitz]] pero admite retardos y plantas inestables.

---

## Ejemplo

> [!ejemplo]
> **Conteo de rodeos para $L(s)=\dfrac{K}{s(s+1)(s+2)}$ ($P=0$).** Decidir el rango de $K$ estable.
>
> **Paso 1 — Contar $P$.** Polos de $L$: $s=0,-1,-2$. Ninguno en el SPD abierto, $P=0$. El polo en el origen lo esquiva el contorno con un semicírculo (no cuenta como polo del SPD).
>
> **Paso 2 — Cruce con el eje real.** Del [[Diagrama Polar | lugar polar]], $\operatorname{Im}\{L\}=0$ en $\omega_{pc}=\sqrt2$ rad/s y allí $L=-\dfrac{K}{6}$.
>
> **Paso 3 — Contar $N$ según $K$.**
> - $K<6$: el cruce $-K/6$ cae a la **derecha** de $-1$. La curva **no encierra** $-1$ → $N=0$.
> - $K=6$: el cruce es exactamente $-1$ → la curva **pasa por** el punto crítico (caso límite).
> - $K>6$: el cruce $-K/6$ cae a la **izquierda** de $-1$. La curva (con su conjugado) **rodea** $-1$ dos veces en sentido horario → $N=2$.
>
> **Paso 4 — Aplicar $Z=N+P$.**
> $$K<6:\;Z=0+0=0\Rightarrow\textbf{estable};\qquad K>6:\;Z=2+0=2\Rightarrow\textbf{inestable (2 polos en el SPD)}.$$
>
> **Paso 5 — Verificación cruzada.** $K=6$ es el valor crítico: coincide con el límite de [[Routh Hurwitz/index | Routh-Hurwitz]] y con el [[Lugar Raices/index | cruce del eje imaginario]] del lugar de raíces a $\omega=\sqrt2$ rad/s. Tres métodos, el mismo $K_{\text{crít}}=6$.

> [!ejemplo] Contorno de Nyquist
> ![[nyquist_contorno.svg|500]]
>
> El contorno $\Gamma$ recorre el eje imaginario y se cierra por un semicírculo de radio infinito en el SPD; los polos sobre el eje (origen) se rodean con semicírculos pequeños.

---

## Demostración

> [!teorema] Criterio de estabilidad de Nyquist
> Para el sistema de lazo cerrado con lazo abierto $L(s)=G(s)H(s)$:
> $$Z = N + P,$$
> con $Z,P,N$ como arriba. El lazo cerrado es estable $\iff Z=0$, esto es $N=-P$ ($P$ rodeos en sentido **antihorario** a $-1$).

> [!demostracion] Origen de $Z=N+P$
> **Paso 1 — Principio del argumento.** Al recorrer un contorno cerrado $\Gamma$ en sentido horario, el número de rodeos de $F(\Gamma)$ al origen es $N=Z_\Gamma-P_\Gamma$ (ceros menos polos de $F$ dentro de $\Gamma$).
>
> **Paso 2 — Elegir $F=1+L$ y $\Gamma$ = contorno de Nyquist.** Tomamos $\Gamma$ cubriendo todo el SPD (eje $j\omega$ + semicírculo infinito). Entonces $Z_\Gamma$ = ceros de $1+L$ en el SPD = polos de lazo cerrado inestables = $Z$, y $P_\Gamma$ = polos de $1+L$ en el SPD = polos de $L$ en el SPD = $P$.
>
> **Paso 3 — Trasladar el origen a $-1$.** Los rodeos de $1+L$ al origen son los rodeos de $L$ al punto $-1$ (restar $1$ desplaza el origen a $-1$). Ese conteo es $N$.
>
> **Paso 4 — Despejar.** De $N=Z-P$ resulta $\boxed{Z=N+P}$.

> [!info] Caso común: lazo abierto estable ($P=0$)
> Si $L(s)$ no tiene polos en el SPD, entonces $Z=N$ y la estabilidad exige **cero rodeos** a $-1$: basta verificar que la curva **no encierra** el punto crítico.

---

## Receta

> [!algoritmo] Aplicación del criterio
> 1. Contar $P$ = polos de $L(s)$ en el SPD.
> 2. Trazar el [[Diagrama Polar | diagrama de Nyquist]] completo de $L(j\omega)$.
> 3. Contar $N$ = rodeos netos a $-1$ (horario $+$, antihorario $-$).
> 4. Calcular $Z=N+P$. Estable $\iff Z=0$.

> [!info] Por qué Nyquist
> - Funciona con **lazo abierto inestable** ($P>0$), donde Bode da márgenes ambiguos.
> - Maneja **retardos** $e^{-Ts}$ exactamente (no aproximados).
> - Conecta con la **robustez**: la distancia mínima a $-1$ son los [[Margenes MF MG | márgenes]].

---

## Limitaciones

> [!warning] Polos sobre el eje imaginario
> Si $L$ tiene polos en $j\omega$ (p. ej. integradores en el origen), el contorno los **esquiva** con semicírculos infinitesimales, que generan arcos de radio infinito en el lugar. Hay que incluir esos arcos al contar rodeos, o el criterio falla.

---

## Resumen

> [!resumen]
> | Símbolo | Significado | Cómo se obtiene |
> |---|---|---|
> | $P$ | polos de $L$ en el SPD | factorizar $L(s)$ |
> | $N$ | rodeos netos a $-1$ | contar sobre el Nyquist (horario $+$) |
> | $Z$ | polos de lazo cerrado en SPD | $Z=N+P$ |
> | Estable | — | $\iff Z=0$ ($N=-P$) |

> [!corolario]
> El criterio de Nyquist convierte un problema de raíces de $1+L=0$ en un conteo geométrico de rodeos a $-1$. Con $P=0$ basta que la curva no encierre el punto crítico; con $P>0$ se exigen $P$ rodeos antihorarios. Es el único método clásico exacto para retardos y plantas inestables en lazo abierto, y su lectura métrica son los [[Margenes MF MG | márgenes de fase y ganancia]].

> [!referencia]
> - Trazado de la curva: [[Diagrama Polar]].
> - Robustez como distancia a $-1$: [[Margenes MF MG]].
> - Criterio algebraico equivalente: [[Routh Hurwitz/index]] · [[Estabilidad/index]].
> - Valor crítico de $K$ por otro método: [[Lugar Raices/index]].
