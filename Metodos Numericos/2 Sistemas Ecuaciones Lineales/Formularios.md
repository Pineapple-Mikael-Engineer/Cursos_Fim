---
title: Formulario — Sistemas de Ecuaciones Lineales
order: 99
tags:
  - metodos-numericos
  - formulario
  - sistemas-lineales
draft: false
aliases:
  - formulario sistemas lineales
  - formulas sistemas de ecuaciones lineales
---

# Formulario — Sistemas de Ecuaciones Lineales

## Métodos directos — Pivoteo y estabilidad

**Multiplicador de eliminación.** $a_{ij}^{(k+1)} = a_{ij}^{(k)} - m_{ik}\,a_{kj}^{(k)}$, con $m_{ik} = a_{ik}/a_{kk}$.

**Pivoteo parcial.** Selección del pivote en la columna $k$:
$$|a_{p,k}| = \max_{i \geq k} |a_{i,k}|$$

**Pivoteo total.** Selección en toda la submatriz activa:
$$|a_{p,q}| = \max_{i \geq k,\, j \geq k} |a_{i,j}|$$

**Multiplicadores acotados por pivoteo.**
$$|m_{i,k}| \leq 1$$

**Factor de crecimiento.** $\rho$ mide el crecimiento de elementos durante la eliminación:
$$\rho = \frac{\max_{i,j,k} |a_{i,j}^{(k)}|}{\max_{i,j} |a_{i,j}|}$$

**Cotas del factor de crecimiento.**
$$\text{parcial: } \rho \leq 2^{n-1}, \qquad \text{total: } \rho \leq n^{1/2}\big[2\cdot 3^{1/2}\cdots n^{1/(n-1)}\big]^{1/2}$$

**Error hacia atrás (Wilkinson).** $\tilde L,\tilde U$ factores calculados:
$$\tilde L\tilde U = A + \Delta A, \qquad \|\Delta A\|_\infty \leq \rho\, u\, \|A\|_\infty$$

**Factorizaciones con permutación.** $PA = LU$ (parcial); $PAQ = LU$ (total); $PAP^T = LDL^T$ (simétrica indefinida); $A = LL^T$ (Cholesky).

---

## Métodos directos — Conteo de operaciones y complejidad

**Eliminación (fase de eliminación) de $A$.**
$$\text{divisiones: } \sum_{k=1}^{n-1}(n-k) = \frac{n(n-1)}{2} \approx \frac{n^2}{2}$$
$$\text{multiplicaciones/restas: } \sum_{k=1}^{n-1}(n-k)^2 = \frac{(n-1)n(2n-1)}{6} \approx \frac{n^3}{3}$$

**Sustitución regresiva.** $x_i = \dfrac{b_i - \sum_{j=i+1}^{n} a_{ij} x_j}{a_{ii}}$; costo $\approx n^2$ FLOPs.

**Complejidad total de eliminación Gaussiana.**
$$\text{FLOPs} = \frac{2n^3}{3} + \frac{3n^2}{2} + O(n) \sim \frac{2n^3}{3}$$

**Costos por método (orden dominante).** Gauss/LU $\tfrac{2}{3}n^3$; Cholesky $\tfrac{1}{3}n^3$; QR-Householder $\tfrac{4}{3}n^3$; QR-Gram-Schmidt $2n^3$; SVD $\approx 20n^3$; inversa explícita $n^3$.

**Resolución de $m$ sistemas.** Gauss repetido $m\cdot\tfrac{2}{3}n^3$; LU + $m$ sustituciones $\tfrac{2}{3}n^3 + m\,n^2$.

**Complejidad por estructura.** Tridiagonal $O(n)$; banda (ancho $b$) $O(nb^2)$; Hessenberg $O(n^2)$; triangular $O(n^2)$; dispersa $O(n^{1.5})$–$O(n^2)$.

**Algoritmo de Thomas (tridiagonal).** Resuelve $Ax=d$ en $8n$ FLOPs, $O(n)$.

---

## Métodos directos — Acumulación del error de redondeo en Gauss

**Modelo de Wilkinson (error local).** Para $\circ \in \{+,-,\times,\div\}$ con unidad de redondeo $u$:
$$\text{fl}(x \circ y) = (x \circ y)(1 + \delta), \qquad |\delta| \leq u$$

**Actualización en aritmética finita.**
$$\tilde a_{ij}^{(k+1)} = \big(\tilde a_{ij}^{(k)} - \tilde m_{ik}\,\tilde a_{kj}^{(k)}(1+\delta_1)\big)(1+\delta_2), \qquad |\delta_1|,|\delta_2| \leq u$$

**Cota de error hacia atrás.** $\|\Delta A\|_\infty \leq \rho\, n\, u\, \|A\|_\infty$ con $\tilde L\tilde U = A + \Delta A$.

**Error hacia adelante.**
$$\frac{\|\tilde x - x\|_\infty}{\|x\|_\infty} \leq \frac{\rho\, n\, u\, \kappa_\infty(A)}{1 - \rho\, n\, u\, \kappa_\infty(A)}$$

**Pérdida de dígitos (estimación).** $\approx \log_{10}(\rho\, n\, \kappa_\infty(A))$.

**Error en sustitución regresiva.** $(U + \Delta U)\tilde x = c$, con $\|\Delta U\|_\infty \leq n\,u\,\|U\|_\infty + O(u^2)$.

**Refinamiento iterativo.** $r^{(k)} = b - A x^{(k)}$; resolver $A\,\Delta x^{(k)} = r^{(k)}$; $x^{(k+1)} = x^{(k)} + \Delta x^{(k)}$; costo $O(n^2)$ por iteración.

---

## Métodos directos — Factorización LU: existencia y unicidad

**Factorización LU.** $A = LU$; $L$ triangular inferior unitaria ($\ell_{ii}=1$), $U$ triangular superior.

**Menor principal líder de orden $k$.** $\Delta_k = \det(A_{1:k,\,1:k})$, con $\Delta_0 = 1$.

**Existencia (condición).** $A$ no singular admite $A=LU$ sin pivoteo $\iff \Delta_k \neq 0$ para $k=1,\dots,n-1$.

**Menores y pivotes.**
$$\Delta_k = \prod_{i=1}^{k} u_{ii}, \qquad u_{kk} = \frac{\Delta_k}{\Delta_{k-1}}$$

**Unicidad.** Si $A$ no singular admite $A=LU$ ($L$ unitaria), es única (de $L_2^{-1}L_1 = U_2 U_1^{-1} = I$).

**Diagonal dominante estricta por filas (condición suficiente).** $|a_{ii}| > \sum_{j\neq i}|a_{ij}|,\ \forall i$.

---

## Métodos directos — Variantes Doolittle y Crout

**Doolittle** ($L$ unitaria). Para $k=1,\dots,n$:
$$u_{kj} = a_{kj} - \sum_{p=1}^{k-1}\ell_{kp}u_{pj} \quad (j\geq k), \qquad \ell_{ik} = \frac{1}{u_{kk}}\Big(a_{ik} - \sum_{p=1}^{k-1}\ell_{ip}u_{pk}\Big)\quad (i>k)$$

**Crout** ($U$ unitaria, $u_{ii}=1$). Para $k=1,\dots,n$:
$$\ell_{ik} = a_{ik} - \sum_{p=1}^{k-1}\ell_{ip}u_{pk} \quad (i\geq k), \qquad u_{kj} = \frac{1}{\ell_{kk}}\Big(a_{kj} - \sum_{p=1}^{k-1}\ell_{kp}u_{pj}\Big)\quad (j>k)$$

---

## Métodos directos — Factorización de Cholesky

**Cholesky.** $A = LL^T$ con $A$ simétrica definida positiva (SDP) y $\ell_{ii} > 0$.

**Definición positiva.** $A = A^T$ y $x^T A x > 0$ para todo $x \neq 0$; equivale a $\lambda_i > 0$ o $\Delta_k > 0$ (Sylvester).

**Algoritmo de Cholesky (por columnas).** Para $k=1,\dots,n$:
$$\ell_{kk} = \sqrt{a_{kk} - \sum_{p=1}^{k-1}\ell_{kp}^2}, \qquad \ell_{ik} = \frac{1}{\ell_{kk}}\Big(a_{ik} - \sum_{p=1}^{k-1}\ell_{ip}\ell_{kp}\Big)\quad (i>k)$$

**Costo.** $\approx \tfrac{1}{3}n^3$ FLOPs (mitad de LU); estable sin pivoteo, $\rho \leq 1$.

**Error hacia atrás.** $\tilde L\tilde L^T = A + \Delta A$, con $\|\Delta A\|_2 \leq c_n\, u\, \|A\|_2$.

**Variante $LDL^T$** ($L$ unitaria, $D$ diagonal). Para $k=1,\dots,n$:
$$d_{kk} = a_{kk} - \sum_{p=1}^{k-1}\ell_{kp}^2 d_{pp}, \qquad \ell_{ik} = \frac{1}{d_{kk}}\Big(a_{ik} - \sum_{p=1}^{k-1}\ell_{ip}\ell_{kp}d_{pp}\Big)\quad (i>k)$$

**Pivoteo simétrico (Bunch-Kaufman).** $PAP^T = LDL^T$, $D$ diagonal por bloques $1\times1$ y $2\times2$.

**Cholesky banda.** Si ancho de banda $b$, $L$ hereda banda $b$; costo $O(nb^2)$.

**Determinante.** $\det(A) = \prod_{i=1}^n \ell_{ii}^2$.

---

## Métodos directos — Costo computacional LU vs Gauss

**Costos individuales.** Eliminación $\tfrac{2}{3}n^3$; factorización LU $\tfrac{2}{3}n^3$; sustitución progresiva $n^2$; regresiva $n^2$.

**Un solo sistema.** Gauss directo $\tfrac{2}{3}n^3$; LU + resolver $\tfrac{2}{3}n^3 + 2n^2$.

**$m$ sistemas.** Gauss repetido $m\cdot\tfrac{2}{3}n^3$; LU una vez + $m$ pares de sustituciones $\tfrac{2}{3}n^3 + m\cdot 2n^2$.

**Punto de equilibrio.** LU más eficiente cuando
$$\frac{2}{3}n^3 + 2mn^2 < m\cdot\frac{2}{3}n^3 \quad\Longrightarrow\quad m > \frac{\tfrac{2}{3}n^3}{\tfrac{2}{3}n^3 - 2n^2} \approx 1 + \frac{3}{n}$$

**Cholesky + $m$ sustituciones (SDP).** $\tfrac{1}{3}n^3 + 2mn^2$.

**Múltiples lados derechos $AX=B$.** Gauss por columnas $\tfrac{2}{3}n^3 + mn^2$; LU + sustituciones $\tfrac{2}{3}n^3 + 2mn^2$.

**Almacenamiento.** Gauss/LU in-place $n^2$; Cholesky $n(n+1)/2$.

**Otras operaciones.** $Ax$: $2n^2$; $AB$: $2n^3$; inversa vía LU: $\tfrac{8}{3}n^3$.

---

## Métodos directos — Residuo vs error relativo de la solución

**Residuo y error.** Para $Ax=b$, $x=A^{-1}b$, aproximación $\tilde x$:
$$r = b - A\tilde x, \qquad e = x - \tilde x, \qquad e = A^{-1}r, \qquad r = Ae$$

**Número de condición.** $\kappa(A) = \|A\|\,\|A^{-1}\|$.

**Cota fundamental residuo–error.** Para $A$ no singular, $b\neq0$:
$$\frac{1}{\kappa(A)}\,\frac{\|r\|}{\|b\|} \;\leq\; \frac{\|e\|}{\|x\|} \;\leq\; \kappa(A)\,\frac{\|r\|}{\|b\|}$$

**Error hacia atrás normalizado.** $\tilde x$ resuelve exactamente $(A+\Delta A)\tilde x = b$ con
$$\Delta A = \frac{r\,\tilde x^T}{\tilde x^T\tilde x}, \qquad \frac{\|\Delta A\|_2}{\|A\|_2} = \frac{\|r\|_2}{\|A\|_2\,\|\tilde x\|_2}, \qquad \|\Delta A\|_2 = \frac{\|r\|_2}{\|\tilde x\|_2}$$

**Refinamiento iterativo.** $r = b - A\tilde x$; resolver $A\delta = r$ (reusa LU, $O(n^2)$); $\tilde x \leftarrow \tilde x + \delta$; recupera $\approx -\log_{10}(\kappa(A)\,u)$ dígitos/paso.

---

## Métodos directos — Sensibilidad de la solución y número de condición

**Perturbación solo en $b$.** Si $A(x+\Delta x) = b+\Delta b$:
$$\frac{\|\Delta x\|}{\|x\|} \leq \kappa(A)\,\frac{\|\Delta b\|}{\|b\|}$$

**Perturbación solo en $A$.** Si $(A+\Delta A)(x+\Delta x)=b$, $\kappa(A)\|\Delta A\|/\|A\| < 1$:
$$\frac{\|\Delta x\|}{\|x\|} \leq \frac{\kappa(A)}{1 - \kappa(A)\tfrac{\|\Delta A\|}{\|A\|}}\,\frac{\|\Delta A\|}{\|A\|}$$

**Perturbación simultánea (primer orden).**
$$\frac{\|\Delta x\|}{\|x\|} \lesssim \kappa(A)\left(\frac{\|\Delta A\|}{\|A\|} + \frac{\|\Delta b\|}{\|b\|}\right)$$

**Dígitos correctos.** $\approx -\log_{10}(u) - \log_{10}\kappa(A)$.

**Propiedades de $\kappa$.** $\kappa(A)\geq1$; $\kappa_2 = 1$ para ortogonales; $\kappa(\alpha A) = \kappa(A)$; $1/\kappa_2$ = distancia relativa a la singularidad.

---

## Métodos iterativos — Fundamentos de iteración de punto fijo lineal

**Esquema iterativo.** $y^{(k+1)} = T y^{(k)} + c$; punto fijo $x = Tx + c$.

**Construcción por splitting.** $M$ no singular, $N = M - A$; $My^{(k+1)} = Ny^{(k)} + b$; entonces
$$T = M^{-1}N, \qquad c = M^{-1}b$$

**Ecuación del error.** $z^{(k)} = y^{(k)} - x$:
$$z^{(k+1)} = T z^{(k)}, \qquad z^{(k)} = T^k z^{(0)}$$

**Convergencia.** $y^{(k)} \to x$ para todo $y^{(0)} \iff \lim_{k\to\infty} T^k = 0 \iff \rho(T) < 1$.

**Velocidad de convergencia.** $\|z^{(k)}\| \leq (\rho(T)+\varepsilon)^k\|z^{(0)}\|$; factor $\rho(T)$; tasa lineal $R = -\ln\rho(T)$; dígitos/iteración $R_{10} = -\log_{10}\rho(T)$.

**Error de redondeo por iteración.** $\sim \varepsilon_{\text{mach}}\|T\|\,\|y^{(k)}\|$.

**Criterio de parada.** $\dfrac{\|y^{(k+1)} - y^{(k)}\|}{\|y^{(k+1)}\|} \leq \text{tol}$.

---

## Métodos iterativos — Jacobi

**Descomposición.** $A = D - L - U$ ($D$ diagonal; $-L$, $-U$ estrictamente triangulares); $M = D$.

**Forma componente a componente.**
$$y_i^{(k+1)} = \frac{1}{a_{ii}}\Big(b_i - \sum_{j\neq i} a_{ij}\,y_j^{(k)}\Big), \quad i=1,\dots,n$$

**Forma vectorial.** $D y^{(k+1)} = (L+U)y^{(k)} + b$, es decir
$$y^{(k+1)} = D^{-1}(L+U)\,y^{(k)} + D^{-1}b$$

**Matriz de iteración.** $T_J = D^{-1}(L+U) = I - D^{-1}A$; $c_J = D^{-1}b$.

**Convergencia.** $\rho(T_J) < 1$; suficiente: diagonal dominante estricta. Si $A$ SDP, converge $\iff 2D - A$ definida positiva.

---

## Métodos iterativos — Gauss-Seidel

**Splitting.** $M = D - L$; $(D-L)y^{(k+1)} = U y^{(k)} + b$.

**Forma componente a componente.**
$$y_i^{(k+1)} = \frac{1}{a_{ii}}\Big(b_i - \sum_{j=1}^{i-1} a_{ij}\,y_j^{(k+1)} - \sum_{j=i+1}^{n} a_{ij}\,y_j^{(k)}\Big)$$

**Forma vectorial.**
$$y^{(k+1)} = (D-L)^{-1}U\,y^{(k)} + (D-L)^{-1}b$$

**Matriz de iteración.** $T_{GS} = (D-L)^{-1}U = I - (D-L)^{-1}A$; $c_{GS} = (D-L)^{-1}b$.

**Convergencia.** $\rho(T_{GS}) < 1$; suficiente: diagonal dominante estricta, SDP, o irreductible débilmente diagonal dominante. Cota: $\|(D-L)^{-1}U\| < 1 \Rightarrow \rho(T) < 1$.

---

## Métodos iterativos — Criterio del radio espectral

**Radio espectral.** $\rho(T) = \max\{|\lambda| : \lambda \text{ autovalor de } T\}$.

**Error de la iteración de punto fijo.** $e^{(k+1)} = Te^{(k)}$, $e^{(k)} = T^k e^{(0)}$.

**Teorema principal.**
$$\lim_{k\to\infty} T^k = 0 \iff \rho(T) < 1$$

**Lema de la norma.** Para todo $\varepsilon > 0$ existe norma matricial subordinada con $\|T\| \leq \rho(T) + \varepsilon$; luego $\|T^k\| \leq \|T\|^k \leq q^k$ con $q = \tfrac{1+\rho(T)}{2} < 1$.

**Matrices de iteración.** Jacobi $T_J = D^{-1}(E+F)$; Gauss-Seidel $T_{GS} = (D-E)^{-1}F$.

**Interpretación.** $R = -\ln\rho(T)$; $R_{10} = -\log_{10}\rho(T)$.

---

## Métodos iterativos — Teorema de la diagonal dominante estricta

**Definición (por filas).** $|a_{ii}| > \sum_{j\neq i}|a_{ij}|,\ \forall i$. Por columnas: $|a_{jj}| > \sum_{i\neq j}|a_{ij}|,\ \forall j$.

**Teorema.** Si $A$ es estrictamente diagonal dominante: (1) $A$ no singular; (2) Jacobi converge; (3) Gauss-Seidel converge.

**Cota del autovalor de $T_J$.** Para el índice de máximo $|v_i|$:
$$|\lambda|\,|a_{ii}| \leq \sum_{j\neq i}|a_{ij}|, \qquad |\lambda| \leq \frac{\sum_{j\neq i}|a_{ij}|}{|a_{ii}|} < 1 \;\Rightarrow\; \rho(T_J) < 1$$

**Comparación GS.** $\rho(T_{GS}) \leq \rho(T_J) < 1$ (bajo la misma hipótesis).

---

## Métodos iterativos — Teorema de Stein-Rosenberg

**Matriz de tipo M.** $a_{ii} > 0$; $a_{ij} \leq 0$ para $i\neq j$; $A$ no singular con $A^{-1} \geq 0$.

**Teorema (alternativas).** Para $A$ de tipo M:
$$0 \leq \rho(T_{GS}) \leq \rho(T_J) < 1, \quad \text{o}\quad \rho(T_{GS}) = \rho(T_J) = 1, \quad \text{o}\quad \rho(T_{GS}) \geq \rho(T_J) > 1$$

**No negatividad.** $T_J \geq 0$ con $(T_J)_{ij} = -a_{ij}/a_{ii} \geq 0$ ($i\neq j$), $0$ si $i=j$; $T_{GS} \geq 0$.

**Relación de splitting.** $T_J = L + U$ con $L = D^{-1}E \geq 0$, $U = D^{-1}F \geq 0$; $T_{GS} = (I-L)^{-1}U$.

---

## Métodos iterativos — Estimación de error y cotas a priori

**Cota directa.** Con norma inducida y $\|T\| < 1$:
$$\|\varepsilon^{(k)}\| = \|T^k\varepsilon^{(0)}\| \leq \|T\|^k\,\|\varepsilon^{(0)}\|$$

**Cota a priori.** Con $d^{(k)} = y^{(k)} - y^{(k-1)}$:
$$\|\varepsilon^{(k)}\| \leq \frac{\|T\|^k}{1 - \|T\|}\,\|y^{(1)} - y^{(0)}\|$$

**Cota a posteriori.**
$$\|\varepsilon^{(k)}\| \leq \frac{\|T\|}{1 - \|T\|}\,\|y^{(k)} - y^{(k-1)}\|$$

**Número de iteraciones para tolerancia.**
$$k \geq \frac{\log\!\big(\texttt{tol}\,(1-\|T\|)/\|y^{(1)}-y^{(0)}\|\big)}{\log\|T\|}$$

**Relación normas.** $\rho(T) \leq \|T\|$; $\|T\| < 1$ suficiente pero no necesario.

---

## Valores y vectores propios — Fundamentos del valor propio dominante

**Autovalor dominante.** $|\lambda_1| > |\lambda_2| \geq |\lambda_3| \geq \cdots \geq |\lambda_n|$; dirección dominante $v_1$.

**Hipótesis de convergencia.** (1) $A$ diagonalizable; (2) $|\lambda_1| > |\lambda_2|$; (3) $y^{(0)} = \sum_i c_i v_i$ con $c_1 \neq 0$.

**Amplificación del modo dominante.**
$$A^k y^{(0)} = \lambda_1^k\Big(c_1 v_1 + \sum_{i\geq2} c_i\big(\tfrac{\lambda_i}{\lambda_1}\big)^k v_i\Big)$$

**Perron–Frobenius (caso $a_{ij} > 0$).** Existe $\lambda_1 = \rho(A) > 0$ estrictamente dominante, simple, con $v_1 > 0$.

**Tasa.** $|\lambda_2/\lambda_1|$.

---

## Valores y vectores propios — Velocidad de convergencia ($\lambda_2/\lambda_1$)

**Razón de convergencia.** $r = \left|\dfrac{\lambda_2}{\lambda_1}\right| < 1$.

**Iterado en la base de autovectores.**
$$z^{(k)} = A^k y^{(0)} = \lambda_1^k\Big(c_1 v_1 + \sum_{i=2}^n c_i\big(\tfrac{\lambda_i}{\lambda_1}\big)^k v_i\Big)$$

**Error del autovector.**
$$\left\|\frac{z^{(k)}}{\|z^{(k)}\|} - \frac{v_1}{\|v_1\|}\right\| = O\!\left(\left|\frac{\lambda_2}{\lambda_1}\right|^k\right)$$

**Iteraciones para $d$ dígitos.**
$$r^k \leq \varepsilon, \qquad k \geq \frac{\ln\varepsilon}{\ln r} = \frac{d}{\log_{10}(1/r)}, \qquad \text{dígitos/iteración} = -\log_{10} r$$

**No convergencia.** Si $|\lambda_1| = |\lambda_2|$ (p. ej. complejos conjugados), $r = 1$ y la iteración oscila.

---

## Valores y vectores propios — Cociente de Rayleigh

**Definición.** $R_A(y) = \dfrac{y^T A y}{y^T y}$.

**Propiedades.** Homogeneidad $R_A(\alpha y) = R_A(y)$; rango (simétrica) $\lambda_{\min} \leq R_A(y) \leq \lambda_{\max}$; estacionariedad en autovectores.

**Gradiente.** $\nabla R_A(y) = \dfrac{2}{y^T y}\big(Ay - R_A(y)\,y\big)$.

**Optimalidad.** $\alpha = R_A(y)$ minimiza $\|Ay - \alpha y\|_2$.

**Convergencia (simétrica).** $|R_A(y) - \lambda_1| = O(\varepsilon^2)$ con $\varepsilon = \|y - v_1\|$ (cuadrática); no simétrica: $O(|\lambda_2/\lambda_1|^k)$ (lineal).

**Potencia inversa.** $\lambda_{\text{cercano}} \approx \mu + \dfrac{1}{R_{(A-\mu I)^{-1}}(y)}$.

---

## Valores y vectores propios — Caso simétrico y convergencia acelerada

**Teorema espectral.** $A = A^T$: autovalores reales, base ortonormal $v_i^T v_j = \delta_{ij}$.

**Cociente de Rayleigh iterado.** $\lambda^{(k)} = \dfrac{y^{(k)T}Ay^{(k)}}{y^{(k)T}y^{(k)}}$.

**Convergencia cuadrática del autovalor.** Con $\theta = |\lambda_2/\lambda_1|$ y $y^{(k)} = v_1 + O(\theta^k)$:
$$|\lambda^{(k)} - \lambda_1| = O(\theta^{2k})$$

**Expansión.** Con $y = v_1 + \sum_{i\geq2}\epsilon_i v_i$:
$$y^T A y = \lambda_1 + \sum_{i\geq2}\epsilon_i^2\lambda_i, \qquad y^T y = 1 + \sum_{i\geq2}\epsilon_i^2, \qquad \lambda^{(k)} = \lambda_1 + \sum_{i\geq2}\epsilon_i^2(\lambda_i - \lambda_1) + O(\epsilon^4)$$

**Minimax (Courant–Fischer).** $\lambda_1 = \max_{\|y\|=1} y^T A y$.

**Deflación.** $A - \lambda_1 v_1 v_1^T$ conserva simetría y demás autovalores.

**RQI (simétrica).** $(A - \mu_k I)z = y^{(k)}$; $y^{(k+1)} = z/\|z\|$; $\mu_{k+1} = y^{(k+1)T}Ay^{(k+1)}$; convergencia cúbica.

---

## Valores y vectores propios — Potencia inversa

**Definición.** Método de la potencia sobre $A^{-1}$; autovalores $1/\lambda_i$; dominante de $A^{-1}$ = $1/\lambda_n$.

**Orden espectral.** Con $|\lambda_1| \geq \cdots \geq |\lambda_{n-1}| > |\lambda_n| > 0$:
$$\left|\frac{1}{\lambda_n}\right| > \left|\frac{1}{\lambda_{n-1}}\right| \geq \cdots \geq \left|\frac{1}{\lambda_1}\right|$$

**Iteración.** Resolver $A z^{(k)} = y^{(k)}$; $y^{(k+1)} = z^{(k)}/\|z^{(k)}\|$; $\lambda^{(k)} = 1/R_{A^{-1}}(y^{(k)})$.

**Convergencia.** $\lim y^{(k)} = v_n/\|v_n\|$, $\lim 1/R_{A^{-1}}(y^{(k)}) = \lambda_n$.

**Razón de convergencia.** $r = \left|\dfrac{\mu_{n-1}}{\mu_n}\right| = \left|\dfrac{\lambda_n}{\lambda_{n-1}}\right|$.

**Costo.** LU inicial $O(n^3)$ + $O(n^2)$ por iteración; resolver $PLUz = y$ vía $Lw = P^Ty$, $Uz = w$.

---

## Valores y vectores propios — Potencia desplazada y RQI

**Definición.** Potencia inversa sobre $(A - \mu I)^{-1}$; autovalores $1/(\lambda_i - \mu)$; apunta al $\lambda_j$ más cercano a $\mu$.

**Iteración.** Resolver $(A - \mu I)z^{(k)} = y^{(k)}$; $y^{(k+1)} = z^{(k)}/\|z^{(k)}\|$; $\lambda^{(k)} = \mu + 1/R_{(A-\mu I)^{-1}}(y^{(k)})$.

**Razón de convergencia.** $r = \left|\dfrac{\lambda_j - \mu}{\lambda_k - \mu}\right|$, con $\lambda_k$ el siguiente más cercano a $\mu$.

**Recuperación del autovalor.** $\lambda_j = \mu + \dfrac{1}{\mu_j}$.

**Iteración del cociente de Rayleigh (RQI).**
$$\mu^{(k)} = \frac{y^{(k)T}Ay^{(k)}}{y^{(k)T}y^{(k)}}, \qquad (A - \mu^{(k)}I)\,z^{(k)} = y^{(k)}, \qquad y^{(k+1)} = \frac{z^{(k)}}{\|z^{(k)}\|}$$

**Orden RQI.** Cuadrática general ($O(\varepsilon^2)$); cúbica simétrica ($O(\varepsilon^3)$).

**Costo.** $\mu$ fijo: LU una vez $O(n^3)$ + $O(n^2)$/iteración; RQI: $O(n^3)$/iteración (matriz cambia).

---

## Valores y vectores propios — Iteración simultánea

**Definición.** Extensión a subespacio de dimensión $p$: $Y^{(k)} \in \mathbb{R}^{n\times p}$ con columnas ortonormales.

**Iteración (con QR).** $Z^{(k)} = A Y^{(k-1)}$; ortonormalizar $Z^{(k)} = Y^{(k)}R^{(k)}$.

**Valores de Ritz.** $B^{(k)} = Y^{(k)T}A\,Y^{(k)} \in \mathbb{R}^{p\times p}$; sus autovalores aproximan $\lambda_1,\dots,\lambda_p$.

**Aplicación de $A^k$ en bloques.** Con $\Lambda_1 = \operatorname{diag}(\lambda_1,\dots,\lambda_p)$, $\Lambda_2 = \operatorname{diag}(\lambda_{p+1},\dots,\lambda_n)$, $C_{11}$ no singular:
$$A^k Y^{(0)} = V\begin{pmatrix}\Lambda_1^k C_{11} & \Lambda_1^k C_{12}\\ \Lambda_2^k C_{21} & \Lambda_2^k C_{22}\end{pmatrix}$$

**Convergencia del subespacio.**
$$\angle(\mathcal{S}^{(k)}, \mathcal{S}) = O\!\left(\left|\frac{\lambda_{p+1}}{\lambda_p}\right|^k\right)$$

**Relación con QR.** Con $p = n$, $Y^{(0)} = I$: $A_k = Q_k^T A Q_k$ (método QR sin desplazamiento).

**Costo/iteración.** $AY$: $O(p\cdot\text{nnz})$; QR: $O(np^2)$.

---

## Valores y vectores propios — Transformaciones de Householder

**Definición.** $H = I - 2\,\dfrac{vv^T}{v^Tv}$, $v \neq 0$ (reflexión ortogonal).

**Propiedades.** $H^T = H$; $H^TH = I$; $H^{-1} = H$; $H^2 = I$; $\det(H) = -1$; $\|Hx\|_2 = \|x\|_2$.

**Anulación de columna.**
$$Hx = -\operatorname{sgn}(x_1)\|x\|_2\,e_1, \qquad v = x + \operatorname{sgn}(x_1)\|x\|_2\,e_1$$

**Identidades del vector.** Con $\beta = 2/(v^Tv)$: $v^Tv = 2(\|x\|^2 + \alpha x_1)$, $v^Tx = \|x\|^2 + \alpha x_1$, $\beta\,v^Tx = 1$ (con $\alpha = \operatorname{sgn}(x_1)\|x\|_2$).

**Factorización QR.** $A = QR$, $Q = H_1\cdots H_n$ ortogonal, $R$ triangular superior; costo $\approx 2n^2(m - n/3)$; $m=n$: $\tfrac{4}{3}n^3$.

**Estabilidad.** Incondicionalmente estable hacia atrás, $\kappa_2(Q) = 1$.

**Householder vs Givens.** Householder anula columna ($\det=-1$); Givens anula entrada, rotación ($\det=+1$).

---

## Valores y vectores propios — Iteración QR

**Iteración QR.** Desde $A_0 = A$:
$$A_k = Q_k R_k \ (\text{factorización}), \qquad A_{k+1} = R_k Q_k \ (\text{recomposición})$$

**Preservación del espectro.** $A_{k+1} = Q_k^T A_k Q_k$ (semejanza ortogonal; mismos autovalores).

**Convergencia a triangular.** Si $|\lambda_1| > \cdots > |\lambda_n|$: $(A_k)_{ij} \to 0$ ($i>j$), $(A_k)_{ii} \to \lambda_i$, con
$$|(A_k)_{i+1,i}| = O\!\left(\left|\frac{\lambda_{i+1}}{\lambda_i}\right|^k\right)$$

**Reducción a Hessenberg.** $A = U H U^T$, $H_{ij} = 0$ si $i > j+1$; invariante bajo QR; paso $O(n^2)$ (tridiagonal simétrica: $O(n)$).

**Forma de Schur real.** Autovalores complejos $\Rightarrow$ forma cuasi-triangular con bloques $2\times2$.

---

## Valores y vectores propios — Convergencia y desplazamientos QR

**Paso desplazado.**
$$A_k - \mu_k I = Q_k R_k, \qquad A_{k+1} = R_k Q_k + \mu_k I$$

**Factor de convergencia (deflación).**
$$|(A_{k+1})_{n,n-1}| \approx \left|\frac{\lambda_n - \mu_k}{\lambda_{n-1} - \mu_k}\right|\,|(A_k)_{n,n-1}|, \qquad r_k = \left|\frac{\lambda_n - \mu_k}{\lambda_{n-1} - \mu_k}\right|$$

**Estrategias de desplazamiento.** Rayleigh $\mu_k = (A_k)_{nn}$ (cuadrática); Wilkinson: autovalor del bloque $2\times2$ inferior derecho más cercano a $(A_k)_{nn}$; Francis: doble desplazamiento (par conjugado, aritmética real).

**Deflación.** Si $|(A_k)_{i+1,i}| \leq \texttt{tol}\big(|(A_k)_{ii}| + |(A_k)_{i+1,i+1}|\big)$, se fija a cero y se parte la matriz.

**Costo global (autovalores).** Reducción a Hessenberg $\tfrac{10}{3}n^3$; total $\sim 10\,n^3$; con autovectores $\sim 25\,n^3$.
