import numpy as np
import ocean_forest as of


def fig_capacitor_iv():
    fig, (a1, a2) = of.plt.subplots(2, 1, figsize=(6.4, 4.6), sharex=True)
    fig.patch.set_facecolor(of.PANEL)
    for ax in (a1, a2): of.style_axes(ax)
    t = np.linspace(-0.5, 3, 700)
    v = np.clip((t)*10, 0, 10)           # rampa 0->10 V en 1 ms, luego constante
    v[t < 0] = 0
    i = np.where((t >= 0) & (t <= 1), 100.0, 0.0)   # i = C dv/dt = 100 mA durante la rampa
    a1.plot(t, v, color=of.CURVE, lw=2.6)
    a1.set_ylabel(r'$v_C\ (\mathrm{V})$'); a1.set_ylim(-1, 12)
    a1.set_title(r'Condensador: $i=C\,dv/dt$  ($C=10\ \mu$F)', color=of.TEXT, fontsize=12)
    a2.plot(t, i, color=of.ACCENT, lw=2.6)
    a2.set_ylabel(r'$i_C\ (\mathrm{mA})$'); a2.set_xlabel(r'$t\ (\mathrm{ms})$'); a2.set_ylim(-20, 130)
    a2.annotate('la corriente sigue\nla pendiente de $v$', xy=(0.5, 100), xytext=(1.4, 70),
                color=of.TEXT, fontsize=9, arrowprops=dict(arrowstyle='->', color=of.BROWN))
    fig.tight_layout()
    of.save(fig, 'capacitor_iv')


def fig_inductor_vi():
    fig, (a1, a2) = of.plt.subplots(2, 1, figsize=(6.4, 4.6), sharex=True)
    fig.patch.set_facecolor(of.PANEL)
    for ax in (a1, a2): of.style_axes(ax)
    t = np.linspace(-0.5, 3, 700)
    i = np.clip(t*5, 0, 5)
    i[t < 0] = 0
    v = np.where((t >= 0) & (t <= 1), 10.0, 0.0)    # v = L di/dt = 10 V durante la rampa
    a1.plot(t, i, color=of.CURVE, lw=2.6)
    a1.set_ylabel(r'$i_L\ (\mathrm{A})$'); a1.set_ylim(-0.5, 6)
    a1.set_title(r'Inductor: $v=L\,di/dt$  ($L=2\ $mH)', color=of.TEXT, fontsize=12)
    a2.plot(t, v, color=of.ACCENT, lw=2.6)
    a2.set_ylabel(r'$v_L\ (\mathrm{V})$'); a2.set_xlabel(r'$t\ (\mathrm{ms})$'); a2.set_ylim(-2, 13)
    a2.annotate('la tensión sigue\nla pendiente de $i$', xy=(0.5, 10), xytext=(1.4, 7),
                color=of.TEXT, fontsize=9, arrowprops=dict(arrowstyle='->', color=of.BROWN))
    fig.tight_layout()
    of.save(fig, 'inductor_vi')


def fig_continuidad_vc():
    fig, ax = of.new_fig(figsize=(6.4, 4.0)); of.style_axes(ax)
    t = np.linspace(-1, 5, 700)
    V0, Vf, tau = 2.0, 8.0, 1.0
    v = np.where(t < 0, V0, Vf + (V0-Vf)*np.exp(-np.clip(t, 0, None)/tau))
    ax.plot(t, v, color=of.CURVE, lw=2.7, label=r'$v_C(t)$ continua')
    ax.plot([0], [V0], 'o', color=of.ACCENT, ms=9, zorder=5)
    # salto prohibido (a trazos)
    ax.plot([0, 0], [V0, Vf], color=of.BROWN, lw=1.6, ls=':', alpha=0.8)
    ax.annotate('prohibido:\nsalto de $v_C$', xy=(0, 5), xytext=(0.6, 3.0),
                color=of.TEXT, fontsize=9, arrowprops=dict(arrowstyle='->', color=of.BROWN))
    ax.axvline(0, color=of.GRID, lw=0.8, ls='--')
    ax.text(-0.85, V0+0.3, r'$v_C(0^-)$', color=of.TEXT, fontsize=9)
    ax.set_xlim(-1, 5); ax.set_ylim(0, 9)
    of.labels(ax, r'$t$ (conmutación en $t=0$)', r'$v_C\ (\mathrm{V})$')
    of.title(ax, r'La tensión del condensador no salta: $v_C(0^+)=v_C(0^-)$')
    of.legend(ax, loc='lower right')
    of.save(fig, 'continuidad_vc')


if __name__ == '__main__':
    fig_capacitor_iv(); fig_inductor_vi(); fig_continuidad_vc()
    print('listo')
