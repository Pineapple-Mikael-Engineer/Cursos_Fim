# Energía cinética de un cuerpo rígido en movimiento general

Sea un cuerpo **N** con centro de masa en **C** que se mueve en el espacio.

---

# 1. Definición básica

Para un punto arbitrario **p** del cuerpo:

$$
dT_{p} = \frac{1}{2} v_{p}^{2}\, dm
$$

La energía cinética total es:

$$
T = \int_{N} \frac{1}{2} v_{p}^{2} \, dm
$$

o en forma de volumen:

$$
T = \int_{N} \frac{1}{2} \rho\, v_{p}^{2} \, dV
$$

---

# 2. Velocidad de un punto del cuerpo

La velocidad de **p**, respecto al CM, es:

$$
\vec{v}_{p}
= \vec{v}_{c} + \vec{\omega} \times \vec{r}_{p/c}
$$

Entonces:

$$
v_{p}^{2}
= v_{c}^{2}
+ 2\,\vec{v}_{c}\cdot(\vec{\omega}\times\vec{r}_{p/c})
+ (\vec{\omega}\times\vec{r}_{p/c})\cdot(\vec{\omega}\times\vec{r}_{p/c})
$$

---

# 3. Sustitución en la energía cinética

$$
T = \int_{N} \frac{1}{2}\rho\left[
v_{c}^{2}
+ 2\,\vec{v}_{c}\cdot(\vec{\omega}\times\vec{r}_{p/c})
+ (\vec{\omega}\times\vec{r}_{p/c})\cdot(\vec{\omega}\times\vec{r}_{p/c})
\right] dV
$$

El término lineal se anula:

$$
T = 
\int_{N} \frac{1}{2}\rho v_{c}^{2}\,dV
+ \cancelto{0}{\int_{N} \rho\,\vec{v}_{c}\cdot(\vec{\omega}\times\vec{r}_{p/c})\, dV}
+ \int_{N} \frac{1}{2}\rho\, (\vec{\omega}\times\vec{r}_{p/c})\cdot(\vec{\omega}\times\vec{r}_{p/c})\, dV
$$

Definimos:

| Nombre | Definición |
|--------|------------|
| $$I_1$$ | $$\int_{N} \tfrac{1}{2}\rho\, v_c^{2}\, dV$$ |
| $$I_2$$ | $$\int_{N} \tfrac{1}{2}\rho\,(\vec{\omega}\times\vec{r}_{p/c})\cdot(\vec{\omega}\times\vec{r}_{p/c})\,dV$$ |

---

# 4. Primera integral: $I_1$

$$
I_1 = \frac{v_c^{2}}{2} \int_{N} \rho\, dV
= \frac{1}{2} m\, v_c^{2}
$$

$$
\therefore\quad I_1 = \frac{1}{2} m\, v_c^{2}
$$

---

# 5. Segunda integral: $I_2$

Partimos de:

$$
I_2 = \int_{N} \frac{1}{2}\rho
(\vec{\omega}\times\vec{r})\cdot(\vec{\omega}\times\vec{r})\, dV
$$

Sea:

$$
\vec{\omega}\times\vec{r}
= (\omega_i \hat e_i)\times (r_j \hat e_j)
= \omega_i r_j\,\epsilon_{ijk}\,\hat e_k
$$

Entonces:

$$
(\vec{\omega}\times\vec{r})\cdot(\vec{\omega}\times\vec{r})
= (\omega_i r_j\,\epsilon_{ijk}\hat e_k)\cdot(\omega_m r_n\,\epsilon_{mnp}\hat e_p)
$$

Contrayendo:

$$
\omega_i r_j \omega_m r_n\,\epsilon_{ijk}\epsilon_{mnp}\delta_{kp}
= \omega_i r_j \omega_m r_n\,\epsilon_{ijk}\epsilon_{mnk}
$$

Usamos la identidad:

$$
\epsilon_{ijk}\epsilon_{mnk}
= \delta_{im}\delta_{jn} - \delta_{in}\delta_{jm}
$$

Sustituyendo:

$$
\omega_i r_j \omega_m r_n
(\delta_{im}\delta_{jn} - \delta_{in}\delta_{jm})
= \omega_i\omega_i r_j r_j
- (\omega_i r_i)(\omega_j r_j)
$$

Definimos:

| Nombre | Definición |
|--------|------------|
| $$J_1$$ | $$\int \rho\,\omega_i\omega_i\, r_j r_j\, dV$$ |
| $$J_2$$ | $$\int \rho\,(\omega_i r_i)(\omega_j r_j)\, dV$$ |

---

## 5.1. Primera subintegral $J_1$

$$
J_1 = \int \rho\,\omega_i\omega_i r_j r_j\, dV
= \omega_i\omega_i\, Q_{jj}
= \omega^2\, Tr(\hat Q)
= \vec{\omega}\cdot\left[Tr(\hat Q)\,\mathbb{1}\right]\cdot \vec{\omega}
$$

---

## 5.2. Segunda subintegral $J_2$

$$
J_2 = \int\rho\,(\omega_i r_i)(\omega_j r_j)\,dV
= \omega_i\omega_j \int \rho\, r_i r_j\, dV
= \omega_i\omega_j\, Q_{ij}
= \vec{\omega}\cdot\hat Q\cdot\vec{\omega}
$$

---

# 6. Resultado de $I_2$

$$
I_2 = \frac{1}{2}\left[
\vec{\omega}\cdot\left(Tr(\hat Q)\mathbb{1}\right)\cdot\vec{\omega}
- \vec{\omega}\cdot\hat Q\cdot\vec{\omega}
\right]
$$

Por definición del tensor de inercia respecto al CM:

$$
\hat I_c = Tr(\hat Q)\mathbb{1} - \hat Q
$$

Entonces:

$$
I_2 = \frac{1}{2}\,\vec{\omega}\cdot\hat I_c\cdot\vec{\omega}
$$

$$
\therefore\quad
I_2 = \frac{1}{2}\,\vec{\omega}\cdot\hat I_c\cdot\vec{\omega}
$$

---

# 7. Forma final de la energía cinética

$$
T
= \frac{1}{2}m\, v_c^{2}
+ \frac{1}{2}\,\vec{\omega}\cdot\hat{I}_c\cdot\vec{\omega}
$$

---

