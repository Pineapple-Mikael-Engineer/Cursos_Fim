#!/usr/bin/env python3
"""Respuesta temporal de 2.º orden — especificaciones (Mp, Tp, Ts, Tr)."""
import numpy as np
import ocean_forest as of

ANN = of.TEXT  # color de anotaciones


def step2(zeta, wn, t):
    """Respuesta a escalón unitario de 2.º orden subamortiguado."""
    wd = wn * np.sqrt(1 - zeta**2)
    th = np.arccos(zeta)
    return 1 - np.exp(-zeta*wn*t)/np.sqrt(1-zeta**2) * np.sin(wd*t + th)


def base_ax(t, y, ylim=(0, 1.7)):
    fig, ax = of.new_fig(figsize=(6.6, 4.2))
    of.style_axes(ax)
    ax.axhline(1, color=of.BROWN, lw=1.0, ls='--', dashes=(5, 3), alpha=0.7)
    ax.plot(t, y, color=of.CURVE, lw=2.2, zorder=3)
    ax.set_xlim(t[0], t[-1]); ax.set_ylim(*ylim)
    of.labels(ax, r'$t$ [s]', r'$y(t)$')
    return fig, ax


zeta, wn = 0.4, 1.0
wd = wn*np.sqrt(1-zeta**2)
t = np.linspace(0, 16, 1400)
y = step2(zeta, wn, t)

# ---------- 1) Sobrepico Mp ----------
fig, ax = base_ax(t, y)
tp = np.pi/wd
yp = 1 + np.exp(-zeta*wn*tp)
ax.plot(tp, yp, 'o', color=of.ACCENT, ms=8, zorder=4)
ax.annotate('', xy=(tp, yp), xytext=(tp, 1.0),
            arrowprops=dict(arrowstyle='<->', color=of.ACCENT, lw=1.6))
ax.text(tp+0.3, (1+yp)/2, r'$M_p$', color=of.ACCENT, fontsize=14, va='center')
ax.axvline(tp, color=of.GRID, lw=1.0, ls=':', alpha=0.6)
ax.text(0.3, 1.04, r'$y(\infty)=1$', color=of.BROWN, fontsize=10)
ax.text(tp, yp+0.05, r'$y(t_p)=1+M_p$', color=of.ACCENT, fontsize=10, ha='center')
of.title(ax, r'Sobrepico máximo: $M_p=e^{-\pi\zeta/\sqrt{1-\zeta^2}}$  ($\zeta=0.4$)')
of.save(fig, 'resp_sobrepico_mp')

# ---------- 2) Tiempo de pico Tp ----------
fig, ax = base_ax(t, y)
ax.plot(tp, yp, 'o', color=of.ACCENT, ms=8, zorder=4)
ax.axvline(tp, color=of.ACCENT, lw=1.4, ls='--', dashes=(5, 3))
ax.annotate('', xy=(tp, 0.0), xytext=(0, 0.0),
            arrowprops=dict(arrowstyle='<->', color=of.ACCENT, lw=1.6))
ax.text(tp/2, 0.08, r'$t_p$', color=of.ACCENT, fontsize=14, ha='center')
ax.text(tp+0.2, yp, 'primer pico', color=of.ACCENT, fontsize=10, va='center')
of.title(ax, r'Tiempo de pico: $t_p=\dfrac{\pi}{\omega_d}=\dfrac{\pi}{\omega_n\sqrt{1-\zeta^2}}$')
of.save(fig, 'resp_tiempo_pico_tp')

# ---------- 3) Tiempo de establecimiento Ts ----------
fig, ax = base_ax(t, y)
ax.axhspan(0.98, 1.02, color=of.ACCENT, alpha=0.13)
ax.axhline(1.02, color=of.ACCENT, lw=1.0, ls='--', dashes=(5, 3), alpha=0.8)
ax.axhline(0.98, color=of.ACCENT, lw=1.0, ls='--', dashes=(5, 3), alpha=0.8)
ts = 4/(zeta*wn)
ax.axvline(ts, color=of.ACCENT, lw=1.4, ls='--', dashes=(5, 3))
ax.plot(ts, step2(zeta, wn, np.array([ts]))[0], 'o', color=of.ACCENT, ms=8, zorder=4)
ax.text(ts+0.2, 0.5, r'$t_s\approx\dfrac{4}{\zeta\omega_n}$', color=of.ACCENT, fontsize=12)
ax.text(t[-1]-0.3, 1.025, r'$\pm 2\%$', color=of.ACCENT, fontsize=10, ha='right', va='bottom')
of.title(ax, r'Tiempo de establecimiento (banda $\pm 2\%$)')
of.save(fig, 'resp_tiempo_establecimiento_ts')

# ---------- 4) Tiempo de subida Tr ----------
fig, ax = base_ax(t[:600], y[:600], ylim=(0, 1.7))
# cruces 10% y 90% (primera subida)
i10 = np.argmax(y >= 0.1); i90 = np.argmax(y >= 0.9)
t10, t90 = t[i10], t[i90]
for tx, yx, lab in [(t10, 0.1, '10\\%'), (t90, 0.9, '90\\%')]:
    ax.plot(tx, yx, 'o', color=of.ACCENT, ms=7, zorder=4)
    ax.axhline(yx, xmax=tx/t[599], color=of.GRID, lw=0.9, ls=':', alpha=0.6)
ax.annotate('', xy=(t90, 0.5), xytext=(t10, 0.5),
            arrowprops=dict(arrowstyle='<->', color=of.ACCENT, lw=1.6))
ax.text((t10+t90)/2, 0.42, r'$t_r$', color=of.ACCENT, fontsize=14, ha='center', va='top')
ax.text(t10-0.1, 0.13, r'$10\%$', color=of.ACCENT, fontsize=9, ha='right')
ax.text(t90+0.1, 0.86, r'$90\%$', color=of.ACCENT, fontsize=9)
of.title(ax, r'Tiempo de subida ($10\%\!\to\!90\%$ del valor final)')
of.save(fig, 'resp_tiempo_subida_tr')

print('resp_temporal: 4 figuras')
