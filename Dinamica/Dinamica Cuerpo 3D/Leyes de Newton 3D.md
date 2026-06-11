# 🧩 Resumen de fórmulas — Cuerpo rígido en **3D**

| **Concepto**                                       | **Ecuación general**                                                                                                  | **Descripción / Variables**                                         |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **1️⃣ Segunda ley de Newton (traslación)**         | $\sum \vec{F} = m \vec{a}_G$                                                                                          | La fuerza neta determina la aceleración del centro de masa $G$.     |
| **2️⃣ Ecuaciones escalares (componentes)**         | $\sum F_x = m a_{Gx}$ <br> $\sum F_y = m a_{Gy}$ <br> $\sum F_z = m a_{Gz}$                                           | Descomposición cartesiana en 3D.                                    |
| **3️⃣ Momento angular en 3D**                      | $\vec{L} = \mathbf{I}\,\vec{\omega}$                                                                                  | Momento angular definido por el **tensor de inercia**.              |
| **4️⃣ Segunda ley rotacional general (en G)**      | $\sum \vec{\tau}_G = \frac{d\vec{L}}{dt} = \mathbf{I}\vec{\alpha} + \vec{\omega} \times (\mathbf{I}\vec{\omega})$     | Forma completa con término giroscópico.                             |
| **5️⃣ Momento respecto a un punto arbitrario (O)** | $\sum \vec{\tau}_O = \sum \vec{\tau}_G + \vec{r}_{G/O} \times (m\vec{a}_G)$                                           | Útil cuando el punto de referencia **no coincide con G**.           |
| **6️⃣ Teorema del eje paralelo (tensorial)**       | $\mathbf{I}_O = \mathbf{I}_G + m \left[(\vec{d}\cdot \vec{d})\mathbf{1} - \vec{d}\vec{d}^T\right]$                    | Generalización del eje paralelo en 3D. $\vec{d} =$ vector de O a G. |
| **7️⃣ Aceleración de un punto P del cuerpo**       | $\vec{a}_P = \vec{a}_G + \vec{\alpha} \times \vec{r}_{P/G} + \vec{\omega} \times (\vec{\omega} \times \vec{r}_{P/G})$ | Aceleración lineal + rotacional + centrífuga.                       |
| **8️⃣ Ecuación rotacional usando inercia en O**    | $\sum \vec{\tau}_O = \mathbf{I}_O \vec{\alpha} + \vec{\omega} \times (\mathbf{I}_O \vec{\omega})$                     | Igual que en G, pero usando el tensor trasladado.                   |
| **9️⃣ Relación general entre momentos (O y G)**    | $\sum \vec{\tau}_O = \sum \vec{\tau}_G + \vec{r}_{G/O} \times (m\vec{a}_G)$                                           | Conecta ambas descripciones.                                        |

---

# 🧲 Tensor de inercia en 3D

## 🔹 **Definición general**
El **tensor de inercia** respecto al centro de masa $G$ se define como:

$$
\mathbf{I}_G =
\begin{bmatrix}
\int (y^2 + z^2)\,dm & -\int xy\,dm & -\int xz\,dm\\[4pt]
-\int xy\,dm & \int (x^2 + z^2)\,dm & -\int yz\,dm\\[4pt]
-\int xz\,dm & -\int yz\,dm & \int (x^2 + y^2)\,dm
\end{bmatrix}
$$

### 🔸 Significado
- Diagonales → momentos de inercia ($I_{xx}$, $I_{yy}$, $I_{zz}$).  
- Fuera de la diagonal → productos de inercia (miden acoplamiento de ejes).  
- Es una **matriz simétrica 3×3**, lo que garantiza ejes principales ortogonales.

---

# 🧭 Tensor de inercia en ejes principales

Cuando se diagonaliza:

$$
\mathbf{I}_G =
\begin{bmatrix}
I_x & 0 & 0\\
0 & I_y & 0\\
0 & 0 & I_z
\end{bmatrix}
$$

La ecuación rotacional se simplifica:

| Eje | Ecuación |
|-----|----------|
| $x$ | $I_x \alpha_x = \tau_x - (I_z - I_y)\omega_y\omega_z$ |
| $y$ | $I_y \alpha_y = \tau_y - (I_x - I_z)\omega_z\omega_x$ |
| $z$ | $I_z \alpha_z = \tau_z - (I_y - I_x)\omega_x\omega_y$ |

---

# 🧾 Resumen rápido para examen (3D)

- **Traslación:** $\sum \vec{F} = m\vec{a}_G$  
- **Rotación (en G):** $\sum \vec{\tau}_G = \mathbf{I}\vec{\alpha} + \vec{\omega} \times (\mathbf{I}\vec{\omega})$  
- **Rotación (en O):** $\sum \vec{\tau}_O = \mathbf{I}_O\vec{\alpha} + \vec{\omega} \times (\mathbf{I}_O\vec{\omega})$  
- **Eje paralelo:** $\mathbf{I}_O = \mathbf{I}_G + m[(\vec{d}\cdot\vec{d})\mathbf{1} - \vec{d}\vec{d}^T]$  
- **Aceleración de un punto P:** $\vec{a}_P = \vec{a}_G + \vec{\alpha}\times \vec{r}_{P/G} + \vec{\omega}\times(\vec{\omega}\times\vec{r}_{P/G})$

