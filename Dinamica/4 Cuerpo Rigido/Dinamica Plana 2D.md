---
title: Dinámica Plana 2D
tags:
  - dinamica
  - teoria
  - cuerpo-rigido
  - cinetica
draft: false
aliases:
  - cinética plana
  - Newton-Euler 2D
  - dinámica plana del cuerpo rígido
  - planar rigid body dynamics
  - cinética del cuerpo rígido 2D
---

# Dinámica Plana $\;\sum\vec F=m\vec a_G,\quad\sum M_G=I_G\alpha$

> [!definicion]
> La **cinética plana** de un sólido rígido son las ecuaciones de **Newton-Euler** en el plano:
> $$\boxed{\;\sum\vec F=m\vec a_G\quad(\text{2 escalares}),\qquad \sum M_G=I_G\,\alpha\quad(\text{1 escalar})\;}$$
> donde $G$ es el **centro de masa**, $I_G$ el momento de inercia respecto a $G$ y $\alpha$ la aceleración
> angular (la componente $z$, única fuera del plano). Tomando momentos respecto a un punto $O$
> **cualquiera**:
> $$\sum M_O=I_G\,\alpha+\bigl(\vec r_{G/O}\times m\vec a_G\bigr)_z.$$

> [!info]
> Cinética plana del [[4 Cuerpo Rigido/index | cuerpo rígido]]; es el **caso 2D** de las
> [[Ecuaciones de Euler 3D | ecuaciones de Euler]] (sin el término giroscópico
> $\vec\omega\times\mathbf I\vec\omega$, que se anula cuando $\vec\omega\parallel\hat k$). Usa el $I_G$ de
> [[Momentos de Inercia de Figuras]] y la cinemática de [[Cinematica Plana]] (rodadura, CIR, aceleración
> relativa). Referencia: Hibbeler cap. 17.

---

## Ejemplo

> [!ejemplo]
> **Cilindro que rueda por un plano inclinado.**
>
> Un cilindro macizo de masa $m$ y radio $R$ ($I_G=\tfrac12 mR^2$) **rueda sin deslizar** por un plano de
> inclinación $\theta$. Hallar la aceleración del centro $a_G$.
>
> ![[dcl_rodadura.svg|470]]
>
> *DCL: peso $m\vec g$, normal $\vec N$ y rozamiento $\vec f$ (cuesta arriba, el que permite rodar). Newton-Euler + rodadura dan $a_G$.*
>
> Las fuerzas son el peso $mg$, la normal $N$ y el rozamiento $f$ (hacia arriba del plano, es el que
> permite rodar). Se plantean las tres ecuaciones:
> - **Fuerzas a lo largo del plano:** $\;mg\operatorname{sen}\theta-f=m\,a_G$.
> - **Momentos en $G$** (solo $f$ produce momento respecto a $G$, con brazo $R$):
>   $\;fR=I_G\,\alpha=\tfrac12 mR^2\alpha$.
> - **Vínculo de rodadura:** $\;a_G=\alpha R$.
>
> De la 2.ª y la 3.ª: $f=\tfrac12 mR^2\cdot\dfrac{a_G}{R^2}=\tfrac12 m\,a_G$. Sustituyendo en la 1.ª:
> $$mg\operatorname{sen}\theta-\tfrac12 m\,a_G=m\,a_G\;\Longrightarrow\;mg\operatorname{sen}\theta=\tfrac32 m\,a_G.$$
>
> > [!solucion]
> > $$\boxed{a_G=\tfrac{2}{3}\,g\operatorname{sen}\theta}$$
> > Es **menor** que $g\operatorname{sen}\theta$ (deslizamiento sin fricción): parte de la energía
> > potencial va a la **rotación** ($\tfrac12 I_G\omega^2$) y no toda a la traslación. El rozamiento de
> > rodadura no disipa (no hay deslizamiento), solo redistribuye.

---

## En qué consiste

> [!teoria] Tres ecuaciones, tres incógnitas cinemáticas
> El plano da exactamente tres ecuaciones escalares: **dos de fuerza** ($x,y$) y **una de momento** ($z$).
> Estas determinan las tres incógnitas cinemáticas $a_{Gx}$, $a_{Gy}$ y $\alpha$. Cuando hay reacciones
> desconocidas (pasador, normal, rozamiento), se cierran con los **vínculos cinemáticos**: rodadura
> $a_G=\alpha R$, pasador fijo $\vec a_G=\vec\alpha\times\vec r_{G/O}-\omega^2\vec r_{G/O}$, etc.

> [!teorema] Momento respecto a un punto arbitrario
> Para cualquier punto $O$ (incluso **acelerado**):
> $$\sum M_O=I_G\,\alpha+\bigl(\vec r_{G/O}\times m\vec a_G\bigr)_z.$$

> [!demostracion]
> **Paso 1 — Traslado de momentos.** El momento resultante de un sistema de fuerzas respecto a $O$ se
> relaciona con el momento respecto a $G$ por
> $$\sum M_O=\sum M_G+\vec r_{G/O}\times\Bigl(\textstyle\sum\vec F\Bigr),$$
> donde $\vec r_{G/O}$ va de $O$ a $G$ (esto es la propiedad de traslado del momento de un sistema de
> vectores: cambiar el punto base añade $\vec r\times\vec R$ con $\vec R$ la resultante).
>
> **Paso 2 — Ecuaciones de Newton-Euler en $G$.** Por las ecuaciones básicas,
> $\sum M_G=I_G\alpha$ y $\sum\vec F=m\vec a_G$.
>
> **Paso 3 — Sustituir.** Reemplazando ambas:
> $$\sum M_O=I_G\alpha+\vec r_{G/O}\times m\vec a_G.$$
> En el plano solo sobrevive la componente $z$, de donde $\sum M_O=I_G\alpha+(\vec r_{G/O}\times m\vec a_G)_z$.
> El término extra **se anula** si $O\equiv G$ ($\vec r_{G/O}=\vec0$), si $O$ es un punto **fijo** o si
> $\vec a_G\parallel\vec r_{G/O}$. $\blacksquare$

> [!teorema] Energía e impulso-momento
> La **energía cinética** plana se separa en traslación más rotación (teorema de König plano):
> $$T=\tfrac12 m\,v_G^2+\tfrac12 I_G\,\omega^2,$$
> y el **trabajo-energía** da $U=\Delta T$. Las formas **integrales** de Newton-Euler son los teoremas de
> impulso-momento: lineal $\displaystyle\int\sum\vec F\,dt=m\,\Delta\vec v_G$ y angular
> $\displaystyle\int\sum M_G\,dt=I_G\,\Delta\omega$.

> [!demostracion]
> **Energía.** La energía cinética de un sólido es $T=\tfrac12\sum m_i v_i^2$. Con
> $\vec v_i=\vec v_G+\vec\omega\times\vec r_{i/G}$:
> $$T=\tfrac12\sum m_i\bigl(v_G^2+2\,\vec v_G\cdot(\vec\omega\times\vec r_{i/G})+|\vec\omega\times\vec r_{i/G}|^2\bigr).$$
> El término cruzado se anula porque $\sum m_i\vec r_{i/G}=\vec0$ (definición de $G$). En el plano
> $|\vec\omega\times\vec r_{i/G}|=\omega\,r_{i/G}$ (perpendiculares), así que el último término es
> $\tfrac12\omega^2\sum m_i r_{i/G}^2=\tfrac12 I_G\omega^2$. Queda $T=\tfrac12 m v_G^2+\tfrac12 I_G\omega^2$.
>
> **Impulso-momento.** Integrando $\sum\vec F=m\vec a_G=m\,d\vec v_G/dt$ en el tiempo se obtiene
> $\int\sum\vec F\,dt=m\,\Delta\vec v_G$; integrando $\sum M_G=I_G\,d\omega/dt$ resulta
> $\int\sum M_G\,dt=I_G\,\Delta\omega$. Son simplemente las ecuaciones diferenciales en forma integral. $\blacksquare$

> [!proposicion] Cierre del sistema
> Las tres ecuaciones escalares (2 de fuerza + 1 de momento) tienen como incógnitas cinemáticas
> $a_{Gx}$, $a_{Gy}$, $\alpha$. Si además aparecen reacciones desconocidas, cada vínculo geométrico
> (rodadura, pasador, contacto) aporta una relación cinemática que iguala el número de ecuaciones al de
> incógnitas y **cierra** el sistema.

> [!warning]
> $\sum M_G=I_G\alpha$ vale tomando momentos en el **centro de masa** $G$ (o en un punto **fijo**, o en el
> CIR con cuidado). En un punto **acelerado** arbitrario **hay que añadir** el término
> $\vec r_{G/O}\times m\vec a_G$: olvidarlo es el error típico. Además $I_G$ es el momento respecto a $G$;
> para referirlo a otro punto se usa el [[Teorema del Eje Paralelo]].

## Resumen

> [!resumen]
> | Magnitud | Expresión |
> |:---|:---|
> | Fuerza (traslación) | $\sum\vec F=m\vec a_G$ |
> | Momento en $G$ | $\sum M_G=I_G\,\alpha$ |
> | Momento en $O$ arbitrario | $\sum M_O=I_G\alpha+(\vec r_{G/O}\times m\vec a_G)_z$ |
> | Energía cinética | $T=\tfrac12 m v_G^2+\tfrac12 I_G\omega^2$ |
> | Impulso-momento | $\int\sum\vec F\,dt=m\Delta\vec v_G$, $\;\int\sum M_G\,dt=I_G\Delta\omega$ |

> [!corolario]
> La dinámica plana del sólido es traslación de $G$ gobernada por $\sum\vec F=m\vec a_G$ más una rotación
> gobernada por $\sum M_G=I_G\alpha$, desacopladas salvo por los vínculos. Es el límite sin giróscopo de
> las [[Ecuaciones de Euler 3D | ecuaciones de Euler]]: cuando $\vec\omega\parallel\hat k$, el término
> $\vec\omega\times\mathbf I\vec\omega$ desaparece y solo queda el escalar $I_G\alpha$.

> [!referencia]
> Hibbeler cap. 17. Cinemática previa: [[Cinematica Plana]]. Momentos de inercia:
> [[Momentos de Inercia de Figuras]] y [[Teorema del Eje Paralelo]]. Generalización 3D:
> [[Ecuaciones de Euler 3D]]. Contexto: [[4 Cuerpo Rigido/index]].
