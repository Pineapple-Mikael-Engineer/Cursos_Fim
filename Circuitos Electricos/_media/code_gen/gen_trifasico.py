import numpy as np
import ocean_forest as of


def fig_tres_fases():
    fig, (a1, a2) = of.plt.subplots(1, 2, figsize=(9.0, 3.8), gridspec_kw={'width_ratios': [1.7, 1]})
    fig.patch.set_facecolor(of.PANEL)
    for ax in (a1, a2): of.style_axes(ax)
    t = np.linspace(0, 4*np.pi, 600)
    fases = [(0, of.CURVE, 'a'), (-120, of.ACCENT, 'b'), (-240, of.BROWN, 'c')]
    for ph, c, lab in fases:
        a1.plot(t, np.sin(t+np.deg2rad(ph)), color=c, lw=2.4, label=fr'$v_{lab}$')
    a1.axhline(0, color=of.GRID, lw=0.8)
    a1.set_xlim(0, 4*np.pi); a1.set_ylim(-1.25, 1.25)
    a1.set_title(r'tres tensiones desfasadas $120^\circ$', color=of.TEXT, fontsize=11)
    a1.set_xlabel(r'$\omega t$'); a1.legend(loc='upper right', ncol=3, fontsize=9, framealpha=0.9)
    # fasores
    a2.axhline(0, color=of.GRID, lw=0.7); a2.axvline(0, color=of.GRID, lw=0.7)
    for ph, c, lab in fases:
        a = np.deg2rad(ph)
        a2.annotate('', xy=(np.cos(a), np.sin(a)), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='-|>', color=c, lw=2.6))
        a2.text(1.12*np.cos(a), 1.12*np.sin(a), fr'$\overline{{V}}_{lab}$', color=c, fontsize=12,
                ha='center', va='center')
    a2.set_xlim(-1.4, 1.4); a2.set_ylim(-1.4, 1.4); a2.set_aspect('equal')
    a2.set_title('fasores a $120^\circ$', color=of.TEXT, fontsize=11)
    fig.tight_layout(); of.save(fig, 'tres_fases')


if __name__ == '__main__':
    fig_tres_fases()
    print('listo')


def _phasor(ax, ang_deg, color, lab, r=1.0):
    import numpy as _np
    a = _np.deg2rad(ang_deg)
    ax.annotate('', xy=(r*_np.cos(a), r*_np.sin(a)), xytext=(0, 0),
                arrowprops=dict(arrowstyle='-|>', color=color, lw=2.5))
    ax.text(1.18*r*_np.cos(a), 1.18*r*_np.sin(a), lab, color=color, fontsize=11,
            ha='center', va='center')


def fig_componentes_simetricas():
    import numpy as _np
    fig, axs = of.plt.subplots(1, 3, figsize=(9.6, 3.5))
    fig.patch.set_facecolor(of.PANEL)
    cols = [of.CURVE, of.ACCENT, of.BROWN]
    titles = ['secuencia positiva\n($abc$)', 'secuencia negativa\n($acb$)', 'homopolar (en fase)']
    seqs = [[0, -120, 120], [0, 120, -120], [4, 0, -4]]
    labs = [['$a_1$', '$b_1$', '$c_1$'], ['$a_2$', '$b_2$', '$c_2$'], ['$a_0$', '$b_0$', '$c_0$']]
    for ax, ttl, seq, lb in zip(axs, titles, seqs, labs):
        of.style_axes(ax)
        ax.axhline(0, color=of.GRID, lw=0.7); ax.axvline(0, color=of.GRID, lw=0.7)
        for ang, c, l in zip(seq, cols, lb):
            _phasor(ax, ang, c, l)
        ax.set_xlim(-1.45, 1.45); ax.set_ylim(-1.45, 1.45); ax.set_aspect('equal')
        ax.set_title(ttl, color=of.TEXT, fontsize=10.5)
    fig.tight_layout(); of.save(fig, 'componentes_simetricas')


if __name__ == '__main__':
    fig_componentes_simetricas()
    print('comp listo')
