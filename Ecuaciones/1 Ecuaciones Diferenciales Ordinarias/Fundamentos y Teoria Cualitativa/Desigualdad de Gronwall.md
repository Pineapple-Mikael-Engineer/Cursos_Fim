---
title: Desigualdad de Gronwall
tags:
  - ecuaciones
  - edo
  - teoria
  - fundamentos
  - existencia-unicidad
draft: false
aliases:
  - desigualdad de Gronwall
  - lema de Gronwall
  - Grönwall
  - Gronwall inequality
  - Gronwall's lemma
---

# Desigualdad de Gronwall

> [!definicion]
> **(Forma integral.)** Sea $u(x)\ge 0$ continua en $[x_0,b]$ que cumple, para todo $x$ del intervalo,
> $$u(x)\ \le\ \alpha+\int_{x_0}^{x}\beta(t)\,u(t)\,dt,\qquad \alpha\ge 0,\ \ \beta(t)\ge 0\ \text{continua}.$$
> Entonces $u$ queda **acotada por la exponencial** de la integral del peso:
> $$\boxed{\,u(x)\ \le\ \alpha\,\exp\!\Bigl(\int_{x_0}^{x}\beta(t)\,dt\Bigr).}$$
> En su **forma diferencial**: si $u'(x)\le \beta(x)\,u(x)$, entonces $u(x)\le u(x_0)\,e^{\int_{x_0}^{x}\beta}$.
> La desigualdad dice que una cantidad que crece a lo sumo proporcionalmente a sí misma no puede
> crecer más rápido que la solución de la EDO lineal asociada.

> [!info]
> Es la **herramienta de acotación** de los [[index | fundamentos cualitativos]] (libro): no es un
> teorema sobre una EDO concreta, sino un lema que se usa por todas partes para **comparar** una
> cantidad desconocida con una exponencial conocida. Con ella se cierran tres huecos centrales de la
> teoría: la **unicidad** global de [[Existencia y Unicidad Picard | Picard]], la **dependencia
> continua** respecto de los datos (ver [[Dependencia de Condiciones y Parametros | dependencia de
> condiciones y parámetros]]) y las **cotas a priori** que permiten [[Prolongacion de Soluciones |
> prolongar soluciones]]. Complementa, del lado cuantitativo, a la construcción de la
> [[Iteracion de Picard | iteración de Picard]].

---

## Ejemplo

> [!ejemplo] Gronwall demuestra la unicidad de Picard
> Sean $y_1,y_2$ **dos soluciones** de $y'=f(x,y)$ con el **mismo** dato inicial $y_1(x_0)=y_2(x_0)$, y
> sea $f$ Lipschitz en $y$ con constante $L$. Restando sus formas integrales,
> $$y_i(x)=y_i(x_0)+\int_{x_0}^{x} f(t,y_i)\,dt\ \Longrightarrow\
> y_1(x)-y_2(x)=\int_{x_0}^{x}\!\bigl[f(t,y_1)-f(t,y_2)\bigr]dt.$$
> Tomando valor absoluto y aplicando Lipschitz, $u(x):=|y_1(x)-y_2(x)|$ cumple
> $$u(x)\ \le\ \int_{x_0}^{x} L\,|y_1(t)-y_2(t)|\,dt\ =\ \underbrace{0}_{\alpha}+\int_{x_0}^{x} L\,u(t)\,dt.$$
> Es la hipótesis de Gronwall con $\alpha=0$ y $\beta\equiv L$. La conclusión es
> $$u(x)\ \le\ 0\cdot e^{L(x-x_0)}=0\ \Longrightarrow\ u\equiv 0\ \Longrightarrow\ y_1\equiv y_2.$$
> Las dos soluciones coinciden en **todo** el intervalo. Así, sin pedir que $Lh<1$ (la restricción
> técnica que solo servía para que la contracción de [[Existencia y Unicidad Picard | Picard]] funcionara
> en un trozo pequeño), Gronwall entrega la **unicidad global** de un plumazo.

---

## En qué consiste

> [!teoria] La idea: convertir una desigualdad integral en una EDO
> La hipótesis $u\le \alpha+\int\beta u$ es **implícita**: $u$ aparece en ambos lados, dentro y fuera
> de la integral, y no se despeja directamente. El truco es **nombrar el lado derecho**: si llamamos
> $R(x)$ a esa cota, entonces $R$ es derivable (es una constante más una integral), $u\le R$, y $R$
> satisface una **desigualdad diferencial** $R'\le\beta R$. Esa desigualdad sí se integra con el
> **factor integrante** $e^{-\int\beta}$, igual que la EDO lineal de primer orden. El resultado es que
> $R$ —y con ella $u$— queda atrapada bajo la exponencial.

> [!teorema] Lema de Gronwall (forma integral)
> Si $u\ge 0$ continua cumple $u(x)\le \alpha+\int_{x_0}^{x}\beta(t)\,u(t)\,dt$ en $[x_0,b]$, con
> $\alpha\ge 0$ y $\beta\ge 0$ continua, entonces para todo $x\in[x_0,b]$
> $$u(x)\ \le\ \alpha\,\exp\!\Bigl(\int_{x_0}^{x}\beta(t)\,dt\Bigr).$$

> [!demostracion]
> **Paso 1 — bautizar la cota.** Define
> $$R(x):=\alpha+\int_{x_0}^{x}\beta(t)\,u(t)\,dt.$$
> Por hipótesis $u(x)\le R(x)$, y $R$ es derivable con $R(x_0)=\alpha$. Su derivada es el integrando
> evaluado en $x$, y usando $u\le R$ y $\beta\ge 0$:
> $$R'(x)=\beta(x)\,u(x)\ \le\ \beta(x)\,R(x).$$
> Hemos transformado la desigualdad integral en una **desigualdad diferencial** $R'\le\beta R$, mucho
> más manejable.
>
> **Paso 2 — factor integrante.** Sea $\Phi(x)=e^{-\int_{x_0}^{x}\beta(t)\,dt}>0$. Como $\Phi'=-\beta\Phi$,
> al multiplicar $R'-\beta R\le 0$ por $\Phi$ aparece una derivada exacta:
> $$\frac{d}{dx}\bigl(R(x)\,\Phi(x)\bigr)=\bigl(R'-\beta R\bigr)\,\Phi\ \le\ 0.$$
> El producto $R\,\Phi$ es **no creciente**. Integrando de $x_0$ a $x$ (y usando $\Phi(x_0)=1$):
> $$R(x)\,\Phi(x)\ \le\ R(x_0)\,\Phi(x_0)=\alpha,\qquad\text{luego}\qquad R(x)\ \le\ \alpha\,\Phi(x)^{-1}=\alpha\,e^{\int_{x_0}^{x}\beta}.$$
>
> **Paso 3 — volver a $u$.** Como $u(x)\le R(x)$ por el Paso 1, encadenando con la cota anterior,
> $$u(x)\ \le\ R(x)\ \le\ \alpha\,\exp\!\Bigl(\int_{x_0}^{x}\beta(t)\,dt\Bigr),$$
> que es lo afirmado. $\blacksquare$

> [!proposicion] Dependencia continua de la condición inicial
> Gronwall también mide **cuánto** se separan dos soluciones cuando se separan sus datos iniciales.
> Sean $y(x;a)$ e $y(x;b)$ las soluciones de $y'=f(x,y)$ con $y(x_0)=a$ y $y(x_0)=b$, y $f$ Lipschitz-$L$.
> Restando las formas integrales, $u(x)=|y(x;a)-y(x;b)|$ cumple
> $$u(x)\ \le\ |a-b|+\int_{x_0}^{x} L\,u(t)\,dt,$$
> ahora con $\alpha=|a-b|$. Gronwall da entonces
> $$|y(x;a)-y(x;b)|\ \le\ |a-b|\,e^{L|x-x_0|}.$$
> Si $a\to b$, las soluciones se acercan uniformemente en intervalos acotados: la solución **depende
> con continuidad** del dato inicial. Es la base del [[Dependencia de Condiciones y Parametros | estudio
> de la dependencia respecto de condiciones y parámetros]] y la garantía de que pequeñas perturbaciones
> del estado inicial no provocan saltos en la evolución (aunque el factor $e^{L|x-x_0|}$ avisa de que el
> error puede **amplificarse** exponencialmente a largo plazo).

> [!info] Forma diferencial y cotas a priori
> La forma diferencial $u'\le\beta u\Rightarrow u\le u(x_0)e^{\int\beta}$ es el mismo lema con
> $R=u$. Es la que se usa para obtener **cotas a priori**: si una solución desconocida $y$ satisface
> una desigualdad del tipo $\frac{d}{dx}|y|^2\le \beta|y|^2$ (por ejemplo, por una estimación de energía),
> Gronwall acota $|y|$ por una exponencial **antes** de conocer la solución, lo que impide que escape a
> infinito en tiempo finito y permite [[Prolongacion de Soluciones | prolongarla]].

## Resumen

> [!resumen]
> | Forma | Hipótesis | Conclusión |
> |---|---|---|
> | Integral | $u\le \alpha+\int_{x_0}^{x}\beta\,u$, $\ \alpha,\beta\ge 0$ | $u(x)\le \alpha\,e^{\int_{x_0}^{x}\beta}$ |
> | Diferencial | $u'\le\beta\,u$ | $u(x)\le u(x_0)\,e^{\int_{x_0}^{x}\beta}$ |
> | Unicidad | $\alpha=0$, $\beta=L$ | $u\equiv 0\Rightarrow y_1\equiv y_2$ |
> | Dependencia continua | $\alpha=\|a-b\|$, $\beta=L$ | $\|y(x;a)-y(x;b)\|\le\|a-b\|e^{L\|x-x_0\|}$ |
> | Cota a priori | estimación $\frac{d}{dx}\|y\|^2\le\beta\|y\|^2$ | $\|y\|$ atrapada bajo exponencial |

> [!corolario]
> Gronwall es el "multiplicador" de toda la teoría cualitativa: con $\alpha=0$ da **unicidad**, con
> $\alpha=|a-b|$ da **dependencia continua**, y en forma diferencial da **cotas a priori** para
> prolongar soluciones. Su único mecanismo —pasar de una desigualdad integral implícita a una
> diferencial vía factor integrante— se reutiliza una y otra vez. Es, junto con la
> [[Iteracion de Picard | iteración de Picard]], el motor analítico que sostiene a
> [[Existencia y Unicidad Picard | Picard-Lindelöf]].

> [!referencia]
> - El teorema cuya unicidad global cierra: [[Existencia y Unicidad Picard]].
> - La construcción cuya convergencia cuantifica: [[Iteracion de Picard]].
> - La propiedad que justifica con $\alpha=|a-b|$: [[Dependencia de Condiciones y Parametros]].
> - El uso para cotas a priori: [[Prolongacion de Soluciones]].
> - Marco general: [[index]].
