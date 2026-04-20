---
title: Polos Dominantes
tags:
  - control-clasico
  - estabilidad
  - aproximacion
  - reduccion-de-orden
draft: true
aliases:
  - Dominant Poles
  - Polo Dominante
  - Aproximación de Orden Reducido
---

# Polos Dominantes

> [!definicion] Definición
> En un sistema [[Sistemas LTI]] de orden $n$ con función de transferencia racional, los **polos dominantes** son aquellos polos cuya parte real es la **más cercana al eje imaginario** (en valor absoluto), es decir, los que tienen el menor $|\Re(p_i)|$ entre todos los polos del sistema.

---

## Justificación Matemática

> [!teorema] Descomposición en Fracciones Parciales
> Para un sistema con polos distintos, la respuesta al impulso es:
> $$
> h(t) = \sum_{i=1}^{n} A_i e^{p_i t} \cdot \mathbf{1}(t)
> $$
> 
> Cada polo $p_i = \sigma_i + j\omega_i$ aporta un término $A_i e^{\sigma_i t} e^{j\omega_i t}$.
> 
> La **velocidad de decaimiento** de cada modo está determinada por $\sigma_i = \Re(p_i)$:
> - Si $\sigma_i$ es muy negativo (polo lejano), $e^{\sigma_i t}$ decae rápidamente
> - Si $\sigma_i$ es cercano a cero (polo cercano al eje imaginario), $e^{\sigma_i t}$ decae lentamente

> [!proposicion] Constante de Tiempo
> Asociada a un polo real $p = \sigma$ (con $\sigma < 0$), se define la **constante de tiempo**:
> $$
> \tau = \frac{1}{|\sigma|}
> $$
> 
> El modo asociado decae al $36.8\%$ de su valor inicial en $t = \tau$, y se considera **extinguido** en $t \approx 5\tau$ (menos del $1\%$).

> [!ejemplo] Comparación de constantes de tiempo
> | Polo | Constante de tiempo $\tau$ | Tiempo de extinción $5\tau$ |
> |------|---------------------------|----------------------------|
> | $p = -1$ | $1$ s | $5$ s |
> | $p = -10$ | $0.1$ s | $0.5$ s |
> | $p = -100$ | $0.01$ s | $0.05$ s |
> 
> Un polo en $-100$ se extingue **100 veces más rápido** que uno en $-1$.

---

## Condición para ser Polo Dominante

> [!definicion] Criterio de Dominancia
> Sea $\mathcal{P}$ el conjunto de polos del sistema. Un polo $p_d \in \mathcal{P}$ es **dominante** si:
> $$
> |\Re(p_d)| \ll |\Re(p_k)|, \quad \forall p_k \in \mathcal{P} \setminus \{p_d\}
> $$
> 
> En la práctica, se considera que un polo es dominante si su parte real es al menos **5 a 10 veces menor** en valor absoluto que la de los demás polos:
> $$
> \frac{|\Re(p_{\text{no dominante}})|}{|\Re(p_{\text{dominante}})|} \ge 5 \quad \text{(regla práctica)}
> $$

> [!ejemplo] Sistema de tercer orden
> Sea $G(s) = \dfrac{1}{(s+1)(s+10)(s+100)}$:
> - Polos: $p_1 = -1$, $p_2 = -10$, $p_3 = -100$
> - Polo dominante: $p_d = -1$ (más cercano al eje imaginario)
> - Relaciones: $10/1 = 10$, $100/1 = 100$ (cumple criterio)
> 
> El sistema puede aproximarse por:
> $$
> G_{\text{aprox}}(s) \approx \frac{K}{s+1}
> $$
> donde $K$ se ajusta para igualar la ganancia en régimen permanente.

---

## Aproximación de Sistemas de Orden Superior

> [!teoria] Reducción de Orden
> Dado un sistema de orden $n$ con polos dominantes bien separados, la dinámica transitoria está gobernada casi exclusivamente por los polos dominantes. Los polos rápidos (lejanos) se extinguen antes de que los modos dominantes hayan evolucionado significativamente.

> [!proposicion] Procedimiento de Aproximación
> 1. Identificar los polos dominantes (los de menor $|\Re(p_i)|$)
> 2. Despreciar los polos rápidos (alta frecuencia)
> 3. Ajustar la ganancia estática del sistema reducido para que coincida con la del sistema original
> 
> Para polos reales dominantes:
> $$
> G_{\text{aprox}}(s) = \frac{K}{s + |p_d|}
> $$
> 
> Para polos complejos conjugados dominantes:
> $$
> G_{\text{aprox}}(s) = \frac{K \omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}
> $$

> [!ejemplo] Sistema original vs aproximación
> Sea $G(s) = \dfrac{10}{(s+1)(s+10)}$:
> - Polo dominante: $p_d = -1$
> - Polo rápido: $p_r = -10$
> 
> **Aproximación de primer orden:**
> $$
> G_{\text{aprox}}(s) = \frac{1}{s+1}
> $$
> (ganancia estática: $G(0)=10$, $G_{\text{aprox}}(0)=1$ → requiere ajuste: $G_{\text{aprox}}(s) = \frac{10}{s+1}$)
> 
> **Comparación de respuestas al escalón:**
> - Sistema original: $y(t) = 1 - 1.111e^{-t} + 0.111e^{-10t}$
> - Aproximación: $y_{\text{aprox}}(t) = 1 - e^{-t}$
> 
> La diferencia es pequeña después de $t > 0.5$ s (el término $e^{-10t}$ se extingue rápidamente).

---

## Limitaciones de la Aproximación

> [!warning] Cuándo NO aplicar la aproximación por polos dominantes
> 1. **Ceros cercanos a polos dominantes:** Un cero puede cancelar el efecto del polo dominante o modificar significativamente los residuos.
> 
> 2. **Residuos muy grandes en polos rápidos:** Aunque el polo rápido decae rápidamente, si su residuo es enorme, su contribución inicial puede ser significativa.
> 
> 3. **Polos no separados por un factor suficiente:** Si la relación entre partes reales es menor a 5, la aproximación puede ser pobre.
> 
> 4. **Sistemas con polos dominantes complejos y ceros en el SPD:** La dinámica puede ser más compleja que lo que sugiere el polo dominante.

> [!ejemplo] Falla por cero cercano
> Sea $G(s) = \dfrac{s + 0.9}{(s+1)(s+10)}$:
> - Polo dominante: $p_d = -1$
> - Cero en $z = -0.9$ (muy cercano al polo dominante)
> - El cero casi cancela el polo, alterando drásticamente la respuesta
> - La aproximación de primer orden $\frac{K}{s+1}$ falla

> [!ejemplo] Falla por residuo grande
> Sea $G(s) = \dfrac{100}{(s+1)(s+100)}$:
> - Polo dominante: $p_d = -1$
> - Polo rápido: $p_r = -100$
> - Residuos: $A_1 = 1.0101$, $A_2 = -0.0101$
> - El residuo del polo rápido es pequeño → aproximación válida
> 
> Pero si $G(s) = \dfrac{10000}{(s+1)(s+100)}$:
> - Residuos: $A_1 = 101.01$, $A_2 = -1.01$
> - El polo rápido tiene residuo comparable → la aproximación puede fallar

---

## Representación Gráfica en el Plano $s$

> [!definicion] Visualización de Polos Dominantes
> En el plano $s$, los polos dominantes son aquellos **más cercanos al eje imaginario**.
> 
> ```
>     jω
>      ↑
>    3 +
>      |                    × (polo lejano)
>    2 +
>      |        × (polo dominante)
>    1 +
>      |
> ----+----+----+----+----→ σ
>    -4  -3  -2  -1   0
>      |
>    -1 +
>      |        × (polo dominante conjugado)
>    -2 +
>      |                    × (polo lejano conjugado)
>    -3 +
> ```
> 
> Los polos en $-1 \pm j0$ son dominantes; los polos en $-4 \pm j0$ son rápidos y pueden despreciarse.

---

## Relación con el Lugar de las Raíces

> [!teoria] Diseño de Controladores
> El concepto de polos dominantes es fundamental en el diseño de controladores mediante el [[Lugar de las Raíces]]:
> - El controlador se diseña para ubicar los polos dominantes en posiciones deseadas
> - Los polos restantes se colocan lo suficientemente lejos para no afectar la dinámica
> - La aproximación permite diseñar controladores PID basados en sistemas de segundo orden

---

## Polos Dominantes en Sistemas Discretos

> [!definicion] Caso Discreto
> En sistemas discretos, los polos dominantes son aquellos **más cercanos al círculo unitario** (los de mayor módulo $|p_i|$), pues determinan la velocidad de decaimiento de la respuesta transitoria.
> 
> | Polo continuo | Polo discreto equivalente | Relación |
> |---------------|--------------------------|----------|
> | $\sigma$ (negativo) | $p = e^{\sigma T}$ | $\|p\| < 1$ |
> | Cercano a 0 | Cercano a 1 | Lento |
> | Lejano (gran $\|\sigma\|$) | Cercano a 0 | Rápido |

> [!ejemplo] Sistema discreto
> Sea $H(z) = \dfrac{1}{(z - 0.9)(z - 0.1)}$:
> - Polos: $p_1 = 0.9$, $p_2 = 0.1$
> - Polo dominante: $p_d = 0.9$ (más cercano al círculo unitario)
> - Aproximación: $H_{\text{aprox}}(z) = \dfrac{K}{z - 0.9}$

---

## Resumen

> [!info]
> - Los **polos dominantes** son los más cercanos al eje imaginario en sistemas continuos (o al círculo unitario en discretos)
> - Determinan la dinámica transitoria de la respuesta
> - Permiten aproximar sistemas de orden superior por modelos de primer o segundo orden
> - La aproximación es válida si la separación entre partes reales es al menos 5:1
> - **Precaución:** Ceros cercanos o residuos grandes pueden invalidar la aproximación