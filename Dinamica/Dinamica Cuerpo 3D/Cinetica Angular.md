# Derivación usando el **operador derivada en una base móvil**  
(Todo está escrito usando `$ ... $` y `$$ ... $$` como pediste)

---

# 1. Identidad fundamental del operador derivada en un sistema móvil

Sea un vector $\,\mathbf{v}(t)\,$. La derivada absoluta (respecto al sistema inercial $I$) y la derivada relativa (vista desde un sistema móvil $A$ que rota con velocidad angular $\boldsymbol{\omega}_A$) se relacionan mediante:

$$
\left.\frac{d\mathbf{v}}{dt}\right|_I
=
\left.\frac{d\mathbf{v}}{dt}\right|_A 
+ \boldsymbol{\omega}_A \times \mathbf{v}
$$

Esta fórmula surge porque una base móvil $\{\mathbf{e}_i\}$ satisface:

$$
\left.\frac{d\mathbf{e}_i}{dt}\right|_I
= \boldsymbol{\omega}_A \times \mathbf{e}_i
$$

---

# 2. Obtención de la suma de velocidades angulares  
## $$\boldsymbol{\omega}_B = \boldsymbol{\omega}_A + \boldsymbol{\omega}_{B/A}$$

Sea $\{\mathbf{E}_i\}$ la base del sistema móvil $B$. Por **definición de velocidad angular**:

$$
\left.\frac{d\mathbf{E}_i}{dt}\right|_I
= \boldsymbol{\omega}_B \times \mathbf{E}_i.
$$

Pero usando el operador de derivada respecto al marco $A$:

$$
\left.\frac{d\mathbf{E}_i}{dt}\right|_I
=
\left.\frac{d\mathbf{E}_i}{dt}\right|_A
+ \boldsymbol{\omega}_A \times \mathbf{E}_i
=
\boldsymbol{\omega}_{B/A} \times \mathbf{E}_i
+ \boldsymbol{\omega}_A \times \mathbf{E}_i.
$$

Comparando con la definición de $\boldsymbol{\omega}_B$:

$$
\boldsymbol{\omega}_B \times \mathbf{E}_i
=
(\boldsymbol{\omega}_A + \boldsymbol{\omega}_{B/A}) \times \mathbf{E}_i.
$$

Como esto vale para los tres vectores independientes $\mathbf{E}_i$:

$$
\boxed{\boldsymbol{\omega}_B=\boldsymbol{\omega}_A+\boldsymbol{\omega}_{B/A}}.
$$

---

# 3. Obtención de la aceleración angular total  
## $$\boldsymbol{\alpha}_B=\boldsymbol{\alpha}_A+\boldsymbol{\alpha}_{B/A}+\boldsymbol{\omega}_A\times\boldsymbol{\omega}_{B/A}$$

Partimos de la suma de velocidades angulares:

$$
\boldsymbol{\omega}_B = \boldsymbol{\omega}_A + \boldsymbol{\omega}_{B/A}.
$$

Tomamos derivada absoluta:

$$
\boldsymbol{\alpha}_B
=
\left.\frac{d\boldsymbol{\omega}_A}{dt}\right|_I
+
\left.\frac{d\boldsymbol{\omega}_{B/A}}{dt}\right|_I
=
\boldsymbol{\alpha}_A
+
\left.\frac{d\boldsymbol{\omega}_{B/A}}{dt}\right|_I.
$$

Usamos el operador de derivada para un vector visto desde $A$:

$$
\left.\frac{d\boldsymbol{\omega}_{B/A}}{dt}\right|_I
=
\left.\frac{d\boldsymbol{\omega}_{B/A}}{dt}\right|_A
+ \boldsymbol{\omega}_A \times \boldsymbol{\omega}_{B/A}
$$

y definimos:

$$
\boldsymbol{\alpha}_{B/A} = \left.\frac{d\boldsymbol{\omega}_{B/A}}{dt}\right|_A.
$$

Sustituyendo:

$$
\boxed{
\boldsymbol{\alpha}_B
=
\boldsymbol{\alpha}_A
+
\boldsymbol{\alpha}_{B/A}
+
\boldsymbol{\omega}_A\times\boldsymbol{\omega}_{B/A}
}.
$$

El término cruzado aparece porque el vector $\boldsymbol{\omega}_{B/A}$ es medido en un sistema que rota, así que él mismo está rotando cuando lo observa un observador inercial.

---

# 4. Resultado final (compacto para apuntes)

$$
\boxed{
\boldsymbol{\omega}_B = \boldsymbol{\omega}_A + \boldsymbol{\omega}_{B/A}
}
$$

$$
\boxed{
\boldsymbol{\alpha}_B = \boldsymbol{\alpha}_A + \boldsymbol{\alpha}_{B/A}
+ \boldsymbol{\omega}_A \times \boldsymbol{\omega}_{B/A}
}
$$

---

Si quieres, puedo transformar todo esto en una **tabla tipo ficha/anotación** como las que usas para tus resúmenes de dinámica en 3D.
