---
title: Materiales Magnéticos
tags:
  - electromagnetismo
  - teoria
  - magnetostatica
draft: false
aliases:
  - Materiales magnéticos
  - Magnetización
  - Campo H
---

# Materiales Magnéticos $\vec H=\dfrac{\vec B}{\mu_0}-\vec M,\quad \nabla\times\vec H=\vec J_{\text{libre}}$

> [!definicion] Magnetización
> La **magnetización** $\vec M$ de un material es su **momento dipolar magnético por unidad de volumen**:
> $$\vec M\equiv\frac{d\vec m}{d^3r'}\qquad\left[\frac{\text{A}}{\text{m}}\right].$$
> Es la respuesta de la materia a un campo magnético externo: los dipolos atómicos (espines y corrientes orbitales) se alinean o desalinean, dejando una imanación neta. El **campo auxiliar** $\vec H$ separa esa respuesta de las corrientes que controlamos:
> $$\boxed{\ \vec H\equiv\frac{\vec B}{\mu_0}-\vec M\ }\qquad\Longrightarrow\qquad \nabla\times\vec H=\vec J_{\text{libre}}.$$

> [!info] Ubicación y contexto
> Esta nota pertenece a la sección [[3 Magnetostatica/index | Magnetostática]] y completa el tratamiento del campo en presencia de materia. Sus notas hermanas son [[Ley de Ampere]] (de la cual nace $\vec H$) y [[Potencial Vector]] (la herramienta para deducir las corrientes ligadas).
>
> Todo el desarrollo es el **análogo magnético exacto** del que se hizo para los [[2 Electrostatica/Dielectricos/index | Dieléctricos]]: donde allá había polarización $\vec P$, cargas ligadas $\rho_b,\sigma_b$ y el campo $\vec D$, aquí hay magnetización $\vec M$, **corrientes** ligadas $\vec J_b,\vec K_b$ y el campo $\vec H$. La correspondencia, sin embargo, **no es perfecta** (ver la advertencia al final).
>
> Referencia: Griffiths, *Introduction to Electrodynamics*, capítulo 6.

---

## Tipos de respuesta magnética

Antes de calcular, conviene nombrar los tres comportamientos posibles según el signo y magnitud de la imanación inducida:

- **Diamagnetismo.** $\vec M$ se induce **opuesta** al campo aplicado (susceptibilidad $\chi_m<0$, muy pequeña). Es universal y débil; domina cuando no hay momentos permanentes. Ejemplos: agua, cobre, bismuto.
- **Paramagnetismo.** $\vec M$ se alinea **a favor** del campo ($\chi_m>0$, pequeña). Hay momentos atómicos permanentes que el campo orienta parcialmente contra la agitación térmica. Ejemplos: aluminio, oxígeno.
- **Ferromagnetismo.** Acoplamiento cooperativo entre espines; $\vec M$ enorme, **no lineal** y con memoria (histéresis). Persiste imanación aun sin campo. Ejemplos: hierro, cobalto, níquel.

En lo que sigue tratamos $\vec M$ como un campo dado y deducimos qué campos produce; el caso lineal (dia/para) se cierra al final.

---

## Corrientes ligadas — la deducción central

> [!teorema] Un material magnetizado equivale a corrientes ligadas
> Un cuerpo con magnetización $\vec M(\vec r\,')$ produce, fuera y dentro de él, exactamente el mismo potencial vector que las distribuciones de corriente
> $$\boxed{\ \vec J_b=\nabla\times\vec M\quad(\text{volumétrica}),\qquad \vec K_b=\vec M\times\hat n\quad(\text{superficial}).\ }$$

> [!demostracion]
> **Paso 1 — Potencial de un dipolo y superposición.** Un dipolo magnético puntual $\vec m$ situado en $\vec r\,'$ genera el potencial vector
> $$\vec A(\vec r)=\frac{\mu_0}{4\pi}\,\frac{\vec m\times\hat{\mathscr r}}{\mathscr r^2},\qquad \mathscr r=|\vec r-\vec r\,'|.$$
> En un cuerpo magnetizado cada elemento $d^3r'$ aporta $d\vec m=\vec M\,d^3r'$. Sumando (integrando):
> $$\vec A(\vec r)=\frac{\mu_0}{4\pi}\int_V\frac{\vec M(\vec r\,')\times\hat{\mathscr r}}{\mathscr r^2}\,d^3r'.$$
>
> **Paso 2 — El truco del gradiente.** El factor geométrico es un gradiente respecto a la variable de integración:
> $$\nabla'\frac{1}{\mathscr r}=\frac{\hat{\mathscr r}}{\mathscr r^2},$$
> donde $\nabla'$ deriva respecto a $\vec r\,'$ (el signo es positivo precisamente porque $\mathscr r$ depende de $\vec r\,'$ con el orden $\vec r-\vec r\,'$). Sustituyendo:
> $$\vec A=\frac{\mu_0}{4\pi}\int_V \vec M\times\!\left(\nabla'\frac{1}{\mathscr r}\right)d^3r'.$$
>
> **Paso 3 — Identidad vectorial e integración por partes.** Usamos
> $$\nabla'\times\!\left(\frac{\vec M}{\mathscr r}\right)=\frac{1}{\mathscr r}\,\nabla'\times\vec M-\vec M\times\nabla'\frac{1}{\mathscr r},$$
> de donde
> $$\vec M\times\nabla'\frac{1}{\mathscr r}=\frac{1}{\mathscr r}\,\nabla'\times\vec M-\nabla'\times\!\left(\frac{\vec M}{\mathscr r}\right).$$
> Por tanto
> $$\vec A=\frac{\mu_0}{4\pi}\left[\int_V\frac{\nabla'\times\vec M}{\mathscr r}\,d^3r'-\int_V\nabla'\times\!\left(\frac{\vec M}{\mathscr r}\right)d^3r'\right].$$
>
> **Paso 4 — Convertir el segundo término en superficie.** Para todo campo vectorial $\vec F$ vale el teorema
> $$\int_V\left(\nabla'\times\vec F\right)d^3r'=-\oint_S\vec F\times d\vec a'=-\oint_S\vec F\times\hat n\,da'.$$
> Con $\vec F=\vec M/\mathscr r$:
> $$-\int_V\nabla'\times\!\left(\frac{\vec M}{\mathscr r}\right)d^3r'=\oint_S\frac{\vec M\times\hat n}{\mathscr r}\,da'.$$
>
> **Paso 5 — Identificación.** Reuniendo los dos términos:
> $$\vec A=\frac{\mu_0}{4\pi}\left[\int_V\frac{\nabla'\times\vec M}{\mathscr r}\,d^3r'+\oint_S\frac{\vec M\times\hat n}{\mathscr r}\,da'\right].$$
> Esta es **idéntica** en forma al potencial de una corriente volumétrica $\vec J_b$ más una corriente superficial $\vec K_b$,
> $$\vec A=\frac{\mu_0}{4\pi}\left[\int_V\frac{\vec J_b}{\mathscr r}\,d^3r'+\oint_S\frac{\vec K_b}{\mathscr r}\,da'\right],$$
> luego por comparación término a término
> $$\vec J_b=\nabla\times\vec M,\qquad \vec K_b=\vec M\times\hat n. \qquad\blacksquare$$

> [!info] Interpretación física
> Las corrientes ligadas son **reales** pero no las controlamos: provienen de los lazos microscópicos. En el interior, si $\vec M$ es uniforme, los lazos vecinos circulan en sentidos opuestos y **se cancelan** salvo en la frontera, donde sobrevive una corriente superficial $\vec K_b=\vec M\times\hat n$ que recorre el contorno. Si $\vec M$ varía en el espacio, la cancelación es imperfecta y aparece además $\vec J_b=\nabla\times\vec M$ en el volumen.

![[magnetizacion.svg|420]]
> **Figura.** Cilindro uniformemente magnetizado a lo largo de su eje. Los lazos de corriente internos (microscópicos) circulan en el mismo sentido; allí donde dos lazos contiguos se tocan, sus corrientes son opuestas y **se cancelan**. Sólo en la superficie lateral queda una corriente neta sin compensar: la corriente ligada superficial $\vec K_b=\vec M\times\hat n$, que envuelve el cilindro como un solenoide. En el interior $\vec J_b=\nabla\times\vec M=\vec 0$ por ser $\vec M$ uniforme.

---

## El campo auxiliar $\vec H$

> [!proposicion] Ley de Ampère para $\vec H$
> En presencia de materia magnetizada, la ley de Ampère se reescribe en términos **sólo** de la corriente libre:
> $$\nabla\times\vec H=\vec J_{\text{libre}},\qquad \oint_{\partial S}\vec H\cdot d\vec l=I_{\text{libre,enc}},\qquad \vec H=\frac{\vec B}{\mu_0}-\vec M.$$

> [!demostracion]
> **Paso 1 — Ampère con la corriente total.** El campo $\vec B$ siempre obedece a la corriente **total**, que incluye la libre y la ligada:
> $$\frac{1}{\mu_0}\nabla\times\vec B=\vec J=\vec J_{\text{libre}}+\vec J_b.$$
>
> **Paso 2 — Sustituir la corriente ligada.** Por el teorema anterior $\vec J_b=\nabla\times\vec M$:
> $$\frac{1}{\mu_0}\nabla\times\vec B=\vec J_{\text{libre}}+\nabla\times\vec M.$$
>
> **Paso 3 — Agrupar los rotacionales.** Pasamos $\nabla\times\vec M$ al miembro izquierdo y usamos la linealidad del rotacional:
> $$\nabla\times\!\left(\frac{\vec B}{\mu_0}\right)-\nabla\times\vec M=\vec J_{\text{libre}}\quad\Longrightarrow\quad \nabla\times\underbrace{\left(\frac{\vec B}{\mu_0}-\vec M\right)}_{\displaystyle \vec H}=\vec J_{\text{libre}}.$$
>
> **Paso 4 — Forma integral.** Integrando sobre una superficie $S$ con borde $\partial S$ y aplicando Stokes:
> $$\int_S(\nabla\times\vec H)\cdot d\vec a=\oint_{\partial S}\vec H\cdot d\vec l=\int_S\vec J_{\text{libre}}\cdot d\vec a=I_{\text{libre,enc}}. \qquad\blacksquare$$

La utilidad práctica es enorme: $\vec H$ se calcula **conociendo únicamente la corriente libre** (la que pasa por los cables), sin necesidad de saber de antemano cómo se magnetiza el material. Las unidades de $\vec H$ y de $\vec M$ coinciden: $\text{A}/\text{m}$.

---

## Medios lineales

> [!proposicion] Permeabilidad de un medio lineal
> En un material lineal e isótropo la magnetización es proporcional al campo auxiliar:
> $$\vec M=\chi_m\,\vec H,$$
> con $\chi_m$ la **susceptibilidad magnética** (adimensional). Entonces
> $$\boxed{\ \vec B=\mu\,\vec H,\qquad \mu=\mu_0\,\mu_r,\qquad \mu_r=1+\chi_m.\ }$$

> [!demostracion]
> **Paso 1 — Despejar $\vec B$.** De la definición $\vec H=\vec B/\mu_0-\vec M$ se tiene $\vec B=\mu_0(\vec H+\vec M)$.
>
> **Paso 2 — Insertar la relación lineal.** Con $\vec M=\chi_m\vec H$:
> $$\vec B=\mu_0\left(\vec H+\chi_m\vec H\right)=\mu_0(1+\chi_m)\,\vec H.$$
>
> **Paso 3 — Definir la permeabilidad.** Llamando $\mu\equiv\mu_0(1+\chi_m)$ y $\mu_r\equiv 1+\chi_m$ queda $\vec B=\mu\vec H$, con $\mu=\mu_0\mu_r$. $\qquad\blacksquare$

Según el signo de $\chi_m$:

| Tipo            | $\chi_m$                  | $\mu_r$        | Comportamiento de $\vec M$        |
| --------------- | ------------------------- | -------------- | --------------------------------- |
| Diamagnético    | $\chi_m<0$ (muy pequeño)  | $\mu_r<1$      | opuesta a $\vec H$                 |
| Paramagnético   | $\chi_m>0$ (pequeño)      | $\mu_r>1$      | a favor de $\vec H$               |
| Ferromagnético  | no lineal, $\chi_m\gg 1$  | $\mu_r\gg 1$   | histéresis, imanación permanente  |

---

## Ejemplo

> [!ejemplo] Barra cilíndrica uniformemente magnetizada y barra lineal en un solenoide
> **(a)** Un cilindro largo de radio $R$ está magnetizado uniformemente a lo largo de su eje, $\vec M=M\,\hat z$. Halla las corrientes ligadas y el campo $\vec B$ interior.
>
> **(b)** Ese mismo solenoide (de $n$ vueltas por unidad de longitud y corriente libre $I$) se rellena con un material lineal de susceptibilidad $\chi_m$. Halla $\vec H$, $\vec B$ y $\vec M$ dentro.

> [!solucion]
> **Parte (a).**
>
> **Paso 1 — Corriente volumétrica.** Como $\vec M=M\hat z$ es constante,
> $$\vec J_b=\nabla\times\vec M=\vec 0.$$
> No hay corriente ligada en el volumen.
>
> **Paso 2 — Corriente superficial.** En la cara lateral la normal saliente es $\hat n=\hat s$ (radial). Entonces
> $$\vec K_b=\vec M\times\hat n=M\,\hat z\times\hat s=M\,\hat\phi.$$
> Es una corriente azimutal de magnitud $K_b=M$ que envuelve el cilindro: **idéntica a un solenoide** con $nI\to M$.
>
> **Paso 3 — Campo interior.** Un solenoide ideal con corriente superficial $K_b$ produce en su interior
> $$\vec B=\mu_0 K_b\,\hat z=\mu_0 M\,\hat z.$$
> Coherentemente, dentro $\vec H=\vec B/\mu_0-\vec M=M\hat z-M\hat z=\vec 0$, como exige $\oint\vec H\cdot d\vec l=I_{\text{libre}}=0$ (no hay corriente libre).
>
> **Parte (b).**
>
> **Paso 1 — Hallar $\vec H$ por simetría.** $\vec H$ sólo depende de la corriente libre. Tomando un lazo amperiano rectangular de longitud $L$ con un lado dentro y otro fuera del solenoide (donde $\vec H=\vec 0$),
> $$\oint\vec H\cdot d\vec l=H\,L=I_{\text{libre,enc}}=n L\,I\quad\Longrightarrow\quad \vec H=nI\,\hat z.$$
>
> **Paso 2 — Campo $\vec B$.** Como el medio es lineal, $\vec B=\mu\vec H=\mu_0(1+\chi_m)\,nI\,\hat z$.
>
> **Paso 3 — Magnetización.** $\vec M=\chi_m\vec H=\chi_m\,nI\,\hat z.$
>
> Obsérvese que $\vec H$ es el mismo que sin material; el material amplifica $\vec B$ en el factor $\mu_r=1+\chi_m$. $\qquad\blacksquare$

---

## En qué consiste

La idea de fondo es **trasladar a la magnetostática toda la maquinaria de los dieléctricos**, cambiando el lenguaje de cargas por el de corrientes:

- La materia responde con una imanación $\vec M$, igual que el dieléctrico respondía con una polarización $\vec P$.
- Esa imanación equivale a **corrientes ligadas** $\vec J_b=\nabla\times\vec M$ y $\vec K_b=\vec M\times\hat n$, el análogo de las cargas ligadas $\rho_b=-\nabla\cdot\vec P$ y $\sigma_b=\vec P\cdot\hat n$.
- Para no arrastrar las corrientes ligadas (que no controlamos) se define $\vec H$, cuya fuente es **sólo la corriente libre**. Es el gemelo de $\vec D$, cuya fuente era sólo la carga libre.
- En medios lineales todo se cierra con una constante: $\mu_r=1+\chi_m$, análogo de $\varepsilon_r=1+\chi_e$.

El gran rédito es operativo: en problemas con simetría (solenoides, toroides, cilindros) se obtiene $\vec H$ de inmediato con la corriente libre, y luego $\vec B=\mu\vec H$ y $\vec M=\chi_m\vec H$.

> [!warning] La analogía $\vec H\leftrightarrow\vec D$ es sólo parcial
> Pese al paralelo, hay diferencias importantes que conviene tener presentes:
> - **$\vec H$ no se determina sólo por $\vec J_{\text{libre}}$.** La ley $\oint\vec H\cdot d\vec l=I_{\text{libre,enc}}$ permite *despejar* $\vec H$ **únicamente cuando hay simetría suficiente** (como con $\vec D$ y Gauss). Sin simetría, $\nabla\times\vec H=\vec J_{\text{libre}}$ no basta: falta la divergencia.
> - **$\vec H$ tiene divergencia.** Tomando divergencias en $\vec H=\vec B/\mu_0-\vec M$ y usando $\nabla\cdot\vec B=0$:
>   $$\nabla\cdot\vec H=-\,\nabla\cdot\vec M,$$
>   que **no es cero en general** (por ejemplo, en los extremos de una barra magnetizada). Es decir, $\vec H$ puede tener "fuentes" donde $\vec M$ cambia, a diferencia de $\vec B$, que nunca las tiene.
> - Por todo esto, $\vec B$ —y no $\vec H$— es el campo magnético fundamental; $\vec H$ es una comodidad de cálculo.

---

## Resumen

| Concepto                | Expresión                                                                            |
| ----------------------- | ----------------------------------------------------------------------------------- |
| Magnetización           | $\vec M=d\vec m/d^3r'$ (momento dipolar por unidad de volumen)                       |
| Corriente ligada vol.   | $\vec J_b=\nabla\times\vec M$                                                        |
| Corriente ligada sup.   | $\vec K_b=\vec M\times\hat n$                                                         |
| Potencial vector        | $\vec A=\dfrac{\mu_0}{4\pi}\left[\int_V\dfrac{\vec J_b}{\mathscr r}d^3r'+\oint_S\dfrac{\vec K_b}{\mathscr r}da'\right]$ |
| Campo auxiliar          | $\vec H=\dfrac{\vec B}{\mu_0}-\vec M$                                                |
| Ampère para $\vec H$    | $\nabla\times\vec H=\vec J_{\text{libre}}$,\quad $\oint\vec H\cdot d\vec l=I_{\text{libre,enc}}$ |
| Divergencia de $\vec H$ | $\nabla\cdot\vec H=-\nabla\cdot\vec M$                                               |
| Medio lineal            | $\vec M=\chi_m\vec H$,\quad $\vec B=\mu\vec H$,\quad $\mu=\mu_0\mu_r$,\quad $\mu_r=1+\chi_m$ |

> [!corolario] Idea para recordar
> Un imán es, a todos los efectos externos, **un manojo de corrientes** ($\vec J_b,\vec K_b$). El campo $\vec H$ existe para poder hablar **sólo de los cables que enchufamos** ($\vec J_{\text{libre}}$); pero al carecer de divergencia nula no es tan limpio como $\vec B$, y por eso $\vec B$ sigue siendo el campo físico.

> [!referencia] Para profundizar
> - **Griffiths**, *Introduction to Electrodynamics*, capítulo 6 (Magnetic Fields in Matter): corrientes ligadas, campo $\vec H$, medios lineales y ferromagnetismo.
> - **Jackson**, *Classical Electrodynamics*, capítulo 5: tratamiento avanzado de $\vec H$ y condiciones de frontera.
> - **Landau & Lifshitz**, *Electrodinámica de los medios continuos* (Vol. 8): magnetización y respuesta de la materia.
> - Notas relacionadas: [[Ley de Ampere]], [[Potencial Vector]], [[2 Electrostatica/Dielectricos/index | Dieléctricos]] (la analogía completa).
