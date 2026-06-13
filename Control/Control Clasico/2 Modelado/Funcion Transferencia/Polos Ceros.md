---
title: Polos y Ceros
tags:
  - control-clasico
  - teoria
  - analisis
draft: false
aliases:
  - polos
  - ceros
  - modos naturales
---

# Polos y Ceros

> [!definicion]
> Para $G(s)=N(s)/D(s)$: los **polos** son las raíces $p_i$ del denominador ($D(p_i)=0$, $G\to\infty$) y los **ceros** las raíces $z_i$ del numerador ($N(z_i)=0$, $G\to 0$). Cada polo aporta un **modo natural** $\propto e^{p_i t}$ a la respuesta; los ceros modulan con qué peso aparece cada modo en la salida.

> [!info]
> Los polos son el corazón del análisis de la [[Funcion Transferencia/index | función de transferencia]]: deciden la [[Estabilidad/index | estabilidad]] (BIBO) y el carácter de la respuesta. Su posición se diseña con el [[Lugar Raices/index | lugar de las raíces]]; su número fija el [[Orden | orden]].

---

## Ejemplo

> [!ejemplo] Polos y ceros en el plano-$s$
> ![[polos_ceros_plano_s.svg|520]]
>
> Cada polo (×) aporta un modo natural: cuanto más a la izquierda, más rápido decae. Los pares complejos dan oscilación amortiguada; los ceros (○) no añaden modos pero modifican su peso.

> [!ejemplo] Polos reales distintos → modos exponenciales
> $$G(s)=\frac{6}{(s+1)(s+2)(s+3)}.$$
> **Paso 1 — Fracciones parciales** (residuos $r_i=(s-p_i)G(s)|_{s=p_i}$):
> $$G(s)=\frac{3}{s+1}-\frac{6}{s+2}+\frac{3}{s+3}.$$
> **Paso 2 — Antitransformar:** la respuesta impulsional es
> $$g(t)=3e^{-t}-6e^{-2t}+3e^{-3t}.$$
> Tres polos reales negativos ⟹ tres modos que decaen; domina $e^{-t}$ (el más lento).

> [!ejemplo] Tabla de estabilidad según los polos
> | Polos | Estabilidad | Respuesta característica |
> |---|---|---|
> | $-2$ | Estable | $e^{-2t}$ (decae) |
> | $-0.1$ | Estable | $e^{-0.1t}$ (decae lento) |
> | $0$ (simple) | Marginal | constante |
> | $0$ (doble) | Inestable | $t$ (crece) |
> | $0.5$ | Inestable | $e^{0.5t}$ (crece) |
> | $\pm j3$ (simples) | Marginal | $\sin 3t$ (oscila) |
> | $\pm j3$ (dobles) | Inestable | $t\sin 3t$ |
> | $-0.1\pm j2$ | Estable | $e^{-0.1t}\sin 2t$ (amortiguada) |
> | $0.1\pm j2$ | Inestable | $e^{0.1t}\sin 2t$ (creciente) |

> [!ejemplo] Cero en el semiplano derecho (fase no mínima)
> $$G(s)=\frac{s-1}{(s+1)^2}.$$
> Respuesta a escalón: arranca hacia abajo, $y(0^+)=-1$ (*undershoot*), luego sube hasta $1$. Un cero con $\Re(z)>0$ provoca esta respuesta inversa inicial y limita el ancho de banda alcanzable.

---

## Modos naturales

> [!teorema] Relación polo ↔ modo
> Cada polo aporta un modo a la respuesta homogénea:
>
> | Tipo de polo | Modo natural $y_h(t)$ |
> |---|---|
> | Real simple $p$ | $C\,e^{pt}$ |
> | Real múltiple (orden $r$) | $(C_0+C_1 t+\dots+C_{r-1}t^{r-1})e^{pt}$ |
> | Par complejo $\sigma\pm j\omega$ | $e^{\sigma t}(A\cos\omega t+B\sin\omega t)$ |
> | Par complejo múltiple | $e^{\sigma t}\cdot(\text{polinomio en }t)\cdot(A\cos\omega t+B\sin\omega t)$ |

> [!ejemplo] Par complejo conjugado
> $$G(s)=\frac{\omega_n^2}{s^2+2\zeta\omega_n s+\omega_n^2},\quad \text{polos } -\zeta\omega_n\pm j\omega_d,\ \omega_d=\omega_n\sqrt{1-\zeta^2}.$$
> Modo: $e^{-\zeta\omega_n t}\sin(\omega_d t+\phi)$. Ver [[Respuesta Temporal/Segundo Orden/index | segundo orden]].

---

## Estabilidad

> [!definicion] Estabilidad BIBO
> Un sistema es BIBO estable (entrada acotada → salida acotada) **si y solo si** todos los polos tienen parte real estrictamente negativa: $\Re(p_i)<0\ \forall i$. Ver [[Estabilidad/index | estabilidad]] para criterios algebraicos (Routh-Hurwitz).

> [!info] Clasificación
> | Condición | Estabilidad |
> |---|---|
> | $\Re(p_i)<0$ para todo $i$ | **Asintóticamente estable** |
> | Polos en eje imaginario simples; resto $\Re<0$ | **Marginalmente estable** |
> | Algún $\Re(p_i)>0$ | **Inestable** |
> | Polo en eje imaginario con multiplicidad $\ge 2$ | **Inestable** |

---

## Cancelación polo-cero

> [!definicion]
> Un polo $p$ y un cero $z$ se cancelan si $p=z$: el factor $(s-p)$ desaparece de $G(s)$. Ejemplo: $\dfrac{s-1}{(s-1)(s+2)}=\dfrac{1}{s+2}$.

> [!warning] Cancelar polos inestables es peligroso
> Si se cancela un polo con $\Re(p)\ge 0$, su modo **sigue existiendo internamente** aunque desaparezca de la salida. Para $\dot{x}=x+u,\ y=x-u$ se obtiene $G(s)=\frac{2-s}{s-1}$ con cancelación aparente de $s=1$: la salida puede ser estable, pero el estado $x$ diverge. **Nunca cancelar polos inestables** sin control total del estado interno. Ver [[Espacio Estados/index | espacio de estados]].

---

## Polos dominantes y ceros

> [!regla] Aproximación por polos dominantes
> Los polos más cercanos al eje imaginario (menor $|\Re(p_i)|$) dominan el transitorio. Si $|\Re(p)|\ge 5\,|\Re(p_\text{dom})|$, ese polo decae al menos 5 veces más rápido y se desprecia.

> [!ejemplo] Reducción a polo dominante
> $$G(s)=\frac{10}{(s+1)(s+10)}=\frac{10/9}{s+1}-\frac{10/9}{s+10}\approx\frac{1}{s+1}.$$
> El polo $s=-10$ decae 10× más rápido que $s=-1$; tras $t>0.5$ s su aporte es despreciable. Ver [[Orden | orden]].

> [!info] Efecto de los ceros
> Un cero cercano a un polo casi lo cancela y reduce el peso de ese modo. Un cero en el origen ($G=s$, derivador) bloquea el DC. Un cero en RHP ($\Re(z)>0$) da fase no mínima (respuesta inversa, ver ejemplo de arriba).

---

## Fracciones parciales

> [!teorema] Polos simples
> Si todos los $p_i$ son distintos: $G(s)=\sum_i \dfrac{r_i}{s-p_i}$ con residuo $r_i=(s-p_i)G(s)\big|_{s=p_i}$.

> [!teorema] Polos múltiples
> Para $p$ de multiplicidad $r$:
> $$G(s)=\frac{c_r}{(s-p)^r}+\dots+\frac{c_1}{s-p}+(\text{otros polos}),\quad c_{r-k}=\frac{1}{k!}\frac{d^k}{ds^k}\big[(s-p)^rG(s)\big]_{s=p}.$$

> [!ejemplo] Polo doble
> $$G(s)=\frac{1}{(s+1)^2(s+2)}=\frac{1}{(s+1)^2}-\frac{1}{s+1}+\frac{1}{s+2}.$$
> Modos: $t\,e^{-t}$, $e^{-t}$, $e^{-2t}$.

---

## Resumen

> [!resumen]
> | Elemento | Definición | Efecto |
> |---|---|---|
> | Polo $p_i$ | raíz de $D(s)$ | modo $e^{p_i t}$; signo de $\Re$ ⟹ estabilidad |
> | Cero $z_i$ | raíz de $N(s)$ | modula peso del modo; RHP ⟹ fase no mínima |
> | Cancelación | $p=z$ | reduce orden aparente; peligrosa si $\Re(p)\ge0$ |
> | Dominante | menor $|\Re(p)|$ | gobierna el transitorio |

> [!corolario]
> La posición de los polos lo decide todo: $\Re(p_i)<0$ es estabilidad, su distancia al eje fija la velocidad, su parte imaginaria fija la oscilación. Los ceros no crean modos pero los ponderan, y un cero en RHP introduce respuesta inversa. Diseñar control es, en esencia, reubicar polos: ese es el objeto del [[Lugar Raices/index | lugar de las raíces]].

> [!referencia]
> - Definición base: [[Funcion Transferencia/index]].
> - Estabilidad: [[Estabilidad/index]].
> - Reducción de orden: [[Orden]].
> - Reubicación: [[Lugar Raices/index]].
