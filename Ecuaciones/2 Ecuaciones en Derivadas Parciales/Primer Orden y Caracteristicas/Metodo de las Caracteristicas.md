---
title: Método de las Características
order: 1
tags:
  - ecuaciones
  - edp
  - teoria
  - caracteristicas
  - transporte
draft: false
aliases:
  - Curvas características
  - Ecuación de transporte
  - Method of Characteristics
---

# Método de las Características

> [!definicion]
> Para la EDP de primer orden $a(x,y)\,u_x+b(x,y)\,u_y=c(x,y,u)$, las **ecuaciones características** son el sistema de EDO
> $$\frac{dx}{dt}=a,\qquad \frac{dy}{dt}=b,\qquad \frac{du}{dt}=c.$$
> Las curvas $(x(t),y(t))$ que resuelven las dos primeras son las **características**; sobre ellas la EDP se convierte en la EDO $\dfrac{du}{dt}=c$, que **transporta** el dato inicial a lo largo de la curva.

> [!info]
> Es el método base de [[Primer Orden y Caracteristicas/index| Primer Orden y Características]]. Su versión cuasilineal está en [[Cuasilineal y No Lineal]]; aplicado a la onda da la [[Solucion de dAlembert| solución de d'Alembert]], y limpia la conexión con las [[Formas Canonicas| formas canónicas]].

---

## Ejemplo

> [!ejemplo] Ecuación de transporte $u_t+c\,u_x=0$
> Resolvamos el problema de Cauchy
> $$u_t+c\,u_x=0,\qquad u(x,0)=f(x),\qquad c=\text{cte}>0.$$
> Aquí la variable "tiempo" del método es $t$ (que coincide con la física), y los coeficientes son $a=c$ (en $x$) y $1$ (en $t$). Las **ecuaciones características** son
> $$\frac{dx}{dt}=c,\qquad \frac{du}{dt}=0.$$
> La primera se integra de inmediato: $x(t)=x_0+c\,t$, es decir, **las características son las rectas $x-ct=\text{cte}$**, todas con la misma pendiente. La segunda dice que $u$ **no cambia** mientras avanzamos sobre cada recta. Por tanto, el valor de $u$ en $(x,t)$ es el que tenía en el pie $x_0=x-ct$ de su característica:
> $$\boxed{\,u(x,t)=f(x-ct)\,}.$$
> El perfil inicial $f$ **viaja rígido a velocidad $c$**, sin deformarse: es una onda viajera pura.

> [!ejemplo] Características de la ecuación de transporte
> ![[caracteristicas.svg|470]]
>
> Las rectas $x-ct=$ cte (características) llevan el valor inicial sin cambiarlo: el perfil $f(x)$ se traslada rígido a velocidad $c$.

---

## En qué consiste

> [!teoria]
> El método explota que la combinación $a\,u_x+b\,u_y$ es **una sola derivada**: la derivada de $u$ a lo largo de la curva con tangente $(a,b)$. Parametrizando esa curva por $t$ mediante $\dot x=a$, $\dot y=b$, la regla de la cadena da
> $$\frac{d}{dt}\,u\big(x(t),y(t)\big)=u_x\,\dot x+u_y\,\dot y=a\,u_x+b\,u_y=c.$$
> Lo que era una **EDP** (con dos derivadas parciales acopladas) se desacopla en un **sistema de tres EDO**: dos para la geometría de la curva ($x,y$) y una para el valor transportado ($u$). Resolviendo el sistema con el dato inicial como condición de arranque y eliminando el parámetro $t$ y el pie $x_0$, se reconstruye $u(x,y)$.

> [!teorema] Solución de la ecuación de transporte
> El problema $u_t+c\,u_x=0$, $u(x,0)=f(x)$ con $f\in C^1$ tiene **solución única** $u(x,t)=f(x-ct)$, constante a lo largo de cada recta $x-ct=\text{cte}$.

> [!demostracion]
> **Paso 1 — La solución es constante sobre cada característica.** Fijemos una característica $x(t)=x_0+ct$ y miremos cómo varía $u$ sobre ella. Por la regla de la cadena,
> $$\frac{d}{dt}\,u\big(x(t),t\big)=u_t+\dot x\,u_x=u_t+c\,u_x=0,$$
> donde el último paso usa la propia EDP. Luego $u\big(x(t),t\big)$ **no depende de $t$**: es constante sobre toda la recta.
>
> **Paso 2 — Identificar la constante con el dato inicial.** Evaluando en $t=0$, donde $x(0)=x_0$, esa constante vale $u(x_0,0)=f(x_0)$. Por tanto, sobre la recta entera, $u\big(x(t),t\big)=f(x_0)$.
>
> **Paso 3 — Despejar en términos de $(x,t)$.** Un punto genérico $(x,t)$ está sobre la característica cuyo pie es $x_0=x-ct$. Sustituyendo, $u(x,t)=f(x-ct)$.
>
> **Paso 4 — Unicidad.** Si $v$ es otra solución $C^1$ con el mismo dato, el Paso 1 aplicado a $v$ obliga a que $v$ sea constante sobre cada recta y valga $f$ en el pie; luego $v=f(x-ct)=u$. $\blacksquare$

> [!ejemplo] Coeficientes variables y término fuente: $u_x+u_y=u$
> Resolvamos $u_x+u_y=u$ con $u(x,0)=\cos x$. Tomando $x$ como segunda variable y $y$ como la que crece, las ecuaciones características son
> $$\frac{dx}{dt}=1,\qquad \frac{dy}{dt}=1,\qquad \frac{du}{dt}=u.$$
> **Geometría:** $x=x_0+t$, $y=t$ (arrancamos del eje inicial $y=0$, donde $x=x_0$). Entonces las características son las rectas $x-y=x_0=\text{cte}$ de pendiente $1$. **Transporte:** $\dfrac{du}{dt}=u\Rightarrow u=u(0)\,e^{t}$. En el pie ($t=0$, $y=0$) vale $u=\cos x_0$, así que $u=\cos(x_0)\,e^{t}$. **Eliminando el parámetro:** $t=y$ y $x_0=x-y$, luego
> $$\boxed{\,u(x,y)=e^{\,y}\cos(x-y)\,}.$$
> Comprobación rápida: $u_x=-e^{y}\sin(x-y)$, $u_y=e^{y}\cos(x-y)+e^{y}\sin(x-y)$, y su suma es $e^{y}\cos(x-y)=u$. El término fuente $c=u$ produce el **crecimiento exponencial** $e^{y}$ a lo largo de la característica, mientras el dato $\cos$ se desplaza con ella.

> [!algoritmo] Método de las características (primer orden)
> 1. **Identifica** los coeficientes $a,b,c$ en $a\,u_x+b\,u_y=c$.
> 2. **Escribe** el sistema $\dfrac{dx}{dt}=a,\ \dfrac{dy}{dt}=b,\ \dfrac{du}{dt}=c$.
> 3. **Resuelve la geometría** ($x(t),y(t)$) con el dato inicial como condición de arranque (parametriza el pie con $x_0$ y pon $t=0$ en la curva de datos).
> 4. **Resuelve el transporte** $\dfrac{du}{dt}=c$ a lo largo de la característica, usando el valor inicial en el pie.
> 5. **Elimina** el parámetro $t$ y el pie $x_0$ para obtener $u$ como función de $(x,y)$.
> 6. **Verifica** sustituyendo en la EDP y en la condición inicial.

---

> [!warning]
> El método clásico supone que **por cada punto pasa exactamente una característica** que llega al dato inicial. Si las características **se cruzan** (típico del caso cuasilineal) o **dejan huecos** (datos discontinuos), la fórmula falla: hay que pasar a soluciones débiles, choques y rarefacciones —ver [[Cuasilineal y No Lineal]] y [[Ondas de Choque y Burgers]].

> [!proposicion]
> Si la curva donde se dan los datos es **ella misma una característica** (o tangente a una en algún punto), el problema de Cauchy está **mal planteado**: o no hay solución, o hay infinitas. Los datos deben prescribirse sobre una curva **no característica**.

## Resumen

> [!resumen]
> | Paso | Qué se hace |
> |---|---|
> | Sistema | $\dfrac{dx}{dt}=a,\ \dfrac{dy}{dt}=b,\ \dfrac{du}{dt}=c$ |
> | Características | curvas $(x(t),y(t))$ (la geometría) |
> | Transporte | $\dfrac{du}{dt}=c$ sobre cada curva |
> | Transporte ($u_t+c\,u_x=0$) | $u(x,t)=f(x-ct)$ |
> | $u_x+u_y=u,\ u(x,0)=\cos x$ | $u=e^{y}\cos(x-y)$ |

> [!corolario]
> Una EDP de primer orden **siempre** se reduce a EDO sobre las características. Lo único que decide la dificultad es la geometría de esas curvas: si son ordenadas (lineal), la fórmula cerrada existe; si dependen de $u$ (cuasilineal), la suavidad solo dura hasta que se cruzan.

> [!referencia]
> - El caso con coeficientes que dependen de $u$: [[Cuasilineal y No Lineal]].
> - Conexión con la onda y el cambio de variables: [[Formas Canonicas]] y [[Solucion de dAlembert]].
> - Vuelta al mapa de la sección: [[Primer Orden y Caracteristicas/index]].
