import numpy as np, ocean_forest as of
def fig_centro_masa_proyectil():
    fig, ax = of.plt.subplots(figsize=(7.6,3.6)); fig.patch.set_facecolor(of.PANEL); of.style_axes(ax)
    x=np.linspace(0,10,200); y=x*1.0-0.1*x**2  # parabola
    ax.plot(x,y,'--',color=of.TEXT,lw=1.6,alpha=0.6,label='trayectoria del CM')
    # explosion point
    xe=5.0; ye=xe-0.1*xe**2
    ax.plot(xe,ye,'o',color=of.BROWN,ms=8)
    ax.annotate('explosión',(xe,ye),(xe-1.6,ye+0.9),color=of.BROWN,fontsize=9,
                arrowprops=dict(arrowstyle='->',color=of.BROWN))
    # fragments after explosion (diverging)
    for dvx,dvy,c in [(1.2,1.0,of.CURVE),(0.4,-0.6,of.ACCENT),(-0.8,0.4,of.GRID)]:
        t=np.linspace(0,3.2,60); fx=xe+(1.0+dvx)*t; fy=ye+(0.0+dvy)*t-0.5*0.2*(10)*0 - 0.1* (xe+(1+dvx)*t)**2 + 0.1*xe**2 + dvy*t
        # simpler: each fragment continues under gravity from explosion
        fx=xe+(1.0+dvx)*t; fy=ye+( (1-0.2*xe)+dvy)*t-0.1*( (1+dvx)*t)**2*0 - 0.1*t**2*1.0
        ax.plot(fx,fy,color=c,lw=1.6,alpha=0.85)
    # CM continues on same parabola (highlight)
    ax.plot(x[x>=xe],y[x>=xe],color=of.TEXT,lw=2.4)
    ax.axhline(0,color=of.GRID,lw=0.9); ax.set_xlim(0,10.5); ax.set_ylim(0,3.2)
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.set_title('el centro de masa sigue su parábola pese a la explosión',color=of.TEXT,fontsize=10.5)
    ax.legend(loc='upper right',fontsize=9,framealpha=0.9)
    fig.tight_layout(); of.save(fig,'centro_masa_proyectil')
if __name__=='__main__': fig_centro_masa_proyectil(); print('ok')
