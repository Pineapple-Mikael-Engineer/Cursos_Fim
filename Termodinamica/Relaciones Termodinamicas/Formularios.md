---
title: Formulario — Relaciones Termodinámicas
order: 99
tags:
  - termodinamica
  - formulario
  - relaciones
draft: false
aliases:
  - formulario relaciones termodinamicas
---

# Formulario — Relaciones Termodinámicas

## Coeficientes fundamentales

$$\alpha \equiv \frac{1}{v}\left(\frac{\partial v}{\partial T}\right)_P$$
Expansividad térmica isobárica $[\mathrm{K}^{-1}]$.

$$\kappa_T \equiv -\frac{1}{v}\left(\frac{\partial v}{\partial P}\right)_T$$
Compresibilidad isoterma $[\mathrm{Pa}^{-1}]$.

$$\kappa_s \equiv -\frac{1}{v}\left(\frac{\partial v}{\partial P}\right)_s$$
Compresibilidad isentrópica.

$$c_v \equiv \left(\frac{\partial u}{\partial T}\right)_v = T\left(\frac{\partial s}{\partial T}\right)_v, \qquad c_p \equiv \left(\frac{\partial h}{\partial T}\right)_P = T\left(\frac{\partial s}{\partial T}\right)_P$$
Calores específicos.

$$\gamma \equiv \frac{c_p}{c_v} = \frac{\kappa_T}{\kappa_s}$$
Razón de calores específicos.

$$c_v = c_p - \frac{Tv\alpha^2}{\kappa_T}$$
Determinación de $c_v$ a partir de datos medibles.

## Identidades de derivadas parciales

$$\left(\frac{\partial x}{\partial y}\right)_z = \frac{1}{(\partial y/\partial x)_z}$$
Regla recíproca.

$$\left(\frac{\partial x}{\partial y}\right)_z\!\left(\frac{\partial y}{\partial z}\right)_x\!\left(\frac{\partial z}{\partial x}\right)_y = -1$$
Regla triple producto (cíclica).

$$\left(\frac{\partial x}{\partial y}\right)_w = \left(\frac{\partial x}{\partial z}\right)_w\!\left(\frac{\partial z}{\partial y}\right)_w$$
Regla de la cadena.

$$\left(\frac{\partial x}{\partial y}\right)_z = \left(\frac{\partial x}{\partial y}\right)_w + \left(\frac{\partial x}{\partial w}\right)_y\!\left(\frac{\partial w}{\partial y}\right)_z$$
Cambio de variable fija.

$$\left(\frac{\partial y}{\partial x}\right)_z = -\frac{(\partial z/\partial x)_y}{(\partial z/\partial y)_x}$$
Forma equivalente de la regla cíclica.

$$\left(\frac{\partial v}{\partial P}\right)_T = -v\kappa_T, \qquad \left(\frac{\partial v}{\partial T}\right)_P = v\alpha$$
Derivadas de la ecuación de estado.

$$\left(\frac{\partial P}{\partial T}\right)_v = \frac{\alpha}{\kappa_T}, \qquad \left(\frac{\partial T}{\partial P}\right)_v = \frac{\kappa_T}{\alpha}$$
Recíproca de la anterior.

$$\left(\frac{\partial T}{\partial v}\right)_P = \frac{1}{v\alpha}, \qquad \left(\frac{\partial P}{\partial v}\right)_T = -\frac{1}{v\kappa_T}$$
Recíprocas restantes.

## Regla cíclica: aplicaciones

$$\left(\frac{\partial P}{\partial T}\right)_v = -\frac{(\partial v/\partial T)_P}{(\partial v/\partial P)_T} = \frac{\alpha}{\kappa_T}$$
Conversión fundamental.

$$\left(\frac{\partial s}{\partial v}\right)_T = \left(\frac{\partial P}{\partial T}\right)_v = \frac{\alpha}{\kappa_T}$$
Maxwell 3.ª en forma medible.

$$\left(\frac{\partial u}{\partial v}\right)_T = T\left(\frac{\partial P}{\partial T}\right)_v - P = \frac{T\alpha}{\kappa_T} - P$$
Presión interna.

$$\left(\frac{\partial P}{\partial v}\right)_T = -\frac{1}{v\kappa_T}$$
Módulo isotermo.

$$\left(\frac{\partial u}{\partial P}\right)_T = v(\kappa_T P - T\alpha)$$
Cambio de $u$ con $P$.

$$\left(\frac{\partial h}{\partial v}\right)_T = \frac{T\alpha - 1}{\kappa_T}$$
Cambio de $h$ con $v$.

## Relaciones de Maxwell

$$M = \left(\frac{\partial z}{\partial x}\right)_y, \quad N = \left(\frac{\partial z}{\partial y}\right)_x \;\Longrightarrow\; \left(\frac{\partial M}{\partial y}\right)_x = \left(\frac{\partial N}{\partial x}\right)_y$$
Condición de Schwarz (exactitud).

$$du = T\,ds - P\,dv, \quad dh = T\,ds + v\,dP, \quad df = -s\,dT - P\,dv, \quad dg = -s\,dT + v\,dP$$
Diferenciales de los potenciales ($f=u-Ts$, $g=h-Ts$).

$$\left(\frac{\partial T}{\partial v}\right)_s = -\left(\frac{\partial P}{\partial s}\right)_v$$
1.ª relación (desde $u$).

$$\left(\frac{\partial T}{\partial P}\right)_s = \left(\frac{\partial v}{\partial s}\right)_P$$
2.ª relación (desde $h$).

$$\left(\frac{\partial s}{\partial v}\right)_T = \left(\frac{\partial P}{\partial T}\right)_v = \frac{\alpha}{\kappa_T}$$
3.ª relación (desde $f$).

$$\left(\frac{\partial s}{\partial P}\right)_T = -\left(\frac{\partial v}{\partial T}\right)_P = -v\,\alpha$$
4.ª relación (desde $g$).

$$\left(\frac{dP}{dT}\right)_{\rm sat} = \frac{s_v - s_l}{v_v - v_l} = \frac{h_{fg}}{T\,v_{fg}}$$
Relación de Clapeyron.

## Ecuaciones $T\,ds$

$$T\,ds = c_v\,dT + T\!\left(\frac{\partial P}{\partial T}\right)_v\!dv$$
1.ª ecuación (variables $T,v$).

$$T\,ds = c_p\,dT - T\!\left(\frac{\partial v}{\partial T}\right)_P\!dP$$
2.ª ecuación (variables $T,P$).

$$\left(\frac{\partial s}{\partial T}\right)_v = \frac{c_v}{T}, \qquad \left(\frac{\partial s}{\partial T}\right)_P = \frac{c_p}{T}$$
Derivadas de $s$ con $T$.

$$\Delta s = \int_1^2 \frac{c_v}{T}\,dT + \int_1^2 \left(\frac{\partial P}{\partial T}\right)_v\!dv = \int_1^2 \frac{c_p}{T}\,dT - \int_1^2 \left(\frac{\partial v}{\partial T}\right)_P\!dP$$
Cambio de entropía entre dos estados.

$$dT\big|_{ds=0} = -\frac{T}{c_v}\left(\frac{\partial P}{\partial T}\right)_v\!dv, \qquad dT\big|_{ds=0} = \frac{T}{c_p}\left(\frac{\partial v}{\partial T}\right)_P\!dP$$
Procesos isentrópicos.

$$\Delta s = c_v\ln\frac{T_2}{T_1} + R\ln\frac{v_2}{v_1} = c_p\ln\frac{T_2}{T_1} - R\ln\frac{P_2}{P_1}$$
Gas ideal ($c$ constantes).

$$ds = c_v\frac{dT}{T} + R\frac{dv}{v} = c_p\frac{dT}{T} - R\frac{dP}{P}$$
Gas ideal, forma diferencial.

$$\Delta s = c\,\ln\frac{T_2}{T_1}$$
Sustancia incompresible ($dv=0$, $c_p\approx c_v=c$).

## Relación $c_p - c_v$

$$c_p - c_v = T\!\left(\frac{\partial P}{\partial T}\right)_v\!\left(\frac{\partial v}{\partial T}\right)_P = \frac{Tv\,\alpha^2}{\kappa_T} \ge 0$$
Resultado general.

$$c_p - c_v = R$$
Gas ideal (relación de Mayer).

$$\bar{c}_p - \bar{c}_v = \frac{R_u}{\,1 - \dfrac{2a(\bar{v}-b)^2}{R_u T\,\bar{v}^3}\,}$$
Gas de van der Waals (forma molar).

$$\alpha = 0 \;\Longrightarrow\; c_p = c_v$$
Igualdad (máximo de densidad; incompresible).

## Razón de calores específicos $\gamma$

$$\gamma = \frac{c_p}{c_v} = \frac{\kappa_T}{\kappa_s}$$
Relación exacta.

$$\gamma = 1 + \frac{2}{f}$$
Gas ideal con $f$ grados de libertad; $c_v=(f/2)R$, $c_p=(f/2+1)R$.

$$\left(\frac{\partial v}{\partial P}\right)_s = \left(\frac{\partial v}{\partial P}\right)_T + \frac{T}{c_p}\!\left(\frac{\partial v}{\partial T}\right)_P^{\!2}$$
Compresibilidad isentrópica vs. isoterma.

$$Pv^\gamma = \text{cte}, \qquad Tv^{\gamma-1} = \text{cte}, \qquad T\,P^{-(\gamma-1)/\gamma} = \text{cte}$$
Relaciones isentrópicas del gas ideal.

$$\frac{R}{c_v} = \gamma - 1$$
Identidad auxiliar del gas ideal.

## Velocidad del sonido

$$c_{\rm son}^2 = \left(\frac{\partial P}{\partial\rho}\right)_s = -v^2\!\left(\frac{\partial P}{\partial v}\right)_s = \frac{v}{\kappa_s} = \frac{\gamma\,v}{\kappa_T} = \gamma\,P\,v$$
Formas equivalentes.

$$c_{\rm son}^2 = \frac{\gamma}{\rho\kappa_T} = \frac{1}{\rho\kappa_s}$$
En función de la densidad $\rho = 1/v$.

$$c_{\rm son} = \sqrt{\gamma\,R_s\,T}$$
Gas ideal; $R_s = R_u/M$.

## Efecto Joule-Thomson

$$\mu_{JT} \equiv \left(\frac{\partial T}{\partial P}\right)_h$$
Coeficiente de Joule-Thomson $[\mathrm{K/Pa}]$.

$$\left(\frac{\partial h}{\partial P}\right)_T = T\left(\frac{\partial s}{\partial P}\right)_T + v = v(1 - T\,\alpha)$$
Derivada intermedia.

$$\mu_{JT} = -\frac{v(1-T\alpha)}{c_p} = \frac{v(T\alpha - 1)}{c_p}$$
Coeficiente en función de $\alpha$, $v$, $c_p$.

$$\mu_{JT}^{\rm ideal} = 0$$
Gas ideal ($T\alpha = 1$).

$$T\alpha = 1 \;\Longleftrightarrow\; T\left(\frac{\partial v}{\partial T}\right)_P = v$$
Condición de la curva de inversión.

$$T_{\rm inv}^+ \approx \frac{2a}{Rb}$$
Temperatura de inversión superior (van der Waals, $P\to 0$).

## Presión interna

$$\pi_T \equiv \left(\frac{\partial u}{\partial v}\right)_T = T\left(\frac{\partial P}{\partial T}\right)_v - P = \frac{T\alpha}{\kappa_T} - P$$
Presión interna.

$$\pi_T^{\rm ideal} = 0$$
Gas ideal (teorema de Joule).

$$\pi_T^{\rm vdW} = \frac{a}{v^2}$$
Gas de van der Waals.

$$u(T,v) = u^{\rm ideal}(T) + \int_\infty^v \pi_T(T,v')\,dv'$$
Energía configuracional.

$$u^{\rm vdW}(T,v) = u^{\rm ideal}(T) - \frac{a}{v}$$
Energía interna del gas de van der Waals.

## Método de Jacobianos (Bridgman)

$$J(x,y) \equiv \frac{\partial(x,y)}{\partial(T,P)} = \left(\frac{\partial x}{\partial T}\right)_P\!\left(\frac{\partial y}{\partial P}\right)_T - \left(\frac{\partial x}{\partial P}\right)_T\!\left(\frac{\partial y}{\partial T}\right)_P$$
Jacobiano termodinámico respecto a $(T,P)$.

$$\left(\frac{\partial x}{\partial y}\right)_z = \frac{J(x,z)}{J(y,z)}$$
Fórmula central.

$$J(x,P) = \left(\frac{\partial x}{\partial T}\right)_P, \qquad J(x,T) = -\left(\frac{\partial x}{\partial P}\right)_T$$
Jacobianos elementales.

$$J(v,P)=v\alpha,\; J(v,T)=v\kappa_T,\; J(s,P)=c_p/T,\; J(s,T)=v\alpha$$
Tabla de Bridgman (parte 1).

$$J(u,P)=c_p - Pv\alpha,\; J(u,T)=v(T\alpha-\kappa_T P),\; J(h,P)=c_p,\; J(h,T)=v(T\alpha-1)$$
Tabla de Bridgman (parte 2).

$$J(f,P)=-(Pv\alpha+s),\; J(f,T)=-Pv\kappa_T,\; J(g,P)=-s,\; J(g,T)=-v$$
Tabla de Bridgman (parte 3).

## Derivadas isentrópicas

$$\left(\frac{\partial T}{\partial P}\right)_s = \frac{T}{c_p}\!\left(\frac{\partial v}{\partial T}\right)_P = \frac{Tv\alpha}{c_p}$$
Gradiente adiabático en presión.

$$\left(\frac{\partial T}{\partial v}\right)_s = -\frac{T}{c_v}\!\left(\frac{\partial P}{\partial T}\right)_v = -\frac{T\alpha}{c_v\kappa_T}$$
Gradiente adiabático en volumen.

$$\left(\frac{\partial P}{\partial v}\right)_s = \left(\frac{\partial P}{\partial v}\right)_T\frac{\kappa_T}{\kappa_s} = -\frac{\gamma}{v\kappa_T}$$
Módulo de compresión isentrópico.

$$\left(\frac{\partial P}{\partial T}\right)_s = \frac{1}{(\partial T/\partial P)_s} = \frac{c_p}{Tv\alpha}$$
Pendiente $P$-$T$ isentrópica.

$$\kappa_s = \frac{\kappa_T}{\gamma} = \frac{c_v}{c_p}\,\kappa_T$$
Compresibilidad isentrópica.

$$\Gamma \equiv \frac{v\alpha}{c_v\kappa_T} = \frac{v}{c_v}\!\left(\frac{\partial P}{\partial T}\right)_v, \qquad \left(\frac{\partial T}{\partial v}\right)_s = -\frac{T\Gamma}{v}$$
Coeficiente de Grüneisen.

## Derivadas por jacobianos (compilación)

$$\left(\frac{\partial h}{\partial P}\right)_T = v(1-T\alpha)$$
Caso ideal: $0$.

$$\left(\frac{\partial u}{\partial v}\right)_T = \frac{T\alpha}{\kappa_T} - P$$
Caso ideal: $0$.

$$\left(\frac{\partial s}{\partial v}\right)_T = \frac{\alpha}{\kappa_T}, \qquad \left(\frac{\partial s}{\partial P}\right)_T = -v\alpha$$
Casos ideales: $R/v$, $-R/P$.

$$\left(\frac{\partial s}{\partial P}\right)_v = \frac{c_p\kappa_T}{\alpha T} - v\alpha$$
Caso ideal: $c_v/P$.

$$\left(\frac{\partial T}{\partial P}\right)_s = \frac{Tv\alpha}{c_p}, \qquad \left(\frac{\partial T}{\partial v}\right)_s = -\frac{T\alpha}{c_v\kappa_T}$$
Coeficientes isentrópicos.

$$\left(\frac{\partial P}{\partial v}\right)_s = -\frac{\gamma}{v\kappa_T}, \qquad c_p - c_v = \frac{Tv\alpha^2}{\kappa_T}$$
Cierre de la tabla.
