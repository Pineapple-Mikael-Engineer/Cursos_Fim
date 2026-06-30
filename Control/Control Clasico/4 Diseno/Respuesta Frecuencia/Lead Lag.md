---
title: Compensador Lead-Lag
order: 3
tags:
  - control-clasico
  - diseno
  - respuesta-frecuencial
  - compensador
draft: false
aliases:
  - lead-lag
  - adelanto-retardo
  - compensador lead-lag
---

# Compensador Lead-Lag

> [!definicion]
> Cascada de un [[Respuesta Frecuencia/Lead | lead]] (corrige transitorio/MF a frecuencia media) y un [[Respuesta Frecuencia/Lag | lag]] (corrige error a baja frecuencia):
> $$G_c(s) = K_c\,\underbrace{\frac{T_1 s + 1}{\alpha T_1 s + 1}}_{\text{lead},\ \alpha<1}\,\underbrace{\frac{T_2 s + 1}{\beta T_2 s + 1}}_{\text{lag},\ \beta>1}.$$
> Cada parte actúa en su **banda**: el lag sube la ganancia DC sin tocar el cruce; el lead añade $+\phi_m$ en el cruce. Es la versión frecuencial del [[PID | PID]].

> [!info]
> Vive en `4 Diseno/Respuesta Frecuencia/`. Combina sus dos hermanas [[Respuesta Frecuencia/Lead | Lead]] y [[Respuesta Frecuencia/Lag | Lag]]; el diseño por plano-$s$ usa [[Lugar Raices/Lead]] + [[Lugar Raices/Lag]] y el análogo es el [[PID]]. Marco general en [[Respuesta Frecuencia/index]]; cuándo usarlo en [[Seleccion Metodo]].

---

## Ejemplo

> [!ejemplo]
> **Diseño lead-lag, paso a paso.** Planta $G(s)=\dfrac{K}{s(s+1)(s+2)}$. Specs **simultáneas**: $K_v\ge10$ (error a rampa $\le0.1$) y $\text{MF}\ge45^\circ$. Ni lead ni lag solos bastan.
>
> **Paso 1 — Ganancia por error.** $K_v=\dfrac{K}{2}\ge10\Rightarrow K=20$. Con $L_0=\dfrac{20}{s(s+1)(s+2)}$ el cruce queda en $\omega_c\approx2.5$ rad/s con fase $-90^\circ-68^\circ-51^\circ=-209^\circ$ → $\text{MF}_0\approx-29^\circ$ (**inestable**). Hay que recuperar margen sin perder $K_v$ → lead-lag.
>
> **Paso 2 — Lag primero (recolocar el cruce).** Bajar el cruce a una zona de mejor fase. Buscamos $\omega_c'$ con fase $-180^\circ+(45^\circ+10^\circ)=-125^\circ$:
> $$-90^\circ-\arctan\omega-\arctan(\omega/2)=-125^\circ\;\Rightarrow\;\omega_c'\approx0.45\ \text{rad/s}.$$
> Magnitud de $L_0$ allí: $|L_0(j0.45)|\approx\dfrac{20}{0.45\cdot1.097\cdot2.05}\approx19.7$ ($+25.9$ dB). El lag debe atenuar la mitad de ese exceso y dejar el resto al lead; usamos $\beta=10$ → atenúa $-20$ dB, esquina superior $\dfrac1{T_2}=\dfrac{\omega_c'}{10}=0.045$ → $T_2=22$ s.
>
> **Paso 3 — Re-evaluar el cruce tras el lag.** Con la atenuación de $-20$ dB, el nuevo cruce $\omega_c''$ baja a $\approx0.5$ rad/s. Fase de la planta más lag allí $\approx-90^\circ-26.6^\circ-14^\circ-3^\circ_{\text{lag}}\approx-133.6^\circ$ → $\text{MF}\approx46^\circ$... pero el residuo de magnitud pide un pequeño empuje y colchón → diseñamos el lead para garantizar el margen.
>
> **Paso 4 — Lead después (margen en el nuevo cruce).** Déficit de fase a cubrir con colchón: $\phi_m\approx20^\circ$. Entonces
> $$\alpha=\frac{1-\sin20^\circ}{1+\sin20^\circ}=\frac{1-0.342}{1+0.342}=\frac{0.658}{1.342}\approx0.49,$$
> con $\omega_m\approx\omega_c''\approx0.5$ rad/s → $T_1=\dfrac{1}{\omega_m\sqrt\alpha}=\dfrac{1}{0.5\cdot0.7}\approx2.86$ s.
>
> **Paso 5 — Compensador final.**
> $$G_c(s)=20\cdot\underbrace{\frac{2.86s+1}{1.40s+1}}_{\text{lead}}\cdot\underbrace{\frac{22s+1}{220s+1}}_{\text{lag}}.$$
> **Verificación:** en $\omega_c''\approx0.5$ la fase total $\approx-180^\circ+47^\circ$ → $\text{MF}\approx47^\circ\ge45^\circ$ ✓, y $K_v=10$ ✓ (los factores DC del lead y lag se cancelan en el límite, $K_c\alpha\beta\cdot\tfrac1\alpha\tfrac1\beta=K_c$). Las bandas no se solapan: lag en $\sim0.045$, lead en $\sim0.5$ rad/s.

> [!ejemplo]
> **Bode del lead-lag.**
>
> ![[bode_lead_lag.svg|600]]
>
> A baja frecuencia domina el **lag** (ganancia DC, mejora $K_v$); en la banda media aparece la **joroba de fase del lead** (sube la MF en el cruce); a alta frecuencia, atenuación. Las dos bandas están separadas para que cada compensador no interfiera con el otro.

---

## En qué consiste

> [!teoria] Cada parte en su banda
> - El **lag** actúa a **baja frecuencia**: aporta ganancia DC (mejora $K_v$, error estacionario) con su esquina muy por debajo del cruce, para no añadir retardo donde importa.
> - El **lead** actúa a **frecuencia media**: aporta adelanto de fase $+\phi_m$ centrado en el cruce de ganancia (mejora MF y transitorio).
> - Las bandas se **separan** (al menos una década) para que el retardo del lag no coma el adelanto del lead ni viceversa.

> [!info] Equivalencia con PID
> | Lead-lag | PID |
> |---|---|
> | parte lag (polo cerca del origen) | acción [[Integral I \| integral]] ([[PI]]) |
> | parte lead (cero a media frecuencia) | acción [[Derivativo D \| derivativa]] ([[PD]]) |
> | conjunto | [[PID \| PID completo]] |
>
> El lead-lag usa polos finitos (realizable, filtra ruido); el PID ideal usa el origen e infinito.

---

## Algoritmo

> [!algoritmo] Diseño combinado
> 1. Ajustar $K_c$ para el error estacionario ($K_v$).
> 2. **Lag primero:** elegir $\beta$ para la ganancia DC / recolocación del cruce; esquina muy por debajo del cruce deseado.
> 3. **Lead después:** sobre el Bode ya modificado por el lag, diseñar el lead ($\alpha$, $\omega_m$) para el [[Margenes MF MG | margen de fase]] objetivo en el nuevo cruce.
> 4. Verificar que las bandas no se solapen; comprobar MF y $K_v$, y simular.

> [!info] En MATLAB
> ```matlab
> G    = tf(20,conv([1 0],conv([1 1],[1 2])));   % Kc=20 incluido
> lag  = tf([22 1],[220 1]);                      % beta=10, esquina baja
> alpha = 0.49; wm = 0.5; T1 = 1/(wm*sqrt(alpha));
> lead = tf([T1 1],[alpha*T1 1]);
> Gc   = lead*lag;
> margin(Gc*G)                                    % MF>=45, Kv=10
> ```

---

## Cuándo usarlo

> [!info] Uso
> Cuando se requieren **simultáneamente**:
> - error estacionario pequeño (necesita lag / ganancia DC), y
> - buen transitorio y margen de fase (necesita lead / adelanto),
>
> y ni el lead ni el lag por separado bastan. Es el caso más general de la compensación clásica.

## Limitaciones

> [!warning]
> - Si las **bandas se solapan**, el lag resta fase donde el lead la añade: el diseño se degrada → separar al menos una década.
> - Más complejo de sintonizar (cuatro parámetros $T_1,\alpha,T_2,\beta$ más $K_c$); conviene **iterar** verificando en Bode.
> - Hereda los costes de cada parte: el lag deja una cola lenta, el lead realza algo de ruido (menos que un lead solo, pues el lag filtra alta f.).

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Forma | $K_c\dfrac{T_1s+1}{\alpha T_1s+1}\dfrac{T_2s+1}{\beta T_2s+1}$ |
> | Lag (baja f.) | ganancia DC → error estacionario |
> | Lead (media f.) | adelanto $+\phi_m$ → MF, transitorio |
> | Orden de diseño | lag primero, lead después |
> | Clave | separar bandas $\ge$ una década |
> | Equivalente | [[PID]] |

> [!corolario]
> El lead-lag resuelve el caso general donde fallan a la vez error y transitorio: el lag recoloca el cruce y sube la ganancia DC, el lead repone el margen de fase en ese nuevo cruce, y separar sus bandas evita que se estorben. Es el [[PID]] de la compensación clásica, realizable con polos finitos. Si solo falla uno de los dos, basta el [[Respuesta Frecuencia/Lead | lead]] o el [[Respuesta Frecuencia/Lag | lag]] por separado.

> [!referencia]
> - Componentes: [[Respuesta Frecuencia/Lead]] · [[Respuesta Frecuencia/Lag]].
> - Equivalente PID: [[PID]] · [[Configuraciones/index]].
> - Diseño por plano-$s$: [[Lugar Raices/Lead]] · [[Lugar Raices/Lag]].
> - Elección de método: [[Seleccion Metodo]].
