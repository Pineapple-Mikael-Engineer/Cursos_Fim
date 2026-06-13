import numpy as np
import ocean_forest as of


def fig_potencia_instantanea():
    fig, ax = of.new_fig(figsize=(7.0, 4.3)); of.style_axes(ax)
    t = np.linspace(0, 2*np.pi, 700); phi = np.deg2rad(53)
    v = np.sin(t); i = np.sin(t-phi); p = v*i
    Pavg = 0.5*np.cos(phi)
    ax.plot(t, v, color=of.ACCENT, lw=1.8, label=r'$v$')
    ax.plot(t, i, color=of.GRID, lw=1.8, ls='--', label=r'$i$')
    ax.plot(t, p, color=of.CURVE, lw=2.7, label=r'$p=vi$')
    ax.fill_between(t, p, Pavg, where=(p >= Pavg), color=of.CURVE, alpha=0.10)
    ax.axhline(Pavg, color=of.BROWN, lw=1.6)
    ax.text(0.2, Pavg+0.05, r'$P=V_{ef}I_{ef}\cos\varphi$ (potencia media)', color=of.TEXT, fontsize=9.5)
    ax.axhline(0, color=of.GRID, lw=0.8)
    ax.set_xlim(0, 2*np.pi); ax.set_ylim(-1.15, 1.25)
    of.labels(ax, r'$\omega t$', '')
    of.title(ax, r'Potencia instantánea: oscila a $2\omega$ con media $P$')
    of.legend(ax, loc='upper right')
    of.save(fig, 'potencia_instantanea')


def fig_potencia_elementos():
    fig, (a1, a2, a3) = of.plt.subplots(1, 3, figsize=(9.2, 3.2), sharey=True)
    fig.patch.set_facecolor(of.PANEL)
    t = np.linspace(0, 2*np.pi, 500)
    for ax, phi, title, avg in [(a1, 0.0, r'Resistencia: $p\geq0$ (disipa)', 0.5),
                                (a2, np.pi/2, r'Inductor: media $=0$', 0.0),
                                (a3, -np.pi/2, r'Condensador: media $=0$', 0.0)]:
        of.style_axes(ax)
        p = np.sin(t)*np.sin(t-phi)
        ax.plot(t, p, color=of.CURVE, lw=2.5)
        ax.fill_between(t, p, where=(p >= 0), color=of.CURVE, alpha=0.16)
        ax.fill_between(t, p, where=(p < 0), color=of.BROWN, alpha=0.16)
        ax.axhline(avg, color=of.ACCENT, lw=1.8)
        ax.axhline(0, color=of.GRID, lw=0.7)
        ax.set_xlim(0, 2*np.pi); ax.set_ylim(-0.6, 1.05)
        ax.set_title(title, color=of.TEXT, fontsize=9.5); ax.set_xlabel(r'$\omega t$', fontsize=9)
    a1.set_ylabel(r'$p(t)$')
    fig.tight_layout(); of.save(fig, 'potencia_elementos')


def fig_triangulo_potencias():
    fig, ax = of.new_fig(figsize=(6.0, 4.8)); of.style_axes(ax)
    P, Q = 1.2, 1.6
    ax.annotate('', xy=(P, 0), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=of.ACCENT, lw=2.6))
    ax.annotate('', xy=(P, Q), xytext=(P, 0), arrowprops=dict(arrowstyle='-|>', color=of.BROWN, lw=2.4))
    ax.annotate('', xy=(P, Q), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=of.CURVE, lw=2.9))
    ax.text(P/2, -0.16, r'$P=1200$ W (activa)', color=of.TEXT, ha='center', fontsize=10)
    ax.text(P+0.04, Q/2, r'$Q=1600$ VAr (reactiva)', color=of.TEXT, fontsize=10)
    ax.text(P/2-0.5, Q/2+0.14, r'$S=2000$ VA', color=of.TEXT, fontsize=11, rotation=53)
    arc = np.linspace(0, np.arctan2(Q, P), 40)
    ax.plot(0.4*np.cos(arc), 0.4*np.sin(arc), color=of.GRID, lw=1.5)
    ax.text(0.46, 0.16, r'$\varphi$', color=of.TEXT, fontsize=13)
    ax.text(1.55, 1.75, r'$\cos\varphi=P/S=0{,}6$', color=of.TEXT, fontsize=10)
    ax.set_xlim(-0.2, 2.1); ax.set_ylim(-0.35, 2.0); ax.set_aspect('equal')
    of.labels(ax, r'$P$ (W)', r'$Q$ (VAr)')
    of.title(ax, r'Triángulo de potencias  $S=P+jQ$')
    of.save(fig, 'triangulo_potencias')


def fig_correccion_fp():
    fig, ax = of.new_fig(figsize=(6.2, 4.8)); of.style_axes(ax)
    P, Q, Qp = 1.2, 1.6, 0.58
    ax.annotate('', xy=(P, 0), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=of.ACCENT, lw=2.5))
    # triangulo original (a trazos)
    ax.plot([P, P], [0, Q], color=of.GRID, lw=1.4, ls='--')
    ax.plot([0, P], [0, Q], color=of.GRID, lw=1.8, ls='--')
    ax.text(P/2-0.55, Q/2+0.1, r'$S=2000$ VA', color=of.GRID, fontsize=9, rotation=53)
    # triangulo corregido
    ax.annotate('', xy=(P, Qp), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=of.CURVE, lw=2.8))
    ax.plot([P, P], [0, Qp], color=of.BROWN, lw=2.2)
    ax.text(P/2-0.35, Qp/2+0.06, r"$S'=1333$ VA", color=of.CURVE, fontsize=10, rotation=26)
    # Q_C (lo que aporta el condensador)
    ax.annotate('', xy=(P, Qp), xytext=(P, Q), arrowprops=dict(arrowstyle='-|>', color=of.ACCENT, lw=2.4))
    ax.text(P+0.04, (Q+Qp)/2, r'$Q_C$ (capacitor)', color=of.ACCENT, fontsize=9.5)
    ax.text(P+0.04, Qp/2-0.02, r"$Q'$", color=of.TEXT, fontsize=10)
    ax.text(P/2, -0.16, r'$P=1200$ W (no cambia)', color=of.TEXT, ha='center', fontsize=9.5)
    ax.set_xlim(-0.2, 2.0); ax.set_ylim(-0.35, 1.95); ax.set_aspect('equal')
    of.labels(ax, r'$P$ (W)', r'$Q$ (VAr)')
    of.title(ax, r'Corrección del FP: el capacitor reduce $Q$ (y $S$)')
    of.save(fig, 'correccion_fp')


if __name__ == '__main__':
    fig_potencia_instantanea(); fig_potencia_elementos(); fig_triangulo_potencias(); fig_correccion_fp()
    print('listo')
