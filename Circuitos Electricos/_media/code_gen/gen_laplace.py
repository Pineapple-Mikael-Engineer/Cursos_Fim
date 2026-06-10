import numpy as np
import ocean_forest as of


def fig_polos_ceros():
    fig, ax = of.new_fig(figsize=(6.6, 4.8)); of.style_axes(ax)
    ax.axvspan(-6, 0, alpha=0.07, color=of.CURVE)
    ax.axhline(0, color=of.BROWN, lw=1.1); ax.axvline(0, color=of.BROWN, lw=1.1)
    alpha, wd = 1.5, 3.0
    ax.plot([-alpha, -alpha], [wd, -wd], 'x', color=of.CURVE, ms=14, mew=3.2, label='polos')
    ax.plot([-4], [0], 'o', color=of.ACCENT, ms=12, mew=2.4, fillstyle='none', label='cero')
    ax.plot([-alpha, 0], [wd, 0], color=of.GRID, lw=1.0, ls='--')
    ax.plot([-alpha, -alpha], [0, wd], color=of.GRID, lw=0.9, ls=':')
    ax.plot([-alpha, 0], [0, 0], color=of.GRID, lw=0.9, ls=':')
    ax.annotate(r'$-\alpha+j\omega_d$', xy=(-alpha, wd), xytext=(-1.25, 3.55), color=of.TEXT, fontsize=10)
    ax.text(-alpha-0.05, -0.55, r'$-\alpha$', color=of.TEXT, fontsize=9.5, ha='center')
    ax.text(0.12, wd, r'$+\omega_d$', color=of.TEXT, fontsize=9.5, va='center')
    ax.text(0.12, -wd, r'$-\omega_d$', color=of.TEXT, fontsize=9.5, va='center')
    ax.text(-3.0, 4.5, 'semiplano izquierdo:\nestable (decae)', color=of.TEXT, fontsize=9, ha='center')
    ax.text(2.0, 4.5, 'derecho:\ninestable', color=of.TEXT, fontsize=9, ha='center')
    ax.set_xlim(-6, 4); ax.set_ylim(-5, 5.4)
    of.labels(ax, r'Re$(s)=-\alpha$  (amortiguamiento)', r'Im$(s)=\pm\omega_d$  (oscilación)')
    of.title(ax, r'Polos y ceros en el plano $s$')
    of.legend(ax, loc='lower right')
    of.save(fig, 'polos_ceros')


if __name__ == '__main__':
    fig_polos_ceros()
    print('listo')
