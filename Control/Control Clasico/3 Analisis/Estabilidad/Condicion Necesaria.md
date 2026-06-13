---
title: Condición Necesaria de Estabilidad
tags:
  - control-clasico
  - teoria
  - analisis
  - estabilidad
draft: false
aliases:
  - condicion necesaria
  - coeficientes positivos
  - condicion polinomio
---

# Condición Necesaria de Estabilidad

> [!definicion]
> Para que un sistema LTI con polinomio característico $P(s)=a_n s^n+\dots+a_1 s+a_0$ sea **estable**, todos sus coeficientes deben tener el **mismo signo** y **ninguno** puede ser cero. Es **necesaria pero no suficiente**: sirve para descartar de un vistazo, no para confirmar. En orden 1 y 2 es además suficiente.

> [!info]
> Filtro previo de [[index | estabilidad]] antes de aplicar el criterio completo de [[Routh Hurwitz/index | Routh-Hurwitz]]. El polinomio característico sale del denominador de la [[Funcion Transferencia/index | función de transferencia]].

---

## Ejemplo

> [!ejemplo] Descartar inestables por inspección
> Aplicar el filtro a cuatro polinomios **sin calcular polos**.
>
> | $P(s)$ | Coeficientes | ¿Pasa el filtro? | Veredicto |
> |---|---|---|---|
> | $s^2+5s+6$ | $1,5,6$ | sí (todos $>0$) | candidato a estable |
> | $s^3+2s^2-s+4$ | $1,2,-1,4$ | **no** (signo mezclado) | **inestable seguro** |
> | $s^3+2s^2+3$ | $1,2,0,3$ | **no** (falta $s^1$) | **inestable/marginal** |
> | $s^3+s^2+2s+8$ | $1,1,2,8$ | sí (todos $>0$) | **indeciso** → usar Routh |
>
> Las dos filas centrales se descartan **sin más cuentas**. La última pasa el filtro pero no garantiza nada: hay que ir a Routh-Hurwitz (resulta inestable, ver abajo).

> [!ejemplo] Pasa el filtro y aun así es inestable (orden 3)
> $$P(s)=s^3+s^2+2s+8,\qquad \text{coef. }1,1,2,8>0\ ✓$$
> La condición necesaria se cumple, pero la **condición adicional** de orden 3 es $a_2a_1>a_3a_0$:
> $$a_2a_1=1\cdot2=2,\qquad a_3a_0=1\cdot8=8,\qquad 2>8\ \text{❌}.$$
> Falla → **inestable**. Confirma que coeficientes positivos no bastan a partir de orden 3.

> [!ejemplo] Semiplanos de estabilidad
> ![[estabilidad_semiplanos.svg|560]]
>
> Todos los polos en el semiplano izquierdo ($\Re(p)<0$) → estable; sobre el eje imaginario → marginal; alguno en el derecho → inestable. La condición de coeficientes es la huella algebraica de "todos los polos a la izquierda".

---

## Por qué es necesaria

> [!teorema] Condición necesaria
> Si $P(s)=a_n s^n+\dots+a_0$ es estable, entonces todos los $a_i$ tienen el mismo signo y ninguno es nulo.

> [!demostracion] Producto de factores estables
> **Paso 1 — Factorizar por polos.** $P(s)=a_n\prod_i(s-p_i)$. Si es estable, todo polo cumple $\Re(p_i)<0$.
>
> **Paso 2 — Polos reales.** Un polo real estable es $p_i=-\alpha_i$ con $\alpha_i>0$; aporta el factor $(s+\alpha_i)$, de coeficientes **positivos**.
>
> **Paso 3 — Pares complejos.** Un par $p=-\sigma\pm j\omega$ con $\sigma>0$ aporta
> $$(s+\sigma-j\omega)(s+\sigma+j\omega)=s^2+2\sigma s+(\sigma^2+\omega^2),$$
> de coeficientes $1,\,2\sigma,\,\sigma^2+\omega^2$, todos **positivos**.
>
> **Paso 4 — Producto.** $P(s)=a_n\cdot\prod(\text{factores de coef. positivos})$. Multiplicar polinomios de coeficientes positivos nunca produce un coeficiente negativo ni nulo. Luego todos los $a_i$ comparten el signo de $a_n$. $\blacksquare$

> [!corolario] Por qué no es suficiente
> La demostración va en un solo sentido: que el producto tenga coeficientes positivos **no obliga** a que cada factor sea estable. A partir de orden 3, términos cruzados pueden recomponer coeficientes positivos a partir de factores con $\Re>0$ (ejemplo $s^3+s^2+2s+8$).

---

## Casos particulares

> [!demostracion] Orden 1 — necesaria y suficiente
> $P(s)=a_1 s+a_0$, polo $s=-a_0/a_1$.
>
> | Condición | Conclusión |
> |---|---|
> | $a_0,a_1$ mismo signo | polo $<0$ → **estable** |
> | $a_0,a_1$ signo distinto | polo $>0$ → **inestable** |
> | $a_0=0$ | polo en $0$ → marginal |

> [!demostracion] Orden 2 — necesaria y suficiente
> $P(s)=a_2 s^2+a_1 s+a_0$, polos $s=\dfrac{-a_1\pm\sqrt{a_1^2-4a_2a_0}}{2a_2}$.
>
> Ambos polos tienen $\Re<0$ **si y solo si** $a_2,a_1,a_0$ comparten signo. No hay condición extra: el filtro decide.

> [!demostracion] Orden 3 — hace falta una condición extra
> $P(s)=a_3 s^3+a_2 s^2+a_1 s+a_0$. Es estable si y solo si:
> 1. todos los coeficientes con el mismo signo, **y**
> 2. $a_2 a_1>a_3 a_0$.
>
> El término (1) es la condición necesaria; (2) es lo que añade [[Routh Hurwitz/index | Routh-Hurwitz]].

---

## Uso en diseño

> [!info] Primer filtro con parámetro
> Con un parámetro $K$, la condición necesaria acota su rango antes de Routh. Para
> $$P(s)=s^3+3s^2+2s+K,$$
> todos los coeficientes $>0$ exige $K>0$. Routh estrecha luego el rango: la fila $s^1$ da $\frac{3\cdot2-K}{3}>0\Rightarrow K<6$. Rango final $0<K<6$. Ver [[Routh Hurwitz/Ajuste Parametros | ajuste de parámetros]].

---

## Limitaciones

> [!warning]
> 1. **No suficiente** desde orden 3: muchos polinomios de coeficientes positivos son inestables.
> 2. **No detecta** estabilidad marginal por sí sola (coeficientes positivos y aun así oscilación).
> 3. **No aplica** a sistemas con retardo $e^{-sT}$ (introduce términos no polinomiales).
> 4. **No mide** el grado de estabilidad ni la ubicación de los polos.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Enunciado | $a_i$ mismo signo y todos $\ne0$ |
> | Carácter | necesaria, no suficiente ($n\ge3$) |
> | Orden 1 y 2 | también suficiente |
> | Orden 3 extra | $a_2a_1>a_3a_0$ |
> | Uso | descarte rápido y primer filtro de $K$ |

> [!corolario]
> La condición necesaria es el cribado barato de la estabilidad: mira los coeficientes y descarta de inmediato los signos mezclados o términos faltantes. Lo que pasa el filtro queda **indeciso** y debe ir a [[Routh Hurwitz/index | Routh-Hurwitz]], que sí es necesario y suficiente.

> [!referencia]
> - Marco general: [[index]].
> - Criterio completo: [[Routh Hurwitz/index]].
> - Construcción de la tabla: [[Construccion Tabla]].
> - Rango de un parámetro: [[Routh Hurwitz/Ajuste Parametros]].
