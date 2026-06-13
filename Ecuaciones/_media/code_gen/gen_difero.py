#!/usr/bin/env python3
"""Figuras del capitulo Difero-integrales (integro-dif. + calculo fraccionario).
Estilo Ocean Forest. Salida -> ../img_gen/*.svg"""
import numpy as np
from scipy.special import gamma
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize, LinearSegmentedColormap
import ocean_forest as of

QCMAP = LinearSegmentedColormap.from_list('q', ['#2e4824', '#6a8858', '#cdbb86', '#b07828'])


# ---------------------------------------------------------- 1. el differintegral D^q x
def fig_differintegral():
    fig, ax = of.new_fig(figsize=(6.8, 4.6)); of.style_axes(ax)
    x = np.linspace(0.015, 2.0, 400)
    qs = [-1.0, -0.5, 0.0, 0.5, 1.0, 1.5]
    norm = Normalize(vmin=-1, vmax=2)
    # posición y manual de cada etiqueta (para evitar solapes en el borde derecho)
    ylab = {-1.0: 2.18, -0.5: 1.92, 0.0: 1.62, 0.5: 1.30, 1.0: 1.0, 1.5: 0.42}
    for q in qs:
        y = x**(1-q)/gamma(2-q)        # D^q x = x^{1-q}/Gamma(2-q)
        col = QCMAP(norm(q))
        ax.plot(x, y, color=col, lw=2.5)
        lbl = {-1: r'$q=-1$ (integral)', 0: r'$q=0$ (función)', 1: r'$q=1$ (derivada)'}.get(q, fr'$q={q}$')
        ax.text(2.05, ylab[q], lbl, color=col, fontsize=8.5, va='center')
    ax.axhline(0, color=of.BROWN, lw=0.8, alpha=0.5)
    ax.text(1.0, 0.06, r'$q=2$ (2ª derivada) $\to 0$', color=of.TICK, fontsize=8.5)
    ax.set_xlim(0, 2.7); ax.set_ylim(-0.1, 2.3)
    of.labels(ax, r'$x$', r'$D^{q}x$')
    of.title(ax, r'El differintegral: $D^{q}x=\dfrac{x^{1-q}}{\Gamma(2-q)}$ al variar el orden $q$')
    sm = ScalarMappable(norm=norm, cmap=QCMAP); sm.set_array([])
    cb = fig.colorbar(sm, ax=ax, fraction=0.04, pad=0.13)
    cb.set_label(r'orden $q$', color=of.TEXT); cb.ax.tick_params(colors=of.TICK)
    of.save(fig, 'differintegral')


# ---------------------------------------------------------- 2. memoria corta vs larga
def fig_memoria_viscoelasticidad():
    fig, ax = of.new_fig(figsize=(6.6, 4.4)); of.style_axes(ax)
    t = np.linspace(0.02, 6, 500)
    G_exp = np.exp(-t/0.8)                       # Maxwell: memoria corta
    al = 0.5
    G_pow = (1 + t/0.8)**(-al)                   # ley de potencias: memoria larga
    ax.plot(t, G_exp, color=of.ACCENT, lw=2.6, label=r'exponencial $e^{-t/\tau}$ (memoria corta)')
    ax.plot(t, G_pow, color=of.CURVE, lw=2.6, label=r'ley de potencias $\sim t^{-\alpha}$ (memoria larga)')
    ax.fill_between(t, 0, G_pow, color=of.CURVE, alpha=0.08)
    ax.annotate('cola larga:\nmemoria persistente', xy=(4.5, G_pow[np.argmin(np.abs(t-4.5))]),
                xytext=(3.0, 0.55), color=of.TEXT, fontsize=9.5,
                arrowprops=dict(arrowstyle='->', color=of.BROWN))
    ax.set_xlim(0, 6); ax.set_ylim(0, 1.03)
    of.labels(ax, r'$t$', r'módulo de relajación $G(t)$')
    of.title(ax, r'Núcleo de memoria: corta (exponencial) vs larga (ley de potencias)')
    of.legend(ax, loc='upper right')
    of.save(fig, 'memoria_viscoelasticidad')


from scipy.special import gammaln


def _mlf_neg(alpha, x, K=160):
    """E_alpha(-x) para x>=0 (array), por serie en log-magnitud."""
    x = np.asarray(x, float); s = np.zeros_like(x)
    pos = x > 0; lx = np.zeros_like(x); lx[pos] = np.log(x[pos])
    for k in range(K):
        mag = np.exp(k*lx - gammaln(alpha*k + 1.0))
        term = ((-1.0)**k)*mag
        term = np.where(pos, term, 1.0 if k == 0 else 0.0)
        s = s + term
    return s


# ---------------------------------------------------------- 3. Mittag-Leffler vs exponencial
def fig_mittag_leffler():
    fig, ax = of.new_fig(figsize=(6.6, 4.4)); of.style_axes(ax)
    t = np.linspace(0, 6, 400)
    for a, c in [(0.5, of.CURVE), (0.75, of.ACCENT), (1.0, of.BROWN)]:
        y = _mlf_neg(a, t**a)
        lbl = (r'$\alpha=1$:  $e^{-t}$ (exponencial)' if a == 1
               else fr'$\alpha={a}$:  cola $\sim t^{{-\alpha}}$')
        ax.plot(t, y, color=c, lw=2.6, ls='-' if a == 1 else '--', label=lbl)
    ax.axhline(0, color=of.BROWN, lw=0.7, alpha=0.4)
    ax.annotate('memoria larga:\ndecae como ley de potencias',
                xy=(4.6, _mlf_neg(0.5, np.array([4.6**0.5]))[0]),
                xytext=(2.7, 0.62), color=of.TEXT, fontsize=9,
                arrowprops=dict(arrowstyle='->', color=of.BROWN))
    ax.set_xlim(0, 6); ax.set_ylim(0, 1.03)
    of.labels(ax, r'$t$', r'$E_{\alpha}(-t^{\alpha})$')
    of.title(ax, r'Mittag-Leffler: la "exponencial fraccionaria" $E_{\alpha}(-t^{\alpha})$')
    of.legend(ax, loc='upper right')
    of.save(fig, 'mittag_leffler')


# ---------------------------------------------------------- 4. difusion anomala (MSD ~ t^alpha)
def fig_difusion_anomala():
    fig, ax = of.new_fig(figsize=(6.4, 4.4)); of.style_axes(ax)
    t = np.logspace(-1, 2, 200)
    for a, c, lbl in [(0.5, of.CURVE, r'subdifusión $\alpha=0.5$ (atrapamiento)'),
                      (1.0, of.ACCENT, r'difusión normal $\alpha=1$ (browniana)'),
                      (1.5, of.BROWN, r'superdifusión $\alpha=1.5$ (Lévy)')]:
        ax.loglog(t, t**a, color=c, lw=2.6, label=lbl)
    ax.set_xlim(0.1, 100)
    of.labels(ax, r'tiempo $t$', r'$\langle x^{2}\rangle \sim t^{\alpha}$')
    of.title(ax, r'Difusión anómala: la pendiente log-log es $\alpha$')
    of.legend(ax, loc='upper left')
    of.save(fig, 'difusion_anomala')


if __name__ == '__main__':
    print('Generando figuras Difero-integrales:')
    fig_differintegral()
    fig_memoria_viscoelasticidad()
    fig_mittag_leffler()
    fig_difusion_anomala()
    print('Listo.')
