"""Diagramas de ciclos de potencia y refrigeración. Estilo Ocean Forest."""
import numpy as np
import ocean_forest as of
of.setup()

G = 1.4


def isentropic_pv(v_a, v_b, P_a, n=60):
    v = np.linspace(v_a, v_b, n)
    return v, P_a * (v_a / v) ** G


def ts_dome(n=200):
    t = np.linspace(0.999, 0.52, n)
    sf = 1 - 0.95 * (1 - t)
    sg = 1 + 1.55 * (1 - t) ** 0.5
    return sf, sg, t


def ph_dome(n=200):
    p = np.linspace(0.999, 0.28, n)
    hf = 1 - 0.85 * (1 - p) ** 0.55
    hg = 1 + 0.95 * (1 - p) ** 0.5
    return hf, hg, p


def mark(ax, pts, dxy=None):
    dxy = dxy or [(6, 6)] * len(pts)
    for k, (x, y) in enumerate(pts):
        ax.plot(x, y, 'o', color=of.TEXT, ms=6, zorder=8)
        ax.annotate(str(k + 1), (x, y), dxy[k], textcoords='offset points',
                    color=of.TEXT, fontsize=10, weight='bold')


# ============ OTTO (P-v) ============
def otto_pv(ax):
    r = 8.0
    v1, P1 = 1.0, 1.0
    v2 = v1 / r
    P2 = P1 * r ** G
    P3 = 2.6 * P2
    P4 = P3 * (v2 / v1) ** G
    va, Pa = isentropic_pv(v1, v2, P1); ax.plot(va, Pa, color=of.CURVE, lw=2.4)
    ax.plot([v2, v2], [P2, P3], color=of.ACCENT, lw=2.4)              # 2-3 isocórico
    vc, Pc = isentropic_pv(v2, v1, P3); ax.plot(vc, Pc, color=of.CURVE, lw=2.4)
    ax.plot([v1, v1], [P4, P1], color=of.BROWN, lw=2.4)              # 4-1 isocórico
    mark(ax, [(v1, P1), (v2, P2), (v2, P3), (v1, P4)],
         [(6, -12), (-14, -2), (-14, 2), (8, 4)])
    ax.annotate('$q_{in}$ ($v$=cte)', (v2, (P2 + P3) / 2), (v2 + 0.08, (P2 + P3) / 2),
                color=of.ACCENT, fontsize=8.5)
    ax.annotate('$q_{out}$', (v1, (P1 + P4) / 2), (v1 - 0.30, (P1 + P4) / 2),
                color=of.BROWN, fontsize=8.5)
    of.labels(ax, x=r'$v$', y=r'$P$'); of.title(ax, r'Otto  ($r=8$)')
    ax.set_xlim(0, 1.15); ax.set_ylim(0, P3 * 1.1)


# ============ DIESEL (P-v) ============
def diesel_pv(ax):
    r, rc = 18.0, 2.0
    v1, P1 = 1.0, 1.0
    v2 = v1 / r
    P2 = P1 * r ** G
    v3 = rc * v2
    P3 = P2
    P4 = P3 * (v3 / v1) ** G
    va, Pa = isentropic_pv(v1, v2, P1); ax.plot(va, Pa, color=of.CURVE, lw=2.4)
    ax.plot([v2, v3], [P2, P3], color=of.ACCENT, lw=2.4)             # 2-3 isobárico
    vc, Pc = isentropic_pv(v3, v1, P3); ax.plot(vc, Pc, color=of.CURVE, lw=2.4)
    ax.plot([v1, v1], [P4, P1], color=of.BROWN, lw=2.4)             # 4-1 isocórico
    mark(ax, [(v1, P1), (v2, P2), (v3, P3), (v1, P4)],
         [(6, -12), (-6, 6), (8, 4), (8, 4)])
    ax.annotate('$q_{in}$ ($P$=cte)', (v3, P3), (v3 + 0.06, P3 * 0.97),
                color=of.ACCENT, fontsize=8.5)
    ax.annotate('$q_{out}$', (v1, (P1 + P4) / 2), (v1 - 0.30, (P1 + P4) / 2),
                color=of.BROWN, fontsize=8.5)
    of.labels(ax, x=r'$v$', y=r'$P$'); of.title(ax, r'Diesel  ($r=18,\ r_c=2$)')
    ax.set_xlim(0, 1.15); ax.set_ylim(0, P2 * 1.1)


for nombre, fn, tit in [('otto_diagrama_Pv', otto_pv, 'Ciclo Otto'),
                        ('diesel_diagrama_Pv', diesel_pv, 'Ciclo Diesel')]:
    fig, ax = of.new_fig(figsize=(5.6, 4.4)); of.style_axes(ax); fn(ax)
    of.save(fig, nombre)

# CCI combinado
fig, (a1, a2) = of.new_fig(ncols=2, figsize=(9.4, 4.2))
of.style_axes(a1); of.style_axes(a2); otto_pv(a1); diesel_pv(a2)
fig.suptitle('Ciclos de combustión interna: Otto vs Diesel', color=of.TEXT, fontsize=12)
fig.tight_layout(rect=[0, 0, 1, 0.95]); of.save(fig, 'CCI_PV_otto_diesel')

# ============ BRAYTON (T-s) ============
fig, ax = of.new_fig(figsize=(6.0, 4.5)); of.style_axes(ax)
s23 = np.linspace(0, 0.693, 60)
ax.plot([0, 0], [1, 2], color=of.CURVE, lw=2.4)                      # 1-2 compresor
ax.plot(s23, 2 * np.exp(s23), color=of.ACCENT, lw=2.4)              # 2-3 isóbara PH
ax.plot([0.693, 0.693], [4, 2], color=of.CURVE, lw=2.4)            # 3-4 turbina
ax.plot(s23, np.exp(s23), color=of.BROWN, lw=2.4)                  # 4-1 isóbara PL
mark(ax, [(0, 1), (0, 2), (0.693, 4), (0.693, 2)],
     [(-14, -2), (-14, 2), (6, 4), (8, -2)])
ax.annotate('$P_H$', (0.35, 2 * np.exp(0.35)), color=of.ACCENT, fontsize=9)
ax.annotate('$P_L$', (0.5, np.exp(0.5)), (0.5, np.exp(0.5) - 0.45), color=of.BROWN, fontsize=9)
of.labels(ax, x=r'entropía  $s$', y=r'temperatura  $T$')
of.title(ax, r'Ciclo Brayton ideal en $T$–$s$')
ax.set_xlim(-0.1, 0.85); ax.set_ylim(0.6, 4.5); of.save(fig, 'brayton_diagrama_Ts')

# ============ RANKINE (T-s) con cúpula ============
SF, SG, TT = ts_dome()
fig, ax = of.new_fig(figsize=(6.2, 4.6)); of.style_axes(ax)
ax.plot(SF, TT, color=of.CURVE, lw=2.2); ax.plot(SG, TT, color=of.CURVE, lw=2.2)
ax.fill_betweenx(TT, SF, SG, color=of.CURVE, alpha=0.08)
Tcond = 0.56
ic = int(np.argmin(np.abs(TT - Tcond)))
sf1, sg1 = SF[ic], SG[ic]
# 1: líq sat condensador; 2: tras bomba (s≈cte, T sube poco); 3: vapor sobrecalentado; 4: salida turbina
s1, T1 = sf1, Tcond
s2, T2 = sf1, Tcond + 0.02
T3, s3 = 1.15, 1.9
T4, s4 = Tcond, s3
ax.plot([s1, s2], [T1, T2], color=of.ACCENT, lw=2.4)                       # bomba
# caldera 2-3: calentar líquido (rama líq) -> vaporizar (horizontal) -> sobrecalentar
ih = int(np.argmin(np.abs(TT - 0.92)))                                     # T_sat a P_H
sliq, Tliq = SF[ih:ic + 1][::-1], TT[ih:ic + 1][::-1]
ax.plot(np.r_[sliq, [SF[ih], SG[ih], s3]],
        np.r_[Tliq, [TT[ih], TT[ih], T3]], color=of.BROWN, lw=2.4)
ax.plot([s3, s4], [T3, T4], color=of.CURVE, lw=2.4)                        # turbina
ax.plot([s4, s1], [T4, T1], color='#6a8858', lw=2.4)                       # condensador
mark(ax, [(s1, T1), (s2, T2 + 0.06), (s3, T3), (s4, T4)],
     [(-14, -2), (-16, 0), (8, 2), (8, -2)])
ax.annotate('caldera', (0.5, 1.0), color=of.BROWN, fontsize=8.5, rotation=30)
ax.annotate('turbina', (s3 + 0.02, 0.9), color=of.CURVE, fontsize=8.5)
ax.annotate('condensador', ((s1 + s4) / 2, T1 - 0.06), color='#6a8858', fontsize=8.5, ha='center')
of.labels(ax, x=r'entropía  $s$', y=r'temperatura  $T$')
of.title(ax, r'Ciclo Rankine en $T$–$s$')
ax.set_xlim(0.3, 2.4); ax.set_ylim(0.45, 1.3); of.save(fig, 'rankine_diagrama_Ts')

# ============ RANKINE (P-h) con cúpula ============
HF, HG, PP = ph_dome()
fig, ax = of.new_fig(figsize=(6.2, 4.6)); of.style_axes(ax)
ax.plot(HF, PP, color=of.CURVE, lw=2.2); ax.plot(HG, PP, color=of.CURVE, lw=2.2)
ax.fill_betweenx(PP, HF, HG, color=of.CURVE, alpha=0.08)
PH, PL = 0.9, 0.33
ih = int(np.argmin(np.abs(PP - PH))); il = int(np.argmin(np.abs(PP - PL)))
h1, h2, h3, h4 = HF[il], HF[ih], 1.9, 1.55
ax.plot([h1, h2], [PL, PH], color=of.ACCENT, lw=2.4)               # bomba (P sube, h≈cte)
ax.plot([h2, h3], [PH, PH], color=of.BROWN, lw=2.4)               # caldera (P=cte, h sube)
ax.plot([h3, h4], [PH, PL], color=of.CURVE, lw=2.4)               # turbina
ax.plot([h4, h1], [PL, PL], color='#6a8858', lw=2.4)             # condensador
mark(ax, [(h1, PL), (h2, PH), (h3, PH), (h4, PL)],
     [(-12, -10), (-10, 6), (8, 6), (8, -10)])
ax.set_yscale('log')
of.labels(ax, x=r'entalpía  $h$', y=r'presión  $P$ (log)')
of.title(ax, r'Ciclo Rankine en $P$–$h$')
ax.set_xlim(0.0, 2.2); ax.set_ylim(0.2, 1.3); of.save(fig, 'rankine_diagrama_Ph')

# ============ VCR (P-h) refrigeración ============
fig, ax = of.new_fig(figsize=(6.2, 4.6)); of.style_axes(ax)
ax.plot(HF, PP, color=of.CURVE, lw=2.2); ax.plot(HG, PP, color=of.CURVE, lw=2.2)
ax.fill_betweenx(PP, HF, HG, color=of.CURVE, alpha=0.08)
PH, PL = 0.85, 0.33
ih = int(np.argmin(np.abs(PP - PH))); il = int(np.argmin(np.abs(PP - PL)))
h1 = HG[il]; h3 = HF[ih]; h4 = h3; h2 = 1.85
ax.plot([h1, h2], [PL, PH], color=of.ACCENT, lw=2.4)              # 1-2 compresor
ax.plot([h2, h3], [PH, PH], color=of.BROWN, lw=2.4)              # 2-3 condensador
ax.plot([h4, h4], [PH, PL], color=of.CURVE, lw=2.4)             # 3-4 válvula (h=cte)
ax.plot([h4, h1], [PL, PL], color='#6a8858', lw=2.4)           # 4-1 evaporador
mark(ax, [(h1, PL), (h2, PH), (h3, PH), (h4, PL)],
     [(8, -10), (8, 6), (-12, 6), (-12, -10)])
ax.annotate('compresor', ((h1 + h2) / 2, (PL + PH) / 2), color=of.ACCENT, fontsize=8.5, rotation=18)
ax.annotate('válvula', (h4 - 0.02, (PL + PH) / 2), color=of.CURVE, fontsize=8.5, ha='right')
ax.annotate('$q_L$ (evaporador)', ((h4 + h1) / 2, PL), ((h4 + h1) / 2, PL - 0.08),
            color='#6a8858', fontsize=8.5, ha='center')
ax.set_yscale('log')
of.labels(ax, x=r'entalpía  $h$', y=r'presión  $P$ (log)')
of.title(ax, r'Ciclo de compresión de vapor en $P$–$h$')
ax.set_xlim(0.0, 2.2); ax.set_ylim(0.2, 1.3); of.save(fig, 'VCR_diagrama_Ph')

# ============ Comparación de ciclos en T-s ============
fig, ax = of.new_fig(figsize=(6.2, 4.5)); of.style_axes(ax)
sA, sB = 0.15, 1.05
TL = 1.0
THb_lo, THb_hi = 1.4, 1.4 * np.exp(0.9 * 0.55)        # Brayton: T2 y T3
# Carnot: rectángulo TL .. T3 (dos isotermas + dos isentrópicas), discontinuo
TH = THb_hi
for seg in ([[sA, sB], [TH, TH]], [[sA, sB], [TL, TL]], [[sA, sA], [TL, TH]], [[sB, sB], [TL, TH]]):
    ax.plot(seg[0], seg[1], color=of.BROWN, lw=2.0, ls='--', dashes=(5, 3))
ax.text((sA + sB) / 2, TH + 0.07, 'Carnot (ideal)', color=of.BROWN, fontsize=9, ha='center')
# Brayton: 1-2 isentrópica, 2-3 isóbara PH, 3-4 isentrópica, 4-1 isóbara PL
s = np.linspace(0, 0.9, 60)
ax.plot([sA, sA], [TL, THb_lo], color=of.CURVE, lw=2.3)
ax.plot(sA + s, THb_lo * np.exp(s * 0.55), color=of.CURVE, lw=2.3)
ax.plot([sB, sB], [THb_hi, TL * np.exp(0.9 * 0.55)], color=of.CURVE, lw=2.3)
ax.plot(sA + s, TL * np.exp(s * 0.55), color=of.CURVE, lw=2.3)
ax.fill_between(sA + s, TL * np.exp(s * 0.55), THb_lo * np.exp(s * 0.55),
                color=of.CURVE, alpha=0.12)
ax.text(0.62, 1.28, 'Brayton', color=of.CURVE, fontsize=9.5)
ax.annotate('área $= w_{neto}$', (0.6, 1.7), color=of.TEXT, fontsize=8.5, ha='center')
of.labels(ax, x=r'entropía  $s$', y=r'temperatura  $T$')
of.title(ax, r'Comparación: Carnot vs Brayton en $T$–$s$')
ax.set_xlim(0.0, 1.25); ax.set_ylim(0.8, 2.5); of.save(fig, 'Ts_comparacion_ciclos_potencia')

print('OK ciclos')
