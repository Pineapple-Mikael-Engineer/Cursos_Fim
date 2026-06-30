---
title: Compensador Lag (por Lugar de Raíces)
order: 7
tags:
  - control-clasico
  - diseno
  - lugar-raices
  - compensador
draft: false
aliases:
  - compensador lag
  - retardo de fase
  - lag por lugar de raíces
---

# Compensador Lag (por Lugar de Raíces)

> [!definicion]
> Compensador de **retardo** $G_c(s)=K_c\,\dfrac{s+z}{s+p}$ con $|p|<|z|$ (polo más cerca del origen que el cero, al revés que el [[Lead | lead]]). Aporta **ganancia a baja frecuencia**, generalizando la [[PI | acción PI]] sin integrador puro. Se ubica el par cero-polo muy cerca del origen, con razón $\beta=z/p>1$: multiplica el coeficiente de error estacionario por $\beta$ **sin** mover apreciablemente los polos dominantes (su aporte de ángulo en $s_d$ es casi nulo).

> [!info]
> Método de diseño por [[Lugar Raices/index | lugar de raíces]], hermano del [[Lead | lead]] (que corrige transitorio) y combinable en [[Lead Lag | lead-lag]]. Mejora el **error estacionario** ([[Coeficientes Kp Kv Ka | coeficientes]] $K_p,K_v,K_a$) manteniendo $s_d$ casi fijo. Alternativa frecuencial: [[Respuesta Frecuencia/Lag | lag por Bode]].

---

## Ejemplo

> [!ejemplo]
> **Mejorar el error sin mover el lugar.** Planta compensada en transitorio $G(s)=\dfrac{5}{s(s+2)}$ (realimentación unitaria), con polos dominantes deseados $s_d=-1+j2$ ya sobre el lugar. El error de velocidad actual es grande; se pide **reducirlo a la décima parte** (factor $10$).
>
> **Paso 1 — Coeficiente de error actual.** Sistema tipo 1, error de velocidad:
> $$K_{v,\text{viejo}}=\lim_{s\to0}s\,G(s)=\lim_{s\to0}s\cdot\frac{5}{s(s+2)}=\frac{5}{2}=2.5\;\Rightarrow\;e_{ss}=\frac{1}{K_v}=0.4.$$
>
> **Paso 2 — Factor de mejora requerido.** Para que $e_{ss}$ baje a $0.04$ hace falta $K_v=25$, es decir multiplicar por $10$:
> $$\beta=\frac{K_{v,\text{nuevo}}}{K_{v,\text{viejo}}}=\frac{z}{p}=10.$$
>
> **Paso 3 — Ubicar cero y polo cerca del origen.** Se elige el cero pequeño, p. ej. $z=0.1$, y el polo diez veces menor:
> $$p=\frac{z}{\beta}=\frac{0.1}{10}=0.01\;\Rightarrow\;G_c(s)=\frac{s+0.1}{s+0.01}.$$
>
> **Paso 4 — Verificar que casi no mueve $s_d$.** Aporte de ángulo del par en $s_d=-1+j2$:
> $$\angle(s_d+0.1)=\angle(-0.9+j2)=180^\circ-65.8^\circ=114.2^\circ,$$
> $$\angle(s_d+0.01)=\angle(-0.99+j2)=180^\circ-63.7^\circ=116.3^\circ,$$
> $$\Delta\angle=114.2^\circ-116.3^\circ=-2.1^\circ.$$
> Solo $-2.1^\circ$ (menor que el límite usual de $5^\circ$): el lugar **apenas** se desplaza, $s_d$ sigue siendo válido con un retoque mínimo de $K$.
>
> **Paso 5 — Comprobar la ganancia DC.** La razón $z/p=0.1/0.01=10$ multiplica la ganancia a baja frecuencia: el nuevo coeficiente es $K_v=2.5\times10=25$ y $e_{ss}=0.04$, justo lo pedido. El transitorio (polos dominantes $\approx -1+j2$) queda intacto, salvo una **cola lenta** que introduce el polo en $-0.01$.

> [!ejemplo]
> **Par cero-polo cerca del origen (lectura gráfica).**
>
> ![[lgr_lag_diseno.svg|600]]
>
> El cero y el polo del lag, juntos cerca del origen, casi no alteran el lugar cerca de $s_d$, pero multiplican la ganancia DC por $\beta=z/p$.

---

## En qué consiste

> [!teoria] Contribución de ángulo despreciable
> Si $z$ y $p$ están muy cerca entre sí y del origen, los vectores $(s_d+z)$ y $(s_d+p)$ vistos desde un $s_d$ lejano son casi paralelos: $\angle(s_d+z)-\angle(s_d+p)\approx0$. El lugar **no se desplaza** cerca de $s_d$. Pero en $s=0$ (DC) la razón $z/p$ sí multiplica la ganancia — de ahí la mejora de error sin tocar el transitorio.

> [!teorema] Mejora del coeficiente de error
> $$\frac{K_{v,\text{nuevo}}}{K_{v,\text{viejo}}}=\frac{z}{p}=\beta>1.$$
> Para reducir el error estacionario por un factor $\beta$ se elige $z/p=\beta$. (Vale igual para $K_p$ o $K_a$ según el [[Coeficientes Kp Kv Ka | tipo de sistema]].)

> [!algoritmo] Diseño
> 1. Verificar que el [[Reglas Construccion | lugar de raíces]] **ya pasa** por $s_d$ con la $K$ adecuada (si no, primero un [[Lead | lead]]).
> 2. Calcular la mejora de error necesaria: $\beta=z/p$ = factor de aumento del coeficiente de error.
> 3. Ubicar el par cero-polo **muy cerca del origen** (ambos pequeños) para que su aporte de ángulo en $s_d$ sea $<5^\circ$.
> 4. La ganancia DC se multiplica por $\beta=z/p$ sin mover apreciablemente $s_d$.

---

## Efecto

> [!info] Trade-offs del lag
> | Aspecto | Efecto |
> |---|---|
> | Error estacionario | **mejora** (factor $\beta$) |
> | Amortiguamiento / polos dominantes | casi sin cambio |
> | Velocidad de respuesta | **se reduce** (polo lento añade cola lenta) |
> | Ruido | no amplifica (filtra) |

> [!info] En MATLAB
> ```matlab
> G  = tf(5, [1 2 0]);             % 5/(s(s+2))
> Gc = tf([1 0.1], [1 0.01]);      % (s+0.1)/(s+0.01), beta=10
> [Kv_old] = dcgain(tf([5 0],[1 2 0])*1);  % aprox; o usar el limite
> rlocus(Gc*G)                     % el lugar casi no cambia cerca de s_d
> step(feedback(Gc*G,1))           % cola lenta visible
> ```

---

## Limitaciones

> [!warning]
> El lag **ralentiza** el sistema: el polo cercano al origen introduce un modo lento (cola larga en la respuesta al escalón). Si además se necesita mejorar el transitorio, combinar con [[Lead]] → [[Lead Lag | lead-lag]].

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Forma | $G_c(s)=K_c\dfrac{s+z}{s+p}$, $|p|<|z|$ |
> | Razón clave | $\beta=z/p>1$ (factor de mejora de error) |
> | Colocación | cero y polo cerca del origen; aporte $<5^\circ$ en $s_d$ |
> | Mejora | error estacionario ($\times\beta$) |
> | No mejora | transitorio; añade cola lenta |
> | Requisito | el lugar ya debe pasar por $s_d$ |

> [!corolario]
> El lag explota la asimetría entre el ángulo (casi nulo si cero y polo están juntos cerca del origen) y la ganancia DC (multiplicada por $z/p$): mejora el coeficiente de error por el factor $\beta=z/p$ sin desplazar los polos dominantes. El precio es una respuesta más lenta; para el transitorio se usa el [[Lead | lead]] o el [[Lead Lag | lead-lag]].

> [!referencia]
> - Acción equivalente: [[PI]].
> - Diseño alternativo por frecuencia: [[Respuesta Frecuencia/Lag | lag por Bode]].
> - Para el transitorio: [[Lead]] · [[Lead Lag]].
> - Coeficientes de error: [[Coeficientes Kp Kv Ka]] · [[Error Estacionario/index]].
