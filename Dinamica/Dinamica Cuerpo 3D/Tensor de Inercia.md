
# 🧩 **Anotación — El Tensor de Inercia en 3D (definición, propiedades y teoremas)**

Esta anotación resume **qué es el tensor de inercia**, cómo se construye, sus **propiedades matemáticas**, cómo se **diagonaliza**, y los **teoremas fundamentales** asociados.

---

# 🧲 1. Definición general del tensor de inercia

El tensor de inercia respecto al centro de masa $G$ está dado por:

$$
\mathbf{I}_G =
\begin{bmatrix}
\int (y^2 + z^2)\,dm & -\int xy\,dm & -\int xz\,dm\\[4pt]
-\int xy\,dm & \int (x^2 + z^2)\,dm & -\int yz\,dm\\[4pt]
-\int xz\,dm & -\int yz\,dm & \int (x^2 + y^2)\,dm
\end{bmatrix}
$$

| Elemento | Interpretación |
|----------|----------------|
| $I_{xx} = \int(y^2+z^2)\,dm$ | Momento de inercia respecto al eje $x$ |
| $I_{yy} = \int(x^2+z^2)\,dm$ | Momento respecto al eje $y$ |
| $I_{zz} = \int(x^2+y^2)\,dm$ | Momento respecto al eje $z$ |
| $I_{xy} = -\int xy\,dm$ | Producto de inercia (acoplamiento entre los ejes $x$ e $y$) |
| $I_{xz} = -\int xz\,dm$ | Producto entre $x$ y $z$ |
| $I_{yz} = -\int yz\,dm$ | Producto entre $y$ y $z$ |

---

# 🧭 2. Significado físico

| Concepto | Explicación |
|----------|-------------|
| Momento de inercia | Mide **resistencia a rotar** alrededor de un eje |
| Productos de inercia | Miden cuánta masa está **mal alineada** respecto al eje principal |
| Ejes principales | Direcciones donde **no hay acoplamiento** entre rotaciones |
| Tensor de inercia | Matriz que cuantifica la **distribución espacial de la masa** |

---

# 🧮 3. Propiedades matemáticas del tensor de inercia

| Propiedad | Consecuencia |
|-----------|--------------|
| **Simétrico** ($I_{ij} = I_{ji}$) | Puede diagonalizarse mediante rotación ortogonal |
| **Definido positivo** | $v^T I v > 0$ para cualquier vector no nulo |
| **Base dependiente** | Cambia si rotas los ejes, pero mantiene valores invariables (autovalores) |
| **Autovalores reales** | Son los **momentos de inercia principales** |
| **Autovectores ortogonales** | Son los **ejes principales de inercia** |

---

# 🔄 4. Tensor de inercia en ejes principales

Cuando el sistema de referencia coincide con los **ejes principales**, el tensor se vuelve **diagonal**:

$$
\mathbf{I}_G =
\begin{bmatrix}
I_x & 0 & 0\\
0 & I_y & 0\\
0 & 0 & I_z
\end{bmatrix}
$$

| Eje | Interpretación |
|-----|----------------|
| $I_x$ | Momento alrededor del eje principal 1 |
| $I_y$ | Momento alrededor del eje principal 2 |
| $I_z$ | Momento alrededor del eje principal 3 |

---

# 📐 5. ¿Cómo encontrar los ejes principales?

Resolviendo el problema de autovalores:

$$
\mathbf{I}_G \vec{v} = \lambda \vec{v}
$$

| Objeto | Interpretación |
|--------|----------------|
| $\lambda_i$ | Momentos de inercia principales |
| $\vec{v}_i$ | Ejes principales de inercia |
| $\{\vec{v}_1,\vec{v}_2,\vec{v}_3\}$ | Forman un sistema ortonormal |

---

# 🧲 6. Teorema del eje paralelo (forma tensorial)

Si queremos el tensor respecto a un punto $O$:

$$
\mathbf{I}_O = \mathbf{I}_G + m[(\vec{d}\cdot \vec{d})\mathbf{1} - \vec{d}\vec{d}^T]
$$

| Símbolo          | Significado                |
| ---------------- | -------------------------- |
| $\vec{d}$        | Vector desde $O$ hasta $G$ |
| $\mathbf{1}$     | Matriz identidad 3×3       |
| $m$              | Masa total                 |
| $d =\|\vec{d}\|$ | Distancia entre los puntos |

La forma expandida:

$$
\mathbf{I}_O = 
\mathbf{I}_G +
m\begin{bmatrix}
d_y^2 + d_z^2 & -d_x d_y & -d_x d_z\\
-d_y d_x & d_x^2 + d_z^2 & -d_y d_z\\
-d_z d_x & -d_z d_y & d_x^2 + d_y^2
\end{bmatrix}
$$

---

# 📦 7. Propiedades físicas importantes

| Propiedad | Enunciado |
|-----------|-----------|
| **Máxima estabilidad rotacional** | La rotación pura ocurre alrededor de un eje principal |
| **Acoplamiento dinámico** | Si hay productos de inercia ≠ 0, un torque en un eje causa aceleración en otros |
| **Mayores $I$ → menor aceleración angular** | $\alpha = I^{-1}(\tau - \omega\times(I\omega))$ |
| **El tensor depende de la geometría y la orientación** | No depende de la velocidad, solo de cómo está distribuida la masa |

---

# 📄 8. Resumen rápido del tensor de inercia


• El tensor de inercia es una matriz simétrica 3×3 que describe cómo la masa  
está distribuida respecto a un punto o un eje.  
• Sus elementos diagonales son momentos de inercia.  
• Sus elementos fuera de la diagonal son productos de inercia.  
• Es simétrico, definido positivo y siempre diagonalizable.  
• Sus autovalores → momentos principales.  
• Sus autovectores → ejes principales.  
• Teorema del eje paralelo:  
$\mathbf{I}_O = \mathbf{I}_G + m[(\vec{d}\cdot \vec{d})\mathbf{1} - \vec{d}\vec{d}^T]$