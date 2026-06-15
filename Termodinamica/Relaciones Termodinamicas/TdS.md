---
title: "Ecuaciones $TdS$"
tags:
  - termodinamica
  - relaciones_termodinamicas
  - entropia
  - tds
draft: false
aliases:
  - TdS equations
  - ecuaciones Tds
  - Relaciones TdS
  - Gibbs equations
---

# Ecuaciones $TdS$

> [!definicion]
> Las **ecuaciones $T\,ds$** expresan el diferencial de entropía específica en términos de cantidades medibles ($T$, $P$, $v$, $c_p$, $c_v$), eliminando las derivadas de $s$ mediante las [[Maxwell | relaciones de Maxwell]]. Son la herramienta operativa central para calcular $\Delta s$ entre dos estados cualesquiera de una sustancia real, sin medir entropía de forma directa.

---

## Las dos ecuaciones

> [!teorema]
> Para una sustancia simple compresible (propiedades específicas):
> $$T\,ds = c_v\,dT + T\!\left(\frac{\partial P}{\partial T}\right)_v\!dv \qquad \textbf{(1.ª ecuación }T\!ds\textbf{)}$$
> $$T\,ds = c_p\,dT - T\!\left(\frac{\partial v}{\partial T}\right)_P\!dP \qquad \textbf{(2.ª ecuación }T\!ds\textbf{)}$$
> La 1.ª conviene cuando el proceso se describe en variables $(T,v)$; la 2.ª cuando se describe en $(T,P)$.

---

## Derivación completa de ambas ecuaciones

### 1.ª ecuación $T\,ds$ — desde $s(T,v)$

> [!demostracion]
> **Paso 1 — Diferencial total de $s = s(T,v)$:**
> $$ds = \left(\frac{\partial s}{\partial T}\right)_v\!dT + \left(\frac{\partial s}{\partial v}\right)_T\!dv.$$
>
> **Paso 2 — Identificar $(\partial s/\partial T)_v$.** A volumen constante, $\delta q_{\rm rev} = T\,ds = du$, por lo que:
> $$c_v \equiv \left(\frac{\partial u}{\partial T}\right)_v = T\left(\frac{\partial s}{\partial T}\right)_v \;\Longrightarrow\; \left(\frac{\partial s}{\partial T}\right)_v = \frac{c_v}{T}.$$
>
> **Paso 3 — Sustituir $(\partial s/\partial v)_T$ con la 3.ª relación de [[Maxwell]]** (desde $f$, exactitud de $df = -s\,dT - P\,dv$):
> $$\left(\frac{\partial s}{\partial v}\right)_T = \left(\frac{\partial P}{\partial T}\right)_v.$$
>
> **Paso 4 — Combinar y multiplicar por $T$:**
> $$T\,ds = c_v\,dT + T\!\left(\frac{\partial P}{\partial T}\right)_v\!dv. \qquad \blacksquare$$

### 2.ª ecuación $T\,ds$ — desde $s(T,P)$

> [!demostracion]
> **Paso 1 — Diferencial total de $s = s(T,P)$:**
> $$ds = \left(\frac{\partial s}{\partial T}\right)_P\!dT + \left(\frac{\partial s}{\partial P}\right)_T\!dP.$$
>
> **Paso 2 — Identificar $(\partial s/\partial T)_P$.** A presión constante, $\delta q_{\rm rev} = T\,ds = dh$, por lo que:
> $$c_p \equiv \left(\frac{\partial h}{\partial T}\right)_P = T\left(\frac{\partial s}{\partial T}\right)_P \;\Longrightarrow\; \left(\frac{\partial s}{\partial T}\right)_P = \frac{c_p}{T}.$$
>
> **Paso 3 — Sustituir $(\partial s/\partial P)_T$ con la 4.ª relación de [[Maxwell]]** (desde $g$, exactitud de $dg = -s\,dT + v\,dP$):
> $$\left(\frac{\partial s}{\partial P}\right)_T = -\left(\frac{\partial v}{\partial T}\right)_P.$$
>
> **Paso 4 — Combinar y multiplicar por $T$:**
> $$T\,ds = c_p\,dT - T\!\left(\frac{\partial v}{\partial T}\right)_P\!dP. \qquad \blacksquare$$

> [!info]
> La 2.ª ecuación no es "análoga" a la 1.ª de forma superficial: parte de una expansión diferente ($s(T,P)$ frente a $s(T,v)$) y usa una relación de Maxwell de un potencial distinto ($g$ frente a $f$). La estructura es paralela pero las variables naturales y los potenciales de origen son distintos.

---

## Integración: cambio de entropía entre dos estados

> [!proposicion]
> Para cualquier proceso entre estados $1$ y $2$ (la ruta de integración es libre; $s$ es función de estado):
> $$\Delta s = \int_1^2 \frac{c_v}{T}\,dT + \int_1^2 \left(\frac{\partial P}{\partial T}\right)_v\!dv = \int_1^2 \frac{c_p}{T}\,dT - \int_1^2 \left(\frac{\partial v}{\partial T}\right)_P\!dP.$$
> Estrategia conveniente: integrar por la ruta $1\to A$ (isoterma, $dT=0$) seguida de $A\to 2$ (a $v$ ó $P$ constante). Las dos formas dan el mismo resultado.
>
> ![[tds_rutas_integracion.svg|440]]
> *Dos rutas equivalentes de integración: isoterma seguida de isocora (izquierda) o isobara (derecha). La entropía es función de estado.*

---

## Gas ideal

> [!ejemplo]
> Con $Pv = RT$: $(\partial P/\partial T)_v = R/v$ y $(\partial v/\partial T)_P = R/P$.
>
> **1.ª ecuación $T\,ds$:**
> $$T\,ds = c_v\,dT + \frac{RT}{v}\,dv \;\Rightarrow\; ds = c_v\frac{dT}{T} + R\frac{dv}{v}.$$
> Integrando con $c_v$ constante:
> $$\Delta s = c_v\ln\frac{T_2}{T_1} + R\ln\frac{v_2}{v_1}.$$
>
> **2.ª ecuación $T\,ds$:**
> $$T\,ds = c_p\,dT - \frac{RT}{P}\,dP \;\Rightarrow\; ds = c_p\frac{dT}{T} - R\frac{dP}{P}.$$
> Integrando:
> $$\Delta s = c_p\ln\frac{T_2}{T_1} - R\ln\frac{P_2}{P_1}. \qquad \blacksquare$$

---

## Gas de van der Waals

> [!ejemplo]
> $(P + a/v^2)(v-b) = RT$. Calcular $\Delta s$ entre $(T_1,v_1)$ y $(T_2,v_2)$.
>
> **Paso 1 — Derivada para la 1.ª ecuación.** De $P = RT/(v-b) - a/v^2$:
> $$\left(\frac{\partial P}{\partial T}\right)_v = \frac{R}{v-b}.$$
> El parámetro $a$ (atracción intermolecular) no contribuye: $\partial(a/v^2)/\partial T = 0$.
>
> **Paso 2 — 1.ª ecuación $T\,ds$ para vdW:**
> $$T\,ds = c_v^{\rm vdW}(T,v)\,dT + \frac{RT}{v-b}\,dv.$$
>
> **Paso 3 — Integrar por la ruta** $1\to A=(T_1,v_2)$ (isoterma a $T_1$) $\to 2=(T_2,v_2)$ (isocora a $v_2$):
> $$\Delta s = R\ln\frac{v_2-b}{v_1-b} + \int_{T_1}^{T_2}\frac{c_v^{\rm vdW}(T,v_2)}{T}\,dT.$$
>
> **Paso 4 — Comparación con el gas ideal.** El término isotermo es $R\ln[(v_2-b)/(v_1-b)]$ en lugar de $R\ln(v_2/v_1)$: el volumen excluido $b$ reduce el espacio efectivo disponible. El parámetro $a$ no aparece porque $(\partial P/\partial T)_v$ no depende de $a$. Para $c_v^{\rm vdW} \approx c_v^{\rm ideal}$ (válido a bajas presiones reducidas):
> $$\Delta s \approx c_v\ln\frac{T_2}{T_1} + R\ln\frac{v_2-b}{v_1-b}. \qquad \blacksquare$$

---

## Sustancia incompresible

> [!ejemplo]
> $dv = 0$, $c_p \approx c_v = c$. La 1.ª ecuación con $dv = 0$:
> $$T\,ds = c\,dT \;\Longrightarrow\; \Delta s = c\,\ln\frac{T_2}{T_1}.$$
> El cambio de entropía depende únicamente de la temperatura. Usado para líquidos y sólidos en rangos moderados de presión. $\blacksquare$

---

## Procesos isentrópicos

> [!proposicion]
> Imponiendo $ds = 0$ en cada ecuación:
>
> **Desde la 1.ª:**
> $$dT\big|_{ds=0} = -\frac{T}{c_v}\left(\frac{\partial P}{\partial T}\right)_v\!dv.$$
> Para gas ideal: $dT/T = -(R/c_v)\,dv/v$ → integra a $Tv^{\gamma-1} = \text{cte}$.
>
> **Desde la 2.ª:**
> $$dT\big|_{ds=0} = \frac{T}{c_p}\left(\frac{\partial v}{\partial T}\right)_P\!dP.$$
> Para gas ideal: $dT/T = (R/c_p)\,dP/P$ → integra a $T\,P^{-(\gamma-1)/\gamma} = \text{cte}$.
>
> Combinando ambas con $Pv = RT$: la relación isentrópica $Pv^\gamma = \text{cte}$.

---

## Consecuencia: $c_p - c_v$

> [!proposicion]
> Igualando las dos ecuaciones $T\,ds$ y usando $dv = (\partial v/\partial T)_P\,dT + (\partial v/\partial P)_T\,dP$ para expresar $dv$ en función de las variables independientes de la 2.ª ecuación se obtiene, comparando coeficiente de $dT$:
> $$c_p - c_v = T\!\left(\frac{\partial P}{\partial T}\right)_v\!\left(\frac{\partial v}{\partial T}\right)_P = \frac{Tv\,\alpha^2}{\kappa_T} \ge 0.$$
> La prueba completa, incluyendo el paso con la [[Identidades/index | regla triple producto]], está en [[Cp Cv/index | $c_p - c_v$]].

---

## Relación con otras notas

> [!info]
> - Construidas sobre las [[Maxwell | relaciones de Maxwell]] (3.ª y 4.ª).
> - Para gas ideal, reproducen los $\Delta s$ de la nota de [[Entropia]].
> - Igualadas derivan la relación [[Cp Cv/index | $c_p - c_v$]].
> - El [[Jacobianos/index | método de Jacobianos]] las genera como casos particulares del determinante jacobiano.

> [!warning]
> Los calores específicos $c_p$, $c_v$ son en general funciones de $T$ (y de $P$ o $v$ fuera del gas ideal): no sacarlos de la integral salvo que se justifique constancia en el rango de integración.

> [!referencia]
> Çengel & Boles, *Termodinámica*, §12-3; Callen, *Thermodynamics*, §7-1; Moran & Shapiro, §11.2; Borgnakke & Sonntag, §13.4.
