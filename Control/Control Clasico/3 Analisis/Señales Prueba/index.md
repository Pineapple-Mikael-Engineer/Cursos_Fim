---
title: Señales de Prueba
order: 1
tags:
  - control-clasico
  - analisis
  - señales-prueba
  - index
draft: false
aliases:
  - señales de prueba
  - entradas de prueba
  - test signals
---

# Señales de Prueba

> [!definicion]
> Las **señales de prueba** son entradas canónicas —**impulso**, **escalón**, **rampa** y **parábola**— con las que se caracteriza y compara la respuesta de los sistemas. Están encadenadas por integración ($\text{impulso}\xrightarrow{\int}\text{escalón}\xrightarrow{\int}\text{rampa}\xrightarrow{\int}\text{parábola}$) y cada una exige más al sistema en régimen permanente: sirven para definir los **tipos de sistema** y el **error estacionario**.

> [!info]
> Herramienta del [[3 Analisis/index| análisis]]: son las entradas estándar para la [[Respuesta Temporal/index| respuesta temporal]] y para medir el error en régimen permanente. Ogata, cap. 5; Nise, cap. 4 y 7.

## Una familia ligada por la integral

> [!teoria] Del impulso a la parábola
> El **impulso** $\delta(t)$ concentra energía en un instante y su respuesta revela los modos naturales del sistema. Su integral es el **escalón** (cambio brusco de referencia, la prueba más usada). La integral del escalón es la **rampa** (entrada que crece a velocidad constante) y la de la rampa, la **parábola** (aceleración constante). Como cada una es "más difícil" de seguir que la anterior, el error en régimen permanente ante escalón, rampa y parábola define los coeficientes de error ($K_p, K_v, K_a$) y el **tipo** del sistema.

## Mapa de la sección

> [!info] Las señales
> | Nota | Señal | Definición |
> |:---|:---|:---|
> | [[Impulso]] | $\delta(t)$ | pulso ideal de área unidad |
> | [[Escalon]] | $u(t)$ | salto unitario (posición) |
> | [[Rampa]] | $t\,u(t)$ | crecimiento a velocidad constante |
> | [[Parabola]] | $\tfrac12 t^2 u(t)$ | aceleración constante |

> [!corolario]
> Impulso, escalón, rampa y parábola son una **escalera de integrales** que somete al sistema a exigencias crecientes. Elegir la señal adecuada es lo que permite medir tanto el transitorio (impulso, escalón) como la capacidad de seguimiento en régimen permanente (rampa, parábola).

> [!referencia]
> Ogata, *Ingeniería de Control Moderna*, cap. 5. Nise, *Control Systems Engineering*, cap. 4 y 7.
