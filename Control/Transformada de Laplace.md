---
title: Transformada de Laplace — Análisis en el dominio s
tags:
  - control-clasico
  - transformada-integral
  - laplace
  - variable-compleja
  - condiciones-iniciales
draft: true
aliases:
  - Laplace
  - Dominio s
  - Transformada Unilateral
---

# Transformada de Laplace

> [!definicion] Definición Formal (Transformada Unilateral)
> Sea $f(t)$ una función definida para $t \geq 0$. Su **Transformada de Laplace** es una función $F(s)$ de variable compleja $s = \sigma + j\omega \in \mathbb{C}$, definida por la integral impropia:
> $$
> F(s) = \mathcal{L}\{f(t)\} = \int_{0^-}^{\infty} f(t) e^{-st} \, dt
> $$
> donde:
> - El operador $\mathcal{L}$ denota la **transformación integral**.
> - El límite inferior $0^-$ es un detalle técnico que asegura capturar posibles discontinuidades impulsivas en $t=0$ (Ver: [[Delta de Dirac]]).
> - La integral es **impropia** porque el límite superior es infinito. Su existencia depende del comportamiento de $f(t)$.

> [!definicion] Transformada Bilateral
> Para señales definidas en todo $\mathbb{R}$ (no necesariamente causales):
> $$
> F(s) = \mathcal{L}_{II}\{f(t)\} = \int_{-\infty}^{\infty} f(t) e^{-st} \, dt
> $$
> En [[Control Clásico]] se usa exclusivamente la **unilateral** porque los sistemas físicos son causales y parten de condiciones iniciales conocidas en $t=0$.

---

## Existencia y Región de Convergencia

> [!teoria] Condición de Existencia
> La integral que define $\mathcal{L}\{f(t)\}$ no siempre converge. Existe si $f(t)$ es:
> 1. **Continua a trozos** en $[0, \infty)$.
> 2. De **orden exponencial**, es decir, existen constantes $M > 0$, $\alpha \in \mathbb{R}$ tales que:
>    $$
>    |f(t)| \le M e^{\alpha t}, \quad \forall t \ge T
>    $$
>    *(La función no crece más rápido que una exponencial).*

> [!definicion] Abscisa de Convergencia
> El ínfimo de los valores $\sigma = \Re(s)$ para los cuales la integral converge se denomina **abscisa de convergencia**, denotada $\sigma_c$.
> $$
> \sigma_c = \inf \{ \Re(s) \mid \text{la integral } \int_{0^-}^\infty f(t) e^{-st} dt \text{ converge} \}
> $$
> La **Región de Convergencia (ROC)** es el semiplano complejo $\Re(s) > \sigma_c$.

> [!example] Cálculo de la Abscisa de Convergencia
> - **$f(t) = e^{3t}$**:
>   $\int_0^\infty e^{3t} e^{-st} dt = \int_0^\infty e^{-(s-3)t} dt$. Converge si $\Re(s) > 3 \implies \sigma_c = 3$.
> - **$f(t) = e^{-2t}$**:
>   Converge si $\Re(s) > -2 \implies \sigma_c = -2$.
> - **$f(t) = \mathbf{1}(t)$** (Escalón):
>   Converge si $\Re(s) > 0 \implies \sigma_c = 0$.
> - **$f(t) = e^{t^2}$**:
>   Crece más rápido que cualquier exponencial. **No existe** su Transformada de Laplace.

---

## ¿Por qué la Exponencial como Núcleo?

> [!teoria] Conexión con Sistemas LTI
> La elección del núcleo $K(s,t) = e^{-st}$ **no es arbitraria**. Como se demostró en [[Sistemas LTI]], la exponencial compleja $e^{st}$ es la **[[Funciones Propias|función propia]]** universal de todo sistema LTI.
>
> La Transformada de Laplace **descompone** una señal arbitraria $f(t)$ en una superposición continua de estas funciones propias, ponderadas por $F(s)$:
> $$
> f(t) = \frac{1}{2\pi j} \int_{\sigma - j\infty}^{\sigma + j\infty} F(s) e^{st} \, ds
> $$
> *(Transformada Inversa de Laplace, donde $\sigma > \sigma_c$).*

> [!example] Interpretación Física de $s = \sigma + j\omega$
> - **$\sigma$ (Parte Real):** Controla el **decaimiento** ($\sigma < 0$) o **crecimiento** ($\sigma > 0$) exponencial $e^{\sigma t}$.
> - **$\omega$ (Parte Imaginaria):** Controla la **frecuencia de oscilación** mediante $e^{j\omega t} = \cos(\omega t) + j\sin(\omega t)$.
> 
> **Comparación con Fourier:**
> - **[[Transformada de Fourier]]** ($s = j\omega$): Solo evalúa el eje imaginario ($\sigma = 0$). Captura únicamente **régimen permanente senoidal**.
> - **Laplace** ($s = \sigma + j\omega$): Evalúa todo el plano complejo. Captura **transitorios** ($\sigma \neq 0$) y permite analizar **estabilidad**.

---

## Propiedades Fundamentales

Estas propiedades convierten [[Ecuación Diferencial Ordinaria Lineal|Ecuaciones Diferenciales]] en ecuaciones algebraicas.

### 1. Linealidad
> [!teoria] Propiedad de Superposición
> $$
> \mathcal{L}\{\alpha f(t) + \beta g(t)\} = \alpha F(s) + \beta G(s)
> $$
> Esta propiedad se hereda de la [[Linealidad de la Integral]].

### 2. Derivación en el Tiempo
> [!teoria] Propiedad Fundamental para Control
> $$
> \mathcal{L}\left\{ \frac{df}{dt} \right\} = s F(s) - f(0^-)
> $$
> $$
> \mathcal{L}\left\{ \frac{d^n f}{dt^n} \right\} = s^n F(s) - s^{n-1} f(0^-) - s^{n-2} \dot{f}(0^-) - \dots - f^{(n-1)}(0^-)
> $$

> [!demostracion] Demostración (Caso Primera Derivada)
> Aplicando [[Integración por Partes]] a la definición:
> $$
> \mathcal{L}\{f'(t)\} = \int_{0^-}^{\infty} f'(t) e^{-st} dt
> $$
> Sea $u = e^{-st} \implies du = -s e^{-st} dt$ y $dv = f'(t) dt \implies v = f(t)$.
> $$
> \int_{0^-}^{\infty} f'(t) e^{-st} dt = \left[ f(t) e^{-st} \right]_{0^-}^{\infty} - \int_{0^-}^{\infty} f(t) (-s e^{-st}) dt
> $$
> Asumiendo que $f(t)$ es de [[#Existencia y Región de Convergencia|orden exponencial]], $\lim_{t \to \infty} f(t)e^{-st} = 0$ para $\Re(s) > \sigma_c$.
> $$
> = 0 - f(0^-)(1) + s \int_{0^-}^{\infty} f(t) e^{-st} dt = s F(s) - f(0^-)
> $$
> $\square$

### 3. Integración en el Tiempo
> [!teoria] Efecto de un Integrador
> $$
> \mathcal{L}\left\{ \int_{0^-}^{t} f(\tau) d\tau \right\} = \frac{F(s)}{s}
> $$

### 4. Desplazamiento en Frecuencia
> [!teoria] Multiplicación por Exponencial en el Tiempo
> $$
> \mathcal{L}\{e^{at} f(t)\} = F(s - a)
> $$
> *(Útil para analizar respuestas amortiguadas).*

### 5. Desplazamiento en el Tiempo
> [!teoria] Retardo Puro
> $$
> \mathcal{L}\{f(t - t_0) \mathbf{1}(t - t_0)\} = e^{-t_0 s} F(s), \quad t_0 > 0
> $$
> donde $\mathbf{1}(t)$ es la **[[Función Escalón de Heaviside]]**.

### 6. Teoremas de Valor Límite
> [!teoria] Teorema del Valor Inicial
> $$
> f(0^+) = \lim_{s \to \infty} s F(s)
> $$
> *(Predice el valor de $f(t)$ inmediatamente después de $t=0$).*

> [!teoria] Teorema del Valor Final
> $$
> \lim_{t \to \infty} f(t) = \lim_{s \to 0} s F(s)
> $$
> **Condición de validez:** Todos los polos de $s F(s)$ deben tener $\Re(p_i) < 0$ (parte real negativa), o a lo sumo un polo simple en $s=0$. Es la herramienta fundamental para calcular el **[[Error en Estado Estacionario]]** en [[Sistemas de Control]].

---

## Tabla de Transformadas Elementales

| Función Temporal $f(t), \; t \ge 0$ | Transformada $F(s) = \mathcal{L}\{f(t)\}$ | Abscisa $\sigma_c$ |
|-------------------------------------|-------------------------------------------|---------------------|
| $\delta(t)$ ([[Delta de Dirac\|Impulso]]) | $1$ | $-\infty$ |
| $\mathbf{1}(t)$ ([[Función Escalón de Heaviside\|Escalón Unitario]]) | $\frac{1}{s}$ | $0$ |
| $t$ (Rampa Unitaria) | $\frac{1}{s^2}$ | $0$ |
| $t^n, \; n \in \mathbb{N}$ | $\frac{n!}{s^{n+1}}$ | $0$ |
| $e^{-at}$ | $\frac{1}{s + a}$ | $-a$ |
| $\sin(\omega t)$ | $\frac{\omega}{s^2 + \omega^2}$ | $0$ |
| $\cos(\omega t)$ | $\frac{s}{s^2 + \omega^2}$ | $0$ |
| $e^{-at} \sin(\omega t)$ | $\frac{\omega}{(s+a)^2 + \omega^2}$ | $-a$ |
| $e^{-at} \cos(\omega t)$ | $\frac{s+a}{(s+a)^2 + \omega^2}$ | $-a$ |
| $t e^{-at}$ | $\frac{1}{(s+a)^2}$ | $-a$ |

---

## Técnica de Fracciones Parciales

Para invertir $F(s)$ y obtener $f(t)$, es necesario descomponer funciones racionales en sumas de términos elementales.

> [!teoria] Expansión en Fracciones Parciales
> Sea $F(s) = \frac{N(s)}{D(s)}$ una función racional propia ($\deg(N) < \deg(D)$).
> 
> **Caso 1: Polos Reales Simples**
> Si $D(s) = (s-p_1)(s-p_2)\dots(s-p_n)$ con $p_i \neq p_j$:
> $$
> F(s) = \sum_{i=1}^n \frac{A_i}{s - p_i}, \quad \text{donde } A_i = \left. (s-p_i)F(s) \right|_{s=p_i}
> $$
> *(Método de [[Residuos]] o de Heaviside).*
>
> **Caso 2: Polos Complejos Conjugados Simples**
> Si $p_{1,2} = \sigma \pm j\omega$, se agrupan en un término cuadrático:
> $$
> \frac{As + B}{(s-\sigma)^2 + \omega^2}
> $$
> *(Para obtener senos/cosenos amortiguados).*
>
> **Caso 3: Polos Repetidos (Multiplicidad $r$)**
> Si $(s-p_1)^r$ es factor de $D(s)$:
> $$
> \frac{A_1}{s-p_1} + \frac{A_2}{(s-p_1)^2} + \dots + \frac{A_r}{(s-p_1)^r}
> $$

> [!example] Ejemplo de Fracciones Parciales
> **Problema:** Encontrar la transformada inversa de $F(s) = \frac{1}{s(s+1)(s+2)}$.
> 
> **Paso 1: Descomponer en fracciones simples.**
> $$
> \frac{1}{s(s+1)(s+2)} = \frac{A}{s} + \frac{B}{s+1} + \frac{C}{s+2}
> $$
> 
> **Paso 2: Calcular residuos.**
> - $A = \left. s \cdot F(s) \right|_{s=0} = \left. \frac{1}{(s+1)(s+2)} \right|_{s=0} = \frac{1}{2}$.
> - $B = \left. (s+1) \cdot F(s) \right|_{s=-1} = \left. \frac{1}{s(s+2)} \right|_{s=-1} = \frac{1}{(-1)(1)} = -1$.
> - $C = \left. (s+2) \cdot F(s) \right|_{s=-2} = \left. \frac{1}{s(s+1)} \right|_{s=-2} = \frac{1}{(-2)(-1)} = \frac{1}{2}$.
> 
> **Paso 3: Aplicar transformada inversa.**
> $$
> F(s) = \frac{1/2}{s} - \frac{1}{s+1} + \frac{1/2}{s+2}
> $$
> $$
> f(t) = \frac{1}{2} - e^{-t} + \frac{1}{2}e^{-2t}, \quad t \ge 0
> $$

---

## Aplicación Estrella: Solución de Ecuaciones Diferenciales

> [!example] Sistema Masa-Resorte-Amortiguador
> **Ecuación Diferencial:** $m\ddot{y} + c\dot{y} + ky = u(t)$
> **Condiciones Iniciales:** $y(0) = y_0, \quad \dot{y}(0) = v_0$.
> 
> **Paso 1: Aplicar Laplace a ambos lados.**
> $$
> m[s^2 Y(s) - s y_0 - v_0] + c[s Y(s) - y_0] + k Y(s) = U(s)
> $$
> 
> **Paso 2: Agrupar términos de $Y(s)$.**
> $$
> (m s^2 + c s + k) Y(s) - (m s y_0 + m v_0 + c y_0) = U(s)
> $$
> 
> **Paso 3: Despejar $Y(s)$.**
> $$
> Y(s) = \frac{U(s)}{m s^2 + c s + k} + \frac{(m s + c) y_0 + m v_0}{m s^2 + c s + k}
> $$
> 
> **Interpretación:**
> - Primer término: **Respuesta Forzada** (debido a la entrada $u(t)$).
> - Segundo término: **Respuesta Libre** (debido a las condiciones iniciales).
> 
> Si $y_0 = 0$ y $v_0 = 0$ (**condiciones iniciales nulas**), obtenemos la **[[Función de Transferencia]]**:
> $$
> G(s) = \frac{Y(s)}{U(s)} = \frac{1}{m s^2 + c s + k}
> $$

> [!example] Obtención de la Respuesta al Escalón
> Sea $m=1, c=3, k=2, u(t)=\mathbf{1}(t)$ ([[Función Escalón de Heaviside\|Escalón Unitario]]) y condiciones iniciales nulas.
> $$
> Y(s) = G(s)U(s) = \frac{1}{s^2 + 3s + 2} \cdot \frac{1}{s} = \frac{1}{s(s+1)(s+2)}
> $$
> *(Esta es exactamente la fracción parcial resuelta en el ejemplo anterior).*
> 
> **Solución en el tiempo:**
> $$
> y(t) = \frac{1}{2} - e^{-t} + \frac{1}{2}e^{-2t}, \quad t \ge 0
> $$

---

## Notas Relacionadas

- [[Sistemas LTI]]
- [[Función de Transferencia]]
- [[Delta de Dirac]]
- [[Función Escalón de Heaviside]]
- [[Transformada de Fourier]]
- [[Ecuación Diferencial Ordinaria Lineal]]
- [[Error en Estado Estacionario]]
- [[Integración por Partes]]
- [[Residuos]]