# ⚡ Trabajo, Energía y Momentos — Cuerpo Rígido en 2D (generalizado)

---

## 🧩 Energía cinética

| **Concepto** | **Fórmula** | **Tipo / Comentario** |
|---------------|-------------|------------------------|
| Energía cinética total (forma estándar) | $T=\tfrac{1}{2}m v_G^{2}+\tfrac{1}{2}I_G\omega^{2}$ | Siempre válida (referida al centro de masa $G$). |
| Energía cinética usando un punto $O$ (general) | $T=\tfrac{1}{2}m v_O^{2}+\tfrac{1}{2}I_O\omega^{2}+m v_O\!\cdot\!(\omega\times r_{G/O})$ | General. Incluye término cruz si $O$ se mueve o $G\neq O$. |
| Caso particular: $O$ fijo ($v_O=0$) | $T=\tfrac{1}{2}I_O\omega^{2}$ | Si $O$ es un pivote o punto fijo. |
| Caso particular: $O\equiv G$ | $T=\tfrac{1}{2}m v_G^{2}+\tfrac{1}{2}I_G\omega^{2}$ | Término cruz desaparece. |
| Relación entre inercia en $O$ y en $G$ | $I_O=I_G+m d^{2}$ | Teorema del eje paralelo, $d=|r_{G/O}|$. |

---

## ⚙️ Trabajo y Potencia

| **Concepto** | **Fórmula** | **Comentario** |
|---------------|-------------|----------------|
| Teorema trabajo–energía | $W_{\text{ext}}=\Delta T$ | Válido en cualquier referencia consistente. |
| Trabajo traslacional (referido a $G$) | $W_{\text{tras}}=\int\sum\vec{F}\cdot d\vec{r}_G$ | Trabajo de las fuerzas externas sobre el CG. |
| Trabajo rotacional (respecto a $G$) | $W_{\text{rot,G}}=\int\sum M_G\,d\theta$ | Momento medido respecto a $G$. |
| Trabajo rotacional (respecto a $O$) | $W_{\text{rot,O}}=\int\sum M_O\,d\theta$ | Momento medido respecto a $O$. |
| Trabajo total (en $G$) | $W_{\text{ext}}=\int(\sum\vec{F}\cdot d\vec{r}_G+\sum M_G\,d\theta)$ | Forma combinada. |
| Trabajo total (en $O$) | $W_{\text{ext}}=\int(\sum\vec{F}\cdot d\vec{r}_O+\sum M_O\,d\theta)$ | Forma equivalente, referida a $O$. |
| Potencia instantánea (en $G$) | $P=\sum\vec{F}\cdot\vec{v}_G+\sum M_G\omega$ | Tasa de variación de $T$ en $G$. |
| Potencia instantánea (en $O$) | $P=\sum\vec{F}\cdot\vec{v}_O+\sum M_O\omega$ | Misma potencia expresada desde otro punto. |

---

## 🌀 Momentos lineales y angulares

| **Magnitud** | **Fórmula (general)** | **Comentario / Particularidad** |
|---------------|------------------------|---------------------------------|
| Momento lineal total | $\vec{P}=m\vec{v}_G$ | Traslación del centro de masa. |
| Derivada del momento lineal | $\dfrac{d\vec{P}}{dt}=\sum\vec{F}$ | Segunda ley de Newton aplicada al CG. |
| Momento angular respecto a $O$ | $\vec{H}_O=\vec{H}_G+m(\vec{r}_G-\vec{r}_O)\times\vec{v}_G$ | Expresa $\vec{H}_O$ en función de $G$. |
| Derivada del momento angular (general) | $\dfrac{d\vec{H}_O}{dt}=\sum\vec{M}_O - m(\vec{v}_O\times\vec{v}_G)$ | **Forma generalizada válida para $O$ móvil.** |
| Caso particular: $O$ fijo ($\vec{v}_O=0$) | $\dfrac{d\vec{H}_O}{dt}=\sum\vec{M}_O$ | Forma usual simplificada. |
| Caso particular: $O\equiv G$ | $\dfrac{d\vec{H}_G}{dt}=\sum\vec{M}_G=I_G\vec{\alpha}$ | Ecuación rotacional directa en el CG. |
| Relación de momentos (traslado) | $\sum\vec{M}_O=\sum\vec{M}_G+(\vec{r}_G-\vec{r}_O)\times\sum\vec{F}$ | Útil para pasar de $G$ a $O$. |
| Relación escalar 2D (z) | $\dfrac{dH_{O,z}}{dt}=\sum M_{O,z}-m(v_{Ox}v_{Gy}-v_{Oy}v_{Gx})$ | Versión práctica para exámenes (2D). |

---

## 📘 Formas resumidas (para repaso rápido)

| Tipo | Fórmula | Observación |
|------|----------|-------------|
| Energía cinética (en $G$) | $T=\tfrac{1}{2}m v_G^{2}+\tfrac{1}{2}I_G\omega^{2}$ | General y más usada. |
| Energía cinética (en $O$) | $T=\tfrac{1}{2}m v_O^{2}+\tfrac{1}{2}I_O\omega^{2}+m v_O\cdot(\omega\times r_{G/O})$ | Incluir término cruz si $O$ se mueve. |
| Trabajo total (en $G$) | $W=\int(\sum\vec{F}\cdot d\vec{r}_G+\sum M_G\,d\theta)$ | Teorema trabajo–energía clásico. |
| Trabajo total (en $O$) | $W=\int(\sum\vec{F}\cdot d\vec{r}_O+\sum M_O\,d\theta)$ | Mismo resultado si coherente. |
| Potencia (en $G$) | $P=\sum\vec{F}\cdot\vec{v}_G+\sum M_G\omega$ | Derivada instantánea de $T$. |
| Potencia (en $O$) | $P=\sum\vec{F}\cdot\vec{v}_O+\sum M_O\omega$ | Alternativa equivalente. |
| Ecuación general de momentos | $\sum M_O=I_G\alpha+m(r_{G/O}\times a_G)$ | Siempre válida (2D o 3D). |
| Teorema del eje paralelo | $I_O=I_G+m d^{2}$ | $d$ es la distancia entre $O$ y $G$. |

---

## ✅ Notas finales de uso (para examen)

- El **teorema del trabajo y energía** siempre se cumple: $W_{\text{ext}}=\Delta T$.  
- Si el punto $O$ **no está fijo**, debes usar la forma **generalizada** con el término $-m(\vec{v}_O\times\vec{v}_G)$.  
- El uso del **centro de masa $G$** simplifica todas las ecuaciones (sin términos cruz).  
- El momento angular y la energía cinética pueden expresarse respecto a cualquier punto, pero deben ser **consistentes con los momentos y velocidades medidos en ese punto**.  
- Para problemas de examen en 2D, trabaja con las **componentes escalares** y considera el eje de rotación perpendicular al plano.

---
