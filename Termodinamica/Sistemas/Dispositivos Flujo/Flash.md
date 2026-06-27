---
title: Flash (Vaporización Instantánea)
order: 7
tags:
  - termodinamica
  - dispositivos-flujo
  - separacion
  - equilibrio-fases
  - flash-drum
draft: false
aliases:
  - flash drum
  - vaporizacion instantanea
  - tambor de flash
---

# Flash (Vaporización Instantánea)

> [!definicion]
> Un proceso de **flash** es una separación de una sola etapa en la que una corriente líquida a alta presión se expande bruscamente (mediante una [[Valvulas | válvula de estrangulamiento]]) a una cámara a menor presión. La caída de presión hace que una fracción del líquido se **vaporice instantáneamente**; las dos fases resultantes se separan por gravedad en el **tambor de flash**.
>
> *¿Por qué se vaporiza?* La expansión isoentálpica reduce $P$ por debajo de la presión de burbuja del líquido. Para alcanzar el nuevo equilibrio a $P_{\rm tambor}$, parte del líquido debe evaporarse — la energía para el cambio de fase sale del propio líquido, que se enfría. El resultado es una mezcla bifásica en equilibrio a $T_{\rm tambor}$, $P_{\rm tambor}$.
>
> *Ventaja:* es el separador más sencillo y barato posible. No requiere calefacción externa ni trabajo de eje. Su limitación es que la separación es solo parcial (una sola etapa equilibrada); para separaciones más completas se usan columnas de destilación (muchas etapas en serie).
>
> *Aplicaciones:* destilación de crudo (la columna atmosférica es un flash multicomponente de muchas etapas), desalinización MSF, separadores de gas-líquido en campos petroleros, ciclos de refrigeración de dos etapas (flash economizer).

![[flash_drum_esquema.svg|440]]
*Tambor de flash. La alimentación $F$ entra a través de una válvula de expansión. En el tambor las fases se separan: vapor $V$ sale por arriba, líquido $L$ por abajo. Un eliminador de niebla retiene las gotas arrastradas por el vapor.*

---

## Modelo termodinámico del flash

> [!teorema]
> Para un tambor de flash estacionario, adiabático, sin trabajo de eje:
>
> **Balance de masa global:**
> $$F = V + L.$$
>
> **Balance de masa por componente** (fracción molar $z_i$ en alimentación, $y_i$ en vapor, $x_i$ en líquido):
> $$F z_i = V y_i + L x_i \quad \forall\,i.$$
>
> **Balance de energía** (proceso total: válvula + tambor):
> $$\boxed{F h_F = V H_V + L h_L,}$$
> donde $h_F = h_F(T_F, P_F)$ antes de la válvula; $H_V$ y $h_L$ en equilibrio a $(T_{\rm tambor}, P_{\rm tambor})$.
>
> **Equilibrio de fases:** a cada componente $i$, en la fase vapor y líquida se cumple la igualdad de fugacidades; en la aproximación de ley de Raoult modificada:
> $$y_i = K_i(T_{\rm tambor}, P_{\rm tambor})\,x_i, \qquad K_i \approx \frac{P_i^{\rm sat}(T_{\rm tambor})}{P_{\rm tambor}}.$$

> [!demostracion]
> **Hipótesis:** VC estacionario (válvula + tambor como un VC único), $\dot{Q}=0$, $\dot{W}=0$, $\Delta EC=\Delta EP=0$, equilibrio entre fases en el tambor.
>
> **Paso 1 — Vc válvula.** La válvula es isoentálpica: $h_F(P_F, T_F) = h_{F'}(P_{\rm tambor}, T_{\rm tambor,\ entrada})$. El estado $F'$ es la mezcla bifásica justo al entrar al tambor.
>
> **Paso 2 — VC tambor.** En el tambor (sin Q, sin W, estado estacionario), primera ley:
> $$F h_{F'} = V H_V + L h_L.$$
> Como $h_{F'} = h_F$ (por el paso 1), se puede combinar: $F h_F = V H_V + L h_L$.
>
> **Paso 3 — Balance de masa por componente.** Para cada especie $i$:
> $$F z_i = V y_i + L x_i.$$
> Sustituyendo $L=F-V$ y usando $y_i = K_i x_i$:
> $$F z_i = V K_i x_i + (F-V) x_i = x_i[F + V(K_i-1)].$$
> $$x_i = \frac{z_i}{1 + (V/F)(K_i-1)}, \qquad y_i = \frac{K_i z_i}{1 + (V/F)(K_i-1)}.$$
>
> **Paso 4 — Ecuación de Rachford-Rice.** La normalización $\sum_i y_i = \sum_i x_i$ conduce a la ecuación implícita en $\Psi = V/F$:
> $$\sum_i \frac{z_i(K_i-1)}{1+\Psi(K_i-1)} = 0.$$
> Esta ecuación se resuelve iterativamente para obtener $\Psi$ dado $\{z_i, K_i\}$.
>
> **Paso 5 — Consistencia termodinámica.** La segunda ley exige $\dot{S}_{\rm gen} = V s_V + L s_L - F s_F \geq 0$. Como la válvula es irreversible y la separación en el tambor es aproximadamente reversible (equilibrio), $\dot{S}_{\rm gen}$ es dominado por la válvula. $\blacksquare$

---

## Ejemplo: flash de mezcla propano-butano

> [!ejemplo]
> Una alimentación equimolar de propano (C₃H₈, $P_1^{\rm sat}(60\,°\mathrm{C})=10.0\,\mathrm{bar}$) y n-butano (C₄H₁₀, $P_2^{\rm sat}(60\,°\mathrm{C})=2.6\,\mathrm{bar}$) con caudal total $F=100\,\mathrm{kmol/h}$ se flashea a $P_{\rm tambor}=5.0\,\mathrm{bar}$, $T_{\rm tambor}=60\,°\mathrm{C}$. Calcular las corrientes de vapor $V$ y líquido $L$, y sus composiciones. Usar ley de Raoult: $K_i = P_i^{\rm sat}/P$.

> [!solucion]
> **Paso 1 — Calcular $K_i$ a $(60\,°\mathrm{C},\,5\,\mathrm{bar})$.**
> $$K_{\rm C_3} = 10.0/5.0 = 2.00, \qquad K_{\rm C_4} = 2.6/5.0 = 0.52.$$
> Verificación: $K_1>1$ (propano más volátil que la mezcla), $K_2<1$ (butano menos volátil) ✓.
>
> **Paso 2 — Ecuación de Rachford-Rice.** Con $z_1=z_2=0.50$:
> $$f(\Psi) = \frac{0.50\times(2.00-1)}{1+\Psi\times1.00} + \frac{0.50\times(0.52-1)}{1+\Psi\times(-0.48)} = \frac{0.50}{1+\Psi} - \frac{0.24}{1-0.48\Psi} = 0.$$
>
> **Paso 3 — Resolver para $\Psi$.** Igualando numeradores tras llevar a denominador común:
> $$0.50(1-0.48\Psi) - 0.24(1+\Psi) = 0 \implies 0.50 - 0.24\Psi - 0.24 - 0.24\Psi = 0.$$
> $$0.26 = 0.48\Psi \implies \Psi = V/F = 0.541.$$
> $$V = 54.1\,\mathrm{kmol/h}, \quad L = 45.9\,\mathrm{kmol/h}.$$
>
> **Paso 4 — Composiciones.**
> $$x_1 = \frac{z_1}{1+\Psi(K_1-1)} = \frac{0.50}{1+0.541\times1.00} = \frac{0.50}{1.541} = 0.325.$$
> $$x_2 = 1-x_1 = 0.675. \qquad y_1 = K_1 x_1 = 2.00\times0.325 = 0.650. \qquad y_2 = 0.350.$$
>
> **Paso 5 — Verificación de balances.** $V y_1+L x_1 = 54.1\times0.650+45.9\times0.325=35.2+14.9=50.1\approx50$ ✓. $V y_2+L x_2=54.1\times0.350+45.9\times0.675=18.9+31.0=49.9\approx50$ ✓.
>
> $\boxed{V=54.1\,\mathrm{kmol/h}\;(y_{\rm C_3}=0.650),\quad L=45.9\,\mathrm{kmol/h}\;(x_{\rm C_3}=0.325).}$ $\blacksquare$

> [!teoria]
> El flash adiabático que incluye el balance de energía simultáneamente (para determinar $T_{\rm tambor}$, no solo la composición) se llama **flash adiabático completo**. Requiere resolver el sistema $\{f(\Psi,T)=0, \, \text{balance de} \, h\}$ de forma acoplada e iterativa: se propone $T$, se calculan $K_i(T)$, se resuelve Rachford-Rice, se verifican las entalpías, y se ajusta $T$ hasta que el balance de energía converge.

> [!warning]
> El flash tiene sentido solo si $\sum_i z_i/K_i < 1 < \sum_i z_i K_i$ (condición de punto de burbuja / punto de rocío encuadrando la $P$ del tambor). Si $\sum_i K_i z_i < 1$ toda la alimentación es líquida (no hay flash); si $\sum_i z_i/K_i < 1$ y se cumple la condición inversa, todo es vapor.

> [!referencia]
> Borgnakke & Sonntag, §12.4; Çengel & Boles, §Apéndice Mezclas; Moran & Shapiro, §12.3. Para la ecuación de Rachford-Rice: Smith, Van Ness & Abbott, *Introduction to Chemical Engineering Thermodynamics*, §13.
