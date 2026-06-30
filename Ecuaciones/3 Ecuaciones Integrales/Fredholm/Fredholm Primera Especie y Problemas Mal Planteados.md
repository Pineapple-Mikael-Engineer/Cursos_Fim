---
title: Fredholm Primera Especie y Problemas Mal Planteados
order: 2
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - fredholm
  - mal-planteado
draft: false
aliases:
  - Fredholm de primera especie
  - problemas mal planteados
  - regularización de Tikhonov
  - first kind Fredholm
  - ill-posed problems
  - Tikhonov regularization
---

# Fredholm Primera Especie y Problemas Mal Planteados

> [!definicion]
> Una **ecuación de Fredholm de 1ª especie** tiene la incógnita **solo dentro** de la integral:
> $$f(x)=\int_{a}^{b}K(x,t)\,\varphi(t)\,dt.$$
> El operador integral $K$ es **compacto**: promedia y **suaviza** a $\varphi$, de modo que su inversa $K^{-1}$ resulta **no acotada**. Por eso es un problema **mal planteado** en el sentido de Hadamard: aunque exista solución, **no depende de forma continua** de los datos — pequeñas perturbaciones de $f$ (ruido de medición) se **amplifican** sin control en $\varphi$.

> [!info]
> Es la cara **inversa** de [[Fredholm Segunda Especie| Fredholm de 2ª especie]] dentro del [[Fredholm/index| bloque de Fredholm]]: en la 2ª especie buscamos un $\varphi$ que también aparece fuera (problema estable); en la 1ª especie solo está dentro (problema inestable). Es el modelo de los **problemas inversos**: medir un efecto $f$ y reconstruir la causa $\varphi$ (deconvolución, tomografía, restauración de imágenes). La versión de Volterra es el [[Problema de Abel| problema de Abel]].

---

## Ejemplo

> [!ejemplo] Por qué la primera especie es inestable
> ![[mal_planteado.svg|480]]
>
> Los valores singulares $\sigma_n$ del núcleo decaen rápido; al invertir, los factores $1/\sigma_n$ explotan y amplifican el ruido. El filtro de Tikhonov $\sigma_n^2/(\sigma_n^2+\alpha)$ corta los modos inestables y estabiliza la reconstrucción.

---

## En qué consiste

> [!teoria]
> La herramienta para entender —y curar— el mal planteamiento es la **descomposición en valores singulares** del operador. Un núcleo compacto admite el desarrollo
> $$K(x,t)=\sum_{n}\sigma_n\,u_n(x)\,v_n(t),\qquad \sigma_1\ge\sigma_2\ge\cdots\to 0,$$
> con $\{u_n\}$ y $\{v_n\}$ bases ortonormales y $\sigma_n$ los **valores singulares**. Proyectando $f=\sum_n\langle f,u_n\rangle u_n$, la solución formal es
> $$\varphi=\sum_{n}\frac{\langle f,u_n\rangle}{\sigma_n}\,v_n.$$
> Aquí está el problema: dividir por valores singulares $\sigma_n$ **minúsculos** multiplica por $1/\sigma_n$ **enorme**. El ruido de $f$, que vive sobre todo en los modos de alta frecuencia (índices grandes, $\sigma_n$ diminutos), se **amplifica** y arruina la reconstrucción.
>
> **Regularización de Tikhonov.** En lugar de exigir $K\varphi=f$ exactamente, se **minimiza**
> $$\lVert K\varphi-f\rVert^{2}+\alpha\,\lVert\varphi\rVert^{2},\qquad\alpha>0,$$
> donde el término $\alpha\lVert\varphi\rVert^2$ **penaliza** soluciones grandes y oscilantes. La solución regularizada introduce un **filtro** sobre cada modo:
> $$\varphi_\alpha=\sum_{n}\frac{\sigma_n^{2}}{\sigma_n^{2}+\alpha}\cdot\frac{\langle f,u_n\rangle}{\sigma_n}\,v_n.$$
> Para modos estables ($\sigma_n^2\gg\alpha$) el filtro $\sigma_n^2/(\sigma_n^2+\alpha)\approx1$ y no toca nada; para modos inestables ($\sigma_n^2\ll\alpha$) el filtro $\approx\sigma_n^2/\alpha\to0$ y los **apaga**. Así se atenúan los modos que el ruido haría explotar.

> [!teorema] Las tres condiciones de Hadamard
> Un problema está **bien planteado** si: (a) **existe** solución; (b) la solución es **única**; (c) depende **continuamente** de los datos. La Fredholm de 1ª especie con núcleo compacto viola (c): como $\sigma_n\to0$, el operador inverso $K^{-1}$ es **no acotado**, luego una perturbación $\delta f$ de norma pequeña puede producir $\delta\varphi=K^{-1}\delta f$ de norma arbitrariamente grande.

> [!demostracion] La inversa de un operador compacto es no acotada
> **Paso 1 — perturbar un modo alto.** Tomemos $\delta f=\varepsilon\,u_n$, una perturbación de los datos de norma $\lVert\delta f\rVert=\varepsilon$ tan pequeña como queramos, alineada con el $n$-ésimo modo.
>
> **Paso 2 — propagar por la inversa.** La solución correspondiente es $\delta\varphi=K^{-1}\delta f=\dfrac{\varepsilon}{\sigma_n}\,v_n$, cuya norma es $\lVert\delta\varphi\rVert=\varepsilon/\sigma_n$.
>
> **Paso 3 — dejar crecer el cociente.** El factor de amplificación es
> $$\frac{\lVert\delta\varphi\rVert}{\lVert\delta f\rVert}=\frac{1}{\sigma_n}\xrightarrow[n\to\infty]{}\infty,$$
> porque $\sigma_n\to0$. No existe ninguna constante $C$ con $\lVert K^{-1}g\rVert\le C\lVert g\rVert$ para todo $g$: la inversa es **no acotada** y la dependencia de los datos **no** es continua. $\blacksquare$

> [!algoritmo] Resolver una 1ª especie de forma estable (Tikhonov)
> 1. **Descompón** el núcleo en valores singulares $\sigma_n$ y modos $u_n,v_n$.
> 2. **Proyecta** los datos: calcula $\langle f,u_n\rangle$.
> 3. **Elige $\alpha$** (parámetro de regularización), p. ej. por el criterio de la discrepancia $\lVert K\varphi_\alpha-f\rVert\approx$ nivel de ruido.
> 4. **Reconstruye con filtro** $\varphi_\alpha=\sum_n\dfrac{\sigma_n}{\sigma_n^2+\alpha}\langle f,u_n\rangle\,v_n$.

> [!warning]
> Resolver una Fredholm de 1ª especie **sin regularizar** —por ejemplo invirtiendo numéricamente $K$ o dividiendo por $\sigma_n$ directamente— amplifica el error de medición y produce reconstrucciones que oscilan sin sentido físico. **Siempre regularizar** (Tikhonov, truncamiento de valores singulares, etc.) y ajustar $\alpha$ al nivel de ruido de los datos.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Forma | $f(x)=\int_a^b K(x,t)\varphi(t)\,dt$ (incógnita solo dentro) |
> | Operador | **compacto**, suaviza; inversa $K^{-1}$ **no acotada** |
> | Carácter | **mal planteado** (Hadamard): no hay dependencia continua |
> | Solución formal | $\varphi=\sum_n\frac{\langle f,u_n\rangle}{\sigma_n}v_n$, inestable si $\sigma_n\to0$ |
> | Tikhonov | minimizar $\lVert K\varphi-f\rVert^2+\alpha\lVert\varphi\rVert^2$ |
> | Filtro | $\dfrac{\sigma_n^2}{\sigma_n^2+\alpha}$ apaga los modos inestables |

> [!corolario]
> La 1ª especie es el prototipo de **problema inverso**: medir el efecto y reconstruir la causa. Su inestabilidad no es un defecto de método sino una propiedad intrínseca del operador compacto, y la única salida es la **regularización**, que sacrifica un poco de exactitud a cambio de estabilidad.

> [!referencia]
> - El problema directo, estable: [[Fredholm Segunda Especie]].
> - La versión de Volterra (1ª especie): [[Problema de Abel]].
> - Vista de conjunto: [[Fredholm/index]].
