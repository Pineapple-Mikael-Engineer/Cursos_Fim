import numpy as np
import ocean_forest as of

def fig_fourier_armonicos():
    fig, ax = of.plt.subplots(figsize=(8.4, 4.0))
    fig.patch.set_facecolor(of.PANEL); of.style_axes(ax)
    t = np.linspace(0, 2*np.pi, 1000)
    sq = np.sign(np.sin(t))
    ax.plot(t, sq, '--', color=of.TEXT, lw=1.6, label='onda cuadrada', alpha=0.7)
    h1 = (4/np.pi)*np.sin(t); h3 = (4/np.pi)*np.sin(3*t)/3; h5 = (4/np.pi)*np.sin(5*t)/5
    ax.plot(t, h1, color=of.CURVE, lw=1.4, alpha=0.85, label=r'$1^{\mathrm{er}}$ armónico')
    ax.plot(t, h3, color=of.ACCENT, lw=1.3, alpha=0.8, label=r'$3^{\mathrm{er}}$ armónico')
    ax.plot(t, h5, color=of.BROWN, lw=1.2, alpha=0.75, label=r'$5^{\mathrm{o}}$ armónico')
    s = h1 + h3 + h5 + (4/np.pi)*np.sin(7*t)/7
    ax.plot(t, s, color=of.CURVE, lw=2.8, label='suma (1+3+5+7)')
    ax.axhline(0, color=of.GRID, lw=0.8)
    ax.set_xlim(0, 2*np.pi); ax.set_ylim(-1.6, 1.6); ax.set_xlabel(r'$\omega t$')
    ax.set_title('una onda periódica = suma de senoides (Fourier)', color=of.TEXT, fontsize=11.5)
    ax.legend(loc='upper right', fontsize=8.5, ncol=2, framealpha=0.92)
    fig.tight_layout(); of.save(fig, 'fourier_armonicos')

if __name__ == '__main__':
    fig_fourier_armonicos(); print('ok')
