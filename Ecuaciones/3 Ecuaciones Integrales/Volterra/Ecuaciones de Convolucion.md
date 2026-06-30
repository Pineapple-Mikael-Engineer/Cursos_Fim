---
title: Ecuaciones de Convolución
order: 4
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - volterra
  - convolucion
draft: false
aliases:
  - ecuaciones de convolución
  - núcleo de convolución
  - método de Laplace para Volterra
  - convolution type integral equations
---

# Ecuaciones de Convolución

> [!definicion]
> Una ecuación de Volterra es de **tipo convolución** cuando su núcleo depende **solo de la diferencia** $x-t$, es decir $K(x,t)=K(x-t)$:
> $$\varphi(x)=f(x)+\lambda\int_{0}^{x}K(x-t)\,\varphi(t)\,dt.$$
> La integral es exactamente la **convolución** $K*\varphi$, de modo que la ecuación se escribe $\varphi=f+\lambda\,K*\varphi$. Estas ecuaciones se resuelven **algebraicamente** aplicando la **transformada de Laplace**, que convierte la convolución en un simple producto.

> [!info]
> Caso especial de [[Volterra Segunda Especie| Volterra de 2ª especie]] dentro de la sección [[Volterra/index| Volterra]] del [[3 Ecuaciones Integrales/index| capítulo de ecuaciones integrales]]. La herramienta central es la [[Transformada de Laplace/index| transformada de Laplace]]. El [[Problema de Abel| problema de Abel]] es el caso de convolución con núcleo singular, y este método conecta con el [[Calculo Fraccionario/index| cálculo fraccionario]]. Fuente: Krasnov, *Ecuaciones integrales*, §5.

---

## Ejemplo

> [!ejemplo] Resolver $\varphi(x)=1+\int_0^x e^{x-t}\varphi(t)\,dt$
> El núcleo es $K(x-t)=e^{x-t}$, de convolución, y el término libre es $f(x)=1$. Buscamos $\varphi$.
>
> **Paso 1 — identificar las transformadas.** Llamamos $\Phi(s)=\mathcal{L}\{\varphi\}$, $F(s)=\mathcal{L}\{f\}$. Aquí
> $$F(s)=\mathcal{L}\{1\}=\frac{1}{s},\qquad \hat K(s)=\mathcal{L}\{e^{x}\}=\frac{1}{s-1}.$$
>
> **Paso 2 — transformar la ecuación.** Por el teorema de convolución $\mathcal{L}\{K*\varphi\}=\hat K(s)\,\Phi(s)$, así que con $\lambda=1$
> $$\Phi(s)=F(s)+\hat K(s)\,\Phi(s)=\frac{1}{s}+\frac{1}{s-1}\,\Phi(s).$$
>
> **Paso 3 — despejar $\Phi$.** Agrupando los términos en $\Phi$,
> $$\Phi(s)\left(1-\frac{1}{s-1}\right)=\frac{1}{s}\ \Longrightarrow\ \Phi(s)\,\frac{s-2}{s-1}=\frac{1}{s}
> \ \Longrightarrow\ \Phi(s)=\frac{s-1}{s\,(s-2)}.$$
>
> **Paso 4 — fracciones parciales.** Escribimos $\dfrac{s-1}{s(s-2)}=\dfrac{A}{s}+\dfrac{B}{s-2}$. De $s-1=A(s-2)+Bs$ se obtiene, en $s=0$: $-1=-2A\Rightarrow A=\tfrac12$; en $s=2$: $1=2B\Rightarrow B=\tfrac12$.
> $$\Phi(s)=\frac{1}{2}\,\frac{1}{s}+\frac{1}{2}\,\frac{1}{s-2}.$$
>
> **Paso 5 — antitransformar.** Como $1/s\leftrightarrow 1$ y $1/(s-2)\leftrightarrow e^{2x}$,
> $$\boxed{\ \varphi(x)=\frac{1}{2}+\frac{1}{2}\,e^{2x}.\ }$$
>
> **Verificación.** $\varphi(0)=1=f(0)$ y, derivando la ecuación original, $\varphi'=f'+\varphi+\int_0^x e^{x-t}\varphi$, que se cumple con $\varphi'=e^{2x}$. Hemos convertido una ecuación integral en **álgebra de fracciones parciales**.

---

## En qué consiste

> [!teoria]
> La convolución de dos funciones causales (definidas para $x\ge 0$) es
> $$(K*\varphi)(x)=\int_0^x K(x-t)\,\varphi(t)\,dt.$$
> Su rasgo decisivo es el **teorema de convolución**: la transformada de Laplace de una convolución es el **producto** de las transformadas, $\mathcal{L}\{K*\varphi\}=\hat K(s)\,\Phi(s)$. Una ecuación integral acopla $\varphi$ consigo misma a través de una integral; al pasar al dominio de Laplace ese acoplamiento se vuelve una **multiplicación**, y resolver la ecuación se reduce a **despejar** una incógnita algebraica $\Phi(s)$.

> [!teorema] Solución por transformada de Laplace
> Sea la ecuación de convolución $\varphi(x)=f(x)+\lambda\displaystyle\int_0^x K(x-t)\,\varphi(t)\,dt$, con $f$ y $K$ de orden exponencial. Si $1-\lambda\hat K(s)\neq 0$, su solución es
> $$\varphi(x)=\mathcal{L}^{-1}\!\left\{\frac{F(s)}{1-\lambda\,\hat K(s)}\right\}\!,\qquad
> F(s)=\mathcal{L}\{f\},\ \hat K(s)=\mathcal{L}\{K\}.$$

> [!demostracion]
> **Paso 1 — aplicar Laplace.** Tomamos transformada en ambos lados. Por linealidad, $\mathcal{L}\{\varphi\}=\mathcal{L}\{f\}+\lambda\,\mathcal{L}\{K*\varphi\}$.
>
> **Paso 2 — usar el teorema de convolución.** Como la integral es $K*\varphi$, $\mathcal{L}\{K*\varphi\}=\hat K(s)\,\Phi(s)$. Por tanto
> $$\Phi(s)=F(s)+\lambda\,\hat K(s)\,\Phi(s).$$
>
> **Paso 3 — despejar la incógnita algebraica.** Agrupando,
> $$\Phi(s)\big(1-\lambda\,\hat K(s)\big)=F(s)\ \Longrightarrow\ \Phi(s)=\frac{F(s)}{1-\lambda\,\hat K(s)}.$$
>
> **Paso 4 — antitransformar.** La solución se recupera con la transformada inversa, $\varphi(x)=\mathcal{L}^{-1}\{\Phi(s)\}$, usualmente vía fracciones parciales o tablas. $\blacksquare$
>
> La cantidad $\dfrac{1}{1-\lambda\hat K(s)}$ es, en el dominio de Laplace, la **resolvente**: su antitransformada es el núcleo resolvente $\Gamma(x-t;\lambda)$ que aparece en [[Resolvente y Nucleos Iterados| la teoría general]].

> [!info] Ecuaciones integro-diferenciales
> El mismo método resuelve **ecuaciones integro-diferenciales** de convolución, que mezclan derivadas de $\varphi$ con una convolución, por ejemplo
> $$\varphi'(x)=f(x)+\lambda\int_0^x K(x-t)\,\varphi(t)\,dt,\qquad \varphi(0)=\varphi_0.$$
> Laplace transforma $\varphi'$ en $s\Phi(s)-\varphi_0$ y la integral en $\hat K(s)\Phi(s)$; todo queda de nuevo en álgebra. Es el puente natural hacia las ecuaciones **difero-integrales** del [[Calculo Fraccionario/index| cálculo fraccionario]], donde el "orden" de derivación es fraccionario (Krasnov, §6).

> [!algoritmo] Resolver una ecuación de convolución
> 1. **Reconocer** que el núcleo es $K(x-t)$ (depende solo de la diferencia).
> 2. **Transformar** con Laplace: calcular $F(s)$ y $\hat K(s)$.
> 3. **Despejar** $\Phi(s)=\dfrac{F(s)}{1-\lambda\hat K(s)}$ (sumando $s\Phi-\varphi_0$ si hay derivadas).
> 4. **Antitransformar** $\varphi=\mathcal{L}^{-1}\{\Phi\}$, normalmente por fracciones parciales.

> [!warning]
> El método exige que $f$ y $K$ admitan transformada de Laplace (orden exponencial) y que $1-\lambda\hat K(s)\not\equiv 0$. Si $\hat K(s)\to 0$ no lo bastante rápido —como en el [[Problema de Abel| núcleo singular de Abel]] $1/\sqrt{x-t}$, con $\hat K=\sqrt{\pi/s}$— la ecuación sigue resolviéndose, pero la inversión involucra **derivadas fraccionarias**.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Forma | $\varphi=f+\lambda\,K*\varphi$, con $K=K(x-t)$ |
> | Herramienta | transformada de [[Transformada de Laplace/index\|Laplace]] |
> | Clave | $\mathcal{L}\{K*\varphi\}=\hat K(s)\Phi(s)$ |
> | Solución | $\Phi=\dfrac{F}{1-\lambda\hat K}$, luego antitransformar |
> | Extensión | integro-diferenciales; [[Problema de Abel\|Abel]] singular |

> [!corolario]
> Cuando el núcleo solo "ve" la diferencia $x-t$, la ecuación integral pierde su dificultad: Laplace convierte la convolución en producto, la ecuación en una **fracción algebraica** $\Phi=F/(1-\lambda\hat K)$, y el problema entero en antitransformar. Es el método más limpio de todo Volterra.

> [!referencia]
> - El caso singular de convolución: [[Problema de Abel]].
> - La ecuación general de la que es caso particular: [[Volterra Segunda Especie]].
> - La herramienta: [[Transformada de Laplace/index]].
> - Vuelta al índice: [[Volterra/index]].
