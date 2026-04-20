---
title: "Control Clásico - Sílabo Secuencial"
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
  - laplace
  - funcion-transferencia
  - lgr
  - bode
  - nyquist
  - pid
  - silabo
---

# Control Clásico — Sílabo Secuencial (por semanas)

## Semana 01: Introducción a los sistemas de control

### 1.1 Conceptos fundamentales
- Definición de sistemas y sistemas de control
- Lazo abierto vs. lazo cerrado
- Componentes de un sistema de control

### 1.2 Matemática base

$$
\frac{Y(s)}{R(s)} = \frac{G(s)}{1 + G(s)H(s)}
$$

- Sensibilidad: $S = \frac{\partial T/T}{\partial G/G} = \frac{1}{1 + GH}$
- Señal de error: $E(s) = \frac{R(s)}{1 + G(s)H(s)}$

### 1.3 Introducción al diseño
- Compensadores: concepto básico
- Especificaciones de desempeño

---

## Semana 02: Modelado Matemático de Sistemas de Control

### 2.1 Transformada de Laplace

$$
\mathcal{L}\{f(t)\} = F(s) = \int_0^\infty f(t)e^{-st}\,dt
$$

**Transformadas fundamentales:**

| $f(t)$ | $F(s)$ |
|--------|--------|
| $\delta(t)$ | $1$ |
| $u(t)$ | $\frac{1}{s}$ |
| $t^n$ | $\frac{n!}{s^{n+1}}$ |
| $e^{-at}$ | $\frac{1}{s+a}$ |
| $\sin(\omega t)$ | $\frac{\omega}{s^2+\omega^2}$ |
| $\cos(\omega t)$ | $\frac{s}{s^2+\omega^2}$ |

**Propiedades:**
- Derivación: $\mathcal{L}\{f'(t)\} = sF(s) - f(0)$
- Integración: $\mathcal{L}\left\{\int f(t)\,dt\right\} = \frac{F(s)}{s}$
- Traslación: $\mathcal{L}\{e^{-at}f(t)\} = F(s+a)$
- Convolución: $\mathcal{L}\{f * g\} = F(s)G(s)$

### 2.2 Función de transferencia

$$
G(s) = \frac{Y(s)}{U(s)} = \frac{N(s)}{D(s)}
$$

- Polos: raíces de $D(s) = 0$
- Ceros: raíces de $N(s) = 0$
- Orden: grado de $D(s)$

### 2.3 Espacio de estados

$$
\begin{aligned}
\dot{\mathbf{x}} &= \mathbf{A}\mathbf{x} + \mathbf{B}u \\
y &= \mathbf{C}\mathbf{x} + \mathbf{D}u
\end{aligned}
$$

$$
G(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}
$$

### 2.4 Linealización

Punto de operación: $(\mathbf{x}_0, u_0)$

$$
f(\mathbf{x},u) \approx f(\mathbf{x}_0,u_0) + \left.\frac{\partial f}{\partial \mathbf{x}}\right|_0 \cdot (\mathbf{x}-\mathbf{x}_0) + \left.\frac{\partial f}{\partial u}\right|_0 \cdot (u-u_0)
$$

Variables de desviación: $\delta\mathbf{x} = \mathbf{x} - \mathbf{x}_0$, $\delta u = u - u_0$

### 2.5 MATLAB
- `tf`, `ss`, `tf2ss`, `ss2tf`
- `step`, `impulse`, `lsim`

---

## Semana 03: Modelado de Sistemas Mecánicos y Eléctricos

### 3.1 Sistemas mecánicos traslacionales

Ley de Newton: $\sum F = m\frac{d^2x}{dt^2}$

**Elementos:**
- Masa: $F = m a \;\to\; ms^2X(s)$
- Resorte: $F = kx \;\to\; kX(s)$
- Amortiguador: $F = bv \;\to\; bsX(s)$

Ecuación general: $m\ddot{x} + b\dot{x} + kx = F(t)$

$$
\frac{X(s)}{F(s)} = \frac{1}{ms^2 + bs + k}
$$

### 3.2 Sistemas mecánicos rotacionales

$$
\sum \tau = J\frac{d^2\theta}{dt^2}
$$

**Elementos:**
- Inercia: $\tau = J\alpha \;\to\; Js^2\Theta(s)$
- Torsión: $\tau = k\theta \;\to\; k\Theta(s)$
- Amortiguador rotacional: $\tau = b\omega \;\to\; bs\Theta(s)$

$$
\frac{\Theta(s)}{\tau(s)} = \frac{1}{Js^2 + bs + k}
$$

### 3.3 Sistemas eléctricos

Leyes de Kirchhoff

**Elementos en dominio $s$:**
- Resistencia: $V = Ri \;\to\; RI(s)$
- Inductor: $V = L\frac{di}{dt} \;\to\; Ls\,I(s)$
- Capacitor: $V = \frac{1}{C}\int i\,dt \;\to\; \frac{I(s)}{Cs}$

Circuito RLC serie:

$$
\frac{V_{out}(s)}{V_{in}(s)} = \frac{1}{LCs^2 + RCs + 1}
$$

### 3.4 Analogías

| Mecánico (traslacional) | Eléctrico |
|------------------------|-----------|
| Fuerza $F$ | Voltaje $V$ |
| Velocidad $v$ | Corriente $i$ |
| Masa $m$ | Inductancia $L$ |
| Resorte $k$ | Capacitancia $1/C$ |
| Amortiguador $b$ | Resistencia $R$ |

---

## Semana 04: Modelado de Sistemas de Fluidos y Térmicos

### 4.1 Sistemas de nivel líquido

Ecuación de continuidad: $q_{in} - q_{out} = A\frac{dh}{dt}$

Válvula lineal: $q_{out} = \frac{h}{R}$

Modelo: $RC\frac{dh}{dt} + h = R\,q_{in}$

$$
\frac{H(s)}{Q_{in}(s)} = \frac{R}{RCs + 1}
$$

$\tau = RC$ (constante de tiempo), $K = R$ (ganancia estática)

### 4.2 Sistemas neumáticos

Flujo másico: $q_m = \frac{P_{in} - P_{out}}{R}$

Capacitancia: $C = \frac{d(\rho V)}{dP}$

$\tau = RC$

### 4.3 Sistemas térmicos

Balance de energía: $C\frac{dT}{dt} = q_{in} - \frac{T - T_{amb}}{R}$

Modelo: $RC\frac{dT}{dt} + T = R\,q_{in} + T_{amb}$

Variables de desviación: $T' = T - T_{amb}$

$$
\frac{T'(s)}{Q_{in}(s)} = \frac{R}{RCs + 1}
$$

### 4.4 Práctica calificada 01 (Semana 04)

---

## Semana 05: Análisis de Respuesta Transitoria y Estacionaria

### 5.1 Sistemas de primer orden

$$
G(s) = \frac{K}{\tau s + 1}
$$

Respuesta al escalón: $y(t) = K(1 - e^{-t/\tau})$

**Parámetros:**
- $t_s$ (2\%): $4\tau$
- $t_s$ (5\%): $3\tau$
- $t_r$ (10\%-90\%): $2.2\tau$

### 5.2 Sistemas de segundo orden

Forma estándar: $G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$

**Casos:**
- $\zeta > 1$: sobreamortiguado
- $\zeta = 1$: críticamente amortiguado
- $0 < \zeta < 1$: subamortiguado

Respuesta subamortiguada (escalón unitario):

$$
y(t) = 1 - \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}} \sin(\omega_d t + \phi)
$$

donde $\omega_d = \omega_n\sqrt{1-\zeta^2}$, $\phi = \arccos(\zeta)$

**Especificaciones:**
- $t_p = \frac{\pi}{\omega_d}$
- $M_p = e^{-\pi\zeta/\sqrt{1-\zeta^2}} \times 100\%$
- $t_s (2\%) = \frac{4}{\zeta\omega_n}$, $t_s (5\%) = \frac{3}{\zeta\omega_n}$
- $t_r \approx \frac{1.8}{\omega_n}$ (para $\zeta \approx 0.5$)

### 5.3 Sistemas de orden superior
- Polos dominantes
- Reducción de orden

### 5.4 Criterio de Routh-Hurwitz

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

**Condición de estabilidad:**
- Necesaria: todos $a_i > 0$
- Suficiente: todos los elementos de la primera columna $> 0$

### 5.5 Error en estado estacionario

$$
e_{ss} = \lim_{s\to 0} sE(s) = \lim_{s\to 0} \frac{sR(s)}{1 + G(s)H(s)}
$$

Sistema tipo $N$: $G(s)H(s) = \frac{K}{s^N} G_0(s)$, con $G_0(0) = 1$

Coeficientes de error:

$$
K_p = \lim_{s\to 0} G(s)H(s),\qquad
K_v = \lim_{s\to 0} sG(s)H(s),\qquad
K_a = \lim_{s\to 0} s^2 G(s)H(s)
$$

**Errores estáticos:**

| Tipo | Escalón ($1/s$) | Rampa ($1/s^2$) | Parábola ($1/s^3$) |
|------|-----------------|-----------------|-------------------|
| 0 | $\frac{1}{1+K_p}$ | $\infty$ | $\infty$ |
| 1 | $0$ | $\frac{1}{K_v}$ | $\infty$ |
| 2 | $0$ | $0$ | $\frac{1}{K_a}$ |

---

## Semana 06: Lugar de las Raíces (Parte 1)

### 6.1 Ecuación característica

$$
1 + K\,G(s)H(s) = 0
$$

**Condición de ángulo:** $\angle G(s)H(s) = 180^\circ(2k+1)$

**Condición de magnitud:** $|G(s)H(s)| = \frac{1}{K}$

### 6.2 Reglas de construcción

- Número de ramas: $n$ (número de polos)
- Simetría: respecto al eje real
- Segmentos en eje real: a la izquierda de número impar de polos + ceros
- Asíntotas:
  - Centro: $\sigma_a = \frac{\sum p_i - \sum z_i}{n - m}$
  - Ángulos: $\theta_a = \frac{(2k+1)\pi}{n - m}$
- Puntos de ruptura: $\frac{d}{ds}[G(s)H(s)] = 0$
- Cruce con eje imaginario: Routh-Hurwitz

---

## Semana 07: Lugar de las Raíces (Parte 2) y Diseño

### 7.1 Ángulos de salida/llegada

Ángulo de salida (polo complejo $p$):

$$
\theta_{salida} = 180^\circ - \sum \angle(p - p_i) + \sum \angle(p - z_i)
$$

Ángulo de llegada (cero complejo $z$):

$$
\theta_{llegada} = 180^\circ - \sum \angle(z - p_i) + \sum \angle(z - z_i)
$$

### 7.2 Compensación vía LGR

**Adelanto (Lead):**

$$
G_c(s) = K_c \frac{s + z}{s + p},\quad |z| < |p|
$$

- Efecto: desplaza LGR hacia la izquierda
- Objetivo: aumentar $\zeta$ y $\omega_n$
- Procedimiento: ubicar cero en $-z$, polo en $-p$ según especificaciones

**Retardo (Lag):**

$$
G_c(s) = K_c \frac{s + z}{s + p},\quad |z| > |p|
$$

- Efecto: aumenta ganancia estática
- Objetivo: mejorar error en estado estacionario
- Procedimiento: $z$ y $p$ pequeños, $z/p \approx K_{v\_deseado}/K_{v\_actual}$

**Retardo-Adelanto:**

$$
G_c(s) = K_c \frac{s + z_1}{s + p_1} \cdot \frac{s + z_2}{s + p_2},\quad |z_1| < |p_1|,\; |z_2| > |p_2|
$$

### 7.3 Práctica calificada 02 (Semana 07)

---

## Semana 08: Examen Parcial

---

## Semana 09: Diagrama de Bode

### 9.1 Respuesta en frecuencia

$$
G(j\omega) = |G(j\omega)| e^{j\angle G(j\omega)}
$$

Magnitud (dB): $20\log|G(j\omega)|$

Fase (grados): $\angle G(j\omega)$

### 9.2 Factores básicos

| Factor | Magnitud (dB) | Fase (grados) |
|--------|---------------|---------------|
| $K$ | $20\log K$ (constante) | $0^\circ$ |
| $(j\omega)^{\pm 1}$ | $\pm 20$ dB/déc | $\pm 90^\circ$ |
| $(1 + j\omega/\omega_0)^{\pm 1}$ | $0$ dB, luego $\pm 20$ dB/déc | $0^\circ \to \pm 90^\circ$ |
| $[1 + 2\zeta(j\omega/\omega_n) + (j\omega/\omega_n)^2]^{\pm 1}$ | pico en $\omega_n$ | $0^\circ \to \pm 180^\circ$ |

### 9.3 Construcción de diagrama

1. Escribir $G(j\omega)$ en forma de factores
2. Identificar frecuencias de esquina
3. Dibujar asíntotas de magnitud
4. Corregir cerca de esquinas ($3$ dB en $\omega_0$)
5. Dibujar fase sumando contribuciones

### 9.4 Sistemas de fase mínima
- Todos los ceros en semiplano izquierdo
- Relación única entre magnitud y fase

---

## Semana 10: Criterio de Nyquist

### 10.1 Diagrama polar

Gráfica de $G(j\omega)$ para $\omega: 0 \to \infty$

- $\omega = 0$: punto en eje real
- $\omega \to \infty$: tiende al origen
- Sentido: $\omega$ creciente

### 10.2 Criterio de Nyquist

$$
Z = N + P
$$

- $Z$: polos en lazo cerrado con $\operatorname{Re}(s) > 0$
- $N$: número de rodeos al punto $-1$ (positivo = antihorario)
- $P$: polos en lazo abierto con $\operatorname{Re}(s) > 0$

Estable en lazo cerrado $\iff Z = 0$

### 10.3 Estabilidad relativa

**Margen de fase (MF):**
- $\omega_{gc}$: frecuencia de cruce de ganancia ($|G| = 0$ dB)
- $MF = 180^\circ + \angle G(j\omega_{gc})$

**Margen de ganancia (MG):**
- $\omega_{pc}$: frecuencia de cruce de fase ($\angle G = -180^\circ$)
- $MG = -20\log|G(j\omega_{pc})|$ dB

---

## Semana 11: Diseño de Compensadores vía LGR (Repaso)

### 11.1 Configuraciones de compensador

- Serie: $G_c(s) = K_c \frac{s+z}{s+p}$
- Realimentación: $G_c(s) = K_c \cdot \frac{s+z}{s+p}$
- Paralelo: $G_c(s) = K_c \cdot (1 + K_d s)$

### 11.2 Efecto de añadir polos/ceros

**Cero:**
- Atrae al LGR
- Mejora estabilidad relativa
- Aumenta ancho de banda

**Polo:**
- Repulsa al LGR
- Degrada estabilidad
- Reduce ancho de banda

### 11.3 Práctica calificada 03 (Semana 11)

---

## Semana 12: Diseño de Compensadores vía Bode

### 12.1 Compensación en adelanto (lead)

$$
G_c(s) = K_c \frac{1 + \alpha\tau s}{1 + \tau s},\quad \alpha < 1
$$

Máximo adelanto de fase:

$$
\phi_m = \arcsin\left(\frac{1-\alpha}{1+\alpha}\right),\qquad
\omega_m = \frac{1}{\tau\sqrt{\alpha}}
$$

**Procedimiento:**
1. Determinar $K_c$ para error estático
2. Medir $MF$ actual
3. $\phi_m = MF_{deseado} - MF_{actual} + 5^\circ\text{ a }10^\circ$
4. $\alpha = \frac{1 - \sin\phi_m}{1 + \sin\phi_m}$
5. Ubicar $\omega_m$ en nueva $\omega_{gc}$: $|G(j\omega_m)|_{dB} = 10\log(1/\alpha)$
6. $\tau = \frac{1}{\omega_m\sqrt{\alpha}}$

### 12.2 Compensación en atraso (lag)

$$
G_c(s) = K_c \frac{1 + \beta\tau s}{1 + \tau s},\quad \beta > 1
$$

**Procedimiento:**
1. Determinar $K_c$ para error estático
2. Medir $MF$ actual
3. Seleccionar $\omega_{gc\_nueva}$ donde $MF$ es suficiente
4. Atenuación: $20\log\beta = |G(j\omega_{gc\_nueva})|_{dB}$
5. $\tau = \frac{10}{\omega_{gc\_nueva}}$

### 12.3 Compensador atraso-adelanto

$$
G_c(s) = K_c \frac{1 + \tau_1 s}{1 + \alpha\tau_1 s} \cdot \frac{1 + \tau_2 s}{1 + \tau_2 s/\beta},\quad \alpha > 1,\; \beta > 1
$$

- Sección adelanto: mejora $MF$ y ancho de banda
- Sección atraso: mejora error estático

---

## Semana 13: Controladores PID

### 13.1 Formas del controlador

Forma ideal: $G_c(s) = K_p + \frac{K_i}{s} + K_d s$

Forma paralelo: $G_c(s) = K_p\left(1 + \frac{1}{T_i s} + T_d s\right)$
- $K_p = K_p$
- $K_i = K_p/T_i$
- $K_d = K_p T_d$

Forma serie: $G_c(s) = K_c \frac{\tau_i s + 1}{\tau_i s} \cdot (\tau_d s + 1)$

### 13.2 Acciones de control

**Proporcional (P):** $G_c(s) = K_p$
- Reduce error estático
- Aumenta ganancia → reduce estabilidad
- Error estático = $\frac{1}{1+K_p}$ para tipo 0

**Integral (I):** $G_c(s) = \frac{K_i}{s}$
- Elimina error estático
- Aumenta tipo del sistema en 1
- Añade $-90^\circ$ de fase → desestabiliza

**Derivativo (D):** $G_c(s) = K_d s$
- Adelanto de fase → mejora estabilidad
- Amplifica ruido
- No afecta error estático

### 13.3 Combinaciones

**PI:**
$$
G_c(s) = K_p + \frac{K_i}{s} = K_p \frac{s + K_i/K_p}{s}
$$
- Elimina error estático
- Compensador tipo atraso (lag)
- Diseño: ubicar cero cerca del origen

**PD:**
$$
G_c(s) = K_p + K_d s = K_d \left(s + \frac{K_p}{K_d}\right)
$$
- Mejora transitoria
- Compensador tipo adelanto (lead)
- Diseño: ubicar cero para aumentar $\zeta$

**PID:**
$$
G_c(s) = K_p + \frac{K_i}{s} + K_d s = K_d \frac{s^2 + (K_p/K_d)s + K_i/K_d}{s}
$$
- Cero doble + integrador
- Compensador tipo atraso-adelanto
- Mayor flexibilidad de diseño

### 13.4 Reglas de sintonización Ziegler-Nichols

**Método de oscilación:**

| Control | $K_p$ | $T_i$ | $T_d$ |
|---------|-------|-------|-------|
| P | $0.5 K_u$ | — | — |
| PI | $0.45 K_u$ | $T_u/1.2$ | — |
| PID | $0.6 K_u$ | $T_u/2$ | $T_u/8$ |

**Método de reacción (curva de reacción):**

Modelo: $G(s) = \dfrac{K e^{-Ls}}{Ts + 1}$

| Control | $K_p$ | $T_i$ | $T_d$ |
|---------|-------|-------|-------|
| P | $\frac{T}{KL}$ | — | — |
| PI | $\frac{0.9T}{KL}$ | $\frac{L}{0.3}$ | — |
| PID | $\frac{1.2T}{KL}$ | $2L$ | $0.5L$ |

---

## Semana 14: Análisis de Controladores PID

### 14.1 Análisis en dominio del tiempo

**PD:** $G_c(s) = K_p + K_d s$
- Efecto: añade cero en $s = -K_p/K_d$
- Resultado: aumenta $\zeta$, reduce $t_s$
- Limitación: amplifica ruido

**PI:** $G_c(s) = K_p \frac{s + K_i/K_p}{s}$
- Efecto: añade polo en origen y cero real
- Resultado: elimina error estático
- Limitación: reduce margen de fase

**PID:** $G_c(s) = K_d \frac{s^2 + (K_p/K_d)s + K_i/K_d}{s}$
- Efecto: dos ceros + integrador
- Resultado: mejora transitoria y elimina error
- Requiere: sintonización cuidadosa

### 14.2 Análisis en dominio de la frecuencia

**PD $\leftrightarrow$ Lead:**
- Aumenta $MF$
- Aumenta $\omega_{gc}$
- Mejora ancho de banda

**PI $\leftrightarrow$ Lag:**
- Aumenta ganancia en bajas frecuencias
- Reduce error estático
- Puede reducir $MF$ si no se diseña bien

### 14.3 Repaso integrador
- LGR: diseño por ubicación de polos dominantes
- Bode: diseño por márgenes de fase y ganancia
- PID: sintonización empírica

### 14.4 Práctica calificada 04 (Semana 14)

---

## Semana 15: Repaso y Proyecto Integrador

### 15.1 Temas de repaso
- Modelado de sistemas
- Análisis de respuesta temporal
- Estabilidad (Routh-Hurwitz, LGR, Nyquist)
- Diseño en frecuencia (Bode)
- Controladores PID

### 15.2 Proyecto integrador

**Estructura:**
1. Selección de planta (física o propuesta)
2. Modelado matemático
3. Análisis de desempeño actual
4. Especificaciones de diseño
5. Selección y diseño del compensador/PID
6. Simulación y validación
7. Documentación de resultados

---

## Evaluación

| Evaluación | Semana | Peso |
|------------|--------|------|
| Práctica Calificada 01 | 04 | 25% del PP |
| Práctica Calificada 02 | 07 | 25% del PP |
| Práctica Calificada 03 | 11 | 25% del PP |
| Práctica Calificada 04 | 14 | 25% del PP |
| Examen Parcial | 08 | 25% del PF |
| Examen Final | 16 | 50% del PF |

**Fórmula:**

$$
PF = \frac{1\cdot EP + 2\cdot EF + 1\cdot PP}{4}
$$