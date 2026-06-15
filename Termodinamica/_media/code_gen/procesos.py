import numpy as np
import ocean_forest as of
of.setup()

g = 1.4                      # gamma = cp/cv
v0, P0, T0, s0 = 1.0, 3.0, 1.0, 1.0
cv, cp = 1.0, g              # unidades arbitrarias para forma

# ---------- 1) Comparativa P-v ----------
fig, ax = of.new_fig(figsize=(6.2,4.6)); of.style_axes(ax)
v = np.linspace(0.62, 1.95, 300)
ax.axhline(P0, color=of.BROWN, lw=2.2, label='isobárico  $n=0$')                     # isobarico
ax.plot([v0,v0],[1.2,5.4], color='#6a8858', lw=2.2, label='isocórico  $n\\to\\infty$') # isocorico
ax.plot(v, P0*v0/v, color=of.CURVE, lw=2.4, label='isotérmico  $n=1$  ($Pv$=cte)')    # isotermico
ax.plot(v, P0*(v0/v)**g, color=of.ACCENT, lw=2.4, label='adiabático  $n=\\gamma$  ($Pv^\\gamma$=cte)') # adiabatico
ax.plot(v0,P0,'o',color=of.TEXT,ms=7,zorder=6); ax.annotate('estado 1',(v0,P0),(v0+0.05,P0+0.45),color=of.TEXT,fontsize=10)
of.labels(ax,x='volumen específico  $v$',y='presión  $P$'); of.title(ax,'Procesos en el plano $P$–$v$')
ax.set_xlim(0.55,2.0); ax.set_ylim(1.0,5.6); of.legend(ax,loc='upper right',fontsize=8.5)
of.save(fig,'procesos_pv_comparacion')

# ---------- 2) Comparativa T-s ----------
fig, ax = of.new_fig(figsize=(6.2,4.6)); of.style_axes(ax)
s = np.linspace(0.62, 1.95, 300)
ax.axvline(s0, color=of.ACCENT, lw=2.2, label='adiabático rev.  ($s$=cte)')           # adiabatico isentropico
ax.plot([0.7,1.9],[T0,T0], color=of.CURVE, lw=2.2, label='isotérmico  ($T$=cte)')      # isotermico
ax.plot(s, T0*np.exp((s-s0)/cv), color='#6a8858', lw=2.4, label='isocórico  ($T=T_0e^{\\Delta s/c_v}$)')  # isocorico
ax.plot(s, T0*np.exp((s-s0)/cp), color=of.BROWN, lw=2.4, label='isobárico  ($T=T_0e^{\\Delta s/c_p}$)')   # isobarico
ax.plot(s0,T0,'o',color=of.TEXT,ms=7,zorder=6); ax.annotate('estado 1',(s0,T0),(s0+0.04,T0+0.18),color=of.TEXT,fontsize=10)
of.labels(ax,x='entropía específica  $s$',y='temperatura  $T$'); of.title(ax,'Procesos en el plano $T$–$s$')
ax.set_xlim(0.6,1.95); ax.set_ylim(0.55,2.4); of.legend(ax,loc='upper left',fontsize=8.5)
of.save(fig,'procesos_ts_comparacion')

# ---------- 3) Familia politropica P-v ----------
fig, ax = of.new_fig(figsize=(6.0,4.6)); of.style_axes(ax)
v = np.linspace(0.62,1.95,300)
for n,c,lab in [(0,of.BROWN,'$n=0$ (isobárico)'),(1,of.CURVE,'$n=1$ (isotérmico)'),
                (g,of.ACCENT,'$n=\\gamma=1{,}4$ (adiabático)'),(2.2,'#9a7030','$n=2{,}2$')]:
    ax.plot(v, P0*(v0/v)**n, lw=2.3, color=c, label=lab)
ax.plot([v0,v0],[1.2,5.4], color='#6a8858', lw=2.2, label='$n\\to\\infty$ (isocórico)')
ax.plot(v0,P0,'o',color=of.TEXT,ms=7,zorder=6)
of.labels(ax,x='volumen específico  $v$',y='presión  $P$'); of.title(ax,'Familia politrópica  $Pv^n=$ cte')
ax.set_xlim(0.55,2.0); ax.set_ylim(1.0,5.6); of.legend(ax,loc='upper right',fontsize=8.5)
of.save(fig,'politropico_familia')

# ---------- 4-7) Por proceso: P-v (area=W) | T-s (area=Q) ----------
def dos_paneles(nombre, titulo, pv_path, ts_path, shade_W=True, shade_Q=True, nota=''):
    fig,(a1,a2)=of.new_fig(ncols=2,figsize=(8.6,4.0)); of.style_axes(a1); of.style_axes(a2)
    vv,PP=pv_path; ss,TT=ts_path
    a1.plot(vv,PP,color=of.CURVE,lw=2.6)
    if shade_W: a1.fill_between(vv,PP,0,color=of.CURVE,alpha=0.16)
    a1.plot([vv[0],vv[-1]],[PP[0],PP[-1]],'o',color=of.TEXT,ms=6,zorder=6)
    a1.annotate('1',(vv[0],PP[0]),(vv[0],PP[0]+0.001),color=of.TEXT,fontsize=11,weight='bold')
    a1.annotate('2',(vv[-1],PP[-1]),color=of.TEXT,fontsize=11,weight='bold')
    of.labels(a1,x='$v$',y='$P$'); of.title(a1,'$P$–$v$'+('   (área $=W$)' if shade_W else '   ($W=0$)'))
    a2.plot(ss,TT,color=of.ACCENT,lw=2.6)
    if shade_Q: a2.fill_between(ss,TT,0,color=of.ACCENT,alpha=0.16)
    a2.plot([ss[0],ss[-1]],[TT[0],TT[-1]],'o',color=of.TEXT,ms=6,zorder=6)
    of.labels(a2,x='$s$',y='$T$'); of.title(a2,'$T$–$s$'+('   (área $=Q$)' if shade_Q else '   ($Q=0$)'))
    fig.suptitle(titulo,color=of.TEXT,fontsize=12)
    fig.tight_layout(rect=[0,0,1,0.95]); of.save(fig,nombre)

vexp=np.linspace(v0,1.8,200); sexp=np.linspace(s0,1.7,200)
# Isotermico: Pv=cte ; T-s horizontal (T cte)
dos_paneles('isotermico_pv_ts','Proceso isotérmico  ($T$=cte,  $W=Q$)',
            (vexp, P0*v0/vexp), (sexp, np.full_like(sexp,T0)))
# Isobarico: P cte ; T-s curva isobarica
dos_paneles('isobarico_pv_ts','Proceso isobárico  ($P$=cte,  $Q_p=\\Delta h$)',
            (vexp, np.full_like(vexp,P0)), (sexp, T0*np.exp((sexp-s0)/cp)))
# Isocorico: v cte (W=0) ; T-s curva isocorica
dos_paneles('isocorico_pv_ts','Proceso isocórico  ($v$=cte,  $W=0$,  $Q_v=\\Delta u$)',
            (np.full(200,v0), np.linspace(P0,1.7*P0,200)), (sexp, T0*np.exp((sexp-s0)/cv)),
            shade_W=False)
# Adiabatico: Pv^g=cte ; T-s vertical (s cte, Q=0)
dos_paneles('adiabatico_pv_ts','Proceso adiabático reversible  ($Q=0$,  $s$=cte)',
            (vexp, P0*(v0/vexp)**g), (np.full(200,s0), np.linspace(T0,0.72*T0,200)),
            shade_Q=False)
print("OK figuras procesos")
