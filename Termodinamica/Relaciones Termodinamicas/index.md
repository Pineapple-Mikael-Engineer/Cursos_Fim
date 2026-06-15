---
title: "Relaciones Termodinámicas"
tags:
  - termodinamica
  - relaciones_termodinamicas
  - index
draft: false
aliases:
  - Relaciones Termodinamicas
  - Relaciones termodinámicas generales
---

# Relaciones Termodinámicas

> [!definicion]
> Las **relaciones termodinámicas** son identidades entre derivadas parciales de propiedades de estado cuyo propósito central es expresar cambios de [[Entropia]] —no medible directamente— en función de magnitudes accesibles al experimento: $P$, $v$, $T$, $c_p$, $c_v$. El resultado es que la totalidad de la información termodinámica de cualquier sustancia queda capturada por **tres coeficientes** medibles ($c_p$, $\alpha$, $\kappa_T$) más la [[Ecuaciones de Estado/index | ecuación de estado]] $P$-$v$-$T$, sin requerir hipótesis de gas ideal.

---

## Cadena de derivación

> [!teoria]
> La secuencia lógica es:
>
> **1.** [[Identidades/index | Identidades diferenciales]] — regla recíproca, regla triple producto (cíclica), regla de la cadena: el álgebra de derivadas parciales para funciones de varias variables.
>
> **2.** [[Maxwell]] — exactitud de los cuatro diferenciales $du$, $dh$, $df$, $dg$ → cuatro igualdades de derivadas cruzadas (relaciones de Maxwell), en particular:
> $$\left(\frac{\partial s}{\partial v}\right)_T = \left(\frac{\partial P}{\partial T}\right)_v = \frac{\alpha}{\kappa_T}, \qquad \left(\frac{\partial s}{\partial P}\right)_T = -\left(\frac{\partial v}{\partial T}\right)_P = -v\,\alpha.$$
>
> **3.** [[TdS | Ecuaciones $T\,ds$]] — sustituyendo los resultados de Maxwell en las expansiones de $s(T,v)$ y $s(T,P)$:
> $$T\,ds = c_v\,dT + T\left(\frac{\partial P}{\partial T}\right)_v dv, \qquad T\,ds = c_p\,dT - T\left(\frac{\partial v}{\partial T}\right)_P dP.$$
>
> **4.** [[Cp Cv/index | $c_p - c_v$]] — igualando las dos ecuaciones $T\,ds$ y usando la [[Identidades/index | regla triple producto]]:
> $$c_p - c_v = \frac{Tv\,\alpha^2}{\kappa_T} \ge 0.$$
>
> **5.** [[Jacobianos/index | Jacobianos]] — el determinante jacobiano $J(x,y)/J(a,b)$ unifica toda la cadena anterior: cada relación de Maxwell, cada ecuación $T\,ds$ y cada identidad entre $c_p$, $c_v$, $\kappa_T$, $\kappa_s$ surge como caso particular de un mismo operador.
>
> ![[mapa_relaciones_termodinamicas.svg|560]]
> *Mapa de dependencias de las relaciones termodinámicas. Las flechas indican «se deriva de». Las cajas sombreadas son las notas principales de esta sección.*

---

## Coeficientes de referencia

> [!teoria] Los tres coeficientes experimentales
> Toda sustancia simple compresible en equilibrio queda caracterizada por:
> $$\alpha \equiv \frac{1}{v}\left(\frac{\partial v}{\partial T}\right)_P \;[\mathrm{K}^{-1}], \qquad \kappa_T \equiv -\frac{1}{v}\left(\frac{\partial v}{\partial P}\right)_T \;[\mathrm{Pa}^{-1}], \qquad c_p \;[\mathrm{kJ/(kg\cdot K)}].$$
> - $\alpha$: **coeficiente de dilatación isobárica** (expansividad térmica). Positivo para casi todas las sustancias; negativo para el agua líquida entre 0 y 4 °C.
> - $\kappa_T$: **compresibilidad isoterma**. Siempre positivo (condición de estabilidad mecánica).
> - $c_p$: calor específico a presión constante; junto con $\alpha$ y $\kappa_T$ determina $c_v = c_p - Tv\alpha^2/\kappa_T$.
>
> Con estos tres datos y la ecuación de estado, **todas** las derivadas de primer orden de las propiedades termodinámicas son calculables. La tabla de Bridgman (ver [[Jacobianos/index | Jacobianos]]) sistematiza el proceso.

> [!proposicion] Dos identidades exactas entre coeficientes
> Sin hipótesis adicionales:
> $$c_p - c_v = \frac{Tv\,\alpha^2}{\kappa_T}, \qquad \gamma \equiv \frac{c_p}{c_v} = \frac{\kappa_T}{\kappa_s},$$
> donde $\kappa_s = -(1/v)(\partial v/\partial P)_s$ es la compresibilidad isentrópica (velocidad del sonido: $c^2 = v/\kappa_s$).

---

## Mapa de notas

> [!info]
> | Nota | Contenido |
> |:---|:---|
> | [[Identidades/index \| Identidades]] | Regla recíproca, triple producto, cadena; demostración de las tres |
> | [[Identidades/Regla Ciclica \| Regla cíclica]] | Aplicaciones de la regla triple producto a $\alpha$, $\kappa_T$; presión interna |
> | [[Maxwell]] | Cuatro relaciones de Maxwell con prueba completa desde cada potencial |
> | [[TdS]] | Dos ecuaciones $T\,ds$; integración de $\Delta s$; casos gas ideal, vdW, incompresible |
> | [[Cp Cv/index \| $c_p-c_v$]] | Prueba de $Tv\alpha^2/\kappa_T$; signos; Mayer; van der Waals |
> | [[Cp Cv/Razon de Calores \| Razón $\gamma$]] | $\gamma=c_p/c_v$; relación $\kappa_T/\kappa_s=\gamma$; velocidad del sonido |
> | [[Cp Cv/Efecto Joule Thomson \| Joule-Thomson]] | $\mu_{JT}=(\partial T/\partial P)_h$; curva de inversión; gas ideal y vdW |
> | [[Jacobianos/index \| Jacobianos]] | Método general con el determinante jacobiano |
> | [[Jacobianos/Aplicaciones Termodinamicas \| Aplic. jacobianos]] | Derivar Maxwell, $T\,ds$, coeficientes isentrópicos con jacobianos |

---

## Convención de notación

> [!info]
> - Minúsculas: propiedades específicas (por unidad de masa) — $u$, $h$, $f$, $g$, $s$, $v$.
> - $f = u - Ts$: energía de Helmholtz; $g = h - Ts$: energía de Gibbs.
> - $\alpha$: expansividad térmica isobárica; $\kappa_T$: compresibilidad isoterma; $\kappa_s$: isentrópica.
> - $\gamma = c_p/c_v$: razón de calores específicos (también escrito $k$ en algunos textos de ingeniería).

> [!referencia]
> Çengel & Boles, *Termodinámica*, cap. 12; Callen, *Thermodynamics and an Introduction to Thermostatistics*, cap. 4–7; Moran & Shapiro, *Fundamentos de Ingeniería Termodinámica*, cap. 11.
