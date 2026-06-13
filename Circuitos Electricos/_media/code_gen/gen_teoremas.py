import numpy as np
import ocean_forest as of


def fig_max_transferencia():
    fig, ax = of.new_fig(figsize=(6.6, 4.3)); of.style_axes(ax)
    Vth, Rth = 8.0, 4.0
    RL = np.linspace(0.02, 20, 500)
    P = Vth**2 * RL / (Rth + RL)**2
    Pmax = Vth**2 / (4*Rth)
    ax.plot(RL, P, color=of.CURVE, lw=2.7, label=r'$P_L=\dfrac{V_{Th}^2\,R_L}{(R_{Th}+R_L)^2}$')
    ax.axvline(Rth, color=of.BROWN, lw=0.9, ls='--', alpha=0.6)
    ax.plot([Rth], [Pmax], 'o', color=of.ACCENT, ms=10, zorder=5)
    ax.annotate('máximo en $R_L=R_{Th}$\n$P_{max}=V_{Th}^2/4R_{Th}=4$ W',
                xy=(Rth, Pmax), xytext=(7.5, 2.9), color=of.TEXT, fontsize=10,
                arrowprops=dict(arrowstyle='->', color=of.BROWN))
    ax.set_xlim(0, 20); ax.set_ylim(0, Pmax*1.18)
    of.labels(ax, r'resistencia de carga $R_L\ (\Omega)$', r'potencia en la carga $P_L\ (\mathrm{W})$')
    of.title(ax, r'Máxima transferencia de potencia ($V_{Th}=8$ V, $R_{Th}=4\ \Omega$)')
    of.legend(ax, loc='upper right')
    of.save(fig, 'max_transferencia')


if __name__ == '__main__':
    fig_max_transferencia()
    print('listo')
