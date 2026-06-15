---
title: "Relaciones de Maxwell"
tags:
  - termodinamica
  - relaciones_termodinamicas
  - maxwell
  - potenciales_termodinamicos
draft: false
aliases:
  - Maxwell relations
  - relaciones de Maxwell
---

# Relaciones de Maxwell

> [!definicion]
> Las **relaciones de Maxwell** son cuatro igualdades entre derivadas parciales de variables de estado, obtenidas al imponer la condición de Schwarz $(\partial M/\partial y)_x = (\partial N/\partial x)_y$ sobre los diferenciales exactos de los cuatro [[Potenciales Termodinamicos/index | potenciales termodinámicos]]. Su propósito central: las relaciones con $T$ constante (3.ª y 4.ª) sustituyen derivadas de $s$ —inaccesibles al experimento— por derivadas de $P$ y $v$ de la [[Ecuaciones de Estado/index | ecuación de estado]], habilitando el cálculo de $\Delta s$ sin medir entropía.

---

## Condición de exactitud

> [!lema] Condición de Schwarz
> Sea $z = z(x,y)$ una función de estado con diferencial exacto $dz = M\,dx + N\,dy$:
> $$M = \left(\frac{\partial z}{\partial x}\right)_y, \qquad N = \left(\frac{\partial z}{\partial y}\right)_x.$$
> La existencia de $z$ como función del punto exige igualdad de derivadas cruzadas:
> $$\left(\frac{\partial M}{\partial y}\right)_x = \left(\frac{\partial N}{\partial x}\right)_y.$$
> Aplicar esta condición a cada uno de los cuatro potenciales genera una relación de Maxwell distinta.

---

## Derivación completa de las cuatro relaciones

### 1.ª relación — desde $u(s,v)$

> [!demostracion]
> **Paso 1 — Diferencial de $u$.** De la primera y segunda ley combinadas para proceso reversible:
> $$du = T\,ds - P\,dv.$$
> Variables naturales $(s,v)$: coeficientes $M = T$, $N = -P$.
>
> **Paso 2 — Condición de Schwarz** con $x=s$, $y=v$:
> $$\left(\frac{\partial T}{\partial v}\right)_s = \left(\frac{\partial (-P)}{\partial s}\right)_v.$$
>
> **Paso 3 — 1.ª relación de Maxwell:**
> $$\boxed{\left(\frac{\partial T}{\partial v}\right)_s = -\left(\frac{\partial P}{\partial s}\right)_v.} \qquad \blacksquare$$

### 2.ª relación — desde $h(s,P)$

> [!demostracion]
> **Paso 1 — Diferencial de $h$.** De $h = u + Pv$, diferenciando y sustituyendo $du = T\,ds - P\,dv$:
> $$dh = T\,ds - P\,dv + P\,dv + v\,dP = T\,ds + v\,dP.$$
> Variables naturales $(s,P)$: coeficientes $M = T$, $N = v$.
>
> **Paso 2 — Condición de Schwarz** con $x=s$, $y=P$:
> $$\left(\frac{\partial T}{\partial P}\right)_s = \left(\frac{\partial v}{\partial s}\right)_P.$$
>
> **Paso 3 — 2.ª relación de Maxwell:**
> $$\boxed{\left(\frac{\partial T}{\partial P}\right)_s = \left(\frac{\partial v}{\partial s}\right)_P.} \qquad \blacksquare$$

### 3.ª relación — desde $f(T,v)$

> [!demostracion]
> **Paso 1 — Diferencial de $f$.** De $f = u - Ts$:
> $$df = du - T\,ds - s\,dT = (T\,ds - P\,dv) - T\,ds - s\,dT = -s\,dT - P\,dv.$$
> Variables naturales $(T,v)$: coeficientes $M = -s$, $N = -P$.
>
> **Paso 2 — Condición de Schwarz** con $x=T$, $y=v$:
> $$\left(\frac{\partial(-s)}{\partial v}\right)_T = \left(\frac{\partial(-P)}{\partial T}\right)_v \;\Longrightarrow\; -\left(\frac{\partial s}{\partial v}\right)_T = -\left(\frac{\partial P}{\partial T}\right)_v.$$
>
> **Paso 3 — 3.ª relación de Maxwell** (la más usada en variables $(T,v)$):
> $$\boxed{\left(\frac{\partial s}{\partial v}\right)_T = \left(\frac{\partial P}{\partial T}\right)_v = \frac{\alpha}{\kappa_T}.} \qquad \blacksquare$$
> La forma $\alpha/\kappa_T$ proviene de la [[Identidades/Regla Ciclica | regla cíclica]] $(\partial P/\partial T)_v = \alpha/\kappa_T$ con $\alpha = (1/v)(\partial v/\partial T)_P$, $\kappa_T = -(1/v)(\partial v/\partial P)_T$.

### 4.ª relación — desde $g(T,P)$

> [!demostracion]
> **Paso 1 — Diferencial de $g$.** De $g = h - Ts$:
> $$dg = dh - T\,ds - s\,dT = (T\,ds + v\,dP) - T\,ds - s\,dT = -s\,dT + v\,dP.$$
> Variables naturales $(T,P)$: coeficientes $M = -s$, $N = v$.
>
> **Paso 2 — Condición de Schwarz** con $x=T$, $y=P$:
> $$\left(\frac{\partial(-s)}{\partial P}\right)_T = \left(\frac{\partial v}{\partial T}\right)_P \;\Longrightarrow\; -\left(\frac{\partial s}{\partial P}\right)_T = \left(\frac{\partial v}{\partial T}\right)_P.$$
>
> **Paso 3 — 4.ª relación de Maxwell** (la más usada en variables $(T,P)$):
> $$\boxed{\left(\frac{\partial s}{\partial P}\right)_T = -\left(\frac{\partial v}{\partial T}\right)_P = -v\,\alpha.} \qquad \blacksquare$$

---

## Tabla resumen y regla de signos

> [!teoria] Las cuatro relaciones
> | Potencial | Var. naturales | Diferencial | Relación de Maxwell |
> |:---:|:---:|:---|:---|
> | $u$ | $(s,v)$ | $du = T\,ds - P\,dv$ | $(\partial T/\partial v)_s = -(\partial P/\partial s)_v$ |
> | $h$ | $(s,P)$ | $dh = T\,ds + v\,dP$ | $(\partial T/\partial P)_s = +(\partial v/\partial s)_P$ |
> | $f$ | $(T,v)$ | $df = -s\,dT - P\,dv$ | $(\partial s/\partial v)_T = +(\partial P/\partial T)_v$ |
> | $g$ | $(T,P)$ | $dg = -s\,dT + v\,dP$ | $(\partial s/\partial P)_T = -(\partial v/\partial T)_P$ |
>
> **Regla de los signos.** El signo de la relación es $-$ cuando en el diferencial del potencial el par de coeficientes $(M,N)$ tiene signos opuestos (como en $u$: $+T$ y $-P$, o en $g$: $-s$ y $+v$). Es $+$ cuando tienen el mismo signo (como en $h$: $+T$ y $+v$, o en $f$: $-s$ y $-P$).
>
> ![[maxwell_rueda_potenciales.svg|460]]
> *"Rueda de Maxwell": los cuatro potenciales en los vértices, variables naturales en los lados, signos de las relaciones en las diagonales.*

---

## Las relaciones 3.ª y 4.ª: valor práctico central

> [!proposicion]
> Las relaciones 3.ª (desde $f$) y 4.ª (desde $g$) expresan $(\partial s/\partial v)_T$ y $(\partial s/\partial P)_T$ en términos de la ecuación de estado $P$-$v$-$T$:
> $$\left(\frac{\partial s}{\partial v}\right)_T = \left(\frac{\partial P}{\partial T}\right)_v, \qquad \left(\frac{\partial s}{\partial P}\right)_T = -\left(\frac{\partial v}{\partial T}\right)_P.$$
> Sustituyendo estas expresiones en las expansiones de $s(T,v)$ y $s(T,P)$ se obtienen directamente las [[TdS | ecuaciones $T\,ds$]], que permiten integrar $\Delta s$ entre dos estados cualesquiera.

---

## Verificación: gas ideal y gas de van der Waals

> [!ejemplo]
> **Gas ideal** ($Pv = RT$). Verificar la 3.ª y la 4.ª relación.
>
> **3.ª relación.** $(\partial s/\partial v)_T$: de $ds = c_v\,dT/T + R\,dv/v$ (ver [[TdS]]), a $T$ cte. → $(\partial s/\partial v)_T = R/v$.
> Desde la EdE: $(\partial P/\partial T)_v = R/v$. Iguales. $\checkmark$
>
> **4.ª relación.** $(\partial s/\partial P)_T$: de $ds = c_p\,dT/T - R\,dP/P$, a $T$ cte. → $(\partial s/\partial P)_T = -R/P$.
> Desde la EdE: $-(\partial v/\partial T)_P = -R/P$. Iguales. $\checkmark\;\blacksquare$

> [!ejemplo]
> **Gas de van der Waals** $(P + a/v^2)(v-b) = RT$.
>
> **Paso 1 — Calcular $(\partial P/\partial T)_v$.** Despejando $P = RT/(v-b) - a/v^2$:
> $$\left(\frac{\partial P}{\partial T}\right)_v = \frac{R}{v-b}.$$
>
> **Paso 2 — Interpretación.** El resultado difiere del gas ideal $R/v$ solo en el denominador $(v-b)$: el volumen excluido por las moléculas aumenta el cambio de entropía con $v$ comparado con el gas ideal. El parámetro $a$ (presión de cohesión) no aparece: la atracción intermolecular no afecta directamente a $(\partial s/\partial v)_T$.
>
> **Paso 3 — Integración isoterma** ($T = \text{cte}$) de $v_1$ a $v_2$:
> $$\Delta s\big|_T = R\ln\frac{v_2 - b}{v_1 - b}.$$
> Reemplaza a $R\ln(v_2/v_1)$ del gas ideal. Cuando $v \to b$, $\Delta s \to -\infty$: es termodinámicamente imposible comprimir por debajo del volumen excluido $b$. $\blacksquare$

---

## Aplicación: relación de Clapeyron

> [!proposicion]
> La condición de equilibrio de fases $g_l = g_v$ implica, sobre la curva de saturación, $dg_l = dg_v$. Usando $dg = -s\,dT + v\,dP$:
> $$(-s_l + s_v)\,dT = (v_v - v_l)\,dP \;\Longrightarrow\; \left(\frac{dP}{dT}\right)_{\rm sat} = \frac{s_v - s_l}{v_v - v_l} = \frac{h_{fg}}{T\,v_{fg}}.$$
> La exactitud de $dg$ (que produce la 4.ª relación de Maxwell) es la hipótesis de fondo. Ver [[Diagramas de Fase]] para la integración (Clausius-Clapeyron).

---

## Relación con otras notas

> [!info]
> - Las cuatro relaciones nacen de los cuatro [[Potenciales Termodinamicos/index | potenciales termodinámicos]].
> - Las 3.ª y 4.ª son la entrada a las [[TdS | ecuaciones $T\,ds$]] y a la relación [[Cp Cv/index | $c_p - c_v$]].
> - La [[Identidades/Regla Ciclica | regla cíclica]] reescribe $(\partial P/\partial T)_v = \alpha/\kappa_T$ y $(\partial v/\partial T)_P = v\alpha$.
> - El [[Jacobianos/index | método de Jacobianos]] permite derivar las cuatro relaciones desde una sola identidad algebraica.

> [!warning]
> Válidas para sustancias simples compresibles en equilibrio termodinámico. Con trabajo adicional (magnético, eléctrico, superficial) aparecen potenciales y relaciones de Maxwell adicionales.

> [!referencia]
> Çengel & Boles, *Termodinámica*, §12-1 a 12-2; Callen, *Thermodynamics*, §5-1 a 5-3; Moran & Shapiro, §11.1; Borgnakke & Sonntag, §13.2.
