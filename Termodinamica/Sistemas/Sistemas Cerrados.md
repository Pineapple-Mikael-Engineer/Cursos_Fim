---
title: "Sistema cerrado"
tags:
  - termodinamica
  - sistemas
  - sistema_cerrado
draft: false
aliases:
  - closed system
  - masa de control
  - sistemas cerrados
---

# Sistema cerrado

> [!definicion]
> Sistema de **masa fija**: no hay flujo de materia a través de su frontera, aunque sí puede haber transferencia de calor y trabajo, y la frontera puede moverse (pistón). También llamado *masa de control*.
> $$
> \frac{dm}{dt} = 0 \quad\Rightarrow\quad m = \text{cte}
> $$

## Balances

> [!teorema]
> Con masa constante, los balances se escriben por unidad de masa o para la masa total. La energía y la entropía se desarrollan en notas propias:
> $$
> \Delta U = Q - W \qquad \text{(ver [[Primera Ley SC]])}
> $$
> $$
> \Delta S = \int \frac{\delta Q}{T} + S_{gen}, \quad S_{gen} \ge 0 \qquad \text{(ver [[Segunda Ley SC]])}
> $$
> $$
> \Delta X = \ldots - X_{dest} \qquad \text{(ver [[Balance de Exergia SC]])}
> $$

## Trabajo

> [!proposicion]
> En un sistema cerrado el trabajo incluye el de **frontera móvil** y cualquier otro modo (eje, eléctrico). Para proceso cuasiestático con frontera móvil:
> $$
> W_{borde} = \int_1^2 P\,dV
> $$
> No hay término de flujo ($\dot m\,h$) porque no entra ni sale masa: esa es la diferencia esencial con el [[Volumenes de Control | volumen de control]].

## Cuándo usarlo

> [!info]
> Modelo adecuado para:
> - gas en un dispositivo pistón-cilindro (ver [[Problema 02]]),
> - una masa de fluido confinada que se calienta o comprime,
> - procesos por lotes (*batch*) sin entrada ni salida de materia.

## Relación con otras notas

> [!info]
> - Balances específicos: [[Primera Ley SC]], [[Segunda Ley SC]], [[Balance de Exergia SC]].
> - Contraparte abierta: [[Volumenes de Control]] y su caso de [[Flujo Estacionario]].
> - El estado interno se describe con [[Presion]], [[Temperatura]] y [[Volumen Especifico]].

> [!info]
> **Convención de notación**:
> - $Q > 0$: calor hacia el sistema; $W > 0$: trabajo realizado por el sistema.
> - propiedades extensivas en mayúscula ($U$, $S$, $V$), específicas en minúscula.
