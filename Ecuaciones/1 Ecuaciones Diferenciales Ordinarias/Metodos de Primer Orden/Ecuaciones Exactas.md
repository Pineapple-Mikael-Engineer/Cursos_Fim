---
title: Ecuaciones Exactas
tags:
  - ecuaciones
  - edo
  - teoria
  - primer-orden
  - exactas
draft: false
aliases:
  - ecuaciones exactas
  - ecuación exacta
  - diferencial exacto
  - exact equation
  - exact differential
---

# Ecuaciones Exactas

> [!definicion]
> El diferencial $M(x,y)\,dx+N(x,y)\,dy$ es **exacto** si es el **diferencial total** de alguna
> función escalar $f(x,y)$, es decir
> $$M=\frac{\partial f}{\partial x},\qquad N=\frac{\partial f}{\partial y}.$$
> En ese caso la EDO $M\,dx+N\,dy=0$ no es más que $df=0$, y su solución es **implícita**:
> $$\boxed{\,f(x,y)=C\,}.$$
> La forma práctica de detectarlo, en un dominio **simplemente conexo**, es la **condición de
> exactitud**:
> $$\frac{\partial M}{\partial y}=\frac{\partial N}{\partial x}.$$

> [!info]
> Cuarto tipo del [[Metodos de Primer Orden/index| catálogo de primer orden]] (libro, cap. 1.3.3). Va de la mano con
> [[Factor Integrante]]: cuando **no** se cumple $\partial_yM=\partial_xN$, se multiplica por un
> $\mu$ que vuelve exacta la ecuación. El método cierra en una integración, así que en el fondo
> emparenta con [[Variables Separables| separar variables]]. Punto de retorno: el
> [[Metodos de Primer Orden/index| índice de métodos]].

---

## Ejemplo

> [!ejemplo] Construir $f$ verificando primero la exactitud
> **Resolver $\cos y\,dx-(x\sin y-y^2)\,dy=0$** (libro, Ej. 9). Identificamos
> $$M=\cos y,\qquad N=-x\sin y+y^2.$$
>
> **Paso 1 — verificar la exactitud.**
> $$\frac{\partial M}{\partial y}=-\sin y,\qquad \frac{\partial N}{\partial x}=-\sin y.$$
> Coinciden: la ecuación **es exacta**, así que existe $f$ con $df=M\,dx+N\,dy$.
>
> **Paso 2 — integrar $M$ respecto de $x$** (tratando $y$ como constante):
> $$f=\int M\,dx=\int\cos y\,dx=x\cos y+g(y).$$
> La "constante" de integración es una **función de $y$** porque integramos solo en $x$.
>
> **Paso 3 — derivar respecto de $y$ e igualar a $N$.**
> $$\frac{\partial f}{\partial y}=-x\sin y+g'(y)\ \stackrel{!}{=}\ N=-x\sin y+y^2
> \ \Longrightarrow\ g'(y)=y^2.$$
> Los términos en $x$ se cancelan: esa cancelación es **la firma de que la ecuación era exacta**.
>
> **Paso 4 — integrar $g$ y escribir la solución.**
> $$g(y)=\frac{y^3}{3}\ \Longrightarrow\ f(x,y)=x\cos y+\frac{y^3}{3}.$$
> La solución general es la familia de curvas de nivel
> $$\boxed{\,x\cos y+\frac{y^3}{3}=C\,}.$$

---

## En qué consiste

> [!teoria]
> Recuerda el **diferencial total** de una función de dos variables:
> $$df=\frac{\partial f}{\partial x}\,dx+\frac{\partial f}{\partial y}\,dy.$$
> Si la EDO dice $df=0$, entonces $f$ **no cambia** a lo largo de la solución, luego $f=$ cte. Por
> eso resolver una exacta es simplemente **reconstruir la $f$** de la que provino el diferencial.
>
> ¿De dónde sale la condición $\partial_yM=\partial_xN$? De la **igualdad de las derivadas mixtas**.
> Si $M=\partial_xf$ y $N=\partial_yf$, entonces
> $$\frac{\partial M}{\partial y}=\frac{\partial^2 f}{\partial y\,\partial x},
> \qquad \frac{\partial N}{\partial x}=\frac{\partial^2 f}{\partial x\,\partial y},$$
> y por el **teorema de Clairaut–Schwarz** (con $f$ de clase $C^2$) ambas mixtas son iguales. Por
> eso la exactitud **obliga** a $\partial_yM=\partial_xN$.
>
> **Analogía física.** Un diferencial exacto es un **campo conservativo**: el "trabajo"
> $\int M\,dx+N\,dy$ entre dos puntos **no depende del camino**, solo de los extremos, porque es la
> diferencia de potencial $f(B)-f(A)$. Un diferencial **inexacto** —como el calor $\delta Q$ en
> termodinámica— **sí** depende del camino: no existe una "función calor" de estado.

> [!teorema] La condición de exactitud es suficiente (dominio simplemente conexo)
> Si $M,N$ son de clase $C^1$ y satisfacen $\partial_yM=\partial_xN$ en un dominio **simplemente
> conexo** (sin agujeros), entonces existe $f$ con $df=M\,dx+N\,dy$, y por tanto la EDO es exacta.

> [!demostracion]
> **Paso 1 — proponer $f$ integrando $M$.** Define, fijando un $x_0$,
> $$f(x,y)=\int_{x_0}^{x} M(t,y)\,dt+g(y),$$
> con $g$ por determinar. Por construcción $\partial f/\partial x=M(x,y)$, que es **la mitad** de lo
> pedido.
>
> **Paso 2 — imponer la segunda condición.** Derivando respecto de $y$ bajo el signo integral,
> $$\frac{\partial f}{\partial y}=\int_{x_0}^{x}\frac{\partial M}{\partial y}(t,y)\,dt+g'(y)
> =\int_{x_0}^{x}\frac{\partial N}{\partial x}(t,y)\,dt+g'(y),$$
> donde hemos usado **la hipótesis** $\partial_yM=\partial_xN$. La integral es ahora de una derivada
> en $x$, así que por el teorema fundamental del cálculo
> $$\frac{\partial f}{\partial y}=\big[N(x,y)-N(x_0,y)\big]+g'(y).$$
>
> **Paso 3 — despejar $g$.** Para que $\partial f/\partial y=N$ basta elegir $g'(y)=N(x_0,y)$, que
> depende **solo de $y$** y por tanto es integrable. Con esa $g$, la $f$ construida cumple
> $df=M\,dx+N\,dy$. La hipótesis de dominio simplemente conexo garantiza que el camino de
> integración se puede deformar sin tropezar con agujeros. $\blacksquare$

> [!algoritmo] Resolver una exacta
> 1. Escribe la ecuación en forma diferencial $M\,dx+N\,dy=0$ e identifica $M$ y $N$.
> 2. **Verifica** $\partial_yM=\partial_xN$. Si no se cumple, no es exacta (ve al paso de la
>    advertencia).
> 3. Integra: $f=\displaystyle\int M\,dx+g(y)$ (la "constante" es función de $y$).
> 4. Deriva en $y$ e iguala a $N$: $\partial_yf=N$. Los términos en $x$ deben cancelarse; despeja
>    $g'(y)$.
> 5. Integra $g'(y)$ para obtener $g(y)$.
> 6. Escribe la solución implícita $f(x,y)=C$.

> [!proposicion] Simetría del método
> Es equivalente empezar **integrando $N$ respecto de $y$**: $f=\int N\,dy+h(x)$, derivar en $x$,
> igualar a $M$ y despejar $h'(x)$. Conviene elegir la integral **más fácil** de las dos. El
> resultado $f(x,y)=C$ es el mismo.

> [!warning] Si la condición falla
> Si $\partial_yM\neq\partial_xN$, la ecuación **no es exacta** y el método tal cual no aplica: al
> intentar el paso 4 aparecerían términos en $x$ que **no se cancelan** y $g'(y)$ no quedaría solo en
> función de $y$. La salida es buscar un [[Factor Integrante]] $\mu(x,y)$ que multiplique la ecuación
> y la vuelva exacta.

## Resumen

> [!resumen]
> | Paso | Acción |
> |---|---|
> | Forma | $M\,dx+N\,dy=0$ |
> | Test | $\partial_yM=\partial_xN$ (si no, $\to$ factor integrante) |
> | Integrar | $f=\displaystyle\int M\,dx+g(y)$ |
> | Ajustar | $\partial_yf=N\Rightarrow g'(y)$, luego integrar $g$ |
> | Solución | $f(x,y)=C$ |

> [!corolario]
> Una ecuación exacta es una **igualdad disfrazada de "potencial = constante"**. Toda la dificultad
> está en (1) reconocer la exactitud con el test de las mixtas y (2) reconstruir $f$ por integración
> parcial. Es la versión bidimensional de "una EDO es dos integrales": aquí es **una sola** integral
> en $x$ más un ajuste en $y$.

> [!info] Conexión con la termodinámica
> La distinción exacto / inexacto es central en física: la energía interna $U$, la entropía $S$ o el
> volumen son **funciones de estado** (sus diferenciales $dU$, $dS$ son exactos), mientras que el
> calor $\delta Q$ y el trabajo $\delta W$ **no** lo son (dependen del proceso). El truco genial es
> que $\delta Q$ inexacto se vuelve exacto al dividir por la temperatura: $dS=\delta Q/T$. Esa $1/T$
> es precisamente un [[Factor Integrante]] —ver la nota siguiente.

> [!referencia]
> - Cuando el test falla: [[Factor Integrante]] (fabricar la exactitud con $\mu$).
> - El método cierra en una integral, como [[Variables Separables]].
> - Lugar en el catálogo: [[Metodos de Primer Orden/index]].
