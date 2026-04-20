---
titulo: Teorema Fundamental del Cálculo
tema: Cálculo Integral
dificultad: fundamental
fuente: Spivak, Calculus, Cap. 14
cssclasses:
  - teorema
draft: true
---



# Teorema Fundamental del Cálculo


> [!teoria] Contexto 
> Este teorema es el resultado más importante del cálculo de una variable. Establece la conexión profunda entre diferenciación e integración, mostrando que son operaciones inversas entre sí.

## Parte I

> [!teorema] TFC — Parte I
>  Sea $f$ continua en $[a, b]$. Define $F: [a,b] \to \mathbb{R}$ por: $$F(x) = \int_a^x f(t),dt$$ Entonces $F$ es diferenciable en $(a,b)$ y $F'(x) = f(x)$.

> [!demostracion] 
> Debemos mostrar que $\lim_{h \to 0} \dfrac{F(x+h) - F(x)}{h} = f(x)$.
> 
> Por definición de $F$: $$\frac{F(x+h)-F(x)}{h} = \frac{1}{h}\int_x^{x+h} f(t),dt$$
> 
> Como $f$ es continua en $x$, dado $\varepsilon > 0$ existe $\delta > 0$ tal que $|t - x| < \delta \Rightarrow |f(t) - f(x)| < \varepsilon$.
> 
> Para $|h| < \delta$: $$\left|\frac{1}{h}\int_x^{x+h} f(t),dt - f(x)\right| = \left|\frac{1}{h}\int_x^{x+h}(f(t)-f(x)),dt\right| \leq \frac{1}{|h|}\cdot\varepsilon|h| = \varepsilon$$

## Parte II

> [!teorema] TFC — Parte II 
> (Regla de Barrow) Si $F$ es una antiderivada de $f$ continua en $[a,b]$, entonces: $$\int_a^b f(x),dx = F(b) - F(a)$$

> [!corolario] 
> Evaluación práctica Cualquier antiderivada sirve para evaluar la integral definida. Si $G = F + C$ es otra antiderivada, entonces $G(b) - G(a) = F(b) + C - F(a) - C = F(b) - F(a)$.

> [!ejemplo] 
> Calcular $\int_0^\pi \sin x,dx$ Una antiderivada de $\sin x$ es $F(x) = -\cos x$. $$\int_0^\pi \sin x,dx = [-\cos x]_0^\pi = -\cos\pi - (-\cos 0) = 1 + 1 = 2$$