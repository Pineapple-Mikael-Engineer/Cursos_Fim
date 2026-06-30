---
title: Diseño en Respuesta de Frecuencia
order: 2
tags:
  - control-clasico
  - diseno
  - respuesta-frecuencial
  - compensador
  - index
draft: false
aliases:
  - diseño frecuencial
  - compensación por Bode
  - diseño por frecuencia
---

# Diseño en Respuesta de Frecuencia

> [!definicion]
> Síntesis de compensadores $G_c(s)=K_c\dfrac{s+z}{s+p}$ sobre el [[Bode/index | diagrama de Bode]] de lazo abierto $L(j\omega)=G_c(j\omega)G(j\omega)$: en vez de ubicar polos, se moldean magnitud y fase para alcanzar un **margen de fase** MF objetivo y un ancho de banda dado. Como el Bode de una cascada **suma**, el efecto del compensador es $20\log|G_c|$ y $\angle G_c$ añadidos punto a punto a los de la planta.

> [!info]
> Es la rama frecuencial de la carpeta `4 Diseno/`, complementaria al [[Lugar Raices/index | diseño por lugar de raíces]]. Subnotas hermanas: [[Respuesta Frecuencia/Lead | Lead]] (adelanto de fase), [[Respuesta Frecuencia/Lag | Lag]] (atenuación / error) y [[Lead Lag | Lead-lag]] (ambos). Se apoya en [[Bode/index]] y [[Margenes MF MG]].

---

## Ejemplo

> [!ejemplo]
> **Elegir compensador y traducir specs a MF.** Planta $G(s)=\dfrac{K}{s(s+2)}$. Specs: error a rampa unitaria $e_{ss}\le 0.1$ y sobrepico $M_p\le 16\%$. Decidir qué compensar y con cuántos grados de adelanto.
>
> **Paso 1 — Ganancia por error estacionario.** Sistema [[Coeficientes Kp Kv Ka | tipo 1]], así que $K_v=\lim_{s\to0}sG(s)=K/2$. Para $e_{ss}=1/K_v\le0.1$ se necesita $K_v\ge10\Rightarrow K\ge20$. Fijamos $K=20$:
> $$L(s)=\frac{20}{s(s+2)}.$$
>
> **Paso 2 — Traducir $M_p$ a MF.** De [[Segundo Orden/index | segundo orden]], $M_p=16\%\Rightarrow\zeta\approx0.5$. La regla práctica $\text{MF}\approx100\,\zeta$ da $\text{MF}_{obj}\approx50^\circ$.
>
> **Paso 3 — Cruce y MF actual.** El cruce de ganancia cumple $|L(j\omega_c)|=1$:
> $$\frac{20}{\omega_c\sqrt{\omega_c^2+4}}=1\;\Rightarrow\;\omega_c\approx4.2\ \text{rad/s}.$$
> Fase allí: $\angle L=-90^\circ-\arctan(\omega_c/2)=-90^\circ-64.5^\circ=-154.5^\circ$, luego $\text{MF}_0=180^\circ-154.5^\circ\approx25.5^\circ$.
>
> **Paso 4 — Diagnóstico.** El error ya se cumple con $K$ (no hace falta lag). El déficit de margen es $\text{MF}_{obj}-\text{MF}_0\approx50^\circ-25.5^\circ=24.5^\circ$ → falta **adelanto de fase** → se elige un [[Respuesta Frecuencia/Lead | Lead]]. Añadiendo el margen de seguridad usual ($\sim5^\circ$) se necesita $\phi_m\approx30^\circ$ (el diseño completo del lead está en su nota).
>
> **Conclusión:** specs temporales → MF objetivo; error OK con ganancia → lead, no lag; ~$30^\circ$ de adelanto. Si además fallara el error, se añadiría un lag → [[Lead Lag | Lead-lag]].

---

## En qué consiste

> [!teoria]
> El diseño frecuencial explota tres hechos sobre $L(j\omega)$:
> - El **margen de fase** controla el [[Segundo Orden/index | amortiguamiento]]: $\zeta\approx\text{MF}/100$, y con él el sobrepico. Una MF de $45^\circ$–$60^\circ$ es el rango sano típico.
> - La cascada **suma** en Bode: $20\log|G_cG|=20\log|G_c|+20\log|G|$ y $\angle(G_cG)=\angle G_c+\angle G$. Diseñar es decidir cuánta magnitud/fase añadir y **dónde**.
> - El **cruce de ganancia** $\omega_c$ (donde $|L|=1$, 0 dB) es el punto crítico: la fase ahí fija la MF, y $\omega_c$ aproxima el ancho de banda (velocidad).

> [!info] Los tres compensadores
> | Compensador | Aporta | Mejora | Ubicación en el Bode |
> |---|---|---|---|
> | [[Respuesta Frecuencia/Lead \| Lead]] | adelanto $+\phi_m$ | MF, ancho de banda, transitorio | joroba de fase en el nuevo $\omega_c$ |
> | [[Respuesta Frecuencia/Lag \| Lag]] | atenuación $-20\log\beta$ | error estacionario ($K_v$) | esquina $\ll\omega_c$ |
> | [[Lead Lag \| Lead-lag]] | ambos | transitorio + error | dos bandas separadas |

> [!info] Relación con el lugar de raíces
> Son los **mismos** compensadores $G_c(s)=K_c\frac{s+z}{s+p}$ del [[Lugar Raices/Lead | diseño por lugar de raíces]]; cambia el **lenguaje**: aquí se ajustan magnitud y fase de $L(j\omega)$ para una MF objetivo, allá se ubican polos en el plano-$s$. Mismo resultado, distinta vista.

---

## Receta

> [!algoritmo]
> Pasos comunes a todo diseño por Bode:
> 1. **Specs → objetivos.** Traducir a MF objetivo (vía $\text{MF}\approx100\zeta$), ancho de banda y error estacionario ($K_v$, $K_p$, $K_a$).
> 2. **Ganancia.** Fijar $K_c$ para el error estacionario requerido.
> 3. **Diagnóstico.** Trazar el Bode de $L=K_cG$ y medir MF$_0$ y $\omega_c$ actuales; comparar con el objetivo.
> 4. **Elegir compensador.** Falta MF → lead; falta ganancia DC/error → lag; ambos → lead-lag.
> 5. **Diseñar** (ver la subnota correspondiente) y **verificar** en Bode/Nyquist; simular e iterar.

> [!info] En MATLAB
> ```matlab
> G = tf(20,[1 2 0]);        % planta tipo 1
> margin(G)                  % MF, MG, w_c actuales
> [Gm,Pm,Wcg,Wcp] = margin(G);
> Gc = tf([1 z],[1 p]);      % compensador a sintetizar
> margin(Gc*G)               % verificar MF objetivo
> ```

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Variable de diseño | Bode de $L(j\omega)=K_cG_c(j\omega)G(j\omega)$ |
> | Spec central | margen de fase MF ($\approx100\zeta$) |
> | Punto crítico | cruce de ganancia $\omega_c$ ($|L|=1$) |
> | Lead | sube MF y $\omega_c$ (transitorio) |
> | Lag | atenúa a alta f., sube ganancia DC (error) |
> | Lead-lag | ambos en bandas separadas |
> | Equivalente plano-$s$ | mismos $K_c\frac{s+z}{s+p}$ del lugar de raíces |

> [!corolario]
> Diseñar en frecuencia es moldear el Bode de lazo abierto hasta obtener la MF objetivo en el cruce de ganancia: la ganancia $K_c$ fija el error, el **lead** corrige el margen/transitorio y el **lag** corrige el error sin estropear el margen. Es el dual del [[Lugar Raices/index | lugar de raíces]] y el lenguaje natural cuando hay retardos o solo datos experimentales.

> [!referencia]
> - Compensadores: [[Respuesta Frecuencia/Lead]] · [[Respuesta Frecuencia/Lag]] · [[Lead Lag]].
> - Base de análisis: [[Bode/index]] · [[Margenes MF MG]].
> - Diseño equivalente por plano-$s$: [[Lugar Raices/index]].
> - Cuándo usar cada enfoque: [[Seleccion Metodo]].
