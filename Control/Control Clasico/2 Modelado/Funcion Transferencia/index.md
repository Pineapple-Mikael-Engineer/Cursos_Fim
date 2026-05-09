---
title: Función Transferencia
tags:
  - control-clasico
  - teoria
  - modelado
draft: false
aliases:
  - FT
  - G(s)
  - función de transferencia
---

# Función Transferencia

> [!definicion] Definición
> $$G(s) = \frac{Y(s)}{U(s)} \bigg|_{\text{CI}=0}$$
> 
> - $Y(s) = \mathcal{L}\{y(t)\}$, $U(s) = \mathcal{L}\{u(t)\}$
> - **Condiciones iniciales nulas**: $y^{(k)}(0^-)=0$, $u^{(k)}(0^-)=0$ ∀k
> - Existe solo para sistemas **LTI** (lineales e invariantes en el tiempo)
> 
> Forma racional (para LTI):
> $$G(s) = \frac{b_m s^m + b_{m-1}s^{m-1} + \dots + b_0}{a_n s^n + a_{n-1}s^{n-1} + \dots + a_0}, \quad n \ge m$$

> [!info] Caso EDO
> Dada $a_n y^{(n)} + \dots + a_0 y = b_m u^{(m)} + \dots + b_0 u$:
> $$G(s) = \frac{b_m s^m + \dots + b_0}{a_n s^n + \dots + a_0}$$
> Los coeficientes pasan directamente.

> [!ejemplo] Masa-resorte-amortiguador
> $$m\ddot{y} + b\dot{y} + ky = u$$
> Aplicando Laplace: $(ms^2 + bs + k)Y(s) = U(s)$
> $$G(s) = \frac{1}{ms^2 + bs + k}$$
> - **Orden**: 2
> - **Polos**: $\frac{-b \pm \sqrt{b^2-4mk}}{2m}$
> - **Ganancia estática**: $G(0) = 1/k$

> [!ejemplo] Circuito RC
> $$RC\dot{v}_o + v_o = v_i$$
> $$G(s) = \frac{1}{RCs + 1}$$
> - **Orden**: 1
> - **Polo**: $s = -1/(RC)$
> - **Ganancia estática**: $G(0) = 1$
> - **Constante de tiempo**: $\tau = RC$

> [!ejemplo] Motor DC (velocidad)
> $$J\dot{\omega} + b\omega = K_t i_a$$
> Con $i_a$ entrada, $\omega$ salida:
> $$G(s) = \frac{K_t}{Js + b}$$
> - **Orden**: 1
> - **Polo**: $s = -b/J$
> - **Ganancia estática**: $K_t/b$

---

## Conexiones

> [!info] Álgebra de diagramas
> | Conexión | $G_{eq}(s)$ |
> |----------|--------------|
> | Serie | $G_1 G_2$ |
> | Paralelo | $G_1 + G_2$ |
> | Realimentación unitaria negativa | $\frac{G}{1+G}$ |
> | Realimentación general | $\frac{G}{1+GH}$ |
> 
> Ver [[Algebra Diagramas]] para reducción sistemática.

---

## Parámetros fundamentales

> [!definicion] Polos
> Raíces del denominador: $a_n s^n + \dots + a_0 = 0$
> - Determinan [[Polos Ceros|modos naturales]]: $y_{\text{natural}}(t) \propto e^{p_i t}$
> - **Estabilidad BIBO**: todos los polos con $\Re(p_i) < 0$
> - Margina: $\Re(p_i)=0$ simple
> - Inestable: $\Re(p_i) > 0$ o múltiples en eje imaginario
> 
> Ver [[Polos Ceros]] para cancelaciones, respuesta modal y lugar geométrico.

> [!definicion] Ceros
> Raíces del numerador: $b_m s^m + \dots + b_0 = 0$
> - Bloquean modos: si cero = polo, ese modo no aparece en salida
> - **Cancelación polo-cero**: peligroso si polo inestable (el estado interno diverge)
> 
> Ver [[Polos Ceros#Cancelación polo-cero]] para ejemplos.

> [!definicion] Orden
> Grado del denominador **tras cancelar** factores comunes con numerador.
> $$G(s) = \frac{s+1}{(s+1)(s+2)} = \frac{1}{s+2} \implies \text{orden } 1$$
> 
> Ver [[Orden]] para reducción de orden y sistemas de orden superior.

> [!definicion] Ganancia estática
> $$G(0) = \frac{b_0}{a_0} \quad (\text{si } a_0 \neq 0)$$
> - Interpretación: amplificación en DC (régimen permanente)
> - Para escalón unitario: $\lim_{t\to\infty} y(t) = G(0)$ (ver [[Teorema Valor Inicial Final]])
> - Bajo realimentación unitaria, [[Error Estacionario]] de posición: $e_{ss} = 1/(1+G(0))$ (sistemas tipo 0)
> 
> Ver [[Ganancia Estatica]] para tabla por tipo de sistema.

> [!teorema] Teoremas del valor final e inicial
> **TVF** (si polos de $sG(s)U(s)$ en $\Re(s)<0$, excepto posible $s=0$ simple):
> $$\lim_{t\to\infty} y(t) = \lim_{s\to 0} s G(s) U(s)$$
> 
> **TVI**:
> $$y(0^+) = \lim_{s\to\infty} s G(s) U(s)$$
> 
> Ver [[Teorema Valor Inicial Final]] para demostraciones y contraejemplos.

---

## Relaciones con otras representaciones

> [!info] Respuesta impulsional
> $g(t) = \mathcal{L}^{-1}\{G(s)\}$ es respuesta a $u(t)=\delta(t)$, CI=0.
> Por [[Convolucion]]:
> $$y(t) = (g * u)(t) = \int_0^t g(t-\tau) u(\tau) d\tau$$
> En Laplace: $Y(s) = G(s)U(s)$.

> [!info] Espacio de estados
> Dado $\dot{x}=Ax+Bu$, $y=Cx+Du$, con $x(0)=0$:
> $$G(s) = C(sI-A)^{-1}B + D$$
> 
> Ver [[Pasar a FT]] para ejemplos numéricos y [[Espacio Estados]] para ventajas (CI no nulas, controlabilidad, observabilidad).

---

## Casos prácticos frecuentes

> [!ejemplo] Primer orden
> $$G(s) = \frac{K}{\tau s + 1}$$
> - Polo: $s = -1/\tau$
> - $t_s = 4\tau$ (2%), $t_r = 2.2\tau$
> - Ver [[Respuesta Temporal/Primer Orden]]

> [!ejemplo] Segundo orden subamortiguado
> $$G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$$
> - Polos: $-\zeta\omega_n \pm j\omega_n\sqrt{1-\zeta^2}$
> - $M_p = e^{-\pi\zeta/\sqrt{1-\zeta^2}}$
> - $T_s = 4/(\zeta\omega_n)$ (2%)
> - Ver [[Respuesta Temporal/Segundo Orden]]

> [!ejemplo] Integrador
> $$G(s) = \frac{K}{s}$$
> - Polo en $s=0$
> - Respuesta a escalón: $y(t)=Kt \cdot u(t)$ (rampa)
> - Error estacionario nulo a escalón bajo realimentación

> [!ejemplo] Derivador (no realizable puro)
> $$G(s) = Ks$$
> - Cero en $s=0$
> - Respuesta a escalón: impulso
> - En práctica: $G(s) = \frac{Ks}{\tau s + 1}$ (derivador filtrado)

---

## Limitaciones

> [!warning] Lo que $G(s)$ NO puede hacer
> 1. **CI no nulas**: $G(s)$ supone $x(0)=0$. Para CI arbitrarias, usar [[Espacio Estados]].
> 2. **Estabilidad interna**: Cancelar polo inestable da $G(s)$ estable pero el sistema internamente diverge.
>    $$G(s) = \frac{s-1}{s-1} \cdot \frac{1}{s+1} = \frac{1}{s+1}$$
>    Canceló polo $s=1$ (inestable). Salida estable, estado interno $x(t)=e^t$ diverge.
> 3. **No linealidad / variación temporal**: $G(s)$ no existe. Usar [[Linealizacion]] local o representaciones alternativas.
> 
> Ver [[Espacio Estados]] para análisis completo.

---

## Para diseño y análisis

> [!info] Uso típico
> - **Análisis**: estabilidad (polos), respuesta temporal (polos dominantes), error estacionario (tipo, ganancia estática)
> - **Diseño**: [[Lugar Raices]] (modificar polos), [[Respuesta Frecuencia]] (márgenes), [[PID]] (compensadores)
> - **Realimentación**: $T(s) = \frac{G}{1+GH}$ define dinámica de lazo cerrado