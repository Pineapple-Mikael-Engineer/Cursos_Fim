# 📘 Formulario General — Dinámica 3D del Cuerpo Rígido  
*(Relaciones fundamentales que siempre se cumplen — sin casos especiales)*

---

## 🔷 1. Energía cinética total (respecto a un punto arbitrario O)

| Relación | Ecuación general | Notas |
|---------|------------------|-------|
| Energía total | $$T=\tfrac{1}{2}m v_O^{2}+\tfrac{1}{2}\,\boldsymbol{\omega}^{T}\mathbf{I}_O\boldsymbol{\omega}+m\,\vec{v}_O\cdot(\boldsymbol{\omega}\times\vec{r}_{G/O})$$ | O puede estar acelerando o moviéndose libremente. |
| Tensor trasladado | $$\mathbf{I}_O=\mathbf{I}_G+m\left[(r^2)\mathbf{1}-\vec{r}\vec{r}^T\right]$$ | Teorema del eje paralelo en forma tensorial. |

---

## 🔷 2. Momento angular (respecto a O y respecto a G)

| Relación | Ecuación | Notas |
|----------|----------|--------|
| Momento angular en G | $$\vec{H}_G=\mathbf{I}_G\boldsymbol{\omega}$$ | Forma más compacta. |
| Momento angular en O (general) | $$\vec{H}_O=\vec{H}_G+m\,\vec{r}_{G/O}\times\vec{v}_G$$ | Válido para cualquier punto O. |
| Relación útil | $$\vec{H}_O=\mathbf{I}_G\boldsymbol{\omega}+m(\vec{r}_{G/O}\times\vec{v}_G)$$ | Combinación directa. |

---

## 🔷 3. Ecuaciones de evolución del momento angular

| Relación | Ecuación | Notas |
|----------|----------|--------|
| Ecuación de Euler (en G) | $$\frac{d\vec{H}_G}{dt}=\sum\vec{M}_G=\mathbf{I}_G\boldsymbol{\alpha}+\boldsymbol{\omega}\times(\mathbf{I}_G\boldsymbol{\omega})$$ | Forma general completa. |
| Derivada en un punto arbitrario O | $$\frac{d\vec{H}_O}{dt}=\sum\vec{M}_O - m(\vec{v}_O\times\vec{v}_G)$$ | Válida incluso si O se mueve. |
| Ecuación de momentos respecto a O | $$\sum\vec{M}_O=\mathbf{I}_G\vec{\alpha}+m(\vec{r}_{G/O}\times\vec{a}_G)+\vec{\omega}\times(\mathbf{I}_G\vec{\omega})$$ | Relación más general para torques. |

---

## 🔷 4. Cinemática de un punto P del cuerpo rígido

| Relación | Ecuación general | Notas |
|----------|------------------|--------|
| Velocidad | $$\vec{v}_P=\vec{v}_G+\boldsymbol{\omega}\times\vec{r}_{P/G}$$ | Válida para cualquier punto P. |
| Aceleración | $$\vec{a}_P=\vec{a}_G+\boldsymbol{\alpha}\times\vec{r}_{P/G}+\boldsymbol{\omega}\times(\boldsymbol{\omega}\times\vec{r}_{P/G})$$ | Incluye término centrífugo y tangencial. |

---

## 🔷 5. Relaciones estructurales del tensor de inercia

| Propiedad                         | Ecuación                                                           | Notas                              |
| --------------------------------- | ------------------------------------------------------------------ | ---------------------------------- |
| Simetría                          | $$\mathbf{I}=\mathbf{I}^T$$                                        | Siempre simétrico.                 |
| Positividad                       | $$\boldsymbol{\omega}^T\mathbf{I}\,\boldsymbol{\omega}>0$$         | Energía cinética siempre positiva. |
| Transformación a ejes principales | $$\mathbf{I}= \mathbf{Q}\,\mathbf{I}_{\text{diag}}\,\mathbf{Q}^T$$ | $\mathbf{Q}$ ortogonal.            |
| Traslado entre puntos             | $$\mathbf{I}_O=\mathbf{I}_G+m[(r^2)\mathbf{1}-\vec{r}\vec{r}^T]$$  | Teorema del eje paralelo (3D).     |

---

## 🔷 6. Resumen super-compacto (lo esencial)

| Concepto | Ecuación general |
|----------|------------------|
| Energía | $$T=\frac12 m v_O^2+\frac12\omega^T I_O\omega + m v_O\cdot(\omega\times r)$$ |
| Momento angular | $$H_O=I_G\omega+m(r\times v_G)$$ |
| Euler (en G) | $$\sum M_G = I_G\alpha + \omega\times(I_G\omega)$$ |
| Momento en O | $$\sum M_O = I_G\alpha + m(r\times a_G) + \omega\times(I_G\omega)$$ |
| Derivada general | $$\frac{dH_O}{dt}=\sum M_O - m(v_O\times v_G)$$ |
| Aceleración punto P | $$a_P=a_G + \alpha\times r_{P/G} + \omega\times(\omega\times r_{P/G})$$ |

---
