---
title: Elementos Activos y Pasivos en Notación Fasorial
tags:
  - fasores
  - impedancia
  - circuitos
  - AC
draft: true
---

# Elementos Activos y Pasivos en Dominio Fasorial

En régimen sinusoidal permanente, todos los elementos se analizan en el **dominio fasorial**, eliminando la dependencia temporal $e^{j\omega t}$.

Se trabaja con:

$$
\underline{V}, \quad \underline{I}
$$

y la relación fundamental:

$$
\boxed{
\underline{V} = Z \, \underline{I}
}
$$

donde $Z$ es la **impedancia compleja** del elemento.

---

# 1) Elementos Pasivos

---

## 🔹 Resistencia (R)

### Dominio temporal

$$
v(t) = R\, i(t)
$$

### Dominio fasorial

$$
\boxed{
\underline{V} = R \, \underline{I}
}
$$

### Impedancia

$$
\boxed{
Z_R = R
}
$$

- Número real
- No introduce desfase
- $\angle Z_R = 0^\circ$

```tikz
\begin{document}
\begin{tikzpicture}[scale=2]
    \draw[->] (-0.5,0) -- (2,0) node[right] {$\mathrm{Re}$};
    \draw[->] (0,-0.5) -- (0,1.5) node[above] {$\mathrm{Im}$};

    \draw[->, thick, blue] (0,0) -- (1.5,0);
    \node at (1.5,0.2) {$Z_R = R$};
\end{tikzpicture}
\end{document}
```

📌 Voltaje y corriente están en fase.

---

## 🔹 Inductor (L)

### Dominio temporal

$$
v(t) = L \frac{di(t)}{dt}
$$

Si:

$$
i(t) = I_m \cos(\omega t + \phi)
$$

Entonces en fasores:

$$
\boxed{
\underline{V} = j\omega L \, \underline{I}
}
$$

### Impedancia

$$
\boxed{
Z_L = j\omega L
}
$$

- Parte imaginaria positiva
- $\angle Z_L = +90^\circ$

```tikz
\begin{document}
\begin{tikzpicture}[scale=2]
    \draw[->] (-1,0) -- (1,0) node[right] {$\mathrm{Re}$};
    \draw[->] (0,-0.5) -- (0,2) node[above] {$\mathrm{Im}$};

    \draw[->, thick, blue] (0,0) -- (0,1.5);
    \node at (0.3,1.2) {$Z_L = j\omega L$};
\end{tikzpicture}
\end{document}
```

📌 El voltaje adelanta a la corriente en $90^\circ$.

---

## 🔹 Capacitor (C)

### Dominio temporal

$$
i(t) = C \frac{dv(t)}{dt}
$$

En dominio fasorial:

$$
\boxed{
\underline{V} = \frac{1}{j\omega C} \underline{I}
}
$$

### Impedancia

$$
\boxed{
Z_C = \frac{1}{j\omega C}
= -\frac{j}{\omega C}
}
$$

- Parte imaginaria negativa
- $\angle Z_C = -90^\circ$

```tikz
\begin{document}
\begin{tikzpicture}[scale=2]
    \draw[->] (-1,0) -- (1,0) node[right] {$\mathrm{Re}$};
    \draw[->] (0,-2) -- (0,0.5) node[above] {$\mathrm{Im}$};

    \draw[->, thick, blue] (0,0) -- (0,-1.5);
    \node at (0.5,-1.2) {$Z_C$};
\end{tikzpicture}
\end{document}
```

📌 La corriente adelanta al voltaje en $90^\circ$.

---

# 2) Elementos Activos

Los elementos activos pueden **entregar potencia** al circuito.

---

## 🔹 Fuente de Voltaje

### Temporal

$$
v(t) = V_m \cos(\omega t + \phi)
$$

### Fasorial

$$
\boxed{
\underline{V} = V_{ef} e^{j\phi}
}
$$

- Magnitud: $V_{ef}$
- Fase: $\phi$

---

## 🔹 Fuente de Corriente

### Temporal

$$
i(t) = I_m \cos(\omega t + \phi)
$$

### Fasorial

$$
\boxed{
\underline{I} = I_{ef} e^{j\phi}
}
$$

---

# 3) Impedancia General

Para un circuito RLC serie:

$$
\boxed{
Z = R + j\omega L + \frac{1}{j\omega C}
}
$$

Separando parte real e imaginaria:

$$
Z = R + j\left(\omega L - \frac{1}{\omega C}\right)
$$

Forma polar:

$$
Z = |Z| e^{j\theta}
$$

donde:

$$
|Z| = \sqrt{R^2 + \left(\omega L - \frac{1}{\omega C}\right)^2}
$$

$$
\theta = \tan^{-1}\left(
\frac{\omega L - \frac{1}{\omega C}}{R}
\right)
$$

---

# 4) Resumen Conceptual

| Elemento | Impedancia | Desfase |
|-----------|------------|----------|
| Resistencia | $R$ | $0^\circ$ |
| Inductor | $j\omega L$ | $+90^\circ$ |
| Capacitor | $\frac{1}{j\omega C}$ | $-90^\circ$ |

---

⚡ Idea clave:

En dominio fasorial:

- Derivar → multiplicar por $j\omega$
- Integrar → dividir entre $j\omega$
- Resolver circuito → álgebra compleja normal

---
