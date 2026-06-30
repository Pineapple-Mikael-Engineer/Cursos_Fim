---
title: Reducción de Orden
order: 4
tags:
  - control-clasico
  - analisis
  - respuesta-temporal
draft: false
aliases:
  - reducción de orden
  - modelo reducido
  - model order reduction
---

# Reducción de Orden

> [!definicion]
> Reducir el orden es aproximar un [[Orden Superior | sistema de orden alto]] por uno de orden menor (típicamente [[Segundo Orden/index | segundo orden]]) que conserva la respuesta dominante. Se hace despreciando los polos rápidos (sustituyéndolos por su valor en DC) o cancelando pares polo-cero próximos, **conservando siempre la ganancia DC** $G_{red}(0)=G(0)$.

> [!info]
> Es la aplicación práctica de los [[Orden Superior | polos dominantes]]: simplifica el análisis y el diseño hacia un modelo de [[Segundo Orden/index | segundo orden]]. Cuidado con cancelar en el SPD ([[Sistemas Fase Minima | fase no mínima]]). Liga con [[Ganancia Estatica | ganancia DC]] y [[Teorema Valor Inicial Final | valor final]].

---

## Ejemplo

> [!ejemplo] Tercer orden → segundo orden: completo vs. reducido
> Reducir y comparar
> $$G(s)=\frac{50}{(s^2+2s+5)(s+10)},\qquad G(0)=\frac{50}{5\cdot 10}=1.$$
>
> ![[reduccion_orden_comparacion.svg|560]]
>
> **Paso 1 — Polos y dominancia.** $s^2+2s+5\Rightarrow s=-1\pm j2$; factor lineal $\Rightarrow s=-10$.
> $$\frac{|{-10}|}{|{-1}|}=10\ge 5\;\checkmark\quad\text{→ el par } -1\pm j2 \text{ es dominante.}$$
>
> **Paso 2 — Despreciar el polo rápido conservando la ganancia DC.** Escribir el factor lento como $1+s/p$ con $p=10$ y evaluarlo en DC:
> $$\frac{1}{s+10}=\frac{1/10}{1+s/10}\xrightarrow{s/10\,\to\,0}\frac{1}{10}.$$
> $$\boxed{\,G_{red}(s)=\frac{50/10}{s^2+2s+5}=\frac{5}{s^2+2s+5}.}$$
>
> **Paso 3 — Verificar la ganancia DC** (restricción mínima):
> $$G_{red}(0)=\frac{5}{5}=1=G(0)\;\checkmark$$
>
> **Paso 4 — Parámetros del modelo reducido.** De $s^2+2s+5$:
> $$\omega_n=\sqrt5\approx2.24\ \text{rad/s},\quad \zeta=\tfrac{1}{\sqrt5}\approx0.447,\quad M_p\approx20.8\%,\quad t_s(2\%)\approx 4\ \text{s}.$$
>
> **Paso 5 — Comparar las respuestas al escalón.**
>
> | Característica | Completo (3.º orden) | Reducido (2.º orden) |
> |---|---|---|
> | Valor final | $1$ | $1$ (idéntico, igual ganancia DC) |
> | Polo extra | $-10$ ($e^{-10t}$, extinto en $\sim0.3$ s) | — |
> | $M_p$ | $\approx 18\%$ | $\approx 20.8\%$ |
> | $t_s$ | $\approx 4.1$ s | $\approx 4$ s |
>
> El reducido reproduce la dinámica lenta dominante; el polo en $-10$ solo añade un breve retardo inicial. El reducido **sobreestima** ligeramente $M_p$ (lado conservador), por eso conviene verificar siempre con la respuesta completa.

---

## En qué consiste

> [!info] Métodos comunes
> | Método | Idea |
> |---|---|
> | **Polos dominantes** | retener solo el par dominante; despreciar polos rápidos |
> | **Cancelación polo-cero** | eliminar pares polo-cero próximos en el SPI |
> | **Conservar la ganancia DC** | ajustar el modelo reducido para igualar $G(0)$ |

> [!regla] Despreciar un polo lejano
> Un polo real en $s=-p$ con $p$ grande se desprecia conservando la **ganancia estática**: se reemplaza el factor por su valor en DC.
> $$\frac{1}{1+s/p}\xrightarrow{p\ \text{grande}}1.$$
> El modo $e^{-pt}$ decae casi instantáneamente y no afecta el transitorio dominante.

> [!regla] Cancelar pares polo-cero próximos
> Si un polo y un cero están **muy cerca** ($|p-z|$ pequeño), su efecto neto es casi una constante y se cancelan:
> $$\frac{s+z}{s+p}\approx 1\quad\text{si } z\approx p.$$
> Reduce el orden sin alterar apreciablemente la respuesta.

> [!teorema] Conservar el régimen permanente
> Todo modelo reducido debe satisfacer $G_{red}(0)=G(0)$, garantizando el mismo **valor final** ante escalón ([[Teorema Valor Inicial Final | teorema del valor final]]) y el mismo [[Error Estacionario/index | error estacionario]]. Es la restricción mínima de cualquier reducción válida.

> [!info] Cuándo es válido
> - Existe un par de [[Orden Superior | polos dominantes]] claro (separación $\ge 5\times$).
> - No hay ceros cercanos al par dominante que distorsionen la respuesta.
> - Se conserva la ganancia DC.

> [!info] En MATLAB
> ```matlab
> G   = tf(50, conv([1 2 5],[1 10]));
> Gr  = tf(5, [1 2 5]);     % modelo reducido
> step(G, Gr)               % comparar ambas respuestas
> % alternativa automatica:
> Gr2 = balred(G, 2);       % reduccion balanceada a orden 2
> ```

---

## Limitaciones

> [!warning] No cancelar en el SPD
> Cancelar un polo o cero en el **semiplano derecho** deja un modo **inestable oculto** (incontrolable/inobservable). La cancelación solo es válida —y aproximada— en el SPI, nunca con elementos del SPD ([[Sistemas Fase Minima | fase no mínima]]).

> [!warning]
> Una reducción mal hecha (despreciar un polo no tan rápido, o ignorar un cero cercano) puede **subestimar** el sobrepico o el tiempo de establecimiento. Verificar siempre comparando la respuesta del modelo reducido con la del completo.

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Objetivo | aproximar orden alto por 2.º orden |
> | Polos rápidos | reemplazar por su valor DC: $1/(1+s/p)\to 1$ |
> | Polo-cero próximos | cancelar en el SPI |
> | Restricción mínima | $G_{red}(0)=G(0)$ |
> | Condición | dominancia $\ge 5\times$, sin ceros cercanos |
> | Prohibido | cancelar en el SPD (modo inestable oculto) |

> [!corolario]
> Reducir el orden es quedarse con la dinámica dominante: se desprecian los polos rápidos por su ganancia DC y se cancelan pares polo-cero próximos, siempre forzando $G_{red}(0)=G(0)$ para preservar el valor final. La aproximación es fiable con separación $\ge 5\times$ y sin ceros cercanos; en el SPD nunca se cancela. El resultado es un modelo de [[Segundo Orden/index | segundo orden]] manejable, que debe validarse contra la respuesta completa.

> [!referencia]
> - Sistema completo y dominancia: [[Orden Superior]].
> - Modelo objetivo: [[Segundo Orden/index]].
> - Riesgo de cancelar en el SPD: [[Sistemas Fase Minima]].
> - Ganancia DC y valor final: [[Ganancia Estatica]] · [[Teorema Valor Inicial Final]].
