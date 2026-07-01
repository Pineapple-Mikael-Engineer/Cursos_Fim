---
title: Controladores
order: 5
tags:
  - control-clasico
  - controladores
  - index
draft: false
aliases:
  - controladores
  - controladores clásicos
  - controllers
---

# Controladores

> [!definicion]
> Un **controlador** es el bloque que, a partir del **error** $e(t)=r(t)-y(t)$, genera la acción $u(t)$ que corrige la planta. La familia dominante en la industria es la **PID** —proporcional, integral y derivativa—, que combina respuesta al error presente, al acumulado y a su tendencia. Este bloque cierra el curso mostrando sus **acciones**, **configuraciones** y métodos de **sintonización**.

> [!info]
> Último bloque del [[Control Clasico/index| Control Clásico]]: aplica el [[4 Diseno/index| diseño]] al controlador más usado. El PID es la materialización práctica de las ideas de análisis y diseño vistas antes. Ogata, cap. 8; Nise, cap. 9.

## El controlador PID

> [!teoria] Tres acciones sobre el error
> El PID suma tres términos, $u(t)=K_p e+K_i\!\int e\,dt+K_d\,\dot e$, cada uno con un papel: el **proporcional** reacciona al error actual (rapidez), el **integral** elimina el error permanente (acumula el pasado) y el **derivativo** anticipa (amortigua el sobrepico). Ajustar $K_p, K_i, K_d$ —la **sintonización**— es lo que adapta el mismo controlador a plantas muy distintas; hay reglas empíricas (Ziegler–Nichols) y métodos basados en el modelo. → [[PID/index| Control PID]].

## Mapa de la sección

> [!info] Las subsecciones
> | Subsección | Contenido |
> |:---|:---|
> | [[PID/index\| Control PID]] | acciones P, I, D; configuraciones; sintonización |

> [!corolario]
> Con solo tres parámetros, el PID cubre la mayoría de las necesidades de control industrial. Entender qué aporta cada acción y cómo sintonizarlas es el destino práctico de todo el curso.

> [!referencia]
> Ogata, *Ingeniería de Control Moderna*, cap. 8. Nise, *Control Systems Engineering*, cap. 9. Åström–Hägglund, *PID Controllers*.
