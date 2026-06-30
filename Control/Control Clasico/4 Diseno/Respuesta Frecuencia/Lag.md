---
title: Compensador Lag (por Frecuencia)
order: 2
tags:
  - control-clasico
  - diseno
  - respuesta-frecuencial
  - compensador
draft: false
aliases:
  - lag por Bode
  - retardo por frecuencia
  - diseño lag frecuencial
---

# Compensador Lag (por Frecuencia)

> [!definicion]
> Compensador de **atraso** que se diseña sobre el [[Bode/index | Bode]] para mejorar el error estacionario sin perder margen de fase:
> $$G_c(s) = K_c\,\beta\,\frac{Ts + 1}{\beta Ts + 1}, \qquad \beta > 1.$$
> Su mecanismo útil es la **atenuación** de $-20\log_{10}\beta$ dB a alta frecuencia: al bajar la magnitud, el [[Margenes MF MG | cruce de ganancia]] $\omega_c$ se desplaza a frecuencias menores, donde la planta tiene **más** fase (más MF). Equivale al [[Lugar Raices/Lag | lag]] $K_c\frac{s+z}{s+p}$ con $p=1/(\beta T)<z=1/T$.

> [!info]
> Vive en `4 Diseno/Respuesta Frecuencia/`. Es la versión frecuencial del lag; el diseño por plano-$s$ está en [[Lugar Raices/Lag]] y su análogo PID es el [[PI]]. Hermanas: [[Respuesta Frecuencia/Lead | Lead]] (margen/transitorio) y [[Lead Lag | Lead-lag]] (ambos). Marco general en [[Respuesta Frecuencia/index]].

---

## Ejemplo

> [!ejemplo]
> **Diseño de lag para subir $K_v$ sin perder MF, paso a paso.** Planta $G(s)=\dfrac{1}{s(s+1)(s+2)}$. Specs: $K_v\ge5$ (error a rampa $\le0.2$) y $\text{MF}\ge40^\circ$.
>
> **Paso 1 — Ganancia por error.** $K_v=\lim_{s\to0}sG_cG=\dfrac{K_c}{2}$. Para $K_v=5\Rightarrow K_c=10$. Pero con esa ganancia $L_0=\dfrac{10}{s(s+1)(s+2)}$ tendría el cruce muy alto y la MF sería **negativa** (inestable): hay que rebajar la magnitud a alta frecuencia → lag.
>
> **Paso 2 — Frecuencia que da el MF objetivo.** Se busca $\omega_c'$ donde la **fase** de la planta deje el margen deseado más un colchón ($40^\circ+6^\circ=46^\circ$), es decir $\angle L=-180^\circ+46^\circ=-134^\circ$:
> $$-90^\circ-\arctan\omega-\arctan(\omega/2)=-134^\circ.$$
> Resolviendo: $\arctan\omega+\arctan(\omega/2)=44^\circ$ → $\omega_c'\approx0.5\ \text{rad/s}$.
>
> **Paso 3 — Atenuación necesaria → $\beta$.** En $\omega_c'=0.5$ la magnitud de $L_0$ (con $K_c=10$) es
> $$|L_0(j0.5)|=\frac{10}{0.5\sqrt{0.25+1}\sqrt{0.25+4}}=\frac{10}{0.5\cdot1.118\cdot2.06}\approx8.68\ (\,+18.8\ \text{dB}\,).$$
> Para que $\omega_c'$ sea el **nuevo** cruce, el lag debe atenuar esos $+18.8$ dB:
> $$-20\log_{10}\beta=-18.8\ \text{dB}\;\Rightarrow\;\beta=10^{18.8/20}\approx8.7.$$
>
> **Paso 4 — Colocar la esquina lejos del cruce.** Para que el valle de fase del lag no reste margen en $\omega_c'$, su esquina superior $z=1/T$ se pone **una década por debajo**:
> $$\frac{1}{T}=\frac{\omega_c'}{10}=0.05\;\Rightarrow\;T=20\ \text{s},\qquad \frac{1}{\beta T}=\frac{0.05}{8.7}\approx0.0057.$$
> Allí el retardo de fase del lag en $\omega_c'$ es $\arctan(0.5/0.05)-\arctan(0.5/0.0057)\approx84.3^\circ-89.3^\circ=-5^\circ$ (despreciable, ya incluido en el colchón).
>
> **Paso 5 — Compensador y verificación.**
> $$G_c(s)=10\,\frac{20s+1}{174s+1}\quad\Longleftrightarrow\quad K_c\frac{s+0.05}{s+0.0057}.$$
> En $\omega_c'=0.5$: $|L_cL_0|\approx1$ (0 dB) y fase $\approx-180^\circ+40^\circ$ → $\text{MF}\approx40^\circ$ ✓, con $K_v=5$ ✓. El precio: el ancho de banda baja de $\sim1.3$ a $0.5$ rad/s (sistema más lento).

> [!ejemplo]
> **Bode del compensador lag.**
>
> ![[bode_lag_compensador.svg|550]]
>
> Magnitud: $0$ dB a baja frecuencia, cae $-20\log\beta$ por encima de la esquina superior. Fase: un valle negativo que se **sitúa lejos** (una década) del nuevo cruce para no restar margen. El lag se usa por la **atenuación**, no por su fase (que es indeseada).

---

## En qué consiste

> [!teorema] Atenuación de alta frecuencia
> El lag introduce una atenuación de
> $$-20\log_{10}\beta\ \text{dB}$$
> por encima de su esquina superior $z=1/T$. **No** se usa por su retardo de fase (indeseado), sino por esta atenuación: al bajar la curva de magnitud, el cruce de ganancia $\omega_c$ se mueve a frecuencias menores, donde la planta conserva **más** fase y por tanto más margen.

> [!demostracion]
> **Paso 1.** A baja frecuencia ($\omega\ll1/\beta T$): $|G_c|\to K_c\beta\cdot1=K_c\beta$ → ganancia DC alta (mejora $K_v$). **Paso 2.** A alta frecuencia ($\omega\gg1/T$): $|G_c|\to K_c\beta\cdot\dfrac{\omega T}{\beta\omega T}=K_c$ → la asíntota baja un factor $\beta$ respecto a la DC, es decir $-20\log\beta$ dB. **Paso 3.** Entre las esquinas $1/\beta T$ y $1/T$ la magnitud cae a $-20$ dB/dec; el cruce de ganancia del lazo, que estaba donde $|L_0|=1$, se recorre hacia $\omega$ menor porque ahora $|L|=|G_c||L_0|$ es menor. Allí $\angle L_0$ es menos negativa → mayor MF.

> [!info] Estrategia
> El lag mejora el margen de fase **indirectamente**: no añade fase, sino que reubica $\omega_c$ a una zona de mejor fase de la planta. A la vez, su ganancia DC ($\beta$) eleva el [[Coeficientes Kp Kv Ka | error estacionario]] sin tocar el transitorio.

---

## Algoritmo

> [!algoritmo] Diseño por margen de fase
> 1. Ajustar $K_c$ para el [[Coeficientes Kp Kv Ka | error estacionario]] ($K_v$) requerido.
> 2. Hallar $\omega_c'$ donde la **fase** de la planta da $\text{MF}_{obj}+(5^\circ\text{–}12^\circ)$.
> 3. La atenuación necesaria en $\omega_c'$ fija $\beta$: $-20\log\beta=-|L_0(j\omega_c')|_{\text{dB}}$.
> 4. Colocar la esquina superior $z=1/T$ **una década por debajo** de $\omega_c'$ (retardo de fase allí $<5^\circ$); luego $p=1/(\beta T)$.
> 5. Verificar y simular.

> [!info] En MATLAB
> ```matlab
> G  = tf(10,conv([1 0],conv([1 1],[1 2])));   % Kc ya incluido
> wcp = 0.5;                                    % w donde fase deja MF+colchon
> beta = 10^(18.8/20);                          % atenuacion necesaria
> T  = 10/wcp;                                  % esquina una decada abajo
> Gc = tf([T 1],[beta*T 1]);
> margin(Gc*G)                                  % verificar MF >= 40 deg
> ```

---

## Limitaciones

> [!warning]
> - **Ralentiza el sistema:** baja $\omega_c$ → menor ancho de banda → respuesta más lenta.
> - El **retardo de fase** del lag resta margen si su esquina queda cerca de $\omega_c'$: por eso se aleja una década (de ahí el colchón de $5^\circ$–$12^\circ$).
> - Polo y cero muy cerca del origen → **cola lenta** en la respuesta temporal (un transitorio adicional de baja amplitud y larga duración).
> - Si además se necesita rapidez/transitorio, combinar con lead → [[Lead Lag]].

---

## Efecto

> [!info] Trade-offs
> | Aspecto | Efecto |
> |---|---|
> | Error estacionario | **mejora** (factor $\beta$) |
> | Margen de fase | mejora (indirecto, baja $\omega_c$) |
> | Ancho de banda / velocidad | **se reduce** |
> | Ruido | atenúa (filtra alta frecuencia) |

> [!info] Lead vs Lag (frecuencia)
> | | [[Respuesta Frecuencia/Lead \| Lead]] | Lag |
> |---|---|---|
> | Mecanismo | añade fase $+\phi_m$ | añade atenuación, baja $\omega_c$ |
> | Ancho de banda | aumenta | reduce |
> | Mejora | transitorio | error estacionario |
> | Ruido | amplifica | atenúa |

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Forma | $K_c\beta\dfrac{Ts+1}{\beta Ts+1}$, $\beta>1$ |
> | Mecanismo | atenuación $-20\log\beta$ a alta f. |
> | Diseño | $\omega_c'$ por fase → $\beta$ por atenuación → esquina una década abajo |
> | Mejora | error estacionario ($K_v$) y MF indirecto |
> | Cuesta | ancho de banda / velocidad |
> | Esquina | $z=1/T=\omega_c'/10$, $p=1/(\beta T)$ |

> [!corolario]
> Diseñar un lag por frecuencia es elegir la frecuencia $\omega_c'$ donde la planta ya tiene la fase deseada, atenuar la magnitud allí (factor $\beta$) para hacerla el nuevo cruce, y esconder su esquina una década abajo para no perder fase. Mejora error y margen a costa de velocidad. Para corregir transitorio en vez de error, el dual es el [[Respuesta Frecuencia/Lead | lead]]; ambos juntos forman el [[Lead Lag | lead-lag]].

> [!referencia]
> - Definición y diseño por plano-$s$: [[Lugar Raices/Lag]].
> - Equivalente PI: [[PI]].
> - Compensador de adelanto: [[Respuesta Frecuencia/Lead]].
> - Combinación: [[Lead Lag]].
