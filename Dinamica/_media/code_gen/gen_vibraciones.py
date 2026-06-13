import numpy as np
import ocean_forest as of

def fig_vibracion_amortiguada():
    fig, ax = of.plt.subplots(figsize=(8.4, 4.0))
    fig.patch.set_facecolor(of.PANEL); of.style_axes(ax)
    t = np.linspace(0, 14, 800); wn = 1.0
    # no amortiguada
    ax.plot(t, np.cos(wn*t), color=of.CURVE, lw=2.4, label=r'no amortiguada ($\zeta=0$)')
    # subamortiguada
    z=0.15; wd=wn*np.sqrt(1-z**2)
    x=np.exp(-z*wn*t)*(np.cos(wd*t)+(z*wn/wd)*np.sin(wd*t))
    ax.plot(t, x, color=of.ACCENT, lw=2.4, label=r'subamortiguada ($\zeta=0{,}15$)')
    ax.plot(t, np.exp(-z*wn*t), '--', color=of.ACCENT, lw=1.0, alpha=0.7)
    ax.plot(t, -np.exp(-z*wn*t), '--', color=of.ACCENT, lw=1.0, alpha=0.7)
    # critica
    xc=np.exp(-wn*t)*(1+wn*t)
    ax.plot(t, xc, color=of.BROWN, lw=2.2, label=r'crítica ($\zeta=1$)')
    # sobreamortiguada
    z2=2.0; s1=-z2*wn+wn*np.sqrt(z2**2-1); s2=-z2*wn-wn*np.sqrt(z2**2-1)
    A=s2/(s2-s1); B=-s1/(s2-s1)
    xo=A*np.exp(s1*t)+B*np.exp(s2*t)
    ax.plot(t, xo, color=of.GRID, lw=2.2, label=r'sobreamortiguada ($\zeta=2$)')
    ax.axhline(0, color=of.GRID, lw=0.8)
    ax.set_xlim(0,14); ax.set_ylim(-1.15,1.15)
    ax.set_xlabel(r'$\omega_n t$'); ax.set_ylabel(r'$x/x_0$')
    ax.set_title('vibración libre: regímenes de amortiguamiento', color=of.TEXT, fontsize=11.5)
    ax.legend(loc='upper right', fontsize=9, framealpha=0.92)
    fig.tight_layout(); of.save(fig, 'vibracion_amortiguada')

def fig_resonancia():
    fig, ax = of.plt.subplots(figsize=(8.0, 4.2))
    fig.patch.set_facecolor(of.PANEL); of.style_axes(ax)
    r = np.linspace(0, 2.6, 600)
    for z,c,lab in [(0.1,of.CURVE,'0{,}10'),(0.25,of.ACCENT,'0{,}25'),(0.5,of.BROWN,'0{,}50'),(1.0,of.GRID,'1{,}00')]:
        M=1/np.sqrt((1-r**2)**2+(2*z*r)**2)
        ax.plot(r, M, color=c, lw=2.4, label=fr'$\zeta={lab}$')
    ax.axvline(1, color=of.GRID, lw=0.9, ls=':')
    ax.set_xlim(0,2.6); ax.set_ylim(0,5.4)
    ax.set_xlabel(r'$r=\omega/\omega_n$'); ax.set_ylabel(r'factor de amplificación $M$')
    ax.set_title('resonancia: amplificación frente a la frecuencia', color=of.TEXT, fontsize=11.5)
    ax.legend(loc='upper right', fontsize=9.5, framealpha=0.92)
    fig.tight_layout(); of.save(fig, 'resonancia')

if __name__=='__main__':
    fig_vibracion_amortiguada(); fig_resonancia(); print('ok')
