---
title: Formula de Abel
tags:
  - ecuaciones
  - edo
  - teoria
  - lineales
  - wronskiano
draft: false
aliases:
  - fórmula de Abel
  - identidad de Abel-Liouville
  - fórmula de Liouville
  - Abel's formula
  - Abel-Liouville identity
---

# Fórmula de Abel (Liouville)

> [!definicion]
> Para una EDO lineal homogénea de segundo orden en forma normal
> $$y''+p(x)\,y'+q(x)\,y=0,$$
> el wronskiano $W=y_1y_2'-y_2y_1'$ de dos soluciones cualesquiera cumple la **fórmula de Abel**
> (o identidad de Abel–Liouville):
> $$\boxed{\,W(x)=W(x_0)\,\exp\!\Big(-\!\int_{x_0}^{x}p(t)\,dt\Big)\,}.$$
> En orden $n$, con coeficiente director $1$ y siguiente coeficiente $p_{n-1}$, satisface la ecuación de
> primer orden $W'=-p_{n-1}\,W$, cuya solución es $W(x)=W(x_0)\exp\!\big(-\int_{x_0}^x p_{n-1}\big)$. La
> fórmula da el wronskiano **explícitamente, sin necesidad de conocer las soluciones**.

> [!info]
> Resultado clave del bloque [[Lineales de Orden Superior/index| lineales de orden superior]]. Es lo
> que justifica que el [[Wronskiano e Independencia Lineal| wronskiano]] sea un test válido de
> independencia: como la exponencial nunca se anula, $W$ es **siempre $0$ o nunca $0$**. Además permite
> (a) calcular $W$ sin resolver la EDO y (b) obtener la **segunda solución** a partir de una conocida,
> idea base de la [[Reduccion de Orden| reducción de orden]]. Pertenece al **Capítulo 1 — Ecuaciones
> Diferenciales Ordinarias**.

---

## Ejemplo

> [!ejemplo] Coeficiente $p=0$: wronskiano constante
> En $y''+y=0$ es $p(x)=0$, luego $\int p=0$ y la fórmula da $W(x)=W(x_0)\,e^{0}=W(x_0)$: el wronskiano
> es **constante**. Con $y_1=\cos x$, $y_2=\sin x$ ya sabemos que $W=1$; con $y_1=e^{x},y_2=e^{-x}$ en
> $y''-y=0$ (también $p=0$) sale $W=-2$. La fórmula predice la constancia sin calcular el determinante
> en cada punto.

> [!ejemplo] Coeficiente $p\neq0$: wronskiano que decae
> Considera $x\,y''+y'=0$, es decir $y''+\tfrac1x\,y'=0$ con $p(x)=1/x$ en $x>0$. Entonces
> $$\int_{x_0}^{x}\frac{dt}{t}=\ln\frac{x}{x_0}\;\Rightarrow\; W(x)=W(x_0)\,e^{-\ln(x/x_0)}=W(x_0)\,\frac{x_0}{x}.$$
> El wronskiano decae como $1/x$. En efecto, las soluciones son $y_1=1$, $y_2=\ln x$, y
> $W=1\cdot\tfrac1x-\ln x\cdot0=\tfrac1x$, en perfecto acuerdo con la fórmula (con $W(1)=1$, $x_0=1$).

---

## En qué consiste

> [!teoria]
> La fórmula de Abel surge de una observación notable: aunque cada solución $y_i$ es difícil de hallar,
> la combinación particular $W=y_1y_2'-y_2y_1'$ satisface por sí misma una EDO **de primer orden** muy
> simple. La razón es que al derivar $W$ los términos "cruzados" se cancelan, y al usar que las $y_i$
> resuelven la ecuación, las segundas derivadas se reemplazan por $-py_i'-qy_i$; los términos con $q$ se
> cancelan y solo sobrevive $-pW$. Resolver esa ecuación de primer orden da la exponencial.

> [!teorema] Fórmula de Abel
> Si $y_1,y_2$ son soluciones de $y''+p(x)y'+q(x)y=0$ con $p$ continua en un intervalo $I$, su
> wronskiano satisface $W'=-p\,W$ y por tanto
> $$W(x)=W(x_0)\,\exp\!\Big(-\!\int_{x_0}^{x}p(t)\,dt\Big),\qquad x,x_0\in I.$$

> [!demostracion]
> **Paso 1 — derivar el wronskiano.** Partimos de $W=y_1y_2'-y_2y_1'$ y derivamos con la regla del
> producto:
> $$W'=\big(y_1'y_2'+y_1y_2''\big)-\big(y_2'y_1'+y_2y_1''\big)=y_1y_2''-y_2y_1'',$$
> donde los términos cruzados $y_1'y_2'$ y $y_2'y_1'$ **se cancelan**.
>
> **Paso 2 — usar que cada $y_i$ resuelve la EDO.** De la ecuación, $y_i''=-p\,y_i'-q\,y_i$. Sustituyendo
> en $W'$:
> $$W'=y_1(-p\,y_2'-q\,y_2)-y_2(-p\,y_1'-q\,y_1)
> =-p\,(y_1y_2'-y_2y_1')\;\underbrace{-q\,(y_1y_2-y_2y_1)}_{=\,0}=-p\,W.$$
> Los términos con $q$ se anulan porque $y_1y_2-y_2y_1=0$.
>
> **Paso 3 — resolver $W'=-pW$.** Es una EDO lineal de primer orden separable. Integrando,
> $$\frac{dW}{W}=-p\,dx\;\Rightarrow\;\ln\frac{W(x)}{W(x_0)}=-\!\int_{x_0}^{x}p(t)\,dt
> \;\Rightarrow\;W(x)=W(x_0)\,\exp\!\Big(-\!\int_{x_0}^{x}p\Big).\qquad\blacksquare$$

> [!corolario] Dicotomía "siempre $0$ o nunca $0$"
> Como $\exp(\cdot)>0$ siempre, el signo de $W$ lo fija $W(x_0)$. Por tanto:
> - si $W(x_0)\neq0$, entonces $W(x)\neq0$ para **todo** $x\in I$;
> - si $W(x_0)=0$, entonces $W(x)\equiv0$ en $I$.
>
> Esta dicotomía es justo lo que convierte al wronskiano en un **test válido de independencia lineal**:
> basta evaluarlo en un único punto (ver [[Wronskiano e Independencia Lineal]]).

> [!info] Aplicación: segunda solución y reducción de orden
> La fórmula es operativa para construir una segunda solución a partir de una conocida $y_1$. Tratando
> $W=y_1y_2'-y_2y_1'=W_0\,e^{-\int p}$ como una EDO lineal de primer orden en $y_2$, se divide por
> $y_1^2$ y se reconoce una derivada exacta:
> $$\frac{W}{y_1^2}=\frac{y_1y_2'-y_2y_1'}{y_1^2}=\Big(\frac{y_2}{y_1}\Big)'
> \;\Rightarrow\;\frac{y_2}{y_1}=\int\frac{W_0\,e^{-\int p}}{y_1^2}\,dx,$$
> de donde
> $$y_2=y_1\int\frac{e^{-\int p\,dx}}{y_1^{2}}\,dx.$$
> Esta fórmula explícita es exactamente el resultado de la [[Reduccion de Orden| reducción de orden]].

## Resumen

> [!resumen]
> | Aspecto | Enunciado |
> |---|---|
> | EDO de orden 2 | $y''+p\,y'+q\,y=0$ |
> | EDO del wronskiano | $W'=-p\,W$ (orden $n$: $W'=-p_{n-1}W$) |
> | Fórmula de Abel | $W(x)=W(x_0)\,\exp\!\big(-\int_{x_0}^x p\big)$ |
> | Caso $p=0$ | $W=$ constante |
> | Consecuencia | $W$ siempre $0$ o nunca $0$ (test de independencia) |
> | Segunda solución | $y_2=y_1\int \dfrac{e^{-\int p}}{y_1^{2}}\,dx$ |

> [!corolario]
> La fórmula de Abel revela que el wronskiano, pese a involucrar soluciones desconocidas, obedece una
> ley de primer orden universal que depende **solo** del coeficiente $p$. De ahí salen sus dos usos
> fundamentales: certificar la independencia de soluciones y fabricar una segunda solución a partir de
> una primera.

> [!referencia]
> - El test de independencia que esta fórmula valida: [[Wronskiano e Independencia Lineal]].
> - El método que explota la fórmula para $y_2$: [[Reduccion de Orden]].
> - El operador lineal y la estructura del espacio de soluciones: [[Operador Diferencial Lineal]].
> - Capítulo: [[Lineales de Orden Superior/index]].
