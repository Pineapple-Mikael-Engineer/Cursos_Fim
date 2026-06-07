---
title: El Sistema Esférico
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-curvilineas
  - esfericas
  - index
draft: false
aliases:
  - sistema esferico
  - coordenadas esfericas
  - spherical coordinates
---

# El Sistema Esférico $(r,\theta,\phi)$

> [!definicion]
> El **sistema esférico** describe un punto $P$ por su distancia $r$ al origen (coordenada radial), su ángulo polar $\theta$ medido desde el eje $z$ y su ángulo azimutal $\phi$. Se relaciona con el cartesiano superpuesto por
> $$x=r\operatorname{sen}\theta\cos\phi,\qquad y=r\operatorname{sen}\theta\operatorname{sen}\phi,\qquad z=r\cos\theta,$$
> y su inversa
> $$r=\sqrt{x^2+y^2+z^2},\qquad \theta=\arccos\!\frac{z}{r},\qquad \phi=\arctan\!\frac{y}{x}.$$
> Su base ortonormal de mano derecha es $\hat e_r,\hat e_\theta,\hat e_\phi$, y el vector posición toma la forma compacta $\vec r=r\,\hat e_r$.

> [!info]
> Es la sección **3.3** del [[index | capítulo 3]] (libro, cap. 3.3). Particulariza el marco de los [[Sistemas Curvilineos Generales/index | sistemas curvilíneos generales]] a la simetría central, y reutiliza la descomposición del [[Vector Posicion]]. Se desglosa en:
> - [[Vectores Base y Factores Escala]] — base $\hat e_r,\hat e_\theta,\hat e_\phi$, factores $h_r=1,h_\theta=r,h_\phi=r\operatorname{sen}\theta$ y elemento $d\vec r$.
> - [[Operaciones Esfericas]] — gradiente, divergencia y rotor en $(r,\theta,\phi)$.

> [!info] Coordenadas esféricas y su base
> ![[sistema_esferico.svg|420]]
>
> Coordenadas esféricas $(r,\theta,\phi)$ y su base $\hat e_r,\hat e_\theta,\hat e_\phi$.

---

## Ejemplo

> [!ejemplo]
> **De cartesianas a esféricas (ida y vuelta).** Sea el punto $P=(x,y,z)=(1,\,1,\,\sqrt 2)$.
>
> *Cartesianas → esféricas.* El radio sale de la norma:
> $$r=\sqrt{1^2+1^2+(\sqrt 2)^2}=\sqrt{1+1+2}=2.$$
> El ángulo polar se mide desde el eje $z$:
> $$\theta=\arccos\!\frac{z}{r}=\arccos\!\frac{\sqrt 2}{2}=\frac{\pi}{4}\ (=45^\circ).$$
> El azimutal, con $x>0,\ y>0$ (primer cuadrante):
> $$\phi=\arctan\!\frac{y}{x}=\arctan 1=\frac{\pi}{4}\ (=45^\circ).$$
> Luego $P=(r,\theta,\phi)=\left(2,\,\tfrac{\pi}{4},\,\tfrac{\pi}{4}\right)$.
>
> *Esféricas → cartesianas.* Con las ecuaciones directas y $\operatorname{sen}\tfrac{\pi}{4}=\cos\tfrac{\pi}{4}=\tfrac{\sqrt 2}{2}$:
> $$x=2\cdot\tfrac{\sqrt 2}{2}\cdot\tfrac{\sqrt 2}{2}=2\cdot\tfrac12=1,\quad y=2\cdot\tfrac{\sqrt 2}{2}\cdot\tfrac{\sqrt 2}{2}=1,\quad z=2\cos\tfrac{\pi}{4}=2\cdot\tfrac{\sqrt 2}{2}=\sqrt 2,$$
> recuperando el punto original. Como en cilíndricas, hay que mirar el cuadrante de $(x,y)$ al elegir $\phi$ con el $\arctan$; el polar $\theta\in[0,\pi]$ no tiene esa ambigüedad porque $\arccos$ ya cubre su rango.

---

## En qué consiste

> [!teoria]
> Cada vector base apunta en la dirección en la que se mueve $P$ al **aumentar** su coordenada manteniendo las otras fijas: $\hat e_r$ se aleja radialmente del origen, $\hat e_\theta$ es tangente al **meridiano** (apunta hacia el sur, en sentido de $\theta$ creciente) y $\hat e_\phi$ es tangente al **paralelo** (sentido azimutal). A diferencia del cartesiano, esta base **no es fija**: las tres direcciones dependen de $(\theta,\phi)$ y cambian al desplazarse $P$.
>
> El orden $(r,\theta,\phi)$ forma un sistema de **mano derecha** y la base es **ortonormal**:
> $$\hat e_r\cdot\hat e_\theta=\hat e_r\cdot\hat e_\phi=\hat e_\theta\cdot\hat e_\phi=0,\qquad \hat e_r\cdot\hat e_r=\hat e_\theta\cdot\hat e_\theta=\hat e_\phi\cdot\hat e_\phi=1.$$

> [!warning] Dónde se indefine la base
> Sobre el **eje $z$** ($\theta=0$ o $\theta=\pi$) el azimut $\phi$ es ambiguo, de modo que $\hat e_\theta$ y $\hat e_\phi$ quedan **indefinidos**. En el **origen** ($r=0$), además, ni siquiera $\theta$ está definido y se indefine también $\hat e_r$. Por eso $r=0$ y el eje polar son puntos singulares del sistema.

> [!proposicion] El vector posición es puramente radial
> Proyectando $\vec r$ sobre la base ($\vec r=(\vec r\cdot\hat e_r)\hat e_r+(\vec r\cdot\hat e_\theta)\hat e_\theta+(\vec r\cdot\hat e_\phi)\hat e_\phi$) y notando que $\hat e_\theta$ y $\hat e_\phi$ son **siempre perpendiculares** a $\vec r$, solo sobrevive la componente radial:
> $$\vec r=r\,\hat e_r.$$
> El punto se alcanza yendo en línea recta una distancia $r$ en la dirección $\hat e_r$; toda la información angular $(\theta,\phi)$ está incorporada en la orientación de $\hat e_r$. Es la descomposición más simple posible de un vector posición.

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Coordenadas | $(r,\theta,\phi)$, mano derecha; $\theta$ polar desde $z$, $\phi$ azimutal |
> | Directas | $x=r\operatorname{sen}\theta\cos\phi,\ y=r\operatorname{sen}\theta\operatorname{sen}\phi,\ z=r\cos\theta$ |
> | Inversas | $r=\sqrt{x^2+y^2+z^2},\ \theta=\arccos(z/r),\ \phi=\arctan(y/x)$ |
> | Base | $\hat e_r,\hat e_\theta,\hat e_\phi$ ortonormal, no fija |
> | Indefinición | $\hat e_\theta,\hat e_\phi$ en el eje $z$; $\hat e_r$ en el origen |
> | Factores de escala | $h_r=1,\ h_\theta=r,\ h_\phi=r\operatorname{sen}\theta$ |
> | Vector posición | $\vec r=r\,\hat e_r$ (sin $\hat e_\theta$ ni $\hat e_\phi$) |

> [!corolario]
> El esférico es el sistema natural para problemas con **simetría central** (cargas puntuales, campos gravitatorios, átomos). Su economía nace de que $\hat e_r$ absorbe toda la dependencia angular, dejando $\vec r=r\hat e_r$. El precio, como en todo curvilíneo, es una base móvil que se traduce en los factores $h_\theta=r$ y $h_\phi=r\operatorname{sen}\theta$; esos dos factores distintos de $1$ son los que aparecen en todas las [[Operaciones Esfericas]].

> [!referencia]
> - Base y factores de escala en detalle: [[Vectores Base y Factores Escala]].
> - Operadores diferenciales en esféricas: [[Operaciones Esfericas]].
> - Marco general del que desciende: [[Sistemas Curvilineos Generales/index]].
> - Sistema hermano: [[Sistema Cilindrico/index]].
