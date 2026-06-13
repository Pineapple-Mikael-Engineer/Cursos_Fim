---
title: Campo de Direcciones e Isoclinas
tags:
  - ecuaciones
  - edo
  - teoria
  - fundamentos
  - metodo-geometrico
draft: false
aliases:
  - campo de direcciones
  - isoclinas
  - direction field
  - slope field
---

# Campo de Direcciones e Isoclinas

> [!definicion]
> La EDO de primer orden $y'=f(x,y)$ asigna a **cada punto** $(x,y)$ del plano una **pendiente**
> $f(x,y)$. El dibujo de pequeños segmentos con esa pendiente es el **campo de direcciones**. Una
> solución es una curva tangente al campo en todo punto. Una **isoclina** es el lugar
> $f(x,y)=m$ (pendiente constante): sobre ella todos los segmentos son paralelos.

> [!info]
> Es la lectura **geométrica** de una EDO, previa a cualquier método algebraico (libro, cap. 1.1.1).
> Da intuición de las [[Curvas Integrales y Soluciones| curvas integrales]] y de por qué no se
> cruzan ([[Existencia y Unicidad Picard| unicidad]]), incluso cuando la ecuación no se sabe
> resolver explícitamente.

---

## Ejemplo

> [!ejemplo]
> **Trazar el campo de $y'=2x$ y leer la solución.** La pendiente solo depende de $x$:
> - en $x=0$ todas las flechas son **horizontales** ($y'=0$),
> - en $x=1$ tienen pendiente $2$, en $x=-1$ pendiente $-2$, etc.
>
> Las **isoclinas** $2x=m$ son **rectas verticales** $x=m/2$: sobre cada vertical todos los
> segmentos son paralelos. Siguiendo el campo se adivinan **parábolas**; en efecto, integrando,
> $$y'=2x\ \Rightarrow\ y=x^2+c.$$
> Cada valor de $c$ sube o baja la parábola; el campo es su "esqueleto".

> [!ejemplo] Campo de direcciones e isoclinas de $y'=2x$
> ![[campo_direcciones.svg|460]]
>
> Segmentos con pendiente $2x$ (verde) y curvas integrales $y=x^2+c$ (dorado). Las isoclinas son
> verticales; sobre cada una las flechas son paralelas. Las parábolas **no se cruzan**.

> [!ejemplo]
> **Una isoclina que no es recta: $y'=\dfrac{x+y}{x-y}$.** La isoclina de pendiente $m$ es
> $$\frac{x+y}{x-y}=m\ \Longrightarrow\ y=\frac{m-1}{m+1}\,x,$$
> una **recta por el origen** distinta para cada $m$. El campo gira en espiral alrededor del origen
> (la ecuación es [[Ecuaciones Homogeneas| homogénea]] de grado cero, y
> se indefine sobre la recta $x=y$, donde la pendiente es vertical).

---

## En qué consiste

> [!teoria]
> El campo de direcciones convierte "resolver una EDO" en "seguir las flechas". Aporta tres cosas
> aun sin fórmula de la solución:
> 1. **Forma cualitativa** de las soluciones (crecen, decrecen, tienen asíntotas, equilibrios).
> 2. **Equilibrios**: donde $f(x,y)=0$ la solución es horizontal; soluciones constantes $y=$ cte si
>    $f$ no depende de $x$ ahí.
> 3. **Comportamiento asintótico**: hacia dónde tienden las curvas cuando $x\to\pm\infty$.

> [!algoritmo] Construir el campo a mano con isoclinas
> 1. Elige varios valores de pendiente $m$ (p. ej. $m=0,\pm1,\pm2$).
> 2. Para cada $m$, dibuja la **isoclina** $f(x,y)=m$.
> 3. Sobre esa curva, traza segmentos cortos **todos con pendiente $m$**.
> 4. "Conecta" siguiendo las tangentes para esbozar las curvas integrales.

> [!info] Isoclina vs. curva integral
> | | Isoclina | Curva integral |
> |---|---|---|
> | Definición | $f(x,y)=m$ (pendiente fija) | tangente al campo en todo punto |
> | Sobre ella | todas las flechas paralelas | la flecha es su propia tangente |
> | Relación | la **cruza** con pendiente $m$ | **es** la solución $y(x)$ |
> | La isoclina $m=0$ | candidatos a máximos/mínimos de $y(x)$ | — |

> [!warning]
> Una isoclina **no** es, en general, una solución. Solo lo sería si su propia pendiente coincidiera
> en todo punto con $m$ (caso excepcional). Confundirlas es el error típico al leer el dibujo.

## Conexión con lo cualitativo

> [!proposicion]
> Donde el campo está definido y es suave, por cada punto pasa **exactamente una** curva integral;
> por eso las soluciones **no se cruzan** (dos curvas que se cortaran darían dos pendientes en el
> punto de corte). Esta observación geométrica es la antesala del
> [[Existencia y Unicidad Picard| teorema de existencia y unicidad]].

## Resumen

> [!resumen]
> | Concepto | Definición | Para qué sirve |
> |---|---|---|
> | Campo de direcciones | segmento de pendiente $f(x,y)$ en cada punto | ver la forma de las soluciones sin resolver |
> | Isoclina | $f(x,y)=m$ | trazar el campo rápido; localizar extremos ($m=0$) |
> | Curva integral | curva tangente al campo | la solución $y(x)$ |
> | Equilibrio | $f=0$ (y sin dependencia en $x$) | soluciones constantes |

> [!corolario]
> El campo de direcciones es la EDO "tal cual es": una regla de pendientes. Todo método posterior
> —separar variables, factor integrante, series— es un atajo para **integrar** ese campo cuando
> tiene estructura. Cuando no la tiene, el dibujo y lo numérico siguen funcionando.

> [!referencia]
> - Qué curvas dibuja el campo: [[Curvas Integrales y Soluciones]].
> - Por qué no se cruzan: [[Existencia y Unicidad Picard]].
> - Primer método algebraico: [[Variables Separables]].
