---
title: Sistemas Mecánicos Traslacionales
order: 1
tags:
  - control-clasico
  - dominios-fisicos
  - modelado
draft: false
aliases:
  - mecanico traslacional
  - masa-resorte-amortiguador
  - traslacional
---

# Sistemas Mecánicos Traslacionales

> [!definicion]
> Un sistema mecánico traslacional se modela combinando tres elementos —masa $m$, resorte $k$ y amortiguador $b$— mediante la segunda ley de Newton. Para el conjunto masa-resorte-amortiguador con fuerza de entrada $F$ y posición de salida $x$:
> $$m\ddot{x}+b\dot{x}+kx=F(t)\qquad\Longrightarrow\qquad G(s)=\frac{X(s)}{F(s)}=\frac{1}{ms^2+bs+k}.$$

> [!info]
> Es uno de los [[Funcion Transferencia/index | dominios físicos]] básicos del modelado. Es **análogo** al [[Mecanico Rotacional | rotacional]] (cambiando fuerza↔par, $x$↔$\theta$, $m$↔$J$) y al [[Electrico | eléctrico]] (fuerza↔voltaje, $v$↔corriente). Casi siempre produce dinámica de [[Respuesta Temporal/Segundo Orden/index | segundo orden]].

---

## Ejemplo

> [!ejemplo]
> **Masa-resorte-amortiguador con valores numéricos.** Sea $m=1\ \text{kg}$, $b=4\ \text{N·s/m}$, $k=3\ \text{N/m}$. Hallar la FT, los polos y el tipo de respuesta.
>
> ![[mra_simple.svg|500]]
>
> **Paso 1 — Ecuación de movimiento** (suma de fuerzas sobre la masa):
> $$F(t)-\underbrace{kx}_{F_k}-\underbrace{b\dot{x}}_{F_b}=m\ddot{x}\;\Longrightarrow\;m\ddot{x}+b\dot{x}+kx=F.$$
>
> **Paso 2 — Función de transferencia** (condiciones iniciales nulas, $\mathcal{L}\{\ddot{x}\}=s^2X$):
> $$G(s)=\frac{1}{ms^2+bs+k}=\frac{1}{s^2+4s+3}.$$
>
> **Paso 3 — Polos:** $s^2+4s+3=(s+1)(s+3)=0\Rightarrow s=-1,\,-3$. Reales y negativos → **sobreamortiguado** y estable.
>
> **Paso 4 — Parámetros de 2.º orden:**
> $$\omega_n=\sqrt{k/m}=\sqrt{3}\approx1.73\ \text{rad/s},\qquad \zeta=\frac{b}{2\sqrt{km}}=\frac{4}{2\sqrt{3}}\approx1.15>1.$$
> Como $\zeta>1$ se confirma la respuesta sobreamortiguada (sin oscilación). Si en cambio fuera $b=2$, saldría $\zeta\approx0.58$ y la respuesta sería subamortiguada con [[Sobrepico Mp | sobrepico]].

> [!ejemplo]
> **Dos masas acopladas (sistema MIMO).** Masas $m_1,m_2$ unidas por resorte $k_1$ y amortiguador $b$; $m_1$ atada a la pared por $k_2$.
>
> ![[mra_doble.svg|600]]
>
> **DCL de $m_1$** (entrada $F_1$): la atan el resorte de pared $-k_2x_1$, el resorte central $-k_1(x_1-x_2)$ y el amortiguador $-b(\dot{x}_1-\dot{x}_2)$:
> $$m_1\ddot{x}_1+b\dot{x}_1-b\dot{x}_2+(k_1+k_2)x_1-k_1x_2=F_1.$$
>
> **DCL de $m_2$** (entrada $F_2$): solo lo unen el resorte central y el amortiguador a $m_1$:
> $$m_2\ddot{x}_2-b\dot{x}_1+b\dot{x}_2-k_1x_1+k_1x_2=F_2.$$
>
> Cada masa aporta una coordenada y una ecuación de 2.º orden → el sistema completo es de **orden 4**. Los términos cruzados ($-k_1x_2$, $-b\dot{x}_2$) representan el acoplamiento; en forma matricial $M\ddot{\mathbf{x}}+B\dot{\mathbf{x}}+K\mathbf{x}=\mathbf{F}$, ideal para pasar a [[Espacio Estados/index | espacio de estados]].

---

## Elementos y leyes constitutivas

> [!teoria]
> El modelado traslacional usa tres elementos pasivos. Cada uno relaciona la fuerza que soporta con el movimiento de sus extremos:
>
> | Elemento | Parámetro (unidad) | Relación constitutiva | Almacena / disipa |
> |---|---|---|---|
> | Masa | $m$ (kg) | $F=m\ddot{x}$ | energía cinética |
> | Resorte | $k$ (N/m) | $F=k\,x$ (o $k\,\Delta x$) | energía potencial |
> | Amortiguador | $b$ (N·s/m) | $F=b\dot{x}$ | disipa (calor) |
>
> La ley que las une es la **segunda ley de Newton**: para cada masa, $\sum F=m\ddot{x}$, sumando con signo todas las fuerzas según la coordenada positiva elegida. El amortiguador también se denota $c$ o $B$; el resorte central entre dos masas ejerce $k(x_i-x_j)$ sobre cada una, con signos opuestos (tercera ley).

> [!info] Convención de signos
> ![[mecanico_traslacional_convencion.svg|400]]
>
> Se asigna una coordenada $x_i$ a cada masa con sentido positivo arbitrario pero **fijo**. Resortes y amortiguadores se oponen al movimiento relativo: si $x_i$ crece, sus fuerzas apuntan en $-x_i$. Mantener la convención evita errores de signo en el DCL.

---

## Receta de modelado

> [!algoritmo]
> Para obtener la FT de cualquier sistema traslacional:
> 1. **Coordenadas.** Asignar una posición $x_i$ a cada masa (un grado de libertad por masa), con sentido positivo fijo.
> 2. **Diagrama de cuerpo libre.** Para cada masa, dibujar todas las fuerzas: entradas externas y reacciones de resortes/amortiguadores conectados.
> 3. **Suma de fuerzas.** Escribir $\sum F=m_i\ddot{x}_i$ para cada masa, con los signos de la convención.
> 4. **Relaciones constitutivas.** Sustituir $F_k=k\,\Delta x$ y $F_b=b\,\Delta\dot{x}$ (usar diferencias de posición/velocidad entre extremos).
> 5. **Laplace con CI nulas.** $\dot{x}\to sX$, $\ddot{x}\to s^2X$; despejar la FT $X_i(s)/F_j(s)$ buscada.

> [!info] Analogía fuerza-voltaje
> | Mecánico | Eléctrico |
> |---|---|
> | Fuerza $F$ | Voltaje $V$ |
> | Velocidad $v$ | Corriente $i$ |
> | Masa $m$ | Inductancia $L$ |
> | Resorte $1/k$ (compliancia) | Capacitancia $C$ |
> | Amortiguador $b$ | Resistencia $R$ |
>
> Permite reutilizar la intuición de circuitos: una masa "se opone a cambios de velocidad" igual que una inductancia a cambios de corriente. Ver [[Electrico | sistemas eléctricos]].

> [!info] En MATLAB
> ```matlab
> m=1; b=4; k=3;
> G = tf(1, [m b k]);   % 1/(s^2+4s+3)
> damp(G)               % polos, wn y zeta
> step(G)               % respuesta al escalon de fuerza
> ```

---

## Limitaciones del modelo lineal

> [!warning]
> 1. **Resorte lineal:** $F=kx$ solo vale para pequeñas deformaciones (ley de Hooke); resortes reales se endurecen o saturan.
> 2. **Amortiguador lineal:** $F=b\dot{x}$ supone fricción viscosa (flujo laminar); a alta velocidad el arrastre es $\propto\dot{x}^2$.
> 3. **Rozamiento seco (Coulomb):** fuerza constante opuesta al movimiento, **no lineal**, no incluida; requiere [[Linealizacion/index | linealización]] o modelo conmutado.
> 4. **Cuerpos rígidos:** se desprecia la deformación interna y la masa de resortes/amortiguadores.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Elementos | masa $m$, resorte $k$, amortiguador $b$ |
> | Ley | $\sum F=m\ddot{x}$ (Newton) |
> | EDO típica | $m\ddot{x}+b\dot{x}+kx=F$ |
> | FT | $G(s)=\dfrac{1}{ms^2+bs+k}$ |
> | Parámetros | $\omega_n=\sqrt{k/m}$, $\zeta=\dfrac{b}{2\sqrt{km}}$ |
> | Orden | 2 por masa (grado de libertad) |

> [!corolario]
> Modelar un sistema traslacional es aplicar Newton masa por masa y sustituir las relaciones constitutivas: el resultado es siempre una EDO lineal de 2.º orden por grado de libertad, cuya FT $1/(ms^2+bs+k)$ fija $\omega_n$ y $\zeta$. La misma plantilla sirve, por analogía, para los dominios [[Mecanico Rotacional | rotacional]] y [[Electrico | eléctrico]]; el acoplamiento entre masas se trata cómodamente en [[Espacio Estados/index | espacio de estados]].

> [!referencia]
> - Dominio análogo rotacional: [[Mecanico Rotacional]].
> - Analogía eléctrica: [[Electrico]].
> - Respuesta del sistema resultante: [[Respuesta Temporal/Segundo Orden/index]].
> - Representación matricial: [[Espacio Estados/index]].
