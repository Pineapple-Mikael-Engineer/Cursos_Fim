---
title: Potencia en Régimen Sinusoidal y Dominio Fasorial
tags:
  - potencia
  - fasores
  - AC
  - circuitos
draft: true
---

# Potencia en Régimen Sinusoidal

En régimen sinusoidal permanente:

$$
v(t) = V_m \cos(\omega t)
$$

$$
i(t) = I_m \cos(\omega t - \theta)
$$

Donde:

- $\theta$ → ángulo de desfase entre voltaje y corriente
- Si $\theta > 0$ → corriente atrasada (carga inductiva)
- Si $\theta < 0$ → corriente adelantada (carga capacitiva)

---

# 1) Potencia Instantánea

La potencia instantánea es:

$$
\boxed{
p(t) = v(t)\, i(t)
}
$$

Multiplicando:

$$
p(t) =
V_m I_m
\cos(\omega t)
\cos(\omega t - \theta)
$$

Usando identidad trigonométrica:

$$
\cos A \cos B =
\frac{1}{2}
\left[
\cos(A-B) + \cos(A+B)
\right]
$$

Se obtiene:

$$
\boxed{
p(t) =
\frac{V_m I_m}{2}
\left[
\cos\theta +
\cos(2\omega t - \theta)
\right]
}
$$

🔎 Observación clave:

- Primer término → constante
- Segundo término → oscilante a frecuencia $2\omega$

---

# 2) Potencia Activa (Real)

Es el valor promedio de la potencia instantánea:

$$
\boxed{
P = \frac{V_m I_m}{2} \cos\theta
}
$$

Como:

$$
V_{ef} = \frac{V_m}{\sqrt{2}}
\quad
I_{ef} = \frac{I_m}{\sqrt{2}}
$$

Entonces:

$$
\boxed{
P = V_{ef} I_{ef} \cos\theta
}
$$

- Unidad: Watt (W)
- Representa energía realmente consumida

---

# 3) Potencia Reactiva

Se define como:

$$
\boxed{
Q = V_{ef} I_{ef} \sin\theta
}
$$

- Unidad: Volt–Ampere reactivo (VAR)
- Asociada al almacenamiento y devolución de energía
- No produce trabajo útil

Signo:

- $Q > 0$ → carga inductiva
- $Q < 0$ → carga capacitiva

---

# 4) Potencia Aparente

Se define como:

$$
\boxed{
S = V_{ef} I_{ef}
}
$$

Unidad: Volt–Ampere (VA)

---

# 5) Potencia Compleja

En dominio fasorial:

$$
\boxed{
\underline{S} =
\underline{V} \,
\underline{I}^{\,*}
}
$$

donde $^*$ indica conjugado complejo.

Desarrollando:

$$
\underline{S} =
P + jQ
$$

Forma polar:

$$
\underline{S} =
S e^{j\theta}
$$

Magnitud:

$$
|\underline{S}| = \sqrt{P^2 + Q^2}
$$

---

# 6) Triángulo de Potencias

```tikz
\begin{document}
\begin{tikzpicture}[scale=2.5]
    \draw[->] (0,0) -- (2,0) node[right] {$P$};
    \draw[->] (0,0) -- (0,1.5) node[above] {$Q$};

    \draw[thick, blue] (0,0) -- (1.8,0);
    \draw[thick, red] (1.8,0) -- (1.8,1.2);
    \draw[thick] (0,0) -- (1.8,1.2);

    \node at (0.9,-0.15) {$P$};
    \node at (2.0,0.6) {$Q$};
    \node at (1.1,0.8) {$S$};

    \draw (0.6,0) arc (0:34:0.6);
    \node at (0.75,0.25) {$\theta$};
\end{tikzpicture}
\end{document}
```

Relaciones:

$$
S^2 = P^2 + Q^2
$$

$$
\tan\theta = \frac{Q}{P}
$$

---

# 7) Relación con el Desfase

El ángulo $\theta$ es el mismo ángulo entre:

- $\underline{V}$
- $\underline{I}$

En el plano fasorial:

```tikz
\begin{document}
\begin{tikzpicture}[scale=2.5]
    \draw[->] (-0.5,0) -- (2,0) node[right] {$\mathrm{Re}$};
    \draw[->] (0,-0.5) -- (0,2) node[above] {$\mathrm{Im}$};

    % Voltaje
    \draw[->, thick, blue] (0,0) -- (1.6,0.8);
    \node at (1.5,0.9) {$\underline{V}$};

    % Corriente
    \draw[->, thick, red] (0,0) -- (1.8,0);
    \node at (1.8,-0.15) {$\underline{I}$};

    % Ángulo
    \draw (0.7,0) arc (0:27:0.7);
    \node at (0.8,0.25) {$\theta$};
\end{tikzpicture}
\end{document}
```

---

# 8) Factor de Potencia

$$
\boxed{
\text{fp} = \cos\theta
}
$$

- $fp = 1$ → puramente resistivo
- $0 < fp < 1$ → carga reactiva
- Bajo fp → mayor corriente para misma potencia activa

---

# Resumen Conceptual

| Magnitud | Expresión | Significado |
|----------|------------|-------------|
| $P$ | $V_{ef} I_{ef} \cos\theta$ | Potencia útil |
| $Q$ | $V_{ef} I_{ef} \sin\theta$ | Potencia reactiva |
| $S$ | $V_{ef} I_{ef}$ | Potencia aparente |
| $\underline{S}$ | $\underline{V}\underline{I}^*$ | Potencia compleja |

---

 > [!idea] IDEA CLAVE:
>
>El desfase $\theta$ controla completamente cómo se reparte la potencia entre:
>
> - Trabajo real ($P$)
> - Energía almacenada ($Q$)
>
> Sin desfase → no existe potencia reactiva.

---
