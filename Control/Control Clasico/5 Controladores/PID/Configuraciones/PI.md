---
title: Controlador PI
tags:
  - control-clasico
  - controladores
  - pid
draft: false
aliases:
  - PI
  - control PI
  - proporcional integral
---

# Controlador PI

> [!definicion]
> El control **proporcional-integral** suma a la acción proporcional un término proporcional a la integral del error. En forma estándar (ISA) y en forma paralela:
> $$G_c(s)=K_p\left(1+\frac{1}{T_i s}\right)=K_p+\frac{K_i}{s}=\frac{K_p\big(s+z\big)}{s},\qquad z=\frac{K_i}{K_p}=\frac{1}{T_i}.$$
> Añade un **polo en el origen** (integrador, sube el [[Coeficientes Kp Kv Ka | tipo]] en 1) y un **cero** en $s=-1/T_i$. El polo en el origen da ganancia infinita en DC y **elimina el error estacionario**; el cero atenúa el retardo de fase del integrador.

> [!info]
> Es una de las [[index | configuraciones del PID]], hermana de [[PD | PD]] y [[PID | PID]]. Combina las [[Acciones/index | acciones]] [[Proporcional P | P]] e [[Integral I | I]]. Es el caso límite del compensador **lag** del [[Lugar Raices/index | lugar de raíces]].

---

## Ejemplo

> [!ejemplo]
> **Diseñar un PI para anular el error estacionario de una planta tipo 0.** Sea la planta (realimentación unitaria)
> $$G(s)=\frac{1}{(s+1)(s+5)}.$$
> Con control proporcional queda error estacionario ante escalón. Se pide $e_{ss}=0$ a escalón conservando un transitorio razonable. Diseñar $G_c(s)=K_p\left(1+\dfrac{1}{T_i s}\right)$.
>
> **Paso 1 — Cuantificar el problema con P.** Constante de posición con $G_c=K_p$:
> $$K_{pos}=\lim_{s\to0}K_p\,G(s)=\frac{K_p}{1\cdot5}=\frac{K_p}{5},\qquad e_{ss}=\frac{1}{1+K_{pos}}=\frac{5}{5+K_p}.$$
> Para $K_p=10$ el error es $e_{ss}=5/15=0.33$ (33 %): inaceptable. Subir $K_p$ lo reduce pero nunca lo anula y degrada el transitorio.
>
> **Paso 2 — Añadir el integrador.** El PI introduce un polo en $s=0$, elevando el sistema a **tipo 1**. Entonces
> $$K_{pos}=\lim_{s\to0}G_c(s)G(s)=\infty\;\Rightarrow\;e_{ss}=\frac{1}{1+\infty}=0.$$
> El error estacionario a escalón pasa a ser **exactamente cero**, sin importar $K_p$.
>
> **Paso 3 — Ubicar el cero (regla del lag).** Para no distorsionar el transitorio, el cero $z=1/T_i$ se coloca **cerca del origen**, mucho menor que la parte real de los polos dominantes (que están cerca de $-1$). Se elige
> $$z=\frac{1}{T_i}=0.1\;\Rightarrow\;T_i=10\ \text{s}.$$
> Así el cero en $-0.1$ casi cancela el efecto del polo del integrador en la zona de los polos dominantes: el lugar de raíces apenas se mueve cerca de $-1$.
>
> **Paso 4 — Ganancia.** Manteniendo $K_p=5$ (elegido sobre el lugar de raíces para un $\zeta$ razonable), el controlador es
> $$G_c(s)=5\left(1+\frac{1}{10\,s}\right)=5+\frac{0.5}{s}=\frac{5(s+0.1)}{s},\qquad K_i=K_p/T_i=0.5.$$
>
> **Paso 5 — Verificación del efecto.** Lazo abierto $G_cG=\dfrac{5(s+0.1)}{s(s+1)(s+5)}$.
> - **Error estacionario:** $e_{ss}=0$ a escalón (tipo 1). Logrado.
> - **Transitorio:** como $z=0.1\ll1$, los polos dominantes apenas se desplazan respecto al caso P; aparece un polo lento de lazo cerrado cerca del cero, que se cancela casi por completo con él → un transitorio adicional pequeño y lento ("cola").
> - **Coste:** el integrador resta $90^\circ$ de fase a baja frecuencia (parcialmente recuperados por el cero), por lo que el **margen de fase baja** y el **sobrepico tiende a subir** respecto a P con la misma $K_p$.

> [!ejemplo] Respuesta PI vs P
> ![[pi_vs_p_escalon.svg|550]]
>
> P deja offset permanente; PI lo elimina por completo, a cambio de una respuesta algo más lenta y mayor sobrepico.

---

## En qué consiste

> [!teoria]
> El PI **acumula** el error en el tiempo: mientras quede error, la integral sigue creciendo y empuja la salida hasta que $e=0$. Esa es la razón física de que anule el offset. En frecuencia, el polo en el origen da pendiente $-20\ \text{dB/dec}$ y fase $-90^\circ$ a baja frecuencia (ganancia DC infinita); el cero $z=1/T_i$ devuelve fase a frecuencia media para no arruinar el margen.
>
> El compromiso clave es la posición del cero: cerca del origen ⇒ poco daño al transitorio pero integración lenta; más a la derecha ⇒ corrige el error más rápido pero distorsiona más los polos dominantes.

> [!teorema] PI como retardo (lag)
> El PI es el caso límite del **compensador lag** $\dfrac{s+z}{s+p}$ con el polo en el origen ($p=0$):
> $$G_c(s)=K_p\,\frac{s+z}{s},\qquad z=\frac{K_i}{K_p}=\frac{1}{T_i}.$$
> Mejora el **error estacionario** (ganancia infinita en DC) sin alterar mucho el transitorio si el cero $z$ se coloca **cerca del origen**, lejos de los polos dominantes.

> [!regla] Ubicación del cero
> Colocar el cero $z=K_i/K_p=1/T_i$ **a la izquierda y cerca del origen** (mucho menor que la parte real de los polos dominantes) para:
> - mantener el [[Lugar Raices/index | lugar de raíces]] casi sin distorsión cerca de los polos dominantes,
> - aportar la ganancia integral sin degradar el [[Margenes MF MG | margen de fase]].

---

## Limitaciones

> [!warning]
> El PI **no mejora el transitorio** (no aporta adelanto de fase); si se necesita más amortiguamiento, usar [[PD | PD]] o [[PID | PID]]. El integrador resta margen de fase, por lo que tiende a aumentar el sobrepico. Además, ante saturación del actuador el integrador sufre ***windup*** (sigue acumulando error): exige [[Integral I | anti-windup]].

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | FT (ISA) | $G_c(s)=K_p\left(1+\dfrac{1}{T_i s}\right)$ |
> | FT (paralela) | $K_p+\dfrac{K_i}{s}=\dfrac{K_p(s+z)}{s}$ |
> | Aporta | polo en el origen + cero en $-1/T_i$ |
> | Equivale a | compensador **lag** |
> | Error estacionario | **eliminado** (escalón) |
> | Sobrepico $M_p$ | tiende a subir |
> | Velocidad | algo menor |
> | Margen de fase | se reduce (mitigado por el cero) |
> | Ruido | no lo amplifica (sin D) |

> [!corolario]
> El PI sube el tipo del sistema en 1 gracias al polo en el origen, anulando el error estacionario a escalón; el cero $z=1/T_i$ cerca del origen recupera fase para no destrozar el transitorio. El precio es un margen de fase menor (más sobrepico) y el riesgo de *windup*. Es la configuración reina en procesos lentos y ruidosos. Para añadir amortiguamiento conviene la acción derivativa ([[PD | PD]], [[PID | PID]]).

> [!referencia]
> - Acciones que combina: [[Proporcional P]] · [[Integral I]].
> - Para mejorar el transitorio: [[PD]] · [[PID]].
> - Compensador lag equivalente: [[Lugar Raices/index]].
> - Tipo y error estacionario: [[Coeficientes Kp Kv Ka]].
> - Marco general: [[index]].
> - Sintonización: [[Sintonizacion/index]].
