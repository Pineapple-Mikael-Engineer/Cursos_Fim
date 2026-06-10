import numpy as np
import ocean_forest as of


def fig_rc_respuesta():
    fig, (a1, a2) = of.plt.subplots(2, 1, figsize=(6.4, 4.6), sharex=True)
    fig.patch.set_facecolor(of.PANEL)
    for ax in (a1, a2): of.style_axes(ax)
    t = np.linspace(0, 10, 600); tau = 2.0
    vc = 10*(1-np.exp(-t/tau)); ic = 5*np.exp(-t/tau)
    a1.plot(t, vc, color=of.CURVE, lw=2.6)
    a1.axhline(10, color=of.BROWN, lw=0.8, ls='--', alpha=0.6)
    a1.plot([tau], [10*(1-np.exp(-1))], 'o', color=of.ACCENT, ms=8)
    a1.text(tau+0.2, 5.4, r'$63\%$ en $t=\tau$', color=of.TEXT, fontsize=9)
    a1.set_ylabel(r'$v_C\ (\mathrm{V})$'); a1.set_ylim(0, 11)
    a1.set_title(r'Carga de un RC: $v_C=V_s(1-e^{-t/\tau})$,  $\tau=RC=2$ ms', color=of.TEXT, fontsize=11.5)
    a2.plot(t, ic, color=of.ACCENT, lw=2.6)
    a2.plot([tau], [5*np.exp(-1)], 'o', color=of.CURVE, ms=8)
    a2.set_ylabel(r'$i\ (\mathrm{mA})$'); a2.set_xlabel(r'$t\ (\mathrm{ms})$'); a2.set_ylim(0, 5.5)
    for ax in (a1, a2): ax.axvline(tau, color=of.GRID, lw=0.8, ls=':')
    fig.tight_layout(); of.save(fig, 'rc_respuesta')


def fig_rl_respuesta():
    fig, (a1, a2) = of.plt.subplots(2, 1, figsize=(6.4, 4.6), sharex=True)
    fig.patch.set_facecolor(of.PANEL)
    for ax in (a1, a2): of.style_axes(ax)
    t = np.linspace(0, 10, 600); tau = 2.0
    il = 2*(1-np.exp(-t/tau)); vl = 10*np.exp(-t/tau)
    a1.plot(t, il, color=of.CURVE, lw=2.6)
    a1.axhline(2, color=of.BROWN, lw=0.8, ls='--', alpha=0.6)
    a1.plot([tau], [2*(1-np.exp(-1))], 'o', color=of.ACCENT, ms=8)
    a1.text(tau+0.2, 1.05, r'$63\%$ en $t=\tau$', color=of.TEXT, fontsize=9)
    a1.set_ylabel(r'$i_L\ (\mathrm{A})$'); a1.set_ylim(0, 2.2)
    a1.set_title(r'Carga de un RL: $i_L=\dfrac{V_s}{R}(1-e^{-t/\tau})$,  $\tau=L/R=2$ ms', color=of.TEXT, fontsize=11.5)
    a2.plot(t, vl, color=of.ACCENT, lw=2.6)
    a2.plot([tau], [10*np.exp(-1)], 'o', color=of.CURVE, ms=8)
    a2.set_ylabel(r'$v_L\ (\mathrm{V})$'); a2.set_xlabel(r'$t\ (\mathrm{ms})$'); a2.set_ylim(0, 11)
    for ax in (a1, a2): ax.axvline(tau, color=of.GRID, lw=0.8, ls=':')
    fig.tight_layout(); of.save(fig, 'rl_respuesta')


def fig_constante_tiempo():
    fig, ax = of.new_fig(figsize=(6.6, 4.3)); of.style_axes(ax)
    t = np.linspace(0, 6, 600)
    y = 1-np.exp(-t)
    ax.plot(t, y, color=of.CURVE, lw=2.7, label=r'$1-e^{-t/\tau}$')
    # tangente en el origen: pendiente 1/tau, llega a 1 en t=tau
    ax.plot([0, 1], [0, 1], color=of.BROWN, lw=1.4, ls='--', label='tangente en el origen')
    ax.axhline(1, color=of.GRID, lw=0.8, ls=':')
    for k, lab in [(1, r'$63{,}2\%$'), (2, r'$86{,}5\%$'), (3, r'$95\%$'), (5, r'$99{,}3\%$')]:
        yk = 1-np.exp(-k)
        ax.plot([k], [yk], 'o', color=of.ACCENT, ms=6)
        ax.plot([k, k], [0, yk], color=of.GRID, lw=0.7, ls=':')
        ax.text(k, yk-0.08, lab, color=of.TEXT, fontsize=8.5, ha='center')
    ax.set_xticks(range(7)); ax.set_xticklabels(['0', r'$\tau$', r'$2\tau$', r'$3\tau$', r'$4\tau$', r'$5\tau$', r'$6\tau$'])
    ax.set_xlim(0, 6); ax.set_ylim(0, 1.12)
    of.labels(ax, r'tiempo (en unidades de $\tau$)', r'fracción del cambio total')
    of.title(ax, r'La constante de tiempo $\tau$: a los $5\tau$ el transitorio se ha extinguido')
    of.legend(ax, loc='center right')
    of.save(fig, 'constante_tiempo')


def fig_respuesta_completa():
    fig, ax = of.new_fig(figsize=(6.6, 4.3)); of.style_axes(ax)
    t = np.linspace(0, 10, 600); tau = 2.0; x0, xinf = 1.0, 5.0
    forzada = np.full_like(t, xinf)
    natural = (x0-xinf)*np.exp(-t/tau)
    completa = forzada + natural
    ax.plot(t, completa, color=of.CURVE, lw=2.8, label=r'completa $x(t)=x_\infty+(x_0-x_\infty)e^{-t/\tau}$')
    ax.plot(t, forzada, color=of.ACCENT, lw=2.0, ls='--', label=r'forzada $x_\infty$ (permanente)')
    ax.plot(t, natural, color=of.BROWN, lw=2.0, ls=':', label=r'natural $(x_0-x_\infty)e^{-t/\tau}$')
    ax.axhline(0, color=of.GRID, lw=0.7)
    ax.plot([0], [x0], 'o', color=of.CURVE, ms=8); ax.text(0.15, x0-0.5, r'$x_0$', color=of.TEXT, fontsize=10)
    ax.set_xlim(0, 10); ax.set_ylim(-4.5, 6)
    of.labels(ax, r'$t\ (\mathrm{ms})$', r'$x(t)$')
    of.title(ax, r'Respuesta completa = forzada + natural')
    of.legend(ax, loc='center right')
    of.save(fig, 'respuesta_completa')


if __name__ == '__main__':
    fig_rc_respuesta(); fig_rl_respuesta(); fig_constante_tiempo(); fig_respuesta_completa()
    print('listo')
