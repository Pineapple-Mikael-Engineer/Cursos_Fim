#!/usr/bin/env python3
"""Señales de prueba: impulso, rampa, parábola."""
import numpy as np
import ocean_forest as of


def base():
    fig, ax = of.new_fig(figsize=(5.6, 4.0))
    of.style_axes(ax)
    ax.axhline(0, color=of.BROWN, lw=1.0, alpha=0.7)
    ax.axvline(0, color=of.BROWN, lw=1.0, alpha=0.7)
    return fig, ax


# ---------- Impulso delta de Dirac ----------
fig, ax = base()
t = np.linspace(-1, 4, 500)
ax.plot(t, np.zeros_like(t), color=of.CURVE, lw=2.2)
ax.annotate('', xy=(0, 1.0), xytext=(0, 0),
            arrowprops=dict(arrowstyle='-|>', color=of.CURVE, lw=3))
ax.text(0.15, 1.0, r'$(1)$', color=of.CURVE, fontsize=12, va='center')
ax.text(0.15, 0.5, r'$\delta(t)$', color=of.ACCENT, fontsize=14)
ax.set_xlim(-1, 4); ax.set_ylim(-0.25, 1.3)
of.labels(ax, r'$t$', r'$\delta(t)$')
of.title(ax, r'Impulso unitario:  $\mathcal{L}\{\delta(t)\}=1$')
of.save(fig, 'senal_impulso')

# ---------- Rampa unitaria ----------
fig, ax = base()
t = np.linspace(-1, 4, 500)
r = np.where(t >= 0, t, 0)
ax.plot(t, r, color=of.CURVE, lw=2.4)
ax.plot([0, 3], [0, 3], color=of.ACCENT, lw=1.0, ls='--', dashes=(5, 3), alpha=0.7)
ax.text(2.4, 2.0, r'$r(t)=t$', color=of.ACCENT, fontsize=13)
ax.text(2.55, 2.55, 'pend. $=1$', color=of.GRID, fontsize=9, rotation=33)
ax.set_xlim(-1, 4); ax.set_ylim(-0.4, 3.6)
of.labels(ax, r'$t$', r'$r(t)$')
of.title(ax, r'Rampa unitaria:  $\mathcal{L}\{r(t)\}=\dfrac{1}{s^2}$')
of.save(fig, 'senal_rampa')

# ---------- Parábola unitaria ----------
fig, ax = base()
t = np.linspace(-1, 4, 500)
p = np.where(t >= 0, t**2/2, 0)
ax.plot(t, p, color=of.CURVE, lw=2.4)
ax.text(2.0, 3.3, r'$p(t)=\dfrac{t^2}{2}$', color=of.ACCENT, fontsize=13)
ax.set_xlim(-1, 4); ax.set_ylim(-0.6, 6.0)
of.labels(ax, r'$t$', r'$p(t)$')
of.title(ax, r'Parábola unitaria:  $\mathcal{L}\{p(t)\}=\dfrac{1}{s^3}$')
of.save(fig, 'senal_parabola')

print('senales: 3 figuras')
