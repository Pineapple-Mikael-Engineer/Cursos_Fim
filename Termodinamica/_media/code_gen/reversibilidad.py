import numpy as np
import ocean_forest as of
of.setup()
fig,(a1,a2)=of.new_fig(ncols=2,figsize=(8.6,4.0)); of.style_axes(a1); of.style_axes(a2)
v0,P0=1.0,3.0; v2=2.0; P2=P0*v0/v2
v=np.linspace(v0,v2,200)
# Reversible: cuasiestatico, P=P0 v0/v, area grande
a1.plot(v,P0*v0/v,color=of.CURVE,lw=2.6)
a1.fill_between(v,P0*v0/v,0,color=of.CURVE,alpha=0.18)
a1.plot([v0,v2],[P0,P2],'o',color=of.TEXT,ms=6,zorder=6)
a1.annotate('1',(v0,P0),(v0-0.02,P0+0.18),color=of.TEXT,fontsize=11,weight='bold')
a1.annotate('2',(v2,P2),(v2-0.06,P2+0.18),color=of.TEXT,fontsize=11,weight='bold')
of.labels(a1,x='$v$',y='$P$'); of.title(a1,'Reversible  ($W_{rev}=\\int P\\,dv$)')
a1.set_ylim(0,3.4); a1.set_xlim(0.9,2.15)
# Irreversible: contra P_ext = P2 constante, area = P2(v2-v0) rectangulo
a2.plot([v0,v0,v2],[P0,P2,P2],color=of.ACCENT,lw=2.0,ls='--')
a2.fill_between([v0,v2],[P2,P2],0,color=of.ACCENT,alpha=0.18)
a2.plot([v0,v2],[P0,P2],'o',color=of.TEXT,ms=6,zorder=6)
a2.annotate('1',(v0,P0),(v0-0.02,P0+0.18),color=of.TEXT,fontsize=11,weight='bold')
a2.annotate('2',(v2,P2),(v2-0.06,P2+0.18),color=of.TEXT,fontsize=11,weight='bold')
a2.annotate('$P_{ext}=P_2$',(1.5,P2),(1.4,P2-0.6),color=of.TEXT,fontsize=9)
of.labels(a2,x='$v$',y='$P$'); of.title(a2,'Irreversible  ($W=P_{ext}\\Delta v<W_{rev}$)')
a2.set_ylim(0,3.4); a2.set_xlim(0.9,2.15)
fig.suptitle('Expansión: el trabajo reversible es el máximo',color=of.TEXT,fontsize=12)
fig.tight_layout(rect=[0,0,1,0.95]); of.save(fig,'reversibilidad')
print("ok")
