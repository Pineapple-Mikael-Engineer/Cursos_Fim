import numpy as np, ocean_forest as of
def fig_centro_masa_proyectil():
    fig, ax = of.plt.subplots(figsize=(7.8,3.7)); fig.patch.set_facecolor(of.PANEL); of.style_axes(ax)
    t=np.linspace(0,10,300); y=t-0.1*t**2
    ax.plot(t,y,'--',color=of.TEXT,lw=1.5,alpha=0.55,label='trayectoria del CM')
    xe=5.0; ye=xe-0.1*xe**2  # apex (vx=1, vy=0)
    # fragmentos: salen del punto de explosion, bajo gravedad g=0.2
    frags=[(0.6,0.7,of.CURVE),(0.0,-0.5,of.ACCENT),(-0.6,0.35,of.BROWN),(0.35,-0.2,of.GRID)]
    for dvx,dvy,c in frags:
        tau=np.linspace(0,3.4,80); fx=xe+(1+dvx)*tau; fy=ye+dvy*tau-0.1*tau**2
        mask=fy>=0
        ax.plot(fx[mask],fy[mask],color=c,lw=1.5,alpha=0.85)
    # CM continua (negrita sobre la parabola)
    tc=t[t>=xe]; ax.plot(tc,tc-0.1*tc**2,color=of.TEXT,lw=2.6)
    ax.plot(xe,ye,'o',color=of.BROWN,ms=8,zorder=5)
    ax.annotate('explosión',(xe,ye),(xe+0.3,ye-0.95),color=of.BROWN,fontsize=9.5,
                arrowprops=dict(arrowstyle='->',color=of.BROWN,lw=1.1))
    ax.axhline(0,color=of.GRID,lw=0.9); ax.set_xlim(0,10.4); ax.set_ylim(0,3.6)
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.set_title('el CM sigue su parábola pese a la explosión',color=of.TEXT,fontsize=11,pad=10)
    ax.legend(loc='upper left',fontsize=9,framealpha=0.9)
    fig.tight_layout(); of.save(fig,'centro_masa_proyectil')
if __name__=='__main__': fig_centro_masa_proyectil(); print('ok')
