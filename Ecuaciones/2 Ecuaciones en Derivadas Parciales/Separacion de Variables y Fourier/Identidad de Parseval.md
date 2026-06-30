---
title: Identidad de Parseval
order: 5
tags:
  - ecuaciones
  - edp
  - teoria
  - fourier
  - parseval
draft: false
aliases:
  - identidad de Parseval
  - teorema de Parseval
  - desigualdad de Bessel
  - conservación de energía Fourier
  - Parseval's identity
  - Bessel's inequality
---

# Identidad de Parseval

> [!definicion]
> La **identidad de Parseval** iguala la "energía" de una función con la suma de los cuadrados de sus coeficientes de Fourier. Para $f$ de período $2L$ con coeficientes $a_0,a_n,b_n$:
> $$\frac{1}{L}\int_{-L}^{L} f(x)^2\,dx=\frac{a_0^2}{2}+\sum_{n=1}^{\infty}\big(a_n^2+b_n^2\big).$$
> Dicho de otro modo: la **norma al cuadrado** de $f$ es la suma de los cuadrados de sus componentes en la **base ortonormal** de senos y cosenos. Es el **teorema de Pitágoras en dimensión infinita**: la energía total se reparte, sin pérdidas, entre los modos de frecuencia.

> [!info]
> Es la contraparte "global" de [[Convergencia y Gibbs| la convergencia puntual]]: garantiza que la serie reproduce a $f$ **en media cuadrática**. Descansa sobre la [[Funciones Ortogonales| ortogonalidad]] de la base y sobre su **completitud**. Pertenece a [[Separacion de Variables y Fourier/index| Separación de Variables y Fourier]], en el capítulo de [[2 Ecuaciones en Derivadas Parciales/index| Ecuaciones en Derivadas Parciales]]. Físicamente: al pasar al **dominio de frecuencias** no se crea ni se destruye energía.

---

## Ejemplo

> [!ejemplo] El problema de Basilea: $\sum 1/n^2=\pi^2/6$
> Tomemos $f(x)=x$ en $[-\pi,\pi]$ (período $2\pi$, así $L=\pi$). Es **impar**, luego $a_0=a_n=0$ y solo sobreviven los senos. Integrando por partes,
> $$b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}x\,\operatorname{sen}(nx)\,dx=\frac{2(-1)^{n+1}}{n}.$$
> **Lado izquierdo (energía).**
> $$\frac{1}{\pi}\int_{-\pi}^{\pi}x^2\,dx=\frac{1}{\pi}\cdot\frac{2\pi^3}{3}=\frac{2\pi^2}{3}.$$
> **Lado derecho (coeficientes).**
> $$\sum_{n=1}^{\infty}b_n^2=\sum_{n=1}^{\infty}\frac{4}{n^2}.$$
> **Igualando** por Parseval:
> $$\frac{2\pi^2}{3}=\sum_{n=1}^{\infty}\frac{4}{n^2}\quad\Longrightarrow\quad
> \boxed{\;\sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{\pi^2}{6}\;}$$
> El célebre **problema de Basilea**, resuelto sin esfuerzo: la conservación de energía de Fourier "suma" la serie por nosotros.

---

## En qué consiste

> [!teoria] La intuición: Pitágoras con infinitos catetos
> En $\mathbb{R}^3$, si $\mathbf{v}=v_1\mathbf{e}_1+v_2\mathbf{e}_2+v_3\mathbf{e}_3$ con base **ortonormal**, entonces $\|\mathbf{v}\|^2=v_1^2+v_2^2+v_3^2$. Las funciones de cuadrado integrable forman un espacio con producto interno $\langle f,g\rangle=\int f g$, y las funciones $\{1,\cos nx,\operatorname{sen} nx\}$ son una **base ortogonal**. Los coeficientes de Fourier son exactamente las **componentes** de $f$ en esa base. Parseval es, literalmente, Pitágoras: la longitud al cuadrado del "vector" $f$ es la suma de los cuadrados de sus componentes. Que la igualdad sea **exacta** (y no solo una cota) exige que la base **no deje direcciones fuera**: que sea **completa**.

> [!teorema] Desigualdad de Bessel e identidad de Parseval
> Sea $\{\varphi_n\}$ un sistema **ortonormal** y $c_n=\langle f,\varphi_n\rangle$ los coeficientes de $f$. Entonces:
> - **(Bessel)** para todo $N$, $\;\displaystyle\sum_{n=1}^{N}c_n^2\le\|f\|^2$ — vale **siempre**.
> - **(Parseval)** $\;\displaystyle\sum_{n=1}^{\infty}c_n^2=\|f\|^2$ — vale **si y solo si** la base es **completa** (la serie $\sum c_n\varphi_n$ converge a $f$ en norma).

> [!demostracion] De Bessel a Parseval
> **Paso 1 — el error es un cuadrado, luego $\ge 0$.** Sea la suma parcial $S_N=\sum_{n\le N}c_n\varphi_n$. Desarrollamos la norma del error usando que es no negativa:
> $$0\le\Big\|f-S_N\Big\|^2=\langle f,f\rangle-2\langle f,S_N\rangle+\langle S_N,S_N\rangle.$$
> **Paso 2 — usar la ortonormalidad.** Como $\langle\varphi_n,\varphi_m\rangle=\delta_{nm}$:
> $$\langle f,S_N\rangle=\sum_{n\le N}c_n\langle f,\varphi_n\rangle=\sum_{n\le N}c_n^2,\qquad
> \langle S_N,S_N\rangle=\sum_{n\le N}c_n^2.$$
> Sustituyendo, $\;0\le\|f\|^2-2\sum_{n\le N}c_n^2+\sum_{n\le N}c_n^2=\|f\|^2-\sum_{n\le N}c_n^2.$ **Paso 3 — Bessel.** Reordenando: $\sum_{n\le N}c_n^2\le\|f\|^2$ para todo $N$. La serie de cuadrados está **acotada** y crece, luego **converge**. **Paso 4 — completitud da la igualdad.** Si la base es **completa**, $\|f-S_N\|^2\to 0$ por definición. Pero del Paso 2, $\|f-S_N\|^2=\|f\|^2-\sum_{n\le N}c_n^2$; tomando $N\to\infty$, el miembro derecho tiende a $\|f\|^2-\sum c_n^2$. Igualar a cero da $\sum_{n=1}^{\infty}c_n^2=\|f\|^2$. $\blacksquare$

> [!proposicion] La versión clásica (senos y cosenos)
> Para la base $\{1,\cos nx,\operatorname{sen} nx\}$ en $[-L,L]$, las normas son $\|1\|^2=2L$ y $\|\cos\tfrac{n\pi x}{L}\|^2=\|\operatorname{sen}\tfrac{n\pi x}{L}\|^2=L$. Sustituir esas normas en $\sum c_n^2=\|f\|^2$ y despejar reproduce la forma de la definición:
> $$\frac{1}{L}\int_{-L}^{L}f(x)^2\,dx=\frac{a_0^2}{2}+\sum_{n=1}^{\infty}(a_n^2+b_n^2).$$

> [!info]
> Parseval es **conservación de la energía** al cambiar al dominio de frecuencias: la energía de la señal $\int f^2$ es igual a la energía repartida entre sus armónicos $\sum(a_n^2+b_n^2)$. Es la versión discreta del **teorema de Plancherel** de la transformada de Fourier, $\int |f(x)|^2\,dx=\frac{1}{2\pi}\int|\hat f(\omega)|^2\,d\omega$, base del análisis espectral en física e ingeniería.

## Resumen

> [!resumen]
> | Objeto | Espacio físico | Espacio de frecuencias |
> |:--|:--|:--|
> | Energía | $\frac1L\int_{-L}^L f^2\,dx$ | $\dfrac{a_0^2}{2}+\sum(a_n^2+b_n^2)$ |
> | Cota (Bessel) | siempre | $\sum_{n\le N}c_n^2\le\|f\|^2$ |
> | Igualdad (Parseval) | base **completa** | $\sum c_n^2=\|f\|^2$ |

> [!corolario]
> Parseval es Pitágoras en dimensión infinita: confirma que los coeficientes de Fourier **no pierden información** cuando la base es completa. Como subproducto, "suma" series numéricas famosas —el problema de Basilea $\sum 1/n^2=\pi^2/6$ entre ellas— con solo igualar dos formas de medir la misma energía.

> [!referencia]
> - La base y su producto interno: [[Funciones Ortogonales]].
> - De dónde salen los coeficientes $a_n,b_n$: [[Series de Fourier]].
> - Qué pasa punto a punto (y el fenómeno de Gibbs): [[Convergencia y Gibbs]].
> - El método global: [[Separacion de Variables y Fourier/index]].
