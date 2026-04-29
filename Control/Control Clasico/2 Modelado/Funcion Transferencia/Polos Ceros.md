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

# Definición

> [!definicion] Polos
> Raíces del denominador de $G(s) = N(s)/D(s)$:
> $$D(p_i) = 0$$
> 
> $G(s) \to \infty$ cuando $s \to p_i$.
> 
> Ver [[Funcion Transferencia/index | función transferencia]].

> [!definicion] Ceros
> Raíces del numerador de $G(s) = N(s)/D(s)$:
> $$N(z_i) = 0$$
> 
> $G(s) \to 0$ cuando $s \to z_i$.

# Modos naturales

> [!teorema] Relación polo-modo
> Cada polo $p_i$ aporta un **modo natural** a la respuesta homogénea:
> 
> | Tipo de polo | Modo natural $y_h(t)$ |
> |--------------|----------------------|
> | Real simple $p$ | $C e^{pt}$ |
> | Real múltiple (orden $r$) | $(C_0 + C_1 t + \dots + C_{r-1} t^{r-1}) e^{pt}$ |
> | Par complejo conjugado $\sigma \pm j\omega$ | $e^{\sigma t}(A \cos \omega t + B \sin \omega t)$ |
> | Par complejo múltiple (orden $r$) | $e^{\sigma t} \cdot (\text{polinomio en } t) \cdot (A \cos \omega t + B \sin \omega t)$ |

> [!ejemplo] Polos reales distintos
> $$G(s) = \frac{6}{(s+1)(s+2)(s+3)}$$
> Fracciones parciales:
> $$G(s) = \frac{3}{s+1} - \frac{6}{s+2} + \frac{3}{s+3}$$
> Modos: $e^{-t}$, $e^{-2t}$, $e^{-3t}$

> [!ejemplo] Par complejo
> $$G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$$
> Polos: $-\zeta\omega_n \pm j\omega_n\sqrt{1-\zeta^2}$, $\quad \omega_d = \omega_n\sqrt{1-\zeta^2}$
> Modo: $e^{-\zeta\omega_n t} \sin(\omega_d t + \phi)$
> 
> Ver [[Segundo Orden/index | respuesta de segundo orden]].

# Estabilidad

> [!definicion] Estabilidad BIBO
> Un sistema es BIBO estable (entrada acotada → salida acotada) **si y solo si** todos los polos tienen parte real estrictamente negativa:
> $$\Re(p_i) < 0 \quad \forall i$$
> 
> Ver [[Estabilidad/index | estabilidad]] para criterios alternativos (Routh-Hurwitz).

> [!info] Clasificación según polos
> | Condición | Estabilidad |
> |-----------|-------------|
> | $\Re(p_i) < 0$ para todo $i$ | **Asintóticamente estable** |
> | $\Re(p_i) \le 0$; polos en eje imaginario simples; resto $\Re < 0$ | **Marginalmente estable** |
> | Algún $\Re(p_i) > 0$ | **Inestable** |
> | Polo en eje imaginario con multiplicidad $\ge 2$ | **Inestable** |

> [!ejemplo] Tabla de estabilidad
> | Polos | Estabilidad | Respuesta característica |
> |-------|-------------|--------------------------|
> | $-2$ | Estable | $e^{-2t}$ (decae) |
> | $-0.1$ | Estable | $e^{-0.1t}$ (decae lento) |
> | $0$ (simple) | Marginal | constante o rampa |
> | $0$ (doble) | Inestable | $t$ (crece linealmente) |
> | $0.5$ | Inestable | $e^{0.5t}$ (crece exponencial) |
> | $\pm j3$ (simples) | Marginal | $\sin 3t$ (oscila) |
> | $\pm j3$ (dobles) | Inestable | $t \sin 3t$ (oscila creciente) |
> | $-0.1 \pm j2$ | Estable | $e^{-0.1t}\sin 2t$ (oscila amortiguada) |
> | $0.1 \pm j2$ | Inestable | $e^{0.1t}\sin 2t$ (oscila creciente) |

# Cancelación polo-cero

> [!definicion] Cancelación
> Un polo $p$ y un cero $z$ se cancelan si $p = z$. El factor $(s-p)$ desaparece de $G(s)$.

> [!ejemplo] Cancelación aparente
> $$G(s) = \frac{(s-1)}{(s-1)(s+2)} = \frac{1}{s+2}$$
> Polo en $s=1$ "desaparece" de $G(s)$.

> [!warning] Peligro: cancelación de polos inestables
> Si se cancela un polo con $\Re(p) \ge 0$, el modo asociado **sigue existiendo internamente** aunque no aparezca en la salida.
> 
> **Ejemplo:**
> $$\dot{x} = x + u, \quad y = x - u$$
> $$G(s) = \frac{1}{s-1} - 1 = \frac{2-s}{s-1} = \frac{s-2}{-(s-1)}$$
> Hay cancelación aparente del polo $s=1$. La salida puede ser estable, pero el estado $x$ diverge si se excita.
> 
> **Regla:** Nunca cancelar polos inestables a menos que se tenga control total sobre el estado interno.
> 
> Ver [[Espacio Estados/index | espacio de estados]] para análisis interno.

# Ceros y su efecto

> [!info] Cero cerca de un polo
> Un cero cercano a un polo casi lo cancela, reduciendo la contribución de ese modo en la salida.

> [!info] Cero en el semiplano derecho (RHP)
> Si $G(s)$ tiene un cero con $\Re(z_i) > 0$, el sistema es de **fase no mínima**:
> - Respuesta inversa inicial (*undershoot*)
> - Limitaciones de ancho de banda
> - Dificultad para controlar con altas ganancias

> [!ejemplo] Cero en RHP
> $$G(s) = \frac{s-1}{(s+1)^2}$$
> Respuesta a escalón: $y(0^+) = -1$ (comienza hacia abajo), luego sube a $1$.

> [!info] Cero en el origen
> $G(s) = s$ (derivador puro). Respuesta a escalón: impulso. No realizable físicamente; se aproxima como $\frac{Ks}{\tau s + 1}$.

# Polos dominantes

> [!regla] Aproximación de orden reducido
> Los polos más cercanos al eje imaginario (menor $|\Re(p_i)|$) dominan la respuesta transitoria.
> 
> Si un polo tiene $|\Re(p)| \ge 5 \times |\Re(p_{\text{dom}})|$, su contribución decae al menos 5 veces más rápido y puede despreciarse.

> [!ejemplo] Polo dominante
> $$G(s) = \frac{10}{(s+1)(s+10)} = \frac{10/9}{s+1} - \frac{10/9}{s+10}$$
> Polo $s=-10$ decae 10 veces más rápido que $s=-1$. Se aproxima:
> $$G(s) \approx \frac{1}{s+1}$$
> (error pequeño después de $t > 0.5$ s)
> 
> Ver [[Orden | orden del sistema]] para reducción sistemática.

# Descomposición en fracciones parciales

> [!teorema] Expansión para polos simples
> Si todos los polos $p_i$ son distintos:
> $$G(s) = \sum_{i=1}^n \frac{r_i}{s - p_i}$$
> donde el residuo $r_i = \left. (s-p_i) G(s) \right|_{s=p_i}$.

> [!teorema] Expansión para polos múltiples
> Para un polo $p$ de multiplicidad $r$:
> $$G(s) = \frac{c_r}{(s-p)^r} + \frac{c_{r-1}}{(s-p)^{r-1}} + \dots + \frac{c_1}{s-p} + \text{(términos de otros polos)}$$
> con $c_{r-k} = \frac{1}{k!} \frac{d^k}{ds^k} \left[ (s-p)^r G(s) \right]_{s=p}$.

> [!ejemplo] Polo doble
> $$G(s) = \frac{1}{(s+1)^2(s+2)}$$
> Expansión:
> $$G(s) = \frac{1}{(s+1)^2} + \frac{-1}{s+1} + \frac{1}{s+2}$$
> Modos: $t e^{-t}$, $e^{-t}$, $e^{-2t}$.

# Relación con diseño

> [!info] Lugar de las raíces
> El [[Lugar Raices/index | lugar de las raíces]] muestra cómo los polos de lazo cerrado se mueven al variar la ganancia $K$, partiendo de polos de $G(s)H(s)$ y terminando en sus ceros.
> 
> Útil para diseñar polos dominantes que cumplan especificaciones de $M_p$, $T_s$, etc.