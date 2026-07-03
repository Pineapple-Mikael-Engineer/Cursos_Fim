---
title: Formulario — Ecuaciones No Lineales
order: 99
tags:
  - metodos-numericos
  - formulario
  - ecuaciones-no-lineales
draft: false
aliases:
  - formulario ecuaciones no lineales
  - formulas raices
---

# Formulario — Ecuaciones No Lineales

## Teorema de Bolzano y método gráfico

**Teorema de Bolzano (existencia).** $f$ continua en $[a,b]$, $f(a)f(b)<0 \Rightarrow \exists\, c\in(a,b): f(c)=0$.
$$f(a) \cdot f(b) < 0 \quad \Rightarrow \quad \exists\, c \in (a, b): f(c) = 0$$

**Longitud del intervalo por bisección.**
$$b_k - a_k = \frac{b - a}{2^{k-1}}, \qquad \lim_{k \to \infty} (b_k - a_k) = 0$$

**Cambio de signo en malla** ($x_0,\dots,x_m$): raíz localizada en $(x_i,x_{i+1})$.
$$f(x_i) \cdot f(x_{i+1}) < 0 \quad \Rightarrow \quad \text{raíz en } (x_i, x_{i+1})$$

**Multiplicidad $m$ de una raíz $r$.**
$$f(r) = f'(r) = \cdots = f^{(m-1)}(r) = 0, \quad f^{(m)}(r) \neq 0$$

---

## Bisección (método cerrado)

**Punto medio.**
$$c = \frac{a + b}{2}$$

**Cota de error** (iteración $k$).
$$|c_k - r| \leq \frac{b - a}{2^k}$$

**Longitud del intervalo tras $k$ pasos.**
$$L_k = \frac{b - a}{2^k}, \qquad |c_k - r| \leq \frac{b_k - a_k}{2} = \frac{b - a}{2^{k+1}}$$

**Iteraciones para error $\varepsilon$.**
$$k \geq \log_2\left(\frac{b - a}{\varepsilon}\right)$$

**Orden de convergencia lineal, factor $1/2$.**
$$\lim_{k \to \infty} \frac{|c_{k+1} - r|}{|c_k - r|} = \frac{1}{2}$$

---

## Regula Falsi (falsa posición, método cerrado)

**Interpolación lineal (aproximación de la raíz).**
$$c = b - f(b) \cdot \frac{b - a}{f(b) - f(a)} = \frac{a f(b) - b f(a)}{f(b) - f(a)}$$

**Recta secante que la genera** ($y=0$ en $c$).
$$y = f(a) + \frac{f(b) - f(a)}{b - a}(x - a)$$

**Forma alternativa (más estable si $f(b)$ pequeño).**
$$c = a - \frac{f(a)(b - a)}{f(b) - f(a)}$$

Orden lineal ($p=1$), factor variable (puede $\to 1$ por estancamiento unilateral).

---

## Newton-Raphson: derivación

**Iteración de Newton.** $x_{k+1}=x_k-f(x_k)/f'(x_k)$.
$$x^{(k+1)} = x^{(k)} - \frac{f(x^{(k)})}{f'(x^{(k)})}$$

**Recta tangente en $(x^{(k)}, f(x^{(k)}))$.**
$$y = f(x^{(k)}) + f'(x^{(k)})(x - x^{(k)})$$

**Serie de Taylor con resto.**
$$f(x) = f(x^{(k)}) + f'(x^{(k)})(x - x^{(k)}) + \frac{f''(\xi)}{2}(x - x^{(k)})^2$$

**Error** $e^{(k)} = x^{(k)} - r$; relación por paso.
$$e^{(k+1)} = \frac{\left(f''(\eta_k) - \frac{f''(\xi_k)}{2}\right) (e^{(k)})^2}{f'(r) + f''(\eta_k) e^{(k)}} = \frac{f''(\xi_k)}{2f'(x^{(k)})} (e^{(k)})^2$$

**Cota cuadrática del error.**
$$|e^{(k+1)}| \leq C |e^{(k)}|^2, \qquad |e^{(k)}| \leq \frac{1}{C} (C |e^{(0)}|)^{2^k} \to 0$$

**Función de iteración y su derivada.**
$$g(x) = x - \frac{f(x)}{f'(x)}, \qquad g'(x) = \frac{f(x) f''(x)}{(f'(x))^2}, \qquad g'(r) = 0 \;\text{(raíz simple)}$$

---

## Newton-Raphson: convergencia cuadrática (raíz simple)

**Definición de convergencia cuadrática.**
$$\lim_{k \to \infty} \frac{|x^{(k+1)} - r|}{|x^{(k)} - r|^2} = C$$

**Constante asintótica.**
$$C = \frac{|f''(r)|}{2|f'(r)|}$$

**Derivadas de $g$ en $r$.**
$$g'(r) = 0, \qquad g''(r) = \frac{f''(r)}{f'(r)}$$

**Expansión de Taylor de $g$ y relación de error.**
$$g(x) = r + \frac{g''(r)}{2}(x - r)^2 + O((x - r)^3), \qquad \lim_{k \to \infty} \frac{x^{(k+1)} - r}{(x^{(k)} - r)^2} = \frac{f''(r)}{2f'(r)}$$

**Progresión de dígitos correctos.**
$$\|e^{(k+1)}\| \approx C \cdot 10^{-2d}, \qquad d \to 2d - \log_{10}(1/C)$$

---

## Newton-Raphson: raíces múltiples (convergencia lineal)

**Raíz de multiplicidad $m$.**
$$f(r) = f'(r) = \cdots = f^{(m-1)}(r) = 0, \quad f^{(m)}(r) \neq 0$$

**Factorización.** $f(x) = (x-r)^m h(x)$, $h(r)\neq 0$.
$$\frac{f(x)}{f'(x)} = \frac{(x-r) h(x)}{m h(x) + (x-r) h'(x)}$$

**Derivada de $g$ en raíz múltiple → convergencia lineal.**
$$g'(r) = 1 - \frac{1}{m} \neq 0, \qquad c = 1 - \frac{1}{m}$$

**Newton modificado (con $m$ conocido), recupera orden 2.**
$$x^{(k+1)} = x^{(k)} - m \cdot \frac{f(x^{(k)})}{f'(x^{(k)})}$$

**Método de Schröder (no requiere $m$).**
$$x^{(k+1)} = x^{(k)} - \frac{f(x^{(k)}) f'(x^{(k)})}{(f'(x^{(k)}))^2 - f(x^{(k)}) f''(x^{(k)})}$$

---

## Newton-Raphson: criterios de fallo

**Iteración (división por cero si $f'(x^{(k)})=0$).**
$$x^{(k+1)} = x^{(k)} - \frac{f(x^{(k)})}{f'(x^{(k)})}$$

**Ciclo de periodo 2.**
$$g(g(x^{(0)})) = x^{(0)} \quad \text{pero} \quad g(x^{(0)}) \neq x^{(0)}$$

**Newton con relajación (paso atenuado).**
$$x^{(k+1)} = x^{(k)} - \omega \frac{f(x^{(k)})}{f'(x^{(k)})}, \quad \omega \in (0, 1)$$

Fronteras de cuencas de atracción (ej. $x^3-x$): $x^{(0)}=\pm 1/\sqrt{5}$ → ciclo.

---

## Método de la secante (método abierto)

**Iteración de la secante.** $x_{k+1}=x_k-f(x_k)\dfrac{x_k-x_{k-1}}{f(x_k)-f(x_{k-1})}$.
$$x^{(k+1)} = x^{(k)} - f(x^{(k)})\,\frac{x^{(k)} - x^{(k-1)}}{f(x^{(k)}) - f(x^{(k-1)})}$$

**Pendiente (diferencia finita $\approx f'$).**
$$\frac{f(x^{(k)}) - f(x^{(k-1)})}{x^{(k)} - x^{(k-1)}} \approx f'(x^{(k)})$$

**Orden áureo $\varphi$.**
$$p = \varphi = \frac{1+\sqrt5}{2} \approx 1.618, \qquad \lim_{k\to\infty}\frac{|e^{(k+1)}|}{|e^{(k)}|^{\varphi}} = C^{1/\varphi}, \quad C = \left|\frac{f''(r)}{2f'(r)}\right|$$

**Relación de error (producto de errores previos).**
$$e^{(k+1)} \approx C\, e^{(k)} e^{(k-1)}$$

**Ecuación del exponente.**
$$p = 1 + \frac1p \;\Longrightarrow\; p^2 - p - 1 = 0 \;\Longrightarrow\; p = \frac{1+\sqrt5}{2} = \varphi$$

---

## Punto fijo: teorema de Banach (contracción)

**Contracción** ($L\in[0,1)$).
$$g(I) \subset I, \qquad |g(x) - g(y)| \leq L |x - y| \quad \forall x, y \in I$$

**Condición suficiente diferenciable.**
$$\max_{x \in I} |g'(x)| \leq L < 1$$

**Diferencias sucesivas.**
$$|x^{(k+1)} - x^{(k)}| \leq L^k |x^{(1)} - x^{(0)}|$$

**Cota a priori.**
$$|x^{(k)} - r| \leq \frac{L^k}{1-L} |x^{(1)} - x^{(0)}|$$

**Cota a posteriori.**
$$|x^{(k)} - r| \leq \frac{L}{1-L} |x^{(k)} - x^{(k-1)}|$$

**Cota geométrica.**
$$|x^{(k)} - r| \leq L |x^{(k-1)} - r|$$

**Construcción de $g$ para $f(x)=0$.** $g(x)=x+cf(x)$, condición $|1+cf'(r)|<1$.

---

## Punto fijo: función de iteración y convergencia local

**Iteración de punto fijo.** $x_{k+1}=g(x_k)$, con $r=g(r)$.
$$x^{(k+1)} = g(x^{(k)})$$

**Condición de convergencia local.**
$$|g'(r)| < 1$$

**Método de suma** ($g(x)=x+cf(x)$), derivada en la raíz.
$$g'(r) = 1 + c f'(r)$$

**Estimación del error (valor medio).**
$$g(x) - r = g'(\xi)(x - r), \qquad L = \tfrac{1}{2}(|g'(r)| + 1)$$

**Aceleración de Aitken $\Delta^2$.**
$$\hat{x}^{(k)} = x^{(k)} - \frac{(x^{(k+1)} - x^{(k)})^2}{x^{(k+2)} - 2x^{(k+1)} + x^{(k)}}$$

**Método de Steffensen (orden 2 sin derivada).**
$$x^{(k+1)} = x^{(k)} - \frac{(g(x^{(k)}) - x^{(k)})^2}{g(g(x^{(k)})) - 2g(x^{(k)}) + x^{(k)}}$$

---

## Punto fijo: orden lineal y constante asintótica

**Convergencia lineal** ($c\in(0,1)$).
$$\lim_{k \to \infty} \frac{|x^{(k+1)} - r|}{|x^{(k)} - r|} = c, \qquad c = |g'(r)|$$

**Iteraciones para reducir el error un factor $\varepsilon=10^{-d}$.**
$$c^k \approx \varepsilon \quad \Rightarrow \quad k \approx \frac{\ln \varepsilon}{\ln c} = \frac{-d \ln 10}{\ln c}$$

**Estimación práctica de $c$.**
$$c_k = \frac{|x^{(k+1)} - x^{(k)}|}{|x^{(k)} - x^{(k-1)}|} \xrightarrow{k\to\infty} c$$

**Convergencia sublineal (caso límite).**
$$\lim_{k \to \infty} \frac{|x^{(k+1)} - r|}{|x^{(k)} - r|} = 1$$

---

## Comparación analítica del orden de convergencia

**Orden $p$ y constante asintótica $C$.**
$$\lim_{k\to\infty}\frac{|x^{(k+1)} - r|}{|x^{(k)} - r|^{p}} = C, \qquad C > 0$$

**Progresión de dígitos correctos** ($|e^{(k)}|\approx 10^{-d_k}$).
$$d_{k+1} \approx p\,d_k - \log_{10}\!\frac{1}{C}$$

**Índice de eficiencia** ($m$ = evaluaciones/iter).
$$E = p^{1/m}$$

**Eficiencia secante vs Newton.**
$$E_{\text{secante}} = \varphi^{1/1} \approx 1.618 \;>\; E_{\text{Newton}} = 2^{1/2} \approx 1.414$$

---

## Sistemas no lineales: matriz jacobiana y sistema lineal

**Matriz jacobiana.** $J_{ij}=\partial f_i/\partial x_j$.
$$J(x) = \frac{\partial F}{\partial x} = \begin{pmatrix} \dfrac{\partial f_1}{\partial x_1} & \cdots & \dfrac{\partial f_1}{\partial x_n} \\ \vdots & \ddots & \vdots \\ \dfrac{\partial f_n}{\partial x_1} & \cdots & \dfrac{\partial f_n}{\partial x_n} \end{pmatrix}$$

**Taylor de primer orden.**
$$F(x) = F(x^{(k)}) + J(x^{(k)})\,(x - x^{(k)}) + O(\|x - x^{(k)}\|^2)$$

**Sistema lineal por paso.** Resolver, no invertir.
$$J(x^{(k)})\,\Delta x^{(k)} = -F(x^{(k)}), \qquad x^{(k+1)} = x^{(k)} + \Delta x^{(k)}$$

**Forma con inversa (solo notación).**
$$x^{(k+1)} = x^{(k)} - J(x^{(k)})^{-1}F(x^{(k)})$$

**Jacobiana por diferencias finitas.**
$$J(x)\,e_j \approx \frac{F(x + h e_j) - F(x)}{h}, \qquad h \approx \sqrt{u}\,\|x\|$$

Costo LU: $\tfrac{2}{3}n^3$ (resolver) vs $2n^3$ (invertir).

---

## Sistemas no lineales: convergencia local cuadrática de Newton

**Cota cuadrática.**
$$\|x^{(k+1)} - r\| \leq C\,\|x^{(k)} - r\|^2$$

**Hipótesis:** $J$ Lipschitz $\|J(x)-J(y)\|\leq\gamma\|x-y\|$; $J(r)$ no singular, $\|J(r)^{-1}\|\leq\beta$.
$$\|x^{(k+1)} - r\| \leq \beta\gamma\,\|x^{(k)} - r\|^2$$

**Error tras un paso.**
$$x^{(k+1)} - r = J(x^{(k)})^{-1}\big[F(r) - F(x^{(k)}) - J(x^{(k)})(r - x^{(k)})\big]$$

**Término de linealización (teorema fundamental del cálculo).**
$$F(r) - F(x^{(k)}) = \int_0^1 J\big(x^{(k)} + t(r - x^{(k)})\big)\,(r - x^{(k)})\,dt$$
$$\big\|F(r) - F(x^{(k)}) - J(x^{(k)})(r - x^{(k)})\big\| \leq \frac{\gamma}{2}\|x^{(k)} - r\|^2$$

**Globalización (paso amortiguado).**
$$x^{(k+1)} = x^{(k)} + t_k\,\Delta x^{(k)}, \quad t_k \in (0, 1], \qquad \min \tfrac12\|F(x)\|_2^2$$

---

## Sistemas no lineales: costo y cuasi-Newton

**Costo por iteración de Newton:** evaluar $F$ ($n$), formar $J$ ($n^2$), factorizar LU ($\tfrac{2}{3}n^3$), resolver ($2n^2$) → $O(n^3)$.

**Actualización de Broyden ("bueno").** $s_k=x^{(k+1)}-x^{(k)}$, $y_k=F(x^{(k+1)})-F(x^{(k)})$.
$$B_{k+1} = B_k + \frac{(y_k - B_k s_k)\,s_k^T}{s_k^T s_k}$$

**Ecuación de la secante (multivariable).**
$$B_{k+1}(x^{(k+1)} - x^{(k)}) = F(x^{(k+1)}) - F(x^{(k)})$$

**Newton–Krylov inexacto (producto $Jv$ sin formar $J$).**
$$J v \approx \frac{F(x + hv) - F(x)}{h}$$

Broyden: costo $O(n^2)$/iter, orden superlineal.

---

## Sistemas no lineales: contracción y norma matricial

**Iteración de punto fijo multivariable.** $x^{(k+1)}=G(x^{(k)})$, $x^*=G(x^*)$.
$$\|G(x) - G(y)\| \leq L\,\|x - y\| \quad \forall x, y \in D$$

**Cotas de error (Banach multivariable).**
$$\|x^{(k)} - x^*\| \leq \frac{L^k}{1-L}\,\|x^{(1)} - x^{(0)}\| \;\text{(a priori)}, \qquad \|x^{(k)} - x^*\| \leq \frac{L}{1-L}\,\|x^{(k)} - x^{(k-1)}\| \;\text{(a posteriori)}$$

**Criterio práctico vía jacobiana.**
$$L = \max_{x}\,\|J_G(x)\|, \qquad \rho(J_G(x^*)) \leq \|J_G(x^*)\| < 1$$

**Criterio exacto de convergencia local.**
$$\rho(J_G(x^*)) < 1$$

**Valor medio integral.**
$$G(x) - G(y) = \int_0^1 J_G\big(y + t(x - y)\big)(x - y)\,dt$$

**Normas matriciales inducidas.**
$$\|A\|_\infty = \max_i \sum_j |a_{ij}|, \qquad \|A\|_1 = \max_j \sum_i |a_{ij}|, \qquad \|A\|_2 = \sigma_{\max}(A)$$

**Newton como punto fijo óptimo.** $G_N(x)=x-J_F(x)^{-1}F(x)$, $J_{G_N}(x^*)=0$ (contracción con $L=0$).
