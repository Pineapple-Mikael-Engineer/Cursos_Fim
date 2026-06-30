---
title: Potencial Vector
order: 4
tags:
  - electromagnetismo
  - teoria
  - magnetostatica
draft: false
aliases:
  - Potencial vector
  - Potencial vectorial magnético
---

# Potencial Vector $\vec B=\nabla\times\vec A,\quad \nabla^2\vec A=-\mu_0\vec J$

> [!definicion] Potencial vector magnético
> En magnetostática, como el campo magnético cumple $\nabla\cdot\vec B=0$ en todo punto, **siempre** existe un campo vectorial $\vec A(\vec r)$, llamado **potencial vector**, tal que
> $$\boxed{\;\vec B=\nabla\times\vec A\;}$$
> En el **gauge de Coulomb** ($\nabla\cdot\vec A=0$) este potencial obedece la **ecuación de Poisson vectorial**
> $$\boxed{\;\nabla^2\vec A=-\mu_0\,\vec J\;}$$
> cuya solución, para corrientes localizadas, es
> $$\vec A(\vec r)=\frac{\mu_0}{4\pi}\int\frac{\vec J(\vec r\,')}{\mathscr r}\;d^3r',\qquad \mathscr r=|\vec r-\vec r\,'|.$$

> [!info] Ubicación y relaciones
> Esta nota pertenece a la sección [[3 Magnetostatica/index | Magnetostática]]. Es **hermana** de [[Ley de Ampere]] y [[Ley de Biot-Savart]], y se apoya fuertemente en las [[Identidades Vectoriales]] (en particular $\nabla\cdot(\nabla\times\vec A)=0$ y la identidad BAC–CAB del rotacional doble).
>
> El potencial vector $\vec A$ es el análogo magnético del [[Potencial Electrostatico | potencial escalar]] $V$: lo que $V$ es a $\rho$, lo es $\vec A$ a $\vec J$. La referencia base es **Griffiths, *Introduction to Electrodynamics*, capítulo 5**.

---

## Existencia del potencial vector

> [!teorema] Existencia de $\vec A$
> Si un campo vectorial $\vec B$ satisface $\nabla\cdot\vec B=0$ en todo el espacio, entonces existe un campo vectorial $\vec A$ tal que $\vec B=\nabla\times\vec A$.

> [!demostracion] El divergente de un rotacional es nulo
> **Paso 1 —** Por las [[Identidades Vectoriales]], el divergente de cualquier rotacional se anula idénticamente:
> $$\nabla\cdot(\nabla\times\vec A)=0\qquad \text{para todo }\vec A.$$
> En componentes, $\partial_i\,\varepsilon_{ijk}\,\partial_j A_k=\varepsilon_{ijk}\,\partial_i\partial_j A_k=0$, porque $\varepsilon_{ijk}$ es antisimétrico en $(i,j)$ mientras que $\partial_i\partial_j$ es simétrico.
>
> **Paso 2 —** La ley de Gauss magnética (ausencia de monopolos) afirma que **siempre**
> $$\nabla\cdot\vec B=0.$$
>
> **Paso 3 —** Ambas condiciones son **compatibles**: postular $\vec B=\nabla\times\vec A$ garantiza automáticamente $\nabla\cdot\vec B=0$. Recíprocamente, la teoría de campos asegura que, si $\nabla\cdot\vec B=0$, la ecuación $\nabla\times\vec A=\vec B$ admite solución (puede construirse explícitamente, p. ej. integrando a lo largo de rayos desde el origen). Por tanto $\vec A$ existe. $\blacksquare$

---

## Libertad de gauge

> [!proposicion] Invariancia de gauge y gauge de Coulomb
> El potencial vector **no es único**: la transformación
> $$\vec A\;\longrightarrow\;\vec A\,'=\vec A+\nabla\lambda$$
> con $\lambda(\vec r)$ una función escalar arbitraria, deja $\vec B$ **invariante**. Esta libertad permite **imponer** la condición adicional
> $$\nabla\cdot\vec A=0\qquad(\textbf{gauge de Coulomb}).$$

> [!demostracion] El campo es invariante y el gauge de Coulomb siempre es alcanzable
> **Paso 1 (invariancia) —** Calculemos el campo asociado a $\vec A\,'$:
> $$\nabla\times\vec A\,'=\nabla\times\bigl(\vec A+\nabla\lambda\bigr)=\nabla\times\vec A+\nabla\times(\nabla\lambda).$$
> Por las [[Identidades Vectoriales]], el rotacional de un gradiente se anula, $\nabla\times(\nabla\lambda)=0$, de modo que
> $$\nabla\times\vec A\,'=\nabla\times\vec A=\vec B.$$
> El campo físico no cambia: $\vec A$ y $\vec A\,'$ describen el mismo $\vec B$.
>
> **Paso 2 (se puede elegir $\nabla\cdot\vec A=0$) —** Supongamos un potencial cualquiera $\vec A$ con $\nabla\cdot\vec A=f(\vec r)\neq0$. Buscamos $\lambda$ tal que el nuevo potencial $\vec A\,'=\vec A+\nabla\lambda$ tenga divergencia nula:
> $$\nabla\cdot\vec A\,'=\nabla\cdot\vec A+\nabla\cdot(\nabla\lambda)=f+\nabla^2\lambda.$$
>
> **Paso 3 —** Imponer $\nabla\cdot\vec A\,'=0$ equivale a resolver la **ecuación de Poisson escalar**
> $$\nabla^2\lambda=-\,\nabla\cdot\vec A=-f.$$
> Esta ecuación **siempre** tiene solución (es formalmente idéntica a la electrostática $\nabla^2 V=-\rho/\varepsilon_0$, con solución $\lambda=\frac{1}{4\pi}\int\frac{f(\vec r\,')}{\mathscr r}\,d^3r'$ para fuentes localizadas).
>
> **Paso 4 —** Por tanto, **dado cualquier** $\vec A$ podemos fabricar un $\lambda$ que lo lleve al gauge de Coulomb sin alterar $\vec B$. La elección $\nabla\cdot\vec A=0$ es siempre legítima. $\blacksquare$

---

## Ecuación de Poisson vectorial

> [!teorema] De Ampère a Poisson
> En el gauge de Coulomb, la ley de [[Ley de Ampere | Ampère]] diferencial $\nabla\times\vec B=\mu_0\vec J$ se transforma en tres ecuaciones de Poisson, una por componente:
> $$\nabla^2\vec A=-\mu_0\,\vec J.$$

> [!demostracion] Reducción mediante la identidad BAC–CAB
> **Paso 1 —** Partimos de la forma diferencial de la [[Ley de Ampere | ley de Ampère]]:
> $$\nabla\times\vec B=\mu_0\,\vec J.$$
>
> **Paso 2 —** Sustituimos $\vec B=\nabla\times\vec A$:
> $$\nabla\times(\nabla\times\vec A)=\mu_0\,\vec J.$$
>
> **Paso 3 —** Aplicamos la identidad del rotacional doble (BAC–CAB para operadores), de las [[Identidades Vectoriales]]:
> $$\nabla\times(\nabla\times\vec A)=\nabla(\nabla\cdot\vec A)-\nabla^2\vec A.$$
> Así, la ecuación queda
> $$\nabla(\nabla\cdot\vec A)-\nabla^2\vec A=\mu_0\,\vec J.$$
>
> **Paso 4 —** Imponemos el **gauge de Coulomb** $\nabla\cdot\vec A=0$ (siempre posible, por la proposición anterior). El primer término se anula:
> $$-\nabla^2\vec A=\mu_0\,\vec J\quad\Longrightarrow\quad \boxed{\;\nabla^2\vec A=-\mu_0\,\vec J\;}$$
>
> **Paso 5 —** En coordenadas cartesianas el laplaciano vectorial actúa componente a componente, $(\nabla^2\vec A)_i=\nabla^2 A_i$, de modo que la ecuación se desdobla en **tres ecuaciones de Poisson escalares** independientes:
> $$\nabla^2 A_x=-\mu_0 J_x,\qquad \nabla^2 A_y=-\mu_0 J_y,\qquad \nabla^2 A_z=-\mu_0 J_z.\qquad\blacksquare$$

> [!corolario] Solución por analogía con la electrostática
> Cada componente es formalmente idéntica a la ecuación electrostática $\nabla^2 V=-\rho/\varepsilon_0$, cuya solución conocida es $V=\frac{1}{4\pi\varepsilon_0}\int\frac{\rho(\vec r\,')}{\mathscr r}\,d^3r'$. Reemplazando $V\to A_i$, $\rho/\varepsilon_0\to\mu_0 J_i$ y recomponiendo el vector:
> $$\boxed{\;\vec A(\vec r)=\frac{\mu_0}{4\pi}\int\frac{\vec J(\vec r\,')}{\mathscr r}\;d^3r'\;}$$
> La correspondencia es **exacta**: $\;V\leftrightarrow\vec A\;$ y $\;\rho\leftrightarrow\vec J\;$ a nivel de la ecuación de Poisson. (Para corrientes filiformes, $\vec J\,d^3r'\to I\,d\vec l\,'$ y se recupera el integrando de [[Ley de Biot-Savart | Biot–Savart]].)

![[potencial_vector.svg|420]]
> **Figura.** El potencial vector $\vec A$ **circula alrededor del flujo** de $\vec B$ (líneas concéntricas en torno al tubo de campo), del mismo modo que $\vec B$ circula alrededor de la corriente $\vec J$. La relación $\vec B=\nabla\times\vec A$ es geométricamente análoga a $\vec B=\mu_0$(rotacional de la circulación de la corriente).

---

## Ejemplo

> [!ejemplo] Potencial vector de un solenoide infinito
> Un solenoide infinito de radio $R$, con $n$ vueltas por unidad de longitud y corriente $I$, está orientado según $\hat z$. Su campo magnético (ver [[Ley de Ampere | Ampère]]) es
> $$\vec B=\begin{cases}\mu_0\,n\,I\,\hat z, & s<R\quad(\text{dentro}),\\[2pt]\vec 0, & s>R\quad(\text{fuera}).\end{cases}$$
> Hallar el potencial vector $\vec A(s)$ dentro y fuera, en el gauge de Coulomb.

> [!solucion] Uso del flujo y verificación por el rotacional
> **Paso 1 (simetría) —** Por la simetría cilíndrica el potencial es azimutal y depende solo de $s$: $\vec A=A_\varphi(s)\,\hat\varphi$. Esta forma cumple $\nabla\cdot\vec A=0$ automáticamente (gauge de Coulomb satisfecho).
>
> **Paso 2 (relación integral) —** Como $\vec B=\nabla\times\vec A$, integrando sobre un disco de radio $s$ y usando el teorema de Stokes:
> $$\oint_{\mathcal C}\vec A\cdot d\vec l=\int_{\mathcal S}(\nabla\times\vec A)\cdot d\vec a=\int_{\mathcal S}\vec B\cdot d\vec a=\Phi_B(s).$$
> El lado izquierdo, con $\vec A=A_\varphi\,\hat\varphi$ y circunferencia de radio $s$, vale $A_\varphi(s)\,(2\pi s)$. Por tanto
> $$A_\varphi(s)=\frac{\Phi_B(s)}{2\pi s}.$$
>
> **Paso 3 (dentro, $s<R$) —** El flujo encerrado es $\Phi_B=\mu_0 n I\,(\pi s^2)$, luego
> $$\boxed{\;\vec A=\frac{\mu_0\,n\,I}{2}\,s\;\hat\varphi\;}\qquad(s<R).$$
>
> **Paso 4 (fuera, $s>R$) —** Todo el flujo está confinado en $s<R$, así que para $s>R$ el flujo encerrado es constante, $\Phi_B=\mu_0 n I\,(\pi R^2)$, y
> $$\boxed{\;\vec A=\frac{\mu_0\,n\,I\,R^2}{2\,s}\;\hat\varphi\;}\qquad(s>R).$$
> **Aunque $\vec B=\vec 0$ fuera, el potencial vector $\vec A\neq\vec 0$.**
>
> **Paso 5 (verificación $\vec B=\nabla\times\vec A$) —** En coordenadas cilíndricas, para $\vec A=A_\varphi(s)\,\hat\varphi$,
> $$\nabla\times\vec A=\frac{1}{s}\frac{\partial\bigl(s\,A_\varphi\bigr)}{\partial s}\,\hat z.$$
> - Dentro: $s\,A_\varphi=\frac{\mu_0 n I}{2}\,s^2\Rightarrow \frac{1}{s}\frac{\partial}{\partial s}\!\left(\frac{\mu_0 n I}{2}s^2\right)=\mu_0 n I$. Luego $\vec B=\mu_0 n I\,\hat z$. ✓
> - Fuera: $s\,A_\varphi=\frac{\mu_0 n I R^2}{2}$ es constante $\Rightarrow \frac{\partial}{\partial s}=0$. Luego $\vec B=\vec 0$. ✓
>
> Ambos resultados reproducen el campo de partida. $\blacksquare$

> [!info] Semilla del efecto Aharonov–Bohm
> Que $\vec A\neq\vec 0$ en una región donde $\vec B=\vec 0$ no es un mero artificio matemático: en mecánica cuántica una partícula cargada que viaja por fuera del solenoide adquiere una fase proporcional a $\oint\vec A\cdot d\vec l=\Phi_B$, produciendo interferencia observable. Es el **efecto Aharonov–Bohm**, donde $\vec A$ adquiere significado físico más allá de la magnetostática clásica.

---

## En qué consiste

La estrategia del potencial vector reproduce, en magnetostática, el éxito del potencial escalar en electrostática: **convertir un problema de campo en un problema de fuentes**.

- En electrostática, $\nabla\times\vec E=0$ permite escribir $\vec E=-\nabla V$, y la ley de Gauss se vuelve $\nabla^2 V=-\rho/\varepsilon_0$. Resolvemos **un** campo escalar $V$ y luego derivamos $\vec E$.
- En magnetostática, $\nabla\cdot\vec B=0$ permite escribir $\vec B=\nabla\times\vec A$, y la ley de Ampère se vuelve $\nabla^2\vec A=-\mu_0\vec J$. Resolvemos el campo vectorial $\vec A$ (tres Poisson) y luego derivamos $\vec B=\nabla\times\vec A$.

La ventaja es doble: (1) trabajar con $\vec A$ suele ser **más simple** que integrar [[Ley de Biot-Savart | Biot–Savart]] directamente, porque el integrando $\vec J/\mathscr r$ apunta en la dirección de la corriente y no involucra el producto vectorial $\hat{\mathscr r}$; (2) la analogía con la electrostática nos **regala** la solución, copiando la del potencial escalar.

El precio es la **libertad de gauge**: $\vec A$ no es único. Fijamos esa ambigüedad imponiendo $\nabla\cdot\vec A=0$ (Coulomb), lo que limpia la ecuación dejándola en forma de Poisson pura. La condición de gauge **no** tiene contenido físico: solo selecciona un representante cómodo dentro de la clase de potenciales que producen el mismo $\vec B$.

> [!warning] El potencial vector no es único; solo $\vec B$ es físico
> En magnetostática clásica, **únicamente $\vec B=\nabla\times\vec A$ es observable**; el propio $\vec A$ depende del gauge elegido ($\vec A\to\vec A+\nabla\lambda$ no cambia ninguna predicción clásica). No debe interpretarse $\vec A$ como una magnitud medible punto a punto en este contexto. Eso sí, la **analogía** $V\leftrightarrow\vec A$, $\rho\leftrightarrow\vec J$ es **exacta** a nivel de la ecuación de Poisson y de su solución integral. (En cuántica, la circulación $\oint\vec A\cdot d\vec l$ sí adquiere significado físico vía Aharonov–Bohm.)

---

## Resumen

> [!resumen] Potencial vector magnético
>
> | Concepto | Expresión | Comentario |
> |---|---|---|
> | Definición | $\vec B=\nabla\times\vec A$ | garantiza $\nabla\cdot\vec B=0$ |
> | Existencia | $\nabla\cdot\vec B=0\Rightarrow\exists\,\vec A$ | vía $\nabla\cdot(\nabla\times\vec A)=0$ |
> | Libertad de gauge | $\vec A\to\vec A+\nabla\lambda$ | $\vec B$ invariante ($\nabla\times\nabla\lambda=0$) |
> | Gauge de Coulomb | $\nabla\cdot\vec A=0$ | siempre alcanzable: $\nabla^2\lambda=-\nabla\cdot\vec A$ |
> | Ecuación de campo | $\nabla^2\vec A=-\mu_0\vec J$ | tres Poisson (una por componente) |
> | Solución | $\vec A=\dfrac{\mu_0}{4\pi}\displaystyle\int\dfrac{\vec J(\vec r\,')}{\mathscr r}\,d^3r'$ | $\mathscr r=\|\vec r-\vec r\,'\|$ |
> | Analogía | $V\leftrightarrow\vec A,\;\;\rho\leftrightarrow\vec J$ | exacta en la ecuación de Poisson |
>
> **Corolario.** Toda la magnetostática de corrientes localizadas se reduce a resolver tres ecuaciones de Poisson escalares, idénticas a la electrostática: el campo magnético se obtiene como $\vec B=\nabla\times\vec A$ del potencial así calculado. El solenoide muestra que $\vec A$ puede ser no nulo donde $\vec B=\vec 0$, anticipando el efecto Aharonov–Bohm.

> [!referencia] Fuentes y notas relacionadas
> - **Griffiths**, *Introduction to Electrodynamics*, capítulo 5 (Magnetostática) — sección del potencial vector.
> - Notas hermanas: [[Ley de Ampere]], [[Ley de Biot-Savart]].
> - Herramienta: [[Identidades Vectoriales]] ($\nabla\cdot\nabla\times=0$, $\nabla\times\nabla=0$, BAC–CAB del rotacional doble).
> - Índice: [[3 Magnetostatica/index | Magnetostática]].
