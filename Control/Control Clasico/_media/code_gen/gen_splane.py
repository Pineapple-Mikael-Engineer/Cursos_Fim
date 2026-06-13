#!/usr/bin/env python3
"""Genera gráficas de plano-s y lugar de raíces (en ../img_gen/). Uso: python3 gen_splane.py"""
import numpy as np
import ocean_forest as of


def locus(num, den, Kmax=200, nK=4000):
    """Calcula el lugar de raíces de 1 + K num/den = 0 para K en [0, Kmax]."""
    Ks = np.linspace(1e-3, Kmax, nK)
    num = np.atleast_1d(num).astype(float)
    den = np.atleast_1d(den).astype(float)
    n = len(den)
    roots = np.zeros((nK, n-1), dtype=complex)
    npad = np.zeros(n); npad[n-len(num):] = num
    for i, K in enumerate(Ks):
        roots[i] = np.roots(den + K*npad)
    return roots


def lead_diseno():
    # planta 1/(s(s+4)), lead: cero -2, polo -20
    den = np.poly([0, -4, -20]); num = [1, 2]
    R = locus(num, den, Kmax=400)
    fig, ax = of.new_fig(figsize=(5.8, 5.4)); of.splane(ax, xlim=(-22, 4), ylim=(-12, 12))
    for j in range(R.shape[1]):
        ax.plot(R[:, j].real, R[:, j].imag, color=of.CURVE, lw=1.6)
    of.pole(ax, 0); of.pole(ax, -4); of.pole(ax, -20); of.zero(ax, -2)
    ax.plot(-3, 5, '*', color=of.ACCENT, ms=16); ax.annotate(r'$s_d$', (-3, 5),
            color=of.TEXT, xytext=(8, 0), textcoords='offset points')
    of.title(ax, 'Diseño lead: el cero atrae el lugar a la izquierda')
    of.save(fig, 'lgr_lead_diseno')


def lag_diseno():
    """Mapa polo-cero: el par lag junto al origen casi no mueve los polos dominantes."""
    fig, ax = of.new_fig(figsize=(6.6, 4.6))
    of.splane(ax, xlim=(-4, 0.6), ylim=(-1.8, 1.8))
    dom = -1.5+1.3j
    of.pole(ax, dom, color=of.ACCENT); of.pole(ax, np.conj(dom), color=of.ACCENT)
    of.pole(ax, -3)                              # polo de planta
    of.pole(ax, -0.06); of.zero(ax, -0.4)        # par lag junto al origen
    ax.annotate('polos dominantes\n(casi no se mueven)', (dom.real, dom.imag),
                color=of.TEXT, fontsize=9, xytext=(8, 8), textcoords='offset points')
    ax.annotate('par lag\njunto al origen', (-0.23, 0), color=of.TEXT, fontsize=9,
                ha='center', xytext=(0, -46), textcoords='offset points',
                arrowprops=dict(arrowstyle='->', color=of.BROWN, lw=1))
    # zoom del origen en esquina superior izquierda (zona vacía)
    axins = ax.inset_axes([0.05, 0.60, 0.34, 0.34])
    of.style_axes(axins)
    axins.axhline(0, color=of.BROWN, lw=0.8, alpha=0.6)
    of.pole(axins, -0.06, ms=10, mew=2.5); of.zero(axins, -0.4, ms=10, mew=2)
    axins.set_xlim(-0.6, 0.1); axins.set_ylim(-0.12, 0.12)
    axins.set_xticks([-0.4, 0]); axins.set_yticks([]); axins.tick_params(labelsize=7)
    axins.set_title('zoom origen', color=of.TEXT, fontsize=8)
    of.title(ax, 'Diseño lag: par cero-polo junto al origen')
    of.save(fig, 'lgr_lag_diseno')


def angulo_salida():
    p1, p2, p3 = -1+2j, -1-2j, -3+0j   # par complejo + polo real -> theta_d = 45 deg
    fig, ax = of.new_fig(figsize=(6.2, 5.4)); of.splane(ax, xlim=(-4, 1.2), ylim=(-3, 3))
    for p in (p1, p2, p3):
        of.pole(ax, p)
    # vectores de contribucion hacia p1 (faint)
    for src in (p2, p3):
        ax.annotate('', xy=(p1.real, p1.imag), xytext=(src.real, src.imag),
                    arrowprops=dict(arrowstyle='-|>', color=of.BROWN, lw=1.2, alpha=0.55))
    ax.annotate(r'$90^\circ$', (p1.real+0.08, p1.imag-1.1), color=of.TEXT, fontsize=9)
    ax.annotate(r'$45^\circ$', (p1.real-1.3, p1.imag-0.85), color=of.TEXT, fontsize=9)
    # linea de referencia horizontal y angulo de salida
    ax.plot([p1.real, p1.real+1.1], [p1.imag, p1.imag], color=of.BROWN, lw=0.9, ls=':')
    th = 45.0; L = 1.5
    ax.annotate('', xy=(p1.real+L*np.cos(np.radians(th)), p1.imag+L*np.sin(np.radians(th))),
                xytext=(p1.real, p1.imag),
                arrowprops=dict(arrowstyle='-|>', color=of.ACCENT, lw=2.4))
    arc = np.linspace(0, np.radians(th), 40)
    ax.plot(p1.real+0.6*np.cos(arc), p1.imag+0.6*np.sin(arc), color=of.ACCENT, lw=1.6)
    ax.annotate(r'$\theta_d$', (p1.real+0.75, p1.imag+0.32), color=of.TEXT)
    ax.annotate(r'$p_1$', (p1.real, p1.imag), color=of.TEXT, ha='right',
                xytext=(-8, 8), textcoords='offset points')
    ax.annotate(r'$\theta_d = 180^\circ - (90^\circ + 45^\circ) = 45^\circ$', (-3.9, 2.6),
                color=of.TEXT, fontsize=10)
    of.title(ax, 'Ángulo de salida de un polo complejo')
    of.save(fig, 'lgr_angulo_salida')


def cruce_eje():
    # 1 + K/(s(s+1)(s+2)) ; cruza jw en w=sqrt(2), K=6
    den = np.poly([0, -1, -2]); num = [1]
    R = locus(num, den, Kmax=40)
    fig, ax = of.new_fig(figsize=(5.6, 5.4)); of.splane(ax, xlim=(-3.5, 1.5), ylim=(-3, 3))
    for j in range(R.shape[1]):
        ax.plot(R[:, j].real, R[:, j].imag, color=of.CURVE, lw=1.6)
    of.pole(ax, 0); of.pole(ax, -1); of.pole(ax, -2)
    wc = np.sqrt(2)
    ax.plot([0, 0], [wc, -wc], '*', color=of.ACCENT, ms=15)
    ax.annotate(r'$\pm j\sqrt{2}$, $K_{cr}=6$', (0, wc), color=of.TEXT,
                xytext=(8, 0), textcoords='offset points')
    of.title(ax, 'Cruce del eje imaginario (ganancia crítica)')
    of.save(fig, 'lgr_cruce_eje_imaginario')


def polos_dominantes():
    fig, ax = of.new_fig(figsize=(5.8, 5.0)); of.splane(ax, xlim=(-11, 1), ylim=(-4, 4))
    dom = -1+2j
    of.pole(ax, dom, color=of.ACCENT); of.pole(ax, np.conj(dom), color=of.ACCENT)
    for p in [-8, -9, -10]:
        of.pole(ax, p)
    ax.axvspan(-2, 0, color=of.ACCENT, alpha=0.10)
    ax.annotate('par dominante', (dom.real, dom.imag), color=of.TEXT,
                xytext=(10, 6), textcoords='offset points')
    ax.annotate('polos rápidos\n(despreciables)', (-9, 0), color=of.TEXT, fontsize=9,
                ha='center', xytext=(0, 30), textcoords='offset points')
    of.title(ax, r'Polos dominantes vs lejanos ($\geq 5\times$)')
    of.save(fig, 'polos_dominantes_plano_s')


if __name__ == '__main__':
    print('Generando plano-s / lugar de raíces...')
    lead_diseno(); lag_diseno(); angulo_salida(); cruce_eje(); polos_dominantes()
    print('OK')
