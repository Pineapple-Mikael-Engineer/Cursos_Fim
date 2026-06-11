# Convenciones del tensor de inercia — explicación definitiva

## Notación útil
- $$Q_{ij} = \int r_i r_j\, dm$$ (tensor de segundo momento)
- $$\mathrm{Tr}(Q)=Q_{xx}+Q_{yy}+Q_{zz}=\int r^2\,dm$$

La **definición matemática única** del tensor de inercia (tensor físico) es:

$$
\boxed{\,I_{ij}^{(\text{tensor})}=\int \big(r^2\delta_{ij}-r_i r_j\big)\,dm \,}
$$

De ahí se sigue **sin ambigüedad**:

$$
\boxed{\,I_{ij}^{(\text{tensor})}=\mathrm{Tr}(Q)\,\delta_{ij}-Q_{ij}\,}
$$

y en particular (caso cruzado):

$$
\boxed{\,I_{xy}^{(\text{tensor})}=-\int xy\,dm\, = -Q_{xy}\,}
$$

---

## ¡Aquí vienen las 2 convenciones que producen la confusión!

### Convención A — *Componentes del tensor* (convención matemática, consistente)
Se llaman **componentes del tensor** y **ya incluyen** el signo negativo para los elementos cruzados:
- Definición:
  $$I_{xy}^{(\text{comp})}= -\int xy\,dm$$
- Matriz del tensor (usar directamente estas componentes, SIN signos extra):
  $$
  \mathbf I =
  \begin{pmatrix}
  I_{xx}^{(\text{comp})} & I_{xy}^{(\text{comp})} & I_{xz}^{(\text{comp})}\\[4pt]
  I_{xy}^{(\text{comp})} & I_{yy}^{(\text{comp})} & I_{yz}^{(\text{comp})}\\[4pt]
  I_{xz}^{(\text{comp})} & I_{yz}^{(\text{comp})} & I_{zz}^{(\text{comp})}
  \end{pmatrix}
  $$
  donde, por ejemplo, $$I_{xy}^{(\text{comp})}=-\int xy\,dm.$$
- Nota: en esta convención **no** pones más signos en la matriz, porque ya están dentro de las componentes.

---

### Convención B — *Notación de ingeniería para productos de inercia*
Se define el **producto de inercia** como la integral sin signo y luego la matriz del tensor introduce explícitamente un signo negativo en las posiciones off-diagonal:
- Producto de inercia (ingeniería):
  $$P_{xy}:=\int xy\,dm \quad \text{(a.k.a. "I {xy}" en muchos textos de ingeniería)}$$
- Matriz *usando la notación de ingeniería*:
  $$
  \mathbf I =
  \begin{pmatrix}
  I_{xx} & -P_{xy} & -P_{xz}\\[4pt]
  -P_{xy} & I_{yy} & -P_{yz}\\[4pt]
  -P_{xz} & -P_{yz} & I_{zz}
  \end{pmatrix}
  $$
- Relación entre objetos:
  $$I_{xy}^{(\text{comp})} = -P_{xy}.$$

---

## Por qué parecía que los signos "se cancelaban"
Si mezclas:

- escribir la matriz con los signos (como en la **Convención B**) **y además**  
- definir $I_{xy}$ como $I_{xy}^{(\text{comp})}=-\int xy\,dm$ (es decir, usas la **Convención A** para la letra),

entonces estás usando **dos veces** el signo negativo. Eso produce la falsa sensación de que los "-" se “cancelan” o que la relación con $Q_{ij}$ falla. **El problema es mezclar definiciones.**

---

## Cómo evitar el error (regla práctica)
1. **Escoge una convención y mantenla.**  
   - Si usas las componentes del tensor $I_{ij}^{(\text{comp})}$, coloca **esas** directamente en la matriz (sin signos extra).  
   - Si usas los productos $P_{ij}=\int r_i r_j\,dm$ con la notación de ingeniería (muchos libros usan $I_{xy}$ para esto), entonces recuerda que la matriz lleva signos en las off-diagonales: $-P_{xy}$.

1. **Mejor aún:** trabaja con $Q_{ij}$ y la fórmula compacta
   $$I_{ij}=\mathrm{Tr}(Q)\delta_{ij}-Q_{ij}$$
   y entonces no hay posibilidad de malentendidos.

---

## Mapeo explícito (para que lo copies rápido)
- Si en tu libro aparece $$I_{xy}=-\int xy\,dm$$ entonces **usa** la matriz:
  $$
  \mathbf I=
  \begin{pmatrix}
  I_{xx} & I_{xy} & I_{xz}\\
  I_{xy} & I_{yy} & I_{yz}\\
  I_{xz} & I_{yz} & I_{zz}
  \end{pmatrix}
  $$
  (sin signos extra).

- Si en tu libro aparece $$I_{xy}=\int xy\,dm$$ entonces la matriz será:
  $$
  \mathbf I=
  \begin{pmatrix}
  I_{xx} & -I_{xy} & -I_{xz}\\
  -I_{xy} & I_{yy} & -I_{yz}\\
  -I_{xz} & -I_{yz} & I_{zz}
  \end{pmatrix}
  $$

---

## Ejemplo numérico rápido (compruébalo tú mismo)
Sea una distribución tal que $$\int xy\,dm = 2.$$
- Convención A (componentes del tensor): $$I_{xy}^{(\text{comp})}=-2.$$ Matriz: off-diagonal = \(-2\).
- Convención B (producto $P_{xy}$): $$P_{xy}=2.$$ Matriz (con signo en la matriz): off-diagonal $=-P_{xy}=-2.$

Ambas dan el mismo número \(-2\) para el elemento del tensor. No hay contradicción si no mezclas definiciones.

