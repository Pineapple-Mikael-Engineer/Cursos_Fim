import numpy as np
import ocean_forest as of


def fig_onda_sinusoidal():
    fig, ax = of.new_fig(figsize=(7.0, 4.2)); of.style_axes(ax)
    t = np.linspace(-0.6, 4*np.pi, 900); Vm = 10; phi = np.pi/6
    v = Vm*np.sin(t+phi)
    ax.plot(t, v, color=of.CURVE, lw=2.7)
    ax.axhline(0, color=of.GRID, lw=0.9)
    ax.axhline(Vm, color=of.BROWN, lw=0.8, ls='--', alpha=0.6)
    peak = np.pi/2 - phi
    ax.annotate('', xy=(peak, Vm), xytext=(peak, 0), arrowprops=dict(arrowstyle='<->', color=of.ACCENT, lw=1.8))
    ax.text(peak+0.12, Vm*0.5, r'$V_m$', color=of.TEXT, fontsize=12)
    ax.annotate('', xy=(peak, Vm*1.16), xytext=(peak+2*np.pi, Vm*1.16), arrowprops=dict(arrowstyle='<->', color=of.BROWN, lw=1.6))
    ax.text(peak+np.pi-0.2, Vm*1.22, r'$T=2\pi/\omega$', color=of.TEXT, fontsize=10.5)
    ax.plot([-phi], [0], 'o', color=of.ACCENT, ms=7)
    ax.text(-phi-0.1, -Vm*0.28, r'$\varphi$', color=of.TEXT, fontsize=11, ha='right')
    ax.set_xlim(-0.6, 4*np.pi); ax.set_ylim(-Vm*1.25, Vm*1.4)
    of.labels(ax, r'$\omega t$ (rad)', r'$v(t)$')
    of.title(ax, r'Onda sinusoidal  $v(t)=V_m\,\operatorname{sen}(\omega t+\varphi)$')
    of.save(fig, 'onda_sinusoidal')


def fig_valor_medio():
    fig, (a1, a2) = of.plt.subplots(2, 1, figsize=(6.8, 4.6), sharex=True)
    fig.patch.set_facecolor(of.PANEL)
    for ax in (a1, a2): of.style_axes(ax)
    t = np.linspace(0, 2*np.pi, 600); s = np.sin(t)
    a1.plot(t, s, color=of.CURVE, lw=2.5)
    a1.fill_between(t, s, where=(s >= 0), color=of.CURVE, alpha=0.18)
    a1.fill_between(t, s, where=(s < 0), color=of.BROWN, alpha=0.18)
    a1.axhline(0, color=of.ACCENT, lw=2.0)
    a1.set_ylabel(r'$v$'); a1.set_ylim(-1.3, 1.3)
    a1.set_title(r'Onda completa: valor medio $=0$ (las áreas $+$ y $-$ se cancelan)', color=of.TEXT, fontsize=10.5)
    a2.plot(t, np.abs(s), color=of.CURVE, lw=2.5)
    a2.fill_between(t, np.abs(s), color=of.CURVE, alpha=0.15)
    a2.axhline(2/np.pi, color=of.ACCENT, lw=2.0)
    a2.text(np.pi, 2/np.pi+0.08, r'$V_{med}=\dfrac{2V_m}{\pi}\approx0{,}637\,V_m$', color=of.TEXT, fontsize=10, ha='center')
    a2.set_ylabel(r'$|v|$'); a2.set_xlabel(r'$\omega t$ (rad)'); a2.set_ylim(0, 1.3)
    a2.set_title(r'Rectificada de onda completa: valor medio $=2V_m/\pi$', color=of.TEXT, fontsize=10.5)
    fig.tight_layout(); of.save(fig, 'valor_medio')


def fig_valor_eficaz():
    fig, ax = of.new_fig(figsize=(7.0, 4.2)); of.style_axes(ax)
    t = np.linspace(0, 2*np.pi, 700); Vm = 1.0
    v = Vm*np.sin(t); v2 = v**2
    ax.plot(t, v, color=of.CURVE, lw=2.5, label=r'$v=V_m\operatorname{sen}\omega t$')
    ax.plot(t, v2, color=of.BROWN, lw=2.0, ls='-.', label=r'$v^2$')
    ax.fill_between(t, v2, color=of.BROWN, alpha=0.12)
    Vrms = 1/np.sqrt(2)
    ax.axhline(Vrms, color=of.ACCENT, lw=2.0)
    ax.text(0.15, Vrms+0.05, r'$V_{ef}=\dfrac{V_m}{\sqrt{2}}\approx0{,}707\,V_m$', color=of.TEXT, fontsize=10.5)
    ax.axhline(0.5, color=of.ACCENT, lw=1.2, ls=':')
    ax.text(4.3, 0.53, r'media de $v^2=V_{ef}^2=\frac{1}{2} V_m^2$', color=of.TEXT, fontsize=9.5)
    ax.axhline(0, color=of.GRID, lw=0.8)
    ax.set_xlim(0, 2*np.pi); ax.set_ylim(-1.15, 1.25)
    of.labels(ax, r'$\omega t$ (rad)', '')
    of.title(ax, r'Valor eficaz (RMS): la DC que calienta igual')
    of.legend(ax, loc='lower right')
    of.save(fig, 'valor_eficaz')


def fig_generacion_alterna():
    fig, (a1, a2) = of.plt.subplots(1, 2, figsize=(8.4, 3.8), gridspec_kw={'width_ratios': [1, 1.7]})
    fig.patch.set_facecolor(of.PANEL)
    for ax in (a1, a2): of.style_axes(ax)
    th = np.deg2rad(55)
    ang = np.linspace(0, 2*np.pi, 200)
    a1.plot(np.cos(ang), np.sin(ang), color=of.GRID, lw=1.4)
    a1.annotate('', xy=(np.cos(th), np.sin(th)), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=of.CURVE, lw=2.4))
    a1.plot([np.cos(th), 1.35], [np.sin(th), np.sin(th)], color=of.ACCENT, lw=1.2, ls='--')
    a1.plot([0, np.cos(th)], [0, 0], color=of.GRID, lw=1.0)
    a1.annotate(r'$\omega t$', xy=(0.42, 0.16), color=of.TEXT, fontsize=11)
    a1.set_xlim(-1.3, 1.5); a1.set_ylim(-1.3, 1.3); a1.set_aspect('equal')
    a1.set_title('rotación uniforme', color=of.TEXT, fontsize=11)
    a1.axhline(0, color=of.GRID, lw=0.7); a1.axvline(0, color=of.GRID, lw=0.7)
    t = np.linspace(0, 2*np.pi, 400)
    a2.plot(t, np.sin(t), color=of.CURVE, lw=2.6)
    a2.plot([th], [np.sin(th)], 'o', color=of.ACCENT, ms=8)
    a2.plot([0, th], [np.sin(th), np.sin(th)], color=of.ACCENT, lw=1.2, ls='--')
    a2.axhline(0, color=of.GRID, lw=0.8)
    a2.set_xlim(0, 2*np.pi); a2.set_ylim(-1.2, 1.2)
    a2.set_title(r'$e=E_m\operatorname{sen}\omega t$ (proyección)', color=of.TEXT, fontsize=11)
    a2.set_xlabel(r'$\omega t$', fontsize=10)
    fig.tight_layout(); of.save(fig, 'generacion_alterna')


if __name__ == '__main__':
    fig_onda_sinusoidal(); fig_valor_medio(); fig_valor_eficaz(); fig_generacion_alterna()
    print('listo')
