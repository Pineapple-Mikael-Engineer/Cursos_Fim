---
title: Función de Mittag-Leffler
order: 6
tags:
  - ecuaciones
  - difero-integrales
  - teoria
  - calculo-fraccionario
  - mittag-leffler
draft: false
aliases:
  - función de Mittag-Leffler
  - exponencial fraccionaria
  - Mittag-Leffler function
---

# Función de Mittag-Leffler $E_\alpha$

> [!definicion]
> La **función de Mittag-Leffler** es la "exponencial" del cálculo fraccionario:
> $$E_\alpha(z)=\sum_{k=0}^{\infty}\frac{z^{k}}{\Gamma(\alpha k+1)},\qquad E_{\alpha,\beta}(z)=\sum_{k=0}^{\infty}\frac{z^{k}}{\Gamma(\alpha k+\beta)}\ \text{(dos parámetros)}.$$
> Para $\alpha=1$ recupera la exponencial, $E_1(z)=e^{z}$ (porque $\Gamma(k+1)=k!$). Es la **autofunción de la derivada fraccionaria**: igual que $e^{\lambda t}$ resuelve $\varphi'=\lambda\varphi$, $E_\alpha(\lambda t^\alpha)$ resuelve la ecuación fraccionaria $D^{\alpha}\varphi=\lambda\varphi$.

> [!info]
> El centro del [[Calculo Fraccionario/index| cálculo fraccionario]]: aparece en la solución de toda [[Ecuaciones Diferenciales Fraccionarias| ecuación diferencial fraccionaria]] lineal, igual que la exponencial en las [[Coeficientes Constantes Homogenea| EDO de coeficientes constantes]]. Su transformada de Laplace es la pieza que las resuelve ([[Laplace de Derivadas Fraccionarias| Laplace fraccional]]).

---

## Ejemplo

> [!ejemplo] Relajación fraccionaria: entre estirada y ley de potencias
> ![[mittag_leffler.svg|480]]
>
> La relajación $E_\alpha(-t^{\alpha})$ (solución de $D^{\alpha}\varphi=-\varphi$, $\varphi(0)=1$) **interpola** entre dos comportamientos según $\alpha$:
> - en $\alpha=1$ es la exponencial pura $e^{-t}$;
> - para $0<\alpha<1$ decae como una **exponencial estirada** al inicio y como una **ley de potencias** $E_\alpha(-t^\alpha)\sim\dfrac{t^{-\alpha}}{\Gamma(1-\alpha)}$ para $t$ grande — una **cola larga** (relajación lenta) que la exponencial nunca tiene.
>
> Esa cola de ley de potencias es la firma de los sistemas con **memoria**: la materia viscoelástica y los dieléctricos relajan así (ley de Cole-Cole), no exponencialmente.

---

## En qué consiste

> [!teorema] Mittag-Leffler resuelve la ecuación fraccionaria de relajación
> El problema $D^{\alpha}_{C}\varphi(t)=\lambda\,\varphi(t)$, $\varphi(0)=1$ (con $0<\alpha\le1$, derivada de [[Derivada de Caputo| Caputo]]) tiene solución
> $$\varphi(t)=E_\alpha(\lambda\,t^{\alpha}).$$

> [!demostracion] Por la serie (término a término)
> **Paso 1 — proponer la serie.** Sea $\varphi(t)=\sum_{k\ge0}\dfrac{(\lambda t^{\alpha})^{k}}{\Gamma(\alpha k+1)}=\sum_{k\ge0}\dfrac{\lambda^{k}t^{\alpha k}}{\Gamma(\alpha k+1)}$. **Paso 2 — aplicar $D^{\alpha}$ a cada potencia.** Por la regla $D^{\alpha}t^{\mu}=\dfrac{\Gamma(\mu+1)}{\Gamma(\mu+1-\alpha)}t^{\mu-\alpha}$ con $\mu=\alpha k$:
> $$D^{\alpha}\frac{\lambda^{k}t^{\alpha k}}{\Gamma(\alpha k+1)}=\frac{\lambda^{k}}{\Gamma(\alpha k+1)}\cdot\frac{\Gamma(\alpha k+1)}{\Gamma(\alpha k+1-\alpha)}t^{\alpha k-\alpha}=\frac{\lambda^{k}t^{\alpha(k-1)}}{\Gamma(\alpha(k-1)+1)}.$$
> **Paso 3 — reindexar.** La suma sobre $k\ge1$ (el término $k=0$ es constante y Caputo lo anula) es, con $j=k-1$, $\lambda\sum_{j\ge0}\dfrac{\lambda^{j}t^{\alpha j}}{\Gamma(\alpha j+1)}=\lambda\,\varphi(t)$. Luego $D^{\alpha}\varphi=\lambda\varphi$. $\blacksquare$

> [!proposicion] Transformada de Laplace (la herramienta clave)
> $$\mathcal{L}\big\{t^{\beta-1}E_{\alpha,\beta}(\lambda t^{\alpha})\big\}=\frac{s^{\alpha-\beta}}{s^{\alpha}-\lambda},\qquad\text{en particular}\quad \mathcal{L}\{E_\alpha(\lambda t^\alpha)\}=\frac{s^{\alpha-1}}{s^{\alpha}-\lambda}.$$
> Antitransformar $\dfrac{s^{\alpha-1}}{s^{\alpha}-\lambda}$ es lo que produce $E_\alpha$ al resolver EDF por [[Laplace de Derivadas Fraccionarias| Laplace]].

> [!info] Casos especiales
> | Función | Es |
> |---|---|
> | $E_1(z)$ | $e^{z}$ |
> | $E_2(-z^2)$ | $\cos z$ |
> | $E_2(z^2)$ | $\cosh z$ |
> | $E_{1/2}(z)$ | $e^{z^2}\operatorname{erfc}(-z)$ |
> Así $E_\alpha$ **unifica** exponenciales, trigonométricas e hiperbólicas como casos de un parámetro.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Definición | $E_\alpha(z)=\sum_k z^k/\Gamma(\alpha k+1)$ |
> | Caso $\alpha=1$ | $e^{z}$ |
> | Autofunción | $D^{\alpha}E_\alpha(\lambda t^\alpha)=\lambda E_\alpha(\lambda t^\alpha)$ |
> | Relajación $E_\alpha(-t^\alpha)$ | cola de ley de potencias $\sim t^{-\alpha}$ |
> | Laplace | $\mathcal{L}\{E_\alpha(\lambda t^\alpha)\}=s^{\alpha-1}/(s^\alpha-\lambda)$ |

> [!corolario]
> Mittag-Leffler es a las ecuaciones fraccionarias lo que la exponencial a las ordinarias: la función propia del operador. Su decaimiento de **ley de potencias** (no exponencial) explica por qué los sistemas con memoria relajan tan despacio —la huella matemática de "no olvidar el pasado"—.

> [!referencia]
> - La ecuación que resuelve: [[Ecuaciones Diferenciales Fraccionarias]].
> - La herramienta para obtenerla: [[Laplace de Derivadas Fraccionarias]].
> - El análogo entero: [[Coeficientes Constantes Homogenea]].
