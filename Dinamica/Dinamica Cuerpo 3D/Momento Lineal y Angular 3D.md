# 💠 Cantidad de movimiento lineal y angular (3D, **general y correcta**)

---

## 🔹 1. Cantidad de movimiento lineal (3D)

| Concepto | Ecuación | Descripción breve |
|-----------|-----------|-------------------|
| Definición | $\vec{P}=m\vec{v}_G$ | Momento lineal del cuerpo rígido. |
| Ecuación fundamental | $\dfrac{d\vec{P}}{dt}=\sum\vec{F}$ | Segunda ley de Newton. |
| Componentes | $\sum F_x = m a_{Gx}$<br>$\sum F_y = m a_{Gy}$<br>$\sum F_z = m a_{Gz}$ | Descomposición en ejes cartesianos. |
| Impulso lineal | $\Delta\vec{P}=\int \sum\vec{F}\,dt$ | Relación impulso–momento lineal. |

---

## 🔹 2. Cantidad de movimiento angular en 3D (respecto a un punto O)

| Concepto                         | Ecuación (vectorial)                                                                                                                                 | Descripción breve                                        |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| Definición general               | $\vec{H}_O=\mathbf{I}_G\vec{\omega}+m(\vec{r}_{G/O}\times\vec{v}_G)$                                                                                 | Momento angular total respecto a $O$.                    |
| Derivada general (punto O móvil) | $\dfrac{d\vec{H}_O}{dt}=\sum\vec{M}_O - m(\vec{v}_O\times\vec{v}_G)$                                                                                 | **Forma más general**, válida si $O$ acelera o se mueve. |
| Si $O$ fijo                      | $\dfrac{d\vec{H}_O}{dt}=\sum\vec{M}_O$                                                                                                               | Forma de uso común.                                      |
| Si $O=G$                         | $\vec{H}_G=\mathbf{I}_G\vec{\omega}$<br>$\dfrac{d\vec{H}_G}{dt}=\sum\vec{M}_G=\mathbf{I}_G\vec{\alpha}+\vec{\omega}\times(\mathbf{I}_G\vec{\omega})$ | **Ecuación de Euler** en el centro de masa.              |
| Relación de momentos             | $\sum\vec{M}_O=\sum\vec{M}_G+\vec{r}_{G/O}\times\sum\vec{F}$                                                                                         | Traslada torques entre puntos.                           |
| Relación con aceleraciones       | $\sum\vec{M}_O=\mathbf{I}_G\vec{\alpha}+m(\vec{r}_{G/O}\times\vec{a}_G)+\vec{\omega}\times(\mathbf{I}_G\vec{\omega})$                                | Ecuación rotacional completa en 3D.                      |

---

## 🔹 3. Tensor de inercia (traslación entre puntos)

| Concepto | Ecuación | Descripción |
|-----------|-----------|-------------|
| Tensor de inercia trasladado | $\mathbf{I}_O=\mathbf{I}_G+m\big( (\vec{r}_{G/O}\cdot\vec{r}_{G/O})\mathbf{1}-\vec{r}_{G/O}\otimes\vec{r}_{G/O} \big)$ | **Teorema del eje paralelo en 3D**. |
| Forma alternativa | $\mathbf{I}_O=\mathbf{I}_G+ m\begin{bmatrix} y^2+z^2 & -xy & -xz \\ -xy & x^2+z^2 & -yz \\ -xz & -yz & x^2+y^2 \end{bmatrix}$ | $x,y,z$ son las componentes de $r_{G/O}$. |
| Uso en ecuaciones de movimiento | $\sum\vec{M}_O=\mathbf{I}_O\vec{\alpha}+\vec{\omega}\times(\mathbf{I}_O\vec{\omega})$ | Solo válido si $O$ es **punto fijo**. |

---

## 🔹 4. Formas escalares (en un sistema ortonormal genérico)

Sea $\vec{\omega}=(\omega_x,\omega_y,\omega_z)$:

| Concepto               | Ecuación                                                                                                                                                                                                                                 | Descripción                    |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| Momento angular en $G$ | $\vec{H}_G=\mathbf{I}_G\vec{\omega}$                                                                                                                                                                                                     | Lineal en $\vec{\omega}$.      |
| Ecuaciones de Euler    | $\begin{aligned} I_{xx}\dot{\omega}_x - (I_{yy}-I_{zz})\omega_y\omega_z &= M_{Gx} \\ I_{yy}\dot{\omega}_y - (I_{zz}-I_{xx})\omega_z\omega_x &= M_{Gy} \\ I_{zz}\dot{\omega}_z - (I_{xx}-I_{yy})\omega_x\omega_y &= M_{Gz} \end{aligned}$ | Forma escalar más usada en 3D. |
| Momento angular en $O$ | $\vec{H}_O=\mathbf{I}_G\vec{\omega}+m(\vec{r}_{G/O}\times\vec{v}_G)$                                                                                                                                                                     | Separa rotación y traslación.  |
| Derivada general       | $\dfrac{d\vec{H}_O}{dt}=\sum\vec{M}_O - m(\vec{v}_O\times\vec{v}_G)$                                                                                                                                                                     | Aplica aunque $O$ se mueva.    |
|                        |                                                                                                                                                                                                                                          |                                |

---

## 🔹 5. Resumen final (para examen en 3D)

| Tipo | Ecuación | Comentario |
|------|----------|-------------|
| Lineal | $\dfrac{d\vec{P}}{dt}=\sum\vec{F}$ | Siempre válida. |
| Angular (general, punto móvil) | $\dfrac{d\vec{H}_O}{dt}=\sum\vec{M}_O - m(\vec{v}_O\times\vec{v}_G)$ | **Ecuación más general de rotación**. |
| Angular en $G$ (ecuaciones de Euler) | $\dfrac{d\vec{H}_G}{dt}=\sum\vec{M}_G=\mathbf{I}_G\vec{\alpha}+\vec{\omega}\times(\mathbf{I}_G\vec{\omega})$ | Forma canónica de dinámica 3D. |
| Traslado de momentos | $\sum\vec{M}_O=\sum\vec{M}_G+\vec{r}_{G/O}\times\sum\vec{F}$ | Relación entre puntos. |
| Tensor trasladado | $\mathbf{I}_O=\mathbf{I}_G+m[(r\cdot r)\mathbf{1}-r\otimes r]$ | Eje paralelo 3D. |
| Torque en punto fijo | $\sum\vec{M}_O=\mathbf{I}_O\vec{\alpha}+\vec{\omega}\times(\mathbf{I}_O\vec{\omega})$ | Solo si $O$ no se mueve. |

---

## ✅ Notas clave para usar en problemas 3D

- El momento angular **SIEMPRE** se descompone en rotacional + traslacional.  
- Para puntos móviles, **no** puedes usar $\sum\vec{M}_O=\dfrac{d\vec{H}_O}{dt}$ sin corregir el término $-m(\vec{v}_O\times\vec{v}_G)$.  
- El tensor de inercia puede cambiar si el sistema de referencia rota.  
- Para cuerpos simétricos, el tensor se vuelve diagonal → las ecuaciones de Euler se simplifican mucho.  
- En problemas en 3D, revisa siempre si $O$ está fijo, acelerado o coincide con $G$.

---
