---
title: Compensador Lead (por Lugar de Raíces)
tags:
  - control-clasico
  - diseno
  - lugar-raices
  - compensador
draft: false
aliases:
  - compensador lead
  - adelanto de fase
  - lead por lugar de raíces
---

# Compensador Lead (por Lugar de Raíces)

> [!definicion]
> Compensador de **adelanto** $G_c(s)=K_c\,\dfrac{s+z}{s+p}$ con $|z|<|p|$ (cero más cerca del origen que el polo). Aporta **fase positiva**, generalizando la [[PD | acción PD]] de forma realizable. Se diseña por la **deficiencia de ángulo**: si los polos dominantes deseados $s_d$ no están sobre el lugar, el lead añade el ángulo faltante $\phi_{def}=180^\circ-\angle G(s_d)H(s_d)$ para que el lugar pase por $s_d$; luego $K_c$ se fija con la condición de magnitud.

> [!info]
> Método de diseño por [[Lugar Raices/index | lugar de raíces]], hermano del [[Lag | lag]] (que corrige error) y combinable en [[Lead Lag | lead-lag]]. Mejora el **transitorio**: sube el [[Segundo Orden/index | amortiguamiento]] $\zeta$ y la velocidad $\omega_n$ reubicando los polos dominantes más a la izquierda. Alternativa frecuencial: [[Respuesta Frecuencia/Lead | lead por Bode]].

---

## Ejemplo

> [!ejemplo]
> **Diseño completo por deficiencia de ángulo.** Planta $G(s)=\dfrac{1}{s(s+2)}$ (realimentación unitaria, $H=1$). Especificaciones: $\zeta=0.5$ y $\omega_n=4$ rad/s para los polos dominantes (transitorio más rápido que la planta).
>
> **Paso 1 — Polos dominantes deseados.**
> $$s_d=-\zeta\omega_n\pm j\omega_n\sqrt{1-\zeta^2}=-0.5\cdot4\pm j\,4\sqrt{1-0.25}=-2\pm j3.46.$$
>
> **Paso 2 — Ángulo de $G(s_d)$ (deficiencia).** Vectores desde los polos de la planta ($0$ y $-2$) hasta $s_d=-2+j3.46$:
> $$\angle(s_d-0)=\angle(-2+j3.46)=180^\circ-60^\circ=120^\circ,$$
> $$\angle(s_d+2)=\angle(0+j3.46)=90^\circ.$$
> $$\angle G(s_d)=-\big(120^\circ+90^\circ\big)=-210^\circ.$$
>
> **Paso 3 — Deficiencia de ángulo.** La condición de ángulo exige $\angle G(s_d)=-180^\circ$ (es decir $\pm180^\circ$). Falta:
> $$\phi_{def}=-180^\circ-\angle G(s_d)=-180^\circ-(-210^\circ)=+30^\circ.$$
> El lead debe aportar **$+30^\circ$** en $s_d$.
>
> **Paso 4 — Colocar cero y polo.** Estrategia simple: cancelar el polo de la planta en $-2$ poniendo el **cero en $z=2$** ($s+2$). El cero aporta entonces $\angle(s_d+2)=90^\circ$. El polo debe restar de modo que $\angle(s_d+z)-\angle(s_d+p)=30^\circ$:
> $$90^\circ-\angle(s_d+p)=30^\circ\;\Rightarrow\;\angle(s_d+p)=60^\circ.$$
> Con $s_d=-2+j3.46$ y polo en $-p$ (real): $\angle(-2+p+j3.46)=60^\circ\Rightarrow \dfrac{3.46}{p-2}=\tan60^\circ=1.732\Rightarrow p-2=2\Rightarrow p=4$.
> Compensador: $G_c(s)=K_c\dfrac{s+2}{s+4}$.
>
> **Paso 5 — Ganancia $K_c$ por condición de magnitud** $|G_c(s_d)G(s_d)|=1$. Como el cero cancela el polo en $-2$:
> $$G_c G=K_c\frac{s+2}{s+4}\cdot\frac{1}{s(s+2)}=\frac{K_c}{s(s+4)}.$$
> $$|s_d|=|-2+j3.46|=4,\qquad |s_d+4|=|2+j3.46|=4.$$
> $$\frac{K_c}{4\cdot4}=1\;\Rightarrow\;K_c=16.$$
>
> **Paso 6 — Resultado.** $\boxed{G_c(s)=16\,\dfrac{s+2}{s+4}}$. El lazo abierto compensado $\dfrac{16}{s(s+4)}$ tiene sus polos dominantes en $-2\pm j3.46$: $\zeta=0.5$, $\omega_n=4$ rad/s — el doble de rápido que la planta sin compensar, con el mismo amortiguamiento.

> [!ejemplo]
> **Reubicación de polos (lectura gráfica).**
>
> ![[lgr_lead_diseno.svg|600]]
>
> El cero del lead "atrae" las ramas hacia el semiplano izquierdo; los polos dominantes pasan a $s_d$, con mayor $\zeta$ y $\omega_n$.

---

## En qué consiste

> [!teoria]
> Los polos de lazo cerrado solo pueden estar sobre el lugar de raíces de $G(s)H(s)$. Si los $s_d$ deseados no caen sobre él, $\angle G(s_d)H(s_d)\neq\pm180^\circ$ y falta un ángulo $\phi_{def}$. El lead inserta un par cero-polo cuyo aporte neto $\angle(s_d+z)-\angle(s_d+p)=\phi_{def}>0$ desplaza el lugar para que pase por $s_d$. El cero, más cercano al origen, **atrae** el lugar hacia la izquierda.

> [!algoritmo] Diseño por deficiencia de ángulo
> 1. De las especificaciones ($M_p$, $t_s$) obtener los **polos dominantes deseados** $s_d=-\zeta\omega_n\pm j\omega_d$.
> 2. Evaluar la [[Condicion Angulo Magnitud | condición de ángulo]] de $GH$ en $s_d$. La deficiencia es $\phi_{def}=180^\circ-\angle G(s_d)H(s_d)$.
> 3. Elegir cero y polo tales que $\angle(s_d+z)-\angle(s_d+p)=\phi_{def}$ (con $|z|<|p|$).
> 4. Calcular $K_c$ con la condición de magnitud $|G_c\,GH|=1$ en $s_d$.

> [!regla] Colocación del cero y el polo
> - Hay **infinitas** soluciones (cero+polo) que dan $\phi_{def}$; se elige por criterios adicionales.
> - Ubicar el **cero cerca de $s_d$** o cancelando un polo real de la planta simplifica el cálculo.
> - El polo lo más a la **izquierda** posible, pero no tanto que amplifique ruido (limita la separación $p/z$).
> - Regla de bisección (Ogata): maximiza la separación útil entre cero y polo.

---

## Efecto

> [!info] Trade-offs del lead
> | Aspecto | Efecto |
> |---|---|
> | Amortiguamiento $\zeta$ | **mejora** |
> | Velocidad $\omega_n$ / ancho de banda | aumenta |
> | Sobrepico $M_p$, $t_s$ | bajan |
> | Error estacionario | **apenas mejora** (para eso, [[Lag]]) |
> | Ruido | amplifica (cero) |

> [!info] En MATLAB
> ```matlab
> G  = tf(1, [1 2 0]);        % 1/(s(s+2))
> Gc = 16 * tf([1 2], [1 4]); % 16 (s+2)/(s+4)
> rlocus(Gc*G)                % el lugar ya pasa por -2 +- j3.46
> step(feedback(Gc*G,1))      % transitorio mejorado
> ```

---

## Limitaciones

> [!warning]
> El lead **no** corrige el error estacionario significativamente (su ganancia DC $K_c\,z/p$ es modesta) y **amplifica el ruido** de alta frecuencia por el cero. Si además se requiere error pequeño/nulo, combinar con [[Lag]] → [[Lead Lag | lead-lag]].

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Forma | $G_c(s)=K_c\dfrac{s+z}{s+p}$, $|z|<|p|$ |
> | Diseño | aportar $\phi_{def}=180^\circ-\angle G(s_d)H(s_d)$ |
> | Cero/polo | $\angle(s_d+z)-\angle(s_d+p)=\phi_{def}$ |
> | Ganancia | $K_c$ por $|G_c\,GH|=1$ en $s_d$ |
> | Mejora | transitorio ($\zeta$, $\omega_n$) |
> | No mejora | error estacionario; amplifica ruido |

> [!corolario]
> Diseñar un lead por lugar de raíces es resolver una deficiencia de ángulo: ubicar un par cero-polo (cero más cercano al origen) que aporte el ángulo faltante en $s_d$ y ajustar $K_c$ por magnitud. El resultado son polos dominantes más rápidos y mejor amortiguados, a costa de más ruido y sin tocar apenas el error; para el error, va el [[Lag | lag]].

> [!referencia]
> - Acción equivalente: [[PD]].
> - Diseño alternativo por frecuencia: [[Respuesta Frecuencia/Lead | lead por Bode]].
> - Para el error estacionario: [[Lag]] · [[Lead Lag]].
> - Base: [[Condicion Angulo Magnitud]] · [[Reglas Construccion]] · [[Segundo Orden/index]].
