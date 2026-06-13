import numpy as np
import ocean_forest as of


def fig_triangulo_impedancia():
    fig, ax = of.new_fig(figsize=(6.0, 5.0)); of.style_axes(ax)
    ax.axhline(0, color=of.BROWN, lw=1.0); ax.axvline(0, color=of.BROWN, lw=1.0)
    R, X = 3.0, 4.0
    ax.annotate('', xy=(R, 0), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=of.ACCENT, lw=2.5))
    ax.annotate('', xy=(R, X), xytext=(R, 0), arrowprops=dict(arrowstyle='-|>', color=of.BROWN, lw=2.3))
    ax.annotate('', xy=(R, X), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=of.CURVE, lw=2.9))
    ax.text(R/2, -0.42, r'$R$ (resistencia)', color=of.TEXT, ha='center', fontsize=11)
    ax.text(R+0.12, X/2, r'$X$ (reactancia)', color=of.TEXT, fontsize=11)
    ax.text(R/2-0.85, X/2+0.35, r'$Z=R+jX$', color=of.TEXT, fontsize=12.5, rotation=53)
    ax.text(R/2-0.85, X/2-0.25, r'$|Z|=\sqrt{R^2+X^2}$', color=of.TEXT, fontsize=10, rotation=53)
    arc = np.linspace(0, np.arctan2(X, R), 40)
    ax.plot(0.85*np.cos(arc), 0.85*np.sin(arc), color=of.GRID, lw=1.5)
    ax.text(1.0, 0.36, r'$\varphi$', color=of.TEXT, fontsize=13)
    ax.text(2.6, 4.35, r'$\varphi=\arctan\dfrac{X}{R}$', color=of.TEXT, fontsize=10)
    ax.set_xlim(-0.5, 5.2); ax.set_ylim(-0.8, 5.0)
    of.labels(ax, r'Re: resistencia $R$', r'Im: reactancia $X$')
    of.title(ax, r'Triángulo de impedancias  $Z=R+jX$')
    of.save(fig, 'triangulo_impedancia')


def fig_respuesta_pasivos():
    fig, (a1, a2, a3) = of.plt.subplots(1, 3, figsize=(9.2, 3.2), sharey=True)
    fig.patch.set_facecolor(of.PANEL)
    t = np.linspace(0, 2*np.pi, 400)
    specs = [(a1, 0.0, r'Resistencia: $i$ en fase con $v$'),
             (a2, -np.pi/2, r'Inductor: $i$ atrasa $90^\circ$'),
             (a3, +np.pi/2, r'Condensador: $i$ adelanta $90^\circ$')]
    for ax, dphi, title in specs:
        of.style_axes(ax)
        ax.plot(t, np.sin(t), color=of.ACCENT, lw=2.5, label=r'$v$')
        ax.plot(t, 0.8*np.sin(t+dphi), color=of.CURVE, lw=2.5, ls='--', label=r'$i$')
        ax.axhline(0, color=of.GRID, lw=0.8)
        ax.set_xlim(0, 2*np.pi); ax.set_ylim(-1.25, 1.25)
        ax.set_title(title, color=of.TEXT, fontsize=9.5)
        ax.set_xlabel(r'$\omega t$', fontsize=9)
        ax.legend(loc='upper right', fontsize=9, framealpha=0.9)
    fig.tight_layout(); of.save(fig, 'respuesta_pasivos')


if __name__ == '__main__':
    fig_triangulo_impedancia(); fig_respuesta_pasivos()
    print('listo')
