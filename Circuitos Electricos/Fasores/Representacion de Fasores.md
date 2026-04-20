---
title: Representación de Fasores
tags:
  - fasores
  - electricidad
  - circuitos
draft: true
---

# Representación de Fasores

## 1) Señal Sinusoidal en el Tiempo

Se define una señal sinusoidal real como:

$$
\boxed{
x(t) = X_m \cos(\omega t + \phi)
}
$$

```tikz
\begin{document}
\begin{tikzpicture}[scale=2.5]
    \draw[->] (0,0) -- (6.5,0) node[right] {$t$};
    \draw[->] (0,-1.5) -- (0,1.5) node[above] {$x(t)$};
    
    \draw[domain=0:6.28, smooth, thick, blue] plot (\x, {1.2*cos(2*\x r + 0.5)});
    
    \draw[dashed] (0,1.2) -- (6.28,1.2) node[right] {$X_m$};
    \draw[dashed] (0,-1.2) -- (6.28,-1.2);
    
    \node at (3.14, -1.8) {$x(t) = X_m \cos(\omega t + \phi)$};
\end{tikzpicture}
\end{document}
```

**Donde:**

- $x(t)$ → valor instantáneo
- $X_m$ → valor máximo (amplitud)
- $\omega = 2\pi f$ → frecuencia angular [rad/s]
- $f$ → frecuencia [Hz]
- $\phi$ → fase inicial [rad]

---

## 2) Valor Eficaz (RMS)

Definición general:

$$
\boxed{
X_{ef} = \sqrt{\frac{1}{T} \int_0^T x^2(t)\, dt}
}
$$

Para una señal sinusoidal:

$$
X_{ef}
= \sqrt{\frac{1}{T} \int_0^T X_m^2 \cos^2(\omega t + \phi)\, dt}
$$

Factorizando:

$$
X_{ef}
= \sqrt{\frac{X_m^2}{T} \int_0^T \cos^2(\omega t + \phi)\, dt}
$$

Usando que:

$$
\frac{1}{T}\int_0^T \cos^2(\omega t + \phi)\, dt = \frac{1}{2}
$$

Se obtiene:

$$
\boxed{
X_{ef} = \frac{X_m}{\sqrt{2}}
}
$$

```tikz
\begin{document}
\begin{tikzpicture}[scale=2.5]
    \draw[->] (0,0) -- (6.5,0) node[right] {$t$};
    \draw[->] (0,-1.5) -- (0,1.5) node[above] {$x(t)$};
    
    \draw[domain=0:6.28, smooth, thick, blue] plot (\x, {1.2*cos(2*\x r)});
    
    \draw[dashed] (0,1.2) -- (6.28,1.2);
    \draw[dashed] (0,-1.2) -- (6.28,-1.2);
    
    \draw[thick, red] (0,0.85) -- (6.28,0.85) node[right] {$X_{ef} = X_m/\sqrt{2}$};
    \draw[thick, red] (0,-0.85) -- (6.28,-0.85);
    
    \draw[<->] (1,0) -- (1,0.85) node[midway, right] {$\frac{X_m}{\sqrt{2}}$};
\end{tikzpicture}
\end{document}
```
⚠ Nota: Para una señal sinusoidal pura, el valor eficaz es independiente de la fase $\phi$.

---

## 3) Representación Compleja (Señal Analítica)

Se define la señal compleja asociada como:

$$
\boxed{
x_c(t) = X_m e^{j(\omega t + \phi)}
}
$$
```tikz

\begin{document}
\begin{tikzpicture}[scale=2]
    % Plano complejo
    \draw[->] (-0.5,0) -- (3,0) node[right] {$\mathrm{Re}$};
    \draw[->] (0,-0.5) -- (0,2) node[above] {$\mathrm{Im}$};
    
    % Vector rotante
    \draw[->, thick, blue] (0,0) -- (2,1.2);
    \node at (1,0.8) [above, sloped] {$X_m e^{j\phi}$};
    
    % Proyecciones
    \draw[dashed] (2,0) -- (2,1.2);
    \draw[dashed] (0,1.2) -- (2,1.2);
    
    % Proyección en eje real
    \draw[->, thick, red] (0,0) -- (2,0);
    \node at (1,-0.2) {$x(t)$};
    
    % Ángulo
    \draw (0.8,0) arc (0:30:0.8);
    \node at (1.1,0.2) {$\phi$};
    
\end{tikzpicture}
\end{document}
```

Recordando que:

$$
x(t) = \mathrm{Re}\{x_c(t)\}
$$

Separando factores:

$$
x_c(t) = X_m e^{j\phi} \, e^{j\omega t}
$$

Aquí se observa claramente:

- $e^{j\omega t}$ → evolución temporal
- $X_m e^{j\phi}$ → información de amplitud y fase

---

## 4) Definición de Fasor

El **fasor** se define eliminando la dependencia temporal $e^{j\omega t}$ y trabajando en términos eficaces:

$$
\boxed{
\underline{X} = X_{ef} e^{j\phi}
}
$$
```tikz
\begin{document}
\begin{tikzpicture}[scale=2.5]
    % Plano complejo
    \draw[->] (-1.5,0) -- (2.5,0) node[right] {$\mathrm{Re}$};
    \draw[->] (0,-1.5) -- (0,2.5) node[above] {$\mathrm{Im}$};
    
    % Fasor (ángulo de 45°)
    \draw[->, thick, blue] (0,0) -- (1.41,1.41);
    \node at (0.8,0.9) [above, sloped] {$\underline{X}$};
    
    % Proyecciones
    \draw[dashed] (1.41,0) -- (1.41,1.41);
    \draw[dashed] (0,1.41) -- (1.41,1.41);
    
    % Ángulo
    \draw (0.7,0) arc (0:45:0.7);
    \node at (1.0,0.3) {$\phi$};
    
    % Magnitud
    \node at (0.7,0.7) {$X_{ef}$};
    
    \node at (1.5,2.2) {Fasor (sin tiempo)};
\end{tikzpicture}
\end{document}
```
Donde:

- $\underline{X}$ → fasor (dominio fasorial)
- $X_{ef}$ → magnitud eficaz
- $\phi$ → fase

---

## 5) Resumen Conceptual

| Dominio | Expresión | Contiene tiempo |
|----------|-----------|----------------|
| Tiempo real | $x(t)=X_m\cos(\omega t+\phi)$ | Sí |
| Complejo | $x_c(t)=X_m e^{j(\omega t+\phi)}$ | Sí |
| Fasorial | $\underline{X}=X_{ef} e^{j\phi}$ | No |

---
