---
title: Cruce del Eje Imaginario
order: 5
tags:
  - control-clasico
  - diseno
  - lugar-raices
  - estabilidad
draft: false
aliases:
  - cruce del eje imaginario
  - cruce jω
  - ganancia crítica
  - imaginary axis crossing
---

# Cruce del Eje Imaginario

> [!definicion]
> Punto donde una rama del [[Lugar Raices/index | lugar de raíces]] cruza el eje imaginario, pasando del semiplano izquierdo (estable) al derecho (inestable). Marca la **ganancia crítica** $K_{cr}$ y la **frecuencia de oscilación** $\omega$ en el límite de estabilidad. Se halla con [[Routh Hurwitz/index | Routh-Hurwitz]] (la fila que se anula da $K_{cr}$; la ecuación auxiliar da $\pm j\omega$) o sustituyendo $s=j\omega$ en la ecuación característica.

> [!info]
> Regla de trazado del [[Lugar Raices/index | lugar de raíces]], hermana de [[Trayectoria eje real y Asintotas]], [[Puntos Ruptura]] y [[Angulos Salida Llegada]]. El mismo $K_{cr}$ es la ganancia última de [[Ziegler Nichols Oscilacion | Ziegler-Nichols]] y el cruce de [[Criterio Nyquist | Nyquist]] por $-1$.

---

## Ejemplo

> [!ejemplo]
> **Vía Routh.** $G(s)H(s)=\dfrac{K}{s(s+1)(s+2)}$. Hallar $K_{cr}$ y la frecuencia del cruce.
>
> **Paso 1 — Ecuación característica.** $1+G(s)H(s)=0$:
> $$s(s+1)(s+2)+K=0\;\Rightarrow\;s^3+3s^2+2s+K=0.$$
>
> **Paso 2 — Tabla de Routh.**
> $$\begin{array}{c|cc} s^3 & 1 & 2 \\ s^2 & 3 & K \\ s^1 & \dfrac{3\cdot2-1\cdot K}{3}=\dfrac{6-K}{3} & 0 \\ s^0 & K & \end{array}$$
>
> **Paso 3 — Anular una fila.** La fila $s^1$ se hace cero cuando
> $$\frac{6-K}{3}=0\;\Rightarrow\;K_{cr}=6.$$
>
> **Paso 4 — Ecuación auxiliar** (fila inmediatamente superior, $s^2$, con $K=6$):
> $$3s^2+K=3s^2+6=0\;\Rightarrow\;s^2=-2\;\Rightarrow\;s=\pm j\sqrt2.$$
> Luego $\omega=\sqrt2\approx1.41$ rad/s.
>
> **Paso 5 — Interpretar.** Para $K<6$ el sistema es estable; en $K=6$ dos ramas tocan el eje imaginario en $\pm j\sqrt2$ (oscilación sostenida); para $K>6$ esas ramas entran al semiplano derecho → inestable.

> [!ejemplo]
> **Mismo sistema vía $s=j\omega$** (comprobación). Sustituir $s=j\omega$ en $s^3+3s^2+2s+K=0$:
>
> **Paso 1 — Potencias de $j\omega$.** $s^2=-\omega^2$, $s^3=-j\omega^3$:
> $$-j\omega^3-3\omega^2+2j\omega+K=0.$$
>
> **Paso 2 — Separar real e imaginaria:**
> $$\text{Re: } K-3\omega^2=0,\qquad \text{Im: } -\omega^3+2\omega=\omega(2-\omega^2)=0.$$
>
> **Paso 3 — Resolver.** De la imaginaria (con $\omega\neq0$): $\omega^2=2\Rightarrow\omega=\sqrt2$. Sustituyendo en la real:
> $$K=3\omega^2=3\cdot2=6.$$
>
> **Paso 4 — Conclusión.** $K_{cr}=6$, $\omega=\sqrt2$ rad/s: idéntico a Routh.

> [!ejemplo]
> **Lectura gráfica del cruce.**
>
> ![[lgr_cruce_eje_imaginario.svg|550]]
>
> Las ramas cruzan a $\pm j\sqrt2$ cuando $K=6$; para $K>6$ los polos están en el semiplano derecho (inestable).

---

## En qué consiste

> [!teoria]
> Sobre el lugar de raíces, los polos de lazo cerrado se mueven al variar $K$. El cruce del eje $j\omega$ es el valor de $K$ para el cual un par de polos pasa por $\pm j\omega$ (parte real nula): el límite de estabilidad. Hay dos formas equivalentes de localizarlo.

> [!teorema] Vía Routh-Hurwitz
> En la [[Construccion Tabla | tabla de Routh]] de $1+K\,G(s)H(s)=0$:
> 1. El $K$ que **anula una fila completa** produce raíces simétricas respecto al origen — aquí el par imaginario puro $\pm j\omega$. Ese $K$ es $K_{cr}$.
> 2. La **ecuación auxiliar** formada con la fila inmediatamente superior tiene por raíces ese $\pm j\omega$: da la frecuencia del cruce.

> [!teorema] Vía sustitución $s=j\omega$
> Sustituyendo $s=j\omega$ en la ecuación característica $1+K\,G(j\omega)H(j\omega)=0$ y separando:
> $$\operatorname{Re}\{1+K\,G(j\omega)H(j\omega)\}=0,\qquad \operatorname{Im}\{1+K\,G(j\omega)H(j\omega)\}=0.$$
> El sistema de dos ecuaciones da $K_{cr}$ y $\omega$ a la vez.

> [!info] Por qué la fila de ceros
> Una fila nula en [[Routh Hurwitz/index | Routh-Hurwitz]] señala raíces simétricas respecto al origen; cuando son un par imaginario puro $\pm j\omega$, esos polos están **justo sobre** el eje. El $K$ que la genera es exactamente la ganancia crítica.

---

## Receta

> [!algoritmo]
> 1. Escribir la ecuación característica $1+K\,G(s)H(s)=0$ como polinomio en $s$.
> 2. **Routh:** construir la tabla; hallar el $K=K_{cr}$ que anula una fila; formar la ecuación auxiliar (fila anterior) y resolver $\pm j\omega$.
> 3. **O $s=j\omega$:** sustituir, separar Re e Im, resolver el sistema para $K_{cr}$ y $\omega$.
> 4. Reportar: rango estable $K<K_{cr}$, frecuencia de oscilación $\omega$, periodo $T=2\pi/\omega$.

> [!info] En MATLAB
> ```matlab
> G = tf(1, [1 3 2 0]);     % K/(s(s+1)(s+2))
> rlocus(G)                 % localiza el cruce graficamente
> [Kcr,poles] = rlocfind(G) % click sobre el eje jw: da Kcr y +-jw
> % comprobacion analitica:
> K = 6;  roots([1 3 2 K])  % raices ~ -3, +-j*sqrt(2)
> ```

---

## Conexión con otros métodos

> [!teorema] Tres caminos al mismo punto
> La ganancia crítica $K_{cr}$ y la frecuencia $\omega$ del cruce coinciden con:
> - el límite de estabilidad de [[Routh Hurwitz/index | Routh-Hurwitz]],
> - la **ganancia última** $K_u=K_{cr}$ y el periodo $T_u=2\pi/\omega$ de [[Ziegler Nichols Oscilacion | Ziegler-Nichols]],
> - el cruce del lugar de [[Criterio Nyquist | Nyquist]] por el punto $-1$ ($\omega_{pc}$, margen de ganancia nulo).
>
> Tres representaciones del **mismo** límite de estabilidad.

---

## Para qué sirve

> [!info]
> Fija el **rango de ganancia estable** ($K<K_{cr}$) y la frecuencia de oscilación incipiente. Es el dato de partida para sintonizar por [[Ziegler Nichols Oscilacion | Ziegler-Nichols]] y para saber cuánto margen de $K$ queda antes de la inestabilidad.

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Qué marca | límite estable→inestable sobre el eje $j\omega$ |
> | Routh | $K$ que anula una fila $=K_{cr}$; ecuación auxiliar $\to\pm j\omega$ |
> | $s=j\omega$ | $\operatorname{Re}=0$ y $\operatorname{Im}=0$ dan $K_{cr},\omega$ |
> | Ejemplo $\frac{K}{s(s+1)(s+2)}$ | $K_{cr}=6$, $\omega=\sqrt2$ rad/s |
> | Equivalentes | $K_u$ de Ziegler-Nichols · cruce de Nyquist por $-1$ |

> [!corolario]
> El cruce del eje imaginario es la frontera de estabilidad del lazo cerrado vista sobre el lugar de raíces. Routh (fila nula + ecuación auxiliar) y la sustitución $s=j\omega$ dan el **mismo** par $(K_{cr},\omega)$, que además es la ganancia última de Ziegler-Nichols y el cruce de Nyquist por $-1$.

> [!referencia]
> - Tabla de Routh: [[Construccion Tabla]] · [[Routh Hurwitz/index]].
> - Ganancia última y sintonización: [[Ziegler Nichols Oscilacion]].
> - Equivalente frecuencial: [[Criterio Nyquist]] · [[Margenes MF MG]].
> - Otras reglas del lugar: [[Reglas Construccion]] · [[Angulos Salida Llegada]].
