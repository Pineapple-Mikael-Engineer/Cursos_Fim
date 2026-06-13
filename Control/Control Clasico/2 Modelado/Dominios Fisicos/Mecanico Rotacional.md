---
title: Sistemas Mecánicos Rotacionales
tags:
  - control-clasico
  - dominios-fisicos
  - modelado
draft: false
aliases:
  - rotacional
  - inercia
  - torsional
  - ejes
  - engranajes
---

# Sistemas Mecánicos Rotacionales

> [!definicion]
> Un sistema rotacional se modela combinando inercia $J$, resorte torsional $k$ y amortiguador rotacional $b$ mediante la segunda ley de Newton angular $\sum\tau=J\ddot\theta$. Para una inercia con torque de entrada $\tau$ y carga viscosa $b$:
> $$J\ddot\theta+b\dot\theta=\tau\qquad\Longrightarrow\qquad G(s)=\frac{\Theta(s)}{\tau(s)}=\frac{1}{s(Js+b)}.$$
> Es el **análogo rotacional** del traslacional: $F\leftrightarrow\tau$, $x\leftrightarrow\theta$, $m\leftrightarrow J$.

> [!info]
> Es uno de los [[Funcion Transferencia/index | dominios físicos]] del modelado, **análogo** al [[Mecanico Traslacional | traslacional]] (toda la receta de Newton se traslada cambiando lineal↔angular). Aparece en motores, ejes y transmisiones; los **engranajes** permiten reflejar inercias entre ejes. El acoplamiento entre inercias se trata bien en [[Espacio Estados/index | espacio de estados]].

---

## Ejemplo

> [!ejemplo]
> **Eje con inercia y fricción viscosa, valores numéricos.** Sea $J=2\ \text{kg·m}^2$, $b=4\ \text{N·m·s/rad}$, torque de entrada $\tau_{\text{in}}$, salida ángulo $\theta$.
>
> ![[eje_torques.svg]]
>
> **Paso 1 — Newton angular** (la fricción $b\dot\theta$ se opone al giro):
> $$\tau_{\text{in}}-b\dot\theta=J\ddot\theta\;\Longrightarrow\;J\ddot\theta+b\dot\theta=\tau_{\text{in}}.$$
>
> **Paso 2 — Laplace (CI nulas):**
> $$(Js^2+bs)\,\Theta(s)=\tau_{\text{in}}(s)\;\Longrightarrow\;G(s)=\frac{\Theta(s)}{\tau_{\text{in}}(s)}=\frac{1}{s(Js+b)}=\frac{1}{s(2s+4)}.$$
>
> **Paso 3 — Polos:** $s(2s+4)=0\Rightarrow s=0,\,-2$. Un **integrador** (polo en el origen: la posición se acumula) más un polo real en $s=-2$.
>
> **Paso 4 — FT en velocidad:** si la salida es la velocidad $\omega=\dot\theta$, entonces $\Omega(s)=s\Theta(s)$ y
> $$\frac{\Omega(s)}{\tau_{\text{in}}(s)}=\frac{1}{Js+b}=\frac{1}{2s+4}=\frac{0.5}{s+2},$$
> un **primer orden** con $\tau=J/b=0.5\ \text{s}$. Sin fricción ($b=0$) queda $1/(Js^2)$: doble integrador.

> [!ejemplo]
> **Reducción por engranajes.** Motor con inercia $J_1$ acciona, vía engranajes de relación $n=N_1/N_2$, una carga $J_2$. Reflejar todo al eje del motor.
>
> ![[engranajes.svg]]
>
> **Paso 1 — Cinemática y torques** (engranajes ideales, conservación de potencia): $\theta_2/\theta_1=n$ y $\tau_2=\tau_1/n$.
>
> **Paso 2 — Reflejar la inercia de la carga al eje 1:** $J_{2,\text{ref}}=n^2 J_2$. La inercia equivalente vista por el motor es
> $$J_{\text{eq}}=J_1+n^2 J_2.$$
>
> **Paso 3 — Sistema equivalente y FT** (a $\theta_1$):
> $$J_{\text{eq}}\ddot\theta_1=\tau_1\;\Longrightarrow\;\frac{\Theta_1(s)}{\tau_1(s)}=\frac{1}{J_{\text{eq}}s^2},\qquad \frac{\Theta_2(s)}{\tau_1(s)}=\frac{n}{J_{\text{eq}}s^2}.$$
> Resortes y amortiguadores en el eje 2 se reflejan igual: $k_{\text{eq}}=n^2k_2$, $b_{\text{eq}}=n^2b_2$. Ejemplo numérico: $J_1=1$, $J_2=4$, $n=1/2$ → $J_{\text{eq}}=1+(1/4)(4)=2\ \text{kg·m}^2$.

---

## Elementos y leyes constitutivas

> [!teoria]
> El modelado rotacional usa tres elementos pasivos análogos a los traslacionales. Cada uno relaciona el torque con el movimiento angular de sus extremos:
>
> | Elemento | Parámetro (unidad) | Relación constitutiva | Operador $\Theta/\tau$ |
> |---|---|---|---|
> | Inercia | $J$ (kg·m²) | $\tau=J\ddot\theta$ | $1/Js^2$ (doble integrador) |
> | Resorte torsional | $k$ (N·m/rad) | $\tau=k(\theta_1-\theta_2)$ | $1/k$ (algebraico) |
> | Amortiguador | $b$ (N·m·s/rad) | $\tau=b(\dot\theta_1-\dot\theta_2)$ | $1/bs$ (integrador) |
>
> La ley que las une es la **segunda ley de Newton rotacional**: para cada inercia, $\sum\tau=J\ddot\theta$, sumando torques externos, de resortes torsionales $k(\theta_j-\theta_i)$, de amortiguadores $b(\dot\theta_j-\dot\theta_i)$ y de reacción de ejes. Un eje **rígido** impone $\theta_1=\theta_2$ y $\tau_1=-\tau_2$ (acción-reacción).

> [!info] Engranajes: reflexión de impedancias
> Con relación $n=N_1/N_2=\theta_2/\theta_1$ y conservación de potencia ($\tau_2\theta_2=\tau_1\theta_1$), todo elemento del eje secundario se "refleja" al primario multiplicado por $n^2$:
> $$J_{\text{ref}}=n^2J,\qquad k_{\text{ref}}=n^2k,\qquad b_{\text{ref}}=n^2b,\qquad \tau_{\text{carga,ref}}=n\,\tau_{\text{carga}}.$$
> Así un sistema de varios ejes se colapsa en una sola ecuación sobre el eje de entrada.

---

## Más configuraciones resueltas

> [!ejemplo] Dos inercias en eje rígido común
> ![[ejes_compartidos.svg]]
> Si $J_1$ y $J_2$ giran solidarias ($\theta_1=\theta_2=\theta$), las inercias **se suman**:
> $$\tau_1+\tau_2=(J_1+J_2)\ddot\theta\;\Longrightarrow\;G(s)=\frac{\Theta(s)}{\tau_1+\tau_2}=\frac{1}{(J_1+J_2)s^2}.$$

> [!ejemplo] Eje flexible (transmisión elástica)
> ![[eje_flexible.svg]]
> $J_1$ (motor) y $J_2$ (carga) unidas por resorte torsional $k$. Con $\tau_{\text{eje}}=k(\theta_1-\theta_2)$:
> $$(J_1s^2+k)\Theta_1-k\Theta_2=\tau_{\text{motor}},\qquad -k\Theta_1+(J_2s^2+k)\Theta_2=0.$$
> Resolviendo de $\tau_{\text{motor}}$ a $\theta_2$:
> $$G(s)=\frac{k}{J_1J_2s^4+(J_1+J_2)k\,s^2}=\frac{k/J_1}{s^2\big(s^2+\frac{J_1+J_2}{J_1J_2}k\big)}.$$
> Dos polos en el origen (modo rígido) + par de polos complejos (modo elástico, resonancia del eje).

> [!ejemplo] Tren de engranajes multietapa
> ![[tren_engranajes.svg]]
> Relación total $n_{\text{total}}=n_1n_2n_3\cdots$ Inercia reflejada al eje de entrada:
> $$J_{\text{eq}}=J_1+n_1^2J_2+(n_1n_2)^2J_3+\cdots,$$
> y el sistema equivalente es $J_{\text{eq}}\ddot\theta_{\text{in}}+b_{\text{eq}}\dot\theta_{\text{in}}+k_{\text{eq}}\theta_{\text{in}}=\tau_{\text{in}}-\tau_{\text{carga,ref}}$.

---

## Tabla de funciones de transferencia

> [!info] Configuraciones comunes ($\Theta_{\text{sal}}/\tau_{\text{ent}}$)
> | Configuración | $G(s)$ | Polos en $s=0$ | Tipo |
> |---|---|---|---|
> | Inercia sola | $\dfrac{1}{Js^2}$ | 2 | doble integrador |
> | Inercia + $b$ (velocidad) | $\dfrac{1}{Js+b}$ | 0 | polo real |
> | Inercia + $b$ (posición) | $\dfrac{1}{s(Js+b)}$ | 1 | integrador |
> | Dos inercias, eje rígido | $\dfrac{1}{(J_1+J_2)s^2}$ | 2 | doble integrador |
> | Eje flexible (posición carga) | $\dfrac{k/J_1}{s^2(s^2+\frac{J_1+J_2}{J_1J_2}k)}$ | 2 | doble integrador + modo elástico |
> | Engranajes ideales | $\dfrac{n}{J_{\text{eq}}s^2}$ | 2 | doble integrador con ganancia |

---

## Receta de modelado

> [!algoritmo]
> Para obtener la FT de un sistema rotacional:
> 1. **Coordenadas.** Asignar un ángulo $\theta_i$ a cada inercia, sentido positivo fijo.
> 2. **Engranajes.** Si hay reducciones, reflejar inercias/resortes/amortiguadores al eje elegido con factor $n^2$ y colapsar en $J_{\text{eq}}$, etc.
> 3. **Newton angular.** Escribir $\sum\tau=J_i\ddot\theta_i$ por inercia, con torques de resortes $k(\theta_j-\theta_i)$ y amortiguadores $b(\dot\theta_j-\dot\theta_i)$.
> 4. **Laplace con CI nulas.** $\dot\theta\to s\Theta$, $\ddot\theta\to s^2\Theta$; despejar la FT buscada.

> [!info] Analogía traslacional ↔ rotacional
> | Traslacional | Rotacional |
> |---|---|
> | Fuerza $F$ | Torque $\tau$ |
> | Posición $x$ | Ángulo $\theta$ |
> | Masa $m$ | Inercia $J$ |
> | Resorte $k$ | Resorte torsional $k$ |
> | Amortiguador $b$ | Amortiguador rotacional $b$ |
>
> Toda la receta del [[Mecanico Traslacional | traslacional]] se reutiliza cambiando lineal por angular.

> [!info] En MATLAB
> ```matlab
> J=2; b=4;
> G_pos = tf(1, [J b 0]);   % posicion: 1/(s(Js+b))
> G_vel = tf(1, [J b]);     % velocidad: 1/(Js+b)
> damp(G_vel)
> step(G_vel)
> ```

---

## Limitaciones

> [!warning]
> 1. **Ejes rígidos:** asumen deformación nula (válido para alta rigidez; si no, usar el modelo de eje flexible).
> 2. **Engranajes ideales:** sin juego (*backlash*), sin fricción ni elasticidad.
> 3. **Resorte lineal:** $k$ constante solo para pequeñas deformaciones.
> 4. **Amortiguador lineal:** $b$ constante solo para bajas velocidades.
> 5. **Inercias internas** de engranajes y acoplamientos despreciadas.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Elementos | inercia $J$, resorte torsional $k$, amortiguador $b$ |
> | Ley | $\sum\tau=J\ddot\theta$ (Newton angular) |
> | EDO típica | $J\ddot\theta+b\dot\theta+k\theta=\tau$ |
> | FT (posición) | $G(s)=\dfrac{1}{s(Js+b)}$ |
> | Engranajes | reflejan $n^2J$, $n^2k$, $n^2b$ |
> | Orden | 2 por inercia (grado de libertad) |

> [!corolario]
> Modelar un sistema rotacional es aplicar Newton angular inercia por inercia, idéntico al [[Mecanico Traslacional | traslacional]] cambiando $F\to\tau$, $x\to\theta$, $m\to J$. Los engranajes añaden la reflexión $n^2$ que colapsa varios ejes en uno solo; el eje flexible introduce un modo resonante. El acoplamiento entre inercias se trata cómodamente en [[Espacio Estados/index | espacio de estados]].

> [!referencia]
> - Dominio análogo traslacional: [[Mecanico Traslacional]].
> - Respuesta de segundo orden: [[Respuesta Temporal/Segundo Orden/index]].
> - Representación matricial: [[Espacio Estados/index]].
