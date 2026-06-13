#!/usr/bin/env python3
"""Figuras varias: reducción de orden, rango de K (Routh), tipo de sistema,
coeficientes Kp/Kv/Ka, ganancia estática."""
import numpy as np
from scipy import signal
import ocean_forest as of


def step_tf(num, den, t):
    _, y = signal.step((num, den), T=t)
    return y


# ---------- Reducción de orden ----------
fig, ax = of.new_fig(figsize=(6.6, 4.2))
of.style_axes(ax)
t = np.linspace(0, 6, 1000)
# completo: polo dominante -1 + polo rápido -8  (DC gain 1)
yf = step_tf([8], np.polymul([1, 1], [1, 8]), t)
# reducido: solo polo dominante (mismo DC gain)
yr = step_tf([1], [1, 1], t)
ax.axhline(1, color=of.BROWN, lw=1.0, ls='--', dashes=(5, 3), alpha=0.6)
ax.plot(t, yf, color=of.CURVE, lw=2.2, label=r'completo $\frac{8}{(s+1)(s+8)}$')
ax.plot(t, yr, color=of.ACCENT, lw=2.0, ls='--', dashes=(6, 3),
        label=r'reducido $\frac{1}{s+1}$')
ax.set_xlim(0, 6); ax.set_ylim(0, 1.15)
of.labels(ax, r'$t$ [s]', r'$y(t)$')
of.title(ax, r'Reducción de orden: polo dominante $s=-1$')
of.legend(ax, fontsize=9, loc='lower right')
of.save(fig, 'reduccion_orden_comparacion')

# ---------- Rango de K estable (Routh) ----------
fig, ax = of.new_fig(figsize=(6.8, 2.4))
of.style_axes(ax)
ax.set_ylim(-1, 1); ax.set_xlim(-1, 9)
ax.get_yaxis().set_visible(False)
for sp in ['left', 'right', 'top']:
    ax.spines[sp].set_visible(False)
ax.axhline(0, color=of.BROWN, lw=1.4)
ax.annotate('', xy=(9, 0), xytext=(-1, 0),
            arrowprops=dict(arrowstyle='-|>', color=of.BROWN, lw=1.4))
# región estable 0 < K < 6
ax.axvspan(0, 6, ymin=0.42, ymax=0.58, color=of.CURVE, alpha=0.25)
ax.plot([0, 6], [0, 0], color=of.CURVE, lw=6, alpha=0.5, solid_capstyle='butt')
for x, lab, c in [(0, r'$K=0$', of.BROWN), (6, r'$K_{cr}=6$', of.ACCENT)]:
    ax.plot(x, 0, 'o', color=c, ms=8, zorder=4)
    ax.text(x, -0.45, lab, color=c, fontsize=11, ha='center')
ax.text(3, 0.45, 'estable', color=of.CURVE, fontsize=12, ha='center', weight='bold')
ax.text(7.5, 0.45, 'inestable', color=of.ACCENT, fontsize=11, ha='center')
ax.text(9, -0.45, r'$K$', color=of.BROWN, fontsize=13, ha='center')
of.title(ax, r'Rango de ganancia estable por Routh-Hurwitz')
of.save(fig, 'routh_ajuste_k_rango')

# ---------- Tipo de sistema: respuesta a rampa ----------
fig, ax = of.new_fig(figsize=(6.6, 4.4))
of.style_axes(ax)
t = np.linspace(0, 10, 1200)
ramp = t
ax.plot(t, ramp, color=of.BROWN, lw=1.6, ls='--', dashes=(6, 3), label='entrada rampa $r(t)=t$')
# tipo 0: G=2/(s+1) -> lazo cerrado sigue mal (ess infinito en rampa)
sys0 = signal.TransferFunction([2], [1, 1])
cl0 = signal.TransferFunction(np.polymul([2], [1]),
                              np.polyadd(np.polymul([1, 1], [1, 0]), [0, 0, 2]))
# Construir lazos cerrados unitarios y respuesta a rampa via step de G*(1/s)
def ramp_resp(numG, denG):
    # T = G/(1+G); respuesta a rampa = step de T*(1/s)
    numT = numG
    denT = np.polyadd(np.polymul(denG, [1]), np.polymul(numG, [1])) if len(denG) >= len(numG) else None
    # cerrar lazo
    denT = np.polyadd(denG, np.r_[np.zeros(len(denG)-len(numG)), numG])
    # multiplicar por 1/s -> integрar
    num2, den2 = numT, np.polymul(denT, [1, 0])
    _, y = signal.step((num2, den2), T=t)
    return y

y0 = ramp_resp([2], [1, 1])            # tipo 0
y1 = ramp_resp([2], [1, 1, 0])         # tipo 1  (un integrador)
y2 = ramp_resp([4, 4], [1, 0, 0])      # tipo 2  L=(4s+4)/s^2 -> T=(4s+4)/(s+2)^2 estable
ax.plot(t, y0, color=of.ACCENT, lw=2.0, label='tipo 0 ($e_{ss}\\to\\infty$)')
ax.plot(t, y1, color=of.CURVE, lw=2.0, label='tipo 1 ($e_{ss}=1/K_v$)')
ax.plot(t, y2, color='#3a5a2a', lw=2.0, ls=':', label='tipo 2 ($e_{ss}=0$)')
ax.set_xlim(0, 10); ax.set_ylim(0, 10)
of.labels(ax, r'$t$ [s]', r'$y(t)$')
of.title(ax, r'Seguimiento de rampa según tipo de sistema')
of.legend(ax, fontsize=9, loc='upper left')
of.save(fig, 'error_tipo_sistema')

# ---------- Coeficientes Kp/Kv/Ka: ess por entrada (sistema tipo 1) ----------
fig, axs = of.new_fig(ncols=3, figsize=(9.4, 3.4))
t = np.linspace(0, 8, 800)
titles = [r'Escalón: $e_{ss}=\frac{1}{1+K_p}=0$',
          r'Rampa: $e_{ss}=\frac{1}{K_v}$',
          r'Parábola: $e_{ss}\to\infty$']
inputs = [np.ones_like(t), t, t**2/2]
# tipo 1: G = 2/(s(s+1)), T = G/(1+G)
numG, denG = [2], [1, 1, 0]
denT = np.polyadd(denG, np.r_[np.zeros(len(denG)-len(numG)), numG])
# escalón: T (sin integración extra); rampa: T/s; parábola: T/s^2
for ax, ti, u, mult in zip(axs, titles, inputs, [[1], [1, 0], [1, 0, 0]]):
    of.style_axes(ax)
    num2, den2 = numG, np.polymul(denT, mult)
    _, y = signal.step((num2, den2), T=t)
    ax.plot(t, u, color=of.BROWN, lw=1.4, ls='--', dashes=(6, 3))
    ax.plot(t, y, color=of.CURVE, lw=2.0)
    ax.set_xlim(0, 8)
    ax.set_title(ti, fontsize=9, color=of.TEXT)
axs[0].set_ylim(0, 1.4); axs[1].set_ylim(0, 8); axs[2].set_ylim(0, 35)
of.labels(axs[0], r'$t$', 'amplitud')
fig.suptitle(r'Error estacionario y coeficientes $K_p,K_v,K_a$ (sistema tipo 1)',
             color=of.TEXT, fontsize=12)
of.save(fig, 'error_coef_kp_kv_ka')

# ---------- Ganancia estática ----------
fig, ax = of.new_fig(figsize=(6.4, 4.0))
of.style_axes(ax)
t = np.linspace(0, 6, 800)
K = 2.0
y = step_tf([K], [1, 1], t)   # G=2/(s+1), G(0)=2
ax.plot(t, y, color=of.CURVE, lw=2.2)
ax.axhline(K, color=of.ACCENT, lw=1.4, ls='--', dashes=(6, 3))
ax.text(4.2, K+0.12, r'$y(\infty)=G(0)=K=2$', color=of.ACCENT, fontsize=11)
ax.plot(0, 0, 'o', color=of.BROWN, ms=6)
ax.set_xlim(0, 6); ax.set_ylim(0, 2.4)
of.labels(ax, r'$t$ [s]', r'$y(t)$')
of.title(ax, r'Ganancia estática $G(0)$: valor final ante escalón unitario')
of.save(fig, 'ganancia_estatica_escalon')

print('misc: 5 figuras')
