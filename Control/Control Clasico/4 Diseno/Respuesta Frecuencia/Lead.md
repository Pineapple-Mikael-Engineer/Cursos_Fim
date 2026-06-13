---
title: Compensador Lead (por Frecuencia)
tags:
  - control-clasico
  - diseno
  - respuesta-frecuencial
  - compensador
draft: false
aliases:
  - lead por Bode
  - adelanto por frecuencia
  - diseño lead frecuencial
---

# Compensador Lead (por Frecuencia)

> [!definicion]
> Compensador de **adelanto de fase** que se diseña sobre el [[Bode/index | Bode]] para subir el [[Margenes MF MG | margen de fase]]:
> $$G_c(s) = K_c\,\alpha\,\frac{Ts + 1}{\alpha Ts + 1}, \qquad 0 < \alpha < 1.$$
> Aporta su fase máxima $\phi_m$ en $\omega_m=\dfrac{1}{T\sqrt\alpha}$, con $\sin\phi_m=\dfrac{1-\alpha}{1+\alpha}$ y magnitud $|G_c(j\omega_m)|=1/\sqrt\alpha$ sobre $K_c\alpha$. Equivale al [[Lugar Raices/Lead | lead]] $K_c\frac{s+z}{s+p}$ con $z=1/T<p=1/(\alpha T)$.

> [!info]
> Vive en `4 Diseno/Respuesta Frecuencia/`. Es la versión frecuencial del lead; el diseño por plano-$s$ está en [[Lugar Raices/Lead]] y su análogo PID es el [[PD]]. Hermanas: [[Respuesta Frecuencia/Lag | Lag]] (error estacionario) y [[Lead Lag | Lead-lag]] (ambos). Marco general en [[Respuesta Frecuencia/index]].

---

## Ejemplo

> [!ejemplo]
> **Diseño de lead por margen de fase, paso a paso.** Planta $G(s)=\dfrac{K}{s(s+2)}$. Specs: $K_v\ge10$ (error a rampa $\le0.1$) y $\text{MF}\ge50^\circ$.
>
> **Paso 1 — Ganancia por error estacionario.** $K_v=\lim_{s\to0}sG(s)=K/2\ge10\Rightarrow K=20$. Con esto $L_0(s)=\dfrac{20}{s(s+2)}$ (la $K_c$ del lead se ajusta luego para no alterar este $K_v$).
>
> **Paso 2 — MF actual.** Cruce de ganancia: $|L_0(j\omega_c)|=\dfrac{20}{\omega_c\sqrt{\omega_c^2+4}}=1\Rightarrow\omega_c\approx4.2\ \text{rad/s}$. Fase: $-90^\circ-\arctan(4.2/2)=-154.5^\circ$, luego $\text{MF}_0=180^\circ-154.5^\circ\approx25.5^\circ$.
>
> **Paso 3 — Adelanto necesario.** Déficit $=50^\circ-25.5^\circ=24.5^\circ$. Como el lead **mueve el cruce** a mayor frecuencia (donde la planta tiene menos fase), se añade un margen de seguridad de $\sim5^\circ$–$8^\circ$:
> $$\phi_m=24.5^\circ+5.5^\circ\approx30^\circ.$$
>
> **Paso 4 — Calcular $\alpha$:**
> $$\alpha=\frac{1-\sin30^\circ}{1+\sin30^\circ}=\frac{1-0.5}{1+0.5}=\frac{0.5}{1.5}=\boxed{0.333}.$$
>
> **Paso 5 — Nuevo cruce $\omega_m$.** El lead añade $+10\log(1/\alpha)$ dB en $\omega_m$; se coloca $\omega_m$ donde la planta valga $-10\log(1/\alpha)$ dB, para que el nuevo cruce caiga justo en $\omega_m$:
> $$-10\log_{10}(1/\alpha)=-10\log_{10}(3)=-4.77\ \text{dB}.$$
> Se busca $\omega$ tal que $|L_0(j\omega)|=+4.77$ dB $=1.73$: $\dfrac{20}{\omega\sqrt{\omega^2+4}}=1.73\Rightarrow\omega_m\approx5.4\ \text{rad/s}$.
>
> **Paso 6 — Constantes del lead.**
> $$T=\frac{1}{\omega_m\sqrt\alpha}=\frac{1}{5.4\sqrt{0.333}}=\frac{1}{5.4\cdot0.577}\approx0.321\ \text{s}.$$
> $$z=\frac{1}{T}\approx3.12,\qquad p=\frac{1}{\alpha T}=\frac{z}{\alpha}\approx9.36.$$
> El factor $K_c\alpha$ debe valer 1 a baja frecuencia para no tocar $K_v$, luego $K_c=1/\alpha=3$. Compensador:
> $$G_c(s)=3\cdot0.333\,\frac{0.321s+1}{0.107s+1}=\frac{s+3.12}{s/3+3.12}\quad\Longleftrightarrow\quad K_c\frac{s+z}{s+p}\ \text{con }z=3.12,\ p=9.36.$$
>
> **Paso 7 — Verificación.** En $\omega_m=5.4$: fase de la planta $-90^\circ-\arctan(5.4/2)=-159.7^\circ$; el lead aporta $+30^\circ$ → fase total $-129.7^\circ$ → $\text{MF}\approx50.3^\circ\ge50^\circ$. ✓ Se cumple sin perder $K_v$. Si la verificación quedara corta, se itera el Paso 3 con más margen.

> [!ejemplo]
> **Bode del compensador lead (joroba de fase).**
>
> ![[bode_lead_compensador.svg|550]]
>
> La fase forma una "joroba" con pico $\phi_m$ centrado en $\omega_m=\sqrt{zp}$ (media geométrica de las esquinas); la magnitud sube $+20$ dB/dec entre $z=1/T$ y $p=1/(\alpha T)$. Diseñar el lead es **deslizar y dimensionar** esa joroba para que su pico caiga en el nuevo cruce de ganancia.

---

## En qué consiste

> [!teorema] Pico de fase
> El lead aporta su fase máxima $\phi_m$ en la media geométrica de sus esquinas:
> $$\sin\phi_m = \frac{1 - \alpha}{1 + \alpha}, \qquad \alpha = \frac{1 - \sin\phi_m}{1 + \sin\phi_m}, \qquad \omega_m = \frac{1}{T\sqrt\alpha} = \sqrt{z\,p}.$$
> En $\omega_m$ la magnitud vale $|G_c(j\omega_m)| = 1/\sqrt\alpha$, es decir $+10\log(1/\alpha)$ dB sobre la asíntota $K_c\alpha$.

> [!demostracion]
> **Paso 1.** La fase del lead (con $K_c\alpha$ real) es $\phi(\omega)=\arctan(\omega T)-\arctan(\alpha\omega T)$.
> **Paso 2.** Derivando e igualando a cero, $\dfrac{d\phi}{d\omega}=0$ da $\omega^2=\dfrac{1}{\alpha T^2}$, luego $\omega_m=\dfrac{1}{T\sqrt\alpha}$, que es $\sqrt{(1/T)(1/\alpha T)}=\sqrt{zp}$.
> **Paso 3.** Sustituyendo $\omega_m$: $\tan\phi_m=\dfrac{\omega_mT-\alpha\omega_mT}{1+\alpha\omega_m^2T^2}=\dfrac{(1-\alpha)/\sqrt\alpha}{2}$, de donde $\sin\phi_m=\dfrac{1-\alpha}{1+\alpha}$.
> **Paso 4.** La magnitud en $\omega_m$: $|G_c(j\omega_m)|/(K_c\alpha)=\sqrt{\dfrac{1+\omega_m^2T^2}{1+\alpha^2\omega_m^2T^2}}=\sqrt{\dfrac{1+1/\alpha}{1+\alpha}}=\dfrac{1}{\sqrt\alpha}$.

> [!info] Adelanto alcanzable
> | $\alpha$ | $\phi_m$ |
> |---|---|
> | $0.5$ | $19.5^\circ$ |
> | $0.333$ | $30.0^\circ$ |
> | $0.2$ | $41.8^\circ$ |
> | $0.1$ | $54.9^\circ$ |
> | $0.05$ | $64.8^\circ$ |
>
> Un solo lead da hasta $\sim60^\circ$; para más, encadenar dos (la separación $p/z$ se vuelve impráctica y amplifica ruido).

---

## Algoritmo

> [!algoritmo] Diseño por margen de fase
> 1. Ajustar $K_c$ para el [[Coeficientes Kp Kv Ka | error estacionario]] ($K_v$) requerido.
> 2. Trazar el [[Bode/index | Bode]] de $L_0=K_cG$ y medir $\text{MF}_0$ y $\omega_c$.
> 3. Adelanto necesario: $\phi_m=\text{MF}_{obj}-\text{MF}_0+(5^\circ\text{–}12^\circ)$ (extra porque el cruce se desplaza).
> 4. $\alpha=\dfrac{1-\sin\phi_m}{1+\sin\phi_m}$.
> 5. Situar $\omega_m$ en el **nuevo cruce**: donde $|L_0|=-10\log(1/\alpha)$ dB; luego $T=\dfrac{1}{\omega_m\sqrt\alpha}$, $z=1/T$, $p=1/(\alpha T)$.
> 6. Verificar la MF resultante; iterar si hace falta.

> [!info] En MATLAB
> ```matlab
> G  = tf(20,[1 2 0]);
> phim = 30*pi/180;
> alpha = (1-sin(phim))/(1+sin(phim));         % 0.333
> % w_m donde |L0| = -10log10(1/alpha) dB:
> wm = 5.4;
> T  = 1/(wm*sqrt(alpha));
> Gc = (1/alpha)*tf([T 1],[alpha*T 1]);        % Kc*alpha = 1
> margin(Gc*G)                                 % verificar MF >= 50 deg
> ```

---

## Limitaciones

> [!warning]
> - **Amplifica ruido:** la magnitud sube $+20$ dB/dec entre esquinas → realza la alta frecuencia.
> - **Más de $\sim60^\circ$ es impráctico** con un solo lead: $\alpha$ se hace diminuto y $p/z$ enorme.
> - **No mejora el error estacionario** (lo fija $K_c$); si el error falla, usar lag → [[Lead Lag]].
> - El cruce se mueve: hay que **iterar** porque $\phi_m$ se evalúa en una $\omega$ que el propio lead desplaza.

---

## Efecto

> [!info] Trade-offs
> | Aspecto | Efecto |
> |---|---|
> | Margen de fase | **aumenta** ($+\phi_m$) |
> | Ancho de banda / $\omega_c$ | aumenta (respuesta más rápida) |
> | Sobrepico / transitorio | mejora |
> | Error estacionario | apenas (lo fija $K_c$) |
> | Ruido de alta frecuencia | **amplifica** ($+20$ dB/dec) |

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Forma | $K_c\alpha\dfrac{Ts+1}{\alpha Ts+1}$, $0<\alpha<1$ |
> | Pico de fase | $\sin\phi_m=\dfrac{1-\alpha}{1+\alpha}$ en $\omega_m=\dfrac{1}{T\sqrt\alpha}$ |
> | Magnitud en $\omega_m$ | $1/\sqrt\alpha$ ($+10\log\tfrac1\alpha$ dB) |
> | Diseño | $\phi_m$ del déficit → $\alpha$ → $\omega_m$ en nuevo cruce → $T$ |
> | Mejora | margen de fase, transitorio, velocidad |
> | Cuesta | amplifica ruido |

> [!corolario]
> Diseñar un lead por frecuencia es calcular el adelanto faltante $\phi_m$, traducirlo a $\alpha$ y deslizar la joroba de fase ($\omega_m$) hasta el nuevo cruce de ganancia, sin tocar $K_c$ (y con ello el error). Sube la MF y el ancho de banda a costa de realzar ruido. Para corregir error en vez de transitorio, el dual es el [[Respuesta Frecuencia/Lag | lag]]; ambos juntos forman el [[Lead Lag | lead-lag]].

> [!referencia]
> - Definición y diseño por plano-$s$: [[Lugar Raices/Lead]].
> - Equivalente PD: [[PD]].
> - Margen de fase y amortiguamiento: [[Margenes MF MG]] · [[Segundo Orden/index]].
> - Para el error estacionario: [[Respuesta Frecuencia/Lag]] · [[Lead Lag]].
