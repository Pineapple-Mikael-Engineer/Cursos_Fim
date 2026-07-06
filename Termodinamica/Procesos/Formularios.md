---
title: Formulario — Procesos Termodinámicos
order: 99
tags:
  - termodinamica
  - formulario
  - procesos
draft: false
aliases:
  - formulario procesos termodinamicos
---

# Formulario — Procesos Termodinámicos

## Convenciones y relaciones base (gas ideal)

Ecuación de estado:
$$Pv=RT$$

Relación de Mayer:
$$c_p-c_v=R,\qquad c_p=c_v+R$$

Coeficiente adiabático:
$$\gamma=\frac{c_p}{c_v}$$

$c_v$ en función de $R$ y $\gamma$:
$$c_v=\frac{R}{\gamma-1},\qquad c_p=\gamma\,c_v,\qquad R=c_v(\gamma-1)$$

Primera ley (sistema cerrado, base másica):
$$\delta q-\delta w=du,\qquad q=\Delta u+w$$

Trabajo de frontera:
$$w=\int_1^2 P\,dv$$

Energía interna y entalpía (gas ideal):
$$\Delta u=c_v\,\Delta T,\qquad \Delta h=c_p\,\Delta T,\qquad h=u+Pv=u+RT$$

Calores específicos (definición):
$$c_v=\left(\frac{\partial u}{\partial T}\right)_v,\qquad c_p=\left(\frac{\partial h}{\partial T}\right)_P$$

## Procesos Reversibles e Irreversibles

Balance de entropía (sistema cerrado):
$$\Delta S=S_2-S_1=\int_1^2\frac{\delta Q}{T}+S_{gen},\qquad S_{gen}\ge 0$$
$T$: temperatura de la frontera por donde entra $\delta Q$.

Desigualdad de Clausius:
$$\oint\frac{\delta Q}{T}\le 0$$

Definición de entropía (proceso reversible):
$$dS\equiv\frac{\delta Q_{rev}}{T}$$

Sistema adiabático:
$$\Delta S=S_{gen}\ge 0$$

Trabajo en proceso irreversible (presión externa):
$$w=\int_1^2 P_{ext}\,dv,\qquad P_{ext}=P\mp\varepsilon$$

Trabajo reversible como extremo:
$$\text{expansión: } w_{rev}>w_{irrev};\qquad \text{compresión: } w_{rev}<w_{irrev}$$

Trabajo perdido (Gouy–Stodola):
$$w_{perdido}=T_0\,S_{gen}\ge 0$$
$T_0$: temperatura ambiente de referencia.

Entropía isotérmica (gas ideal, mismos estados por cualquier camino):
$$\Delta s_{sis}=R\ln\frac{v_2}{v_1}=R\ln\frac{P_1}{P_2}$$

Expansión contra $P_{ext}=P_2$ constante:
$$w_c=P_2\,(v_2-v_1)=RT\left(1-\frac{P_2}{P_1}\right)$$

## Proceso Isocórico ($v=\text{cte}$)

Condición:
$$v=\text{cte},\qquad dv=0$$

Trabajo de frontera:
$$w=\int_1^2 P\,dv=0$$

Primera ley (sin otros trabajos):
$$q_v=\Delta u=c_v\,\Delta T=c_v(T_2-T_1)$$

Relación de estados (ley de Gay-Lussac):
$$\frac{P_1}{T_1}=\frac{P_2}{T_2}$$

Cambio de entropía:
$$\Delta s=\int_1^2 c_v\,\frac{dT}{T}=c_v\ln\frac{T_2}{T_1}=c_v\ln\frac{P_2}{P_1}$$

Curva en el plano $T$–$s$:
$$T=T_1\,e^{(s-s_1)/c_v}=T_1\,e^{\Delta s/c_v}$$

Pendiente en $T$–$s$:
$$\left(\frac{\partial T}{\partial s}\right)_v=\frac{T}{c_v}$$

## Proceso Isobárico ($P=\text{cte}$)

Condición:
$$P_1=P_2=P=\text{cte}$$

Trabajo de frontera:
$$w=P\,(v_2-v_1)=P\,\Delta v=R\,(T_2-T_1)$$

Calor = cambio de entalpía:
$$q_p=\Delta h=h_2-h_1=c_p\,(T_2-T_1)=c_p\,\Delta T$$

Forma diferencial:
$$\delta q_p=dh,\qquad dh=du+P\,dv+v\,dP$$

Relación de estados (ley de Charles):
$$\frac{v_1}{T_1}=\frac{v_2}{T_2}$$

Cambio de entropía:
$$\Delta s=\int_1^2 c_p\,\frac{dT}{T}=c_p\ln\frac{T_2}{T_1}$$

Pendiente en $T$–$s$:
$$\left(\frac{\partial T}{\partial s}\right)_P=\frac{T}{c_p}$$

Relación de Mayer:
$$c_p=c_v+R,\qquad c_p-c_v=R$$

## Proceso Isotérmico ($T=\text{cte}$)

Condición:
$$T=\text{cte},\qquad dT=0,\qquad Pv=\text{cte}$$

Energía interna y entalpía (gas ideal):
$$\Delta u=0,\qquad \Delta h=0$$

Primera ley:
$$q=w$$

Trabajo de frontera (reversible):
$$w=RT\ln\frac{v_2}{v_1}=RT\ln\frac{P_1}{P_2}$$

Calor:
$$q=w=RT\ln\frac{v_2}{v_1}$$

Cambio de entropía:
$$\Delta s=\frac{q}{T}=R\ln\frac{v_2}{v_1}=R\ln\frac{P_1}{P_2}$$

Relación de estados:
$$P_1v_1=P_2v_2=RT$$

## Proceso Adiabático ($q=0$, $Pv^\gamma=\text{cte}$)

Condición:
$$q=0,\qquad \delta q=0$$

Primera ley:
$$w=-\Delta u$$

Relaciones $P$–$v$–$T$ (adiabático reversible):
$$Tv^{\gamma-1}=\text{cte},\qquad Pv^{\gamma}=\text{cte},\qquad TP^{(1-\gamma)/\gamma}=\text{cte}$$

Relación entre estados:
$$\frac{T_2}{T_1}=\left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma}=\left(\frac{v_1}{v_2}\right)^{\gamma-1}$$

Proceso adiabático reversible es isentrópico:
$$ds=\frac{\delta q_{rev}}{T}=0,\qquad \Delta s=0,\qquad s_2=s_1$$

Adiabático irreversible:
$$\Delta s=s_{gen}>0$$

Trabajo:
$$w=-\Delta u=c_v\,(T_1-T_2)=\frac{P_1v_1-P_2v_2}{\gamma-1}=\frac{R\,(T_1-T_2)}{\gamma-1}$$

Pendiente en $P$–$v$ (isoterma vs. adiabática):
$$\left(\frac{dP}{dv}\right)_T=-\frac{P}{v},\qquad \left(\frac{dP}{dv}\right)_s=-\gamma\,\frac{P}{v}=\gamma\left(\frac{dP}{dv}\right)_T$$

Entropía generada (gas ideal, $c_p$ cte):
$$s_{gen}=c_p\ln\frac{T_2}{T_1}-R\ln\frac{P_2}{P_1}$$

Eficiencia isentrópica de compresor:
$$\eta_s=\frac{w_{c,s}}{w_{c,real}}=\frac{h_{2s}-h_1}{h_2-h_1}=\frac{T_{2s}-T_1}{T_2-T_1}$$

## Proceso Politrópico ($Pv^{\,n}=\text{cte}$)

Condición:
$$P\,v^{\,n}=\text{cte},\qquad P_1v_1^{\,n}=P_2v_2^{\,n}$$
$n$: exponente politrópico (real).

Casos particulares:
$$n=0\ \text{(isobárico)},\quad n=1\ \text{(isotérmico)},\quad n=\gamma\ \text{(adiabático rev.)},\quad n\to\infty\ \text{(isocórico)}$$

Pendiente en $P$–$v$:
$$\frac{dP}{dv}=-\,n\,\frac{P}{v}$$

Relaciones de estado:
$$\frac{T_2}{T_1}=\left(\frac{v_1}{v_2}\right)^{n-1}=\left(\frac{P_2}{P_1}\right)^{(n-1)/n}$$

Trabajo de frontera ($n\neq 1$):
$$w=\frac{P_1v_1-P_2v_2}{n-1}=\frac{R\,(T_1-T_2)}{n-1}$$

Trabajo de frontera ($n=1$):
$$w=R\,T\,\ln\frac{v_2}{v_1}$$

Calor específico politrópico ($n\neq 1$):
$$c_n=c_v\,\frac{n-\gamma}{n-1}$$

Calor:
$$q=c_v(T_2-T_1)+\frac{R\,(T_1-T_2)}{n-1}=c_n\,(T_2-T_1)$$

Cambio de entropía:
$$\Delta s=c_n\,\ln\frac{T_2}{T_1}=c_v\,\ln\frac{T_2}{T_1}+R\,\ln\frac{v_2}{v_1}$$

Trabajo de flujo (volumen de control, $n\neq 1$):
$$w_{flujo}=\int_1^2 v\,dP=\frac{n}{n-1}\,R\,(T_2-T_1)=-\,n\,w$$

Potencia:
$$\dot W_{flujo}=\dot m\,w_{flujo}$$
