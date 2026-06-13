#!/usr/bin/env python3
"""Plano-s: polos/ceros con modos naturales, y semiplanos de estabilidad."""
import numpy as np
import ocean_forest as of

# ---------- Polos y ceros en el plano-s ----------
fig, ax = of.new_fig(figsize=(6.2, 5.4))
of.splane(ax, xlim=(-3.5, 1.5), ylim=(-3, 3))
# par complejo dominante, polo real, cero real
polos = [-0.5+2j, -0.5-2j, -3]
ceros = [-2]
for p in polos:
    of.pole(ax, p)
for z in ceros:
    of.zero(ax, z)
# anotaciones de modos
ax.annotate(r'$e^{-0.5t}\sin(2t)$', xy=(-0.5, 2), xytext=(-3.3, 2.4),
            color=of.CURVE, fontsize=10,
            arrowprops=dict(arrowstyle='->', color=of.GRID, lw=1.2))
ax.annotate(r'$e^{-3t}$ (rápido)', xy=(-3, 0), xytext=(-3.3, -1.3),
            color=of.CURVE, fontsize=10,
            arrowprops=dict(arrowstyle='->', color=of.GRID, lw=1.2))
ax.annotate('cero', xy=(-2, 0), xytext=(-1.6, 0.7),
            color=of.BROWN, fontsize=10,
            arrowprops=dict(arrowstyle='->', color=of.GRID, lw=1.2))
# wn, zeta sobre el polo complejo
p0 = polos[0]
ax.plot([0, p0.real], [0, p0.imag], color=of.ACCENT, lw=1.2, ls='--', dashes=(5, 3))
ax.text(-1.5, 1.35, r'$\omega_n$', color=of.ACCENT, fontsize=12, rotation=-50)
of.title(ax, r'Polos $\times$ y ceros $\circ$ en el plano-$s$')
of.save(fig, 'polos_ceros_plano_s')

# ---------- Semiplanos de estabilidad ----------
fig, ax = of.new_fig(figsize=(6.4, 5.0))
of.splane(ax, xlim=(-3, 3), ylim=(-2.8, 2.8))
ax.axvspan(-3, 0, color=of.CURVE, alpha=0.10)
ax.axvspan(0, 3, color=of.ACCENT, alpha=0.12)
ax.text(-1.5, 2.4, 'ESTABLE', color=of.CURVE, fontsize=13, ha='center', weight='bold')
ax.text(-1.5, 2.05, r'$\Re(p)<0$', color=of.CURVE, fontsize=11, ha='center')
ax.text(1.5, 2.4, 'INESTABLE', color=of.ACCENT, fontsize=13, ha='center', weight='bold')
ax.text(1.5, 2.05, r'$\Re(p)>0$', color=of.ACCENT, fontsize=11, ha='center')
# ejemplos de polos
for p in [-2+1j, -2-1j, -0.6]:
    of.pole(ax, p, color=of.CURVE)
for p in [1.4+0.8j, 1.4-0.8j]:
    of.pole(ax, p, color=of.ACCENT)
of.pole(ax, 1j, color=of.BROWN); of.pole(ax, -1j, color=of.BROWN)
ax.annotate('eje $j\\omega$:\nmarginal', xy=(0, 1), xytext=(0.4, 1.5),
            color=of.BROWN, fontsize=9,
            arrowprops=dict(arrowstyle='->', color=of.BROWN, lw=1.0))
of.title(ax, r'Estabilidad según ubicación de polos')
of.save(fig, 'estabilidad_semiplanos')

print('planos: 2 figuras')
