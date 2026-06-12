---
title: Dieléctricos
tags:
  - electromagnetismo
  - teoria
  - electrostatica
  - dielectricos
  - indice
draft: false
aliases:
  - Dieléctricos
  - Campos en la materia
  - Respuesta dieléctrica
---

# Dieléctricos $\vec D=\varepsilon_0\vec E+\vec P,\quad \nabla\cdot\vec D=\rho_{\text{libre}}$

> [!definicion]
> Un **dieléctrico** es un material aislante cuyas cargas no se mueven libremente, pero cuyos átomos/moléculas se **polarizan** ante un campo externo: aparecen pequeños dipolos alineados, descritos por la **densidad de polarización** $\vec P$ (momento dipolar por unidad de volumen). Esta polarización genera **cargas ligadas** $\rho_b=-\nabla\cdot\vec P$ que, sumadas a las **libres**, son fuente del campo. Para separar ambas se introduce el **desplazamiento eléctrico** $\vec D=\varepsilon_0\vec E+\vec P$, cuya fuente es solo la carga libre: $\nabla\cdot\vec D=\rho_{\text{libre}}$.

---

> [!info]
> **Subsección de [[2 Electrostatica/index | Electrostática]]** (curso Electromagnetismo). Cierra el capítulo: tras Coulomb, Gauss, potencial, energía y conductores, describe la **respuesta de la materia aislante**. Contrasta con [[Conductores]] (donde $\vec E=0$ dentro): en un dieléctrico el campo no se anula, solo se **reduce**.
> **Referencia.** Griffiths, *Introduction to Electrodynamics*, cap. 4.

---

## La idea

> [!teoria] Cómo responde la materia aislante
> Sin campo, los dipolos atómicos están desordenados y el material es neutro en promedio. Al aplicar $\vec E_0$, los dipolos se alinean (o se inducen): el material adquiere una polarización $\vec P$. Dos efectos:
> - **En el volumen**, si $\vec P$ no es uniforme, hay carga ligada neta $\rho_b=-\nabla\cdot\vec P$.
> - **En las superficies**, aparece carga ligada superficial $\sigma_b=\vec P\cdot\hat n$.
>
> ![[polarizacion.svg|440]]
> *Dieléctrico polarizado por $\vec E_0$: los dipolos se alinean; en el interior la carga se cancela, pero en las caras queda $\pm\sigma_b$. Esa carga ligada produce un campo que se opone a $\vec E_0$ y reduce el campo total.*

> [!proposicion] El truco del desplazamiento $\vec D$
> La carga ligada es real pero **difícil de conocer de antemano** (depende del propio campo). El campo $\vec D=\varepsilon_0\vec E+\vec P$ esquiva el problema: su divergencia solo ve la carga **libre**, la que nosotros controlamos. En medios **lineales** $\vec P=\varepsilon_0\chi_e\vec E$, de modo que
> $$\vec D=\varepsilon_0(1+\chi_e)\vec E=\varepsilon\vec E,\qquad \varepsilon=\varepsilon_0\varepsilon_r,\quad \varepsilon_r=1+\chi_e,$$
> y la ley de Gauss para $\vec D$ se resuelve igual que en el vacío, con $\rho_{\text{libre}}$ y $\varepsilon$ en lugar de $\varepsilon_0$. Esto reduce el campo dentro del material por el factor $\varepsilon_r$.

---

## Mapa de la subsección

> [!algoritmo] Notas
> 1. **[[Polarizacion]]** — el vector $\vec P$; deducción de las cargas ligadas $\rho_b=-\nabla\cdot\vec P$ y $\sigma_b=\vec P\cdot\hat n$; el campo que crea un dieléctrico polarizado.
> 2. **[[Desplazamiento Electrico]]** — $\vec D=\varepsilon_0\vec E+\vec P$; ley de Gauss para $\vec D$ ($\nabla\cdot\vec D=\rho_{\text{libre}}$); medios lineales, $\varepsilon_r$ y condiciones de frontera.

> [!corolario] Por qué cierra la electrostática
> Con conductores y dieléctricos, la electrostática queda completa para **cualquier medio**: en un conductor las cargas se reorganizan hasta anular el campo interno; en un dieléctrico se polarizan y lo atenúan. La pareja $(\vec E,\vec D)$ —campo total y campo de carga libre— reaparecerá en electrodinámica y en las ondas en medios materiales.

> [!referencia]
> Griffiths, *Introduction to Electrodynamics*, cap. 4 ("Electric Fields in Matter"). Para la descripción microscópica de $\chi_e$: Jackson, cap. 4.
