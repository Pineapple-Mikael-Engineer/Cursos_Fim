---
title: "Control Clásico - Temario Temático"
author: "Jorge Enrique Ortiz Porras / Manuel Ronald Gomez Casasola"
subject: "Control Clásico"
code: "MT235"
cycle: 6
credits: 3
hours_per_week: 5
prerequisites: "MB158"
academic_area: "Ingeniería Aplicada"
tags:
  - control-clasico
  - modelado
  - respuesta-temporal
  - lugar-de-raices
  - respuesta-en-frecuencia
  - pid
  - temario
---

# Control Clásico — Temario Temático (por bloques conceptuales)

---

## Bloque I: Modelado Matemático de Sistemas

### I.1 Fundamentos de Control
- Definición de sistemas de control
- Lazo abierto vs. lazo cerrado
- Componentes de un sistema de control
- Sensibilidad a variaciones de parámetros

### I.2 Transformada de Laplace

$$
\mathcal{L}\{f(t)\} = F(s) = \int_0^\infty f(t)e^{-st}\,dt
$$

**Transformadas elementales:**

| $f(t)$ | $F(s)$ |
|--------|--------|
| $\delta(t)$ | $1$ |
| $u(t)$ | $\frac{1}{s}$ |
| $t^n$ | $\frac{n!}{s^{n+1}}$ |
| $e^{-at}$ | $\frac{1}{s+a}$ |
| $\sin(\omega t)$ | $\frac{\omega}{s^2+\omega^2}$ |
| $\cos(\omega t)$ | $\frac{s}{s^2+\omega^2}$ |

**Propiedades:**

| Propiedad | Dominio $t$ | Dominio $s$ |
|-----------|-------------|-------------|
| Linealidad | $af(t) + bg(t)$ | $aF(s) + bG(s)$ |
| Derivación | $f'(t)$ | $sF(s) - f(0)$ |
| Derivada $n$-ésima | $f^{(n)}(t)$ | $s^nF(s) - s^{n-1}f(0) - \dots$ |
| Integración | $\int f(t)\,dt$ | $\frac{F(s)}{s}$ |
| Traslación en $t$ | $f(t-a)u(t-a)$ | $e^{-as}F(s)$ |
| Traslación en $s$ | $e^{-at}f(t)$ | $F(s+a)$ |
| Convolución | $\int f(\tau)g(t-\tau)d\tau$ | $F(s)G(s)$ |
| Valor inicial | $f(0^+)$ | $\lim_{s\to\infty} sF(s)$ |
| Valor final | $f(\infty)$ | $\lim_{s\to 0} sF(s)$ |

**Expansión en fracciones parciales:**

- Caso raíces reales distintas: $F(s) = \sum_{i=1}^n \frac{A_i}{s+p_i}$, $A_i = (s+p_i)F(s)\big|_{s=-p_i}$
- Caso raíces complejas conjugadas: $F(s) = \frac{As + B}{s^2 + as + b} + \text{términos reales}$
- Caso raíces múltiples: $F(s) = \sum_{i=1}^r \frac{A_i}{(s+p)^i} + \text{otros términos}$

### I.3 Función de Transferencia

$$
G(s) = \frac{Y(s)}{U(s)} = \frac{N(s)}{D(s)}
$$

- Polos: raíces de $D(s) = 0$
- Ceros: raíces de $N(s) = 0$
- Orden del sistema: grado de $D(s)$
- Polos dominantes: los más cercanos al eje imaginario

### I.4 Diagramas de Bloques

Álgebra de bloques:
- Serie: $G = G_1 \cdot G_2$
- Paralelo: $G = G_1 + G_2$
- Retroalimentación negativa: $\frac{Y}{R} = \frac{G}{1 + GH}$
- Retroalimentación positiva: $\frac{Y}{R} = \frac{G}{1 - GH}$

### I.5 Modelado de Sistemas Físicos

**Mecánicos traslacionales:**

Ley de Newton: $\sum F = m\frac{d^2x}{dt^2}$

Elementos:
- Masa: $F = ma \;\to\; ms^2X(s)$
- Resorte: $F = kx \;\to\; kX(s)$
- Amortiguador: $F = bv \;\to\; bsX(s)$

Ecuación: $m\ddot{x} + b\dot{x} + kx = F(t)$

$$
\frac{X(s)}{F(s)} = \frac{1}{ms^2 + bs + k}
$$

**Mecánicos rotacionales:**

$$
\sum \tau = J\frac{d^2\theta}{dt^2}
$$

Elementos:
- Inercia: $\tau = J\alpha \;\to\; Js^2\Theta(s)$
- Torsión: $\tau = k\theta \;\to\; k\Theta(s)$
- Amortiguador: $\tau = b\omega \;\to\; bs\Theta(s)$

$$
\frac{\Theta(s)}{\tau(s)} = \frac{1}{Js^2 + bs + k}
$$

**Eléctricos:**

Leyes de Kirchhoff

Elementos en dominio $s$:
- Resistencia: $V = Ri \;\to\; RI(s)$
- Inductor: $V = L\frac{di}{dt} \;\to\; Ls\,I(s)$
- Capacitor: $V = \frac{1}{C}\int i\,dt \;\to\; \frac{I(s)}{Cs}$

Circuitos:
- RL: $\frac{V_{out}}{V_{in}} = \frac{R}{Ls + R}$
- RC: $\frac{V_{out}}{V_{in}} = \frac{1}{RCs + 1}$
- RLC: $\frac{V_{out}}{V_{in}} = \frac{1}{LCs^2 + RCs + 1}$

**Analogías:**

| Mecánico (traslacional) | Eléctrico | Mecánico (rotacional) |
|------------------------|-----------|----------------------|
| Fuerza $F$ | Voltaje $V$ | Torque $\tau$ |
| Velocidad $v$ | Corriente $i$ | Velocidad angular $\omega$ |
| Masa $m$ | Inductancia $L$ | Inercia $J$ |
| Resorte $k$ | Capacitancia $1/C$ | Torsión $k$ |
| Amortiguador $b$ | Resistencia $R$ | Amortiguador $b$ |

**Nivel de líquido:**

Ecuación: $q_{in} - q_{out} = A\frac{dh}{dt}$

Válvula lineal: $q_{out} = \frac{h}{R}$

Modelo: $RC\frac{dh}{dt} + h = R\,q_{in}$

$$
\frac{H(s)}{Q_{in}(s)} = \frac{R}{RCs + 1}
$$

$\tau = RC$, $K = R$

**Sistemas térmicos:**

Balance: $C\frac{dT}{dt} = q_{in} - \frac{T - T_{amb}}{R}$

Modelo: $RC\frac{dT}{dt} + T = R\,q_{in} + T_{amb}$

Variables de desviación: $T' = T - T_{amb}$

$$
\frac{T'(s)}{Q_{in}(s)} = \frac{R}{RCs + 1}
$$

### I.6 Espacio de Estados

Forma general:

$$
\begin{aligned}
\dot{\mathbf{x}} &= \mathbf{A}\mathbf{x} + \mathbf{B}u \\
y &= \mathbf{C}\mathbf{x} + \mathbf{D}u
\end{aligned}
$$

Relación con FT:

$$
G(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}
$$

Formas canónicas:
- Controlable
- Observable
- Diagonal (Jordan)
- Compañera

### I.7 Linealización

Punto de operación: $(\mathbf{x}_0, u_0)$

Expansión de Taylor:

$$
f(\mathbf{x},u) \approx f(\mathbf{x}_0,u_0) + \left.\frac{\partial f}{\partial \mathbf{x}}\right|_0 \cdot (\mathbf{x}-\mathbf{x}_0) + \left.\frac{\partial f}{\partial u}\right|_0 \cdot (u-u_0)
$$

Variables de desviación: $\delta\mathbf{x} = \mathbf{x} - \mathbf{x}_0$, $\delta u = u - u_0$, $\delta y = y - y_0$

Sistema linealizado:

$$
\begin{aligned}
\delta\dot{\mathbf{x}} &= \mathbf{A}\,\delta\mathbf{x} + \mathbf{B}\,\delta u \\
\delta y &= \mathbf{C}\,\delta\mathbf{x} + \mathbf{D}\,\delta u
\end{aligned}
$$

---

## Bloque II: Análisis de Respuesta Temporal

### II.1 Respuesta Transitoria

**Sistemas de primer orden:**

$$
G(s) = \frac{K}{\tau s + 1}
$$

Respuesta al escalón: $y(t) = K(1 - e^{-t/\tau})$

**Parámetros:**
- $\tau$: constante de tiempo
- $t_r$ (10-90\%): $2.2\tau$
- $t_s$ (2\%): $4\tau$
- $t_s$ (5\%): $3\tau$

**Sistemas de segundo orden:**

Forma estándar: $G(s) = \dfrac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$

**Casos:**
- $\zeta > 1$: sobreamortiguado (raíces reales distintas)
- $\zeta = 1$: críticamente amortiguado (raíces reales iguales)
- $0 < \zeta < 1$: subamortiguado (raíces complejas conjugadas)
- $\zeta = 0$: sin amortiguamiento (raíces imaginarias)

Respuesta subamortiguada (escalón unitario):

$$
y(t) = 1 - \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}} \sin(\omega_d t + \phi)
$$

donde $\omega_d = \omega_n\sqrt{1-\zeta^2}$, $\phi = \arccos(\zeta)$

**Especificaciones:**
- $t_p = \frac{\pi}{\omega_d}$
- $M_p = e^{-\pi\zeta/\sqrt{1-\zeta^2}} \times 100\%$
- $t_s$ (2\%) = $\frac{4}{\zeta\omega_n}$, $t_s$ (5\%) = $\frac{3}{\zeta\omega_n}$
- $t_r$ (0-100\%) = $\frac{\pi}{\omega_d}$, $t_r$ (10-90\%) $\approx \frac{1.8}{\omega_n}$ ($\zeta \approx 0.5$)

**Sistemas de orden superior:**
- Polos dominantes: los de menor parte real
- Reducción de orden: aproximar por polos dominantes
- Ceros: afectan sobreimpulso y velocidad

### II.2 Error en Estado Estacionario

$$
e_{ss} = \lim_{t\to\infty} e(t) = \lim_{s\to 0} sE(s) = \lim_{s\to 0} \frac{sR(s)}{1 + G(s)H(s)}
$$

Sistema tipo $N$: $G(s)H(s) = \frac{K}{s^N} G_0(s)$, con $G_0(0) = 1$

**Coeficientes de error:**

$$
K_p = \lim_{s\to 0} G(s)H(s) \quad \text{(error de posición)}
$$

$$
K_v = \lim_{s\to 0} s\,G(s)H(s) \quad \text{(error de velocidad)}
$$

$$
K_a = \lim_{s\to 0} s^2\,G(s)H(s) \quad \text{(error de aceleración)}
$$

**Errores estáticos:**

| Tipo | Escalón ($1/s$) | Rampa ($1/s^2$) | Parábola ($1/s^3$) |
|------|-----------------|-----------------|-------------------|
| 0 | $\frac{1}{1+K_p}$ | $\infty$ | $\infty$ |
| 1 | $0$ | $\frac{1}{K_v}$ | $\infty$ |
| 2 | $0$ | $0$ | $\frac{1}{K_a}$ |

### II.3 Estabilidad

**Definición:**
- Estable: todos los polos con $\operatorname{Re}(s) < 0$
- Marginalmente estable: polos en eje imaginario (sin parte real positiva)
- Inestable: algún polo con $\operatorname{Re}(s) > 0$

**Criterio de Routh-Hurwitz:**

$D(s) = a_n s^n + a_{n-1}s^{n-1} + \dots + a_1 s + a_0$

Tabla de Routh:

| $s^n$ | $a_n$ | $a_{n-2}$ | $a_{n-4}$ | $\dots$ |
|-------|-------|-----------|-----------|--------|
| $s^{n-1}$ | $a_{n-1}$ | $a_{n-3}$ | $a_{n-5}$ | $\dots$ |
| $s^{n-2}$ | $b_1$ | $b_2$ | $b_3$ | $\dots$ |
| $s^{n-3}$ | $c_1$ | $c_2$ | $c_3$ | $\dots$ |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | |
| $s^0$ | $h_1$ | | | |

donde:

$$
b_1 = \frac{a_{n-1}a_{n-2} - a_n a_{n-3}}{a_{n-1}},\quad
b_2 = \frac{a_{n-1}a_{n-4} - a_n a_{n-5}}{a_{n-1}},\quad \dots
$$

**Condiciones:**
- Necesaria: todos $a_i > 0$
- Suficiente: todos los elementos de la primera columna $> 0$

**Casos especiales:**
- Cero en primera columna: reemplazar por $\varepsilon \to 0$
- Fila completa de ceros: ecuación auxiliar, polos simétricos

---

## Bloque III: Lugar de las Raíces (LGR)

### III.1 Fundamentos

Ecuación característica: $1 + K\,G(s)H(s) = 0$

Condición de ángulo: $\angle G(s)H(s) = 180^\circ(2k+1)$

Condición de magnitud: $|G(s)H(s)| = \frac{1}{K}$

### III.2 Reglas de Construcción

1. Número de ramas: $n$ (número de polos)
2. Simetría: respecto al eje real
3. Segmentos en eje real: a la izquierda de número impar de polos + ceros
4. Asíntotas:
   - Centro: $\sigma_a = \frac{\sum p_i - \sum z_i}{n - m}$
   - Ángulos: $\theta_a = \frac{(2k+1)\pi}{n - m}$
5. Puntos de ruptura: $\frac{d}{ds}[G(s)H(s)] = 0$
6. Ángulos de salida/llegada:
   - Salida (polo complejo $p$): $180^\circ - \sum \angle(p-p_i) + \sum \angle(p-z_i)$
   - Llegada (cero complejo $z$): $180^\circ - \sum \angle(z-p_i) + \sum \angle(z-z_i)$
7. Cruce con eje imaginario: Routh-Hurwitz ($s = j\omega$)

### III.3 Diseño con LGR

**Compensador de adelanto (lead):**

$$
G_c(s) = K_c \frac{s+z}{s+p},\quad |z| < |p|
$$

**Procedimiento:**
1. Especificaciones: $\zeta$, $\omega_n$, $t_s$, $M_p$
2. Ubicar polos dominantes deseados: $s_d = -\zeta\omega_n \pm j\omega_n\sqrt{1-\zeta^2}$
3. Calcular ángulo faltante: $\phi = 180^\circ - \angle G(s_d)H(s_d)$
4. Ubicar cero en $-z$ y polo en $-p$ tal que $\angle(s_d+z) - \angle(s_d+p) = \phi$
5. Calcular $K_c$ de condición de magnitud

**Compensador de retardo (lag):**

$$
G_c(s) = K_c \frac{s+z}{s+p},\quad |z| > |p|
$$

**Procedimiento:**
1. Especificación: $K_v$ deseado
2. Seleccionar $\omega_{gc}$ actual donde $MF$ es suficiente
3. Calcular atenuación: $|G(j\omega_{gc})| = 1/\beta$
4. Ubicar cero y polo: $z = \omega_{gc}/10$, $p = z/\beta$
5. $K_c = K_{v\_deseado} / K_{v\_actual}$ (para compensar ganancia)

---

## Bloque IV: Respuesta en Frecuencia

### IV.1 Diagrama de Bode

$$
G(j\omega) = |G(j\omega)| e^{j\angle G(j\omega)}
$$

Magnitud (dB): $20\log|G(j\omega)|$

Fase (grados): $\angle G(j\omega)$

**Factores básicos:**

| Factor | Magnitud | Fase |
|--------|----------|------|
| $K$ | $20\log K$ (constante) | $0^\circ$ |
| $(j\omega)^N$ | $20N$ dB/déc | $90^\circ N$ |
| $(1 + j\omega/\omega_0)^{\pm 1}$ | $0$ dB, luego $\pm 20$ dB/déc | $0^\circ \to \pm 90^\circ$ |
| $[1 + 2\zeta(j\omega/\omega_n)+(j\omega/\omega_n)^2]^{\pm 1}$ | $0$ dB, pico en $\omega_n$ | $0^\circ \to \pm 180^\circ$ |

**Correcciones:**
- En $\omega = \omega_0$: error $\pm 3$ dB
- Pico de resonancia: $M_r = \frac{1}{2\zeta\sqrt{1-\zeta^2}}$ para $\zeta < 0.707$
- Frecuencia de resonancia: $\omega_r = \omega_n\sqrt{1-2\zeta^2}$

### IV.2 Margen de Fase y Ganancia

**Margen de fase (MF):**
- $\omega_{gc}$: frecuencia de cruce de ganancia ($|G| = 0$ dB)
- $MF = 180^\circ + \angle G(j\omega_{gc})$

**Margen de ganancia (MG):**
- $\omega_{pc}$: frecuencia de cruce de fase ($\angle G = -180^\circ$)
- $MG = -20\log|G(j\omega_{pc})|$ dB

**Relaciones con respuesta temporal (aproximadas):**
- $\zeta \approx MF/100$ (para $MF$ en grados)
- $M_p \approx 1/\sin(MF)$ ($MF$ en radianes)
- $\omega_{gc} \cdot t_s \approx 4/\tan(MF)$
- $\omega_{bw}$ (ancho de banda) $\approx \omega_{gc}$

### IV.3 Diagrama de Nyquist

Gráfica polar de $G(j\omega)$ para $\omega: -\infty \to \infty$

**Propiedades:**
- Simetría: $G(-j\omega) = \overline{G(j\omega)}$
- $\omega = 0$: punto en eje real
- $\omega \to \infty$: tiende al origen

**Criterio de Nyquist:**

$$
Z = N + P
$$

- $Z$: polos en lazo cerrado con $\operatorname{Re}(s) > 0$
- $N$: número de rodeos al punto $-1$ (positivo = antihorario)
- $P$: polos en lazo abierto con $\operatorname{Re}(s) > 0$

Estabilidad en lazo cerrado $\iff Z = 0$

**Casos especiales:**
- Polos en origen: rodear con semicírculo de radio $\varepsilon \to 0$
- Sistemas de fase no mínima: ceros en semiplano derecho

### IV.4 Diseño con Bode

**Compensación en adelanto (lead):**

$$
G_c(s) = K_c \frac{1 + \alpha\tau s}{1 + \tau s},\quad \alpha < 1
$$

Máximo adelanto de fase:

$$
\phi_m = \arcsin\left(\frac{1-\alpha}{1+\alpha}\right),\qquad
\omega_m = \frac{1}{\tau\sqrt{\alpha}}
$$

**Procedimiento:**
1. Determinar $K_c$ para error estático deseado
2. Trazar Bode de $G(s) = K_c \cdot G_0(s)$
3. Medir $MF$ actual
4. $\phi_m = MF_{deseado} - MF_{actual} + 5^\circ\text{ a }10^\circ$
5. $\alpha = \frac{1 - \sin\phi_m}{1 + \sin\phi_m}$
6. Ubicar $\omega_m$ en $\omega_{gc\_nueva}$: $|G(j\omega_m)|_{dB} = 10\log(1/\alpha)$
7. $\tau = \frac{1}{\omega_m\sqrt{\alpha}}$

**Compensación en atraso (lag):**

$$
G_c(s) = K_c \frac{1 + \beta\tau s}{1 + \tau s},\quad \beta > 1
$$

**Procedimiento:**
1. Determinar $K_c$ para error estático deseado
2. Trazar Bode de $G(s) = K_c \cdot G_0(s)$
3. Seleccionar $\omega_{gc\_nueva}$ donde $MF$ es suficiente
4. Medir atenuación: $|G(j\omega_{gc\_nueva})|_{dB} = 20\log\beta$
5. Ubicar cero: $\omega_z = \frac{\omega_{gc\_nueva}}{5} \text{ a } \frac{\omega_{gc\_nueva}}{10}$
6. $\tau = 1/\omega_z$, $p = 1/(\beta\tau)$

---

## Bloque V: Controladores PID

### V.1 Formas del Controlador

Forma ideal: $G_c(s) = K_p + \frac{K_i}{s} + K_d s$

Forma paralelo: $G_c(s) = K_p\left(1 + \frac{1}{T_i s} + T_d s\right)$
- $K_p = K_p$
- $K_i = K_p/T_i$
- $K_d = K_p T_d$

Forma serie: $G_c(s) = K_c \frac{\tau_i s + 1}{\tau_i s} \cdot (\tau_d s + 1)$

### V.2 Acciones de Control

| Acción | $G_c(s)$ | Efecto en tiempo | Efecto en frecuencia |
|--------|----------|------------------|---------------------|
| P | $K_p$ | Reduce error, puede aumentar $M_p$ | Aumenta ganancia, reduce $MF$ |
| I | $\frac{K_i}{s}$ | Elimina error estático | Añade $-90^\circ$, reduce $MF$ |
| D | $K_d s$ | Mejora amortiguamiento | Añade $+90^\circ$, amplifica ruido |
| PI | $K_p + \frac{K_i}{s}$ | Elimina error, puede aumentar $t_s$ | Lag, mejora error estático |
| PD | $K_p + K_d s$ | Mejora $t_s$, $M_p$ | Lead, mejora $MF$ |
| PID | $K_p + \frac{K_i}{s} + K_d s$ | Combina beneficios | Lag-lead |

### V.3 Sintonización Ziegler-Nichols

**Método de oscilación (lazo cerrado):**

Procedimiento:
- $K_u$: ganancia crítica (oscilación sostenida)
- $T_u$: período crítico

| Control | $K_p$ | $T_i$ | $T_d$ |
|---------|-------|-------|-------|
| P | $0.5 K_u$ | — | — |
| PI | $0.45 K_u$ | $T_u/1.2$ | — |
| PID | $0.6 K_u$ | $T_u/2$ | $T_u/8$ |

**Método de reacción (curva de reacción):**

Modelo: $G(s) = \dfrac{K e^{-Ls}}{Ts + 1}$

Procedimiento:
- Aplicar escalón a lazo abierto
- Medir: $K = \Delta y/\Delta u$, $L =$ retardo, $T =$ constante de tiempo

| Control | $K_p$ | $T_i$ | $T_d$ |
|---------|-------|-------|-------|
| P | $\frac{T}{KL}$ | — | — |
| PI | $\frac{0.9T}{KL}$ | $\frac{L}{0.3}$ | — |
| PID | $\frac{1.2T}{KL}$ | $2L$ | $0.5L$ |

### V.4 Relación PID - Compensadores

**PD $\leftrightarrow$ Compensador de adelanto (lead):**
- $G_c(s) = K_d (s + K_p/K_d)$
- Aumenta $MF$ y $\omega_{gc}$
- Mejora respuesta transitoria

**PI $\leftrightarrow$ Compensador de atraso (lag):**
- $G_c(s) = K_p \frac{s + K_i/K_p}{s}$
- Mejora error estático
- Puede reducir $MF$

**PID $\leftrightarrow$ Compensador de atraso-adelanto:**
- $G_c(s) = K_d \frac{s^2 + (K_p/K_d)s + K_i/K_d}{s}$
- Combina ventajas de ambos
- Mayor flexibilidad de diseño

---

## Bloque VI: Relaciones y Transformaciones

### VI.1 Dominio del Tiempo $\leftrightarrow$ Dominio de la Frecuencia

| Temporal | Frecuencia |
|----------|------------|
| $\zeta$ (amortiguamiento) | $MF$ (margen de fase) $\approx 100\zeta$ |
| $M_p$ (sobreimpulso) | $M_p \approx 1/\sin(MF)$ ($MF$ en rad) |
| $t_s$ (establecimiento) | $\omega_{gc} \cdot t_s \approx 4/\tan(MF)$ |
| $\omega_n$ (frecuencia natural) | $\omega_{gc} \approx \omega_n$ (para $\zeta \approx 0.7$) |
| Error estático | Ganancia en baja frecuencia |

### VI.2 Representaciones Equivalentes

$$
\begin{array}{ccccc}
\text{Ecuación diferencial} \\
\downarrow & & & & \\
\text{Función de transferencia} & & & & \\
G(s) = \mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B} + \mathbf{D} & & & & \\
\swarrow & & \searrow & & \\
\text{Espacio de estados} & & \text{Respuesta en frecuencia} & & \\
(\mathbf{A},\mathbf{B},\mathbf{C},\mathbf{D}) & & G(j\omega) & & \\
\searrow & & \swarrow & & \\
& \text{Lugar de las raíces} & & & \\
& 1 + K\,G(s)H(s) = 0 & & &
\end{array}
$$

### VI.3 Especificaciones de Diseño

| Dominio | Especificación | Expresión |
|---------|----------------|-----------|
| Tiempo | Sobreimpulso $M_p$ | $M_p = e^{-\pi\zeta/\sqrt{1-\zeta^2}}$ |
| Tiempo | Tiempo establecimiento $t_s$ | $t_s = \frac{4}{\zeta\omega_n}$ |
| Tiempo | Error estático $e_{ss}$ | Depende del tipo |
| Frecuencia | Margen de fase $MF$ | $MF = 180^\circ + \angle G(j\omega_{gc})$ |
| Frecuencia | Margen de ganancia $MG$ | $MG = -20\log|G(j\omega_{pc})|$ |
| Frecuencia | Ancho de banda $\omega_{bw}$ | Frecuencia donde $|G| = -3$ dB |

---

## Referencias Bibliográficas

1. Dorf, R. C., & Bishop, R. H. (2017). *Modern Control Systems* (13th ed.). Pearson.
2. Golnaraghi, F., & Kuo, B. C. (2017). *Automatic Control Systems* (10th ed.). McGraw-Hill.
3. Nise, N. S. (2014). *Control Systems Engineering* (7th ed.). Wiley.
4. Ogata, K. (2010). *Ingeniería de Control Moderna* (5th ed.). Pearson.