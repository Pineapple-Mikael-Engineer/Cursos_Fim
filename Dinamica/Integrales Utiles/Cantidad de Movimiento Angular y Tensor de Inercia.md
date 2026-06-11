# Momento angular (cantidad de movimiento angular) — cuerpo rígido en coordenadas no inerciales

Sea un cuerpo **N** con centro de masa **C** que se mueve en el espacio tridimensional, respecto a un sistema de coordenadas **no inercial** con origen en **O**.

---

## 1. Definición

Definimos el diferencial de momento angular de un elemento $p\in N$ como:

$$
d \vec{H}^{o}_{p} = \vec{r}_{p / o} \times \vec{v}_{p} \; dm
$$

El momento angular total (integrando sobre N) es:

$$
\vec{H}^{o} = \int_{N} \vec{r}_{p / o} \times \vec{v}_{p} \; dm
$$

o en forma de volumen:

$$
\vec{H}^{o} = \int_{N} \rho \,\vec{r}_{p / o} \times \vec{v}_{p} \; dV
$$

---

## 2. Relaciones cinemáticas usadas

Posición:

$$
\vec{r}_{p / o} = \vec{r}_{p / c} + \vec{r}_{c / o}
$$

Velocidad (velocidad de un punto del cuerpo en movimiento rígido):

$$
\vec{v}_{p}= \vec{v}_{c} + \vec{\omega} \times \vec{r}_{p / c}
$$

Sustituyendo estas relaciones en la expresión de $\vec H^o$:

$$
\vec{H}^{o} = \int_{N} \rho \left(\vec{r}_{p / c} + \vec{r}_{c / o} \right)  \times \left( \vec{v}_{c} + \vec{\omega} \times \vec{r}_{p / c} \right)  \; dV
$$

Expandimos y agrupamos términos:

$$
\vec{H}^{o} = I_{1} + I_{2}
$$

donde

$$
I_{1} = \int _{N} \rho\; \left[ \vec{r}_{p / c} \times \vec{v}_{c} + \vec{r}_{p / c} \times \left( \vec{\omega} \times \vec{r}_{p / c} \right) \right] \, dV
$$

$$
I_{2} = \int _{N} \rho\; \left[ \vec{r}_{c / o} \times \vec{v}_{c} + \vec{r}_{c / o} \times \left( \vec{\omega} \times \vec{r}_{p / c} \right) \right] \, dV
$$

---

# 3. Separación de términos y anulaciones

### 3.1. Primer integral ($I_1$)

Observamos que, por definición del CM,

$$
\int_{N} \rho \,\vec{r}_{p/c}\, dV = \vec{0}
$$

por lo que el primer término de $I_1$ se anula:

$$
I_{1} = \cancelto{ 0 }{ \int_{N} \rho\; \vec{r}_{p / c} \times \vec{v}_{c} \, dV } + \int_{N} \rho\; \vec{r}_{p / c} \times \left( \vec{\omega} \times \vec{r}_{p / c} \right) \, dV
$$

Es decir:

$$
I_{1} = \int_{N} \rho\; \vec{r}_{p / c} \times \left( \vec{\omega} \times \vec{r}_{p / c} \right) \, dV
$$

Usamos la identidad vectorial:

$$
\vec{r} \times \left(  \vec{\omega} \times \vec{r} \right) = \vec{\omega} \, r^{2} - \vec{r} \left( \vec{\omega} \cdot \vec{r} \right)
$$

---

### 3.1.1. Primera componente (proyección sobre $\vec{\omega}$)

$$
\int_{N} \rho \; \vec{\omega} \, |r|^{2}\; dV = \vec{\omega} \int_{N} \rho |r|^{2} \; dV
$$

### 3.1.2. Segunda componente (término tensórico)

Se escribe en componentes:

$$
\vec{r} \left( \vec{\omega} \cdot \vec{r} \right) = r_{i}\hat{e}_{i} \left( \omega_{j}r_{j} \right)
$$

Por tanto:

$$
\int_{N} \rho \; r_{i}r_{j} \omega_{j} \hat{e}_{i} \; dV = Q_{ij} \omega_{j} \hat{e}_{i} = \hat{Q} \cdot \vec{\omega}
$$

---

### 3.1.3. Identidades y resultado intermedio

Definimos la traza del tensor $\hat{Q}$:

$$
Tr(\hat Q) = \int_N \rho(x^2+y^2+z^2)\,dV
$$

Con ello:

$$
\int_N \rho\,\vec{\omega}\,|r|^2 dV
= Tr(\hat Q_c)\,\mathbb{1}\cdot\vec{\omega}
$$

y

$$
\int_N \rho\, \vec{r}(\vec{r}\cdot\vec{\omega}) \, dV
= \hat Q_c\cdot\vec{\omega}
$$

Por lo tanto:

$$
I_{1}
= Tr(\hat Q_c)\mathbb{1}\cdot\vec{\omega}
- \hat Q_c\cdot \vec{\omega}
$$

Recordando la definición del tensor de inercia respecto al CM:

$$
\hat I_c = Tr(\hat Q_c)\mathbb 1 - \hat Q_c
$$

obtenemos finalmente:

$$
I_{1}= \hat I_c \cdot \vec{\omega}
$$

---

### 3.2. Segunda integral ($I_2$)

Partimos de:

$$
I_{2} = \int_{N} \rho\; \vec{r}_{c / o} \times \vec{v}_{c}  \, dV + \int_{N} \rho\; \vec{r}_{c / o} \times \left( \vec{\omega} \times \vec{r}_{p / c} \right) \, dV
$$

El segundo término se anula porque $\vec{r}_{c/o}$ es constante y $\int_N \rho\,\vec{r}_{p/c}\,dV=\vec0$:

$$
I_{2} = \int_{N} \rho\; \vec{r}_{c / o} \times \vec{v}_{c}  \, dV + \cancelto{ 0 }{ \int_{N} \rho\; \vec{r}_{c / o} \times \left( \vec{\omega} \times \vec{r}_{p / c} \right) \, dV }
$$

Sacando constantes de la integral:

$$
I_{2} = \left[ \int_{N} \rho\;dV \right]  \vec{r}_{c / o} \times \vec{v}_{c}
$$

Por tanto:

$$
\therefore I_{2} = m  \left( \vec{r}_{c / o} \times \vec{v}_{c} \right)
$$

---

## 4. Forma final

Sumando $I_1$ e $I_2$:

$$
\boxed{\;
\vec{H}^{o} = \hat I_c \cdot \vec{\omega} + m  \left( \vec{r}_{c / o} \times \vec{v}_{c} \right)
\;}
$$

---

## 5. Caso especial (origen en el CM)

Si elegimos $O=C$ (origen en el centro de masa), $\vec{r}_{c/o}=\vec{0}$ y se simplifica a:

$$
\boxed{\;
\vec{H}^{c} = \hat I_c \cdot \vec{\omega}
\;}
$$

---


