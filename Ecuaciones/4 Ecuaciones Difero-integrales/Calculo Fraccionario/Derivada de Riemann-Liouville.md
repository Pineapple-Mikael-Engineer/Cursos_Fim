---
title: Derivada de Riemann-Liouville
order: 3
tags:
  - ecuaciones
  - difero-integrales
  - teoria
  - calculo-fraccionario
  - riemann-liouville
draft: false
aliases:
  - derivada fraccionaria de Riemann-Liouville
  - derivada de Riemann-Liouville
  - Riemann-Liouville derivative
  - fractional derivative
---

# Derivada de Riemann-Liouville $D^{\alpha}$

> [!definicion]
> La **derivada fraccionaria de Riemann-Liouville** de orden $\alpha>0$, con $n=\lceil\alpha\rceil$ (el menor entero $\geq\alpha$), se obtiene **integrando** fraccionariamente hasta orden $n-\alpha$ y luego **derivando** $n$ veces enteras:
> $$D^{\alpha}f=\frac{d^{n}}{dx^{n}}\,I^{\,n-\alpha}f.$$
> En el caso más usado $0<\alpha<1$ (entonces $n=1$) esto es
> $$D^{\alpha}f(x)=\frac{1}{\Gamma(1-\alpha)}\,\frac{d}{dx}\int_0^x (x-t)^{-\alpha}\,f(t)\,dt.$$
> El orden es: **primero integrar, después derivar**. Invertir ese orden da otra cosa —la [[Derivada de Caputo| derivada de Caputo]]—.

> [!info]
> Es la derivada "matemática" del [[Calculo Fraccionario/index| cálculo fraccionario]]: se construye directamente sobre la [[Integral de Riemann-Liouville| integral fraccionaria]] $I^{n-\alpha}$ y reproduce la regla de potencias del [[Operador Differintegral| differintegral]]. Su rareza con las constantes y las condiciones iniciales motiva, por contraste, la [[Derivada de Caputo| derivada de Caputo]]. Capítulo: [[4 Ecuaciones Difero-integrales/index| Ecuaciones difero-integrales]].

---

## Ejemplo

> [!ejemplo] La media derivada de $f(x)=x$
> Calculamos $D^{1/2}x$. Aquí $\alpha=\tfrac12$, $\mu=1$, y $n=\lceil\tfrac12\rceil=1$. **Vía directa (regla de potencias).** Con $D^{\alpha}x^{\mu}=\dfrac{\Gamma(\mu+1)}{\Gamma(\mu+1-\alpha)}x^{\mu-\alpha}$,
> $$D^{1/2}x=\frac{\Gamma(2)}{\Gamma(2-\tfrac12)}\,x^{1-1/2}=\frac{\Gamma(2)}{\Gamma(3/2)}\,x^{1/2}
> =\frac{1}{\tfrac12\sqrt{\pi}}\,x^{1/2}=\frac{2}{\sqrt{\pi}}\sqrt{x}.$$
> **Vía definición (integrar y luego derivar), para verlo en acción.** Primero $I^{1/2}x$ usando la integral fraccionaria con $\mu=1$:
> $$I^{1/2}x=\frac{\Gamma(2)}{\Gamma(2+\tfrac12)}x^{1+1/2}=\frac{1}{\Gamma(5/2)}x^{3/2},\qquad \Gamma(5/2)=\tfrac34\sqrt{\pi}.$$
> Ahora derivamos una vez ($n=1$): $\dfrac{d}{dx}\!\left(\dfrac{x^{3/2}}{\tfrac34\sqrt\pi}\right) =\dfrac{1}{\tfrac34\sqrt\pi}\cdot\tfrac32 x^{1/2}=\dfrac{2}{\sqrt\pi}\sqrt{x}.$ $\checkmark$ Ambas vías coinciden: $D^{1/2}x=\dfrac{2}{\sqrt{\pi}}\sqrt{x}$. Y, como debe ser, aplicando $D^{1/2}$ otra vez se recupera $D^{1}x=1$.

---

## En qué consiste

> [!algoritmo] Cómo calcular $D^{\alpha}f$
> 1. Fijar $n=\lceil\alpha\rceil$ (para $0<\alpha<1$ es $n=1$).
> 2. **Integrar** fraccionariamente: formar $g=I^{\,n-\alpha}f$ con la [[Integral de Riemann-Liouville| integral $I^{n-\alpha}$]].
> 3. **Derivar** $n$ veces de forma clásica: $D^{\alpha}f=\dfrac{d^{n}}{dx^{n}}g$.
> 4. Sobre potencias, atajar con la regla de potencias de abajo.

> [!teorema] Regla de las potencias
> Para $\mu>-1$,
> $$D^{\alpha}x^{\mu}=\frac{\Gamma(\mu+1)}{\Gamma(\mu+1-\alpha)}\,x^{\mu-\alpha},$$
> que coincide exactamente con la del [[Operador Differintegral| differintegral]] (con $q=\alpha$).

> [!demostracion]
> **Paso 1 — integrar $n-\alpha$.** Por la regla de potencias de la integral fraccionaria,
> $$I^{\,n-\alpha}x^{\mu}=\frac{\Gamma(\mu+1)}{\Gamma(\mu+1+n-\alpha)}\,x^{\mu+n-\alpha}.$$
> **Paso 2 — derivar $n$ veces.** Para un monomio $x^{p}$ con $p=\mu+n-\alpha$, $\dfrac{d^{n}}{dx^{n}}x^{p}=\dfrac{\Gamma(p+1)}{\Gamma(p+1-n)}x^{p-n}$. Aplicándolo,
> $$D^{\alpha}x^{\mu}=\frac{\Gamma(\mu+1)}{\Gamma(\mu+1+n-\alpha)}\cdot\frac{\Gamma(\mu+n-\alpha+1)}{\Gamma(\mu+n-\alpha+1-n)}\,x^{\mu+n-\alpha-n}.$$
> **Paso 3 — telescopio de Gammas.** El factor $\Gamma(\mu+1+n-\alpha)=\Gamma(\mu+n-\alpha+1)$ se cancela, y el exponente queda $\mu-\alpha$:
> $$D^{\alpha}x^{\mu}=\frac{\Gamma(\mu+1)}{\Gamma(\mu+1-\alpha)}\,x^{\mu-\alpha}.\qquad\blacksquare$$

> [!proposicion] No invierte exactamente a la integral por la izquierda
> Se cumple $D^{\alpha}I^{\alpha}f=f$ (la derivada deshace a la integral fraccionaria). Pero $I^{\alpha}D^{\alpha}f\neq f$ en general: reaparecen **términos de borde** con los valores iniciales,
> $$I^{\alpha}D^{\alpha}f(x)=f(x)-\sum_{k=1}^{n}\big[D^{\alpha-k}f\big]_{x=0}\,\frac{x^{\alpha-k}}{\Gamma(\alpha-k+1)}.$$
> Esos términos contienen **derivadas fraccionarias evaluadas en $0$**, no valores de $f$.

> [!warning] La derivada de una constante NO es cero
> Aplicando la regla con $\mu=0$ (es decir $f=1=x^{0}$):
> $$D^{\alpha}1=\frac{\Gamma(1)}{\Gamma(1-\alpha)}\,x^{-\alpha}=\frac{x^{-\alpha}}{\Gamma(1-\alpha)}\neq 0.$$
> Una constante "tiene" media derivada no nula. Más grave para las aplicaciones: los **problemas de valor inicial** con la derivada de Riemann-Liouville exigen condiciones del tipo $\big[D^{\alpha-1}f\big]_{x=0}$ —**derivadas fraccionarias** en el origen—, magnitudes sin lectura física clara. Esto es lo que motiva pasar a la [[Derivada de Caputo| derivada de Caputo]], cuyas condiciones iniciales son las clásicas $f(0),f'(0),\dots$

## Resumen

> [!resumen]
> | Objeto | Expresión |
> |:--|:--|
> | Definición | $D^{\alpha}f=\dfrac{d^{n}}{dx^{n}}I^{\,n-\alpha}f$, con $n=\lceil\alpha\rceil$ |
> | Caso $0<\alpha<1$ | $D^{\alpha}f=\dfrac{1}{\Gamma(1-\alpha)}\dfrac{d}{dx}\int_0^x (x-t)^{-\alpha}f(t)\,dt$ |
> | Orden | **integrar** $n-\alpha$, **luego derivar** $n$ |
> | Potencias | $D^{\alpha}x^{\mu}=\dfrac{\Gamma(\mu+1)}{\Gamma(\mu+1-\alpha)}x^{\mu-\alpha}$ |
> | Constante | $D^{\alpha}1=\dfrac{x^{-\alpha}}{\Gamma(1-\alpha)}\neq 0$ |
> | Inversa | $D^{\alpha}I^{\alpha}f=f$, pero $I^{\alpha}D^{\alpha}f\neq f$ |

> [!corolario]
> La derivada de Riemann-Liouville es elegante y mecánica —integrar y derivar—, pero paga un precio: no anula constantes y arrastra condiciones iniciales fraccionarias difíciles de interpretar. Es la referencia matemática; para la física, su gemela con el orden invertido —la [[Derivada de Caputo| de Caputo]]— resulta más cómoda.

> [!referencia]
> - Sobre lo que se construye: [[Integral de Riemann-Liouville]].
> - La intuición de orden arbitrario: [[Operador Differintegral]].
> - La alternativa física: [[Derivada de Caputo]].
