---
title: Fredholm Multidimensional
order: 1
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - multivariable
  - fredholm
draft: false
aliases:
  - ecuación de Fredholm multidimensional
  - Fredholm en varias variables
  - ecuaciones integrales multidimensionales
  - multidimensional Fredholm equation
  - higher dimensional integral equations
---

# Fredholm Multidimensional

> [!definicion]
> La **ecuación de Fredholm multidimensional** tiene la incógnita $\varphi$ definida sobre un dominio $\Omega\subset\mathbb{R}^n$ y un núcleo que integra sobre todo ese dominio:
> $$\varphi(\mathbf{x})=f(\mathbf{x})+\lambda\int_{\Omega}K(\mathbf{x},\mathbf{y})\,\varphi(\mathbf{y})\,d\mathbf{y},\qquad \mathbf{x},\mathbf{y}\in\mathbb{R}^n.$$
> Lo esencial: **toda la teoría de [[Fredholm Segunda Especie| Fredholm de 2ª especie]]** —resolvente, serie de Neumann, alternativa, espectro de un núcleo simétrico— **sigue valiendo igual que en 1D**. La razón es que esa teoría no depende de que el dominio sea un intervalo, sino solo de que el operador $K\varphi=\int_\Omega K(\mathbf{x},\mathbf{y})\varphi(\mathbf{y})\,d\mathbf{y}$ sea **compacto** en $L^2(\Omega)$. La dimensión $n$ es casi un espectador.

> [!info]
> La nota que justifica por qué la física vive en este capítulo. Casi toda aplicación física relevante —[[Teoria de Potencial| potencial]], [[Ecuacion de Lippmann-Schwinger| dispersión]], transporte— es una Fredholm sobre $\Omega\subset\mathbb{R}^n$ o sobre su frontera. Pertenece a [[Multivariable/index| Multivariable y Física]], dentro del capítulo [[3 Ecuaciones Integrales/index| Ecuaciones Integrales]].

---

## Ejemplo

> [!ejemplo] Una Fredholm 2D con núcleo separable
> Sea $\Omega=[0,1]^2$ el cuadrado unidad y el núcleo **separable** (degenerado)
> $$K(\mathbf{x},\mathbf{y})=a(\mathbf{x})\,b(\mathbf{y}),$$
> con $\mathbf{x}=(x_1,x_2)$, $\mathbf{y}=(y_1,y_2)$. La ecuación $\varphi(\mathbf{x})=f(\mathbf{x})+\lambda\,a(\mathbf{x})\int_\Omega b(\mathbf{y})\varphi(\mathbf{y})\,d\mathbf{y}$ tiene la forma
> $$\varphi(\mathbf{x})=f(\mathbf{x})+\lambda\,c\,a(\mathbf{x}),\qquad c:=\int_\Omega b(\mathbf{y})\,\varphi(\mathbf{y})\,d\mathbf{y}.$$
> Multiplicando por $b$ e integrando sobre $\Omega$ y llamando $\alpha=\int_\Omega b\,a$, $f_b=\int_\Omega b\,f$, queda **una sola ecuación escalar** $c=f_b+\lambda c\,\alpha$, es decir
> $$c=\frac{f_b}{1-\lambda\alpha},\qquad \varphi(\mathbf{x})=f(\mathbf{x})+\frac{\lambda f_b}{1-\lambda\alpha}\,a(\mathbf{x}).$$
> **Exactamente el mismo sistema finito** que en 1D: las únicas integrales que cambiaron son sobre el cuadrado en lugar de sobre un intervalo. El polo en $\lambda=1/\alpha$ es el autovalor; nada en el procedimiento "se enteró" de que $n=2$.

---

## En qué consiste

> [!teoria] Qué cambia y qué no al subir de dimensión
> **Lo que NO cambia (la maquinaria de Fredholm):**
> - La **serie de Neumann** $\varphi=\sum_{m\ge0}\lambda^m K^m f$ converge igual para $\lvert\lambda\rvert$ pequeño; el **operador resolvente** $(I-\lambda K)^{-1}$ existe salvo en los autovalores.
> - La **alternativa de Fredholm**: o $(I-\lambda K)\varphi=f$ tiene solución única para todo $f$, o la homogénea tiene soluciones no triviales (y entonces hay condición de compatibilidad). Es un resultado sobre operadores compactos, indiferente a $n$.
> - **Núcleo simétrico** $K(\mathbf{x},\mathbf{y})=K(\mathbf{y},\mathbf{x})$ en $L^2(\Omega)$: el teorema de **Hilbert–Schmidt** da autofunciones **ortogonales** $\{\varphi_k\}$ con autovalores reales $\mu_k\to0$. La incógnita se desarrolla en esa base igual que en 1D.
>
> **Lo que SÍ cambia (la geometría del núcleo):**
> - Aparecen **núcleos débilmente singulares** del tipo $K(\mathbf{x},\mathbf{y})\sim \lvert\mathbf{x}-\mathbf{y}\rvert^{-\alpha}$, heredados de la [[Solucion Fundamental| solución fundamental]] del operador físico. La clave: en $\mathbb{R}^n$ el elemento de volumen $d\mathbf{y}\sim r^{n-1}\,dr$ aporta $n-1$ potencias de $r$, de modo que
>   $$\int_{\lvert\mathbf{y}\rvert<1}\frac{d\mathbf{y}}{\lvert\mathbf{x}-\mathbf{y}\rvert^{\alpha}}<\infty
>   \iff \alpha<n.$$
>   La **dimensión ayuda**: una singularidad $1/r$ que sería brutal en 1D es perfectamente integrable en 3D. Así el potencial de Coulomb ($\alpha=1$, $n=3$) da un operador integral acotado y compacto.

> [!teorema] Compacidad de un núcleo débilmente singular
> Si $\Omega\subset\mathbb{R}^n$ es acotado y $\lvert K(\mathbf{x},\mathbf{y})\rvert\le C\,\lvert\mathbf{x}-\mathbf{y}\rvert^{-\alpha}$ con $\alpha<n$, entonces el operador $K\varphi(\mathbf{x})=\int_\Omega K(\mathbf{x},\mathbf{y})\varphi(\mathbf{y})\,d\mathbf{y}$ es **compacto** en $L^2(\Omega)$. Por tanto vale toda la teoría de Fredholm.

> [!demostracion] Esquema
> **Paso 1 — integrabilidad.** Con $d\mathbf{y}=r^{n-1}\,dr\,d\sigma$ en coordenadas esféricas centradas en $\mathbf{x}$, $\int_\Omega\lvert\mathbf{x}-\mathbf{y}\rvert^{-\alpha}d\mathbf{y}\le c_n\int_0^{R}r^{n-1-\alpha}\,dr$, finito porque $n-1-\alpha>-1\iff\alpha<n$. El núcleo es integrable uniformemente en $\mathbf{x}$. **Paso 2 — aproximación.** Truncando la singularidad, $K_\varepsilon(\mathbf{x},\mathbf{y})= K(\mathbf{x},\mathbf{y})\,\mathbf{1}_{\lvert\mathbf{x}-\mathbf{y}\rvert>\varepsilon}$ es de Hilbert–Schmidt (acotado, $\int\int\lvert K_\varepsilon\rvert^2<\infty$), luego compacto. **Paso 3 — límite.** Por el Paso 1, $\lVert K-K_\varepsilon\rVert\to0$ cuando $\varepsilon\to0$ (la cola de la integral tiende a cero uniformemente). Un límite en norma de operadores compactos es compacto. $\blacksquare$

> [!proposicion] El "milagro de la dimensión", en una línea
> El mismo exponente $\alpha$ que haría **divergente** una integral en 1D la deja **convergente** en 3D. Por eso las ecuaciones integrales de la física en $\mathbb{R}^3$ —con sus núcleos $1/r$— son tan manejables: la geometría del espacio absorbe la singularidad de la solución fundamental.

## Resumen

> [!resumen]
> | Aspecto | 1D (intervalo) | $n$ dimensiones ($\Omega\subset\mathbb{R}^n$) |
> |---|---|---|
> | Maquinaria de Fredholm | Neumann, resolvente, alternativa | **idéntica** (basta compacidad) |
> | Núcleo simétrico | Hilbert–Schmidt, base ortogonal | **igual**, en $L^2(\Omega)$ |
> | Núcleo separable | sistema lineal finito | **mismo** sistema finito |
> | Singularidad $\lvert\mathbf{x}-\mathbf{y}\rvert^{-\alpha}$ | integrable si $\alpha<1$ | integrable si $\alpha<n$ |

> [!corolario]
> La dimensión no añade dificultad **teórica**: Fredholm es Fredholm porque el operador es compacto, no porque el dominio sea un intervalo. Lo único genuinamente nuevo es geométrico —los núcleos débilmente singulares de la [[Solucion Fundamental| solución fundamental]]—, y ahí la dimensión juega a favor: cuanto mayor es $n$, más singularidad tolera la integral.

> [!referencia]
> - La teoría base que se reutiliza: [[Fredholm Segunda Especie]].
> - El origen físico de los núcleos: [[Solucion Fundamental]].
> - Las aplicaciones: [[Teoria de Potencial]], [[Ecuacion de Lippmann-Schwinger]].
> - El índice de la sección: [[Multivariable/index]].
