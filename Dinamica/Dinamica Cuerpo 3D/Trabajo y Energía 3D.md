# ⚡ Trabajo, Energía y Momento Angular — **Cuerpo Rígido en 3D (Generalizado)**

Esta anotación extiende completamente el caso 2D hacia **3D**, incorporando el **tensor de inercia**, el **teorema del eje paralelo tensorial**, y la forma **generalizada** de las ecuaciones de energía, trabajo y momento angular.

---

# 🧩 **1. Energía Cinética del Cuerpo Rígido en 3D**

| **Concepto**                             | **Fórmula**                                                                                                                                                  | **Comentario**                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------- |
| Energía cinética total (general)         | $$T=\tfrac{1}{2}m v_G^{2}+\tfrac{1}{2}\,\boldsymbol{\omega}^{T}\mathbf{I}_G \boldsymbol{\omega}$$                                                            | Expresada respecto al centro de masa $G$. |
| Energía cinética respecto a un punto $O$ | $$T=\tfrac{1}{2}m v_O^{2}+\tfrac{1}{2}\,\boldsymbol{\omega}^{T}\mathbf{I}_O\boldsymbol{\omega} + m\,\vec{v}_O\cdot(\boldsymbol{\omega}\times\vec{r}_{G/O})$$ | Forma **más general**.                    |
| Caso: $O$ fijo                           | $$T=\tfrac{1}{2}\,\boldsymbol{\omega}^{T}\mathbf{I}_O\boldsymbol{\omega}$$                                                                                   | Si $v_O=0$.                               |
| Caso: $O\equiv G$                        | $$T=\tfrac{1}{2}m v_G^{2}+\tfrac{1}{2}\,\boldsymbol{\omega}^{T}\mathbf{I}_G\boldsymbol{\omega}$$                                                             | Forma estándar.                           |

---

# 🧮 **2. Trabajo y Potencia en 3D**

| Concepto | Fórmula | Comentario |
|----------|---------|------------|
| Teorema trabajo–energía | $$W_{\text{ext}} = \Delta T$$ | Universal. |
| Trabajo traslacional en $G$ | $$W_{\text{tras}}=\int \sum \vec{F}\cdot d\vec{r}_G$$ | Fuerzas externas. |
| Trabajo rotacional en $G$ | $$W_{\text{rot,G}}=\int \sum \vec{M}_G\cdot d\boldsymbol{\theta}$$ | Momento respecto a $G$. |
| Trabajo rotacional en $O$ | $$W_{\text{rot,O}} = \int \sum \vec{M}_O\cdot d\boldsymbol{\theta}$$ | Generalizado a cualquier punto. |
| Potencia instantánea (en $G$) | $$P=\sum\vec{F}\cdot\vec{v}_G + \sum \vec{M}_G\cdot\boldsymbol{\omega}$$ | Derivada de $T$. |
| Potencia instantánea (en $O$) | $$P=\sum\vec{F}\cdot\vec{v}_O + \sum \vec{M}_O\cdot\boldsymbol{\omega}$$ | Punto arbitrario. |

---

# 🌀 **3. Momento Lineal y Angular en 3D**

| Magnitud                             | Fórmula                                                                                                                            | Comentario                                |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| Momento lineal                       | $$\vec{P} = m\vec{v}_G$$                                                                                                           | Igual que en traslación pura.             |
| Derivada del momento lineal          | $$\frac{d\vec{P}}{dt} = \sum \vec{F}$$                                                                                             | Segunda ley de Newton.                    |
| Momento angular respecto a $G$       | $$\vec{H}_G = \mathbf{I}_G\,\boldsymbol{\omega}$$                                                                                  | Usando el tensor.                         |
| Momento angular respecto a $O$       | $$\vec{H}_O = \vec{H}_G + m\,\vec{r}_{G/O}\times\vec{v}_G$$                                                                        | Forma general 3D.                         |
| Derivada general del momento angular | $$\frac{d\vec{H}_O}{dt}=\sum \vec{M}_O - m(\vec{v}_O\times\vec{v}_G)$$                                                             | **La más general** (cuando $O$ se mueve). |
| Caso: $O$ fijo                       | $$\frac{d\vec{H}_O}{dt}=\sum\vec{M}_O$$                                                                                            | Forma clásica.                            |
| Caso: $O\equiv G$                    | $$\frac{d\vec{H}_G}{dt}=\sum\vec{M}_G=\mathbf{I}_G\boldsymbol{\alpha}+\boldsymbol{\omega}\times(\mathbf{I}_G\boldsymbol{\omega})$$ | Ecuación de Euler.                        |

---

# 🧱 **4. Tensor de Inercia — Teoremas esenciales en 3D**

## 4.1 Definición general

$$
\mathbf{I}_G =
\begin{bmatrix}
\int(y^2+z^2)\,dm & -\int xy\,dm & -\int xz\,dm\\
-\int xy\,dm & \int(x^2+z^2)\,dm & -\int yz\,dm\\
-\int xz\,dm & -\int yz\,dm & \int(x^2+y^2)\,dm
\end{bmatrix}
$$

---

## 4.2 Propiedades matemáticas del tensor

| Propiedad | Implicación |
|-----------|-------------|
| Simétrico | Se puede diagonalizar mediante rotación ortogonal. |
| Definido positivo | $\boldsymbol{\omega}^T I \boldsymbol{\omega} > 0$. |
| Autovalores reales | Momentos de inercia principales. |
| Autovectores ortogonales | Ejes principales de inercia. |
| Cambia con rotaciones | Pero sus autovalores permanecen invariantes. |

---

## 4.3 Tensor en ejes principales

$$
\mathbf{I}_{G,\text{principal}} =
\begin{bmatrix}
I_1 & 0 & 0\\
0 & I_2 & 0\\
0 & 0 & I_3
\end{bmatrix}
$$

| Eje | Interpretación |
|-----|---------------|
| $I_1,I_2,I_3$ | Momentos principales de inercia. |

---

## 4.4 Teorema del eje paralelo (forma tensorial)

$$
\mathbf{I}_O = \mathbf{I}_G + m\left[(\vec{d}\cdot\vec{d})\mathbf{1} - \vec{d}\vec{d}^{T}\right]
$$

Forma expandida:

$$
m\begin{bmatrix}
d_y^2+d_z^2 & -d_x d_y & -d_x d_z\\
-d_y d_x & d_x^2+d_z^2 & -d_y d_z\\
-d_z d_x & -d_z d_y & d_x^2+d_y^2
\end{bmatrix}
$$

---

# 🛰 **5. Ecuaciones Rotacionales (Ecuaciones de Euler)**

Expresadas en **ejes principales**:

$$
I_1\dot{\omega}_1 - (I_2-I_3)\omega_2\omega_3 = M_1
$$

$$
I_2\dot{\omega}_2 - (I_3-I_1)\omega_3\omega_1 = M_2
$$

$$
I_3\dot{\omega}_3 - (I_1-I_2)\omega_1\omega_2 = M_3
$$

---

# 📘 **6. Formas resumidas (para repaso)**

| Tipo | Fórmula | Nota clave |
|------|---------|------------|
| Energía cinética | $$T=\tfrac{1}{2}m v_G^{2}+\tfrac{1}{2}\boldsymbol{\omega}^T I_G\boldsymbol{\omega}$$ | Forma estándar. |
| Momento angular (en $G$) | $$\vec{H}_G = I_G \boldsymbol{\omega}$$ | Fundamental en dinámica 3D. |
| Momento angular (en $O$) | $$\vec{H}_O = I_G\omega + m(r_{G/O}\times v_G)$$ | Para cualquier punto. |
| Ecuaciones de Euler | $$I\alpha+\omega\times(I\omega)=M$$ | La ecuación “máxima” de rotación. |
| Eje paralelo tensorial | $$I_O = I_G + m[(d\cdot d)I - dd^T]$$ | Usar siempre en 3D. |

---

# 🧠 **7. Notas finales útiles para examen**

- Toda rotación real ocurre respecto a **ejes principales**.  
- El término $\omega\times(I\omega)$ describe **acoplamiento giroscópico**.  
- En 3D **nunca** se reduce a una sola ecuación escalar (como sí en 2D).  
- Todos los resultados dependen de **punto de referencia + orientación del cuerpo**.  
- La forma tensorial del eje paralelo es imprescindible para problemas con ejes desplazados.  

---


$$
I_{1} = \left[ \int_{N} \rho \; \vec{r}_{ p / c} \, dV \right]  \times \vec{a}_{c}
$$
