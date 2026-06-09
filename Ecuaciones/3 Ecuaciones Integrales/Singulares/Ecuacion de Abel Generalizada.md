---
title: Ecuación de Abel Generalizada
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - singulares
  - calculo-fraccionario
draft: false
aliases:
  - ecuación de Abel generalizada
  - Abel generalizada
  - generalized Abel equation
  - integral fraccionaria de Riemann-Liouville
---

# Ecuación de Abel Generalizada

> [!definicion]
> La **ecuación de Abel generalizada** es la ecuación integral de Volterra de **primera especie**
> con núcleo **débilmente singular** de tipo potencia
> $$f(x)=\int_0^x\frac{\varphi(t)}{(x-t)^{\alpha}}\,dt,\qquad 0<\alpha<1,$$
> donde $f$ es dato, $\varphi$ es la incógnita y el exponente $0<\alpha<1$ hace que el núcleo
> $(x-t)^{-\alpha}\to\infty$ cuando $t\to x$ pero la integral **siga convergiendo** (singularidad
> integrable). El caso $\alpha=\tfrac12$ es el clásico [[Problema de Abel| problema de Abel]] de la
> tautócrona; el caso general interpola entre la identidad ($\alpha\to0$) y una singularidad cada vez
> más fuerte ($\alpha\to1$, ya frontera con el [[Nucleo de Cauchy y Riemann-Hilbert| núcleo de Cauchy]]).

> [!info]
> Vive en la sección [[Singulares/index| Singulares]] del capítulo
> [[3 Ecuaciones Integrales/index| Ecuaciones Integrales]]. Es la **única familia singular que se
> resuelve en forma cerrada de modo elemental**, y la puerta de entrada al
> [[Calculo Fraccionario/index| cálculo fraccionario]]: la integral de la derecha es, salvo una
> constante, una **integral de orden no entero**. Fuente: **Krasnov, Kiseliov, Makarenko**,
> *Ecuaciones integrales*.

---

## Ejemplo

> [!ejemplo] Invertir una Abel generalizada con término libre potencia
> Resolvamos, para $0<\alpha<1$,
> $$f(x)=x^{\beta}=\int_0^x\frac{\varphi(t)}{(x-t)^{\alpha}}\,dt,\qquad \beta>-1.$$
>
> **Idea.** El núcleo es de **convolución** de tipo potencia, y la integral de un producto de potencias
> sobre $[0,x]$ es una **función Beta**. Recordemos la identidad maestra (cambio $t=xs$):
> $$\int_0^x t^{\,p-1}(x-t)^{\,q-1}\,dt=x^{\,p+q-1}\,B(p,q),\qquad B(p,q)=\frac{\Gamma(p)\,\Gamma(q)}{\Gamma(p+q)}.$$
>
> **Ensayo.** Como el lado izquierdo es una potencia $x^\beta$, probamos $\varphi(t)=C\,t^{\,\gamma}$ y
> ajustamos $C,\gamma$. Sustituyendo con $p-1=\gamma$ y $q-1=-\alpha$:
> $$\int_0^x C\,t^{\gamma}(x-t)^{-\alpha}\,dt
> = C\,x^{\,\gamma-\alpha+1}\,B(\gamma+1,\,1-\alpha)
> = C\,\frac{\Gamma(\gamma+1)\,\Gamma(1-\alpha)}{\Gamma(\gamma+2-\alpha)}\;x^{\,\gamma-\alpha+1}.$$
>
> **Igualar exponentes.** Para que esto sea $x^\beta$ pedimos $\gamma-\alpha+1=\beta$, es decir
> $\gamma=\beta+\alpha-1$. Y para fijar la constante, igualamos coeficientes:
> $$C=\frac{\Gamma(\gamma+2-\alpha)}{\Gamma(\gamma+1)\,\Gamma(1-\alpha)}
> =\frac{\Gamma(\beta+1)}{\Gamma(\beta+\alpha)\,\Gamma(1-\alpha)}.$$
>
> **Solución.**
> $$\boxed{\;\varphi(x)=\frac{\Gamma(\beta+1)}{\Gamma(\beta+\alpha)\,\Gamma(1-\alpha)}\;x^{\,\beta+\alpha-1}.\;}$$
>
> **Comprobación rápida** ($\alpha=\tfrac12,\ \beta=1$, la tautócrona con $f(x)=x$): da
> $\varphi(x)=\dfrac{\Gamma(2)}{\Gamma(3/2)\Gamma(1/2)}x^{1/2}=\dfrac{1}{(\sqrt\pi/2)\sqrt\pi}\,x^{1/2}
> =\dfrac{2}{\pi}\sqrt{x}$, el resultado conocido de [[Problema de Abel| Abel]].

---

## En qué consiste

> [!teoria] La integral de Abel **es** una integral fraccionaria
> Define la **integral fraccionaria de Riemann-Liouville** de orden $\mu>0$ con base en $0$:
> $$\big(I^{\mu}\varphi\big)(x):=\frac{1}{\Gamma(\mu)}\int_0^x (x-t)^{\mu-1}\,\varphi(t)\,dt.$$
> Es la generalización natural de "integrar $\mu$ veces": para $\mu=n$ entero reproduce la fórmula de
> Cauchy de la integral iterada $n$ veces. Comparando con la definición, con $\mu-1=-\alpha$ (o sea
> $\mu=1-\alpha$, que cae en $(0,1)$):
> $$f(x)=\int_0^x\frac{\varphi(t)}{(x-t)^{\alpha}}\,dt=\Gamma(1-\alpha)\,\big(I^{\,1-\alpha}\varphi\big)(x).$$
> Es decir: **resolver la ecuación de Abel = invertir una integral fraccionaria**. Y el inverso de
> integrar $1-\alpha$ veces es **derivar** $1-\alpha$ veces: la incógnita es
> $\varphi=\dfrac{1}{\Gamma(1-\alpha)}\,D^{\,1-\alpha}f$, donde $D^{\,1-\alpha}$ es la
> [[Calculo Fraccionario/index| derivada fraccionaria]] de Riemann-Liouville.

> [!teorema] Fórmula de inversión de Abel generalizada
> Si $f$ es suficientemente regular (basta $f$ absolutamente continua con $f(0)=0$) y
> $0<\alpha<1$, la ecuación
> $$f(x)=\int_0^x\frac{\varphi(t)}{(x-t)^{\alpha}}\,dt$$
> tiene **solución única**
> $$\varphi(x)=\frac{\operatorname{sen}(\pi\alpha)}{\pi}\,\frac{d}{dx}\int_0^x\frac{f(t)}{(x-t)^{\,1-\alpha}}\,dt.$$

> [!demostracion]
> **Paso 1 — Aplicar el núcleo "complementario".** El núcleo de Abel es $(x-t)^{-\alpha}$; su
> complemento es $(x-t)^{-(1-\alpha)}=(x-t)^{\alpha-1}$, con exponentes que **suman $-1$**. La estrategia
> es aplicar el operador integral de núcleo complementario a ambos lados. Multiplicamos $f(s)$ por
> $(x-s)^{\alpha-1}$ e integramos en $s\in[0,x]$:
> $$J(x):=\int_0^x (x-s)^{\alpha-1}\,f(s)\,ds
> =\int_0^x (x-s)^{\alpha-1}\!\left[\int_0^s \frac{\varphi(t)}{(s-t)^{\alpha}}\,dt\right]ds.$$
>
> **Paso 2 — Intercambiar el orden (Fubini) y reconocer una Beta.** El dominio es $0\le t\le s\le x$;
> intercambiando,
> $$J(x)=\int_0^x \varphi(t)\left[\int_t^x (x-s)^{\alpha-1}(s-t)^{-\alpha}\,ds\right]dt.$$
> La integral interior, con el cambio $s=t+(x-t)u$, $u\in[0,1]$, es **constante** (no depende de $x$ ni
> de $t$):
> $$\int_t^x (x-s)^{\alpha-1}(s-t)^{-\alpha}\,ds=\int_0^1 (1-u)^{\alpha-1}u^{-\alpha}\,du
> =B(\alpha,\,1-\alpha)=\Gamma(\alpha)\Gamma(1-\alpha)=\frac{\pi}{\operatorname{sen}(\pi\alpha)},$$
> usando la **fórmula de reflexión** de Euler $\Gamma(\alpha)\Gamma(1-\alpha)=\pi/\operatorname{sen}(\pi\alpha)$.
>
> **Paso 3 — La convolución de los dos núcleos colapsa a una primitiva.** Sustituyendo,
> $$\int_0^x (x-s)^{\alpha-1}\,f(s)\,ds=\frac{\pi}{\operatorname{sen}(\pi\alpha)}\int_0^x \varphi(t)\,dt.$$
> Aplicar los núcleos $(x-t)^{-\alpha}$ y $(x-s)^{\alpha-1}$ uno tras otro **deshace** la singularidad y
> deja solo la integral simple de $\varphi$, multiplicada por la constante Beta. (En lenguaje
> fraccionario: $I^{\,\alpha}I^{\,1-\alpha}=I^{1}$, integrar una vez.)
>
> **Paso 4 — Derivar para despejar.** Derivando ambos lados respecto de $x$ y despejando $\varphi$:
> $$\varphi(x)=\frac{\operatorname{sen}(\pi\alpha)}{\pi}\,\frac{d}{dx}\int_0^x\frac{f(t)}{(x-t)^{\,1-\alpha}}\,dt.
> \qquad\blacksquare$$

> [!info] Lazo profundo con el cálculo fraccionario
> Esta ecuación no es un caso aislado: **es** la teoría de las integrales y derivadas de orden no entero
> vista desde el lado de las ecuaciones integrales. La fórmula de inversión es literalmente
> $\varphi=\Gamma(1-\alpha)^{-1}D^{\,1-\alpha}f$, donde $D^{\,1-\alpha}=\frac{d}{dx}I^{\,\alpha}$ es la
> **derivada fraccionaria de Riemann-Liouville**. Históricamente fue justo el problema de Abel el que
> motivó a definir derivadas de orden $\tfrac12$. Todo el aparato (semigrupo $I^\mu I^\nu=I^{\mu+\nu}$,
> reflexión de Euler) se desarrolla en [[Calculo Fraccionario/index| cálculo fraccionario]].

> [!proposicion] Por qué la inversión es estable aquí
> Una Volterra de **primera especie** suele ser un problema inverso **mal planteado** porque invertirla
> equivale a derivar (amplifica el ruido). La Abel generalizada es la excepción **amable**: su inversión
> exige solo **una derivada fraccionaria de orden $1-\alpha<1$**, no una derivada entera completa. Cuanto
> más cerca esté $\alpha$ de $1$ (singularidad más fuerte), **menor** es el orden de derivación
> necesario para invertir y más estable resulta la reconstrucción.

> [!warning]
> La fórmula exige $f(0)=0$ y suficiente regularidad de $f$; si no, hay que escribir la inversión en la
> forma "derivada dentro de la integral" o regularizar. Y cuidado con el orden de las potencias: el
> núcleo directo tiene exponente $-\alpha$ y el de inversión $-(1-\alpha)$; **suman $-1$**, esa es la
> firma de que son complementarios.

## Resumen

> [!resumen]
> | Objeto | Expresión | Papel |
> |---|---|---|
> | Ecuación directa | $f(x)=\displaystyle\int_0^x (x-t)^{-\alpha}\varphi(t)\,dt$ | Volterra 1ª especie, débilmente singular |
> | Lectura fraccionaria | $f=\Gamma(1-\alpha)\,I^{\,1-\alpha}\varphi$ | integral de orden $1-\alpha$ |
> | Inversión | $\varphi=\dfrac{\operatorname{sen}\pi\alpha}{\pi}\dfrac{d}{dx}\displaystyle\int_0^x (x-t)^{\alpha-1}f(t)\,dt$ | derivada fraccionaria $D^{\,1-\alpha}f$ |
> | Constante clave | $B(\alpha,1-\alpha)=\dfrac{\pi}{\operatorname{sen}\pi\alpha}$ | reflexión de Euler; colapsa la doble convolución |
> | Caso $\alpha=\tfrac12$ | tautócrona | [[Problema de Abel\| Abel]] clásico |

> [!corolario]
> La ecuación de Abel generalizada se resuelve **aplicando el núcleo complementario y derivando una vez**:
> la doble convolución de potencias da una Beta constante (reflexión de Euler) que deja $\int_0^x\varphi$,
> y basta derivar. Conceptualmente: la integral de Abel es una **integral fraccionaria** y resolverla es
> tomar una **derivada fraccionaria**. Es el único miembro de la familia singular con inversión cerrada
> elemental.

> [!referencia]
> - El caso físico $\alpha=\tfrac12$: [[Problema de Abel]].
> - El marco que la engloba: [[Calculo Fraccionario/index]].
> - El mapa de la sección: [[Singulares/index]].
