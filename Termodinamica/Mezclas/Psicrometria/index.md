---
title: Psicrometría
tags:
  - termodinamica
  - teoria
  - mezclas
  - psicrometria
  - aire-humedo
draft: false
aliases:
  - Psicrometría
  - Aire Húmedo
  - Psychrometrics
---

# Psicrometría $\omega=0.622\dfrac{P_v}{P-P_v},\quad \phi=\dfrac{P_v}{P_{\rm sat}(T)}$

> [!definicion]
> La **psicrometría** es el estudio termodinámico del **aire húmedo**: mezcla binaria de aire seco (componente no condensable, tratado como gas ideal con $M_a=28.97\,\mathrm{kg/kmol}$) y vapor de agua (componente condensable). El estado del aire húmedo queda fijado por tres variables: presión total $P$, temperatura $T$ y composición (expresada como $\omega$, $\phi$ o $T_d$). La psicrometría es el fundamento del diseño de sistemas de climatización (HVAC).

---

## Variables de estado del aire húmedo

Sean $m_a$ la masa de aire seco y $m_v$ la masa de vapor de agua en la mezcla.

**Razón de humedad** (humidity ratio, razón de mezcla):
$$\omega \equiv \frac{m_v}{m_a}\quad [\mathrm{kg\,vapor/kg\,aire\,seco}].$$

**Relación con presiones parciales.** Aplicando el modelo de Dalton con gas ideal a cada componente ($P_v = P_v$, $P_a = P - P_v$):
$$\frac{m_v}{m_a} = \frac{n_v M_v}{n_a M_a} = \frac{P_v/P_a \cdot M_v}{M_a} = \frac{P_v}{P-P_v}\cdot\frac{18.015}{28.97}$$

> [!demostracion]
> **Paso 1.** Número de moles: $n_v = m_v/M_v = m_v/18.015$, $n_a = m_a/M_a = m_a/28.97$.
>
> **Paso 2.** Por Dalton (gas ideal): $P_v = (n_v/n)P$ y $P_a = (n_a/n)P$, luego $P_v/P_a = n_v/n_a$.
>
> **Paso 3.** Sustituyendo:
> $$\omega = \frac{m_v}{m_a} = \frac{n_v M_v}{n_a M_a} = \frac{P_v}{P_a}\cdot\frac{M_v}{M_a} = \frac{P_v}{P-P_v}\cdot\frac{18.015}{28.97}.$$
>
> **Paso 4.** El cociente $18.015/28.97 = 0.6219\approx0.622$:
> $$\boxed{\omega = 0.622\,\frac{P_v}{P-P_v}.} \qquad \blacksquare$$

**Humedad relativa:**
$$\phi \equiv \frac{P_v}{P_{\rm sat}(T)} \in [0,1].$$
$\phi=0$: aire seco. $\phi=1$: aire saturado (máxima humedad sin condensación). Si se añade vapor con $\phi=1$, el exceso condensa.

**Temperatura de rocío $T_d$:** temperatura a la que el aire húmedo, enfriado a $P$ y $\omega$ constantes, alcanza la saturación:
$$P_v = P_{\rm sat}(T_d) \implies T_d = T_{\rm sat}^{-1}(P_v).$$
Relación con $\omega$ y $\phi$:
$$P_v = \frac{\omega\,P}{0.622+\omega} = \phi\,P_{\rm sat}(T).$$

**Temperatura de bulbo húmedo $T_{bh}$:** temperatura alcanzada por el aire que se satura adiabáticamente. Para el **saturador adiabático ideal** (proceso de referencia termodinámico):

> [!proposicion] Balance del saturador adiabático
> El aire húmedo entra con $(T,\omega)$, sale saturado a $(T_{bh},\omega_{bh})$, y el agua de maquillaje entra como líquido a $T_{bh}$. Balance de masa de agua y balance de energía (por kg de aire seco):
> $$\omega_{bh}-\omega = \frac{(\omega_{bh}-\omega)\,h_{f}(T_{bh}) + (h_{a,bh}-h_a) + \omega_{bh}\,h_{v,bh} - \omega\,h_v}{0}$$
>
> Resulta la ecuación del saturador:
> $$\omega = \frac{c_{pa}(T_{bh}-T) + \omega_{bh}\,h_{fg}(T_{bh})}{h_v(T) - h_f(T_{bh})}$$
> o equivalentemente:
> $$\omega \approx \omega_{bh} - \frac{c_{pa}(T-T_{bh})}{h_{fg}(T_{bh})}.$$

> [!demostracion]
> **Sistema:** saturador adiabático en régimen estacionario. Por kg de aire seco.
>
> **Balance de masa (vapor):**
> $$\dot{m}_{\rm maq} = \dot{m}_a(\omega_{bh}-\omega).$$
> El agua de maquillaje entra como líquido saturado a $T_{bh}$: $h_{\rm maq}=h_f(T_{bh})$.
>
> **Balance de energía** (adiabático, sin trabajo de eje, $\Delta\mathrm{Ec}=0$):
> $$h_{\rm entrada} + (\omega_{bh}-\omega)h_f(T_{bh}) = h_{\rm salida}$$
> $$[h_a(T)+\omega h_v(T)] + (\omega_{bh}-\omega)h_f(T_{bh}) = h_a(T_{bh})+\omega_{bh}h_v(T_{bh}).$$
>
> Usando $h_a(T)=c_{pa}T$, $h_v(T)\approx h_{fg,0}+c_{pv}T$ (con $h_{fg,0}=2501\,\mathrm{kJ/kg}$), y $h_v(T_{bh})-h_f(T_{bh})=h_{fg}(T_{bh})$:
> $$c_{pa}(T-T_{bh}) = \omega_{bh}\,h_{fg}(T_{bh}) - \omega[h_v(T)-h_f(T_{bh})].$$
>
> Como $h_v(T)-h_f(T_{bh})\approx h_{fg}(T_{bh}) + c_{pv}(T-T_{bh})\approx h_{fg}(T_{bh})$ (corrección $c_{pv}\Delta T$ pequeña):
> $$\omega \approx \omega_{bh} - \frac{c_{pa}(T-T_{bh})}{h_{fg}(T_{bh})}. \qquad \blacksquare$$

---

## Entalpía del aire húmedo

Por kg de **aire seco** (base estándar en psicrometría):
$$h = h_a + \omega\,h_v \approx c_{pa}\,T + \omega\,(h_{fg,0}+c_{pv}\,T)$$

donde $c_{pa}=1.005\,\mathrm{kJ/(kg\cdot K)}$, $c_{pv}=1.86\,\mathrm{kJ/(kg\cdot K)}$, $h_{fg,0}=2501\,\mathrm{kJ/kg}$ (entalpía de vaporización a $0\,°\mathrm{C}$).

En forma compacta:
$$h = (1.005 + 1.86\,\omega)\,T + 2501\,\omega \qquad [\mathrm{kJ/kg\,a.s.}]$$
con $T$ en $°\mathrm{C}$ y $\omega$ en kg/kg.

---

## Volumen específico y densidad

Por kg de aire seco:
$$v = \frac{R_a T}{P_a} = \frac{R_a T}{P - P_v} = \frac{(R_u/M_a)T}{P(1-P_v/P)}\qquad [\mathrm{m^3/kg\,a.s.}]$$

donde $R_a = R_u/M_a = 8.314/28.97 = 0.2870\,\mathrm{kJ/(kg\cdot K)}$.

---

## Diagrama psicrométrico (carta de Mollier para aire húmedo)

El diagrama psicrométrico traza $\omega$ (eje $y$) vs. $T$ de bulbo seco (eje $x$) a presión fija ($P=101.325\,\mathrm{kPa}$). Las curvas principales son:

| Curva | Condición |
|:---|:---|
| Humedad relativa $\phi=\text{cte}$ | $P_v/P_{\rm sat}(T)=\phi$ |
| Temperatura de bulbo húmedo $T_{bh}=\text{cte}$ | Líneas diagonales (casi rectas) |
| Entalpía $h=\text{cte}$ | Casi paralelas a $T_{bh}=\text{cte}$ |
| Temperatura de rocío $T_d=\text{cte}$ | Horizontales ($\omega=\text{cte}$) |
| Volumen específico $v=\text{cte}$ | Líneas con pendiente negativa |

![[diagrama_psicrometrico.svg|500]]
*Carta psicrométrica a $P=101.325\,\mathrm{kPa}$. La curva de saturación ($\phi=1$) es el límite superior; los estados sobre ella corresponden a niebla o lluvia. Las líneas de $T_{bh}=\text{cte}$ y $h=\text{cte}$ son casi paralelas, lo que permite leer la entalpía en la escala de $T_{bh}$.*

---

## Ejemplo: condiciones de un cuarto climatizado

> [!ejemplo]
> Aire entra a un salón a $T=28\,°\mathrm{C}$, $\phi=70\%$ y $P=101.325\,\mathrm{kPa}$. Determinar:
> (a) Presión parcial del vapor $P_v$.
> (b) Razón de humedad $\omega$.
> (c) Temperatura de rocío $T_d$.
> (d) Entalpía específica $h$ por kg de aire seco.
> (e) Si la temperatura baja a $15\,°\mathrm{C}$ sin cambio de composición, ¿condensa agua?

> [!solucion]
> **Datos.** De tablas (CATT3 o A-4): $P_{\rm sat}(28\,°\mathrm{C})=3.779\,\mathrm{kPa}$.
>
> **(a)** $P_v = \phi\cdot P_{\rm sat}(T) = 0.70\times3.779 = 2.645\,\mathrm{kPa}$.
>
> **(b)** $\omega = 0.622\times P_v/(P-P_v) = 0.622\times2.645/(101.325-2.645) = 0.622\times2.645/98.68 = 0.01668\,\mathrm{kg/kg\,a.s.}$
>
> **(c)** $T_d$: la temperatura a la que $P_{\rm sat}(T_d)=P_v=2.645\,\mathrm{kPa}$. De tablas: $P_{\rm sat}(22\,°\mathrm{C})=2.645\,\mathrm{kPa}$ (interpolando: exactamente $22.0\,°\mathrm{C}$). Luego $T_d\approx22.0\,°\mathrm{C}$.
>
> **(d)** $h = (1.005+1.86\times0.01668)\times28 + 2501\times0.01668$.
> $= (1.005+0.03102)\times28 + 41.71 = 1.0360\times28 + 41.71 = 29.01 + 41.71 = 70.72\,\mathrm{kJ/kg\,a.s.}$
>
> **(e)** A $T=15\,°\mathrm{C}$: $P_{\rm sat}(15\,°\mathrm{C})=1.706\,\mathrm{kPa}$. Como $P_v=2.645\,\mathrm{kPa}>P_{\rm sat}(15\,°\mathrm{C})=1.706\,\mathrm{kPa}$, el aire estaría supersaturado: **sí condensa**. La cantidad de condensado por kg de aire seco es:
> $$\Delta m_{\rm cond} = \omega - \omega'\quad\text{con}\quad\omega' = 0.622\times\frac{P_{\rm sat}(15)}{P-P_{\rm sat}(15)}=0.622\times\frac{1.706}{101.325-1.706}=0.622\times0.01712=0.01065\,\mathrm{kg/kg}.$$
> $$\Delta m_{\rm cond}=0.01668-0.01065=0.00603\,\mathrm{kg\,agua/kg\,a.s.}\quad(6.03\,\mathrm{g/kg}). \qquad \blacksquare$$

> [!referencia]
> Çengel & Boles, *Termodinámica*, cap. 14; Moran & Shapiro §12.5; ASHRAE Fundamentals Handbook, cap. 1 (Psychrometrics).
