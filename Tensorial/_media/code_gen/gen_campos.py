#!/usr/bin/env python3
"""Campos escalares/vectoriales del cap. 2 (equipotenciales + líneas de campo)."""
import numpy as np
import ocean_forest as of

# ---------- 1) Dos líneas de carga ----------
fig, ax = of.new_fig(figsize=(5.8, 4.6)); of.style_axes(ax)
x = np.linspace(-3, 3, 400); y = np.linspace(-2.3, 2.3, 400)
X, Y = np.meshgrid(x, y)
d1 = (X-1)**2 + Y**2; d2 = (X+1)**2 + Y**2
Phi = np.log(d2/d1)
Ex = 4*(X**2 - Y**2 - 1)/(d1*d2)
Ey = 4*(2*X*Y)/(d1*d2)
ax.contour(X, Y, Phi, levels=np.linspace(-3, 3, 13), colors=of.ACCENT,
           linewidths=0.7, alpha=0.7)
ax.streamplot(X, Y, Ex, Ey, color=of.CURVE, density=1.2, linewidth=0.7, arrowsize=0.8)
ax.plot(1, 0, 'o', color=of.BROWN, ms=9)                       # carga +
ax.plot(-1, 0, 'o', mfc='white', mec=of.BROWN, mew=1.6, ms=9)  # carga −
ax.set_xlim(-3, 3); ax.set_ylim(-2.3, 2.3); ax.set_aspect('equal')
of.labels(ax, r'$x$', r'$y$')
of.title(ax, 'Dos líneas de carga: equipotenciales y líneas de campo')
of.save(fig, 'campo_dos_cargas')

# ---------- 2) Silla Φ = -xy ----------
fig, ax = of.new_fig(figsize=(5.2, 4.8)); of.style_axes(ax)
x = np.linspace(-2.5, 2.5, 400); y = np.linspace(-2.5, 2.5, 400)
X, Y = np.meshgrid(x, y)
Phi = -X*Y
U, V = Y, X                      # E = -grad Phi = (y, x)
lv = np.array([-4, -2, -1, -0.3, 0.3, 1, 2, 4])
ax.contour(X, Y, Phi, levels=lv, colors=of.ACCENT, linewidths=0.8, alpha=0.8)
ax.streamplot(X, Y, U, V, color=of.CURVE, density=1.1, linewidth=0.7, arrowsize=0.8)
ax.set_xlim(-2.5, 2.5); ax.set_ylim(-2.5, 2.5); ax.set_aspect('equal')
of.labels(ax, r'$x$', r'$y$')
of.title(ax, r'$\Phi=-xy$: equipotenciales (hipérbolas) y campo')
of.save(fig, 'campo_silla')

# ---------- 3) Vórtice (rotor 0) vs sólido rígido (rotor ≠ 0) ----------
fig, (a1, a2) = of.new_fig(ncols=2, figsize=(9.2, 4.4))
for ax in (a1, a2):
    of.style_axes(ax); ax.set_aspect('equal')
    ax.set_xlim(-2, 2); ax.set_ylim(-2, 2)
x = np.linspace(-2, 2, 300); y = np.linspace(-2, 2, 300)
X, Y = np.meshgrid(x, y)
# rígido: v=(-y,x) -> rotor = 2 ê_z
a1.streamplot(X, Y, -Y, X, color=of.CURVE, density=1.1, linewidth=0.7, arrowsize=0.8)
of.title(a1, r'Sólido rígido $\vec v=(-y,x)$: rotor $=2\hat e_z\neq0$')
of.labels(a1, r'$x$', r'$y$')
# vórtice: v=(-y,x)/r^2 -> rotor = 0 (salvo origen)
r2 = X**2 + Y**2 + 1e-9
a2.streamplot(X, Y, -Y/r2, X/r2, color=of.CURVE, density=1.1, linewidth=0.7, arrowsize=0.8)
a2.plot(0, 0, 'o', color=of.BROWN, ms=6)
of.title(a2, r'Vórtice $\vec v=(-y,x)/r^2$: rotor $=0$')
of.labels(a2, r'$x$', r'$y$')
of.save(fig, 'rotor_vortice_vs_rigido')

print('campos: 3 figuras')
