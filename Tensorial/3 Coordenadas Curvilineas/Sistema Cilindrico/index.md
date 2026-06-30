---
title: El Sistema Cilíndrico
order: 2
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-curvilineas
  - cilindricas
  - index
draft: false
aliases:
  - sistema cilindrico
  - coordenadas cilindricas
  - cylindrical coordinates
---

# El Sistema Cilíndrico $(\rho,\phi,z)$

> [!definicion]
> El **sistema cilíndrico** describe un punto $P$ por su distancia $\rho$ al eje $z$, su ángulo azimutal $\phi$ y su altura $z$. Se relaciona con el cartesiano superpuesto por
> $$x=\rho\cos\phi,\qquad y=\rho\operatorname{sen}\phi,\qquad z=z,$$
> y su inversa
> $$\rho=\sqrt{x^2+y^2},\qquad \phi=\arctan(y/x),\qquad z=z.$$
> Su base ortonormal de mano derecha es $\hat e_\rho,\hat e_\phi,\hat e_z$, y el vector posición toma la forma compacta $\vec r=\rho\,\hat e_\rho+z\,\hat e_z$.

> [!info]
> Es la sección **3.2** del [[index | capítulo 3]] (libro, cap. 3.2). Particulariza el marco de los [[Sistemas Curvilineos Generales/index | sistemas curvilíneos generales]] a la simetría axial, y reutiliza la descomposición del [[Vector Posicion]]. Se desglosa en:
> - [[Vectores Base y Factores Escala]] — base $\hat e_\rho,\hat e_\phi,\hat e_z$, factores $h_\rho=1,h_\phi=\rho,h_z=1$ y elemento $d\vec r$.
> - [[Operaciones Cilindricas]] — gradiente, divergencia y rotor en $(\rho,\phi,z)$.

> [!info] Coordenadas cilíndricas y su base
> ![[sistema_cilindrico.svg|420]]
>
> Coordenadas cilíndricas $(\rho,\phi,z)$ y su base $\hat e_\rho,\hat e_\phi,\hat e_z$.

---

## Ejemplo

> [!ejemplo]
> **De cartesianas a cilíndricas (ida y vuelta).** Sea el punto $P=(x,y,z)=(-1,\,\sqrt 3,\,4)$.
>
> *Cartesianas → cilíndricas.* Con las ecuaciones inversas:
> $$\rho=\sqrt{(-1)^2+(\sqrt 3)^2}=\sqrt{1+3}=2,\qquad z=4.$$
> Para $\phi$, el punto está en el segundo cuadrante ($x<0,\ y>0$), así que $\arctan(y/x)$ debe ajustarse sumando $\pi$:
> $$\phi=\arctan\!\frac{\sqrt 3}{-1}=\pi-\frac{\pi}{3}=\frac{2\pi}{3}\ (=120^\circ).$$
> Luego $P=(\rho,\phi,z)=\left(2,\,\tfrac{2\pi}{3},\,4\right)$.
>
> *Cilíndricas → cartesianas.* Con las ecuaciones directas:
> $$x=2\cos\tfrac{2\pi}{3}=2\left(-\tfrac12\right)=-1,\quad y=2\operatorname{sen}\tfrac{2\pi}{3}=2\cdot\tfrac{\sqrt 3}{2}=\sqrt 3,\quad z=4,$$
> recuperando el punto original. El ejemplo ilustra la trampa del $\arctan$: hay que mirar el cuadrante de $(x,y)$ para elegir bien $\phi$.

---

## En qué consiste

> [!teoria]
> Cada vector base apunta en la dirección en la que se mueve $P$ al **aumentar** su coordenada manteniendo las otras fijas: $\hat e_\rho$ se aleja radialmente del eje $z$, $\hat e_\phi$ gira en sentido azimutal y $\hat e_z$ sube. A diferencia del cartesiano, esta base **no es fija**: como $\hat e_\rho$ y $\hat e_\phi$ dependen de $\phi$, sus direcciones cambian al desplazarse $P$. En el propio eje ($\rho=0$) el ángulo $\phi$ es ambiguo, así que $\hat e_\rho$ y $\hat e_\phi$ quedan **indefinidas**.
>
> El orden $(\rho,\phi,z)$ forma un sistema de **mano derecha** y la base es **ortonormal**:
> $$\hat e_\rho\cdot\hat e_\phi=\hat e_\rho\cdot\hat e_z=\hat e_\phi\cdot\hat e_z=0,\qquad \hat e_\rho\cdot\hat e_\rho=\hat e_\phi\cdot\hat e_\phi=\hat e_z\cdot\hat e_z=1.$$

> [!proposicion] El vector posición no tiene componente azimutal
> Proyectando $\vec r$ sobre la base ($\vec r=(\vec r\cdot\hat e_\rho)\hat e_\rho+(\vec r\cdot\hat e_\phi)\hat e_\phi+(\vec r\cdot\hat e_z)\hat e_z$) y notando que $\hat e_\phi$ es **siempre perpendicular** a $\vec r$, la componente azimutal se anula y queda
> $$\vec r=\rho\,\hat e_\rho+z\,\hat e_z.$$
> El punto se alcanza yendo radialmente una distancia $\rho$ y subiendo $z$; no hace falta "girar", porque $\hat e_\rho$ ya incorpora la información de $\phi$.

> [!info] Caso 2D: el sistema polar plano
> Suprimiendo $z$, las coordenadas $(\rho,\phi)$ forman el **sistema polar plano**. Su base es $\hat e_\rho,\hat e_\phi$ y el vector posición tiene una sola componente,
> $$\vec r=\rho\,\hat e_\rho.$$
> Un vector **arbitrario** $\vec v$ sí puede tener ambas componentes $(v_\rho,v_\phi)$; solo $\vec r$ se reduce a la radial.

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Coordenadas | $(\rho,\phi,z)$, mano derecha |
> | Directas | $x=\rho\cos\phi,\ y=\rho\operatorname{sen}\phi,\ z=z$ |
> | Inversas | $\rho=\sqrt{x^2+y^2},\ \phi=\arctan(y/x),\ z=z$ |
> | Base | $\hat e_\rho,\hat e_\phi,\hat e_z$ ortonormal, no fija |
> | Indefinición | $\hat e_\rho,\hat e_\phi$ en $\rho=0$ |
> | Factores de escala | $h_\rho=1,\ h_\phi=\rho,\ h_z=1$ |
> | Vector posición | $\vec r=\rho\,\hat e_\rho+z\,\hat e_z$ (sin $\hat e_\phi$) |
> | Caso 2D (polar) | $\vec r=\rho\,\hat e_\rho$ |

> [!corolario]
> El cilíndrico es el sistema natural para problemas con **simetría axial** (hilos de carga, solenoides, flujo en tuberías). Su economía nace de que $\hat e_\rho$ absorbe la dependencia angular, dejando $\vec r=\rho\hat e_\rho+z\hat e_z$. El precio, como en todo curvilíneo, es una base móvil que se traduce en el factor $h_\phi=\rho$; ese único factor distinto de $1$ es el que aparece en todas las [[Operaciones Cilindricas]].

> [!referencia]
> - Base y factores de escala en detalle: [[Vectores Base y Factores Escala]].
> - Operadores diferenciales en cilíndricas: [[Operaciones Cilindricas]].
> - Marco general del que desciende: [[Sistemas Curvilineos Generales/index]].
> - Sistema hermano: [[Sistema Esferico/index]].
