# Anotación — Torque general y relación con el tensor de inercia

# 1. Definiciones iniciales

Sea un cuerpo **N**, con centro de masa **C**, y un sistema inercial centrado en **O**.

## Torque diferencial

$$
d \vec{\tau}^{o}_{p} = \vec{r}_{ p / o } \times d \vec{F}_{p},
\qquad
d \vec{F}_{p} = \vec{a}_{p} dm,
\qquad
p: \text{punto arbitrario de } N
$$

## Relaciones cinemáticas

$$
\vec{a}_{p}=\vec{a}_{c}+ \vec{\alpha} \times \vec{r}_{p / c} + \vec{w} \times (\vec{w} \times \vec{r}_{p / c})
$$

$$
\vec{r}_{p / o} = \vec{r}_{p / c} + \vec{r}_{c / o}
$$

$$
dm = \rho \, dV
$$

## Resultado estructural preliminar

$$
\vec{\tau}^{o}= \left( I_{1}+I_{2} \right)
$$

donde:

$$
I_{1}= \int_{N}{\rho\left[
\vec{r}_{p / c}\times \vec{a}_{c} +
\vec{r}_{p / c} \times (\vec{\alpha} \times \vec{r}_{p / c}) +
\vec{r}_{p / c} \times ( \vec{w} \times (\vec{w} \times \vec{r}_{p / c}))
\right]} dV
$$

$$
I_{2} = \int_{N}{\rho\left[
\vec{r}_{c / o}\times \vec{a}_{c} +
\vec{r}_{c / o} \times (\vec{\alpha} \times \vec{r}_{p / c}) +
\vec{r}_{c / o} \times ( \vec{w} \times (\vec{w} \times \vec{r}_{p / c}))
\right]} dV
$$

---

# 2. Separación de términos

## 2.1. Primer término: $I_1$

Aplicando cancelaciones:

$$
I_{1} = \cancelto{0}{ \int_{N} \rho(\vec{r}_{p / c}\times \vec{a}_{c}) dV }
+ \int_{N} \rho(\vec{r}_{p / c} \times (\vec{\alpha} \times \vec{r}_{p / c}))dV
+ \int_{N}\rho(\vec{r}_{p / c} \times ( \vec{w} \times (\vec{w} \times \vec{r}_{p / c})))dV 
$$

Llamamos:

| Nombre | Definición |
|--------|------------|
| $$J_1$$ | $$\int_{N} \rho\big( \vec{r}_{p / c} \times (\vec{\alpha} \times \vec{r}_{p / c})\big)\,dV$$ |
| $$J_2$$ | $$\int_{N}\rho(\vec{r}_{p / c} \times ( \vec{w} \times (\vec{w} \times \vec{r}_{p / c})))\,dV$$ |

---

# 3. Cálculo del término $J_1$

## Identidad vectorial

$$
\vec{r}\times(\vec{\alpha}\times\vec{r})
= \vec{\alpha}\,|r|^{2} - \vec{r}\,(\vec{r}\cdot\vec{\alpha})
$$

### Primer componente:

$$
\int_{N} \rho \;\vec{\alpha} \; |r|^{2}_{p / c} \; dV
= \vec{\alpha} \int_{N} \rho |r|^{2} dV
$$

### Segundo componente:

$$
\vec{r} \;(\vec{r}\cdot \vec{\alpha})
= r_i \hat e_i (r_j \alpha_j)
= r_i r_j \alpha_j \hat e_i
$$

$$
\int_{N} \rho \; r_i r_j \alpha_j \hat e_i \; dV
= Q_{ij} \alpha_j \hat e_i
= \hat Q \cdot \vec{\alpha}
$$

### Identidades útiles

$$
Tr(\hat Q) = \int \rho(x^2+y^2+z^2)\,dV
$$

Con ello:

$$
\int \rho\,\vec{\alpha}|r|^2 dV
= Tr(\hat Q_c)\,\mathbb{1}\cdot\vec{\alpha}
$$

$$
\int \rho\left( \vec{r}(\vec{r}\cdot\vec{\alpha}) \right) dV
= \hat Q_c\cdot\vec{\alpha}
$$

### Resultado del término $J_1$

$$
J_1
= Tr(\hat Q_c)\mathbb{1}\cdot\vec{\alpha}
- \hat Q_c\cdot \vec{\alpha}
$$

Definición del tensor de inercia respecto a **C**:

$$
\hat I_c = Tr(\hat Q_c)\mathbb 1 - \hat Q_c
$$

Por tanto:

$$
J_1 = \hat I_c \cdot \vec{\alpha}
$$

---

# 4. Cálculo del término $J_2$

Partimos de:

$$
J_{2} =
\int_{N}\rho(\vec{r}_{p/c} \times ( \vec{w} \times (\vec{w} \times \vec{r}_{p/c})))dV
$$

Usamos:

$$
\vec{r}\times[\vec{w}\times(\vec{w}\times \vec{r})]
= (\vec{r}\times\vec{w})(\vec{r}\cdot\vec{w})
$$

---

## Expansión indexada

$$
(r_i \hat e_i \times w_j \hat e_j)(r_k w_k)
= r_i w_j r_k w_k\,\epsilon_{ijl}\,\hat e_l
$$

$$
\int \rho\; r_i w_j r_k w_k\,\epsilon_{ijl}\hat e_l\, dV
= Q_{ik}w_j w_k\,\epsilon_{ijl}\hat e_l
$$

$$
Q_{ik} w_k \hat e_i \times (w_j\hat e_j)
= (\hat Q_c\cdot\vec{w}) \times \vec{w}
$$

### Resultado del término $J_2$

$$
J_2 = (\hat Q_c\cdot\vec{w}) \times \vec{w}
$$

## Relación con el tensor de inercia

Como:

$$
\hat I_c\cdot\vec{\omega}
= Tr(\hat Q_c)\vec{\omega} - \hat Q_c\cdot\vec{\omega}
$$

y

$$
\vec{\omega}\times\vec{\omega}=0,
$$

tenemos:

$$
\vec{\omega}\times(\hat I_c\cdot\vec{\omega})
= -\vec{\omega}\times(\hat Q_c\cdot\vec{\omega})
= (\hat Q_c\cdot\vec{\omega})\times\vec{\omega}
$$

Por tanto:

$$
J_2 = \vec{\omega}\times(\hat I_c\cdot\vec{\omega})
$$

---

# 5. Cálculo del término $I_2$

Solo sobrevive:

$$
I_2 = \int_{N} \rho(\vec{r}_{c / o}\times \vec{a}_{c})dV
$$

Como $\vec{r}_{c/o}$ y $\vec{a}_c$ son constantes para la integral:

$$
I_2 = (\vec{r}_{c / o}\times \vec{a}_{c}) \int_{N} \rho dV
= (\vec{r}_{c / o}\times \vec{a}_{c})\,m
$$

Finalmente:

$$
I_2 = \vec{r}_{c/o} \times \vec{F}
$$

---

# 6. Resultado general (forma limpia)

Sumando:

$$
\vec{\tau}^o
= \hat I_c\cdot\vec{\alpha}
+ \vec{\omega}\times(\hat I_c\cdot\vec{\omega})
+ \vec{r}_{c/o}\times\vec{F}
$$

---

# 7. Forma habitual (cuando el origen es el CM)

Si elegimos $O=C$:

$$
\vec{\tau}^c
= \hat I_c\cdot\vec{\alpha}
+ \vec{\omega}\times(\hat I_c\cdot\vec{\omega})
$$

que es la ecuación estándar de la dinámica rotacional.

