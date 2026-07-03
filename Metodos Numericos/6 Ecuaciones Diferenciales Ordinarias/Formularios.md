---
title: Formulario — Ecuaciones Diferenciales Ordinarias
order: 99
tags:
  - metodos-numericos
  - formulario
  - edo
draft: false
aliases:
  - formulario edo
  - formulas ecuaciones diferenciales ordinarias
---

# Formulario — Ecuaciones Diferenciales Ordinarias

## Existencia y unicidad (Picard-Lindelöf)

**Condición de Lipschitz en $y$** — $L$: constante de Lipschitz.
$$\|f(t, y_1) - f(t, y_2)\| \leq L\,\|y_1 - y_2\| \qquad \forall (t,y_1), (t,y_2)\in D$$

**Constante de Lipschitz por la derivada.**
$$L = \max\|\partial f/\partial y\|$$

**Teorema:** PVI $y'=f(t,y)$, $y(t_0)=y_0$ con $f$ continua y Lipschitz tiene solución única en $[t_0-\alpha, t_0+\alpha]$.
$$\alpha = \min(a,\ b/M), \qquad M = \max_D\|f\|$$

**Forma integral equivalente del PVI.**
$$y(t) = y_0 + \int_{t_0}^t f(s, y(s))\,ds$$

**Iteración de Picard.**
$$y^{(0)}(t) = y_0, \qquad y^{(k+1)}(t) = y_0 + \int_{t_0}^t f(s, y^{(k)}(s))\,ds$$

**Operador de punto fijo y contracción.**
$$T[y](t) = y_0 + \int_{t_0}^t f(s,y(s))\,ds, \qquad \|T[y_1] - T[y_2]\|_\infty \leq L\,|t-t_0|\,\|y_1-y_2\|_\infty$$

**Cota de separación de soluciones vecinas (condicionamiento).**
$$\|e_n\| \lesssim \frac{C}{L}\big(e^{L(t_n-t_0)}-1\big)h^p$$

---

## Euler explícito (orden 1)

**Método** — $h$: paso; $y_n\approx y(t_n)$.
$$y_{n+1} = y_n + h\,f(t_n, y_n), \qquad t_{n+1} = t_n + h$$

**Deducción desde Taylor y error local.**
$$y(t_{n+1}) = y(t_n) + h\,f(t_n,y_n) + \underbrace{\frac{h^2}{2}y''(\xi)}_{\tau_n = O(h^2)}$$

**Orden global.**
$$e_n = O(h)$$

**Factor de amplificación / estabilidad condicional** ($z=h\lambda$).
$$R(z) = 1+z, \qquad |1 + h\lambda| \leq 1$$

**Crecimiento de energía en el oscilador armónico** ($\ddot x=-x$, $E_n=\tfrac12(x_n^2+v_n^2)$).
$$E_{n+1} = (1+h^2)E_n$$

---

## Error local de truncamiento vs error global

**Error local de truncamiento** ($\Phi$: función incremento).
$$\tau_n = y(t_{n+1}) - \big[\,y(t_n) + h\,\Phi(t_n, y(t_n), h)\,\big]$$

**Error global.**
$$e_n = y(t_n) - y_n$$

**Relación orden local–global.**
$$\tau_n = O(h^{p+1}) \;\Rightarrow\; e_n = O(h^p)$$

**Teorema de convergencia (cota del error global)** — $L_\Phi$: Lipschitz de $\Phi$.
$$|e_n| \leq \frac{C\,h^p}{L_\Phi}\Big(e^{L_\Phi(t_n - t_0)} - 1\Big) = O(h^p)$$

**Recurrencia del error.**
$$e_{n+1} = e_n + h\big[\Phi(t_n, y(t_n),h) - \Phi(t_n, y_n, h)\big] + \tau_n$$
$$|e_{n+1}| \leq (1 + hL_\Phi)|e_n| + Ch^{p+1}$$

**Suma de la recurrencia.**
$$|e_n| \leq Ch^{p+1}\frac{(1+hL_\Phi)^n - 1}{hL_\Phi} \leq \frac{Ch^p}{L_\Phi}\big(e^{L_\Phi(t_n-t_0)}-1\big)$$

**Acumulación de $N$ pasos.**
$$\text{error global} \sim N \cdot O(h^{p+1}) = \frac{t_f-t_0}{h}\cdot O(h^{p+1}) = O(h^p)$$

**Verificación del orden.**
$$p \approx \log_2\!\big(E(h)/E(h/2)\big)$$

---

## Euler implícito (A-estable, orden 1)

**Método** — pendiente evaluada en el punto de llegada.
$$y_{n+1} = y_n + h\,f(t_{n+1},\, y_{n+1})$$

**Caso lineal $y'=\lambda y$ (despeje).**
$$y_{n+1} = y_n + h\lambda y_{n+1} \;\Rightarrow\; y_{n+1} = \frac{y_n}{1 - h\lambda}$$

**Ecuación de paso no lineal (se resuelve por Newton).**
$$g(y_{n+1}) = y_{n+1} - y_n - hf(t_{n+1},y_{n+1}) = 0$$

**Factor de amplificación y A-estabilidad** ($z=h\lambda$).
$$R(z) = \frac{1}{1 - z}, \qquad |R(z)| < 1 \ \ \forall\, \operatorname{Re}(z)<0$$
$$|1-z|^2 = (1-\operatorname{Re}z)^2 + (\operatorname{Im}z)^2 > 1$$

---

## Métodos de serie de Taylor de orden superior

**Método de orden $p$.**
$$y_{n+1} = y_n + h\,y'_n + \frac{h^2}{2!}y''_n + \cdots + \frac{h^p}{p!}y^{(p)}_n$$

**Derivadas totales de $f$ (regla de la cadena).**
$$y' = f, \qquad y'' = f_t + f_y\,f$$
$$y''' = f_{tt} + 2f_{ty}f + f_{yy}f^2 + f_y(f_t + f_y f)$$

**Método de Taylor de orden 2.**
$$y_{n+1} = y_n + h\,f(t_n,y_n) + \frac{h^2}{2}\big[f_t(t_n,y_n) + f_y(t_n,y_n)\,f(t_n,y_n)\big]$$

**Errores.** local $O(h^{p+1})$, global $O(h^p)$; orden 2: local $O(h^3)$.

---

## Runge-Kutta: construcción general ($s$ etapas, orden $p$)

**Definición general** — $c_i$ nodos, $a_{ij}$ coeficientes, $b_i$ pesos.
$$k_i = f\Big(t_n + c_i h,\ y_n + h\textstyle\sum_{j=1}^s a_{ij}k_j\Big), \qquad y_{n+1} = y_n + h\sum_{i=1}^s b_i k_i$$

**Consistencia de nodos.**
$$c_i = \sum_j a_{ij}$$

**Condiciones de orden.**
$$\text{orden 1:}\ \sum_i b_i = 1, \qquad \text{orden 2:}\ \sum_i b_i c_i = \tfrac12$$
$$\text{orden 3:}\ \sum_i b_i c_i^2 = \tfrac13,\qquad \sum_{i,j} b_i a_{ij} c_j = \tfrac16$$

**Familia RK de 2 etapas (tabla de Butcher).**
$$\begin{array}{c|cc} 0 & 0 & 0 \\ c_2 & c_2 & 0 \\ \hline & b_1 & b_2 \end{array}$$
$$b_1 + b_2 = 1, \qquad b_2 c_2 = \tfrac12$$

**Barrera de Butcher (orden máximo $p$ para $s$ etapas explícitas).**

| Etapas $s$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Orden máx. $p$ | 1 | 2 | 3 | 4 | 4 | 5 | 6 | 6 |

**RK implícitos de Gauss:** orden hasta $2s$.

---

## RK2 (Heun, punto medio, Ralston)

**Heun (trapecio).**
$$k_1 = f(t_n, y_n), \quad k_2 = f(t_n + h,\ y_n + h k_1), \quad y_{n+1} = y_n + \frac{h}{2}(k_1 + k_2)$$
$$\begin{array}{c|cc} 0 & & \\ 1 & 1 & \\ \hline & \tfrac12 & \tfrac12 \end{array}$$

**Punto medio (Euler modificado).**
$$k_1 = f(t_n, y_n), \quad k_2 = f\big(t_n + \tfrac{h}{2},\ y_n + \tfrac{h}{2}k_1\big), \quad y_{n+1} = y_n + h\,k_2$$
$$\begin{array}{c|cc} 0 & & \\ \tfrac12 & \tfrac12 & \\ \hline & 0 & 1 \end{array}$$

**Ralston (error mínimo).**
$$k_2 = f\big(t_n+\tfrac{2h}{3},\ \cdot\big), \qquad y_{n+1} = y_n + h\big(\tfrac14 k_1 + \tfrac34 k_2\big)$$

**Orden.** local $O(h^3)$, global $O(h^2)$; familia con $b_2c_2=\tfrac12$.

---

## RK4 clásico (orden 4)

**Método.**
$$y_{n+1} = y_n + \frac{h}{6}\big(k_1 + 2k_2 + 2k_3 + k_4\big)$$
$$k_1 = f(t_n, y_n),\quad k_2 = f\big(t_n+\tfrac h2, y_n+\tfrac h2 k_1\big),\quad k_3 = f\big(t_n+\tfrac h2, y_n+\tfrac h2 k_2\big),\quad k_4 = f\big(t_n+h, y_n+hk_3\big)$$

**Tabla de Butcher.**
$$\begin{array}{c|cccc} 0 & & & & \\ \tfrac12 & \tfrac12 & & & \\ \tfrac12 & 0 & \tfrac12 & & \\ 1 & 0 & 0 & 1 & \\ \hline & \tfrac16 & \tfrac13 & \tfrac13 & \tfrac16 \end{array}$$

**Orden.** global $O(h^4)$; óptimo $p=s=4$.

---

## Control de paso adaptativo (RK45, Dormand-Prince)

**Par encajado** — $b_i$ orden $p$, $\hat b_i$ orden $p+1$, mismas etapas $k_i$.
$$y_{n+1} = y_n + h\sum_i b_i k_i, \qquad \hat y_{n+1} = y_n + h\sum_i \hat b_i k_i$$

**Error local estimado.**
$$\text{err}_n = \|\hat y_{n+1} - y_{n+1}\| \approx C\,h^{p+1}$$

**Tolerancia mixta.**
$$\text{tol} = \text{atol} + \text{rtol}\cdot\|y_n\|$$

**Nuevo paso (con factor de seguridad).**
$$\text{factor} = \Big(\frac{\text{tol}}{\text{err}}\Big)^{1/(p+1)}, \qquad h_{\text{nuevo}} = h\cdot\min\!\big(\text{facmax},\ \max(\text{facmin},\ 0.9\,\text{factor})\big)$$

**Paso ideal (despeje).**
$$h_{\text{nuevo}} = h\,(\text{tol}/\text{err})^{1/(p+1)}$$

---

## Regiones de estabilidad absoluta y A-estabilidad

**Ecuación de prueba y factor de amplificación** ($z=h\lambda$).
$$y_{n+1} = R(z)\,y_n, \qquad \text{región} = \{z\in\mathbb{C} : |R(z)| \leq 1\}$$

**Factores de amplificación por método.**
$$R_{\text{Euler exp}}(z) = 1+z \qquad (\text{disco } |1+z|\leq1)$$
$$R_{\text{Euler imp}}(z) = \frac{1}{1-z} \qquad (|1-z|\geq1,\ \text{todo }\operatorname{Re}z<0)$$
$$R_{\text{trapezoidal}}(z) = \frac{1+z/2}{1-z/2} \qquad (\text{todo }\operatorname{Re}z\leq0)$$
$$R_{\text{RK4}}(z) = 1+z+\tfrac{z^2}{2}+\tfrac{z^3}{6}+\tfrac{z^4}{24} \qquad (\text{acotada},\ z\gtrsim-2.78)$$

**A-estabilidad.** región $\supseteq \{z : \operatorname{Re}(z) \leq 0\}$.

**Barrera de Dahlquist.** ningún método explícito es A-estable; ningún multipaso lineal A-estable tiene orden $>2$.

**Límite de paso de RK4** (para $\lambda<0$ real).
$$|h\lambda| \leq 2.78 \;\Rightarrow\; h \leq \frac{2.78}{|\lambda|}$$

---

## Reducción de EDO de orden $n$ a sistema de primer orden

**EDO de orden $n$** — variables de estado $u_i = y^{(i-1)}$.
$$y^{(n)} = g\big(t, y, y', \dots, y^{(n-1)}\big)$$

**Sistema de primer orden equivalente.**
$$\mathbf{u}' = \begin{pmatrix} u_1' \\ u_2' \\ \vdots \\ u_{n-1}' \\ u_n' \end{pmatrix} = \begin{pmatrix} u_2 \\ u_3 \\ \vdots \\ u_n \\ g(t, u_1, \dots, u_n) \end{pmatrix}, \qquad \mathbf u(t_0) = \big(y_0, y_0', \dots, y_0^{(n-1)}\big)$$

**Oscilador amortiguado forzado** ($m\ddot x + c\dot x + kx = F(t)$, estado $(x,v)$).
$$\begin{pmatrix} \dot u_1 \\ \dot u_2 \end{pmatrix} = \begin{pmatrix} u_2 \\ \frac{1}{m}\big(F(t) - c\,u_2 - k\,u_1\big) \end{pmatrix}$$

**$N$ cuerpos en 3D** ($\ddot{\mathbf r}_i = \mathbf F_i/m_i$, $6N$ componentes).
$$\mathbf y = (\mathbf r_1, \dots, \mathbf r_N, \mathbf v_1, \dots, \mathbf v_N), \qquad \mathbf y' = (\mathbf v_1, \dots, \mathbf v_N, \mathbf F_1/m_1, \dots, \mathbf F_N/m_N)$$

---

## Acoplamiento de métodos a sistemas (RK vectorial)

**Sistema.** $\mathbf{y}' = \mathbf{f}(t, \mathbf{y})$, $\mathbf y\in\mathbb{R}^m$.

**RK4 vectorial** — misma fórmula, estado y etapas vectoriales.
$$\mathbf k_1 = \mathbf f(t_n, \mathbf y_n),\quad \mathbf k_2 = \mathbf f\big(t_n+\tfrac h2, \mathbf y_n+\tfrac h2\mathbf k_1\big),\quad \mathbf k_3 = \mathbf f\big(t_n+\tfrac h2, \mathbf y_n+\tfrac h2\mathbf k_2\big),\quad \mathbf k_4 = \mathbf f(t_n+h, \mathbf y_n+h\mathbf k_3)$$
$$\mathbf y_{n+1} = \mathbf y_n + \tfrac h6(\mathbf k_1 + 2\mathbf k_2 + 2\mathbf k_3 + \mathbf k_4)$$

**Estabilidad por la jacobiana** — estable si todos los $h\lambda_i$ están en la región.
$$J = \frac{\partial\mathbf f}{\partial\mathbf y}, \qquad \lambda_i = \text{autovalores de } J$$

---

## Rigidez (stiffness)

**Razón de rigidez** (jacobiana con $\operatorname{Re}\lambda_i<0$).
$$\frac{\max|\operatorname{Re}\lambda_i|}{\min|\operatorname{Re}\lambda_i|} \gg 1$$

**Ejemplo (cinética química), autovalores $\lambda_1=-1000$, $\lambda_2=-1$.**
$$\dot y_1 = -1000\,y_1 + y_2, \qquad \dot y_2 = -y_2$$

**Límite de paso explícito (RK4).**
$$h \lesssim \frac{2.78}{|\lambda_{\text{rápido}}|}$$

**Cura:** métodos implícitos A-estables (Euler implícito, trapezoidal/Crank-Nicolson, BDF, Radau).

---

## Integradores simplécticos y conservación

**Sistema hamiltoniano.**
$$\dot{\mathbf q} = \frac{\partial H}{\partial \mathbf p}, \qquad \dot{\mathbf p} = -\frac{\partial H}{\partial \mathbf q}, \qquad H = \frac{|\mathbf p|^2}{2m} + V(\mathbf q)$$

**Verlet de velocidades** (orden 2, 1 evaluación de fuerza, reversible; $\mathbf a = -\nabla V/m$).
$$\mathbf v_{n+1/2} = \mathbf v_n + \tfrac{h}{2}\mathbf a(\mathbf q_n), \qquad \mathbf q_{n+1} = \mathbf q_n + h\,\mathbf v_{n+1/2}, \qquad \mathbf v_{n+1} = \mathbf v_{n+1/2} + \tfrac{h}{2}\mathbf a(\mathbf q_{n+1})$$

**Euler simpléctico (semi-implícito, orden 1)** — usa $\mathbf v_{n+1}$ para $\mathbf q$.
$$\mathbf v_{n+1} = \mathbf v_n + h\,\mathbf a(\mathbf q_n), \qquad \mathbf q_{n+1} = \mathbf q_n + h\,\mathbf v_{n+1}$$

**Hamiltoniano modificado conservado (análisis hacia atrás).**
$$\tilde H = H + O(h^p) \quad (\text{energía real acotada, sin deriva secular})$$

---

## Diferencias finitas: discretización y aproximación centrada

**Malla uniforme.**
$$x_i = a + ih, \qquad h = \frac{b-a}{N}, \qquad i=0,\dots,N$$

**Diferencias centradas** — $y_i\approx y(x_i)$.
$$y'(x_i) \approx \frac{y_{i+1} - y_{i-1}}{2h} + O(h^2), \qquad y''(x_i) \approx \frac{y_{i-1} - 2y_i + y_{i+1}}{h^2} + O(h^2)$$

**Desarrollo de Taylor de la segunda derivada.**
$$y(x_i+h) + y(x_i-h) = 2y(x_i) + h^2 y''(x_i) + \tfrac{h^4}{12}y^{(4)}(\xi)$$
$$y''(x_i) = \frac{y_{i-1}-2y_i+y_{i+1}}{h^2} - \frac{h^2}{12}y^{(4)}(\xi)$$

**Ecuación nodal del PVF lineal** ($y'' = p(x)y' + q(x)y + r(x)$).
$$\frac{y_{i-1}-2y_i+y_{i+1}}{h^2} = p_i\frac{y_{i+1}-y_{i-1}}{2h} + q_i\,y_i + r_i$$

---

## Construcción del sistema tridiagonal lineal

**Forma reordenada de la ecuación nodal.**
$$a_i y_{i-1} + b_i y_i + c_i y_{i+1} = d_i$$
$$a_i = 1 + \tfrac{h}{2}p_i, \qquad b_i = -(2 + h^2 q_i), \qquad c_i = 1 - \tfrac{h}{2}p_i, \qquad d_i = h^2 r_i$$

**Sistema tridiagonal $A\mathbf y=\mathbf b$** (fronteras Dirichlet $y_0=\alpha$, $y_N=\beta$).
$$\begin{pmatrix} b_1 & c_1 & & \\ a_2 & b_2 & c_2 & \\ & \ddots & \ddots & \ddots \\ & & a_{N-1} & b_{N-1} \end{pmatrix}\begin{pmatrix} y_1 \\ y_2 \\ \vdots \\ y_{N-1} \end{pmatrix} = \begin{pmatrix} d_1 - a_1\alpha \\ d_2 \\ \vdots \\ d_{N-1} - c_{N-1}\beta \end{pmatrix}$$

**Diagonal dominancia estricta** (si $q\geq0$ y $\tfrac h2|p_i|<1$).
$$|b_i| = 2+h^2q_i \geq |a_i|+|c_i| = 2$$

**Algoritmo de Thomas.** costo $O(N)$ (frente a $\tfrac23 N^3$ denso).

**Caso no lineal:** $y''=f(x,y,y')$ da sistema no lineal, resuelto por Newton (jacobiana tridiagonal, $O(N)$/iteración).

---

## Consistencia, estabilidad y convergencia (teorema de Lax)

**Teorema de equivalencia de Lax** (problema lineal bien planteado).
$$\text{consistencia} + \text{estabilidad} \;\Longleftrightarrow\; \text{convergencia}$$

**Cota de convergencia.** si $\tau_h=O(h^p)$ y $\|A_h^{-1}\|\leq C$, entonces $\|\mathbf y_h - y\| = O(h^p)$.

**Ecuación del error discreto.**
$$A_h\mathbf y^* = \mathbf b_h + \boldsymbol\tau_h, \qquad \mathbf y^* - \mathbf y_h = A_h^{-1}\boldsymbol\tau_h$$
$$\|\mathbf y^* - \mathbf y_h\| \leq \|A_h^{-1}\|\,\|\boldsymbol\tau_h\| \leq C\,O(h^p) = O(h^p)$$

**Consistencia: truncamiento local del esquema centrado.**
$$\tau_i = \frac{y(x_{i-1}) - 2y(x_i) + y(x_{i+1})}{h^2} - y''(x_i) = \frac{h^2}{12}y^{(4)}(\xi_i) = O(h^2)$$

**Estabilidad: cota uniforme del inverso** (operador $-y''$, Dirichlet).
$$\|A_h^{-1}\| \leq C \ \ (\text{indep. de } h), \qquad \|A_h^{-1}\|_\infty \leq \frac{(b-a)^2}{8}$$

---

## Tratamiento de condiciones de frontera

**Dirichlet** (valor fijo $y(a)=\alpha$) — pasa al lado derecho.
$$b_1 y_1 + c_1 y_2 = d_1 - a_1\alpha$$

**Neumann** (derivada fija $y'(a)=\gamma$) — nodo fantasma $y_{-1}$.
$$y'(a) \approx \frac{y_1 - y_{-1}}{2h} = \gamma \;\Rightarrow\; y_{-1} = y_1 - 2h\gamma$$

**Ecuación de frontera resultante (orden $O(h^2)$).**
$$(y_1 - 2h\gamma) - 2y_0 + y_1 = h^2(\cdots) \;\Rightarrow\; -2y_0 + 2y_1 = h^2(\cdots) + 2h\gamma$$

**Robin (mixta).**
$$\mu\,y(a) + \nu\,y'(a) = \delta$$

---

## Disparo (shooting): transformación PVF → PVI

**PVI parametrizado por la pendiente inicial $s=y'(a)$.**
$$y'' = f(x, y, y'), \qquad y(a) = \alpha, \qquad y'(a) = s \;\Rightarrow\; y(x; s)$$

**Función objetivo / residuo de frontera.**
$$\phi(s) = y(b; s) - \beta, \qquad \phi(s)=0$$

**Caso lineal: $\phi$ afín.**
$$\phi(s) = y(b; s) - \beta = As + B$$
$$y(x;s) = y_p(x) + s\,y_h(x)$$

**Raíz exacta con dos disparos (interpolación lineal).**
$$s^* = s_0 - \phi(s_0)\frac{s_1-s_0}{\phi(s_1)-\phi(s_0)}$$

---

## Disparo con Newton (condición de frontera residual)

**Iteración de Newton sobre $s$.**
$$s_{k+1} = s_k - \frac{\phi(s_k)}{\phi'(s_k)}, \qquad \phi'(s) = \frac{\partial y(b;s)}{\partial s}$$

**Ecuación de sensibilidad (variacional)** — $v = \partial y/\partial s$.
$$v'' = \frac{\partial f}{\partial y}\,v + \frac{\partial f}{\partial y'}\,v', \qquad v(a) = 0, \quad v'(a) = 1, \qquad \phi'(s) = v(b)$$

**Alternativa: secante (sin variacional, orden $\varphi\approx1.618$).**
$$s_{k+1} = s_k - \phi(s_k)\frac{s_k - s_{k-1}}{\phi(s_k) - \phi(s_{k-1})}$$

---

## Comparación disparo vs diferencias finitas

**Disparo:** reduce a PVI + raíces; precisión del integrador ($O(h^4)$ con RK4); frágil si el PVI es sensible.

**Diferencias finitas:** sistema tridiagonal global $O(N)$; precisión $O(h^2)$; robusto y escalable a EDPs.
